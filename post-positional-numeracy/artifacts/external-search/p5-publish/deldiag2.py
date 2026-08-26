# -*- coding: utf-8 -*-
"""deldiag2.py — compare deposit-API vs records-API file lists for draft 22114495; test deletes."""
import json, os, sys, time, urllib.request

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

def req(method, path, raw=None, tries=4):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": BASE + "/", "Origin": BASE,
         "Authorization": "Bearer " + TOKEN}
    for i in range(tries):
        try:
            r = urllib.request.Request(BASE + path, data=raw, method=method, headers=h)
            with urllib.request.urlopen(r, timeout=120) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8") if e.fp else b"{}")
        except Exception as e:
            if i == tries - 1:
                return -1, {"__error__": "%s: %s" % (type(e).__name__, e)}
            time.sleep(2 * (i + 1))

# deposit-API list
st1, d1 = req("GET", "/api/deposit/depositions/22114495/files")
dep_names = sorted((f.get("filename") or f.get("key")) for f in d1) if isinstance(d1, list) else []
print("DEPOSIT-API", st1, len(dep_names))
for n in dep_names:
    print("  D", n)

# records-API list
st2, d2 = req("GET", "/api/records/22114495/draft/files")
if isinstance(d2, dict) and "entries" in d2:
    entries = d2["entries"]
else:
    entries = d2 if isinstance(d2, list) else []
rec_names = sorted(e.get("key") for e in entries)
print("RECORDS-API", st2, len(rec_names))
for n in rec_names:
    print("  R", n)

print("ONLY-DEPOSIT:", sorted(set(dep_names) - set(rec_names)))
print("ONLY-RECORDS:", sorted(set(rec_names) - set(dep_names)))
