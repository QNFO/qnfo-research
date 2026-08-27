# QNFO.RES.028 — Arithmetic Anyons

**WBS:** QNFO.RES.028 · **Branch:** res/paper/arithmetic-anyon-contact · **Repo:** QNFO/qnfo-research

Adjudicates the open correspondence of *Quantum Statistics from the Adelic Product Formula* (10.5281/zenodo.22123068): whether the bounded-occupation family ζ(s)/ζ((m+1)s) — the partition function of Gentile intermediate statistics — can carry braid-group exchange phases, and whether the phase-carrying arithmetic objects are instead the multiplicative characters at roots of unity already present in the p-adic anyon braiding records (10.5281/zenodo.21208491, 10.5281/zenodo.22024856).

- Paper: `arithmetic-anyon-contact.md` (+ `.html`, `.pdf`)
- Core claim, disconfirmation criteria (D1–D3), premise depth (L0–L2): `PROJECT-PLAN.md`
- Universal Ignorance Audit (15Q): `artifacts/universal-ignorance-audit.md`
- Phase 1 due diligence (corpus + external): `artifacts/due-diligence-p1.md`
- KIF-29 consilience gate: `artifacts/consilience-gate.md`
- Phase 4 results + hypothesis-card parity: `artifacts/results-p4-reconciliation.md`
- Verification suite: `artifacts/verification/` (3 scripts, final logs, JSON results, reproducibility README)
- Citation audit: `citation-audit.md` (22/22 verified live; evidence `artifacts/external-search/citation-verify.json`)

Verdicts: C1 confirmed (the m-family determines no exchange phase), C2 confirmed (characters at roots of unity carry the phases), H2 confirmed (prime-gap specific-heat deviation nonzero in both statistics).

## How to cite

Cite all versions (always resolves to the latest one):

> Rowan Brad Quni-Gudzinas. *Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, and the Roots of Unity That Carry Braid Phases*. QNFO, 2026. Zenodo. https://doi.org/10.5281/zenodo.22124743

This version (v1.0.0): https://doi.org/10.5281/zenodo.22124744

## Re-run the verification

```
cd artifacts/verification
python verify_m_anyon.py            # C1 — bounded-occupation family adjudication
python verify_braid_characters.py   # C2 — root-of-unity character model
python verify_prime_gap_thermo.py   # H2 — prime-gap specific-heat deviation
```

Python 3 + mpmath only; deterministic; no network access. See `artifacts/verification/README.md`.

## License

CC BY 4.0 (see LICENSE).
