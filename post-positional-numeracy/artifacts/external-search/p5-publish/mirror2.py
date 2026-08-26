# -*- coding: utf-8 -*-
"""mirror2.py — RES.024: complete the R2 mirror to all 42 deposit files (reviewer SOFT-1)."""
import json, os, re, socket, ssl, subprocess, sys, time, urllib.parse, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
BUCKET = "qnfo-releases"
PREFIX = "2026/08/post-positional-numeracy/"

def resolve_ip(host):
    for i in range(6):
        try:
            return socket.getaddrinfo(host, 443, socket.AF_INET, socket.SOCK_STREAM)[0][4][0]
        except Exception:
            time.sleep(3 * (i + 1))
    out = subprocess.run(["nslookup", host, "8.8.8.8"], capture_output=True, text=True, timeout=30).stdout
    m = re.search(r"Addresses?:\s*([\d.]+)", out) or re.search(r"(\d+\.\d+\.\d+\.\d+)", out)
    if m:
        return m.group(1)
    raise RuntimeError("cannot resolve " + host)

def raw(host, path, method="GET", headers=None, data=None, tries=5):
    ip = resolve_ip(host)
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))
    h = {"User-Agent": UA, "Accept": "application/json", "Host": host}
    if headers:
        h.update(headers)
    url = "https://" + ip + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, method=method, headers=h)
            with opener.open(r, timeout=240) as resp:
                body = resp.read()
                try:
                    return resp.status, json.loads(body.decode("utf-8"))
                except Exception:
                    return resp.status, {"__text__": body.decode("utf-8", "replace")[:200]}
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    return -1, {"__error__": str(last)}

CT = {
    ".md": "text/markdown", ".html": "text/html", ".pdf": "application/pdf",
    ".json": "application/json", ".py": "text/plain", ".cjs": "text/plain",
    ".bib": "application/x-bibtex", ".log": "text/plain", ".txt": "text/plain",
    "LICENSE": "text/plain",
}

# flat deposit name -> repo-relative path (30 remaining files)
FILES = [
    ("docs_deep-research.md", "docs/deep-research.md"),
    ("docs_universal-ignorance-audit.md", "docs/universal-ignorance-audit.md"),
    ("docs_literature.md", "docs/literature.md"),
    ("artifacts_consilience-gate.md", "artifacts/consilience-gate.md"),
    ("artifacts_bayesian-evidential-weight.md", "artifacts/bayesian-evidential-weight.md"),
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
    ("upload-publish.py", "artifacts/external-search/p5-publish/upload-publish.py"),
    ("upload-publish.log", "artifacts/external-search/p5-publish/upload-publish.log"),
    ("publish-response.json", "artifacts/external-search/p5-publish/publish-response.json"),
    ("publish-v101-response.json", "artifacts/external-search/p5-publish/publish-v101-response.json"),
    ("version-fix-response.json", "artifacts/external-search/p5-publish/version-fix-response.json"),
    ("verify-newversion.json", "artifacts/external-search/p5-publish/verify-newversion.json"),
    ("verify-newversion.log", "artifacts/external-search/p5-publish/verify-newversion.log"),
    ("verify-published.json", "artifacts/external-search/p5-publish/verify-published.json"),
    ("verify-published.log", "artifacts/external-search/p5-publish/verify-published.log"),
    ("verify-and-newversion.py", "artifacts/external-search/p5-publish/verify-and-newversion.py"),
    ("fix-version.py", "artifacts/external-search/p5-publish/fix-version.py"),
    ("distribute.py", "artifacts/external-search/p5-publish/distribute.py"),
    ("distribution-log.json", "artifacts/external-search/p5-publish/distribution-log.json"),
]

ok = 0
for name, rel in FILES:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        print("SKIP (missing repo file):", name)
        continue
    data = open(path, "rb").read()
    ext = os.path.splitext(name)[1].lower()
    ct = CT.get(ext, "application/octet-stream")
    st, _ = raw("api.cloudflare.com",
                "/client/v4/accounts/%s/r2/buckets/%s/objects/%s" % (ACCT, BUCKET, urllib.parse.quote(PREFIX + name, safe="")),
                method="PUT", headers={"Authorization": "Bearer " + CF_TOKEN, "Content-Type": ct}, data=data)
    print("PUT", st, name)
    ok += 1 if st == 200 else 0

st, lst = raw("api.cloudflare.com",
              "/client/v4/accounts/%s/r2/buckets/%s/objects?prefix=%s" % (ACCT, BUCKET, urllib.parse.quote(PREFIX, safe="")),
              headers={"Authorization": "Bearer " + CF_TOKEN})
r2_keys = [o.get("key") for o in lst.get("result", [])] if isinstance(lst, dict) else []
print("MIRRORED", ok, "of", len(FILES), "| total objects under prefix:", len(r2_keys))
sys.exit(0 if len(r2_keys) >= 42 else 1)
