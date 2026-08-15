# Phase 1 Due Diligence — Gap Analysis

**Project:** QNFO.JPC.002 — JPCUB Applied to AI/LLM Energy Benchmarking
**Slug:** jpcub-llm-energy
**Date:** 2026-08-15
**Status:** Phase 1 (DUE-DILIGENCE-DEPTH-1) — complete

---

## 1. Corpus Sweep Summary

| Source | Tool | Queries | Yield |
|:-------|:-----|:--------|:------|
| Internal KG | `query_graph` | stats + nodes | 8,287 nodes / 8,425 edges; program registry `QNFO.JPC` |
| Internal papers | `search_papers_enriched` | "LLM inference energy efficiency joules per token benchmark" | JPCUB P0 / qudit / competitive-landscape (internal) |
| External (arXiv) | `search_papers` (3 formulations × 3 topics, limit ≥20) | LLM inference energy; AI-vs-brain efficiency; test-time compute; agentic energy; carbon footprint | ~60 unique papers |
| Memory | `recall_facts` + `search_memories` | LLM energy / agentic / J/S | 0 relevant memories (gap confirmed) |
| Cross-system ID | `resolve_paper_id` | 3 JPCUB slugs | all resolve slug→DOI consistently |
| External DOI | DataCite + OpenAlex (curl) | 10.5281/zenodo.21637028 | **verified**: correct title + creators + Zenodo publisher |

## 2. Adjacent WBS Domains (consilience gate — satisfied, ≥2)

- `QNFO.JPC` (host program) · `QNFO.CMP` (Computing Machines) · `QNFO.RES` (Consilience) · `QNFO.UMP` (qudit P2).

## 3. Prior-Art Landscape (external, arXiv)

**Energy-per-token measurement (established):**
- TokenPowerBench (arXiv:2512.03024) — first LLM inference power benchmark; Llama3-405B ≈ 40–60 J/token FP16 on 16×H100; FP8 −30%; MoE ≈ dense 8B.
- "Where Do the Joules Go?" (arXiv:2601.22076) — 46 models / 7 tasks / 1,858 configs; **25× task-type spread** (GPQA problem-solving ≈ 4,625 J/response vs 184 J chat); reasoning = 10× output tokens × smaller batches.
- Energy-to-token position paper (arXiv:2605.11733) — argues Joules/token + PUE-adjusted delivered power as the reporting unit.
- Energy-per-token advocacy (arXiv:2603.20224) — energy-accuracy tradeoff; energy-per-token metric; CoT energy.
- Analytical energy estimator (arXiv:2607.26571) — H100 prefill/decode decomposition.

**Test-time compute / token budget (mechanism, but not joules):**
- Sleep-time Compute (2504.13171); Token-Budget-Aware reasoning (2412.18547); BudgetThinker (2508.17196); BG-MCTS (2602.09574); CoT Token Inflation (2606.25519 — quantization inflates reasoning tokens); CROP (2604.14214 — 80.6% token cut); Reasoning-on-a-Budget survey (2507.02076); Conformal Thinking (2602.03814).

**Carbon / lifecycle (system-boundary evidence):**
- LLMCarbon (2309.14393); LLMSpace (2605.05615); Özcan simulation (2507.11417); scoping review (2511.17179 — "methodological inconsistencies … insufficient attention to end-to-end system perspectives").

**Efficiency (small vs large):**
- Task-Specific PER (2603.21389 — small models win on PER); multi-agent token coherence (2603.15183 — O(n·S·|D|) broadcast overhead).

## 4. Confirmed Gaps (the novelty the project fills)

1. **No joules-per-solution with stochastic correction.** Every energy benchmark reports J/token or J/response; none divides by P(correct) under a stated sampling regime. The "per solution" denominator of JPCUB P0 is absent from the entire LLM-energy literature.
2. **No LLM-vs-human-brain J/S comparison.** The arXiv sweep returned zero works directly comparing LLM energy to the brain (~20 W) on a per-correct-solution basis. (The "human brain" search terms returned unrelated astro/neuro imaging papers — confirming the gap, not filling it.)
3. **No agentic orchestration energy accounting.** Multi-agent token overhead is characterized (2603.15183) but never converted to joules or to J/S.
4. **System-boundary inconsistency** is a documented, unresolved problem (2511.17179) — GPU-only vs PUE-adjusted vs embodied swings results 1.5–5×. JPCUB's six-component boundary is the fix, but no LLM benchmark honors it.
5. **Frontier proprietary models are epistemically opaque** (no joules/query disclosed) — only open-weight models on known hardware are honestly measurable.

## 5. Verdict

The core claim (P6) — that J/S with stochastic + agentic correction shows frontier/agentic LLMs are *not* orders-of-magnitude more efficient than the human brain, with a task-dependent crossover — is a **genuine gap-filling contribution**, not a restatement of existing work. Phase 1 due diligence is satisfied; Phase 2 (metric formalization) may begin.
