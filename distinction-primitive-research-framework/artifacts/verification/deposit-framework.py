"""deposit-framework.py — Zenodo deposit for QNFO.RES.032 v0.1 (distinction-primitive-research-framework).
Retry-hardened (DNS flakiness + 429/5xx), publishes, verifies DOI, asserts deposited frontmatter,
saves deposit-info.json. RUN ONCE (idempotency not guaranteed past publish).
"""
import json, os, subprocess, sys, time, requests

TOKEN = os.environ["ZENODO_TOKEN"]
BASE = "https://zenodo.org/api"
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
PANDOC = r"C:\Users\LENOVO\AppData\Local\Pandoc\pandoc.exe"
BUILDPDF = r"C:\Users\LENOVO\.deepchat\cdp-pipeline\build-pdf.py"
H = {"Authorization": f"Bearer {TOKEN}"}

FILES = [
    "distinction-primitive-research-framework.md",
    "distinction-primitive-research-framework.html",
    "distinction-primitive-research-framework.pdf",
    "references.bib",
    "citation-audit.md",
    "PROJECT-PLAN.md",
    "README.md",
    "FRAMEWORK.md",
    "docs/provenance.md",
    "templates/claim-sheet.md",
    "templates/level-legend.md",
    "templates/gate-checklist.md",
    "artifacts/verification/verify-framework.py",
    "artifacts/verification/verify-output.txt",
    ".gitignore",
]

def api(method, path, **kw):
    last = None
    for i in range(8):
        try:
            r = requests.request(method, BASE + path, headers=H, timeout=180, **kw)
            if r.status_code in (429, 500, 502, 503) and i < 7:
                time.sleep(4 + 3 * i)
                continue
            return r
        except Exception as e:
            last = e
            time.sleep(3 + 2 * i)
    raise RuntimeError(f"api failed: {last}")

# 1. draft
r = api("POST", "/deposit/depositions", json={})
r.raise_for_status()
d = r.json()
dep = d["id"]
doi = (d.get("metadata", {}).get("prereserve_doi") or {}).get("doi") or f"10.5281/zenodo.{dep}"
print("DEPOSIT", dep, "DOI", doi)

# 2. patch frontmatter doi
mdp = os.path.join(PROJ, FILES[0])
md = open(mdp, encoding="utf-8").read()
assert "<RESERVED>" not in md
md = md.replace('date: "2026-08-29"', f'date: "2026-08-29"\ndoi: "{doi}"', 1)
open(mdp, "w", encoding="utf-8").write(md)
print("FRONTMATTER patched with", doi)

# 3. rebuild HTML + PDF from patched source
os.chdir(PROJ)
subprocess.run([PANDOC, FILES[0], "-o", FILES[1], "--standalone", "--citeproc",
                "--bibliography", "references.bib"], check=True, capture_output=True)
print("HTML rebuilt")
subprocess.run([sys.executable, BUILDPDF, "distinction-primitive-research-framework"],
               check=True, capture_output=True)
print("PDF rebuilt")

# 4. metadata
desc = ("The QNFO arithmetic-physics program connects number-theoretic structure to "
        "statistical mechanics: prime-indexed modes with logarithmic energies yield partition "
        "functions that are exactly zeta objects, and hierarchy distance is a "
        "realization-independent ultrametric. This record states the methodological discipline "
        "those results share, as a reusable framework: a nine-level construction ladder from the "
        "primitive of distinction to the empirical filter of physics; two boundary rules (no "
        "uncommitted reification of the primitive; no isomorphism passes as a physical "
        "realization without a stated measurement protocol, null model, and falsification "
        "condition); and a compact claim record with mechanical demotion rules. The framework "
        "makes no empirical claims of its own; it systematizes discipline distributed across six "
        "published QNFO records (cited) and states its one claim - ladder coverage of the "
        "published lineage - together with its falsification protocol. The deposited verification "
        "suite exhaustively checks the framework's mechanical content and reproduces the "
        "underlying zeta identities numerically.")
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
    "version": "0.1",
    "related_identifiers": [{
        "scheme": "url",
        "relation": "issupplementto",
        "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/distinction-primitive-research-framework",
    }],
}
r = api("PUT", f"/deposit/depositions/{dep}", json={"metadata": meta})
r.raise_for_status()
print("METADATA ok; related_identifiers:", len(meta["related_identifiers"]))

# 5. upload files (flat names)
for f in FILES:
    with open(os.path.join(PROJ, f), "rb") as fh:
        data = open(os.path.join(PROJ, f), "rb").read()
    r = api("POST", f"/deposit/depositions/{dep}/files",
            data={"name": os.path.basename(f)},
            files={"file": (os.path.basename(f), data)})
    r.raise_for_status()
    print("UPLOADED", os.path.basename(f), r.json().get("size"))

# 6. placeholder check (all local files)
bad = [f for f in FILES if "<RESERVED>" in open(os.path.join(PROJ, f), encoding="utf-8",
      errors="ignore").read()]
assert not bad, f"placeholder found: {bad}"
print("PLACEHOLDER-CHECK: clean")

# 7. publish
r = api("POST", f"/deposit/depositions/{dep}/actions/publish")
r.raise_for_status()
rec = r.json()
recdoi = rec.get("doi")
concept = rec.get("conceptrecid")
concept_doi = f"10.5281/zenodo.{concept}"
print("PUBLISHED", recdoi, "concept", concept_doi)

# 8. DOI live check
for i in range(6):
    try:
        rr = requests.head(f"https://doi.org/{recdoi}", allow_redirects=True, timeout=60)
        if rr.status_code == 200:
            break
    except Exception:
        time.sleep(5)
print("DOI-LIVE:", rr.status_code)

# 9. POST-PUBLISH-FRONTMATTER-ASSERT: download deposited .md, check doi line
r = requests.get(f"{BASE}/records/{recdoi.split('/')[-1]}/files/{FILES[0]}", timeout=180)
r.raise_for_status()
dep_md = r.content.decode("utf-8")
assert f'doi: "{recdoi}"' in dep_md, "deposited .md frontmatter doi mismatch"
print("POST-PUBLISH-FRONTMATTER-ASSERT: PASS")

json.dump({"deposit": dep, "doi": recdoi, "conceptrecid": concept,
           "concept_doi": concept_doi, "files": len(FILES)},
          open(os.path.join(PROJ, "deposit-info.json"), "w"), indent=2)
print("DONE")
