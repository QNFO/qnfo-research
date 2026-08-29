"""post-publish-v02.py — verify record 22160404: DOI live, frontmatter assert, file count,
write deposit-info-v02.json."""
import json, os, sys, time, urllib.request, urllib.error

BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
REC = "22160404"
RECDOI = f"10.5281/zenodo.{REC}"

def http(method, url, headers=None, tries=8):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, method=method, headers=headers or {})
            with urllib.request.urlopen(req, timeout=240) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < 7:
                time.sleep(4 + 3 * i)
                continue
            return e.code, e.read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(3 + 2 * i)

rr = 0
for i in range(6):
    try:
        req = urllib.request.Request(f"https://doi.org/{RECDOI}", method="HEAD")
        with urllib.request.urlopen(req, timeout=60) as r:
            rr = r.status
        if rr == 200:
            break
    except Exception:
        time.sleep(5)
print("DOI-LIVE:", rr)
assert rr == 200

st, body = http("GET", f"{BASE}/records/{REC}")
rec = json.loads(body)
print("title:", rec["metadata"]["title"][:60])
print("version:", rec["metadata"].get("version"), "| conceptrecid:", rec.get("conceptrecid"))
print("files:", len(rec["files"]))
mdl = [f for f in rec["files"] if f["key"] == "distinction-primitive-research-framework.md"][0]
st, body = http("GET", mdl["links"]["self"])
dep_md = body.decode("utf-8")
assert f'doi: "{RECDOI}"' in dep_md, "frontmatter mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT: PASS")
keys = [f["key"] for f in rec["files"]]
print("has refs:", "references.bib" in keys, "| has uia:", "uia-15q-res032.md" in keys,
      "| has f1:", any(k.startswith("f1-sweep-") for k in keys),
      "| has external:", "external-verification-dprf-2026-08-29.json" in keys)

json.dump({"record": RECDOI, "conceptrecid": int(rec.get("conceptrecid") or 22159887),
           "concept_doi": "10.5281/zenodo.22159887", "files": len(rec["files"]), "version": "0.2"},
          open(os.path.join(PROJ, "deposit-info-v02.json"), "w"), indent=2)
print("DONE")
