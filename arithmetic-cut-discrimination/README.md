# Discriminating the Arithmetic Cut

Matched-level-density null models for the primon-gas specific heat and
spectral correlations — does the arithmetic signature survive its own null
objection?

**How to cite:** Quni-Gudzinas, Rowan Brad (2026). *Discriminating the
Arithmetic Cut: Matched-Level-Density Null Models for the Primon-Gas Specific
Heat and Spectral Correlations*. QNFO. DOI (concept): 10.5281/zenodo.XXXXXXX.
Repository: https://github.com/QNFO/qnfo-research/tree/res/paper/arithmetic-cut-discrimination

## What this record is

The arithmetic-statistics program identifies the two exchange statistics with
two multiplicity rules on the integer lattice; its published observable is the
primon-gas specific heat. This record adjudicates the program's own
red-team objection — that any irregular spectrum with the same level density
could reproduce the published deviation — by constructing three
matched-density non-arithmetic null ensembles and measuring the cut against
them. The specific heat separates at 2 sigma from the smallest tested cutoff
onward (fixed-count nulls) and beyond a computable minimum cutoff
(Poisson-type nulls); the two-point information is concentrated in the
small-spacing hard core (34 sigma). Two published numbers of the estimation
record are also adjudicated (Dyson window mismatch; Bost-Connes finite-cutoff
crossover).

## Repository layout

```
arithmetic-cut-discrimination/
├── arithmetic-cut-discrimination.md   (paper, plain scholarly prose)
├── arithmetic-cut-discrimination.html (rendered, MathJax)
├── arithmetic-cut-discrimination.pdf  (CDP pipeline, A4/2cm)
├── references.bib                     (16 cited refs, audit-clean)
├── citation-audit.md                  (live audit evidence)
├── PROJECT-PLAN.md                    (WBS: QNFO.RES.030)
├── README.md                          (this file)
├── docs/                              (deep-research, due-diligence, estimator
│                                       construction, UIA, seed-cluster intake,
│                                       verification-integration, red-team P4)
├── notebooks/                         (reserved)
└── artifacts/
    ├── external-search/               (Phase-1 evidence: corpus sweep JSON,
    │                                   cross-system validation, external probes)
    └── verification/                  (deposited deterministic scripts + outputs:
                                        sim-spectral-estimators.py,
                                        sim-arithmetic-cut-discrimination.py,
                                        diag-number-variance.py, citation-audit.py,
                                        *-output.json, run logs)
```

## Reproducibility

Seed 20260829 everywhere. Python 3.12.10, NumPy 2.4.4, SciPy 1.17.1.
Riemann zeros via vectorized Riemann-Siegel Z-function; cache
`artifacts/verification/riemann-zeros-3000.npy`. Run from the repo root:
`python arithmetic-cut-discrimination/artifacts/verification/<script>.py`.
Every quantitative claim in the paper is reproduced by the deposited scripts
(VERIFY-IN-CODE-1); the outputs are committed in the record.

## Premise boundary

The claims are isomorphisms of mathematical structure and computed
discrimination thresholds. No physical realization is asserted; the premises
end where a physical temperature is identified at a p-adic place.

## Related program records

- QNFO.RES.027 Quantum Statistics from the Adelic Product Formula (10.5281/zenodo.22133122)
- QNFO.RES.028 Arithmetic Anyons (10.5281/zenodo.22124744)
- QNFO.RES.029 Adelic Quantum Arithmetic (10.5281/zenodo.22142794)
- QNFO.UMP.014 The Distinction-Based Ultrametric (10.5281/zenodo.22150472)
- QNFO.RES.023 The Ultrametric Program (10.5281/zenodo.22076816)
- H-DIST-3 disconfirmation pre-registration (osf.io/ba8ns)
