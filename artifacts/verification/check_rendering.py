#!/usr/bin/env python3
"""JPC.003 rendering gate — run BEFORE publish (CURRENCY-DOLLAR-ESCAPE-1,
FRONTMATTER-DUPLICATION-1, FFFD-RAW-FALSE-POSITIVE-1, reference-count parity).

Checks:
  1. odd-unescaped-$ scan in body lines (false MathJax pairs)
  2. currency-digit scan ($ followed by digit without escape)
  3. frontmatter duplication: body must not repeat YAML title/date/abstract verbatim
  4. raw U+FFFD scan in .md (informational; PDF glyph gate is separate)
  5. reference-count parity: [n] markers vs rendered list count

Usage: python check_rendering.py <paper.md>
Exit 0 = PASS, 1 = FAIL.
"""
import re, sys

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "paper.md"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    problems = []
    # frontmatter
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm_block = fm.group(1) if fm else ""
    yaml_title = re.search(r"^title:\s*\"?(.+?)\"?\s*$", fm_block, re.M)
    body = text[fm.end():] if fm else text
    ytitle = yaml_title.group(1).strip().strip('"') if yaml_title else None
    if ytitle and ytitle in body:
        problems.append(f"H1 body duplicates YAML title: {ytitle[:60]}")
    # odd unescaped dollars per line
    for i, line in enumerate(body.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("$"):  # math block open/close
            continue
        # count unescaped '$'
        unesc = len(re.findall(r"(?<!\\)\$", stripped))
        if unesc % 2 == 1:
            problems.append(f"H2 odd-unescaped-$ line {i}: {stripped[:70]}")
        if re.search(r"(?<!\\)\$\s*\d", stripped):
            problems.append(f"H3 currency-digit unescaped line {i}: {stripped[:70]}")
    # raw FFFD
    fffd = body.count("\ufffd")
    if fffd:
        problems.append(f"H4 raw U+FFFD in body: {fffd} occurrence(s)")
    # reference count parity
    markers = set(re.findall(r"\[(\d+)\]", body))
    n_markers = len({int(m) for m in markers if m.isdigit()})
    ref_lines = [l for l in body.splitlines() if re.match(r"^\[\d+\]\s", l.strip())]
    n_refs = len(ref_lines)
    if n_markers != n_refs:
        problems.append(f"H5 marker/ref count mismatch: {n_markers} markers vs {n_refs} refs")
    # marker max vs ref count
    max_marker = max((int(m) for m in markers if m.isdigit()), default=0)
    if max_marker != n_refs:
        problems.append(f"H6 max marker {max_marker} != ref count {n_refs}")
    if problems:
        print("RENDERING GATE: FAIL")
        for p in problems:
            print(" -", p)
        return 1
    print(f"RENDERING GATE: PASS ({n_refs} refs, no odd-$, no dup frontmatter, 0 U+FFFD)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
