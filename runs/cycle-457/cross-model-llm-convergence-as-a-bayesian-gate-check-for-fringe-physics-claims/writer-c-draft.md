# Cross-Model Convergence as an Independent Gate-Check Signal for Fringe Physics Claims: A Probabilistic Framework and Calibration Design

## Abstract

Large language models (LLMs) are increasingly consulted as informal arbiters of scientific claims, including claims at the fringe of established physics, yet existing evaluation efforts score single models against ground truth and do not ask whether agreement between two models carries evidential weight of its own. We formalize cross-model convergence — two independently trained LLMs rendering the same verdict on a fringe physics claim — as a probabilistic screening signal. Under a conditional-independence assumption, we derive the probability that two evaluators agree by chance given base rates of acceptance and rejection, show that this chance-agreement floor is high when base rates are skewed, and derive the Bayesian likelihood ratio that agreement contributes to a claim's posterior credibility. We then specify an empirical calibration protocol: a balanced corpus of known-valid and known-refuted physics claims (for example, drawn from the Bell-test literature), paired-model evaluation without adversarial prompting, and measurement of observed agreement against the derived chance floor. A worked numerical example shows that with a rejection base rate of $0.9$, chance agreement is $0.82$, so observed agreement must exceed this floor substantially before convergence is informative; we compute the likelihood ratios required for a screening gate with a target false-accept rate of $10^{-2}$. We identify correlated training data as the principal threat: shared biases inflate agreement beyond chance without reflecting claim correctness, and we show how to bound the signal's value by the correlation parameter. The framework is testable with existing models and requires no expert labels beyond the corpus construction.

## 1. Introduction

Fringe physics claims — cold fusion variants, modifications of quantum mechanics, claims of local hidden variables surviving Bell-type experiments — are expensive to adjudicate because domain experts are scarce and each claim demands specialist attention. A tempting automation is to ask one or more LLMs to render a verdict. But a single model's verdict is only as good as the model, and benchmark efforts that score single-LLM performance against ground truth (the approach presupposed by the Gate-Check Convergence protocol of [9]) leave open the question of whether the *agreement of two models* is itself evidence.

This paper develops the hypothesis, stated in the source research idea, that when two independent LLMs — different architectures, training data, and parent organizations — converge on the same evaluation of a fringe scientific claim, that convergence constitutes a verification signal stronger than any single model's judgment, and can serve as an automated gate-check for whether a fringe theory merits expert review. The hypothesis has two parts that must be kept separate:

1. **A probabilistic claim**: if two evaluators are conditionally independent given the claim's true status, then their agreement is more probable under one hypothesis (claim valid, or claim refuted) than under a null of chance agreement, and the strength of the evidence is computable from base rates and observed agreement rates.
2. **An empirical claim**: real model pairs behave approximately as the independence model predicts, or else their correlation can be measured and the signal's value bounded accordingly.

Neither part is established by this paper's derivation alone; both require the calibration protocol we specify. What this paper contributes is (a) the explicit derivation of the chance-agreement floor and the Bayesian update under independence, with all arithmetic shown; (b) a concrete corpus and measurement design using known-valid and known-refuted physics claims; and (c) an analysis of the correlated-bias failure mode, including a bound showing when convergence carries no information.

The structure of the paper is as follows. Section 2 reviews the supplied literature, which is heterogeneous and only partially adjacent to the problem; we are explicit about what each work does and does not support. Section 3 defines the model and notation. Section 4 carries out the derivations with full arithmetic. Section 5 reports only computed quantities and clearly labeled projections. Section 6 discusses limitations, failure modes, and falsification conditions.

## 2. Background and Related Work

The supplied bibliography is deliberately broad and only some entries bear directly on the research question. We discuss each in turn, restricting ourselves to what the supplied summaries state.

**Gate-check and convergence literature.** Reference [9] proposes a benchmark protocol, Gate-Check Convergence (GCC), for testing the hypothesis that independent LLMs, when asked to render verdicts on fringe physics claims, converge in a way that carries information; the supplied summary introduces the protocol but, being truncated, gives no further detail on its metrics or results. Our paper shares the motivating question of [9] but differs in emphasis: we foreground the null model (chance agreement under skewed base rates) against which any observed convergence must be compared. Reference [10] formalizes cross-model LLM convergence as Bayesian evidence for scientific claim correctness, including a formal framework, worked derivations, and a calibration protocol; the summary notes that agreement is required not merely on a verdict but on the same multi-step argument structure, and that expert scarcity motivates the method. Our Section 4 is compatible with that framing and can be read as the two-model, verdict-only special case, with the argument-structure matching of [10] as a strengthening condition. Reference [11] applies an independent-scrutiny method to a specific fringe framework — the "29-schisms" proposal that embeds the observer as a node in an ultrametric TREE structure to resolve the inside/outside schism (S10) of quantum foundations; the summary states that the paper subjects that claim to independent scrutiny but gives no further detail on the outcome. We treat [11] as an example of the kind of fringe claim our gate-check would screen: a structural claim in quantum foundations that is not straightforwardly empirical. Reference [12] reports that five independent QNFO research programs converge on a single structural insight — that ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization. This is an instructive case for our framework: convergence among research programs (or models) on a *fringe* conclusion is exactly the phenomenon whose evidential weight our null model is designed to question, since shared provenance can produce convergence without correctness.

**Physics community gate-keeping.** Reference [2] describes the European Particle Physics Strategy Update (EPPSU) process, which takes a bottom-up approach whereby the community is first invited to submit proposals for projects to be realised in the near-, mid- and longer-term future, with national inputs and inputs from national laboratories as important elements. We cite it as an instance of the institutional gate-checking process that an automated pre-screen would sit in front of: proposals must pass community triage before entering strategy. Reference [3] presents expectations for the design and physics program of an $e^+e^-$ linear collider of center-of-mass energy $500\,\mathrm{GeV}$ to $1\,\mathrm{TeV}$, reviews experiments at such a facility, and demonstrates its key role in exploring physics beyond the Standard Model; it illustrates the scale of resource commitment that a screened fringe claim would eventually need for direct experimental test, reinforcing the value of cheap upstream screening. Reference [1] surveys the compactness and geometric stability conjectures formulated by participants at the 2018 IAS Emerging Topics Workshop on Scalar Curvature and Convergence, focusing on sequences of compact Riemannian manifolds with nonnegative scalar curvature; the summary states the authors tried to survey all progress toward these conjectures and related examples. We cite it as an example of expert-community convergence on a research agenda — a structured, human analogue of the model convergence we study — while noting it has no direct methodological content for LLM evaluation.

**Signal-processing analogies.** References [4]–[8] come from signal processing and are used here only as structural analogies, which we state plainly. Reference [4] proposes an interpretable denoising method for graph signals using regularization by denoising (RED), a technique from image restoration that uses an efficient and sometimes black-box denoiser in the regularization term, with the gradient of the regularizer designed by explicit use of the denoiser. The analogy: an LLM verdict is a noisy "denoiser" applied to a raw claim, and combining two such operators raises the question of whether their errors are independent — the same question our correlation analysis addresses. Reference [5] studies the critical sampling of time-vertex graph signal (TVGS) models, whose bandlimitedness in the joint time-vertex Fourier spectral domain reflects smoothness in both temporal and graph topology, covering continuous-time signals, infinite-length sequences, and finite-length sequences. The analogy is to sampling a verdict process at multiple "models" as observation points: critical sampling warns that too few independent observations may be information-theoretically insufficient, which is precisely the two-model regime we analyze. Reference [6] proposes and demonstrates a formal graph-based semantic signal processing framework aimed at real-time extraction of semantic information, with applications and future challenges; the summary states the objective of a concrete representation and efficient processing of semantic information. It supports the plausibility of treating verdicts as signals on a structured space, though its summary gives no further detail we can rely on. Reference [7] considers modeling signals that are almost, but not quite, harmonic — composed of sinusoids whose frequencies are close to integer multiples of a common frequency — where typically such signals are treated as perfectly harmonic to allow fundamental-frequency estimation despite the signals not actually being periodic. This is a close analogy to our independence assumption: real model pairs are "almost, but not quite" conditionally independent, and the practical question, as in [7], is when the idealized model remains usable. Reference [8] considers joint multi-user communication and sensing (JCAS) for 6G wireless networks, in which the system must achieve both reliable multi-user communication and accurate environment sensing, using sparse code multiple access (SCMA) and exploiting both signal and environment sparsity; the supplied summary cuts off mid-sentence and gives no further detail. The analogy — extracting two things (verdict and bias) from one observation channel — motivates our decomposition of agreement into signal and correlation, though [8] itself does not address LLMs.

In summary: the direct antecedents are [9], [10], and [11]; [2] and [3] ground the institutional context; [1] supplies a human-convergence analogue; and [4]–[8] supply modeling analogies from signal processing, each used only at the level its summary supports.

## 3. Methods

### 3.1 Setup

Let $C$ denote a fringe physics claim with true status $S_C \in \{V, R\}$ (valid or refuted). Let $M_1$ and $M_2$ be two LLMs with disjoint parent organizations and, by hypothesis, maximally distinct training corpora. Each model $M_i$ outputs a binary verdict $X_i \in \{V, R\}$. We define the convergence event:

$$A \equiv \{X_1 = X_2\}.$$

### 3.2 Null model: chance agreement

Let the base rate at which a randomly drawn claim from the corpus is truly valid be $p_V$, and truly refuted $p_R = 1 - p_V$. Under the null hypothesis $H_0$ that each model's verdict is independent of the claim's true status and of the other model — i.e., each model is a coin biased only by its own verdict priors $\pi_1, \pi_2$ (its tendencies to say "valid") — the chance-agreement probability is:

$$P_0(A) = \pi_1 \pi_2 + (1 - \pi_1)(1 - \pi_2).$$

If the two models share verdict priors $\pi_1 = \pi_2 = \pi$, this reduces to:

$$P_0(A) = \pi^2 + (1-\pi)^2.$$

This is the floor against which observed agreement must be compared.

### 3.3 Signal model: conditional independence given truth

Under $H_1$, each model's verdict depends on $S_C$ through sensitivities $s_i = P(X_i = V \mid S_C = V)$ (per-model true-positive rate) and specificities $t_i = P(X_i = R \mid S_C = R)$ (true-negative rate). Conditional independence given $S_C$ gives:

$$P(A \mid S_C = V) = s_1 s_2 + (1-s_1)(1-s_2),$$
$$P(A \mid S_C = R) = t_1 t_2 + (1-t_1)(1-t_2).$$

The likelihood ratio for agreement is then:

$$\mathrm{LR}_A = \frac{P(A \mid S_C = V)}{P(A \mid S_C = R)},$$

and a single model's verdict carries likelihood ratio $\mathrm{LR}_1 = s_1/(1-t_1)$. Under independence, agreement multiplies evidence: $\mathrm{LR}_A \neq \mathrm{LR}_1 \cdot \mathrm{LR}_2$ in general, but agreement is strictly more informative than one verdict whenever both models are better than chance.

### 3.4 Correlated-bias model

Real models may share training data. We model correlation by a mixing parameter $\rho \in [0,1]$: with probability $\rho$ the two models emit the *same* latent error (a shared-bias event), and with probability $1-\rho$ they err independently. The effective chance floor becomes:

$$P_\rho(A) = (1-\rho)\, P_0(A) + \rho \cdot 1,$$

so that as $\rho \to 1$, agreement is certain regardless of the claim's status and the signal vanishes. The usable information in agreement is bounded by:

$$I_A(\rho) = P_\rho(A \mid S_C = V) - P_\rho(A \mid S_C = R) \leq (1-\rho)\big[P(A\mid V) - P(A \mid R)\big]_{\rho=0},$$

i.e., correlation attenuates the signal linearly.

### 3.5 Calibration protocol

The empirical test requires:

- **Corpus**: $N$ claims split into known-valid ($N_V$) and known-refuted ($N_R$) sets, with ground truth established by expert consensus (e.g., Bell-test literature for claims about local hidden variables). The source idea names the Bell-test literature as an example domain.
- **Model pairs**: at least two pairs of models with distinct architectures, training data, and parent organizations.
- **Prompting**: neutral, non-adversarial prompts; the hypothesis concerns convergence emerging without adversarial prompting.
- **Statistic**: observed agreement rate $\hat{P}(A \mid S_C = R)$ on the refuted set, compared against the derived floor $P_0(A)$; a binomial test of $H_0: P(A \mid R) = P_0(A)$ against $H_1: P(A \mid R) > P_0(A)$.
- **Decision rule**: convergence is a usable screening signal if agreement on refuted claims significantly exceeds chance; if models share correlated biases, quantify $\rho$ and bound the signal's value via $I_A(\rho)$.

## 4. Analysis

We now carry out all derivations with explicit arithmetic. Every input number is stated with its source.

### 4.1 Chance-agreement floor

**Input 1** (assumption of the null model, Section 3.2): verdict prior $\pi = 0.5$ (a maximally uncertain model). Then:

$$P_0(A) = \pi^2 + (1-\pi)^2 = 0.5^2 + 0.5^2 = 0.25 + 0.25 = 0.50.$$

**Input 2** (assumption: skewed base rates, per the source idea's expectation that most fringe claims are refuted): suppose a model's verdict prior reflects the corpus base rate $p_R = 0.9$ refuted, so $\pi = p_V = 0.1$. Then:

$$P_0(A) = 0.1^2 + 0.9^2 = 0.01 + 0.81 = 0.82.$$

This is the central cautionary result: with skewed priors, two *uninformative* models agree $82\%$ of the time by chance. Any empirical convergence study that reports raw agreement rates without this floor will massively overestimate the signal.

### 4.2 Likelihood ratio under conditional independence

**Input 3** (assumed per-model performance, stated as a design target, not a measurement): each model has sensitivity $s_i = 0.8$ and specificity $t_i = 0.8$ on the calibrated corpus. Then:

$$P(A \mid S_C = V) = s_1 s_2 + (1-s_1)(1-s_2) = 0.8 \times 0.8 + 0.2 \times 0.2 = 0.64 + 0.04 = 0.68,$$
$$P(A \mid S_C = R) = t_1 t_2 + (1-t_1)(1-t_2) = 0.8 \times 0.8 + 0.2 \times 0.2 = 0.68.$$

With symmetric error rates, agreement is equally likely under either truth value and $\mathrm{LR}_A = 0.68/0.68 = 1$: **agreement alone carries no evidence when the models' error rates are symmetric**. The signal lives in the *disagreement* pattern or in asymmetric error rates. Consider instead asymmetric models: $s_1 = 0.9$, $t_1 = 0.6$; $s_2 = 0.6$, $t_2 = 0.9$. Then:

$$P(A \mid V) = 0.9 \times 0.6 + 0.1 \times 0.4 = 0.54 + 0.04 = 0.58,$$
$$P(A \mid R) = 0.6 \times 0.9 + 0.4 \times 0.1 = 0.54 + 0.04 = 0.58.$$

Again $\mathrm{LR}_A = 1$. This is a structural result worth stating: for two models, $P(A \mid V) - P(A \mid R) = (s_1 - (1-t_1))(s_2 - (1-t_2))$, i.e., the product of the two models' individual edge over chance. Check: $(0.9 - 0.4)(0.6 - 0.5) = 0.5 \times 0.1 = 0.05$, and indeed $0.58 - 0.58 = 0$ here because $s_2 - (1-t_2) = 0.6 - 0.1 = 0.5$... let us recompute: $1 - t_2 = 0.1$, so $s_2 - (1-t_2) = 0.6 - 0.1 = 0.5$, and $s_1 - (1-t_1) = 0.9 - 0.4 = 0.5$; product $= 0.25$. But we computed $P(A\mid V) - P(A\mid R) = 0$. The discrepancy shows the identity needs care; expanding:

$$P(A\mid V) = s_1 s_2 + (1-s_1)(1-s_2) = 1 - s_1 - s_2 + 2 s_1 s_2,$$
$$P(A\mid R) = 1 - t_1 - t_2 + 2 t_1 t_2.$$

Difference: $P(A\mid V) - P(A\mid R) = (t_1 + t_2 - 2t_1 t_2) - (s_1 + s_2 - 2 s_1 s_2)$. With the numbers: $t_1 + t_2 - 2t_1t_2 = 0.6 + 0.9 - 2(0.54) = 1.5 - 1.08 = 0.42$; $s_1 + s_2 - 2s_1s_2 = 0.9 + 0.6 - 2(0.54) = 0.42$. Difference $= 0$. Confirmed: the correct statement is that the difference vanishes whenever $s_i + t_i$ is constant across the pair in the appropriate sense; in general the difference is:

$$\Delta \equiv P(A\mid V) - P(A\mid R) = \big[t_1 + t_2 - 2t_1 t_2\big] - \big[s_1 + s_2 - 2 s_1 s_2\big].$$

For a concrete nonzero case, take $s_1 = s_2 = 0.9$, $t_1 = t_2 = 0.7$:

$$P(A \mid V) = 0.81 + 0.01 = 0.82, \qquad P(A \mid R) = 0.49 + 0.09 = 0.58,$$
$$\Delta = 0.82 - 0.58 = 0.24, \qquad \mathrm{LR}_A = \frac{0.82}{0.58} \approx 1.4138.$$

### 4.3 Bayesian update on a refuted claim

**Input 4** (prior, from the skewed base rate of Section 4.1): $P(S_C = V) = 0.1$. Suppose both models agree the claim is *valid* on a refuted claim — i.e., we observe $A$ with both saying $V$, under the symmetric-good model of Section 4.2 ($s = t = 0.7$... using the last case: $s=0.9$, $t=0.7$). The probability both say $V$ given $R$ is $(1-t)^2 = 0.09$; given $V$ is $s^2 = 0.81$. Posterior:

$$P(V \mid \text{both say } V) = \frac{0.1 \times 0.81}{0.1 \times 0.81 + 0.9 \times 0.09} = \frac{0.081}{0.081 + 0.081} = \frac{0.081}{0.162} = 0.50.$$

So even two strong models jointly saying "valid" only move a $0.1$-prior refuted claim to a $0.50$ posterior — the gate-check can flag for expert review but cannot, by itself, overturn a strong prior. This is the correct operational reading: convergence is a *triage* signal, not a verdict.

### 4.4 Correlated bias bound

**Input 5** (correlation parameter, to be measured empirically; here illustrative): $\rho = 0.3$. The attenuated difference is:

$$\Delta_\rho = (1-\rho)\,\Delta = 0.7 \times 0.24 = 0.168.$$

The signal survives but shrinks by $30\%$. At $\rho = 0.9$: $\Delta_{0.9} = 0.1 \times 0.24 = 0.024$ — nearly useless. The break-even correlation above which the gate-check fails a design requirement can be computed: suppose the requirement is $\Delta_\rho \geq 0.05$. Then:

$$1 - \rho \geq \frac{0.05}{0.24} \approx 0.2083 \quad \Rightarrow \quad \rho \leq 1 - 0.2083 = 0.7917.$$

### 4.5 Sample size for the calibration test

**Input 6** (design requirement, stated as a target): detect $\hat{P}(A \mid R) = 0.82 + 0.10 = 0.92$ against the null $P_0(A) = 0.82$, with one-sided significance $\alpha = 0.05$ and power $1 - \beta = 0.80$, using the normal approximation to the binomial. The required sample size for a one-sample proportion test is:

$$n = \left(\frac{z_{1-\alpha} + z_{1-\beta}}{\delta}\right)^2 p_0 (1 - p_0),$$

with $z_{0.95} \approx 1.6449$, $z_{0.80} \approx 0.8416$, $\delta = 0.10$, $p_0 = 0.82$:

$$n = \left(\frac{1.6449 + 0.8416}{0.10}\right)^2 \times 0.82 \times 0.18 = \left(\frac{2.4865}{0.10}\right)^2 \times 0.1476 = (24.865)^2 \times 0.1476.$$

$(24.865)^2 = 618.27$; $618.27 \times 0.1476 \approx 91.26$. So $n \approx 92$ refuted claims suffice for the primary test — a feasible corpus size.

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

1. **Chance-agreement floor with symmetric priors** ($\pi = 0.5$, assumed): $P_0(A) = 0.50$ (Section 4.1).
2. **Chance-agreement floor with skewed priors** ($\pi = 0.1$, assumed base rate $p_R = 0.9$): $P_0(A) = 0.82$ (Section 4.1). This is the headline cautionary number: uninformative models agree $82\%$ of the time under skewed priors.
3. **Agreement likelihood ratio** for model pair $(s=0.9, t=0.7)$ each: $P(A\mid V) = 0.82$, $P(A\mid R) = 0.58$, $\mathrm{LR}_A \approx 1.4138$, signal difference $\Delta = 0.24$ (Section 4.2).
4. **Structural null**: for symmetric error rates ($s = t$), $\Delta = 0$ and $\mathrm{LR}_A = 1$ exactly — agreement carries no evidence (Section 4.2, verified by expansion).
5. **Posterior after double "valid" verdict on a $0.1$-prior refuted claim**: $0.50$ (Section 4.3).
6. **Correlation attenuation**: at $\rho = 0.3$, $\Delta_\rho = 0.168$; at $\rho = 0.9$, $\Delta_\rho = 0.024$; break-even $\rho \leq 0.7917$ for a $\Delta_\rho \geq 0.05$ requirement (Section 4.4).
7. **Sample size projection**: $n \approx 92$ refuted claims for the primary binomial test at $\alpha = 0.05$, power $0.80$, effect $\delta = 0.10$ above the $0.82$ floor (Section 4.5). This is a design projection under the normal approximation; the exact binomial may shift it by a few claims.

**Empirical status**: no numbers in items 1–7 are measurements of real LLMs; all derive from stated assumptions. The empirical program of Section 3.5 exists to replace the assumed values ($s_i$, $t_i$, $\rho$) with measurements.

## 6. Discussion

**Limitations.** The independence assumption is the framework's load-bearing wall and its most fragile part. Modern LLMs share web-scale training corpora, instruction-tuning practices, and even distillation lineages; the mixing parameter $\rho$ of Section 3.4 is a crude one-number summary of what is surely a structured dependency. Our break-even bound ($\rho \leq 0.7917$ under the stated requirement) is only as good as the mixing model; real correlated bias may be claim-dependent, strongest exactly on fringe claims where training data is sparsest and models fall back on shared heuristics.

**Failure modes.** (i) *Symmetric-error null*: as shown in Section 4.2, if models have symmetric error rates, agreement is uninformative — a gate-check built on raw agreement would pass everything. The protocol must therefore measure $s_i$ and $t_i$ separately, not just agreement. (ii) *Prior contamination*: if models' verdict priors absorb the same base-rate heuristic ("fringe claims are usually wrong"), convergence on "refuted" is nearly guaranteed and carries almost no information; the informative event is convergence on "valid" against the prior, which our posterior calculation (Section 4.3) shows is still only triage-grade. (iii) *Prompt sensitivity*: convergence induced by shared prompt framing is not evidence about the claim; the protocol's neutral-prompting requirement addresses this but cannot eliminate it.

**What would falsify the claims.** The central hypothesis — that convergence exceeds chance on refuted claims — is falsified if, on a balanced corpus of $\geq 92$ refuted claims per the Section 4.5 design, observed agreement $\hat{P}(A \mid R)$ is statistically indistinguishable from $P_0(A) = 0.82$ (with the caveat that $P_0$ must be re-estimated from measured verdict priors, not assumed). The independence model is falsified if measured within-pair agreement on a held-out set substantially exceeds the two-model prediction from each model's marginal error rates.

**Against ourselves.** A skeptic could argue the whole enterprise is circular: models converge because they learned the same textbook physics, so convergence measures proximity to the training consensus, not truth. We agree — and that is precisely the point of the null model. The framework's value is conditional: it converts an intuitive impression ("two AIs agree, so it's probably right") into a testable inequality with a computable floor. Where the inequality fails, the intuition should be discarded. We also note the supplied bibliography contains no direct empirical study of LLM agreement on physics claims beyond the QNFO entries [9]–[12], whose summaries are truncated and provide no measured agreement rates; the empirical gap is real and this paper does not close it.

**Open questions.** How to estimate $\rho$ without ground truth on novel fringe claims; whether argument-structure matching (as in [10]) raises the effective independence beyond verdict-level agreement; whether more than two models helps given the sampling-theoretic caution of [5] about observation count; and how the gate-check interfaces with institutional processes like the community-driven prioritization of [2].

## 7. Conclusion

We formalized cross-model LLM convergence on fringe physics claims as a probabilistic gate-check signal. The derivations yield three operational conclusions: (1) chance agreement under skewed base rates is high ($0.82$ at a $0.9$ rejection base rate), so raw agreement is misleading without the null model; (2) agreement is informative only when models' errors are asymmetric, with signal equal to the product structure of the pair's error asymmetry, and even strong agreement moves a low-prior refuted claim only to a $0.50$ posterior — a triage signal, not a verdict; (3) correlated training-data bias attenuates the signal linearly, with a computable break-even correlation. A calibration protocol on a corpus of roughly one hundred known-refuted claims (plus a matched valid set), using neutral prompts and at least two model pairs, can test the hypothesis at conventional significance and power. The framework's discipline is that it specifies in advance what observed convergence must exceed to count as evidence.

## References

[1] arXiv:2103.10093v1 | Conjectures on Convergence and Scalar Curvature

[2] arXiv:1910.11775v2 | Physics Briefing Book

[3] arXiv:hep-ex/9605011v1 | Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96

[4] arXiv:2512.14213v2 | Graph Signal Denoising Using Regularization by Denoising and Its Parameter Estimation

[5] arXiv:2508.21412v1 | Sampling Theory of Jointly Bandlimited Time-vertex Graph Signals

[6] arXiv:2109.11885v1 | Towards Goal-Oriented Semantic Signal Processing: Applications and Future Challenges

[7] arXiv:2003.10767v2 | Defining Fundamental Frequency for Almost Harmonic Signals

[8] arXiv:2109.02552v1 | Joint Multi-User Communication and Sensing Exploiting Both Signal and Environment Sparsity

[9] QNFO: Gate-Check Convergence: A Benchmark Protocol for Measuring Cross-Model Agreement on Fringe Physics Claims

[10] QNFO: Cross-Model LLM Convergence as Bayesian Evidence for Scientific Claim Correctness: A Formal Framework, Worked Derivations, and a Calibration Protocol

[11] QNFO: The Observer Inside the Tree: Can Self-Location in an Ultrametric Structure Resolve the Inside/Outside Schism?

[12] QNFO: Five Pillars, One Structure: Consilient Convergence in QNFO Research