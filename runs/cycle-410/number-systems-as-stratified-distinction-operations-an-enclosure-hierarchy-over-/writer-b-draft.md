# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark (Corrected Version)

## Abstract

The conventional tower of number systems—$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$—augmented by the $p$-adic fields $\mathbb{Q}_{p}$ and the adele ring $\mathbb{A}$ is usually presented as a sequence of completions without a unifying generative principle. Practitioners in physics, logic, and computer science lack a quantitative criterion for choosing among these systems, which leads to ad-hoc model selection and undocumented information loss when finite-precision arithmetic is projected onto the continuum. This corrected version of the framework defines a family of enclosure operators $E_{i}$ that generate each stratum from a primitive mark and a loss functional $\Lambda_{i\to j}=\log_{2}N_{i}-\log_{2}N_{j}$ over distinguishable-state counts $N_{i}$, and it repairs three defects of the earlier version: the state-count verification scope, the attribution of the Ostrowski classification, and a misattributed reference. For the tree-to-continuum (Monna) projection, presented explicitly as an instance of the cross-stratum loss functional, we compute $\Lambda_{6\to4}=7$ bits at depth $n=10$, base $p=2$, real precision $\varepsilon=2^{-3}$; we prove the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed $\varepsilon$ and identify the loss-free matching depth $n=3$. Finite simultaneous-valuation products over the primes $\{2,3,5\}$ yield $30$ states at depth 1 and $900$ at depth 2. State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth. All numbers are derived by hand with every arithmetic step shown; no simulation or external measurement is used. The result converts a philosophical thesis into falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: $\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$, with $\mathbb{Q}_{p}$ and $\mathbb{A}$ attached to $\mathbb{Q}$ as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; as the distinction-based-ultrametric work states, quantum mechanics is written in the Archimedean completion of the rationals, yet Ostrowski's theorem gives one completion for every prime, so the real line is one completion among many and the choice of $\mathbb{R}$ as the base field is an assumption rather than a derivation [5]. A logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order. A computer scientist working with finite-precision arithmetic has no theory of what information is destroyed when a tree-structured limit is flattened onto a line. If the progression $\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}$ could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The calculus-of-re-entrant-distinctions program develops the thesis that the primitive act of distinction—the drawing of a boundary between marked and unmarked—generates, under re-entry and linear resource management, the landscape of completions of the rational numbers, and it attaches an explicit falsifiability condition to that thesis: if the formal system cannot derive its target results without importing the real numbers as external axioms, the claim of a purely logical derivation fails [6]. The distinction-based-ultrametric work supplies the finite-resolution reading of that program: a finite-resolution world distinguishes states rather than positioning them, and on a finite rooted tree the natural distance is the number of distinctions required to separate two leaves [5]. Neither work supplies a quantitative layer of state counts and bit budgets; this paper adds one, and repairs the defects recorded against the earlier version of the present work.

This version is a remediation. Three corrections are incorporated and are flagged where they occur. First, the scope of verified state-count arithmetic is stated precisely: it is verified only for strata 0, 1, 3, and 6 at finite depth, and only the state-count formulas for those strata are used in finite arithmetic (Section 3.2, Section 6). Second, the classification of the completions of $\mathbb{Q}$—the result that underwrites falsifier F3 and justifies the operator list of Section 3.2—is attributed to Ostrowski's theorem as stated in the distinction-based-ultrametric work [5], replacing the earlier version's unsupported attribution. Third, the earlier version attached a claim about super-powers and $p$-adic valuations to a reference whose actual content is the global regularity of nonlinear elliptic systems with symmetric gradients [1]; that misattributed claim is withdrawn in Section 2, since the present reference list contains no work supporting it.

We posit a primitive mark $M$ and a family of enclosure operators $E_{i}$, each a closure-type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable-state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree-to-continuum cross-stratum comparison. Four falsifiability conditions are stated so that a single counterexample kills the corresponding claim.

**Contributions.**
1. Explicit state-count derivations for the tally, real-enclosure, and $p$-adic strata at finite depth, with every arithmetic step shown, restricted to the verified strata 0, 1, 3, and 6 (Section 4, Derivations 1–3).
2. The Monna cross-stratum loss budget, presented explicitly as an instance of the general loss functional: $\Lambda_{6\to4}=7$ bits at $(p=2,n=10,\varepsilon=2^{-3})$, the exact linear law $\Lambda_{6\to4}(n)=n-3$ at fixed precision, the vanishing of the loss at matched depth $n=3$, and the reclassification of this quantity as cross-stratum rather than adjacent-stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous-valuation product counts of $30$ and $900$ over the primes $\{2,3,5\}$ at depths 1 and 2 (Section 4, Derivation 6).
4. The non-dyadic no-matching result: for $p=3$ and $\varepsilon=2^{-3}$ no integer depth yields zero loss because the required depth $n=3/\log_{2}3\approx1.893$ is not an integer (Section 4, Derivation 7).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of $\Lambda$, with the operator-list condition now underwritten by the Ostrowski classification as stated in [5] (Section 3.4).

## 2. Background and Related Work

The reference list available to this corrected version contains seven works. Each is discussed here through a specific result its text states; the small size of the list is recorded as a limitation in Section 6.

The global-regularity paper studies nonlinear elliptic systems of the form $-\operatorname{div}\big((\delta+|\varepsilon u|)^{p-2}\varepsilon u\big)=f$ with Dirichlet boundary conditions, where $\varepsilon u$ is the symmetric part of the gradient, and covers the full range of exponents $p\in(1,\infty)$ within the framework of systems of Orlicz growth, including the degenerate case $p>2$ [1]. This identifier is the one to which the earlier version of the present work attached a claim about super-powers and $p$-adic valuations; the content just stated is the actual content of the work, no super-powers result appears in it, and the present reference list contains no work supporting that claim. The misattributed sentence is therefore withdrawn, and nothing in the stratification argument of this paper depended on it.

The degree-based-topological-indices paper derives sharp lower bounds for the first and second Zagreb indices of trees with a given number of pendent vertices: Theorem 1 gives $M_{1}(T)\geq 9n-16$ for a tree with $n\geq 2$ pendent vertices when $n$ is even, with equality at $4$-trees (all internal vertices of degree 4), and Theorem 3 gives $M_{2}(T)\geq 11n-27$ for $n\geq 8$ pendent vertices, with equality when each stem vertex has degree 4 or 5 [2]. These theorems show that a scalar count over a tree family depends sharply on the branching profile of the tree—the same number of leaves admits different internal degree distributions with different index values. This is the precise shape of the limitation, recorded in Section 6, that the loss functional $\Lambda$ inherits from the branching profile of the source tree.

The arithmetic-lattices note describes arithmetic quotients of real, complex, and quaternionic hyperbolic spaces and states a variant of Sunada's theorem (Theorem 5.1): if $H$ and $K$ are elementwise conjugate subgroups of a group $G$ and $\pi_{1}(M)$ admits a homomorphism onto $G$, then the covers $M_{H}$ and $M_{K}$ have equal Laplace spectra, $L(M_{H})=L(M_{K})$ [3]. Sunada-type equivalence is exactly the phenomenon falsifier F4 guards against: two structures built by different constructions can be indistinguishable to a scalar spectral invariant, so a single number such as $\Lambda$ may fail to separate intuitively different projections.

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

The verification scope is stated exactly, correcting the earlier version's loose phrasing. State-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth: $N_{0}=1$ is definitional, $N_{1}(n)=n+1$ counts the tally marks, $N_{3}$ is infinite because the computable reals are countably infinite, and $N_{6}(n)=p^{n}$ counts the residue classes of $\mathbb{Z}/p^{n}\mathbb{Z}$. Only the state-count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below. The formula $N_{4}(\varepsilon)=1/\varepsilon$ is a definition of the target precision, not a verified recovery claim; the recovery claims that $E_{4}$ yields $\mathbb{R}$, $E_{5}$ yields $\mathbb{C}$, and $E_{7}$ yields $\mathbb{A}$ remain conjectural. The $p$-adic stratum instantiates the tree formalism of the distinction-based ultrametric, in which states are leaves of a finite rooted tree separated by ancestor depth [5].

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
= \log_{2}(1024