# -*- coding: utf-8 -*-
"""check_rendering.py — QNFO.RES.024 rendering gates (2026-08-26).

Checks (research skill Phase 5 gates):
  CURRENCY-DOLLAR-ESCAPE-1  — odd unescaped $ per line; leftover $ + digit after math-pair stripping
  PANDOC-SAFE / UNICODE-MATH-1 — banned Unicode math glyphs in source (ord-range based)
  PANDOC-PIPE-TABLE-1       — bare | inside pipe-table cells
  FRONTMATTER-DUPLICATION-1 — body byline/H1/abstract duplication (HTML-level)
  TITLE-DUPLICATION-1       — exactly one h1.title, zero body h1 (HTML-level)
  FFFD                      — U+FFFD in rendered HTML text
Exit 0 iff all pass.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
MD = os.path.join(ROOT, "post-positional-numeracy.md")
HTML = os.path.join(ROOT, "post-positional-numeracy.html")

fails = []

def check(name, ok, detail):
    if not ok:
        fails.append((name, detail))
    print(("PASS" if ok else "FAIL"), name, "-", detail)

def is_banned(ch):
    o = ord(ch)
    # arrows, math operators, ceiling/floor, middle-dot, times, divide,
    # unicode super/subscripts, double-struck letters, mathematical alphanumerics
    return (0x2190 <= o <= 0x21FF) or (0x2200 <= o <= 0x22FF) \
        or (0x2308 <= o <= 0x230B) or (o == 0x00B7) or (o == 0x00D7) or (o == 0x00F7) \
        or (0x2070 <= o <= 0x209C) or (o in (0x2115, 0x211A, 0x211D, 0x2124, 0x2148)) \
        or (o >= 0x1D400)

src = io.open(MD, encoding="utf-8").read()
lines = src.splitlines()

# 1. odd-$ per line
odd = [(i + 1, ln.count("$")) for i, ln in enumerate(lines) if ln.count("$") % 2 == 1]
check("ODD-DOLLAR-LINES", not odd, "odd-$ lines: %s" % odd[:5])

# 2. currency: after removing complete $...$ pairs, any leftover $+digit is an unescaped currency dollar
cur = []
for i, ln in enumerate(lines, 1):
    stripped = re.sub(r"\$[^$]*\$", "", ln)
    if re.search(r"\$\d", stripped):
        cur.append((i, ln[:70]))
check("CURRENCY-UNESCAPED", not cur, "leftover $+digit after math-pair stripping: %s" % cur[:5])

# 3. banned Unicode math glyphs (ord-range based)
hits = []
for i, ln in enumerate(lines, 1):
    for ch in ln:
        if is_banned(ch):
            hits.append((i, hex(ord(ch)), ln[:60]))
            break
check("UNICODE-MATH-GLYPHS", not hits, "banned glyphs: %s" % hits[:5])

# 4. bare | inside pipe-table cells
bad_pipes = []
for i, ln in enumerate(lines, 1):
    if ln.lstrip().startswith("|") and ln.rstrip().endswith("|"):
        body = ln.strip()[1:-1]
        cells = body.split("|")
        for c in cells:
            if "|" in c:
                bad_pipes.append((i, c.strip()[:50]))
check("PIPE-TABLE-BARE-PIPE", not bad_pipes, "bare pipes in cells: %s" % bad_pipes[:5])

# 5. frontmatter duplication in source: body bylines / H1 title
title_match = re.search(r'^title:\s*"([^"]+)"', src)
title = title_match.group(1) if title_match else ""
body = src.split("---", 2)[2] if src.count("---") >= 2 else src
bylines = [ln.strip() for ln in body.splitlines() if re.match(r"\*\*(Date|Abstract|Author)\*\*", ln.strip())]
h1s = [ln.strip() for ln in body.splitlines() if ln.startswith("# ")]
check("BODY-BYLINE-DUP", not bylines, "body bylines: %s" % bylines[:3])
check("BODY-H1-DUP", not any(h == "# " + title for h in h1s), "body H1s: %s" % h1s[:3])

# 6. HTML-level checks
if os.path.exists(HTML):
    html = io.open(HTML, encoding="utf-8").read()
    n_title_h1 = len(re.findall(r'<h1[^>]*class="[^"]*title[^"]*"', html))
    n_body_h1 = len(re.findall(r"<h1", html)) - n_title_h1
    n_abstract = html.count('class="abstract"')
    check("HTML-ONE-TITLE", n_title_h1 == 1, "h1.title count: %d" % n_title_h1)
    check("HTML-NO-BODY-H1", n_body_h1 == 0, "non-title h1 count: %d" % n_body_h1)
    check("HTML-ONE-ABSTRACT", n_abstract == 1, "abstract divs: %d" % n_abstract)
    check("HTML-NO-FFFD", "\ufffd" not in html, "U+FFFD in HTML: %s" % ("\ufffd" in html))
    print("INFO  - rendered reference entries:", html.count('class="csl-entry"'))
else:
    check("HTML-EXISTS", False, "HTML not built yet — run pandoc first")

print()
if fails:
    print("FAILURES:", len(fails))
    for n, d in fails:
        print("  -", n, d)
    sys.exit(1)
print("ALL RENDERING GATES PASS")
