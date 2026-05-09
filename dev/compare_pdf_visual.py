"""
Render two PDF pages at the same DPI and generate visual comparison images.

Typical usage:
    uv pip install -r dev/requirements.txt
    .venv\\Scripts\\python dev\\compare_pdf_visual.py word.pdf main.pdf
    .venv\\Scripts\\python dev\\compare_pdf_visual.py word.pdf main.pdf --page 1 --dpi 300
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import fitz
import numpy as np
from PIL import Image, ImageChops, ImageOps


DEFAULT_DPI = 300


@dataclass(frozen=True)
class ImageInfo:
    width: int
    height: int


@dataclass(frozen=True)
class DiffMetrics:
    dpi: int
    word_pdf: str
    latex_pdf: str
    word_page: int
    latex_page: int
    word_image: ImageInfo
    latex_image: ImageInfo
    compared_image: ImageInfo
    crop_mode: str
    changed_pixels: int
    changed_percent: float
    mean_abs_diff: float
    max_abs_diff: int
    diff_bbox: tuple[int, int, int, int] | None


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def pdf_page_to_gray_image(pdf_path: Path, page_number: int, dpi: int) -> Image.Image:
    page_index = page_number - 1
    scale = dpi / 72

    with fitz.open(pdf_path) as doc:
        if page_index >= len(doc):
            raise ValueError(
                f"{pdf_path} has {len(doc)} page(s), cannot render page {page_number}"
            )

        page = doc[page_index]
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        return image.convert("L")


def align_images(
    word: Image.Image, latex: Image.Image, crop_mode: str
) -> tuple[Image.Image, Image.Image]:
    if crop_mode == "min":
        width = min(word.width, latex.width)
        height = min(word.height, latex.height)
        return word.crop((0, 0, width, height)), latex.crop((0, 0, width, height))

    if crop_mode == "pad":
        width = max(word.width, latex.width)
        height = max(word.height, latex.height)
        return pad_to_size(word, width, height), pad_to_size(latex, width, height)

    raise ValueError(f"unknown crop mode: {crop_mode}")


def pad_to_size(image: Image.Image, width: int, height: int) -> Image.Image:
    canvas = Image.new("L", (width, height), 255)
    canvas.paste(image, (0, 0))
    return canvas


def make_ink_overlay(word: Image.Image, latex: Image.Image) -> Image.Image:
    """Show Word-only ink in red, LaTeX-only ink in blue, overlap in dark purple."""
    word_ink = np.asarray(ImageOps.invert(word), dtype=np.uint8)
    latex_ink = np.asarray(ImageOps.invert(latex), dtype=np.uint8)

    height, width = word_ink.shape
    overlay = np.full((height, width, 3), 255, dtype=np.uint8)
    overlay[:, :, 0] = 255 - latex_ink
    overlay[:, :, 1] = 255 - np.maximum(word_ink, latex_ink)
    overlay[:, :, 2] = 255 - word_ink
    return Image.fromarray(overlay, mode="RGB")


def make_highlight(word: Image.Image, latex: Image.Image, threshold: int) -> Image.Image:
    diff = ImageChops.difference(word, latex)
    diff_np = np.asarray(diff, dtype=np.uint8)
    base = np.asarray(Image.blend(word, latex, 0.5), dtype=np.uint8)

    highlight = np.repeat(base[:, :, None], 3, axis=2)
    mask = diff_np > threshold
    highlight[mask] = np.array([255, 32, 32], dtype=np.uint8)
    return Image.fromarray(highlight, mode="RGB")


def collect_metrics(
    *,
    word_pdf: Path,
    latex_pdf: Path,
    word_page: int,
    latex_page: int,
    dpi: int,
    crop_mode: str,
    original_word: Image.Image,
    original_latex: Image.Image,
    word: Image.Image,
    latex: Image.Image,
    diff: Image.Image,
    threshold: int,
) -> DiffMetrics:
    diff_np = np.asarray(diff, dtype=np.uint8)
    changed_mask = diff_np > threshold
    changed_pixels = int(changed_mask.sum())
    total_pixels = diff_np.size
    ys, xs = np.where(changed_mask)
    bbox = None
    if changed_pixels:
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)

    return DiffMetrics(
        dpi=dpi,
        word_pdf=str(word_pdf),
        latex_pdf=str(latex_pdf),
        word_page=word_page,
        latex_page=latex_page,
        word_image=ImageInfo(original_word.width, original_word.height),
        latex_image=ImageInfo(original_latex.width, original_latex.height),
        compared_image=ImageInfo(word.width, word.height),
        crop_mode=crop_mode,
        changed_pixels=changed_pixels,
        changed_percent=(changed_pixels / total_pixels) * 100,
        mean_abs_diff=float(diff_np.mean()),
        max_abs_diff=int(diff_np.max()),
        diff_bbox=bbox,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate pixel diff and red/blue overlay images for two PDF pages."
    )
    parser.add_argument("word_pdf", type=Path, help="Word-exported reference PDF")
    parser.add_argument("latex_pdf", type=Path, help="LaTeX-generated PDF")
    parser.add_argument(
        "--page",
        type=positive_int,
        default=1,
        help="1-based page number to compare for both PDFs, default: 1",
    )
    parser.add_argument(
        "--word-page",
        type=positive_int,
        help="1-based page number for the Word PDF; overrides --page",
    )
    parser.add_argument(
        "--latex-page",
        type=positive_int,
        help="1-based page number for the LaTeX PDF; overrides --page",
    )
    parser.add_argument(
        "--dpi",
        type=positive_int,
        default=DEFAULT_DPI,
        help=f"rendering DPI, default: {DEFAULT_DPI}",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("dev/pdf-diff"),
        help="directory for generated images, default: dev/pdf-diff",
    )
    parser.add_argument(
        "--prefix",
        default="compare",
        help="output filename prefix, default: compare",
    )
    parser.add_argument(
        "--crop-mode",
        choices=("min", "pad"),
        default="min",
        help="align different page sizes by cropping to min size or padding to max size",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=0,
        choices=range(0, 256),
        metavar="0-255",
        help="ignore per-pixel grayscale differences at or below this value",
    )
    parser.add_argument(
        "--save-rendered",
        action="store_true",
        help="also save the rendered grayscale pages",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    word_pdf = args.word_pdf.resolve()
    latex_pdf = args.latex_pdf.resolve()
    word_page = args.word_page or args.page
    latex_page = args.latex_page or args.page

    if not word_pdf.exists():
        raise FileNotFoundError(f"Word PDF does not exist: {word_pdf}")
    if not latex_pdf.exists():
        raise FileNotFoundError(f"LaTeX PDF does not exist: {latex_pdf}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    original_word = pdf_page_to_gray_image(word_pdf, word_page, args.dpi)
    original_latex = pdf_page_to_gray_image(latex_pdf, latex_page, args.dpi)
    word, latex = align_images(original_word, original_latex, args.crop_mode)

    diff = ImageChops.difference(word, latex)
    diff_enhanced = ImageOps.autocontrast(diff)
    overlay = make_ink_overlay(word, latex)
    highlight = make_highlight(word, latex, args.threshold)

    diff_path = args.output_dir / f"{args.prefix}_diff.png"
    enhanced_path = args.output_dir / f"{args.prefix}_diff_enhanced.png"
    overlay_path = args.output_dir / f"{args.prefix}_overlay_word_red_latex_blue.png"
    highlight_path = args.output_dir / f"{args.prefix}_highlight.png"
    metrics_path = args.output_dir / f"{args.prefix}_metrics.json"

    diff.save(diff_path)
    diff_enhanced.save(enhanced_path)
    overlay.save(overlay_path)
    highlight.save(highlight_path)

    if args.save_rendered:
        word.save(args.output_dir / f"{args.prefix}_word_page.png")
        latex.save(args.output_dir / f"{args.prefix}_latex_page.png")

    metrics = collect_metrics(
        word_pdf=word_pdf,
        latex_pdf=latex_pdf,
        word_page=word_page,
        latex_page=latex_page,
        dpi=args.dpi,
        crop_mode=args.crop_mode,
        original_word=original_word,
        original_latex=original_latex,
        word=word,
        latex=latex,
        diff=diff,
        threshold=args.threshold,
    )
    metrics_path.write_text(
        json.dumps(asdict(metrics), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Generated: {diff_path}")
    print(f"Generated: {enhanced_path}")
    print(f"Generated: {overlay_path}")
    print(f"Generated: {highlight_path}")
    print(f"Generated: {metrics_path}")
    print(
        "Changed pixels: "
        f"{metrics.changed_pixels} ({metrics.changed_percent:.4f}%), "
        f"mean abs diff: {metrics.mean_abs_diff:.4f}, max abs diff: {metrics.max_abs_diff}"
    )


if __name__ == "__main__":
    main()
