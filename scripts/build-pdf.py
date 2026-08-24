#!/usr/bin/env python3
"""Permanent PDF build pipeline — QNFO research papers (RES.023 canonical).

Protocol (research skill v2.134 gates + user directives 2026-08-24, v2.3):
  1. Math MUST render as typeset mathematics (MathJax -> SVG), never plain text.
  2. NO visible formatting header/footer (display_header_footer=False) AND
     NO CSS-source dump: the stylesheet must be wrapped in <style> inside
     the HTML <head> (pandoc -H with a bare .css file inserts it RAW after
     the template's </style>, HTML5 moves it into <body>, and it renders as
     visible page-1 text while every rule stays inert — the v2.1/v2.2 defect).
  3. A4 explicit size (EDGE-PDF-PAGE-KEYWORD-1) with 2 cm margins all around
     (user mandate); MediaBox verified.
  4. Verification gates (pypdf) — MUST catch every prior defect:
     - MediaBox A4 595.28x841.89pt on every page
     - 0 U+FFFD in raw bytes and text layer
     - CSS-leak: page-1 text contains NO CSS markers (/*, @page,
       page-break-inside, "Protocol-compliant")
     - title-first: page-1 text begins with the paper title
     - math-render: plain-text math forms absent from the BODY text layer
       (References exempt as bibliographic)
     - no running header: "http" absent from page-1 top zone
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
CSS_MARKERS = ["/*", "@page", "page-break-inside", "Protocol-compliant",
               "font-family", "margin: 0", "box-sizing"]


def build_pdf(md_path: pathlib.Path, css_path: pathlib.Path,
              out_pdf: pathlib.Path) -> dict:
    md_path = pathlib.Path(md_path).resolve()
    css_path = pathlib.Path(css_path).resolve()
    out_pdf = pathlib.Path(out_pdf).resolve()
    tmp = pathlib.Path(tempfile.gettempdir()) / f"buildpdf-{md_path.stem}"
    tmp.mkdir(parents=True, exist_ok=True)
    html_path = tmp / (md_path.stem + ".html")

    # 0) Wrap the stylesheet in <style> so pandoc -H emits a VALID style block.
    #    (Bare CSS via -H is the known defect: raw text after </style> renders
    #    as visible page-1 content and no rule applies.)
    css_text = css_path.read_text(encoding="utf-8")
    style_include = tmp / "style-include.html"
    style_include.write_text(
        "<style>\n" + css_text + "\n</style>\n", encoding="utf-8")

    # 1) pandoc -> HTML with MathJax (tex-svg) and the <style>-wrapped sheet
    r = subprocess.run(
        ["pandoc", str(md_path), "-o", str(html_path), "--standalone",
         "--metadata", "lang=en", "-H", str(style_include),
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

    # 3) Verification gates (each one catches a previously shipped defect)
    reader = PdfReader(str(out_pdf))
    pages = len(reader.pages)
    media_ok = all(
        abs(float(pg.mediabox.width) - 595.28) < 2 and
        abs(float(pg.mediabox.height) - 841.89) < 2
        for pg in reader.pages)
    raw = out_pdf.read_bytes()
    fffd_raw = raw.count(b"\xef\xbf\xbd")
    texts = [(pg.extract_text() or "") for pg in reader.pages]
    text = "\n".join(texts)
    fffd_text = text.count("\ufffd")
    p1 = texts[0]

    # CSS-leak gate (v2.1/v2.2 defect): page-1 text must not contain CSS source
    css_leaks = [m for m in CSS_MARKERS if m in p1]
    # title-first gate: page-1 text begins with the paper title
    # (title derived from the markdown frontmatter — never hardcoded)
    md_text = md_path.read_text(encoding="utf-8")
    import re as _re
    _tm = _re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", md_text, _re.M)
    title = (_tm.group(1).strip().strip("\"'") if _tm else md_path.stem)
    # normalize whitespace: pypdf may wrap a long title across lines
    p1_norm = " ".join(p1.split())
    title_first = p1_norm.startswith(title)
    # math-render gate: plain-text math forms absent from BODY (References exempt)
    body_text, _, _ = text.partition("References")
    plain_forms = ["sigma^2/n", "tau ~ 1/n", "1/n^2", "<= max(d(x",
                   "Q_p", "d(x, z) <= max", "tau ~ 1/n^2"]
    math_hits = [f for f in plain_forms if f in body_text]
    # no running header gate
    header_leak = "http" in p1[:300]

    verdict = {
        "pages": pages,
        "mediabox_a4": media_ok,
        "fffd_raw": fffd_raw,
        "fffd_text": fffd_text,
        "css_leak_markers": css_leaks,
        "title_first": title_first,
        "plain_math_remaining": math_hits,
        "header_leak": header_leak,
        "pass": (media_ok and fffd_raw == 0 and fffd_text == 0
                 and not css_leaks and title_first
                 and not math_hits and not header_leak),
    }
    return verdict


if __name__ == "__main__":
    md = sys.argv[1] if len(sys.argv) > 1 else "ultrametric-program.md"
    css = sys.argv[2] if len(sys.argv) > 2 else "pdf-style.css"
    out = sys.argv[3] if len(sys.argv) > 3 else "ultrametric-program.pdf"
    v = build_pdf(pathlib.Path(md), pathlib.Path(css), pathlib.Path(out))
    print(v)
    sys.exit(0 if v["pass"] else 1)
