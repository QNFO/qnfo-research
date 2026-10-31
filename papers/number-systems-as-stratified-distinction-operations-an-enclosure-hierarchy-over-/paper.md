# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The conventional tower of number systems—$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$—augmented by the $p$-adic fields $\mathbb{Q}_{p}$ and the adele ring $\mathbb{A}$ is usually presented as a sequence of completions without a unifying generative principle. Practitioners in physics, logic, and computer science lack a quantitative criterion for choosing among these systems, which leads to ad-hoc model selection and undocumented information loss when finite-precision arithmetic is projected onto the continuum. This paper defines a family of enclosure operators $E_{i}$ that generate each stratum from a primitive mark and a loss functional $\Lambda_{i\to j}=\log_{2}N_{i}-\log_{2}N_{j}$ over distinguishable-state counts $N_{i}$. For the tree-to-continuum (Monna) projection, presented explicitly as an instance of the cross-stratum loss functional, we compute $\Lambda_{6\to4}=7$ bits at depth $n=10$, base $p=2$, real precision $\varepsilon=2^{-3}$; we prove the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed $\varepsilon$ and identify the loss-free matching depth $n=3$. Finite simultaneous-valuation products over the primes $\{2,3,5\}$ yield $30$ states at depth 1 and $900$ at depth 2. State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth. All numbers are derived by hand with every arithmetic step shown; no simulation or external measurement is used. The result converts a philosophical thesis into falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: $\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$, with $\mathbb{Q}_{p}$ and $\mathbb{A}$ attached to $\mathbb{Q}$ as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; as the distinction-based-ultrametric work states, quantum mechanics is written in the Archimedean completion of the rationals, yet Ostrowski's theorem gives one completion for every prime, so the real line is one completion among many and the choice of $\mathbb{R}$ as the base field is an assumption rather than a derivation [5]. A logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order. A computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression $\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}$ could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The calculus-of-re-entrant-distinctions program develops the thesis that the primitive act of distinction—the drawing of a boundary between marked and unmarked—generates, under re-entry and linear resource management, the landscape of completions of the rational numbers, and it attaches an explicit falsifiability condition to that thesis: if the formal system cannot derive its target results without importing the real numbers as external axioms, the claim of a purely logical derivation fails [6]. The distinction-based-ultrametric work supplies the finite-resolution reading of that program: a finite-resolution world distinguishes states rather than positioning them, and on a finite rooted tree the natural distance is the number of distinctions required to separate two leaves [5]. Neither work supplies a quantitative layer of state counts and bit budgets; this paper adds one.

Two scope restrictions are stated here and enforced throughout. First, the scope of verified state-count arithmetic is stated precisely: it is verified only for strata 0, 1, 3, and 6 at finite depth, and only the state-count formulas for those strata are used in finite arithmetic (Sections 3.2 and 6). Second, the classification of the completions of $\mathbb{Q}$—the result that underwrites falsifier F3 and justifies the operator list of Section 3.2—is attributed to Ostrowski's theorem as stated in the distinction-based-ultrametric work [5].

We posit a primitive mark $M$ and a family of enclosure operators $E_{i}$, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree-to-continuum cross-stratum comparison. Four falsifiability conditions are stated so that a single counterexample kills the corresponding claim.

**Contributions.**
1. Explicit state-count derivations for the tally, real-enclosure, and $p$-adic strata at finite depth, with every arithmetic step shown, restricted to the verified strata 0, 1, 3, and 6 (Section 4, Derivations 1–3).
2. The Monna cross-stratum loss budget, presented explicitly as an instance of the general loss functional: $\Lambda_{6\to4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed precision, the vanishing of the loss at matched depth $n=3$, and the reclassification of this quantity as cross-stratum rather than adjacent-stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous-valuation product counts of $30$ and $900$ over the primes $\{2,3,5\}$ at depths 1 and 2 (Section 4, Derivation 6).
4. The non-dyadic no-matching result: for $p=3$ and $\varepsilon=2^{-3}$ no integer depth yields zero loss because the required depth $n=3/\log_{2}3\approx1.893$ is not an integer (Section 4, Derivation 7).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of $\Lambda$, with the operator-list condition underwritten by the Ostrowski classification as stated in [5] (Section 3.4).

## 2. Background and Related Work

Seven works are discussed here, each through a specific result its text states; the size of the reference list is recorded as a limitation in Section 6.

The global-regularity paper studies nonlinear elliptic systems of the form $-\operatorname{div}\big((\delta+|\varepsilon u|)^{p-2}\varepsilon u\big)=f$ with Dirichlet boundary conditions, where $\varepsilon u$ is the symmetric part of the gradient, and covers the full range of exponents $p\in(1,\infty)$ within the framework of systems of Orlicz growth, including the degenerate case $p>2$ [1]. Its relevance here is methodological: it shows that structures built from primitive operations can sustain deep analytic treatment, so the stratified framework is not confined to finite counting arguments.

The degree-based-topological-indices paper derives sharp lower bounds for the first and second Zagreb indices of trees with a given number of pendent vertices: Theorem 1 gives $M_{1}(T)\geq 9n-16$ for a tree with $n\geq 2$ pendent vertices when $n$ is even, with equality at 4-trees (all internal vertices of degree 4), and Theorem 3 gives $M_{2}(T)\geq 11n-27$ for $n\geq 8$ pendent vertices, with equality when each stem vertex has degree 4 or 5 [2]. These theorems show that a scalar count over a tree family depends sharply on the branching profile of the tree—the same number of leaves admits different internal degree distributions with different index values. This is the precise shape of the limitation, recorded in Section 6, that the loss functional $\Lambda$ inherits from the branching profile of the source tree.

The arithmetic-lattices note describes arithmetic quotients of real, complex, and quaternionic hyperbolic spaces and states a variant of Sunada's theorem (Theorem 5.1): if $H$ and $K$ are elementwise conjugate subgroups of a group $G$ and $\pi_{1}(M)$ admits a homomorphism onto $G$, then the covers $M_{H}$ and $M_{K}$ have equal Laplace spectra, $L(M_{H})=L(M_{K})$ [3]. Sunada-type equivalence is exactly the phenomenon falsifier F4 guards against: two structures built by different constructions can be indistinguishable to a scalar spectral invariant, so a single number such as $\Lambda$ may fail to separate intuitively different projections. The constructions also connect the higher strata of Section 3.2 to arithmetic geometry built over the $p$-adic and adelic completions.

The statistical-audit paper examines the claim that all Standard Model mass ratios are Pythagorean ($2^{a}\cdot 3^{b}\cdot 5^{c}$) to within approximately 1%, and finds that two of the nine claimed fits are arithmetically false (for example, the printed value 16.80 for $m_{\tau}/m_{\mu}$ against an actual value of 0.2624, a 98.4% deviation), that five of nine triples are non-optimal under an exhaustive bounded search, and that a look-elsewhere analysis assigns $p_{\text{global}}=0.116$, yielding the verdict "consistent with look-elsewhere artifact" [4]. This audit is the cautionary precedent for the present paper's discipline: hand-assembled arithmetic tables can contain errors that survive into print, so every quantitative claim here is derived with every arithmetic step shown in Section 4, and the numbers are stated so that an independent recomputation can check them line by line.

The distinction-based-ultrametric paper makes three contributions used directly here. It states the classification on which falsifier F3 rests: Ostrowski's theorem classifies the completions of the rational numbers as the real line and one $p$-adic field per prime [5]. It defines the distinction-based distance on a finite rooted tree—two states are either distinct or not at a given resolution, and the distance is the depth of the lowest common ancestor measured from the leaves, $d(a,b)=k-\ell$ for leaves at depth $k$ and lowest common ancestor at depth $\ell$—and records that the induced distance satisfies the ultrametric inequality $d(a,c)\le\max(d(a,b),d(b,c))$ [5]. And it reports the empirical ledger of null results for prime-specific structure in physical systems, including a certified radix-agnostic null on CMB log-periodic oscillations at $p=0.89$ [5]. The first point underwrites F3 and the operator list of Section 3.2; the second supplies the tree formalism that the $p$-adic stratum of Section 3.2 instantiates; the third cautions that reading $p$-adic structure into physical data has so far returned nulls, which bounds what the strata of this paper may be claimed to describe.

The calculus-of-re-entrant-distinctions treatise is the source of the two primitives used in Section 3.1: the mark, drawn as a boundary between marked and unmarked states, and the re-entrant form, whose repeated self-application generates an alternating sequence that the treatise reads temporally—as a clock in which each crossing is a tick [6]. The treatise further claims that the completions of the rational numbers belong to the landscape generated by disciplined distinction, and it attaches to that claim an explicit falsifiability condition: if the formal system cannot derive its targets without importing the real numbers and the exponential function as external axioms, the claim of a purely logical derivation fails [6]. This paper adopts the mark and the enclosure as primitives and imitates the treatise's falsifiability discipline in Section 3.4, while remaining agnostic on the stronger generative claims.

The prime-valuation paper subjects the branch-depth reading—the $p$-adic valuation $v_{p}(n)$ as depth along a prime branch of the factorization tree, with $v_{2}(\dim H)=n$ counting tensor-branch depth for $n$ qubits—to its own falsifiability condition, and reports the negative result that reading the $[[n,k,d]]$ parameters of quantum error-correcting codes as valuations is largely pure relabeling: the valuation-based overhead bound is strictly weaker than the quantum Singleton bound, the valuation-based complexity characterization is complexity-vacuous, and the no-cloning re-expression yields no new checkable consequence [7]. This is a worked instance of the failure mode that falsifier F4 names for $\Lambda$: a valuation- or count-based reading can be definitional rather than informative. The paper's conclusion—that the honest outcome is a negative result plus a sharpened open question—is the standard this paper applies to its own conjectural strata.

Together these works supply the primitives, the classification theorem, the tree formalism, the cautionary precedents, and the falsifiability discipline within which the stratified-distinction framework is here made quantitative.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark $M$ satisfying the idempotent law
$$MM = M,$$
the *Calling* rule of the calculus of indications (assumed, following the primitive of the re-entrant-distinctions treatise [6]). A *distinction operation* $D$ partitions a structure into distinguishable classes. An *enclosure operator* $E$ is a closure-type operator on structures satisfying
$$S\subseteq E(S),\qquad E(E(S))=E(S),\qquad S\subseteq T\;\Rightarrow\;E(S)\subseteq E(T).$$

Each stratum is defined recursively as
$$S_{i}=E_{i}(S_{i-1}),\qquad i=1,\dots,7,$$
with the operators indexed by their target stratum.

### 3.2 The strata

| Stratum | Operator $E_{i}$ | Minimal algebraic structure | Distinguishable-state count $N_{i}$ (parameterised) |
|---|---|---|---|
| 0 (the mark) | — | $\{M\}$ | $N_{0}=1$ |
| 1 (tally, $\mathbb{N}$) | tally enclosure | free monoid on one generator $\to\mathbb{N}$ with addition | $N_{1}(n)=n+1$ (depth $n$) |
| 2 (ratio, $\mathbb{Q}$) | ratio-compare | field of fractions of $\mathbb{Z}$ $\to\mathbb{Q}$ | $N_{2}$ infinite (no finite truncation) |
| 3 (convergent sequences, $\mathbb{R}_{\text{comp}}$) | Cauchy-sequence enclosure | computable reals $\mathbb{R}_{\text{comp}}$ | $N_{3}$ infinite |
| 4 (lossy tree projection, $\mathbb{R}$) | Monna-type projection $\pi_{M}$ | continuum $\mathbb{R}$ | $N_{4}(\varepsilon)=1/\varepsilon$ (real precision $\varepsilon$) |
| 5 (phase enclosure, $\mathbb{C}$) | phase enclosure | $\mathbb{C}\cong\mathbb{R}\times S^{1}$ | $N_{5}$ infinite |
| 6 (divisibility enclosure, $\mathbb{Q}_{p}$) | $p$-adic completion | $\mathbb{Q}_{p}$ | $N_{6}(n)=p^{n}$ (depth $n$) |
| 7 (simultaneous valuations, $\mathbb{A}$) | adele enclosure | $\mathbb{A}= \mathbb{R}\times\!\!\prod_{p}'\mathbb{Q}_{p}$ | $N_{7}$ infinite (restricted product) |

The verification scope is stated exactly. State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth: $N_{0}=1$ is definitional, $N_{1}(n)=n+1$ counts the tally marks, $N_{3}$ is infinite because the computable reals are countably infinite, and $N_{6}(n)=p^{n}$ counts the residue classes of $\mathbb{Z}/p^{n}\mathbb{Z}$. Only the state-count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below. The formula $N_{4}(\varepsilon)=1/\varepsilon$ is a definition of the target precision, not a verified recovery claim; the recovery claims that $E_{4}$ yields $\mathbb{R}$, $E_{5}$ yields $\mathbb{C}$, and $E_{7}$ yields $\mathbb{A}$ remain conjectural. The $p$-adic stratum instantiates the tree formalism of the distinction-based ultrametric, in which states are leaves of a finite rooted tree separated by ancestor depth [5].

### 3.3 Morphisms and the loss functionals

Between adjacent strata $S_{i}\to S_{i+1}$ we take the canonical map induced by the operator. The *adjacent-stratum information-loss functional* is
$$\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),$$
the base-2 logarithm of the ratio of distinguishable-state counts.

**Cross-stratum loss functional.** For any ordered pair of strata $i,j$ with finite counts we define
$$\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),$$
which reduces to the adjacent-stratum functional when $j=i+1$. The Monna projection $\pi_{M}$ maps a depth-$n$, base-$p$ tree (state count $N_{6}(n)=p^{n}$) onto a line at precision $\varepsilon$ (state count $N_{4}(\varepsilon)=1/\varepsilon$); source and target are strata 6 and 4, which are not adjacent. Consequently the Monna loss is a *cross-stratum* quantity, and Derivation 4 presents it explicitly as an instance of the general functional:
$$\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).$$

### 3.4 Falsifiability conditions

* **F1 (stratification).** Exhibit a number system in the historical sequence that no closure operator over the mark can generate.
* **F2 (loss functional).** Exhibit a projection whose state-count loss decreases as the source is refined at fixed target precision.
* **F3 (operator list).** Exhibit a completion of $\mathbb{Q}$ outside the list $\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}$. By Ostrowski's theorem as stated in [5], the completions of the rational numbers are the real line and one $p$-adic field per prime, so the theorem itself asserts that no such completion exists; F3 therefore functions as a consistency check on the operator list, and the theorem underwrites both F3 and the operator list of Section 3.2.
* **F4 ($\Lambda$ adequacy).** Exhibit two intuitively different projections with identical $\Lambda$ but markedly different information content. The Sunada variant of [3]—elementwise conjugate subgroups yielding covers with equal Laplace spectra—and the relabeling verdict of [7] both describe scalar invariants that fail to separate genuinely different structures; either phenomenon realized for $\Lambda$ would falsify F4.

## 4. Analysis

All inputs are either definitions of Section 3 or explicitly stated here; every arithmetic step is shown.

**Input 1.** Tally depth $n=9$. (Chosen parameter.)
**Input 2.** Prime $p=2$, tree depth $n=10$. (Chosen parameter.)
**Input 3.** Real precision $\varepsilon=2^{-3}$ (unit interval partitioned into cells of width $2^{-3}$). (Chosen parameter.)
**Input 4.** Primes $\{2,3,5\}$ for the finite adele-type product. (Chosen parameter.)
**Input 5.** Prime $p=3$ for the non-dyadic analysis. (Chosen parameter.)
**Input 6.** Projection parameters for a non-dyadic example: $p=3$, $n=5$, $\varepsilon=10^{-2}$. (Assumed for illustration.)

### Derivation 1 (tally states)

With $n=9$ marks the distinguishable counts are $\{0,1,\dots,9\}$, so
$$N_{1}(9)=9+1=10.$$

### Derivation 2 (real-enclosure states)

The unit interval $[0,1]$ partitioned into cells of width $\varepsilon=2^{-3}$ contains
$$N_{4}(\varepsilon)=\frac{1}{\varepsilon}= \frac{1}{2^{-3}} = 2^{3}=8$$
distinguishable cells.

### Derivation 3 ($p$-adic tree states)

The residue ring $\mathbb{Z}/p^{n}\mathbb{Z}$ with $p=2$, $n=10$ has exactly
$$N_{6}(10)=2^{10}=1024$$
elements. Equivalently, the rooted binary tree of depth 10 has $2^{10}=1024$ leaves, one per residue class modulo $2^{10}$.

### Derivation 4 (Monna cross-stratum loss as an instance of the loss functional)

The Monna projection $\pi_{M}$ maps the depth-10 binary tree onto the real line at precision $\varepsilon=2^{-3}$. Substituting $N_{6}(10)=1024$ (Derivation 3) and $N_{4}(2^{-3})=8$ (Derivation 2) into the cross-stratum instance $\Lambda_{6\to4}=\log_{2}N_{6}-\log_{2}N_{4}$ of the general functional of Section 3.3,
$$\Lambda_{6\to4}= \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)
= \log_{2}(1024)-\log_{2}(8)=10-3=7.$$
Checking via the ratio form,
$$\Lambda_{6\to4}= \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,$$
and $2^{7}=128$ confirms the ratio.

### Derivation 5 (linearity and vanishing)

Fix $\varepsilon=2^{-3}$ and vary depth $n$. Since $N_{6}(n)=2^{n}$ and $N_{4}(\varepsilon)=2^{3}$,
$$\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,$$
which is strictly increasing in $n$. At $n=3$ the loss is
$$\Lambda_{6\to4}(3)=3-3=0,$$
so the depth-3 binary tree and the precision-$2^{-3}$ continuum have identical state counts $2^{3}=8$ and the projection is loss-free there.

### Derivation 6 (finite simultaneous-valuation products)

Take the primes $\{2,3,5\}$. At depth 1 the simultaneous-valuation state space is the product of residue rings $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/5\mathbb{Z}$, with count
$$N_{7}^{(1)}=2\cdot3\cdot5=30.$$
At depth 2 it is $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/9\mathbb{Z}\times\mathbb{Z}/25\mathbb{Z}$, with count
$$N_{7}^{(2)}=4\cdot9\cdot25=900.$$
Both products are finite because each factor is finite; the Chinese remainder theorem makes the simultaneous residue classes independent, so the total count is the product of the individual counts.

### Derivation 7 (non-dyadic no-matching)

Fix $\varepsilon=2^{-3}$ and take $p=3$. Zero loss requires
$$n\log_{2}3=\log_{2}(1/\varepsilon)=3,$$
so the required depth is
$$n=\frac{3}{\log_{2}3}.$$
We compute $\log_{2}3=\ln 3/\ln 2\approx1.584963$, hence
$$n\approx\frac{3}{1.584963}=1.892789\approx1.893.$$
Since $n$ must be an integer depth, no integer solution exists; at $n=1$ the loss is $\Lambda_{6\to4}(1)=1.584963-3=-1.415037$ bits (the tree is coarser than the target), and at $n=2$ it is $\Lambda_{6\to4}(2)=3.169925-3=0.169925$ bits (the tree is already finer). The loss jumps across zero without vanishing.

### Derivation 8 (projected loss for a non-dyadic example)

Assume parameters $p=3$, $n=5$, $\varepsilon=10^{-2}$. Then
$$\log_{2}(1/\varepsilon)=\log_{2}100=\frac{\ln 100}{\ln 2}\approx6.643856,$$
and
$$\Lambda_{6\to4}=5\log_{2}3-\log_{2}100\approx5\times1.584963-6.643856\approx1.280957\;\text{bits}.$$
We report this as a projection under the stated assumptions.

## 5. Results

All quantities below are obtained from the explicit derivations of Section 4; no simulation, measurement, or external data are used.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth $n=9$ | $N_{1}(9)=10$ | Derivation 1 |
| Real-enclosure cells at $\varepsilon=2^{-3}$ | $N_{4}=8$ | Derivation 2 |
| Binary-tree states at depth $n=10$ | $N_{6}(10)=1024$ | Derivation 3 |
| Monna cross-stratum loss for $(p=2,n=10,\varepsilon=2^{-3})$ | $\Lambda_{6\to4}=7$ bits | Derivation 4 |
| Linear law $\Lambda_{6\to4}(n)=n-3$ (fixed $\varepsilon$) | $\Lambda_{6\to4}(n)=n-3$ bits | Derivation 5 |
| Depth at which loss vanishes (dyadic case) | $n=3$ (so $\Lambda_{6\to4}=0$) | Derivation 5 |
| Finite simultaneous-valuation product at depth 1 | $30$ states | Derivation 6 |
| Finite simultaneous-valuation product at depth 2 | $900$ states | Derivation 6 |
| Non-dyadic no-matching depth (base 3) | No integer solution; required $n\approx1.893$ | Derivation 7 |
| Projected loss for $(p=3,n=5,\varepsilon=10^{-2})$ | $\approx1.28$ bits | Derivation 8 |

**Result R1.** The Monna cross-stratum loss obeys the exact linear law
$$\Lambda_{6\to4}(n)=n-3\;\text{bits}$$
for base $p=2$ and precision $\varepsilon=2^{-3}$; increasing the tree depth strictly increases the information loss relative to a fixed-precision continuum target.

**Result R2.** A loss-free matching occurs at the dyadic pair $(n=3,\varepsilon=2^{-3})$, where the 2-adic tree and the real interval have identical state counts ($2^{3}=8$). No integer depth yields zero loss for the non-dyadic base $p=3$ at the same precision.

**Result R3.** The finite simultaneous-valuation product over the primes $\{2,3,5\}$ yields $30$ states at depth 1 and $900$ states at depth 2, illustrating how the adele-type construction multiplies state counts across independent $p$-adic components.

## 6. Discussion

### Limitations

* The recovery claims for strata 4, 5, and 7 remain conjectural; state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth.
* The loss functional $\Lambda$ counts *states* but not *structure*: two projections can destroy the same number of bits while destroying very different algebraic features (e.g., order versus branching). The Zagreb-index theorems of [2] make this limitation precise for trees: with the same number of pendent vertices, different branching profiles give different index values ($M_{1}(T)\geq 9n-16$, $M_{2}(T)\geq 11n-27$), so a scalar over a tree family is not determined by leaf count alone.
* The Monna analysis assumes the tree is exactly a $p$-adic ball in state count; a more general tree-like limit with a different branching profile would alter $\Lambda$.
* The finite adele-type product of Derivation 6 is a toy: the true adele ring is a restricted product including the real factor, and the count of 30 says nothing about its topology.
* $\Lambda$ is defined only for finite state counts; at infinite depth both source and target counts diverge, requiring renormalisation or a rate formulation.
* The reference list contains seven works; the literature treatment is correspondingly narrow, and claims that would need support from works outside this list (for example, on the history of number systems or on floating-point error analysis) are not made here.

The remaining part of the Discussion addresses failure modes and the conditions under which the central results would fail.

### Failure modes

* **Non-canonical realizations.** A single enclosure operator can admit multiple inequivalent concrete realizations; the operator, not the realization, determines the stratum. The state counts of Section 4 are therefore counts for the operator, and a different realization of $E_{6}$ could carry a different branching profile while retaining $N_{6}(n)=p^{n}$.
* **Operator-list incompleteness.** If a number system in the historical sequence required a completion outside $\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}$, the present operator list would be incomplete, falsifying F3. By Ostrowski's theorem as stated in [5], the completions of $\mathbb{Q}$ are exactly the real line and one $p$-adic field per prime, so the theorem asserts that no such completion exists; the failure mode is therefore the misapplication of the list to structures that are not completions of $\mathbb{Q}$.
* **$\Lambda$ inadequacy.** Two intuitively different projections could share the same $\Lambda$ value while differing in preserved structure, mirroring the Sunada-type phenomenon recorded in [3], where elementwise conjugate subgroups yield covers with equal Laplace spectra; this would falsify F4 and motivate a structural refinement of $\Lambda$.
* **Valuation relabeling.** A count-based reading can be definitional rather than informative. The prime-valuation work reports exactly this outcome for the $[[n,k,d]]$ reading: the valuation-based overhead bound is strictly weaker than the quantum Singleton bound, the complexity characterization is vacuous, and the no-cloning re-expression yields no new checkable consequence [7]. If the loss functional $\Lambda$ were shown to be definitional in the same sense—restating $N_{6}(n)=p^{n}$ without predictive content—the present framework would reduce to bookkeeping.

### What would falsify the main result

The main result is the linear law $\Lambda_{6\to4}(n)=n-3$ at fixed $\varepsilon=2^{-3}$ and the loss-free matching at $n=3$. A single counterexample falsifies it: any projection from a depth-$n$ binary tree to a precision-$2^{-3}$ continuum whose distinguishable-state count differs from $2^{n}$ at the source or $2^{3}=8$ at the target would break the identity $\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3$, because the law is an immediate consequence of those two counts and no other input. Equivalently, exhibiting a depth at which the loss decreases as the source is refined at fixed target precision would falsify F2 and with it R1. The derivation is three lines long, so the falsification test is correspondingly cheap: recompute $N_{6}(n)$ and $N_{4}(\varepsilon)$ under any alternative definition of distinguishable state and check whether the difference remains linear in $n$.

### Limitations list

The result rests on the following assumptions, in decreasing order of sensitivity:

1. **State-count definition.** $\Lambda$ depends entirely on what counts as a distinguishable state; the counts $N_{6}(n)=p^{n}$ and $N_{4}(\varepsilon)=1/\varepsilon$ are definitions, not measurements, and a different definition changes $\Lambda$ by an additive constant or destroys linearity altogether.
2. **Verified-strata restriction.** State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth, and only the state-count formulas for those strata are used in finite arithmetic; the recovery claims for strata 4, 5, and 7 remain conjectural.
3. **Branching profile.** The Monna analysis assumes the source tree is exactly a $p$-adic ball in state count; a tree with a different branching profile alters $\Lambda$, as the Zagreb-index bounds of [2] make precise for tree families ($M_{1}(T)\geq 9n-16$, $M_{2}(T)\geq 11n-27$ at fixed pendent-vertex count).
4. **Finite counts only.** $\Lambda$ is defined only for finite state counts; at infinite depth both source and target counts diverge, and a rate formulation or renormalisation would be needed.
5. **Toy adele product.** The finite simultaneous-valuation product of Derivation 6 omits the real factor and the restricted-product topology of $\mathbb{A}$; the counts 30 and 900 describe state spaces, not the adele ring.
6. **Narrow literature base.** The reference list contains seven works; claims that would need support from outside this list (for example, on the history of number systems or on floating-point error analysis) are not made here.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**
Researchers who must choose a numeric representation for formal models—in mathematical physics, constructive analysis, and exact-arithmetic software—are the principal users of the loss functional $\Lambda$ and the state-count formulas of Sections 4–5. When a model requires a target real precision $\varepsilon$, the user can compute the bit loss
$$\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr)$$
(Derivation 5) for any candidate $p$-adic depth $n$. If $\Lambda_{6\to4}=0$, the $p$-adic tree can replace the real interval at that precision without state-count loss; the dyadic case $p=2$, $n=3$, $\varepsilon=2^{-3}$ is the first such matching (Result R2). The decision that changes is the choice of storage representation: a modeler can store data in a depth-3 binary tree rather than a floating-point format and know, by the count $2^{3}=8=N_{4}(2^{-3})$, that no distinguishable state is discarded by the projection.

**(b) Technology readiness.**
The work is purely analytical, has not undergone peer review, and involves no hardware or software implementation. Against the NASA Technology Readiness Level definitions it resides at TRL 1–2: basic principles have been observed and stated, but no proof-of-concept application has been demonstrated. Analytical extensions do not exceed TRL 3; no claim of manufacturing or deployment readiness is made.

**(c) Minimal next experiment.**
A computational experiment that would test, and possibly falsify, the monotonicity claim of F2 can be specified conditionally:

1. Generate the residue set $\mathbb{Z}/p^{n}\mathbb{Z}$ for a chosen prime $p$ (for example $p=3$) and depths $n\in\{1,2,3\}$.
2. Map each residue class to a sub-interval of $[0,1]$ of width $\varepsilon$ (for example $\varepsilon=10^{-2}$) by a deterministic Monna-type rule.
3. Count the distinct real cells $N_{4}(\varepsilon)=1/\varepsilon$ (Derivation 2) and compute the empirical loss $\Lambda_{\text{emp}}=\log_{2}N_{6}(n)-\log_{2}N_{4}(\varepsilon)$.
4. Compare $\Lambda_{\text{emp}}$ with the predicted value $\Lambda_{6\to4}=n\log_{2}p-\log_{2}(1/\varepsilon)$ (Derivation 5).

If for any $(p,n,\varepsilon)$ the computed loss deviates from the predicted value, the linear law would be falsified, invalidating F2 and with it Result R1. The experiment requires no hardware beyond exact integer arithmetic.

**(d) First-order engineering constraints.**

* *Data representation.* Storing $p^{n}$ residues requires memory of at least $p^{n}$ integers (Derivation 3); for the depth-10 dyadic case this is 1024 entries.
* *Precision handling.* The real target demands $1/\varepsilon$ cells; for $\varepsilon=10^{-2}$ this is 100 cells (Derivation 2).
* *Computational throughput.* Mapping each of the $p^{n}$ residues to a real cell entails $O(p^{n})$ elementary operations, so runtime scales linearly in $p^{n}$.
* *Software tooling.* Exact integer arithmetic is needed to avoid overflow once $p^{n}$ exceeds native word size.

Whether other constraints (regulatory, cost, or materials) bind first is an open question; the present analysis derives only the state-count-driven ones.

**(e) Projected cost and performance bounds (assumptions).**
Assume a single elementary mapping operation costs $c_{\text{op}}=10^{-6}\,\text{s}$. The total runtime $T$ for depth $n$ and base $p$ is then
$$T=c_{\text{op}}\,p^{n}.$$
For the dyadic loss-free case $p=2$, $n=3$ this gives $T\approx 10^{-6}\times 2^{3}=8\times 10^{-6}\,\text{s}$. For the non-dyadic example $p=3$, $n=5$ the projection gives $T\approx 10^{-6}\times 3^{5}=2.43\times 10^{-4}\,\text{s}$. These figures are projections based on the assumed operation cost and the state count $N_{6}(n)=p^{n}$; actual timings depend on implementation details.

**(f) Direct risks and misuse pathways.**
Treating the scalar loss $\Lambda$ as a complete measure of suitability for replacing a real-valued representation ignores the structural differences recorded in Section 6: two projections with identical $\Lambda$ can preserve different algebraic features. Deploying a $p$-adic data structure solely because it yields a low $\Lambda$ could introduce defects in algorithms that rely on the order properties of $\mathbb{R}$. The cost projection assumes idealised operation costs; real systems may exhibit latency and memory effects not captured by the model.

## 8. Conclusion

The tower of number systems can be read as a sequence of enclosure operations applied to a primitive mark, and the cost of each operation can be measured in bits. This paper made that reading quantitative where a finite count exists: state-count arithmetic was derived with every step shown for strata 0, 1, 3, and 6 at finite depth; the Monna projection was presented explicitly as an instance of the cross-stratum loss functional, yielding $\Lambda_{6\to4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed precision, and the loss-free matching depth $n=3$; the non-dyadic base $p=3$ was shown to admit no integer zero-loss depth; and finite simultaneous-valuation products of 30 and 900 states were computed over the primes $\{2,3,5\}$. Four falsifiability conditions convert the stratification thesis, the loss functional, the operator list, and the adequacy of $\Lambda$ into killable claims, with the operator list underwritten by the Ostrowski classification as stated in [5] and the adequacy condition disciplined by the precedents of [3] and [7].

The framework's honest boundary is as important as its results. The recovery claims for strata 4, 5, and 7 remain conjectural; $\Lambda$ counts states but not structure; and the empirical record of prime-specific structure in physical data is a ledger of nulls [5], which bounds what the $p$-adic and adele strata may be claimed to describe. The next step is the minimal computational experiment of Section 7: recompute $N_{6}(n)$ and $N_{4}(\varepsilon)$ under alternative state-count definitions and check whether the linear law survives. If it does, the choice of number system acquires the measurable criterion this paper set out to supply; if it does not, the negative result sharpens the question in the same way the relabeling verdict of [7] sharpened its own.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 11. length 4465 -> 3640 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. references 11 -> 11. length 3688 -> 3932 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. references 11 -> 14. length 4004 -> 4026 words.
- Version 2.3.0 (2026-10-20, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 14 -> 11. length 4129 -> 4099 words.
- Version 2.4.0 (2026-10-21, from 2.3.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. references 11 -> 10. length 4235 -> 3949 words.
- Version 3.0.0 (2026-10-31, from 2.4.0): rewritten in full through the research pipeline. references 10 -> 7. length 3949 -> 5275 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.9-errata-claim-fair). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 6 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2310.17310&amp;start=0&amp;max_results=1
[2] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[3] Arithmetic lattices and weak spectral geometry. arXiv:0706.3841v1. https://arxiv.org/abs/0706.3841v1
[4] https://papers.qnfo.org/papers/acrp04-five-smooth-audit. QNFO: Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim.
[5] https://papers.qnfo.org/papers/distinction-based-ultrametric. QNFO: The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra.
[6] https://papers.qnfo.org/papers/reentrant-distinctions. QNFO: The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference.
[7] https://papers.qnfo.org/papers/prime-valuation-qec-implications. QNFO: Implications for Computing and Quantum Error Correction.
