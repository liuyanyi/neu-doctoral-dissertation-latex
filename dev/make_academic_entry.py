"""
Create a temporary LaTeX entry file with professional-degree disabled.

The repository's sample main.tex is used for the professional-degree path.
This helper keeps the CI comparison matrix able to render the academic title
page without asking contributors to edit main.tex by hand.
"""

from __future__ import annotations

import argparse
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
    old = "professional-degree = true"
    new = "professional-degree = false"
    if old not in text:
        raise ValueError(f"cannot find expected setting in {source}: {old}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"Generated {output}")


if __name__ == "__main__":
    main()
