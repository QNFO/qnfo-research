# P3 — Computational Verification Integration (QNFO.RES.023)

- **Date:** 2026-08-23
- **Gate:** COMPUTATIONAL-VERIFICATION-1 / VERIFY-IN-CODE-1 (every
  quantitative claim checked in code; verification artifacts deposited with
  the paper; reproducibility statement).
- **Source of inherited suite:** RES.022 (10.5281/zenodo.22071421) branch
  res/paper/keyword-taxonomy-consilience @ be36005 — `artifacts/verification/`.

## 1. What was integrated

The full deterministic verification suite was copied byte-identical from
the predecessor record into this paper's repo:

| Script | Checks | Inputs |
|:-------|:-------|:-------|
| `rq5_keyword_load.py` | taxonomy audit (L1-L4: 335 kws, 334 program-local, Fisher p=1.0) | keyword-taxonomy-source.md |
| `rq1_retrieval_benchmark.py` | H1 retrieval (p@5/p@10/MRR, three comparators) | corpus_qnfo_titles.json |
| `rq2_consilience_links.py` | RQ2 consilience-link test (same-label rate at matched counts) | corpus_qnfo_titles.json |
| `rq3_archimedean_limit.py` | H2 numeric (ultrametric violations, CLT golden, Gaussianity) | (generated) |
| `rq4_noise_scaling.py` | H3 scaling (log-log slopes, exact arithmetic, MC sanity) | (generated) |

Inputs `keyword-taxonomy-source.md` (12,684 B LF at fetch) and
`corpus_qnfo_titles.json` (400 pinned titles) copied byte-identical.
Expected outputs archived at `artifacts/verification/inherited-res022/`
(results JSONs + run logs from the RES.022 deposit).

## 2. Regeneration proof (run from repository root)

All five scripts re-run on this branch, seed 20260823, pure Python
standard library:

| Script | Exit | Regenerated vs inherited |
|:-------|:----:|:-------------------------|
| rq5_keyword_load.py | 0 | **BYTE-IDENTICAL** |
| rq1_retrieval_benchmark.py | 0 | **BYTE-IDENTICAL** |
| rq2_consilience_links.py | 0 | **BYTE-IDENTICAL** |
| rq3_archimedean_limit.py | 0 | **BYTE-IDENTICAL** |
| rq4_noise_scaling.py | 0 | **BYTE-IDENTICAL** |

Invocation note (validated): scripts use repo-root-relative input paths —
they MUST be run from the repository root (`python
artifacts/verification/rq5_keyword_load.py`), not from inside
artifacts/verification/. Running from inside the directory fails with
FileNotFoundError (observed and documented here as a guardrail, not a bug).

## 3. Claims verified by this suite (as cited in the paper)

- §5.1: 335 keywords, 334 program-local (99.7%), 1 shared (complexity-
  measure, INM∩RES), 0 shared by ≥3, contingency (0,53,0,282), Fisher
  p = 1.0, hierarchy family the only ≥3-program bridge family
  (SLB 2 + RES 2 + DEM 4).
- §5.2 H1: corpus A p@10 1.000 vs 1.000 (Δ=0.000); corpus B 0.765 vs 0.807
  (Δ=−0.042); hash control 0.210 (encoding dependence).
- §5.2 H2: 0 ultrametric violations (30k triples); CLT golden rel. err
  0.004–0.039 vs sigma^2/n; Gaussianity (|skew|≤0.088, |kurt|≤0.100).
- §5.2 H3: Markovian slope −2.0000 vs p-adic −0.9881 (separation 1.012);
  exact arithmetic 0.0 rel. err; MC sanity 1.4e-3.
- §6 RQ2: same-label rate p-adic depth vs cosine at N=50/100/200 —
  corpus A 0.120/0.190/0.170 vs 1.000; corpus B 0.660/0.570/0.625 vs
  0.960/0.870/0.845 (NOT SUPPORTED for raw-hash encoding — encoding
  dependence per UIA Q2).

## 4. Reproducibility statement (paper §12)

All quantitative claims in this paper are produced by the deterministic,
seeded verification suite archived in `artifacts/verification/` (pure
Python standard library; fixed seed 20260823; no random seeds required
beyond the declared constants). Re-running from the repository root
regenerates every JSON artifact byte-identically (proven above; expected
outputs archived in `inherited-res022/`). Runtime: under two minutes for
the full suite on the reference machine; no external services required.
