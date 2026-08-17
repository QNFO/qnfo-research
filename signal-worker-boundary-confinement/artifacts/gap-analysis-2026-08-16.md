# Phase 1 Due Diligence — Post-v0.2 Re-Sweep (2026-08-16)

**WBS:** QNFO.INM.001 — Signal-Worker Boundary Confinement
**Trigger:** CMD RESEARCH on `D:\Obsidian\notes\v1\2026\08\16\_26228215041.md` ("Quantum surface distinction")
**Phase 0 verdict:** EXISTING project (registry row QNFO.INM.001, v0.2 published 2026-08-16) → Phase 0 scaffold skipped per CMD.
**Protocol:** DUE-DILIGENCE-DEPTH-1 (HARD GATE) — corpus-scale sweep, cross-system ID validation, adjacent-domain breadth, external verification, evidence files.

---

## (a) QNFO Cross-Reference

**QNFO Cross-Reference: Found 14 related papers across 4 domains (corpus size 997 D1 living-paper; KG 8,293 nodes / 1,633 Papers).**

3-formulation Vectorize sweep + direct D1 title scans. Unique slugs with evidence files:

| Domain | Papers |
|:-------|:-------|
| INM (primary) | adaptive-thick-skin (17864277), gauge-invariant-field-theory-of-signal-worker-interactions (18466521), unifying-photosynthetic (18330365), signal-and-worker-how-proteins-activate-electrons (20329449), superfluid-substrate (17955974), thermodynamic-scaling-4-kelvin (17899087), thermodynamic-imperative (17928156), hamiltonian-engineering-weyl-semimetals |
| RES | electron-hook-treatise (21970454, RES.013), scale-invariant-physics (17216191), operationalizing-generalized-symmetries (18199396) |
| UMP | zbw-majorana-tqc-p1-zbw-padic-observable (21335853), thermodynamic-genesis-of-the-standard-model (18111349) |
| SLB-adjacent | spin-statistics lineage (RES.009/010/011) — referenced in project falsifiability register |

**Adjacent-domain note:** the seed note's thermodynamics thread (entropy primary → temperature derivative → G as inverse entropy density; frequency-as-count; Ostrowski: Archimedean reals are one completion) is RES.013 (electron-hook-treatise) + UMP territory, NOT INM.001. The note's surface-vs-bulk thread is INM.001. Both threads already have owners; no net-new project is warranted.

## (b) External Literature

Evidence files in `artifacts/external-search/` (this commit):

| File | Verdict |
|:-----|:--------|
| openalex-signal-worker-ontology.json | 43 hits; top hits = QNFO's own records. **"Signal-Worker ontology" is QNFO-proprietary externally** — MAP-level novelty holds. |
| openalex-bulk-boundary.json | 9,768 hits — TERRITORY mature. C1 (TI/QH boundary confinement) = established physics, no novelty claim. |
| openalex-anomalous-skin-effect.json | 16,981 hits — classical skin effect literature mature. |
| arxiv-nhse-search.json | NHSE literature mature AND experimentally realized (Schneider et al. 2505.03658, 2025). Founding paper Yao-Wang 1803.01876 = PRL 121, 086803 (Crossref-verified). |
| crossref-10_1103_PhysRevLett_121_086803.json | Verified: Yao & Wang, PRL 121, 086803 (2018-08-21). |
| crossref-10_1103_RevModPhys_82_3045.json | Verified: Hasan & Kane, RMP 82, 3045 (2010-11-08). |
| doi.org HEAD checks | concept 10.5281/zenodo.21931224 → 200 → records/21969297 (latest v0.2) ✓; v0.1 21931225 → 200 ✓; v0.2 21969297 → 200 ✓. Concept-DOI chain healthy (ZENODO-CONCEPT-DOI-CITE-1 satisfied). |

**Citation coverage check (v0.2 body):** Yao-Wang cited (`121:086803`) ✓; S-W siblings mentioned by title (9 combined matches: Photosynthetic / Proteins-Activate / Gauge-Invariant / Adaptive-Thick-Skin / Quantum-Abacus / Architectonics) ✓.

## (c) Gap Analysis

**Verdict: existing project confirmed at P8-complete; due diligence re-validates v0.2. Findings:**

1. **[GAP-NOVELTY] Novel in MAP, not TERRITORY** — the corrected ontology's category distinction (field expulsion vs mode confinement vs NHSE) is externally anchored; only the S-W correction layer is novel (externally proprietary, OpenAlex-verified). All territory claims must keep the "established physics" label (v0.2 already does per C1).
2. **[GAP-NHSE] NHSE as the third surface category** — the note's "category distinction survives the nanoscale" argument gains precision if NHSE is named as a distinct third category (non-reciprocal eigenstate localization ≠ classical skin ≠ topological boundary). v0.2 carries NHSE keywords + cites Yao-Wang; v0.3 candidate: cite 2505.03658 (experimental NHSE) + 2302.03057 (review).
3. **[DQ-1] D1 data-quality — adaptive-thick-skin**: `papers.doi` = NULL while body DOI = 10.5281/zenodo.17864277; `identifier_type`="arxiv" with internal id `qnfo-2025-12-adaptive-thick-skin` (not real arXiv). Same pattern: gauge-invariant-field-theory (18466521 body DOI, D1 NULL). → fix in a D1 backfill pass.
4. **[DQ-2] electron-hook-treatise resolve_paper_id**: `identifier` = "electron-hook-treatise" (slug) with `identifier_type`="zenodo" — identifier field carries slug, not DOI.
5. **[DQ-3] signal-worker-boundary-confinement resolve_paper_id**: `id` = null (no Vectorize ID surfaced) — verify v0.2 Vectorize chunking status before claiming semantic-search coverage.
6. **[KG-SEED-GAP] prog-qnfo-inm has exactly 1 Paper neighbor** (this project). The INM program's S-W founding papers (18330365, 18466521, 20329449) and NHSE sibling (17864277) are NOT BELONGS_TO-connected in the KG. Edge Seeding Gate: seed BELONGS_TO edges for ≥4 INM papers.
7. **[NOT-A-GAP] Meissner effect**: 0 D1 title-level papers, but discussed inside superconductor papers; no external gap (RMP/PRL territory mature).

## Phase 1b (next step)

KIF-29 Consilience gate (cross-domain lexicon + silo-cost table + synthesis) → then v0.3 planning from findings 1-6.

## Evidence Discipline

Every count above cites an evidence file in `artifacts/external-search/` (this commit) or a live tool call in the session tape (KG stats, D1 queries, resolve_paper_id, arXiv API).

## Remediation Status (2026-08-16, same-cycle fixes)

| Finding | Status | Evidence |
|:--------|:-------|:---------|
| KG-SEED-GAP (prog-qnfo-inm had 1 paper neighbor) | **FIXED** — 4 BELONGS_TO edges seeded via graph-api /sync (`edgesInserted: 4`, verified: 5 paper neighbors: signal-worker-boundary-confinement + unifying-photosynthetic + gauge-invariant + signal-and-worker-proteins + adaptive-thick-skin) | graph-api /query verify, this session |
| DQ-1 (D1 `doi` NULL on adaptive-thick-skin + gauge-invariant) | **FIXED** — targeted 2-row backfill, ownership live-verified against Zenodo API (creator Quni-Gudzinas, Rowan Brad; ORCID 0009-0002-4317-5604): adaptive-thick-skin doi=10.5281/zenodo.17864278 identifier=10.5281/zenodo.17864277; gauge-invariant doi=10.5281/zenodo.18466522 identifier=10.5281/zenodo.18466521; both identifier_type=zenodo; `changes: 5` per row + SELECT re-verification | D1 SELECT verify, this session |
| DQ-2 (electron-hook-treatise resolve identifier=slug) | **FIXED (2026-08-17)** — identifier backfilled to concept DOI 10.5281/zenodo.21970453 (ownership live-verified: creator Quni-Gudzinas, Rowan Brad / QNFO Research Foundation; conceptrecid=21970453; `changes: 5`); resolve_paper_id re-verification confirms. **NOTE (red-team A-2, 2026-08-17):** the record DOI advanced 21970736 → **10.5281/zenodo.21971503** (v0.2.2) via a concurrent-session publish AFTER the backfill; the concept identifier remains correct and version-agnostic (doi.org 21970453 → 200 → records/21971503) | Zenodo API + D1 SELECT + resolve_paper_id + doi.org HEAD, this session |
| DQ-3 (project resolve id=null — Vectorize chunking status) | **FIXED (2026-08-17)** — signal-worker-boundary-confinement indexed into Vectorize via qnfo-paper-indexer /webhook (31 chunks, 0 errors, `indexed:true`); papers.id backfilled `signal-worker-boundary-confinement` (`changes: 5`); paper_ids registry row upserted (vectorize_id + doi + zenodo_url, `changes: 1`); resolve_paper_id re-verification confirms | indexer /webhook + D1 SELECT + resolve_paper_id, this session |

Phase 1b (KIF-29/KIF-60 gates) — see `artifacts/consilience-gate.md` + `artifacts/bayesian-evidential-weight.md` (this commit). Phase 1 COMPLETE for the v0.3 cycle.

**Maintenance-pass notes (red-team SOFT closure, 2026-08-17):**
- **C-2 FIXED (2026-08-17)** — `zenodo_doi` + `zenodo_url` backfilled for adaptive-thick-skin (10.5281/zenodo.17864278) and gauge-invariant (10.5281/zenodo.18466522); ownership re-verified live (creators: Quni-Gudzinas, Rowan Brad) before write per ZENODO-KG-OWNERSHIP-1; SELECT re-verification confirms both rows.
- **C-3 noted** — D1's `meta.changes: 5` per single-row UPDATE is the tool's own counter, **not** an authoritative row-count; every fix in this table was re-verified with a SELECT (the trustworthy evidence). Do not report `changes:` counters as row counts.
- **D-1 (open, publish-gated)** — Vectorize index holds v0.2 body_md; re-index of v0.3 content happens at publish-time D1 update (P6). Correct to defer.

