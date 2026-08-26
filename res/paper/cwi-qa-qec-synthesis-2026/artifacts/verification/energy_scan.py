#!/usr/bin/env python3
"""RES.026 P4 — energy-term scan over the CWI deck texts.

Reproduces the paper's section 3 claim: across the seven decks, zero energy
PRICING statements.

Classification rule (stated and reproducible):
  hit           = case-insensitive occurrence of an energy term
                  (joule|energy|power|watt|thermodynamic|cooling|landauer|
                   consumption|dissipation|heat)
  pricing hit   = a hit whose +/-200-char window contains a number AND one of
                  the multi-char unit tokens (kW|MW|mW|uW|uW(unicode)|J|kJ|mJ|
                  uJ|Wh|kWh|TWh|watt|watts|joule|joules). Single-letter "K"
                  and "W" are deliberately excluded: in these decks "K" is the
                  decoder list-size parameter (e.g. K=2^12) and "W" is a
                  logical weight symbol, not a unit.

Usage:
  python energy_scan.py --decks-dir DIR [--out energy_scan.json]

Deck texts are extracted with pypdf (runtime: CPython 3.12 + pypdf; no other
dependencies). The decks themselves remain with the organizers (password-
protected SURFdrive share); this script runs on the seven PDFs as retrieved
2026-08-26.
"""
import argparse
import json
import os
import re

try:
    import pypdf
except ImportError:  # pragma: no cover
    pypdf = None

TERMS = re.compile(
    r"joule|energy|power|watt|thermodynamic|cooling|landauer|consumption|dissipation|heat",
    re.I,
)
UNITS = re.compile(
    r"\b(kW|MW|mW|uW|\u00b5W|J|kJ|mJ|uJ|\u00b5J|Wh|kWh|TWh|watts?|joules?)\b",
    re.I,
)
NUMBER = re.compile(r"\d")


def extract(path):
    """Return per-page text of a PDF."""
    reader = pypdf.PdfReader(path)
    return [p.extract_text() or "" for p in reader.pages]


def scan(text):
    hits = []
    for m in TERMS.finditer(text):
        a = max(0, m.start() - 200)
        b = min(len(text), m.end() + 200)
        ctx = text[a:b]
        pricing = bool(NUMBER.search(ctx) and UNITS.search(ctx))
        hits.append(
            {
                "term": m.group(0),
                "pos": m.start(),
                "pricing": pricing,
                "context": ctx,
            }
        )
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--decks-dir", required=True)
    ap.add_argument("--out", default="energy_scan.json")
    args = ap.parse_args()

    if pypdf is None:
        raise SystemExit("pypdf required: pip install pypdf")

    decks = sorted(f for f in os.listdir(args.decks_dir) if f.lower().endswith(".pdf"))
    if not decks:
        raise SystemExit(f"no PDFs in {args.decks_dir}")

    result = {"scan_date": "2026-08-26", "decks": [], "pricing_statements": 0, "hits": {}}
    for name in decks:
        pages = extract(os.path.join(args.decks_dir, name))
        text = "\n".join(pages)
        hits = scan(text)
        result["decks"].append({"file": name, "pages": len(pages), "chars": len(text)})
        result["hits"][name] = hits
        result["pricing_statements"] += sum(1 for h in hits if h["pricing"])

    result["claim"] = "section 3: zero energy pricing statements across the seven decks"
    result["claim_holds"] = result["pricing_statements"] == 0

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=1)

    total = sum(len(v) for v in result["hits"].values())
    print(f"decks={len(decks)} total_hits={total} "
          f"pricing_statements={result['pricing_statements']} "
          f"claim_holds={result['claim_holds']}")
    for name in decks:
        hits = result["hits"][name]
        print(f"  {name}: {len(hits)} hit(s) "
              f"[{', '.join(sorted({h['term'] for h in hits}))}]")


if __name__ == "__main__":
    main()
