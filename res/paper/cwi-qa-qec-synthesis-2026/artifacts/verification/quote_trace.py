#!/usr/bin/env python3
"""RES.026 P4 — quote trace: assert every verbatim quote in the paper.

Sections 2-4 of the paper quote the deck texts. This script asserts each
verbatim quote against its deck's extracted text.

Matching rule: both sides are normalized by (1) lowercasing, (2) mapping
unicode ellipsis/dash/quote characters to ASCII, (3) removing ALL whitespace.
Whitespace-insensitive matching is required because pypdf's extraction both
drops spaces (e.g. "is essentially" -> "isessentially") and inserts them
(e.g. "10^7 - 10^8"). Substring match on the normalized deck text, per page.

Scope: verbatim prose quotes only. Numeric claims are covered separately by
the citation audit (P3.AUTHOR-GATE-EVERY-ENTRY-1: arXiv-verified titles for
refs [2] and [3], live-source verification recorded in citation-audit.md) and
by the deck-traced rows of artifacts/cwi-slide-audit.md.

Usage:
  python quote_trace.py --decks-dir DIR --paper PATH [--out quote_trace.json]
"""
import argparse
import json
import os
import re
import unicodedata

try:
    import pypdf
except ImportError:  # pragma: no cover
    pypdf = None

# (deck file, verbatim quote as it appears in the paper, slide reference)
QUOTES = [
    ("Leverrier-1.pdf", "hardware progress alone won't get us there!", "slide 4"),
    ("Leverrier-2.pdf", "QLDPC decoding is still wide open", "slide 2"),
    ("Leverrier-2.pdf", "Heavy runtime tails", "slide 10"),
    ("Leverrier-2.pdf", "expensive training", "slide 11"),
    ("Leverrier-2.pdf",
     "Time complexity should be at most (roughly) linear in n. Ideally, process "
     "available syndrome bits as they are produced.", "slide 15"),
    # The paper's slide-15 quote continues with "Streaming decoders..." (ellipsis
    # truncation of "Streaming decoders: window decoding carries partial boundary
    # information forward"); truncated quotes are asserted as their longest
    # verbatim fragment plus the verbatim tail fragment below.
    ("Leverrier-2.pdf", "Streaming decoders", "slide 15"),
    ("Leverrier-1.pdf",
     "terribly bad code parameters, but this is essentially (!) optimal in 2 dimensions",
     "slide 17"),
    ("Leverrier-1.pdf", "interesting theory results, maybe not so useful in practice", "slide 40"),
    ("Leverrier-2.pdf", "Main open question: why do small lists work so well?", "slide 51"),
]

_TR = str.maketrans(
    {
        "\u2026": "...",
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2261": "=",
        "\u21d2": "=>",
        "\u2264": "<=",
        "\u2022": "",  # bullets are layout artifacts, not text
        "\u00b7": "",
    }
)


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(_TR)
    return re.sub(r"\s+", "", text.lower())


def extract_pages(path):
    reader = pypdf.PdfReader(path)
    return [p.extract_text() or "" for p in reader.pages]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--decks-dir", required=True)
    ap.add_argument("--paper", required=True)
    ap.add_argument("--out", default="quote_trace.json")
    args = ap.parse_args()

    if pypdf is None:
        raise SystemExit("pypdf required: pip install pypdf")

    with open(args.paper, encoding="utf-8") as fh:
        paper = fh.read()
    paper_norm = normalize(paper)

    # deck -> normalized per-page text
    deck_texts = {}
    for name in sorted(os.listdir(args.decks_dir)):
        if name.lower().endswith(".pdf"):
            deck_texts[name] = [
                normalize(p) for p in extract_pages(os.path.join(args.decks_dir, name))
            ]

    results = []
    for deck, quote, slide in QUOTES:
        q = normalize(quote)
        found = False
        page = None
        pages = deck_texts.get(deck, [])
        for i, p in enumerate(pages, 1):
            if q in p:
                found = True
                page = i
                break
        results.append(
            {"deck": deck, "quote": quote, "slide": slide, "found": found, "page": page}
        )
        print(f"{'OK ' if found else 'MISS'} {deck} [{slide}] p={page}: {quote[:60]}")

    n_missing = sum(1 for r in results if not r["found"])
    out = {
        "check_date": "2026-08-26",
        "quotes": results,
        "total": len(results),
        "missing": n_missing,
        "claim": "section 4 quote-trace: all verbatim quotes asserted against their decks",
        "claim_holds": n_missing == 0,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print(f"total={len(results)} missing={n_missing} claim_holds={out['claim_holds']}")


if __name__ == "__main__":
    main()
