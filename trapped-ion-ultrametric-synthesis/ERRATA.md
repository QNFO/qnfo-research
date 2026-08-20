# ERRATA — QNFO.RES.017 Trapped-Ion Ultrametric Testbed

Version-history errata trail for the published synthesis record. This file is the
repo-level ERRATA trail referenced in handoff 28629 (2026-08-19); the authoritative
audit-log entries live in `qnfo-audit.audit_trail` (project_id `QNFO.RES.017`,
task_ids `ERRATA-v1.1`, `ERRATA-v1.2`, `ERRATA-v1.3`, `REGISTRY-SYNC`).

## Record versions

| Zenodo version | Record DOI | Status | Notes |
|:---------------|:-----------|:-------|:------|
| v1.0 | 10.5281/zenodo.22013264 | published (historical) | Original publication, 2026-08-19 |
| v1.1 | (superseded) | published (historical) | Carryover incident — see below |
| v1.2 | (superseded) | published (historical) | Carryover incident — see below |
| v1.3 | 10.5281/zenodo.22017933 | published (current) | Red-team remediation; concept DOI 10.5281/zenodo.22013263; DataCite findable; doi.org HEAD 200 |

## Carryover incidents (v1.1, v1.2)

Both intermediate versions were published from newversion drafts that carried the
parent's files byte-identical without a full frontmatter refresh
(NEWVERSION-FRONTMATTER-CARRYOVER-1 class). The incidents are documented in the
session notes of 2026-08-19 and are superseded by v1.3; the versions themselves are
immutable and remain visible in the Zenodo version history.

## v1.3 remediation

- Frontmatter `doi:` patched to the v1.3 record's own DOI (10.5281/zenodo.22017933)
  and `status: published` verified against the deposited file.
- 4 orphan bibliography entries (dirac1928, fisher2015, white1992,
  berrykeating1999) moved in-body; 39/39 citations used.
- Prose-gate label removed (Section 10 = Assumptions and Imported Inputs).
- How-to-Cite block uses the CONCEPT DOI (10.5281/zenodo.22013263).
- citation-audit.md regenerated (16 rows).

## Residual cosmetic wart (v1.4 decision: NOT needed)

The deposited `.md` frontmatter `version:` field still reads `1.1` while the record
version is `1.3`. This is cosmetic: Zenodo's record metadata is authoritative, the
DOI/status fields are correct, and no reader-facing misresolution occurs. Per
handoff 28629 ("verify v1.4 not needed"), a v1.4 republish was deliberately NOT
created; the wart is documented here and in `qnfo-audit.audit_trail` instead.

## Cross-store sync repair (2026-08-20)

CROSS-STORE-PUBLISH-SYNC-1: `portfolio-state.program_registry` row for QNFO.RES.017
was stale (zenodo_doi=10.5281/zenodo.22013264, current_version=1.0, phase=P6) after
the v1.3 cycle. Updated to 10.5281/zenodo.22017933 / 1.3 / P8 (changes=1,
read-back verified). All other stores (D1 living-paper, paper_ids, KG node,
Vectorize, R2 mirror, wbs_state) were already current.
