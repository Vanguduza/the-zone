#!/usr/bin/env python3
"""Render the assembled RC WORLD Master Development Plan to a professionally
formatted PDF.

Pipeline: assembled markdown -> pandoc (HTML5 + TOC) -> cover injection ->
WeasyPrint (A4 PDF with running headers, page numbers, TOC page references).

Run build/assemble.py first (this script will invoke it if the assembled
markdown is missing).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BUILD = Path(__file__).resolve().parent
ROOT = BUILD.parent
MASTER_MD = BUILD / "RC-WORLD-Master-Development-Plan.md"
CSS = BUILD / "pdf-style.css"
HTML_OUT = BUILD / "RC-WORLD-Master-Development-Plan.html"
PDF_OUT = BUILD / "RC-WORLD-Master-Development-Plan.pdf"

COVER = """
<div class="cover">
  <div class="rule"></div>
  <h1>RC WORLD</h1>
  <p class="subtitle">Master Development Plan</p>
  <p class="tagline">Investor Prospectus &bull; Operations Manual &bull; Engineering Handbook</p>
  <p class="volumes-note">
    Fourteen volumes covering the executive master plan, market research, the four
    operating divisions (Motorsport, Construction, Aviation, Marine), the engineering
    &amp; workshop manual, the China procurement handbook, customer experience &amp;
    loyalty, finance, architecture &amp; park design, the franchise manual, the
    RC&nbsp;WORLD&nbsp;OS technology platform &mdash; and the self-funded
    <strong style="color:#e8a13d">$10,000 / 300&nbsp;m&sup2; Bootstrap Launch Plan</strong>
    that starts the journey.
  </p>
  <p class="edition">Revision 1.0 &mdash; July 2026 &nbsp;&nbsp;|&nbsp;&nbsp;
    Living master document &mdash; volumes are revised independently; the canon of
    record is <span style="font-family: 'DejaVu Sans Mono', monospace;">style-guide.md</span>.
  </p>
</div>
"""


def main() -> int:
    if not MASTER_MD.exists():
        print("Assembled markdown missing; running assemble.py ...")
        subprocess.run([sys.executable, str(BUILD / "assemble.py")], check=True)

    print("pandoc: markdown -> HTML5 (with TOC) ...")
    subprocess.run(
        [
            "pandoc", str(MASTER_MD),
            "-f", "markdown+pipe_tables+task_lists",
            "-t", "html5", "--standalone",
            "--toc", "--toc-depth=2",
            "--metadata", "title=RC WORLD — Master Development Plan",
            "--metadata", "lang=en",
            "-c", CSS.name,
            "-o", str(HTML_OUT),
        ],
        check=True,
    )

    html = HTML_OUT.read_text(encoding="utf-8")
    body_tag = "<body>"
    idx = html.index(body_tag) + len(body_tag)
    html = html[:idx] + COVER + html[idx:]
    HTML_OUT.write_text(html, encoding="utf-8")

    print("weasyprint: HTML -> PDF (large document; this takes several minutes) ...")
    from weasyprint import HTML  # imported late so pandoc errors surface first

    HTML(filename=str(HTML_OUT), base_url=str(BUILD)).write_pdf(str(PDF_OUT))
    size_mb = PDF_OUT.stat().st_size / 1e6
    print(f"Wrote {PDF_OUT.relative_to(ROOT)} ({size_mb:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
