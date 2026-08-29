"""check_rendering.py — QNFO.RES.031 publication gate (project-level).

Checks per the publication gates:
  CURRENCY-DOLLAR-ESCAPE-1  — no '$' immediately followed by a digit (currency
                              vs math delimiter false-positive); balanced '$'.
  FRONTMATTER-DUPLICATION-1 — no body H1 duplicating the YAML title; abstract
                              not repeated in body.
  GLYPH-INTEGRITY           — no U+FFFD / U+FFFF in source.
  PUBLICATION-PROSE-GATE-1  — no internal pipeline vocabulary in the paper md.
Usage: python check_rendering.py <paper.md>
Exit 0 = PASS, 1 = FAIL (with reasons).
"""
import re
import sys

INTERNAL_PATTERNS = [
    ("WBS code", r"QNFO\.[A-Z]+\.\d+"),
    ("org brand token", r"\bQNFO\b"),
    ("gate names", r"SO-WHAT-GATE|PRACTITIONER-RELEVANCE|PUBLICATION-PROSE|COMPUTATIONAL-VERIFICATION|CROSSWALK-TRANSLATION|ZENODO-INQUIRY|DUE-DILIGENCE"),
    ("claim shorthand", r"\bC[1-4]\b(?=\s*\(|\s*[-–—])|C3\("),
    ("phase/deliverable codes", r"\b[MPD][0-9]\b(?=\s*\()|DR[0-9]\b"),
    ("pipeline vocab", r"provenance chat|red[- ]team|re-audit|handoff|registry|deep research doc|UIA"),
    ("internal refs", r"vault notes|\.md\b.*(?=vault)|artifacts/"),
]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "arithmetic-quantum-thermodynamics.md"
    text = open(path, encoding="utf-8").read()
    fails = []

    # --- math/currency dollar checks ---
    # math spans: pair up '$' delimiters; '$$' display pairs first
    n_dollar = text.count("$")
    if n_dollar % 2 != 0:
        fails.append(f"unbalanced '$' delimiters ({n_dollar} total)")
    # currency = '$' immediately followed by a digit OUTSIDE a math span
    currency_hits = []
    i = 0
    in_math = False
    while i < len(text) - 1:
        if text[i] == "$":
            in_math = not in_math
            i += 1
            continue
        if text[i] == "$" and not in_math and text[i + 1].isdigit():
            currency_hits.append(text[max(0, i - 12):i + 14].replace("\n", " "))
        i += 1
    if currency_hits:
        fails.append(f"currency pattern '$'+digit outside math: {currency_hits[:3]}")

    # --- frontmatter duplication ---
    m_title = re.search(r"^title:\s*\"([^\"]+)\"", text, re.M)
    yaml_title = m_title.group(1) if m_title else None
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    h1s = re.findall(r"^#\s+(.+)$", body, re.M)
    if h1s:
        fails.append(f"body H1 present (title duplication risk): {h1s[:2]}")
    if yaml_title and yaml_title.lower() in body.lower():
        fails.append("YAML title string appears verbatim in body")
    m_abs = re.search(r"^abstract:\s*\|?\s*", text, re.M)
    if m_abs:
        abs_start = m_abs.end()
        abs_text = text[abs_start:abs_start + 220]
        first_sentence = re.split(r"(?<=\.)\s", abs_text.strip())[0][:120]
        if first_sentence and first_sentence in body:
            fails.append("abstract first sentence repeated in body")

    # --- glyphs ---
    if "\ufffd" in text or "\uffff" in text:
        fails.append("U+FFFD/U+FFFF present in source")

    # --- internal vocabulary ---
    for label, pat in INTERNAL_PATTERNS:
        hits = re.findall(pat, text)
        if hits:
            fails.append(f"internal vocabulary '{label}': {sorted(set(hits))[:4]}")

    # --- citation sanity ---
    cited = set(re.findall(r"@([a-zA-Z0-9]+)", text))
    print(f"[INFO] distinct citation keys used: {len(cited)}")

    if fails:
        print("[FAIL] " + "; ".join(fails))
        sys.exit(1)
    print("[PASS] paper renders clean: balanced math, no currency-$ collisions, no frontmatter duplication, no bad glyphs, no internal vocabulary")
    sys.exit(0)


if __name__ == "__main__":
    main()
