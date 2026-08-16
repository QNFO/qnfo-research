# Citation Audit — Signal-Worker Boundary Confinement v0.2

**Date:** 2026-08-16 · **Method:** field-level live verification per P3.AUTHOR-GATE — every entry's author, title, and DOI re-checked against live Crossref (refs 1–6) and the live Zenodo records API (refs 7–15) in the same session. Concept-DOI citations per ZENODO-CONCEPT-DOI-CITE-1.
**Scope:** all 15 numbered references; the shipped `references.bib` file itself (not a reconstruction).

| # | Key | Cited DOI | Source | HTTP | Author match | Title match | DOI/concept match | Verdict |
|:--|:----|:----------|:-------|:-----|:-------------|:------------|:------------------|:--------|
| 1 | ref1 | 10.1103/RevModPhys.82.3045 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 2 | ref2 | 10.1103/RevModPhys.83.1057 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 3 | ref3 | 10.1103/PhysRevLett.121.086803 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 4 | ref4 | 10.1103/PhysRevB.83.205101 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 5 | ref5 | 10.1126/science.aaa9297 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 6 | ref6 | 10.1103/PhysRev.130.439 | Crossref | 200 | PASS | PASS | PASS | PASS |
| 7 | ref7 | 10.5281/zenodo.18330366 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 8 | ref8 | 10.5281/zenodo.18441402 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 9 | ref9 | 10.5281/zenodo.18515458 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 10 | ref10 | 10.5281/zenodo.18466522 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 11 | ref11 | 10.5281/zenodo.18543167 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 12 | ref12 | 10.5281/zenodo.18222365 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 13 | ref13 | 10.5281/zenodo.18496890 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 14 | ref14 | 10.5281/zenodo.21574555 | Zenodo | 200 | PASS | PASS | PASS | PASS |
| 15 | ref15 | 10.5281/zenodo.18447478 | Zenodo | 200 | PASS | PASS | PASS | PASS |

**Totals:** 15/15 entries PASS field-level (author + title + DOI/concept) · 0 FAIL · 0 fabricated entries · 0 duplicate keys.

**Remediations in this file generation (red-team 2026-08-16, R1–R3):**
- **R1** — ref11 now cites the CONCEPT DOI `10.5281/zenodo.18543167` (live check: GET /records/18543167 → conceptrecid=18543167; the version record is 18543168). The generator bug that wrote the version-record DOI is documented in the 2026-08-16 red-team report.
- **R2** — ref14 author corrected to `Quni, Rowan` (live record 21574555 creators: [Quni, Rowan]).
- **R3** — this audit now includes per-entry Author/Title/DOI field columns; the earlier '15/15 verified' claim checked HTTP + title only and missed both divergences. The claim is now field-grounded.

**New in v0.2:** references.bib and this citation-audit.md were absent from the v0.1 deposit (PUBLICATION-SOURCE-COMPLETENESS-1 gap); both are now included as deposited source files.
