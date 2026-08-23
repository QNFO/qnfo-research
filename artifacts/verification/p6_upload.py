#!/usr/bin/env python3
"""P6: upload all deposit files via bucket PUT (octet-stream, access_token)."""
import json
import os
import urllib.request
import urllib.parse

TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
DEP = json.load(open("artifacts/verification/p6_deposit.json", encoding="utf-8"))
BUCKET = DEP["links"]["bucket"]

FILES = [
    "keyword-taxonomy-consilience.md",
    "keyword-taxonomy-consilience.html",
    "keyword-taxonomy-consilience.pdf",
    "references.bib",
    "citation-audit.md",
    "README.md",
    "PROJECT-PLAN.md",
    "docs/deep-research.md",
    "docs/red-team-p5-2026-08-23.md",
    "docs/QNFO-KEYWORD-TAXONOMY.md",
    "artifacts/universal-ignorance-audit.md",
    "artifacts/due-diligence-phase1.md",
    "artifacts/p2-consilience-map.md",
    "artifacts/p2-consilience-map.json",
    "artifacts/external-search/arxiv-evidence-2026-08-23.json",
    "artifacts/external-search/arxiv-evidence-g5-2026-08-23.json",
    "artifacts/verification/rq5_keyword_load.py",
    "artifacts/verification/rq5_results.json",
    "artifacts/verification/rq5_run.log",
    "artifacts/verification/rq1_retrieval_benchmark.py",
    "artifacts/verification/rq1_results.json",
    "artifacts/verification/rq1_run.log",
    "artifacts/verification/rq2_consilience_links.py",
    "artifacts/verification/rq2_results.json",
    "artifacts/verification/rq2_run.log",
    "artifacts/verification/rq3_archimedean_limit.py",
    "artifacts/verification/rq3_results.json",
    "artifacts/verification/rq3_run.log",
    "artifacts/verification/rq4_noise_scaling.py",
    "artifacts/verification/rq4_results.json",
    "artifacts/verification/rq4_run.log",
    "artifacts/verification/verification-summary.md",
    "artifacts/verification/keyword-taxonomy-source.md",
    "artifacts/verification/corpus_qnfo_titles.json",
    "artifacts/verification/p6_gate_check.py",
    "artifacts/verification/p6_gate_check.json",
    "artifacts/verification/p6_gate_check.log",
    "artifacts/verification/p6_create_deposit.py",
    "artifacts/verification/p6_deposit.json",
    "artifacts/verification/p6_deposit.log",
]

results = []
for f in FILES:
    if not os.path.exists(f):
        results.append({"file": f, "status": "MISSING"})
        continue
    key = urllib.parse.quote(f, safe="/")
    url = f"{BUCKET}/{key}?access_token={TOKEN}"
    with open(f, "rb") as fh:
        data = fh.read()
    req = urllib.request.Request(url, data=data, method="PUT",
                                 headers={"Content-Type": "application/octet-stream"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            results.append({"file": f, "status": r.status, "bytes": len(data)})
    except Exception as e:
        results.append({"file": f, "status": "ERR", "error": str(e)[:200]})

print(json.dumps(results, indent=1))
ok = sum(1 for r in results if r.get("status") == 201)
print(f"UPLOADED {ok}/{len(FILES)}")
with open("artifacts/verification/p6_upload.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
