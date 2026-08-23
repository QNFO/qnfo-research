#!/usr/bin/env python3
"""P6: R2 mirror of the published deposit (R2-MIRROR-AFTER-PUBLISH-1).
Mirrors the 37 deposited files byte-identical from Zenodo to
qnfo-releases/2026/08/ultrametric-program/ via the Cloudflare REST API."""
import json
import os
import urllib.parse
import urllib.request

ZTOKEN = open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
CFTOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
ACCOUNT = "edb167b78c9fb901ea5bca3ce58ccc4b"
BUCKET = "qnfo-releases"
PREFIX = "2026/08/ultrametric-program"
RECORD_ID = 22072162
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36 qnfo-audit"}

def get(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read()

st, body = get(f"https://zenodo.org/api/records/{RECORD_ID}")
record = json.loads(body)
files = record.get("files", [])
print("DEPOSIT FILES:", len(files))

results = []
for f in files:
    fname = f["key"]
    fsize = f.get("size")
    fmd5 = f.get("checksum", "").replace("md5:", "")
    st, data = get(f"https://zenodo.org/api/records/{RECORD_ID}/files/{urllib.parse.quote(fname)}/content")
    if st != 200 or len(data) != fsize:
        results.append({"file": fname, "stage": "download", "status": st, "size": len(data), "expected": fsize})
        continue
    key = f"{PREFIX}/{fname}"
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/r2/buckets/{BUCKET}/objects/{urllib.parse.quote(key, safe='')}"
    req = urllib.request.Request(url, data=data, method="PUT",
                                 headers={"Authorization": f"Bearer {CFTOKEN}",
                                          "Content-Type": "application/octet-stream"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            put_st = r.status
    except Exception as e:
        results.append({"file": fname, "stage": "put", "error": str(e)[:200]})
        continue
    results.append({"file": fname, "size": fsize, "md5": fmd5, "put": put_st, "bytes": len(data)})

print(json.dumps(results, indent=1))
ok = sum(1 for r in results if r.get("put") == 200)
print(f"MIRRORED {ok}/{len(files)}")
with open("artifacts/verification/p6_r2_mirror.json", "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
