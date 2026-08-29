"""post-deposit-verify.py — POST-PUBLISH-FRONTMATTER-ASSERT + DEPOSIT-LAYOUT-VERIFY + info save.
Record: 10.5281/zenodo.22159888, concept 10.5281/zenodo.22159887, conceptrecid 22159887.
"""
import json, os, subprocess, sys, urllib.request, zipfile, io

REC = "22159888"
DOI = "10.5281/zenodo.22159888"
CONCEPT_DOI = "10.5281/zenodo.22159887"
BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
UA = {"User-Agent": "Mozilla/5.0 (QNFO deposit verify)"}

def get(url):
    r = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(r, timeout=180).read()

# 1. POST-PUBLISH-FRONTMATTER-ASSERT-1
md = get(f"{BASE}/records/{REC}/files/distinction-primitive-research-framework.md").decode("utf-8")
assert f'doi: "{DOI}"' in md, "deposited .md frontmatter doi mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT-1: PASS")

# 2. DEPOSIT-LAYOUT-VERIFY-1: download the full archive, extract, re-run the verification suite
zb = get(f"{BASE}/records/{REC}/files-archive")
zf = zipfile.ZipFile(io.BytesIO(zb))
stage = os.path.join(PROJ, "artifacts", "verification", "layout-check")
os.makedirs(stage, exist_ok=True)
zf.extractall(stage)
names = zf.namelist()
assert "verify-framework.py" in names and "references.bib" in names
out = subprocess.run([sys.executable, os.path.join(stage, "verify-framework.py")],
                     capture_output=True, text=True, cwd=stage)
print("DEPOSIT-LAYOUT-VERIFY-1: verify exit", out.returncode)
print(out.stdout.strip().splitlines()[-1])
assert out.returncode == 0
print("archive files:", len(names))
json.dump({"doi": DOI, "concept_doi": CONCEPT_DOI, "conceptrecid": 22159887,
           "files": len(names), "layout_verify": "PASS"},
          open(os.path.join(PROJ, "deposit-info.json"), "w"), indent=2)
print("DONE")
