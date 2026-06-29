"""
Run configured PDF visual comparisons and optionally check/update baselines.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG = Path("dev/pdf_compare_cases.json")
DEFAULT_OUTPUT_DIR = Path("tmp/pdf-compare")
DEFAULT_BASELINE_DIR = Path("template_reference/compare_result/baseline")
BASELINE_METRICS_FILENAME = "diff_metrics.json"
DEFAULT_CHANGED_PERCENT_TOLERANCE = 0.05
DEFAULT_MEAN_ABS_DIFF_TOLERANCE = 0.1


@dataclass(frozen=True)
class CompareCase:
    id: str
    label: str
    reference_pdf: Path
    reference_page: int
    latex_pdf: Path
    latex_page: int
    dpi: int
    threshold: int
    crop_mode: str


@dataclass(frozen=True)
class MetricCheck:
    metric_name: str
    actual: float
    expected: float | None
    tolerance: float | None
    delta: float | None
    passed: bool | None


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def load_cases(config_path: Path) -> list[CompareCase]:
    data = json.loads(config_path.read_text(encoding="utf-8"))
    defaults: dict[str, Any] = data.get("defaults", {})
    cases = []
    for item in data["cases"]:
        cases.append(
            CompareCase(
                id=item["id"],
                label=item.get("label", item["id"]),
                reference_pdf=Path(item["reference_pdf"]),
                reference_page=int(item.get("reference_page", 1)),
                latex_pdf=Path(item["latex_pdf"]),
                latex_page=int(item["latex_page"]),
                dpi=int(item.get("dpi", defaults.get("dpi", 300))),
                threshold=int(item.get("threshold", defaults.get("threshold", 0))),
                crop_mode=str(item.get("crop_mode", defaults.get("crop_mode", "min"))),
            )
        )
    return cases


def run_compare(case: CompareCase, output_dir: Path) -> dict[str, Any]:
    command = [
        sys.executable,
        "dev/compare_pdf_visual.py",
        str(case.reference_pdf),
        str(case.latex_pdf),
        "--word-page",
        str(case.reference_page),
        "--latex-page",
        str(case.latex_page),
        "--dpi",
        str(case.dpi),
        "--threshold",
        str(case.threshold),
        "--crop-mode",
        case.crop_mode,
        "--output-dir",
        str(output_dir),
        "--prefix",
        case.id,
        "--save-rendered",
    ]
    subprocess.run(command, check=True)

    metrics_path = output_dir / f"{case.id}_metrics.json"
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    return metrics


def baseline_files(case_id: str) -> list[str]:
    return [
        f"{case_id}_overlay_word_red_latex_blue.png",
    ]


def update_baseline(case: CompareCase, output_dir: Path, baseline_dir: Path) -> None:
    baseline_dir.mkdir(parents=True, exist_ok=True)
    for filename in baseline_files(case.id):
        shutil.copy2(output_dir / filename, baseline_dir / filename)


def check_metric(
    *,
    case_id: str,
    metric_name: str,
    actual: float,
    expected: float,
    tolerance: float,
) -> str | None:
    delta = abs(actual - expected)
    if delta <= tolerance:
        return None

    return (
        f"{case_id}: {metric_name} changed from {expected:.6f} to "
        f"{actual:.6f} (delta {delta:.6f}, tolerance {tolerance:.6f})"
    )


def check_baseline_metrics(
    *,
    baseline_dir: Path,
    metrics_by_case: dict[str, dict[str, Any]],
    changed_percent_tolerance: float,
    mean_abs_diff_tolerance: float,
) -> list[str]:
    baseline_path = baseline_dir / BASELINE_METRICS_FILENAME
    if not baseline_path.exists():
        return [f"missing baseline metrics: {baseline_path}"]

    baseline_metrics = json.loads(baseline_path.read_text(encoding="utf-8"))
    failures = []

    for case_id, actual_metrics in metrics_by_case.items():
        expected_metrics = baseline_metrics.get(case_id)
        if expected_metrics is None:
            failures.append(f"{case_id}: missing baseline metrics")
            continue

        checks = [
            (
                "changed_percent",
                float(actual_metrics["changed_percent"]),
                float(expected_metrics["changed_percent"]),
                changed_percent_tolerance,
            ),
            (
                "mean_abs_diff",
                float(actual_metrics["mean_abs_diff"]),
                float(expected_metrics["mean_abs_diff"]),
                mean_abs_diff_tolerance,
            ),
        ]
        for metric_name, actual, expected, tolerance in checks:
            failure = check_metric(
                case_id=case_id,
                metric_name=metric_name,
                actual=actual,
                expected=expected,
                tolerance=tolerance,
            )
            if failure:
                failures.append(failure)

    return failures


def load_baseline_metrics(baseline_dir: Path) -> dict[str, Any]:
    baseline_path = baseline_dir / BASELINE_METRICS_FILENAME
    if not baseline_path.exists():
        return {}
    return json.loads(baseline_path.read_text(encoding="utf-8"))


def build_metric_checks(
    *,
    metrics_by_case: dict[str, dict[str, Any]],
    baseline_metrics: dict[str, Any],
    changed_percent_tolerance: float,
    mean_abs_diff_tolerance: float,
) -> dict[str, list[MetricCheck]]:
    checks_by_case = {}
    for case_id, actual_metrics in metrics_by_case.items():
        expected_metrics = baseline_metrics.get(case_id, {})
        specs = [
            (
                "changed_percent",
                float(actual_metrics["changed_percent"]),
                expected_metrics.get("changed_percent"),
                changed_percent_tolerance,
            ),
            (
                "mean_abs_diff",
                float(actual_metrics["mean_abs_diff"]),
                expected_metrics.get("mean_abs_diff"),
                mean_abs_diff_tolerance,
            ),
        ]

        checks = []
        for metric_name, actual, expected_raw, tolerance in specs:
            if expected_raw is None:
                checks.append(
                    MetricCheck(
                        metric_name=metric_name,
                        actual=actual,
                        expected=None,
                        tolerance=tolerance,
                        delta=None,
                        passed=None,
                    )
                )
                continue

            expected = float(expected_raw)
            delta = actual - expected
            checks.append(
                MetricCheck(
                    metric_name=metric_name,
                    actual=actual,
                    expected=expected,
                    tolerance=tolerance,
                    delta=delta,
                    passed=abs(delta) <= tolerance,
                )
            )

        checks_by_case[case_id] = checks

    return checks_by_case


def format_float(value: float | None, digits: int = 6) -> str:
    if value is None:
        return "-"
    return f"{value:.{digits}f}"


def format_status(checks: list[MetricCheck]) -> str:
    if any(check.passed is False for check in checks):
        return "FAIL"
    if any(check.passed is None for check in checks):
        return "N/A"
    return "PASS"


def build_markdown_summary(
    *,
    metrics_by_case: dict[str, dict[str, Any]],
    metric_checks_by_case: dict[str, list[MetricCheck]],
    failures: list[str],
) -> str:
    lines = [
        "# PDF Visual Compare Summary",
        "",
        "| Case | Status | Changed % | Baseline % | Delta % | Tolerance % | Mean diff | Baseline mean | Delta mean | Tolerance mean | Max diff |",
        "| :--- | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for case_id, metrics in metrics_by_case.items():
        checks = {
            check.metric_name: check
            for check in metric_checks_by_case.get(case_id, [])
        }
        changed_percent = checks.get("changed_percent")
        mean_abs_diff = checks.get("mean_abs_diff")
        lines.append(
            "| {case_id} | {status} | {changed_percent} | {baseline_percent} | "
            "{delta_percent} | {tolerance_percent} | {mean_diff} | "
            "{baseline_mean} | {delta_mean} | {tolerance_mean} | {max_abs_diff} |".format(
                case_id=case_id,
                status=format_status(list(checks.values())),
                changed_percent=format_float(metrics["changed_percent"], 4),
                baseline_percent=format_float(
                    changed_percent.expected if changed_percent else None, 4
                ),
                delta_percent=format_float(
                    changed_percent.delta if changed_percent else None, 4
                ),
                tolerance_percent=format_float(
                    changed_percent.tolerance if changed_percent else None, 4
                ),
                mean_diff=format_float(metrics["mean_abs_diff"], 4),
                baseline_mean=format_float(
                    mean_abs_diff.expected if mean_abs_diff else None, 4
                ),
                delta_mean=format_float(
                    mean_abs_diff.delta if mean_abs_diff else None, 4
                ),
                tolerance_mean=format_float(
                    mean_abs_diff.tolerance if mean_abs_diff else None, 4
                ),
                max_abs_diff=metrics["max_abs_diff"],
            )
        )

    if failures:
        lines.extend(["", "## Baseline Check Failures", ""])
        lines.extend(f"- {failure}" for failure in failures)

    return "\n".join(lines) + "\n"


def write_summary(
    *,
    output_dir: Path,
    metrics_by_case: dict[str, dict[str, Any]],
    metric_checks_by_case: dict[str, list[MetricCheck]],
    failures: list[str],
) -> None:
    summary = build_markdown_summary(
        metrics_by_case=metrics_by_case,
        metric_checks_by_case=metric_checks_by_case,
        failures=failures,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "summary.md").write_text(summary, encoding="utf-8")
    (output_dir / "summary.json").write_text(
        json.dumps(metrics_by_case, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(summary)

    github_step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_step_summary:
        with Path(github_step_summary).open("a", encoding="utf-8") as summary_file:
            summary_file.write(summary)


def write_baseline_metrics(
    baseline_dir: Path, metrics_by_case: dict[str, dict[str, Any]]
) -> None:
    baseline_metrics = {}
    for case_id, metrics in metrics_by_case.items():
        baseline_metrics[case_id] = {
            "dpi": metrics["dpi"],
            "word_page": metrics["word_page"],
            "latex_page": metrics["latex_page"],
            "word_image": metrics["word_image"],
            "latex_image": metrics["latex_image"],
            "compared_image": metrics["compared_image"],
            "crop_mode": metrics["crop_mode"],
            "changed_pixels": metrics["changed_pixels"],
            "changed_percent": metrics["changed_percent"],
            "mean_abs_diff": metrics["mean_abs_diff"],
            "max_abs_diff": metrics["max_abs_diff"],
            "diff_bbox": metrics["diff_bbox"],
        }

    baseline_dir.mkdir(parents=True, exist_ok=True)
    (baseline_dir / BASELINE_METRICS_FILENAME).write_text(
        json.dumps(baseline_metrics, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--baseline-dir", type=Path, default=DEFAULT_BASELINE_DIR)
    parser.add_argument(
        "--case",
        dest="case_ids",
        action="append",
        help="run only the selected case id; can be passed more than once",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="copy generated comparison artifacts into the baseline directory",
    )
    parser.add_argument(
        "--check-baseline",
        action="store_true",
        help="fail when generated metrics exceed the committed baseline window",
    )
    parser.add_argument(
        "--changed-percent-tolerance",
        type=float,
        default=DEFAULT_CHANGED_PERCENT_TOLERANCE,
        help=(
            "allowed absolute changed_percent drift, default: "
            f"{DEFAULT_CHANGED_PERCENT_TOLERANCE}"
        ),
    )
    parser.add_argument(
        "--mean-abs-diff-tolerance",
        type=float,
        default=DEFAULT_MEAN_ABS_DIFF_TOLERANCE,
        help=(
            "allowed absolute mean_abs_diff drift, default: "
            f"{DEFAULT_MEAN_ABS_DIFF_TOLERANCE}"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected = set(args.case_ids or [])
    cases = [
        case
        for case in load_cases(args.config)
        if not selected or case.id in selected
    ]

    if selected and {case.id for case in cases} != selected:
        missing = sorted(selected - {case.id for case in cases})
        raise ValueError(f"unknown case id(s): {', '.join(missing)}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    metrics_by_case = {}
    failures: list[str] = []

    for case in cases:
        print(f"Comparing {case.id}: {case.label}")
        metrics_by_case[case.id] = run_compare(case, args.output_dir)
        if args.update_baseline:
            update_baseline(case, args.output_dir, args.baseline_dir)

    if args.check_baseline:
        failures.extend(
            check_baseline_metrics(
                baseline_dir=args.baseline_dir,
                metrics_by_case=metrics_by_case,
                changed_percent_tolerance=args.changed_percent_tolerance,
                mean_abs_diff_tolerance=args.mean_abs_diff_tolerance,
            )
        )

    baseline_metrics = load_baseline_metrics(args.baseline_dir)
    metric_checks_by_case = build_metric_checks(
        metrics_by_case=metrics_by_case,
        baseline_metrics=baseline_metrics,
        changed_percent_tolerance=args.changed_percent_tolerance,
        mean_abs_diff_tolerance=args.mean_abs_diff_tolerance,
    )

    write_summary(
        output_dir=args.output_dir,
        metrics_by_case=metrics_by_case,
        metric_checks_by_case=metric_checks_by_case,
        failures=failures,
    )

    if args.update_baseline:
        write_baseline_metrics(args.baseline_dir, metrics_by_case)

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
