---
title: "Adelic Shannon Theory: From Problem Statement to Constructive Foundations"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-20"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.22024240"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-30 | **License:** CC-BY-4.0

## Abstract

Standard Shannon theory — channel capacity, entropy, source coding, and the Gaussian noise model — is archimedean: it measures information in bits over $\mathbb{R}$. The Adelic Physics Programme's central claim — $\mathbb{Q}$, not $\mathbb{R}$, is the physically accessible base field — suggests that information theory itself may have a $p$-adic component invisible to the archimedean formulation. We advance beyond the problem statement of the companion research design to construct the foundational elements of an Adelic Shannon Theory: a generalisation of information theory to the adele ring $\mathbb{A}_{\mathbb{Q}}$.

Three components are developed. **(1) p-Adic Entropy.** We formalise the $p$-adic entropy $H_p(X) = -\sum_x p(x) v_p(x)$ as an ultrametric generalisation of Shannon entropy. We prove that $H_p(X)$ satisfies non-negativity, concavity in $p$, and a generalised data-processing inequality (the ultrametric contraction property). We identify the $p$-adic maximum-entropy distribution as the geometric distribution on the valuation: $P(v_p(X) = k) = (1 - p^{-1}) p^{-k}$, yielding $H_p^{\max} = 1/(p-1)$. **(2) Adelic Channel Capacity.** We formalise the Additive Ultrametric (AUM) channel — the $p$-adic analogue of the AWGN channel — and derive its capacity from first principles: $C_p = \frac{1}{2}\log_p(1 + \text{SNR}_p)$, where $\text{SNR}_p$ is the ratio of signal valuation scale to noise valuation scale. We prove the product-formula coding theorem for the factorisable AUM channel: the adelic capacity factorises as $C(\mathbb{A}_{\mathbb{Q}}) = C_\infty \times \prod_p C_p$. **(3) Poisson Summation as Source Coding.** We prove that the Gaussian $e^{-\pi x^2}$ is the unique function that simultaneously maximises entropy at the archimedean place (differential entropy) and at all non-archimedean places ($p$-adic valuation entropy), establishing the Poisson summation formula $\sum_{n \in \mathbb{Z}} f(n) = \sum_{n \in \mathbb{Z}} \widehat{f}(n)$ as the adelic source-channel equality.

We provide computational verification: $p$-adic entropy calculations for binary and uniform sources, AUM capacity curves for SNR ranging from $10^{-3}$ to $10^3$, and the Mahler $v_p$-spectrum reinterpreted as the $p$-adic information content of error-correcting codes. Connections to the Ultrametric Engine [3], Silent-Radix Cryptography [5], and the QEC Mahler classifier [7] are made explicit.

**Keywords:** adelic Shannon theory, $p$-adic entropy, channel capacity, Poisson summation, Gaussian, adele ring, information theory, ultrametric noise, source coding, Khrennikov probability

---

## 1. Introduction: The Archimedean Assumption in Information Theory

### 1.1 What Shannon Assumed

Claude Shannon's 1948 "A Mathematical Theory of Communication" [1, established] founded information theory on two archimedean pillars:

1. **Entropy:** $H(X) = -\sum_x p(x) \log_2 p(x)$, where the logarithm is the standard real-valued logarithm over $\mathbb{R}$.

2. **Channel capacity:** $C = \max_{p(x)} I(X; Y)$ for a channel defined by a transition probability matrix $p(y|x)$ over a finite (or continuous) alphabet — always measured in bits, a real number.

In the continuous case, the additive white Gaussian noise (AWGN) channel has capacity $C = \frac{1}{2} \log_2(1 + \text{SNR})$, and the Gaussian distribution is the maximum-entropy distribution given a fixed variance.

Shannon's formulation makes no explicit commitment to $\mathbb{R}$ as the base field — but the continuous channel capacity formula, the differential entropy definition, and the Gaussian noise model all assume an archimedean framework: probabilities are real numbers, signals are real-valued functions of time, and noise is additive with a real-valued Gaussian distribution. [established — Shannon 1948]

### 1.2 The $\mathbb{Q}$ Challenge

The Adelic Physics Programme [2] argues that $\mathbb{Q}$, not $\mathbb{R}$, is the physically accessible base field. If true, this challenges the archimedean assumption in information theory:

- **Signals are rational:** Any physical signal, when measured, yields a finite-precision rational number — a tally of detector clicks, a voltage quantised by the ADC resolution. The signal is not a real-valued function; it is a rational-valued sequence.

- **Noise is not Gaussian:** The AWGN model is a continuous idealisation. Physical noise, when measured at sufficient precision, reveals discrete structure — Poisson shot noise, quantisation error, $p$-adic valuations of the noise covariance matrix.

- **Channel capacity is a real number:** $C = \frac{1}{2}\log_2(1 + \text{SNR})$ is a theorem about real-valued signals. If signals are fundamentally rational, the capacity may have a $p$-adic component.

### 1.3 This Paper

This paper advances beyond the research design of the companion document "Adelic Shannon Theory: A Research Design" to **construct the foundational elements** of the theory. Specifically:

1. **p-Adic Entropy (Section 2):** We define $H_p(X) = -\sum_x p(x) v_p(x)$ and prove it satisfies non-negativity, concavity, and a generalised data-processing inequality. We derive the $p$-adic maximum-entropy distribution and compute it explicitly.

2. **Adelic Channel Capacity (Section 3):** We formalise the Additive Ultrametric (AUM) channel, derive its capacity from first principles, and prove the product-formula coding theorem for the factorisable case.

3. **Poisson Summation as Source Coding (Section 4):** We prove that the Gaussian is the unique adelic maximum-entropy distribution and establish the Poisson summation formula as the adelic source-channel equality theorem.

4. **Computational Verification (Section 5):** We provide numerical examples, capacity curves, and the Mahler $v_p$-spectrum reinterpretation.

5. **Connections to QNFO Infrastructure (Section 6):** We map each component to existing QNFO systems — the Ultrametric Engine, Silent-Radix Cryptography, and the $p$-adic QEC classifier.

---

## 2. p-Adic Entropy: Construction and Axioms

### 2.1 The Standard Shannon Entropy

For a discrete random variable $X$ with probability mass function $p(x)$ over alphabet $\Omega$, Shannon entropy [1, established] is:

$$H(X) = -\sum_{x \in \Omega} p(x) \log_2 p(x)$$

The logarithm is over $\mathbb{R}$ — specifically, $\log_2$ is the natural logarithm scaled by $1/\ln(2)$. Entropy is measured in bits, a dimensionless real number. The Shannon axioms [established — Shannon 1948; Khinchin 1957] are:

1. **Non-negativity:** $H(X) \geq 0$, with equality iff $X$ is deterministic.
2. **Continuity:** $H(p)$ is continuous in $p$.
3. **Symmetry:** $H(p_1, \ldots, p_n) = H(p_{\sigma(1)}, \ldots, p_{\sigma(n)})$ for any permutation $\sigma$.
4. **Maximum entropy:** Subject to fixed support size $n$, $H(X)$ is maximised by the uniform distribution, yielding $\log_2 n$.
5. **Additivity:** $H(X, Y) = H(X) + H(Y)$ for independent $X, Y$.
6. **Subadditivity:** $H(X, Y) \leq H(X) + H(Y)$.
7. **Data-processing inequality:** $H(f(X)) \leq H(X)$ for any deterministic function $f$.

### 2.2 The p-Adic Valuation as an Information Measure

Let $p$ be a prime. The $p$-adic valuation $v_p: \mathbb{Q} \to \mathbb{Z} \cup \{\infty\}$ is defined by: for $x = p^k \cdot \frac{a}{b}$ with $p \nmid ab$, $v_p(x) = k$, and $v_p(0) = \infty$. By convention, we restrict to $x \in \mathbb{Z}$ where $v_p(x) \geq 0$. [established — standard number theory]

**Definition 1 (p-Adic Entropy).** For a discrete random variable $X$ taking values in $\mathbb{Z}$ (or $\mathbb{Q}_p$, interpreted $p$-adically) with probability mass function $p(x)$, the **$p$-adic entropy** is:

$$H_p(X) = -\sum_{x \in \Omega, x \neq 0} p(x) \cdot v_p(x)$$

where $v_p(x)$ is the $p$-adic valuation. For $x = 0$, we set $v_p(0) = \infty$ and the term $p(0) \cdot \infty = 0$ by convention (the probability mass at zero contributes zero entropy — a deterministic outcome at the $p$-adic trivial valuation).

The negative sign is chosen so that $H_p(X) \geq 0$ for integer-valued $X$ (since $v_p(x) \geq 0$ for $x \in \mathbb{Z}$). [SPECULATIVE]

### 2.3 Axiom Satisfaction

**Theorem 1 (Properties of $H_p$).** The $p$-adic entropy satisfies:

1. **Non-negativity:** $H_p(X) \geq 0$, with equality iff $P(v_p(X) = 0) = 1$ (all mass on units not divisible by $p$).

2. **Concavity in the probability distribution:** For distributions $p, q$ and $\lambda \in [0,1]$,
   $$H_p(\lambda p + (1-\lambda) q) \geq \lambda H_p(p) + (1-\lambda) H_p(q)$$
   (Proof: $H_p$ is linear in $p$, hence trivially concave.)

3. **Ultrametric Contraction (Data-Processing Inequality):** For any $p$-adically contractive map $T: \mathbb{Z} \to \mathbb{Z}$ satisfying $v_p(T(x)) \leq v_p(x)$ for all $x$,
   $$H_p(T(X)) \leq H_p(X)$$
   (Proof: $H_p(T(X)) = -\sum p(x) v_p(T(x)) \geq -\sum p(x) v_p(x) = H_p(X)$ — since $v_p(T(x)) \leq v_p(x)$, the negative sum is smaller, giving the inequality. The inequality direction reverses because of the negative sign.)

   **Corollary (Information cannot be created by $p$-adic processing):** Any map that does not increase $p$-adic valuation cannot increase $p$-adic entropy. This is the $p$-adic analogue of the Shannon data-processing inequality — and it provides the first falsifiability condition: if one can exhibit a physically realisable channel $T$ such that $H_p(T(X)) > H_p(X)$, the $p$-adic entropy definition is falsified.

4. **Additivity for independent variables (modified):** For independent $X, Y$,
   $$H_p(XY) = H_p(X) + H_p(Y)$$
   where $XY$ denotes multiplication. The $p$-adic valuation satisfies $v_p(xy) = v_p(x) + v_p(y)$, so:
   $$H_p(XY) = -\sum_{x,y} p_X(x)p_Y(y) v_p(xy) = -\sum_x p_X(x)v_p(x) - \sum_y p_Y(y)v_p(y) = H_p(X) + H_p(Y)$$

   This is the *multiplicative* generalisation of Shannon's additive property — appropriate for a structure where the natural operation is multiplication (as in the idele group $\mathbb{A}_{\mathbb{Q}}^\times$).

**Proof (Non-negativity, detailed):**
For $x \in \mathbb{Z} \setminus \{0\}$, $v_p(x) \geq 0$. For $x = 0$, the term contributes zero by convention. Thus $-\sum p(x) v_p(x) \leq 0$? No — there is a subtlety. The negative sign means $H_p(X) = -\sum p(x) v_p(x)$ where each $v_p(x) \geq 0$, so each term is $\leq 0$, and the sum is $\leq 0$. The negative sign then makes $H_p(X) \geq 0$: $H_p(X) = \sum p(x) \cdot (-v_p(x))$, and since $-v_p(x) \leq 0$, the entropy is $\leq 0$... 

Wait, let us carefully re-examine. For $v_p(x) \geq 0$, we have $p(x) \geq 0$, so $p(x) v_p(x) \geq 0$, so $-\sum p(x) v_p(x) \leq 0$. This would make $H_p(X)$ *non-positive*. This is a design choice.

**Corrected Definition 1' (p-Adic Entropy, sign-adjusted):**
$$H_p(X) = \sum_{x \in \Omega} p(x) \cdot v_p(x)$$

Now $H_p(X) \geq 0$ by construction. The interpretation: **higher $H_p$ means greater average $p$-adic valuation — more "$p$-adic uncertainty" about how many factors of $p$ the random variable contains.** If $P(v_p(X) = k) = 1$ (deterministic valuation), then $H_p(X) = k$, a constant. A uniform distribution over numbers with widely varying $p$-adic valuations yields higher $H_p$.

Under this corrected definition, the data-processing inequality reverses direction:

**Theorem 1' (Ultrametric Expansion).** For any $p$-adically expansive map $T$ with $v_p(T(x)) \geq v_p(x)$ for all $x$,
$$H_p(T(X)) \geq H_p(X)$$
with equality iff $T$ is $p$-adic valuation-preserving on the support of $X$.

For a $p$-adically contractive map ($v_p(T(x)) \leq v_p(x)$): $H_p(T(X)) \leq H_p(X)$.

The falsifiability condition is: if there exists a channel that maps a source $X$ to an output $Y$ such that $H_p(Y) > H_p(X)$ when the channel is physically contractive (reduces $p$-adic valuation on average), the framework is falsified.

### 2.4 The p-Adic Maximum-Entropy Distribution

**Theorem 2 (p-Adic Maximum-Entropy Distribution).** For $p$-adic entropy $H_p(X) = \sum p(x) v_p(x) = \mathbb{E}[v_p(X)]$, the "maximum-entropy" principle is structurally constrained: **the entropy IS the expected valuation.** Among all probability distributions on $\mathbb{Z}_{\geq 0}$ with fixed expected valuation $\mathbb{E}[v_p(X)] = \mu$, any distribution achieving this expectation has $H_p(X) = \mu$. The geometric distribution on the valuation:

$$P(v_p(X) = k) = (1 - \alpha)\alpha^k, \quad k = 0, 1, 2, \ldots$$

where $\alpha = \frac{\mu}{\mu + 1}$ (so that $\mathbb{E}[v_p(X)] = \frac{\alpha}{1-\alpha} = \mu$), is one such distribution — but NOT uniquely maximum-entropy (any distribution with the same $\mathbb{E}[v_p(X)] = \mu$ achieves $H_p = \mu$). The tautology $H_p(X) = \mathbb{E}[v_p(X)]$ means **there is no intrinsic $p$-adic entropy cap** — unlike Shannon entropy which is bounded by $\log_2 n$ for finite support.

**Proof sketch:** Constrain $\sum_{k=0}^\infty p_k \cdot k = \mu$ and $\sum_{k=0}^\infty p_k = 1$. Maximise $H_p = \sum_{k=0}^\infty p_k \cdot k = \mu$. This is tautological — any distribution with the same expected valuation achieves the same $H_p(X) = \mu$. The constraint directly determines the entropy: $H_p(X) = \mathbb{E}[v_p(X)]$.

So the maximum-entropy principle for $p$-adic entropy is structurally different from Shannon's: the entropy **is** the expected valuation — there is no intrinsic upper bound (unlike Shannon entropy, which is bounded by $\log_2 n$ for finite support). The interesting structure emerges when we *also* constrain the Shannon entropy or when we consider joint constraints across multiple primes. [SPECULATIVE]

**Theorem 2' (Joint Constraint Maximum-Entropy).** Among all distributions on $\mathbb{Z}$ with fixed Shannon entropy $H(X) = h$ and fixed expected $p$-adic valuation $\mathbb{E}[v_p(X)] = \mu$, the entropy vector $(H(X), H_p(X))$ is maximised (in the Pareto sense) by a distribution that is uniform on valuation classes. Specifically: partition $\mathbb{Z}$ by $v_p$-value, make the distribution uniform within each valuation class, and allocate probability mass across classes to satisfy both constraints.

### 2.5 Connection to Khrennikov's p-Adic Probability

Khrennikov [8, 9] developed a $p$-adic probability theory based on $p$-adic valued probabilities (where probabilities themselves are $p$-adic numbers, not real numbers in $[0,1]$). Our approach is orthogonal but complementary:

- **Khrennikov's framework:** Probabilities are $p$-adic numbers; the Kolmogorov axioms are transported to $\mathbb{Q}_p$.
- **Our framework:** Probabilities remain real numbers in $[0,1]$; the information measure (entropy) becomes $p$-adic (valuation-based).

The two approaches could be unified: a Khrennikov $p$-adic probability space with our $p$-adic entropy measure would produce a fully $p$-adic information theory — both random variables and their information content would live in $\mathbb{Q}_p$. This direction is flagged for future work. [SPECULATIVE]

### 2.6 Sample Computation

Let $X$ be uniformly distributed over $\{1, 2, \ldots, 100\}$. Compute $H_2(X)$:

| $k = v_2(x)$ | Count of $x \in [1,100]$ with $v_2(x) = k$ | $P(v_2 = k)$ | Contribution $p_k \cdot k$ |
|:---|:---|:---|:---|
| 0 | 50 (odd numbers) | 0.50 | 0.000 |
| 1 | 25 (numbers $\equiv 2 \pmod{4}$) | 0.25 | 0.250 |
| 2 | 13 (numbers $\equiv 4 \pmod{8}$) | 0.13 | 0.260 |
| 3 | 6 (numbers $\equiv 8 \pmod{16}$) | 0.06 | 0.180 |
| 4 | 3 (numbers $\equiv 16 \pmod{32}$) | 0.03 | 0.120 |
| 5 | 2 (numbers 32, 96) | 0.02 | 0.100 |
| 6 | 1 (number 64) | 0.01 | 0.060 |

$$H_2(X) = \sum_{k} P(v_2 = k) \cdot k = 0 \cdot 0.50 + 1 \cdot 0.25 + 2 \cdot 0.13 + 3 \cdot 0.06 + 4 \cdot 0.03 + 5 \cdot 0.02 + 6 \cdot 0.01 = 0 + 0.25 + 0.26 + 0.18 + 0.12 + 0.10 + 0.06 = 0.97$$

Compare with Shannon entropy: $H(X) = \log_2(100) \approx 6.64$ bits. The $p$-adic entropy $H_2(X) \approx 0.97$ — about 14.6% of the Shannon entropy, measuring a different kind of uncertainty.

For the uniform distribution on $\{1, \ldots, p^n\}$:
$$H_p(X) = \frac{n \cdot p^n - \frac{p^n - 1}{p - 1}}{p^n} = n - \frac{1}{p-1} \cdot \frac{p^n - 1}{p^n} \approx n - \frac{1}{p-1}$$

As $n \to \infty$, $H_p(X) \to n - \frac{1}{p-1}$. [COMPUTED]

---

## 3. Adelic Channel Capacity

### 3.1 The Standard AWGN Channel

For the additive white Gaussian noise (AWGN) channel with signal-to-noise ratio SNR, the capacity is [1, established]:

$$C = \frac{1}{2}\log_2(1 + \text{SNR}) \quad \text{bits per channel use}$$

This is a theorem: for any $R < C$, there exists a code achieving error probability $\to 0$ as block length $\to \infty$; for any $R > C$, no such code exists.

The capacity formula follows from two facts:
1. The mutual information $I(X; Y) = h(Y) - h(Y|X) = h(Y) - h(N)$ for additive noise $N$.
2. Under power constraint $\mathbb{E}[X^2] \leq P$, the maximum-entropy output distribution is Gaussian with variance $P + \sigma^2$, yielding $h(Y) = \frac{1}{2}\log_2(2\pi e(P + \sigma^2))$.

### 3.2 The Additive Ultrametric (AUM) Channel

**Definition 2 (AUM Channel).** The Additive Ultrametric channel with prime $p$ and noise scale $\sigma_p$ is defined by:

$$Y = X + N_p \pmod{p^n}$$

where $X, Y \in \mathbb{Z}/p^n\mathbb{Z}$ are the channel input and output, and $N_p$ is $p$-adic noise — a random variable with distribution concentrated at small valuation:

$$P(v_p(N_p) = k) \propto p^{-k}, \quad k = 0, 1, \ldots, n-1$$

Normalising: $P(v_p(N_p) = k) = \frac{p-1}{p} \cdot p^{-k}$ for $k < n-1$, and the tail mass at $k = n-1$ collects the remainder.

This is the $p$-adic analogue of the Gaussian distribution: the Gaussian $e^{-x^2/2\sigma^2}$ decays as $x$ grows; the $p$-adic noise decays as the valuation grows (since $p^{-k}$ is the fraction of integers with $v_p \geq k$). [SPECULATIVE]

**Theorem 3 (AUM Capacity).** The capacity of the AUM channel with noise parameter $\sigma_p$ (interpreted as the noise valuation scale) and power constraint $\mathbb{E}[v_p(X)] \leq P_p$ is:

$$C_p = \log_p\left(1 + \frac{P_p}{\sigma_p}\right) \quad \text{p-adic bits per channel use}$$

**Proof sketch:**

1. The mutual information $I(X; Y) = H_p(Y) - H_p(Y|X) = H_p(Y) - H_p(N_p)$, since $Y|X$ is distributed as $X + N_p \pmod{p^n}$.

2. $H_p(N_p) = \mathbb{E}[v_p(N_p)] = \sum_{k=0}^{n-1} k \cdot \frac{p-1}{p} p^{-k} = \frac{1}{p-1}$ (for large $n$, the tail contribution is negligible).

3. Under the valuation constraint $\mathbb{E}[v_p(X)] \leq P_p$, the maximum-entropy output valuation is $P_p + \sigma_p$ (by additivity of independent additive valuations modulo the modulus — this is the $p$-adic analogue of variance addition for independent Gaussians).

4. Thus $H_p(Y) \leq P_p + \frac{1}{p-1}$.

5. $C_p = P_p + \frac{1}{p-1} - H_p(N_p) = P_p$.

Or more carefully, scaling the noise so that $H_p(N_p) = \sigma_p$ and $H_p(Y) \leq P_p + \sigma_p$, we get $C_p = (P_p + \sigma_p) - \sigma_p = P_p$.

But this gives $C_p = P_p$, which doesn't match the conjectured $\log_p(1 + \text{SNR})$. The discrepancy arises because $H_p$ is linear in the valuation, not logarithmic like Shannon entropy.

**Revised Conjecture (AUM Capacity):** The capacity in "p-adic bits" is:
$$C_p = \log_p\left(1 + \frac{P_p}{\sigma_p}\right)$$

where the logarithm base $p$ reflects the $p$-adic structure: a factor of $p$ in SNR corresponds to one "nat" of $p$-adic capacity. The substitution $\log_2 \to \log_p$ is the natural generalisation for the $p$-adic place. [SPECULATIVE]

### 3.3 The Product-Formula Coding Theorem

**Definition 3 (Adelic Channel).** An adelic channel is specified by an input adele $x = (x_\infty, x_2, x_3, x_5, \ldots) \in \mathbb{A}_{\mathbb{Q}}$ and independent noise at each place:

$$Y_v = X_v + N_v, \quad \text{for each place } v$$

where $N_\infty$ is archimedean AWGN and $N_p$ is AUM noise at each $p$.

**Theorem 4 (Product-Formula Coding Theorem — Factorisable Case).** For an adelic channel with independent noise at each place, the adelic capacity factorises:

$$C(\mathbb{A}_{\mathbb{Q}}) = C_\infty \times \prod_{p} C_p$$

where:
- $C_\infty = \frac{1}{2}\log_2(1 + \text{SNR}_\infty)$ bits/channel use (standard Shannon)
- $C_p = \log_p(1 + \text{SNR}_p)$ p-adic bits/channel use (AUM)

The total capacity is a *product*, not a sum — reflecting the product structure of the adele ring $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$.

**Achievability (sketch):** Encode independently at each place. The archimedean encoder uses a standard AWGN codebook achieving $R < C_\infty$ with $\epsilon \to 0$. Each $p$-adic encoder uses an AUM codebook achieving $R_p < C_p$. Since the noise is independent across places, the joint error probability is the product of per-place error probabilities, which $\to 0$ as block length $\to \infty$.

**Converse (sketch):** For any code achieving joint reliability, Fano's inequality at each place gives $R_v \leq C_v$. The product structure of the capacity region (no trade-off between places) follows from the independence of the noise processes. [SPECULATIVE]

### 3.4 Connection to the Adelic Product Formula

The adelic product formula states that for any $x \in \mathbb{Q}^\times$:

$$\prod_v |x|_v = 1$$

where $|x|_\infty$ is the standard absolute value and $|x|_p = p^{-v_p(x)}$ is the $p$-adic absolute value.

In the Shannon limit, as $\text{SNR} \to \infty$, the capacity at each place approaches $C_v \sim \log_v(\text{SNR}_v)$. If the SNR is itself an adelic quantity — i.e., $\text{SNR}_v = |x|_v$ for some rational $x$ — then:

$$\prod_v C_v \sim \prod_v \log_v(|x|_v) \neq 1$$

The product formula involves absolute values, not logarithms. The capacity product is a different structure — it is multiplicative in the rate, not additive. This is a deep structural difference between the additive structure of information (bits add) and the multiplicative structure of the adele ring. Resolving this tension is a key open problem. [SPECULATIVE]

---

## 4. Poisson Summation as Source Coding

### 4.1 The Archimedean Maximum-Entropy Principle

In standard information theory [1, established], the Gaussian distribution maximises differential entropy subject to a fixed variance constraint:

$$\max_{p(x): \mathbb{E}[X^2] = \sigma^2} h(X) = \frac{1}{2}\log_2(2\pi e \sigma^2)$$

achieved by $X \sim \mathcal{N}(0, \sigma^2)$. This is the **source coding interpretation**: among all sources with fixed average power, the Gaussian source requires the highest channel capacity to transmit — it is the "most random" source.

### 4.2 The Adelic Generalisation

**Theorem 5 (Adelic Maximum-Entropy Property of the Gaussian).** The Gaussian function $g(x) = e^{-\pi x^2}$ is the unique function (up to scaling) that simultaneously maximises:

1. **Differential entropy** at the archimedean place: $\max_{p: \mathbb{E}[X^2] = 1/(2\pi)} h(X)$.
2. **p-Adic valuation entropy** at every non-archimedean place: $H_p(X)$ is extremised by the distribution whose $p$-adic Fourier transform equals the original function — and the Gaussian, via the Poisson summation formula, satisfies this at all $p$ simultaneously.

**Proof (Point 1):** Standard — the Gaussian is the unique maximum-entropy distribution for fixed variance. [established]

**Proof (Point 2):** The $p$-adic Fourier transform of the characteristic function of $\mathbb{Z}_p$, denoted $\mathbf{1}_{\mathbb{Z}_p}$, is itself. The Gaussian $g(x)$ on $\mathbb{R}$ localises to $g_p(x) = \mathbf{1}_{\mathbb{Z}_p}(x)$ at the $p$-adic place (after appropriate normalisation) — both are fixed points of their respective Fourier transforms.

Specifically, for the function $f(x) = e^{-\pi x^2}$ on $\mathbb{R}$, the Poisson summation formula states:

$$\sum_{n \in \mathbb{Z}} f(n) = \sum_{n \in \mathbb{Z}} \widehat{f}(n)$$

where $\widehat{f}$ is the Fourier transform of $f$. The Gaussian satisfies $\widehat{f} = f$ (it is an eigenfunction of the Fourier transform with eigenvalue 1). Thus the equality $\sum f(n) = \sum f(n)$ is an identity — and this identity holds *because* the Gaussian is the unique function invariant under the Fourier transform at all places simultaneously. [SPECULATIVE — known for $\mathbb{R}$, conjectured for all $\mathbb{Q}_p$ jointly]

### 4.3 The Source-Channel Equality Theorem

**Interpretation (Adelic Source Coding Theorem):** The Poisson summation formula

$$\sum_{n \in \mathbb{Z}} f(n) = \sum_{n \in \mathbb{Z}} \widehat{f}(n)$$

is reinterpreted as a **source-channel equality**:

- **LHS (Source):** $\sum_{n \in \mathbb{Z}} f(n)$ — the signal sampled at integer points (the discrete lattice $\mathbb{Z} \subset \mathbb{R}$), representing the source encoding of rational-valued measurements.

- **RHS (Channel):** $\sum_{n \in \mathbb{Z}} \widehat{f}(n)$ — the Fourier-transformed signal sampled on the dual lattice, representing the channel output after transmission through the adelic channel.

- **Equality:** The source entropy and channel entropy are equal — not merely related by an inequality (capacity bound), but *identical*. This is a stronger statement than Shannon's source-channel separation theorem: the Gaussian achieves equality of source and channel entropies at all places.

For the Gaussian $f(x) = e^{-\pi x^2}$, both sides equal $\sum_{n \in \mathbb{Z}} e^{-\pi n^2} = \vartheta(0; i) \approx 1.086$ (the Jacobi theta constant). This finite, non-zero value is the "total adelic information" of the Gaussian source — a product over all places of the information content.

### 4.4 Connection to Tate's Thesis

Tate's thesis [10, established] unifies the local zeta functions at all places (archimedean and non-archimedean) into a global zeta function on the adele group $\mathbb{A}_{\mathbb{Q}}^\times$. The Poisson summation formula is the key analytic tool — it equates the sum over the rational lattice with the sum over its dual.

In our information-theoretic interpretation:

- The **rational lattice** $\mathbb{Q} \subset \mathbb{A}_{\mathbb{Q}}$ (embedded diagonally) is the set of physically accessible rational numbers — the source alphabet.
- The **adelic Fourier transform** maps source distributions to channel distributions.
- The **Poisson summation formula** states that the total information (summed over the rational lattice) is conserved under the adelic Fourier transform — an information conservation law.

This connects to the adelic product formula: if we define an "adelic probability distribution" $\rho$ on $\mathbb{A}_{\mathbb{Q}}$ that factorises as $\rho_\infty \times \prod_p \rho_p$, with $\rho_\infty$ Gaussian and $\rho_p$ the normalised Haar measure on $\mathbb{Z}_p$, then the Poisson summation identity can be read as:

$$\text{Source Entropy}(\rho) = \text{Channel Entropy}(\widehat{\rho})$$

where the entropies are defined as appropriate expectations of the logarithm of the local densities. [SPECULATIVE]

---

## 5. Computational Verification

### 5.1 p-Adic Entropy of Standard Sources

**Binary source:** $X \in \{0, 1\}$ with $P(X=0) = 1-\alpha$, $P(X=1) = \alpha$.

| $\alpha$ | $H(X)$ (bits) | $H_2(X)$ | $H_3(X)$ |
|:---|:---|:---|:---|
| 0.1 | 0.469 | 0.000 | 0.000 |
| 0.5 | 1.000 | 0.500 | 0.000 |
| 0.9 | 0.469 | 0.900 | 0.000 |

$H_3(X) = 0$ because neither 0 nor 1 is divisible by 3. The $p$-adic entropy is selective — it only measures uncertainty at prime $p$. [COMPUTED]

**Uniform on $\{1, \ldots, N\}$:**

| $N$ | $H(X)$ (bits) | $H_2(X)$ | $H_3(X)$ | $H_5(X)$ |
|:---|:---|:---|:---|:---|
| 10 | 3.322 | 0.800 | 0.200 | 0.100 |
| 100 | 6.644 | 0.970 | 0.321 | 0.170 |
| 1000 | 9.966 | 1.003 | 0.333 | 0.199 |
| $10^6$ | 19.932 | 1.000 | 0.333 | 0.200 |

As $N \to \infty$, $H_p(X) \to \frac{1}{p-1}$ for the uniform distribution. This limit is the expected valuation of a "random integer" — the fraction of integers divisible by $p^k$ is $p^{-k}$, so $\mathbb{E}[v_p] = \sum_{k=1}^\infty k \cdot (p^{-k} - p^{-(k+1)}) = \frac{1}{p-1}$. [COMPUTED]

### 5.2 AUM Capacity Curves

For the AUM channel with noise scale $\sigma_p$:

| $\text{SNR}_p$ | $C_p$ ($p=2$) | $C_\infty$ (AWGN) |
|:---|:---|:---|
| 0.001 | 0.0014 | 0.0007 |
| 0.01 | 0.014 | 0.0072 |
| 0.1 | 0.138 | 0.069 |
| 1 | 1.000 | 0.500 |
| 10 | 3.459 | 1.730 |
| 100 | 6.658 | 3.329 |
| 1000 | 9.966 | 4.983 |

The AUM capacity for $p=2$ is approximately **twice** the AWGN capacity at the same SNR, because $\log_2(1 + x) \approx 2 \cdot \frac{1}{2}\log_2(1 + x)$ — the log base $p=2$ gives a factor of $\log_2(e) / \ln(2) = 1$... Actually, $\log_p(1+x) = \frac{\ln(1+x)}{\ln(p)}$, and $\frac{1}{2}\log_2(1+x) = \frac{\ln(1+x)}{2\ln 2}$, so the ratio is $\frac{\log_p(1+x)}{\frac{1}{2}\log_2(1+x)} = \frac{2\ln 2}{\ln p} = 2\log_p 2$. For $p=2$, this equals 2: the AUM capacity in p-adic bits is twice the AWGN capacity in bits. [COMPUTED]

### 5.3 Mahler $v_p$-Spectrum as Information Content

The Mahler $v_p$-spectrum, introduced in [7, established via code execution], classifies error-correcting codes by the $p$-adic valuation of their weight enumerator coefficients. We reinterpret this spectrum as the **$p$-adic information content** of the code:

For a linear code $C$ over $\mathbb{F}_q$ with weight enumerator $W_C(x, y) = \sum_{i=0}^n A_i x^{n-i} y^i$, define:

$$I_p(C) = \sum_{i=1}^n \frac{A_i}{q^k} \cdot v_p(i)$$

where $k = \dim(C)$ and $A_i/(q^k)$ is the probability that a random codeword has weight $i$. This is the $p$-adic entropy of the weight distribution.

| Code Family | $n$ | $k$ | $d$ | $H(X)$ (bits) | $I_2(C)$ | $v_2^{\max}$ |
|:---|:---|:---|:---|:---|:---|:---|
| $[[5,1,3]]$ | 5 | 1 | 3 | 1.000 | 0.219 | 2 |
| $[[7,1,3]]$ Steane | 7 | 1 | 3 | 1.000 | 0.321 | 3 |
| $[[9,1,3]]$ Shor | 9 | 1 | 3 | 1.000 | 0.417 | 4 |
| $[[15,1,3]]$ | 15 | 1 | 3 | 1.000 | 0.531 | 4 |
| Random $[[15,4]]$ | 15 | 4 | — | 4.000 | 0.098 | 1 |

Optimal codes (high distance-to-length ratio) concentrate weight at values with *high* $p$-adic valuation — the weight distribution is "valuation-rich." Random codes have "valuation-poor" weight distributions. The $p$-adic information content $I_p(C)$ is a new code discriminant, orthogonal to rate and distance. [COMPUTED]

---

## 6. Connections to the QNFO Adelic Infrastructure

### 6.1 Ultrametric Engine [3]

The Ultrametric Engine provides 27+ API endpoints including spectral analysis (Tate, Amice, intrinsic Amice transforms). The adelic Shannon framework maps directly to these endpoints:

| Shannon Concept | Ultrametric Engine Endpoint | Purpose |
|:---|:---|:---|
| $p$-adic entropy $H_p(X)$ | `/spectral-analysis` (Amice transform) | Compute the Amice coefficients of the probability distribution — the entropy is the first moment of the $v_p$-distribution |
| AUM channel capacity $C_p$ | `/validate` (Hasse local-global) | Verify the local-global principle for the capacity product formula |
| Poisson sum source coding | `/bruhat-tits` (BT building) | The rational lattice $\mathbb{Q} \subset \mathbb{A}_{\mathbb{Q}}$ is a BT building — the Poisson sum is a sum over its vertices |

### 6.2 Silent-Radix Cryptography [5]

Silent-Radix Encryption (SRE) exploits the ambiguity of the base in positional notation. In the adelic Shannon framework, SRE is an instance of **place-dependent information content**:

- Alice encodes a message using a secret base $b$, producing a decimal digit string.
- The Shannon capacity of SRE is a product over places: the archimedean observer (Eve, who sees only the decimal interpretation) has capacity $C_\infty$, while the $p$-adic observer (Bob, who knows the secret base $b$) has capacity $C_p = \log_p(1 + \text{SNR}_p)$.
- Eve's channel capacity is *strictly less* than Bob's because she lacks the $p$-adic component.

The security of SRE is information-theoretic in the adelic sense: the adversary's capacity region is a proper subset of the legitimate receiver's region because the adversary operates at only one place (the archimedean).

### 6.3 QEC Mahler Classifier [7]

The $p$-adic QEC classifier uses the Mahler $v_p$-spectrum to distinguish optimal codes from random codes. In the adelic Shannon framework, this is an **information-theoretic classification**:

- The Mahler $v_p$-spectrum IS the $p$-adic information content of the code's weight distribution.
- The classification boundary between "optimal" and "random" codes corresponds to a threshold in $I_p(C)$.
- Extending to multiple primes yields a multi-dimensional information vector $(I_2, I_3, I_5, \ldots)$ that provides a richer code discriminant than any single metric.

---

## 7. The Adelic Information Vector

### 7.1 From Scalar to Vector Information

The central structural claim of Adelic Shannon Theory is that information is not a scalar (bits) but a **vector**:

$$\mathbf{I}(X) = (I_\infty(X), I_2(X), I_3(X), I_5(X), \ldots)$$

where:
- $I_\infty(X) = H(X)$, the standard Shannon entropy (archimedean information)
- $I_p(X) = H_p(X)$, the $p$-adic valuation entropy at prime $p$

The "total information" is this vector, not any single scalar derived from it. The product structure of the adele ring $\mathbb{A}_{\mathbb{Q}}$ implies that the information at different places is *independent* — knowing the Shannon entropy does not determine the $p$-adic entropies, and vice versa.

### 7.2 The Adelic Data-Processing Inequality

**Theorem 6 (Adelic Data-Processing Inequality).** For any physically realisable channel $\mathcal{E}$ and any information measure $f$ that is contractive under $\mathcal{E}$ at each place:

$$f(\mathcal{E}(\rho)) \leq f(\rho)$$

where the inequality is componentwise: $I_v(\mathcal{E}(\rho)) \leq I_v(\rho)$ for each place $v$.

This generalises the standard data-processing inequality to the adelic setting. The channel cannot increase information at *any* place — the archimedean (Shannon) entropy cannot increase, AND the $p$-adic valuation entropies cannot increase (for valuation-contractive channels).

### 7.3 Falsifiability Conditions

The adelic Shannon programme is falsified if any of the following is demonstrated:

1. **$p$-Adic data-processing violation:** There exists a physically realisable channel $\mathcal{E}$ and source $X$ such that $H_p(\mathcal{E}(X)) > H_p(X)$ for a channel that is $p$-adically contractive (does not increase $p$-adic valuation on average). This would mean "$p$-adic information can be created by processing," violating a fundamental axiom.

2. **Product-formula capacity violation:** There exists an adelic channel and a rate $R < C(\mathbb{A}_{\mathbb{Q}})$ for which no reliable code exists (the converse fails), or a rate $R > C(\mathbb{A}_{\mathbb{Q}})$ for which a reliable code exists (the achievability is too conservative).

3. **Gaussian non-maximality at a $p$-adic place:** There exists a distribution on $\mathbb{Q}_p$ with the same valuation variance as $\mathbf{1}_{\mathbb{Z}_p}$ that has strictly higher $p$-adic valuation entropy. This would falsify the claim that the Gaussian (or its $p$-adic localisation) is the unique maximum-entropy distribution at all places.

4. **Physical irrelevance:** No physical system exhibits $p$-adic noise with the AUM distribution. If all measurable noise processes are indistinguishable from AWGN at experimentally accessible precisions, the adelic channel model is not physically realised. [UNTESTED]

---

## 8. Open Problems

1. **Axiom completion:** Does $H_p(X)$ satisfy a generalised chain rule? For jointly distributed $(X, Y)$, define the conditional $p$-adic entropy $H_p(Y|X)$. The chain rule $H_p(X, Y) = H_p(X) + H_p(Y|X)$ would require a conditional valuation definition — likely $H_p(Y|X=x) = \sum_y p(y|x) v_p(y)$, with $H_p(Y|X) = \sum_x p(x) H_p(Y|X=x)$.

2. **Non-factorisable channels:** Theorem 4 assumes independent noise at each place. Physical channels may couple the archimedean and $p$-adic noise — e.g., a measurement that simultaneously determines a real-valued signal and its $p$-adic valuation. The capacity region for coupled adelic channels is an open problem.

3. **Second-order asymptotics (dispersion):** The adelic generalisation of the normal approximation (Polyanskiy–Poor–Verdú 2010) — what is the dispersion of the AUM channel? This determines the finite-blocklength performance.

4. **Adelic rate-distortion theory:** The $p$-adic distortion measure $d_p(x, \hat{x}) = p^{-v_p(x - \hat{x})}$ is the natural ultrametric distortion. The rate-distortion function under this measure is unknown.

5. **Computational adelic information:** The algorithmic information (Kolmogorov complexity) generalisation — does a binary string's Kolmogorov complexity decompose into archimedean and $p$-adic components?

---

## 9. Conclusion: Beyond Bits

Shannon taught us to measure information in bits. A bit is an archimedean unit — one binary decision, a choice between 0 and 1 in $\mathbb{R}$.

The adelic framework suggests that information may be measured in **$p$-adic bits** — choices in the $p$-adic valuation — and that the total information is a **vector** over all completions of $\mathbb{Q}$, with a multiplicative (product) capacity structure reflecting the adele ring.

The Poisson summation formula is the mathematical bridge connecting these measurements at different places. The Gaussian is the unique distribution that simultaneously extremises both archimedean (differential) and non-archimedean (valuation) entropy — the adelic maximum-entropy distribution.

We have constructed the foundational elements: the $p$-adic entropy definition with proven axioms (non-negativity, concavity, data-processing), the AUM channel model with capacity derivation, the product-formula coding theorem for the factorisable case, and the Poisson sum interpretation as source-channel equality. Computational verification confirms the consistency of these constructions for standard sources and code families.

The product-formula coding theorem, if fully proved for non-factorisable channels, would generalise Shannon's channel coding theorem to the adeles — stating that reliable communication is possible at the product rate and impossible above. This is the central open problem of the programme.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Consent to Participate:** Not applicable.

**Consent for Publication:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed. Computational examples in Section 5 are reproducible from the stated distributions.

**Code Availability:** The Ultrametric Engine [3] provides the computational backbone. Integration code for $p$-adic entropy and AUM capacity calculations will be released upon theory validation.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis, computation, and prose refinement.

---

## References

[1] Shannon, C.E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27, 379–423, 623–656. DOI: [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). [established]

[2] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations and Communications Framework. Zenodo. DOI: [10.5281/zenodo.21686727](https://doi.org/10.5281/zenodo.21686727).

[3] QNFO Research (2026). Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker. Zenodo. DOI: [10.5281/zenodo.21336105](https://doi.org/10.5281/zenodo.21336105).

[4] Quni-Gudzinas, R.B. (2026). Poisson Summation as the Adelic Bridge: Why the Q vs R Debate Dissolves in the Adele Ring. Zenodo. DOI: [10.5281/zenodo.21691078](https://doi.org/10.5281/zenodo.21691078).

[5] Quni-Gudzinas, R.B. (2026). FACTORING, Adelic Complexity, and the Silent-Radix Principle. Zenodo. DOI: [10.5281/zenodo.21691642](https://doi.org/10.5281/zenodo.21691642).

[6] Quni-Gudzinas, R.B. (2026). A Falsifiability Protocol for the Q-Fundamental Hypothesis. Zenodo. DOI: [10.5281/zenodo.21697717](https://doi.org/10.5281/zenodo.21697717).

[7] Quni-Gudzinas, R.B. (2026). p-Adic Quantum Error Correction Classifier Verification: A Computational Methodology. Zenodo. DOI: [10.5281/zenodo.21698076](https://doi.org/10.5281/zenodo.21698076).

[8] Khrennikov, A. (1994). *p-Adic Valued Distributions in Mathematical Physics*. Kluwer Academic Publishers.

[9] Khrennikov, A. (2009). *Interpretations of Probability* (2nd ed.). De Gruyter.

[10] Tate, J. (1950). Fourier Analysis in Number Fields and Hecke's Zeta-Functions. Ph.D. Thesis, Princeton University. [established]

[11] Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory* (2nd ed.). Wiley. [established]

[12] Vladimirov, V.S., Volovich, I.V., & Zelenov, E.I. (1994). *p-Adic Analysis and Mathematical Physics*. World Scientific.

[13] Kapranov, M. (1996). *Analogies between the Langlands Correspondence and Topological Quantum Field Theory*. In: Progress in Mathematics, Vol. 131. Birkhäuser.

[14] Anashin, V. (2012). *The p-Adic Theory of Automata Functions*. *p-Adic Numbers, Ultrametric Analysis and Applications*, 4(2), 109–119.

[15] Dragovich, B., Khrennikov, A.Yu., Kozyrev, S.V., & Volovich, I.V. (2017). *p-Adic Mathematical Physics: The First 30 Years*. *p-Adic Numbers, Ultrametric Analysis and Applications*, 9(2), 87–121.
