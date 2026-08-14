# Due Diligence — Phase 1 Report (QNFO.RES.007)

**Project:** Invariant Structural Value
**Date:** 2026-08-14
**Branch:** res/paper/invariant-structural-value
**WBS:** QNFO.RES.007

## 1. KG Ecosystem Overview (query_graph stats — live 2026-08-14)

- totalNodes: 8,279
- totalEdges: 8,417
- Paper nodes: 1,621 · Project: 150 · Concept: 68 · ResearchQuestion: 49 · Program: 21

## 2. QNFO Cross-Reference (DUE-DILIGENCE-DEPTH-1: ≥3 query formulations, limit ≥20)

Query formulations run (semantic drift):
1. `invariant structural value fundamental constants formulas dimensionless relations` (search_papers_enriched limit 10)
2. `quantum mechanics invariant structure projective Hilbert space gauge symmetry` (search_papers_enriched limit 10)
3. `laws of form mark distinction euler identity self-reference fixed point e pi` (search_papers_enriched limit 8)
4. `fundamental constants fine-structure alpha pi euler identity invariance laws of form` (search_papers_enriched limit 8)
5. KG node searches: label=Paper search `invariant` (28 hits), `constant` (14 hits), `laws of form` (9 hits), `euler` (0 hits)
6. recall_facts keyword `invariant` (15 memories)
7. qnfo-memory-mcp search_papers — DOWN (Worker 1101 non-retryable; documented tool gap, PAPER-CONTEXT-TOOL-EMPTY-1 class; fallback used)

### Top adjacent QNFO records (all resolve_paper_id-validated)

| Slug | Title | DOI | Status | Relevance |
|:-----|:------|:----|:-------|:----------|
| alpha-pi-helix | α-π-Helix: Geometric Unification of Fundamental Constants | 10.5281/zenodo.21515789 | published | C3-adjacent: π/α as projections of helical geometry; does NOT derive e/π from mark/distinction self-reference |
| invariant-patterns-adelic-refactoring | Invariant Patterns and the Adelic Refactoring of Fundamental Physics (QNFO.UMP.003) | 10.5281/zenodo.21785893 (KG: 21786511 — MISMATCH flagged) | published | C1-adjacent: invariant patterns + adelic refactoring |
| ostrowski-dimensionless-reformulation | The Ostrowski Dimensionless Reformulation (ODR v4.0.4) | 10.5281/zenodo.21756190 (KG: 21751722 v2.0) | published | C1-adjacent: dimensionless ratios, Planck units, place democracy; compendium, not structuralist analysis |
| quantum-mechanical-physics-as-invariant-geometric-structure | Quantum-Mechanical Physics as Invariant Geometric Structure | 10.5281/zenodo.20109773 | published (kg-backfill) | C2-adjacent: QM as invariant geometric structure |
| fine-structure-constant-as-a-cross-ratio | Fine-Structure Constant as a Cross-Ratio | 10.5281/zenodo.20108536 | published | C1-adjacent: α as projective invariant (cross-ratio) |
| syntactic-token-calculus-m1-foundational-syntax | Syntactic Token Calculus (mark and void → projective invariants) | 10.5281/zenodo.19547736 | published | C3-adjacent: distinction calculus, projective invariants as measurable quantities |
| quantum-laws-of-form-superposition-as-re-entry-measurement-as-distinction | Quantum Laws of Form: Superposition as Re-Entry, Measurement as Distinction | 10.5281/zenodo.21205110 | published | C3-adjacent: LoF re-entry and distinction in QM |
| the-calculus-of-distinction-a-formal-isomorphism-between-laws-of-form-and-ultrametric-trees | Calculus of Distinction: LoF ↔ Ultrametric Trees | 10.5281/zenodo.21205097 | published | C3-adjacent: LoF/ultrametric isomorphism |
| measurable-vs-imaginable | The Computable Real Boundary: Where Physics Ends and Cognitive Fiction Begins | 10.5281/zenodo.21645350 | published | Adjacent: computable-real boundary; distinct from invariant-content thesis |
| adelic-constraints-project | The Adelic Constraints Project — A Complete Account | 10.5281/zenodo.20120042 | published | C1-adjacent: adelic constraints on constants (null-result discipline) |
| master-work-plan-v2-x-phase | Master Work Plan v2.0 — Cross-Domain Phase X1-X6 | 10.5281/zenodo.21491676 | published | Nexus: α as adelic-compton-harmonic nexus |
| winding-numbers-and-strange-loops | Winding Numbers and Strange Loops | 10.5281/zenodo.17322662 | published | C2/C3-adjacent: S¹ topology, winding numbers as invariants, e^{inθ} |
| strange-loop-of-being | Strange Loop Theory of Physical Quantization | 10.5281/zenodo.17419332 | published | C3-adjacent: fixed-point equation R(Ψ)=Ψ, self-reference, topological invariants |
| zbw-majorana-tqc-p2-majorana-zbw-correlator | Majorana ZBW Correlator: Z2 Topological Invariant | 10.5281/zenodo.21336045 | published | C2-example: measured topological invariant |
| adelic-core-synthesis | Adelic Core Synthesis | 10.5281/zenodo.21786473 | draft | C1-adjacent: "1/137 is a red herring" — running coupling, true invariant is functional α(μ) |

### Adjacent WBS domains (≥2 required): 
RES (this project), **UMP** (invariant-patterns-adelic-refactoring, ODR), **SLB** (Quantum Laws of Form, Syntactic Token Calculus, Calculus of Distinction, Notation Problem), **INM** (scale-invariant information thermodynamics series), **CFE** (master work plan X-series).

## 3. External Literature Search (independent verification)

Evidence saved to `artifacts/external-search/`.

| Source | Result | File |
|:-------|:-------|:-----|
| arXiv: 2508.01616 | De Haro & Butterfield, The Philosophy and Physics of Duality (2025) — dualities, geometric view of theories, realism | external-search/arxiv-duality-2508.01616.json |
| arXiv: 1507.02229 | Solà, Fundamental Constants in Physics and Their Time Variation (2015) | external-search/arxiv-sola-constants-1507.02229.json |
| arXiv: 1702.07382 | Thompson, Relation Between Fundamental Constants and Particle Physics Parameters (2017) | external-search/arxiv-thompson-1702.07382.json |
| arXiv: 1504.06686 | Knuth, The Deeper Roles of Mathematics in Physical Laws (2015) | external-search/arxiv-knuth-1504.06686.json |
| arXiv: 1805.10602 | Rovelli, Physics Needs Philosophy. Philosophy Needs Physics (2018) | external-search/arxiv-rovelli-1805.10602.json |
| arXiv: 2306.13975 | de Ronde, Bohr's Anti-Realist Realism (2023) | external-search/arxiv-deronde-2306.13975.json |
| arXiv LoF/e/π query | **ZERO relevant external hits** for laws-of-form → e/π derivation | external-search/arxiv-lof-zero-hits.json |

## 4. Gap Analysis

### Covered by QNFO:
- Dimensionless reformulation / Planck units / place democracy (ODR v4.0.4) — compilation, Ostrowski grounding
- α as cross-ratio projective invariant (Fine-Structure Constant as Cross-Ratio)
- π and α as helical projections (α-π-Helix)
- QM as invariant geometric structure (QM-IGS)
- LoF re-entry in QM (Quantum Laws of Form), LoF↔ultrametric trees
- Scale-invariant information thermodynamics series
- Measurable-vs-imaginable boundary

### NOT covered (genuine novelty for RES.007):
1. **C1 unified claim**: the invariant structural value of constants/formulas as *the* subject — a systematic structuralist account of WHY dimensionful constants are bridges and dimensionless ratios/angles/phases/topological indices/fixed points are the invariant content. ODR is a compendium; α-π-Helix is geometric-specific; neither states the general structuralist thesis with C1's scope.
2. **C2 quotient formulation**: measurable physics = invariants of a larger mathematical structure / redundancy groups, with explicit catalog of the non-measurable scaffolding (complex phases, gauge potentials, path integrals, ghosts/BRST, bare parameters, complexified kinematic spaces). QM-IGS is close but does not frame the redundancy-group quotient.
3. **C3 generative claim**: e and π as fixed points of self-application/self-closure from a primitive mark/distinction; Euler identity as joint fixed point; compact-closed/trace setting. **No QNFO record and no external arXiv record derives e and π from mark-and-distinction self-reference.** α-π-Helix treats π as geometry of a helix; Strange Loop uses fixed-point equations for the Standard Model but not for e/π from LoF primitives; Syntactic Token Calculus uses mark/void for projective invariants but not the e/π fixed-point derivation.

### Confirmation-bias disclosure:
Most high-scoring Vectorize hits are QNFO-internal (expected: corpus is the author's own ~1,000 records). External corroboration exists for the C1/C2 components (structural realism literature: Worrall, Ladyman-Ross, French; duality philosophy: De Haro & Butterfield; Knuth's symmetry-as-law derivation; Rovelli's relationalism) — will be integrated in P2 literature review. C3 (LoF→e/π) has NO external corroboration found → flag [UNIQUE-CLAIM] with corresponding epistemic burden (symmetric audit required).

### Data-quality findings:
- invariant-patterns-adelic-refactoring: Zenodo 21785893 (search) vs 21786511 (KG properties) — DOIs differ; flag for reconciliation (not this project's scope; log to kaizen).

## 5. Conclusion

Net-new at the standalone-thesis level: the unified invariant-structural-value thesis (C1) + redundancy-group quotient (C2) + mark/distinction e/π fixed-point derivation (C3) is not present in the QNFO corpus or external literature. Proceed to Phase 1b consilience gate, then P2.
