# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound (Revised)

## Abstract

Active quantum error correction (QEC) dominates the overhead of scalable quantum processors: repeated syndrome extraction, low-latency decoding, and large ancilla counts inflate hardware cost and energy consumption, and a passive alternative that removes measurement cycles would reduce system complexity. The ultrametric geometry of the $p$-adic numbers satisfies the strong triangle inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$, which forces balls in the associated Bruhat–Tits tree $T_{p+1}$ to be either nested or disjoint; whether this property can be turned into a genuine quantum error-correcting code with provable parameters is an open question. We define a ball code on $T_{p+1}$, prove a nesting lemma, and derive the exact code size $n_t=1+(p+1)(p^{t}-1)/(p-1)$ together with a conditional distance $d=2t+1$ that rests on a stated symmetry assumption on the encoder. We compute analytically the passive logical failure probability under independent depolarising noise with physical error rate $\varepsilon=10^{-3}$, obtaining $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, a suppression factor of $\approx100.2$ over an unencoded qudit, and $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ for $t=2$. As an explicitly labeled projection under stated assumptions, we obtain a $\approx4.08$-fold advantage over an active distance-3 baseline with measurement error $\varepsilon_m=\varepsilon$, and a pseudo-threshold $\varepsilon_{\mathrm{th}}\approx0.3245$ under a dominant-term approximation. All quantitative results are derived step by step; the conditional nature of the distance claim, the model limitations, and falsification criteria are stated plainly.

## 1. Introduction

Scalable quantum computing is presently blocked by the overhead of active quantum error correction, which requires repeated syndrome extraction, low-latency decoding, and large ancilla resources. This overhead directly limits the size of computations that can be run on near-term hardware and inflates the thermodynamic cost of error-correction cycles; the physical-to-logical overhead of surface-code-class schemes has been placed (as an explicit assumption in the prior literature on this proposal) in the range $10^{2}$–$10^{4}$ [11]. If a hardware platform could store logical information in a structure that *passively* blocks error propagation, the need for active cycles would disappear, reducing both hardware complexity and energy consumption. The decision that would change if the present result holds is concrete: a quantum-memory architect could allocate qudits to a static geometric layout instead of to measurement and feedback circuitry, and the resource question shifts from "how many ancillas and how fast a decoder" to "does a symmetric encoder exist on this geometry."

The non-Archimedean (ultrametric) geometry of the $p$-adic numbers provides a candidate structure. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality
$$\|x+y\|_p\le\max\bigl(\|x\|_p,\|y\|_p\bigr),$$
which implies that any two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has degree $p+1$. By placing qudits at the vertices and encoding a logical qudit into a ball $B_t(v_0)$, we obtain a geometry in which local errors cannot coherently add across distinct branches. Hecke operators, which average over the $p+1$ forward neighbours of each vertex, serve as a natural gate set that respects the tree locality.

This paper is a post-publication revision of an earlier version of the same proposal [9]. Relative to that version it strengthens the derivations, states more carefully what is proved versus assumed, and places the quantitative claims in dialogue with the barrier-analysis literature on the same tree geometry [8], [10], [11]. No simulation, measurement, or hardware experiment is performed or reported here; every quantitative claim is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

**Contributions.**
- Lemma 1 (nesting/disjointness of equal-radius balls) with its proof, and the exact code-size formula $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ (Section 4.1).
- Proposition 1: correctability of all weight-$\le t$ error sets and conditional distance $d=2t+1$, with the proved-versus-assumed split stated explicitly (Section 4.2).
- Analytic passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, $\varepsilon=10^{-3}$, and $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ for $t=2$, each with fully shown arithmetic (Section 4.3).
- A labeled projection of a $\approx4.08$-fold advantage over an active distance-3 baseline under assumptions (A1)–(A4), and a pseudo-threshold $\varepsilon_{\mathrm{th}}\approx0.3245$ under a dominant-term approximation (Sections 4.4 and 4.5).
- A reconciliation of the failure-probability values reported across the prior literature on this proposal, resolved by explicit arithmetic (Section 4.3).

The nesting structure and the binomial failure computation may also inform passive-protection analyses for other hierarchical physical systems, and the qudit framing connects to the growing engineering literature on multilevel quantum processors [3].

## 2. Background and Related Work

We review the literature that directly informs the construction, citing specific points from each source.

**Continuous-time QEC.** Continuous-time quantum error correction treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, and analyses them from the point of view of the subsystem principle, which states that protected quantum information resides in a subsystem $\mathcal{H}^{A}$ of the system Hilbert space, with correctability defined by the existence of a CPTP recovery map $\mathcal{R}$ such that $\mathrm{Tr}_{B}\{(\mathcal{P}^{AB}\circ\mathcal{R}\circ\mathcal{E})(\sigma)\}=\mathrm{Tr}_{B}\{\sigma\}$ for all states in the code subsystem [1]. Its outlook section notes that further research is needed to construct optimal CTQEC protocols and that a quasi-equilibrium code-space fidelity can be used to estimate performance under the quantum-jump model [1]. Our passive scheme shares the motivation of reducing discrete measurement rounds but seeks a geometry-based containment that eliminates any feedback operation; the subsystem principle is compatible with our ball-code construction, since a geometric code space is a special case of a correctable subsystem.

**Entanglement-assisted codes.** Entanglement-assisted quantum error-correcting codes (EAQECCs) extend the stabilizer formalism by allowing the sender to append pre-shared ebits as well as ancillas before the encoding unitary, and their conclusion states that this allows construction of quantum codes from classical linear codes without imposing the dual-containing constraint, while entanglement can increase either the rate of communication or the number of correctable errors [2]. Our codes are not entanglement-assisted; the protection mechanism is purely geometric, and no shared entanglement is consumed. The contrast is instructive: EAQECCs buy code parameters with a physical resource (ebits), whereas the present proposal attempts to buy them with geometry, and both routes remain subordinate to the requirement that a concrete encoder exist.

**Qudit algorithms.** Efficient implementation of quantum algorithms on multilevel systems is addressed by a transpilation approach in which a qubit circuit is mapped onto qudit hardware; the discussion section establishes scalability by showing that transpiling a single-, two-, or multi-qubit gate grows no more than polynomially with the number of qubits affected, that whole-circuit transpilation grows linearly in the number of gates, and that a greedy mapping-finder algorithm of $\mathcal{O}(n^{3})$ complexity is shown for qudit dimensions $4\le d\le 7$ [3]. The same work demonstrates a $6$-qubit circuit realized with four $4$-level qudits with a considerably smaller number of two-particle operations than a straightforward qubit-based implementation [3]. This motivates the use of qudits of dimension $p$ as natural carriers for the tree-based code: the hardware context for small-dimensional qudits is actively developed, so a code whose natural carrier is the qutrit ($p=3$) is not merely a formal object.

**Classical-to-quantum coding surveys.** Surveys of error-correcting codes establish the shared skeleton of classical and quantum coding: redundancy is added by an invertible encoding process, a syndrome is measured, and errors are corrected, with similar conditions for error detectability and correctability in both settings [4]. The same survey records that quantum code construction had migrated to stabilizer codes and to nonbinary codes, which supports treating a qudit (nonbinary) code as a natural object rather than an exotic one [4]. This supplies the conceptual baseline — redundancy plus syndrome measurement — against which the passive scheme defines itself by removing the measurement step.

**Foundations of QEC.** The foundational treatment of quantum computing and error correction shows that general noise and relaxation of a set of two-state quantum systems can always be understood as a combination of Pauli operators acting on the system, and that each QEC code corrects a subset of these errors [5]. It also recalls the historical anchor points: Shor's 9-qubit code protecting a single qubit against general errors, Steane's 7-qubit construction, and the Knill–Laflamme framework describing the requirements for quantum error-correcting codes [5]. We adopt exactly this Pauli-expansion picture for the error model on the tree: vertex-localised Weyl operators $X^{a}Z^{b}$, and the Knill–Laflamme conditions as the correctness criterion.

**Operator-algebra QEC.** Operator-algebra quantum error correction (OAQEC) generalizes Gottesman's stabilizer formalism and Poulin's operator/subsystem formulation; its stabilizer construction generates hybrid classical-quantum stabilizer codes and characterizes which sets of Pauli errors are correctable for a code determined by a stabilizer subgroup, gauge and logical operators, and coset representatives [7]. The introduction of that work records that OQEC brought together traditional QEC with passive notions such as decoherence-free subspaces and noiseless subsystems [7]. This makes OAQEC the natural analytical lens for the present proposal: a passive geometric code, if it exists, should be expressible in the OAQEC framework, and the gauge-group structure of [7] is a candidate language for the encoder we leave open.

**Ultrametric barrier analysis on Bruhat–Tits trees.** Three prior papers in this line supply the quantitative context that the present revision engages. The first derives, for the same ball-code family, the code sizes $n_1=5$, $n_2=17$, $n_3=53$ for $p=3$, the passive failure probabilities $P_{\mathrm{pass}}=9.98\times10^{-6}$ at $\varepsilon=10^{-3}$ for $t=1$ and $P_{\mathrm{pass}}^{(2)}=6.73\times10^{-7}$ for $t=2$, and additionally an energy-barrier analysis with $B(3)=8$, $B(4)=16$, logical-error bounds $p_L(3)=6.5536\times10^{-4}$ and $p_L(4)=4.295\times10^{-7}$ at $p_{\mathrm{err}}=0.40$, thermal bounds $p_L(3)\le3.35\times10^{-4}$, $p_L(5)\le1.27\times10^{-14}$, $p_L(10)\le10^{-444.7}$, and a cooling-budget projection of a per-site gap $\Delta\ge1.727\,k_{\mathrm{B}}T$ to reach $10^{-12}$ logical error at depth 4 [8]. The second develops the barrier picture further: it models the strong triangle inequality as implying that any path connecting two distant vertices must cross a "cut" whose size grows exponentially with the hierarchical level, reports barrier heights $B(3)=8$ and $B(4)=16$, logical-error bounds $p_L(3)=6.5536\times10^{-4}$ and $p_L(4)=4.29\times10^{-7}$ at $p_{\mathrm{err}}=0.40$, suppression factors $\approx6.10\times10^{2}$ (depth 3) and $\approx9.31\times10^{5}$ (depth 4), and a recursive majority-vote cascade with first-, second-, and third-level failure probabilities $0.1736704$, $5.5489\times10^{-3}$, and $2.905\times10^{-10}$ [10]. Its falsification section defines Hypothesis Q — that the ultrametric geometry enforces an exponential error barrier for quantum errors — and names three observations that would falsify it, including a depth-independent plateau in $p_L(d)$ and coherent error paths that survive majority voting [10]. The third reports the same ball-size formula, a passive failure probability $P_{\mathrm{pass}}=5.992003\times10^{-6}$ at $t=1$, $\varepsilon=10^{-3}$ with suppression factor $166.9$, and $P_{\mathrm{pass}}^{(2)}=3.997\times10^{-9}$ at $t=2$, together with an energy barrier $E_{\text{barrier}}(d)=2^{d}$ [11]. Section 4.3 of the present paper resolves the numerical divergence between [8] and [11] by explicit arithmetic.

**The immediately preceding version.** The version of this paper under revision [9] already contains the nesting lemma, the code-size formula, the conditional distance $d=2t+1$, the passive failure computation $P_{\mathrm{pass}}\approx9.98\times10^{-6}$, the active-baseline projection $\approx4.08$, and the pseudo-threshold $\approx0.3245$, and it flags that Proposition 1 is conditional on a branch-permutation symmetry of the encoder [9]. The present revision keeps all of that structure, sharpens the proofs, adds the reconciliation against [8], [10], [11], and strengthens the discussion of what would falsify the claims.

No cited source derives the ball-code parameters $n_t$ and the distance $d=2t+1$ together with a Knill–Laflamme proof for such codes; that combination, with its conditional status made explicit, is the contribution of the present work.

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

The proof uses two facts, both standard for trees and ultrametrics: the four-point (median) property of trees, and the strong triangle inequality. The strong triangle inequality is the same inequality that [10] takes as its starting point, modeling it as a cut whose size grows with hierarchical level; here it is used in its exact combinatorial form, which is what allows the weight-counting arguments of Section 4.

### 3.2 The code

A logical qudit of dimension $p$ (matching the tree's branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:
$$
n_t = 1 + \sum_{k=1}^{t}(p+1)p^{k-1}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$
The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level. We state this branch-permutation symmetry as a design requirement and flag it as an assumption wherever it is used; explicit state vectors, stabilizer generators, and logical operators are not constructed in this paper, and Section 6 discusses the consequences. Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbours of each vertex; they are local in the tree metric (each couples a qudit only to its $p+1$ neighbours), and the Hecke algebra is commutative, so gate ordering within a ball is not a fault-tolerance hazard of the usual kind.

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
P\,E_i^{\dagger}E_j\,P = c_{ij}\,P.
$$
This is the general theoretical framework for the requirements of quantum error-correcting codes recalled in [5], and it is the same condition whose stabilizer-level generalization to the operator-algebra setting is formulated in [7]. Our task is to show the geometry enforces this for all error sets of weight $\le t$, conditional on the encoder symmetry.

### 3.5 Computational method

All quantitative results are obtained by closed-form combinatorics and explicit numerical evaluation of the resulting expressions, with every arithmetic step shown in Section 4. No simulation, measurement, or hardware experiment is performed or reported; the comparison to active correction in Section 4.4 is a projection under stated assumptions, and the pseudo-threshold in Section 4.5 is a projection under a stated dominant-term approximation. Where prior papers in this line report different numerical values for the same quantity, we recompute from first principles and state which value the arithmetic supports.

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

These values agree with those reported in [8], [10], and [11], all of which list $n_1=5$, $n_2=17$, $n_3=53$ for $p=3$.

### 4.2 Correctability and distance (proposition)

**Proposition 1.** The ball code on $B_t(v_0)$ corrects every error set of weight $\le t$, hence has distance $d=2t+1$.

*Proof sketch.* (i) **Correctability.** Let $E,F$ be error sets with $|E|,|F|\le t$, supported on vertex subsets $S_E,S_F\subseteq B_t(v_0)$. By Lemma 1, the sub-balls generated by the error supports are either nested or disjoint. If $S_E$ and $S_F$ lie in disjoint sub-balls, then $E^{\dagger}F$ moves amplitude between orthogonal branch sectors, so $P\,E^{\dagger}F\,P=0$. If they lie in the same nested chain, the code's branch-permutation symmetry (Section 3.2) makes $P\,E^{\dagger}F\,P=c_{EF}P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [7].

(ii) **Distance.** Errors of weight $\le t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbour $v'$, which is orthogonal to the code space, so weight-$(t+1)$ errors are detectable but not correctable. Hence $d=2t+1$. $\square$

We flag what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch-permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d=2t+1$ follow. This conditional status is the same one stated in the preceding version [9], and it is the single most important caveat on the whole proposal.

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

**Reconciliation with prior values.** The preceding version [8] reports the same value $P_{\mathrm{pass}}=9.98\times10^{-6}$ and suppression $\approx100.2$ for $t=1$, while [11] reports $P_{\mathrm{pass}}=5.992003\times10^{-6}$ and suppression $166.9$ for the same nominal parameters. We take the value $9.98\times10^{-6}$ under the convention that the failure probability is the exact binomial tail $1-(1-\varepsilon)^{5}-\binom{5}{1}\varepsilon(1-\varepsilon)^{4}$ evaluated at $\varepsilon=10^{-3}$, which the arithmetic above reproduces step by step; the alternative value in [11] is not reproducible from the stated binomial model and we therefore do not adopt it. The same divergence appears at $t=2$: [8] reports $6.73\times10^{-7}$ and [11] reports $3.997\times10^{-9}$; the computation below supports the former.

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
  