#!/usr/bin/env python3
"""P5: upload all deposit files. Flat keys via bucket PUT (octet-stream +
access_token per ZENODO-BUCKET-PUT-415-1); nested paths via deposit-API
multipart POST /files (ZENODO-MULTIPART-BYPASS-1: bucket PUT 404s on
nested keys)."""
import json
import os
import urllib.request
import urllib.parse

TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
DEP = json.load(open("artifacts/verification/p5_deposit.json", encoding="utf-8"))
BUCKET = DEP["links"]["bucket"]
DEP_ID = DEP["id"]

FLAT = [
    "ultrametric-program.md",
    "ultrametric-program.html",
    "ultrametric-program.pdf",
    "references.bib",
    "citation-audit.md",
    "README.md",
    "PROJECT-PLAN.md",
]
NESTED = [
    "docs/deep-research.md",
    "docs/red-team-p4-2026-08-23.md",
    "artifacts/universal-ignorance-audit.md",
    "artifacts/due-diligence-phase1.md",
    "artifacts/p2-consilience-map.json",
    "artifacts/external-search/arxiv-evidence-2026-08-23.json",
    "artifacts/external-search/arxiv-evidence-g5-2026-08-23.json",
    "artifacts/external-search/arxiv-evidence-res023-2026-08-23.json",
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
    "artifacts/verification/verification-integration-res023.md",
    "artifacts/verification/keyword-taxonomy-source.md",
    "artifacts/verification/corpus_qnfo_titles.json",
    "artifacts/verification/p5_gates.log",
    "artifacts/verification/p5_create_deposit.py",
    "artifacts/verification/p5_deposit.json",
    "artifacts/verification/p5_deposit.log",
]

results = []
for f in FLAT + NESTED:
    if not os.path.exists(f):
        results.append({"file": f, "status": "MISSING"})
        continue
    with open(f, "rb") as fh:
        data = fh.read()
    if f in FLAT:
        key = urllib.parse.quote(f, safe="/")
        url = f"{BUCKET}/{key}?access_token={TOKEN}"
        req = urllib.request.Request(url, data=data, method="PUT",
                                     headers={"Content-Type": "application/octet-stream"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                results.append({"file": f, "status": r.status, "bytes": len(data)})
        except Exception as e:
            results.append({"file": f, "status": "ERR", "error": str(e)[:200]})
    else:
        boundary = "----p5b" + os.urandom(8).hex()
        name = os.path.basename(f)
        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="name"\r\n\r\n{name}\r\n'
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{name}"\r\n'
            f"Content-Type: application/octet-stream\r\n\r\n"
        ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")
        url = f"https://zenodo.org/api/deposit/depositions/{DEP_ID}/files?access_token={TOKEN}"
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                results.append({"file": f, "status": r.status, "bytes": len(data)})
        except Exception as e:
            results.append({"file": f, "status": "ERR", "error": str(e)[:200]})

print(json.dumps(results, indent=1))
ok = sum(1 for r in results if r.get("status") == 201)
print(f"UPLOADED {ok}/{len(FLAT) + len(NESTED)}")
with open("artifacts/verification/p5_upload.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
