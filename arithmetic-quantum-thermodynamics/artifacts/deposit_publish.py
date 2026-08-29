"""deposit_publish.py — QNFO.RES.031 Zenodo deposit driver (canonical deposit-API shape).

Flow: create deposition -> write README-DEPOSIT.md (how-to-cite with live
concept DOI) -> upload all files (flattened keys, UMP.014 convention) ->
PUT metadata (deposit-API shape: upload_type/publication_type STRINGS,
plain-string license, plain-list keywords — ZENODO-RECORDS-API-DROPS-METADATA-1)
-> publish -> print DOI summary JSON to artifacts/deposit-result.json.
"""
import json
import os
import sys

import requests

TOKEN = open(os.path.expanduser("~/tokens/zenodo"), encoding="utf-8").read().strip()
BASE = "https://zenodo.org/api/deposit/depositions"
H = {"Authorization": "Bearer " + TOKEN}

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(PROJ, "artifacts")

TITLE = "The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations"

FILES = [
    "arithmetic-quantum-thermodynamics.md",
    "arithmetic-quantum-thermodynamics.html",
    "arithmetic-quantum-thermodynamics.pdf",
    "references.bib",
    "PROJECT-PLAN.md",
    "LICENSE",
    "LICENSE-CC-BY-4.0.txt",
    ("docs/corrected-dictionary.md", "docs_corrected-dictionary.md"),
    ("docs/literature-triage-2026-08-29.md", "docs_literature-triage-2026-08-29.md"),
    ("docs/due-diligence-2026-08-29.md", "docs_due-diligence-2026-08-29.md"),
    ("docs/uia-15q-res031.md", "docs_uia-15q-res031.md"),
    ("docs/uia-15q-res031-p4-reaudit.md", "docs_uia-15q-res031-p4-reaudit.md"),
    ("docs/deep-research-2026-08-29.md", "docs_deep-research-2026-08-29.md"),
    ("docs/dataset-acquisition-2026-08-29.md", "docs_dataset-acquisition-2026-08-29.md"),
    ("artifacts/verification/verify-dictionary-p2.py", "artifacts_verification_verify-dictionary-p2.py"),
    ("artifacts/verification/verify-dictionary-p2-output.txt", "artifacts_verification_verify-dictionary-p2-output.txt"),
    ("artifacts/verification/verify-suite-p3.py", "artifacts_verification_verify-suite-p3.py"),
    ("artifacts/verification/verify-suite-p3-output.txt", "artifacts_verification_verify-suite-p3-output.txt"),
    ("artifacts/verification/check_rendering.py", "artifacts_verification_check_rendering.py"),
    ("artifacts/verification/gammas-120.npy", "artifacts_verification_gammas-120.npy"),
    ("artifacts/external-datasets/riemann-zeros-3000.npy", "artifacts_external-datasets_riemann-zeros-3000.npy"),
    ("artifacts/external-datasets/riemann-zeros-3000-provenance.json", "artifacts_external-datasets_riemann-zeros-3000-provenance.json"),
    ("artifacts/external-search/external-verification-2026-08-29.json", "artifacts_external-search_external-verification-2026-08-29.json"),
    ("artifacts/external-search/corpus-sweep-2026-08-29.json", "artifacts_external-search_corpus-sweep-2026-08-29.json"),
]

PREDECESSOR_DOIS = [
    "10.5281/zenodo.22133122", "10.5281/zenodo.22124744", "10.5281/zenodo.22142794",
    "10.5281/zenodo.22152967", "10.5281/zenodo.22150472", "10.5281/zenodo.22046458",
    "10.5281/zenodo.21916939", "10.5281/zenodo.22076816", "10.5281/zenodo.21905186",
]

DESCRIPTION = (
    "The primon gas - a free quantum gas whose single-particle modes are indexed by the "
    "primes, with energies equal to the logarithms of the primes - has connected quantum "
    "statistical mechanics with multiplicative number theory since the early 1990s and "
    "remains in active use in high-energy theory. This paper consolidates the correspondence "
    "into a single audited reference: a term-by-term dictionary in which every entry is "
    "corrected and every formula is verified by deposited deterministic computations, a "
    "five-level ladder that separates mathematical isomorphism from physical realization "
    "claims, and a negative list stating what the correspondence does not license. The "
    "deposit contains the paper (Markdown, HTML, PDF), the citation database, the two "
    "deterministic verification suites with their outputs (52 checks), the corrected "
    "dictionary reference, and the supporting documentation. The dictionary is exact and "
    "model-specific. The premises end where a physical temperature would be identified at a "
    "p-adic place, and no such identification is asserted."
)

KEYWORDS = [
    "primon gas", "zeta function", "partition function", "quantum statistics",
    "Riemann zeros", "Gentile statistics", "spectral statistics",
    "arithmetic dictionary", "Bost-Connes", "prime gaps",
]


def main():
    # 1. create deposition
    r = requests.post(BASE, headers=H, json={}, timeout=60)
    if r.status_code != 201:
        print("CREATE FAIL", r.status_code, r.text[:500]); sys.exit(1)
    dep = r.json()
    dep_id = dep["id"]
    conceptrecid = dep["conceptrecid"]
    print(f"DEPOSIT: id={dep_id} conceptrecid={conceptrecid}")

    # 2. README-DEPOSIT.md with live how-to-cite (concept DOI)
    readme = f"""# The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations

**Author:** Rowan Brad Quni-Gudzinas (ORCID 0009-0002-4317-5604) · **Date:** 2026-08-29 · **License:** CC BY 4.0

## How to cite

Rowan Brad Quni-Gudzinas (2026). *The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations*. Zenodo. https://doi.org/10.5281/zenodo.{conceptrecid}

BibTeX:

```bibtex
@misc{{qunigudzinas2026correctedprimon,
  author       = {{Quni-Gudzinas, Rowan Brad}},
  title        = {{The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations}},
  year         = {{2026}},
  publisher    = {{Zenodo}},
  doi          = {{10.5281/zenodo.{conceptrecid}}},
}}
```

## Contents

- `arithmetic-quantum-thermodynamics.md/.html/.pdf` — the paper
- `references.bib` — the citation database (rendered bibliography)
- `artifacts_verification_*` — the two deterministic verification suites and outputs (52 checks, all passing)
- `docs_*` — the corrected dictionary reference, the literature triage, the due-diligence record, the ignorance-audit reports, the structured forecast, and the dataset-acquisition record
- `PROJECT-PLAN.md` — the project plan with the pre-registered claim set and disconfirmation matrix

## Reproducibility

Python 3.12.10, NumPy 2.4.4, SciPy 1.17.1, mpmath. Run `python artifacts_verification_verify-dictionary-p2.py` (18/18) and `python artifacts_verification_verify-suite-p3.py` (34/34); the seeded Monte Carlo uses seeds 20260829 and 777. The cached zero ordinates (`artifacts_verification_gammas-120.npy`) are recomputed via mpmath when absent.
"""
    readme_path = os.path.join(PROJ, "README-DEPOSIT.md")
    open(readme_path, "w", encoding="utf-8").write(readme)
    print("README-DEPOSIT.md written with concept DOI")

    # 3. upload files
    upload_keys = [p for p in FILES]
    for item in FILES + ["README-DEPOSIT.md"]:
        if isinstance(item, tuple):
            src, key = item
        else:
            src, key = item, item
        path = os.path.join(PROJ, src)
        if not os.path.exists(path):
            print("MISSING", src); sys.exit(1)
        with open(path, "rb") as fh:
            up = requests.post(
                f"{BASE}/{dep_id}/files",
                headers=H,
                files={"file": (key, fh)},
                timeout=300,
            )
        if up.status_code not in (201,):
            print("UPLOAD FAIL", key, up.status_code, up.text[:300]); sys.exit(1)
        print("  uploaded:", key)

    # 4. metadata (deposit-API shape — strings, plain lists)
    meta = {
        "metadata": {
            "title": TITLE,
            "creators": [
                {"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO",
                 "orcid": "0009-0002-4317-5604"}
            ],
            "description": DESCRIPTION,
            "upload_type": "publication",
            "publication_type": "preprint",
            "access_right": "open",
            "license": "cc-by-4.0",
            "keywords": KEYWORDS,
            "communities": [{"identifier": "qnfo"}],
            "related_identifiers": [
                {"relation": "cites", "identifier": doi, "scheme": "doi"}
                for doi in PREDECESSOR_DOIS
            ],
        }
    }
    r = requests.put(f"{BASE}/{dep_id}", headers=H, json=meta, timeout=60)
    if r.status_code != 200:
        print("META FAIL", r.status_code, r.text[:500]); sys.exit(1)
    # read-back verify (license + keywords must survive)
    rb = r.json()["metadata"]
    print("META readback: license =", rb.get("license"), "| keywords =", len(rb.get("keywords", [])),
          "| related =", len(rb.get("related_identifiers", [])))

    # 5. publish
    r = requests.post(f"{BASE}/{dep_id}/actions/publish", headers=H, timeout=120)
    if r.status_code not in (202,):
        print("PUBLISH FAIL", r.status_code, r.text[:500]); sys.exit(1)
    pub = r.json()
    doi = pub.get("doi")
    result = {
        "deposit_id": dep_id,
        "conceptrecid": conceptrecid,
        "doi": doi,
        "concept_doi": pub.get("conceptdoi") or f"10.5281/zenodo.{conceptrecid}",
        "files": len(FILES) + 1,
    }
    out = os.path.join(ART, "deposit-result.json")
    json.dump(result, open(out, "w"), indent=2)
    print("RESULT:", json.dumps(result))
    print("saved:", out)


if __name__ == "__main__":
    main()
