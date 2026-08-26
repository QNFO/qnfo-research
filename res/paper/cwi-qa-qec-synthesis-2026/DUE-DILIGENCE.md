# DUE-DILIGENCE.md — QNFO.RES.026 Phase 1

**Project:** The Unpriced Column: A Slide-Level Synthesis of the CWI Summer School on QA and QEC (24–28 Aug 2026)
**Phase 1 date:** 2026-08-26
**Evidence:** `artifacts/external-search/corpus-sweep-2026-08-26.json`, `artifacts/external-search/crosswalk-validation-2026-08-26.json`

## 1. Sweep method (DUE-DILIGENCE-DEPTH-1)

- Corpus size at sweep: 8,329 nodes / 8,511 edges / 1,665 papers (query_graph stats).
- 6 query formulations across 3 topic facets (energy/thermodynamics; practical overhead; metascience/self-presentation), each limit=16 (VECTORIZE-TOP-K-50-1).
- recall_facts + search_memories ran in parallel; KG neighbor walk attempted (see §3).
- Cross-system ID validation via resolve_paper_id on every first-order hit (7 records, §3).

## 2. Adjacent-domain coverage (>=2 required)

| Domain | Records touched |
|---|---|
| QNFO.JPC (JPCub) | joules-per-solution-metric, JPC.002 scorecard branch, JPC.003 (10.5281/zenodo.22114431) |
| QNFO.UMP / QEC-adjacent | qec-darwinism-ultrametric (10.5281/zenodo.21964674), locale-framework-quantum-applications (10.5281/zenodo.21991270), trapped-ion-ultrametric-synthesis |
| QNFO.RES / metascience | universal-ignorance-audit, ai4metascience-ignorance-audit (10.5281/zenodo.22026592), ignorance-ai-pipeline-synthesis, huang-2025-quantum-advantage-audit (10.5281/zenodo.21440671), paper-manifesto-honest-computation |

Three adjacent WBS domains swept (JPC, UMP, RES). CROSSWALK-TRANSLATION-1: the synthesis bridges the QEC-engineering vocabulary (syndrome, decoder, physical-qubit overhead) to the adjacent-domain equivalents (erasure/erasure-engine, energy-per-corrected-bit, curriculum audit); the bridge is named in the working title ("The Unpriced Column").

## 3. Findings that constrain the claim

1. **The thesis exists; the evidence snapshot does not.** The energy-cost-of-QEC thesis is already published (bottlenecks 2025-12; JPC.003 v1.4/v1.5). No corpus record performs a slide-level audit of the field's own teaching materials. RES.026's distinct contribution is the evidence-side snapshot + the metascience reading, not the thesis.
2. **The user's own Day-1 threads extend the claim.** The Obsidian synthesis draft (`_cwi-synthesis-draft-2026-08-26.md`) carries six threads (definitional tautology, unpriced physical cost, design-choice-dressed-as-law, geometric fictions, reality-as-syndrome, epistemic frames). The provisional core claim stays energy-focused; the other threads become secondary sections at P3, carried as the attendee's reading of the decks, each tied to deck evidence where it exists.
3. **Poster-withdrawal narrative is internal-archive content.** The v7.1 verdict and the poster decision are pipeline history — excluded from publication prose (PAPERS-NO-NAVEL-GAZING-1). Only the empirical threads survive.
4. **Known title drift, not a new finding.** qec-darwinism-ultrametric carries the self-disclosed title drift (D1 vs Zenodo). Cite the canonical Zenodo title "Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces."
5. **KG neighbor walk empty.** The bottlenecks paper node has no KG edges — the BUILDS_ON/BELONGS_TO edges for RES.026 will be built explicitly at P6 (semantic links are built, not discovered).

## 4. External verification

- arXiv:2602.11457 (Pinnacle) and arXiv:2603.28627 (Cain et al.) verified via arXiv API 2026-08-26 — titles and key abstract numbers match the slide citations (evidence in JPC.003 `artifacts/cwi-slide-audit.md`, shared).
- The slide PDFs themselves are primary evidence: retrieved 2026-08-26 from the organizers' SURFdrive share, text-extracted, slide-number-traced.

## 5. Gap analysis (vs provisional core claim)

The claim survives Phase 1 with one refinement: **the synthesis is an evidence-and-reading paper, not a new physics claim.** It documents (a) what the 2026 curriculum prices (qubits, time, error rates), (b) what it omits (energy), (c) the decks' own caveats, and (d) the attendee's threads that go beyond energy. It BUILDS_ON the published thesis rather than re-deriving it. No corpus contradiction found that flips the claim; the strongest complication is scope discipline (findings 2–3 above).

## 6. Phase 2 entry

P2 = draft outline mapping deck evidence to each thread, then P3 draft absorbing the Obsidian synthesis content. Publish path and gates unchanged from PROJECT-PLAN.
