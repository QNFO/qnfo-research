# Citation Audit — QNFO.RES.004 Prime Valuation Depth

**Date:** 2026-08-13 · **Phase:** P3 · **WBS:** QNFO.RES.004.P3
**Gate:** P3.AUTHOR-GATE (HARD — every entry verified against live Crossref/OpenAlex/arXiv)

## 1. Verification Method

Every DOI in `references/prime-valuation-depth.bib` was verified via live API in THIS session:
- Crossref `api.crossref.org/works/{doi}` — author list, title, year, container, volume, pages (res004_p3.py)
- OpenAlex fallback for any Crossref failure (none needed)
- arXiv API `export.arxiv.org/api/query?id_list=` — title + authors for eprint entries (res004_p3b.py)
- Crossref `query.bibliographic` search used to locate the correct Dieks DOI and the Ostrowski Acta Mathematica DOI (res004_p3b.py, res004_p3c.py)

## 2. Verification Table

| # | Key | DOI / ID | Verified via | Title match | Authors match | Result |
|:--|:----|:---------|:-------------|:------------|:--------------|:-------|
| 1 | ostrowski1916 | 10.1007/bf02422947 | Crossref | ✓ (Acta Math 41, ψ(x)·ψ(x)=ψ(xy)) | ✓ Ostrowski | PASS |
| 2 | spencerbrown1969 | — (book) | Crossref search | ✓ (no DOI record exists — standard bibliographic identity) | ✓ Spencer-Brown | PASS (no-DOI book, flagged) |
| 3 | wootters1982 | 10.1038/299802a0 | Crossref | ✓ "A single quantum cannot be cloned" | ✓ Wootters; Zurek | PASS |
| 4 | dieks1982 | 10.1016/0375-9601(82)90084-6 | Crossref search | ✓ "Communication by EPR devices" (Phys. Lett. A 92:271-272) | ✓ Dieks | PASS |
| 5 | volovich1987 | 10.1088/0264-9381/4/4/003 | Crossref | ✓ "p-adic string" (CQG 4:L83) | ✓ Volovich | PASS |
| 6 | coeckeduncan2011 | 10.1088/1367-2630/13/4/043016 | Crossref | ✓ | ✓ Coecke; Duncan | PASS |
| 7 | coeckepaquette2010 | 10.1007/978-3-642-12821-9_3 | Crossref | ✓ | ✓ Coecke; Paquette | PASS |
| 8 | hung2019 | 10.1007/jhep04(2019)170 | Crossref | ✓ | ✓ Hung; Li; Melby-Thompson | PASS |
| 9 | heydeman2018 | 10.4310/atmp.2018.v22.n1.a4 | Crossref | ✓ | ✓ Heydeman; Marcolli; Saberi; Stoica | PASS |
| 10 | varela1979 | 10.1305/ndjfl/1093882412 | Crossref | ✓ | ✓ Varela | PASS |
| 11 | rapoport2009 | 10.1007/s10701-009-9334-5 | Crossref | ✓ | ✓ Rapoport | PASS |
| 12 | almheiri2015 | 10.1007/jhep04(2015)163 | Crossref | ✓ | ✓ Almheiri; Dong; Harlow | PASS |
| 13 | alvarez2015 | 10.1038/srep11983 | Crossref | ✓ | ✓ Alvarez-Rodriguez; Sanz; Lamata; Solano | PASS |
| 14 | datta2022 | 10.36227/techrxiv.21716615.v1 | Crossref | ✓ | ✓ Datta | PASS |
| 15 | niestegge2015 | arXiv:1502.02151 | arXiv API | ✓ | ✓ Niestegge | PASS |
| 16 | isaacson2016 | arXiv:1606.06965 | arXiv API | ✓ | ✓ Isaacson; Kauffman | PASS |
| 17 | ji2017 | arXiv:1711.00385 | arXiv API | ✓ | ✓ Ji; Liu; Song | PASS |

**Result: 17/17 PASS. Zero fabricated entries. Zero unresolved DOIs.**

## 3. P3 Gate Catch Log (fabrication prevention in action)

| Incident | Initial (recalled/guessed) | Verified | Severity |
|:---------|:--------------------------|:---------|:---------|
| p-adic string author | "Freund & Olson" (training recall) | **Volovich** (Crossref) | HARD — author fabrication risk; corrected in classification + bib |
| Categories author | "Coecke & Heunen" | **Coecke & Paquette** (Crossref) | HARD — author fabrication risk; corrected |
| Dieks DOI | 10.1016/0375-9601(82)90284-6 (recalled) | **10.1016/0375-9601(82)90084-6** (Crossref search) | HARD — wrong-DOI fabrication risk; corrected |
| Ostrowski DOI | none assumed | 10.1007/bf02422947 (Crossref search) | PASS — located via bibliographic search |
| Spencer-Brown DOI | none (book) | no DOI exists — flagged in bib note | SOFT — no-DOI book, standard identity |

## 4. Duplicate-Key Check (CITING-5)

`@\w+\{([^,]+),` regex over the .bib → 17 keys, **0 duplicates** (verified via script output).

## 5. Source Discipline (P3.SOURCE-DISCIPLINE)

- All 17 entries originate from THIS session's live API calls (res004_p3.py, res004_p3b.py, res004_p3c.py).
- The canonical anchors (Ostrowski, Spencer-Brown, Wootters–Zurek, Dieks) were not in the top-8 external-search hits — they were located via explicit Crossref bibliographic searches this session. Labeled accordingly.
- **3-count audit:** 21 queries sent → 59 sources received → 17 cited (this .bib) + 31 classified in P2. cited ≤ received — PASS.
- Excluded from .bib: items classified Reject (R1–R6) and off-topic background — no fabrication of "nice-looking" entries.
