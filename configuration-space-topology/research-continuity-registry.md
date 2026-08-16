# Research Continuity Registry — QNFO.RES.011

**Protocol:** research skill v2.64 (Research Continuity Registry Protocol, HARD)
**Created:** 2026-08-15 (remediation cycle, post-publication audit)

---

## 1. Project identity

| Field | Value |
|:------|:------|
| WBS code | `QNFO.RES.011` |
| Slug | `configuration-space-topology` |
| Name | Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its +/-1 Shadow, and a Pre-Registered Derivation Program |
| Repo | `QNFO/qnfo-research` |
| Branch | `res/paper/configuration-space-topology` |
| Program | QNFO.RES (QNFO Research Archive) |

## 2. Publication chain

| Version | DOI | Zenodo ID | Date | Status |
|:--------|:----|:----------|:-----|:-------|
| v0.1-phase5 (initial) | 10.5281/zenodo.21945450 | 21945450 | 2026-08-15 | published |
| Concept DOI | 10.5281/zenodo.21945449 | (concept) | — | — |
| v0.2 (remediation newversion) | 10.5281/zenodo.21957291 | 21957291 | 2026-08-15 | published |
| v0.3 (corrected & expanded) | 10.5281/zenodo.21962450 | 21962450 | 2026-08-16 | published |

**Remediation status (2026-08-16, v0.3 cycle):**
- HARD-1 (stale frontmatter self-DOI): v2's deposited .md still carried the v1 DOI (`21945450`) — re-verified by direct download 2026-08-16; FIXED FOR REAL in v0.3 (frontmatter `doi: 10.5281/zenodo.21962450`, P5.FRESH pre-upload patch).
- HARD-2 (no "So what?" section): v0.3 adds Section 2 — "So What? Why Should a Reader Care About This Research?" (user mandate 2026-08-16).
- HARD-3 (empty References in .md): v0.3 renders the complete 42-entry bibliography in the markdown body (rebuilt from references.bib).
- SOFT-1 (EuroSciVoc subjects): carried forward in v0.3 metadata (philosophy + mathematics, verified URIs).
- SOFT-4 (README status stale "Phase 0 scaffold"): corrected to published v0.3.
- SOFT-5 (INTERNAL-REF-1): WBS code `QNFO.RES.011` removed from byline + acknowledgements.

## 3. Predecessor linkage

| Record | DOI | Relation |
|:-------|:----|:---------|
| RES.009 spin-statistics-distinction | 10.5281/zenodo.21944401 (v1.4) | BUILDS_ON (cites) |
| RES.010 exchange-phase-logical-scalar | 10.5281/zenodo.21941238 | BUILDS_ON (cites) |
| SLB.002 reentrant-distinctions | 10.5281/zenodo.21908818 | foundation (cites) |
| Tyranny of the ±1 (v3) | 10.5281/zenodo.21939692 | background (cites) |

## 4. Phase state machine

| Phase | WBS | Status | Commit/DOI |
|:------|:----|:-------|:-----------|
| P0 Init | QNFO.RES.011.P0 | done | 9553512, tag v0.1-phase0-configuration-space-topology |
| P1 Due Diligence | .P1 | done | ac2bfa8 |
| P2 Literature & Triage | .P2 | done | b90df3c |
| P3 Citation Management | .P3 | done | 0fd4e44 |
| P4 Deep Research & Forecast | .P4 | done | bfe75d2 |
| P5 Publication | .P5 | done | c03d351, a327260, 06b5f66; DOI 10.5281/zenodo.21945450 |
| P6 Cloudflare Deployment | .P6 | done | 06b5f66 (D1/KG/Vectorize/R2 verified) |
| P6R Remediation (audit) | .P6R | in progress | this cycle |
| P7 Dissemination | .P7 | pending | journal/outreach/SEO/social |
| P8 Core Distribution | .P8 | pending | IPFS/DNSLink/Internet Archive/4-D props |

## 5. Verification anchors (as of 2026-08-15)

- D1 living-paper: row `configuration-space-topology` (doi, status=published) verified via SELECT
- D1 program_registry: phase P6, zenodo_doi set, verified
- KG: node `paper:configuration-space-topology` + BELONGS_TO prog-res + BUILDS_ON (RES.009/RES.010); neighbors count 6 verified
- Vectorize: 42 chunks, 0 errors (webhook `{"indexed":true}` at index time; unchanged-skip on re-check)
- R2: 15/15 objects at `qnfo-releases/2026/08/configuration-space-topology/`
- Zenodo: 15 files; doi.org 200; DataCite findable

## 6. Next actions

1. Zenodo newversion of concept 21945449 with patched md + EuroSciVoc subjects → publish → 3-layer verify.
2. Update D1 body_md + R2 mirror with patched md.
3. P7: journal submission, targeted outreach, SEO, social (Buffer).
4. P8: IPFS/DNSLink, Internet Archive, 4-D distribution props.
