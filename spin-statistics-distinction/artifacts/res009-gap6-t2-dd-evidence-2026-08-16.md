# RES.009 GAP-6 — T2 Derivation: Due-Diligence Evidence Report

- **WBS:** QNFO.RES.009 (spin-statistics-distinction, branch `res/paper/spin-statistics-distinction`)
- **Target artifact:** Obsidian note `2026/08/15/res009-gap6-t2-derivation.md` (DRAFT v0.1, derivation sketch)
- **Cycle:** CMD RESEARCH Phase 1 (due diligence) — existing project (Phase 0 net-new steps skipped)
- **Date:** 2026-08-16
- **Corpus size (KG stats):** 8,290 nodes / 8,432 edges; 1,630 Paper nodes

## 1. Corpus sweep (DUE-DILIGENCE-DEPTH-1)

### Infrastructure findings (HARD, infra — qnfo-memory-mcp Worker)

- **INFRA-A:** `search_papers` (base MCP endpoint) throws **Error 1101 Worker exception on ALL requests** (6/6, 2026-08-16 04:44Z; ray `a2bdc8b9...`; retryable:false). Same request, same exception.
- **INFRA-B:** `search_papers_enriched` throws **1101 when `limit >= 20`** (2/2 at limit=20, ray `a2bdce58`/`a2bdce5b`), succeeds at limit<=10 (5/5). Hypothesis: unhandled Vectorize `topK` cap in the Worker. Limit parameter is the trigger.
- Per BLAME-EXTERNAL-1 these are OUR-Worker bugs, not platform outages. Remediation (next cycle, cloudflare skill): clamp limit / catch Vectorize maxTopK in qnfo-memory-mcp. The sweep below was completed within the cap (limits 5-10) plus KG + memory paths.

### Query formulations executed (13 working, enriched; base endpoint unavailable)

| # | Topic | Formulation | Result |
|---|---|---|---|
| 1 | T1 exchange/S_n | exchange statistics braiding involutivity boson fermion symmetric group characters | 8 hits |
| 2 | T1 | exchange statistics braid group anyons spin statistics symmetric group fundamental group | 10 hits |
| 3 | T1 | trivial and sign representations of the symmetric group exchange phase (base endpoint — failed, 1101) | — |
| 4 | T2 ribbon/abelian | abelian object ribbon braided tensor category quantum trace topological spin | 8 hits |
| 5 | T2 | theta equals double braiding ribbon identity anyon dimension | 8 hits |
| 6 | T2 | dimension one object braiding scalar simple object Schur lemma | 8 hits |
| 7 | T3 TL/braid | Temperley-Lieb algebra anyon fusion braid group representation | 8 hits |
| 8 | T3 | p-adic braid group ultrametric anyon braiding | 8 hits |
| 9 | T3 | Artin presentation braid group symmetric group involutive quotient configuration space | 8 hits |
| 10 | T4 DHR/AQFT | DHR superselection sectors parastatistics exclusion locality | 8 hits (weak — no dedicated AQFT record) |
| 11 | T4 | spin statistics theorem Lorentz microcausality positive energy derivation | 8 hits |
| 12 | SLB | Calling Crossing laws of form calculus of indications Spencer-Brown distinction | 8 hits |
| 13 | SLB | laws of form distinction Spencer-Brown mark re-entrant calculus | 5 hits |
| — | KG | nodes label=Paper search=spin-statistics / search=braid | 1 + 5 nodes |
| — | memory | recall_facts("braid"), recall_facts("RES.009"), search_memories x2 | 7 + 10 facts |

**Adjacent WBS domains swept:** SLB (RES.009 home; reentrant-distinctions, void-is-not-false, prime-valuation-depth), UMP (p-adic braid/TL/anyon series, zbw-majorana), RES (audits). **>=2 domains satisfied.**

## 2. Key corpus hits + cross-system ID validation

| Slug | Vectorize | KG | D1/DOI | Verdict |
|---|---|---|---|---|
| spin-statistics-distinction | fa1765cb... | paper:spin-statistics-distinction (concept 10.5281/zenodo.21938970, v1.4=21944401, domain SLB, r2_path `qnfo-releases/2026/08/...`) | 10.5281/zenodo.21944401, r2_key `releases/2026/08/...` | CONSISTENT; SOFT: D1 r2_key bucket name vs KG (qnfo-releases) drift |
| configuration-space-topology | d8e05457... | (absent) | 10.5281/zenodo.21957291 | SOFT: identifier_type="arxiv", id=null (Zenodo record mislabeled) |
| p-adic-anyon-fusion-braiding | paper:...:0 + hashes | paper:p-adic-anyon-fusion-braiding | 10.5281/zenodo.21208491 | CONSISTENT; SOFT: identifier_type="arxiv", id="padic-anyons-phase3" |
| p-adic-braid-groups-bruhat-tits | paper:...:0 | present | 10.5281/zenodo.21208366 | CONSISTENT |
| p-adic-temperley-lieb-parameter | c9be5217... | — | 10.5281/zenodo.21208368 | CONSISTENT |
| zbw-majorana-tqc-p4-zbw-anyon-braiding | paper:...:0 | present | 10.5281/zenodo.21336087 | CONSISTENT |
| exchange-phase-logical-scalar | 3e2885f6... | — | 10.5281/zenodo.21941238 | CONSISTENT (sibling) |
| from-distinction-to-dissipation | 3a4ec011... | — | 10.5281/zenodo.21940822 | CONSISTENT (companion) |
| reentrant-distinctions | e5c1a5ed... | — | 10.5281/zenodo.21908818 | CONSISTENT (SLB flagship) |

All note-cited corpus tooling (21208491, 21208366, 21208368, zbw-majorana series) **verified live — no phantoms.**

## 3. External verification (P1b)

1. **Oeckl, hep-th/0008072** "The Quantum Geometry of Spin and Statistics" (2000) — REAL, on-topic (spin/statistics from quantum-group symmetries; Bose-Fermi + anyonic classification; braid-statistics path integrals). Appropriate for the note §2.
2. **Johnson-Freyd, 1507.06297** "Spin, statistics, orientations, unitarity" (2015) — REAL, on-topic (topological Spin-Statistics Theorem; reflection-positivity ⇒ Hermitian + spin-statistics). Appropriate.
3. **Bruillard DOI check (HARD finding):** the published T2 notebook cites "Bruillard 10.1007/s00220-009-0908-z". Crossref resolves that DOI to **Rowell, Stong, Wang, "On Classification of Modular Tensor Categories", Commun. Math. Phys. (2009)** — NOT Bruillard. Name/DOI MISMATCH in the published v1.4 notebook; the draft note inherits the bare name "Bruillard". (Same class as RES.007 joyal1986→joyalstreet1993.) Fix in the rigor pass / next citation-audit newversion: cite Rowell–Stong–Wang with that DOI, or pin the intended Bruillard work (e.g. Rank-4 premodular categories) with its own DOI.
4. **T2 notebook §2 live-verified** against Zenodo record 21944401 (29 files, artifacts_notebooks_t2.md 4,191 B): contains "## 2. Exchange as rotation — the ribbon identity", θ_X = quantum-trace(c_{X,X})/d_X, abelian (d_X=1) ⇒ θ_X = c_{X,X} = R_{XX} = e^{2πis}; citation trio present. The note's source-attribution is TRUE; SOFT-D1 (phantom t1-t2-dill-full-check.md dropped) confirmed in published file.
5. **Recipe source verified:** `_1786768950228.md` ("The Occam Objection, Sharpened") contains the exact parsimony-ledger framing: "the abelian-pair postulate is the silent assumption, relocated ... S_n is literally the quotient of B_n." Note §0 provenance is accurate.
6. Artin presentation S_n = B_n / ⟨σᵢ²=1⟩: textbook-standard ([KNOWN], Kassel–Turaev GTM 247); corroborated in-corpus by configuration-space-topology (21957291) + the recipe note's fact-check table (Leinaas–Myrheim 1977, Laidlaw–DeWitt 1971, π₁(C₂(ℝ³)) = ℤ₂, d≥3 ⇒ S_n).

## 4. Gap analysis — verdict per derivation-note claim

1. **§3 Involutivity from Crossing: SOUND (modulo F construction).** Crossing is the order-2 law; F functorial ⇒ σ² = id in the image of F ⇒ per-summand eigenvalues λᵢ = ±1. Note's own §5 item 2 (explicit construction of F) is the only open input. d≥3 specialization matches the CST sibling paper's π₁(S_N) reading.
2. **§2 Simplicity lemma ⇒ scalar exchange: INCOMPLETE AS STATED (HARD for the draft).** Schur per summand gives σ = ⊕ λᵢ·id_{Sᵢ}, NOT a single scalar. The uniformity step imports "abelian object (d_X = 1)" from the T2 ribbon identity — that IS the abelian-pair postulate. Physical M⊗M has TWO channels (Sym² = +1, Λ² = −1), so "σ = λ·id" is false for the physical case; it holds only per-channel or when M⊗M is simple (M invertible). Counterexample class: V⊗V for the 2-dim simple V of Rep(U_q(sl₂)), q generic — σ non-scalar. **"Consequence: abelian-pair demoted from axiom to theorem" OVERCLAIMS; the demotion is circular unless M⊗M-simplicity is itself derived.** As written, the note's own falsifiability test (F2) FAILS. The honest minimal postulate set remains {compact closure, self-duality, abelian pair (M⊗M simple), (symmetric braiding or Crossing-derived involutivity)} — consistent with the 2026-08-14 T1/T2 memory finding. This is the #1 rigor-pass task.
3. **§4 Reading (two 1-dim S_n characters ↔ Calling/Crossing): CONSISTENT** with T1 notebook + exchange-phase-logical-scalar (R = (−1)^{2s}, parity of 2s). Standard rep theory.
4. **§5 item 1** (End(M) ≅ ℂ; single-particle Hilbert space = simple M): correctly flagged open; needs category semantics.
5. **§5 item 4** (spin↔statistics needs Lorentz/microcausality/positive energy): consistent with paper §5 boundary, Johnson-Freyd, Oeckl. Correctly out of T2 scope.
6. **Novelty:** no corpus record performs the image-of-F involutivity derivation; closest are T2 §3 (assumes symmetric category), CST paper (topological route), exchange-phase-logical-scalar (algebraic reading). The note's route is distinct — but must cite Joyal–Street, "Braided Tensor Categories" (1993, 10.1006/aima.1993.1055 — the CORRECTED citation from RES.007 HARD-1) for the ribbon-category background, to avoid duplicate/synthetic-citation risk.
7. **Corpus contradictions:** none found. Complications surfaced: (a) T2-notebook §3 "σ acts as scalar η·id" vs physical two-channel picture (same tension as finding 2); (b) CST paper positions π₁ route as "correct kinematical explanation but not terminus" — the note's algebraic route is complementary, not competing; (c) D1 identifier_type anomalies (soft).

## 5. Findings summary

- **HARD-1 (draft):** §2 abelian-pair "demotion" is circular (uniformity imports d_X=1). F2 fails as written.
- **HARD-2 (citation):** Bruillard ↔ 10.1007/s00220-009-0908-z mismatch; DOI = Rowell–Stong–Wang (CMP 2009). Inherited by the note from published T2 notebook.
- **HARD-3 (infra):** qnfo-memory-mcp search_papers 1101 on all requests + enriched limit≥20 1101 (ray ids in §1).
- **SOFT-1:** D1 identifier_type="arxiv" on configuration-space-topology and p-adic-anyon-fusion-braiding (Zenodo records).
- **SOFT-2:** D1 r2_key `releases/...` vs KG r2_path `qnfo-releases/...` bucket-name drift for spin-statistics-distinction.
- **SOFT-3:** Note cites "Bruillard" bare (no identifier); pin the corrected work in the rigor pass.

## 6. Next-cycle recommendations (WBS-coded)

- [QNFO.RES.009.T2] Rigor pass on the derivation note: fix §2 (replace scalar-lemma with per-channel statement; prove or explicitly postulate M⊗M-simplicity; add U_q(sl₂) counterexample to §5), construct F explicitly, add Joyal–Street + Rowell–Stong–Wang citations.
- [QNFO.RES.009.P8] Citation-audit newversion item: Bruillard/Rowell–Stong–Wang fix in T2 notebook + paper references.
- [QNFO.RES.INFRA] Fix qnfo-memory-mcp Worker: clamp limit to Vectorize topK cap; fix base search_papers 1101.
- [QNFO.RES.DATA] D1 hygiene: identifier_type values; r2_key bucket naming.
