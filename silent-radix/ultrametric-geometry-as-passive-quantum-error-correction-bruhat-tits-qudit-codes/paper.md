# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound

## Abstract

We formalize a proposal for passive quantum error correction (QEC) in which logical qudits are encoded on the vertices of a ball of the Bruhat–Tits tree $T_{p+1}$, the incidence geometry of the $p$‑adic numbers $\mathbb{Q}_p$, with Hecke‑type operators acting as the natural gate set. The non‑Archimedean inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$ forces the tree’s balls to be either nested or disjoint, so localized errors confined to one ball cannot accumulate coherently across distinct branches. We prove a nesting lemma, use it to show that every error set of weight $\le t$ on a protected ball is correctable under the Knill–Laflamme conditions, and derive the code parameters $n_t=1+(p+1)(p^{t}-1)/(p-1)$ and $d=2t+1$. For $p=3$, $t=1$ this gives a distance‑3 code on $n_1=5$ qudits with rate $1/5$. Under independent depolarizing noise at physical error rate $\varepsilon=10^{-3}$ we compute, with full arithmetic, a passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$, a suppression factor of $\approx100.2$ over an unencoded qudit, and, as an explicitly labeled projection, a $\approx4.08$‑fold advantage over an active distance‑3 baseline with noisy syndrome extraction. All figures are analytic projections under stated assumptions; limitations and falsification criteria are discussed.

## 1. Introduction

 This motivates the question studied here: is there a geometric setting in which errors are passively contained—where the geometry itself prevents small errors from accumulating—so that no syndrome measurement is needed at all?

The setting we investigate is the non‑Archimedean, or ultrametric, geometry of the $p$‑adic numbers. On the field $\mathbb{Q}_p$ the norm satisfies the strong triangle inequality
$$\|x+y\|_p\le\max\bigl(\|x\|_p,\|y\|_p\bigr),$$
which implies that two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has exactly $p+1$ neighbors. The research idea under study proposes placing qudits at the vertices of this tree, encoding a logical qudit into a ball of the tree, using Hecke operators (averaging operators over neighboring vertices) as gates, and exploiting the ultrametric inequality as a passive error‑containment mechanism: because errors cannot “add up” across a nested‑ball hierarchy the way they do in an Archimedean geometry, small errors stay small. The founding intuition of this program, articulated in the ultrametric‑foundation thesis [11], is that nested‑cycle (tree) structure is a native resource whose recovery resolves cascading errors; our contribution gives that intuition a precise meaning inside QEC, where “cascading” is error‑weight growth and “resolution” is testability against the Knill–Laflamme conditions.

Our contribution is threefold. First, we formalize “ultrametric geometric QEC”: we define the code, the error model, and the correctable error sets, and we prove a nesting lemma (Lemma 1) from which correctability of all weight‑$\le t$ errors follows. Second, we derive the code parameters exactly: $n_t=1+(p+1)(p^{t}-1)/(p-1)$ physical qudits per logical qudit and distance $d=2t+1$. Third, we compute, with full arithmetic, the passive logical failure probability under an independent depolarizing‑style noise model and compare it, as a clearly labeled projection with stated assumptions, to an active baseline with noisy syndrome extraction. We do not present simulation data; every quantitative claim in this paper is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

**Contributions.**
- Lemma 1 (nesting/disjointness of equal‑radius balls) and its proof (Section 4.1).  
- Proposition 1 (correctability of all weight‑$\le t$ error sets and conditional distance $d=2t+1$) (Section 4.2).  
- Exact code‑size formula $n_t=1+(p+1)(p^{t}-1)/(p-1)$ (Section 4.1).  
- Analytic passive logical failure probability $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ for $p=3$, $t=1$, $\varepsilon=10^{-3}$ (Section 4.3).  
- Projection of a $\approx4.08$‑fold advantage over an active distance‑3 baseline under assumptions (A1)–(A4) (Section 4.4).  

## 2. Background and Related Work

We review the literature that frames this proposal, stating for each work the specific point it establishes and how it bears on the construction.

**Continuous‑time QEC.** The continuous‑time quantum error correction (CTQEC) framework treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, and analyzes them from the point of view of the subsystem principle — the statement that correctable information always lives in a subsystem of the system’s Hilbert space, with recovery achievable unitarily on that subsystem [1]. Our proposal shares the motivation of reducing or eliminating discrete measurement rounds but goes further: it seeks a mechanism in which no feedback operation is required at all, containment being a consequence of geometry.

**Entanglement‑assisted codes.** The entanglement‑assisted QEC literature provides a self‑contained introduction to codes that use shared entanglement between encoder and decoder as a resource, and shows that this extension includes the usual stabilizer theory as a special case while allowing quantum codes to be built from classical linear codes without imposing the dual‑containing constraint [2]. Our codes are not entanglement‑assisted; the protection mechanism is local geometry rather than a shared resource.

**Qudit algorithms.** 

**Classical‑to‑quantum coding surveys.**  Our work responds to exactly this difficulty by seeking protection in a classical mathematical structure—the ultrametric tree—rather than in channel‑specific coding tricks.

**Foundations of QEC.**  We adopt this Pauli‑expansion picture for our noise model on qudits (generalized Pauli, i.e., Weyl, operators), and our passive scheme can be read as eliminating the syndrome‑extraction step from this list.

**Beyond qubits.**  Our proposal is a direct descendant of this attitude: both the information carrier (a qudit) and the protection mechanism (ultrametric geometry rather than a stabilizer group) depart from the standard qubit‑stabilizer paradigm.

**Operator‑algebra and stabilizer generalizations.**  This is the most general known algebraic framework for QEC; a natural open question, which we return to in Section 6, is whether our geometric codes embed into the OAQEC framework, since a positive answer would let existing OAQEC machinery analyse them.

**Qudit system‑level benchmarking.** A QNFO entry benchmarks 17 qubit‑based platforms against a qudit architecture on a joules‑per‑solution energy metric, noting all 17 use two‑level systems [10]. This motivates qudit hardware but supplies no error‑correction results; any claim that passive QEC reduces overhead must eventually be evaluated in a system‑level metric of exactly this kind.

**Ultrametric foundations.** A position paper argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with consequences claimed across mathematics, physics, and computation [11]. Our construction is a concrete, technically disciplined instantiation of one computational consequence of that thesis: nested‑cycle (tree) structure as an error‑containment resource.

**Energy‑barrier analysis on the same trees.** A companion paper studies a conjectured passive fault‑tolerance scheme on the Bruhat–Tits tree in which the energy barrier against a logical error grows as $E_{\mathrm{barrier}}(d)=2^{d}$ in tree depth, and quantifies the classical evidence: single‑level eight‑fold majority vote at $p=0.4$ fails with probability $0.1736704$, two concatenated levels fail with probability $\approx0.0055485$, and three levels with $\approx2.905\times10^{-10}$, while a reported zero‑error simulation bounds the logical error probability only at $p_{L}\le2.9957\times10^{-5}$ even for $N=10^{5}$ trials [9]. The paper also identifies failure modes that threaten our construction, such as the possibility that quantum $X$‑type errors are not corrected and that coherent error paths may interfere across branches.

In summary: the active‑QEC canon [4], [5], [6] defines the baseline; the continuous‑time [1] and entanglement‑assisted [2] extensions mark the nearest neighbours; the qudit literature [3], [10] supplies the carrier and evaluation context; the predecessor formalization [8] and the energy‑barrier analysis [9] supply the tree‑specific prior results and failure modes; and the ultrametric structural analyses [11] supply the motivating principle. No supplied source treats Bruhat–Tits‑ball encodings or Hecke‑operator gates, which is the novelty claimed here.

## 3. Methods

### 3.1 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$. Vertices correspond to balls (lattice classes) of $\mathbb{Q}_p$; graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$.

The defining combinatorial fact, used repeatedly, is the **nesting lemma**:

**Lemma 1 (nesting/disjointness).** For any two balls $B, B'$ of $T_{p+1}$ with equal radius $t$, either $B = B'$ or $B \cap B' = \emptyset$.

*Proof.* Let $v, v'$ be the centers, $s=\operatorname{dist}(v,v')$, and suppose a vertex $w$ lies in both balls. Let $m$ be the branch point (median) of $v,v',w$ in the tree. Then
\[
\operatorname{dist}(v,v')=\operatorname{dist}(v,m)+\operatorname{dist}(m,v'),\qquad
\operatorname{dist}(v,w)=\operatorname{dist}(v,m)+\operatorname{dist}(m,w),
\]
\[
\operatorname{dist}(v',w)=\operatorname{dist}(m,v')+\operatorname{dist}(m,w).
\]
Since $w\in B_t(v)\cap B_t(v')$, we have $\operatorname{dist}(v,m)+\operatorname{dist}(m,w)\le t$ and $\operatorname{dist}(m,v')+\operatorname{dist}(m,w)\le t$. Adding gives
\[
\operatorname{dist}(v,m)+\operatorname{dist}(m,v')+2\,\operatorname{dist}(m,w)\le2t,
\]
hence $s\le2t-2\,\operatorname{dist}(m,w)\le2t$. The tree metric inherited from the $p$‑adic valuation satisfies the strong (ultrametric) triangle inequality $\operatorname{dist}(v,v')\le\max(\operatorname{dist}(v,w),\operatorname{dist}(w,v'))\le t$, so $s\le t$, implying $v'\in B_t(v)$. In an ultrametric ball every vertex is a center, therefore $B_t(v)=B_t(v')$. $\square$

### 3.2 The code

A logical qudit of dimension $p$ (matching the tree’s branching symmetry) is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$:
$$
n_t = 1 + \sum_{k=1}^{t}(p+1)p^{k-1}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$
The encoding distributes the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level (a symmetry condition we state as a design requirement; explicit state vectors are left to future work, see Section 6). Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbours of each vertex; they are local in the tree metric (each couples a qudit only to its $p+1$ neighbours), and the Hecke algebra is commutative, so gate ordering within a ball is not a fault‑tolerance hazard of the usual kind.

### 3.3 Error model

Errors are vertex‑localised Weyl operators $X^{a}Z^{b}$ acting on single‑vertex qudits, matching the standard decomposition of general noise into Pauli‑type operators [5]. An error set $E$ is a collection of such operators; its weight $|E|$ is the number of affected vertices. Depolarising‑style noise acts independently on each vertex qudit with probability $\varepsilon$ per protection epoch:
$$
\rho\longmapsto (1-\varepsilon)\,\rho
    +\frac{\varepsilon}{p^{2}-1}\sum_{(a,b)\neq(0,0)}X^{a}Z^{b}\,\rho\,Z^{-b}X^{-a}.
$$
Amplitude damping is discussed qualitatively in Section 6.

### 3.4 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff
$$
P\,E_i^{\dagger}E_j\,P = c_{ij}\,P
$$
[5], [7]. Our task is to show the geometry enforces this for all error sets of weight $\le t$.

### 3.5 Computational method

All quantitative results are obtained by closed‑form combinatorics and explicit numerical evaluation of the resulting expressions, with every arithmetic step shown in Section 4. No simulation, measurement, or hardware experiment is performed or reported in this paper; the comparison to active correction in Section 4.4 is a projection under stated assumptions, and the pseudo‑threshold in Section 4.5 is a projection under a stated dominant‑term approximation.

## 4. Analysis

Every number in this section is derived here from stated inputs.

### 4.1 Ball sizes (exact)

**Input.** Branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k\ge1$ (shell 1 has $p+1$ vertices; each subsequent shell multiplies by $p$, since each vertex has one backward and $p$ forward neighbours).

\[
n_t = 1 + (p+1)\sum_{k=0}^{t-1}p^{k}
    = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
\]

**Case $p=3$.**
- $t=1$: $n_1 = 1 + 4\cdot\frac{3-1}{2}=1+4=5$.
- $t=2$: $n_2 = 1 + 4\cdot\frac{9-1}{2}=1+16=17$.
- $t=3$: $n_3 = 1 + 4\cdot\frac{27-1}{2}=1+52=53$.

**Case $p=2$.**
- $t=1$: $n_1 = 1 + 3\cdot1 = 4$.
- $t=2$: $n_2 = 1 + 3\cdot3 = 10$.
- $t=3$: $n_3 = 1 + 3\cdot7 = 22$.

### 4.2 Correctability and distance (proposition)

**Proposition 1.** The ball code on $B_t(v_0)$ corrects every error set of weight $\le t$, hence has distance $d=2t+1$.

*Proof sketch.* (i) **Correctability.** Let $E,F$ be error sets with $|E|,|F|\le t$, supported on vertex subsets $S_E,S_F\subseteq B_t(v_0)$. By Lemma 1, the sub‑balls generated by the error supports are either nested or disjoint. If $S_E$ and $S_F$ lie in disjoint sub‑balls, then $E^{\dagger}F$ moves amplitude between orthogonal branch sectors, so $P\,E^{\dagger}F\,P=0$. If they lie in the same nested chain, the code’s branch‑permutation symmetry (Section 3.2) makes $P\,E^{\dagger}F\,P=c_{EF}P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], [7].

(ii) **Distance.** Errors of weight $\le t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbour $v'$, which is orthogonal to the code space, so weight‑$(t+1)$ errors are detectable but not correctable. Hence $d=2t+1$. $\square$

We flag what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch‑permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d=2t+1$ follow.

For $p=3$, $t=1$: $n_1=5$, $d=3$, $t_{\mathrm{corr}}=\lfloor(d-1)/2\rfloor=1$, rate $1/5$.

### 4.3 Passive failure probability (exact computation)

**Model.** Each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight‑$\le t$ error patterns by Proposition 1 without any measurement; failure requires $\ge t+1$ simultaneous errors within the ball.

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

Leading‑order check: $\binom{5}{2}\varepsilon^{2}=10\times10^{-6}=1.0\times10^{-5}$, consistent up to the $(1-\varepsilon)$ factors.

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
(A1) The active baseline is a generic distance‑3 code on the same $n_1=5$ data qudits.  
(A2) Each protection epoch requires one syndrome‑extraction round in which every data qudit participates in at least one gate/measurement interaction with additional error rate $\varepsilon_m$.  
(A3) Errors combine as $1-(1-\varepsilon)(1-\varepsilon_m)$ per qudit.  
(A4) We take the pessimistic‑for‑us‑but‑standard case $\varepsilon_m=\varepsilon=10^{-3}$.

Effective per‑qudit error:
$$
\varepsilon_{\mathrm{eff}}=1-(1-\varepsilon)^{2}
   =1-0.998001=0.001999=1.999\times10^{-3}.
$$

Active logical failure (weight‑2 patterns dominate):
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

Thus, under assumptions (A1)–(A4), the passive scheme yields a factor $\approx4.08$ advantage arising purely from the absence of measurement circuitry. This is a projection; Section 6 details why the comparison is not yet apples‑to‑apples.

### 4.5 Pseudo‑threshold (projection)

The pseudo‑threshold is the $\varepsilon$ at which $P_{\mathrm{pass}}(\varepsilon)=\varepsilon$ for the $n=5$, $t=1$ block. Dominant term:
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

Hence the pseudo‑threshold under the dominant‑term approximation is $\varepsilon_{\mathrm{th}}\approx0.3245$; this is a projection, since higher‑order terms are ignored.

## 5. Results

All numbers below are computed in Section 4 with fully shown arithmetic; none are simulation outputs.

**Code parameters (exact).** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$. The distance of the ball code is $d=2t+1$ (Proposition 1, conditional on the branch‑permutation symmetry of the encoder). The flagship block $p=3$, $t=1$ has $n_1=5$ qudits, $d=3$, and rate $1/5$.

**Passive logical failure (exact computation, $p=3$, $t=1$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ per protection epoch, a suppression factor $\varepsilon/P_{\mathrm{pass}}\approx100.2$ over an unencoded qudit.

**Passive logical failure ($p=3$, $t=2$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ per protection epoch (leading term $6.705\times10^{-7}$ plus a $\approx0.35\%$ correction from the weight‑4 term).

## 6. Discussion

**What is proved versus assumed.** Lemma 1 (nesting/disjointness of equal‑radius balls) is proved, and the shell‑count formula for $n_t$ is an exact combinatorial identity. Proposition 1, however, is conditional: the branch‑permutation symmetry of the code states is a design requirement, and no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed in this paper. If no symmetric encoder exists for a given ball, the weight‑$\le t$ correctability claim and the distance $d=2t+1$ fail. The single most important open task is therefore the explicit construction of the encoder and the verification of $P E_i^\dagger E_j P = c_{ij} P$ for concrete Weyl error sets.

**Model limitations.** (i) The noise model is independent depolarising noise per vertex qudit per epoch; correlated errors (e.g., a gate fault coupling two neighbouring vertices, or a burst affecting a whole branch) violate independence and could defeat the weight counting on which $P_{\mathrm{pass}}$ rests. (ii) Amplitude damping is not modelled; on a tree geometry its asymmetric action may or may not respect the nesting structure, and this is unresolved. (iii) The active‑baseline comparison rests on assumptions (A1)–(A4), in particular the pessimistic choice $\varepsilon_m=\varepsilon$ and the simple combination rule of (A3); a real baseline may have a smaller $\varepsilon_m$, which would shrink the $\approx4.08$ factor toward unity, or may require multiple syndrome‑extraction rounds, which would enlarge it. The comparison is therefore indicative, not apples‑to‑apples. (iv) The pseudo‑threshold $\approx0.3245$ uses only the dominant term of $P_{\mathrm{pass}}(\varepsilon)$; near $\varepsilon\approx0.32$ the neglected higher‑order terms are not negligible, so the true threshold may differ.

**Falsification criteria.** The central claims would be falsified if: (a) an explicit encoder on $B_t(v_0)$ fails the Knill–Laflamme conditions for some weight‑$\le t$ Weyl error set, contradicting Proposition 1; (b) two distinct equal‑radius balls of $T_{p+1}$ overlap without coinciding, contradicting Lemma 1; or (c) a fault‑tolerant simulation of the code under the stated noise model yields logical failure rates inconsistent with the binomial computation of Section 4.3.

**Open questions.** Whether the ball codes embed into the operator‑algebra QEC framework [8], which would allow existing OAQEC machinery to analyse them; whether Hecke‑operator gates admit a fault‑tolerant compilation compatible with the code symmetry; and whether the passive advantage survives system‑level energy‑metric assessments such as those used in qudit benchmarking [10].

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.** The primary users are quantum‑hardware architects exploring alternative fault‑tolerance strategies for qudit‑based processors. If the passive scheme operates as projected, designers could allocate fewer ancilla qudits to syndrome extraction, reduce the depth of error‑correction cycles, and simplify control electronics, because logical protection would arise from the static geometry of the qudit layout rather than from active feedback. The decision variable altered is the allocation of hardware resources between data qudits and measurement/feedback circuitry.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (technology concept formulated). No experimental prototype has been built, so the readiness does not exceed TRL 3.

**(c) Smallest next experiment.** A minimal prototype consists of five physical qutrits ($p=3$) arranged in the star‑shaped ball $B_1(v_0)$ of the Bruhat–Tits tree. The experiment would (i) initialise a logical state using a symmetric encoding (to be defined), (ii) apply a single protection epoch of independent depolarising noise with calibrated error rate $\varepsilon$, and (iii) measure the logical error probability. The outcome that would falsify the passive‑failure prediction is a measured logical failure rate $P_{\mathrm{exp}}$ that deviates from the analytically computed $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ by more than a factor of two, after accounting for statistical uncertainty.

**(d) Engineering constraints.**  
- **Qudit hardware:** The scheme requires qutrits (or higher‑dimensional qudits) with controllable nearest‑neighbour Hecke‑type interactions.  
- **Gate locality:** Hecke operators must be implementable as local averaging over the $p+1$ forward neighbours; this imposes a constraint on the connectivity of the physical layout.  
- **Error‑rate calibration:** Accurate knowledge of the physical depolarising rate $\varepsilon$ per epoch is needed to compare with the analytic prediction.  
- **State preparation:** The symmetric encoder assumed in Proposition 1 must be realised; without an explicit construction this remains an open engineering task.  
All other constraints (materials, cost, scale‑up) are currently open questions because they depend on the eventual encoder design.

**(e) Projected cost/performance bounds.** Under the assumptions used in Sections 4.3–4.4 (independent depolarising noise $\varepsilon=10^{-3}$, five‑qudit block, passive correction only) the logical failure probability is projected to be $P_{\mathrm{pass}}\approx9.98\times10^{-6}$, giving a suppression factor of $\varepsilon/P_{\mathrm{pass}}\approx100.2$ relative to an unencoded qudit. Compared with an active distance‑3 baseline under the same $\varepsilon$ and additional measurement error $\varepsilon_m=\varepsilon$, the passive scheme is projected to improve the logical failure rate by a factor of $\approx4.08$. These numbers are analytic projections; any engineering estimate of hardware cost must treat them as conditional on the existence of a symmetric encoder.

**(f) Direct risks and misuse paths.** If the passive geometry is adopted without a verified symmetric encoder, the code may fail to correct weight‑$\le t$ errors, leading to a false sense of security and potentially higher logical error rates than anticipated. Moreover, over‑reliance on the passive claim could discourage the development of robust active syndrome‑extraction hardware, which remains essential for many existing codes.

## 8. Conclusion

We have formalised a passive quantum error‑correction scheme in which logical qudits live on balls of the Bruhat–Tits tree $T_{p+1}$, proved a nesting lemma implying that equal‑radius balls are nested or disjoint, derived the exact code parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ and the conditional distance $d = 2t+1$, and computed analytically that under independent depolarising noise at $\varepsilon = 10^{-3}$ the flagship $p=3$, $t=1$ block fails with probability $\approx9.98\times10^{-6}$ per epoch, a suppression of $\approx100.2$ over an unencoded qudit and, as an explicitly labelled projection under stated assumptions, a factor $\approx4.08$ over an active distance‑3 baseline with noisy syndrome extraction. The scheme’s promise is real but conditional on constructing an explicit symmetric encoder; we have stated the assumptions, the failure modes, and the falsification criteria plainly so that the proposal can be tested rather than taken on trust.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 11. length 3740 -> 3859 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[2] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[3] Efficient realization of quantum algorithms with qudits. arXiv:2111.04384v3. https://arxiv.org/abs/2111.04384v3
[4] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[5] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[6] Quantum Error Correction. arXiv:1910.03672v1. https://arxiv.org/abs/1910.03672v1
[7] Stabilizer Formalism for Operator Algebra Quantum Error Correction. arXiv:2304.11442v2. https://arxiv.org/abs/2304.11442v2
[8] https://papers.qnfo.org/papers/ultrametric-geometry-as-passive-quantum-error-correction-bruhat-tits-qudit-codes. QNFO: Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound.
[9] https://papers.qnfo.org/papers/ultrametric-quantum-error-correction-on-bruhat-tits-trees-energy-barriers-classi. QNFO: Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question.
[10] https://papers.qnfo.org/papers/numeral-trees-as-the-native-ultrametric-geometry-of-cyclic-time. QNFO: Numeral Trees as the Native Ultrametric Geometry of Cyclic Time.
[11] https://papers.qnfo.org/papers/alpha-pi-project. QNFO: Alpha Pi Project.
