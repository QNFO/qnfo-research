# Citation Audit — QNFO.RES.012 (research-purpose-utility)

AUTHOR-GATE live verification · 2026-08-16 · 28 entries (19 arXiv export, 7 DataCite, 2 books, 2 corpus-native)

## Verification method
- **arXiv anchors:** `export_citations` (authoritative arXiv metadata — title/authors/year/primaryClass from arXiv API, never model-generated). 19/19 success.
- **Zenodo anchors:** DataCite REST `api.datacite.org/dois/{doi}` live fetch (publicationYear + creators + titles). 7/7 HTTP 200.
- **Books:** Crossref bibliographic query (review/existence records). Both confirmed real with correct author/year.
- **Corpus-native (no DOI):** resolve_paper_id → D1 record status=published + get_paper_context body confirmed.

## Entry status table

| Entry key | Source | Method | Status |
|:----------|:-------|:-------|:-------|
| mongeon2016concentration | arXiv:1602.07396 | export_citations | VERIFIED |
| kenna2010normalization | arXiv:1006.3863 | export_citations | VERIFIED |
| wang2025funding | arXiv:2509.16323 | export_citations | VERIFIED |
| leydesdorff2009macrolevel | arXiv:0911.1044 | export_citations | VERIFIED |
| traag2022science | arXiv:2207.11116 | export_citations | VERIFIED |
| chen2025aidriven | arXiv:2505.12039 | export_citations | VERIFIED |
| rons2013research | arXiv:1307.7033 | export_citations | VERIFIED |
| rons2013interdisciplinary | arXiv:1307.6784 | export_citations | VERIFIED |
| rons2013output | arXiv:1307.6778 | export_citations | VERIFIED |
| thelwall2022is | arXiv:2212.05418 | export_citations | VERIFIED |
| hajkowicz2023artificial | arXiv:2306.09145 | export_citations | VERIFIED |
| abramo2018do | arXiv:1810.12637 | export_citations | VERIFIED |
| jiang2025automatic | arXiv:2502.16390 | export_citations | VERIFIED |
| markus2025societal | arXiv:2506.08738 | export_citations | VERIFIED |
| sun2021interdisciplinary | arXiv:2104.13091 | export_citations | VERIFIED |
| hyrynsalmi2025not | arXiv:2501.06523 | export_citations | VERIFIED |
| holy2024are | arXiv:2405.05227 | export_citations | VERIFIED |
| eck2012citation | arXiv:1210.0442 | export_citations | VERIFIED |
| mortera2025the | arXiv:2501.11104 | export_citations | VERIFIED |
| qnfo2026institutional | 10.5281/zenodo.21299211 | DataCite | VERIFIED (2026, QNFO Research Collective) |
| qnfo2025quantifying | 10.5281/zenodo.17229528 | DataCite | VERIFIED (2025, Quni-Gudzinas) |
| qnfo2026joules | 10.5281/zenodo.21637028 | DataCite | VERIFIED (2026, QNFO Research Collective) |
| qnfo2026consilience | 10.5281/zenodo.21804073 | DataCite | VERIFIED (2026, Quni-Gudzinas) |
| qnfo2026ultrametric | 10.5281/zenodo.21722395 | DataCite | VERIFIED (2026, Quni-Gudzinas) |
| qnfo2026gapsynthesis | 10.5281/zenodo.21782596 | DataCite | VERIFIED (2026, Quni-Gudzinas) |
| qnfo2026reification | 10.5281/zenodo.19605445 | DataCite | VERIFIED (2026, Quni-Gudzinas) |
| gibbons1994new | 10.4135/9781446221853 | Crossref | VERIFIED (Gibbons et al., 1994/2010 SAGE) |
| stokes1997pasteurs | Brookings 1997 | Crossref reviews | VERIFIED (Stokes, 1997; via 10.1086/384572 + 10.2307/40253438) |
| qnfo2025sowhat | corpus (no DOI) | resolve_paper_id + body | VERIFIED (corpus record, published 2025-11) |
| qnfo2025twofaced | corpus (no DOI) | resolve_paper_id + body | VERIFIED (corpus record, published 2025-01) |

## Data-quality findings (SOFT, logged for remediation)
1. **D1 `meta-pattern-of-reification-in-physics` row missing `zenodo_doi`** — resolve_paper_id returned `doi:null`/`zenodo_doi:null` while DataCite confirms 10.5281/zenodo.19605445 (2026, live). The row's identifier (`qnfo-2026-04-...`) and r2_key are present. Fix: backfill `zenodo_doi` on the D1 row (next D1-capable session; CHECK-THEN-WRITE per WBS-REGISTRY-STALE-1 discipline).
2. **`so-what-of-knowledge` + `two-faced-scientific-methodology` have no DOIs** — corpus-native records. Recommend minting Zenodo DOIs for these two (publication program) so future cross-references are DOI-stable (P6-adjacent action, deferred).

## S2-ZENODO-GAP-1
Semantic Scholar does not index the QNFO Zenodo set — no S2 verification attempted for the 7 Zenodo entries (DataCite is the authoritative check per research skill ZENODO-PHANTOM-DOI-1).

## P3 gate
P3.AUTHOR-GATE: **PASS** — 30/30 entries verified (28 bib entries + 2 corpus-native), zero fabricated/unverifiable entries. references.bib + this audit committed for the P4 draft.
