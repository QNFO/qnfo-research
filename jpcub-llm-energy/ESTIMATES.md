# Task-Stratified Joules-per-Solution Estimates: LLM / Agentic AI vs Human Brain

**Project:** QNFO.JPC.002 — jpcub-llm-energy (JPCUB Paper P3)
**Phase:** 3 (Estimation & Comparison)
**Date:** 2026-08-15
**Status:** Draft — Phase 3

---

## 1. Pre-registered Assumption Block

Every estimate below is order-of-magnitude and audit-trailed to published sources. Changing any assumption moves numbers; the *shape* of the result (Section 7) is robust to ±3× in any single input.

| ID | Assumption | Value | Source |
|:---|:-----------|:------|:-------|
| A1 | GPU-only J/token (frontier MoE, e.g., Qwen3-235B-A22B Thinking FP8, min-energy) | ~0.4 J/token | 2601.22076 (measured, B200 min-energy config) |
| A2 | GPU-only J/token (mid dense, e.g., Qwen3-32B) | ~0.15–0.31 J/token | 2601.22076 |
| A3 | GPU-only J/token (frontier dense, Llama3-405B FP16, 16×H100) | ~40–60 J/token | 2512.03024 (measured) |
| A4 | System multiplier (PUE + host + networking; GPU share 50–70% of datacenter) | ×1.5 | 2601.22076; 2512.03024; JPCUB P0 |
| A5 | Measured mean output tokens: text chat | 717 | 2601.22076 (B200, min-energy) |
| A6 | Measured mean output tokens: GPQA problem-solving (reasoning) | 6,988 | 2601.22076 |
| A7 | Measured energy per response: text chat (mean across models) | 184 J (GPU-only) | 2601.22076 |
| A8 | Measured energy per response: GPQA problem-solving (mean across models) | 4,625 J (GPU-only) | 2601.22076 |
| A9 | pass@1 accuracy: factoid/MCQ (MMLU-class) | 0.85–0.95 | public leaderboards |
| A10 | pass@1 accuracy: GSM8K-class math | 0.85–0.95 | public leaderboards |
| A11 | pass@1 accuracy: GPQA Diamond (frontier reasoning) | 0.55–0.75 | public leaderboards |
| A12 | Agentic coding (SWE-bench-class): total tokens per attempt | 10⁵–10⁶ | agentic traces literature; scaling pathology 2603.15183 (assumption — no direct energy trace published) |
| A13 | Agentic coding: verified solve rate (pass@1 attempt) | 0.30–0.60 | public leaderboards |
| A14 | Human brain power (resting, brain-only) | ~20 W | Kety & Schmidt 1948; Raichle & Mintun 2006; Herculano-Houzel 2009 |
| A15 | Human expert task times | QA 20–30 s; GSM8K 45–90 s; GPQA 5–15 min; SWE-bench 2–6 h | expert-task-time convention |

## 2. Task-Stratified J/S Table (order-of-magnitude)

System-level J/S = (GPU-only × A4) ÷ accuracy, per Definitions 3.1/5.3 of METRIC-FORMALIZATION.md.

| Task class | LLM J/S (system, J) | Human J/S (20 W, J) | Ratio LLM/human | Verdict |
|:-----------|:---------------------|:--------------------|:----------------|:--------|
| Simple verifiable QA (factoid/MCQ) | ~35–70 | 400–600 | ~0.06–0.17 | LLM ~6–17× more efficient |
| Math word problems (GSM8K-class) | ~150–300 | 900–1,800 | ~0.08–0.33 | LLM ~3–12× more efficient |
| Graduate reasoning (GPQA-class, single pass) | ~7,000–12,000 | 6,000–18,000 | ~0.4–2.0 | **Parity** |
| GPQA + self-consistency (n = 8) | ~55,000–95,000 | 6,000–18,000 | ~3–16× | **LLM worse** |
| Agentic coding (SWE-bench-class) | ~10⁵–5×10⁶ | 1.4×10⁵–4.3×10⁵ | ~0.2–12× | **Parity to worse** |

Worked anchor for the GPQA row (the load-bearing estimate):
- GPU-only response energy (measured mean) = 4,625 J (A8) → system ≈ 6,900 J (A4) → J/S = 6,900 ÷ 0.6 (A11 mid) ≈ **11,500 J**.
- Human expert: 20 W × 10 min = **12,000 J** (A14, A15).
- Both are ~10⁴ J: the two substrates are within a factor of ~2 on graduate reasoning.

## 3. The Three Multipliers (why J/token misleads)

1. **Accuracy correction** (÷ p): 0.6 accuracy ⇒ 1.67× per-query energy per solution; 0.3 ⇒ 3.3×.
2. **Reasoning-token explosion** (× output tokens × J/token): measured 25× energy-per-response spread between chat and problem-solving (A7/A8) — token count and per-token cost *multiply* because long sequences cap batch size (2601.22076).
3. **Agentic orchestration** (× total tokens across graph): 10⁵–10⁶ tokens per SWE-bench attempt (A12) ⇒ 10⁵–10⁶ J before the accuracy correction.

## 4. Training-Amortization Asymmetry (symmetric reporting)

| System | Training/development energy | Amortization base | Amortized per solution |
|:-------|:---------------------------|:------------------|:-----------------------|
| GPT-3 (frontier, 2020) | ~4.6×10¹² J (1,287 MWh) | 10⁹–10¹¹ lifetime queries | 46 – 4.6×10³ J/query |
| GPT-4-class (frontier, 2023) | ~1.8–3.6×10¹⁴ J (50–100 GWh) | 10⁹–10¹¹ lifetime queries | 1.8×10³ – 3.6×10⁵ J/query |
| Human brain (development/education) | ~1.3×10¹⁰ J (20 W × 20 yr, brain-only) | ~10⁵ lifetime professional solutions | ~1.3×10⁵ J/solution |

**Finding.** At high query volume (10¹¹), frontier-model training amortizes to ~10³ J/query — comparable to per-query inference. At 10⁹ queries, amortized training (up to 3.6×10⁵ J/query) *dominates* inference. The human "training" amortization (~10⁵ J/solution) sits in the same band as agentic LLM J/S. Any comparison that charges one side's amortization without the other's is biased by up to three orders of magnitude.

## 5. Reasoning-Budget Pareto Frontier (qualitative, from token-budget literature)

- Accuracy rises **sub-linearly** with token budget; budgets cut 60–80% with nominal accuracy loss are repeatedly demonstrated (CROP: 80.6% token reduction; 2604.14214; token-budget-aware reasoning 2412.18547; BudgetThinker 2508.17196; BG-MCTS 2602.09574; conformal stopping 2602.03814).
- Consequence: $J/S(b)$ is **U-shaped** in the budget $b$ — the efficient frontier selects the knee, and "spend more thinking tokens" eventually *increases* J/S per correct solution.
- Falsification hook P6-F2: if accuracy were linear or super-linear in $b$ past the knee, the U-shape claim fails.

## 6. Disconfirmation Status (pre-registered, unmeasured as of 2026-08-15)

These are estimates from published measurement data, not new measurements. The falsification conditions of PROJECT-PLAN.md §1.2 (P6-F) are the acceptance test for the *measurement protocol* (paper §9). If an independent measurement under the full J/S boundary finds frontier/agentic J/S < 0.1× the human baseline on ≥2 of 3 hard task classes, P6 is falsified and the paper publishes that result.

## 7. Robustness of the Shape (what the estimates actually claim)

Even if every input moves ±3× in the worst direction simultaneously (GPU-only understatement, accuracy optimism, token-count optimism), the *ordering* of the rows does not change: **LLM advantage is largest on cheap single-shot tasks and shrinks monotonically as tasks demand more tokens, more samples, or more orchestration — crossing parity inside the hard-reasoning and agentic bands.** That monotonic crossover, not any single number, is the load-bearing claim of P6.
