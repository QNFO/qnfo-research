# Deep Research — QNFO.RES.022 (consolidated due diligence)

- **Date:** 2026-08-23 (Phase 1; evidence updated through Phase 5.1)
- **Protocol:** DUE-DILIGENCE-DEPTH-1 (full-corpus sweep; cross-system ID
  validation; adjacent-domain breadth; external verification; evidence
  discipline)
- **Canonical Phase-1 artifact:** `artifacts/due-diligence-phase1.md`
  (2026-08-23, commit c3fbe03); this document consolidates it for the
  publication record.

## 1. Corpus baseline

QNFO knowledge graph: 8,324 nodes / 8,497 edges; 1,660 Paper nodes; 156
Project nodes (queried 2026-08-23). Living-paper database: 400 titles pinned
for the H1 corpus B (2026-08-23).

## 2. Full-corpus sweep (11 query formulations, 6 topics, 4 domains)

- T1 ultrametric compression prior: nonlinear-tree-based-numeration-systems
  (10.5281/zenodo.21046213 — positional notation is natively an ultrametric
  tree), projective-geometric-frameworks-for-semantic-structures
  (10.5281/zenodo.19564091 — ultrametric semantic memory, computationally
  validated), proof-of-concept-auditable-attention (R2-only),
  principia-ontologica.
- T2 adelic/global synthesis: consilience-physics-numtheory
  (10.5281/zenodo.21590155), adelic-core-synthesis, adelic-distinction,
  adelic-constraints-on-qft, ostrowski-dimensionless-reformulation.
- T3 measurement stratigraphy: measurement-stratigraphy
  (10.5281/zenodo.21705220), valuation-independent-foundations
  (10.5281/zenodo.21803677), anthropometric-fossils,
  operationalizing-generalized-symmetries.
- T4 SLB bridge: reentrant-distinctions, void-is-not-false, idempotent-core,
  prime-valuation-depth (10.5281/zenodo.21918838 — multiplication as
  branching).
- T5 Ruliad/computational universe: computational-syntax-of-reality,
  syntactic-token-calculus, topological-and-computational-unification-of-
  emergent-agency, time-as-epistemic-cognitive-fiction.
- T6 UMP dynamics / INM bounds: ballistic-transport-on-the-bruhat-tits-tree,
  spectral-dynamics-on-bruhat-tits-trees, ultrametric-quantum-gravity-and-
  computation, number-theory-as-physics, paper-physics-of-computation,
  electron-hook-treatise, thermodynamic-and-informational-bottlenecks,
  structural-vs-driven-quantum-coherence.

## 3. Cross-system ID validation

10 key records resolved via `resolve_paper_id` (slug → Vectorize → KG → DOI).
Clean: 8/10. Findings: F1 reentrant-distinctions dual DOI (21964453 vs
21908818 — resolved to 10.5281/zenodo.21908818 for citation; not cited in
this paper's reference list); F2 atlas KG/D1 conflict (resolved at P6:
DOI findable, citation stands); F3 two records R2-only (proof-of-concept-
auditable-attention, ballistic-transport — cited by slug only, not in the
reference list).

## 4. Adjacent-domain breadth

UMP, SLB, INM, RES swept (>=2 required, 4 delivered). CFE returned no direct
hits in the Phase-1 sweep — the CFE bridge (gap G6) remains the weakest
documented link, disclosed in the paper §9.

## 5. External verification (arXiv, 2026-08-23)

Evidence files: `artifacts/external-search/arxiv-evidence-2026-08-23.json`
(3 queries: Murtagh ultrametric data science; p-adic representation
learning — empty, superseded by G5 closure; RSB ultrametricity) +
`arxiv-evidence-g5-2026-08-23.json` (G5 closure: hyperbolic embeddings
Ganea 2018; p-adic/ultrametric data model Murtagh 2008).

- G1: Murtagh 2006/2007/2010/2012 — H1 prior art; repositioned as modern
  re-execution with baselines (paper §8).
- G2/G4: Parisi RSB ultrametricity measured in random lasers (2209.03781)
  and cavity-QED (2307.10176); Newman-Stein finite-d controversy
  (cond-mat/0105282) confronted in §8.
- G3: Marsh et al. (2307.10176) = nearest existing experiment to H3.
- G5: closed at P6 (section 5 above).
- G6: CFE gap open, disclosed.

## 6. Verification suite (Phase 4 + 5.1)

Five deterministic scripts in `artifacts/verification/`:
rq5_keyword_load.py (taxonomy audit — L1 string level NOT SUPPORTED,
334/335 program-local), rq1_retrieval_benchmark.py (H1 — ultrametric
single-link index matches cosine on corpus A, −0.042 p@10 on corpus B;
hash encoding control collapses as predicted), rq2_consilience_links.py
(RQ2 — raw-hash p-adic prefixes do not identify consilience links better
than cosine; encoding dependence), rq3_archimedean_limit.py (H2 numeric
PASS — 0 ultrametric violations, CLT golden), rq4_noise_scaling.py (H3
numeric PASS — p-adic slope −0.9881 vs Markovian −2.0000, separation 1.012).
Full results and logs deposited with the paper.

## 7. Universal Ignorance Audit

`artifacts/universal-ignorance-audit.md` — 15 questions answered on the
locked core claim (2026-08-23). Products: standing dangerous question (Q9),
H1 pre-registration requirements, plural-radix seed (Q15) — the invariant-is-
hierarchy reading confirmed by the corpus audit (Q6 convergence).
