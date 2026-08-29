"""resume-upload.py — continue v0.2 newversion (draft 22160404) after the POST /files 400.
Uploads the 29-file set via bucket PUT (?access_token=), then placeholder check, publish,
DOI-live verify, frontmatter assert, concept check, save deposit-info-v02.json.
"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request

TOKEN = os.environ["ZENODO_TOKEN"]
BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
DEP = "22160404"
DOI = f"10.5281/zenodo.{DEP}"

FILES = [
    ("distinction-primitive-research-framework.md", "distinction-primitive-research-framework.md"),
    ("distinction-primitive-research-framework.html", "distinction-primitive-research-framework.html"),
    ("distinction-primitive-research-framework.pdf", "distinction-primitive-research-framework.pdf"),
    ("references.bib", "references.bib"),
    ("citation-audit.md", "citation-audit.md"),
    ("PROJECT-PLAN.md", "PROJECT-PLAN.md"),
    ("README.md", "README.md"),
    ("FRAMEWORK.md", "FRAMEWORK.md"),
    ("docs/provenance.md", "provenance.md"),
    ("templates/claim-sheet.md", "claim-sheet.md"),
    ("templates/level-legend.md", "level-legend.md"),
    ("templates/gate-checklist.md", "gate-checklist.md"),
    ("artifacts/verification/verify-framework.py", "verify-framework.py"),
    ("artifacts/verification/verify-output.txt", "verify-output.txt"),
    ("docs/uia-15q-res032.md", "uia-15q-res032.md"),
    ("docs/f1-sweep/README.md", "f1-sweep-README.md"),
    ("docs/f1-sweep/01-ump014.md", "f1-sweep-01-ump014.md"),
    ("docs/f1-sweep/02-res021.md", "f1-sweep-02-res021.md"),
    ("docs/f1-sweep/03-res027.md", "f1-sweep-03-res027.md"),
    ("docs/f1-sweep/04-res028.md", "f1-sweep-04-res028.md"),
    ("docs/f1-sweep/05-res029.md", "f1-sweep-05-res029.md"),
    ("docs/f1-sweep/06-res030.md", "f1-sweep-06-res030.md"),
    ("docs/f1-sweep/07-res031.md", "f1-sweep-07-res031.md"),
    ("artifacts/external-search/external-verify.py", "external-verify.py"),
    ("artifacts/external-search/external-verification-dprf-2026-08-29.json", "external-verification-dprf-2026-08-29.json"),
    ("artifacts/verification/deposit-framework.py", "verification-deposit-framework.py"),
    ("artifacts/verification/layout-verify.py", "verification-layout-verify.py"),
    ("artifacts/verification/post-deposit-verify.py", "verification-post-deposit-verify.py"),
    ("artifacts/verification/deploy-framework.py", "verification-deploy-framework.py"),
]

def http(method, url, body=None, headers=None, tries=8):
    last = None
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
            last = e
            time.sleep(3 + 2 * i)
    raise RuntimeError(f"http failed: {last}")

# 1. bucket link
st, body = http("GET", f"{BASE}/deposit/depositions/{DEP}",
                headers={"Authorization": f"Bearer {TOKEN}"})
draft = json.loads(body)
bucket = draft["links"]["bucket"]
print("bucket:", bucket)

# 2. upload each file via bucket PUT
for rel, name in FILES:
    data = open(os.path.join(PROJ, rel), "rb").read()
    url = f"{bucket}/{urllib.parse.quote(name)}?access_token={urllib.parse.quote(TOKEN)}"
    st, body = http("PUT", url, body=data,
                    headers={"Content-Type": "application/octet-stream"})
    if st not in (200, 201):
        print("UPLOAD-FAIL", name, st, body[:200])
        sys.exit(1)
print("UPLOADED", len(FILES), "via bucket PUT")

# 3. verify file count in draft
st, body = http("GET", f"{BASE}/deposit/depositions/{DEP}",
                headers={"Authorization": f"Bearer {TOKEN}"})
draft = json.loads(body)
print("draft files:", len(draft.get("files", [])), "->", [f.get("key") or f.get("filename") for f in draft.get("files", [])][:5], "...")
assert len(draft.get("files", [])) == len(FILES), "file count mismatch"

# 4. placeholder check
for rel, _ in FILES:
    if "<RESERVED>" in open(os.path.join(PROJ, rel), encoding="utf-8", errors="ignore").read():
        sys.exit("PLACEHOLDER FOUND in " + rel)
print("PLACEHOLDER-CHECK: clean")

# 5. publish
st, body = http("POST", f"{BASE}/deposit/depositions/{DEP}/actions/publish",
                headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
                body=b"{}")
if st != 202:
    print("PUBLISH-FAIL", st, body[:300])
    sys.exit(1)
rec = json.loads(body)
recdoi = rec.get("doi")
concept = rec.get("conceptrecid")
print("PUBLISHED", recdoi, "conceptrecid", concept)
assert concept == 22159887, f"CONCEPT CHANGED: {concept}"

# 6. DOI live
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

# 7. POST-PUBLISH-FRONTMATTER-ASSERT
st, body = http("GET", f"{BASE}/records/{recdoi.split('/')[-1]}", headers={})
rec2 = json.loads(body)
mdl = [f for f in rec2["files"] if f["key"] == "distinction-primitive-research-framework.md"][0]
st, body = http("GET", mdl["links"]["self"])
dep_md = body.decode("utf-8")
assert f'doi: "{recdoi}"' in dep_md, "deposited .md frontmatter doi mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT: PASS")
print("FILES:", len(rec2["files"]))

json.dump({"record": recdoi, "conceptrecid": concept, "concept_doi": "10.5281/zenodo.22159887",
           "files": len(rec2["files"]), "version": "0.2"},
          open(os.path.join(PROJ, "deposit-info-v02.json"), "w"), indent=2)
print("DONE")
