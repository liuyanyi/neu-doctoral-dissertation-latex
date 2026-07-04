"""
Create a temporary LaTeX entry file with professional-degree disabled.

The repository's sample main.tex is used for the professional-degree path.
This helper keeps the CI comparison matrix able to render the academic title
page without asking contributors to edit main.tex by hand.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("main.tex"),
        help="source TeX entry, default: main.tex",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tmp/ci-academic/main-academic.tex"),
        help="temporary academic TeX entry to write",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.source.resolve()
    output = args.output

    text = source.read_text(encoding="utf-8")
    text, changed = disable_professional_degree(text)
    if not changed:
        raise ValueError(f"cannot find professional-degree setting in {source}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(f"Generated {output}")


def disable_professional_degree(text: str) -> tuple[str, bool]:
    documentclass_pattern = re.compile(
        r"\\documentclass\s*\[(?P<options>.*?)\]\s*\{neudissertation\}",
        re.DOTALL,
    )

    def replace_documentclass(match: re.Match[str]) -> str:
        options = match.group("options")
        new_options, changed = remove_professional_degree_option(options)
        if not changed:
            return match.group(0)
        if new_options.strip():
            return f"\\documentclass[{new_options}]{{neudissertation}}"
        return "\\documentclass{neudissertation}"

    text_after_class, class_count = documentclass_pattern.subn(
        replace_documentclass,
        text,
        count=1,
    )
    if class_count and text_after_class != text:
        return text_after_class, True

    return text, False


def remove_professional_degree_option(options: str) -> tuple[str, bool]:
    if "\n" in options:
        lines = options.splitlines(keepends=True)
        kept_lines = []
        changed = False
        for line in lines:
            code = line.split("%", 1)[0]
            if re.fullmatch(
                r"\s*,?\s*professional-degree\s*,?\s*",
                code,
            ):
                changed = True
                continue
            kept_lines.append(line)
        return "".join(kept_lines), changed

    option_items = [item.strip() for item in options.split(",")]
    kept_options = [
        item
        for item in option_items
        if item and item.strip() != "professional-degree"
    ]
    changed = len(kept_options) != len([item for item in option_items if item])
    return ", ".join(kept_options), changed


if __name__ == "__main__":
    main()
