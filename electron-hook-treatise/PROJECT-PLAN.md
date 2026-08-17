# PROJECT-PLAN — electron-hook-treatise (QNFO.RES.013)

> "A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation" (subtitle: The Electron as a Hook) · v0.2 · 2026-08-16/17

## Version ledger

| Version | DOI | Scope |
|:--------|:----|:------|
| v0.1 | 10.5281/zenodo.21970454 | Architecture (Parts I–IV) + two research notes; 21 deposit files |
| v0.2 | 10.5281/zenodo.21970697 | Full Edition: 9 parts, 51 chapters, 34 six-step audits; 25 deposit files |
| v0.2.1 | 10.5281/zenodo.21970736 | §0.4/Preface prose correction (Chapter 51 reference); 26 deposit files |
| v0.2.2 | 10.5281/zenodo.21971503 | Bibliography extension (30 → 42 live-verified entries) + 19.4 phrasing fix; 27 deposit files |
| **v0.3** | **10.5281/zenodo.21972676** | **Depth expansion: Part VIII + Appendices A–C + 6 core chapters to prose (11.8k → 17.5k words); Abstract overclaim corrected; 28 deposit files** |

## Phase 0 — Context

- Trigger (v0.1): user CMD PUBLISH with three Obsidian source notes (`_26228215046.md` outline; `_26228215041.md` quantum-surface note; `_26228180242.md` copper-wire audit note). Zenodo DUPCHECK clean; WBS QNFO.RES.013 claimed (check-then-insert; RES.012 backfilled).
- Trigger (v0.2): user CMD "GENERATE full treatise: nine parts and fifty-one chapters" + CMD RED TEAM SUB + CMD EXECUTE.

## Phase 1 — Plan & due diligence

- v0.1 due diligence: `research-due-diligence-2026-08-16-copper-ultrametric.md` (corpus sweep 995 papers; arXiv lineage verified live).
- Premise-depth: no new physical postulate; primitives named (set theory, measurement practice, empirical adequacy). SO-WHAT in abstract.

## Phase 2 — Sources

v0.1 manuscript (preserved as `electron-hook-treatise-v0.1.md`) + the three verbatim source notes. Full Edition expands the v0.1 architecture chapter by chapter.

## Phase 3 — Citations

30 entries, AUTHOR-GATE verified two-phase (exact-DOI Crossref + arXiv for 't Hooft). Evidence: `artifacts/external-search/reference-verification.json`; audit: `citation-audit.md`; Full Edition Appendix D carries the inline bibliography.

## Phase 4 — Full Edition + red team

- Generated: 9 parts, 51 chapters, 31 six-step blocks (v0.2 adds §9.5–9.7 → 34).
- Red team (3 slots): Accuracy (failed → direct audit), Completeness (1 HARD / 5 SOFT / 1 DESIGN), Dependency (stalled → direct audit). Findings remediated; closure log: `artifacts/v0.2-red-team-remediation.md`; aggregate: `artifacts/red-team-full-edition.md`; re-verification reviewer dispatched (9imUglD3ekqerRhMm_c3R).

## Phase 5 — Publication (v0.2 newversion)

- Records API newversion from 21970454 → draft 21970697; reserved DOI 10.5281/zenodo.21970697.
- Frontmatter patched to own DOI + status published BEFORE upload (NEWVERSION-FRONTMATTER-CARRYOVER-1).
- Full fresh upload (25 files) — draft carried 0 files (records-API newversion did not migrate the parent bucket).
- Metadata: concept DOI cite-awareness (ZENODO-CONCEPT-DOI-CITE-1); related_identifiers isSupplementTo (GitHub branch) + isVersionOf (10.5281/zenodo.21970454).
- Verify: DOI HEAD 200; P5.FRESH (deposited .md own-DOI + published); 25 files.

## Phase 6 — Distribution (v0.2)

- D1 living-paper row re-pointed (doi, zenodo_url, version 0.2.0, body_md/body_html = Full Edition).
- KG node properties updated (doi/version); Vectorize re-index + webhook verify.
- R2 mirror update `qnfo-releases/2026/08/electron-hook-treatise/` (rclone check 0 differences).
- papers.qnfo.org route 200. program_registry zenodo_doi + current_version updated.

## Phase 7 — Dissemination (deferred)

Zenodo community inclusion REQUEST (curator-gated); IA/SWH/IndexNow — follow-up cycle.

## Phase 8 — Audit

Post-publication adversarial analysis for v0.2 (`artifacts/post-publication-audit.md` updated); HARD findings → next newversion.
