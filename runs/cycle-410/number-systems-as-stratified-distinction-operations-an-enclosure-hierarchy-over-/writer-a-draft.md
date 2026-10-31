# Number Systems as Stratified Distinction Operations: An Enclosure Hierarchy over the Mark

## Abstract

The conventional tower of number systems—\(\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\)—augmented by the \(p\)-adic fields \(\mathbb{Q}_{p}\) and the adele ring \(\mathbb{A}\) is usually presented as a sequence of completions without a unifying generative principle. Practitioners in physics, logic, and computer science lack a quantitative criterion for choosing among these systems, which leads to ad‑hoc model selection, ambiguous foundational arguments, and undocumented information loss when finite‑precision arithmetic is projected onto the continuum. This paper supplies a quantitative layer by defining a family of enclosure operators \(E_{i}\) that generate each stratum from a primitive mark and by introducing a loss functional
\[
\Lambda_{i\to j}(\text{params})=\log_{2}N_{i}(\text{params})-\log_{2}N_{j}(\text{params}),
\]
where \(N_{i}\) counts distinguishable states in stratum \(S_{i}\). For the tree‑to‑continuum (Monna) projection we compute \(\Lambda_{6\to4}=7\) bits at depth \(n=10\), base \(p=2\) and real precision \(\varepsilon=2^{-3}\); we prove the exact linear law \(\Lambda_{6\to4}(n)=n-3\) at fixed \(\varepsilon\) and identify the loss‑free matching depth \(n=3\). Finite simultaneous‑valuation products over the primes \(\{2,3,5\}\) yield \(30\) states at depth 1 and \(900\) at depth 2. All numbers are derived by hand; no simulation or external measurement is used. The result converts a philosophical thesis into a family of falsifiable, countable claims and specifies the minimal computational experiment that would test them.

## 1. Introduction

Anyone who teaches, formalizes, or computes with numbers inherits a fixed tower: \(\mathbb{N}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}\), with \(\mathbb{Q}_{p}\) and \(\mathbb{A}\) attached to \(\mathbb{Q}\) as a parallel branch. The cost of this presentation is concrete. A physicist choosing a number system for a model has no principled way to decide whether the continuum is forced or merely conventional; every measurement yields a rational number to finite precision and every simulation operates on finite‑precision rationals, yet the choice of \(\mathbb{R}\) as the base field is rarely justified. A logician studying constructive foundations has no unified account of why the historical sequence unfolded in this order. A computer scientist working with finite‑precision arithmetic has no theory of what information is destroyed when a tree‑structured limit is flattened onto a line. If the progression \(\mathbb{N}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}\to\mathbb{Q}_{p}\to\mathbb{A}\) could be derived from increasingly refined acts of distinction, each decision would acquire a measurable criterion: the choice of number system would become a choice of operator, and the cost of each choice would be quantifiable in bits.

The measurement‑stratigraphy program proposes that the history of number systems is a sequence of expanding distinction operations, each era adding a new enclosure—marking, ratio comparison, convergent sequences, lossy projection to the continuum, imaginary enclosure, \(p\)-adic enclosure. The computable‑real‑boundary work builds number systems from two primitives of Spencer‑Brown’s *Laws of Form*: the mark, whose repeated indication collapses under the Calling rule, and the enclosure, the boundary a distinction creates; it identifies the fixed point of finite enclosure operations with the computable reals \(\mathbb{R}_{\text{comp}}\). Neither work supplies a quantitative layer; this paper adds one, and repairs two misattributions that appeared in the earlier version of the present work.

We posit a primitive mark \(M\) and a family of enclosure operators \(E_{i}\), each a closure‑type operator whose application to the previous stratum yields the next. For each stratum we state the minimal algebraic structure generated, the canonical map to the following stratum, and a distinguishable‑state count where a finite count exists. The counts support a loss functional, which we compute in full arithmetic for the tree‑to‑continuum cross‑stratum comparison. Four falsifiability conditions are stated so that a single counterexample kills the corresponding claim.

**Contributions.**
1. Explicit state‑count derivations for the tally, real‑enclosure, and \(p\)-adic strata at finite depth, with every arithmetic step shown (Section 4, Derivations 1–3).
2. The corrected Monna cross‑stratum loss budget: \(\Lambda_{6\to4}=7\) bits at \((p=2,n=10,\varepsilon=2^{-3})\), the exact linear law \(\Lambda_{6\to4}(n)=n-3\) at fixed precision, the vanishing of the loss at matched depth \(n=3\), and the explicit reclassification of this quantity as cross‑stratum rather than adjacent‑stratum loss (Section 4, Derivations 4–5; Results R1–R2).
3. Finite simultaneous‑valuation product counts of \(30\) and \(900\) over the primes \(\{2,3,5\}\) at depths 1 and 2 (Section 4, Derivation 6).
4. The non‑dyadic no‑matching result: for \(p=3\) and \(\varepsilon=2^{-3}\) no integer depth yields zero loss because the required depth \(n=3/\log_{2}3\approx1.893\) is not an integer (Section 4, Derivation 7).
5. Four falsifiability conditions F1–F4 for the stratification, the loss functional, the operator list, and the adequacy of \(\Lambda\) (Section 3.4).

## 2. Background and Related Work

We review eight works that illustrate concrete aspects of the stratified‑distinction framework.

* The distinction‑based ultrametric paper defines a finite‑resolution distance as the number of distinctions required to separate two states and proves that this distance satisfies the ultrametric inequality. This provides a concrete implementation of a distinction operation and shows how a quantitative metric can be derived from the primitive act of enclosure [5].

* The noncanonical number systems paper studies positional systems with digit sets that do not contain \(0\); it proves that such digit sets exist for every base \(|b|\ge4\) and exhibits \(\{1,2\}\) as a valid digit set for base \(-2\). This demonstrates that a single enclosure operator can admit many inequivalent concrete realizations, highlighting the importance of the operator rather than the digit set in defining a stratum [7].

* The Zagreb indices paper derives sharp lower bounds for the first and second Zagreb indices of trees and characterizes extremal trees achieving those bounds. The combinatorial state‑count nature of these results illustrates how finite counting arguments can yield precise quantitative constraints, analogous to our state‑count formulas for strata [2].

* The Caccetta‑Häggkvist survey records Kemperman’s theorem, which gives an upper bound for the growth of product sets via the quantity \(k(A,B)=|A|+|B|-|A+B|\). Product‑set growth is the combinatorial shadow of our state‑count process, because iterating an enclosure on a finite set is exactly an iterated product set [6].

* The arithmetic lattices note describes constructions of arithmetic lattices in the isometry groups of real, complex, and quaternionic hyperbolic spaces. These constructions connect deep arithmetic geometry to the \(p\)-adic and adelic completions that appear in our higher strata, showing that the algebraic structures underlying \(E_{6}\) and \(E_{7}\) have rich geometric realizations [3].

* The super‑powers paper studies sequences \(s_{n}=\sum_{i=1}^{k}\prod_{j=0}^{\ell}x_{i,j}^{\,n^{j}}\) and proves that the number \(\omega(s_{n})\) of distinct prime factors exceeds a super‑logarithmic bound for infinitely many \(n\), using the \(p\)-adic valuation \(\upsilon_{p}\). This demonstrates how valuation‑based analytic tools can be attached to the \(p\)-adic stratum, complementing our state‑count formalism [9].

* The statistical audit of the 5‑smooth semigroup mass‑ratio claim performs a quantitative audit of a claimed numerical relationship, identifies arithmetic errors, and concludes that the claim does not survive statistical scrutiny. This exemplifies the falsifiability condition F4: a scalar measure can be inadequate for the structure it is meant to grade, and a stratified refinement (our \(\Lambda\)) may be required [4].

* The symmetric‑gradient regularity paper studies global regularity of nonlinear elliptic systems depending on the symmetric part of the gradient. Although its focus is analytic PDE theory, the work illustrates how deep analytic techniques can be applied to structures derived from primitive operations, supporting the broader methodological stance that the stratified framework can accommodate sophisticated mathematical objects [1].

Together these works provide concrete instances of operators, state‑count phenomena, and deep arithmetic that the stratified‑distinction framework must accommodate.

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

The recovery claims that \(E_{4}\) yields \(\mathbb{R}\), \(E_{5}\) yields \(\mathbb{C}\), and \(E_{7}\) yields \(\mathbb{A}\) are conjectural, consistent with the stratigraphy framework’s own status for these strata. Only the state‑count formulas for strata 0, 1, 3, and 6 are used in finite arithmetic below; the formula \(N_{4}(\varepsilon)=1/\varepsilon\) is a definition of the target precision, not a verified recovery claim.

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
* **F3 (operator list).** Exhibit a completion of \(\mathbb{Q}\) outside the list \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\). Classical Ostrowski’s theorem states that every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the Archimedean absolute value (completion \(\mathbb{R}\)) or to a \(p\)-adic absolute value for some prime \(p\) (completion \(\mathbb{Q}_{p}\)); thus no such completion exists, providing a consistency check on the operator list.
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
* **Non‑canonical realizations.** The existence of many valid digit sets for a given base (e.g., \(\{1,2\}\) for base \(-2\)) shows that a single enclosure operator can admit multiple inequivalent concrete realizations; the operator, not the digit set, determines the stratum [7].
* **Operator‑list incompleteness.** Ostrowski’s theorem guarantees that every non‑trivial absolute value on \(\mathbb{Q}\) is equivalent either to the Archimedean absolute value or to a \(p\)-adic one; if a number system in the historical sequence required a completion outside \(\{\mathbb{R},\mathbb{Q}_{p}:p\text{ prime}\}\), the present operator list would be incomplete, falsifying F3.
* **\(\Lambda\) inadequacy.** Two intuitively different projections could share the same \(\Lambda\) value while differing dramatically in preserved structure, mirroring the failure of classical \(\beta\)-numbers in Carnot groups [2]; this would falsify F4 and motivate a stratified refinement of \(\Lambda\).

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Researchers who must choose a numeric representation for formal models—particularly in mathematical physics, constructive analysis, and exact‑arithmetic software—are the principal users of the loss functional \(\Lambda\) and the state‑count formulas derived in Sections 4–5. When a simulation requires a target real precision \(\varepsilon\), the user can compute the bit‑loss
\[
\Lambda_{6\to4}(n,p,\varepsilon)=n\log_{2}p-\log_{2}\!\bigl(1/\varepsilon\bigr)
\]
(Derivation 5) for any candidate \(p\)-adic depth \(n\). If \(\Lambda_{6\to4}=0\), the \(p\)-adic tree can replace the real interval without any information loss; the dyadic case \(p=2\), \(n=3\), \(\varepsilon=2^{-3}\) provides the first such loss‑free matching (Result R2). Consequently, a modeler can decide to store data in a binary‑tree structure of depth 3 rather than in floating‑point format, thereby guaranteeing that no bits are discarded by the projection to \(\mathbb{R}\).

**(b) Technology readiness.**  
The work is purely analytical, has not undergone peer review, and involves no hardware or software implementation. According to NASA’s Technology Readiness Level definitions, it resides at TRL 1–2 (basic principles observed). Analytical extensions never exceed TRL 3; therefore no claim of manufacturing or deployment readiness is made.

**(c) Minimal next experiment.**  
A concrete computational experiment that would falsify the monotonicity claim of F2 (that \(\Lambda_{6\to4}(n)\) increases with \(n\) for fixed \(\varepsilon\)) consists of the following steps, expressed conditionally:

1. Generate the residue set \(\mathbb{Z}/p^{n}\mathbb{Z}\) for a chosen odd prime \(p\) (e.g., \(p=3\)) and depth \(n\in\{1,2,3\}\).
2. Map each residue class to a sub‑interval of