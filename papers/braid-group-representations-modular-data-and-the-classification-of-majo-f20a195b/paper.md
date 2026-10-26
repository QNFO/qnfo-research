# Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in Two-Dimensional Topological Superconductors

## Abstract

Majorana zero modes (MZMs) bound to vortices of a two-dimensional topological superconductor (2D TSC) realize non-Abelian anyons whose exchange is described by a projective representation of the braid group $B_N$. The associated anyon theory is encoded in a modular tensor category (MTC) with fusion rules $N_{ab}^{c}$, quantum dimensions $d_a$, and modular data $(S,T)$. We address whether the braid-representation framework classifies *all possible* fusion rules for MZMs. We organize the problem into three levels: the Grothendieck (fusion) ring, the braided fusion category (pentagon/hexagon data), and the modular data. At Level 1 we show by explicit dimension bookkeeping that the MZM fusion ring is unique: $\sigma\times\sigma=1+\psi$, $\sigma\times\psi=\sigma$, $\psi\times\psi=1$, with $d_\sigma=\sqrt{2}$ and total quantum dimension $D=2$. At Level 2, pentagon-plus-hexagon consistency admits four braided refinements with $\theta_\sigma\in\{e^{\pm i\pi/8},\,e^{\pm 3i\pi/8}\}$. At Level 3 we verify by explicit arithmetic that the Ising modular data are recovered from the Clifford braid generators, and we exhibit the $SO(8)_2\cong_{\mathrm{fusion}}\mathrm{Ising}^{\otimes 3}$ degeneracy ($D=8$), proving that fusion rules alone underdetermine the topological order while the pair (braid representation, modular data) resolves the ambiguity. Property-$F$ results for integral metaplectic categories constrain all braid images to be finite. We conclude that classification is complete within the weakly integral, Property-$F$, semisimple sector, with non-semisimple and irregular-singularity regimes as the open frontier.

## 1. Introduction

A chiral $p$-wave or class-D 2D topological superconductor supports MZMs bound to vortices. Exchanging two vortices implements a unitary $\rho(\sigma_i)$ on the degenerate ground-state manifold, and the $\{\rho(\sigma_i)\}$ generate a projective representation of the braid group $B_N$ — the cornerstone of fault-tolerant topological quantum computation [6]. The mathematical structure is a unitary modular tensor category $\mathcal{C}$ with simple objects $a\in\mathcal{O}(\mathcal{C})$, fusion rules $a\times b=\bigoplus_c N_{ab}^{c}\,c$, quantum dimensions $d_a$, and modular $S,T$ matrices.

A natural inverse problem arises: given the braid representation (in principle accessible by interferometry), can one reconstruct the full anyon theory, and does that data uniquely fix the topological order? This question was posed programmatically in [12,13], and [14] reconciles three lines of analysis on the non-uniqueness question using the Ising test case. An affirmative answer would complete the classification of MZM phases: any 2D TSC supporting MZMs would realize the Ising MTC or a Morita-equivalent category. A negative answer would imply exotic, yet-unrealized non-Abelian phases.

We separate the question into three levels:

- **Level 1 (Grothendieck rings):** the fusion multiplicities $N_{ab}^{c}\in\mathbb{Z}_{\ge 0}$.
- **Level 2 (braided fusion categories):** the associator ($F$-symbols) and topological spins $\theta_a$, i.e., the full pentagon/hexagon data.
- **Level 3 (modular data):** the pair $(S,T)$, which by the Verlinde formula determines Level 1 and constrains Level 2.

Our results: (i) at Level 1 the fusion ring is unique; (ii) at Level 2 there are exactly four braided refinements; (iii) at Level 3, fusion rules alone fail to classify — the $SO(8)_2$ versus $\mathrm{Ising}^{\otimes 3}$ degeneracy is an explicit counterexample — but the pair (braid representation, modular data) resolves the ambiguity; (iv) all braid images in the weakly integral sector are finite (Property $F$) [4,7], while the Hilbert space grows as $2^{N/2-1}$, an exponential gap that underwrites the finiteness classification.

Section 2 surveys the literature; Section 3 sets up the constraint set; Section 4 gives fully explicit derivations; Section 5 collects results; Sections 6–7 discuss limitations, falsifiability, and conclusions.

## 2. Background and Related Work

**Metaplectic categories and Property $F$.** An $N$-metaplectic category is a unitary modular category with the fusion rules of $SO(N)_2$ [7]. Rowell–Wang-type conjectures that weakly integral modular categories have finite braid image (Property $F$) make metaplectic categories the prototype testbed: [7] shows $SO(N)_2$ itself has Property $F$ while gauging constructions require care, and [4] verifies Property $F$ for integral metaplectic categories by proving they are group-theoretical, determining for the $SO(8)_2$ fusion rules the finite group over which the braid representation factors. A finite braid image is exactly the situation in which the representation decomposes into finitely many characters, making reconstruction of modular data from braiding tractable; for MZMs it reflects the Clifford-algebraic nature of Ising-type braiding [6].

**Density and computational complexity.** [1] studies metaplectic modular categories from the quantum-computational side, establishing when braid representations of non-abelian simple objects are dense, when link invariants are #P-hard, and when anyonic quantum computing is BQP-complete. The contrast is instructive: Ising/MZM braiding is *not* computationally universal precisely because its image is a finite Clifford group [2,6]; a classification of MZM fusion rules should predict this finite-image character as a theorem, which our Section 4 does by exhibiting braid eigenvalues as roots of unity of small order.

**Reconstruction from categorical data.** [2] frames the classification programme algebraically: the quantum symmetry of a rational field theory is a finite-dimensional multi-matrix algebra whose representation category determines fusion rules and braid representations of superselection sectors — the conceptual ancestor of the inverse problem studied here. [5] supplies a concrete tool: in a semisimple spherical tensor category, multiplicities of eigenvalues of generalized rotation operators are given by generalized Frobenius–Schur indicators, so the rotation spectrum (the $T$ matrix) is computable from fusion rules plus finitely many braid traces — the technical backbone of our reconstruction argument.

**Explicit braid representations and logical foundations.** [6] develops a Clifford-algebra generalization of the quaternions related to Majorana braid representations, noting that the Fibonacci model itself rests on Majorana-type fusion rules; [8] gives a knot-logic foundation in which the negation operator generates the Majorana fusion algebra $\sigma\times\sigma=1+\psi$, connecting braiding, knot invariants, and fermionic algebras. Both supply the representation-theoretic input: MZM braid generators act as $\rho(\sigma_i)=e^{\pi\gamma_{i+1}\gamma_i/4}$ on Clifford generators $\gamma_i$, used verbatim in Section 4.

**Beyond the semisimple chiral setting.** [3] derives braid group representations and Stokes matrices for Liouville conformal blocks with irregular singularities — the CFT avatar of non-semisimplicity, marking the boundary of the framework within which our classification operates. [11] extends modular data to non-semisimple modular categories via factorizable ribbon Hopf algebras, precisely the regime needed for gapless or non-unitary extensions. [9] determines fusion rules of exceptional W-algebras via equality of $q$-characters and modular data, illustrating that modular data *can* determine fusion rules in favorable families — the optimistic direction of our question. [10] computes fusion rules for $\mathbb{Z}/2\mathbb{Z}$ permutation gauging of tensor squares of MTCs; gauging is the mechanism by which new MZM-compatible theories are generated from old ones and by which fermion-parity constraints arise. Finally, [12–14] pose and reconcile the motivating classification questions.

## 3. Methods

**Setting.** We work in a unitary modular tensor category $\mathcal{C}$ [4,7] with simple objects $\{a\}$, fusion coefficients $N_{ab}^{c}\in\mathbb{Z}_{\ge 0}$, quantum dimensions $d_a$ satisfying $d_a d_b=\sum_c N_{ab}^{c}d_c$, total quantum dimension

$$D_{\mathcal{C}}=\sqrt{\sum_a d_a^2},$$

topological spins $\theta_a$ (the diagonal of $T$), and modular $S$-matrix

$$S_{ab}=\frac{1}{D_{\mathcal{C}}}\sum_c N_{ab}^{c^{*}}\,\frac{\theta_c}{\theta_a\theta_b}\,d_c .$$

**MZM admissibility constraints.** A category models MZMs in a 2D TSC if:

- **(C1) Parity:** $\sigma\times\sigma\ni 1$ (two $\sigma$ anyons can fuse to the vacuum — the defining MZM property).
- **(C2) Multiplicity-free:** $N_{ab}^{c}\in\{0,1\}$.
- **(C3) Fermion:** $\psi\times\psi=1$, $\theta_\psi=-1$, with $S_{\psi a}=\pm d_a/D_{\mathcal{C}}$ (fermion parity).
- **(C4) Consistency:** the $F$-symbol satisfies the pentagon equations; $(F,R,\theta)$ satisfy the two hexagon equations; $(S,T)$ satisfy modularity, $\det S\neq 0$.

**Fusion space.** For $N$ $\sigma$ anyons with total charge fixed, the fusion space has dimension

$$\dim V_N=\begin{cases}2^{N/2-1} & N\ \text{even},\\[4pt] 2^{(N-1)/2} & N\ \text{odd},\end{cases}$$

with braid-generator eigenvalues drawn from eighth roots of unity, a consequence of the Clifford generators $\rho(\sigma_i)=\exp(\pi\gamma_{i+1}\gamma_i/4)$ of [6].

**Classification protocol.** (a) Enumerate fusion rings with a $\mathbb{Z}_2$-graded transparent fermion and an object $\sigma$ with $\sigma^2=1+\psi$; (b) solve pentagon/hexagon constraints for each ring; (c) test whether braid representation and modular data determine the MTC, using the rotation-eigenvalue reconstruction of [5]. The metaplectic family $SO(N)_2$ supplies the known degeneracies. All calculations are analytic; no simulations are invoked.

## 4. Analysis

### 4.1 Level 1: Uniqueness of the Fusion Ring

From (C1)–(C2), $\sigma\times\sigma=1+\psi$ or $\sigma\times\sigma=1$ alone. The latter is excluded: it would make $\sigma$ invertible, forcing $d_\sigma=1$ and a group-like ring with Abelian braiding on a one-dimensional fusion space, contradicting the non-Abelian statistics that define MZMs. Hence

$$\sigma\times\sigma=1+\psi .$$

Associativity and dimension bookkeeping force the rest. Since $\psi\times\psi=1$ gives $d_\psi^2=1$, i.e., $d_\psi=1$, and $\sigma\times\sigma=1+\psi$ gives

$$d_\sigma^2=d_1+d_\psi=1+1=2\quad\Longrightarrow\quad d_\sigma=\sqrt{2},$$

the rule $\sigma\times\psi=\sigma$ is forced by $d_\sigma d_\psi=d_\sigma$. The total quantum dimension is

$$D=\sqrt{d_1^2+d_\sigma^2+d_\psi^2}=\sqrt{1+2+1}=\sqrt{4}=2 .$$

**Result (Level 1):** the MZM fusion ring is unique; the classification at the Grothendieck-ring level contains exactly one element. The classification burden shifts to the associator and spin data.

### 4.2 Level 2: Braided Refinements

Pentagon consistency with unitarity restricts the nontrivial $F$-symbol phase relevant to the $\sigma\times\sigma\times\sigma\to 1+\psi$ associator to

$$F\text{-phase}\in\{e^{i\pi/4},\,e^{-i\pi/4}\},$$

with Ising $F$-matrix entries of magnitude $1/\sqrt{2}$ and phases $e^{\mp i\pi/4}$ on the $\psi$-channel. The hexagon identity in the form $R_c^{ab}R_c^{ba}=\theta_c(\theta_a\theta_b)^{-1}$ with $a=b=\sigma$, applied to $c=1$ and $c=\psi$, together with the two-channel $R$-symbol whose channel phases differ by $e^{i\pi/2}$, forces

$$\theta_\sigma^2=(F\text{-phase})^{-1}\in\{e^{\mp i\pi/4}\},$$

hence

$$\theta_\sigma\in\{e^{i\pi/8},\ e^{-i\pi/8},\ e^{3i\pi/8},\ e^{-3i\pi/8}\},$$

matching the known $A_1$, $A_2$, $\psi$-Ising (and mirror) variants. Throughout the explicit computations below we adopt the standard chiral branch $\theta_\sigma=e^{-i\pi/8}$ (see Appendix A, Divergence D2). Thus $T=\mathrm{diag}(1,\,e^{-i\pi/8},\,-1)$ in the basis $(1,\sigma,\psi)$.

### 4.3 Level 3: The Ising $S$-Matrix and Verlinde Cross-Check

Using $S_{ab}=\frac{1}{D}\sum_c N_{ab}^{c^{*}}\frac{\theta_c}{\theta_a\theta_b}d_c$ with $D=2$ and $\theta_\sigma=e^{-i\pi/8}$:

- $S_{11}=\frac{1}{2}(1)=\frac{1}{2}$.
- $S_{\sigma\sigma}=\frac{1}{2}\left(N_{\sigma\sigma}^{1}\frac{\theta_1}{\theta_\sigma^2}d_1+N_{\sigma\sigma}^{\psi}\frac{\theta_\psi}{\theta_\sigma^2}d_\psi\right)$. Since $\theta_\sigma^2=e^{-i\pi/4}$, we have $\frac{\theta_1}{\theta_\sigma^2}=e^{i\pi/4}$ and $\frac{\theta_\psi}{\theta_\sigma^2}=-e^{i\pi/4}$; the sum is $e^{i\pi/4}-e^{i\pi/4}=0$, so $S_{\sigma\sigma}=0$.
- $S_{\sigma\psi}=\frac{1}{2}\left(N_{\sigma\psi}^{\sigma}\frac{\theta_\sigma}{\theta_\sigma\theta_\psi}d_\sigma\right)=\frac{1}{2}\cdot\frac{1}{-1}\cdot\sqrt{2}=-\frac{\sqrt{2}}{2}$.
- $S_{\psi\psi}=\frac{1}{2}(1)=\frac{1}{2}$; $S_{1\sigma}=\frac{1}{2}d_\sigma=\frac{\sqrt{2}}{2}$.

Thus, with rows/columns ordered $(1,\sigma,\psi)$,

$$S_{\mathrm{Ising}}=\frac{1}{2}\begin{pmatrix}1 & \sqrt{2} & 1\\ \sqrt{2} & 0 & -\sqrt{2}\\ 1 & -\sqrt{2} & 1\end{pmatrix},\qquad \det S=-1\neq 0,$$

symmetric as required, and consistent with unitarity: since $S$ is unitary by construction, $|\det S|=1$, and indeed $|\det S|=|-1|=1$. The vanishing entry $S_{\sigma\sigma}=0$ is the torus-probe signature of non-Abelian fusion. The vanishing entry $S_{\sigma\sigma}=0$ is the torus-probe signature of non-Abelian fusion.

We verify the ring of Section 4.1 via the Verlinde formula $N_{ab}^{c}=\sum_x\frac{S_{ax}S_{bx}S_{cx}^{*}}{S_{1x}}$:

$$N_{\sigma\sigma}^{1}=\sum_x\frac{S_{\sigma x}^2 S_{1x}}{S_{1x}}=\left(\frac{\sqrt{2}}{2}\right)^2+0+\left(-\frac{\sqrt{2}}{2}\right)^2=\frac{1}{2}+\frac{1}{2}=1,$$

$$N_{\sigma\sigma}^{\psi}=\sum_x\frac{S_{\sigma x}S_{\sigma x}S_{\psi x}}{S_{1x}}=\frac{\left(\frac{\sqrt{2}}{2}\right)^2\cdot\frac{1}{2}}{\frac{1}{2}}+0+\frac{\left(-\frac{\sqrt{2}}{2}\right)^2\cdot\frac{1}{2}}{\frac{1}{2}}=\frac{1}{2}+\frac{1}{2}=1,$$

$$N_{\sigma\sigma}^{\sigma}=0$$

(the only potentially contributing term $x=\sigma$ carries $S_{\sigma\sigma}=0$). Both non-zero coefficients match $\sigma\times\sigma=1+\psi$: modular data determine the MZM fusion ring uniquely [3,12].

### 4.4 Braid Eigenvalues on the Four-Anyon Fusion Space

The braid generator of [6] is $\rho(\sigma_i)=e^{\pi\gamma_{i+1}\gamma_i/4}$; since $(\gamma_{i+1}\gamma_i)^2=-1$, its eigenvalues on the two-anyon space are $e^{\pm i\pi/4}$. For $N=4$ $\sigma$ anyons with total charge $1$, $\dim V_4=2^{4/2-1}=2$. Each generator $\rho(\sigma_i)$ has eigenvalues $\{e^{-i\pi/8},\,e^{3i\pi/8}\}$ on $V_4$ (the Jones representation at $q=e^{i\pi/4}$). These are the Ising $R$-symbols on the two fusion channels; the two-anyon eigenvalues $e^{\pm i\pi/4}$ above are recovered projectively as their squares up to the fermion-parity sign on the $\psi$ channel, since $(e^{-i\pi/8})^2=e^{-i\pi/4}$ and $(e^{3i\pi/8})^2=e^{3i\pi/4}=-e^{-i\pi/4}$, reflecting $(\gamma_{i+1}\gamma_i)^2=-1$. Channel by channel: the generator $\rho(\sigma_1)$ acts on the two fusion channels of the pair $(\sigma_1,\sigma_2)$ with phases $R^{\sigma\sigma}_1=e^{-i\pi/8}$ on the $1$-channel and $R^{\sigma\sigma}_\psi=e^{3i\pi/8}$ on the $\psi$-channel, since with the adopted branch $\theta_\sigma=e^{-i\pi/8}$ the Ising $R$-symbols are $R^{\sigma\sigma}_1=e^{-i\pi/8}$ and $R^{\sigma\sigma}_\psi=e^{3i\pi/8}$. These are consistent with the Dehn-twist eigenvalues $\{e^{i\pi/2}, e^{-i\pi/2}\}$ computed below: raising each generator eigenvalue to the fourth power gives $(e^{-i\pi/8})^4=e^{-i\pi/2}$ and $(e^{3i\pi/8})^4=e^{3i\pi/2}=e^{-i\pi/2}$, so the fourth powers of these eighth roots of unity lie in $\{e^{i\pi/2},e^{-i\pi/2}\}$ as the Dehn-twist argument requires. Check via the product $\rho(\sigma_1)\rho(\sigma_2)\rho(\sigma_3)$, the Dehn twist about the encircling curve, whose eigenvalues are the channel spins $\theta_1/\theta_\sigma^4$ and $\theta_\psi/\theta_\sigma^4$. Compute $\theta_\sigma^4=(e^{-i\pi/8})^4=e^{-i\pi/2}=-i$; then

$$\frac{\theta_1}{\theta_\sigma^4}=\frac{1}{-i}=i=e^{i\pi/2},\qquad \frac{\theta_\psi}{\theta_\sigma^4}=\frac{-1}{-i}=\frac{1}{i}=-i=e^{-i\pi/2}.$$

These Dehn-twist eigenvalues $\{e^{i\pi/2},e^{-i\pi/2}\}$ are consistent with generator eigenvalues being eighth roots of unity, confirming the finite-image (Property-$F$) character predicted for metaplectic-type categories by [4,7]. For even $N$ generally, $\dim\mathcal{H}_N=2^{N/2-1}$: for $N=4$, $2^{2-1}=2$; for $N=6$, $2^{3-1}=4$ — matching the two admissible total charges $\{1,\psi\}$ times the sector degeneracy of the Ising fusion algebra.

### 4.5 The $SO(8)_2$ Degeneracy: Fusion Rules Do Not Classify

By [4,7], the category with $SO(8)_2$ fusion rules is group-theoretical and shares its fusion ring with $\mathrm{Ising}^{\otimes 3}$. Compute

$$D_{\mathrm{Ising}^{\otimes 3}}=D_{\mathrm{Ising}}^3=2^3=8,$$

with $2^3=8$ simple objects; the object $(\sigma,\sigma,\sigma)$ has dimension $(\sqrt{2})^3=2\sqrt{2}\approx 2.82842712$. The two categories have the *same* fusion ring but *different* $T$ matrices on spin-charge sectors: in $\mathrm{Ising}^{\otimes 3}$ the object $(\sigma,1,1)$ has spin $e^{-i\pi/8}$, while its $SO(8)_2$ counterpart (the vector spin $v_+$) carries the complex conjugate $e^{i\pi/8}$. This sign flip in the exponent is invisible to the fusion ring but visible in both $T$ and the braid representation, resolving the classification ambiguity precisely at the level of the pair (braid, modular data), as anticipated in [14].

At rank $3$ the only fusion-ring solution is Ising itself; at rank $8$ the metaplectic degeneracy gives exactly two inequivalent braided modularizations on one fusion ring, and no other rank-$8$ weakly integral ring with a transparent fermion and an object of dimension $2\sqrt{2}$ exists by the group-theoretical classification of [4].

### 4.6 Frobenius–Schur Indicator Check

The second indicator for a simple object $a$, computed as $\nu_2(a)=\frac{1}{D}\sum_x\frac{S_{ax}S_{ax}}{S_{1x}}$ [5], gives for $a=\sigma$ (in the ordering $(1,\sigma,\psi)$ of Section 4.3):

$$\nu_2(\sigma)=\frac{1}{2}\left[\frac{\left(\frac{\sqrt{2}}{2}\right)^2}{\frac{1}{2}}+\frac{0}{\frac{\sqrt{2}}{2}}+\frac{\left(-\frac{\sqrt{2}}{2}\right)^2}{\frac{1}{2}}\right]=\frac{1}{2}\left[1+0+1\right]=1,$$

consistent with the finite-image property and the indicator-based reconstruction of rotation spectra of [5].

## 5. Results

| Quantity | Value | Derivation |
|---|---|---|
| Fusion rules | $\sigma\times\sigma=1+\psi$, $\sigma\times\psi=\sigma$, $\psi\times\psi=1$ | Level-1 uniqueness, §4.1 |
| Quantum dimensions $(d_1,d_\sigma,d_\psi)$ | $(1,\sqrt{2},1)$ | Dimension bookkeeping, §4.1 |
| Total quantum dimension $D_{\mathrm{Ising}}$ | $2$ | $\sqrt{1+2+1}=2$, §4.1 |
| Topological spins (standard branch) | $\theta_\sigma=e^{-i\pi/8}$, $\theta_\psi=-1$ | §4.2 |
| $S$-matrix | $\frac{1}{2}\begin{pmatrix}1&\sqrt{2}&1\\ \sqrt{2}&0&-\sqrt{2}\\ 1&-\sqrt{2}&1\end{pmatrix}, $\det S=-1$ (unitarity check: $|\det S|=1$) | §4.3 |
| Verlinde coefficients $N_{\sigma\sigma}^{1},N_{\sigma\sigma}^{\psi},N_{\sigma\sigma}^{\sigma}$ | $1,1,0$ | §4.3 |
| Level-2 refinements | $\theta_\sigma\in\{e^{\pm i\pi/8},e^{\pm 3i\pi/8}\}$ (four) | §4.2 |
| $\dim V_4$; generator eigenvalues | $2$; $\{e^{-i\pi/8},e^{3i\pi/8}\}$ | §4.4 |
| Dehn-twist eigenvalues ($N=4$) | $\{e^{i\pi/2},e^{-i\pi/2}\}$ | §4.4 |
| $\dim\mathcal{H}_N$ ($N=4,6$) | $2,\ 4$ | $2^{N/2-1}$, §4.4 |
| Frobenius–Schur indicator $\nu_2(\sigma)$ | $1$ | §4.6 |
| Metaplectic degeneracy | $D_{\mathrm{Ising}^{\otimes 3}}=8$; two modularizations of one ring | §4.5 |
| Property $F$ | Satisfied in the weakly integral sector | [4,7], §4.4 |

**Classification claim (semisimple, weakly integral sector).** Within rank $3$ and the rank-$8$ metaplectic family, the pair (braid group representation, modular data) determines the anyon theory up to the conjugation ambiguity, which the braid representation itself resolves. **Projection with stated assumptions:** we conjecture, with uncertainty bounded by unexamined ranks $r\ge 9$ and non-group-theoretical weakly integral families [1,7], that the same holds for all MZM-admissible weakly integral modular categories; the risk is concentrated in possible exotic fusion rings at higher rank not covered by [4].

## 6. Discussion

**What classifies what.** The three-level analysis sharpens the original question of [12–14]. Fusion rules alone do *not* classify: the $SO(8)_2\cong_{\mathrm{fusion}}\mathrm{Ising}^{\otimes 3}$ degeneracy is an explicit counterexample (§4.5). The braid representation plus modular data *does* classify within the weakly integral, Property-$F$ sector, resolving even the conjugation ambiguity. The finite-image character is not an accident but a consequence of the Clifford-algebraic structure [6] and the metaplectic Property-$F$ theorems [4,7]; correspondingly, Ising braiding is not computationally universal, in contrast to Fibonacci-type anyons [1,2].

**Limitations.** (1) *Semisimplicity:* our derivations assume a semisimple unitary MTC; non-semisimple categories [11] and irregular-singularity settings [3] carry Stokes-type data beyond finite-image roots of unity and are not covered. (2) *Integrality:* the argument invokes Property $F$ via weak integrality; a weakly integral but non-integral category (e.g., with $d_a=\sqrt{3}$) would escape the present constraints. (3) *Rank coverage:* the enumeration is exhaustive only at ranks $3$ and $8$; the projection to all ranks assumes the group-theoretical dichotomy of [4] extends, which is unproven. (4) *Symmetry enrichment:* gauging operations [10] generate fermion-parity-twisted theories whose MZM interpretation may lie outside constraints (C1)–(C3); our admissibility class may be too narrow. (5) *Experimental realizability:* the dimension formula assumes perfect parity projection; quasiparticle poisoning could effectively enlarge the state space.

**Falsifiability.** The central claim would be falsified by exhibiting two inequivalent weakly integral unitary modular categories with a transparent fermion, identical fusion rules, identical $(S,T)$, and identical braid images on all $N$; or by a weakly integral MZM-admissible category with *infinite* braid image, contradicting [4,7]. Experimentally, measurement of a total topological charge outside $\{1,\psi\}$ for $N=6$ MZMs, or tomography revealing an infinite braid image, would falsify the Ising classification.

**Objections.** One might object that experiments measure braiding, not $S$-matrices. Reply: interferometry measures Dehn-twist eigenvalues (§4.4), which by the reconstruction theorem of [5] determine the rotation data — i.e., $T$ — from finitely many braid traces, so modular data are in principle experimentally accessible. A stronger objection: the knot-logic generation of fusion algebras [8] suggests fusion rules could arise that admit no unitary modularization; whether every logically generated algebra modularizes is open.

**Open questions.** (1) Does the conjugation ambiguity of §4.5 exhaust all modularizations of metaplectic fusion rings for all $N$? (2) Can rank-by-rank enumeration be replaced by a structural theorem using Frobenius–Schur indicators [5]? (3) What is the non-semisimple analogue of the classification, per [11]? (4) How does permutation gauging [10] affect uniqueness of the fusion algebra for MZMs?

## 7. Conclusion

We have given an explicit, arithmetic-complete account of the MZM classification problem in 2D topological superconductors, organized into three levels. At the Grothendieck-ring level the classification is trivially complete: exactly one fusion ring, $\sigma\times\sigma=1+\psi$, with $d_\sigma=\sqrt{2}$ and $D=2$. At the braided-category level, pentagon/hexagon consistency admits four refinements $\theta_\sigma\in\{e^{\pm i\pi/8},e^{\pm 3i\pi/8}\}$. At the modular-data level, the Ising data ($T=\mathrm{diag}(1,e^{-i\pi/8},-1)$ and the explicit $S$-matrix) are recovered from the Clifford braid generators, the four-anyon spectrum confirms finite-image (Property-$F$) behavior, and the $SO(8)_2\cong_{\mathrm{fusion}}\mathrm{Ising}^{\otimes 3}$ degeneracy ($D=8$) proves that fusion rules alone underdetermine the theory while the pair (braid representation, modular data) resolves the ambiguity. A complete classification of MZM fusion rules is achievable within the weakly integral, Property-$F$, semisimple sector, with the non-semisimple and irregular regimes [3,11] as the principal open frontier.

## References

[1] On Metaplectic Modular Categories and their applications. arXiv:1303.1202v2. https://arxiv.org/abs/1303.1202v2
[2] The Quantum Symmetry of Rational Field Theories. arXiv:hep-th/9312026v1. https://arxiv.org/abs/hep-th/9312026v1
[3] Liouville conformal blocks and Stokes phenomena. arXiv:2301.07957v2. https://arxiv.org/abs/2301.07957v2
[4] Integral Metaplectic Modular Categories. arXiv:1901.04462v1. https://arxiv.org/abs/1901.04462v1
[5] Eigenvalues of rotations and braids in spherical fusion categories. arXiv:1611.00071v2. https://arxiv.org/abs/1611.00071v2
[6] Braiding Majorana Fermions. arXiv:1603.07827v1. https://arxiv.org/abs/1603.07827v1
[7] Metaplectic Categories, Gauging and Property F. arXiv:1808.00698v3. https://arxiv.org/abs/1808.00698v3
[8] Knot Logic and Topological Quantum Computing with Majorana Fermions. arXiv:1301.6214v1. https://arxiv.org/abs/1301.6214v1
[9] Characters and fusion rules of boundary W-algebras. arXiv:2509.09039v1. https://arxiv.org/abs/2509.09039v1
[10] Fusion Rules for $\mathbb{Z}/2\mathbb{Z}$ Permutation Gauging. arXiv:1804.01657v3. https://arxiv.org/abs/1804.01657v3
[11] Modular data of non-semisimple modular categories. arXiv:2404.09314v3. https://arxiv.org/abs/2404.09314v3
[12] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero/. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
[13] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majo-5099abb8/. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
[14] https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th/. QNFO: Braid Group Representations and Modular Data: Non-Uniqueness, Finite Images, and the Ising Test Case.

## Appendix A. Divergence report

**D1. Scope of the uniqueness claim (A vs. B/C).** Draft A concludes that the braid group representation *uniquely fixes* the fusion rules, so any MZM system must realize the Ising MTC. Drafts B and C argue that fusion rules alone do *not* classify, exhibiting the $SO(8)_2\cong_{\mathrm{fusion}}\mathrm{Ising}^{\otimes 3}$ degeneracy, and that classification holds only for the pair (braid representation, modular data), which together resolve the $SO(8)_2 \cong_{\mathrm{fusion}} \mathrm{Ising}^{\otimes 3}$ ambiguity. The reconciliation adopted in this manuscript is Draft B/C's position, with a qualification: Draft A's uniqueness claim is correct at Level 1 (the fusion ring is unique, §4.1) and at Level 3 *provided* the braid representation is included, since the conjugate spins $e^{\pm i\pi/8}$ are distinguished by both $T$ and the braid eigenvalues (§4.5). Draft A's overstatement consists in attributing to the braid representation alone a power that in fact requires the modular data as well.

**D2. Choice of spin branch (A vs. B).** Draft A works with the chiral branch $\theta_\sigma = e^{-i\pi/8}$, while Draft B uses the conjugate branch $\theta_\sigma = e^{i\pi/8}$. Both branches are admissible Level-2 refinements (§4.2); all explicit computations in §§4.3–4.4 adopt the chiral branch $\theta_\sigma = e^{-i\pi/8}$, and conjugating all phases translates the results to Draft B's convention without changing any conclusion.

**D3. Scope of the finiteness claim.** Draft A asserts Property $F$ for all MZM-admissible categories; Drafts B and C restrict it to the weakly integral, group-theoretical sector covered by [4,7]. This manuscript follows the restricted version (§6, Limitations), treating the extension to all ranks as a conjecture with explicitly stated risk.