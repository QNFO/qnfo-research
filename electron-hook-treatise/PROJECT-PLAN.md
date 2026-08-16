# PROJECT-PLAN — electron-hook-treatise (QNFO.RES.013)

> "A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation" (subtitle: The Electron as a Hook) · v0.1 · 2026-08-16

## Phase 0 — Context (2026-08-16)

- **Trigger:** user CMD PUBLISH with three Obsidian source notes (2026-08-16):
  `_26228215046.md` (detailed treatise outline), `_26228215041.md` (quantum surface /
  thermodynamics of scale note), `_26228180242.md` (copper-wire assumption audit note).
- **Corpus check:** no existing QNFO record for this title (D1 sweep + Zenodo DUPCHECK,
  `q="Electron as a Hook"` → 0 hits; token live-check 200). Related sibling:
  10.5281/zenodo.21777931 "Six Load-Bearing Assumptions" (different project, cited in gap analysis).
- **WBS:** RES.011 is the highest registered RES paper code; RES.012 (research-purpose-utility)
  exists in D1 living-paper but lacks its program_registry row → backfilled during this project;
  this project claims **QNFO.RES.013** (atomic check-then-insert, WBS-COLLISION-2).

## Phase 1 — Plan & due diligence

- Prior due diligence for the two research notes: `research-due-diligence-2026-08-16-copper-ultrametric.md`
  (Obsidian) — corpus sweep (995 D1 papers), cross-system ID validation, arXiv lineage for
  p-adic QM and non-Hermitian skin effect verified live.
- Gap analysis: `artifacts/gap-analysis.md`. The treatise's premise-chain depth: it introduces
  NO new physical postulate; premises are named (set theory, measurement practice, empirical
  adequacy). Its claims are taxonomic/analytical, bounded accordingly (SO-WHAT-GATE-1).

## Phase 2 — Sources

| Source | Role | Size |
|:-------|:-----|:-----|
| `source-notes/_26228215046.md` | treatise architecture (Part I basis) | 17.4 KB |
| `source-notes/_26228215041.md` | Research Note A (Part II basis) | 167.2 KB |
| `source-notes/_26228180242.md` | Research Note B (Part III basis) | 349.3 KB |
| `electron-hook-treatise.md` | assembled manuscript (Parts I–IV, 30 references) | 58 KB |

## Phase 3 — Citations

All 30 bibliographic entries live-verified (AUTHOR-GATE) via exact-DOI Crossref lookups
(`api.crossref.org/works/{doi}`) + arXiv abstract check for 't Hooft gr-qc/9310026. Evidence:
`artifacts/external-search/reference-verification.json`. Citation audit: `citation-audit.md`.

## Phase 4 — Draft

Manuscript assembled from the three notes (editorial rendering; originals deposited verbatim).
Gates: premise-depth disclosure in Abstract; SO-WHAT statement in Abstract; no internal
references (WBS codes, repo paths) in the rendered text; map–territory labels audited
(0 TERRITORY claims); terminology audit (BP-2) — every field term used in its standard sense;
BP-1 fit-verify PASS (skin depth, λ_T, G0, L0, Unruh prefactor recomputed).

## Phase 5 — Publication (Zenodo)

- Deposit API PATH A; ALL source files (21): `.md/.html/.pdf` + `references.bib` +
  `citation-audit.md` + `PROJECT-PLAN.md` + `README.md` + `docs/` + `artifacts/` +
  `source-notes/*` (3 original notes) + `RESEARCH-CONTINUITY-REGISTRY.md`.
- GitHub provenance: `related_identifiers` isSupplementTo →
  `https://github.com/QNFO/qnfo-research/tree/res/paper/electron-hook-treatise`.
- Verify: DOI live (curl -sI 200), P5.FRESH (deposited .md YAML doi=own DOI, status=published),
  title-duplication gate (PASS: 1 rendered title, 0 body H1), mojibake scan (CLEAN).

## Phase 6 — Distribution

- D1 living-paper insert (CHECK-THEN-WRITE; plain INSERT; body_md + PRE-inline body_html).
- KG node `paper:electron-hook-treatise` + BELONGS_TO edge; verify neighbors > 0.
- Vectorize index via qnfo-paper-indexer (`X-Index-Token`, browser UA); verify webhook
  `{indexed:true, chunks:N, errors:0}`.
- R2 mirror `qnfo-releases/2026/08/electron-hook-treatise/` (bucket verified against siblings).
- papers.qnfo.org route verify `curl -sI https://papers.qnfo.org/papers/electron-hook-treatise/` → 200.

## Phase 7 — Dissemination (deferred)

- Zenodo community inclusion REQUEST (advancedtheoreticalphysicsandmathematics or fbt-framework)
  per DISSEMINATION-OUTLETS-1 — post-publish curator-gated step.
- Internet Archive / SWH / IndexNow / Buffer socials — deferred to a follow-up cycle.

## Phase 8 — Audit

- Post-publication adversarial analysis (Accuracy/Completeness/Dependency) + red-team subagent;
  findings → `artifacts/post-publication-audit.md`; HARD findings → next newversion.
