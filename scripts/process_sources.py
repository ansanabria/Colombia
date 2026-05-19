from __future__ import annotations

import re
import shutil
from pathlib import Path

import pdfplumber
import pypdfium2 as pdfium
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
TRANS = ROOT / "fuentes-transcritas"
IMG = ROOT / "fuentes-imagenes"
COMIC = ROOT / "comic-paginas"
LEGACY = ROOT / "legacy"


def ensure_dirs() -> None:
    for path in [TRANS, IMG, COMIC, LEGACY, ROOT / "scripts"]:
        path.mkdir(parents=True, exist_ok=True)


def clean_text(text: str) -> str:
    lines = []
    for line in text.splitlines():
        line = line.rstrip()
        if re.match(r"^Paisajes del despojo cotidiano:.*https://", line):
            continue
        if re.match(r"^\d+ of \d+ ", line):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def extract_pdf_text(pdf_name: str, title: str, output_name: str) -> None:
    source = ROOT / pdf_name
    out = TRANS / output_name
    parts = [f"# {title}", "", f"Fuente original: `legacy/{pdf_name}`", ""]
    with pdfplumber.open(source) as pdf:
        parts.append(f"Páginas: {len(pdf.pages)}")
        parts.append("")
        for idx, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text = clean_text(text)
            if not text:
                continue
            parts.append(f"## Página {idx}")
            parts.append("")
            parts.append(text)
            parts.append("")
    out.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")


def render_pdf_pages(pdf_name: str, out_dir: Path, title: str) -> None:
    source = ROOT / pdf_name
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(source))
    index = [f"# {title}", "", f"Fuente original: `legacy/{pdf_name}`", ""]
    for i, page in enumerate(pdf, start=1):
        bitmap = page.render(scale=2).to_pil()
        filename = f"pagina-{i:02d}.png"
        bitmap.save(out_dir / filename)
        index.append(f"## Página {i}")
        index.append("")
        index.append(f"![Página {i}]({out_dir.relative_to(ROOT) / filename})")
        index.append("")
    (TRANS / f"{Path(pdf_name).stem}-imagenes.md").write_text(
        "\n".join(index).strip() + "\n", encoding="utf-8"
    )


def crop_whitespace(image: Image.Image, border: int = 18) -> Image.Image:
    rgb = image.convert("RGB")
    bg = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg).convert("L")
    mask = diff.point(lambda p: 255 if p > 18 else 0)
    bbox = mask.getbbox()
    if not bbox:
        return rgb
    left, top, right, bottom = bbox
    left = max(0, left - border)
    top = max(0, top - border)
    right = min(rgb.width, right + border)
    bottom = min(rgb.height, bottom + border)
    return rgb.crop((left, top, right, bottom))


def render_cropped_comic(pdf_name: str) -> None:
    source = ROOT / pdf_name
    pdf = pdfium.PdfDocument(str(source))
    index = ["# Cómic recortado: Caminos Condenados", "", f"Fuente original: `legacy/{pdf_name}`", ""]
    for i, page in enumerate(pdf, start=1):
        image = page.render(scale=2).to_pil()
        cropped = crop_whitespace(image)
        filename = f"caminos-condenados-{i:02d}.png"
        cropped.save(COMIC / filename, optimize=True)
        index.append(f"## Página {i}")
        index.append("")
        index.append(f"![Caminos Condenados página {i}](../comic-paginas/{filename})")
        index.append("")
    (TRANS / "primaria-2-comic.md").write_text("\n".join(index).strip() + "\n", encoding="utf-8")


def move_legacy_pdfs() -> None:
    for pdf_name in ["primaria-1.pdf", "contexto-1.pdf", "primaria-2.pdf", "contexto-2.pdf", "contexto-3.pdf"]:
        src = ROOT / pdf_name
        dst = LEGACY / pdf_name
        if src.exists() and not dst.exists():
            shutil.move(str(src), str(dst))


def main() -> None:
    ensure_dirs()
    extract_pdf_text(
        "contexto-2.pdf",
        "Paisajes del despojo cotidiano: acaparamiento de tierra y agua en Montes de María, Colombia",
        "contexto-2-paisajes-del-despojo-cotidiano.md",
    )
    extract_pdf_text(
        "contexto-3.pdf",
        "La política del canto y el poder de las alabaoras de Pogue (Bojayá, Chocó)",
        "contexto-3-alabaoras-de-pogue.md",
    )
    render_pdf_pages("primaria-1.pdf", IMG / "primaria-1-las-delicias", "Primaria 1: Un ataque en Las Delicias")
    render_pdf_pages("contexto-1.pdf", IMG / "contexto-1-conscripcion", "Contexto 1: Conscripción y democracia")
    render_cropped_comic("primaria-2.pdf")
    move_legacy_pdfs()


if __name__ == "__main__":
    main()
