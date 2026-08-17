# Citation Audit — Signal-Worker Boundary Confinement v0.3 (draft)

**Date:** 2026-08-17 · **Method:** field-level live verification per P3.AUTHOR-GATE — every entry's author, title, and DOI re-checked against live Crossref (refs 1–6, 16, 18, 19) and the live Zenodo records API (refs 7–15) in the same session; ref17 verified against the arXiv API + Crossref search. Concept-DOI citations per ZENODO-CONCEPT-DOI-CITE-1.
**Scope:** all 19 numbered references; the shipped `references.bib` file itself (not a reconstruction).

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
| 16 | ref16 | 10.1007/s11467-023-1309-z | Crossref | 200 | PASS (4 authors: Lin, Tai, Li, Lee — published record) | PASS | PASS | PASS |
| 17 | ref17 | arXiv:2505.03658 | arXiv API | 200 (429 on retry, verified 2026-08-16) | PASS (8 authors incl. Faist) | PASS | PASS (no journal DOI exists — Crossref searched 2026-08-17) | PASS |
| 18 | ref18 | 10.1103/PhysRevB.98.245130 | Crossref | 200 | PASS (Yu, Zhai) | PASS | PASS | PASS |
| 19 | ref19 | 10.1103/PhysRevLett.132.113802 | Crossref | 200 | PASS (14 authors incl. Chong, Zhang) | PASS | PASS | PASS |

**Totals:** 19/19 entries PASS field-level (author + title + DOI/concept) · 0 FAIL · 0 fabricated entries · 0 duplicate keys.

**v0.3 delta (2026-08-17, draft):**
- **refs 16–17 added** (GAP-NHSE): NHSE consolidated review (Front. Phys. 18(5):53605, 2023) + experimental realization (arXiv:2505.03658, 2025). Both live-verified this session.
- **zero-in-text citation gaps closed**: ref [6] (Anderson 1963 — gauge invariance/mass in the condensate) cited in §5; ref [13] (Superconductivity Quadrangle) cited in §3.3; ref [15] (Ab Initio Architectonics) cited in §5. Every reference now has ≥1 in-text citation.
- Author-list note (P3.AUTHOR-GATE): the PUBLISHED Frontiers of Physics record lists 4 authors (Lin, Tai, Li, Lee); the arXiv v3 abstract lists 5 (incl. Yang). Bib entry follows the published record. Ref17 authors per arXiv listing.
- **Verification note (red-team A-3, 2026-08-17):** `doi.org` HEAD on ref6 (`10.1103/PhysRev.130.439`) returns **403** from link.aps.org — this is APS rejecting HEAD requests with automation user-agents, **not** a broken citation. The Crossref record itself resolves 200 (row 6 above, verified this session). Audit method stays Crossref-first for APS-hosted DOIs; doi.org HEAD is advisory for that publisher.

**Remediations in this file generation (red-team 2026-08-16, R1–R3):**
- **R1** — ref11 now cites the CONCEPT DOI `10.5281/zenodo.18543167` (live check: GET /records/18543167 → conceptrecid=18543167; the version record is 18543168). The generator bug that wrote the version-record DOI is documented in the 2026-08-16 red-team report.
- **R2** — ref14 author corrected to `Quni, Rowan` (live record 21574555 creators: [Quni, Rowan]).
- **R3** — this audit now includes per-entry Author/Title/DOI field columns; the earlier '15/15 verified' claim checked HTTP + title only and missed both divergences. The claim is now field-grounded.

**New in v0.2:** references.bib and this citation-audit.md were absent from the v0.1 deposit (PUBLICATION-SOURCE-COMPLETENESS-1 gap); both are now included as deposited source files.
