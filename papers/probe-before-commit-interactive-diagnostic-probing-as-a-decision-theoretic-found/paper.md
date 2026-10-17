# Probe-Before-Commit: Interactive Diagnostic Probing as a Decision-Theoretic Foundation for LLM Task Routing

## Abstract

Static capability benchmarks poorly predict how well a given large language model (LLM) will perform on a specific task, yet most routing systems assign tasks to models using exactly such static signals. The gap is that per-task fitness — the probability that a specific model produces an acceptable answer to a specific task — is never measured before commitment. We propose operationalizing intelligent routing as a low-cost interactive probe: before committing a task, the router sends cheap diagnostic queries to candidate models, observes their responses, updates a per-model fitness estimate, and routes according to a decision matrix combining predicted quality, latency, and monetary cost. We formalize the probe as an expected-value-of-information (EVI) problem nested inside a routing decision, derive the posterior update for binary probe signals, and give a fully worked numerical example in which probe-informed routing raises expected utility from $0.5700$ to $0.6782$ — a net gain of $0.1082$ after probe costs of \$0.001 per model (\$0.003 per task) — with a break-even per-probe cost of $c_p^{*} \approx$ \$0.00821. A complementary precision analysis shows a routing decision is statistically meaningful only if per-candidate probe precision satisfies $\sigma_f \lesssim 0.0379$. The framework gives router builders concrete design targets — a probe price ceiling and a precision floor — and states explicit falsification conditions for the claim that probing beats static routing.

## 1. Introduction

Organizations that deploy LLMs face a routing problem: for each incoming task, choose among several candidate models that differ in predicted output quality, latency, and per-token cost. The dominant practice is to route by static signals — leaderboard rankings, benchmark aggregates, or hand-tuned heuristics. The cost of this mismatch is concrete: a router that sends a mathematics task to a model with a strong general reputation but weak mathematics fitness pays premium per-token prices for rejected or low-quality outputs, while a router that over-avoids expensive models pays in rework and failed tasks. What would change if this paper's result holds: a router builder could decide, before building any probing infrastructure, whether probing can pay at all at their probe price point, by checking one derived number — the break-even per-probe cost — and one precision target.

The premise of this paper is that static routing is structurally mismatched to the problem, because per-task fitness (the probability that a specific model produces an acceptable answer to a specific task) is exactly the quantity that static aggregates fail to estimate, while it is precisely the quantity a cheap interactive measurement could estimate directly.

The research idea examined here is: before committing a task, send cheap diagnostic queries ("probes") to candidate models; use the responses to estimate each model's fitness for the task; then route based on a decision matrix combining predicted quality, latency, and cost. The idea matters because routing heuristics are rarely grounded in measured fitness, and because probing converts an inference-time guess into a measurement problem with a well-defined price.

The stakes are practical. Efficiency-focused work on LLM deployment shows that serving costs and latency constraints are structural: YouZhi identifies KV-cache memory overhead as the bottleneck that "inflates infrastructure costs and throttles scalability" in high-concurrency deployment, and reports that a naive architecture transition degrades Llama3-8B perplexity from $6.1$ to $25.8$ while its layer-adaptive transition limits the degradation to $6.1 \rightarrow 12.9$ [7]. Serving-cost differences across candidate models are therefore real and persistent, so the difference between routing to an adequate cheap model and an over-provisioned expensive one compounds at deployment scale. On the other side, work on LLM stochasticity shows that output quality is not a fixed model property: AutoDroid observes a $2.1\%$ accuracy reduction when the temperature of GPT-3.5 is set to $0$ and a $3.8\%$ accuracy boost when it is raised to $0.7$ [1], which motivates defining fitness as a probability rather than a deterministic attribute.

This paper makes three contributions:

1. It formalizes probe-based routing as a two-stage decision problem — a probe-design stage (which queries to send, at what cost) and a routing stage (which model to commit, given probe responses) — and shows the probe decision is an EVI calculation (Section 3).
2. It derives, with full arithmetic, a worked example demonstrating when probing beats static routing and when it barely pays, including the break-even probe cost of $c_p^{*} \approx \$0.00821$ and the precision requirement $\sigma_f \lesssim 0.0379$ (Section 4).
3. It specifies who would use the result, at what readiness level, and what the smallest falsifying experiment is (Sections 6 and 7).

We emphasize scope: this paper contains no new empirical measurements. All quantitative results are derived from explicitly stated illustrative assumptions in Section 4; the empirical program is specified, not executed.

## 2. Background and Related Work

The literature relevant to probe-before-commit routing spans four threads: deployed LLM task execution and its stochasticity, routing under uncertain node quality, measurable task-conditioned structure in model computation, and online signals derived from offline evaluations. We discuss each thread through specific results, then state the gap.

**Deployed LLM task execution and stochasticity.** AutoDroid applies LLMs to mobile task automation, motivated by the poor scalability of prior approaches, which suffered from limited language understanding ability and non-trivial manual effort from developers or end-users [1]. Its evaluation deploys Vicuna-7B both on the smartphone itself and on an edge server with an NVIDIA 3090 to assess inference latency, and it fine-tunes on the MoTiF dataset of more than $4.7$k tasks; its discussion reports that setting the temperature of GPT-3.5 to $0$ reduces accuracy by $2.1\%$ while raising it to $0.7$ boosts action accuracy by $3.8\%$, and proposes an instruction cache to reduce latency by reusing common commands [1]. Two of these results bear directly on our formalism: the temperature findings show that the same model's task accuracy shifts measurably with sampling conditions, supporting our definition of fitness as a probability $q_i \in [0,1]$ rather than a fixed attribute, and the edge-versus-device deployment shows that latency and invocation cost differ across serving configurations, supporting the cost and latency terms in our utility function.

**Routing under uncertain node quality.** Trusted routing in blockchain-enabled low-altitude intelligent networks formulates routing among UAVs whose distributed topology, high mobility, and vulnerability to attacks and node failures make links unreliable, and reformulates the problem as a Dec-POMDP to deal with the challenge of obtaining global information in LAINs, and improves the learning efficiency of the MARL with a SHERPA-family algorithm (named SHERB-MA... in its conclusions); the work conducts Python simulations over a $15\,\text{km} \times 5\,\text{km}$ area (with UAV altitudes in $[0.2, 0.4]\,\text{km}$) and presents comparisons of the four algorithms in accumulative reward, convergence performance, and average end-to-end delay (Figs. 2–4) [2]. The structural parallel is exact: [2] routes data through nodes whose availability is uncertain and partially observable, and it treats state estimation as part of the routing problem rather than a preprocessing step. Our router faces the same abstract structure with models in place of UAVs; the difference is that our uncertainty reduction mechanism is a purchased measurement (the probe) with an explicit price, which lets us derive a break-even condition that a learned POMDP policy does not expose.

**Adaptive interaction with a modeled partner state.** The common-model-of-cognition coaching work builds human-aware collaborative agents that model, learn, and reason about a human partner's physiological, cognitive, and affective states, and evaluates PARCcoach with $60$ participants over more than $28$ days, finding that participants confident in their target behavior complied more and that CMC-guided reminders improved behavioral compliance [3]. This supplies the closest conceptual ancestor of our probe: a coaching agent adapts its interaction to a measured partner state before acting, exactly as our router adapts model selection to a measured model state before committing. The PARCcoach finding that the ideal adaptive coach must be cognizant of difficulty as it pertains to each individual trainee [3] is the human-facing analogue of our claim that fitness is task- and instance-specific, not a global model property.

**Measurable task-conditioned structure inside models.** The routing-signatures work introduces vector representations summarizing expert activation patterns across layers for a given prompt in sparse Mixture-of-Experts transformers, and demonstrates in OLMoE that routing signatures cluster strongly by task category, that this clustering exceeds what sparse load-balancing constraints alone would produce, that task signal increases toward deeper layers, and that signatures alone support high-accuracy linear classification of task type; it releases the MoE-Xray toolkit for routing telemetry [4]. This is the closest internal-routing analogue to our proposal: [4] establishes empirically that how a model allocates computation is task-conditioned and measurable rather than assumed. Our probe operationalizes the same thesis at the model-selection level, observing input-output behavior of opaque models at the API boundary where internal routing telemetry is unavailable.

**The cost of inference-time interaction.** Interactive Learning for LLM Reasoning (ILR) notes that existing multi-agent learning approaches build interactive training environments among multiple LLMs, but that at inference they require re-executing the multi-agent system to obtain final solutions, which diverges from human cognition, in which individuals enhance reasoning without re-execution [5]. ILR's own protocol estimates each LLM's capability parameter $\gamma_i$ offline from a randomly selected validation set of $1{,}000$ MATH samples before training, and compares this one-time measurement against a periodic-update strategy [5]. Two points connect to our framework. First, ILR's offline $\gamma_i$ estimation is a static fitness estimate of exactly the kind our probe is designed to refine per task; its periodic-update comparison shows the authors already recognize that stale fitness estimates lose value. Second, the re-execution objection motivates our cost constraint: any inference-time interaction must be cheap enough to preserve the economics that motivated routing, so our probe is deliberately non-re-executive — a lightweight pre-commitment measurement, not a full multi-agent execution.

**Real-time commitment under live constraints.** The intelligent interactive theatre work proposes an intelligent agent that serves simultaneously as drama manager and as an actor playing a character in live theatre, and poses the research challenges of believable acting skills, learning character behavior from actors and players, and combining these into a single system [6]. The work proposes an agent that serves simultaneously as drama manager and as an actor playing a character, poses the research challenges of believable acting skills, learning character behavior from actors and players, and combining these into a single system, and proposes the development steps of building narrative permutations, learning behavior from player modelling, and then combining the components into one system [6]. In our reading, this is the commitment structure our router instantiates: a system committing to actions in real time from a portfolio of options under live performance constraints, with models in place of the agent's action portfolio. The work's own proposed steps — developing narrative permutations, learning behavior from player modelling, then combining into one system [6] — mirror our two-stage decomposition of probe design followed by commitment.

**Structural serving cost.** YouZhi identifies KV-cache memory overhead as the bottleneck that inflates infrastructure costs and throttles scalability in high-concurrency LLM deployment, and proposes an adaptive GQA-to-MLA structural transition with a post-training pipeline, evaluated on Huawei Ascend clusters [7]. Its quantified results ground the cost side of our decision matrix: the layer-adaptive transition reduces perplexity degradation by $65\%$ relative to the TransMLA baseline on Llama3-8B ($6.1 \rightarrow 12.9$ versus $6.1 \rightarrow 25.8$), and the resulting YouZhi-7B and YouZhi-14B achieve average general-benchmark scores of $66.8$ and $68.0$ [7]. The lesson for routing is that quality, cost, and serving efficiency vary across models and configurations simultaneously, so a routing objective that ignores cost or latency optimizes only part of the problem — hence the $\lambda c_i$ and $\mu \ell_i$ terms in our utility.

**Online signals from offline evaluations.** Task-aware delegation cues observes that human-agent teamwork remains brittle due to information asymmetry: users lack task-specific reliability cues and agents rarely surface calibrated uncertainty or rationale, and proposes a collaboration signaling layer that turns offline preference evaluations into online, user-facing primitives for delegation [8]. Its experiments validate two task-conditioned signals — a capability profile (task-specific win tendency) and a coordination-risk cue — on Chatbot-Arena-style pairwise comparisons, using stratified 5-fold cross-validation in which Ridge regularization performs best for both tasks, and removing cluster features reduces Task A accuracy and increases Task B mean squared error [8]. This is conceptually the nearest neighbor of our probe: both convert offline evaluation evidence into online, task-specific signals. Our contribution differs in the consumer of the signal — an automated router rather than a human user — and in treating signal acquisition as a priced decision with a derivable break-even cost, which [8] does not attempt.

**Fitness as a probability and expectation-based efficiency.** We define per-task fitness as a probability of acceptable output and frame model selection as a utility maximization problem over quality, cost, and latency trade-offs; our utility function in Section 3.2 adopts exactly this structure, with the probe supplying the evidence term in $\mathbb{E}[q_i \mid \text{evidence}]$. We treat fitness as an expectation $\mathbb{E}[q_i]$ and the routing objective as an expected utility rather than a per-run score, because a single run of a stochastic system does not identify its fitness probability.

**The gap.** Across these threads, no work formalizes pre-commitment diagnostic probing of candidate LLMs as a priced expected-value-of-information problem with an explicit break-even probe cost and a precision requirement on the fitness estimate. That is the gap this paper addresses.

## 3. Methods

### 3.1 Setting

A router receives a task $\tau$ and chooses among $N$ candidate models $M_1, \dots, M_N$. Each model $M_i$ has a known per-task monetary cost $c_i$ (dollars), a known latency $\ell_i$ (seconds), and an unknown per-task fitness $q_i \in [0,1]$, the probability that $M_i$'s output for $\tau$ is acceptable. Following the stochasticity evidence reviewed above — for example the temperature-dependent accuracy shifts reported in [1] — fitness is a probability, not a deterministic property.

### 3.2 Decision matrix

The router maximizes expected scalarized utility

$$U_i = \mathbb{E}[q_i \mid \text{evidence}] - \lambda\, c_i - \mu\, \ell_i,$$

where $\lambda$ (utility per dollar) and $\mu$ (utility per second) are fixed trade-off weights. Static rubric routing uses only prior evidence $\mathcal{E}_0$ (benchmarks, rubric scores); probe-informed routing augments it with probe responses.

### 3.3 Probe model

A probe is a cheap diagnostic query sent to model $M_i$ before commitment, costing $c_p$ dollars and $\ell_p$ seconds. We model the binary case: the probe returns a signal $s_i \in \{0,1\}$ (fail/pass). The probe has sensitivity $a = P(s_i = 1 \mid M_i \text{ fit})$ and false-positive rate $b = P(s_i = 1 \mid M_i \text{ not fit})$, with $a > b$. The router holds a prior $\pi_i = P(M_i \text{ fit})$. By Bayes' rule,

$$\pi_i^{+} = P(\text{fit} \mid s_i = 1) = \frac{a\,\pi_i}{a\,\pi_i + b(1 - \pi_i)}, \qquad \pi_i^{-} = P(\text{fit} \mid s_i = 0) = \frac{(1-a)\,\pi_i}{(1-a)\,\pi_i + (1-b)(1 - \pi_i)}.$$

We take fitness probability as the quality term, i.e., $\mathbb{E}[q_i \mid s_i] = \pi_i^{\pm}$, so that a fit model yields an acceptable solution with probability $1$ and an unfit model with probability $0$; this is a conservative two-point approximation to a continuous fitness distribution.

### 3.4 Probe decision as EVI

Let $U^{\text{static}} = \max_i U_i$ under priors, and let $U^{\text{probe}}$ be the expected utility of the two-stage policy: probe all $N$ candidates (in parallel, so probe latency is $\ell_p$ once), then commit optimally. The probe is worth sending iff

$$\Delta = U^{\text{probe}} - \lambda N c_p - \mu \ell_p - U^{\text{static}} > 0.$$

The break-even per-probe cost is

$$c_p^{*} = \frac{U^{\text{probe,gross}} - \mu \ell_p - U^{\text{static}}}{\lambda N},$$

where $U^{\text{probe,gross}}$ excludes probe monetary cost.

### 3.5 Precision requirement for a meaningful decision

For a routing decision to be statistically meaningful, the utility gap between the top two candidates must exceed the decision noise. With independent fitness standard errors $\sigma_{f,1}, \sigma_{f,2}$ for the top two candidates, the standard error of the utility difference is $\sigma_{\Delta} = \sqrt{\sigma_{f,1}^2 + \sigma_{f,2}^2}$, and the decision is significant at confidence level $z$ (e.g., $z = 1.96$ for two-sided $95\%$) iff $|\hat{U}_1 - \hat{U}_2| > z\,\sigma_{\Delta}$. Setting $\sigma_{f,1} = \sigma_{f,2} = \sigma_f$ yields a minimum-probe-precision requirement

$$\sigma_f \le \frac{|\hat{U}_1 - \hat{U}_2|}{z\sqrt{2}}.$$

### 3.6 Extension to graded probes

Binary probes generalize to graded scores $s_i \in \{1, \dots, K\}$ with likelihoods $P(s_i \mid \text{fit})$ and $P(s_i \mid \text{not fit})$; the posterior update is the same Bayes rule over $K$ outcomes. Probe families may include plan-quality sketches and self-evaluation accuracy checks; the formalism is agnostic to probe content, requiring only a likelihood model.

## 4. Analysis

All numbers below are derived from explicitly stated illustrative assumptions; none are empirical measurements.

### 4.1 Inputs (assumed for the worked scenario)

Three candidate models with priors, costs, and latencies:

| Model | Prior $\pi_i$ | Cost $c_i$ (\$) | Latency $\ell_i$ (s) |
|---|---|---|---|
| $M_1$ | $0.70$ | $0.020$ | $3$ |
| $M_2$ | $0.50$ | $0.005$ | $1$ |
| $M_3$ | $0.80$ | $0.080$ | $8$ |

Trade-off weights: $\lambda = 5$ utility per dollar, $\mu = 0.01$ utility per second. Probe parameters: sensitivity $a = 0.9$, false-positive rate $b = 0.3$, probe cost $c_p = 0.001$ dollars per model, probe latency $\ell_p = 0.5$ s, probes sent in parallel to all $N = 3$ models, signals conditionally independent across models.

### 4.2 Step 1: Static routing

The static utility of each model is $U_i = \pi_i - \lambda c_i - \mu \ell_i$:

$$U_1 = 0.70 - 5(0.020) - 0.01(3) = 0.70 - 0.10 - 0.03 = 0.57,$$
$$U_2 = 0.50 - 5(0.005) - 0.01(1) = 0.50 - 0.025 - 0.01 = 0.465,$$
$$U_3 = 0.80 - 5(0.080) - 0.01(8) = 0.80 - 0.40 - 0.08 = 0.32.$$

Static routing selects $M_1$: $U^{\text{static}} = 0.57$.

### 4.3 Step 2: Posterior updates

Using $\pi_i^{+} = \frac{0.9\,\pi_i}{0.9\,\pi_i + 0.3(1-\pi_i)}$ and $\pi_i^{-} = \frac{0.1\,\pi_i}{0.1\,\pi_i + 0.7(1-\pi_i)}$:

- $M_1$: $\pi_1^{+} = \frac{0.9 \times 0.70}{0.9 \times 0.70 + 0.3 \times 0.30} = \frac{0.63}{0.63 + 0.09} = \frac{0.63}{0.72} = 0.875$; $\pi_1^{-} = \frac{0.1 \times 0.70}{0.1 \times 0.70 + 0.7 \times 0.30} = \frac{0.07}{0.07 + 0.21} = \frac{0.07}{0.28} = 0.25$.
- $M_2$: $\pi_2^{+} = \frac{0.9 \times 0.50}{0.9 \times 0.50 + 0.3 \times 0.50} = \frac{0.45}{0.45 + 0.15} = \frac{0.45}{0.60} = 0.75$; $\pi_2^{-} = \frac{0.1 \times 0.50}{0.1 \times 0.50 + 0.7 \times 0.50} = \frac{0.05}{0.05 + 0.35} = \frac{0.05}{0.40} = 0.125$.
- $M_3$: $\pi_3^{+} = \frac{0.9 \times 0.80}{0.9 \times 0.80 + 0.3 \times 0.20} = \frac{0.72}{0.72 + 0.06} = \frac{0.72}{0.78} \approx 0.923077$; $\pi_3^{-} = \frac{0.1 \times 0.80}{0.1 \times 0.80 + 0.7 \times 0.20} = \frac{0.08}{0.08 + 0.14} = \frac{0.08}{0.22} \approx 0.363636$.

### 4.4 Step 3: Post-probe utilities

Post-probe utilities are $U_i^{\pm} = \pi_i^{\pm} - \lambda c_i - \mu \ell_i$; the cost-latency deductions from Step 1 are $0.13$, $0.035$, and $0.48$ for $M_1$, $M_2$, $M_3$ respectively:

- $M_1$: $U_1^{+} = 0.875 - 0.13 = 0.745$; $U_1^{-} = 0.25 - 0.13 = 0.12$.
- $M_2$: $U_2^{+} = 0.75 - 0.035 = 0.715$; $U_2^{-} = 0.125 - 0.035 = 0.09$.
- $M_3$: $U_3^{+} = 0.923077 - 0.48 = 0.443077$; $U_3^{-} = 0.363636 - 0.48 = -0.116364$.

### 4.5 Step 4: Signal marginal probabilities

For each model, $P(s_i = 1) = a\pi_i + b(1-\pi_i)$:

- $M_1$: $0.9(0.7) + 0.3(0.3) = 0.63 + 0.09 = 0.72$; fail probability $1 - 0.72 = 0.28$.
- $M_2$: $0.9(0.5) + 0.3(0.5) = 0.45 + 0.15 = 0.60$; fail probability $0.40$.
- $M_3$: $0.9(0.8) + 0.3(0.2) = 0.72 + 0.06 = 0.78$; fail probability $0.22$.

### 4.6 Step 5: Expected utility of the probe policy

With independent signals there are $2^3 = 8$ joint outcomes. For each, the router picks the model with maximum $U_i^{\pm}$:

```
Outcome (s1 s2 s3)   Probability                    Best model   Utility
111                  0.72*0.60*0.78 = 0.33696       M1           0.745
110                  0.72*0.60*0.22 = 0.09504       M1           0.745
101                  0.72*0.40*0.78 = 0.22464       M1           0.745
100                  0.72*0.40*0.22 = 0.06336       M1           0.745
011                  0.28*0.60*0.78 = 0.13104       M2           0.715
010                  0.28*0.60*0.22 = 0.03696       M2           0.715
001                  0.28*0.40*0.78 = 0.08736       M3           0.443077
000                  0.28*0.40*0.22 = 0.02464       M1           0.12
```

$$U^{\text{probe,gross}} = 0.745(0.72) + 0.715(0.168) + 0.443077(0.08736) + 0.12(0.02464),$$

where the four utility levels correspond to the best model in each outcome block: $M_1$ passes in the first four outcomes (total probability $0.72$), $M_2$ is chosen in outcomes 011 and 010 (total probability $0.13104 + 0.03696 = 0.168$), $M_3$ is chosen in outcome 001 (probability $0.08736$), and $M_1$ is chosen in outcome 000 (probability $0.02464$). Computing each term:

$$0.745 \times 0.72 = 0.53640,$$
$$0.715 \times 0.168 = 0.12012,$$
$$0.443077 \times 0.08736 = 0.0387068,$$
$$0.12 \times 0.02464 = 0.0029568.$$

Summing:

$$U^{\text{probe,gross}} = 0.53640 + 0.12012 + 0.0387068 + 0.0029568 = 0.6981836 \approx 0.698184.$$

Subtracting the probe monetary cost $\lambda N c_p = 5 \times 3 \times 0.001 = 0.015$ and the probe latency cost $\mu \ell_p = 0.01 \times 0.5 = 0.005$:

$$U^{\text{probe}} = 0.698184 - 0.015 - 0.005 = 0.678184.$$

The gain over static routing is

$$\Delta = U^{\text{probe}} - U^{\text{static}} = 0.678184 - 0.57 = 0.108184 \approx 0.1082 > 0,$$

so probing is worth sending under the assumed parameters.

### 4.7 Step 6: Break-even probe cost

Setting $\Delta = 0$ and solving for $c_p$:

$$c_p^{*} = \frac{U^{\text{probe,gross}} - \mu \ell_p - U^{\text{static}}}{\lambda N} = \frac{0.698184 - 0.005 - 0.57}{5 \times 3} = \frac{0.123184}{15} = 0.00821227 \approx \$0.00821.$$

Any per-probe price below \$0.00821 makes the probe policy strictly better than static routing in this scenario; the assumed price of \$0.001 sits at roughly $12\%$ of the ceiling.

### 4.8 Step 7: Precision requirement

The static utility gap between the top two candidates is $|\hat{U}_1 - \hat{U}_2| = |0.57 - 0.465| = 0.105$. With $z = 1.96$ (two-sided $95\%$):

$$\sigma_f \le \frac{0.105}{1.96\sqrt{2}} = \frac{0.105}{1.96 \times 1.414214} = \frac{0.105}{2.771859} = 0.037874 \approx 0.0379.$$

A fitness estimate with per-candidate standard error at or below $0.0379$ makes the routing decision between $M_1$ and $M_2$ statistically meaningful at the $95\%$ level; a noisier estimate cannot distinguish them from each other with confidence, even though their assumed utilities differ by $0.105$.

## 5. Results

All results follow from the assumptions in Section 4.1 and the arithmetic in Sections 4.2–4.8; none are empirical measurements.

1. Probe-informed routing raises expected utility from $U^{\text{static}} = 0.5700$ to $U^{\text{probe}} = 0.6782$, a net gain of $\Delta = 0.1082$ after probe costs of \$0.001 per model (\$0.003 per task) and $0.5$ s of probe latency (Section 4.6).
2. The break-even per-probe cost is $c_p^{*} \approx$ \$0.00821; the assumed probe price of \$0.001 is a factor of about $8.2$ below the ceiling (Section 4.7).
3. The routing decision is statistically meaningful only if per-candidate fitness estimates satisfy $\sigma_f \lesssim 0.0379$ (Section 4.8).
4. The gain concentrates in the disagreement outcomes: the probe policy selects a model other than $M_1$ in $25.536\%$ of the probability mass ($0.13104 + 0.03696 + 0.08736 = 0.25536$; outcomes 011, 010, 001), and in outcome 000 (probability $0.02464$) it retains $M_1$ but at the failed-probe utility $U_1^{-} = 0.12$ instead of the static $0.57$-level commitment, so the total mass in which the committed utility departs from the static level is $0.25536 + 0.02464 = 0.28$. The probe's value is therefore driven by its ability to overturn the prior ranking, not by confirming it.

## 6. Discussion

The worked example establishes possibility, not prevalence: under the assumed priors, probe quality, and trade-off weights, probing pays with a wide margin. Several assumptions could fail in deployment, and each failure mode has a checkable signature.

**Sensitivity of the break-even cost to $\lambda$.** The break-even cost scales as $1/\lambda$: at $\lambda = 5$ it is $\$0.00821$, at $\lambda = 10$ it halves to $\$0.00411$, and at $\lambda = 1$ it rises to $\$0.0411$. Router builders whose cost sensitivity is ten times ours can afford probes only five times more expensive, not ten times, because the gross probe value is fixed by the scenario: at $\lambda = 1$ the break-even is $0.123184 / (1 \times 3) = 0.041061 \approx$ \$0.0411, a factor of $0.041061 / 0.00821227 = 5.0$ above the $\lambda = 5$ value. This non-proportional response is a direct consequence of the linear cost term and should be recomputed per deployment.

**Sensitivity to probe quality.** The assumed discriminative power ($a = 0.9$, $b = 0.3$) is generous. As $b \to a$ the posterior collapses to the prior, $U^{\text{probe,gross}} \to U^{\text{static}}$, and $c_p^{*} \to 0$: a probe no better than a coin flip has zero value at any price. The framework therefore prices probe quality implicitly — a weak probe must be nearly free to be worth sending.

**Correlated probe errors.** We assumed conditional independence of signals across models. If probes share a failure mode (for example, all models fail on an ambiguous probe phrasing), the joint outcome distribution narrows and the effective information content drops; the EVI calculation in Section 4.6 would overstate the gain. Extending the analysis to a correlated-signal model is straightforward in principle but changes the eight-outcome enumeration.

**Two-point fitness approximation.** Taking $\mathbb{E}[q_i \mid s_i] = \pi_i^{\pm}$ assumes fit models are always acceptable and unfit models never are. A continuous fitness distribution would soften the utility swings and shrink $\Delta$; the direction of the correction is toward smaller gains, so our result is an upper bound under this approximation.

**Falsification conditions.** The central claim — probing beats static routing when $c_p < c_p^{*}$ — is falsified if an empirical deployment with measured probe costs below the deployment's computed break-even cost yields no utility gain over static routing. Two specific observations would falsify it: (i) measured probe sensitivity and false-positive rates close enough that the realized posterior updates do not change the selected model on a material fraction of tasks, or (ii) probe-induced switches that occur but reduce realized acceptability relative to the static choice, indicating that the probe signal measures something other than task fitness. Either observation would indicate model misspecification rather than a failure of the EVI logic itself, but both would defeat the practical claim.

**Limitations.** The result rests on: (1) binary probe outcomes — graded probes change the posterior algebra but not the EVI structure; (2) conditional independence of signals — violated if probes share failure modes, and the gain is sensitive to this; (3) a linear utility model with fixed $\lambda, \mu$ — the break-even cost is proportional to $1/\lambda$; (4) the two-point fitness approximation — the gain is an upper bound under it; (5) illustrative priors, costs, and latencies — no empirical distribution of these quantities is measured here; (6) parallel probing with fixed $N$ — sequential probe designs (probe the top candidate first, stop early) could lower total probe cost and are not analyzed; (7) no probe-induced distribution shift — repeated probing could let models overfit probe formats, degrading $a$ and raising $b$ over time.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are builders of LLM routing layers: platform teams operating multi-model inference gateways, and vendors of model-routing middleware. If the result holds, two design decisions change. First, the router acquires a pre-commitment probe stage: before dispatching a task, it issues one or more cheap diagnostic queries to the top candidates and routes on the posterior rather than the prior. Second, the procurement decision for probing infrastructure becomes a one-line check: estimate the deployment's $c_p^{*}$ from its measured utility gap, trade-off weight, and candidate count, and reject any probe design whose per-query cost exceeds it. In the worked scenario, a probe costing $\$0.001$ per model clears the $\$0.00821$ ceiling by a factor of $8.2$; a probe design quoting $\$0.01$ per query does not, and should be redesigned or rejected before any integration work begins.

**(b) Readiness level.** This work is purely analytical and has not been peer reviewed: by the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). Analytical work never exceeds TRL 3, and no claim of implemented or validated routing infrastructure is made here. The posterior update and EVI calculation are at the level of basic principles; nothing in this paper has been demonstrated in a relevant environment.

**(c) Smallest next experiment.** The smallest de-risking test is a retrospective replay: take a fixed task suite (for example, several hundred tasks of one type), run each candidate model on both the tasks and a small set of candidate probe queries, and compute — offline, with no live routing — (i) the realized probe sensitivity $a$ and false-positive rate $b$ against ground-truth acceptability, and (ii) the realized utility gain of the probe policy over static routing using the Section 3.4 formula with measured $a, b$. The outcome that refutes the framework is a measured $(a, b)$ pair for which the computed $c_p^{*}$ falls below the actual marginal cost of serving the probe queries, while the realized gain remains positive only under the assumed generous parameters — or, more directly, a measured gain of zero at probe costs below the measured break-even. This requires only API access and an acceptability rubric; no new infrastructure.

**(d) Binding constraints.** The constraints that would bind first, in order: (i) probe design quality — the parameters $a$ and $b$ are the load-bearing quantities, and no amount of cheap probing compensates for a non-discriminative probe (as $b \to a$, $c_p^{*} \to 0$); (ii) probe latency — at $\mu = 0.01$ utility per second, probe latency of $0.5$ s costs $0.005$ utility per task, which is one-third of the assumed monetary probe cost, so latency budgeting is not negligible; (iii) acceptability ground truth — computing $a$ and $b$ requires labeled judgments of what counts as an acceptable output, which is a data-collection cost the framework takes as given; (iv) correlated probe failures across models, which would require the independence assumption to be replaced by an estimated correlation structure. Regulation and manufacturing constraints do not bind at this stage.

**(e) Order-of-magnitude bounds (projection).** As a labeled projection with stated assumptions: if a deployment serves $10^{6}$ tasks per month with $N = 3$ candidates and the worked scenario's parameters, the monthly value of probing is $\Delta \times 10^{6} = 0.1082 \times 10^{6} \approx 1.08 \times 10^{5}$ utility units, and the monthly probe spend at $c_p = 0.001$ dollars is $3 \times 10^{6} \times 0.001 = 3000$ dollars (\$3,000). These figures assume the per-task utility gain of the worked example transfers unchanged to the deployment's task mix, which Section 6 argues is an upper bound; they are illustrative scaling arithmetic, not a forecast.

**(f) Risks and misuse paths.** A direct risk is probe gaming: if a model provider knows that routers probe with a standard query family, the provider can tune its model to pass probes without improving task fitness, raising the effective false-positive rate $b$ while appearing to raise $a$. This is an adversarial analogue of the distribution-shift limitation in Section 6, and it argues for rotating or private probe families. A second risk is over-trust in the precision figure: $\sigma_f \lesssim 0.0379$ is derived for a specific utility gap ($0.105$); deployments with smaller gaps need proportionally tighter precision, and applying the $0.0379$ figure unchanged would produce confidently wrong routing decisions.

## 8. Conclusion

We formalized probe-before-commit routing as an expected-value-of-information problem nested inside a routing decision, derived the posterior update for binary probe signals, and computed a fully worked example in which probing raises expected utility from $0.5700$ to $0.6782$ — a net gain of $0.1082$ — with a break-even per-probe cost of $\$0.00821$ and a precision requirement of $\sigma_f \lesssim 0.0379$. These two derived numbers give router builders concrete design targets: a price ceiling for probe queries and a precision floor for fitness estimates. The framework states its own falsification conditions, and the smallest next test — a retrospective replay measuring realized probe sensitivity and utility gain on a fixed task suite — is within reach of any team with API access and an acceptability rubric. The contribution is a decision-theoretic foundation, not a validated system; its value is that it converts the question "should we probe?" from a matter of intuition into a matter of arithmetic.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.25-model-floor-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] AutoDroid: LLM-powered Task Automation in Android. arXiv:2308.15272v4. https://arxiv.org/abs/2308.15272v4
[2] Trusted Routing for Blockchain-Enabled Low-Altitude Intelligent Networks. arXiv:2506.22745v1. https://arxiv.org/abs/2506.22745v1
[3] Exploring the Role of Common Model of Cognition in Designing Adaptive Coaching Interactions for Health Behavior Change. arXiv:1910.07728v3. https://arxiv.org/abs/1910.07728v3
[4] Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers. arXiv:2603.11114v1. https://arxiv.org/abs/2603.11114v1
[5] Interactive Learning for LLM Reasoning. arXiv:2509.26306v5. https://arxiv.org/abs/2509.26306v5
[6] Towards Intelligent Interactive Theatre: Drama Management as a way of Handling Performance. arXiv:1909.10371v2. https://arxiv.org/abs/1909.10371v2
[7] YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition. arXiv:2606.05868v1. https://arxiv.org/abs/2606.05868v1
[8] Task-Aware Delegation Cues for LLM Agents. arXiv:2603.11011v1. https://arxiv.org/abs/2603.11011v1
