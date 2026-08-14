# Citation Audit — P3.AUTHOR-GATE (QNFO.RES.007)

**Project:** Invariant Structural Value
**Date:** 2026-08-14
**Gate:** HARD — every bibliography entry verified against a live source at P3 time; unverified entries are flagged and BLOCKED from final publication until P5 re-verification.

## 1. Verification Method

| Class | Method | Evidence |
|:------|:-------|:---------|
| arXiv entries (9) | `export_citations` — authoritative arXiv metadata (title/author/year/primaryClass from arXiv API, never model-generated) | export_citations result, 9/9 success |
| DOI journal/book entries | OpenAlex + Crossref API responses saved to `external-search/openalex_*.json` / `crossref_*.json` — authors, year, DOI, journal, biblio | 17 entries verified from these JSONs |
| QNFO corpus entries (15) | `resolve_paper_id` (slug → DOI) + Zenodo record search in Phase 1/2 | due-diligence-phase1.md §2 table |
| Canonical background (3) | Known literature (Worrall 1989; Spencer-Brown 1969; Joyal-Street 1991) — DOI/page metadata FLAGGED for P5 re-verify | flag in references.bib |
| Preprints (2) | Europe PMC hit — authors NOT extracted at P3; FLAGGED | flag in references.bib |

## 2. Entry-by-Entry Status

### VERIFIED (arXiv export — authoritative)
1. haro2025the — De Haro & Butterfield 2025 ✓
2. sola2015fundamental — Solà 2015 ✓
3. thompson2017the — Thompson 2017 ✓
4. knuth2015the — Knuth 2015 ✓
5. rovelli2018physics — Rovelli 2018 ✓
6. ronde2023bohrs — de Ronde 2023 ✓
7. moldoveanu2013quantum — Moldoveanu 2013 ✓
8. ezhela2004the — Ezhela, Kuyanov, Larin, Siver 2004 ✓
9. mohr2007codata — Mohr, Taylor, Newell 2007 ✓

### VERIFIED (OpenAlex/Crossref evidence JSON)
10. laudan1981confutation — Larry Laudan; Phil. Sci. 48(1):19-49; 1981; 10.1086/288975 ✓
11. ladyman2007everything — Ladyman, Ross, Spurrett, Collier; OUP 2007 ✓
12. ladyman2007ontic — same 4 authors; OUP chapter 2007 ✓
13. ladyman2013structural — James Ladyman; OBO entry 2013 ✓
14. tulodziecki2016structural — Dana Tulodziecki; SHPSA 2016 ✓
15. landry2011methodological — Elaine M. Landry; Springer 2011 ✓
16. worrall2011miracles — John Worrall; Springer 2011 ✓
17. esfeld2006moderate — Esfeld & Lam; Synthese 160(1):27-46 2006 ✓ (OpenAlex DOI 10.1007/s11229-006-9076-2 — NOTE: differs from Phase-2 draft's "-8" typo; corrected)
18. ainsworth2010what — Ainsworth; SHPSB 41(1) 2010 ✓
19. mckenzie2017ontic — McKenzie; Phil Compass 12(4) 2017 ✓
20. nounou2015foragainst — Nounou; SHPSB 2015 ✓
21. esfeld2009modal — Esfeld; ISPS 23(2) 2009 ✓
22. lyre2004holism — Lyre; SHPSB 35(4) 2004 ✓
23. french2011shifting — French; SHPSC 42(2) 2011 ✓
24. maciejko2010topological — Maciejko, Qi, Drew, Zhang; PRL 105:166803 ✓
25. butterfield2021dualities — Butterfield; OUP 2021 ✓
26. polchinski2015dualities — Polchinski; SHPSB 2015 ✓
27. kapustin2007electric — Kapustin & Witten; CNTP 1(1) 2007 ✓
28. peebles2003cosmological — Peebles & Ratra; RMP 75(2):559-606 ✓
29. carroll2001cosmological — Carroll; LRR 4:1 ✓
30. carter1976understanding — Brandon Carter; Springer 1976 ✓
31. ashby1956introduction — W. Ross Ashby; Chapman & Hall 1956 ✓

### VERIFIED (QNFO corpus — resolve_paper_id / Zenodo)
32. odr2026 — 10.5281/zenodo.21756190 (v4.0.4) ✓
33. qmigs2026 — 10.5281/zenodo.20109773 ✓
34. fscrossratio2026 — 10.5281/zenodo.20108536 ✓
35. syntactictoken2026 — 10.5281/zenodo.19547736 ✓
36. alphapihelix2026 — 10.5281/zenodo.21515789 ✓ (v2.1 record DOI 21420521/21419867 exist; 21515789 is the authoritative KG/living-paper DOI)
37. qlof2026 — 10.5281/zenodo.21205110 ✓
38. calculusdistinction2026 — 10.5281/zenodo.21205097 ✓
39. computablereal2026 — 10.5281/zenodo.21645350 ✓
40. baseinvariant2026 — 10.5281/zenodo.19469966 ✓
41. winding2025 — 10.5281/zenodo.17322662 ✓
42. strangeloop2025 — 10.5281/zenodo.17419332 ✓
43. notationproblem2026 — 10.5281/zenodo.21690262 ✓
44. adeliccore2026 — 10.5281/zenodo.21786473 ✓ (draft status)
45. adelicconstraints2026 — 10.5281/zenodo.20120042 ✓
46. physicsolved2025 — 10.5281/zenodo.17368960 ✓ (Tier-4 contrast only)

### FLAGGED — P5 re-verification REQUIRED (BLOCK final citation until re-checked)
47. **domainprojection2026** — Research Square preprint 10.21203/rs.3.rs-8629054/v1; author NOT extracted from Europe PMC hit at P3. [P5: fetch record, extract authors, verify against RS page]
48. **z3graded2025** — Preprints.org 10.20944/preprints202512.2527.v2; author NOT extracted. [P5: same]
49. **worrall1989structural** — Dialectica 43(1-2):99-124; DOI 10.1111/j.1746-8361.1989.tb00933.x from canonical knowledge; not independently re-queried at P3. [P5: doi.org HEAD + Crossref verify]
50. **joyalstreet1991geometry** — Adv. Math. 88(1):55-112, DOI 10.1016/0001-8708(91)90003-P; same treatment. [P5: verify]
51. **spencerbrown1969laws** — book, no DOI; canonical. [P5: confirm edition/year if cited with page refs]

## 3. Cross-Cutting Notes

- **Data-quality finding (Phase 1 carried):** invariant-patterns-adelic-refactoring DOI mismatch (Zenodo 21785893 vs KG 21786511) — this record is NOT in references.bib (adjacent only); flagged for kaizen reconciliation, not this paper's P3.
- **Phase-2 typo corrected:** esfeld2006moderate DOI corrected from 10.1007/s11229-006-9076-**8** to 10.1007/s11229-006-9076-**2** (OpenAlex-authoritative).
- **BP-10 (Independent recompute):** applies to any numerical claim this paper makes about α or other constants in P4 — not to bibliography entries; referenced for P4 gate.
- **AUTHOR-GATE verdict:** 46/51 entries VERIFIED at P3; 5 FLAGGED (2 preprints + 3 canonical) — none may appear in the final published reference list until P5 re-verification completes. This audit file ships with the deposit (PUBLICATION-SOURCE-COMPLETENESS-1).
