# Due Diligence Report — QNFO.RES.006

**Project:** Implications for Computing and Quantum Error Correction
**Slug:** prime-valuation-qec-implications
**Anchor:** Prime Valuation Depth (QNFO.RES.005, DOI 10.5281/zenodo.21918838)
**Date:** 2026-08-13
**Phase:** P1 (Due Diligence)

---

## 1. Method

| Step | Tool | Result |
|:-----|:-----|:-------|
| KG ecosystem | `query_graph(stats)` | 8,270 nodes / 8,410 edges; Paper=1,619, Program=16, Project=148 |
| WBS resolution | D1 `portfolio-state.program_registry` | RES.006 assigned; anchor = RES.005 (published, P8) |
| KG paper search | `query_graph(nodes, "quantum error correction")` | 16 hits |
| KG paper search | `query_graph(nodes, "p-adic")` | 50 hits (capped) |
| Semantic search | `search_papers_enriched` | 5 hits (top-ranked) |
| Durable recall | `recall_facts` (QEC / p-adic) | 1 + 1 records |
| Semantic memory | `search_memories` | 0 hits (QEC gap query) |

**Tool gap (SOFT):** `search_papers` is not available in this session — Phase 1 (a) external literature search via Vectorize must route through `search_papers_enriched` and `query_graph(nodes)` instead. Logged for kaizen.

## 2. QNFO Cross-Reference — the p-adic QEC corpus is already densely populated

The KG + Vectorize reveal a substantial existing QNFO corpus at the exact intersection of this project. This is the single most important due-diligence finding: **the "implications for computing and QEC" are not a blank slate — QNFO has already produced a large p-adic QEC and p-adic computing literature.**

**Directly overlapping p-adic QEC papers (DOI):**
- Number-Theoretic Ultrametric Foundations: A Unified p-adic Framework for Error-Correcting Code Classification — **10.5281/zenodo.21193487** (the "83% accuracy" source; Kodaira-Néron classifier; 7 pillars; Mahler v_p-spectral decomposition)
- Qudit Quantum Error Correction — 10.5281/zenodo.21046993
- p-Adic QEC Classifier Verification: A Computational Methodology — 10.5281/zenodo.21698279
- Adelic QEC: Code Constructions Beyond the Stabilizer Formalism — 10.5281/zenodo.21205100
- Adelic QEC: Intrinsic Qubit Protection from Ostrowski — 10.5281/zenodo.21336099
- Ultrametric Code Spaces: Bruhat-Tits Tree as a Geometry for QEC — 10.5281/zenodo.21819232
- Toward p-adic QEC: The Metric Mismatch Hypothesis — 10.5281/zenodo.20556327
- Ultrametric Information Geometry: From p-Adic Spaces to QEC — 10.5281/zenodo.21204115
- Adelic QEC: A Synthesis Across All Primes — 10.5281/zenodo.20570212
- p-adic Quantum Hardware: Qubit Layouts for Ultrametric EC — 10.5281/zenodo.20570236
- Quantum Error Correction Is a Misnomer — 10.5281/zenodo.21204706
- Ultrametric Physics Module 5: Ratio-Based QEC — 10.5281/zenodo.19437432
- Adelic Rate-Distortion Theory — 10.5281/zenodo.21705076

**Overlapping p-adic computing papers (DOI):**
- Exact Rational Arithmetic via p-adic Hensel Codes — 10.5281/zenodo.20754449 / .20756305 / .20756222
- The Morita p-Adic Gamma Function — 10.5281/zenodo.20119700
- Spectral Dynamics on Bruhat-Tits Trees (primality testing) — 10.5281/zenodo.18629520
- The Fontaine-Stack (thermodynamically viable QC) — 10.5281/zenodo.21335256
- The QWAV Decade: Enterprise p-Adic Computing 2025-2035 — 10.5281/zenodo.21722393
- Q-PNA: Quantum-Native p-Adic Neural Architecture — 10.5281/zenodo.20287743

## 3. Gap Analysis

**What is already covered (do NOT re-derive):**
- p-adic QEC classification (Kodaira-Néron, Mahler spectral, Ostrowski protection, Bruhat-Tits geometry) — QNFO.UF and the Adelic QEC program.
- p-adic computing (Hensel codes, Morita gamma, enterprise roadmap).

**What is genuinely new in THIS project (the differentiation):**
1. The **branch-depth reading** is specific to Prime Valuation Depth: v_p(n) as *depth along a prime branch* (not size, not spectral weight). The existing corpus uses p-adic valuation as a *classifier weight* (Kodaira-Néron/Mahler), not as a *depth metric*.
2. The **calculus-of-indications bridge** (Spencer-Brown distinction/branching) is absent from the existing QEC corpus — that cross-domain bridge is unique to the Prime Valuation Depth lineage.
3. The **no-cloning-as-structural** reading (no linear diagonal map; monoidal-not-Cartesian) as the *root* of QEC limits is not the framing used by the existing corpus (which treats QEC constructively via codes, not via the no-go theorem that forces QEC to exist).
4. The **[[n,k,d]] ↔ branch-depth mapping** (n = v_2(dim H), k = v_2(dim H_L), d = branch-crossing weight) is a specific, checkable claim not stated in the existing corpus.

**Verdict:** The project is *not* novel in its territory (p-adic QEC is heavily pre-worked) but *is* novel in its specific bridge (branch-depth + calculus of indications + structural no-cloning → [[n,k,d]]). The core claim's falsifiability conditions (§2 of PROJECT-PLAN) are designed to force this differentiation or fail honestly.

## 4. Findings

| ID | Severity | Finding |
|:---|:---------|:--------|
| F1 | HARD (fixed) | The "83% accuracy" prior result was initially cited as DOI 10.5281/zenodo.21046993 (Qudit QEC); the correct source is 10.5281/zenodo.21193487 (Number-Theoretic Ultrametric Foundations). Corrected in PROJECT-PLAN.md, README.md, docs/core-claim.md. |
| F2 | SOFT | `search_papers` tool unavailable this session; semantic search routed through `search_papers_enriched`. |
| F3 | [CONFIRMATION-BIAS-RISK] | All QEC/p-adic hits are QNFO-internal. External literature (OpenAlex/arXiv/Crossref) was NOT yet queried. Phase 2 must run the 8-source external search to distinguish internal vs external corroboration. |
| F4 | DESIGN | The "83% accuracy" claim must be independently reproduced or refuted (fresh train/test split) — currently it is an unverified internal report. This is P4 critical path. |
| F5 | DESIGN | Registry `program_registry` QNFO.UF description links DOI 21046993 to the "83%" summary, but that DOI is "Qudit QEC". Suggest a registry metadata correction as a follow-up (not blocking this project). |

## 5. External Literature Status

Not yet executed (Phase 2). The 8-source external search (OpenAlex PRIMARY, Crossref, Zenodo, Europe PMC, arXiv, web, QNFO Vectorize, QNFO KG) is the next gate. Evidence discipline: save every response to `artifacts/external-search/`.
