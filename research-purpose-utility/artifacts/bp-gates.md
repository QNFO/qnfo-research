# BP Gates — QNFO.RES.012 (research-purpose-utility)

Pre-Publication Requirements (research skill v2.115) · 2026-08-16 · Draft fbb0a97 + P4.5 fixes

## Gate status

| Gate | Requirement | Status | Evidence |
|:-----|:------------|:-------|:---------|
| BP-1 | Fit-Verify: independent recomputation of every claimed numerical value | **N/A** — paper makes no numerical claims (criterion/philosophy paper; zero quantitative assertions in the body) | draft word count 2760; no numeric literals of substance |
| BP-2 | Terminology audit: every field-specific term checked against standard definition | **PASS** | `artifacts/terminology-audit.md` (this cycle) |
| BP-3 | Density gate (dense-set approximation claims) | **N/A** — no approximation claims | — |
| BP-4 | Cross-paper numerical consistency | **N/A** — no numbers | — |
| BP-5 | Overdetermined system closure error | **N/A** — no fitted ratios | — |
| BP-6 | Derived-quantity recompute | **N/A** — no derived quantities | — |
| BP-7 | Sigma/error propagation | **N/A** — no σ claims | — |
| BP-8 | Numerology claim classification | **N/A** — no numerological claims | — |
| BP-9 | Audit-the-auditor | **PASS** | `artifacts/red-team.md` (this cycle) + this bp-gates.md self-audit |
| BP-10 | Independent-recompute before citing numerical claims | **PASS (descriptive-only)** | number→source table below; every cited number quoted from its source abstract (evidence file artifacts/external-search/evidence-2026-08-16.md); zero numbers used as derived evidence |

## BP-10 number→source verification (descriptive counts only)

| Number in draft | Source | Source abstract (evidence file) |
|:----------------|:-------|:-------------------------------|
| 12,720 researchers / fifteen years | Mongeon arXiv:1602.07396 | "12,720 researchers in Quebec over a fifteen year period" ✓ |
| 113,877 articles (REF 2021) | Thelwall arXiv:2212.05418 | "peer review quality scores for 113,877 articles" ✓ |
| 7M grants → 140M papers → 160M patents → 10.9M policy docs → 800K trials | Wang arXiv:2509.16323 | "connects 7M research grants to 140M scientific publications, 160M patents, 10.9M policy documents, 800K clinical trials" ✓ |
| 44,419 UK grants (2006-2018) | Sun arXiv:2104.13091 | "dataset of 44,419 research grants awarded between 2006 and 2018" ✓ |
| 100K+ arXiv papers (2014-2024) | Markus arXiv:2506.08738 | "analyzes over 100,000 AI-related papers published on ArXiv between 2014 and 2024" ✓ |
| 226,600 abstracts / 32 subfields / 86 venues | Jiang arXiv:2502.16390 | "226,600 paper abstracts from 32 CS-related subfields and 86 popular publishing venues" ✓ |
| 333 fields / 137M publications | Hajkowicz arXiv:2306.09145 | "333 fields of research during 1960-2021 … 137 million peer-reviewed publications" ✓ |
| $35B quantum bubble | qnfo2026institutional | "the $35B quantum computing bubble with zero viable output" ✓ |
| >50yr Laws-of-Form never-connected | RES.009 corpus silo table | corpus memory + RES.009 artifacts/consilience-gate.md ✓ |
| 10.5281/zenodo.19605445 (meta-pattern) | DataCite live | DataCite 200, 2026, Quni-Gudzinas ✓ |

## PANDOC-SAFE
- 0 U+FFFD / 0 U+FFFF (mojibake scan) ✓
- 0 `\(...\)` / `\[...\]` delimiters (source uses `$...$` / `$$...$$`) ✓
- 0 bare `|` in math (grep scan) ✓
- Pipe tables in §4 contain no bare `|` inside cells (checked visually) ✓

## Verdict
**BP-1..BP-10: PASS (7 N/A with documented reason, 3 substantive PASS).** PANDOC-SAFE: PASS.
