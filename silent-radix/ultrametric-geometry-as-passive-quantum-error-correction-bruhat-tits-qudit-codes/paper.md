# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound

## Abstract

Active quantum error correction (QEC) dominates the overhead of scalable quantum processors, requiring repeated syndrome extraction, low-latency decoding, and large ancilla counts that inflate hardware cost and energy consumption. A passive alternative that eliminates measurement cycles would reduce system complexity and improve the feasibility of large-scale quantum advantage. The ultrametric geometry of the $p$-adic numbers satisfies the strong triangle inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$, which forces balls in the associated Bruhat–Tits tree $T_{p+1}$ to be either nested or disjoint. We ask whether this property can be formalized as a genuine quantum error-correcting code with provable distance thresholds and whether it can outperform active correction for realistic noise channels. We (i) define a ball code on $T_{p+1}$, prove a nesting lemma, and derive exact code parameters $n_t=1+(p+1)(p^{t}-1)/(p-1)$ and conditional distance $d=2t+1$; (ii) compute analytically the passive logical failure probability under independent depolarising noise with physical error rate $\varepsilon=10^{-3}$, obtaining $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, a suppression factor of $\approx100.2$ over an unencoded qudit; (iii) project a $\approx4.08$-fold advantage over an active distance-3 baseline when the same physical error rate and an additional measurement error $\varepsilon_m=\varepsilon$ are assumed. All quantitative results are derived step by step; limitations and falsification criteria are discussed.

## 1. Introduction

Scalable quantum computing is presently blocked by the overhead of active quantum error correction, which requires repeated syndrome extraction, low-latency decoding, and large ancilla resources. This overhead directly limits the size of computations that can be run on near-term hardware and inflates the thermodynamic cost of error-correction cycles [8]. If a hardware platform could store logical information in a structure that *passively* blocks error propagation, the need for active cycles would disappear, reducing both hardware complexity and energy consumption.

The non-Archimedean (ultrametric) geometry of the $p$-adic numbers provides such a structure. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality
$$\|x+y\|_p\le\max\bigl(\|x\|_p,\|y\|_p\bigr),$$
which implies that any two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has degree $p+1$. By placing qudits at the vertices and encoding a logical qudit into a ball $B_t(v_0)$, we obtain a geometry in which local errors cannot coherently add across distinct branches. Hecke operators, which average over the $p+1$ forward neighbours of each vertex, serve as a natural gate set that respects the tree locality.

In this work we formalize the above intuition, derive exact code parameters, and compute the passive logical failure probability under a standard depolarising noise model. We also compare the passive scheme to a conventional active distance-3 code under comparable noise assumptions. No simulation, measurement, or hardware experiment is performed or reported; every quantitative claim is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

**Contributions.**
- Lemma 1 (nesting/disjointness of equal-radius balls) and its proof (Section 4.1).
- Proposition 1 (correctability of all weight-$\le t$ error sets and conditional distance $d=2t+1$) (Section 4.2).
- Exact code-size formula $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ (Section 4.1).
- Analytic passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, $\varepsilon=10^{-3}$ (Section 4.3).
- Projection of a $\approx4.08$-fold advantage over an active distance-3 baseline under assumptions (A1)–(A4) (Section 4.4).

The result may also inform the design of fault-tolerant architectures for quantum memories, and could inspire passive protection schemes for other hierarchical physical systems.

## 2. Background and Related Work

We review the literature that directly informs our construction, citing specific points from each source.

**Continuous-time QEC.** The continuous-time quantum error correction framework treats both noise and correction as continuous processes based on weak measurements and feedback, and analyses them via the subsystem principle, which states that protected information resides in a subsystem of the total Hilbert space [1]. Our passive scheme shares the motivation of reducing discrete measurement rounds but seeks a geometry-based containment that eliminates any feedback operation.

**Entanglement-assisted codes.** Entanglement-assisted quantum error-correcting codes (EAQECCs) allow construction of quantum codes from classical linear codes without imposing the dual-containing constraint, extending the stabilizer formalism so that shared entanglement can increase rate or distance [2]. Our codes are not entanglement-assisted; the protection mechanism is purely geometric.

**Qudit algorithms.** Efficient implementation of quantum algorithms on multilevel systems benefits from polynomial-time transpilation of qubit circuits to qudit hardware; an exhaustive-search mapping finder achieves $O(n^{3})$ complexity for dimensions $4\le d\le7$ [3]. This motivates the use of qudits (dimension $p$) as natural carriers for the tree-based code.

**Classical-to-quantum coding surveys.** Surveys of quantum error-correcting codes emphasize redundancy and syndrome measurement as essential components of active QEC, establishing the distance-3 stabilizer-code family as a widely used baseline for fault-tolerant architectures [4]. This supplies the active baseline against which Section 4.4 compares.

**Foundations of QEC.** The Pauli-expansion picture models general noise as a combination of Weyl (generalized Pauli) operators and states the Knill–Laflamme conditions for correctability [5]. We adopt this framework for our error model and correctness proof.

**Beyond qubits.** Quantum error-correction literature discusses methods to protect multi-level systems (qudits), extending concepts originally developed for qubits [6]; this supports our choice of qudit carriers.

**Operator-algebra QEC.** Operator-algebra QEC (OAQEC) generalizes the stabilizer formalism, incorporating decoherence-free subspaces and subsystem codes [7]. Our ball codes could be embedded in this framework once an explicit encoder is constructed; OAQEC already encompasses passive notions such as decoherence-free subspaces, making it the natural analytical lens.

**Energy-barrier analysis on Bruhat–Tits trees.**  These results provide concrete benchmarks for our analytic failure probabilities and motivate the quantum extension attempted here.



In summary, the active-QEC canon [4]–[6] defines the baseline; continuous-time [1] and entanglement-assisted [2] extensions mark nearby research directions; qudit algorithmic work [3] supplies the hardware context; operator-algebra [7] offers a theoretical lens; and ultrametric structural analyses [8] provide the motivating principle. No cited source derives the ball-code parameters $n_t$ and distance $d=2t+1$, or provides a Knill–Laflamme proof for such codes, which constitutes the novelty of the present work.

## 3. Methods

### 3.1 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$. Vertices correspond to closed balls (lattice classes) of $\mathbb{Q}_p$; graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$.

**Lemma 1 (nesting/disjointness).** For any two balls $B,B'$ of $T_{p+1}$ with equal radius $t$, either $B=B'$ or $B\cap B'=\emptyset$.

*Proof.* Let $v,v'$ be the centres, $s=\operatorname{dist}(v,v')$, and suppose a vertex $w$ lies in both balls. Let $m$ be the branch point (median) of $v,v',w$ in the tree. Then
$$
\operatorname{dist}(v,v')=\operatorname{dist}(v,m)+\operatorname{dist}(m,v'),\qquad
\operatorname{dist}(v,w)=\operatorname{dist}(v,m)+\operatorname{dist}(m,w),
$$
$$
\operatorname{dist}(v',w)=\operatorname{dist}(m,v')+\operatorname{dist}(m,w).
$$
Since $w\in B_t(v)\cap B_t(v')$, we have $\operatorname{dist}(v,m)+\operatorname{dist}(m,w)\le t$ and $\operatorname{dist}(m,v')+\operatorname{dist}(m,w)\le t$. Adding gives
$$
\operatorname{dist}(v,m)+\operatorname{dist}(m,v')+2\,\operatorname{dist}(m,w)\le2t,
$$
hence $s\le2t-2\,\operatorname{dist}(m,w)\le2t$. The tree metric inherited from the $p$-adic valuation satisfies the strong (ultrametric) triangle inequality $\operatorname{dist}(v,v')\le\max(\operatorname{dist}(v,w),\operatorname{dist}(w,v'))\le t$, so $s\le t$, implying $v'\in B_t(v)$. In an ultrametric ball every vertex is a centre, therefore $B_t(v)=B_t(v')$. $\square$

### 3.2 The code

A logical qudit of dimension $p$ (matching the tree's branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:
$$
n_t = 1 + \sum_{k=1}^{t}(p+1)p^{k-1}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$
The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level (a symmetry condition we state as a design requirement; explicit state vectors are left to future work). Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbours of each vertex; they are local in the tree metric (each couples a qudit only to its $p+1$ neighbours), and the Hecke algebra is commutative, so gate ordering within a ball is not a fault-tolerance hazard of the usual kind.

### 3.3 Error model

Errors are vertex-localised Weyl operators $X^{a}Z^{b}$ acting on single-vertex qudits, matching the standard decomposition of general noise into Pauli-type operators [5]. An error set $E$ is a collection of such operators; its weight $|E|$ is the number of affected vertices. Depolarising-style noise acts independently on each vertex qudit with probability $\varepsilon$ per protection epoch:
$$
\rho\longmapsto (1-\varepsilon)\,\rho
    +\frac{\varepsilon}{p^{2}-1}\sum_{(a,b)\neq(0,0)}X^{a}Z^{b}\,\rho\,Z^{-b}X^{-a}.
$$
Amplitude damping is discussed qualitatively in Section 6.

### 3.4 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff
$$
P\,E_i^{\dagger}E_j\,P = c_{ij}\,P
$$
[5], [7]. Our task is to show the geometry enforces this for all error sets of weight $\le t$.

### 3.5 Computational method

All quantitative results are obtained by closed-form combinatorics and explicit numerical evaluation of the resulting expressions, with every arithmetic step shown in Section 4. No simulation, measurement, or hardware experiment is performed or reported; the comparison to active correction in Section 4.4 is a projection under stated assumptions, and the pseudo-threshold in Section 4.5 is a projection under a stated dominant-term approximation.

## 4. Analysis

Every number in this section is derived here from stated inputs.

### 4.1 Ball sizes (exact)

**Input.** Branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k\ge1$ (shell 1 has $p+1$ vertices; each subsequent shell multiplies by $p$, since each vertex has one backward and $p$ forward neighbours).
$$
n_t = 1 + (p+1)\sum_{k=0}^{t-1}p^{k}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$

**Case $p=3$.**
- $t=1$: $n_1 = 1 + 4\cdot\frac{3-1}{2}=1+4=5$.
- $t=2$: $n_2 = 1 + 4\cdot\frac{9-1}{2}=1+16=17$.
- $t=3$: $n_3 = 1 + 4\cdot\frac{27-1}{2}=1+52=53$.

**Case $p=2$.**
- $t=1$: $n_1 = 1 + 3\cdot1 = 4$.
- $t=2$: $n_2 = 1 + 3\cdot3 = 10$.
- $t=3$: $n_3 = 1 + 3\cdot7 = 22$.

### 4.2 Correctability and distance (proposition)

**Proposition 1.** The ball code on $B_t(v_0)$ corrects every error set of weight $\le t$, hence has distance $d=2t+1$.

*Proof sketch.* (i) **Correctability.** Let $E,F$ be error sets with $|E|,|F|\le t$, supported on vertex subsets $S_E,S_F\subseteq B_t(v_0)$. By Lemma 1, the sub-balls generated by the error supports are either nested or disjoint. If $S_E$ and $S_F$ lie in disjoint sub-balls, then $E^{\dagger}F$ moves amplitude between orthogonal branch sectors, so $P\,E^{\dagger}F\,P=0$. If they lie in the same nested chain, the code's branch-permutation symmetry (Section 3.2) makes $P\,E^{\dagger}F\,P=c_{EF}P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [7].

(ii) **Distance.** Errors of weight $\le t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbour $v'$, which is orthogonal to the code space, so weight-$(t+1)$ errors are detectable but not correctable. Hence $d=2t+1$. $\square$

We flag what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch-permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d=2t+1$ follow.

For $p=3$, $t=1$: $n_1=5$, $d=3$, $t_{\mathrm{corr}}=\lfloor(d-1)/2\rfloor=1$, rate $1/5$.

### 4.3 Passive failure probability (exact computation)

**Model.** Each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight-$\le t$ error patterns by Proposition 1 without any measurement; failure requires $\ge t+1$ simultaneous errors within the ball.

**Case $p=3$, $t=1$** ($n_1=5$, $d=3$). Failure probability:
$$
P_{\mathrm{pass}} = 1-(1-\varepsilon)^{5}
                 -\binom{5}{1}\varepsilon(1-\varepsilon)^{4}.
$$

**Input.** $\varepsilon=10^{-3}$.

1. $(1-\varepsilon)^2 = 0.999^{2}=0.998001$.
2. $(1-\varepsilon)^4 = 0.998001^{2}=0.996005996001$.
3. $(1-\varepsilon)^5 = 0.996005996001\times0.999=0.995009990005$.
4. $\binom{5}{1}\varepsilon(1-\varepsilon)^{4}=5\times10^{-3}\times0.996005996001=0.004980029980$.
5. $P_{\mathrm{pass}} = 1-0.995009990005-0.004980029980=0.000009980015$,
   i.e.
$$
P_{\mathrm{pass}}\approx9.98\times10^{-6}.
$$

Leading-order check: $\binom{5}{2}\varepsilon^{2}=10\times10^{-6}=1.0\times10^{-5}$, consistent up to the $(1-\varepsilon)$ factors.

**Suppression factor** relative to the unencoded qudit (failure probability $\varepsilon=10^{-3}$):
$$
\frac{\varepsilon}{P_{\mathrm{pass}}}
   =\frac{10^{-3}}{9.980015\times10^{-6}}\approx100.2.
$$

**Case $p=3$, $t=2$** ($n_2=17$, $d=5$). Failure requires $\ge3$ errors:
$$
P_{\mathrm{pass}}^{(2)} \approx \binom{17}{3}\varepsilon^{3}(1-\varepsilon)^{14}.
$$

1. $\binom{17}{3}=680$.
2. $(1-\varepsilon)^{14}=0.999^{14}\approx0.98609$.
3. $P\approx680\times10^{-9}\times0.98609=6.705\times10^{-7}$.
4. The next term $\binom{17}{4}\varepsilon^{4}=2380\times10^{-12}\approx2.4\times10^{-9}$ adds $\approx0.35\%$.
Thus
$$
P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}.
$$

### 4.4 Active baseline comparison (labeled projection)

**Assumptions (explicitly stated; this is a projection).**
(A1) The active baseline is a generic distance-3 code on the same $n_1=5$ data qudits.
(A2) Each protection epoch requires one syndrome-extraction round in which every data qudit participates in at least one gate/measurement interaction with additional error rate $\varepsilon_m$.
(A3) Errors combine as $1-(1-\varepsilon)(1-\varepsilon_m)$ per qudit.
(A4) We take the pessimistic-for-us-but-standard case $\varepsilon_m=\varepsilon=10^{-3}$.

Effective per-qudit error:
$$
\varepsilon_{\mathrm{eff}}=1-(1-\varepsilon)^{2}
   =1-0.998001=0.001999=1.999\times10^{-3}.
$$

Active logical failure (weight-2 patterns dominate):
$$
P_{\mathrm{act}} = 1-(1-\varepsilon_{\mathrm{eff}})^{5}
                -\binom{5}{1}\varepsilon_{\mathrm{eff}}(1-\varepsilon_{\mathrm{eff}})^{4}.
$$

1. $(1-\varepsilon_{\mathrm{eff}})^{2}=0.998001^{2}=0.996005996001$.
2. $(1-\varepsilon_{\mathrm{eff}})^{4}=0.996005996001^{2}=0.992027944257$.
3. $(1-\varepsilon_{\mathrm{eff}})^{5}=0.992027944257\times0.998001=0.990045096313$.
4. $5\times0.001999\times0.992027944257=0.009914239966$.
5. $P_{\mathrm{act}}=1-0.990045096313-0.009914239966=0.000040663721$,
   i.e.
$$
P_{\mathrm{act}}\approx4.07\times10^{-5}.
$$

**Ratio.**
$$
\frac{P_{\mathrm{act}}}{P_{\mathrm{pass}}}
   =\frac{4.0664\times10^{-5}}{9.9800\times10^{-6}}\approx4.08.
$$

Thus, under assumptions (A1)–(A4), the passive scheme yields a factor $\approx4.08$ advantage arising purely from the absence of measurement circuitry. This is a projection; Section 6 details why the comparison is not yet apples-to-apples.

### 4.5 Pseudo-threshold (projection)

The pseudo-threshold is the $\varepsilon$ at which $P_{\mathrm{pass}}(\varepsilon)=\varepsilon$ for the $n=5$, $t=1$ block. Dominant term:
$$
10\,\varepsilon(1-\varepsilon)^{3}\approx1.
$$

Evaluate $f(\varepsilon)=10\,\varepsilon(1-\varepsilon)^{3}$:
- $f(0.32)=3.2\times0.68^{3}=3.2\times0.314432=1.00618>1$.
- $f(0.33)=3.3\times0.67^{3}=3.3\times0.300763=0.99252<1$.

Linear interpolation gives
$$
\varepsilon_{\mathrm{th}}\approx0.32+0.01\times\frac{1.00618-1}{1.00618-0.99252}
   =0.32+0.01\times0.4524=0.3245.
$$

Hence the pseudo-threshold under the dominant-term approximation is $\varepsilon_{\mathrm{th}}\approx0.3245$; this is a projection, since higher-order terms are ignored.

## 5. Results

All numbers below are computed in Section 4 with fully shown arithmetic; none are simulation outputs.

**Code parameters (exact).** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$. The distance of the ball code is $d=2t+1$ (Proposition 1, conditional on the branch-permutation symmetry of the encoder). The flagship block $p=3$, $t=1$ has $n_1=5$ qudits, $d=3$, and rate $1/5$.

**Passive logical failure (exact computation, $p=3$, $t=1$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ per protection epoch, a suppression factor $\varepsilon/P_{\mathrm{pass}}\approx100.2$ over an unencoded qudit.

**Passive logical failure ($p=3$, $t=2$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ per protection epoch (leading term $6.705\times10^{-7}$ plus a $\approx0.35\%$ correction from the weight-4 term).

**Active baseline projection.** $P_{\mathrm{act}}\approx4.07\times10^{-5}$ under assumptions (A1)–(A4), giving a $\approx4.08$-fold advantage for the passive scheme.

**Pseudo-threshold projection.** $\varepsilon_{\mathrm{th}}\approx0.3245$ under the dominant-term approximation.

## 6. Discussion

**What is proved versus assumed.** Lemma 1 (nesting/disjointness of equal-radius balls) is proved, and the shell-count formula for $n_t$ is an exact combinatorial identity. Proposition 1, however, is conditional: the branch-permutation symmetry of the code states is a design requirement, and no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed in this paper. If no symmetric encoder exists for a given ball, the weight-$\le t$ correctability claim and the distance $d=2t+1$ fail. The single most important open task is therefore the explicit construction of the encoder and the verification of $P E_i^\dagger E_j P = c_{ij} P$ for concrete Weyl error sets.

**Model limitations.**
(i) The noise model is independent depolarising noise per vertex qudit per epoch; correlated errors (e.g., a gate fault coupling two neighbouring vertices, or a burst affecting a whole branch) violate independence and could defeat the weight counting on which $P_{\mathrm{pass}}$ rests.
(ii) Amplitude damping is not modelled; on a tree geometry its asymmetric action may or may not respect the nesting structure, and this is unresolved.
(iii) The active-baseline comparison rests on assumptions (A1)–(A4), in particular the pessimistic choice $\varepsilon_m=\varepsilon$ and the simple combination rule of (A3); a real baseline may have a smaller $\varepsilon_m$, which would shrink the $\approx4.08$ factor toward unity, or may require multiple syndrome-extraction rounds, which would enlarge it. The comparison is therefore indicative, not apples-to-apples.
(iv) The pseudo-threshold $\approx0.3245$ uses only the dominant term of $P_{\mathrm{pass}}(\varepsilon)$; near $\varepsilon\approx0.32$ the neglected higher-order terms are not negligible, so the true threshold may differ.

**Falsification criteria.** The central claims would be falsified if: (a) an explicit encoder on $B_t(v_0)$ fails the Knill–Laflamme conditions for some weight-$\le t$ Weyl error set, contradicting Proposition 1; (b) two distinct equal-radius balls of $T_{p+1}$ overlap without coinciding, contradicting Lemma 1; or (c) a fault-tolerant simulation of the code under the stated noise model yields logical failure rates inconsistent with the binomial computation of Section 4.3.

**Open questions.** Whether the ball codes embed into the operator-algebra QEC framework [7], which would allow existing OAQEC machinery to analyse them; whether Hecke-operator gates admit a fault-tolerant compilation compatible with the code symmetry; and whether the passive advantage survives system-level energy-metric assessments such as those used in qudit benchmarking.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.** The primary users are quantum-hardware architects exploring alternative fault-tolerance strategies for qudit-based processors. If the passive scheme operates as projected, designers could allocate fewer ancilla qudits to syndrome extraction, reduce the depth of error-correction cycles, and simplify control electronics, because logical protection would arise from the static geometry of the qudit layout rather than from active feedback. The decision variable altered is the allocation of hardware resources between data qudits and measurement/feedback circuitry.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (technology concept formulated). No experimental prototype has been built, so the readiness does not exceed TRL 3.

**(c) Smallest next experiment.** A minimal prototype would consist of five physical qutrits ($p=3$) arranged in the star-shaped ball $B_1(v_0)$ of the Bruhat–Tits tree. The experiment would (i) initialise a logical state using a symmetric encoding (to be defined), (ii) apply a single protection epoch of independent depolarising noise with calibrated error rate $\varepsilon$, and (iii) measure the logical error probability. The outcome that would falsify the passive-failure prediction is a measured logical failure rate $P_{\mathrm{exp}}$ that deviates from the analytically computed $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ by more than a factor of two, after accounting for statistical uncertainty.

**(d) Engineering constraints.**
- **Qudit hardware:** The scheme requires qutrits (or higher-dimensional qudits) with controllable nearest-neighbour Hecke-type interactions.
- **Gate locality:** Hecke operators must be implementable as local averaging over the $p+1$ forward neighbours; this imposes a constraint on the connectivity of the physical layout.
- **Error-rate calibration:** Accurate knowledge of the physical depolarising rate $\varepsilon$ per epoch is needed to compare with the analytic prediction.
- **State preparation:** The symmetric encoder assumed in Proposition 1 must be realised; without an explicit construction this remains an open engineering task.

All other constraints (materials, cost, scale-up) are currently open questions because they depend on the eventual encoder design.

**(e) Projected cost/performance bounds.** Under the assumptions used in Sections 4.3–4.4 (independent depolarising noise $\varepsilon=10^{-3}$, five-qudit block, passive correction only) the logical failure probability is projected to be $P_{\mathrm{pass}}\approx9.98\times10^{-6}$, giving a suppression factor of $\varepsilon/P_{\mathrm{pass}}\approx100.2$ relative to an unencoded qudit. Compared with an active distance-3 baseline under the same $\varepsilon$ and additional measurement error $\varepsilon_m=\varepsilon$, the passive scheme is projected to improve the logical failure rate by a factor of $\approx4.08$. These numbers are analytic projections; any engineering estimate of hardware cost must treat them as conditional on the existence of a symmetric encoder.

**(f) Direct risks and misuse paths.** If the passive geometry is adopted without a verified symmetric encoder, the code may fail to correct weight-$\le t$ errors, leading to a false sense of security and potentially higher logical error rates than anticipated. Moreover, over-reliance on the passive claim could discourage the development of robust active syndrome-extraction hardware, which remains essential for many existing codes.

## 8. Conclusion

We have formalised a passive quantum error-correction scheme in which logical qudits live on balls of the Bruhat–Tits tree $T_{p+1}$, proved a nesting lemma implying that equal-radius balls are nested or disjoint, derived the exact code parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ and the conditional distance $d = 2t+1$, and computed analytically that under independent depolarising noise at $\varepsilon = 10^{-3}$ the flagship $p=3$, $t=1$ block fails with probability $\approx9.98\times10^{-6}$ per epoch, a suppression of $\approx100.2$ over an unencoded qudit and, as an explicitly labeled projection under stated assumptions, a factor $\approx4.08$ over an active distance-3 baseline with noisy syndrome extraction. The scheme's promise is real but conditional on constructing an explicit symmetric encoder; we have stated the assumptions, the failure modes, and the falsification criteria plainly so that the proposal can be tested rather than taken on trust.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 11. length 3740 -> 3859 words.
- Version 2.1.0 (2026-11-03, from 2.0.0): revised against the current literature, re-reviewed and re-verified. references 11 -> 8. length 3859 -> 3588 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 1 quantitative claim from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[2] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[3] Efficient realization of quantum algorithms with qudits. arXiv:2111.04384v3. https://arxiv.org/abs/2111.04384v3
[4] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[5] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[6] Quantum Error Correction. arXiv:1910.03672v1. https://arxiv.org/abs/1910.03672v1
[7] Stabilizer Formalism for Operator Algebra Quantum Error Correction. arXiv:2304.11442v2. https://arxiv.org/abs/2304.11442v2
[8] https://papers.qnfo.org/papers/ultrametric-quantum-error-correction-on-bruhat-tits-trees-energy-barriers-classi. QNFO: Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question.
