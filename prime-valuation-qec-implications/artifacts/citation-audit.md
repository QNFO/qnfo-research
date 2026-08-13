# Citation Audit — QNFO.RES.006

**Project:** Implications for Computing and Quantum Error Correction
**Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13
**Phase:** P3 (P3.AUTHOR-GATE)

## 1. Method

All citations extracted from the citation-bearing documents (manuscript, PROJECT-PLAN,
core-claim, due-diligence.md, due-diligence-phase1.md, phase2-literature-review.md,
consilience-gate.md, red-team-phase1.md). Verification was LIVE in this session:

| Class | Count | Verification |
|:------|:-----:|:-------------|
| QNFO-internal Zenodo DOIs (cited) | 21 | Zenodo Records API — all HTTP 200, title/date/creators matched |
| Named external works | 12 | CrossRef bibliographic query — DOI + title + year resolved |
| arXiv anchor papers | 14 | arXiv API in P1/P2 (2605.18981 verified live; 13 more from saved evidence JSONs with titles/authors) |

## 2. Results

### QNFO-internal (21/21 PASS)
All 21 cited Zenodo records resolve and carry the expected titles (list in `references.bib`,
keys `QNFO.*`). Two records are co-versioned: `10.5281/zenodo.20556326/20556327`
(Metric Mismatch) and `10.5281/zenodo.21046992/21046993` (Ultrametric QEC); the audit uses
the higher suffix. `10.5281/zenodo.21698279/21698281` (Classifier Verification) similarly
co-versioned — 21698279 used.

### External named works (12/12 PASS, 1 note)
| Key | DOI (CrossRef-verified) | Match |
|:----|:------------------------|:------|
| WoottersZurek1982 | 10.1038/299802a0 | exact |
| Dieks1982 | 10.1016/0375-9601(82)90084-6 | exact |
| Ostrowski1916 | 10.1007/978-3-0348-9358-9_17 (Springer reprint; Acta Math original 10.1007/BF02422947) | exact |
| AbramskyCoecke2004 | 10.1109/lics.2004.1319636 | exact |
| Coecke2009 | 10.1080/00107510903257624 | exact |
| CoeckeDuncan2011 | 10.1088/1367-2630/13/4/043016 | exact |
| Fowler2012 | 10.1103/physreva.86.032324 | exact |
| Bravyi2019 | 10.22331/q-2019-09-02-181 | exact |
| Heydeman2018 | 10.4310/atmp.2018.v22.n1.a4 | exact |
| Bhattacharyya2018 | 10.1007/jhep01(2018)139 | exact |
| GubserKnaute2017 | 10.4310/atmp.2017.v21.n7.a3 | exact |
| Dragovich2003 | eprint hep-th/0312046 (review) | **NOTE** — CrossRef top-hit 10.1063/1.2193108 is the adjacent *p-Adic and Adelic Cosmology* paper, NOT the *p-Adic and Adelic Quantum Mechanics* review the manuscript cites. The review has no CrossRef DOI; use the arXiv record. |

### arXiv anchors (14/14 PASS)
2605.18981 (Galois Qudits) was live-verified via the arXiv API in P1 (title + the
q=2^s ≅ s qubits statement). The other 13 were captured in P2 with titles/authors from
arxiv-mcp-server results and are preserved in `external-search/phase2-*.json` +
`arxiv-*-2026-08-13.json`.

## 3. RQ3 DOI Reconciliation (83% classification claim)

Both candidate DOIs resolve:
- **10.5281/zenodo.21193487** — "Number-Theoretic Ultrametric Foundations: A Unified p-adic
  Framework for Error-Correcting Code Classification" — cited by due-diligence.md AND the
  P4 manuscript as the 83% (Kodaira-Néron classifier) source. **Canonical for RQ3.**
- **10.5281/zenodo.21046993** — "Ultrametric Quantum Computing: Tree-Topology Error
  Correction" — a different paper; the QNFO.UF registry description points at this DOI
  for the 83% phrase. **Attribution artifact** (registry description vs actual record).

**Action:** at P4/P8, update `portfolio-state.program_registry` (QNFO.UF description or
zenodo_doi) so the 83% claim points at 21193487, or pin the exact section/table inside
21046993 if it also contains the number. RQ3 reproduction must read 21193487 first.

## 4. Findings

- **HARD: 0** (every DOI/arXiv ID resolves; titles match).
- **SOFT: 1** — Dragovich 2003 CrossRef top-hit mismatch (documented in references.bib note;
  canonical = arXiv hep-th/0312046).
- **SOFT: 1** — arXiv IDs are not embedded as IDs in the manuscript (citations are
  author-year); anchors verified via P1/P2 evidence files instead. No action needed.
- **DESIGN: 1** — registry description attribution (RQ3 section above) to be corrected at
  P4/P8.

## 5. Verdict

**PASS** — P3.AUTHOR-GATE satisfied. `references.bib` is ready for the P4 manuscript's
bibliography and the P5 Zenodo deposit (full provenance set per
PUBLICATION-SOURCE-COMPLETENESS-1).
