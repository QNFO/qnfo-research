# Grounding block - source: rem-a492d9b0-d15e-4d74-b3b4-6bd1544c2646

## Research idea

Correct the published paper 'number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over-' for erratum pl-number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over--2.0.0-0: 'state-count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth' (Section 6, Limitations).
[ERRATA-ROUTE-PER-PAPER-1 merged errata:391] erratum pl-number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over--2.3.0-1: Section 6 / Section 2: Ostrowski's theorem 'underwrites our falsifier F3 and justifies the operator list of Section 3.2.'
[ERRATA-ROUTE-PER-PAPER-1 merged errata:187] erratum pl-number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over--2.1.0-0: Section 3.2 and Section 6 state that state-count arithmetic is 'verified only for strata 0, 1, 3, and 6 at finite depth,' and that 'only the state-count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below.'
[ERRATA-ROUTE-PER-PAPER-1 merged errata:120] erratum pl-number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over--2.0.0-1: The Monna loss Λ_Monna = log₂N₆(10) − log₂N₄(ε) is presented as an instance of the loss functional (Derivation 4).
Also: pl-number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over--2.2.0-1: Reference [8] is cited for the 'super-powers paper' proving a bound on ω(s_n) via p-adic valuations (Section 2), but the listed title of [8] is 'Global regularity for nonlinear systems with symmetric gradients' (arXiv:2310.17310).

## Existing paper under revision (remediation only)

# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The conventional tower of number systems—\(\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\)—augmented by the \(p\)-adic fields \(\mathbb{Q}_{p}\) and the adele ring \(\mathbb{A}\) is usually presented as a sequence of completions without a unifying generative principle. Practitioners in physics, logic, and computer science lack a quantitative criterion for choosing among these systems, which leads to ad‑hoc model selection, ambiguous foundational arguments, and undocumented information loss when finite‑precision arithmetic is projected onto the continuum. This paper supplies a quantitative layer by defining a family of enclosure operators \(E_{i}\) that generate each stratum from a primitive mark and by introducing a loss functional
\[
\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),
\]
where \(N_{i}\) counts distinguishable states in stratum \(S_{i}\). For the tree‑to‑continuum (Monna) projection we compute \(\Lambda_{6\to4}=7\) bits at depth \(n=10\), base \(p=2\) and real precision \(\varepsilon=2^{-3}\); we prove the exact linear law \(\Lambda_{6\to4}(n)=n-3\) at fixed \(\varepsilon\) and identify the loss‑free matching depth \(n=3\). Finite simultaneous‑valuation products over the primes \(\{2,3,5\}\) yield \(30\) states at depth 1 and \(900\) at depth 2. All numbers are derived by hand; no simulation or external measurement is used. The result converts a philosophical thesis into a family of falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: \(\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\), with \(\mathbb{Q}_{p}\) and \(\mathbb{A}\) attached to \(\mathbb{Q}\) as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; the adelic‑physics program argues that the choice of \(\mathbb{R}\) as the base field of physics is an unjustified assumption, because every measurement yields a rational number to finite precision and every simulation operates on finite‑precision rationals [7]. A logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order. A computer scientist working with finite‑precision arithmetic has no theory of what information is destroyed when a tree‑structured limit is flattened onto a line. If the progression \(\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}\) could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The measurement‑stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, \(p\)-adic enclosure [8]. The computable‑real‑boundary work builds number systems from two primitives of Spencer‑Brown’s *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates; it identifies the fixed point of finite enclosure operations with the computable reals \(\mathbb{R}_{\text{comp}}\) [9]. Neither work supplies a quantitative layer; this paper adds one, and repairs two misattributions that appeared in the earlier version of the present work [10].

We posit a primitive mark \(M\) and a family of enclosure operators \(E_{i}\), each a closure‑type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable‑state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree‑to‑continuum cross‑stratum comparison. Four falsifiability conditions are stated so that a single counterexample kills the corresponding claim.

**Contributions.**
1. Explicit state‑count derivations for the tally, real‑enclosure, and \(p\)-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
2. The corrected Monna cross‑stratum loss budget: \(\Lambda_{6\to4}=7\) bits at \((p=2,n=10,\varepsilon=2^{-3})\), the exact linear law \(\Lambda_{6\to4}(n)=n-3\) at fixed precision, the vanishing of the loss at matched depth \(n=3\), and the explicit reclassification of this quantity as cross‑stratum rather than adjacent‑stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous‑valuation product counts of \(30\) and \(900\) over the primes \(\{2,3,5\}\) at depths 1 and 2 (Section 4, Derivation 6).
4. The non‑dyadic no‑matching result: for \(p=3\) and \(\varepsilon=2^{-3}\) no integer depth yields zero loss because the required depth \(n=3/\log_{2}3\approx1.893\) is not an integer (Section 4, Derivation 7).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of \(\Lambda\) (Section 3.4).

## 2. Background and Related Work

We review the works most directly relevant to the stratified‑distinction framework.

* The Tate‑conjectures paper proves Tate’s two conjectures for algebraic cycles on certain products of elliptic curves and abelian surfaces, working with \(\ell\)-adic cycle‑class maps and compatible systems of semisimple \(\ell\)-adic representations [2]. Its use of \(\ell\)-adic (hence \(p\)-adic) cohomology demonstrates that the \(E_{6}\) stratum naturally connects to deep arithmetic geometry, motivating the inclusion of \(p\)-adic completions in the hierarchy.

* The stratified‑\(\beta\)-numbers paper introduces a modified version of Jones’s \(\beta\)-numbers for Carnot groups and proves that an analogue of Jones’s traveling‑salesman theorem holds when the earlier \(\beta\)’s are replaced by stratified ones; Section 3 shows that the non‑stratified \(\beta\)’s cannot provide sharp two‑sided inequalities for certain Carnot groups [4]. This result supplies the model for falsifier F4: a scalar measure can be inadequate for the structure it is meant to grade, and a stratified refinement (our \(\Lambda\)) may be required.

* The harmonic‑congruence paper proves, for any prime \(p\ge7\), the congruence \(\sum_{k=1}^{p-1}H_{k}^{2}/k^{2}\equiv\frac{4}{5}pB_{p-5}\pmod{p^{2}}\) for harmonic numbers \(H_{n}\) and confirms a conjecture of Z‑W Sun [3]. This illustrates the rich \(p\)-adic residue structure that lives inside the divisibility enclosure \(E_{6}\) and that our simple field‑level operator list does not capture.

* The super‑powers paper studies sequences \(s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{\,n^{j}}\) and proves that the number \(\omega(s_{n})\) of distinct prime factors exceeds a super‑logarithmic bound for infinitely many \(n\), using the \(p\)-adic valuation \(\upsilon_{p}\) [9]. This demonstrates how valuation‑based analytic tools can be attached to the \(E_{6}\) stratum, complementing our state‑count formalism.

* The non‑canonical‑number‑systems paper studies positional systems \((\mathbb{Z},b,\mathcal{D})\) with digit sets that do not contain \(0\), proves that such digit sets exist for every base \(|b|\ge4\), and exhibits \(\{1,2\}\) as a valid digit set for base \(-2\) [7]. This supplies the non‑canonicality failure mode: a single enclosure operator can admit many inequivalent concrete realizations, so the operator, not the digit set, determines the stratum.

* The Caccetta‑Häggkvist survey records Kemperman’s theorem, which gives an upper bound for the growth of product sets \(A\cdot B\) via the quantity \(k(A,B)=|A|+|B|-|A+B|\) [6]. Product‑set growth is the combinatorial shadow of our state‑count process, because iterating an enclosure on a finite set is exactly an iterated product set.

* The adelic‑physics program references Ostrowski’s theorem, which states that every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the standard Archimedean absolute value (completion \(\mathbb{R}\)) or to a \(p\)-adic absolute value for some prime \(p\) (completion \(\mathbb{Q}_{p}\)). This theorem underwrites falsifier F3 and justifies the operator list of Section 3.2; it also supplies the physical motivation for taking the \(p\)-adic and adele strata seriously rather than as curiosities.

* The measurement‑stratigraphy framework explicitly identifies each historical number‑system era with a corresponding distinction operation—marking (\(\mathbb{N}\)), ratio comparison (\(\mathbb{Q}\)), convergent sequences (\(\mathbb{R}_{\text{comp}}\)), lossy projection (\(\mathbb{R}\)), imaginary enclosure (\(\mathbb{C}\)), and \(p\)-adic enclosure (\(\mathbb{Q}_{p}\))—and argues that the tower is a stratified expansion of information. The present paper adopts the same mapping for the operators \(E_{1},\dots,E_{6}\) and attaches quantitative analyses to each step.

* The computable‑real‑boundary paper derives \(\mathbb{N}\) from iterated marking under the Calling rule, positional notation from nested enclosures, and \(\mathbb{Q}\) from enclosures of ratio groups; it identifies the fixed point of finite enclosure operations with the computable reals \(\mathbb{R}_{\text{comp}}\) and places everything beyond that closure in a category that cannot be reduced by any finite sequence of the two primitive laws [9]. Our stratum 3 adopts this identification, and stratum 4 (the lossy continuum) is the structure that lies beyond the computable fixed point.

Together these works provide concrete instances of the operators, the state‑count phenomena, and the deep arithmetic that the stratified‑distinction framework must accommodate.

## 3. Methods

### 3.1 The mark and the distinction operation

We begin with an undifferentiated mark \(M\) satisfying the idempotent law
\[
MM = M,
\]
the *Calling* rule of the Laws of Form calculus (assumed). A *distinction operation* \(D\) partitions a structure into distinguishable classes. An *enclosure operator* \(E\) is a closure‑type operator on structures satisfying
\[
S\subseteq E(S),\qquad E(E(S))=E(S),\qquad S\subseteq T\;\Rightarrow\;E(S)\subseteq E(T).
\]

Each stratum is defined recursively as
\[
S_{i}=E_{i}(S_{i-1}),\qquad i=1,\dots,7,
\]
with the operators indexed by their target stratum.

### 3.2 The strata

| Stratum | Operator \(E_{i}\) | Minimal algebraic structure | Distinguishable‑state count \(N_{i}\) (parameterised) |
|---|---|---|---|
| 0 (the mark) | — | \(\{M\}\) | \(N_{0}=1\) |
| 1 (tally, \(\mathbb{N}\)) | tally enclosure | free monoid on one generator \(\to\mathbb{N}\) with addition | \(N_{1}(n)=n+1\) (depth \(n\)) |
| 2 (ratio, \(\mathbb{Q}\)) | ratio‑compare | field of fractions of \(\mathbb{Z}\) \(\to\mathbb{Q}\) | \(N_{2}\) infinite (no finite truncation) |
| 3 (convergent sequences, \(\mathbb{R}_{\text{comp}}\)) | Cauchy‑sequence enclosure | computable reals \(\mathbb{R}_{\text{comp}}\) | \(N_{3}\) infinite |
| 4 (lossy tree projection, \(\mathbb{R}\)) | Monna‑type projection \(\pi_{M}\) | continuum \(\mathbb{R}\) | \(N_{4}(\varepsilon)=1/\varepsilon\) (real precision \(\varepsilon\)) |
| 5 (phase enclosure, \(\mathbb{C}\)) | phase enclosure | \(\mathbb{C}\cong\mathbb{R}\times S^{1}\) | \(N_{5}\) infinite |
| 6 (divisibility enclosure, \(\mathbb{Q}_{p}\)) | \(p\)-adic completion | \(\mathbb{Q}_{p}\) | \(N_{6}(n)=p^{n}\) (depth \(n\)) |
| 7 (simultaneous valuations, \(\mathbb{A}\)) | adele enclosure | \(\mathbb{A}= \mathbb{R}\times\!\!\prod_{p}'\mathbb{Q}_{p}\) | \(N_{7}\) infinite (restricted product) |

The recovery claims that \(E_{4}\) yields \(\mathbb{R}\), \(E_{5}\) yields \(\mathbb{C}\), and \(E_{7}\) yields \(\mathbb{A}\) are conjectural, consistent with the stratigraphy framework’s own status for these strata [8]. Only the state‑count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below; the formula \(N_{4}(\varepsilon)=1/\varepsilon\) is a definition of the target precision, not a verified recovery claim.

### 3.3 Morphisms and the loss functionals

Between adjacent strata \(S_{i}\to S_{i+1}\) we take the canonical map induced by the operator. The *adjacent‑stratum information‑loss functional* is
\[
\Lambda_{i\to i+1}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{i+1}(\text{params}),
\]
the base‑2 logarithm of the ratio of distinguishable‑state counts.

**Cross‑stratum loss functional.** For any ordered pair of strata \(i,j\) with finite counts we define
\[
\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),
\]
which reduces to the adjacent‑stratum functional when \(j=i+1\). The Monna projection \(\pi_{M}\) maps a depth‑\(n\), base‑\(p\) tree (state count \(N_{6}(n)=p^{n}\)) onto a line at precision \(\varepsilon\) (state count \(N_{4}(\varepsilon)=1/\varepsilon\)); source and target are strata 6 and 4, which are not adjacent. Consequently the Monna loss is a *cross‑stratum* quantity
\[
\Lambda_{\text{Monna}}(n,p,\varepsilon)=\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr).
\]

### 3.4 Falsifiability conditions

* **F1 (stratification).** Exhibit a number system in the historical sequence that no closure operator over the mark can generate.
* **F2 (loss functional).** Exhibit a projection whose state‑count loss decreases as the source is refined at fixed target precision.
* **F3 (operator list).** Exhibit a completion of \(\mathbb{Q}\) outside the list \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\). By Ostrowski’s theorem as stated in [7] every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the Archimedean one or to a \(p\)-adic one, so the theorem itself asserts that no such completion exists; F3 therefore functions as a consistency check on the operator list.
* **F4 (\(\Lambda\) adequacy).** Exhibit two intuitively different projections with identical \(\Lambda\) but markedly different information content.

## 4. Analysis

All inputs are either definitions of Section 3 or explicitly stated here; every arithmetic step is shown.

**Input 1.** Tally depth \(n=9\). (Chosen parameter.)
**Input 2.** Prime \(p=2\), tree depth \(n=10\). (Chosen parameter.)
**Input 3.** Real precision \(\varepsilon=2^{-3}\) (unit interval partitioned into cells of width \(2^{-3}\)). (Chosen parameter.)
**Input 4.** Primes \(\{2,3,5\}\) for the finite adele‑type product. (Chosen parameter.)
**Input 5.** Prime \(p=3\) for the non‑dyadic analysis. (Chosen parameter.)
**Input 6.** Projection parameters for a non‑dyadic example: \(p=3\), \(n=5\), \(\varepsilon=10^{-2}\). (Assumed for illustration.)

### Derivation 1 (tally states)

With \(n=9\) marks the distinguishable counts are \(\{0,1,\dots,9\}\), so
\[
N_{1}(9)=9+1=10.
\]

### Derivation 2 (real‑enclosure states)

The unit interval \([0,1]\) partitioned into cells of width \(\varepsilon=2^{-3}\) contains
\[
N_{4}(\varepsilon)=\frac{1}{\varepsilon}= \frac{1}{2^{-3}} = 2^{3}=8
\]
distinguishable cells.

### Derivation 3 (\(p\)-adic tree states)

The residue ring \(\mathbb{Z}/p^{n}\mathbb{Z}\) with \(p=2\), \(n=10\) has exactly
\[
N_{6}(10)=2^{10}=1024
\]
elements. Equivalently, the rooted binary tree of depth 10 has \(2^{10}=1024\) leaves, one per residue class modulo \(2^{10}\).

### Derivation 4 (Monna cross‑stratum loss)

The Monna projection \(\pi_{M}\) maps the depth‑10 binary tree onto the real line at precision \(\varepsilon=2^{-3}\). As a cross‑stratum comparison \(\Lambda_{6\to4}\) we obtain
\[
\Lambda_{6\to4}= \log_{2}N_{6}(10)-\log_{2}N_{4}(\varepsilon)
= \log_{2}(1024)-\log_{2}(8)=10-3=7.
\]
Checking via the ratio form,
\[
\Lambda_{6\to4}= \log_{2}\!\left(\frac{1024}{8}\right)=\log_{2}(128)=7,
\]
and \(2^{7}=128\) confirms the ratio.

### Derivation 5 (linearity and vanishing)

Fix \(\varepsilon=2^{-3}\) and vary depth \(n\). Since \(N_{6}(n)=2^{n}\) and \(N_{4}(\varepsilon)=2^{3}\),
\[
\Lambda_{6\to4}(n)=\log_{2}(2^{n})-\log_{2}(2^{3})=n-3,
\]
which is strictly increasing in \(n\). At \(n=3\) the loss is
\[
\Lambda_{6\to4}(3)=3-3=0,
\]
so the depth‑3 binary tree and the precision‑\(2^{-3}\) continuum have identical state counts \(2^{3}=8\) and the projection is loss‑free there.

### Derivation 6 (finite simultaneous‑valuation products)

Take the primes \(\{2,3,5\}\). At depth 1 the simultaneous‑valuation state space is the product of residue rings \(\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/5\mathbb{Z}\), with count
\[
N_{7}^{(1)}=2\cdot3\cdot5=30.
\]
At depth 2 it is \(\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/9\mathbb{Z}\times\mathbb{Z}/25\mathbb{Z}\), with count
\[
N_{7}^{(2)}=4\cdot9\cdot25=900.
\]
Both products are finite because each factor is finite; the Chinese remainder theorem makes the simultaneous residue classes independent, so the total count is the product of the individual counts.

### Derivation 7 (non‑dyadic no‑matching)

Fix \(\varepsilon=2^{-3}\) and take \(p=3\). Zero loss requires
\[
n\log_{2}3=\log_{2}(1/\varepsilon)=3,
\]
so the required depth is
\[
n=\frac{3}{\log_{2}3}.
\]
We compute \(\log_{2}3=\ln 3/\ln 2\approx1.584963\), hence
\[
n\approx\frac{3}{1.584963}=1.892789\approx1.893.
\]
Since \(n\) must be an integer depth, no integer solution exists; at \(n=1\) the loss is \(\Lambda_{6\to4}(1)=1.584963-3=-1.415037\) bits (the tree is coarser than the target), and at \(n=2\) it is \(\Lambda_{6\to4}(2)=3.169925-3=0.169925\) bits (the tree is already finer). The loss jumps across zero without vanishing.

### Derivation 8 (projected loss for a non‑dyadic example)

Assume parameters \(p=3\), \(n=5\), \(\varepsilon=10^{-2}\). Then
\[
\log_{2}(1/\varepsilon)=\log_{2}100=\frac{\ln 100}{\ln 2}\approx6.643856,
\]
and
\[
\Lambda_{6\to4}=5\log_{2}3-\log_{2}100\approx5\times1.584963-6.643856\approx1.280957\;\text{bits}.
\]
We report this as a projection under the stated assumptions.

## 5. Results

All quantities below are obtained from the explicit derivations of Section 4; no simulation, measurement, or external data are used.

| Quantity | Value | Source derivation |
|---|---|---|
| Tally states at depth \(n=9\) | \(N_{1}(9)=10\) | Derivation 1 |
| Real‑enclosure cells at \(\varepsilon=2^{-3}\) | \(N_{4}=8\) | Derivation 2 |
| Binary‑tree states at depth \(n=10\) | \(N_{6}(10)=1024\) | Derivation 3 |
| Monna cross‑stratum loss for \((p=2,n=10,\varepsilon=2^{-3})\) | \(\Lambda_{6\to4}=7\) bits | Derivation 4 |
| Linear law \(\Lambda_{6\to4}(n)=n-3\) (fixed \(\varepsilon\)) | \(\Lambda_{6\to4}(n)=n-3\) bits | Derivation 5 |
| Depth at which loss vanishes (dyadic case) | \(n=3\) (so \(\Lambda_{6\to4}=0\)) | Derivation 5 |
| Finite simultaneous‑valuation product at depth 1 | \(30\) states | Derivation 6 |
| Finite simultaneous‑valuation product at depth 2 | \(900\) states | Derivation 6 |
| Non‑dyadic no‑matching depth (base 3) | No integer solution; required \(n\approx1.893\) | Derivation 7 |
| Projected loss for \((p=3,n=5,\varepsilon=10^{-2})\) | \(\approx1.28\) bits | Derivation 8 |

**Result R1.** The Monna cross‑stratum loss obeys the exact linear law
\[
\Lambda_{6\to4}(n)=n-3\;\text{bits}
\]
for base \(p=2\) and precision \(\varepsilon=2^{-3}\); increasing the tree depth strictly increases the information loss relative to a fixed‑precision continuum target.

**Result R2.** A loss‑free matching occurs at the dyadic pair \((n=3,\varepsilon=2^{-3})\), where the \(2\)-adic tree and the real interval have identical state counts (\(2^{3}=8\)). No integer depth yields zero loss for the non‑dyadic base \(p=3\) at the same precision.

**Result R3.** The finite simultaneous‑valuation product over the primes \(\{2,3,5\}\) yields \(30\) states at depth 1 and \(900\) states at depth 2, illustrating how the adele‑type construction multiplies state counts across independent \(p\)-adic components.

## 6. Discussion

### Limitations
* The recovery claims for strata 4, 5, and 7 remain conjectural; state‑count arithmetic is verified only for strata 0, 1, 3, and 6 at finite depth.
* The loss functional \(\Lambda\) counts *states* but not *structure*: two projections can destroy the same number of bits while destroying very different algebraic features (e.g., order versus branching).
* The Monna analysis assumes the tree is exactly a \(p\)-adic ball in state count; a more general tree‑like limit with a different branching profile would alter \(\Lambda\).
* The finite adele‑type product of Derivation 6 is a toy: the true adele ring is a restricted product including the real factor, and the count of 30 says nothing about its topology.
* \(\Lambda\) is defined only for finite state counts; at infinite depth both source and target counts diverge, requiring renormalisation or a rate formulation.

### Failure modes
* **Non‑canonical realizations.** The existence of many valid digit sets for a given base (e.g., \(\{1,2\}\) for base \(-2\)) shows that a single enclosure operator can admit multiple inequivalent concrete realizations; the operator, not the digit set, determines the stratum [5].
* **Operator‑list incompleteness.** Ostrowski’s theorem guarantees that every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the Archimedean absolute value or to a \(p\)-adic one [7]. If a number system in the historical sequence required a completion outside \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\), the present operator list would be incomplete, falsifying F3.
* **\(\Lambda\) inadequacy.** Two intuitively different projections could share the same \(\Lambda\) value while differing dramatically in preserved structure, mirroring the failure of classical \(\beta\)-numbers in Carnot groups [2]; this would falsify F4 and motivate a stratified refinement of \(\Lambda\).

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**
Researchers who must choose a numeric representation for formal models—particularly in mathematical physics, constructive analysis, and exact‑arithmetic software—are the principal users of the loss functional $\Lambda$ and the state‑count formulas derived in Sections 4–5. When a simulation requires a target real precision $\varepsilon$, the user can compute the bit‑loss
\[
\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr)
\]
(Derivation 5) for any candidate $p$‑adic depth $n$. If $\Lambda_{6\to4}=0$, the $p$‑adic tree can replace the real interval without any information loss; the dyadic case $p=2$, $n=3$, $\varepsilon=2^{-3}$ provides the first such loss‑free matching (Result R2). Consequently, a modeler can decide to store data in a binary‑tree structure of depth 3 rather than in floating‑point format, thereby guaranteeing that no bits are discarded by the projection to $\mathbb{R}$.

**(b) Technology readiness.**
The work is purely analytical, has not undergone peer review, and involves no hardware or software implementation. According to NASA’s Technology Readiness Level definitions, it resides at TRL 1–2 (basic principles observed). Analytical extensions never exceed TRL 3; therefore no claim of manufacturing or deployment readiness is made.

**(c) Minimal next experiment.**
A concrete computational experiment that would falsify the monotonicity claim of F2 (that $\Lambda_{6\to4}(n)$ increases with $n$ for fixed $\varepsilon$) consists of the following steps, expressed conditionally:

1. Generate the residue set $\mathbb{Z}/p^{n}\mathbb{Z}$ for a chosen odd prime $p$ (e.g., $p=3$) and depth $n\in\{1,2,3\}$.
2. Map each residue class to a sub‑interval of $[0,1]$ of width $\varepsilon$ (e.g., $\varepsilon=10^{-2}$) by a deterministic Monna‑type rule.
3. Count the number of distinct real cells $N_{4}(\varepsilon)=1/\varepsilon$ (Derivation 2) and compute the empirical loss $\Lambda_{\text{emp}}=\log_{2}N_{6}(n)-\log_{2}N_{4}(\varepsilon)$.
4. Compare $\Lambda_{\text{emp}}$ with the predicted value $\Lambda_{6\to4}=n\log_{2}p-\log_{2}(1/\varepsilon)$ (Derivation 5).

If for any $(p,n,\varepsilon)$ the measured loss deviates by more than $0.1$ bits from the predicted value, the linear law $\Lambda_{6\to4}(n)=n\log_{2}p-\log_{2}(1/\varepsilon)$ would be falsified, thereby invalidating F2.

**(d) First‑order engineering constraints.**

*Data representation.*  The experiment requires storing $p^{n}$ residues; this imposes a memory requirement of at least $p^{n}$ integers (Derivation 3).

*Precision handling.*  The real target demands $1/\varepsilon$ cells; for $\varepsilon=10^{-2}$ this is $100$ cells (Derivation 2).

*Computational throughput.*  Mapping each of the $p^{n}$ residues to a real cell entails $O(p^{n})$ elementary operations; runtime therefore scales linearly with $p^{n}$.

*Software tooling.*  Exact integer arithmetic (e.g., arbitrary‑precision libraries) is needed to avoid overflow when $p^{n}$ exceeds native word size.

All of these constraints follow directly from the state‑count formulas; any deviation would constitute an open question for future work.

**(e) Projected cost and performance bounds (assumptions).**
Assume a single elementary mapping operation costs $c_{\text{op}}=10^{-6}\,\text{s}$ (typical for a modern CPU integer operation). The total runtime $T$ for depth $n$ and base $p$ is then
\[
T = c_{\text{op}}\;p^{n}.
\]
For the dyadic loss‑free case $p=2$, $n=3$ this yields $T \approx 10^{-6}\times2^{3}=8\times10^{-6}\,\text{s}$, well within interactive limits. For the non‑dyadic example $p=3$, $n=5$ the projection gives $T \approx 10^{-6}\times3^{5}=2.43\times10^{-4}\,\text{s}$. These figures are projections based on the arithmetic cost model and the state‑count $N_{6}(n)=p^{n}$; actual timings will depend on implementation details.

**(f) Direct risks and misuse pathways.**
Treating the scalar loss $\Lambda$ as a complete measure of suitability for replacing a real‑valued representation ignores the structural differences highlighted in the Limitations (Section 6). Deploying a $p$‑adic data structure solely because it yields a lower $\Lambda$ could introduce hidden bugs in algorithms that rely on the order properties of $\mathbb{R}$. Moreover, the cost projection assumes idealised operation costs; real systems may exhibit latency spikes, memory fragmentation, or security vulnerabilities when handling large $p^{n}$ tables. Awareness of these risks is essential before any engineering adoption.

## 9. Conclusion

Overall, the stratified distinction approach offers a unifying lens for interpreting the emergence of classical number systems as successive information‑theoretic expansions of a primitive mark. By grounding each operator in explicit state‑count formulas and by exposing the quantitative trade‑offs through the loss functional $\Lambda$, the framework makes concrete predictions that can be tested in future computational or experimental settings. The methodology also suggests pathways for extending the hierarchy—such as incorporating non‑canonical digit encodings, exploring alternative branching structures in the tree‑to‑continuum projection, or refining $\Lambda$ with stratified $\beta$‑number techniques—to capture richer structural aspects beyond mere state counts. These extensions promise to deepen the connection between foundational mathematics and practical measurement, and to clarify the role of different completions of $\mathbb{Q}$ in both theoretical and applied contexts.

The quantitative framework presented here opens avenues for systematic evaluation of number‑system choices in modeling and computation, allowing practitioners to balance precision, information loss, and implementation constraints in a principled manner.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 14 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=1907.12657&amp;start=0&amp;max_results=1
[2] A note on Tate's conjectures for abelian varieties. arXiv:2112.15164v2. https://arxiv.org/abs/2112.15164v2
[3] Proof of a congruence for harmonic numbers conjectured by Z.-W. Sun. arXiv:1108.1171v2. https://arxiv.org/abs/1108.1171v2
[4] Stratified $β$-numbers and traveling salesman in Carnot groups. arXiv:1902.03268v2. https://arxiv.org/abs/1902.03268v2
[5] Conjectures on congruences involving binomial coefficients and Apéry-like numbers. arXiv:2007.12042v4. https://arxiv.org/abs/2007.12042v4
[6] The Caccetta-Haggkvist conjecture and additive number theory. arXiv:math/0603469v1. https://arxiv.org/abs/math/0603469v1
[7] Noncanonical number systems in the integers. arXiv:0804.2190v1. https://arxiv.org/abs/0804.2190v1
[8] New conjectures involving binomial coefficients and Apéry-like numbers. arXiv:2111.04538v2. https://arxiv.org/abs/2111.04538v2
[9] On the number of distinct prime factors of a sum of super-powers. arXiv:1511.08784v3. https://arxiv.org/abs/1511.08784v3
[10] https://papers.qnfo.org/papers/number-systems-as-stratified-distinction-operations-an-enclosure-hierarchy-over-. QNFO: Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark.


## Source material (fetched from arXiv)

TITLE: arXiv Query: search_query=&amp;id_list=2310.17310&amp;start=0&amp;max_results=1

ABSTRACT: We study global regularity of nonlinear systems of partial differential equations depending on the symmetric part of the gradient with Dirichlet boundary conditions. These systems arise from variational problems in plasticity with power growth. We cover the full range of exponents $p \in (1,\infty)$. As a novelty the degenerate case for $p&gt;2$ is included. We present a unified approach for all exponents by showing the regularity for general systems of Orlicz growth.

FULL TEXT (https://arxiv.org/html/2310.17310), excerpts of its own sections:
§ 1. Introduction: In this paper we investigate the global regularity of solutions of nonlinear elliptic systems arising from problems in plasticity, see e.g.  [ FS00 ] . In particular, we are interested in systems of the form (1.1) $\displaystyle-\operatorname{div}\big((\delta+|{\varepsilon}u|)^{p-2}{\varepsilon}u\big)$ $\displaystyle=f\qquad\text{in }\Omega$ $\displaystyle u$ $\displaystyle=0\qquad\text{on }\partial\Omega.$ Here, $\Omega\subset\mathbb{R}^{n}$ is a bounded domain, $p\in(1,\infty)$ , $\delta\geq 0$ , $u:\Omega\rightarrow\mathbb{R}^{n}$ is a vector field and ${\varepsilon}u\coloneqq\tfrac{1}{2}(\nabla u+(\nabla u)^{T})$ is the symmetric part of $\nabla u$ , also abbreviated as symmetric gradient . Similar systems arise in the context of non-Newtonian fluids (power-law fluids), where additionally a pressure and a incompressibility constraint appears, see e.g.  [ MNRR96 ] . For $\delta=0$ our system is also known as the symmetric $p$ -Laplace system . Sometimes in the literature the case $\delta=0$ and $1 singular and the case $\delta=0$ and $p>2$ is called degenerate . [...]
§ 2. Objective and main result: Our main focus is the study of system ( 1.1 ). This fits nicely in the more general framework of systems with Orlicz growth. In this section we introduce the corresponding partial differential system and the necessary background on Orlicz spaces and N-functions.
§ 2.1. Uniformly convex Orlicz spaces: We begin with a bit of standard notation. With $a\lesssim b$ we mean that there exists a constant $c>0$ independent of all important quantities such that $a\leq cb$ . We use the notation $a\lor b\coloneqq\max(a,b)$ and $a\land b\coloneqq\min(a,b)$ . For a measurable set $U\subset\mathbb{R}^{n}$ and $f\in L^{1}_{\mathrm{loc}}(\mathbb{R}^{n})$ we denote by $|U|$ the Lebesgue measure $\mathcal{L}^{n}(U)$ and define $\langle{f}\rangle_{U}\coloneqq\mathop{}\mkern-3.0mu\mathchoice{\hbox to0.0pt{$\displaystyle\vbox{\hbox to5.83331pt{\hss$\textstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\textstyle\vbox{\hbox to5.83331pt{\hss$\scriptstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\scriptstyle\vbox{\hbox to5.1215pt{\hss$\scriptscriptstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\scriptscriptstyle\vbox{\hbox to4.82639pt{\hss$\scriptscriptstyle{-}$\hss}}$\hss}}\mkern-3.0mu\int_{U}f(x)\,dx\coloneqq\dfrac{1}{|U|}\int_{U}f(x)\,dx.$ For a ball $B\subset\mathbb{R}^{n}$ let $2B$ denote the ball with the same center but twice the diameter. Usually, we denote the radius of a ball  $B$ by  $r$ . [...]
§ 2.2. Main result: In this section we introduce our system and present our main result on global regularity. We denote by $\partial_{i}$ the partial derivative and by $\nabla=(\partial_{1},\dots,\partial_{n})$ the gradient of either a scalar function, a vector field or a tensor field. If $A:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n\times n}$ is a function then by $\operatorname{div}A:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ we mean the row-wise divergence of $A$ , i.e. $\operatorname{div}A=\sum_{k=1}^{n}\partial_{k}A_{j,k}$ . For matrices $M,N\in\mathbb{R}^{n\times n}$ we define the Kronecker product $A:B\coloneqq\sum_{i,j=1}^{n}A_{ij}B_{ij}$ and for vectors $u$ , $v$ we set $u\otimes v\coloneqq(u_{i}v_{j})_{ij}$ . For a vector field $u:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ we define the symmetric gradient ${\varepsilon}u$ via ${\varepsilon}u\coloneqq\tfrac{1}{2}\big(\nabla u+(\nabla u)^{T}\big).$ In the following let $\varphi$ be a fixed uniformly convex N-function with indices of uniform convexity $p^{-}$ and $p^{+}$ . [...]

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

TITLE: arXiv Query: search_query=&amp;id_list=2310.17310&amp;start=0&amp;max_results=1
arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
arXiv:0706.3841v1 | Arithmetic lattices and weak spectral geometry

## QNFO corpus context (Vectorize)

QNFO: Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim | https://papers.qnfo.org/papers/acrp04-five-smooth-audit
QNFO: The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra | https://papers.qnfo.org/papers/distinction-based-ultrametric
QNFO: The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference | https://papers.qnfo.org/papers/reentrant-distinctions
QNFO: Implications for Computing and Quantum Error Correction | https://papers.qnfo.org/papers/prime-valuation-qec-implications

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] TITLE: arXiv Query: search_query=&amp;id_list=2310.17310&amp;start=0&amp;max_results=1

ABSTRACT: We study global regularity of nonlinear systems of partial differential equations depending on the symmetric part of the gradient with Dirichlet boundary conditions. These systems arise from variational problems in plasticity with power growth. We cover the full range of exponents $p \in (1,\infty)$. As a novelty the degenerate case for $p&gt;2$ is included. We present a unified approach for all exponents by showing the regularity for general systems of Orlicz growth.
  Full text (https://arxiv.org/html/2310.17310), excerpts of its own sections:
  § 1. Introduction: In this paper we investigate the global regularity of solutions of nonlinear elliptic systems arising from problems in plasticity, see e.g.  [ FS00 ] . In particular, we are interested in systems of the form (1.1) $\displaystyle-\operatorname{div}\big((\delta+|{\varepsilon}u|)^{p-2}{\varepsilon}u\big)$ $\displaystyle=f\qquad\text{in }\Omega$ $\displaystyle u$ $\displaystyle=0\qquad\text{on }\partial\Omega.$ Here, $\Omega\subset\mathbb{R}^{n}$ is a bounded domain, $p\in(1,\infty)$ , $\delta\geq 0$ , $u:\Omega\rightarrow\mathbb{R}^{n}$ is a vector field and ${\varepsilon}u\coloneqq\tfrac{1}{2}(\nabla u+(\nabla u)^{T})$ is the symmetric part of $\nabla u$ , also abbreviated as symmetric gradient . Similar systems arise in the context of non-Newtonian fluids (power-law fluids), where additionally a pressure and a incompressibility constraint appears, see e.g.  [ MNRR96 ] . For $\delta=0$ our system is also known as the symmetric $p$ -Laplace system . Sometimes in the literature the case $\delta=0$ and $1 singular and the case $\delta=0$ and $p>2$ is called degenerate . [...]
  § 2. Objective and main result: Our main focus is the study of system ( 1.1 ). This fits nicely in the more general framework of systems with Orlicz growth. In this section we introduce the corresponding partial differential system and the necessary background on Orlicz spaces and N-functions.
  § 2.1. Uniformly convex Orlicz spaces: We begin with a bit of standard notation. With $a\lesssim b$ we mean that there exists a constant $c>0$ independent of all important quantities such that $a\leq cb$ . We use the notation $a\lor b\coloneqq\max(a,b)$ and $a\land b\coloneqq\min(a,b)$ . For a measurable set $U\subset\mathbb{R}^{n}$ and $f\in L^{1}_{\mathrm{loc}}(\mathbb{R}^{n})$ we denote by $|U|$ the Lebesgue measure $\mathcal{L}^{n}(U)$ and define $\langle{f}\rangle_{U}\coloneqq\mathop{}\mkern-3.0mu\mathchoice{\hbox to0.0pt{$\displaystyle\vbox{\hbox to5.83331pt{\hss$\textstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\textstyle\vbox{\hbox to5.83331pt{\hss$\scriptstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\scriptstyle\vbox{\hbox to5.1215pt{\hss$\scriptscriptstyle{-}$\hss}}$\hss}}{\hbox to0.0pt{$\scriptscriptstyle\vbox{\hbox to4.82639pt{\hss$\scriptscriptstyle{-}$\hss}}$\hss}}\mkern-3.0mu\int_{U}f(x)\,dx\coloneqq\dfrac{1}{|U|}\int_{U}f(x)\,dx.$ For a ball $B\subset\mathbb{R}^{n}$ let $2B$ denote the ball with the same center but twice the diameter. Usually, we denote the radius of a ball  $B$ by  $r$ . [...]
  § 2.2. Main result: In this section we introduce our system and present our main result on global regularity. We denote by $\partial_{i}$ the partial derivative and by $\nabla=(\partial_{1},\dots,\partial_{n})$ the gradient of either a scalar function, a vector field or a tensor field. If $A:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n\times n}$ is a function then by $\operatorname{div}A:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ we mean the row-wise divergence of $A$ , i.e. $\operatorname{div}A=\sum_{k=1}^{n}\partial_{k}A_{j,k}$ . For matrices $M,N\in\mathbb{R}^{n\times n}$ we define the Kronecker product $A:B\coloneqq\sum_{i,j=1}^{n}A_{ij}B_{ij}$ and for vectors $u$ , $v$ we set $u\otimes v\coloneqq(u_{i}v_{j})_{ij}$ . For a vector field $u:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ we define the symmetric gradient ${\varepsilon}u$ via ${\varepsilon}u\coloneqq\tfrac{1}{2}\big(\nabla u+(\nabla u)^{T}\big).$ In the following let $\varphi$ be a fixed uniformly convex N-function with indices of uniform convexity $p^{-}$ and $p^{+}$ . [...]
[2] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[3] arXiv:0706.3841v1 | Arithmetic lattices and weak spectral geometry
  This note is an expansion of three lectures given at the workshop "Topology, Complex Analysis and Arithmetic of Hyperbolic Spaces" held at Kyoto University in December of 2006 and will appear in the proceedings for this workshop.
  Full text (https://arxiv.org/html/0706.3841v1), excerpts of its own sections:
  § Introduction: Our attention in this note will be on the non-exceptional real rank one symmetric spaces arising from the simple Lie groups $\SO(n,1)$ , $\SU(n,1)$ , and $\Sp(n,1)$ and finite volume quotients of these spaces. These spaces and their quotients are known as real, complex, and quaternionic hyperbolic $n$ –space and real, complex, and quaternionic hyperbolic $n$ –manifolds , respectively. For these spaces, our aim is 2-fold: ( $\maltese$ ) Provide a description of some of the arithmetic quotients of these symmetric spaces. ( $\maltese$ ) Produce interesting examples of closed quotients of these symmetric spaces with regard to various spectral problems. These two goals are essentially independent, although in general the former is the only means we have for producing examples in general; in particular, to achieve the latter we are forced to consider arithmetic constructions. We shall take a leisurely and loose approach to these goals, providing some background but largely leaving assertions unproven. [...]
  § Organization of the article: This note is organized into five sections. In the first section, we briefly recall the definitions of real, complex, and quaternionic hyperbolic $n$ –space. In the second section, we provide a description for constructing certain arithmetic lattices in the associated isometry groups for these spaces. In the third section, we discuss some recent results on isospectral manifolds modelled on these symmetric spaces (and more general symmetric spaces of noncompact type). In the four section, we discuss some recent work on weaker spectral constructions. In the fifth section, we discuss some variants of Sunada’s method used to produce the asserted examples from Section 4.
  § 1 Hyperbolic spaces: For completeness, a short section introducing real, complex, and quaternionic hyperbolic space, their isometry groups, and their orbifold quotients is provided below. The reader should look to [ 48 ] , [ 14 ] , and [ 21 ] for more thorough treatments of this material.
  § Notation: Throughout, $X$ will denote either $\mathbf{R},\mathbf{C}$ , or $\mathbb{H}$ . On $X$ , we have the involution $*$ defined by $x^{*}=\begin{cases}\text{identity},&X=\mathbf{R}\\ \text{complex conjugation},&X=\mathbf{C}\\ \text{quaternionic conjugation},&X=\mathbb{H}.\end{cases}$ We extend this to a map on matrices $*\colon\Mat(r,s;X)\longrightarrow\Mat(s,r;X)$ by applying $*$ to the coefficients of the matrix and then taking its transpose.
  § 5.4 A variant of Sunada’s theorem: One of the main results of [ 23 ] is the following variation on Sunada’s theorem. Theorem 5.1 . Let $M$ be a Riemannian manifold, $G$ a group, and $H$ and $K$ elementwise conjugate subgroups of $G$ . (1) If $\pi_{1}(M)$ admits a homomorphism onto $G$ , then $L(M_{H})=L(M_{K})$ for the covers $M_{H}$ and $M_{K}$ associated to the pullback subgroups of $H$ and $K$ . (2) If, in addition, $H$ and $K$ are primitive in $G$ and $\pi_{1}(M)$ has the property that any pair of distinct maximal cyclic subgroups of $\Gamma$ intersect trivially, then $L_{p}(M_{H})=L_{p}(M_{K})$ . (3) If instead $H$ and $K$ are fixed point equivalent, then $E(M_{H})=E(M_{K})$ . The reader will note that on top of being less natural in regard to the associated group theoretic condition, the production of primitive geodesic length equivalent manifolds also requires conditions on the fundamental group $\pi_{1}(M)$ of the Riemannian manifold. The condition on maximal cyclic subgroups required in our proof is likely not needed (that some condition is required is seen from examples in [ 23 ] ).
[4] QNFO: Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim | https://papers.qnfo.org/papers/acrp04-five-smooth-audit
  ACRP-04 statistical audit. Verdict: CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT. p_global=0.116; 2 claimed-fit arithmetic errors; 5 non-optimal triples; precise ratios deviate 4-9138 sigma; pre-registered neutrino prediction trivially passes.
  Full text (https://papers.qnfo.org/papers/acrp04-five-smooth-audit), excerpts of its own sections:
  § Statistical Audit of the Pythagorean Semigroup Mass-Ratio Claim: **Author:** Rowan Brad Quni-Gudzinas (QNFO Research) | **Date:** 2026-07-31 **Program:** ACRP-04 | **License:** QNFO-ULA ---
  § 1.1 Statement (v3.2 §7.2, verbatim structure): > "ALL Standard Model mass ratios are Pythagorean ($2^a \cdot 3^b \cdot 5^c$) to within approximately 1%." Nine ratios are fitted, with maximum claimed deviation 0.29%. The paper's own §7.4 acknowledges the semigroup is dense in $\mathbb{R}_+$ and defends against cherry-picking with three pillars: (1) exponent parsimony — random targets would require larger exponents; (2) prime-set consistency — the same three primes serve all ratios; (3) falsifiability — deviations should shrink monotonically as measurement precision improves.
  § 2.1 Finding A: Two claimed fits are arithmetically false: | Ratio | Printed triple | Printed value | Actual value | Actual deviation | Claimed deviation | |:------|:---------------|:--------------|:-------------|:-----------------|:------------------| | $m_\tau/m_\mu$ | $(-3,8,-5)$ | 16.80 | **0.2624** | 98.4% | 0.14% | | $m_h/m_e$ | $(-5,14,-4)$ | 244888.0 | **239.15** | 99.9% | 0.12% | The value $244{,}888$ is not a 3-smooth number at all: $244{,}888 = 2^3 \cdot 7 \cdot 4373$. The v3.2 §10.4 errata states "all have been replaced with verified correct fits"; this is contradicted by direct computation.
  § 2.2 Finding B: Five of nine triples are not optimal: An exhaustive bounded search ($|a|,|b|,|c| \leq 14$) finds strictly better triples than the paper's for five ratios: | Ratio | Paper's triple | Paper's dev | Optimal triple | Optimal dev | |:------|:---------------|:------------|:---------------|:------------| | $m_\mu/m_e$ | $(6,4,-2)$ | 0.29% | $(-2,-10,11)$ | 0.02% | | $m_\tau/m_\mu$ | $(-3,8,-5)$ | (98.4%) | $(-11,-11,14)$ | 0.02% | | $m_b/m_s$ | $(-6,-3,7)$ | 0.20% | $(2,11,-6)$ | 0.11% | | $m_Z/m_e$ | $(-6,6,6)$ | 0.26% | $(3,-7,11)$ | 0.09% | | $m_h/m_e$ | $(-5,14,-4)$ | (99.9%) | $(6,-13,14)$ | 0.07% | With optimal triples, the maximum deviation across all nine ratios drops to 0.11%. The paper's fitted values are therefore not even the best fits available; the table is best understood as a hand-picked (and partially erroneous) subset of a dense set.
  § 5.2 Result: $R = 2.453 \times 10^{-3} / 7.53 \times 10^{-5} = 32.576$. Best 3-smooth fit: $2^{-5} 3^{-1} 5^5 = 32.552$, deviation **0.07%**. The prediction "passes."
  § 8. Conclusion: **Verdict: `[CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT]`** The Pythagorean semigroup mass-ratio claim of the Adelic Cross-Domain Program v3.2 does not survive statistical audit as evidence for structure. Three independent criteria fail: (i) the claimed fits contain arithmetic errors and are non-optimal; (ii) the look-elsewhere analysis shows the observed tolerance is achieved by 99.8% of random ratio sets ($p_{\text{global}} = 0.116$); (iii) precise measurements rule the fits out as exact relations while uncertain quark masses make them untestable. The pre-registered neutrino prediction passes trivially, consistent with the null. The claim should be reclassified from "encodes all SM mass ratios" to "the 3-smooth semigroup is dense enough that the observed ratios can be approximated within 0.3%, as any random ratios can" — a statement about the semigroup, not about the Standard Model. Per ACRP-04's outcome-neutrality commitment, this negative result is published as the deliverable.
[5] QNFO: The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra | https://papers.qnfo.org/papers/distinction-based-ultrametric
  Quantum mechanics is written in one completion of the rational numbers, the real line, though Ostrowski's theorem gives one completion for every prime. A line of work reads physical structure through those other places, but its empirical tests of prime-specific geometry in physical systems have repeatedly returned null results. This paper separates what survives from what does not. The surviving o
  Full text (https://papers.qnfo.org/papers/distinction-based-ultrametric), excerpts of its own sections:
  § 1. The Archimedean shadow: Quantum mechanics is written in the Archimedean completion of the rational numbers. The complex Hilbert space of the standard formalism is built on the real line, and the real line is one completion among all of them: Ostrowski's theorem classifies the completions of the rational numbers as the real line and one p-adic field per prime [@quni2026ump004]. The primes are the other places. Their structure is multiplicative — unique factorization — never additive. A research line reads physical structure through those places. Its strongest published results are isomorphisms of mathematical structure: the unrestricted exponent rule on an integer lattice gives the Riemann zeta function and Bose-Einstein occupation, the squarefree rule gives a ratio of zeta values and Fermi-Dirac occupation, and the bounded-occupation family between them carries no exchange phase [@quni2026stats; @quni2026anyons; @quni2026res023]. Those results are exact and computationally verified. [...]
  § 2. The distinction-based ultrametric formula: A finite-resolution world distinguishes states rather than positioning them. Two states are either distinct or not at a given resolution, and the natural distance is the number of distinctions required to separate them: $$d(a,b) = \min\left\{\text{number of distinctions required to separate } a \text{ and } b\right\}.$$ On a finite rooted tree whose leaves are the states, this is the depth of the lowest common ancestor, measured from the leaves. If the leaves sit at depth $k$ and the lowest common ancestor of $a$ and $b$ is at depth $\ell$, then $d(a,b) = k - \ell$. This is the cophenetic distance of classical taxonomy [@sokal1962; @jardine1971; @johnson1967]. Two facts are exact and were verified in code (Section 5). First, the induced distance satisfies the ultrametric inequality $$d(a,c) \le \max(d(a,b), d(b,c)),$$ which follows because among any three leaves, the two largest lowest-common-ancestor depths coincide. [...]
  § 3. What has been tested, and what has not: The empirical tests of prime-specific structure in physical systems are a ledger of nulls, and they should be read by channel, not lumped together. The geometric channel has been tested and nullified. The CMB shows no log-periodic oscillations (a certified radix-agnostic null at $p = 0.89$ on Planck 2018 data [@quni2026cmbnull]) and only upper bounds in the bispectrum [@quni2026cmbbis]. The Fenna-Matthews-Olson coupling matrix is anti-ultrametric (cophenetic correlation 0.426, $p = 0.984$), and its exact-clustering test returns $p = 0.598$ [@quni2026register]. A generic clock-rest coupling violates Parisi ultrametricity in 29-35% of simulated instances [@quni2026register]. [...]
  § 11. Conclusion: The distinction-based ultrametric — the number of distinctions required to separate two states — is a finite, prime-free hierarchy distance, an ultrametric on any finite hierarchy, and independent of the realization chosen. It is exact and it is verified. The empirical question it carries is statistical, not geometric: whether physical spectra hold arithmetic information beyond universal random-matrix statistics. The machinery to ask that question is implemented, validated on known answers, and applied to two real molecular spectra, with a first negative result in the pair-correlation channel. The question is now posed, with null models and a disconfirmation criterion, for the larger spectra that will decide it.
[6] QNFO: The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference | https://papers.qnfo.org/papers/reentrant-distinctions
  This treatise develops a single thesis: that the primitive act of distinction — the drawing of a boundary between marked and unmarked — generates, under the discipline of re-entry and linear resource management, the constants $e$ and $\pi$, the landscape of completions of the rational numbers, the loop–tree duality of the Langlands program, the mathematical structure of quantum theory, and the gra
  Full text (https://papers.qnfo.org/papers/reentrant-distinctions), excerpts of its own sections:
  § So What? Why Should a Reader Care About This Research?: **The stakes.** This treatise develops a single thesis: that the primitive act of distinction — the drawing of a boundary between marked and unmarked — generates, under the discipline of re-entry and linear resource management, the constants $e$ and $\pi$, the landscape of completions of the rational numbers, the loop–tree duality of the Langlands program, the mathematical structure of quantum theory, and the grammar of a universal logical language. If the thesis holds even in part, the most fundamental constants and structures of mathematics and physics are not axioms of nature but consequences of a single primitive act. [...]
  § 3.2 The oscillation theorem: The re-entrant form $f = \overline{f}$ generates the sequence $$\overline{\phantom{x}}, \overline{\overline{\phantom{x}}}, \overline{\overline{\overline{\phantom{x}}}}, \ldots$$ which alternates between the marked and unmarked states. Two readings are possible: 1. **The paradoxical reading:** the form has no stable value in the two-valued arithmetic; it is inconsistent. 2. **The temporal reading:** the form is a clock. Each crossing is a tick; the value is not fixed but *changes*; the form is the simplest possible model of a time-dependent system [established as a reading — Spencer-Brown 1969; Kauffman's extension of the waveform interpretation]. This treatise adopts the temporal reading as its primary interpretation, and this choice is the bridge from logic to process that Parts III–VIII exploit.
  § 36.2 These constants are theorems of the type system: The status of the claim: in a *specific model* of the type theory (e.g., the cohesive $\infty$-topos of smooth spaces with the circle type), the trace of the identity computes $\pi$ and the fixed point of the differential exponential computes $e$ [established — the individual computations in models are standard mathematics]. The claim that the *syntax* of the type theory forces these values is [my conjecture] and is the subject of Appendix D (the computational implementation). **Falsifiability condition:** the claim is formally falsifiable: if the formal system of this part cannot derive $e^{i\pi} = -1$ (Part III, §12) without importing the real numbers and the exponential function as external axioms, the claim of a purely logical derivation fails. Appendix D sketches the verification. ---
  § 37.2 Every domain translates into this language: The claim of §37.1 is the treatise's universal claim: the re-entrant distinction, disciplined by linearity, differentiation, and tracing, in a cohesive setting, is the *generative grammar* of the treatise's domains. The claim is [my conjecture] as a complete formalization — the full translation of all domains into a single type theory is a research program (Appendix D). The individual translations (each row of the table) are the content of the corresponding parts of the treatise, where the modal readings are labeled [my conjecture] and the mathematics is [established]. --- ---
  § 40.2 The remainder is the unmarked state, enriched by the entire journey: [PHILOSOPHY] The erasure is not a return to ignorance: the unmarked state at the end of the treatise is *enriched* by the entire journey — it is the state that contains, implicitly, the whole structure that was explicitly developed. This is the treatise's final philosophical claim: the mark's journey is a *deepening of the unmarked state*, and the distinction's ultimate content is the enriched void from which it came. The loop closes. The tree is still.
[7] QNFO: Implications for Computing and Quantum Error Correction | https://papers.qnfo.org/papers/prime-valuation-qec-implications
  The anchor paper introduced the *branch-depth reading*: the p-adic valuation $v_p(n)$ is a measure of depth along a prime branch of the integer factorization tree (not a measure of size), and because the tensor product multiplies Hilbert-space dimensions, $v_2(\dim H) = n$ counts tensor-branch depth for n qubits. This follow-on subjects that reading to its own stated falsifiability condition in th
  Full text (https://papers.qnfo.org/papers/prime-valuation-qec-implications), excerpts of its own sections:
  § 1.1 What the anchor paper established: *Prime Valuation Depth* developed three claims, each with a stated falsifiability condition: 1. **[TERRITORY — established, Ostrowski 1916]** Every positive integer is a finite product of prime powers; $v_p(n)$ is depth along the prime-p branch, not size. 2. **[MAP — interpretive]** The valuation-as-depth reading is a bridge between the calculus of indications (branching distinctions) and number theory (the prime divisor tree). 3. **[MAP — interpretive]** The tensor product multiplies dimensions, so prime factorization of dim H labels branch types and $v_p(\dim H)$ counts branch depth; the no-cloning theorem is then the impossibility of a linear diagonal map — cloning is nonlinear in the amplitudes, and quantum evolution preserves only linear structure.
  § 1.2 The honest starting point of this paper: The anchor paper labels its own quantum reading as "interpretive rather than new physics" and attaches the falsifiability condition: *disconfirmed if the reading yields no explanatory or predictive content beyond the standard formalism — i.e., if it is pure relabeling.* This follow-on takes that condition seriously and applies it to the two domains the anchor flagged for later work. The result, reported here without flinching, is that **the most obvious extension — reading $[[n,k,d]]$ parameters as valuations — is largely pure relabeling.** This is not a failure of the program; it is the falsifiability machinery doing its job, and it sharpens the question to the one place where the branch-depth vocabulary could carry real weight.
  § 1.3 External precedent (confirmation-bias correction): The anchor's quantum reading does not occur in a vacuum. The categorical content — that quantum processes form a compact-closed (monoidal but non-Cartesian) category, and that no-cloning follows from this — is established in the categorical quantum mechanics literature [Abramsky & Coecke 2004; Abramsky 2009; Coecke 2009; Coecke & Duncan 2011]. Independently, the connection between p-adic geometry and quantum error-correcting codes is established in the holographic tensor-network literature [Heydeman, Marcolli, Saberi & Stoica 2018; Bhattacharyya, Hung, Lei & Li 2018; Gubser & Knaute 2017]. [...]
  § 2. The Branch-Depth Reading, Restated: Let $n \in \mathbb{Z}^+$ factor as $n = \prod p_i^{a_i}$. The anchor's reading: each prime $p_i$ is a *branch type*, and the exponent $a_i = v_{p_i}(n)$ is the *depth* of nesting along that branch. [...]
  § 9. Conclusion: The branch-depth reading, applied honestly to computing and quantum error correction, yields a **negative result and a sharpened open question**. The negative result: the obvious extension — reading $[[n,k,d]]$ parameters as valuations — is definitional for n and k and unavailable for d; it is, in the anchor's own terms, pure relabeling, and this paper says so rather than papering over it. The three falsifiable consequences of the reading have now been derived and each is **disconfirmed**: the valuation-based overhead bound is strictly weaker than the quantum Singleton bound (FQ2), the valuation-based complexity characterization is complexity-vacuous (FQ3), and the no-cloning re-expression yields no new checkable consequence beyond the standard categorical result (FQ4). What remains is the single precise open question — *does a non-trivial valuation invariant of stabilizer codes exist?* — where the 83% classification claim (Kodaira–Néron classifier, https://papers.qnfo.org/papers/number-theoretic-ultrametric-foundations/) is the testable hypothesis at the center. [...]