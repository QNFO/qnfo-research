#!/usr/bin/env python3
"""QNFO.RES.028 — check_rendering.py: publication-gate scans for the paper md.
Checks: odd unescaped-$ per line (false MathJax pairs); currency-dollar escapes;
body byline/abstract duplication (FRONTMATTER-DUPLICATION-1); Unicode superscripts
(U+2070-U+209C); banned brand tokens (PUBLICATION-BRAND-LANGUAGE-1 /
PUBLICATION-META-PROSE-1); internal WBS codes (INTERNAL-REF-1); every @cite key
resolves in references.bib (BIB-ORPHAN-1). Exit 0 iff all pass."""
import re
import sys
import unicodedata

MD = "arithmetic-anyon-contact.md"
BIB = "references.bib"

md = open(MD, encoding="utf-8").read()
lines = md.splitlines()
bib = open(BIB, encoding="utf-8").read()
bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))

problems = []

def fail(msg):
    problems.append(msg)
    print(f"[FAIL] {msg}")

def ok(msg):
    print(f"[PASS] {msg}")

# 1. odd unescaped $ per line (body only, after frontmatter)
in_front = True
dash_count = 0
odd_lines = []
for i, line in enumerate(lines, 1):
    if in_front:
        if line.strip() == "---":
            dash_count += 1
            if dash_count == 2:
                in_front = False
        continue
    if line.strip().startswith("```"):
        continue
    dollars = len(re.findall(r"(?<!\\)\$", line))
    if dollars % 2 == 1:
        odd_lines.append(i)
if odd_lines:
    fail(f"odd unescaped-$ lines: {odd_lines[:8]}")
else:
    ok("no odd unescaped-$ lines (MathJax pairs balanced)")

# 2. currency dollars: $ followed by a money amount (3+ digits or comma groups),
# not math like $1/3$, $2m$-th, $1.55$, $10^6$
cur = [i for i, l in enumerate(lines, 1) if re.search(r"(?<!\$)\$(?:\d{3,}|\d{1,3}(?:,\d{3})+)(?:\.\d+)?", l)]
if cur:
    fail(f"currency-dollar patterns at lines {cur[:8]}")
else:
    ok("no currency-dollar patterns")

# 3. body duplication: byline/abstract/date markers in body
body = md.split("---", 2)[2] if md.startswith("---") else md
dup = []
for pat in (r"^\*\*Author", r"^\*\*Date", r"^\*\*Abstract", r"^# .*Arithmetic Anyons"):
    for i, l in enumerate(body.splitlines(), 1):
        if re.match(pat, l):
            dup.append((pat, i))
if dup:
    fail(f"body duplication markers: {dup[:6]}")
else:
    ok("no body byline/abstract/H1 duplication")

# 4. Unicode superscripts U+2070-U+209C
sup = [(i, l) for i, l in enumerate(lines, 1)
       if any(0x2070 <= ord(c) <= 0x209C for c in l)]
if sup:
    fail(f"Unicode superscripts at lines {[s[0] for s in sup[:8]]}")
else:
    ok("no Unicode superscripts (U+2070-U+209C)")

# 5. banned brand tokens (case-insensitive, word-level)
banned = ["honest", "ledger", "weigh this", "kill-condition", "falsifiability register",
          "pre-registered", "falsifier", "not a silence", "published, not hidden",
          "published here", "silenced", "null not hidden"]
hits = {}
for tok in banned:
    for i, l in enumerate(lines, 1):
        if tok in l.lower():
            hits.setdefault(tok, []).append(i)
if hits:
    fail(f"banned brand tokens: {hits}")
else:
    ok("no banned brand tokens")

# 6. internal WBS codes
wbs = [i for i, l in enumerate(lines, 1) if re.search(r"QNFO\.\w+\.\d{3}", l)]
if wbs:
    fail(f"internal WBS codes at lines {wbs[:8]}")
else:
    ok("no internal WBS codes in the paper")

# 7. every @cite key resolves in references.bib
cites = set(re.findall(r"@([A-Za-z0-9_:-]+)", body))
missing = sorted(c for c in cites if c not in bibkeys)
orphans = sorted(b for b in bibkeys if b not in cites)
if missing:
    fail(f"cited keys missing from bib: {missing}")
else:
    ok(f"all {len(cites)} cited keys resolve in references.bib")
if orphans:
    fail(f"uncited bib entries (would be dropped from rendered bibliography): {orphans}")
else:
    ok("no uncited bib entries")

print()
if problems:
    print(f"RESULT: {len(problems)} problem(s)")
    sys.exit(1)
print("RESULT: ALL GATES PASS")
sys.exit(0)
