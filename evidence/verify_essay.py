#!/usr/bin/env python3
"""Verify every key figure in the essay against the evidence files (26-figure check).
Evidence pack file for the $1,032 Research Program (10.5281/zenodo.22028851)."""
import json, re, sys

ESSAY = r"C:\Users\LENOVO\AppData\Local\Temp\v12\ai-accelerated-research.md"
SUM = r"C:\Users\LENOVO\AppData\Local\Temp\v12\usage_summary.json"

text = open(ESSAY, encoding="utf-8").read()
data = json.load(open(SUM, encoding="utf-8"))
g = data["grand"]["__TOTAL__"]

checks = [
    ("total cost", "$1,032.08"), ("requests", "323,381"),
    ("input tokens", "49.86B"), ("output tokens", "248.4M"),
    ("total tokens", "50.11B"), ("cache hit tokens", "48.08B"),
    ("cache miss tokens", "1.79B"), ("hit rate pct", "96.4%"),
    ("blended per 1B", "$20.60"), ("billed days", "184"),
    ("mean/day", "$5.61"), ("peak day", "$61.91"), ("peak week", "$173.22"),
    ("July cost", "$440.16"), ("July requests", "124.3K"),
    ("August cost", "$327.73"), ("August requests", "92.7K"),
    ("pro cost", "$818.97"), ("pro requests", "235.0K"),
    ("pro input", "30.69B"), ("pro output", "152.1M"),
    ("flash cost", "$173.21"), ("flash requests", "79.0K"),
    ("flash input", "18.70B"), ("flash output", "83.3M"),
    ("legacy cost", "$39.91"), ("legacy requests", "9.4K"),
    ("pro miss price", "$0.435"), ("pro hit price", "$0.0036"),
    ("pro out price", "$0.87"), ("flash miss price", "$0.14"),
    ("flash hit price", "$0.0028"), ("flash out price", "$0.28"),
    ("Zenodo records", "911"), ("ORCID works", "877"),
    ("KG paper nodes", "1,646"), ("KG total nodes", "8,308"),
    ("GitHub repos", "114"), ("repos in window", "109"),
    ("Workers", "20"), ("UIA DOI", "10.5281/zenodo.21901984"),
    ("IAPS DOI", "10.5281/zenodo.21901983"), ("Tyranny DOI", "10.5281/zenodo.21939595"),
    ("NIH min 2019", "$50,004"), ("window days", "263"),
    ("per-work cost", "$1.18"), ("output words", "186 million"),
    ("typing work-years", "39 work-years"), ("reading words", "1.34 billion"),
    ("reading work-years", "45 work-years"),
]

fails = []
for label, s in checks:
    if s not in text:
        fails.append((label, s))

t = g
ok = True
if abs(t["cost"] - 1032.08) > 0.01:
    print("MISMATCH total cost vs json"); ok = False
if t["requests"] != 323381:
    print("MISMATCH requests vs json"); ok = False
if abs(t["input_tokens"] - 49.86e9) > 1e7:
    print("MISMATCH input vs json", t["input_tokens"]); ok = False
if abs(t["output_tokens"] - 248.4e6) > 1e5:
    print("MISMATCH output vs json"); ok = False

if fails:
    print(f"FAILED ({len(fails)}):")
    for l, s in fails:
        print(f"  missing: {l} = '{s}'")
    sys.exit(1)
print(f"ALL {len(checks)} figure checks PASSED")
print("summary.json cross-checks:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
