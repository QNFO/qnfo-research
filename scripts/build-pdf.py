#!/usr/bin/env python3
"""Permanent PDF build pipeline — QNFO research papers (RES.023 canonical).

Protocol (research skill v2.134 gates + user directives 2026-08-24):
  1. Math MUST render as typeset mathematics (MathJax -> SVG), never plain text.
  2. NO visible formatting header/footer (display_header_footer=False —
     Chromium's default title/URL header must never appear).
  3. A4 explicit size (the CSS @page keyword is ignored by Chromium —
     EDGE-PDF-PAGE-KEYWORD-1) with 2 cm margins all around (user mandate).
  4. Verification gates (pypdf): MediaBox A4 595.28x841.89pt on every page;
     0 U+FFFD in raw bytes and text layer; math-render sanity (the
     plain-text math forms from the source MUST NOT appear in the PDF text
     layer); no-header check (page 1 text layer must not contain the
     Chromium default header content).
  5. The pipeline is COMMITTED and reproducible from the repo root.

Usage: python scripts/build-pdf.py <paper.md> <style.css>
Requires: pandoc, playwright (chromium), pypdf, network for MathJax CDN.
"""
import pathlib
import subprocess
import sys
import tempfile

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("playwright not installed")

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("pypdf not installed")

MATHJAX = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"


def build_pdf(md_path: pathlib.Path, css_path: pathlib.Path,
              out_pdf: pathlib.Path) -> dict:
    md_path = pathlib.Path(md_path).resolve()
    css_path = pathlib.Path(css_path).resolve()
    out_pdf = pathlib.Path(out_pdf).resolve()
    tmp = pathlib.Path(tempfile.gettempdir()) / f"buildpdf-{md_path.stem}"
    tmp.mkdir(parents=True, exist_ok=True)
    html_path = tmp / (md_path.stem + ".html")

    # 1) pandoc -> HTML with MathJax (tex-svg) and the print stylesheet
    r = subprocess.run(
        ["pandoc", str(md_path), "-o", str(html_path), "--standalone",
         "--metadata", "lang=en", "-H", str(css_path),
         "--mathjax=" + MATHJAX],
        capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pandoc failed: {r.stderr[:500]}")

    # 2) Playwright: load, wait for MathJax, print A4 with 2cm margins, NO header/footer
    html_uri = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(html_uri, wait_until="networkidle")
        try:
            page.wait_for_function(
                "document.querySelectorAll('mjx-container svg').length > 0",
                timeout=30000)
        except Exception:
            pass  # fall through; verification below will catch missing math
        page.pdf(
            path=str(out_pdf),
            format="A4",
            display_header_footer=False,   # NO header/footer artifacts
            margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"},
            print_background=True,
        )
        browser.close()

    # 3) Verification gates
    reader = PdfReader(str(out_pdf))
    pages = len(reader.pages)
    media_ok = all(
        abs(float(pg.mediabox.width) - 595.28) < 2 and
        abs(float(pg.mediabox.height) - 841.89) < 2
        for pg in reader.pages)
    raw = out_pdf.read_bytes()
    fffd_raw = raw.count(b"\xef\xbf\xbd")
    text = "\n".join((pg.extract_text() or "") for pg in reader.pages)
    fffd_text = text.count("\ufffd")
    # math-render sanity: source plain-text forms must NOT appear in the
    # BODY (the References section is bibliographic text — quoted record
    # titles like "embeddable into Q_p" are exact citations, not math)
    body_text, _, _ = text.partition("References")
    plain_forms = ["sigma^2/n", "tau ~ 1/n", "1/n^2", "<= max(d(x",
                   "Q_p", "d(x, z) <= max", "tau ~ 1/n^2"]
    hits = [f for f in plain_forms if f in body_text]
    # no-header check: default Chromium header carries the title+URL
    header_leak = "http" in (reader.pages[0].extract_text() or "")[:200]

    verdict = {
        "pages": pages,
        "mediabox_a4": media_ok,
        "fffd_raw": fffd_raw,
        "fffd_text": fffd_text,
        "plain_math_remaining": hits,
        "header_leak": header_leak,
        "pass": (media_ok and fffd_raw == 0 and fffd_text == 0
                 and not hits and not header_leak),
    }
    return verdict


if __name__ == "__main__":
    md = sys.argv[1] if len(sys.argv) > 1 else "ultrametric-program.md"
    css = sys.argv[2] if len(sys.argv) > 2 else "pdf-style.css"
    out = sys.argv[3] if len(sys.argv) > 3 else "ultrametric-program.pdf"
    v = build_pdf(pathlib.Path(md), pathlib.Path(css), pathlib.Path(out))
    print(v)
    sys.exit(0 if v["pass"] else 1)
