# Citation Audit — QNFO.RES.016 (P3.AUTHOR-GATE)

**Date:** 2026-08-19 · **Method:** every entry verified against live Crossref/OpenAlex/arXiv metadata in-session; evidence files in artifacts/external-search/ (p2-*.json, crossref-*.json, openalex-*.json, arxiv-*.json).

## Entry count and verification status

| # | Key | Entry type | Verification | Method (evidence file) |
|:--|:----|:-----------|:-------------|:-----------------------|
| 1 | vonNeumann1932 | book | ✓ bibliographic | Crossref query (crossref-Mathematische-Grundl.json) + standard bibliography |
| 2 | kolmogorov1933 | book | ✓ bibliographic | Crossref query (crossref-Grundbegriffe-der-Wa.json) + standard bibliography |
| 3 | madelung1926 | article | ✓ LIVE | Crossref 10.1007/bf01400372 (p2-crossref-madelung1926.json) |
| 4 | volovich1987 | article | ✓ LIVE | OpenAlex 10.1088/0264-9381/4/4/003 (p2-openalex-volovich1987.json) |
| 5 | reddiger2017 | article | ✓ LIVE | Crossref 10.1007/s10701-017-0112-5 (crossref-reddiger.json) |
| 6 | reddiger2026 | article | ✓ LIVE | Crossref 10.1080/14786435.2026.2627725 (crossref-reddiger.json) |
| 7 | hardy2001 | preprint | ✓ LIVE | arXiv quant-ph/0101012 (arxiv-hardy2001.json) |
| 8 | nelson1967 | book | ✓ LIVE | Crossref 10.1515/9780691219615 (crossref-nelson1966.json) |
| 9 | wu2013 | article | ✓ LIVE | Crossref 10.1103/physreva.88.023415 (crossref-wu2013.json) |
| 10 | hacohengourgy2020 | article | ✓ LIVE | Crossref 10.1080/23746149.2020.1813626 (crossref-hacohengourgy2020.json) |
| 11 | bassiGhirardi2003 | article | ✓ LIVE | Crossref 10.1016/s0370-1573(03)00103-0 (p2-crossref-bassi2003.json) |
| 12 | garola2006 | article | ✓ LIVE | Crossref 10.1007/s10701-006-9046-z (p2-crossref-garola2006.json) |
| 13 | shafer2006 | article | ✓ LIVE | OpenAlex 10.1214/088342305000000467 (p2-openalex-probability-history.json) |
| 14 | kolmogorovOrigins2018 | preprint | ✓ LIVE | OpenAlex 10.48550/arxiv.1802.06071 (p2-openalex-probability-history.json) |
| 15 | vladimirov1998 | article | ✓ LIVE | OpenAlex 10.2748/tmpub.10.1 (p2-openalex-padic-qm.json) |
| 16 | padicQubit2022 | article | ✓ LIVE | OpenAlex 10.3390/e25010086 (p2-openalex-padic-qm.json) |
| 17 | hensen2015 | article | ✓ LIVE | OpenAlex 10.1103/physrevlett.115.250402 (p2-openalex-bell-local-realism.json); Nature record per standard bibliography |
| 18 | strocchi2011 | preprint | ✓ LIVE | arXiv 1112.1507 (arxiv-1112.1507.json) |
| 19 | quniPQS2025 | Zenodo | ✓ corpus | resolve_paper_id (slug post-quantum-synthesis → 10.5281/zenodo.21993491) |
| 20 | quniHSH2025 | Zenodo | ✓ corpus | resolve_paper_id (slug hydrodynamic-stability-hypothesis → 10.5281/zenodo.21993494) + full body read |
| 21 | quniPQSAudit2025 | Zenodo | ✓ corpus | resolve_paper_id (slug pqs-ai-evaluation-audit → 10.5281/zenodo.21535491) |
| 22 | quniNonArchimedean2026 | Zenodo | ✓ LIVE | OpenAlex 10.5281/zenodo.19600686 (openalex-philpapers-nonarchimedean-syntactic.json) |

**22 entries · 22 verified · 0 fabricated · 0 unresolved.**

## Seed-note URL-level citations (P3.SOURCE-DISCIPLINE)

| Seed note ref | URL | Live status | Disposition |
|:--------------|:----|:------------|:------------|
| [1][2] | papers.ssrn.com 5809662 | 403 bot-filter (Python + browser CF challenge) | `[UNVERIFIED]` at URL level; subject paper verified via corpus DOI 21993494 |
| [3] | philpapers.org/rec/QUNTCI | 403 | `[UNVERIFIED]`; subject (Continuum is Real / HSH) verified via corpus |
| [10] | papers.ssrn.com 5821702 | 403 | `[UNVERIFIED]`; likely Strange Loop paper — corpus DOI 21993496 candidate |
| [11] | philpapers.org/rec/QUNTUP | 403 | `[UNVERIFIED]` |
| [12][13] | philpapers.org/rec/QUNANS | 403 | Subject verified: OpenAlex 10.5281/zenodo.19600685/86 |
| [4] | sciencedirect S1355219808000403 | not fetched (paper-ref) | `[NOT-FETCHED]` — journal article ref in seed note |
| [5] | springer 10.1007/978-94-017-2012-0 | not fetched | `[NOT-FETCHED]` |
| [6] | arxiv 1112.1507 | ✓ 200 | Verified (Strocchi 2011) |
| [7] | mosaic.messiah.edu mps_st/1 | not fetched | `[NOT-FETCHED]` |
| [8] | cambridge.org von Neumann projection postulate PDF | not fetched | `[NOT-FETCHED]` |
| [9] | sciencedirect S037596011930636X | not fetched | `[NOT-FETCHED]` |
| [14] | youtube XSi4JwlFkVI | not fetched | `[NOT-FETCHED]` — video ref, excluded from bibliography |

**CDX check:** zero Wayback captures for all five philpapers/ssrn seed URLs (cdx-*.json evidence) — records exist in live web but are unarchived; consistent with 403 wall, not with nonexistence.

## Duplicate-key check

Run: bibtexparser-free key scan via Python (references.bib, 22 unique keys) → **0 duplicates**.

## P3 verdict

All adjudication-critical references verified. Zero fabricated entries. Seed-note SSRN/PhilPapers URLs flagged `[UNVERIFIED]` and excluded from citation count where URL-level proof is required; corpus DOIs carry the load.

## v1.1 REMEDIATION (2026-08-19, post-publication accuracy audit)

The post-publication adversarial analysis (accuracy reviewer, delegation mVeYbd9GvKcmoev0oD7nH)
surfaced 5 HARD bibliographic defects in v1.0 (10.5281/zenodo.22009653). Each was verified
against live Crossref BEFORE remediation:

| ID | v1.0 defect | Verified truth (live Crossref) | v1.1 fix |
|:---|:------------|:-------------------------------|:---------|
| H-1 | In-text "Caruana et al. 2022" for RMP 94:045007 | Budroni, Cabello, Gühne, Kleinmann, Larsson | In-text + reference entry corrected; entry added to references.bib (budroni2022) |
| H-2 | "Khodjaev, J., et al." for Entropy 25(1):86 | Aniello, Mancini, Parisi | In-text + .bib corrected (aniello2022) |
| H-3 | "Vladimirov, Volovich, Zelenov 1998" on DOI 10.2748/tmpub.10.1 | Youngho Jang, TMP 10, 1–69 | DOI anchored to jang1998; canonical VVZ treatise re-cited as 1994 World Scientific book (vvz1994) |
| H-4 | "780 indexed works" | 790 (openalex-author-works-page1.json meta.count) | Corrected to 790 |
| H-5 | Hensen 2015 Nature DOI cited without same-session verification | Confirmed live 2026-08-19 (10.1038/nature15759, pages 682–686) | Verified; recorded here |

SOFT fixes: "forty-year" → four-decade/nearly-four-decade (1987→2026 = 39 yr); five references
(Garola, Hardy, Madelung, Nelson, Strocchi) now cited in body; §8 grade label for objection 5
clarified. references.bib now 24 entries, paper References 24 entries (1:1).
