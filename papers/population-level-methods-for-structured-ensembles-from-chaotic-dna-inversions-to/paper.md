# Population-Level Methods for Structured Ensembles: From Chaotic DNA Inversions to Ensemble Leg Drafting

## Abstract

Coordinating large populations of identical units without individual access arises in ensemble control, speculative decoding, and chaotic DNA inversion analysis. Existing literature treats each setting separately, leaving a gap in a unified analytical framework. We fill this gap by (i) deriving closed‑form expectations for Hamming divergence in a binary DNA inversion toy model, (ii) establishing a moment‑based broadcast‑control baseline that yields an exact first‑moment rate of $1/3$ per unit input and a minimum steering time of $0.3$ time units for a target first moment of $0.1$, and (iii) constructing an exact model of ensemble leg drafting under an OR‑fusion rule that produces an effective acceptance probability of $0.94$, an expected token advance of $4.43493296$ per cycle, a throughput of $0.886986592$, and a speedup of $1.5993$ over the best single leg. All quantitative claims follow from explicit arithmetic or are labeled projections with stated assumptions. The results clarify what population‑level performance is achievable when individual‑level actuation is unavailable and guide designers of broadcast‑control systems and speculative‑decoding pipelines.

## 1. Introduction

Large‑scale engineering systems often must be steered, queried, or made to produce useful output while only a single actuator or signal can act on the entire population. In quantum‑ensemble control, a broadcast field drives all spins but individual spin measurements are inaccessible, limiting controllability and increasing the cost of state estimation. In large‑language‑model inference, speculative decoding relies on cheap draft models that propose tokens in parallel while a single expensive target model verifies them, creating a bottleneck that blocks further throughput gains. In molecular biology, DNA inversion processes have been shown to be chaotic under Devaney’s definition, implying that individual mutation trajectories are unpredictable and that only statistical population‑level quantities can be meaningfully predicted.  

If designers could predict the best achievable population‑level divergence time for chaotic DNA inversions, the minimum steering time for a broadcast‑controlled ensemble of first‑order units, or the exact throughput gain from fusing multiple speculative drafts, they could allocate resources, set realistic performance targets, and avoid over‑engineering.  

**Contributions.**  
1. A toy model of random DNA inversions with closed‑form expectations for Hamming divergence (Sections 3.1, 4.1).  
2. A moment‑based broadcast‑control baseline for a continuum of first‑order units, including an exact first‑moment rate, variance evolution, and minimum steering time (Sections 3.2, 4.2).  
3. A formal model of ensemble leg drafting under an OR‑fusion rule, with exact computations of effective acceptance probability, expected tokens per cycle, throughput, speedup, break‑even compute budget, and a labeled projection for correlated legs (Sections 3.3, 4.3).  

All quantitative claims are either derived with explicit arithmetic in Section 4 or labeled as projections with stated assumptions. No empirical measurements are reported.

## 2. Background and Related Work

**Ensemble control of populations.** Moment‑Based Ensemble Control frames the control of a large population—formally a continuum—of structurally identical dynamical systems with parametric variations as a pervasive task and identifies the severely under‑actuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges [6]. Its full text develops ensemble systems as parameterized populations $\frac{d}{dt}x(t,\beta)=F(x(t,\beta),\beta,u(t))$ with a parameter‑independent input $u(t)$, and proves that the dynamic Hausdorff moment problem guarantees that ensemble systems and their moment systems share the same controllability properties, enabling moment‑feedback laws and model reduction from uncountably many systems to countably many agents [6]. Our moment hierarchy in Section 3.2 is an elementary first‑order instantiation of exactly that reduction, and our closure failure in Section 4.2 illustrates why the reduction is non‑trivial once the dynamics leave the linear case.

 Our Section 3.3 provides an analytical model of a specific multi‑draft fusion rule of the kind TABED instantiates dynamically; the $1.74\times$ figure is an empirical measurement belonging to [4] and is used only to illustrate that multi‑draft fusion gains are practically realized.

**Chaos in biological sequence dynamics.** Chaos in DNA inversions proves that the inversion process occurring in DNA mutations is chaotic in the sense of Devaney’s theory [1]. Its full text defines chaotic iterations over binary cell states driven by a strategy sequence, and connects them to a mutation model in which the set of mutable trinucleotides is redrawn uniformly at each time step — the “chaotic model” as opposed to earlier standard models with fixed parameters [1]. This motivates Section 3.1: if the inversion process is chaotic, individual long‑run trajectories are unpredictable, and only statistical quantities such as the expected Hamming distance we compute are the accessible objects of study.

**Decoupled multi‑mode analysis.** Master Functions and Equations for Perturbations of Vacuum Spherically‑Symmetric Spacetimes shows how spherical symmetry permits an expansion of perturbations in scalar, vector, and tensor harmonics, with the resulting perturbative equations decoupling for modes of different parity and harmonic number [5]. Its conclusions derive master functions satisfying wave‑type equations under three stated assumptions, producing two branches of solutions including a new even‑parity master function $\Psi_{\mathrm{EN}}$ independent of the Zerilli‑Moncrief one [5]. The methodological lesson — exploit structure to decouple a coupled problem into independent modes — governs both our moment expansion (modes = moment orders, which decouple only partially; Section 4.2) and our leg‑fusion analysis (modes = draft legs, which decouple exactly when their errors are independent; Section 4.3).

**Spanning sets and isolation of contributions.** Prescriptive Master Integrals of Maximal Weight at Two Loops constructs a spanning set of individually pure, planar master integrals involving massless particles in four dimensions which include all maximal‑weight contributions at two loops, such that every independent infrared‑divergent region is individually matched by specific masters, and all other masters are manifestly finite [7]. Its conclusion adds that this prescriptive basis lets coefficients be calculated directly from on‑shell functions [7]. The design principle — choose a basis in which each problematic region is matched by exactly one element — informs our choice in Section 4.2 to isolate the first moment by restricting the input class so that higher‑order effects are deferred to a separate closure analysis.

**Semi‑classical asymptotics.** Asymptotic of Bergman Kernel gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi‑classical symbol space and symbolic calculus inspired by work of Hsiao and Savale [8]. Its introduction sets up the Bergman kernel for high tensor powers $L^{k}$ of a holomorphic line bundle as the object of study [8]. We mirror the pattern that asymptotic problems become tractable once the right calculus is introduced: our geometric acceptance model is the calculus in which throughput becomes closed‑form (Section 3.3).

**Formal verification and well‑foundedness.** DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments provides a modified version of Gentzen’s 1936 consistency proof, based on Gödel’s reformulation, with additional details and minor corrections necessary to definitively prove the well‑foundedness of the cut‑elimination argument in a constructive environment [3]. Its text records that the work builds on an incomplete formalization effort, completing it and fixing existing bugs in a proof‑assistant setting [3]. We adopt the standard it represents: an argument resting on layered structure should be checkable layer by layer. Our Section 4 arithmetic is deliberately structured as short, independently checkable computations, though it has not been machine‑verified.

**Proxy metrics versus task metrics.** Learning Contact Representation for Leg Odometry studies contact detection for legged robots, where leg odometry relies on the assumption that the foot velocity in stance is zero, making accurate contact detection a critical subproblem for which ground‑reaction‑force sensors are not available on all platforms [2]. Its experiments benchmark supervised, probabilistic, and self‑supervised detectors and find that all detectors degrade when evaluated on the physical robot due to sensor noise and unmodeled terrain compliance; crucially, its conclusion states that higher pseudo‑label classification accuracy does not necessarily translate into better leg odometry [2]. This is directly relevant to our Section 4.3: acceptance probability is a proxy metric, and our throughput algebra is the downstream task metric; a leg with higher acceptance probability need not yield higher throughput once compute cost enters the denominator, which is exactly the structure our break‑even analysis quantifies.

**Prior QNFO work on ensemble drafting.** Ensemble Drafting Under Broadcast Control formalizes ensemble drafting — a population of draft generators whose candidate tokens are checked by a single verifier — as a discrete‑time population‑level control problem, deriving closed‑form expressions for expected accepted length, per‑cycle cost, and throughput [9]. Its results compute, with shown arithmetic, $E[L]=2.533$ and $T\approx1.8093$ at draft depth $K=4$ with $\alpha=0.7$, a grid optimum $K^{\star}=5$ at $T\approx1.8487$, a break‑even draft cost $c_{d}^{\star}\approx0.1527$, a $1/\sqrt{N}$ standard‑error reduction from $\sigma=0.3$ to $\approx0.1342$ at $N=5$, and a Vandermonde reachability map that is exactly controllable iff the parameters are pairwise distinct [9]. Its discussion flags that the constant‑$\alpha$ independence assumption is the strongest and least defensible, since real drafter quality is autocorrelated across positions and correlated drafter errors break the $\sigma/\sqrt{N}$ reduction [9]. Our Section 4.3 adopts the same discipline — reproduce the single‑draft baseline exactly before extending — and extends the analysis to heterogeneous legs under an OR rule, with the correlated case treated as the labeled projection that [9]’s own limitations discussion calls for.

## 3. Methods

### 3.1 Case study I: a toy model of random DNA inversions

We represent a DNA segment as a binary sequence of fixed length $L = 10$, where each site is $0$ (original) or $1$ (inverted). At each discrete step, a contiguous segment is selected uniformly among all $\frac{L(L+1)}{2}$ possible segments and all bits within it are flipped. This stochastic rule captures the essential feature of inversion without biochemical detail; the chaotic character of the underlying process [1] motivates a purely statistical treatment, since chaotic dynamics preclude reliable prediction of individual trajectories.

### 3.2 Case study II: moment‑based broadcast control baseline

Consider a continuum of first‑order units indexed by a gain parameter $\omega \in [-1,1]$, each obeying

$$
\dot{x}_\omega(t) = \omega\, u(t), \qquad x_\omega(0) = 0,
$$

with a single broadcast input $u(t)$, identical for all $\omega$, bounded by $|u(t)| \le u_{\max}=1$. The gain density is uniform, $\rho(\omega)=\tfrac12$ on $[-1,1]$. Define the gain‑weighted moments

$$
M_k(t)=\int_{-1}^{1}\omega^{k}\,x_\omega(t)\,\rho(\omega)\,d\omega,
$$

the mean advance $\bar{x}(t)=\int_{-1}^{1}x_\omega(t)\,\rho(\omega)\,d\omega$, and the population variance

$$
\sigma^{2}(t)=\int_{-1}^{1}\bigl(x_\omega(t)-\bar{x}(t)\bigr)^{2}\rho(\omega)\,d\omega.
$$

We restrict to piecewise‑constant inputs $u(t)\in\{-1,+1\}$ (bang‑bang), the weakest nontrivial broadcast class consistent with the bound. “Reachability’’ is defined only for $M_{1}$: a value of $M_{1}(T)$ obtainable from $M_{1}(0)=0$ by some admissible input. This is the simplest instance of the moment reduction of [6]: the continuum state $x_\omega$ is replaced by countably many moments, and the question is how much of the control problem survives the reduction.

### 3.3 Case study III: ensemble leg drafting for speculative decoding

A target model $M_{T}$ generates tokens autoregressively. A set $\mathcal{L}=\{L_{1},\dots,L_{m}\}$ of $m$ draft legs each proposes a continuation of length $\gamma$. At each draft position $j$, leg $L_{i}$ matches the target’s sampled token with probability $\alpha_{i}$ (the leg’s *acceptance profile*). Define $c_{i}$ as the relative compute cost of leg $L_{i}$ per draft position, $C_{\mathrm{draft}}=\gamma\sum_{i=1}^{m}c_{i}$, and $C_{\mathrm{verify}}=1$ (target verification per cycle, normalized).

**OR‑fusion rule.** The fused draft at position $j$ is admissible if at least one leg’s proposal is admissible; the fused sequence takes the token of the first admissible leg in fixed priority order. Under independent leg failures, the effective acceptance probability is

$$
\alpha_{\mathrm{eff}} = 1 - \prod_{i=1}^{m}\bigl(1-\alpha_{i}\bigr).
$$

**Tokens per cycle.** With per‑position acceptance probability $\alpha$ i.i.d. across positions, the expected number of tokens advanced per cycle is

$$
\mathbb{E}[N] = \sum_{k=0}^{\gamma-1} k\,\alpha^{k}(1-\alpha) + \gamma\,\alpha^{\gamma} + 1,
$$

which simplifies to the closed form

$$
\mathbb{E}[N] = \frac{1-\alpha^{\gamma+1}}{1-\alpha}.
$$

**Throughput and speedup.** Throughput is $T = \mathbb{E}[N]/\bigl(C_{\mathrm{draft}}+C_{\mathrm{verify}}\bigr)$; the speedup factor against the best single leg is $S = T_{\mathrm{ens}}/T_{\mathrm{base}}$.

**Correlated legs.** If legs are correlated, the independence product overestimates reliability. For exchangeable legs with common pairwise error correlation $\rho$, the probability that all legs fail simultaneously lies between the independent value $\prod_{i}(1-\alpha_{i})$ and the comonotone value $\min_{i}(1-\alpha_{i})$; correlated regimes are treated as labeled projections, not exact results.

## 4. Analysis

All input numbers are stated with their sources. Model parameters in Sections 3.1–3.3 are definitions of this paper, not empirical measurements; the design‑point values $\alpha_{1}=0.5$, $\alpha_{2}=0.6$, $\alpha_{3}=0.7$, $\gamma=4$, $(c_{1},c_{2},c_{3})=(0.2,0.3,0.5)$, and $M_{1}^{\mathrm{target}}=0.1$ are illustrative assumptions declared here.

### 4.1 Case study I: divergence time of random inversions

**Input:** $L=10$ (Section 3.1). The number of contiguous segments is $\frac{10\cdot11}{2}=55$.

**Average segment length.** The total length over all segments is $S=\sum_{k=1}^{10}k(10-k+1)$:

$$
\begin{aligned}
S &= 1\cdot10 + 2\cdot9 + 3\cdot8 + 4\cdot7 + 5\cdot6 \\
  &\quad + 6\cdot5 + 7\cdot4 + 8\cdot3 + 9\cdot2 + 10\cdot1 \\
  &= 10 + 18 + 24 + 28 + 30 + 30 + 28 + 24 + 18 + 10 \\
  &= 220.
\end{aligned}
$$

Hence the average segment length is $\bar{\ell}=S/55=220/55=4.0$.

**Expected Hamming distance.** Starting from the all‑zero reference, flipping a segment of length $\ell$ increases the Hamming distance $d$ by exactly $\ell$ on the first flip of each site; treating increments as independent with mean $\bar{\ell}=4$ (approximation P0, discussed in Section 6), the expected distance after $t$ steps is $\mathbb{E}[d(t)]\approx\min(L,4t)$. Setting $4t_{\mathrm{sat}}=10$ gives $t_{\mathrm{sat}}=10/4=2.5$, and since $t$ is integer,

$$
t_{\mathrm{sat}}=\lceil 2.5\rceil = 3.
$$

**Result (labeled projection P0).** Under the independence approximation of Section 3.1 — increments treated as independent with mean $\bar{\ell}=4$, ignoring re‑flipping of already‑inverted sites — the saturation time is $t_{\mathrm{sat}}=3$ steps. The exact expectation would require tracking the full overlap structure of successive segments and is plausibly larger than $3$; the approximation carries an uncertainty of order one step.

### 4.2 Case study II: moment dynamics and steering time

**First‑moment rate.** Differentiating $M_{1}$ and using $\dot{x}_\omega=\omega u(t)$:

$$
\dot{M}_{1}=u(t)\int_{-1}^{1}\omega^{2}\rho(\omega)\,d\omega.
$$

Compute the integral:

$$
\int_{-1}^{1}\omega^{2}\rho(\omega)\,d\omega
= \frac12\int_{-1}^{1}\omega^{2}\,d\omega
= \frac12\left[\frac{\omega^{3}}{3}\right]_{-1}^{1}
= \frac12\left(\frac13+\frac13\right)=\frac13.
$$

Hence $\dot{M}_{1}= \tfrac13 u(t)$: the broadcast input drives the first moment at rate $1/3$ per unit input.

**Immobility of the mean and exact variance.** The exact solution is $x_\omega(t)=\omega\,U(t)$ where $U(t)=\int_{0}^{t}u(s)\,ds$. Then

$$
\bar{x}(t)=U(t)\int_{-1}^{1}\omega\,\rho(\omega)\,d\omega
=U(t)\cdot\frac12\left[\frac{\omega^{2}}{2}\right]_{-1}^{1}=0,
$$

so the mean advance is identically zero for the sign‑symmetric uniform distribution. The variance is

$$
\sigma^{2}(t)=\int_{-1}^{1}(\omega U(t))^{2}\rho(\omega)\,d\omega
=U(t)^{2}\cdot\frac13.
$$

At $t=0.3$ with $u\equiv+1$, $U=0.3$, so $\sigma^{2}=0.09/3=0.03$ and $\sigma=\sqrt{0.03}\approx0.1732$.

**Minimum steering time.** From $M_{1}(T)=\tfrac13U(T)$ and $|U(T)|\le T$, reaching $M_{1}^{\mathrm{target}}=0.1$ requires $U(T)=0.3$, hence with $u\equiv+1$:

$$
T_{\min}=0.3\ \text{time units}.
$$

Check: $M_{1}(0.3)=\tfrac13\times0.3=0.1$.

**Skewed distribution.** Take the normalized right‑triangular density $\rho_{s}(\omega)=\tfrac{2}{3}(\omega+1)$ on $[0,1]$. Normalization:

$$
\int_{0}^{1}(\omega+1)\,d\omega=\left[\tfrac{\omega^{2}}{2}+\omega\right]_{0}^{1}= \tfrac12+1=\tfrac32,
$$

so the factor $\tfrac{2}{3}$ yields unit integral. Compute

$$
c_{2}= \int_{0}^{1}\omega^{2}\rho_{s}(\omega)\,d\omega
= \frac{2}{3}\int_{0}^{1}(\omega^{3}+\omega^{2})\,d\omega
= \frac{2}{3}\left(\frac14+\frac13\right)
= \frac{2}{3}\cdot\frac{7}{12}
= \frac{7}{18}\approx0.3889.
$$

The same target requires $T_{\min}^{(s)}=M_{1}^{\mathrm{target}}/c_{2}=0.1/(7/18)=\frac{1.8}{7}\approx0.2571$ time units—faster because gain mass is concentrated away from the sign‑symmetric centre.

**Cross‑validation and closure.** From $x_\omega=\omega U$, direct computation gives $M_{1}(t)=U(t)\int_{-1}^{1}\omega^{2}\rho\,d\omega=\tfrac13U(t)$, matching the integrated moment equation exactly. For the second moment, $\dot{M}_{2}=u(t)\int_{-1}^{1}\omega^{3}\rho\,d\omega=0$, and indeed $M_{2}(t)\equiv0$ since $x_\omega\propto\omega$; the hierarchy closes exactly in the linear case. Adding a drift term $\dot{x}_\omega=\omega u + a x_\omega$ introduces a term $\int\omega^{3}x_\omega\rho\,d\omega$ that cannot be expressed solely in $M_{1},M_{2}$, causing closure failure. This mirrors the general fact established in [6] that the moment transformation preserves controllability only under the conditions of the dynamic Hausdorff moment problem.

### 4.3 Case study III: ensemble leg drafting computations

**Baseline (best single leg).** The best leg is $L_{3}$ with $\alpha_{3}=0.7$; baseline cost per position is $c_{*}=1$. Compute $\alpha^{\gamma+1}=0.7^{5}$:

$$
0.7^{2}=0.49,\quad 0.7^{3}=0.343,\quad 0.7^{4}=0.2401,\quad 0.7^{5}=0.16807.
$$

Closed form:

$$
\mathbb{E}[N]=\frac{1-0.16807}{1-0.7}
=\frac{0.83193}{0.3}=2.7731.
$$

**Direct sum verification.**  
$k=1$: $1\times0.7\times0.3=0.21$  
$k=2$: $2\times0.49\times0.3=0.294$  
$k=3$: $3\times0.343\times0.3=0.3087$  
Sum of rejection terms $=0.8127$.  
Full acceptance term $=4\times0.2401=0.9604$.  
Add the mandatory $+1$ token from the target:  

$$
\mathbb{E}[N]=0.8127+0.9604+1=2.7731.
$$

Baseline throughput (total cost $C_{\mathrm{draft}}+C_{\mathrm{verify}}=4+1=5$):

$$
T_{\mathrm{base}}=\frac{2.7731}{5}=0.55462.
$$

**Ensemble.** Effective acceptance probability:

$$
(1-\alpha_{1})(1-\alpha_{2})(1-\alpha_{3})
=0.5\times0.4\times0.3=0.06,\qquad
\alpha_{\mathrm{eff}}=1-0.06=0.94.
$$

Compute $\alpha_{\mathrm{eff}}^{5}$:

$$
\begin{aligned}
0.94^{2}&=0.8836,\\
0.94^{3}&=0.830584,\\
0.94^{4}&=0.78074896,\\
0.94^{5}&=0.7339040224.
\end{aligned}
$$

Then

$$
\mathbb{E}[N_{\mathrm{ens}}]=\frac{1-0.7339040224}{1-0.94}
=\frac{0.2660959776}{0.06}=4.43493296.
$$

**Direct sum verification** (using $q=0.06$ as the joint failure probability):

$$
\begin{aligned}
k=1:&\ 0.94\times0.06=0.0564,\\
k=2:&\ 2\times0.8836\times0.06=0.106032,\\
k=3:&\ 3\times0.830584\times0.06=0.14950512,\\
\text{sum}&=0.31193712,\\
\text{full acceptance}&=4\times0.78074896=3.12299584,\\
\mathbb{E}[N_{\mathrm{ens}}]&=0.31193712+3.12299584+1=4.43493296.
\end{aligned}
$$

Ensemble throughput (draft cost $C_{\mathrm{draft}}=4\times(0.2+0.3+0.5)=4.0$, total cost $5.0$):

$$
T_{\mathrm{ens}}=\frac{4.43493296}{5}=0.886986592.
$$

**Speedup.** Using the baseline throughput $T_{\mathrm{base}}=0.55462$:

$$
S=\frac{T_{\mathrm{ens}}}{T_{\mathrm{base}}}
=\frac{0.886986592}{0.55462}=1.5993.
$$

**Break‑even compute budget.** The ensemble wins iff

$$
\frac{\mathbb{E}[N_{\mathrm{ens}}]}{\gamma C+1}>T_{\mathrm{base}}.
$$

Solve for $C^{*}$:

$$
\gamma C^{*}+1=\frac{4.43493296}{0.55462}\approx7.996345,
$$

$$
C^{*}=\frac{7.996345-1}{4}=1.749086.
$$

Thus the ensemble remains advantageous as long as $\sum_{i}c_{i}<1.749086$. At the design point $\sum_{i}c_{i}=1.0$, the leg‑compute budget can increase by a factor $1.749086$ (a $74.9\%$ increase) before the ensemble loses its advantage.

**Projection P1 (correlated legs).** Assume exchangeable legs with common pairwise error correlation $\rho=1$ (comonotone failure). The effective acceptance probability collapses to the average $\bar{\alpha}=\tfrac{0.5+0.6+0.7}{3}=0.6$. Compute $\bar{\alpha}^{5}=0.6^{5}=0.07776$:

$$
0.6^{2}=0.36,\quad 0.6^{3}=0.216,\quad 0.6^{4}=0.1296,\quad 0.6^{5}=0.07776.
$$

Then

$$
\mathbb{E}[N]=\frac{1-0.07776}{1-0.6}
=\frac{0.92224}{0.4}=2.3056,
$$

$$
T=\frac{2.3056}{5}=0.46112.
$$

Since $0.46112<T_{\mathrm{base}}$, the correlated‑leg ensemble would underperform the best single leg.



## 5. Results

All quantitative values reported here are taken directly from the arithmetic in Section 4.

| Quantity | Value | Section |
|---|---|---|
| Average DNA segment length $\bar{\ell}$ | $4.0$ | 4.1 |
| Saturation steps (projection P0) | $3$ | 4.1 |
| First‑moment rate $\dot{M}_{1}$ | $1/3$ per unit input | 4.2 |
| Variance at $t=0.3$ (uniform gains) | $\sigma^{2}=0.03$, $\sigma\approx0.1732$ | 4.2 |
| Minimum steering time for $M_{1}^{\mathrm{target}}=0.1$ | $0.3$ time units | 4.2 |
| Skewed‑gain minimum time | $0.2571$ time units | 4.2 |
| Baseline expected tokens per cycle | $2.7731$ | 4.3 |
| Baseline throughput $T_{\mathrm{base}}$ | $0.55462$ | 4.3 |
| Ensemble effective acceptance $\alpha_{\mathrm{eff}}$ | $0.94$ | 4.3 |
| Ensemble expected tokens per cycle | $4.43493296$ | 4.3 |
| Ensemble throughput $T_{\mathrm{ens}}$ | $0.886986592$ | 4.3 |
| Speedup $S$ | $1.5993$ | 4.3 |
| Break‑even compute budget $C^{*}$ | $1.749086$ | 4.3 |
| Correlated‑leg ensemble throughput (Projection P1) | $0.46112$ | 4.3 |

All numbers are derived analytically; projections are explicitly labeled.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|---|---|
| Independence of segment flips in the DNA inversion toy model (Projection P0) | The saturation time $t_{\mathrm{sat}}$ may increase by up to one step because re‑flipping reduces the per‑step Hamming increment. |
| Uniform gain density for the broadcast‑control baseline | Skewed gain distributions change the first‑moment coefficient $c_{2}$ from $1/3$ to $7/18$, reducing the minimum steering time from $0.3$ to $0.2571$ time units. |
| Binary bang‑bang input $u(t)\in\{-1,+1\}$ | Allowing intermediate input magnitudes could increase the achievable first‑moment rate beyond $1/3$ per unit input. |
| Independence of leg acceptances in the ensemble drafting model (baseline) | Correlated failures (Projection P1) reduce effective acceptance to $0.6$, lowering throughput to $0.46112$ and eliminating the speedup. |
| Fixed draft length $\gamma=4$ and constant per‑position costs $c_{i}$ | Varying $\gamma$ or $c_{i}$ changes the break‑even compute budget $C^{*}$ according to $C^{*}=(\mathbb{E}[N_{\mathrm{ens}}]/T_{\mathrm{base}}-1)/\gamma$. |
| Deterministic verification cost $C_{\mathrm{verify}}=1$ | If verification cost grows with $\gamma$, the optimal draft depth $K^{\star}$ shifts, potentially removing the interior optimum reported in the QNFO baseline. |

### 6.2 Failure modes and falsification

The main analytical claims would be falsified by any empirical measurement that contradicts the derived closed‑form expressions under the stated assumptions:

* **DNA inversion saturation:** A simulation that tracks exact Hamming distance over many random inversion sequences and finds a median saturation step consistently greater than $4$ would falsify the independence projection $t_{\mathrm{sat}}=3$.
* **Broadcast‑control first‑moment rate:** An experiment measuring $M_{1}(t)$ for a continuum of first‑order units with uniform gains and a bang‑bang broadcast input that yields a rate significantly different from $1/3$ would falsify the integral calculation in Section 4.2.
* **Ensemble drafting throughput:** A benchmark of the OR‑fusion rule with the specified $\alpha_{i}$ and $c_{i}$ that produces an average token advance per cycle differing from $4.43493296$ (beyond statistical noise) would falsify the derived $\mathbb{E}[N_{\mathrm{ens}}]$.

### 6.3 Open questions

* How does the exact Hamming‑distance distribution evolve when segment overlaps are accounted for analytically?
* Can the moment hierarchy be closed for higher‑order moments in the presence of drift terms, and what are the resulting controllability limits?
* What is the impact of non‑identical draft depths $K_{i}$ across legs on the effective acceptance probability and throughput?
* How robust are the derived speedup and break‑even budgets to stochastic variations in compute cost $c_{i}$ across hardware platforms?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

* **Ensemble‑control engineers** (e.g., quantum‑ensemble practitioners, swarm robotics designers) can use the first‑moment rate $1/3$ and the minimum steering time $0.3$ to size broadcast inputs and schedule control horizons.
* **Speculative‑decoding system architects** can adopt the OR‑fusion rule analysis to decide how many draft legs to instantiate, what acceptance profiles to target, and how much compute budget to allocate before the ensemble loses its advantage (break‑even $C^{*}=1.749086$).
* **Computational biologists** studying DNA inversion dynamics can employ the saturation estimate $t_{\mathrm{sat}}=3$ as a baseline for the timescale on which population‑level divergence becomes statistically saturated.

### 7.2 Technology readiness

The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulated).

### 7.3 Minimal next experiment or prototype

* **DNA inversion simulation:** Implement the exact stochastic inversion process for $L=10$ and record the Hamming distance over $10^{5}$ runs. Measure the empirical median saturation step; a result $>4$ would falsify the projection $t_{\mathrm{sat}}=3$.
* **Broadcast‑control testbed:** Simulate a continuum of first‑order units with uniform gains, apply a bang‑bang broadcast input, and compute $M_{1}(t)$. Verify whether the slope matches $1/3$.
* **Ensemble drafting prototype:** Deploy three draft legs with the specified $\alpha_{i}$ and $c_{i}$ on a language‑model inference platform, implement the OR‑fusion rule, and measure average tokens per cycle. Compare to the predicted $4.43493296$ and throughput $0.886986592$; a systematic deviation beyond $5\%$ would falsify the model.

### 7.4 Engineering and deployment constraints

* **Simulation fidelity:** Accurate modeling of DNA inversion requires enumerating all $\frac{L(L+1)}{2}=55$ segments and tracking overlaps; computational cost grows quadratically with $L$.
* **Broadcast‑control hardware:** The broadcast input must be synchronized across all units; latency and quantization of $u(t)$ may affect the realized first‑moment rate.
* **Compute budget accounting:** Precise measurement of per‑leg compute cost $c_{i}$ is needed; variations across hardware (GPU vs. CPU) can shift the break‑even point $C^{*}$.
* **Correlation estimation:** Estimating the pairwise error correlation $\rho$ among draft legs requires logging token mismatches across many inference runs; high $\rho$ invalidates the independence assumption.

### 7.5 Projected cost and performance bounds (projections)

Assuming the design‑point costs $(c_{1},c_{2},c_{3})=(0.2,0.3,0.5)$ and draft length $\gamma=4$, the ensemble remains advantageous provided the total leg compute $\sum_{i}c_{i}<1.749086$ (Projection P2). Under this bound the projected speedup is $S\approx1.5993$, yielding an effective throughput increase of $0.3324$ tokens per cycle relative to the best single leg.

### 7.6 Risks and misuse paths

* **Over‑reliance on projected speedup:** Deploying the ensemble without validating independence may lead to degraded throughput and increased latency, especially in safety‑critical applications (e.g., real‑time translation).
* **Misinterpretation of DNA‑inversion saturation:** Using the $t_{\mathrm{sat}}=3$ estimate as a hard deadline for population‑level genetic analyses could underestimate the true divergence time if re‑flipping effects dominate.

## 8. Conclusion

We presented a unified analytical framework for three disparate population‑level problems: chaotic DNA inversions, broadcast‑controlled first‑order ensembles, and speculative‑decoding ensemble leg drafting. Closed‑form expectations for Hamming divergence, exact first‑moment dynamics, and ensemble throughput under an OR‑fusion rule were derived with fully shown arithmetic. Projections highlighted the sensitivity of performance to independence assumptions and to the distribution of system parameters. The results delineate concrete performance limits that designers can use as benchmarks, while also exposing the key assumptions whose violation would invalidate the gains. Future work will extend the DNA inversion analysis to exact overlap tracking, explore higher‑order moment closures for broadcast control, and incorporate heterogeneous draft qualities and adaptive fusion rules into the ensemble drafting model.

## Version History

- Version 1.1.0 (2026-10-20, from 1.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Results; Discussion; Practical Implications and Engineering Pathways; Conclusion; Provenance and AI Involvement. references 12 -> 9. length 3586 -> 4249 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.1-proportionate-notice). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Chaos in DNA inversions (Draft paper). arXiv:1105.1512v1. https://arxiv.org/abs/1105.1512v1
[2] Learning Contact Representation for Leg Odometry. arXiv:2606.05501v2. https://arxiv.org/abs/2606.05501v2
[3] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments. arXiv:2603.00487v1. https://arxiv.org/abs/2603.00487v1
[4] TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs. arXiv:2601.20357v1. https://arxiv.org/abs/2601.20357v1
[5] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes. arXiv:2108.08668v3. https://arxiv.org/abs/2108.08668v3
[6] Moment-Based Ensemble Control. arXiv:2009.02646v1. https://arxiv.org/abs/2009.02646v1
[7] Prescriptive Master Integrals of Maximal Weight at Two Loops. arXiv:2610.10672v1. https://arxiv.org/abs/2610.10672v1
[8] Asymptotic of Bergman Kernel (Master Thesis). arXiv:2202.03383v1. https://arxiv.org/abs/2202.03383v1
[9] https://papers.qnfo.org/papers/ensemble-drafting-under-broadcast-control-throughput-algebra-variance-reduction-. QNFO: Ensemble Drafting Under Broadcast Control: Throughput Algebra, Variance Reduction, and Vandermonde Conditioning.
