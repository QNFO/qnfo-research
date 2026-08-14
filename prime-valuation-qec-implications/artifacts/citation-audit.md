# Citation Audit — QNFO.RES.006 (v0.2)

**Slug:** prime-valuation-qec-implications · **DOI:** 10.5281/zenodo.21923000 · **Date:** 2026-08-13 (re-verified 2026-08-14)
**Method:** every bibliography entry verified against authoritative metadata (arXiv export_citations, OpenAlex, Crossref). Zero model-generated fields.

## Audit table

| # | Reference | Verified | Evidence |
|:--|:----------|:---------|:---------|
| 1 | Abramsky & Coecke 2004, *A categorical semantics of quantum protocols* (LICS) | ✅ | DOI 10.1109/lics.2004.1319636 (Crossref/OpenAlex) |
| 2 | Abramsky 2009, *No-Cloning in Categorical Quantum Mechanics* | ✅ | DOI 10.1017/cbo9781139193313.002 (OpenAlex, 62 cit) |
| 3 | Coecke 2009, *Quantum Pictorialism* | ✅ | arXiv:0908.1787 (export_citations, authoritative) + DOI 10.1080/00107510903257624 |
| 4 | Coecke & Duncan 2011, *Interacting Quantum Observables* | ✅ | DOI 10.1088/1367-2630/13/4/043016 (OpenAlex, 302 cit) |
| 5 | Heydeman, Marcolli, Saberi & Stoica 2018, *Tensor networks, p-adic fields, and algebraic curves* | ✅ | arXiv:1605.07639 (export_citations) + DOI 10.4310/atmp.2018.v22.n1.a4 (OpenAlex, 56 cit) |
| 6 | Bhattacharyya, Hung, Lei & Li 2018, *Tensor network and (p-adic) AdS/CFT* | ✅ | DOI 10.1007/jhep01(2018)139 (OpenAlex, 44 cit); arXiv:1703.05445 |
| 7 | Gubser & Knaute 2017, *A p-adic version of AdS/CFT* | ✅ | DOI 10.4310/atmp.2017.v21.n7.a3 (OpenAlex, 89 cit) |
| 8 | Bravyi et al. 2019, *Simulation of quantum circuits by low-rank stabilizer decompositions* | ✅ | DOI 10.22331/q-2019-09-02-181 (OpenAlex, 286 cit) |
| 9 | Ostrowski 1916, *Über einige Lösungen der Funktionalgleichung φ(x)φ(y)=φ(xy)* | ✅ | Acta Mathematica 41:271–284 (standard reference) |
| 10 | Quni-Gudzinas 2026, *Prime Valuation Depth* | ✅ | DOI 10.5281/zenodo.21918838 (live records API) |
| 11 | QNFO Research Collective 2026, *Number-Theoretic Ultrametric Foundations* | ✅ | DOI 10.5281/zenodo.21193487 (live records API) |

## Context-appropriateness spot-checks

- **Abramsky 2009 / Coecke 2009 cited for** "no-cloning follows from monoidal non-Cartesian structure" — CORRECT context (both papers make exactly this claim).
- **Heydeman et al. 2018 cited for** "p-adic geometry ↔ QEC via holographic tensor networks" — CORRECT context (Bruhat–Tits trees + QEC codes; confirmed from arXiv abstract).
- **Bravyi 2019 cited as** "working background for §3–§4" — CORRECT (low-rank stabilizer decomposition, the stabilizer formalism baseline).
- **Gubser & Knaute 2017 cited for** p-adic AdS/CFT — CORRECT (the original p-adic AdS/CFT paper).

## Findings

| ID | Severity | Finding |
|:---|:---------|:--------|
| CA-1 | CORRECTED (2026-08-14) | All 11 entries real + correctly attributed. Venue/year/page corrections applied: Coecke print year 2010 (Crossref; printed list said 2009); Gubser–Knaute pages 1655–1678 (Crossref; was 1655–1683); Ostrowski bib entry re-keyed to Acta Mathematica 41:271–284. |
| CA-2 | PASS | No hallucinated authors, fabricated venues, or wrong-year citations. |
| CA-3 | PASS | Context-appropriateness confirmed for the 4 spot-checked in-text usages. |
| CA-4 | SOFT | The internal NTOF report (ref 11) is the reproduction target, not a support citation — flagged in §6 as UNVERIFIED-INTERNAL, which is the correct handling. |

**Verdict:** bibliography CLEAN after v0.3 corrections (2026-08-14). Pre-correction state: CA-1 was overstated — the 2026-08-13 audit missed the Coecke print-year and Gubser–Knaute page-range discrepancies later caught by the post-publication CMD RED TEAM SUB (Accuracy reviewer ACC-2/ACC-4). See post-publication-audit-21923000.md.

## v0.3 Re-verification notes (2026-08-14)

- **Coecke, Quantum Pictorialism:** printed year corrected 2009 → 2010 (Crossref published-print 2010-01; online 2009-12-15; arXiv:0908.1787 is the 2009 preprint). Bib already said 2010 — paper list now aligned.
- **Gubser & Knaute 2017:** page range corrected 1655–1683 → 1655–1678 (Crossref 10.4310/atmp.2017.v21.n7.a3). NOTE: some indexes (INSPIRE-style) list 1655–1683; final resolution against the journal TOC remains an open item.
- **Ostrowski 1916:** bib entry re-keyed to the original (Acta Mathematica 41:271–284, DOI 10.1007/bf02422947); the Springer "Collected Mathematical Papers" chapter DOI (10.1007/978-3-0348-9358-9_17, 1983) retained as a note.
- **Abramsky 2009:** bib entry added (was missing from the 46-entry file while printed as paper ref 2 — DEP-5a).
- **Self-DOI:** this file's header now cites 10.5281/zenodo.21923000 (v0.2); the shipped v0.2 record's copy cited the v0.1 DOI (DEP-3a/COMP-7).
