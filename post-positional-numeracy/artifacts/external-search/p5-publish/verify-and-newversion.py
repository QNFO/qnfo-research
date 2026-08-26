# -*- coding: utf-8 -*-
"""verify-and-newversion.py — QNFO.RES.024: verify v1.0.0 live, create v1.0.1 newversion, reserve DOI."""
import json, os, urllib.request

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

def get(url, auth=True, data=None, method=None):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": BASE + "/", "Origin": BASE}
    if auth:
        h["Authorization"] = "Bearer " + TOKEN
    r = urllib.request.Request(url, data=data, method=method, headers=h)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

out = {}

# 1. verify v1.0.0
st, rec = get(BASE + "/api/records/22114389")
out["v100_records"] = {"status": st, "state": rec.get("state"), "doi": rec.get("doi"),
                       "nfiles": len(rec.get("files", [])),
                       "files": [f.get("key") for f in rec.get("files", [])]}
print("V1.0.0 RECORDS", st, rec.get("state"), rec.get("doi"), "files:", len(rec.get("files", [])))

st, dc = get("https://api.datacite.org/dois/10.5281/zenodo.22114389", auth=False)
out["v100_datacite"] = {"status": st, "state": (dc.get("data", {}).get("attributes", {}) or {}).get("state")}
print("V1.0.0 DATACITE", st, (dc.get("data", {}).get("attributes", {}) or {}).get("state"))

# 2. newversion draft
st, nv = get(BASE + "/api/deposit/depositions/22114389/actions/newversion", data=b"", method="POST")
out["newversion"] = {"status": st, "draft_id": nv.get("id"), "draft_doi": nv.get("doi")}
print("NEWVERSION", st, "draft:", nv.get("id"))
if st not in (200, 201):
    print(json.dumps(nv)[:600])
    raise SystemExit(1)
draft = nv["id"]

# 3. reserve v1.0.1 DOI via records API
st2, r2 = get(BASE + "/api/records/%s/draft/pids/doi" % draft, data=b"", method="POST")
out["reserve"] = {"status": st2, "doi": r2.get("doi") if isinstance(r2, dict) else r2}
print("RESERVE", st2, r2.get("doi") if isinstance(r2, dict) else r2)

with open(os.path.join(HERE, "verify-newversion.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("WROTE verify-newversion.json")
