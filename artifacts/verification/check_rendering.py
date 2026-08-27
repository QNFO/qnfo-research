#!/usr/bin/env python3
"""QNFO.RES.029 — check_rendering publication gate.

Usage: python check_rendering.py <paper.md> <references.bib>

Checks: dollar parity (MathJax), currency-dollar scan, banned words, brand tokens,
Unicode superscripts, frontmatter duplication (H1 mirror / body byline), remaining
numeric citations, and cite-key integrity (every cited key in the bib; no orphans).
Exit code 0 iff all checks pass.
"""

import re
import sys


def main() -> int:
    paper, bibp = sys.argv[1], sys.argv[2]
    t = open(paper, encoding="utf-8").read()
    bib = open(bibp, encoding="utf-8").read()
    fails = []

    dollars = t.count("$")
    if dollars % 2:
        fails.append("odd-dollar count: %d" % dollars)
    # currency pattern: a $ directly followed by digits continuing into a comma/dot number
    # and NOT closed by another $ on the same line (math delimiters are paired)
    for line in t.splitlines():
        if line.count("$") % 2 == 1:
            for m in re.finditer(r"\$[0-9][0-9,\.]*", line):
                fails.append("currency-like token: %r (line: %s)" % (m.group(0), line.strip()[:60]))

    banned = ["reality", "fundamental", "essence", "truly", "deeply", "profoundly",
              "actually", "basically", "merely", "essentially", "obviously", "clearly"]
    for w in banned:
        n = len(re.findall(r"\b" + w + r"\b", t, re.I))
        if n:
            fails.append("banned word: %s x%d" % (w, n))

    brand = ["kill-condition", "weigh this", "falsifiability register", "null ledger",
             "honest question", "honest landscape", "honest accounting"]
    for w in brand:
        n = len(re.findall(w, t, re.I))
        if n:
            fails.append("brand token: %s x%d (bibliographic-title hits need manual review)" % (w, n))

    sup = [c for c in t if 0x2070 <= ord(c) <= 0x209C]
    if sup:
        fails.append("unicode superscripts: %d" % len(sup))

    if t.count("# Adelic Quantum Arithmetic") > 0:
        fails.append("H1 title mirror present")
    if "**Author:**" in t or "**Date:**" in t:
        fails.append("body byline present")

    num = re.findall(r"\[[0-9]+(\s*,\s*[0-9]+)*\]", t)
    if num:
        fails.append("numeric citations remain: %r" % num)

    cited = set(re.findall(r"@([\w-]+)", t))
    keys = set(re.findall(r"@\w+\{([\w-]+)", bib))
    if cited - keys:
        fails.append("cited-not-in-bib: %s" % sorted(cited - keys))
    if keys - cited:
        fails.append("bib orphans (uncited): %s" % sorted(keys - cited))

    if fails:
        print("RENDER-CHECK: FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("RENDER-CHECK: PASS (dollars %d even; 0 banned; 0 brand; 0 superscripts; 0 duplication; citations %d/%d)"
          % (dollars, len(cited), len(keys)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
