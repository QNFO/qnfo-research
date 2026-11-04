# Citation Audit — The Revolutionary Beginner's Guide to Quantum Computing (v1.3.3)

Audit date: 2026-08-21 (v1.3 additions live-verified). Method: every bibliographic entry verified live against
Crossref (api.crossref.org), the arXiv API, and the Zenodo records API. No entry
was accepted on the citing text's word alone. Author lists checked for every
entry (P3.AUTHOR-GATE-EVERY-ENTRY-1).

## External literature (verified live)

| # | Entry (as cited) | Verification | Result |
|:-:|:-----------------|:-------------|:-------|
| 1 | Preskill (2018), *Quantum* 2, 79 | Crossref 10.22331/q-2018-08-06-79 | PASS — author Preskill, vol 2 |
| 2 | Hempel (2026), *Quantum Technologies*, Springer, ch. 2 | Crossref 10.1007/978-3-031-90727-2_2 | PASS — author Hempel, container Quantum Technologies |
| 3 | Acharya et al. (2025), *Nature* 638, 920–926 | Crossref 10.1038/s41586-024-08449-y | PASS — issued 2024, Nature vol 638 |
| 4 | Google Quantum AI (2023), *Nature* 614, 676–681 | Crossref 10.1038/s41586-022-05434-1 | PASS — vol 614 |
| 5 | Fowler, Mariantoni, Martinis, Cleland (2012), *PRA* 86, 032324 | Crossref 10.1103/PhysRevA.86.032324 | PASS — 4-author list matches |
| 6 | Kliuchnikov, Maslov, Mosca (2013), *QIC* 13(7&8), 607–630 | Crossref 10.26421/qic13.7-8-4 | PASS — 3-author list matches |
| 7 | Shor (1994), FOCS | Crossref 10.1109/SFCS.1994.365700 | PASS |
| 8 | Grover (1996), STOC | Crossref 10.1145/237814.237866 | PASS |
| 9 | Nielsen & Chuang (2010), CUP | Standard textbook, ISBN 9781107002173 | PASS |
| 10 | Gubser, Knaute, Parikh, Samberg, Witaszczyk (2016), arXiv:1605.01061 | arXiv API | PASS — 5-author list matches |
| 11 | Marcolli (2018/2020), arXiv:1801.09623 / *PAMQ* 16(1), 1–33 | Crossref 10.4310/pamq.2020.v16.n1.a1 | PASS — PAMQ = Pure and Applied Mathematics Quarterly, 16(1) |
| 12 | Rammal, Toulouse, Virasoro (1986), *RMP* 58(3), 765–788 | Crossref 10.1103/RevModPhys.58.765 | PASS — 3-author list matches |
| 13 | Popper (1959), *The Logic of Scientific Discovery*, Hutchinson | Standard reference | PASS |
| 14 | Planck Collaboration (2020), *A&A* 641, A1 | Crossref 10.1051/0004-6361/201833910 | PASS |
| 15 | NIST (2024), FIPS 203/204/205 | NIST finalized PQC standards Aug 2024 | PASS |
| 16 | Maity, Onggadinata, Koh (2026), arXiv:2608.03944 | arXiv API | PASS — 3-author list matches |

## QNFO/QWAV program records (verified live on Zenodo)

| DOI | Verification | Result |
|:----|:-------------|:-------|
| 10.5281/zenodo.17938113 | records API 200, v2.0, title matches | PASS |
| 10.5281/zenodo.20109835 | records API 200, v0.1.15, title matches | PASS |
| 10.5281/zenodo.20014913 | records API 200, v0.20, title matches | PASS |
| 10.5281/zenodo.20134944 | records API 200, v0.1, title matches | PASS |
| 10.5281/zenodo.20154558 | records API 200, v0.3, title matches | PASS |
| 10.5281/zenodo.20302276 | records API 200, v1.0, title matches | PASS |
| 10.5281/zenodo.22025544 | records API 200, v1.4, title matches | PASS |
| 10.5281/zenodo.21964674 | records API 200, v1.11, title matches | PASS |
| 10.5281/zenodo.21979060 | records API 200, title matches | PASS |
| 10.5281/zenodo.21991953 | records API 200, v2.1.1, title matches | PASS |
| 10.5281/zenodo.21991899 | records API 200, v1.1.2, title matches | PASS |
| 10.5281/zenodo.21880104 | records API 200, v0.7, title matches | PASS |
| 10.5281/zenodo.17955898 | records API 200, 1.0.1, title matches | PASS |
| 10.5281/zenodo.21747228 | records API 200, 1.0, title matches | PASS |
| 10.5281/zenodo.22012694 | records API 200, 1.1.2, title matches | PASS |
| 10.5281/zenodo.21992229 | records API 200, 0.9, title matches | PASS |

## In-text numeric claims tied to citations

- Google 2023 logical error per round: d=3 → 3.028%, d=5 → 2.914%, Λ = 2.14 ± 0.02
  (matches the published abstract; recomputed independently in
  artifacts/verification/verify_guide_claims.py).
- BTQP thresholds 50.0% / 75.0% / 17.30% and validation results (500 trials,
  p_err = 0.40, E_barrier = 2^d, 15,000 trials) — verbatim from the deposited
  abstracts of 10.5281/zenodo.20109835 and 10.5281/zenodo.20134944.

## Findings and dispositions

1. **No fabricated or misattributed entries.** Every author list verified.
2. **Three non-DOI internal references** remain (Lifecycle of a Fault-Tolerant
   Quantum Computer, QWAV Strategy Archive; A Different Geometry for Computing,
   QNFO/.github releases; Honest Investment Assessment, QWAV Strategy Archive) —
   these are program-internal documents without registered DOIs; they are
   cited as program documents, not as published literature, and are marked
   `[PROP]`/`[EST]` accordingly. No replacement citation exists.
3. **v1.1 numeric corrections** (5) are recorded in the verification log —
   see Appendix B of the manuscript.

Auditor: research-pipeline automated citation audit (live API verification).
