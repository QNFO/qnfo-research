# -*- coding: utf-8 -*-
"""publish_res027.py — QNFO.RES.027 P8: verify deposit state, then publish (2026-08-27)."""
import json, os, time, urllib.request, urllib.error

TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
BASE = "https://zenodo.org"
HERE = os.path.dirname(os.path.abspath(__file__))
DEP = "22123068"

def req(method, path, body=None, tries=6):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(BASE + path, data=data, method=method, headers={
                "User-Agent": UA, "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": BASE + "/", "Origin": BASE,
                "Authorization": "Bearer " + TOKEN,
                "Content-Type": "application/json",
            })
            with urllib.request.urlopen(r, timeout=60) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                last = (e.code, json.loads(e.read().decode("utf-8")))
            except Exception:
                last = (e.code, str(e))
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            return e.code, last[1]
        except Exception as e:
            last = ("NET", str(e))
            time.sleep(3 + 4 * i)
    return (0, last)

def save(name, obj):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)

# 1. verify pre-publish state
st, d = req("GET", "/api/deposit/depositions/%s" % DEP)
save("pre-publish-state.json", {"status": st, "body": d})
files = [f.get("filename") for f in d.get("files", [])]
md = d.get("metadata", {})
print("PRE-PUBLISH", st, "files:", len(files), "| title ok:", md.get("title", "").startswith("Quantum Statistics"),
      "| license:", md.get("license"), "| version:", md.get("version"),
      "| rel_ids:", len(md.get("related_identifiers", [])),
      "| creators:", [(c.get("name")) for c in md.get("creators", [])])
print("  sample files:", sorted(files)[:6], "...")
if len(files) < 40:
    print("FILE-COUNT-ANOMALY: expected >=40, got", len(files))

# 2. publish
st2, d2 = req("POST", "/api/deposit/depositions/%s/actions/publish" % DEP)
save("publish-result.json", {"status": st2, "body": d2})
print("PUBLISH", st2, "| doi:", d2.get("doi"), "| concept:", d2.get("conceptdoi") if isinstance(d2, dict) else "?")
