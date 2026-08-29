"""finalize-upload.py — draft 22160404: purge stray files (e.g. 'gitignore'), verify the
29-file set, publish, DOI-live, frontmatter assert, concept check, save info.
"""
import json, os, sys, time, urllib.request, urllib.error

TOKEN = os.environ["ZENODO_TOKEN"]
BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
DEP = "22160404"
EXPECTED = [
    "distinction-primitive-research-framework.md",
    "distinction-primitive-research-framework.html",
    "distinction-primitive-research-framework.pdf",
    "references.bib", "citation-audit.md", "PROJECT-PLAN.md", "README.md",
    "FRAMEWORK.md", "provenance.md", "claim-sheet.md", "level-legend.md",
    "gate-checklist.md", "verify-framework.py", "verify-output.txt",
    "uia-15q-res032.md",
    "f1-sweep-README.md", "f1-sweep-01-ump014.md", "f1-sweep-02-res021.md",
    "f1-sweep-03-res027.md", "f1-sweep-04-res028.md", "f1-sweep-05-res029.md",
    "f1-sweep-06-res030.md", "f1-sweep-07-res031.md",
    "external-verify.py", "external-verification-dprf-2026-08-29.json",
    "verification-deposit-framework.py", "verification-layout-verify.py",
    "verification-post-deposit-verify.py", "verification-deploy-framework.py",
]

def http(method, url, body=None, headers=None, tries=8):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=body, method=method, headers=headers or {})
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

AUTH = {"Authorization": f"Bearer {TOKEN}"}

# 1. list + purge strays
st, body = http("GET", f"{BASE}/deposit/depositions/{DEP}", headers=AUTH)
draft = json.loads(body)
names = [f.get("key") or f.get("filename") for f in draft.get("files", [])]
print("draft files:", len(names))
purged = 0
for f in draft.get("files", []):
    nm = f.get("key") or f.get("filename")
    if nm not in EXPECTED:
        st2, b2 = http("DELETE", f["links"]["self"], headers=AUTH)
        print("purged", nm, st2)
        purged += 1
st, body = http("GET", f"{BASE}/deposit/depositions/{DEP}", headers=AUTH)
draft = json.loads(body)
names = [f.get("key") or f.get("filename") for f in draft.get("files", [])]
print("after purge:", len(names), "purged:", purged)
missing = [n for n in EXPECTED if n not in names]
assert not missing, f"missing: {missing}"
assert len(names) == len(EXPECTED), f"count {len(names)} != {len(EXPECTED)}"
print("FILE-SET OK (29/29)")

# 2. placeholder check
for rel in ["distinction-primitive-research-framework.md",
            "distinction-primitive-research-framework.html",
            "distinction-primitive-research-framework.pdf"]:
    if "<RESERVED>" in open(os.path.join(PROJ, rel), encoding="utf-8", errors="ignore").read():
        sys.exit("PLACEHOLDER in " + rel)
print("PLACEHOLDER-CHECK: clean")

# 3. publish
st, body = http("POST", f"{BASE}/deposit/depositions/{DEP}/actions/publish",
                headers={**AUTH, "Content-Type": "application/json"}, body=b"{}")
if st != 202:
    print("PUBLISH-FAIL", st, body[:300]); sys.exit(1)
rec = json.loads(body)
recdoi = rec.get("doi")
concept = rec.get("conceptrecid")
print("PUBLISHED", recdoi, "conceptrecid", concept)
assert concept == 22159887, f"CONCEPT CHANGED: {concept}"

# 4. DOI live
rr = 0
for i in range(6):
    try:
        req = urllib.request.Request(f"https://doi.org/{recdoi}", method="HEAD")
        with urllib.request.urlopen(req, timeout=60) as r:
            rr = r.status
        if rr == 200:
            break
    except Exception:
        time.sleep(5)
print("DOI-LIVE:", rr)

# 5. POST-PUBLISH-FRONTMATTER-ASSERT
st, body = http("GET", f"{BASE}/records/{recdoi.split('/')[-1]}", headers={})
rec2 = json.loads(body)
mdl = [f for f in rec2["files"] if f["key"] == "distinction-primitive-research-framework.md"][0]
st, body = http("GET", mdl["links"]["self"])
dep_md = body.decode("utf-8")
assert f'doi: "{recdoi}"' in dep_md, "deposited .md frontmatter doi mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT: PASS")
print("RECORD FILES:", len(rec2["files"]))

json.dump({"record": recdoi, "conceptrecid": concept, "concept_doi": "10.5281/zenodo.22159887",
           "files": len(rec2["files"]), "version": "0.2"},
          open(os.path.join(PROJ, "deposit-info-v02.json"), "w"), indent=2)
print("DONE")
