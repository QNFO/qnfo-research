# Structured Configuration-Style Prompts as Variance Control: An Analytical Framework for Cross-LLM Output Variance Reduction

## Abstract

Large language models (LLMs) are increasingly used as interchangeable components in automated pipelines, yet the same natural-language instruction produces materially different outputs across models, sampling seeds, and runs. This variance blocks the use of LLMs where reproducible execution matters: batch document processing, schema-constrained data extraction, and multi-step agentic workflows. The specific gap is that prompt engineering is practiced as a literary craft with no predictive model of how prompt form controls output variance, and the largest existing variance decomposition of LLM creative output attributes 36.43% of originality variance to prompts but does not separate prompt form from prompt content. We develop an analytical framework that treats a prompt as a partial program whose unspecified parameters are filled in by each model's interpretation, models interpretation divergence as an input to the output-variance machinery of sensitivity analysis, and derives a variance-reduction factor equal to the share of interpretation variance carried by the parameters a structured prompt pins down. Under explicitly labeled illustrative assumptions, pinning four of six interpretation dimensions removes 82% of the prompt-attributable interpretation variance; a 20-field schema at the per-constraint reliability threshold 0.986 yields 75.4% full-compliance probability against 12.2% for an assumed prose baseline of 0.90 per field, a 3.57-fold reduction in violation probability. The framework converts prompt engineering into a specification discipline with measurable design targets and a falsifiable pilot protocol.

## 1. Introduction

Teams that wire LLMs into production pipelines face a reproducibility problem that has no accepted engineering answer. When the same extraction, transformation, or drafting instruction is given to two different models — or to the same model twice — the outputs differ in structure, in content, and sometimes in whether the task is performed at all. Downstream code that parses one model's output fails on another's; a workflow validated against one model breaks silently when a provider is swapped or a model is updated. The cost is concrete: every integration must either build model-specific parsing, accept silent failures, or pay for human review of every output. What is missing is a design lever that makes LLM behavior predictable across models, in the way a written specification makes behavior predictable across implementations of an API.

The dominant practice for controlling LLM behavior is prompt engineering: careful wording of natural-language instructions. This practice implicitly assumes that a prompt acts as a near-deterministic program — find the right phrasing and the model will execute it. Large-scale evidence now quantifies how far that assumption is from reality. A variance decomposition across 12 LLMs, 10 creativity prompts, and 100 samples per cell (N = 12,000) found that prompts explain 36.43% of variance in originality while model choice explains 40.94–51.25% and within-LLM sampling variance 10.56–33.70% [8]. The authors of that study conclude that prompting is "less about programming a machine and more about steering a probabilistic distribution" [8]. If prompts are weak, bounded levers even at their best, the practical question becomes: which property of a prompt makes its lever stronger, and can that property be engineered deliberately rather than discovered by trial?

This paper develops the conjecture that prompt *form* — not content — is that property. Prose-style instructions leave the interpretation of the task to the model: what counts as a section, what order to process items in, what to do on an edge case. Different models resolve these ambiguities differently, and the same model resolves them differently across seeds. Configuration-style prompts — explicit schemas, IF/THEN protocols, state machines, enumerated field lists — remove those degrees of freedom by construction. The claim is testable, and this paper does two things about it: it builds the formal machinery needed to state the claim precisely and predict its magnitude, and it specifies the experiment that would confirm or refute it. The machinery borrows from sensitivity analysis, where the influence of uncertain inputs on output variance is measured by Sobol indices and estimated efficiently from structured approximations [1], [5], and from work showing that the distribution of inputs, not just the map, controls output variance [2].

The contributions are:

- A formal model of a prompt as a partial program with an interpretation map per model, yielding a three-way variance decomposition (prompt-interpretation, model, sampling) aligned with the empirical decomposition of [8]; derived in Section 3 and Section 4.
- A variance-reduction theorem for structured prompts: the reduction factor equals the fraction of interpretation variance carried by the free parameters that the structured form eliminates, expressed through total sensitivity indices in the manner of [1], [5]; derived in Section 4.
- Worked numerical predictions under explicitly labeled illustrative assumptions: an 82% reduction of the prompt-attributable interpretation variance when four of six interpretation dimensions are pinned, a schema-compliance calculation giving 75.4% versus 12.2% full-compliance probability at 20 fields, and a Bayes-factor amplification for cross-model verification protocols from 8 to 16 under a halved null-convergence probability; derived in Section 4 and reported in Section 5.
- A falsifiable pilot protocol — paired prose/structured prompt corpora, fixed temperature, multiple models, structural and semantic agreement metrics — with the specific outcome that would refute the central claim; specified in Section 7.

The framework also bears on adjacent problems: cross-model agreement is used as Bayesian evidence for claim correctness in verification pipelines [14], and any method that raises inter-model agreement raises the evidential weight of such panels; the same variance-control logic applies to any setting where a stochastic generator must satisfy a conjunction of many independent constraints, including the long-form drafting reliability thresholds analyzed in [12]. The result could matter wherever multi-model LLM panels, schema-constrained generation, or reproducible agentic execution are used.

## 2. Background and Related Work

The closest empirical anchor for this paper is the variance decomposition of LLM creative output by [8]. That study evaluated 12 LLMs on 10 creativity prompts with 100 samples each, for N = 12,000 outputs, partitioning variance into model, prompt, and within-LLM sources. Its headline numbers are that prompts explain 36.43% of variance in originality, comparable to model choice at 40.94%, while for fluency model choice dominates at 51.25% and within-LLM variance reaches 33.70% [8]. Its discussion states the premise this paper attacks directly: the field has operated on the premise that prompts act as close-to-deterministic programs, and the decomposition challenges that view [8]. What [8] does not do is separate the *form* of a prompt from its *content* — all its prompts are prose variations — so its 36.43% conflates task framing with interpretive ambiguity. Our framework supplies that separation and predicts that the interpretation component, which structured forms eliminate, is the controllable part.

The machinery for predicting how input uncertainty becomes output variance comes from sensitivity analysis. [1] develops sparse polynomial chaos expansion (SN-PCE) for processes represented as directed acyclic graphs, constructs orthonormal polynomials and Sobol indices from the Hoeffding decomposition, and shows both theoretically and on two manufacturing processes and a flooding process that the sparse approximation identifies influential inputs with substantially fewer observations than Monte Carlo or naive PCE [1]. We reuse its central object — the Sobol index, the fraction of output variance attributable to an input — as the measure of how much output variance each unpinned interpretation parameter carries. [5] applies the same index family to feature selection: its total sensitivity index $S_{T_i}$ incorporates interactions between features, which most filter methods ignore, and on the Friedman dataset with known relevant features the TSI was highest for the relevant features, including under high noise when computed with neural-network models [5]. This matters for our framework because interpretation parameters interact: a model's choice of output format and its choice of section ordering are not independent levers, and a decomposition that ignores interaction would mis-rank which parameters a structured prompt must pin.

A second strand shows that the *distribution* of inputs, independent of the map, controls output variance. [2] studies parameterized quantum circuits and proves that for angle-encoded product states the input distribution's overlap with the circuit's dynamical Lie algebra — its algebraic purity — determines output variance: for the matchgate family every pure product input retains enough overlap to give output variance $\Theta(1/n)$, while for the off-diagonal family computational-basis inputs give exactly zero output for every parameter choice [2]. The structural lesson transfers: changing the distribution over interpretations (which a structured prompt does by shrinking the support) changes output variance even when the model is fixed. [4] provides the complementary network-side result, deriving the exact marginal output variance for $\mathcal{L}$-Lipschitz layers initialized with IID Gaussian weights via the Wishart distribution, and finding empirically that a scaling of $1/\sqrt{n}$ is less effective at controlling per-layer output variance than $10/\sqrt{n}$ [4]. Both works treat variance as a designed quantity — set by the input distribution or the parameterization — which is exactly the stance this paper takes toward prompt form. [9] reaches a similar design conclusion inside LLMs themselves: its LayerNorm Scaling rescales output variance inversely with layer depth so that deeper layers contribute meaningfully, showing that variance placement is an architectural lever with measurable performance consequences [9].

On the measurement side, [3] investigates the sequential sampling method for reducing the variance of a simulation output performance measure in crossdocking systems, targeting a desired 95% confidence interval half-width with a minimum number of replications [3]. The methodological point — that output variance determines how many runs any conclusion needs — governs the pilot protocol we specify in Section 7: the more structured prompts compress variance, the fewer paired runs are needed to establish the effect. [6] analyzes optimal experimental design for Bayesian regression and shows that popular entropy-based criteria have weak, sometimes uncontrollable dependence on the output values of existing samples, so directions of parameter space that contribute most to the output may not be emphasized; it proposes an output-weighted criterion that accelerates convergence [6]. We use its caution in Section 7: the pilot's prompt pairs should be selected to emphasize the interpretation dimensions that carry variance, not sampled uniformly from prompt space. [10] demonstrates the end-to-end pattern with Earth system models: machine-learning emulators make it practical to run global sensitivity analysis and connect forward uncertainty propagation to inverse parameter calibration, with parameter sensitivities depending on the output quantity, averaging window, and regime [10]. This is the template for our proposal to fit an emulator over (prompt form, model, seed) configurations and read off which prompt-form features carry variance. [11] contributes the statistical end of the pipeline: minimum-variance linear approximants for noisy data whose weighting minimizes output variance, equivalent to generalized least squares, with experiments showing the approximant exploits low-noise data regions and noise correlation to drive a performance ratio toward zero as noise vanishes [11]. When pilot measurements of output variance arrive with heteroscedastic noise across models, such weighting is the correct estimator.

Two QNFO analyses supply the reliability and verification arithmetic this paper builds on. [12] models multi-chapter LLM drafting as a conjunction of per-chapter and per-constraint adherence events and derives a per-chapter reliability threshold $p^{*} \approx 0.958$ for a 50% chance of a clean run, a per-constraint threshold $q^{*} \approx 0.986$, a realistic phase-success probability $P_{\text{phase}} \approx 0.185$ at $p = 0.9$, and — directly relevant here — that automated checking lowers the per-constraint generation threshold to 0.979 [12]. Its minimal next experiment defines the falsification pattern we adopt: if the pilot yields a completion rate below 70% or per-chapter adherence below 0.958 despite refined prompts, the hypothesis that prompting alone can raise adherence sufficiently is falsified [12]. [14] formalizes cross-model LLM convergence as Bayesian evidence for claim correctness: under its illustrative assumptions, two-model convergence on multi-step synthesis questions yields a Bayes factor of 8 and a posterior of $8/17 \approx 0.471$ from a 0.1 prior, four models yield $\approx 0.983$, and the two-model posterior spans $\approx 0.182$ to $\approx 0.690$ as the null's convergence probability varies from 0.20 to 0.02, with the framework's value hinging on that single measurable quantity [14]. Structured prompts enter this framework as a mechanism for lowering the null's convergence probability — if constrained output spaces make coincidental agreement less likely while genuine agreement survives, the Bayes factor rises; Section 4 derives the scaling. [13], finally, demonstrates the methodological move this paper makes at small scale: its ultrametric consilience atlas maps one mathematical structure across 12 domains and argues that tool transferability follows from the invariance of the mathematical core [13]. We transfer variance-decomposition tools from process engineering and quantum-machine-learning contexts into prompt engineering on the same logic that a shared mathematical structure licenses the transfer [13].

## 3. Methods

### 3.1 The model

We model an LLM $m$ as a conditional distribution $p_{\theta_m}(y \mid x)$ over outputs $y$ given a prompt $x$, following the probabilistic framing of [8]. A prompt is not a function from intent to output; it is an *underspecified program*: a partial specification $P$ with a set $F(P) = \{f_1, \ldots, f_k\}$ of free interpretation parameters — choices the prompt does not determine, such as output ordering, section granularity, edge-case handling, or format details. Each model $m$ resolves these parameters through an interpretation map

$$g_m : P \mapsto \boldsymbol{\theta}_m = (\theta_{m,1}, \ldots, \theta_{m,k}) \in \Theta,$$

and the observed output is a draw $y \sim p_{\theta_m}(y \mid P)$. Sampling stochasticity is the conditional variance $\operatorname{Var}(y \mid \boldsymbol{\theta}_m)$; interpretation divergence is the spread of $\boldsymbol{\theta}_m$ across models and seeds.

### 3.2 Variance decomposition

Following the three-source partition of [8], we decompose the total output variance over the joint ensemble of models, prompts, and samples as

$$\operatorname{Var}[y] = \underbrace{\operatorname{Var}_{m}\!\left[\mathbb{E}(y \mid \boldsymbol{\theta}_m)\right]}_{\text{interpretation}} + \underbrace{\mathbb{E}_{m}\!\left[\operatorname{Var}(y \mid \boldsymbol{\theta}_m)\right]}_{\text{sampling}} + \operatorname{Var}_{\text{prompt content}},$$

where the first two terms are the law-of-total-variance split of the model-attributable variance and the third is the variance due to differing prompt content across the corpus. The empirical decomposition of [8] measures the sum of these components without separating interpretation from content; our framework predicts that structured forms act only on the first term.

### 3.3 Structured prompts as support restriction

A configuration-style prompt $P_{\text{struct}}$ is one whose free-parameter set is smaller: $F(P_{\text{struct}}) \subset F(P_{\text{prose}})$, with the residual parameters either pinned to fixed values or constrained to a discrete schema (an enumerated field list, an IF/THEN protocol, a state machine). Formally, the structured prompt restricts the support of the interpretation distribution: where the prose prompt induces a distribution $g_m(P) \sim \pi$ over a product space $\Theta_1 \times \cdots \times \Theta_k$, the structured prompt induces a distribution concentrated on a submanifold where $k - k'$ coordinates are fixed. This is the same mechanism by which input-distribution restriction controls output variance in [2]: shrinking the input support toward states of high overlap with the intended behavior shrinks the output variance, without changing the map itself.

### 3.4 Sensitivity weighting of free parameters

Not all free parameters contribute equally to output variance. Following [1] and [5], we assign each free parameter $f_i$ a total sensitivity index $S_{T_i}$, the fraction of output variance attributable to $f_i$ including its interactions, with $\sum_i S_{T_i} \leq 1$ (equality when interactions are fully attributed). The prompt-attributable interpretation variance is then

$$V_{\text{int}} = \operatorname{Var}[y] \cdot \sum_{i=1}^{k} S_{T_i},$$

and a structured prompt that pins the parameters in a set $\bar{F}$ leaves

$$V_{\text{int}}' = \operatorname{Var}[y] \cdot \sum_{f_i \in F \setminus \bar{F}} S_{T_i}.$$

The variance-reduction factor on the interpretation component is $R = V_{\text{int}}' / V_{\text{int}}$. This is the paper's central object: it converts "structured prompts reduce variance" into a computable quantity, estimable by the sparse-PCE machinery of [1] once pilot data exist.

### 3.5 Compliance as a conjunction of constraints

For schema-constrained outputs, success is a conjunction: all $n$ fields must be present and well-formed. If per-field compliance is $q$, independent across fields, the full-compliance probability is $q^n$ — the same conjunction structure that [12] uses to derive its per-chapter and per-constraint thresholds. Structured prompts raise $q$ (the schema states each field explicitly) and, through automated checking of the schema, lower the threshold $q$ must meet, the effect quantified at 0.986 → 0.979 in [12].

### 3.6 What this paper does and does not do

This paper performs no experiment, measurement, or simulation on any model. Every numerical value in Section 4 is either (i) taken from a cited work and attributed to it, or (ii) computed here from explicitly labeled illustrative assumptions, in the same discipline used by [14], whose results section states that all its numbers are computed from explicitly labeled illustrative assumptions with no empirical measurements reported. The pilot study that would supply real estimates of the $S_{T_i}$ is specified as a proposal in Section 7, not executed here.

## 4. Analysis

### 4.1 Consistency check of the empirical decomposition

The decomposition of [8] reports, for originality, prompt variance of 36.43%, model choice of 40.94%, and within-LLM variance in the range 10.56–33.70%. Summing the lower ends:

$$36.43\% + 40.94\% + 10.56\% = 87.93\%,$$

and the upper ends give $36.43\% + 51.25\% + 33.70\% = 121.38\%$. The components are therefore not strictly additive over the reported ranges — the model and within-LLM figures are ranges across metrics or conditions, and shares overlap or are normalized differently across outcome measures. We take from this only the order-of-magnitude facts that the paper states: prompt form (as prose) is a first-order source of variance, comparable to model identity, and within-LLM sampling variance is never negligible (at least 10.56%). Any variance-reduction mechanism that acts only on the prompt component can, at the extreme of the reported decomposition, address at most $36.43 / 87.93 \approx 0.414$ of the total lower-bound variance — a bound we carry into Section 5.

### 4.2 Variance-reduction factor under illustrative sensitivity weights

We assume, as an illustrative configuration to be replaced by pilot estimates, that a prose task prompt leaves $k = 6$ interpretation dimensions with total sensitivity indices

$$S_{T_1} = 0.30,\quad S_{T_2} = 0.25,\quad S_{T_3} = 0.15,\quad S_{T_4} = 0.12,\quad S_{T_5} = 0.10,\quad S_{T_6} = 0.08,$$

which sum to $0.30 + 0.25 + 0.15 + 0.12 + 0.10 + 0.08 = 1.00$, i.e., the interpretation component accounts for the full prompt-attributable variance in this toy configuration. A structured prompt in the style of a configuration file pins the four largest contributors — output schema ($f_1$), processing order ($f_2$), section granularity ($f_3$), and edge-case protocol ($f_4$) — leaving $f_5, f_6$ free. The residual interpretation variance share is

$$R = \frac{S_{T_5} + S_{T_6}}{\sum_i S_{T_i}} = \frac{0.10 + 0.08}{1.00} = 0.18,$$

so the structured form removes $1 - R = 0.82$, i.e., 82%, of the prompt-attributable interpretation variance. Because the pinned set was chosen by descending $S_{T_i}$ — the ranking logic of the total sensitivity index in [5], which correctly identified relevant features including under noise — this is the optimal pinning of four parameters under these weights. If instead the structured prompt pinned the four *smallest* contributors, the residual would be $(0.30 + 0.25)/1.00 = 0.55$, only a 45% reduction: the framework predicts that *which* degrees of freedom a structured form eliminates matters more than how many, a directly testable corollary.

### 4.3 Bound from the empirical decomposition

Combining Section 4.1 with Section 4.2: the interpretation component is at most the prompt share of total variance. At the lower-bound decomposition of [8], the prompt component is $36.43\%$ of $87.93\%$ total, so the maximum total-variance reduction achievable by perfect elimination of interpretation divergence is

$$0.3643 \times 0.82 = 0.2987,$$

i.e., roughly 30 percentage points of total variance under the illustrative weights, with the remainder of total variance (model identity and sampling stochasticity) untouched by prompt form. This bound is the honest statement of the conjecture's reach: structured prompts are a lever on one component, not a cure for LLM stochasticity.

### 4.4 Schema-compliance arithmetic

Take the per-constraint reliability threshold $q^{*} \approx 0.986$ derived in [12] as the per-field compliance probability a well-engineered pipeline must meet, and assume — as an illustrative baseline, not a measurement — that a prose prompt achieves $q = 0.90$ per field while a structured schema prompt achieves the threshold value $q = 0.986$. For a 20-field extraction schema (we assume $n = 20$ as a representative structured-output size), the full-compliance probabilities are:

$$P_{\text{prose}} = 0.90^{20} = e^{20 \ln 0.90} = e^{20 \times (-0.105361)} = e^{-2.10721} = 0.12157 \approx 12.2\%,$$

$$P_{\text{struct}} = 0.986^{20} = e^{20 \ln 0.986} = e^{20 \times (-0.0140982)} = e^{-0.281964} = 0.75429 \approx 75.4\%.$$

The violation probabilities are $1 - 0.12157 = 0.87843$ and $1 - 0.75429 = 0.24571$, a ratio

$$\frac{0.87843}{0.24571} = 3.5746 \approx 3.57,$$

so under these assumptions the structured form reduces the per-document violation probability by a factor of 3.57. The independence assumption across fields is optimistic — field errors are plausibly correlated within a document — and Section 6 treats it as a limitation; the direction of the effect survives moderate correlation because both sides are affected.

The automated-checking result of [12] compounds this: automated checking lowers the required per-constraint generation threshold from 0.986 to 0.979, and at $q = 0.986$ with checking the margin above threshold widens from $0.986 - 0.986 = 0$ to $0.986 - 0.979 = 0.007$ per constraint, which is what makes the 75.4% figure operationally meaningful rather than marginal.

### 4.5 Amplification of cross-model verification evidence

In the framework of [14], two-model convergence on a multi-step synthesis question carries a Bayes factor $K_S = 8$ under its illustrative assumptions, giving a posterior $P_2 = 8/17 \approx 0.4706$ from a 0.1 prior. The Bayes factor is the ratio of the convergence probability under the correctness hypothesis to the convergence probability under the null (shared bias or coincidence). A structured prompt that constrains the output space plausibly affects both, but affects the null more if coincidental agreement becomes easier to distinguish from protocol-following — under a structured protocol, the null must reproduce the *entire constrained output*, not merely agree on a verdict. We assume, as an illustrative mechanism, that the structured form halves the null's convergence probability while leaving the correctness-side convergence unchanged. Then

$$K_S' = K_S \times \frac{p_{\text{null}}}{p_{\text{null}}/2} = 8 \times 2 = 16,$$

and the two-model posterior becomes

$$P_2' = \frac{K_S' \cdot o_0}{1 + K_S' \cdot o_0} = \frac{16 \times 0.111}{1 + 16 \times 0.111} = \frac{1.7781}{2.7781} = 0.6400,$$

where $o_0 = 0.1/0.9 = 0.1111$ is the prior odds. Equivalently $P_2' = 16/33 = 0.4848$ when the Bayes factor is applied as $K/(K+1)$ against the [14] convention — we take the [14] convention, under which the posterior is $K_S'/(K_S' + 9) \cdot$ ... we state it directly: with prior odds $o_0 = 1/9$, posterior odds $= K_S' \cdot o_0 = 16/9$, and posterior $= (16/9)/(16/9 + 1) = 16/25 = 0.6400$. The halving assumption is the load-bearing one; the sensitivity of the [14] framework to the null's convergence probability is already established there, with the two-model posterior spanning $\approx 0.182$ to $\approx 0.690$ as $p^{S}_b$ moves from 0.20 to 0.02 [14], so our illustrative halving sits inside a range the framework itself treats as the decisive measurable quantity.

### 4.6 Pilot sample size

The pilot of Section 7 measures the log variance ratio $\Delta = \ln(V_{\text{prose}} / V_{\text{struct}})$ across paired prompt tasks. We assume a per-task standard deviation $\sigma_\Delta = 0.5$ in log units (an assumption standing in for data no source gives) and require the standard error of the mean over $n_p$ paired tasks to be at most 10% of $\ln 2 \approx 0.6931$, i.e., $\mathrm{SE} \leq 0.0693$. Then

$$n_p \geq \left(\frac{\sigma_\Delta}{0.0693}\right)^{2} = \left(\frac{0.5}{0.0693}\right)^{2} = (7.214)^{2} = 52.05,$$

so $n_p = 53$ paired tasks give the required precision. This is the sequential-sampling logic of [3] — fix the desired confidence-interval half-width, then determine the minimum replications — applied to the log variance ratio instead of a simulation output measure.

## 5. Results

All numbers below are computed in Section 4 from explicitly labeled illustrative assumptions or attributed to cited works; no empirical measurements are reported by this paper.

1. **Decomposition bound.** At the lower-bound decomposition of [8] (prompt 36.43%, model 40.94%, within-LLM 10.56%, summing to 87.93%), prompt form can address at most $36.43/87.93 \approx 41.4\%$ of total output variance (Section 4.1).

2. **Interpretance-variance reduction.** Under the illustrative six-dimension sensitivity configuration of Section 4.2, a structured prompt pinning the four highest-$S_{T_i}$ parameters reduces the prompt-attributable interpretation variance by 82% ($R = 0.18$); pinning the four lowest-$S_{T_i}$ parameters instead yields only a 45% reduction ($R = 0.55$). The ranking of pinned parameters, not their count, controls the reduction (Section 4.2).

3. **Total-variance reduction bound.** Multiplying the 82% interpretation reduction by the 41.4% prompt share gives a maximum total-variance reduction of $\approx 29.9$ percentage points under these assumptions (Section 4.3).

4. **Schema compliance.** At $n = 20$ fields, assumed per-field compliance $q = 0.90$ (prose) versus the threshold $q^{*} = 0.986$ from [12] (structured), full-compliance probability rises from 12.2% to 75.4%, and the violation probability falls by a factor of 3.57 (Section 4.4). Automated checking lowers the required per-constraint threshold to 0.979 [12], converting the structured result from marginal to operational.

5. **Verification-evidence amplification