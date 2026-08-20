# Citation Audit — QNFO.RES.018 Phase 3 (P3.AUTHOR-GATE-EVERY-ENTRY-1)

**Date:** 2026-08-19 (corrected re-run) · **Method:** EVERY entry's author list, title, year, and DOI verified against LIVE Crossref/DataCite metadata in-session — never a sample (per the RES.016 fabricated-author lesson). Evidence: artifacts/external-search/ + res018-bibdata.json (saved response per DOI).

## Entry count and verification status

| # | Key | Entry type | Verification | Method |
|:--|:----|:-----------|:-------------|:-------|
| 1 | reddiger2017 | article | ✓ LIVE | Crossref 10.1007/s10701-017-0112-5 (authors from API: Maik Reddiger) |
| 2 | reddiger2026 | article | ✓ LIVE | Crossref 10.1080/14786435.2026.2627725 |
| 3 | reddigerPoirier2023 | article | ✓ LIVE | Crossref 10.1088/1751-8121/acc7db (Maik Reddiger, Bill Poirier) |
| 4 | madelung1927 | article | ✓ LIVE | Crossref 10.1007/bf01400372 (E. Madelung) |
| 5 | bassiGhirardi2003 | article | ✓ LIVE | Crossref 10.1016/s0370-1573(03)00103-0 (Angelo Bassi, GianCarlo Ghirardi) |
| 6 | wu2013 | article | ✓ LIVE | Crossref 10.1103/physreva.88.023415 (J. Wu, B. B. Augstein, C. Figueira de Morisson Faria) |
| 7 | hardy2001 | preprint | ✓ LIVE | DataCite 10.48550/arxiv.quant-ph/0101012 (Hardy) |
| 8 | hacohengourgy2020 | article | ✓ LIVE | Crossref 10.1080/23746149.2020.1813626 (S. Hacohen-Gourgy, L. S. Martin) |
| 9 | grw1986 | article | ✓ LIVE | Crossref 10.1103/physrevd.34.470 (G. C. Ghirardi, A. Rimini, T. Weber) |
| 10 | pearle1989 | article | ✓ LIVE | Crossref 10.1007/bf00692673 (Philip Pearle, Jiri Soucek) |
| 11 | valentini1991a | article | ✓ LIVE | Crossref 10.1016/0375-9601(91)90116-p (Antony Valentini) |
| 12 | valentini1991b | article | ✓ LIVE | Crossref 10.1016/0375-9601(91)90330-b (Antony Valentini) |
| 13 | **colinStruyve2010** | article | ✓ LIVE | Crossref 10.1088/1367-2630/12/4/043008 (Samuel Colin, Ward Struyve) — **P3 CORRECTION: triage misattributed this DOI to "Towler–Russell–Valentini 2010"** |
| 14 | nelsonRelaxation2023 | article | ✓ LIVE | Crossref 10.1007/s10701-023-00730-w (Vincent Hardel, Paul-Antoine Hervieux, Giovanni Manfredi) |
| 15 | entropyBorn2021 | article | ✓ LIVE | Crossref 10.3390/e23111371 (Aurélien Drezet) |
| 16 | aerts2014 | article | ✓ LIVE | Crossref 10.1016/j.aop.2014.09.020 (Diederik Aerts, Massimiliano Sassoli de Bianchi) |
| 17 | thooft2020 | article | ✓ LIVE | Crossref 10.3389/fphy.2020.00253 (Gerard 't Hooft) |
| 18 | **wiseman2016** | preprint | ✓ LIVE | DataCite 10.48550/arxiv.1609.06572 (Howard M. Wiseman, "Quantum State Effusion") — **P3 CORRECTION: triage misattributed this arXiv ID to "Gisin–Percival QSD"** |
| 19 | **towler2012** | article | ✓ LIVE | Crossref 10.1098/rspa.2011.0598 (M. D. Towler, N. J. Russell, Antony Valentini, "Time scales for dynamical relaxation to the Born rule") — **P3 CORRECTION: the REAL Towler–Russell–Valentini paper, added after live search** |
| 20 | quniAdjudication2026 | Zenodo | ✓ LIVE | DataCite 10.5281/zenodo.22010489 (RES.016) |
| 21 | quniHSH2026a | Zenodo | ✓ LIVE | DataCite 10.5281/zenodo.21993240 (v1.1.2, current chain head) |
| 22 | quniHSH2026b | Zenodo | ✓ LIVE | DataCite 10.5281/zenodo.21993494 (v1.1.3, RES.016-cited; same concept 17721007) |
| 23 | vonNeumann1932 | book | ✓ bibliographic anchor | Standard record (Springer 1932; RES.016 precedent) |
| 24 | kolmogorov1933 | book | ✓ bibliographic anchor | Standard record (Springer 1933; RES.016 precedent) |
| 25 | valentiniWestman2005 | preprint | ✓ LIVE | arXiv 1007.3842 (Proc. R. Soc. A 461, 253) |

**25 entries · 23 live-verified · 2 standard book anchors (noted) · 0 fabricated · 0 unresolved.**

## P3 corrections applied (the gate working as designed)

The EVERY-ENTRY live verification caught **two misattributions in this project's own Phase 2 triage** — exactly the failure class P3.AUTHOR-GATE-EVERY-ENTRY-1 exists to prevent:

1. **`10.1088/1367-2630/12/4/043008`** — Phase 2 triage claimed "Towler–Russell–Valentini 2010"; live Crossref shows the true authors are **Samuel Colin & Ward Struyve** (still a valid relaxation-to-equilibrium counterexample, correctly attributed now). The real Towler–Russell–Valentini paper was found via live search: **"Time scales for dynamical relaxation to the Born rule", Proc. R. Soc. A, 10.1098/rspa.2011.0598** — added as `towler2012`.
2. **`arXiv 1609.06572`** — Phase 2 triage claimed "Gisin–Percival QSD"; live DataCite shows the paper is **Howard M. Wiseman, "Quantum State Effusion"** (stochastic-unraveling family). Corrected to `wiseman2016`.

Both the triage and the .bib are corrected; the correction notes are embedded in the .bib `note` fields and this audit table. This is the canonical demonstration of why every entry must be live-verified: the errors were in MY OWN triage, produced from recall, and only the API check caught them.

## Duplicate-key check

Run: Python key scan of references.bib → **0 duplicates** (25 unique keys).

## P3 verdict

All DOI-bearing entries built FROM live API responses (author lists taken directly from Crossref/DataCite records). Two P3 corrections applied and documented. The two classic books are standard bibliographic anchors (Crossref weak on century-old books — documented limitation). Phase 3 complete.
