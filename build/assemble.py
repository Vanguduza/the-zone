#!/usr/bin/env python3
"""Assemble the RC WORLD Master Development Plan from its volume files.

Concatenates volumes in order into a single markdown master document, reports
word counts and estimated page counts per volume, and renders DOCX/PDF via
pandoc when available.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOLUMES_DIR = ROOT / "volumes"
OUT_DIR = ROOT / "build"
OUT_MD = OUT_DIR / "RC-WORLD-Master-Development-Plan.md"

VOLUME_ORDER = [
    "volume-00-front-matter.md",
    "volume-01-executive-master-plan.md",
    "volume-02-market-research.md",
    "volume-03-motorsport-division.md",
    "volume-04-construction-division.md",
    "volume-05-aviation-division.md",
    "volume-06-marine-division.md",
    "volume-07-engineering-workshop-manual.md",
    "volume-08-procurement-handbook.md",
    "volume-09-customer-experience.md",
    "volume-10-finance.md",
    "volume-11-architecture-park-design.md",
    "volume-12-franchise-manual.md",
]

WORDS_PER_PAGE = 400.0


def count_words(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return len(re.findall(r"\S+", text))


def main() -> int:
    parts: list[str] = []
    total_words = 0
    print(f"{'Volume':52s} {'Words':>8s} {'~Pages':>7s}")
    print("-" * 70)
    missing = []
    for name in VOLUME_ORDER:
        path = VOLUMES_DIR / name
        if not path.exists():
            missing.append(name)
            print(f"{name:52s} {'MISSING':>8s}")
            continue
        text = path.read_text(encoding="utf-8")
        words = count_words(text)
        total_words += words
        print(f"{name:52s} {words:8d} {words / WORDS_PER_PAGE:7.0f}")
        parts.append(text.strip() + "\n")

    print("-" * 70)
    print(f"{'TOTAL':52s} {total_words:8d} {total_words / WORDS_PER_PAGE:7.0f}")

    OUT_DIR.mkdir(exist_ok=True)
    OUT_MD.write_text("\n\n---\n\n\\newpage\n\n".join(parts), encoding="utf-8")
    print(f"\nWrote {OUT_MD.relative_to(ROOT)}")

    if shutil.which("pandoc"):
        docx = OUT_DIR / "RC-WORLD-Master-Development-Plan.docx"
        subprocess.run(
            ["pandoc", str(OUT_MD), "-o", str(docx), "--toc", "--toc-depth=2",
             "-f", "markdown", "--metadata", "title=RC WORLD — Master Development Plan"],
            check=False,
        )
        print(f"Wrote {docx.relative_to(ROOT)}")
        for engine in ("xelatex", "pdflatex", "wkhtmltopdf", "weasyprint"):
            if shutil.which(engine):
                pdf = OUT_DIR / "RC-WORLD-Master-Development-Plan.pdf"
                subprocess.run(
                    ["pandoc", str(OUT_MD), "-o", str(pdf), "--toc", "--toc-depth=2",
                     f"--pdf-engine={engine}",
                     "-V", "geometry:margin=2.2cm", "-V", "fontsize=11pt",
                     "--metadata", "title=RC WORLD — Master Development Plan"],
                    check=False,
                )
                if pdf.exists():
                    print(f"Wrote {pdf.relative_to(ROOT)} (engine: {engine})")
                break
    else:
        print("pandoc not found — skipping DOCX/PDF render.")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
