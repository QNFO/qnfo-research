# -*- coding: utf-8 -*-
"""upload-publish.py — QNFO.RES.024: upload full source set + publish (2026-08-26).

Deposit API multipart upload (ZENODO-UPLOAD-MULTIPART-1: POST /files with name+file fields);
publish via POST /actions/publish. Evidence saved to this directory.
"""
import json, os, sys, time, urllib.request

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
DEPOSIT = 22114389

FILES = [
    ("post-positional-numeracy.md", "post-positional-numeracy.md"),
    ("post-positional-numeracy.html", "post-positional-numeracy.html"),
    ("post-positional-numeracy.pdf", "post-positional-numeracy.pdf"),
    ("references.bib", "references.bib"),
    ("citation-audit.md", "citation-audit.md"),
    ("PROJECT-PLAN.md", "PROJECT-PLAN.md"),
    ("README.md", "README.md"),
    ("LICENSE", "LICENSE"),
    ("docs/deep-research.md", "docs/deep-research.md"),
    ("docs/universal-ignorance-audit.md", "docs/universal-ignorance-audit.md"),
    ("docs/literature.md", "docs/literature.md"),
    ("artifacts/consilience-gate.md", "artifacts/consilience-gate.md"),
    ("artifacts/bayesian-evidential-weight.md", "artifacts/bayesian-evidential-weight.md"),
    ("corpus-sweep-2026-08-26.json", "artifacts/external-search/corpus-sweep-2026-08-26.json"),
    ("arxiv-sweeps-2026-08-26.json", "artifacts/external-search/arxiv-sweeps-2026-08-26.json"),
    ("adjudication-memory-2026-08-26.json", "artifacts/external-search/adjudication-memory-2026-08-26.json"),
    ("hensel-audit-z20756222.json", "artifacts/external-search/hensel-v120-audit/z20756222.json"),
    ("hensel-audit-paper.md", "artifacts/external-search/hensel-v120-audit/hensel_paper.md"),
    ("hensel-audit-source.py", "artifacts/external-search/hensel-v120-audit/hensel_system.py"),
    ("p2-literature-sweep.json", "artifacts/external-search/p2-literature/p2-literature-sweep.json"),
    ("p2-literature-sweep.py", "artifacts/external-search/p2-literature/sweep.py"),
    ("p5-create-deposit.py", "artifacts/external-search/p5-publish/create-deposit.py"),
    ("p5-deposit-create.json", "artifacts/external-search/p5-publish/deposit-create.json"),
    ("p5-deposit-reserve-doi.json", "artifacts/external-search/p5-publish/deposit-reserve-doi.json"),
    ("p5-run.log", "artifacts/external-search/p5-publish/run.log"),
    ("verify_ppn.py", "artifacts/verification/verify_ppn.py"),
    ("ppn-verification-results.json", "artifacts/verification/ppn-verification-results.json"),
    ("run-verification.log", "artifacts/verification/run-verification.log"),
    ("check_rendering.py", "artifacts/verification/check_rendering.py"),
    ("render-pdf.cjs", "artifacts/verification/render-pdf.cjs"),
]

def json_req(method, path, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    r = urllib.request.Request(BASE + path, data=data, method=method, headers={
        "User-Agent": UA, "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9", "Referer": BASE + "/", "Origin": BASE,
        "Authorization": "Bearer " + TOKEN, "Content-Type": "application/json",
    })
    with urllib.request.urlopen(r, timeout=120) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

def upload(name, relpath):
    fpath = os.path.join(ROOT, relpath)
    with open(fpath, "rb") as f:
        content = f.read()
    boundary = "----qnfo%x" % int(time.time() * 1000)
    body = b""
    body += ("--%s\r\n" % boundary).encode()
    body += ('Content-Disposition: form-data; name="name"\r\n\r\n%s\r\n' % name).encode()
    body += ("--%s\r\n" % boundary).encode()
    body += ('Content-Disposition: form-data; name="file"; filename="%s"\r\n' % name).encode()
    body += b"Content-Type: application/octet-stream\r\n\r\n"
    body += content + b"\r\n"
    body += ("--%s--\r\n" % boundary).encode()
    r = urllib.request.Request(BASE + "/api/deposit/depositions/%s/files" % DEPOSIT,
                               data=body, method="POST", headers={
        "User-Agent": UA, "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9", "Referer": BASE + "/", "Origin": BASE,
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "multipart/form-data; boundary=%s" % boundary,
    })
    with urllib.request.urlopen(r, timeout=180) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

results = {}
for name, relpath in FILES:
    try:
        st, body = upload(name, relpath)
    except Exception as e:
        st, body = -1, {"__error__": "%s: %s" % (type(e).__name__, e)}
    results[name] = {"status": st, "id": body.get("id") if isinstance(body, dict) else None,
                     "size": body.get("size") if isinstance(body, dict) else None,
                     "error": body.get("__error__") if isinstance(body, dict) else None}
    print("UPLOAD", st, name, results[name].get("size"))
    time.sleep(0.4)

failed = [n for n, v in results.items() if v["status"] not in (200, 201)]
if failed:
    print("UPLOAD FAILURES:", failed)
    sys.exit(1)

st, pub = json_req("POST", "/api/deposit/depositions/%s/actions/publish" % DEPOSIT)
with open(os.path.join(HERE, "publish-response.json"), "w", encoding="utf-8") as f:
    json.dump({"status": st, "body": pub}, f, indent=1, ensure_ascii=False)
print("PUBLISH", st, "doi:", pub.get("doi"))
