#!/usr/bin/env python3
"""P6: upload nested-path files via deposit-API multipart POST (ZENODO-MULTIPART-BYPASS-1)."""
import json
import os
import sys
import urllib.request

TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
DEP_ID = 22071421

FILES = [
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
]

def multipart_upload(url, filepath):
    boundary = "----p6boundary" + os.urandom(8).hex()
    with open(filepath, "rb") as fh:
        data = fh.read()
    name = os.path.basename(filepath)
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="name"\r\n\r\n{name}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{name}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status

results = []
for f in FILES:
    url = f"https://zenodo.org/api/deposit/depositions/{DEP_ID}/files?access_token={TOKEN}"
    try:
        st = multipart_upload(url, f)
        results.append({"file": f, "status": st})
    except Exception as e:
        results.append({"file": f, "status": "ERR", "error": str(e)[:200]})

print(json.dumps(results, indent=1))
print(f"UPLOADED {sum(1 for r in results if r.get('status') == 201)}/{len(FILES)}")
with open("artifacts/verification/p6_upload2.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
