# Due Diligence — Phase 1
## QNFO.RES.010 — The Exchange Phase as a Logical Scalar

**Date:** 2026-08-14 | **WBS:** QNFO.RES.010 | **Branch:** res/paper/exchange-phase-logical-scalar
**Method:** KG stats + full-corpus sweep (4 query formulations, Vectorize+D1 enriched bodies, D1 fact recall, durable memory) + cross-system ID validation (resolve_paper_id) + ≥2 adjacent WBS domains + external verification (Crossref ✓, arXiv 429, Google Patents 503) + gap analysis.
**Depth gate (DUE-DILIGENCE-DEPTH-1):** ~1,000-record corpus baseline: KG 8,285 nodes / 1,626 Paper nodes; Vectorize+D1 sweep returned 20+ hits across 4 formulations; D1 fact recall 15 rows; durable memory 8 rows.

---

## 1. Corpus baseline

- **KG:** 8,285 nodes (1,626 Paper) / 8,423 edges. Query `query_graph(stats)`.
- **Vectorize+D1 (search_papers_enriched):** 4 formulations × 5 hits = 20 results, deduped to these canonical hits:
  | Slug | DOI | Role |
  |---|---|---|
  | spin-statistics-distinction | 10.5281/zenodo.21938971 (D1: 21939493) | Parent claim [ESTABLISHED] (RES.009) |
  | reentrant-distinctions | 10.5281/zenodo.21908818 | Parent machinery (treatise; KG home: QNFO.SLB) |
  | p-adic-anyon-fusion-braiding | 10.5281/zenodo.21208491 | Adjacent (UMP): non-archimedean anyons |
  | syntactic-token-calculus (v3 / plan) | 10.5281/zenodo.19547736 / 21206272 | Predecessor calculus lineage (SLB) |
  | quantum-correlation-synchronization…gravity | 10.5281/zenodo.17152806 | Tangential (Compton-frequency) |
  | conditional-state-distances-pw-clocks | 10.5281/zenodo.21120286 | Tangential (Page-Wootters) |
- **D1 facts / durable memory:** RES.009 Phase-0/1/P1b-P4/publish memories; RES.009 T1/T2 minimal-postulate finding (compact closure + self-duality + abelian pair + symmetric braiding; Lorentz/microcausality external); Re-entrant spinoff session 2026-08-12 (SLB.001/002 + 5 scoped spinoffs — none claims exchange-phase); ZBW-Majorana-TQC P1–P6 (P4: p-adic anyon braiding bridge); Consilient Synthesis 2026-07-24 ("anyons are adelic objects" conjecture).

## 2. Cross-system ID validation (resolve_paper_id)

| Input | Slug | Vectorize id | KG id | DOI | R2 key |
|---|---|---|---|---|---|
| spin-statistics-distinction | ✓ | 742cf44e… | — | 21939493 (D1) / 21938971 (body) | null |
| reentrant-distinctions | ✓ | e5c1a5ed… | paper:reentrant-distinctions | 21908818 | releases/2026/08/reentrant-distinctions/ |
| invariant-structural-value | ✓ | — | — | 21929902 | releases/2026/08/invariant-structural-value/ |
| syntactic-token-calculus-research-plan | ✓ | — | — | 21206272 | papers/qnfo-2026-04-… |

Note: spin-statistics D1 row carries DOI 21939493 (a newer version) while the published body frontmatter carries 21938971 — both resolve to the same Zenodo concept (21938970). No identifier mismatch blocks Phase 2.

## 3. Adjacent WBS domains (≥2 required — 3 confirmed)

1. **QNFO.SLB (Laws of Form)** — the treatise is KG-registered under `prog-qnfo-slb` (BELONGS_TO edge, verified via `query_graph(neighbors)`); STC lineage; SLB.001/002 spinoffs. RES.010's machinery (re-entry, half-turn, mark) is SLB-native.
2. **QNFO.UMP (Ultrametric Physics)** — p-adic-anyon-fusion-braiding (21208491) constructs anyon models at roots of unity on Bruhat–Tits buildings; ZBW P4 identifies p-adic anyon braiding as ZBW's physical realization; the 2026-07-24 synthesis conjectures "anyons are adelic objects". RES.010 supplies the Archimedean (geometric) reading of the same invariant R.
3. **QNFO.INM (Infomatics)** — treatise Part VII (entropy/statistics as distinction counting) and the Compton-frequency clock (Part VI §24) give the informational reading of the re-entry clock underlying the half-turn.

## 4. External verification

- **Crossref (3 queries, verified live):**
  - `"spin statistics" "laws of form"` → 8 results, **zero** combine spin-statistics with Laws of Form/Spencer-Brown. All irrelevant (transformations, elliptical laws, black-hole dynamics, narrative theory).
  - `"exchange phase" "half-turn" spin statistics` → surfaced **"Spin-half bosons with mass dimension three-half: Evading the spin-statistics theorem"** (EPL 2023, 10.1209/0295-5075/ac97bd + erratum acabe2) — a real evasion-strategy paper; P2 must classify (likely Core for the F2 discussion). Also "Indistinguishability for quantum particles: spin, statistics and the geometric phase" (book chapter, 10.1142/9789813221215_0008) — geometric-phase approach, adjacent but not mark-calculus.
  - `Spencer-Brown exchange statistics boson fermion` → 8 results, **zero** Spencer-Brown/laws-of-form exchange-statistics work.
  - **Novelty verdict (Crossref-anchored):** no prior art derives exchange statistics from the Laws of Form / re-entrant mark. RES.010's specific identification R = (e^{iπ})^{2s} has no external prior.
- **arXiv:** `abs:"exchange phase" AND abs:"topological spin"` → HTTP 429 (rate-limited at IP level; MCP also 429/timeout). `[NOT-VERIFIED this turn — re-run in P2 with pacing]`
- **Google Patents:** generic `exchange phase spin statistics` = 142,472 results (expected: QC/anyon patent space). Targeted phrase queries (`"exchange phase" "half-turn"`, `"spin statistics" "laws of form"`, `"calculus of indications"`) → HTTP 503 rate-limit after first call. `[NOT-VERIFIED this turn — re-run in P2 with ≥25 s pacing]`
- **archive.org CDX:** N/A — no third-party prior-art date claim to verify (the PROVENANCE-ACCUSATION-1 scenario does not apply here).

## 5. Gap analysis

- **G1 — Closest internal prior (RES.009 t2.md, notebook):** the braiding of two marks in a compact closed category yields η = ±1 (symmetric braiding), with η = −1 identified with the treatise crossing e^{iπ} = −1 and η = +1 with Calling; ribbon identity η = θ_M. **RES.010 delta:** (a) the explicit **(2s)-fold power structure** R = (e^{iπ})^{2s} = (−1)^{2s} — RES.009 stops at η = ±1 (the symmetric case) and never writes the power form that covers 2+1D anyons with arbitrary s; (b) the **unification of e, π, R as one family of logical scalars** (fixed point / trace / monodromy power) — not stated in any prior artifact; (c) the **formal derivation target in traced differential cohesive linear HoTT** (treatise Part VIII, §36) — RES.009 explicitly documented its boundary ("paper does not claim full derivation"; Lorentz/microcausality input external to the mark).
- **G2 — External evasion literature:** "Spin-half bosons with mass dimension three-half" (EPL 2023) must be engaged in the paper's falsifiability section: it attacks the standard spin-statistics theorem via mass-dimension-3/2 spinor constructions, not via the invariant R itself — RES.010's F2 (inherited from RES.009) already anticipates the general evasion class.
- **G3 — Geometric-phase literature:** the Berry/geometric-phase reading of indistinguishability (book chapter above) is the closest external conceptual neighbor; RES.010's monodromy-power reading is a distinct, Laws-of-Form-native formulation. P2 classification: Supporting.
- **G4 — Non-archimedean counterpart:** the UMP anyon program (p-adic braiding, quantum groups at roots of unity) is the tree-side of the loop/tree duality; RES.010's half-turn power is the loop-side reading of the same invariant. Consilience bridge to be developed in P4 (KIF-29 lexicon).
- **G5 — Parent boundary honored:** the treatise's §2.3 marks "parity is the ancestor of physical spin-statistics" as [my conjecture] and never delivers; RES.009 sets the derivation target. RES.010's core claim inherits the [my conjecture] status for the logical-derivation component (F1) while keeping the arithmetic identity and the physics invariant at [established] (F2/F3 ladder) — consistent with the publication-language gate.
- **G6 — Registry gap (kaizen):** reentrant-distinctions has no `program_registry` row (KG-only). Recommend retroactive registration under QNFO.SLB.
- **G7 — Tooling outages:** qnfo-memory-mcp `search_papers` Worker throws Error 1101 (unhandled exception); arXiv API 429; Google Patents XHR 503 after first call. All three logged for remediation; workarounds used (search_papers_enriched, Crossref).

## 6. Verdict

**Net-new confirmed.** The arithmetic core (R = (−1)^{2s}, parity of 2s) is elementary and the physics invariant is [ESTABLISHED] (RES.009 + mainstream), but the specific claim — *the exchange phase as the (2s)-fold half-turn of the re-entrant mark, generated alongside e and π as logical scalars of the calculus* — appears in no internal corpus artifact and no external source found by Crossref. Closest prior: RES.009 t2.md (η = ±1 only) and the treatise §12.1 (the single half-turn). The delta (power structure, scalar-family unification, Part-VIII derivation target) is the project's novelty claim, correctly scoped as [my conjecture] at the derivation level.

**Phase 1 gate:** PASS — proceed to P2 (literature classification) with G1–G5 as the classification frame and G7 re-runs scheduled.
