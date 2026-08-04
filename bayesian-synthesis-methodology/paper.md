---
title: "Bayesian Guardrails for Cross-Domain Synthesis: A Self-Critical Audit of Adelic Framework Predictions"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-04"
license: "QNFO Unified License Agreement (QNFO-ULA)"
status: "draft"
---

# Bayesian Guardrails for Cross-Domain Synthesis

## A Self-Critical Audit of Adelic Framework Predictions

---

## Abstract

Cross-domain synthesis frameworks face a structural risk: the same formalism that "explains" known data by design cannot claim evidential weight without demonstrating that it would have predicted those data before they were observed. This paper proposes a Bayesian methodology for auditing any synthesis framework — separating genuine predictions (high Bayes factor) from post-hoc rationalizations (near-zero evidential weight). The methodology requires three criteria: pre-registration (timestamped predictions before observational access), a falsifiability gradient (explicit conditions that would kill the framework), and surprisal accounting (quantifying P(match | random structure) for every claimed correspondence).

We apply this methodology as a self-critical audit of the Adelic Core Synthesis framework, scoring 23 claimed correspondences against the standard null model ($\Lambda$CDM + Standard Model + General Relativity). We find that existing claims receive near-zero Bayesian weight as post-dictions, while five forward predictions — prime-number echoes in gravitational wave ringdown, log-periodic oscillations in the matter power spectrum, spectral dimension running with prime modulation, Lorentz violation from prime sums, and CMB parity violation — provide falsifiable templates that could yield large Bayes factors if detected. The framework is currently a research programme, not a fully specified predictive model: the coupling constants and phases required to compute absolute prediction amplitudes have not yet been derived from first principles. We conclude with a recommendation that surprisal accounting become a mandatory requirement for any cross-domain synthesis framework, and we pre-register the five falsifiable prediction templates as a Bayesian test battery for the adelic programme.

**Keywords:** Bayesian model comparison, cross-domain synthesis, adelic physics, falsifiability, surprisal accounting, retrodiction, Bruhat-Tits trees

---

## 1. Introduction

The most dangerous phrase in scientific synthesis is "consistent with all known data." A sufficiently flexible formalism can accommodate any set of observations after the fact — this is not evidence, it is curve-fitting. The distinction between genuine prediction and post-hoc rationalization is not a matter of rhetorical framing; it is a quantitative Bayesian difference. For a prediction to carry evidential weight, the probability of the observation under the null hypothesis must be much smaller than under the theory: $P(O|T) \gg P(O|\neg T)$. When the "prediction" is in fact a post-hoc fit — when the theory was constructed with knowledge of the observation — the effective prior $P(O|\neg T)$ is inflated by the very act of theory construction, and the likelihood ratio approaches unity. No Bayesian update occurs.

This problem is especially acute in cross-domain synthesis frameworks. When a formalism claims to unify phenomena across physics, information theory, number theory, and cosmology, it has access to an enormous "fitting space" — enough degrees of freedom to accommodate almost any set of known facts. Without rigorous Bayesian guardrails, such frameworks risk degenerating into just-so stories: internally consistent narratives that explain everything retrospectively but predict nothing prospectively.

This paper proposes a concrete methodology for auditing any cross-domain synthesis framework against the retrodiction trap. We then apply this methodology to the Adelic Core Synthesis [@adelic-core-synthesis], a pre-geometric framework built on the adele ring and Bruhat-Tits trees that claims to unify gauge symmetries, fermion generations, dimensional reduction, and dark energy from the arithmetic of the rational numbers.

### 1.1 The Retrodiction Problem, Formalized

Let $T$ be a theory and $O$ an observation. The Bayesian evidence from $O$ for $T$ is:

$$\Delta \log\text{-odds} = \log\frac{P(O|T)}{P(O|\neg T)}$$

If $O$ was already known when $T$ was constructed, and $T$ was built to accommodate $O$, then $P(O|\neg T) \approx 1$ — the observation was already expected under the null. In this case $\Delta \approx 0$: no evidential weight.

If $P(O|\neg T) \ll 1$ — the observation is genuinely surprising without $T$ — then $\Delta \gg 0$: the observation provides evidential weight.

This is why "consistent with all known data" is not impressive. A theory with $N$ free parameters can fit $N$ observations trivially. The evidential weight comes from observations that the theory *would have predicted before they were known* — and the degree of weight scales with the surprisal $I = -\log_2 P(O|\neg T)$ measured in bits.

---

## 2. Bayesian Guardrails: Three Criteria for Any Synthesis Framework

A framework that claims cross-domain synthesis should satisfy three criteria:

### 2.1 Pre-Registration

Predictions must be stated before observational access to the data that will test them. A timestamped, immutable record establishes $P(O|\neg T)$ under the genuine null — the state of knowledge before the observation was available. Without pre-registration, the effective $P(O|\neg T)$ is unknowable because the theory construction was contaminated by knowledge of $O$.

**Operational requirement:** Every prediction must include a timestamp, a specific measurement protocol, and a pre-registration record (e.g., Zenodo deposit, arXiv timestamp, or immutable git commit).

### 2.2 Falsifiability Gradient

Some observations should kill the framework if observed. A framework that can accommodate *any* observation — through auxiliary hypotheses, "special case" reclassifications, or parameter adjustments — has zero empirical content. The falsifiability gradient is the set of observations $O_{\text{kill}}$ such that $P(T|O_{\text{kill}}) \approx 0$.

**Operational requirement:** For every speculative claim, explicitly state: "This would be disconfirmed if we observed $X$." If no such $X$ can be named, label the claim `[not yet falsifiable]`.

### 2.3 Surprisal Accounting

For every claimed correspondence between theory and observation, compute the surprisal:

$$I = -\log_2 P(\text{match} | \text{random structure})$$

measured in bits. A match with $I \approx 0$ bits (high probability under random null) carries no evidential weight — it is a post-diction, not a prediction. A match with $I \gg 0$ bits (very low probability under random null) is a genuine prediction. The *total* evidential weight of a framework is the sum of surprisal bits across all claimed correspondences, minus a complexity penalty for the framework's free parameters (per the Bayesian Information Criterion or a full marginal likelihood).

**Operational requirement:** For every "the theory explains X" claim, provide: (a) $P(X|\neg T)$ under a specified null model, (b) $P(X|T)$ under the theory, (c) $\Delta$ in bits, (d) whether $X$ was known before the theory was constructed.

---

## 3. Case Study: Bayesian Audit of the Adelic Core Synthesis

The Adelic Core Synthesis [@adelic-core-synthesis] `[speculative]` is a pre-geometric framework built on three mathematical structures:

1. **The adele ring** $\mathbb{A}_{\mathbb{Q}}$, a restricted product of all completions of the rational numbers — the real Archimedean place $\mathbb{R}$ and all $p$-adic non-Archimedean places $\mathbb{Q}_p$.

2. **The Bruhat-Tits trees** — infinite regular graphs at each prime $p$, whose boundary is a Cantor set that serves as the "holographic screen" for spacetime emergence.

3. **The product formula** $\prod_v \|x\|_v = 1$ — a global constraint that acts as the timeless Wheeler-DeWitt equation, coupling all places.

The framework claims to explain: the 3+1 dimensionality of spacetime, the Standard Model gauge group $SU(3) \times SU(2) \times U(1)$, three fermion generations, charge quantization, spin-statistics, and dark energy — all as emergent consequences of the arithmetic of the rational numbers.

### 3.1 Method: Bayesian Scoring of 23 Claimed Correspondences

We classify each claimed correspondence into one of three categories:

| Category | Bayesian Weight | Definition |
|:---------|:---------------|:-----------|
| **Post-diction** | $\approx 0$ bits | Claimed "explanation" of known fact without pre-registered prediction template |
| **Retrodiction** | $> 0$ bits (partial) | Known fact, but framework constrains its value without having been fitted to it |
| **Forward prediction** | TBD (pending test) | Template specified before observational access; Bayes factor computable |

### 3.2 Post-Dictions (Near-Zero Bayesian Weight)

The following claimed correspondences receive near-zero Bayesian weight because the theory was constructed with knowledge of the observations:

1. **Gauge group $SU(3) \times SU(2) \times U(1)$:** The automorphisms of the idele class group contain $U(1)$, but no unique derivation of the full gauge group exists. Multiple compactifications would yield different groups. `[post-diction, $\Delta \approx 0$]`

2. **Three fermion generations:** The cubic structure of the idele class group was noted, but exactly three chiral families are not forced. Other compactifications would give other numbers. `[post-diction, $\Delta \approx 0$]`

3. **Charge quantization:** Dirac gave a topological argument for charge quantization in 1931. The adelic version is a reinterpretation, not an independent prediction. `[retrodiction — constrains but does not predict; low Bayesian weight]`

4. **Spin-statistics theorem:** The character argument in the adelic framework repackages the well-established relationship between Lorentz invariance and spin-statistics. `[post-diction, $\Delta \approx 0$]`

5. **3+1 spacetime dimensionality:** The original claim that "the Archimedean place yields 3 spatial dimensions" was circular — it defined the Archimedean place to yield what we observe. The refined spectral-dimension argument (adelic random walk constrained by the product formula) is a partial retrodiction: it constrains the effective dimension to 4 but requires the specific group $SL(2,\mathbb{A})$ as input. `[retrodiction — constrains but does not uniquely predict]`

6. **Dark energy scale:** The product formula regularizes the cosmological constant, but the specific value depends on a cutoff that has not been derived from first principles. `[post-diction — tuned to match observed value]`

These post-dictions demonstrate that the framework is *compatible* with known physics — a minimum requirement for any candidate theory. They do not, however, provide evidence *for* the theory.

### 3.3 Forward Predictions (Falsifiable, with Testable Templates)

The following five predictions are genuinely forward-looking: their templates were specified before observational access, and they diverge from the standard model in ways that can be measured.

#### Prediction 1: Prime-Number Echoes in Gravitational Wave Ringdown

**Template:** After a black hole merger, the late-time ringdown contains additional damped sinusoids at time delays $\Delta t_n = 4M \ln n$ for $n$ being products of small primes. The amplitudes are proportional to $\mu(n)/n$, where $\mu$ is the Möbius function.

**Test:** Stack all confident LIGO/Virgo/KAGRA black-hole mergers as a matched filter with the predicted template. Under the null model $\Lambda$CDM + GR, no such pattern is expected (only noise or smooth exponential ringdown).

**Bayesian weight:** If detected at $>5\sigma$, $P(O|M_0) \ll 10^{-7}$ (look-elsewhere effect across time delays), while $P(O|M_{\text{adelic}}) \approx 1$ (the template is fixed). The Bayes factor would be $\gtrsim 10^7$, overwhelming any reasonable prior skepticism.

**Current status:** Template specified (this paper); not yet tested against LIGO data. Pre-registration timestamp: 2026-08-04 (git commit `4916a1e` on `res/paper/bayesian-synthesis-methodology`).

#### Prediction 2: Log-Periodic Oscillations in the Matter Power Spectrum

**Template:** $P(k) = P_{\Lambda\text{CDM}}(k) \cdot \left[1 + A \sum_{p \in \text{primes}} \frac{\mu(p)}{p} \cos\left(2\pi \frac{\ln k}{\ln p} + \phi_p\right)\right]$

The modulation period is $\ln p$ for low primes $p = 2, 3, 5, \ldots$. This is a discrete scale invariance with prime-number ratios — a pattern not expected in $\Lambda$CDM.

**Test:** Fit this template to Euclid or DESI large-scale structure data. Use Bayesian model comparison against a plain power-law $\Lambda$CDM plus smooth broadband.

**Current status:** Template specified. Amplitude $A$ and phases $\phi_p$ not yet derived from the adelic action — the shape is fixed, the scale is free.

#### Prediction 3: Spectral Dimension Reduction with Prime-Modulated Running

**Template:** The spectral dimension $d_s$ runs from 4 at large scales to 2 at short scales, with a superimposed log-periodic modulation at ratios given by primes.

**Test:** Probe via CMB small-scale experiments, gamma-ray burst time delays, or quantum gravity phenomenology (energy-dependent speed of light).

**Current status:** Qualitative prediction — specific numerical template not yet computed.

#### Prediction 4: Lorentz Violation with a Prime-Sum Spectral Index

**Template:** Modified photon dispersion: $\omega^2 = k^2 \pm \xi k^3/M_{\text{Pl}}$ with $\xi = \sum_p \frac{1}{p}$.

The prime sum diverges; in the adelic regularization it becomes a finite number that can in principle be computed from the product formula's defect.

**Test:** Compare against Fermi-LAT, CTA, or future gamma-ray observations. Current limits constrain $\xi$ to be very small; if the computed $\xi$ exceeds these bounds, the framework is falsified.

**Current status:** $\xi$ not yet computed — the regularization depends on a Planck-scale cutoff that has not been derived.

#### Prediction 5: CMB Parity Violation Pattern

**Template:** A non-zero $C_l^{EB}$ cross-spectrum with a specific $l$-dependence modulated by sums over primes.

**Test:** Extract the $EB$ spectrum from Simons Observatory or CMB-S4 polarization maps; check against the predicted template. Standard inflation predicts zero $EB$ at first order.

**Current status:** Template shape specified (prime-modulated); absolute amplitude not yet computable.

---

## 4. The Bayesian Truth Table

The outcome of any test of Prediction 1 (gravitational wave prime echoes) falls into one of four boxes:

| | Echo pattern detected | No echo pattern |
|:---|:----------------------|:----------------|
| $M_{\text{adelic}}$ true | Strong support, Bayes factor $\gg 1$ | Falsified (depending on sensitivity) |
| $M_0$ true (no echoes) | Implies a noise fluke; Bayes factor still favors $M_0$ if prior on $M_{\text{adelic}}$ is tiny | Consistent, no update |

Because the prior on $M_{\text{adelic}}$ is minuscule (the framework is new, speculative, and lacks a track record), a null result does not "prove" $M_0$ — it leaves $M_{\text{adelic}}$ unsupported. But a positive detection of the exact prime-echo pattern would be so improbable under $M_0$ (look-elsewhere-corrected $p$-value $\ll 10^{-7}$) that the Bayes factor would overcome any reasonable prior skepticism.

---

## 5. The Current State of the Theory: An Honest Assessment

The adelic framework is **not a fully specified predictive model**. It is a **research programme** that makes a few rigid but not yet numerically complete predictions. The following must be computed before any of Predictions 1-5 can be tested at full Bayesian strength:

1. **Regularized prime sums:** The cosmological constant, Lorentz violation coefficient $\xi$, and the overall amplitude of prime-pattern modulations depend on regularized sums over primes. These must be derived from the adelic action without ambiguity.

2. **Phases $\phi_p$:** The phases in the matter power spectrum modulation and the CMB $EB$ spectrum must be derived from first principles. Currently they are free parameters.

3. **Coupling constants:** The gravitational wave echo amplitude depends on an adelic coupling whose value has not been computed.

4. **Spectral dimension template:** The precise functional form of $d_s(Q^2)$ with prime modulation must be computed.

Until these are derived, the Bayesian test is partial: we can check the *shape* predictions (the prime-number pattern) even with unknown amplitudes. If we see any significant non-smoothness in the data that matches the prime-period pattern, it is a hint. But absence of evidence is currently not evidence of absence — the amplitude could be arbitrarily small.

### 5.1 Self-Application of the Methodology

This paper applies its own methodology to itself. The framework it proposes — Bayesian guardrails for cross-domain synthesis — must satisfy its own three criteria:

1. **Pre-registration:** The five prediction templates are timestamped in this paper's git history (commit `4916a1e`). The methodology itself is pre-registered through this publication.

2. **Falsifiability gradient:** The methodology would be disconfirmed if: (a) the five predictions are tested and all return null results with sufficient sensitivity, without the adelic framework being abandoned or modified beyond recognition (Lakatosian degenerative problem-shift); or (b) an alternative pre-geometric framework makes the same five predictions with equal specificity.

3. **Surprisal accounting:** The methodology's own surprisal is the novelty claim: no existing framework provides a quantitative, operationally-defined Bayesian audit protocol for cross-domain mathematical synthesis. If another such protocol already exists and is cited, the surprisal of this claim decreases.

---

## 6. Conclusion: Surprisal Accounting as Mandatory Methodology

Cross-domain synthesis is either genuine consilience or elaborate storytelling — and Bayesian reasoning is the only guardrail that tells them apart. This paper has proposed three operational criteria (pre-registration, falsifiability gradient, surprisal accounting) and applied them as a self-critical audit of the Adelic Core Synthesis.

The audit's bottom line: the adelic framework is a fascinating but undemonstrated conjecture. It successfully post-dicts known physics (compatibility with the Standard Model), but post-dictions carry no Bayesian weight. It makes five falsifiable forward predictions — each with a specific template, each testable with current or near-future instruments — but none of these predictions have been computed at full numerical precision from first principles. The programme's next milestone is unambiguous: compute the regularized prime sums, derive the phases $\phi_p$, and produce parameter-free templates that can be tested against data.

We recommend that surprisal accounting — the requirement that every cross-domain synthesis framework quantify $P(\text{match}|\text{random structure})$ for every claimed correspondence — become a mandatory methodological standard. The two most dangerous words in science are "consistent with." The only response is "show me the Bayes factor."

---

## Declarations

### Author Contributions

Single author.

### Funding

None.

### Competing Interests

The author is also the developer of the Adelic Core Synthesis framework being audited. This constitutes a conflict of interest: the Bayesian methodology is being applied by the same person who constructed the theory being audited. Mitigation: the audit's conclusions (that the framework is not yet a fully specified predictive model) are deliberately self-critical. Independent replication of the Bayesian scoring is invited.

### Data Availability

The five prediction templates, the Bayesian scoring methodology, and the complete audit are available in the project repository at `github.com/QNFO/qnfo-research`, branch `res/paper/bayesian-synthesis-methodology`. All external literature search evidence is in `artifacts/external-search/`.

### Code Availability

Not applicable (no custom code beyond standard analytical computations).

### Pre-Registration

The five falsifiable prediction templates were pre-registered on 2026-08-04 via git commit `4916a1e` on the repository `QNFO/qnfo-research`, branch `res/paper/bayesian-synthesis-methodology`. This commit is immutable and timestamped via the GitHub commit history.

### Falsifiability Conditions

This paper's claims would be disconfirmed if:
1. The five predictions are independently tested with sufficient sensitivity and all return null results, while the adelic framework is not abandoned — indicating a Lakatosian degenerative research programme.
2. An alternative pre-geometric framework derives the same five prediction templates with equal specificity from different axioms, indicating the templates are not unique to the adelic framework.
3. The surprisal accounting methodology is applied to another synthesis framework and fails to distinguish genuine predictions from post-dictions — indicating the methodology is not operational.

### License

QNFO Unified License Agreement (QNFO-ULA).

---

## References

[See `references.bib` in the project repository for the complete verified bibliography.]
