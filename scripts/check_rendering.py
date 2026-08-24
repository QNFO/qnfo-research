#!/usr/bin/env python3
"""check_rendering.py — publication rendering gates (CURRENCY-DOLLAR-ESCAPE-1,
FRONTMATTER-DUPLICATION-1, PUBLICATION-BRAND-LANGUAGE-1, META-PROSE-1).

Scans the markdown source for:
  1. odd-count unescaped $ on a line (false MathJax pairs -> TeX render errors)
  2. body duplication of YAML title/author/date (title page renders them)
  3. banned brand/meta-prose tokens (PUBLICATION-BRAND-LANGUAGE-1,
     PUBLICATION-META-PROSE-1)
Usage: python scripts/check_rendering.py <paper.md>
Exit 0 = all gates pass.
"""
import re
import sys
from pathlib import Path

BANNED = [
    "honest question", "the honest landscape", "honestly reported",
    "weigh this record", "kill-condition", "[speculative]",
    "published, not hidden", "published here rather than hidden",
    "not a silence", "kept on the same ledger", "falsifiability register",
    "pre-registered observables",
]


def main() -> int:
    md = Path(sys.argv[1] if len(sys.argv) > 1 else "paper.md")
    txt = md.read_text(encoding="utf-8")
    fail = False

    # 1) currency-dollar: odd unescaped $ on a line (ignore $$ and \$-escaped)
    problems = []
    for i, line in enumerate(txt.split("\n"), 1):
        stripped = line.replace("\\$", "").replace("$$", "")
        if stripped.count("$") % 2 == 1:
            problems.append(i)
    print(f"[1] CURRENCY-DOLLAR-ESCAPE-1: odd unescaped '$' lines: {problems}")
    fail |= bool(problems)

    # 2) frontmatter duplication: body must not re-state YAML title/author/date
    parts = txt.split("---", 2)
    if len(parts) >= 3:
        yaml, body = parts[1], parts[2]
        title_m = re.search(r"^title:\s*(.+)$", yaml, re.M)
        body_starts = body.strip().startswith("# ")
        byline = bool(re.search(r"\*\*Date:\*\*|\*\*Author\*\*|^\*\*Abstract:\*\*",
                                body, re.M))
        dup_title = bool(title_m and title_m.group(1).strip().strip('"\'')
                         in body.split("\n\n", 1)[0])
        print(f"[2] FRONTMATTER-DUPLICATION-1: body H1 mirror={body_starts}, "
              f"byline={byline}, title-dup-in-first-block={dup_title}")
        fail |= bool(body_starts or byline or dup_title)
    else:
        print("[2] FRONTMATTER-DUPLICATION-1: no YAML frontmatter found (skip)")

    # 3) brand/meta-prose sweep
    low = txt.lower()
    hits = [b for b in BANNED if b in low]
    print(f"[3] BRAND/META-PROSE: banned-token hits: {hits}")
    fail |= bool(hits)

    print("PASS" if not fail else "FAIL")
    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main())
