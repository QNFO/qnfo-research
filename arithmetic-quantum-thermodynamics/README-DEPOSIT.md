# The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations

**Author:** Rowan Brad Quni-Gudzinas (ORCID 0009-0002-4317-5604) · **Date:** 2026-08-29 · **License:** CC BY 4.0

## How to cite

Rowan Brad Quni-Gudzinas (2026). *The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations*. Zenodo. https://doi.org/10.5281/zenodo.22159757

BibTeX:

```bibtex
@misc{qunigudzinas2026correctedprimon,
  author       = {Quni-Gudzinas, Rowan Brad},
  title        = {The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22159757},
}
```

## Contents

- `arithmetic-quantum-thermodynamics.md/.html/.pdf` — the paper
- `references.bib` — the citation database (rendered bibliography)
- `artifacts_verification_*` — the two deterministic verification suites and outputs (52 checks, all passing)
- `docs_*` — the corrected dictionary reference, the literature triage, the due-diligence record, the ignorance-audit reports, the structured forecast, and the dataset-acquisition record
- `PROJECT-PLAN.md` — the project plan with the pre-registered claim set and disconfirmation matrix

## Reproducibility

Python 3.12.10, NumPy 2.4.4, SciPy 1.17.1, mpmath. Run `python artifacts_verification_verify-dictionary-p2.py` (18/18) and `python artifacts_verification_verify-suite-p3.py` (34/34); the seeded Monte Carlo uses seeds 20260829 and 777. The cached zero ordinates (`artifacts_verification_gammas-120.npy`) are recomputed via mpmath when absent.
