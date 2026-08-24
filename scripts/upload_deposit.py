#!/usr/bin/env python3
"""upload_deposit.py — upload publication files to a Zenodo deposit bucket.

Method: bucket-level PUT with access_token query param, application/octet-stream
(ZENODO-BUCKET-PUT-415-1: text/* Content-Type -> 415; octet-stream works).
Keys are percent-encoded (quote(key, safe='')). Verified by re-fetching size.
"""
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEP_ID = sys.argv[1]
FILES = [line.strip() for line in sys.stdin if line.strip()]

with open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8") as f:
    TOKEN = f.read().strip()

# fetch bucket from deposit
req = urllib.request.Request(
    f"https://zenodo.org/api/deposit/depositions/{DEP_ID}",
    headers={"Authorization": f"Bearer {TOKEN}"})
with urllib.request.urlopen(req) as resp:
    dep = json.load(resp)
BUCKET = dep["links"]["bucket"]

ok, fail = [], []
for rel in FILES:
    p = Path(rel)
    key = urllib.parse.quote(p.name, safe="")
    url = f"{BUCKET}/{key}?access_token={TOKEN}"
    data = p.read_bytes()
    r = urllib.request.Request(url, data=data, method="PUT",
                               headers={"Content-Type": "application/octet-stream"})
    try:
        with urllib.request.urlopen(r) as resp:
            body = json.load(resp)
        got = body.get("size")
        ok.append((p.name, got))
        print(f"OK {p.name} ({got})")
    except Exception as exc:  # noqa: BLE001
        fail.append((p.name, str(exc)))
        print(f"FAIL {p.name}: {exc}")

print(f"UPLOADED {len(ok)}/{len(ok) + len(fail)}")
if fail:
    print("FAILURES:", fail)
    sys.exit(1)
