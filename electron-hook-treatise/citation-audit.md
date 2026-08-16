# Citation Audit — electron-hook-treatise v0.1 (AUTHOR-GATE)

Audit of all 30 bibliographic entries against live authoritative sources, 2026-08-16.

## Method (two-phase)

1. **Phase 1 (rejected as noisy):** Crossref generic `query.title` search returned wrong matches for 10/30 classics (e.g., Dirac 1928 → a J. Chem. Ed. article; Ostrowski → a zoology paper). Recorded in `reference-verification.json` v1 history — superseded.
2. **Phase 2 (authoritative, all counts below):** direct exact-DOI lookup `GET https://api.crossref.org/works/{doi}` with title-needle confirmation, plus arXiv abstract check for 't Hooft. Evidence: `artifacts/external-search/reference-verification.json`.

## Results — 30/30 verified

| # | Entry | Verification route | Result |
|:--|:------|:-------------------|:-------|
| 1 | Dirac 1928, Proc. R. Soc. A 117:610 | Crossref 10.1098/rspa.1928.0023 | exact title + 1928 ✓ |
| 2 | von Neumann 1932, Springer | Crossref 10.1007/978-3-642-96048-2 | exact title ✓ (Crossref dates ISBN edition 1971; original 1932) |
| 3 | Ostrowski 1918, Acta Math. 41:271 | Crossref reprint 10.1007/978-3-0348-9358-9_17 (Collected Mathematical Papers, exact title φ(x)φ(y)=φ(xy)) | ✓ (original-citation + verified reprint locator in bib note) |
| 4 | Wigner 1939, Ann. Math. 40:149 | Crossref 10.2307/1968551 | exact title + 1939 ✓ |
| 5 | Pauli 1940, Phys. Rev. 58:716 | Crossref 10.1103/PhysRev.58.716 | ✓ |
| 6 | Landauer 1961 | Crossref 10.1147/rd.53.0183 | ✓ |
| 7 | Bennett 1973 | Crossref 10.1147/rd.176.0525 | ✓ |
| 8 | Unruh 1976 | Crossref 10.1103/PhysRevD.14.870 | ✓ |
| 9 | Leinaas–Myrheim 1977, Nuovo Cim. B 37:1 | Crossref 10.1007/BF02727953 | ✓ |
| 10 | Tsui–Stormer–Gossard 1982 | Crossref 10.1103/PhysRevLett.48.1559 | ✓ |
| 11 | Wilczek 1982 | Crossref 10.1103/PhysRevLett.49.957 | ✓ |
| 12 | Laughlin 1983 | Crossref 10.1103/PhysRevLett.50.1395 | ✓ |
| 13 | Arovas–Schrieffer–Wilczek 1984 | Crossref 10.1103/PhysRevLett.53.722 | ✓ |
| 14 | Halperin 1984 | Crossref 10.1103/PhysRevLett.52.1583 | ✓ (main paper, not erratum) |
| 15 | Mermin–Wagner 1966 | Crossref 10.1103/PhysRevLett.17.1133 | ✓ |
| 16 | Kosterlitz–Thouless 1973 | Crossref 10.1088/0022-3719/6/7/010 | ✓ |
| 17 | BCS 1957 | Crossref 10.1103/PhysRev.108.1175 | ✓ |
| 18 | Wigner 1960 | Crossref 10.1002/cpa.3160130102 | ✓ |
| 19 | Bell 1964 | Crossref 10.1103/PhysicsPhysiqueFizika.1.195 | ✓ |
| 20 | Feynman 1948 | Crossref 10.1103/RevModPhys.20.367 | ✓ |
| 21 | Bekenstein 1973 | Crossref 10.1103/PhysRevD.7.2333 | ✓ |
| 22 | Deutsch 1991 | Crossref 10.1103/PhysRevA.43.2046 | ✓ |
| 23 | Srednicki 1994 | Crossref 10.1103/PhysRevE.50.888 | ✓ |
| 24 | 't Hooft 1993 | arXiv API gr-qc/9310026 | title + author + 1993 live ✓ |
| 25 | Susskind 1995 | Crossref 10.1063/1.531249 | ✓ |
| 26 | Maldacena 1998 | Crossref 10.4310/ATMP.1998.v2.n2.a1 | ✓ |
| 27 | Nielsen–Chuang 2000 | Crossref 10.1017/CBO9780511976667 | ✓ (Crossref dates CUP edition 2012; original 2000) |
| 28 | Dragovich et al. 2009 | Crossref 10.1134/S2070046609010014 | ✓ |
| 29 | Bartolomei et al. 2020 | Crossref 10.1126/science.aaz5601 | ✓ |
| 30 | Nakamura et al. 2020 | Crossref 10.1038/s41567-020-1019-1 | ✓ |

## Context checks

- Every entry is used in the context its source supports (terminology-audit.md confirms standard usage; no wrong-context citations found in manuscript read-through).
- No hallucinated authors, venues, or years: all fields cross-checked against Crossref records.
- Version mismatches: none (no arXiv version-number citations).

**Verdict: PASS — 30/30 verified, 0 corrections required.**
