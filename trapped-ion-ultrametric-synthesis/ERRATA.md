# ERRATA — QNFO.RES.017 Trapped-Ion Ultrametric Testbed

Version-history errata trail for the published synthesis record. This file is the
repo-level ERRATA trail referenced in handoff 28629 (2026-08-19); the authoritative
audit-log entries live in `qnfo-audit.audit_trail` (project_id `QNFO.RES.017`,
task_ids `ERRATA-v1.1`, `ERRATA-v1.2`, `ERRATA-v1.3`, `REGISTRY-SYNC`,
`REDTEAM-SECONDPASS`).

## Record versions

| Zenodo version | Record DOI | Status | Notes |
|:---------------|:-----------|:-------|:------|
| v1.0 | 10.5281/zenodo.22013264 | published (historical) | Original publication, 2026-08-19 |
| v1.1 | (superseded) | published (historical) | Carryover incident — see below |
| v1.2 | (superseded) | published (historical) | Carryover incident — see below |
| v1.3 | 10.5281/zenodo.22017933 | published (historical) | Red-team remediation; concept DOI 10.5281/zenodo.22013263; DataCite findable; doi.org HEAD 200 |
| v1.4 | 10.5281/zenodo.22025544 | published (current) | Red-team improved-version cycle (report red-team-2026-08-20-improved-version.md); record set 16→21; concept DOI 10.5281/zenodo.22013263 |

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

## Residual cosmetic wart (superseded by v1.4)

The v1.3 decision "v1.4 not needed" (frontmatter `version:` field reading `1.1` while
the record version was `1.3`) was SUPERSEDED on 2026-08-20: the red-team
improved-version cycle (user directive "is this the best we can do?") produced a
substantive v1.4 scope (record set 16→21, R5 external p-adic AdS/CFT QEC engagement,
Section 5 ledger extension with CMB/FMO/threshold nulls, R1 clock-spectrum
sharpening, Q-Fundamental cross-map, Artifact 5). The wart is now moot: v1.4 carries
`version: "1.4"` + the new record's own DOI. The v1.3 "not needed" decision is
retrospectively recorded as the correct call AT THAT TIME (no substantive defect was
known); the improved-version scope changed the calculus.

## v1.4 cycle (2026-08-20)

- Trigger: red-team report `red-team-2026-08-20-improved-version.md` (commits 6a590ce,
  4fbe04d; second-pass audit reviewer -c8ik_mvrlcqWtVocUOSr: PASS with corrections;
  H-4 prime-valuation-qec-implications 21979060 added).
- Content: record set 16→21 (adds ultrametric-quantum 21046993, prime-valuation
  21979060, qec-darwinism/Archimedean Shadows 21964674, One Table 22022313, Five
  Objections 22010489); R5 engages external Bruhat-Tits tensor-network QEC literature
  (Gubser 1605.01061, Heydeman 1605.07639, Bhattacharyya 1703.05445, Hung 1902.01411,
  Marcolli 1801.09623, Gubser-Parikh 1704.01149, Okunishi-Takayanagi 2310.12601); Section
  5 ledger extended (CMB null via radix-dsi 21902891 — NOT 19555030; FMO anti-ultrametric
  nulls 21651892; ultrametric-QEC threshold 55×); R1 sharpened (clock-spectrum
  insufficiency, 21120286); R3/R4 external p-adic QM citations; register↔Q-Fundamental
  (21697717) cross-map; Artifact 5 (QEC-Darwinism constraint checker).
- Cross-store sync (CROSS-STORE-PUBLISH-SYNC-1): program_registry → 22025544/1.4/P8;
  D1 living-paper; paper_ids; KG node + CITES seeding to the 21 input records;
  Vectorize re-index; R2 mirror qnfo-releases/2026/08/trapped-ion-ultrametric-synthesis/.

## Cross-store sync repair (2026-08-20)

CROSS-STORE-PUBLISH-SYNC-1: `portfolio-state.program_registry` row for QNFO.RES.017
was stale (zenodo_doi=10.5281/zenodo.22013264, current_version=1.0, phase=P6) after
the v1.3 cycle. Updated to 10.5281/zenodo.22017933 / 1.3 / P8 (changes=1,
read-back verified). All other stores (D1 living-paper, paper_ids, KG node,
Vectorize, R2 mirror, wbs_state) were already current. Re-verified at the v1.4
closeout: registry updated to 10.5281/zenodo.22025544 / 1.4 / P8.
