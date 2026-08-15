from pathlib import Path
import sys

from PIL import Image, ImageOps


def fit_exact(image: Image.Image, width: int, height: int) -> Image.Image:
    target_ratio = width / height
    source_ratio = image.width / image.height
    if abs(source_ratio - target_ratio) > 1e-9:
        if source_ratio > target_ratio:
            crop_width = round(image.height * target_ratio)
            left = (image.width - crop_width) // 2
            image = image.crop((left, 0, left + crop_width, image.height))
        else:
            crop_height = round(image.width / target_ratio)
            top = (image.height - crop_height) // 2
            image = image.crop((0, top, image.width, top + crop_height))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit("usage: compose_food_comparison.py ORIGINAL GENERATED PROCESSED_OUT COMPARISON_OUT")

    original_path, generated_path, processed_path, comparison_path = map(Path, sys.argv[1:])
    # Normalize EXIF orientation before reading dimensions. Phone photos may be
    # stored landscape while carrying a portrait orientation tag.
    original = ImageOps.exif_transpose(Image.open(original_path)).convert("RGB")
    generated = ImageOps.exif_transpose(Image.open(generated_path)).convert("RGB")
    processed = fit_exact(generated, original.width, original.height)

    processed_path.parent.mkdir(parents=True, exist_ok=True)
    processed.save(processed_path, format="PNG", optimize=True)

    divider = max(24, round(original.height * 0.01))
    comparison = Image.new("RGB", (original.width, original.height * 2 + divider), (245, 240, 230))
    comparison.paste(original, (0, 0))
    comparison.paste(processed, (0, original.height + divider))
    comparison.save(comparison_path, format="JPEG", quality=94, subsampling=0, optimize=True)

    print(f"processed={processed_path} {processed.width}x{processed.height}")
    print(f"comparison={comparison_path} {comparison.width}x{comparison.height}")


if __name__ == "__main__":
    main()
