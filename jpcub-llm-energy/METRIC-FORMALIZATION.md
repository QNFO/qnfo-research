# Metric Formalization: Joules-per-Solution for Stochastic and Agentic Inference

**Project:** QNFO.JPC.002 — jpcub-llm-energy (JPCUB Paper P3)
**Phase:** 2 (Metric Formalization)
**Date:** 2026-08-15
**Status:** Draft — Phase 2

---

## 1. Purpose

JPCUB P0 defined the joules-per-solution metric for deterministic solvers: $J_{\mathrm{CUB}} = P_{\mathrm{sys}} \cdot t_{\mathrm{sol}}$ — total system power times time to one verified solution, with six energy components (computation, memory, I/O, cooling, power conversion, amortized manufacturing). P0's implicit model: one run of the solver yields a solution with known, bounded failure probability.

AI/LLM systems violate that model in two ways, and this document supplies the formal extensions:

1. **Stochasticity** — an LLM is a sampler over outputs. "One run" is not "one solution"; the metric must be an *expectation* over the model's output distribution, corrected by the probability of a correct answer under a *stated sampling regime*.
2. **Orchestration** — an agentic system is a graph of sub-queries, tool calls, retrievals, and retries. "One solution" spans many inferences and growing context; the metric must attribute energy across the entire graph.

The human-brain baseline is formalized in Section 6 with a pre-registered attribution rule.

## 2. Notation

| Symbol | Meaning |
|:-------|:--------|
| $\tau$ | a task with verifier $V_{\tau}$ and correctness threshold $\theta$ (e.g., exact match, unit-test pass, ground-truth match) |
| $q$ | a single inference query (prompt + model + decoding config) |
| $y \sim p_{\theta}(y \mid x)$ | the model's stochastic output |
| $E_{q}$ | full-system energy of one query (six-component JPCUB boundary) |
| $p_{q}(\tau)$ | pass@1: probability a single query's output passes $V_{\tau}$ |
| $n$ | number of i.i.d. samples (self-consistency / best-of-$n$ / majority vote) |
| $b$ | reasoning-token budget (test-time compute) for reasoning models |
| $G$ | orchestration graph of an agentic task; $V_G$ = set of sub-queries |

## 3. The Stochastic Correction (closed form)

**Definition 3.1 (J/S, single query).**

$$J/S_{\tau} \;=\; \frac{E_{q}}{p_{q}(\tau)}$$

the expected energy per *correct* solution when queries are repeated until success.

**Definition 3.2 (J/S, sampling regime of $n$ independent queries with single-answer acceptance).**

$$J/S_{\tau}(n) \;=\; \frac{n\,E_{q}}{\,1 - (1 - p_{q}(\tau))^{n}\,}$$

**Proposition 3.3 (U-shape).** For fixed $E_{q}$ and $0 < p_{q} < 1$, the function $J/S(n)$ is (i) flat at $J/S \to E_{q}/p_{q}$ as $n \to 0^{+}$ (since $1-(1-p)^{n} \approx np$), (ii) minimized at a finite $n^{*}$, and (iii) grows linearly as $n \to \infty$ (since the acceptance probability saturates at 1). The efficient operating point $n^{*}$ satisfies $n^{*} \approx \ln(1/p_{q})$ for small $p_{q}$ and is the *metric's* answer to "how much sampling is worth it".

*Interpretation.* The naive "joules per query" understates cost for inaccurate models; the naive "cost of $n$ samples" overstates it because $n$ samples buy accuracy. J/S(n) is the honest middle: the minimum of the U-curve is the defensible efficiency claim, and reporting J/S without a stated $n$ and $p_{q}$ is incomplete (anti-gaming provision A1 below).

**Definition 3.4 (majority-vote / self-consistency).** If the verifier accepts the majority answer over $n$ samples and each sample is correct with probability $p$, then $P_{\mathrm{correct}}(n) = P\!\left(\mathrm{Bin}(n,p) > n/2\right)$, and $J/S_{\tau}(n) = n E_{q} / P_{\mathrm{correct}}(n)$. Regime-specific; computable in closed form for given $n, p$.

## 4. Reasoning-Budget Dependence (test-time compute)

For reasoning models, the query energy is a *decision variable*: $E_{q} = E_{q}(b)$, where $b$ is the thinking-token budget, and accuracy $p_{q}(b)$ rises sub-linearly in $b$ (diminishing returns; cf. token-budget literature: 2412.18547, 2508.17196, 2602.09574, 2602.03814, 2507.02076).

**Definition 4.1 (Pareto frontier).** The benchmark report MUST include the frontier $\{(J/S_{\tau}(b),\; p_{q}(b)) : b \in \mathcal{B}\}$ for a pre-registered budget set $\mathcal{B}$ — never a single point. This is P0's Pareto-frontier mandate applied to the reasoning budget.

**Remark 4.2.** Quantization and other per-token optimizations can shift $b$ itself (token inflation; 2606.25519): a cheaper token is not necessarily a cheaper solution if it lengthens reasoning. J/S captures this automatically; J/token does not.

## 5. Agentic Orchestration Accounting

**Definition 5.1 (orchestration graph).** An agentic task executes a graph $G = (V_G, E_G)$: nodes are LLM sub-queries and tool executions; edges are control/data flow. Each sub-query $v$ has input length $L_{\mathrm{in}}(v)$ and output length $L_{\mathrm{out}}(v)$; context grows along the path (previous tool outputs are re-read).

**Definition 5.2 (total energy per attempt).**

$$E_{\mathrm{attempt}} \;=\; \sum_{v \in V_G} E_{v} \;+\; E_{\mathrm{tools}} \;+\; E_{\mathrm{overhead}}$$

with $E_v$ including the growing-context prefill cost, and $E_{\mathrm{overhead}}$ covering retries, idle, and orchestration (scheduling, verification).

**Definition 5.3 (J/S, agentic).** Let $p_{G}$ be the probability that a completed attempt's artifact passes the task verifier. Then

$$J/S_{\tau_{A}} \;=\; \frac{E_{\mathrm{attempt}}}{p_{G}}$$

expected energy per *verified* task completion, including the energy of failed attempts.

**Remark 5.4 (multi-agent pathology).** Naive broadcast synchronization costs scale as $O(n \cdot S \cdot |D|)$ in agents, steps, and artifact size (2603.15183). J/S must be measured on the *whole system*, so orchestration pathologies are charged to the solution — this is the agentic analogue of P0's "no free cooling" rule.

## 6. Human-Brain Baseline (pre-registered attribution rule)

**Baseline fact.** Resting human brain power $P_{\mathrm{brain}} \approx 20\,\mathrm{W}$ (~86 billion neurons; ~20% of ~100 W basal metabolism; Kety & Schmidt 1948; Raichle & Mintun 2006; Herculano-Houzel 2009).

**Definition 6.1 (human J/S).**

$$J/S_{\mathrm{human}} \;=\; P_{\mathrm{brain}} \cdot t_{\mathrm{sol}}$$

where $t_{\mathrm{sol}}$ is time to a *correct* solution by a task-appropriate expert (verifier identical to the LLM's).

**Attribution rule (pre-registered, symmetric):**
- **Primary:** brain-only, $P = 20\,\mathrm{W}$ (neutral, standard, conservative against the LLM's favor).
- **Sensitivity bounds:** task-marginal cognitive power (~3–5 W) and full-body basal (~100 W) reported as bounds.
- **Amortization:** human "training" (development/education) energy is reported *separately* and *symmetrically* with LLM training amortization (Section 8 of ESTIMATES.md). Never charge one side's amortized cost against the other's marginal cost.

## 7. System Boundary (JPCUB six-component mandate)

All LLM estimates are reported as (a) GPU-only (as published) and (b) system-level = GPU-only $\times$ 1.5 (PUE + host CPU/DRAM + networking + cooling overhead; the 1.5 factor is the JPCUB lower-bound multiplier given GPU share 50–70% of datacenter power; 2601.22076, 2512.03024). Embodied (manufacturing) energy is flagged as an open addendum, not silently included.

## 8. Anti-Gaming Provisions (extending P0)

- **A1 — Sampling transparency:** every J/S number MUST state $(n, p_{q}, \text{temperature})$; no J/S without them.
- **A2 — Pareto mandate:** reasoning-budget and sampling frontiers reported, not single points.
- **A3 — Verifier pre-registration:** task canon restricted to verifiable tasks; verifier and threshold fixed before measurement.
- **A4 — Adversarial validation:** an independent party re-derives the estimates from the same published data; numbers are audit-trailed to source rows.
- **A5 — Component audit:** GPU-only vs system-level breakdown published per estimate.
- **A6 — Living benchmark protocol:** the frontier is re-measured as models/hardware change; J/S claims carry an "as of" date.
