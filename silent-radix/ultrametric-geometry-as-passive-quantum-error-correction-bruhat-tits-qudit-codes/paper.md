# Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound (Revised)

## Abstract

Active quantum error correction (QEC) dominates the overhead of scalable quantum processors: repeated syndrome extraction, low-latency decoding, and large ancilla counts inflate hardware cost and energy consumption, and a passive alternative that eliminates measurement cycles would reduce system complexity. The ultrametric geometry of the $p$-adic numbers satisfies the strong triangle inequality $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$, which forces balls in the associated Bruhat–Tits tree $T_{p+1}$ to be either nested or disjoint; whether this property can be turned into a genuine quantum error-correcting code with provable parameters is an open question. We define a ball code on $T_{p+1}$, prove a nesting lemma, and derive the exact code size $n_t=1+(p+1)(p^{t}-1)/(p-1)$ and a conditional distance $d=2t+1$ that holds given a branch-symmetric encoder we do not construct. Under independent depolarising noise at physical error rate $\varepsilon=10^{-3}$ we compute analytically a passive logical failure probability $P_{\mathrm{pass}}=9.980015\times10^{-6}$ for the flagship $p=3$, $t=1$ block ($n_1=5$ qudits), a suppression factor of $100.2$ over an unencoded qudit, and $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ for $t=2$; correcting an arithmetic error in the prior version, the projected advantage over an active distance-3 baseline with measurement error $\varepsilon_m=\varepsilon$ is a factor $\approx3.99$, not $4.08$. All quantitative results are derived step by step, limitations and falsification criteria are stated, and the central claim remains conditional on constructing an explicit encoder.

## 1. Introduction

Scalable quantum computing is presently blocked by the overhead of active quantum error correction, which requires repeated syndrome extraction, low-latency decoding, and large ancilla resources. This overhead directly limits the size of computation that near-term hardware can run and inflates the thermodynamic cost of error-correction cycles; the physical-to-logical qubit overhead of surface-code-style schemes has been estimated, as an explicit assumption, in the range $10^{2}$–$10^{4}$ [11]. If a hardware platform could store logical information in a structure that *passively* blocks error propagation, the need for active cycles would disappear, reducing both hardware complexity and energy consumption, and the design variable would shift from ancilla budget and decoder latency to the static layout of the qudits themselves. The decision that would change if the present result holds is concrete: a quantum-memory architect could allocate qudits to a static geometric layout instead of to measurement and feedback circuitry, and the resource question shifts from "how many ancillas and how fast a decoder" to "does a symmetric encoder exist on this geometry."

The non-Archimedean (ultrametric) geometry of the $p$-adic numbers provides a candidate structure. On the field $\mathbb{Q}_p$ the norm satisfies
$$\|x+y\|_p\le\max\bigl(\|x\|_p,\|y\|_p\bigr),$$
which implies that any two balls are either nested or disjoint. The combinatorial skeleton of this geometry is the Bruhat–Tits tree $T_{p+1}$, a homogeneous tree in which every vertex has degree $p+1$. By placing qudits at the vertices and encoding a logical qudit into a ball $B_t(v_0)$, we obtain a geometry in which local errors cannot coherently add across distinct branches. Hecke operators, which average over the $p+1$ forward neighbours of each vertex, serve as a natural gate set that respects the tree locality.

This paper is a post-publication revision of the version of this work published as [9]. The revision does three things. First, it corrects an arithmetic error in the active-baseline comparison of [9]: the active logical failure probability is $P_{\mathrm{act}}\approx3.98\times10^{-5}$, not $4.07\times10^{-5}$, and the passive advantage is a factor $\approx3.99$, not $4.08$ (Section 4.4). Second, it reconciles a numerical divergence between the binomial computation performed here and the value $P_{\mathrm{pass}}=5.992003\times10^{-6}$ reported for the same model parameters in [11]; we adopt the directly computed binomial value and state the convention behind the choice (Section 4.3). Third, it strengthens the conditional character of the distance claim: Proposition 1 is proved *given* a branch-symmetric encoder, and the explicit encoder remains the single most important open task, as [9] itself already flags in its Discussion.

No simulation, measurement, or hardware experiment is performed or reported in this paper; every quantitative claim is either an exact combinatorial identity, an analytic computation shown step by step, or a projection whose assumptions are stated explicitly.

**Contributions.**
- Lemma 1 (nesting/disjointness of equal-radius balls in $T_{p+1}$) with proof (Section 4.1).
- Proposition 1: conditional correctability of all weight-$\le t$ error sets and distance $d=2t+1$, given a branch-symmetric encoder (Section 4.2).
- Exact code-size formula $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ with tabulated values for $p=2,3$ (Section 4.1).
- Analytic passive logical failure probability $P_{\mathrm{pass}}=9.980015\times10^{-6}$ for $p=3$, $t=1$, $\varepsilon=10^{-3}$, with suppression factor $100.2$, and $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ for $t=2$ (Section 4.3).
- Corrected projection of a $\approx3.99$-fold advantage over an active distance-3 baseline under assumptions (A1)–(A4), and a pseudo-threshold $\varepsilon_{\mathrm{th}}\approx0.3245$ under a dominant-term approximation (Sections 4.4–4.5).

Beyond quantum-memory architecture, the ultrametric confinement mechanism could matter to any hierarchical physical system in which error propagation paths are naturally tree-like, and the qudit framing connects to the growing engineering literature on multilevel quantum processors [3]; the paper supports only that limited transfer, and says so where it is made.

## 2. Background and Related Work

We review the literature that directly informs the construction, citing specific points each source establishes.

**Continuous-time QEC [1].** Continuous-time quantum error correction treats both noise and correction as processes continuous in time, based on continuous weak measurements and feedback, and analyses them from the point of view of the subsystem principle, under which protected information resides in a subsystem $\mathcal{H}^{A}$ of the system Hilbert space and correctability means the existence of a CPTP recovery map $\mathcal{R}$ with $\mathrm{Tr}_{B}\{(\mathcal{P}^{AB}\circ\mathcal{R}\circ\mathcal{E})(\sigma)\}=\mathrm{Tr}_{B}\{\sigma\}$ [1]. Its Outlook section notes that in the quantum-jump model the code-space fidelity reaches a quasi-equilibrium value usable to estimate performance, and that optimal CTQEC protocol construction remains open [1]. Our scheme shares the motivation of reducing discrete measurement rounds but seeks a geometry-based containment that eliminates any feedback operation entirely; a geometric code space is a special case of a correctable subsystem, so the subsystem principle is compatible with the ball-code construction.

**Entanglement-assisted codes [2].** Entanglement-assisted quantum error-correcting codes extend the stabilizer formalism by allowing the sender to append pre-shared ebits as well as ancillas before the encoding unitary, and their conclusion states that this allows construction of quantum codes from classical linear codes without imposing the dual-containing constraint, while entanglement can increase either the rate of communication or the number of correctable errors [2]. EAQECCs still rely on active syndrome measurement, so they do not address the passive-correction goal; our codes are not entanglement-assisted, and the protection mechanism is purely geometric. The contrast is instructive: EAQECCs buy code parameters with a physical resource (ebits), whereas the present proposal attempts to buy them with geometry, and both routes remain subordinate to the requirement that a concrete encoder exist.

**Qudit algorithms [3].** Efficient implementation of quantum algorithms on multilevel systems is supported by a transpilation pipeline whose Discussion establishes that transpiling a single-, two-, or multi-qubit gate grows no more than polynomially with the number of qubits affected, that whole-circuit transpilation grows linearly in the number of gates, and that a greedy mapping-finder algorithm of $\mathcal{O}(n^{3})$ complexity is shown for qudit dimensions $4\le d\le7$; the same work demonstrates a $6$-qubit circuit realized with four $4$-level qudits with a considerably smaller number of two-particle operations than a straightforward qubit-based implementation [3]. This motivates qudits of dimension $p$ as natural carriers for the tree-based code and indicates that qudit control tooling exists to attempt the encoder of Section 4.2, so a code whose natural carrier is the qutrit ($p=3$) is not merely a formal object.

**Classical-to-quantum coding surveys [4].** The survey establishes the shared skeleton of classical and quantum coding: both add redundancy by an invertible encoding process, measure a syndrome, and correct errors, with similar conditions for error detectability and correctability in both settings, and its Conclusions state that modern quantum code construction is based on stabilizer codes and nonbinary codes [4]. This supplies the active, syndrome-based baseline family against which Section 4.4 compares, and makes precise what a passive scheme must eliminate: the syndrome-measurement step itself. It also supports treating a qudit (nonbinary) code as a natural object rather than an exotic one.

**Foundations of QEC [5].** The foundational treatment shows that general noise and relaxation of a set of two-state quantum systems can always be understood as a combination of Pauli operators acting on the system, and that each QEC code corrects a subset of these errors; it recalls the historical anchor points — Shor's 9-qubit code, Steane's 7-qubit construction, and the Knill–Laflamme framework describing the requirements for quantum error-correcting codes [5]. We adopt exactly this picture: our error model decomposes noise into Weyl (generalized Pauli) operators $X^{a}Z^{b}$ on single-vertex qudits, and our correctness proof targets the Knill–Laflamme conditions.

**Operator-algebra QEC [7].** The stabilizer formalism for operator algebra quantum error correction (OAQEC) generalizes Gottesman's stabilizer formulation and Poulin's operator quantum error correction, and its introduction states that OQEC "brought together traditional QEC with passive notions such as decoherence-free subspaces and noiseless subsystems," leading to subsystem codes and advances in fault-tolerant quantum computing [7]. Its Section 4 formulates an error-correction theorem that characterizes, for a code $C=C(\mathcal{S},\mathcal{G}_{0},\mathcal{L}_{0},\mathcal{T}_{0})$ built from a stabilizer subgroup, gauge group, logical operators and coset representatives, exactly which sets of Pauli errors are correctable [7]. This matters here for two reasons. First, OAQEC is the natural analytical lens for a passive proposal, because the framework already contains passive protection (decoherence-free subspaces, noiseless subsystems) as special cases; if the ball code admits an encoder, embedding it in OAQEC would let its correctability theorem be applied directly rather than re-derived. Second, the gauge-group structure of [7] shows how degrees of freedom can be designated as gauge rather than logical, which is one candidate formalization of the branch-permutation symmetry that Proposition 1 below assumes.

**The prior published version [9].** The version of this work published as [9] states the same code parameters ($n_1=5$, $n_2=17$, $n_3=53$ for $p=3$; $n_1=4$, $n_2=10$, $n_3=22$ for $p=2$), the conditional distance $d=2t+1$, and the passive failure probabilities $P_{\mathrm{pass}}\approx9.98\times10^{-6}$ and $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ at $\varepsilon=10^{-3}$ [9]. Its Discussion already flags the central weakness: the branch-permutation symmetry of the code states is a design requirement, no explicit encoder is constructed, and "if no symmetric encoder exists for a given ball, the weight-$\le t$ correctability claim and the distance $d=2t+1$ fail" [9]. The present revision keeps everything [9] establishes, corrects one arithmetic error in its active-baseline projection (Section 4.4), and reconciles a numerical divergence against [11] (Section 4.3).

**Barrier analysis on Bruhat–Tits trees [8].** A companion QNFO study provides energy barrier estimates and logical error bounds for the same tree geometry in a different error regime ($p_{\mathrm{err}}=0.40$ versus the $\varepsilon=10^{-3}$ used here); these results are useful as an independent barrier-based bound family against which the weight-counting picture can be cross-checked, and the study proposes a minimal experiment (a depth-3, $p=3$ five-qutrit neutral-atom test with $N=10^{4}$ trials and a three-standard-deviation falsification rule) as a template for the next experiment proposed in Section 7.

**Recursive thresholds on $p$-ary trees [10].** A further QNFO study models the strong triangle inequality as implying that any path connecting two distant vertices crosses a "cut" whose size grows exponentially with hierarchical level, and discusses exponential suppression factors and per-level failure probabilities; its falsification analysis is directly relevant to the present conditional claims: Hypothesis Q (that ultrametric geometry enforces an exponential error barrier for quantum errors) would be falsified by a depth-independent plateau in $p_L(d)$, by coherent error paths surviving majority voting, or by correlated multi-qudit errors exceeding the majority threshold. The third criterion is the same correlated-error failure mode that limits the binomial computation of Section 4.3, and we adopt it in the falsification criteria of Section 6.

**Overhead and projections [11].** A QNFO analysis states, as an explicit assumption, a physical-to-logical qubit overhead on the order of $10^{2}$–$10^{4}$ for active stabiliser codes, and discusses failure-probability values for the same ball-code model; it also proposes a minimal-next-experiment using five $^{87}\mathrm{Rb}$ atoms in an optical tweezer array with a falsification rule that an observed logical error rate exceeding a threshold would refute the model. The overhead figure supplies the Introduction's cost framing; the failure-probability values diverge from the binomial computation performed here, and Section 4.3 states the convention under which we resolve that divergence; the tweezer proposal is the concrete starting point for the experiment design in Section 7.

In summary, the active-QEC canon [4] defines the syndrome-based baseline; continuous-time [1], entanglement-assisted [2] and operator-algebra [7] extensions mark nearby research directions; qudit algorithmic work [3] supplies the hardware context; and the ultrametric line of work [8]–[11] provides the barrier bounds, the prior parameter derivations, and the divergent failure-probability values that this revision reconciles. No cited source derives the Knill–Laflamme proof for the ball codes or resolves the encoder existence question, which remains the novelty and the main open task of the present work.

## 3. Methods

### 3.1 Scope of the method

The paper's own method is closed-form combinatorial derivation plus explicit numerical evaluation. No simulation, measurement, or hardware experiment is performed or reported; the comparison to active correction in Section 4.4 is a projection under stated assumptions, and the pseudo-threshold in Section 4.5 is a projection under a stated dominant-term approximation. Every input number is either an exact combinatorial quantity derived here, the physical error rate $\varepsilon=10^{-3}$ (a stated modelling choice), or a value attributed to a cited work by number.

### 3.2 The geometry

Fix a prime $p$. The Bruhat–Tits tree $T_{p+1}$ is the infinite homogeneous tree in which every vertex has degree $p+1$; vertices correspond to homothety classes of lattices of $\mathbb{Q}_p$, and graph distance on the tree mirrors the ultrametric on $\mathbb{Q}_p$, whose norm obeys $\|x+y\|_p\le\max(\|x\|_p,\|y\|_p)$. We write $B_t(v)$ for the closed ball of graph radius $t$ about vertex $v$. The nesting/disjointness property of equal-radius balls (Lemma 1, Section 4.1) is the tree-level image of the ultrametric law that any two $p$-adic balls are nested or disjoint.

### 3.3 The code

A logical qudit of dimension $p$ is encoded in the $n_t$ vertex qudits of a ball $B_t(v_0)$, with
$$
n_t = 1 + \sum_{k=1}^{t}(p+1)p^{k-1} = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$
The encoding is required to distribute the logical amplitude over the ball so that code states are invariant under the permutation group of each branch at every level. We state this branch-permutation symmetry as a design requirement and do not construct explicit state vectors; Proposition 1 is conditional on it. Gates are Hecke operators $T_{\ell}$, which act by averaging over the $p+1$ forward neighbours of each vertex; they are local in the tree metric, and the Hecke algebra is commutative, so gate ordering within a ball is not a fault-tolerance hazard of the usual kind.

### 3.4 Error model

Errors are vertex-localised Weyl operators $X^{a}Z^{b}$ acting on single-vertex qudits, matching the decomposition of general noise into Pauli-type operators established in [5]. The weight $|E|$ of an error set $E$ is the number of affected vertices. Depolarising-style noise acts independently on each vertex qudit with probability $\varepsilon$ per protection epoch:
$$
\rho\longmapsto (1-\varepsilon)\,\rho + \frac{\varepsilon}{p^{2}-1}\sum_{(a,b)\neq(0,0)}X^{a}Z^{b}\,\rho\,Z^{-b}X^{-a}.
$$
Amplitude damping is discussed qualitatively in Section 6.

### 3.5 Correctability criterion

We use the Knill–Laflamme conditions in the standard form: a code with projector $P$ corrects error sets $\{E_i\}$ iff
$$
P\,E_i^{\dagger}E_j\,P = c_{ij}\,P,
$$
as given in the foundational treatment of [5], which recalls the Knill–Laflamme framework as the general theoretical framework describing the requirements for quantum error-correcting codes. The OAQEC error-correction theorem of [7] provides the generalized characterization of correctable Pauli error sets within which the resulting code, once an encoder exists, would sit.

### 3.6 Computational method

All quantitative results are obtained by closed-form combinatorics and explicit numerical evaluation of the resulting expressions, with every arithmetic step shown in Section 4. Where this paper's computation and a cited value disagree, the disagreement is stated in the section that uses the number, together with the convention adopted.

## 4. Analysis

Every number in this section is derived here from stated inputs, except where a value is attributed to a cited work by number.

### 4.1 Ball sizes and the nesting lemma (exact)

**Input.** Branching $p+1$; shell $k$ contains $(p+1)p^{k-1}$ vertices for $k\ge1$ (shell 1 has $p+1$ vertices; each subsequent shell multiplies by $p$, since each vertex has one backward and $p$ forward neighbours). Hence
$$
n_t = 1 + (p+1)\sum_{k=0}^{t-1}p^{k} = 1 + (p+1)\,\frac{p^{t}-1}{p-1}.
$$

**Case $p=3$.**
- $t=1$: $n_1 = 1 + 4\cdot\frac{3-1}{2}=1+4=5$.
- $t=2$: $n_2 = 1 + 4\cdot\frac{9-1}{2}=1+16=17$.
- $t=3$: $n_3 = 1 + 4\cdot\frac{27-1}{2}=1+52=53$.

**Case $p=2$.**
- $t=1$: $n_1 = 1 + 3\cdot1 = 4$.
- $t=2$: $n_2 = 1 + 3\cdot3 = 10$.
- $t=3$: $n_3 = 1 + 3\cdot7 = 22$.

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
hence $s\le2t-2\,\operatorname{dist}(m,w)\le2t$. The tree metric inherited from the $p$-adic valuation satisfies the strong triangle inequality $\operatorname{dist}(v,v')\le\max(\operatorname{dist}(v,w),\operatorname{dist}(w,v'))\le t$, so $s\le t$, implying $v'\in B_t(v)$. In an ultrametric ball every vertex is a centre, therefore $B_t(v)=B_t(v')$. $\square$

### 4.2 Correctability and distance (conditional proposition)

**Proposition 1.** Given a branch-symmetric encoder on $B_t(v_0)$, the ball code corrects every error set of weight $\le t$, hence has distance $d=2t+1$.

*Proof sketch.* (i) **Correctability.** Let $E,F$ be error sets with $|E|,|F|\le t$, supported on vertex subsets $S_E,S_F\subseteq B_t(v_0)$. By Lemma 1, the sub-balls generated by the error supports are either nested or disjoint. If $S_E$ and $S_F$ lie in disjoint sub-balls, then $E^{\dagger}F$ moves amplitude between orthogonal branch sectors, so $P\,E^{\dagger}F\,P=0$. If they lie in the same nested chain, the code's branch-permutation symmetry (Section 3.3) makes $P\,E^{\dagger}F\,P=c_{EF}P$ with $c_{EF}$ depending only on the multiset of error types, not on their positions. Both Knill–Laflamme conditions therefore hold [5], and the error-set characterization is of the type formalized by the OAQEC theorem of [7].

(ii) **Distance.** Errors of weight $\le t$ are correctable; an error acting on the shell at distance $t+1$ moves the state into the disjoint ball $B_t(v')$ for a neighbour $v'$, which is orthogonal to the code space, so weight-$(t+1)$ errors are detectable but not correctable. Hence $d=2t+1$. $\square$

We flag what is proved versus assumed: the nesting/disjointness structure (Lemma 1) and the resulting weight bounds are proved; the branch-permutation symmetry of the code states is a design requirement whose explicit encoder we do not construct here. Proposition 1 is therefore a conditional parameter derivation: *given* a symmetric encoder, $n_t$ and $d=2t+1$ follow.

For $p=3$, $t=1$: $n_1=5$, $d=3$, $t_{\mathrm{corr}}=\lfloor(d-1)/2\rfloor=1$, rate $1/5$.

### 4.3 Passive failure probability (exact computation, with a stated reconciliation)

**Model.** Each of the $n_t$ vertex qudits suffers an error independently with probability $\varepsilon$ per protection epoch; the passive scheme corrects all weight-$\le t$ error patterns by Proposition 1 without any measurement; failure requires $\ge t+1$ simultaneous errors within the ball.

**Case $p=3$, $t=1$** ($n_1=5$, $d=3$). Failure probability:
$$
P_{\mathrm{pass}} = 1-(1-\varepsilon)^{5} -\binom{5}{1}\varepsilon(1-\varepsilon)^{4}.
$$

**Input.** $\varepsilon=10^{-3}$.

**Input.** $\varepsilon=10^{-3}$.

1. $(1-\varepsilon)^2 = 0.999^{2}=0.998001$ (intermediate used for later powers).
2. $(1-\varepsilon)^4 = 0.998001^{2}=0.996005996001$.
3. $(1-\varepsilon)^5 = 0.996005996001\times0.999=0.995009990004999$.
4. $\binom{5}{1}\varepsilon(1-\varepsilon)^{4}=5\times10^{-3}\times0.996005996001=0.004980029980005$.
5. $P_{\mathrm{pass}} = 1-0.995009990004999-0.004980029980005=0.000009980014996$,
   i.e.
$$
P_{\mathrm{pass}}=9.980015\times10^{-6}.
$$

Leading-order check: $\binom{5}{2}\varepsilon^{2}=10\times10^{-6}=1.0\times10^{-5}$, consistent with the exact value up to the $(1-\varepsilon)$ factors.

**Suppression factor** relative to the unencoded qudit (failure probability $\varepsilon=10^{-3}$):
$$
\frac{\varepsilon}{P_{\mathrm{pass}}}
   =\frac{10^{-3}}{9.980015\times10^{-6}}=100.2003\ldots\approx100.2.
$$

**Case $p=3$, $t=2$** ($n_2=17$, $d=5$). Failure requires $\ge3$ errors:
$$
P_{\mathrm{pass}}^{(2)} \approx \binom{17}{3}\varepsilon^{3}(1-\varepsilon)^{14}.
$$

1. $\binom{17}{3}=680$.
2. $(1-\varepsilon)^{14}$: $(1-\varepsilon)^{8}=0.996005996001^{2}=0.992027944070$; $(1-\varepsilon)^{14}=(1-\varepsilon)^{8}(1-\varepsilon)^{4}(1-\varepsilon)^{2}=0.992027944070\times0.996005996001\times0.998001$. The first product is $0.992027944070\times0.996005996001=0.988065684\ldots$; multiplying by $0.998001$ gives $0.986090532\ldots$
3. Leading term: $680\times10^{-9}\times0.986090532=6.705416\times10^{-7}$.
4. The next term $\binom{17}{4}\varepsilon^{4}(1-\varepsilon)^{13}=2380\times10^{-12}\times0.987077\ldots\approx2.349\times10^{-9}$ adds $\approx0.35\%$.

Thus
$$
P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}.
$$

**Reconciliation with [11].** The analysis in [11] reports, for the same model parameters ($p=3$, $t=1$, $\varepsilon=10^{-3}$), the values $P_{\mathrm{pass}}=5.992003\times10^{-6}$, suppression factor $S=166.9$, and $P_{\mathrm{pass}}^{(2)}=3.997\times10^{-9}$ at $t=2$. The binomial computation performed above, with every step shown, gives $9.980015\times10^{-6}$, $100.2$, and $6.73\times10^{-7}$ respectively. We take the directly computed binomial values under the convention that the exact expansion $1-(1-\varepsilon)^{5}-\binom{5}{1}\varepsilon(1-\varepsilon)^{4}$, evaluated term by term, is authoritative; the divergence with [11] is not resolvable from the values [11] states, because [11] does not reproduce the intermediate arithmetic that would locate the difference. The consequence of the convention is conservative: the binomial value is the larger failure probability, so any advantage factor computed from it is smaller.

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
2. $(1-\varepsilon_{\mathrm{eff}})^{4}=0.996005996001^{2}=0.992027944070$.
3. $(1-\varepsilon_{\mathrm{eff}})^{5}=0.992027944070\times0.998001=0.990044900166$.
4. $5\times0.001999\times0.992027944070=0.009915319301$.
5. $P_{\mathrm{act}}=1-0.990044900166-0.009915319301=0.000039780533$,
   i.e.
$$
P_{\mathrm{act}}\approx3.98\times10^{-5}.
$$

This corrects the value $P_{\mathrm{act}}\approx4.07\times10^{-5}$ reported in the prior published version; recomputation of the same stated assumptions (A1)–(A4) gives $3.98\times10^{-5}$, and the earlier figure was an arithmetic slip in the final subtraction.

**Ratio.**
$$
\frac{P_{\mathrm{act}}}{P_{\mathrm{pass}}}
   =\frac{3.9780533\times10^{-5}}{9.980015\times10^{-6}}=3.9860\ldots\approx3.99.
$$

Thus, under assumptions (A1)–(A4), the passive scheme yields a factor $\approx3.99$ advantage arising purely from the absence of measurement circuitry. This is a projection; Section 6 details why the comparison is not yet apples-to-apples.

### 4.5 Pseudo-threshold (projection)

The pseudo-threshold is the $\varepsilon$ at which $P_{\mathrm{pass}}(\varepsilon)=\varepsilon$ for the $n=5$, $t=1$ block. Dominant term:
$$
10\,\varepsilon(1-\varepsilon)^{3}\approx1.
$$

Evaluate $f(\varepsilon)=10\,\varepsilon(1-\varepsilon)^{3}$:
- $f(0.32)=3.2\times0.68^{3}=3.2\times0.314432=1.0061824>1$.
- $f(0.33)=3.3\times0.67^{3}=3.3\times0.300763=0.9925179<1$.

Linear interpolation gives
$$
\varepsilon_{\mathrm{th}}\approx0.32+0.01\times\frac{1.0061824-1}{1.0061824-0.9925179}
   =0.32+0.01\times0.4524=0.3245.
$$

Hence the pseudo-threshold under the dominant-term approximation is $\varepsilon_{\mathrm{th}}\approx0.3245$; this is a projection, since higher-order terms are ignored.

## 5. Results

All numbers below are computed in Section 4 with fully shown arithmetic; none are simulation outputs.

**Code parameters (exact).** For $p=3$: $n_1=5$, $n_2=17$, $n_3=53$; for $p=2$: $n_1=4$, $n_2=10$, $n_3=22$. The distance of the ball code is $d=2t+1$ (Proposition 1, conditional on the branch-permutation symmetry of the encoder). The flagship block $p=3$, $t=1$ has $n_1=5$ qudits, $d=3$, and rate $1/5$.

**Passive logical failure (exact computation, $p=3$, $t=1$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}=9.980015\times10^{-6}$ per protection epoch, a suppression factor $\varepsilon/P_{\mathrm{pass}}\approx100.2$ over an unencoded qudit. Under the reconciliation convention of Section 4.3, this value supersedes the $5.992003\times10^{-6}$ reported for the same model in [11].

**Passive logical failure ($p=3$, $t=2$, $\varepsilon=10^{-3}$).** $P_{\mathrm{pass}}^{(2)}\approx6.73\times10^{-7}$ per protection epoch (leading term $6.705416\times10^{-7}$ plus a $\approx0.35\%$ correction from the weight-4 term).

**Active baseline projection.** $P_{\mathrm{act}}\approx3.98\times10^{-5}$ under assumptions (A1)–(A4), giving a $\approx3.99$-fold advantage for the passive scheme. This corrects the $\approx4.08$ factor of the prior version [9].

**Pseudo-threshold projection.** $\varepsilon_{\mathrm{th}}\approx0.3245$ under the dominant-term approximation.

## 6. Discussion

**What is proved versus assumed.** Lemma 1 (nesting/disjointness of equal-radius balls) is proved, and the shell-count formula for $n_t$ is an exact combinatorial identity. Proposition 1, however, is conditional: the branch-permutation symmetry of the code states is a design requirement, and no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed in this paper. If no symmetric encoder exists for a given ball, the weight-$\le t$ correctability claim and the distance $d=2t+1$ fail. The single most important open task is therefore the explicit construction of the encoder and the verification of $P E_i^\dagger E_j P = c_{ij} P$ for concrete Weyl error sets.

**Model limitations.**
(i) The noise model is independent depolarising noise per vertex qudit per epoch; correlated errors (e.g., a gate fault coupling two neighbouring vertices, or a burst affecting a whole branch) violate independence and could defeat the weight counting on which $P_{\mathrm{pass}}$ rests. This is the same correlated-error failure mode that [10] lists as a falsification criterion for its Hypothesis Q, and we adopt it here.
(ii) Amplitude damping is not modelled; on a tree geometry its asymmetric action may or may not respect the nesting structure, and this is unresolved.
(iii) The active-baseline comparison rests on assumptions (A1)–(A4), in particular the pessimistic choice $\varepsilon_m=\varepsilon$ and the simple combination rule of (A3); a real baseline may have a smaller $\varepsilon_m$, which would shrink the $\approx3.99$ factor toward unity, or may require multiple syndrome-extraction rounds, which would enlarge it. The comparison is therefore indicative, not apples-to-apples.
(iv) The pseudo-threshold $\approx0.3245$ uses only the dominant term of $P_{\mathrm{pass}}(\varepsilon)$; near $\varepsilon\approx0.32$ the neglected higher-order terms are not negligible, so the true threshold may differ.
(v) The numerical divergence with [11] ($5.992003\times10^{-6}$ versus $9.980015\times10^{-6}$) is resolved by convention, not by identifying the source of the discrepancy; until the intermediate arithmetic of [11] is available for comparison, the adopted value carries the residual risk that [11]'s model differs in an unstated detail (for example a different per-epoch definition), in which case the suppression factor would move between $100.2$ and $166.9$.

**Falsification criteria.** The central claims would be falsified if: (a) an explicit encoder on $B_t(v_0)$ fails the Knill–Laflamme conditions for some weight-$\le t$ Weyl error set, contradicting Proposition 1; (b) two distinct equal-radius balls of $T_{p+1}$ overlap without coinciding, contradicting Lemma 1; (c) a fault-tolerant simulation of the code under the stated noise model yields logical failure rates inconsistent with the binomial computation of Section 4.3; or (d) correlated multi-qudit errors exceeding the majority threshold are demonstrated, as [10] states for its Hypothesis Q, in which case the barrier exponent and the binomial weight counting are both overestimated.

**Open questions.** Whether the ball codes embed into the operator-algebra QEC framework [7], which would allow existing OAQEC machinery to analyse them; whether Hecke-operator gates admit a fault-tolerant compilation compatible with the code symmetry; whether the passive advantage survives system-level energy-metric assessments such as those used in qudit benchmarking; and whether the discrepancy with [11] can be traced to an identifiable modelling difference.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.** The primary users are quantum-hardware architects exploring alternative fault-tolerance strategies for qudit-based processors. If the passive scheme operates as projected, designers could allocate fewer ancilla qudits to syndrome extraction, reduce the depth of error-correction cycles, and simplify control electronics, because logical protection would arise from the static geometry of the qudit layout rather than from active feedback. The decision variable altered is the allocation of hardware resources between data qudits and measurement/feedback circuitry.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (technology concept formulated). No experimental prototype has been built, so the readiness does not exceed TRL 3.

**(c) Smallest next experiment.** A minimal prototype would consist of five physical qutrits ($p=3$) arranged in the star-shaped ball $B_1(v_0)$ of the Bruhat–Tits tree. The experiment would (i) initialise a logical state using a symmetric encoding (to be defined), (ii) apply a single protection epoch of independent depolarising noise with calibrated error rate $\varepsilon$, and (iii) measure the logical error probability. The outcome that would falsify the passive-failure prediction is a measured logical failure rate $P_{\mathrm{exp}}$ that deviates from the analytically computed $P_{\mathrm{pass}}=9.980015\times10^{-6}$ by more than a factor of two, after accounting for statistical uncertainty. Two concrete platform templates exist in the cited line of work: a depth-3, $p=3$ five-qutrit neutral-atom test with $N=10^{4}$ trials and a three-standard-deviation falsification rule [8], and a five-$^{87}\mathrm{Rb}$ optical-tweezer array in which an observed logical error rate $>2\times10^{-5}$ would refute the model [11]. Either template, executed with the symmetric encoder of Proposition 1, would constitute the decisive test.

**(d) Engineering constraints.**
- **Qudit hardware:** The scheme requires qutrits (or higher-dimensional qudits) with controllable nearest-neighbour Hecke-type interactions.
- **Gate locality:** Hecke operators must be implementable as local averaging over the $p+1$ forward neighbours; this imposes a constraint on the connectivity of the physical layout.
- **Error-rate calibration:** Accurate knowledge of the physical depolarising rate $\varepsilon$ per epoch is needed to compare with the analytic prediction.
- **State preparation:** The symmetric encoder assumed in Proposition 1 must be realised; without an explicit construction this remains an open engineering task.

All other constraints (materials, cost, scale-up) are currently open questions because they depend on the eventual encoder design.

**(e) Projected cost/performance bounds.** Under the assumptions used in Sections 4.3–4.4 (independent depolarising noise $\varepsilon=10^{-3}$, five-qudit block, passive correction only) the logical failure probability is projected to be $P_{\mathrm{pass}}=9.980015\times10^{-6}$, giving a suppression factor of $\varepsilon/P_{\mathrm{pass}}\approx100.2$ relative to an unencoded qudit. Compared with an active distance-3 baseline under the same $\varepsilon$ and additional measurement error $\varepsilon_m=\varepsilon$, the passive scheme is projected to improve the logical failure rate by a factor of $\approx3.99$. These numbers are analytic projections; any engineering estimate of hardware cost must treat them as conditional on the existence of a symmetric encoder.

**(f) Direct risks and misuse paths.** If the passive geometry is adopted without a verified symmetric encoder, the code may fail to correct weight-$\le t$ errors, leading to a false sense of security and potentially higher logical error rates than anticipated. Moreover, over-reliance on the passive claim could discourage the development of robust active syndrome-extraction hardware, which remains essential for many existing codes.

## 8. Conclusion

We have formalised a passive quantum error-correction scheme in which logical qudits live on balls of the Bruhat–Tits tree $T_{p+1}$, proved a nesting lemma implying that equal-radius balls are nested or disjoint, derived the exact code parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ and the conditional distance $d = 2t+1$, and computed analytically that under independent depolarising noise at $\varepsilon = 10^{-3}$ the flagship $p=3$, $t=1$ block fails with probability $9.980015\times10^{-6}$ per epoch, a suppression of $\approx100.2$ over an unencoded qudit and, as an explicitly labeled projection under stated assumptions, a factor $\approx3.99$ over an active distance-3 baseline with noisy syndrome extraction. This revision corrects the active-baseline arithmetic of the prior version [9] ($P_{\mathrm{act}}\approx3.98\times10^{-5}$, not $4.07\times10^{-5}$), adopts the directly computed binomial value over the divergent figure in [11] under a stated convention, and strengthens the conditional character of the distance claim. The scheme's promise is real but conditional on constructing an explicit symmetric encoder; we have stated the assumptions, the failure modes, and the falsification criteria plainly so that the proposal can be tested rather than taken on trust.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.55.12). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 13 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[2] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[3] Efficient realization of quantum algorithms with qudits. arXiv:2111.04384v3. https://arxiv.org/abs/2111.04384v3
[4] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[5] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[7] Stabilizer Formalism for Operator Algebra Quantum Error Correction. arXiv:2304.11442v2. https://arxiv.org/abs/2304.11442v2
[8] https://papers.qnfo.org/papers/passive-quantum-error-correction-via-ultrametric-geometry-on-bruhat-tits-trees. QNFO: Passive Quantum Error Correction via Ultrametric Geometry on Bruhat–Tits Trees.
[9] https://papers.qnfo.org/papers/ultrametric-geometry-as-passive-quantum-error-correction-bruhat-tits-qudit-codes. QNFO: Ultrametric Geometry as Passive Quantum Error Correction: Bruhat–Tits Qudit Codes and the Non-Archimedean Bound.
[10] https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis. QNFO: Ultrametric Passive Error Correction on \(p\)-ary Bruhat–Tits Trees: Barrier Analysis and Recursive Thresholds.
[11] https://papers.qnfo.org/papers/ultrametric-passive-fault-tolerance-on-bruhat-tits-trees-analytic-deriv-93ee94f3. QNFO: Ultrametric Passive Fault Tolerance on Bruhat–Tits Trees: Analytic Derivation and Quantitative Projections.
