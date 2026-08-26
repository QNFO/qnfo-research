# Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead

Repository and deposit package for QNFO.JPC.003 (branch `res/paper/jpcub-qec-landauer`).

## How to cite

Cite the concept DOI (always resolves to the latest version):

> Quni-Gudzinas, Rowan Brad. (2026). *Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead*. Zenodo. https://doi.org/10.5281/zenodo.22109034

## Contents

- `jpcub-qec-landauer.md` — the paper (canonical markdown, frontmatter carries the record DOI)
- `jpcub-qec-landauer.html`, `jpcub-qec-landauer.pdf` — rendered formats of the paper (A4 PDF)
- `references.bib` — citation-audited bibliography (29 entries, all verified live)
- `citation-audit.md` — per-entry verification record
- `PROJECT-PLAN.md` — charter, locked core claim, hypothesis cards, premise depth
- `README.md`, `LICENSE` — this file and the CC BY 4.0 legal code
- `artifacts/ignorance-audit.md` — Universal Ignorance Audit of the core claim
- `artifacts/due-diligence-phase1.md` — corpus sweep + gap analysis (1,662 papers)
- `artifacts/hypothesis-card-parity.md` — H1/H2/H3 reconciliation at the results gate
- `artifacts/future-research-topics.md` — A1–A7 + B1–B6 future topics
- `artifacts/verification/` — computational verification (floor arithmetic + H2 Monte Carlo + reference renderer + rendering gate), all reproducible with Python 3 stdlib

## Reproduce

```bash
# from the repository root (regenerates the References section from the bib):
python artifacts/verification/render_references.py

cd artifacts/verification
python verification_floor.py   # floor table + golden values (writes verification_floor.json)
python verification_h2.py      # H2 Monte Carlo, seed 20260826 (writes h2_results.json)
python check_rendering.py ../../jpcub-qec-landauer.md   # publication rendering gate
```

Environment: CPython 3.x, standard library only, no external dependencies.

## License

CC BY 4.0 (see `LICENSE`). Source: https://github.com/QNFO/qnfo-research/tree/res/paper/jpcub-qec-landauer
