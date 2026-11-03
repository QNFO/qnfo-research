# Stress-Induced Switching from Fibonacci to Lucas Phyllotaxis: A Quantitative Threshold Model

## Abstract

Plants that develop spiral leaf or floret arrangements predominantly exhibit Fibonacci divergence angles near $137.5^\circ$, yet agronomic guidelines treat phyllotaxis as a static trait, so growers and breeders cannot anticipate the pattern changes observed under water or nutrient stress. Existing analytical models fix the golden angle and provide no criterion for when a stand will depart from it. We propose a stress-dependent threshold model in which a normalized stress parameter $\sigma$ interpolates between a Fibonacci-weighted and a Lucas-weighted contribution to the primordium-packing problem, drawing on algebraic identities that link the two sequences. Equating the weighted contributions at sequence index $n=5$ yields a critical stress $\sigma_c = F_5/(F_5+L_5) = 5/16 = 0.3125$; recomputing at $n=6$ shifts the threshold by only $1.54\%$. The model predicts an abrupt switch of the divergence angle from $\theta_F = 360^\circ/\varphi^2 \approx 137.508^\circ$ to a Lucas-related angle $\theta_L = 360^\circ/(\varphi+2) \approx 99.506^\circ$, a relative angular loss $R = (\theta_L-\theta_F)/\theta_F \approx -0.2764$, that is, a $27.6\%$ reduction in divergence angle. If the threshold holds, irrigation and fertilisation schedules could be set to keep a crop below $\sigma_c$, preserving golden-angle packing, and the index $R$ gives breeders a single metric for selecting stress-tolerant genotypes.

## 1. Introduction

Crop scientists and horticultural engineers face a concrete problem: if water-deficit or nutrient-poor conditions can trigger a sudden alteration of the leaf-spacing pattern, as the model developed here assumes, then canopy light interception and with it grain or flower yield would change in a way current guidelines cannot anticipate. Agronomic guidelines treat phyllotaxis as a fixed trait, so they cannot prescribe irrigation or fertilisation strategies that prevent a detrimental pattern switch; whether such switches occur under stress is precisely the premise the proposed experiment of Section 7.3 would test. If a quantitative stress threshold that triggers a transition from the ubiquitous Fibonacci arrangement to a Lucas-type arrangement were known, decision-makers could adjust resource inputs to hold the plant below that threshold and preserve the golden-angle architecture, the configuration that minimizes overlap of successive primordia and thereby maximizes packing efficiency and photosynthetic exposure.

The practical value of such a threshold is twofold. First, a predictable, stress-linked phyllotactic switch would enable precision-agriculture protocols that maintain the golden-angle architecture by construction rather than by observation. Second, a scalar **phyllotactic resilience index** $R$ that quantifies the relative loss of angular spacing when a switch occurs would give breeding programs a single selection metric for stress-tolerant genotypes, replacing qualitative descriptions of pattern change.

This paper constructs the minimal analytical model needed to state such a threshold and computes it in closed form. The model couples a normalized stress scalar to the relative weight of Fibonacci and Lucas contributions to the packing problem, and it yields an explicit critical stress above which the optimal divergence angle moves from the golden angle to a Lucas-related angle.

**Contributions.**
- **C1.** A stress-dependent weighted divergence-angle formula that couples Fibonacci and Lucas sequences, built on the identity $(n-1)F_n=\sum_{k=1}^{n-1}L_k F_{n-k}$ (Section 3).
- **C2.** Explicit computation of a critical stress threshold $\sigma_c = 5/16 = 0.3125$ from the fifth terms of the two sequences, with a robustness check at $n=6$ showing a $1.54\%$ shift (Section 4).
- **C3.** Definition and calculation of a phyllotactic resilience index $R \approx -0.2764$ that measures the relative angular loss on switching (Section 4).
- **C4.** Falsification criteria, a limitations analysis, and a minimal experimental design that would test or refute the model (Sections 6–7).

The switching mechanism may also matter to adjacent problems: the design of biomimetic spiral packings in engineering, and mathematical-biology studies of bifurcations in discrete pattern-forming systems, both of which face the same question of when a small parameter change flips a packing optimum between two candidate lattices.

## 2. Background and Related Work

The model rests on algebraic and combinatorial results that connect the Fibonacci sequence $F_n$ and the Lucas sequence $L_n$. Eight works supply the specific identities and interpretations used below.

**The Fibonacci–Lucas convolution identity.** [1] proves, for every integer $n \ge 2$,

$$(n-1)F_n=\sum_{k=1}^{n-1}L_k\,F_{n-k},$$

so that a weighted sum of Lucas numbers reproduces a scaled Fibonacci number exactly. This identity is the algebraic core of the present model: it justifies treating the two sequences as interchangeable weight sources, and Section 4 verifies it by direct arithmetic at $n=5$ and $n=6$ before any stress scaling is applied.

**Rational-indexed Fibonacci numbers.** [2] establishes that for a rational index $X=p/q$ the rational-indexed Fibonacci number $F_X$ can differ from the classical $F_n$, and that when the index has continued-fraction form $[3;n_1]$ with $n_0=3$ and $k=1$, the codenominator function $F([3;n_1])$ equals a Lucas number. This supplies a number-theoretic precedent for the central move of our model: an external parameter (there, a rational index; here, a stress scalar) can shift a Fibonacci-determined quantity onto a Lucas-determined one. We use the same continued-fraction condition, under which the codenominator function takes Lucas values, to motivate the Lucas-related angle $\theta_L$ adopted in Section 3.

**Polynomial derivations.** [3] studies derivations on the polynomial algebras generated by $F_n(x)$ and $L_n(x)$ and shows that any kernel element of such a derivation yields an identity linking the two families. This algebraic flexibility supports the construction of a stress-dependent linear combination of the two sequences: the families are not independent algebras but deformations of one another, which is precisely the relation our weighting parameter $\sigma$ exploits.

**Lucas numbers in optimal-move problems.** [4] presents a variant of the Tower of Hanoi whose optimal move count follows the Lucas sequence. The result demonstrates that Lucas numbers arise naturally as optima of packing-style combinatorial problems once the move rules are altered. This is the combinatorial analogue of our hypothesis that altered environmental constraints shift the primordium-packing optimum from a Fibonacci-determined angle to a Lucas-determined one.

**Squares of Fibonacci numbers.** [5] proves that the number of tilings of an $n$-board with half-squares and fence tiles equals $F_{n+1}^2$. This combinatorial interpretation ties the magnitude of a Fibonacci number to a count of stable configurations, which motivates reading a reduction of the Fibonacci weight under stress as a reduction in the number of stable packing configurations available to the meristem.

**A weighted Lucas sum.** [6] proves the identity

$$\sum_{k=0}^{n}2^{k}L_k=2^{n+1}F_{n+1},$$

a concrete weighted sum in which the Lucas terms carry geometrically growing weights yet the total collapses to a scaled Fibonacci term. This shows that weighted mixtures of the two sequences can be exactly re-balanced, supporting the use of a single scalar $\sigma$ to move between Fibonacci-dominated and Lucas-dominated regimes.

**Quadratic reduction.** [7] places both sequences inside a generic Lucas polynomial $P_m(t,d)$ satisfying a quadratic relation, with the reduction

$$x^{m}=P_m(t,d)\,x-d\,P_{m-1}(t,d).$$

This framework treats the recurrence parameters as deformable, which is the algebraic licence for our treatment of stress as a parameter $t$ modifying the underlying relation rather than as an external perturbation bolted onto a fixed recurrence.

**Wythoff representations.** [8] proves that the number of representations of an integer as a sum of a lower and an upper Wythoff number equals a Lucas number under stated conditions, and identifies Lucas numbers as the unique integers $n+1$ admitting exactly two such representations. Lucas numbers therefore encode threshold and uniqueness phenomena in discrete combinatorics, paralleling the unique critical stress $\sigma_c$ that our model assigns to the Fibonacci-to-Lucas transition.

Together these eight results provide the identities, the deformation frameworks, and the combinatorial precedents from which a stress-dependent phyllotactic model can be assembled without new number theory.

## 3. Methods

### 3.1 Model overview

We model the divergence angle $\theta$ of successive primordia as a weighted average of two canonical angles:

$$\theta(\sigma)= (1-\sigma)\,\theta_F + \sigma\,\theta_L, \tag{1}$$

where $\sigma \in [0,1]$ is a normalized stress variable ($\sigma = 0$ for optimal conditions, $\sigma = 1$ for extreme stress), $\theta_F = 360^\circ/\varphi^2$ is the golden angle with $\varphi = (1+\sqrt{5})/2$, and $\theta_L = 360^\circ/(\varphi+2)$ is a Lucas-related angle. The definition $\theta_L = 360^\circ/(\varphi+2)$ is adopted under the convention that the Lucas angle is generated by the same geometric construction as the golden angle with the denominator shifted from $\varphi^2$ to $\varphi+2$, the shift being motivated by the continued-fraction condition of [2] under which a rational-indexed Fibonacci number coincides with a Lucas number. An alternative definition based on the ratio $\psi = L_5/F_5 = 11/5$ was also considered and rejected: it yields $\theta = 360^\circ(1-1/\psi) = 360^\circ \cdot 6/11 \approx 196.36^\circ$, which lies outside the range of divergence angles observed in spiral phyllotaxis, whereas $\theta_L = 360^\circ/(\varphi+2) \approx 99.5^\circ$ does not.

### 3.2 Stress-weighted sequence

To connect $\sigma$ with the underlying integer sequences, we define a stress-weighted term

$$W_n(\sigma)= (1-\sigma)F_n + \sigma L_n, \tag{2}$$

where $F_n$ and $L_n$ are the $n$-th Fibonacci and Lucas numbers. The weighting is linear by assumption; Section 6 lists this as the assumption to which the results are most sensitive. The weighted term is a heuristic bridge between the stress scalar and the sequence algebra: it is constructed so that $\sigma=0$ recovers the pure Fibonacci weight and $\sigma=1$ the pure Lucas weight, in the spirit of the exactly re-balanced weighted sums proved in [6].

### 3.3 Critical stress: convention choice

Two parameterizations of the stress threshold were considered in the construction of this model. The first defines the threshold as the stress at which the weighted contributions of the two sequences are equal, $(1-\sigma_c)F_n = \sigma_c L_n$; the second defines it as the stress at which the interpolated angle $\theta(\sigma)$ of Eq. (1) passes the midpoint between $\theta_F$ and $\theta_L$. We adopt the first under the convention that the switch is governed by the balance of the two sequence weights rather than by the angle interpolation, because the weight balance is what the sequence identities of Section 2 constrain directly. The chosen condition is recorded as

$$(1-\sigma_c)F_n = \sigma_c L_n. \tag{3}$$

The midpoint parameterization would give $\sigma_c = 1/2$ independent of the sequences, which discards the sequence information the model is built on; it is therefore rejected here and listed in Section 6 as a convention whose rejection the results depend on.

### 3.4 Resilience index

We define the **phyllotactic resilience index** as the relative change of the divergence angle when the system switches from the Fibonacci regime to the Lucas regime:

$$R = \frac{\theta_L - \theta_F}{\theta_F}. \tag{4}$$

A genotype or treatment whose stress response keeps $|\sigma - \sigma_c|$ large while $R$ is fixed by the model has, under this definition, no additional protection: $R$ measures the cost of a switch, not the probability of one. The probability of switching is governed by $\sigma_c$, and the two quantities together give breeders a two-axis description: how far the system sits from the threshold, and how much angular architecture is lost if the threshold is crossed.

## 4. Analysis

### 4.1 Sequence values and identity verification

All arithmetic below uses the standard indexing of [1]: $F_1 = 1$, $F_2 = 1$, $F_n = F_{n-1}+F_{n-2}$; $L_0 = 2$, $L_1 = 1$, $L_2 = 3$, $L_n = L_{n-1}+L_{n-2}$. The first six terms are:

$$F_1,\dots,F_6 = 1,\,1,\,2,\,3,\,5,\,8; \qquad L_1,\dots,L_6 = 1,\,3,\,4,\,7,\,11,\,18.$$

Before applying any stress weighting, we verify the convolution identity of [1] by direct arithmetic at the two indices used later.

**At $n=5$:**

$$\sum_{k=1}^{4}L_k F_{5-k} = L_1F_4 + L_2F_3 + L_3F_2 + L_4F_1 = (1)(3) + (3)(2) + (4)(1) + (7)(1) = 3+6+4+7 = 20,$$

and $(n-1)F_n = 4 \cdot 5 = 20$. The identity holds.

**At $n=6$:**

$$\sum_{k=1}^{5}L_k F_{6-k} = L_1F_5 + L_2F_4 + L_3F_3 + L_4F_2 + L_5F_1 = (1)(5) + (3)(3) + (4)(2) + (7)(1) + (11)(1) = 5+9+8+7+11 = 40,$$

and $(n-1)F_n = 5 \cdot 8 = 40$. The identity holds.

As a further check on the weighted-sum balancing that motivates the linear weighting of Eq. (2), we verify the identity of [6] at $n=2$:

$$\sum_{k=0}^{2}2^k L_k = 2^0 L_0 + 2^1 L_1 + 2^2 L_2 = (1)(2) + (2)(1) + (4)(3) = 2+2+12 = 16,$$

and $2^{n+1}F_{n+1} = 2^3 F_3 = 8 \cdot 2 = 16$. The identity holds.

### 4.2 Critical stress at $n=5$

Setting the two weighted contributions equal in Eq. (3) at $n=5$:

$$(1-\sigma_c)F_5 = \sigma_c L_5 \quad\Longrightarrow\quad (1-\sigma_c)(5) = \sigma_c(11).$$

Expanding: $5 - 5\sigma_c = 11\sigma_c$, so $5 = 16\sigma_c$, giving

$$\sigma_c(5) = \frac{F_5}{F_5+L_5} = \frac{5}{5+11} = \frac{5}{16} = 0.3125.$$

### 4.3 Critical stress at $n=6$ and robustness

At $n=6$:

$$\sigma_c(6) = \frac{F_6}{F_6+L_6} = \frac{8}{8+18} = \frac{8}{26} = \frac{4}{13} \approx 0.307692.$$

The relative shift between the two index choices is

$$\Delta = \frac{\sigma_c(5) - \sigma_c(6)}{\sigma_c(5)} = \frac{\frac{5}{16} - \frac{4}{13}}{\frac{5}{16}} = \frac{\frac{65 - 64}{208}}{\frac{5}{16}} = \frac{1}{208}\cdot\frac{16}{5} = \frac{16}{1040} = \frac{1}{65} \approx 0.0153846,$$

that is, a $1.54\%$ shift. The threshold is therefore nearly independent of the reference index over $n \in \{5,6\}$, because $F_n/(F_n+L_n)$ converges rapidly: as $n$ grows, $L_n/F_n \to \sqrt{5} \approx 2.236068$, so $\sigma_c(n) \to 1/(1+\sqrt{5}) \approx 0.309017$, between the two computed values.

### 4.4 The two divergence angles

With $\varphi = (1+\sqrt{5})/2 \approx 1.618034$:

$$\varphi^2 = \varphi + 1 \approx 2.618034, \qquad \theta_F = \frac{360^\circ}{\varphi^2} = \frac{360^\circ}{2.618034} \approx 137.5078^\circ.$$

$$\varphi + 2 \approx 3.618034, \qquad \theta_L = \frac{360^\circ}{\varphi+2} = \frac{360^\circ}{3.618034} \approx 99.5062^\circ.$$

Note that $\varphi + 2 = \varphi^2 + 1$, so the Lucas angle is the golden angle with one unit added to the denominator — a one-step shift in the continued-fraction denominator of the kind that [2] identifies, through the condition $n_0=3$, $k=1$, as the setting in which the codenominator function $F([3;n_1])$ takes Lucas values.

### 4.5 Resilience index

$$R = \frac{\theta_L - \theta_F}{\theta_F} = \frac{99.5062^\circ - 137.5078^\circ}{137.5078^\circ} = \frac{-38.0016^\circ}{137.5078^\circ} \approx -0.27636.$$

In closed form, since $\theta_L/\theta_F = \varphi^2/(\varphi+2)$:

$$R = \frac{\varphi^2}{\varphi+2} - 1 = \frac{\varphi^2 - \varphi - 2}{\varphi+2} = \frac{(\varphi+1) - \varphi - 2}{\varphi+2} = \frac{-1}{\varphi+2} \approx -0.276393.$$

The small difference between the decimal evaluation ($-0.27636$) and the closed form ($-0.276393$) is rounding in the degree values; the closed form $R = -1/(\varphi+2)$ is exact. We report $R \approx -0.2764$, a $27.6\%$ reduction in divergence angle on switching.

### 4.6 Transition sharpness

Because $\theta(\sigma)$ in Eq. (1) is a linear interpolation, the model as written produces a gradual drift of the divergence angle, not an abrupt switch. The abrupt-switch interpretation requires an additional assumption: that the meristem commits to whichever packing solution is locally optimal, so that the observed angle is

$$\theta_{\text{obs}}(\sigma) = \begin{cases} \theta_F, & \sigma < \sigma_c, \\ \theta_L, & \sigma \ge \sigma_c. \end{cases} \tag{5}$$

Under Eq. (5), the linear interpolation $\theta(\sigma)$ of Eq. (1) describes the underlying bias of the packing problem, while the observed angle jumps at $\sigma_c$. The angular jump magnitude is $|\theta_L - \theta_F| \approx 38.0^\circ$. This commitment assumption is the second-most sensitive assumption of the model, after linearity of the weighting; both are listed in Section 6.

## 5. Results

All numbers in this section are computed in Section 4 with the arithmetic shown there; no empirical measurement is reported.

**R1 (Critical stress).** The model yields a critical normalized stress $\sigma_c = F_5/(F_5+L_5) = 5/16 = 0.3125$ at the reference index $n=5$ (Section 4.2).

**R2 (Index robustness).** Recomputing at $n=6$ gives $\sigma_c = 4/13 \approx 0.307692$, a relative shift of $1/65 \approx 1.54\%$; the large-$n$ limit is $1/(1+\sqrt{5}) \approx 0.309017$ (Section 4.3). The threshold is insensitive to the reference index at the level of about $1.5\%$.

**R3 (Angle pair).** The Fibonacci-regime angle is $\theta_F = 360^\circ/\varphi^2 \approx 137.508^\circ$ and the Lucas-regime angle is $\theta_L = 360^\circ/(\varphi+2) \approx 99.506^\circ$ (Section 4.4).

**R4 (Resilience index).** The phyllotactic resilience index is $R = -1/(\varphi+2) \approx -0.2764$: crossing the threshold costs $27.6\%$ of the divergence angle (Section 4.5).

**R5 (Transition sharpness).** Under the commitment assumption of Eq. (5), the observed divergence angle jumps by $|\theta_L-\theta_F| \approx 38.0^\circ$ at $\sigma = \sigma_c$; without that assumption the model predicts a gradual drift governed by Eq. (1) (Section 4.6).

**R6 (Identity verification).** The convolution identity of [1] holds by direct arithmetic at $n=5$ (sum $= 20 = 4F_5$) and $n=6$ (sum $= 40 = 5F_6$), and the weighted identity of [6] holds at $n=2$ (sum $= 16 = 2^3F_3$), confirming the algebraic consistency of the weighting scheme (Section 4.1).

## 6. Discussion

### 6.1 What the model does and does not claim

The model is a phenomenological threshold construction, not a mechanism. It states that if a plant's packing problem can be represented by a scalar stress variable weighting Fibonacci and Lucas contributions linearly, then the switch occurs at $\sigma_c \approx 0.31$ and costs $27.6\%$ of the divergence angle. It does not derive $\sigma$ from water potential or nutrient flux, does not model the meristem dynamically, and does not establish that real meristems ever sit near the threshold. The connection to dynamical primordium-packing models is motivational, and it is the paper's own hypothesis, not a result derived here: if such models produce golden-angle packing from an energy minimum, a stress-dependent term could in principle deform that minimum, but no dynamical derivation is carried out in this paper.

### 6.2 Falsification criteria

The main result, $\sigma_c \approx 0.31$ with an abrupt $38.0^\circ$ angular jump, is falsified by any of the following observations:

1. **Continuous response without a threshold.** If divergence angles measured across a stress gradient vary smoothly with no jump near any fixed stress value, the commitment assumption of Eq. (5) fails and with it the threshold interpretation of $\sigma_c$.
2. **Threshold at a different location with index-dependence.** If experiments locate a switch but its stress position varies strongly with plant age or organ count (i.e., with the effective index $n$) by much more than the predicted $1.54\%$ between adjacent indices, the index-independent threshold claim fails.
3. **Switch to a non-Lucas angle.** If stressed plants switch to divergence angles other than $\approx 99.5^\circ$ (or its $360^\circ$-complement family), the identification of the second regime with the Lucas angle fails, regardless of whether a threshold exists.
4. **No switch at high stress.** If severely stressed plants retain $\theta_F \approx 137.5^\circ$, the premise that stress drives the switch at all is refuted.

### 6.3 Limitations

- **Linearity of the weighting (Eq. 2).** The weighting is linear by assumption; a nonlinear stress response would shift $\sigma_c$ by an amount not computed here. This is the assumption to which the results are most sensitive.
- **The definition of $\theta_L$.** The Lucas angle $360^\circ/(\varphi+2)$ is a convention adopted for geometric continuity with the golden-angle construction; the rejected alternative $\psi = L_5/F_5 = 11/5$ gives $\approx 196.36^\circ$, outside the observed spiral range. Other Lucas-related angles are conceivable, and the model's second regime is only as well-defined as this convention.
- **The commitment assumption (Eq. 5).** The abrupt switch requires that the meristem commit to a locally optimal packing; without it the model predicts gradual drift.
- **No mapping from $\sigma$ to measurable variables.** The model never connects $\sigma$ to water potential, nutrient concentration, or any agronomic measurement, so the numerical threshold cannot yet be converted into an irrigation prescription.
- **No empirical support.** The paper reports no measurement, simulation, or observation; every number is derived from the model's own assumptions. We assume, as a motivating premise not derived or tested here, that Fibonacci-type arrangements dominate in unstressed spiral phyllotaxis; no frequency figure for that dominance is available from this paper's sources.
- **Index choice.** The threshold is computed at $n=5$ and $n=6$ only; the claim of index-insensitivity rests on the analytic limit $\sigma_c \to 1/(1+\sqrt{5})$, not on computation across many indices.

### 6.4 What would strengthen the model

A dynamical derivation that obtains Eq. (3) from a primordium-packing energy with a stress-dependent term would convert the threshold from a definition into a prediction. A single well-controlled stress experiment locating the switch on a measured stress axis would fix the constant of proportionality between $\sigma$ and a physical variable, making R1 actionable.

## 7. Practical Implications and Engineering Pathways

### 7.1 Who would use the result and what changes

If the threshold model holds after empirical testing, three user groups face changed decisions:

- **Irrigation and fertigation managers.** The decision variable changes from "maintain plant health" to "maintain $\sigma < \sigma_c \approx 0.31$," which requires a calibrated mapping from soil moisture or nutrient concentration to $\sigma$. Until that mapping exists, the threshold is not actionable; the calibration is the missing engineering step.
- **Plant breeders.** The resilience index $R \approx -0.2764$ gives a single scalar for ranking genotypes by the angular cost of a stress-induced switch; a breeding program would select genotypes whose observed divergence angle remains at $\theta_F$ under stress levels that push susceptible genotypes past the threshold.
- **Researchers in pattern-forming systems.** The model supplies a concrete, falsifiable bifurcation criterion for discrete packing systems, of the kind studied in biomimetic spiral-structure design.

Where no user can yet be named — specifically, the conversion of $\sigma_c$ into an irrigation prescription — the work is foundational: it establishes the form of the criterion and the robustness of its numerical value, which any later calibration would inherit.

### 7.2 Readiness level

Against the NASA Technology Readiness Level definitions, this work is analytical research with no empirical validation and no peer review at the time of writing: it sits at **TRL 1–2** (basic principles observed and reported; concept formulated). No claim of hardware, greenhouse, or field readiness is made, and analytical work of this kind cannot exceed TRL 3 (proof of concept) without experimental evidence.

### 7.3 The smallest next test

The minimal de-risking experiment is a single-species stress-gradient study: a study would grow one spiral-phyllotaxis species under a stepped water-deficit gradient — we assume five to seven levels would span the presumed threshold region, an assumption about the design, not a derived number — measure each plant's divergence angle from sequential primordium positions, and measure a stress proxy (leaf water potential) on the same plants. The model is refuted if (i) the angle–stress curve shows no jump anywhere in the gradient, (ii) the jump, if present, is not to $\approx 99.5^\circ$ or its equivalents, or (iii) the jump position varies between replicate batches by more than a few percent of the stress range. A complementary purely computational step — adding a stress-dependent term to a dynamical primordium-packing simulation and checking whether the optimum angle bifurcates — would test the mechanism without any plant material.

### 7.4 Binding constraints

- **Measurement precision.** Resolving a $38.0^\circ$ angular jump requires divergence-angle measurement to a few degrees, which sequential-primordium imaging can achieve; the harder requirement is a stress proxy that is repeatable across plants, since $\sigma$ has no physical definition yet.
- **Biological variability.** Real meristems show noise in divergence angle; distinguishing a $27.6\%$ jump from noise requires within-treatment replication whose size is not derivable from this paper and is an open question.
- **Calibration data.** The mapping from water potential or nutrient flux to $\sigma$ requires a dataset that does not exist in this paper; it is the primary data constraint on any field use.
- **Regulation.** No regulatory constraint applies to observational phyllotaxis studies; constraints would arise only if the result were used to justify agronomic input changes, which is premature at TRL 1–2.

### 7.5 Order-of-magnitude bounds

No cost or field-performance figure is derivable from the model, and none is projected. The only quantitative performance bound the paper supports is the angular one already stated: a switch costs $27.6\%$ of the divergence angle ($38.0^\circ$ in absolute terms), and the threshold location is robust to index choice at the $1.54\%$ level. Any yield consequence of that angular change is an open question requiring canopy-level modeling not undertaken here.

### 7.6 Risks and misuse

The main misuse path is premature prescription: quoting "$\sigma_c = 0.3125$" as an irrigation trigger before the $\sigma$-to-physical-variable calibration exists would give the number a false operational meaning. A secondary risk is over-reading the resilience index: $R$ is a property of the model's angle convention, not a measured plant trait, and should not be used as a selection metric until the Lucas-angle convention is empirically confirmed as the actual second regime.

## 8. Conclusion

This paper constructed a minimal analytical model in which a normalized stress scalar interpolates between Fibonacci-weighted and Lucas-weighted contributions to the primordium-packing problem, built on the Fibonacci–Lucas convolution identity verified here by direct arithmetic at $n=5$ and $n=6$. Equating the two contributions yields a critical stress $\sigma_c = 5/16 = 0.3125$, robust to the reference index at the $1.54\%$ level and converging to $1/(1+\sqrt{5}) \approx 0.309$ for large indices. Crossing the threshold moves the divergence angle from $\theta_F \approx 137.508^\circ$ to $\theta_L \approx 99.506^\circ$, a loss quantified by the phyllotactic resilience index $R = -1/(\varphi+2) \approx -0.2764$. The model's value is as a falsifiable scaffold: it fixes the form of the threshold criterion, the size of the predicted angular jump ($38.0^\circ$), and the robustness of the threshold location, while leaving open the two questions on which its usefulness depends — the physical definition of $\sigma$ and the empirical existence of the switch. A single stress-gradient experiment or a stress-extended packing simulation would either supply both or refute the model, and the falsification criteria of Section 6.2 state exactly which observation does which.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.3). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 12 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Fibonacci Numbers and Their Lucas Coefficients. arXiv:2509.00070v1. https://arxiv.org/abs/2509.00070v1
[2] Inverses of Fibonacci and Lucas Numbers via Rational Indices. arXiv:2607.20754v1. https://arxiv.org/abs/2607.20754v1
[3] Derivations and identities for Fibonacci and Lucas polynomials. arXiv:1207.5891v2. https://arxiv.org/abs/1207.5891v2
[4] The Towers of Fibonacci, Lucas, Pell, and Jacobsthal. arXiv:2502.11045v2. https://arxiv.org/abs/2502.11045v2
[5] A new combinatorial interpretation of the Fibonacci numbers squared. arXiv:1907.06517v1. https://arxiv.org/abs/1907.06517v1
[6] Analogues of a Fibonacci-Lucas Identity. arXiv:1510.03159v3. https://arxiv.org/abs/1510.03159v3
[7] Quadratic Reduction and Classical Multiple-Index Fibonacci-Lucas Identities. arXiv:2603.19343v2. https://arxiv.org/abs/2603.19343v2
[8] Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words. arXiv:2610.04842v1. https://arxiv.org/abs/2610.04842v1
