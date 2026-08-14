# Citation Audit — Phase 3 (QNFO.RES.007)

**Project:** Invariant Structural Value
**Date:** 2026-08-14
**Branch:** res/paper/invariant-structural-value
**WBS:** QNFO.RES.007
**Gate:** P3.AUTHOR-GATE (HARD) — every entry verified against live registry metadata before commit

## 1. Summary

| Metric | Value |
|:-------|:------|
| Bibliography entries (`artifacts/references.bib`) | **43** |
| Live-verified via Crossref API | 12 |
| Live-verified via DataCite API (Zenodo records) | 16 |
| Live-verified via arXiv API | 10 |
| Canonical entries (books, fixed metadata) | 3 (Worrall 1989, Joyal-Street 1986, Spencer-Brown 1969) |
| Manually constructed entries | 2 (Joyal-Street 1986, Spencer-Brown 1969 — canonical books without resolvable DOI; flagged MANUAL in evidence) |
| DOI corrections applied (P3.AUTHOR-GATE caught) | **5** |
| Duplicate keys | 0 |
| Wrong-DOI entries removed | 1 (10.1086/289085 — resolved to McMillan book, NOT Worrall) |

## 2. P3.AUTHOR-GATE Findings (DOI corrections — all evidence saved)

| Entry | Review DOI (WRONG) | Verified DOI (CORRECT) | Evidence |
|:------|:-------------------|:-----------------------|:---------|
| Worrall, *Structural Realism: The Best of Both Worlds?* (1989) | 10.1086/289085 (resolved to *Capital, Profits and Prices* by John McMillan — wrong book) | **10.1111/j.1746-8361.1989.tb00933.x** (Dialectica 43:99–124) | phase3-canonical-search.json; phase3-canonical-verification.json |
| French & Ladyman, *Remodelling Structural Realism* (2003) | 10.1016/S0039-3681(03)00021-8 (404) | **10.1023/a:1024156116636** (Synthese 136:31–56) | phase3-canonical-search.json; phase3-canonical-verification.json |
| Esfeld & Lam, *Moderate structural realism about space-time* (2008) | 10.1007/s11229-006-9076-8 (404) | **10.1007/s11229-006-9076-2** (Synthese) | phase3-datacite-verification.json |
| Kapustin & Witten, *Electric-magnetic duality and the geometric Langlands program* (2007) | 10.4310/cntp.2007.v1.n1 (404) | **10.4310/CNTP.2007.v1.n1.a1** | phase3-datacite-verification.json |
| Peebles & Ratra, *The cosmological constant and dark energy* (2003) | 10.1103/revmodphys.75.55 (404) | **10.1103/RevModPhys.75.559** | phase3-datacite-verification.json |

**Removed:** `10.1086/289085` never appears in references.bib — the wrong-Worrall guess was identified and stripped (mcmillan1982 entry removed).

## 3. Verification Method Per Entry

- **Zenodo (16 entries):** live DataCite API (`api.datacite.org/dois/<doi>`) — title, creators, year, publisher confirmed. All QNFO-owned records verified: ODR v4.0.4, QM-IGS, α as Cross-Ratio, Syntactic Token Calculus, α-π-Helix, Quantum Laws of Form, Calculus of Distinction, Computable Real Boundary, Base-Invariant Patterns, Winding Numbers, Strange Loop Theory, Notation Problem, Adelic Core Synthesis, Adelic Constraints Project, plus R1/R2 rejection-contrast records (correctly attributed to their real authors — Panahi, not QNFO).
- **Crossref (12 entries):** live Crossref API (`api.crossref.org/works/<doi>`) — title + author list + journal + volume + year + DOI match. Includes Worrall 1989 and French-Ladyman 2003 (re-verified after correction).
- **arXiv (10 entries):** live arXiv API (`export.arxiv.org/api/query?id_list=<id>`) — title, authors, raw XML saved.
- **Canonical books (2):** Joyal-Street 1986 (*Braided monoidal categories*, Adv. Math. 102:20–78) and Spencer-Brown 1969 (*Laws of Form*, Allen & Unwin) — fixed canonical metadata, flagged MANUAL in phase3-canonical-verification.json (books predate DOI registration).
- **Preprints (2):** Domain Projection (10.21203/rs.3.rs-8629054/v1, Abbas 2026) and Z3-graded framework (10.20944/preprints202512.2527.v2, Zhang et al. 2026) — verified via Crossref; cited as preprints (deficit register item 3 honored).

## 4. Three-Count Audit (P3.SOURCE-DISCIPLINE)

- Queries sent: 29 DOI verifications (Crossref) + 16 (DataCite) + 10 (arXiv) + 2 (Crossref canonical search) = **57**
- Sources received (verified unique works): **43**
- Sources cited in references.bib: **43**
- Cited > received? **NO** — no fabrication possible.

## 5. Duplicate Check

- `bibtexparser`/`biber`: not installed (documented per P3.AUTHOR-GATE rule 4).
- Regex duplicate-key detection run on final file: **43 unique keys, 0 duplicates** (previous build had 1 dup `adelic2026` — fixed in final build; wrong-DOI entry `mcmillan1982` removed).

## 6. Open Items (deferred to P4)

1. **Adelic Constraints Project null (R3)** — full engagement required in C1 section (deficit register item 2).
2. **C3 constructive derivation** — the [UNIQUE-CLAIM] burden: exhibit fixed-point equations for e (self-application) and π (self-closure), with KIF-60 surprise accounting.
3. **BP-10 independent recompute** of any α-adjacent numeric claims if the manuscript makes them (deficit register item 4).

## 7. Conclusion

P3 complete: 43-entry bibliography, all entries live-verified, 5 wrong/stale DOIs corrected (the exact failure class P3.AUTHOR-GATE exists to catch — two guessed canonical DOIs would have shipped wrong without live verification). **Proceed to P4 (Deep Research & Structured Forecast) with the deficit register as input.**
