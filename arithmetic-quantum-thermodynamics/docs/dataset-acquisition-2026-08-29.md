# Dataset Acquisition — QNFO.RES.031 (DATASET-ACQUISITION-1)

- **Date:** 2026-08-29 (red-team H-1 remediation, assigned P2)
- **Evidence dir:** `artifacts/external-search/dataset-probes/`
- **Scope:** every paper under analysis at Phase 1: the two external 2025 JHEP primon-gas papers, the canonical 1990–1995 external lineage, and the six QNFO predecessor records.

## 1. External papers under analysis

| Paper | Nature | Dataset probe | Verdict |
|---|---|---|---|
| The Conformal Primon Gas at the End of Time — JHEP 07(2025)281, arXiv:2502.02661 | pure theory (number-theoretic partition functions in cosmology) | arXiv API metadata: 1 entry, zero ancillary/data links (`arxiv-jhep-primons.xml`) | **documented absence — no dataset exists** |
| Wheeler–DeWitt wavefunctions for 5d BKL dynamics… — JHEP 11(2025)160, arXiv:2507.08788 | pure theory | same probe: zero ancillary/data links | **documented absence** |
| Julia 1990 (10.1007/978-3-642-75405-0_30), Spector 1990 (10.1007/bf02096755), Bakas–Bowick 1991 (10.1063/1.529511), Bost–Connes 1995 (10.1007/bf01589495), Montgomery 1973, Gallagher 1976, Odlyzko 1987 | mathematics/theory papers | theory records; no datasets by construction | **documented absence** |

Nothing was acquired because nothing exists to acquire; each blocked/absent path carries the probe evidence above (never "no dataset" without probe logs).

## 2. QNFO predecessor records (Zenodo file-list probes, `dataset-probes/zenodo-*.json`)

| Record | Files | Raw third-party data? | What IS there (first-class computational artifacts) |
|---|---|---|---|
| RES.027 adelic-quantum-statistics (22133122) | 44 | no | verify_product_formula.py, verify_parastats.py, verify_stats_results.json, run logs |
| RES.028 arithmetic-anyon-contact (22124744) | 29 | no | verify_braid_characters.py, verify_prime_gap_thermo.py, final logs |
| RES.029 adelic-quantum-arithmetic (22142794) | 19 | no | text/PDF + literature evidence only |
| RES.030 arithmetic-cut-discrimination (22152967) | 27 | no | **computed data `riemann-zeros-3000.npy`** + sim-arithmetic-cut-discrimination.py + outputs |
| UMP.014 distinction-based-ultrametric (22150472) | 32 | real-spectrum inputs fetched at run time, NOT redistributed (third-party license) | sim-riemann-zeros-fast.py, run-real-spectrum.py, full-run.txt |
| ultrametric-program (22076816) | 40 | no | rq1_retrieval_benchmark.py + results |
| idempotent-core (21916939) | 31 | no | literature evidence + verification |

**DOI correction recorded here:** the probe of 21906728 resolved to a *reentrant-distinctions* version, not idempotent-core. Idempotent-core's registry-verified DOI is **10.5281/zenodo.21916939** (papers-table resolve_paper_id + Zenodo title read-back agree). Cited as such in PROJECT-PLAN.

## 3. Disposition for RES.031

1. **No original research datasets exist** for the external papers under analysis — documented absence with probe evidence (arXiv ancillary check; Zenodo file lists above).
2. The program's own **computed** artifacts (RES.030 zeros cache; null-ensemble outputs; verification results) are acquired by **re-running the deposited deterministic scripts** at P3 (BP-10: citation is not verification) — DR2 of this plan already binds that.
3. **Third-party raw data** (ExoMol-class molecular spectra via UMP.014's run-real-spectrum.py) enters only at P3 when Appendix D is built; acquisition and license discipline are handled there with probe evidence per DATASET-SOURCE-FALLBACK-1 (static `.states` mirrors, range-request 206; ENSDF-style servlet probes). License discipline: CC BY/CC0 attribution; NC/ND cite-only, no redistribution; the lineage's existing practice (fetch-at-run-time, no redistribution) is retained.
4. No dataset is fabricated and none is claimed to have been acquired.
