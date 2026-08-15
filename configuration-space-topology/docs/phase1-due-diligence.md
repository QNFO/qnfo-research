# QNFO.RES.011 Phase 1 Due Diligence — Gap Analysis

**Project:** Configuration-Space Topology and the Distinction Calculus
**WBS:** QNFO.RES.011 — **Date:** 2026-08-15
**CMD RESEARCH cycle:** net-new project — Phase 0 committed (branch `res/paper/configuration-space-topology`, tag `v0.1-phase0-configuration-space-topology`, commit 9553512); Phase 1 executed per DUE-DILIGENCE-DEPTH-1.
**Source notes:** `D:\Obsidian\notes\v1\2026\08\15\` (CST thread, 26 files)

---

## 1. Protocol compliance record

| Step | Status | Evidence |
|:-----|:-------|:---------|
| Phase 0 (net-new only) | DONE — net-new confirmed | No D1 `program_registry` row, no KG Project node; WBS QNFO.RES.011 allocated (after RES.010), row inserted + re-verified; KG node `project:configuration-space-topology` + BELONGS_TO `prog-res` seeded + neighbor-verified |
| P1.1 KG /stats | DONE | 8,287 nodes / 8,425 edges; Paper 1,628; Project 151 (live 2026-08-15T07:45Z) |
| P1.2 Corpus sweep (≥3 formulations, limit ≥20) | DONE — with fallback | `qnfo-memory-mcp_search_papers` + `search_papers_enriched` worker DOWN (Error 1101, zone qnfo-memory-mcp.q08.workers.dev, retryable:false — same GAP-1 as prior RES.009 cycle). Fallback per prior-cycle protocol: direct D1 living-paper LIKE sweep (3 formulations × 21 patterns, LIMIT 40) + recall_facts (2 keyword sweeps) + KG Paper node searches (braid ×5, configuration ×0) |
| P1.3 Cross-system ID validation | DONE | resolve_paper_id × 8: 7 resolved clean (see §3); 1 known gap |
| P1.4 External verification | DONE | arXiv (3 formulations, 15 each), OpenAlex (3), Crossref (3); 6 JSON evidence files saved + arxiv-evidence.json (see §4) |
| Adjacent WBS domains (≥2 required) | SATISFIED (4) | SLB, UMP, INM, RES |
| Tool deviations | LOGGED | GAP-1 (worker 1101, owner action required); tyranny-of-the-plus-minus-one D1-absent (known) |

## 2. QNFO cross-reference summary

**Corpus size:** 1,628 Paper nodes (KG). **Sweep result: 14 unique hits across 4 domains.**

| Domain | Hits | Records |
|:-------|:-----|:--------|
| SLB | 2 | reentrant-distinctions (21908818, SLB.002 treatise), cancellation-rule (21470438) |
| UMP | 5 | p-adic-braid-groups-bruhat-tits (21208366), p-adic-temperley-lieb-parameter (21208368), p-adic-anyon-fusion-braiding (21208491), zbw-majorana-tqc-p4-zbw-anyon-braiding (21336087), adelic-synthesis-pattern-particle (21208568) |
| INM | 4 | quantum-laws-of-form (21206074), qlof-superposition-as-re-entry (21205110), the-calculus-of-distinction (21205097), qlof-syntactic-foundation (19598745) |
| RES | 3 | spin-statistics-distinction (21939493→21941375), exchange-phase-logical-scalar (21941238), universal-ignorance-audit (21901984, memory-verified) |

**Corpus-level observations:**
1. **No corpus record treats configuration-space topology as a subject** — CST appears only as imported mathematical background in the p-adic braid series and RES.009/010. The CST *layer itself* (Leinaas–Myrheim framework, π₁(C_N(M)), its scaffolds) is corpus-absent → this project occupies a genuine internal gap.
2. **GT/HoTT layer completely absent from the corpus** — zero hits for Grothendieck–Teichmüller (recall_facts "Teichmuller" = 0 rows) and no HoTT record. The C2 synthesis layer is net-new internally.
3. **Braid-group machinery is corpus-native (UMP)** — p-adic braid groups on Bruhat–Tits buildings, p-adic Temperley–Lieb parameter, p-adic anyon fusion — the arithmetic twin of the GT/braided-category claim already exists inside QNFO (see KIF-29 convergence map).
4. **The distinction-calculus side is rich** (SLB.002 treatise, RES.010 exchange phase, INM quantum-laws-of-form series) — all the pieces of the bridge exist internally; the bridge itself does not.

## 3. Cross-system ID validation (resolve_paper_id per hit)

| Slug | D1 DOI | KG ID / Vectorize | R2 | Verdict |
|:-----|:-------|:------------------|:---|:--------|
| spin-statistics-distinction | 21939493 (zenodo 21941375) | identifier qnfo | releases/2026/08/spin-statistics-distinction/ | ✅ consistent |
| exchange-phase-logical-scalar | 21941238 | identifier qnfo | releases/2026/08/exchange-phase-logical-scalar/ | ✅ |
| reentrant-distinctions | 21908818 | paper:reentrant-distinctions | releases/2026/08/reentrant-distinctions/ | ✅ |
| p-adic-braid-groups-bruhat-tits | 21208366 | padic-anyons-phase1 (arxiv-type) | — | ✅ |
| p-adic-anyon-fusion-braiding | 21208491 | padic-anyons-phase3 (arxiv-type) | — | ✅ |
| adelic-synthesis-pattern-particle | 21208568 | padic-anyons-phase4 (arxiv-type) | — | ✅ (new find) |
| zbw-majorana-tqc-p4-zbw-anyon-braiding | 21336087 (zenodo 21214358) | arxiv-type | papers/zbw-majorana-tqc-p4-zbw-anyon-braiding.md | ✅ |
| quantum-laws-of-form | 21206074 (zenodo 21206166) | arxiv-type + 3 KG asset nodes | papers/qnfo-2026-04-quantum-laws-of-form.md | ✅ |
| tyranny-of-the-plus-minus-one | **D1 empty** | KG node healthy (kind popular-essay, distributed, r2_path set) | mirrored | ⚠️ KNOWN state (policy observation, not defect — matches prior cycle finding) |

**No new inconsistencies found.** 8/8 resolved; 1 known D1-absence.

## 4. External verification (evidence files in `artifacts/external-search/`)

Files: `openalex-f1|f2|f3-*.json`, `crossref-f1|f2|f3-*.json`, `arxiv-evidence.json` (7 total).

### F1 — Configuration-space topology / exchange statistics / braid group
- **ESTABLISHED, textbook-grade, and actively extended.** arXiv: traid-group program (Harshman & Knapp 2018, 2021 [PRA 105.052214]; Nagies et al. 2023 lattice model), graph-configuration-space statistics (Harrison–Keating–Robbins–Sawicki 2013; Sawicki 2014; Maciążek–Sawicki 2018; Maciążek 2019), Sati–Schreiber TED K-theory of configuration spaces (2022–2024), Jacak's braid-group holographic proposal (2017, physics.gen-ph, low authority). OpenAlex confirms: 2,750 works match; the top physics hit is the Harshman–Knapp 1D orbifold paper; extended-object configuration spaces exist (2012, doi:10.1007/978-3-0348-0448-6_19).
- **Complications for the project:** (a) the hard-core-diagonal scaffold is *being dissolved* externally (orbifold treatment of singular points — Harshman–Knapp); (b) the braid-group classification is *being generalized* (traid group in 1D); (c) the "3D problem" thread has an external analog (Jacak's holographic braid proposal — low authority, but it exists).

### F2 — Grothendieck–Teichmüller group / braided monoidal categories
- **Mature but narrow and disconnected from physics.** OpenAlex: 36 works, dominated by operads/graph complexes (survey 1904.13097; little discs operads 1811.12536/2006.13663; VOA-parenthesized braid operad 2209.10443). Crossref: braided/symmetric monoidal category literature (Joyal–Street lineage, Morrison–Penneys IMRN 2017, etc.). **Zero** works connect GT to exchange-statistics physics or to any distinction calculus.
- **Risk R1 confirmed (HIGH):** C2's mathematical ingredients are fully mature externally. The novelty can only be claimed on the *route* (distinction calculus → braided monoidal category → GT action → statistical phase as arithmetic act), never on the objects.

### F3 — Laws of Form / Spencer-Brown × spin-statistics
- **Absence confirmed across three independent sources.** OpenAlex top-10 = classic spin-statistics literature (Streater–Wightman 1964/2001, Pauli 1940, Finkelstein–Rubinstein 1968, Wilczek 1983, Read–Green 2000) with zero LoF connection. Crossref = German LoF reception/system-theory literature (no physics). arXiv = noise (OR-tokenization) — consistent with the prior RES.009 cycle's 3-formulation arXiv check (only Mund/Kuckert/Oeckl, nothing deriving statistics from a distinction calculus).
- **The claim "no published derivation of exchange statistics from the mark calculus exists" STANDS** — the exact gap RES.009 pre-registered and this project inherits.

## 5. Novelty verdict

| Claim | Status | Basis |
|:------|:-------|:------|
| C1 (kinematical): CST = correct modern explanation of boson/fermion/anyon trichotomy, with scaffolds | [ESTABLISHED] + [CONTESTED boundaries] | External: Leinaas–Myrheim 1977, Laidlaw–DeWitt 1971 (canonical refs from RES.009 cycle); active extension literature (traid/orbifold/graphs) proves the boundaries are live research |
| C2 (synthesis): Distinction Calculus lifted into HoTT, GT action on braided monoidal categories, boundary-drawing = arithmetic act | [CONJECTURE] — internally novel, externally must-differentiate | GT+braided-category math mature (F2); HoTT×anyons×config-spaces **already exists** (Sati–Schreiber 2022–2024, cohesive HoTT + TED K-theory + topological quantum programming); no external work routes *through a distinction calculus* |
| C3 (boundary): spin-statistics connection needs Lorentz/microcausality/positivity | [ACKNOWLEDGED] — externally unanimous | F3 evidence: every external derivation uses QFT machinery |

**Verdict:** The project is **novel in its route, not in its ingredients**. The gap it occupies — a distinction-theoretic derivation program for exchange statistics, positioned against CST — is open both internally (no CST/GT/HoTT corpus record) and externally (no LoF×statistics literature). The C2 formulation MUST engage the Sati–Schreiber program explicitly (cite + differentiate) or it will read as a restatement of their HoTT-anyon work.

## 6. Confirmation-bias disclosure

- Internal hits are **mixed-domain** (SLB/UMP/INM/RES) — not a self-citation echo chamber for the CST claim itself: the CST-framework hits are **external**, the distinction-calculus-route hits are **internal-only**.
- `[CONFIRMATION-BIAS-RISK]` concentrates exactly where novelty is claimed: the LoF×statistics route has **zero external corroboration** (F3). Phase 2 must actively search *against* it (falsifier literature: parastatistics, Gentile statistics, anyon alternatives in 3D via extended objects) — F1's extended-object work is the first such counter-literature found.

## 7. Institutional Status Neutrality (KIF-16)

No institutional-status language used. External proposals with low corroboration are labeled by evidence status: Jacak 2017 = [UNTESTED conjecture, physics.gen-ph]; traid group = [CONTESTED scope — 1D-only, experimentally unconfirmed]; Sati–Schreiber TED-K = [CONTESTED — program under development, not yet standard].

## 8. AI Convergence Bias (KIF-17)

Not triggered in the HARD sense: the dismissal risk for C2 comes from *shared training-data priors* (HoTT and GT are well-represented in AI training corpora, so "this exists already" convergence is expected). Flag `[AI-CONVERGENCE-WARNING]` for any future AI reviewer that dismisses C2 purely on "GT is known math" grounds without engaging the distinction-calculus route.

## 9. Silo-failure detection (KIF-29) — convergence map

| Thread | Merge target | Status |
|:-------|:-------------|:-------|
| CST (this project) | RES.011 paper: CST as the geometric substrate; scaffolds as the boundary of the map | ACTIVE |
| RES.010 exchange phase R=e^{2πis} | RES.011 C2: R as the invariant whose 3D shadow is ±1; CST provides the kinematical arena | Published; inherits |
| RES.009 spin-statistics T1–T3 | RES.011 C3 boundary + F2/F3 conditions (S_n ≅ B_n/⟨σ²=1⟩ connection belongs here) | Published; inherits |
| UMP p-adic braid series (BT buildings, Temperley–Lieb, anyon fusion) | RES.011 C2 arithmetic side: "drawing a boundary is an arithmetic act" has a corpus-native p-adic twin | Published; must cite |
| INM quantum-laws-of-form series | RES.011 C2 logical side | Published; must cite |
| SLB.002 void-is-not-false + reentrant-distinctions | RES.011 C2 foundation (the mark, the loop, the constants) | Published; must cite |

**Silo check:** no thread is being worked in isolation — every merge target is an existing published branch. The single new deliverable is the bridge document (CST ↔ distinction calculus ↔ GT/HoTT) with the pre-registered derivation targets inherited from RES.009 (T1–T3) and the falsification conditions F1–F3.

## 10. Recommendations for Phase 2 (Literature Search & Triage)

1. **Engage Sati–Schreiber program** as primary external anchor for C2 (2206.13563, 2209.08331, 2408.11896) — differentiate the distinction-calculus route from cohesive-HoTT/TED-K.
2. **Anchor the GT side:** Drinfeld 1990 (original), survey 1904.13097, little-discs operad lineage — establish that GT's action on braided monoidal categories is the *standard* structure C2 claims, and that no one has sourced it from a mark calculus.
3. **Anchor the CST side:** Leinaas–Myrheim 1977 + Laidlaw–DeWitt 1971 (canonical, from RES.009 citation set); Harshman–Knapp orbifold (2108.05653) and traid group (2309.04358) as the active-extension counter-literature.
4. **Search *against* the claim:** parastatistics (Green 1953), Gentile statistics, anyons in 3D via extended objects (10.1007/978-3-0348-0448-6_19), Haldane exclusion — pre-register their existence as F1/F2-adjacent falsifiers.
5. **Include the holographic thread** (Jacak 1704.06560, LOW authority) only as a labeled [UNTESTED] parallel to the notes' "3D problem" — do not cite as support.
6. **Evidence discipline:** extend `artifacts/external-search/` per source; every count/DOI in the Phase 2 report must point at a saved file.

## 11. Tool gaps logged

- **GAP-1 (repeat):** qnfo-memory-mcp worker 1101 on ALL endpoints (search_papers, search_papers_enriched) — owner action required; D1-LIKE fallback used. This is the second cycle affected; escalate as infrastructure debt.
- **GAP-2:** tyranny-of-the-plus-minus-one D1-absent (KG+R2 only) — policy observation, unchanged.
- **GAP-3:** portfolio-state D1 query path via direct REST worked this cycle (no 400) — prior cycle's 400 was not reproduced; d1-query.py canonical path confirmed working.

---
*Compliance: DUE-DILIGENCE-DEPTH-1 satisfied (stats-first; ≥3 formulations × limit ≥20; resolve_paper_id per hit; ≥2 adjacent domains [4]; external verification on 3 sources + archive evidence; every count backed by a saved evidence file).*
