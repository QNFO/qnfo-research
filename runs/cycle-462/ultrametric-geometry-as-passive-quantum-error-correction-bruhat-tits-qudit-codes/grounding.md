# Grounding block - source: rem-rev-0786b94f-b903-4914-b99b-7d91513f5d25

## Research idea

Ultrametric geometry as passive quantum error correction for Bruhat–Tits qudits. Claim: encoding quantum information on qudits placed at vertices of the Bruhat–Tits tree, with Hecke operators as gates, yields passive error protection because the non-Archimedean property ||x+y||_p ≤ max(||x||_p, ||y||_p) prevents small errors from accumulating — no active syndrome measurement needed. Question: can this ultrametric 'geometric QEC' be formalized as a genuine error-correcting code with provable distance thresholds, and does it outperform active correction for specific noise channels? Test: (1) derive the code distance of the p-adic tree encoding and prove/bound correctable error sets under the ultrametric metric; (2) simulate gate sequences (p-adic QFT as radix-p gates) under depolarizing and amplitude-damping noise, comparing logical error rates against standard surface-code baselines; (3) analyze whether Hecke-coupled multi-place (adelic) encodings degrade or enhance protection. If the non-Archimedean bound translates into a rigorous threshold, this would be a novel, hardware-agnostic QEC mechanism distinct from stabilizer codes.

Source: owner notebook notes/v1/2026/07/27/_26208193002.md

Post-publication revision of the published paper "Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

## Existing paper under revision (remediation only)

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


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1311.2485v2 | Continuous-time quantum error correction
arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes
arXiv:2111.04384v3 | Efficient realization of quantum algorithms with qudits
arXiv:quant-ph/0602157v1 | An Introduction to Error-Correcting Codes: From Classical to Quantum
arXiv:quant-ph/0304016v2 | Quantum Computing and Error Correction
arXiv:1910.03672v1 | Quantum Error Correction
arXiv:2304.11442v2 | Stabilizer Formalism for Operator Algebra Quantum Error Correction

## QNFO corpus context (Vectorize)

QNFO: Passive Quantum Error Correction via Ultrametric Geometry on Bruhat–Tits Trees | https://papers.qnfo.org/papers/passive-quantum-error-correction-via-ultrametric-geometry-on-bruhat-tits-trees
QNFO: Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound | https://papers.qnfo.org/papers/ultrametric-geometry-as-passive-quantum-error-correction-bruhat-tits-qudit-codes
QNFO: Ultrametric Passive Error Correction on \(p\)-ary Bruhat–Tits Trees: Barrier Analysis and Recursive Thresholds | https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis
QNFO: Ultrametric Passive Fault Tolerance on Bruhat–Tits Trees: Analytic Derivation and Quantitative Projections | https://papers.qnfo.org/papers/ultrametric-passive-fault-tolerance-on-bruhat-tits-trees-analytic-deriv-93ee94f3

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1311.2485v2 | Continuous-time quantum error correction
  Continuous-time quantum error correction (CTQEC) is an approach to protecting quantum information from noise in which both the noise and the error correcting operations are treated as processes that are continuous in time. This chapter investigates CTQEC based on continuous weak measurements and feedback from the point of view of the subsystem principle, which states that protected quantum informa
  Full text (https://arxiv.org/html/1311.2485v2), excerpts of its own sections:
  § I Introduction: In the standard theory of quantum error correction, both the noise and the error-correcting operations are represented by discrete transformations. If $\mathcal{B}(\mathcal{H})$ denotes the space of bounded operators over a Hilbert space $\mathcal{H}$ , and $\mathcal{H^{S}}$ is the (finite-dimensional) Hilbert space of the controlled system, we say that the code subsystem $\mathcal{H}^{A}$ in the decomposition $\mathcal{H^{S}}=\mathcal{H^{A}}\otimes\mathcal{H}^{B}\oplus\mathcal{K}$ (1) is correctable under the completely positive trace-preserving (CPTP) noise map $\mathcal{E}:\mathcal{B}(\mathcal{H}^{S})\rightarrow\mathcal{B}(\mathcal{H}^{S})$ , if there exists a CPTP error-correcting map $\mathcal{R}:\mathcal{B}(\mathcal{H}^{S})\rightarrow\mathcal{B}(\mathcal{H}^{S})$ , such that $\displaystyle\textrm{Tr}_{B}\{(\mathcal{P}^{AB}\circ\mathcal{R}\circ\mathcal{E})(\sigma)\}=\textrm{Tr}_{B}\{\sigma\},$ (2) $\displaystyle\hskip 2.84544pt\textrm{for all }\sigma\in\mathcal{B}(\mathcal{H}^{S}),\sigma=\mathcal{P}^{AB}(\sigma)\hskip 2.84544pt,$ where $\mathcal{P}^{AB}(\cdot)$ denotes the [...]
  § II CTQEC in an encoded basis: As discussed in Chapter 6, correctable information is always contained in subsystems of the system’s Hilbert space [ 10 , 29 ] . This means, in particular, that if the information initially encoded in the subsystem $\mathcal{H}^{A}$ in Eq. ( 1 ) is correctable after the noise map $\mathcal{E}$ , it is unitarily recoverable [ 9 ] , i.e., there exists a unitary map $\mathcal{U}(\cdot)=U(\cdot)U^{\dagger}$ , $U\in\mathcal{B}(\mathcal{H}^{S})$ , such that $\displaystyle\mathcal{U}\circ\mathcal{E}(\rho\otimes\tau)=\rho\otimes\tau^{\prime},\hskip 11.38092pt\tau^{\prime}\in\mathcal{B}(\mathcal{H}^{B^{\prime}}),$ (12) $\displaystyle\hskip 5.69046pt\text{for all }\rho\in\mathcal{B}(\mathcal{H}^{A}),\hskip 2.84544pt\tau\in\mathcal{B}(\mathcal{H}^{B}),$ where the subsystem $\mathcal{H}^{B^{\prime}}$ can be different from $\mathcal{H}^{B}$ . Complete correction generally requires an additional CPTP map that transforms the operators on $\mathcal{H}^{B^{\prime}}$ into operators on $\mathcal{H}^{B}$ . As shown in Ref. [ 28 ] , Eq. [...]
  § III.1 The single-qubit problem: In this section we will show how to implement the PZ quantum-jump error-correction scheme (Eq. ( 3 )) using weak measurements in the encoded basis. We start with the problem of protecting a single qubit in the state $|0\rangle$ from noise using weak measurements. [...]
  § VI Outlook: In this chapter we saw that the subsystem principle can be useful for understanding various aspects of the workings of CTQEC and its performance under different noise models, as well as for the design of CTQEC protocols using protocols for the protection of a known state. However, further research is needed to understand how to construct optimal CTQEC protocols. In the case of the quantum-jump model, the code-space fidelity reaches a quasi-equilibrium value which can be used to estimate the performance of the scheme. It would be interesting to see whether an analogue of the equilibrium fidelity exists for schemes with indirect feedback. This could prove useful since stochastic evolutions are generally too complicated for analytical treatment. The equilibrium code-space fidelity can be useful also in assessing the performance of CTQEC under non-Markovian decoherence, where the description of the evolution of a system subject to CTQEC can be difficult due to the large number of environment degrees of freedom. [...]
[2] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes
  We provide a self-contained introduction for entanglement-assisted quantum error-correcting codes in this book chapter.
  Full text (https://arxiv.org/html/1610.04013v1), excerpts of its own sections:
  § 1 Introduction: Quantum error-correcting codes (QECCs) have turned out to have many applications; but their primary purpose, of course, is to protect quantum information from noise. This need manifests itself in two rather different situations. The first is in quantum computing. The bits in a quantum computer are subject to noise due both to imprecision in the operations (or gates) and to interactions with the external environment. They undergo errors when they are acted upon, and when they are just being stored (though hopefully not at the same rate). All the qubits in the computer must be kept error-free long enough for the computation to be completed. This is the principle of fault-tolerance. A rather different situation occurs in quantum communication . Here, the sender and receiver (Alice and Bob) are assumed to be physically separated, and the qubits travel from the sender to the receiver over a (presumably noisy) channel. This channel is assumed to be the dominant source of errors. [...]
  § 1.1 Entanglement-assisted codes: In a standard QECC, the encoding operation proceeds in two steps. First, to the quantum state ${|\psi\rangle}$ of $k$ qubits that one wishes to encode, one appends some number of ancilla qubits in a standard state (usually ${|0\rangle}$ ), and then applies an encoding unitary $U_{\rm enc}$ : ${|\psi\rangle}\rightarrow{|\psi\rangle}\otimes{|0\rangle}^{\otimes n-k}\rightarrow{|\Psi_{L}\rangle}=U_{\rm enc}{|\psi\rangle}\otimes{|0\rangle}^{\otimes n-k},$ (1) where ${|\Psi_{L}\rangle}$ is the encoded or logical state. The systems in states ${|\psi\rangle}$ and ${|0\rangle}$ are initially in the possession of Alice, the sender. The encoding unitary acts on the space of the input qubits and ancillas together. In an EAQECC, one can append not only ancillas, but also ebits, before doing the encoding unitary: ${|\psi\rangle}\rightarrow{|\psi\rangle}\otimes{|0\rangle}^{\otimes n-k-c}\otimes{|\Phi_{+}\rangle}_{AB}^{\otimes c}\rightarrow(U_{\rm enc}\otimes{\hat{I}}_{B}){|\psi\rangle}\otimes{|0\rangle}^{\otimes n-k}\otimes{|\Phi_{+}\rangle}_{AB}^{\otimes c}. [...]
  § 2.1 Noncommuting “stabilizers”: First, let us recall the stabilizer formalism for conventional quantum error-correcting codes, as presented in [ LB13 , chapter 2] . Let $G_{n}$ be the $n$ -qubit Pauli group [ NC00 ] . Every operator in $G_{n}$ either has eigenvalues $\pm 1$ or $\pm i$ . Let $S\subset G_{n}$ be an Abelian subgroup that does not contain $-I$ . [...]
  § 5 Conclusions: EAQECCs expand the usual paradigm of quantum error correction by allowing the sender and receiver to make use of pre-shared entanglement. This entanglement can increase either the rate of communication or the number of correctable errors. While entanglement can be used to improve quantum communication in other ways—for example, by sending classical information through the channel and teleporting extra qubits—in many cases EAQECCs have better performance [ HW10a , HW10b ] . In this chapter we have presented an extension of the usual stabilizer formalism for QECCs to include entanglement-assistance. This extension includes the usual theory of stabilizers as a special case, and has a number of advantages; in particular, it allows one to construct quantum codes from classical linear codes without having to impose the dual-containing constraint of standard codes, while retaining the usual relation between the rate and distance of the classical and quantum codes. [...]
[3] arXiv:2111.04384v3 | Efficient realization of quantum algorithms with qudits
  The development of a universal fault-tolerant quantum computer that can solve efficiently various difficult computational problems is an outstanding challenge for science and technology. In this work, we propose a technique for an efficient implementation of quantum algorithms with multilevel quantum systems (qudits). Our method uses a transpilation of a circuit in the standard qubit form, which d
  Full text (https://arxiv.org/html/2111.04384v3), excerpts of its own sections:
  § I Introduction: Progress in engineering coherent quantum many-body systems with a significant degree of control makes it realistic to study properties of exotic quantum phases [ 1 , 2 , 3 , 4 , 5 , 6 ] and to prototype quantum algorithms [ 7 , 8 , 9 , 10 ] . [...]
  § IV.1.1 Finding the optimal mapping with an exhaustive search: The straightforward way for optimizing qubit-to-qudit mapping is to employ an exhaustive search over all possible mappings $\Phi\equiv\{\phi\}$ of the form Eq. ( 10 ). This approach is applicable if the number of available qudits $m$ and their dimension $d$ are reasonably small. The first step of the exhaustive search is to construct a set of all non-equivalent mappings $\widetilde{\Phi}\subset\Phi$ . Here we call two mappings equivalent if they are different only up to permutations of qubits indices within a particular qudit, or up to permutation of whole sets of qubits’ indices belonging to different qudits (and thus definitely provide the same number of entangling gates). Then, the mapping finder sequentially inputs each $\phi\in\widetilde{\Phi}$ to the qudit circuit constructor to get the corresponding qudit circuit ${\sf circ}^{\rm qd}_{\phi}$ . By comparison of two-qudit gate numbers in ${\sf circ}^{\rm qd}_{\phi}$ while going through all mappings, the mapping finder chooses the one ( $\phi_{\rm opt}$ ), which provides the smallest number of two-qudit gates. [...]
  § VI Discussion: Here we stress some important points related to the developed qudit-based transpilation approach. First, we emphasize its scalability with respect to the width and depth of a processed input qubit circuit. The scalability is assured by the facts that (i) the complexity of transpiling of a given single-, two-, or multi-qubit gate to its qudit version grows no more than polynomially with the number of qubits affected by the gate, (ii) the complexity of transpiling the whole qubit circuit with respect to the given qubit-to-qudit mapping grows linearly with a number of gates, and (iii) a polynomial in qubit number $n$ algorithm for mapping finding, which provides an advantage (or at least doesn’t make things worse) compared to a standard qubit-based transpilation, can be used. In particular, a greedy algorithm for the mapping finder of $\mathcal{O}(n^{3})$ complexity for $4\leq d\leq 7$ is shown. Therefore, the resulting qudit-based transpilation complexity is polynomial in the number of qubits $n$ in the processed circuit and linear in the number of gates. [...]
  § VII Conclusion and outlook: We have presented the approach for an efficient implementation of qubit circuits with qudit-based processors. The proposed approach consists of finding the optimized qubit-to-qudit mapping, transpiling a qubit circuit according to this mapping, running a transpiled circuit on a qudit-based processor (or emulator), and then reassigning read-out measurement results back to the qubit-based representation. We have developed a qudit-based transpilation algorithm with respect to a particular universal set of single-qudit and two-qudit gates and proposed an idea of a mapping finder algorithm with polynomial complexity. Then we have shown an example of applying the developed approach for realizing a $6$ -qubit circuit with four $4$ -level qudits. We have demonstrated that the resulting number of two-particle operations required for implementing the given circuit with qudits appears considerably smaller than the one within a straightforward qubit-based implementation. [...]
[4] arXiv:quant-ph/0602157v1 | An Introduction to Error-Correcting Codes: From Classical to Quantum
  This report surveys quantum error-correcting codes. As Preskill claimed, 21st century would be the golden age of quantum error correction. Quantum channels behave differently from classical channels, so researchers face difficulties in developing robust quantum codes. Fortunately, the classical error control methods have been well developed. If we can learn many lessons from classical coding theor
  Full text (https://arxiv.org/html/quant-ph/0602157v1), excerpts of its own sections:
  § I Introduction: In the age of information technology, error-correcting codes are widely used in communication systems and data storage systems. Both types of systems share the same model, as shown in Fig  1 . A source transmits information to a user through a channel. The communication channel, unfortunately, is usually imperfect; i.e., the information might be corrupted by noises during transmission. To immunize information to noises, the sender adds redundancy within the information and follows an invertible encoding process to mix the redundancy and information. When the receiver obtains this mixture, it checks where errors are, corrects the errors as possible, and finally removes redundancy added by the sender. The above scheme of encoding and decoding is referred as error-correcting codes . Figure 1: Block diagram of a communication system. A source transmits information to a user through a channel. The communication channel is usually imperfect so that the information is prone to errors during transmission. Coding theory was initiated by two seminal papers: 1. [...]
  § II Principles of Classical Error Correction: In modern information systems, the unit of information is bit . A bit takes one of two values: 0 or 1. As mentioned in Section  I , a bit transmitted through a channel is prone to errors. At the end of a channel, an information bit 0/1 may remain as 0/1 or flip to 1/0. A simple model of noisy channels is Binary Symmetric Channel with parameter $p$ which flips each transmitted bit with probability $p$ independent of all other events. This effect is sketched in Fig  2 . Using this specific channel is enough to illustrate the basic ideas of error correction. Figure 2: Binary Symmetric Channel. Before proceeding to the detailed discussions, we first introduce the notations. Let the set $\mathbf{A}$ consist of information bit strings. An encoding operator $\mathbf{E}$ maps $\mathbf{A}$ into a space $\mathbf{C}$ called code . The elements in the code $\mathbf{C}$ are called codewords . In the channel, a set of noise operators $\mathbf{N}=\{N_{0}=I,N_{1},N_{2},\cdots\}$ corrupts the codewords. In $\mathbf{N}$ , $I$ is an identity which does nothing wrong to codewords. [...]
  § II.1 Learning from Classical Error-Correcting Codes: The design of error-correcting codes is based on the concept of adding redundancy . This concept happens in our oral communications too. When people have a discussion, they usually convey a viewpoint several times or state it in other words. This is equivalent to repeating the information or changing the wordings of the information. [...]
  § V Conclusions: This report investigates the fundamentals of quantum error-correcting codes. The difference between quantum and classical communication systems results from the different characteristics of bits and qubits and from different error models for the noisy channels. Nevertheless, quantum error correction shares many concepts with its classical counterpart. Both quantum and classical coding schemes add ancillary qubits/bits and measure a syndrome to protect information messages. They also have similar conditions for errror detectability and correctability. Due to lack of time, this report leaves out the construction of quantum error-correcting codes, which is now based on Gottesman’s stabilizer codes  [ 3 ] . The research in quantum error-correcting codes has already migrated to nonbinary codes  [ 19 ] . However, there is still a long ways to go. In order to use ancillary bits efficiently, modern classical coding theory already goes beyond linear codes. [...]
[5] arXiv:quant-ph/0304016v2 | Quantum Computing and Error Correction
  The main ideas of quantum error correction are introduced. These are encoding, extraction of syndromes, error operators, and code construction. It is shown that general noise and relaxation of a set of 2-state quantum systems can always be understood as a combination of Pauli operators acting on the system. Each quantum error correcting code allows a subset of these errors to be corrected. In many
  Full text (https://arxiv.org/html/quant-ph/0304016v2), excerpts of its own sections:
  § 1 Introduction: Quantum error correction (QEC) is one of the basic components of quantum information theory. It arises from the union of quantum mechanics and classical information theory, and leads to some powerful and surprising possibilities in the quantum context. For example, we may use a quantum error correcting code to allow us to store a general, unknown state of a two-state system in a set of five two-state systems (eg two-level atoms), in such a way that if any unknown change (arbitrarily large and including the case of relaxation) should occur in the state of any one atom, then it is still possible to recover the originally stored state precisely: the seemingly large perturbation had no effect at all on the stored information. QEC is by now sufficiently well established that it has chapters devoted to it in text books, for example [ 1 , 2 , 3 ] . Nevertheless, an introduction to the ideas is still useful for people new to the subject, so much of the discussion here will be devoted to this. I will then discuss recent research in section 7. [...]
  § 2 Background: The first quantum error correcting codes were discovered independently by Shor [ 4 ] and Steane [ 5 ] . Shor proved that 9 qubits could be used to protect a single qubit against general errors, while Steane described a general code construction whose simplest example does the same job using 7 qubits (see section 5.1). A general theory of quantum error correction dates from subsequent papers of Calderbank and Shor [ 6 ] and Steane [ 7 ] in which general code constructions, existence proofs, and correction methods were given. Knill and Laflamme [ 8 ] and Bennett et. al. [ 9 ] provided a more general theoretical framework, describing requirements for quantum error correcting codes, and measures of the fidelity of corrected states. The important concept of the stabilizer (section 5.1) is due to Gottesman [ 10 ] and independently Calderbank et. al. [ 11 ] ; this yielded many useful insights into the subject, and permitted many new codes to be discovered [ 10 , 11 , 12 ] . Stabilizer methods will probably make a valuable contribution to other areas in quantum information physics. [...]
  § 3 Three bit code: We will begin by analysing in detail the workings of the most simple quantum error correcting code. Exactly what is meant by a quantum error correcting code will become apparent. Suppose a source A wishes transmit quantum information via a noisy communication channel to a receiver B . Obviously the channel must be noisy in practice since no channel is perfectly noise-free. However, in order to do better than merely sending quantum bits down the channel, we must know something about the noise. For this introductory section, the following properties will be assumed: the noise acts on each qubit independently, and for a given qubit has an effect chosen at random between leaving the qubit’s state unchanged (probability $1-p$ ) and applying a Pauli $\sigma_{x}$ operator (probability $p Figure 1: Example of quantum error correction which illustrates the main features. A single qubit is encoded into three, and these are sent down the noisy channel. [...]
  § 4 Most general possible error, digitization of noise: The most general possible error that a qubit can undergo is a general combination of the ones we have listed, that is, general rotations in the two-dimensional Hilbert space, combined with a possible projection onto any axis. [...]
[6] arXiv:1910.03672v1 | Quantum Error Correction
  Quantum error correction is a set of methods to protect quantum information--that is, quantum states--from unwanted environmental interactions (decoherence) and other forms of noise. The information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space. This code is designed so that the most common errors move the state into an error space orthogonal to the or
  Full text (https://ar5iv.labs.arxiv.org/html/1910.03672v1), excerpts of its own sections:
  § Submission history: From: Todd Brun [ view email ] [v1] Tue, 8 Oct 2019 20:30:06 UTC (539 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Quantum Error Correction, by Todd A. Brun View PDF view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2019-10
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[7] arXiv:2304.11442v2 | Stabilizer Formalism for Operator Algebra Quantum Error Correction
  We introduce a stabilizer formalism for the general quantum error correction framework called operator algebra quantum error correction (OAQEC), which generalizes Gottesman's formulation for traditional quantum error correcting codes (QEC) and Poulin's for operator quantum error correction and subsystem codes (OQEC). The construction generates hybrid classical-quantum stabilizer codes and we formu
  Full text (https://arxiv.org/html/2304.11442v2), excerpts of its own sections:
  § 1 Introduction: Quantum error correction (QEC) is a central topic in quantum information science. Its origins as an independent field of study go back almost three decades [ 64 , 42 , 18 , 65 ] , and it now touches on almost every aspect of quantum information, ranging from theoretical to experimental investigations and in recent years as a key facet in the development of new quantum technologies [ 67 , 12 , 15 , 69 , 70 , 36 , 56 ] . More recently, developments in QEC included the introduction of a unified approach, called ‘operator quantum error correction’ (OQEC) [ 44 , 45 ] that brought together traditional QEC with passive notions such as decoherence-free subspaces and noiseless subsystems, and led to the advent of subsystem codes and advances in fault-tolerant quantum computing [ 61 , 8 , 7 , 14 , 13 , 34 , 47 , 31 ] . [...]
  § 3.4 Motivating Class of Examples: We can build upon the motivating example from the original stabilizer formalism to illustrate the various concepts discussed above for a relatively simple class of examples. The following operators are defined on $n$ -qubit Hilbert space. $\bullet$ Let $s\leq n$ be a fixed positive integer and let $\mathcal{S}=\langle Z_{1},\ldots,Z_{s}\rangle$ ; the subgroup of $\mathcal{P}_{n}$ generated by phase flip operators on the first $s$ qubits. Then $C=C(\mathcal{S})=\mathrm{span}\big\{|\underbrace{0\cdots 0}_{s}\,i_{1}\cdots i_{n-s}\rangle\,:\,i_{j}=0,1\big\},$ and $\dim C=2^{n-s}$ so that $C$ can encode $n-s$ qubits. $\bullet$ Let $r$ be a fixed integer with $0\leq r\leq n-s$ , and let $\mathcal{G}_{0}$ be the set of $r$ pairs of Pauli operators acting on qubits $s+1$ to $r+s$ : $\mathcal{G}_{0}=\big\{X_{i},Z_{i}\,:\,s+1\leq i\leq r+s\big\}.$ Then the gauge group $\mathcal{G}$ is generated by $\mathcal{S}$ , $iI$ , and $\mathcal{G}_{0}$ , and includes the full Pauli subgroup of operators acting non-trivially on the $r$ ‘gauge qubits’. [...]
  § 4 Error Correction Theorem: The code construction above thus defines codes $C=C(\mathcal{S},\mathcal{G}_{0},\mathcal{L}_{0},\mathcal{T}_{0})$ , determined by, respectively, choices of stabilizer subgroup, gauge and logical operators, and subset of coset representatives. We shall characterize what sets of Pauli errors are correctable for a given code, and in doing so, we establish a generalization of the fundamental theorems of [ 25 , 26 ] and [ 61 ] to this setting. We shall first recall the basic notions and relevant results from OAQEC [ 9 , 10 ] , and then specify to the code framework formulated above. The starting point is the basic definition of OAQEC codes, which is most conveniently introduced in the Heisenberg picture. Definition 1 . [...]
  § 7 Concluding Remarks: This work opens up a number of potential new lines of investigation and the possible extension of some others. Further consideration of the hybrid Bacon-Shor subsystem codes introduced here is warranted, given the wide applicability of the subsystem versions [ 61 , 8 ] in fault-tolerant quantum computing and beyond, and in particular with NISQ era quantum computers likely to involve hybrid forms of classical and quantum information processing [ 62 ] . It would be interesting to explore possible implications of our stablizer formalism on other classes of recently constructed hybrid codes; for instance, we expect new light can be shed on codes constructed in works such as [ 29 , 49 , 53 , 54 ] , and one can ask if the formalism allows for construction of more codes with useful properties following the approaches introduced there. [...]
[8] QNFO: Passive Quantum Error Correction via Ultrametric Geometry on Bruhat–Tits Trees | https://papers.qnfo.org/papers/passive-quantum-error-correction-via-ultrametric-geometry-on-bruhat-tits-trees
  Scalable quantum computing is limited by the thermodynamic overhead of active error‑correction cycles, which require repeated syndrome extraction, low‑latency decoding, and large ancilla resources. A quantitative gap exists: no fully derived account shows how non‑Archimedean (ultrametric) geometry can passively confine errors, compute exact code parameters, logical‑failure probabilities, and the a
  Full text (https://papers.qnfo.org/papers/passive-quantum-error-correction-via-ultrametric-geometry-on-bruhat-tits-trees), excerpts of its own sections:
  § 1. Introduction Current quantum processors are constrained by the overhead of active quantum error correction (QEC). Photon‑loss bosonic codes [1] and thermodynamically trivial memory models [2] illustrate passive mechanisms that can reduce error rates without active syndrome extraction. The real‑world problem, therefore, is the scaling bottleneck posed by active QEC for large‑scale quantum computers, a bottleneck that directly impacts the feasibility of quantum advantage in practical applications such as cryptanalysis and quantum simulation.: If a hardware platform could store logical information in a structure that *passively* blocks error propagation, the need for active cycles would disappear, reducing both hardware complexity and thermodynamic cost. The ultrametric geometry of Bruhat–Tits trees provides such a structure: the strong triangle inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$ forces any two $p$‑adic balls to be either nested or disjoint, confining local perturbations to a bounded ultrametric distance class. [...]
  § 5. Results: - **Code parameters.** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$ (directly from the formula in Section 4.1). - **Distance.** $d=2t+1$; flagship block $p=3$, $t=1$ has $d=3$ and rate $1/5$. - **Passive logical failure.** $P_{\mathrm{pass}}=9.98\times10^{-6}$ for $\varepsilon=10^{-3}$ (Section 4.3.1) and $P_{\mathrm{pass}}^{(2)}=6.73\times10^{-7}$ for $t=2$ (Section 4.3.2). - **Barrier heights.** $B(3)=8$, $B(4)=16$ (Section 4.4). - **Logical error bounds.** $p_L(3)=6.5536\times10^{-4}$, $p_L(4)=4.295\times10^{-7}$ for $p_{\mathrm{err}}=0.40$ (Section 4.4). - **Thermal bounds.** $p_L(3)\le3.35\times10^{-4}$, $p_L(5)\le1.27\times10^{-14}$, $p_L(10)\le10^{-444.7}$ (Section 4.5). - **Cooling‑budget projection.** Per‑site gap $\Delta\ge1.727\,k_{\mathrm{B}}T$ to reach $10^{-12}$ logical error at depth 4 (Section 4.5). All results follow from the explicit arithmetic presented in Section 4; no simulation data are used.
  § 6. Summary of derived quantities: | Quantity | Expression | Example (p=5, t=2) | |----------|------------|--------------------| | Code size \(n_t\) | \(1+\dfrac{(p+1)(p^{t}-1)}{p-1}\) | \(n_2=1+\frac{6(25-1)}{4}=1+36=37\) | | Distance \(d\) | \(2t+1\) | \(d=5\) | | Barrier \(B(d)\) | \(2^{d}\) (odd \(p\)) | \(B=2^{5}=32\) | | Logical‑error bound | \(p_{\mathrm{err}}^{\,B(d)}\) | with \(p_{\mathrm{err}}=0.40\): \(p_L=0.40^{32}\approx1.5\times10^{-7}\) | All entries are obtained by direct substitution into the analytic formulas derived earlier; no simulation or empirical data are introduced. These extended derivations reinforce the quantitative backbone of the ultrametric passive‑QEC proposal, clarify its scaling behaviour, and place it in direct dialogue with a broad spectrum of passive and active error‑correction concepts documented in the cited literature.
  § (c) Minimal next experiment: A neutral‑atom platform can realize a depth‑3 ($d=3$) $p=3$ tree comprising five physical qutrits (the $n_1$ ball) plus two additional layers to implement the barrier. The experiment would: 1. Prepare a logical state (e.g., $\ket{0_L}$). 2. Apply engineered depolarising noise with $p_{\mathrm{err}}=0.40$ per vertex. 3. Perform a single majority‑vote decoding pass. 4. Record the logical error rate over $N=10^{4}$ trials. If the observed logical error rate exceeds $p_L(3)=6.55\times10^{-4}$ by more than three standard deviations, the passive‑barrier hypothesis would be falsified.
[9] QNFO: Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound | https://papers.qnfo.org/papers/ultrametric-geometry-as-passive-quantum-error-correction-bruhat-tits-qudit-codes
  Active quantum error correction (QEC) dominates the overhead of scalable quantum processors, requiring repeated syndrome extraction, low-latency decoding, and large ancilla counts that inflate hardware cost and energy consumption. A passive alternative that eliminates measurement cycles would reduce system complexity and improve the feasibility of large-scale quantum advantage. The ultrametric geo
  Full text (https://papers.qnfo.org/papers/ultrametric-geometry-as-passive-quantum-error-correction-bruhat-tits-qudit-codes), excerpts of its own sections:
  § 1. Introduction: Scalable quantum computing is presently blocked by the overhead of active quantum error correction, which requires repeated syndrome extraction, low-latency decoding, and large ancilla resources. This overhead directly limits the size of computations that can be run on near-term hardware and inflates the thermodynamic cost of error-correction cycles [8]. [...]
  § 5. Results: All numbers below are computed in Section 4 with fully shown arithmetic; none are simulation outputs. **Code parameters (exact).** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$. The distance of the ball code is $d=2t+1$ (Proposition 1, conditional on the branch-permutation symmetry of the encoder). The flagship block $p=3$, $t=1$ has $n_1=5$ qudits, $d=3$, and rate $1/5$. **Passive logical failure (exact computation, $p=3$, $t=1$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ per protection epoch, a suppression factor $\varepsilon/P_{\mathrm{pass}}\approx100.2$ over an unencoded qudit. **Passive logical failure ($p=3$, $t=2$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ per protection epoch (leading term $6.705\times10^{-7}$ plus a $\approx0.35\%$ correction from the weight-4 term). **Active baseline projection.** $P_{\mathrm{act}}\approx4.07\times10^{-5}$ under assumptions (A1)–(A4), giving a $\approx4.08$-fold advantage for the passive scheme. [...]
  § 6. Discussion: **What is proved versus assumed.** Lemma 1 (nesting/disjointness of equal-radius balls) is proved, and the shell-count formula for $n_t$ is an exact combinatorial identity. Proposition 1, however, is conditional: the branch-permutation symmetry of the code states is a design requirement, and no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed in this paper. If no symmetric encoder exists for a given ball, the weight-$\le t$ correctability claim and the distance $d=2t+1$ fail. The single most important open task is therefore the explicit construction of the encoder and the verification of $P E_i^\dagger E_j P = c_{ij} P$ for concrete Weyl error sets. **Model limitations.** (i) The noise model is independent depolarising noise per vertex qudit per epoch; correlated errors (e.g., a gate fault coupling two neighbouring vertices, or a burst affecting a whole branch) violate independence and could defeat the weight counting on which $P_{\mathrm{pass}}$ rests. [...]
  § 8. Conclusion: We have formalised a passive quantum error-correction scheme in which logical qudits live on balls of the Bruhat–Tits tree $T_{p+1}$, proved a nesting lemma implying that equal-radius balls are nested or disjoint, derived the exact code parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ and the conditional distance $d = 2t+1$, and computed analytically that under independent depolarising noise at $\varepsilon = 10^{-3}$ the flagship $p=3$, $t=1$ block fails with probability $\approx9.98\times10^{-6}$ per epoch, a suppression of $\approx100.2$ over an unencoded qudit and, as an explicitly labeled projection under stated assumptions, a factor $\approx4.08$ over an active distance-3 baseline with noisy syndrome extraction. The scheme's promise is real but conditional on constructing an explicit symmetric encoder; we have stated the assumptions, the failure modes, and the falsification criteria plainly so that the proposal can be tested rather than taken on trust.
[10] QNFO: Ultrametric Passive Error Correction on \(p\)-ary Bruhat–Tits Trees: Barrier Analysis and Recursive Thresholds | https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis
  Fault‑tolerant quantum computation presently depends on active stabilizer codes such as the surface code, which require repeated syndrome extraction, low‑latency decoding, and large ancilla overhead. A fundamentally different approach would encode logical qubits on the vertices of a regular odd‑\(p\) Bruhat–Tits tree and let the ultrametric geometry enforce a passive error barrier. The gap is the 
  Full text (https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis), excerpts of its own sections:
  § 1. Introduction For example, Active stabilizer codes such as the surface code require repeated syndrome extraction and substantial ancilla overhead. The engineering cost of real‑time syndrome extraction, low‑latency decoders, and ancilla refresh limits scalability.: If logical information could instead be stored in a geometry that *passively* blocks error propagation, the need for active cycles would disappear. [...]
  § 2. Background and Related Work Continuous‑time quantum error correction (CTQEC) treats noise and correction as simultaneous continuous processes; its subsystem‑principle formulation shows that a correctable subsystem \(\mathcal{H}^{A}\) can be isolated by a CPTP map \(\mathcal{R}\) [1]. While CTQEC remains an active research direction, it does not provide a passive geometric barrier.: Entanglement‑assisted quantum error‑correcting codes (EAQECCs) extend the stabilizer formalism by allowing pre‑shared ebits, thereby improving rate or distance [2]. EAQECCs still rely on active syndrome measurement and therefore do not address the passive‑correction goal. Ultrametrics are defined by the strong triangle inequality \(d(x,y)\le\max\{d(x,z),d(z,y)\}\) [3]. The strong triangle inequality $d(x,y)\le\max\{d(x,z),d(z,y)\}$ is established in [3]; we model this property as implying that any path connecting two distant vertices must cross a “cut” whose size grows exponentially with the hierarchical level. The foundational textbook on quantum error correction explains that a code can correct any error drawn from a Pauli basis and that the stabilizer formalism yields distance‑\(d\) codes [4]. The three‑bit repetition code illustrates how a majority vote can correct a single‑bit flip, a principle we lift to the tree geometry. [...]
  § 5. Results: | Quantity | Value | Section | |---|---|---| | Barrier height \(B(3)\) | \(8\) | 4.1 | | Barrier height \(B(4)\) | \(16\) | 4.1 | | Logical error bound \(p_{L}(3)\) | \(6.5536\times10^{-4}\) | 4.2 | | Logical error bound \(p_{L}(4)\) | \(4.29\times10^{-7}\) | 4.2 | | Suppression factor (depth 3) | \(\approx6.10\times10^{2}\) | 4.3 | | Suppression factor (depth 4) | \(\approx9.31\times10^{5}\) | 4.3 | | First‑level failure probability (8‑fold vote) | \(0.1736704\) | 4.4 | | Second‑level failure probability | \(5.5489\times10^{-3}\) | 4.4 | | Third‑level failure probability | \(2.905\times10^{-10}\) | 4.4 | | Ball‑code size \(n_{1}\) (p=3) | \(5\) qudits | 4.5 | | Ball‑code size \(n_{2}\) (p=3) | \(17\) qudits | 4.5 | | Ball‑code size \(n_{3}\) (p=3) | \(53\) qudits | 4.5 | All numbers follow from the arithmetic of Section 4.
  § 6.2 Failure Modes and Falsification The main hypothesis (call it Hypothesis Q) is that the ultrametric geometry enforces an exponential error barrier for quantum errors. It would be falsified if any of the following observations were made:: 1. **Empirical logical error rate does not decay with depth**: Measuring \(p_{L}(d)\) for increasing \(d\) and finding a depth‑independent plateau would contradict (4). 2. **Coherent error paths survive majority voting**: Demonstrating that a unitary error acting on a branch can be reconstructed at the root despite majority‑vote decoding would invalidate the classical‑to‑quantum barrier transfer. 3. **Correlated multi‑qudit errors exceed the majority threshold**: If a physical error mechanism flips \(\lceil p/2\rceil\) edges simultaneously with non‑negligible probability, the barrier exponent is overestimated.
[11] QNFO: Ultrametric Passive Fault Tolerance on Bruhat–Tits Trees: Analytic Derivation and Quantitative Projections | https://papers.qnfo.org/papers/ultrametric-passive-fault-tolerance-on-bruhat-tits-trees-analytic-deriv-93ee94f3
  Quantum computing today is limited by the large physical‑to‑logical qubit overhead required for active error correction, which demands frequent syndrome extraction, low‑latency decoding, and extensive ancilla resources. A proposed alternative encodes logical information on the vertices of a $p$‑adic Bruhat–Tits tree, exploiting the ultrametric strong triangle inequality to confine error propagatio
  Full text (https://papers.qnfo.org/papers/ultrametric-passive-fault-tolerance-on-bruhat-tits-trees-analytic-deriv-93ee94f3), excerpts of its own sections:
  § 1. Introduction Current quantum processors require active stabiliser codes such as the surface code to achieve fault tolerance. Implementing these codes entails a physical‑to‑logical qubit overhead on the order of $10^{2}$–$10^{4}$ (assumption), repeated syndrome extraction, and real‑time decoding, all of which inflate hardware cost, power consumption, and latency. For a cloud‑based quantum service provider (e.g., Tianyan) the overhead translates into higher subscription fees and limits the size of problems that can be run within a given budget. A design that could passively suppress logical errors without ancilla qubits or syndrome processing would therefore lower the economic barrier to scalable quantum computing and enable deeper circuits on near‑term hardware.: The ultrametric passive fault‑tolerance proposal asserts that encoding logical qubits on the balls of a Bruhat–Tits tree creates an energy barrier $E_{\text{barrier}}(d)=2^{d}$ that grows exponentially with tree depth $d$, thereby confining error propagation. If correct, a modest tree of depth $t=1$ would need only five physical qudits to protect a logical qubit, achieving a logical error probability of order $10^{-5}$ at a physical depolarising rate of $10^{-3}$—a two‑order‑of‑magnitude improvement over unencoded qubits and comparable to a distance‑3 surface code. **Contributions.** - **C1.** Derivation of the exact ball‑size formula $n_{t}=1+(p+1)\frac{p^{t}-1}{p-1}$ (Section 3). - **C2.** Proof that the ultrametric strong triangle inequality forces error paths to climb an exponential barrier $E_{\text{barrier}}(d)=2^{d}$ (Section 3). - **C3.** Closed‑form expression for the passive logical failure probability $P_{\mathrm{pass}}$ under independent depolarising noise and its evaluation for $p=3$, $t=1,2$ (Section 4). [...]
  § 5. Results: | Quantity | Value | Section | |----------|-------|---------| | Ball size $n_{1}$ ( $p=3$, $t=1$ ) | $5$ qudits | 4.1 | | Passive logical failure $P_{\mathrm{pass}}$ ( $t=1$, $\varepsilon=10^{-3}$ ) | $5.992003\times10^{-6}$ | 4.3 | | Suppression factor $S$ | $166.9$ | 4.4 | | Ball size $n_{2}$ ( $p=3$, $t=2$ ) | $17$ qudits | 4.5 | | Passive logical failure $P_{\mathrm{pass}}^{(2)}$ ( $t=2$, $\varepsilon=10^{-3}$ ) | $3.997\times10^{-9}$ | 4.5 | | Energy barrier $E_{\text{barrier}}(3)$ | $8$ (arb. units) | 4.6 | | Energy barrier $E_{\text{barrier}}(5)$ | $32$ (arb. units) | 4.6 | All numbers are derived analytically from the model assumptions listed in Section 3; no simulation data are used.
  § (c) Minimal Next Experiment: A prototype consisting of **five** $^{87}$Rb atoms trapped in an optical tweezer array, arranged in a $p=3$ tree of depth $t=1$, would test the model. The experiment would: 1. Initialise each atom in a chosen hyperfine level (encoding a qudit). 2. Apply calibrated depolarising noise with $\varepsilon=10^{-3}$. 3. Perform a majority‑vote readout of the root after one protection epoch. Observing a logical error rate $>2\times10^{-5}$ would falsify the model; a rate $\le10^{-5}$ would support it.