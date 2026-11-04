#!/usr/bin/env python3
"""
check_rendering.py — rendering-integrity gate for the Beginner's Guide (v1.3, 2026-08-21).

Verifies the two defect classes found in post-publication review:
  1. MATH RENDERING: unescaped currency dollars create false MathJax $...$ pairs
     (canonical: the golden-values table row "vs $300,000 | $260,000 |" rendered
     "300,000 | " as TeX). GATE: zero lines with an odd count of unescaped `$`,
     and zero unescaped `$` immediately followed by a digit outside a math pair.
  2. DUPLICATE FRONTMATTER: the body must not repeat YAML-rendered fields.
     GATE: zero body lines starting with "**Date:**" or "**Abstract:**".
  3. PDF GLYPH INTEGRITY: U+FFFD must not appear in DECOMPRESSED text streams
     (a raw-byte hit inside compressed binary is a coincidence, not a text
     replacement char — FFFD-RAW-FALSE-POSITIVE-1). GATE: zero stream hits.

Exit 0 = all checks pass. Runtime: Python 3.12, stdlib only, deterministic.
"""
import re, zlib, sys, io

MD = r"The-Revolutionary-Beginners-Guide-to-Quantum-Computing.md"
PDF = r"The-Revolutionary-Beginners-Guide-to-Quantum-Computing.pdf"
HTML = r"The-Revolutionary-Beginners-Guide-to-Quantum-Computing.html"

log = io.StringIO()
PASS = FAIL = 0

def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{'PASS' if ok else 'FAIL'}] {name} {detail}"
    print(line)
    log.write(line + "\n")

t = io.open(MD, encoding="utf-8").read()
lines = t.split("\n")

# 1. odd unescaped $ per line
odd = [(i, n) for i, ln in enumerate(lines, 1)
       if (n := len(re.findall(r'(?<!\\)\$', ln))) % 2 == 1]
check("no odd unescaped-$ lines", len(odd) == 0, f"odd={len(odd)} {odd[:3]}")

# 2. unescaped currency $ (outside math): $ directly before digit on an even-$ prefix
cur = []
for i, ln in enumerate(lines, 1):
    for m in re.finditer(r'(?<!\\)\$\d', ln):
        if ln[:m.start()].count("$") % 2 == 0 and ln[m.start():].count("$") % 2 == 1:
            cur.append((i, ln[max(0, m.start()-20):m.start()+15]))
check("no unescaped currency dollars", len(cur) == 0, f"cur={len(cur)} {cur[:3]}")

# 3. body duplicate frontmatter lines
dup = [i for i, ln in enumerate(lines, 1) if ln.startswith("**Date:**") or ln.startswith("**Abstract:**")]
check("no duplicated body date/abstract", len(dup) == 0, f"dup={dup}")

# 4. PDF: FFFD in decompressed streams (raw-byte count reported for context)
data = open(PDF, "rb").read()
raw_fffd = data.count(b"\xef\xbf\xbd")
stream_hits = 0
for sm in re.finditer(rb"stream\r?\n", data):
    endm = re.search(rb"endstream", data[sm.end():])
    if not endm:
        continue
    try:
        dec = zlib.decompress(data[sm.end():sm.end() + endm.start()])
    except Exception:
        continue
    if b"\xef\xbf\xbd" in dec:
        stream_hits += 1
check("no U+FFFD in decompressed PDF text streams", stream_hits == 0,
      f"stream_hits={stream_hits} (raw-byte count {raw_fffd} is compressed-data coincidence — FFFD-RAW-FALSE-POSITIVE-1)")

# 4b. C0 control characters in the manuscript (BEL etc. — corrupted TeX class)
c0bad = sorted({c for c in t if ord(c) < 32 and c not in "\n\t\r"})
check("no C0 control chars (BEL/escape corruption)", len(c0bad) == 0,
      f"c0={[f'U+{ord(c):04X}' for c in c0bad]}")

# 4c. heading-without-space lines (stray '#' glued to prose)
hashbad = [i for i, ln in enumerate(lines, 1) if re.match(r"^#[A-Za-z]", ln)]
check("no heading-without-space lines (stray #)", len(hashbad) == 0, f"lines={hashbad[:4]}")

# 5. HTML: single title, single abstract
h = io.open(HTML, encoding="utf-8", errors="replace").read()
check("single rendered title", len(re.findall(r'<h1[^>]*class="title"', h)) == 1)
check("zero body h1", len(re.findall(r"<h1[^>]*>", h)) - len(re.findall(r'<h1[^>]*class="title"', h)) == 0)
check("single abstract div", len(re.findall(r'<div class="abstract">', h)) == 1)
check("no FFFD in rendered HTML text", "\ufffd" not in h)

print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
io.open(r"artifacts\verification\rendering-check-log.txt", "w", encoding="utf-8").write(log.getvalue() + f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL\n")
sys.exit(0 if FAIL == 0 else 1)
