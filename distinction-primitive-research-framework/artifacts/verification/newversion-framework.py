"""newversion-framework.py — QNFO.RES.032 v0.2 newversion deposit.
Fixes shipped in v0.2: expanded citations (build-pdf.py references.bib root-cause fix),
single title (FRONTMATTER-DUPLICATION-1), RES.031 added to bib (seven records),
P1 adjudications + UIA + F1-sweep + external-search evidence files included.
Flow: newversion draft -> frontmatter DOI patch -> rebuild HTML/PDF -> metadata v0.2 ->
delete carried files (per-file links.self, ZENODO-DEPOSIT-DELETE-500-1) -> upload 29-file
set -> placeholder check -> publish -> verify DOI live + frontmatter assert + concept
unchanged -> save deposit-info-v02.json. RUN ONCE.
"""
import json, os, subprocess, sys, time, requests

TOKEN = os.environ["ZENODO_TOKEN"]
BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
BUILDPDF = r"C:\Users\LENOVO\.deepchat\cdp-pipeline\build-pdf.py"
H = {"Authorization": f"Bearer {TOKEN}"}
OLD_DOI = "10.5281/zenodo.22159888"

RESUME_DEP = None
if "--draft" in sys.argv:
    RESUME_DEP = sys.argv[sys.argv.index("--draft") + 1]

# (local path relative to PROJ, flat upload name)
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

def api(method, path, **kw):
    last = None
    for i in range(8):
        try:
            r = requests.request(method, BASE + path, headers=H, timeout=240, **kw)
            if r.status_code in (429, 500, 502, 503) and i < 7:
                time.sleep(4 + 3 * i)
                continue
            return r
        except Exception as e:
            last = e
            time.sleep(3 + 2 * i)
    raise RuntimeError(f"api failed: {last}")

# 1. newversion draft from the published record (skip when resuming)
if RESUME_DEP:
    dep = RESUME_DEP
    doi = f"10.5281/zenodo.{dep}"
    d = {}
    print("RESUME draft", dep, "DOI", doi)
else:
    r = api("POST", "/deposit/depositions/22159888/actions/newversion", json={})
    r.raise_for_status()
    d = r.json()
    dep = d["id"]
    doi = (d.get("metadata", {}).get("prereserve_doi") or {}).get("doi") or f"10.5281/zenodo.{dep}"
    print("NEWVERSION-DRAFT", dep, "DOI", doi)

    # 2. patch frontmatter doi (NEWVERSION-FRONTMATTER-CARRYOVER-1)
    mdp = os.path.join(PROJ, FILES[0][0])
    md = open(mdp, encoding="utf-8").read()
    assert OLD_DOI in md, "old DOI not found in frontmatter"
    md = md.replace(f'doi: "{OLD_DOI}"', f'doi: "{doi}"', 1)
    open(mdp, "w", encoding="utf-8").write(md)
    print("FRONTMATTER patched:", doi)

# 3. rebuild HTML + PDF from patched source (build-pdf.py now finds references.bib)
os.chdir(PROJ)
r = subprocess.run([sys.executable, BUILDPDF, "distinction-primitive-research-framework"],
                   capture_output=True, text=True, timeout=600)
print("BUILDPDF-RC:", r.returncode)
print(r.stdout[-400:])
if r.returncode != 0:
    sys.exit(1)
print("REBUILT ok")

# 4. metadata v0.2 (seven records in description)
desc = ("The QNFO arithmetic-physics program connects number-theoretic structure to "
        "statistical mechanics: prime-indexed modes with logarithmic energies yield partition "
        "functions that are exactly zeta objects, and hierarchy distance is a "
        "realization-independent ultrametric. This record states the methodological discipline "
        "those results share, as a reusable framework: a nine-level construction ladder from the "
        "primitive of distinction to the empirical filter of physics; two boundary rules (no "
        "uncommitted reification of the primitive; no isomorphism passes as a physical "
        "realization without a stated measurement protocol, null model, and falsification "
        "condition); and a compact claim record with mechanical demotion rules. The framework "
        "makes no empirical claims of its own; it systematizes discipline distributed across "
        "seven published QNFO records (cited) and states its one claim - ladder coverage of the "
        "published lineage - together with its falsification protocol. The deposited verification "
        "suite exhaustively checks the framework's mechanical content and reproduces the "
        "underlying zeta identities numerically. Version 0.2 carries the adjudicated level "
        "assignments and the prior-art verification of the boundary rules.")
meta = {
    "title": "Distinction, Number, and the Empirical Filter: The Pre-Arithmetic Research Framework",
    "upload_type": "publication",
    "publication_type": "preprint",
    "description": desc,
    "creators": [{"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO"}],
    "license": "cc-by-4.0",
    "access_right": "open",
    "keywords": ["distinction", "pre-arithmetic", "ultrametric", "zeta function",
                 "primon gas", "map-territory", "falsification", "research framework",
                 "philosophy of physics", "number theory"],
    "version": "0.2",
    "related_identifiers": [{
        "scheme": "url", "relation": "issupplementto",
        "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/distinction-primitive-research-framework",
    }],
}
r = api("PUT", f"/deposit/depositions/{dep}", json={"metadata": meta})
r.raise_for_status()
print("METADATA v0.2 ok")

# 5. delete carried-over files (per-file links.self; key may be 'key' or 'filename')
rd = api("GET", f"/deposit/depositions/{dep}")
rd.raise_for_status()
carried = rd.json().get("files", [])
for f in carried:
    r = api("DELETE", f["links"]["self"])
    if r.status_code not in (204, 200, 404):
        print("delete warn", f.get("key") or f.get("filename"), r.status_code)
print("carried files deleted:", len(carried))

# 6. upload the 29-file set
for rel, name in FILES:
    with open(os.path.join(PROJ, rel), "rb") as fh:
        data = fh.read()
    r = api("POST", f"/deposit/depositions/{dep}/files",
            data={"name": name}, files={"file": (name, data)})
    r.raise_for_status()
print("UPLOADED", len(FILES))

# 7. placeholder check (ZENODO-PLACEHOLDER-DOI-1)
for rel, _ in FILES:
    p = os.path.join(PROJ, rel)
    if "<RESERVED>" in open(p, encoding="utf-8", errors="ignore").read():
        sys.exit("PLACEHOLDER FOUND in " + rel)
print("PLACEHOLDER-CHECK: clean")

# 8. publish
r = api("POST", f"/deposit/depositions/{dep}/actions/publish")
r.raise_for_status()
rec = r.json()
recdoi = rec.get("doi")
concept = rec.get("conceptrecid")
print("PUBLISHED", recdoi, "conceptrecid", concept)
assert concept == 22159887, f"CONCEPT CHANGED: {concept}"

# 9. DOI live
for i in range(6):
    try:
        rr = requests.head(f"https://doi.org/{recdoi}", allow_redirects=True, timeout=60)
        if rr.status_code == 200:
            break
    except Exception:
        time.sleep(5)
print("DOI-LIVE:", rr.status_code)

# 10. POST-PUBLISH-FRONTMATTER-ASSERT (deposited .md via record links.self)
r = requests.get(f"{BASE}/records/{recdoi.split('/')[-1]}", timeout=180)
r.raise_for_status()
rec2 = r.json()
mdl = [f for f in rec2["files"] if f["key"] == "distinction-primitive-research-framework.md"][0]
dep_md = requests.get(mdl["links"]["self"], timeout=240).content.decode("utf-8")
assert f'doi: "{recdoi}"' in dep_md, "deposited .md frontmatter doi mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT: PASS")
print("FILES:", len(rec2["files"]))

json.dump({"record": recdoi, "conceptrecid": concept, "concept_doi": "10.5281/zenodo.22159887",
           "files": len(rec2["files"]), "version": "0.2"},
          open(os.path.join(PROJ, "deposit-info-v02.json"), "w"), indent=2)
print("DONE")
