"""layout-verify.py — DEPOSIT-LAYOUT-VERIFY-1: download all deposited files via record links,
extract, re-run the verification suite from the deposited layout. Saves deposit-info.json."""
import json, os, subprocess, sys, urllib.request

REC = "22159888"
DOI = "10.5281/zenodo.22159888"
CONCEPT_DOI = "10.5281/zenodo.22159887"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0"}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()

rec = json.loads(get(f"https://zenodo.org/api/records/{REC}").decode())
stage = os.path.join(PROJ, "artifacts", "verification", "layout-check")
os.makedirs(stage, exist_ok=True)
for f in rec["files"]:
    data = get(f["links"]["self"])
    out = os.path.join(stage, f["key"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "wb").write(data)
print("downloaded files:", len(rec["files"]))

out = subprocess.run([sys.executable, os.path.join(stage, "verify-framework.py")],
                     capture_output=True, text=True, cwd=stage)
print("layout verify exit:", out.returncode, "|", out.stdout.strip().splitlines()[-1])
assert out.returncode == 0

json.dump({"doi": DOI, "concept_doi": CONCEPT_DOI, "conceptrecid": 22159887,
           "files": len(rec["files"]), "layout_verify": "PASS",
           "frontmatter_assert": "PASS"},
          open(os.path.join(PROJ, "deposit-info.json"), "w"), indent=2)
print("DONE")
