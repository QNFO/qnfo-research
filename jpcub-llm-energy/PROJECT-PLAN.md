# PROJECT-PLAN: JPCUB Applied to AI/LLM Energy Benchmarking

**Version:** v0.1-phase0
**Date:** 2026-08-15
**Repo:** QNFO/qnfo-research
**Branch:** res/paper/jpcub-llm-energy
**WBS:** QNFO.JPC.002
**Slug:** jpcub-llm-energy
**Series:** Joules-per-Compute Universal Benchmark (JPCUB) — Paper P3 (AI/LLM application)

---

## 0. WBS Resolution Record (Phase 0 — net-new project)

Resolved from the QNFO knowledge graph (D1-backed `nodes` table, the program registry):

| Field | Value |
|:------|:------|
| Program | `QNFO.JPC` — JPCub Validation (`wbs_order: 8`, `slug: jpcub-validation`) |
| Parent project | `QNFO.JPC.001` — JPCub Validation (`github_repo: QNFO/jpcub-validation`) |
| **New project WBS** | **`QNFO.JPC.002`** (next available after `.001`; no collision detected in KG) |
| GitHub repo | `QNFO/qnfo-research` (canonical for net-new research papers; `res/paper/<slug>` branch convention) |
| Branch | `res/paper/jpcub-llm-energy` |
| Slug | `jpcub-llm-energy` |

Series lineage: P0 = `joules-per-solution-metric` (DOI 10.5281/zenodo.21637028); P1 = `jpcub-competitive-landscape` (DOI 10.5281/zenodo.21821767, WBS `QNFO.RES.JPCUB-CL`); P2 = `qwave-qudit-advantage` (DOI 10.5281/zenodo.21880104, WBS `QNFO.UMP.005`). This project is P3: the first application of the J/S metric to AI/LLM inference.

---

## 1. Charter

The JPCUB joules-per-solution (J/S) metric was defined in P0 for deterministic solvers (classical and quantum), where one run produces one correct answer with bounded probability. AI/LLM systems break two of P0's implicit assumptions, and no existing benchmark addresses the consequence:

1. **Stochasticity** — an LLM produces a *distribution* over outputs, not a guaranteed solution. The entire "joules-per-token" literature (TokenPowerBench, ML.ENERGY, LLMCarbon) measures energy per token/response but never divides by the probability of a *correct* answer.
2. **Orchestration** — agentic and frontier-reasoning systems spend energy not on one forward pass but on a graph of sub-calls, tool invocations, retries, and reasoning-token budgets. "One solution" is not "one inference."

This project defines the J/S metric for stochastic and agentic inference, computes defensible order-of-magnitude estimates for frontier and agentic models from published measurement data, and compares them against the human brain as a biological energy baseline (~20 W). The goal is the same falsifiable discipline P0 imposed on quantum computing: force AI energy claims to survive the "per correct solution" denominator.

### 1.1 Strategic Rationale

| Dimension | Why this project |
|:----------|:-----------------|
| **QNFO (publications)** | Extends JPCUB from quantum (P0–P2) to the AI/LLM paradigm — the highest-visibility, highest-spend compute paradigm today (~$35B+ inference market) |
| **Honest benchmarking** | The "AI vs human brain efficiency" debate is dominated by asymmetric accounting (marginal vs amortized, GPU-only vs system, joules/token vs joules/solution). A defensible J/S treatment resolves the asymmetry |
| **Research continuity** | Bridges P0's metric, the qudit advantage (P2), and the computing-machines survey; applies the same anti-gaming discipline to AI |
| **Falsifiable** | Explicit disconfirmation conditions (§1.2) — if frontier/agentic LLMs are actually orders-of-magnitude more efficient per correct solution than the brain, the project publishes *that* |

### 1.2 Core Claim Lock (P6)

> **Claim (P6):** When AI/LLM systems — especially frontier reasoning and agentic models — are benchmarked in joules-per-solution (J/S) under the full system boundary, with a stochastic correction ($E[J] / P(\text{correct})$ at a stated sampling regime) and an agentic orchestration accounting, they are **not** orders of magnitude more energy-efficient than the human brain on verifiable cognitive tasks. On cheap, high-accuracy, single-shot tasks the LLM wins by ~1–3 orders of magnitude; on hard verifiable reasoning and agentic tasks, LLM J/S converges to within ~1 order of magnitude of — and frequently exceeds — the expert-human baseline ($\approx 20\,\mathrm{W} \times t_{\text{sol}}$). The crossover is governed by task verifiability, accuracy, and token budget, not by intrinsic substrate advantage.

> **Falsification condition (P6-F):** The claim is **falsified** if a measured frontier/agentic LLM, under the full J/S system boundary and a standardized sampling regime, achieves $J/S < 10^{-1}\times$ the expert-human baseline at matched accuracy on $\ge 2$ of 3 canonical hard-reasoning task classes (GPQA-grade graduate reasoning; SWE-bench-grade verified coding; verified multi-step mathematics). It is **also falsified** if the $(J/S,\ \text{accuracy})$ Pareto frontier for reasoning-budget scaling shows non-diminishing (linear or super-linear) accuracy returns past the measured knee.

> **Primary risk (pre-mortem):** the estimates are order-of-magnitude and depend on published GPU-only energy data that understate the full system boundary by ~1.5–3×. Mitigation: state every assumption explicitly, report both GPU-only and PUE-adjusted numbers, and treat the *shape* of the crossover (not any single number) as the load-bearing claim.

---

## 2. Work Breakdown Structure

### Phase 0: Project Initialization (THIS PHASE)
- [x] WBS resolved from program registry → `QNFO.JPC.002`
- [x] Branch `res/paper/jpcub-llm-energy` created from clean `origin/main`
- [ ] PROJECT-PLAN.md written
- [ ] Core claim (P6) locked
- [ ] Commit / tag `v0.1-phase0` / push / verify via `git ls-remote`

### Phase 1: Due Diligence (DUE-DILIGENCE-DEPTH-1)
- [ ] `query_graph(stats)` baseline
- [ ] Full-corpus sweep: ≥3 query formulations per topic, `search_papers` limit ≥20 + `search_papers_enriched` + `recall_facts` + `search_memories`
- [ ] Cross-system ID validation: `resolve_paper_id` per hit (slug → Vectorize → KG → DOI)
- [ ] ≥2 adjacent WBS domains (QNFO.JPC + QNFO.CMP + QNFO.RES)
- [ ] External verification: arXiv / OpenAlex / Crossref (+ archive.org CDX + Google Patents where claims are date/priority-sensitive)
- [ ] Gap analysis + `update_plan` with WBS codes

### Phase 2: Metric Formalization (J/S for stochastic + agentic inference)
- [ ] Closed-form stochastic correction $J/S = E[J] \cdot n_{\text{samples}} / P(\text{correct})$
- [ ] Agentic orchestration accounting (total-token attribution across the call graph)
- [ ] Human-brain baseline formalization (20 W brain-only; attribution rule pre-registered)

### Phase 3: Estimation & Comparison
- [ ] Task-stratified J/S table (QA / math / graduate reasoning / agentic coding)
- [ ] Training-amortization asymmetry (LLM vs human education)
- [ ] Pareto frontier for reasoning-budget scaling

### Phase 4: Publication
- [ ] Full paper (Genre A: falsifiable claims, Pandoc/MathJax-safe)
- [ ] Citation audit + paper-claim audit
- [ ] Zenodo deposit + metadata provenance note
- [ ] Post-publication red-team (accuracy / completeness / dependency)

---

## 3. Adjacent WBS Domains (consilience gate)

| WBS | Domain | Relevance |
|:----|:-------|:----------|
| `QNFO.JPC` | JPCub Validation | Host program (this project) |
| `QNFO.CMP` | Computing Machines | AI accelerators are the subject hardware |
| `QNFO.RES` | Consilience | Human-brain comparison is a cross-paradigm consilience claim |
| `QNFO.UMP` | Ultrametric Physics | Prior qudit-advantage paper (P2) filed here |

---

## 4. Known Methodological Gaps (to be filled in Phases 2–3)

1. No canonical "solution" taxonomy for verifiable LLM tasks (vs. open-ended generation, where J/S is ill-posed).
2. No published benchmark reports expected-cost-per-correct-answer with a sampling regime.
3. Reasoning-budget (test-time compute) is a free parameter — the (J/S, accuracy) frontier is unmeasured.
4. Agentic orchestration energy is unmeasured (multi-agent broadcast is O(n·S·|D|); cf. arXiv:2603.15183).
5. System boundary inconsistency (GPU-only vs PUE-adjusted vs embodied) swings results 1.5–5×.
6. Frontier proprietary models (GPT-4/Claude/Gemini) disclose no joules/query — epistemically opaque.
7. Human baseline has no standard attribution rule (brain-only vs full-body vs task-marginal; education amortization).
