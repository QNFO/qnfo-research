#!/usr/bin/env python3
"""v2.4 upload: 40 files to draft 22073477 (records-API by-key flow)."""
import json, os, urllib.request, urllib.error
TOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
DRAFT = 22073477
BASE = f"https://zenodo.org/api/records/{DRAFT}/draft/files"
FILES = [
    "ultrametric-program.md", "ultrametric-program.html", "ultrametric-program.pdf",
    "references.bib", "citation-audit.md", "README.md", "PROJECT-PLAN.md",
    "pdf-style.css", "scripts/build-pdf.py",
    "deep-research.md", "red-team-p4-2026-08-23.md", "red-team-p7-2026-08-23.md",
    "red-team-pdf-2026-08-24.md",
    "universal-ignorance-audit.md", "due-diligence-phase1.md", "p2-consilience-map.json",
    "arxiv-evidence-2026-08-23.json", "arxiv-evidence-g5-2026-08-23.json",
    "arxiv-evidence-res023-2026-08-23.json",
    "rq5_keyword_load.py", "rq5_results.json", "rq5_run.log",
    "rq1_retrieval_benchmark.py", "rq1_results.json", "rq1_run.log",
    "rq2_consilience_links.py", "rq2_results.json", "rq2_run.log",
    "rq3_archimedean_limit.py", "rq3_results.json", "rq3_run.log",
    "rq4_noise_scaling.py", "rq4_results.json", "rq4_run.log",
    "verification-integration-res023.md", "keyword-taxonomy-source.md",
    "corpus_qnfo_titles.json",
    "inherited-rq1_results.json", "inherited-rq5_results.json", "p5_gates.log",
]
LOCAL_MAP = {
    "deep-research.md": "docs/deep-research.md",
    "red-team-p4-2026-08-23.md": "docs/red-team-p4-2026-08-23.md",
    "red-team-p7-2026-08-23.md": "docs/red-team-p7-2026-08-23.md",
    "red-team-pdf-2026-08-24.md": "docs/red-team-pdf-2026-08-24.md",
    "universal-ignorance-audit.md": "artifacts/universal-ignorance-audit.md",
    "due-diligence-phase1.md": "artifacts/due-diligence-phase1.md",
    "p2-consilience-map.json": "artifacts/p2-consilience-map.json",
    "arxiv-evidence-2026-08-23.json": "artifacts/external-search/arxiv-evidence-2026-08-23.json",
    "arxiv-evidence-g5-2026-08-23.json": "artifacts/external-search/arxiv-evidence-g5-2026-08-23.json",
    "arxiv-evidence-res023-2026-08-23.json": "artifacts/external-search/arxiv-evidence-res023-2026-08-23.json",
    "rq5_keyword_load.py": "artifacts/verification/rq5_keyword_load.py",
    "rq5_results.json": "artifacts/verification/rq5_results.json",
    "rq5_run.log": "artifacts/verification/rq5_run.log",
    "rq1_retrieval_benchmark.py": "artifacts/verification/rq1_retrieval_benchmark.py",
    "rq1_results.json": "artifacts/verification/rq1_results.json",
    "rq1_run.log": "artifacts/verification/rq1_run.log",
    "rq2_consilience_links.py": "artifacts/verification/rq2_consilience_links.py",
    "rq2_results.json": "artifacts/verification/rq2_results.json",
    "rq2_run.log": "artifacts/verification/rq2_run.log",
    "rq3_archimedean_limit.py": "artifacts/verification/rq3_archimedean_limit.py",
    "rq3_results.json": "artifacts/verification/rq3_results.json",
    "rq3_run.log": "artifacts/verification/rq3_run.log",
    "rq4_noise_scaling.py": "artifacts/verification/rq4_noise_scaling.py",
    "rq4_results.json": "artifacts/verification/rq4_results.json",
    "rq4_run.log": "artifacts/verification/rq4_run.log",
    "verification-integration-res023.md": "artifacts/verification/verification-integration-res023.md",
    "keyword-taxonomy-source.md": "artifacts/verification/keyword-taxonomy-source.md",
    "corpus_qnfo_titles.json": "artifacts/verification/corpus_qnfo_titles.json",
    "inherited-rq1_results.json": "artifacts/verification/inherited-res022/rq1_results.json",
    "inherited-rq5_results.json": "artifacts/verification/inherited-res022/rq5_results.json",
    "p5_gates.log": "artifacts/verification/p5_gates.log",
}
def req(url, method="GET", data=None, ctype=None):
    h = {"Authorization": "Bearer " + TOKEN}
    if ctype: h["Content-Type"] = ctype
    r = urllib.request.Request(url, data=data, method=method, headers=h)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return resp.status, resp.read()
def entries():
    st, body = req(BASE)
    return json.loads(body).get("entries", [])
results = []
for key in FILES:
    local = LOCAL_MAP.get(key, key)
    if not os.path.exists(local):
        results.append({"file": key, "status": "MISSING-LOCAL"})
        continue
    with open(local, "rb") as fh:
        data = fh.read()
    try:
        entry = next((e for e in entries() if e.get("key") == key), None)
        if entry is None:
            st, _ = req(BASE, "POST", json.dumps([{"key": key}]).encode(), "application/json")
            entry = next((e for e in entries() if e.get("key") == key), None)
        if entry is None:
            results.append({"file": key, "status": "ERR", "error": "entry missing after init"})
            continue
        st2, _ = req(entry["links"]["content"], "PUT", data, "application/octet-stream")
        st3, _ = req(entry["links"]["commit"], "POST", b"{}", "application/json")
        results.append({"file": key, "put": st2, "commit": st3, "size": len(data)})
    except urllib.error.HTTPError as e:
        results.append({"file": key, "status": "ERR", "error": f"{e.code}: {e.read().decode()[:120]}"})
    except Exception as e:
        results.append({"file": key, "status": "ERR", "error": str(e)[:120]})
print(json.dumps(results, indent=1))
ok = sum(1 for r in results if r.get("put") == 200 and r.get("commit") == 200)
print(f"UPLOADED {ok}/{len(FILES)}")
with open("ce_upload.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
