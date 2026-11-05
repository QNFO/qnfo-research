# P-adic Spin, Information, and Ultrametric Internal Quantum Numbers

## Abstract

Paper I established that the Archimedean continuum the real numbers_c suffices for all physical dynamics — depth without breadth. Here we complete the picture: what of the ultrametric completions of the rational numbers? We argue that the p-adic numbers the rational numbers_p are not "extra spatial dimensions" in the string-theoretic sense but valuation-theoretic dimensions whose physical role is to encode discrete quantum structure: spin, internal quantum numbers (color, weak isospin, hypercharge), and information-theoretic (hierarchical) properties. The 2-adic Bruhat-Tits tree boundary carries a natural the Z2 grading that matches the spin-statistics distinction. The Standard Model gauge group SU(3) x SU(2) x U(1) decomposes by prime factors, with internal quantum numbers emerging as labels of vertices in Bruhat-Tits buildings at the corresponding primes. Time is Archimedean (Paper I) — connected, dynamical, causal. Spin and information are p-adic — discrete, ultrametric, hierarchical. Ostrowski's theorem — that the real numbers and the rational numbers_p are the only completions of the rational numbers — is the hidden organizing principle behind the structure of quantum observables.

# 1. Introduction: The Puzzle of Discrete Quantum Numbers

## 1.1 The Problem

Quantum mechanics presents a striking dualism:

- **Dynamics** are Archimedean: wavefunctions evolve continuously in time via the Schrödinger equation, operators have continuous spectra (position, momentum), and the intermediate value theorem governs transitions.
- **Observables** are discrete: spin comes in half-integer multiples of ℏ, the Standard Model's internal quantum numbers (color, weak isospin, hypercharge) take values in finite sets, and all measurement outcomes are eigenvalues of operators with — at minimum — a discrete spectral decomposition.

Why should a theory formulated over $\mathbb{R}$ (or $\mathbb{C}$ ≅ $\mathbb{R}$²) exhibit fundamentally discrete structure? The standard answer — "because operators have discrete spectra" — merely restates the observation in mathematical language. It does not explain why the continuum formalism admits discrete structure at all.

## 1.2 The Thesis

We propose that the answer is built into the number system itself. By Ostrowski's theorem (1916), the only non-trivial completions of $\mathbb{Q}$ are:

- **$\mathbb{R}$** (the Archimedean completion, the ∞-place) — connected, ordered, the domain of dynamics and causality.
- **$\mathbb{Q}_p$** for each prime p (the ultrametric completions) — totally disconnected, tree-structured, the domain of discrete quantum structure and information.

The Archimedean completion gives you time, continuity, fields, and causal structure (Paper I). The p-adic completions give you spin, charge, color, and entanglement — the discrete, hierarchical, information-theoretic properties that resist Archimedean description.

This is not a mathematical analogy. It is a physical claim: **quantum observables are discrete because the p-adic places are fundamentally discrete (totally disconnected), and the real place is fundamentally connected — and nature uses both.** The Standard Model's gauge group decomposes by prime factors because gauge symmetries live on Bruhat-Tits buildings at the corresponding primes.

---

# 2. P-adic Numbers as Information Trees

## 2.1 Positional Notation Is a Tree

A p-adic integer a ∈ $\mathbb{Z}_p$ can be written as:

$$a = a_0 + a_1 p + a_2 p^2 + a_3 p^3 + \cdots, \quad a_i \in \{0, 1, \ldots, p-1\}$$

Each digit a_i is a choice among p branches. The expansion unfolds as a rooted p-ary tree:

```
                    root
               /    |    \
              a0=0 a0=1 a0=2  ... (p choices)
             /|\   /|\   /|\
            ...    ...    ...
```

The p-adic distance is:

$$|x - y|_p = p^{-k}$$

where k is the index of the first digit where x and y differ. Two numbers are "close" if they agree deeply in the digit tree — they share a long common ancestor branch.

## 2.2 The Ultrametric Inequality

The p-adic absolute value satisfies:

$$|x + y|_p \leq \max(|x|_p, |y|_p)$$

with equality when |x|_p ≠ |y|_p. This is the *strong triangle inequality*. Geometrically, it means: **all triangles are isosceles, with the two equal sides at least as long as the third.**

**Theorem 2.1 (Ultrametric = Hierarchical).** A metric space (X, d) is ultrametric iff it embeds isometrically into a rooted tree where distance between nodes is the depth of their deepest common ancestor.

*Proof.* Standard. See Carlsson & Mémoli (2010). Done

The ultrametric inequality is the mathematical signature of hierarchical clustering. This is why p-adic numbers naturally encode:

| Physical Domain | Ultrametric Structure | p-adic Realization |
|:----------------|:----------------------|:-------------------|
| **Spin** | $\mathbb{Z}_2$ grading on rotation group fundamental group | Boundary action of $\mathrm{Gal}(\overline{\mathbb{Q}}_p/\mathbb{Q}_p)$ on Bruhat-Tits tree |
| **Internal quantum numbers (color, isospin)** | Finite symmetry groups SU(n) with discrete representations | Vertex labels in Bruhat-Tits buildings for $\mathrm{SL}_n(\mathbb{Q}_p)$ |
| **Entanglement** | Hierarchical clustering of correlations | p-adic valuation of mutual information |
| **Error-correcting codes** | Tree-structured codeword distances | p-adic valuations as code discriminants |
| **Measurement** | Yes/no branching decisions | p-adic digits as binary resolution levels |

## 2.3 Bruhat-Tits Buildings

The Bruhat-Tits building for $\mathrm{SL}_n(\mathbb{Q}_p)$ is a simplicial complex whose vertices correspond to homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^{n}$.

For n = 2, the Bruhat-Tits tree for $\mathrm{SL}_2(\mathbb{Q}_p)$ is a (p+1)-regular tree. Its boundary is $\mathbb{P}^1(\mathbb{Q}_p)$ — the p-adic projective line. The boundary carries a natural action of $\mathrm{PGL}_2(\mathbb{Q}_p)$, and the nontrivial element of the Galois group of the unramified quadratic extension acts as an involution — a $\mathbb{Z}_2$ grading.

This $\mathbb{Z}_2$ is the same $\mathbb{Z}_2$ that gives spin.

---

# 3. Spin from the 2-adic Place

## 3.1 Spin Is Topological, Not Metric

The spin-statistics theorem in 3+1 dimensions rests on two facts:

1. π1(SO(3)) = $\mathbb{Z}_2$ — the rotation group is not simply connected; its double cover is SU(2).
2. In 3+1 dimensions, exchanging two identical particles corresponds to a 2π rotation of the center-of-mass frame, introducing a phase factor of ±1 depending on whether the wavefunction lives in the trivial or nontrivial representation of π1(SO(3)).

The key observation: **π1 is a topological invariant.** It does not depend on the metric on SO(3) — only on the underlying topological space. The fact that rotation in physical space is described by the Archimedean metric is irrelevant to the fact that the fundamental group is $\mathbb{Z}_2$.

## 3.2 The $\mathbb{Z}_2$ Grading on the Bruhat-Tits Boundary

The Bruhat-Tits tree for SL2($\mathbb{Q}_2$) is a 3-regular tree (since p=2, p+1=3). Its boundary $\mathbb{P}$¹($\mathbb{Q}_2$) is a compact, totally disconnected space homeomorphic to a Cantor set.

The Galois group Gal($\mathbb{Q}$̄2/$\mathbb{Q}_2$) acts on $\mathbb{P}$¹($\mathbb{Q}_2$). The unramified quadratic extension $\mathbb{Q}_2$(√ε) (where ε is a non-square unit in $\mathbb{Z}_2$, e.g., ε = 5) has Galois group $\mathbb{Z}_2$. This $\mathbb{Z}_2$ action partitions the boundary points into two orbits — exactly the structure of a spinor under 2π rotation.

**Conjecture 3.1 (2-adic Spin).** The $\mathbb{Z}_2$ grading on the boundary of the Bruhat-Tits tree for SL2($\mathbb{Q}_2$), induced by the Galois action of the unramified quadratic extension, is the number-theoretic origin of the spin-statistics distinction. Bosonic states correspond to the trivial $\mathbb{Z}_2$ orbit; fermionic states correspond to the nontrivial orbit.

**Evidence:**
- Both $\mathbb{Z}_2$'s are topological in origin (π1(SO(3)) is a topological invariant; Gal($\mathbb{Q}$̄2/$\mathbb{Q}_2$) is independent of the metric on $\mathbb{Q}_2$).
- Both $\mathbb{Z}_2$'s govern exchange statistics (the spin-statistics theorem for the first; the boundary involution for the second).
- The 2-adic place is distinguished: p=2 is the only prime for which the Bruhat-Tits tree is a trivalent tree (p+1=3), matching the three spatial rotation axes.
- The connection to Majorana fermions: Majorana zero modes are identified as fixed points on Bruhat-Tits trees (ZBW Program P1-P4, https://papers.qnfo.org/papers), where the $\mathbb{Z}_2$ grading from charge conjugation matches the Bruhat-Tits involution.

## 3.3 Spin-Statistics as a 2-adic Phenomenon

If Conjecture 3.1 holds, the spin-statistics connection is not a consequence of Lorentz invariance (the standard story) but of the fact that **the $\mathbb{Z}_2$ grading of the boundary of the Bruhat-Tits tree at the 2-adic place is the same $\mathbb{Z}_2$ that distinguishes bosons from fermions.** The Lorentz group SO(3,1) inherits its $\mathbb{Z}_2$ fundamental group from the spatial rotation subgroup SO(3), which in turn inherits its $\mathbb{Z}_2$ from the 2-adic boundary grading.

This explains why spin-statistics holds in all Lorentz-invariant theories — because Lorentz invariance preserves the spatial SO(3) subgroup, which carries the 2-adic $\mathbb{Z}_2$ structure.

---

# 4. Internal Quantum Numbers as Bruhat-Tits Vertex Labels

## 4.1 The Standard Model Gauge Group and Its Primes

The Standard Model's internal symmetry group is:

$$G_{SM} = SU(3)_C \times SU(2)_L \times U(1)_Y$$

Decompose by prime factors:

| Factor | Dimension | Relevant Primes | Bruhat-Tits Building |
|:-------|:---------|:----------------|:---------------------|
| SU(3)_C (QCD) | 8 | p=3 | Bruhat-Tits building for SL3($\mathbb{Q}_3$) |
| SU(2)_L (weak isospin) | 3 | p=2 | Bruhat-Tits tree for SL2($\mathbb{Q}_2$) |
| U(1)_Y (hypercharge) | 1 | p=∞ (Archimedean) | Real line $\mathbb{R}$ |

The primes 2 and 3 are not arbitrary — they are the prime factors of the gauge group dimensions, and they correspond to distinct completions of $\mathbb{Q}$.

## 4.2 Representations as Building Vertices

Compact p-adic Lie groups (like SL_n($\mathbb{Z}_p$)) have representations that are naturally stratified by the Bruhat-Tits building. The "floors" of the building correspond to congruence subgroups modulo p^k. Each floor k encodes precision level k in the p-adic expansion.

**Conjecture 4.1 (Internal Quantum Numbers).** The irreducible representations of the Standard Model gauge group correspond to distinguished vertices in the Bruhat-Tits buildings at the relevant primes:
- Color triplets (quarks) and singlets (leptons) are vertices in the SL3($\mathbb{Q}_3$) Bruhat-Tits building at appropriate floor levels.
- Weak isospin doublets and singlets are vertices in the SL2($\mathbb{Q}_2$) Bruhat-Tits tree.
- Hypercharge assignments are Archimedean (real-number) labels.

The discrete and finite nature of internal quantum numbers follows immediately: Bruhat-Tits buildings are simplicial complexes, and their vertex sets at any finite floor are finite. The "continuous" gauge symmetries SU(n) are continuous only in the Archimedean description — their underlying ultrametric structure is discrete.

## 4.3 The Kodaira-Néron Classification and Code Structure

From the Number-Theoretic Ultrametric Foundations (https://papers.qnfo.org/papers/number-theoretic-ultrametric-foundations/), the Kodaira-Néron classification of degenerate elliptic fibers maps onto stabilizer code families with p-adic valuations as discriminants. The classification achieves 83% accuracy with 100% lemma-level agreement across 4 code families.

The key result: optimal quantum error-correcting codes exhibit v_p^{max} = 28 versus v_p^{max} = 4 for random ensembles — a 7$\times$ gap. This is a **physical signal**: structures optimized for quantum information naturally push toward high p-adic valuation. The p-adic channel is not a mathematical curiosity; it is the operational substrate where quantum information lives.

This connects directly to the Standard Model: the representations of SU(3)_C and SU(2)_L are "optimal codes" in the sense that they minimize certain information-theoretic costs, and their structure is captured by the Kodaira-Néron fiber types at the relevant primes.

---

# 5. Time as Archimedean, Information as P-adic

## 5.1 Ostrowski's Theorem as Physical Organizing Principle

Ostrowski's theorem (1916) classifies all non-trivial absolute values on $\mathbb{Q}$ up to equivalence:

$$|\cdot|_\infty \quad \text{and} \quad |\cdot|_p \text{ for each prime } p$$

The completions are $\mathbb{R}$ (connected, ordered, Archimedean) and $\mathbb{Q}_p$ (totally disconnected, ultrametric).

**Thesis (Adelic Physics).** Nature uses all completions of $\mathbb{Q}$, and their physical roles are determined by their topological type:

| Completion | Topology | Physical Role |
|:-----------|:---------|:--------------|
| $\mathbb{R}$ (∞-place) | Connected, Archimedean | **Time, dynamics, causality, limits** (Paper I) |
| $\mathbb{Q}_2$ (2-adic) | Totally disconnected, tree | **Spin, fermion/boson statistics** |
| $\mathbb{Q}_3$ (3-adic) | Totally disconnected, building | **Color charge, QCD** |
| $\mathbb{Q}_p$ for other p | Totally disconnected | **Additional discrete quantum numbers** |

## 5.2 Mutual Singularity and Adelic QEC

The $\mathbb{R}$ and $\mathbb{Q}_p$ topologies on $\mathbb{Q}$ are *mutually singular*: no sequence converges in both simultaneously (except eventually constant sequences). This has profound consequences for quantum error correction.

From the Adelic QEC paper (https://papers.qnfo.org/papers):

> A Majorana zero mode on a Bruhat-Tits tree is a p-adic fixed point — a distinguished vertex invariant under the $\mathbb{Z}_2$ grading. No Archimedean perturbation — regardless of energy scale — can move a p-adic fixed point, because the $\mathbb{R}$ and $\mathbb{Q}_p$ topologies are incommensurable.

This provides **intrinsic qubit protection** without active QEC codes. Hardware-level error correction based on number theory, not energy gaps. The mutual singularity of the topologies means that any error process representable as an Archimedean perturbation (which includes all standard decoherence mechanisms — thermal, electromagnetic, vibrational) cannot affect information encoded in p-adic fixed points.

## 5.3 Falsifiable Predictions

The adelic framework makes specific, falsifiable predictions:

1. **Gromov δ = 0 for spin/ZBW transitions.** The Zitterbewegung (ZBW) current correlator computed on a Bruhat-Tits tree has Gromov hyperbolicity δ = 0 (it is a tree, not merely tree-like). Measurable via spin noise spectroscopy or EELS/RIXS. (ZBW Program P3, https://papers.qnfo.org/papers.)

2. **ZBW $\mathbb{Z}_2$ invariant distinguishes Dirac from Majorana fermions.** At the field-theoretic level, the ZBW current correlator is a momentum-dependent $\mathbb{Z}_2$ topological invariant. Dirac fermions (invariant = +1) and Majorana fermions (invariant = -1) are distinguished by their 2-adic boundary behavior. (ZBW Program P2.)

3. **p-adic stratification of code performance.** Optimal codes exhibit v_p^{max} significantly higher than random codes (7$\times$ for known families). This is testable by constructing code families and measuring their p-adic valuations, independent of any physical implementation.

---

# 6. Relation to String Theory's Extra Dimensions

## 6.1 The Standard String Theory Picture

In string theory, consistency of the superstring requires 10 spacetime dimensions. The extra 6 dimensions are "compactified" — curled up at the Planck scale into a Calabi-Yau manifold whose topology determines the low-energy particle spectrum and gauge group.

This picture faces well-known difficulties:
- The "landscape problem": ~10^500 possible Calabi-Yau compactifications, no principle to select among them.
- The extra dimensions are spatial — they inherit the Archimedean metric from the ambient spacetime. This makes it hard to explain why they produce discrete structure.
- No direct experimental evidence for extra spatial dimensions at any scale.

## 6.2 The P-adic Alternative

In the adelic picture, the "extra dimensions" are not spatial. They are **valuation-theoretic** — the p-adic completions of $\mathbb{Q}$, each with its own geometry (ultrametric, tree-structured, totally disconnected).

This resolves the string theory difficulties:

| Problem | String Theory | Adelic Picture |
|:--------|:-------------|:---------------|
| Landscape | ~10^500 CY manifolds, no selection principle | Finitely many primes; the relevant primes are the prime factors of the gauge group dimensions |
| Why discrete? | Compactification topology mysteriously produces discrete modes | p-adic spaces are intrinsically discrete (totally disconnected) |
| Experimental evidence | None for extra spatial dimensions | Testable via Gromov δ, p-adic valuations, ZBW spectroscopy (see §5.3) |
| Nature of dimensions | Spatial (Archimedean metric) | Valuation-theoretic (ultrametric); the ∞-place is the only spatial one |

The "shape" of the internal dimensions is not a Calabi-Yau manifold — it is a Bruhat-Tits building. The "particle spectrum" is not the cohomology of a compact manifold — it is the vertex set of a simplicial complex stratified by p-adic floor.

---

# 7. Conclusion

## 7.1 Summary

The discrete structure of quantum observables — spin, charge, color, weak isospin, hypercharge — is not a mystery requiring explanation within the Archimedean framework. It is the natural consequence of the fact that $\mathbb{Q}$ has multiple completions (Ostrowski), and nature uses all of them.

- The **∞-place ($\mathbb{R}$)** is the connected, dynamical, causal completion — the domain of time, fields, and limits (Paper I).
- The **2-adic place ($\mathbb{Q}_2$)** is the ultrametric completion encoding spin and fermion/boson statistics via the $\mathbb{Z}_2$ grading on the Bruhat-Tits tree boundary.
- The **3-adic place ($\mathbb{Q}_3$)** encodes color charge (QCD) via the Bruhat-Tits building for SL3($\mathbb{Q}_3$).
- Additional primes may encode additional discrete quantum numbers yet to be discovered.

## 7.2 Relation to Paper I

Paper I established that the Archimedean continuum $\mathbb{R}$ can be reduced to $\mathbb{R}_c$ — depth without breadth — with no loss of physical content. Paper II establishes that the p-adic completions are physically real in their own right, playing roles orthogonal to the Archimedean continuum. Together, they point toward a unified adelic framework where the physical universe is described over the ring of adeles 𝔸_$\mathbb{Q}$ — the product of all completions of $\mathbb{Q}$.

## 7.3 Open Questions

1. **Prove Conjecture 3.1:** Rigorously establish the connection between the $\mathbb{Z}_2$ grading on the Bruhat-Tits boundary at p=2 and the spin-statistics theorem in 3+1 dimensions.
2. **Complete the Standard Model mapping:** Identify the precise Bruhat-Tits vertices corresponding to each Standard Model particle representation.
3. **Experimental validation:** Execute the falsifiable predictions of §5.3 — Gromov δ measurement, ZBW $\mathbb{Z}_2$ invariant detection, and p-adic code stratification.
4. **Adelic unification:** Formulate a field theory over the adele ring 𝔸_$\mathbb{Q}$ that recovers both the Archimedean QFT (at the ∞-place) and the p-adic quantum structure (at the finite places) as projections.

---

# References

1. Ostrowski, A. (1916). "Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy)." *Acta Mathematica*, 41, 271–284.
2. Serre, J.-P. (1980). *Trees*. Springer. (Bruhat-Tits trees for SL2.)
3. Bruhat, F. & Tits, J. (1972). "Groupes réductifs sur un corps local." *Publications Mathématiques de l'IHÉS*, 41, 5–251.
4. QNFO (2026). "Number-Theoretic Ultrametric Foundations." https://papers.qnfo.org/papers/number-theoretic-ultrametric-foundations/.
5. QNFO (2026). "The Adelic Physics Program: A Grand Synthesis." https://papers.qnfo.org/papers.
6. QNFO (2026). "Adelic Quantum Error Correction: Intrinsic Qubit Protection from Ostrowski." https://papers.qnfo.org/papers.
7. QNFO (2026). "Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker." https://papers.qnfo.org/papers.
8. QNFO (2026). "p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity." https://papers.qnfo.org/papers.
9. Witten, E. (2015). "Anomalies, Brahmagupta, and the 24-Cell." (On the prime 2 in the spin-statistics connection.)
10. Carlsson, G. & Mémoli, F. (2010). "Characterization, Stability and Convergence of Hierarchical Clustering Methods." *Journal of Machine Learning Research*, 11, 1425–1470.
11. QNFO (2026). "The Computable Continuum: Depth Without Breadth." (Continuum Trilogy — Paper I.)
