# Ignorance Audit Papers — v0.3 (2026-08-12)

Post-publication adversarial review (Zenodo 21878977 + 21878976) identified 13 HARD /
16 SOFT / 9 DESIGN findings. This directory holds the corrected v0.3 sources.

## Records

- **Paper A** (Knowing What We Do Not Know...) — v0.3 = 10.5281/zenodo.21901983 (supersedes v0.2 10.5281/zenodo.21878977)
- **Paper B** (The Universal Ignorance Audit...) — v0.3 = 10.5281/zenodo.21901984 (supersedes v0.2 10.5281/zenodo.21878976)
- **2026c Corrections and Governance Record** — 10.5281/zenodo.21901930 (new, resolves the previously-unresolvable citation)
- **ERRATA.md** — attached to the governance record

## v0.3 Fixes Applied

| Finding | Fix |
|:--------|:----|
| H-1 2026c unresolvable | Corrections and Governance Record published (10.5281/zenodo.21901930); DOI added to citation |
| H-2 2026b title mismatch | Reference corrected to registered title |
| H-3 Kreps metadata | JEPS 7(2):90-102 → 9(1):104-117 |
| H-4 Whitcomb metadata | PPR 91(1):95-120 → 94(3):509-539 |
| H-5 forensic analyses not deposited | Claim qualified: commissioned + AI-assisted, bounded independence; governance record documents them |
| H-6 fabrication rebuttal unverifiable | Organization identity made verifiable via published governance record + public corpus |
| H-7 ERRATA.md absent | ERRATA.md created + deposited in governance record |
| H-8 AI disclosure not checkable | Model/assistant identified (DeepChat + DeepSeek LLM); prompt history availability noted |
| H-9 reproducibility limitation | Added to Paper B meta-audit limitation list |
| H-10 selection criteria | Added to Paper B §5 worked applications |
| H-11 §3.2 overstatement | Landauer characterization softened to match the analyzed paper's own hedging |
| H-12 "two independent" asserted | Qualified: commissioned by author, AI-assisted, convergence = convergent markers |
| H-13/D-1 self-citing corpus | Explicit disclosure added to Data availability |
| S-2 Dietvorst gloss | Softened to match source finding |
| D-1 Q14 label | Aligned "aporia question" with relational-ignorance definition |
| Merton page range | 13:1-28 → 13:1-29 (verified via annualreviews.org live) |

## Build

Canonical CDP pipeline: pandoc --mathjax → MathJax SVG inline → puppeteer-core page.pdf (A4, 2cm margins).
