# Citation Audit — AI4MetaScience @ NeurIPS 2026 Position Paper

**Audited:** 2026-08-18 · **Auditor:** direct parent-agent + 3-reviewer CMD RED TEAM (Accuracy/Completeness/Dependency)
**Artifact:** `res/paper/ai4metascience-ignorance-audit/` (position-paper.md/.tex/.pdf, references.bib)

## Method

Every entry in references.bib was verified against live authoritative APIs:
Zenodo Records API (api.zenodo.org/records/{id}) and Crossref (api.crossref.org/works/{doi}),
plus doi.org resolution and OpenAlex as second source where a conflict appeared.
All checks performed 2026-08-18.

## Per-entry verdicts

| Entry | DOI / key | Verdict | Evidence |
|---|---|---|---|
| qunigudzinas2026uia | 10.5281/zenodo.21901984 | ✅ PASS | Zenodo API: "The Universal Ignorance Audit: A Fifteen-Question Method…", v0.3, author Rowan Brad Quni-Gudzinas |
| qunigudzinas2026flagship | 10.5281/zenodo.21208346 | ✅ PASS (fixed) | Zenodo API: real title "The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation" — placeholder surrogate title replaced in .bib/.tex/.md (commit 1921613) |
| qunigudzinas2026knowing | 10.5281/zenodo.21901983 | ✅ PASS | Zenodo API: "Knowing What We Do Not Know: Ignorance Auditing, AI-Generation Detection…", v0.3 |
| firestein2012ignorance | (book, no DOI) | ✅ PASS | OpenAlex/Crossref: real OUP monograph, 2012 |
| landauer1961irreversibility | 10.1147/rd.53.0183 | ✅ PASS | Crossref: IBM JRD 5(3):183–191, exact match |
| merton1987three | 10.1146/annurev.so.13.080187.000245 | ✅ PASS | Crossref: Annu. Rev. Sociol. 13:1–29, match |
| proctor2008agnotology | (book, no DOI) | ✅ PASS | Real Stanford UP edited volume, 2008 |
| tetlock2005expert | (book, no DOI) | ✅ PASS | Real Princeton UP monograph, 2005 (print; JSTOR ebook DOI is the 2017 digital edition — print citation correct) |
| tversky1974judgment | 10.1126/science.185.4157.1124 | ✅ PASS | Crossref: Science 185(4157):1124–1131, match |
| whitcomb2015intellectual | 10.1111/phpr.12228 | ✅ PASS (fixed) | Crossref + OpenAlex agree: PPR **94(3):509–539**, print 2017, online 2015-08-17 — bib had circulating mis-citation 91(1):95–120; corrected to 94(3):509–539, year 2017 (commit 1921613) |

## Zenodo claim consistency

- 10.5281/zenodo.21901984 ↔ Section 3 (instrument): titles match exactly.
- 10.5281/zenodo.21901983 ↔ Section 2 (case documentation): titles match exactly.
- 10.5281/zenodo.21208346 ↔ Section 2 (case subject): record exists, same author, domain consistent (ultrametric foundation; number, time, knowledge, computation — matches p-adic geometry, Bruhat–Tits trees, Landauer bound content).

## Workshop-format compliance (verified live, ai4metascience.org + OpenReview API)

- Footnote exact: "Submitted to AI for Meta-Science workshop (NeurIPS 2026)" ✅ (.tex workshoptitle + .md)
- 8-page limit (position track): PDF = 7 pages including references ✅
- NeurIPS 2026 LaTeX template: neurips_2026.tex uses \documentclass{article} + \usepackage{neurips_2026} + neurips_2026.sty (2026-01-29 lineage) ✅
- No paper checklist needed ✅ · Previously published work welcome ✅ · OpenReview submission ✅
- Blinding: OpenReview group NeurIPS.cc/2026/Workshop/AI4MetaScience — NOT blinded (verified via api2.openreview.net 2026-08-18) — identified submission is compliant ✅
- PDF build pathway: QNFO PYMUPDF-FORBIDDEN-1 (HARD) mandates pandoc → MathJax SVG inline → puppeteer-core page.pdf() ONLY (pdflatex forbidden). PDF built via approved pipeline (GATE PASS 176,682 B, 0 U+FFFD/FFFF, math=4, 7 pages). Template-compliant .tex ships as canonical source alongside.

## Findings disposition

- HARD-1 (placeholder title): FIXED (commit 1921613)
- HARD-2 (Whitcomb locators): FIXED (commit 1921613, year 2017 per print edition)
- HARD-3 (banned word "reality"): FIXED (commit e4ea93e — "distinguishing the map from the territory")
- HARD-1 format (Completeness reviewer): RESOLVED — approved-pipeline PDF + template .tex source (PYMUPDF-FORBIDDEN-1)
- HARD-2 completeness (deposit files): THIS FILE + PROJECT-PLAN.md created (2026-08-18)

## Residual notes

- references.bib is documentation; the .tex uses a hand-written thebibliography (no \cite machinery) — both stores verified identical in content.
- Books (Firestein, Proctor & Schiebinger, Tetlock) have no DOIs — verified as real monographs via Crossref/OpenAlex records.
