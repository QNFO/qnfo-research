# Auditing the 25×–90× Claim: An Analytical Decomposition and Pre-Registered Study Design for LLM Force-Multiplier Protocols in Solo Theoretical Research

## Abstract

A five-phase human-orchestrator LLM protocol (define, delegate, execute-iterate, verify, synthesize) has been claimed to deliver 25×–90× throughput speedups for solo theoretical research, but the claim rests entirely on self-experiments by the protocol's creator, so no one can currently tell a funder, a lab head, or a solo researcher whether the methodology is reusable or an artifact of creator familiarity. This paper closes the gap between the claim and the evidence in two steps. First, an analytical decomposition shows what the claim must imply if true: a 25× end-to-end speedup requires at least 96% of baseline wall-clock time to be protocol-accelerable ($f_{\min} = 1 - 1/25 = 0.96$), a 90× claim requires $f_{\min} \approx 0.9889$, and any bounded substrate (wet lab, HPC queue) consuming more than 4% of baseline time caps the achievable speedup below 25×. Second, the paper specifies a pre-registered 2×2 controlled study (protocol vs. control, creator-familiar vs. first-time user) with blind expert review and four verification gates; a power calculation gives 16 participants per cell (64 total) to detect a 1.5× residual speedup at 80% power assuming a coefficient of variation of 0.4. A cost projection under stated assumptions prices a protocol-heavy task at roughly USD 2.20 in inference calls. The result converts an anecdote into a falsifiable budget structure and a runnable experiment.

## 1. Introduction

Solo theoretical researchers — doctoral students, independent investigators, single-author groups in mathematics, formal methods, and computational science — face a productivity decision with no reliable answer today. Vendor marketing and viral practitioner accounts assert that orchestrating large language models (LLMs) through structured personal protocols multiplies individual output by factors of 25 to 90. If such a protocol is real and transferable, a solo researcher's effective output could rise by more than an order of magnitude without new funding, equipment, or collaborators; grant portfolios could be re-weighted toward individual investigators; and doctoral training would need to teach protocol orchestration as a core skill. If the claim is instead an artifact of the protocol's creator measuring their own workflow — familiarity with the task domain, with the protocol, and with the specific LLM tooling — then institutions that adopt it on anecdotal evidence will waste training time and mis-set expectations, and the field will accumulate another unreproducible productivity legend.

The cost of not knowing is concrete. A researcher who budgets a semester around a 25× multiplier and realizes 1.5× loses a semester. A funder who cannot distinguish the two cases has no basis for evaluating proposals that cite such multipliers. The decision that would change if this paper's result holds — that the claim is analytically over-constrained in specific, testable ways — is the decision to run, fund, or demand the controlled replication described here rather than to accept or dismiss the anecdote on rhetorical grounds.

The specific claim under audit is a five-phase human-orchestrator LLM protocol: (1) *define* the problem precisely enough to delegate; (2) *delegate* subproblems to LLM instances; (3) *execute-iterate* on returned fragments; (4) *verify* through four sequential gates; (5) *synthesize* the verified fragments into a finished artifact. Its asserted 25×–90× throughput speedup for solo theoretical research is supported only by self-experiments conducted by the protocol's creator. No independent party has measured the protocol under controlled conditions, and no published analysis states what a speedup of that magnitude would even require to be physically coherent.

This paper does not run the controlled study; it derives the constraints the claim must satisfy and specifies the study that would settle it. The contributions are:

- A closed-form decomposition (an Amdahl-style bound adapted to human-LLM protocols) showing that a 25×–90× end-to-end speedup implies a protocol-accelerable wall-clock fraction of at least 0.96–0.9889, and that per-fragment LLM acceleration must reach 25×–49× under stated coverage assumptions; derived in Section 4.1–4.2 and reported in Section 5 (R1–R2).
- A bounded-substrate corollary: any wet-lab, HPC-queue, or instrument-time fraction $f_b$ of baseline wall-clock caps the speedup at $1/f_b$, so the protocol's applicability boundary is computable before any trial; derived in Section 4.3 (R3).
- A familiarity-confound model separating protocol gain from creator-familiarity gain, showing that a creator-familiarity factor of 3× would reduce the transferable protocol gain from 25× to about 8.3×; derived in Section 4.4 (R4).
- A pre-registered 2×2 study design with a power calculation of 16 participants per cell (64 total) at 80% power to detect a 1.5× residual speedup at a coefficient of variation of 0.4; derived in Section 4.5 (R5).
- A verification-gate analysis and an inference-cost projection (USD 2.20 per protocol-heavy task under stated assumptions); derived in Section 4.6–4.7 (R6–R7).

## 2. Background and Related Work

The claim under audit sits at the intersection of three literatures: LLM-assisted knowledge work, protocol design for human-LLM and multi-agent interaction, and the methodology of speedup claims themselves.

On LLM-assisted knowledge work, [1] presents a proof-of-concept framework using large language models for unstructured insurance claims data, motivated by the observation that manual processing of documents such as medical records, adjuster notes, and call transcripts is time-consuming, inconsistent across reviewers, and unscalable, while actuaries rely primarily on structured numerical data. That framing — LLMs as a delegation target for well-scoped document-level subtasks — is exactly the shape of the *delegate* and *execute-iterate* phases of the protocol under audit, and [1]'s emphasis on inconsistency across human reviewers is the same reviewer-variance problem the blind expert review arm of the proposed study must control. On the systems side, [2] develops YouZhi-LLM, a financial LLM whose high-concurrency deployment is bottlenecked by KV cache memory overhead that inflates infrastructure costs and throttles scalability; its experiments on Ascend clusters measure perplexity and concurrency, with the layer-adaptive GQA-to-MLA transition reducing perplexity degradation on Llama3-8B from 6.1→25.8 under the TransMLA baseline to 6.1→12.9, a 65% reduction in degradation. The relevance to the protocol audit is economic: a protocol that delegates many parallel LLM calls per task multiplies concurrency demand, so the per-call cost and concurrency ceiling of the serving stack — the quantities [2] optimizes — bound how many delegations a solo researcher can afford per unit time. [9] supplies the current price and capability landscape: in its August 2026 audit, DeepSeek V4 Pro 0813 is the mathematics price-performance optimum at 95.1 on the LiveBench-grounded mathematics axis at USD 0.044 per benchmark run, within 1.1 points of the top score of 96.2, while open-weights models lead the agentic axis (Claude 5 Opus Thinking 65.2, Qwen 3.8 Max and Smaug-Agentic 64.6). [9] also separates the "mathematics workhorse" from the "agentic orchestrator," a distinction the protocol's phase structure maps onto directly: define/verify/synthesize calls demand reasoning quality, while delegate/execute calls demand orchestration reliability, and the 33-fold cost spread within the frontier-mathematics class makes phase-aware model routing economically material. [9]'s finding that no Llama model ranks in the top 42 of the LiveBench 2026-06-25 leaderboard further constrains which models a replication study should provision.

On protocol design for human-LLM interaction, [6] formalizes multi-turn human-LLM data-analysis interaction through a two-way intelligibility protocol (PXP), in which agents modeled as finite-state machines exchange tagged messages and send a RATIFY tag when they agree on both prediction and explanation; its experimental evaluation reports that the proportion of one-way and two-way intelligible sessions for the human agent increases as interaction length increases, and that machine performance on test data increases with interaction length. This is the closest formal precedent for the protocol's *verify* phase: intelligibility-as-ratification is a checkable gate semantics, and [6]'s observation that some high intelligibility rates are "due simply to the vast store of prior data and information within an LLM" is a caution that gate-passing may reflect model prior agreement rather than genuine verification — a confound the proposed study's error-injection arm is designed to expose. [11] formalizes a failure mode of agent protocols that bears on the *delegate* phase: protocols typically assume a tool is either available or not, but real deployments exhibit a third state in which capability exists yet is contextually disabled by policy, budget, or routing; a binary-state protocol governing $k$ permission-gated tools is specification-complete on only a $(2/3)^{k}$ fraction of the true state space (e.g., $32/243 \approx 0.132$ at $k=5$), and the compliance-halting problem is undecidable, so well-definedness must be built in syntactically. A protocol that instructs a solo researcher to "delegate to available LLM instances" inherits exactly this mismatch whenever rate limits or budget exhaustion silently disable a delegated call. [3] offers a transport-layer analogy with a general lesson: the TURN protocol's adaptation to SIP is motivated by the weakness of an application-layer protocol vis-à-vis NAT traversal, caused by how the server replies to client requests and by dynamic UDP port allocation; the lesson — that a protocol designed in one layer or context develops unexamined dependencies that fail in another — applies to a personal productivity protocol tuned by its creator on their own tooling and then handed to a stranger's environment. [4] contributes the merge-side problem: in optimistically replicated collaborative systems, replicas diverge and a merge mechanism must preserve consistency and structure, which the CAP theorem shows cannot be bought together with availability and partition tolerance; [4]'s layered approach decouples eventual consistency from data-integrity assurance through composable layers, validated in a public, re-playable benchmark framework. A protocol whose *execute-iterate* phase runs many LLM fragments in parallel and whose *synthesize* phase merges them faces the same divergence-and-merge problem, and [4]'s design principle — integrity enforcement as an explicit layer, not an afterthought — is the argument for making the four verification gates a formally specified layer rather than prose.

On the methodology of speedup claims, [7] is the exemplar the replication study imitates: it demonstrates an algorithmic quantum speedup for a variant of Simon's problem on 127-qubit IBM processors, and — crucially — reports the boundary of the effect, finding that for $n > 29$ results were no better than random guess, so the "quantum range" $n \in [2,29]$ is stated explicitly rather than buried. A credible speedup claim comes with its applicability range; the 25×–90× claim under audit states no range, no baseline, and no boundary, and [7] shows what stating them looks like. [10] is the closest methodological precedent for this paper's approach: it analytically triages a workload-level reuse speedup claim (2.95×–32.84×) with a closed-form amortized-cost model, showing the reported speedups are consistent with shared-prefix cost fractions of roughly 0.66–0.98 at 100-task scale, that the top end requires materialization overhead below about 3.05% of a fresh run, and that the claims are "plausible but single-sourced"; its conclusion that independent replication with reported parameters is the necessary next step is the template this paper applies to the LLM protocol claim. [5] supplies the evidential-governance frame: it develops Publication Authority as an exact-state, single-use publication capability for making AI-assisted claims independently challengeable, and its evaluation strategy explicitly separates evidence layers with "non-combinable claim ceilings" — a specification artifact layer, a reference-path layer, and a precursor layer, none of which is a field trial or user study. Applied here: the protocol creator's self-experiments are a precursor-layer evidence class that cannot be upgraded by narrative into a user-study claim, and the pre-registered controlled study of Section 3 is precisely the layer jump that [5]'s framework demands. [8] supplies the reporting discipline this paper adopts: every derived number is traced to stated assumptions, projections are labeled as projections, and the discussion names the weakest model link — its own linear error-accumulation model — rather than presenting budget figures as predictions.

## 3. Methods

The paper proceeds in three methods stages: a formal decomposition of the speedup claim, a study design, and an economic model.

**3.1 Claim decomposition.** Let a baseline task (the same well-scoped theoretical research task — derivation, data analysis, or drafting — performed without the protocol) consume wall-clock time $T_0$. Let $f \in [0,1]$ be the fraction of $T_0$ spent on activities the protocol can accelerate (problem framing that the *define* phase compresses, fragment production that *delegate* and *execute-iterate* parallelize, error hunting that *verify* mechanizes, assembly that *synthesize* automates). Let $a \geq 1$ be the mean per-fragment acceleration factor on that fraction. The end-to-end speedup is then

$$S = \frac{T_0}{(1-f)\,T_0 + \frac{f\,T_0}{a}} = \frac{1}{(1-f) + \frac{f}{a}}.$$

This is Amdahl's law with the protocol playing the role of the parallelizing mechanism; the same structure appears in the amortized-cost model of [10], where a speedup $S$ is inverted to recover the cost fractions a claim implicitly asserts. Two quantities are unknown ($f$, $a$) and one is claimed ($S \in [25, 90]$); Section 4 derives the feasible region.

**3.2 Study design.** The proposed replication is a pre-registered 2×2 factorial controlled study. Factor A: protocol (five-phase protocol vs. control workflow, where control is the participant's usual ad hoc LLM-or-no workflow). Factor B: familiarity (first-time protocol users vs. the protocol creator or trained proxies). Participants are matched researchers with comparable domain expertise; each solves an identical set of well-scoped problems in three task classes (symbolic derivation, data analysis, manuscript drafting). Outcome measures: (i) wall-clock time to a self-declared done state; (ii) output quality via blind expert review on a rubric with anchored scale points, reviewers blinded to arm and blinded to whether LLMs were used; (iii) error rate, operationalized as defects caught by the four verification gates plus defects caught post hoc by an independent audit pass. Pre-registration fixes the task set, the rubric, the analysis plan (log-linear mixed model on time with arm, familiarity, task class, and their interaction), and the primary hypothesis before recruitment.

**3.3 Economic model.** Protocol cost is modeled as $C_{\text{task}} = N_{\text{calls}} \cdot c_{\text{call}}$, where $N_{\text{calls}}$ is the number of LLM invocations per task and $c_{\text{call}}$ the per-call price of the deployed model. Inputs are taken from [9] where stated and declared as assumptions where not.

**3.4 Evidence-class discipline.** Following the layer-separation argument of [5], the paper keeps three evidence classes distinct: the creator's self-experiments (precursor class), this paper's analytical derivations (artificial/artifact class), and the proposed controlled study (the only class that can support a user-facing speedup claim). No number from one class is presented as if it belonged to another; all derived numbers in Section 4 trace to stated inputs, in the reporting style of [8].

## 4. Analysis

Every input number below is either stated in the claim under audit, taken from a cited source as noted, or declared as an assumption of this analysis. All arithmetic is shown.

**4.1 Minimum accelerable fraction (Derivation 1).** From $S = \left((1-f) + f/a\right)^{-1}$ with $a \to \infty$ (the most generous case: accelerated work costs nothing), the speedup is maximized at $S_{\max} = 1/(1-f)$. Inverting, any claimed $S$ requires

$$f \geq f_{\min} = 1 - \frac{1}{S}.$$

For the claimed lower bound $S = 25$:

$$f_{\min} = 1 - \frac{1}{25} = 1 - 0.04 = 0.96.$$

For the claimed upper bound $S = 90$:

$$f_{\min} = 1 - \frac{1}{90} = 1 - 0.011111\ldots = 0.988889\ldots \approx 0.9889.$$

So even with infinitely fast LLM fragments, at least 96.0% of baseline wall-clock time must be protocol-accelerable for the 25× claim to be reachable, and 98.89% for the 90× claim. Any residual 4% of unaccelerable work — reading the final manuscript, waiting on a collaborator's reply, thinking in the shower — already caps the speedup at 25×.

**4.2 Per-fragment acceleration requirement (Derivation 2).** With finite $a$, fix $f$ and solve $S = \left((1-f) + f/a\right)^{-1}$ for $a$:

$$(1-f) + \frac{f}{a} = \frac{1}{S} \quad\Longrightarrow\quad \frac{f}{a} = \frac{1}{S} - (1-f) \quad\Longrightarrow\quad a = \frac{f}{\frac{1}{S} - (1-f)}.$$

The denominator must be positive, giving the feasibility condition $f > 1 - 1/S$ (consistent with Derivation 1). Assume the protocol covers $f = 0.98$ of baseline time (itself a generous assumption — see Derivation 1) and target $S = 25$:

$$a = \frac{0.98}{\frac{1}{25} - 0.02} = \frac{0.98}{0.04 - 0.02} = \frac{0.98}{0.02} = 49.$$

At full coverage $f = 1$, the formula degenerates to $a = S$, i.e., the per-fragment acceleration must itself equal the claimed end-to-end speedup: $a \geq 25$ for the low end of the claim. For the 90× end at $f = 0.98$:

$$a = \frac{0.98}{\frac{1}{90} - 0.02} = \frac{0.98}{0.011111\ldots - 0.02}.$$

The denominator is negative ($0.011111 < 0.02$), so $S = 90$ is infeasible at $f = 0.98$ regardless of $a$; it requires $f > 1 - 1/90 = 0.9889$ (Derivation 1). The claim therefore implies a combination of near-total task coverage and per-fragment LLM acceleration of 25×–49× over an unaided expert — numbers that are themselves extraordinary and independently testable, since per-fragment acceleration can be measured directly by timing single delegated subtasks with and without LLM assistance.

**4.3 Bounded-substrate corollary (Derivation 3).** Let $f_b$ be the fraction of $T_0$ consumed by substrates the protocol cannot touch: wet-lab execution, HPC queue time, instrument time, ethics approvals. These enter the denominator unaccelerated, so

$$S \leq \frac{1}{f_b}.$$

For the claimed $S = 25$ to be reachable at any $a$:

$$f_b \leq \frac{1}{25} = 0.04.$$

For $S = 90$: $f_b \leq 1/90 \approx 0.0111$. The protocol's applicability boundary is therefore computable per task class before any trial: a derivation task with (assumed) $f_b = 0.01$ admits $S \leq 100$ in principle; a computational-science task whose HPC runs consume (assumed) $f_b = 0.30$ of wall-clock is capped at $S \leq 1/0.30 = 3.33$ no matter how good the protocol is. This is the formal version of the intuition that wet-lab and HPC-bound work "does not parallelize" — and it makes the protocol's silent scope restriction (purely symbolic, compute-light work) explicit.

**4.4 Familiarity confound (Derivation 4).** Model the observed creator speedup as the product of a transferable protocol gain $S_p$ and a creator-familiarity gain $S_{\text{fam}}$ (familiarity with the protocol's own conventions, with the task domain, and with the specific tooling):

$$S_{\text{obs}} = S_p \cdot S_{\text{fam}}.$$

This log-additive decomposition is identifiable in the 2×2 design: the arm×familiarity interaction isolates $S_{\text{fam}}$. To see what magnitudes matter, assume (as a stated scenario, not a measurement) $S_{\text{fam}} = 3$, i.e., the creator is three times faster at using their own protocol than a trained first-time user would be. Then the transferable gain implied by the low end of the claim is

$$S_p = \frac{S_{\text{obs}}}{S_{\text{fam}}} = \frac{25}{3} = 8.3\overline{3} \approx 8.33.$$

At the high end: $S_p = 90/3 = 30$. The scenario shows the stakes of the confound: a 3× familiarity advantage converts an "order-of-magnitude-plus" methodology into a solid-but-ordinary 8× tool — or, if the true $S_{\text{fam}}$ is 25, into $S_p = 1$, i.e., no transferable gain at all. The study design must therefore power on the *residual* speedup $S_p$, not the headline $S_{\text{obs}}$.

**4.5 Sample size and power (Derivation 5).** The primary analysis is a two-sided test on log-transformed task time comparing protocol vs. control arms among first-time users. Assume (stated assumptions) task-time coefficient of variation $\mathrm{CV} = 0.4$ within arm, significance $\alpha = 0.05$ two-sided, power $1 - \beta = 0.80$, and a minimum detectable residual speedup $S_{\min} = 1.5$. For log-normal times the per-arm sample size is approximately

$$n = \frac{2\,(z_{1-\alpha/2} + z_{1-\beta})^2\,\mathrm{CV}^2}{(\ln S_{\min})^2}.$$

Inputs: $z_{0.975} = 1.960$, $z_{0.80} = 0.8416$, so $z_{1-\alpha/2} + z_{1-\beta} = 1.960 + 0.8416 = 2.8016$; $(2.8016)^2 = 7.8490$ (since $2.8016^2 = 7.84896$). $\mathrm{CV}^2 = 0.16$. $\ln 1.5 = 0.405465$; $(0.405465)^2 = 0.164402$. Then

$$n = \frac{2 \times 7.8490 \times 0.16}{0.164402} = \frac{2.51168}{0.164402} = 15.278.$$

Rounding up: $n = 16$ participants per cell. The 2×2 factorial has four cells, so the full design requires $4 \times 16 = 64$ participants. If the study is powered instead on the more ambitious $S_{\min} = 2.0$: $\ln 2 = 0.693147$, $(0.693147)^2 = 0.480453$,

$$n = \frac{2.51168}{0.480453} = 5.227 \implies 6 \text{ per cell, } 24 \text{ total}.$$

The steep dependence of $n$ on $S_{\min}$ ($64$ vs. $24$) means the pre-registered primary hypothesis must be chosen before recruitment; we designate $S_{\min} = 1.5$ as primary because a protocol that cannot beat a control workflow by even 1.5× among trained first-time users has no practical claim on anyone's semester.

**4.6 Verification-gate analysis (Derivation 6).** The protocol's *verify* phase comprises four sequential gates. Model each gate as an independent filter that catches a defective fragment with probability $1 - \varepsilon_g$, leaving escape probability $\varepsilon_g$ per gate. Assume (stated assumption) a per-gate escape probability $\varepsilon_g = 0.1$ — i.e., each gate catches 90% of defects reaching it. A defect that survives all four gates has probability

$$P_{\text{escape}} = \varepsilon_g^4 = 0.1^4 = 0.0001 = 10^{-4}.$$

If a protocol-heavy task produces (assumed) $N_{\text{frag}} = 40$ fragments each with (assumed) pre-gate defect probability $p_d = 0.2$, the expected number of defects entering the gates is $40 \times 0.2 = 8$, and the expected number escaping is

$$8 \times 10^{-4} = 0.008,$$

i.e., roughly one escaped defect per 125 tasks ($1/0.008 = 125$). Two caveats are structural, not numerical. First, gate independence is an assumption; if gates share failure modes (all four are ultimately the same LLM's judgment, per the intelligibility caution in [6] that gate agreement may reflect the model's prior rather than independent scrutiny), the escape probability rises toward $\varepsilon_g = 0.1$ per defect — three orders of magnitude worse. Second, the gates catch only defect classes they test; the study's independent post hoc audit pass measures the residual directly, which is why audit-caught defects are a primary outcome and not a sanity check.

**4.7 Inference-cost projection (Derivation 7).** From [9], DeepSeek V4 Pro 0813 costs USD 0.044 per benchmark run and is the mathematics price-performance optimum at score 95.1. Assume (stated assumptions) a protocol-heavy task issues $N_{\text{calls}} = 50$ LLM calls of comparable length to a benchmark run, routed to the mathematics workhorse for define/verify/synthesize calls and to a cheaper orchestrator tier for delegate/execute calls. Under the conservative assumption that all 50 calls run at the workhorse price