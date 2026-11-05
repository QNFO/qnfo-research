# Harmonic Analysis is Langlands — The Fast Fourier Transform as the Computational Langlands Correspondence for GL(1)

## Abstract

We identify the Fast Fourier Transform (FFT) as the computational Langlands correspondence for the general linear group GL(1). Harmonic analysis on the finite cyclic group $\mathbb{Z}/n\mathbb{Z}$ decomposes functions into irreducible characters -- the FFT -- and this structure generalises directly to harmonic analysis on $G(\mathbb{Q})\backslash G(\mathbb{A})$ for a reductive group $G$ -- the Langlands program. In both cases, the operation is the same: decompose a function on a group into spectral components indexed by the group's irreducible representations. The group changes; the spectral decomposition structure is invariant. We formulate the **Computational Langlands Problem**: what is the algorithmic complexity of harmonic analysis on non-abelian reductive groups over global fields? We argue that the Bruhat--Tits tree -- the geometric model of a $p$-adic group -- provides a natural dyadic decomposition for $p$-adic harmonic analysis, generalising the divide-and-conquer structure of the Cooley--Tukey FFT. The QNFO ultrametric quantum computation framework, in which Hecke operators act as unitary gates on Bruhat--Tits qudits, is identified as the natural physical substrate for a computational solution to the non-abelian Langlands correspondence.

## 1. Introduction

The Fast Fourier Transform -- published by Cooley and Tukey in 1965, traced by them to unpublished work of Gauss in 1805 -- is widely regarded as the most important numerical algorithm of the twentieth century (1). It underpins signal processing, data compression, wireless communication, medical imaging, and quantum computing. Its computational structure -- $O(n \log n)$ operations via recursive divide-and-conquer -- is a canonical example of algorithmic efficiency.

What is less widely appreciated is *what the FFT actually computes*. The FFT is harmonic analysis on the finite cyclic group $\mathbb{Z}/n\mathbb{Z}$: it decomposes a complex-valued function $f: \mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$ into a sum of irreducible characters $\chi_\xi(x) = e^{2\pi i x\xi/n}$, each character corresponding to a frequency $\xi$. The characters of an abelian group are its irreducible representations. Harmonic analysis -- decomposition into irreducibles -- is the conceptual core.

The Langlands program, initiated by Robert Langlands in 1967 (3), is the non-abelian generalisation of harmonic analysis. Where the FFT decomposes functions on abelian groups (the multiplicative group $\mathbb{G}_m = \mathrm{GL}(1)$), the Langlands program decomposes automorphic forms on non-abelian reductive groups $\mathrm{GL}(n)$, $\mathrm{SL}(n)$, $\mathrm{Sp}(2n)$, and more exotic groups over global fields. The Langlands correspondence asserts that automorphic representations of a group $G$ over the adele ring $\mathbb{A}$ correspond to Galois representations into the Langlands dual group ${}^L G$.

This paper makes the following observation:

> **The FFT is the computational Langlands correspondence for $\mathrm{GL}(1)$.** Harmonic analysis on $\mathbb{Z}/n\mathbb{Z}$ (the FFT) generalises to harmonic analysis on $G(\mathbb{Q})\backslash G(\mathbb{A})$ (the Langlands program). The group changes; the spectral decomposition structure is invariant.

The implication is that the Langlands program -- usually regarded as pure mathematics, remote from computation -- has a well-defined computational core. For $\mathrm{GL}(1)$, that core is already solved (the FFT). For $\mathrm{GL}(n)$ with $n \geq 2$, it is an open problem: the **Computational Langlands Problem**. We define this problem precisely and identify a computational architecture -- ultrametric quantum computation on Bruhat--Tits buildings -- that is positioned to address it.

---

## 2. Harmonic Analysis on Abelian Groups: The FFT

### 2.1 Characters as Irreducible Representations

Let $G$ be a finite abelian group. A **character** of $G$ is a group homomorphism $\chi: G \to \mathbb{C}^\times$. The set of all characters $\widehat{G}$ forms a group under pointwise multiplication, the **Pontryagin dual** of $G$. For a finite group, $\widehat{G} \cong G$.

The **Fourier transform** of a function $f: G \to \mathbb{C}$ is the function $\hat{f}: \widehat{G} \to \mathbb{C}$ defined by:

$$
\hat{f}(\chi) = \sum_{x \in G} f(x) \, \overline{\chi(x)}.
\tag{1}
$$

The **Fourier inversion formula** reconstructs $f$ from $\hat{f}$:

$$
f(x) = \frac{1}{|G|} \sum_{\chi \in \widehat{G}} \hat{f}(\chi) \, \chi(x).
\tag{2}
$$

For $G = \mathbb{Z}/n\mathbb{Z}$, the characters are $\chi_\xi(x) = e^{2\pi i x\xi/n}$ for $\xi \in \mathbb{Z}/n\mathbb{Z}$, and the Fourier transform is the discrete Fourier transform:

$$
\hat{f}(\xi) = \sum_{x=0}^{n-1} f(x) \, e^{-2\pi i x\xi/n}.
\tag{3}
$$

The Cooley--Tukey FFT computes all $n$ values of $\hat{f}$ in $O(n \log n)$ operations by exploiting the factorisation $n = n_1 n_2$ to decompose the transform into smaller transforms. This is the computational content of harmonic analysis on $\mathbb{Z}/n\mathbb{Z}$.

### 2.2 Gauss's 1805 Asteroid Interpolation

Gauss's unpublished 1805 manuscript on the interpolation of asteroid Pallas's orbit (2) used what we now recognise as the FFT to compute the Fourier coefficients of a periodic function from unequally spaced samples -- a trigonometric interpolation problem. Gauss was performing harmonic analysis on a cyclic group, decomposing a discrete signal into its frequency components, predating Cooley--Tukey by 160 years.

Gauss's method was adelicity *avant la lettre*: discrete samples at finitely many observation times ($p$-adic-like finite completions) reconstructing a continuous orbital trajectory (Archimedean place). The core structure -- harmonic analysis unifying finite and continuous data -- was already present in the first computational instance.

---

## 3. Harmonic Analysis on Non-Abelian Groups: The Langlands Program

### 3.1 From Characters to Representations

When $G$ is non-abelian, its irreducible representations are no longer one-dimensional characters. A representation of $G$ is a group homomorphism $\pi: G \to \mathrm{GL}(V)$ for some complex vector space $V$. The representation is **irreducible** if $V$ has no proper $G$-invariant subspaces. The set of equivalence classes of irreducible representations is denoted $\widehat{G}$.

Harmonic analysis on $G$ generalises the Fourier transform: a function $f: G \to \mathbb{C}$ is decomposed into its projections onto the irreducible representations:

$$
\hat{f}(\pi) = \sum_{x \in G} f(x) \, \pi(x) \in \mathrm{End}(V_\pi),
\tag{4}
$$

where $\pi(x)$ is a matrix (the dimension of $V_\pi$) rather than a scalar. The **Plancherel formula** for finite groups states:

$$
\sum_{x \in G} |f(x)|^2 = \sum_{\pi \in \widehat{G}} d_\pi \, \|\hat{f}(\pi)\|_{\mathrm{HS}}^2,
\tag{5}
$$

where $d_\pi = \dim V_\pi$ and $\|\cdot\|_{\mathrm{HS}}$ is the Hilbert--Schmidt norm. This is the non-abelian generalisation of Parseval's identity.

### 3.2 Automorphic Forms and the Adelic Langlands Program

The Langlands program extends harmonic analysis from finite groups to reductive algebraic groups over global fields. The setting is the **adele ring** $\mathbb{A}_\mathbb{Q}$ of the rational numbers -- the restricted product of all completions:

$$
\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_{p}^{\prime} \mathbb{Q}_p,
\tag{6}
$$

where $\prod_{p}^{\prime}$ indicates that for almost all primes $p$, the $p$-adic component lies in the ring of $p$-adic integers $\mathbb{Z}_p \subset \mathbb{Q}_p$.

An **automorphic form** on a reductive group $G$ over $\mathbb{Q}$ is a function:

$$
\phi: G(\mathbb{A}_\mathbb{Q}) \to \mathbb{C}
\tag{7}
$$

satisfying: (i) left-invariance under $G(\mathbb{Q})$ (embedded diagonally), (ii) right-invariance under a compact open subgroup of the finite adeles, (iii) $K_\infty$-finiteness at the Archimedean place, and (iv) moderate growth. Automorphic forms are the non-abelian generalisation of periodic functions -- they are functions on $G(\mathbb{Q})\backslash G(\mathbb{A}_\mathbb{Q})$, the adelic quotient, which is the non-abelian analog of the circle $\mathbb{R}/\mathbb{Z}$ on which classical Fourier series are defined.

### 3.3 The Structural Isomorphism

The structural isomorphism is precise:

| Concept | Abelian case ($\mathrm{GL}(1)$) | Non-abelian case ($G$, general) |
|:--------|:-------------------------------|:-------------------------------|
| Group | $\mathbb{Z}/n\mathbb{Z}$ (cyclic) | $G(\mathbb{Q})\backslash G(\mathbb{A})$ (adelic quotient) |
| Function space | $f: \mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$ | $\phi: G(\mathbb{A}) \to \mathbb{C}$, automorphic |
| Decomposition basis | Characters $\chi_\xi$ (1-dim reps) | Automorphic representations $\pi$ (infinite-dim reps) |
| Spectral decomposition | $\hat{f}(\xi) = \sum_x f(x) e^{-2\pi i x\xi/n}$ | $\hat{\phi}(\pi) = \int_{G(\mathbb{Q})\backslash G(\mathbb{A})} \phi(g) \overline{\phi_\pi(g)} \, dg$ |
| Algorithm | Cooley--Tukey FFT, $O(n \log n)$ | **Computational Langlands Problem (OPEN)** |

The operation -- decompose a function on a group into spectral components indexed by irreducible representations -- is identical. The group changes from the cyclic group $\mathbb{Z}/n\mathbb{Z}$ (whose representation theory is trivial: one-dimensional characters) to a non-abelian reductive group $G$ (whose representation theory is the Langlands program). The complexity jumps from $O(n \log n)$ (solved) to unknown (open).

---

## 4. The Computational Langlands Problem

### 4.1 Problem Statement

**Definition (Computational Langlands Problem).** Let $G$ be a connected reductive algebraic group over $\mathbb{Q}$. Let $f: G(\mathbb{Q})\backslash G(\mathbb{A}_\mathbb{Q}) \to \mathbb{C}$ be an automorphic form:

1. **Finitely ramified** -- right-invariant under a compact open subgroup $K_f \subset G(\mathbb{A}_f)$ of index $N$,
2. **$K_\infty$-finite** -- belonging to a finite-dimensional subspace of the minimal $K_\infty$-type.

Compute the spectral decomposition of $f$ -- its projection onto a basis of automorphic representations $\{\pi\}$ with conductor bounded by $N$ -- in operations polynomial (or sub-exponential) in $N$ and the rank of $G$.

For $G = \mathrm{GL}(1)$, the answer is the FFT: $O(N \log N)$ operations [this paper, §2]. For $G = \mathrm{GL}(n)$ with $n \geq 2$, the problem is **open**.

### 4.2 Why This is Hard

Three obstructions separate the non-abelian case from the abelian case:

1. **Infinite-dimensional representations.** For $\mathrm{GL}(1)$, the local representations at each prime $p$ are one-dimensional characters of $\mathbb{Q}_p^\times$, indexed by an integer (the conductor). For $\mathrm{GL}(2)$, the local representations are infinite-dimensional representations of $\mathrm{GL}(2, \mathbb{Q}_p)$, classified by the local Langlands correspondence. At each place, the spectral decomposition requires working in an infinite-dimensional space -- truncated for computation, but the truncation introduces a representation-theoretic error that is poorly understood.

2. **Global multiplicity.** For $\mathrm{GL}(1)$, automorphic representations are one-dimensional and the multiplicity-one theorem holds trivially. For $\mathrm{GL}(n)$, automorphic representations can appear with multiplicity greater than one (though the strong multiplicity-one theorem for $\mathrm{GL}(n)$ guarantees that the multiplicity is at most one for cuspidal representations). The spectral decomposition must account for the possibility of degenerate eigenvalues -- equivalent to computing the multiplicity space of each automorphic representation.

3. **Global constraint (adelic Poisson summation).** The automorphic condition $f(\gamma g) = f(g)$ for $\gamma \in G(\mathbb{Q})$ couples the behaviour of $f$ across all places simultaneously. The adelic Poisson summation formula is the master identity that enforces this constraint. Computing the spectral decomposition requires solving this global constraint -- a problem whose complexity for non-abelian $G$ is not known to be in P.

### 4.3 The Adelic FFT for $\mathrm{GL}(1)$

For completeness, we state the $\mathrm{GL}(1)$ solution. The adelic FFT algorithm (detailed in the companion specification [ALP §5.2]) is:

1. **Local FFT at each finite place $p$:** Compute $\hat{f}_p$ on $\mathbb{Z}/p^{k_p}\mathbb{Z}$ in $O(p^{k_p} \log p^{k_p})$ operations.
2. **Archimedean FFT:** Compute $\hat{f}_\infty$ on an $M$-point grid in $O(M \log M)$ operations.
3. **Global constraint:** Apply the adelic Poisson summation formula to enforce restricted-product consistency.
4. **Assembly:** Combine local transforms: $\hat{f}(\chi) = \prod_v \hat{f}_v(\chi_v) \cdot S(\chi)$, where $S(\chi)$ is the global constraint factor.

The total complexity is $O(N \cdot \pi(N) \cdot \log N) \approx O(N^2 \log\log N / \log N)$, where $\pi(N) \approx N / \log N$ is the prime-counting function. This is super-quadratic in the truncation height $N$ -- substantially worse than the standard $O(N \log N)$ FFT on a cyclic group of order $N$, because the adelic FFT must perform harmonic analysis at *every* prime simultaneously.

---

## 5. The Bruhat--Tits Tree as the Natural Dyadic Decomposition

### 5.1 Geometry of the $p$-adic Group

The Cooley--Tukey FFT works by recursively factoring the group order $n = n_1 n_2$ and performing smaller FFTs on the factor groups. This divide-and-conquer structure relies on the group having a natural hierarchical decomposition -- a chain of subgroups $G \supset G_1 \supset G_2 \supset \cdots \supset \{e\}$.

For a $p$-adic group such as $\mathrm{GL}(2, \mathbb{Q}_p)$, the **Bruhat--Tits tree** $\mathcal{T}_p$ provides exactly this hierarchical structure (4). The tree is defined as follows:

- **Vertices** are homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$.
- **Edges** connect lattices $L \subset L'$ with $[L' : L] = p$.
- Each vertex has $(p+1)$ neighbours.
- The boundary at infinity is the $p$-adic projective line $\mathbb{P}^1(\mathbb{Q}_p) \cong \mathbb{Q}_p \cup \{\infty\}$.

The group $\mathrm{GL}(2, \mathbb{Q}_p)$ acts on the tree by isometries. A vertex at distance $k$ from a fixed origin corresponds to a lattice of index $p^k$ -- this is a natural hierarchical (dyadic for $p=2$, $p$-adic for general $p$) decomposition of the group's action.

### 5.2 Hecke Operators as Generalised Radix-$p$ Stages

The adjacency operator $A_p$ on the Bruhat--Tits tree has spectrum $[-2\sqrt{p}, 2\sqrt{p}]$, and its eigenfunctions are the **spherical functions** for $\mathrm{GL}(2, \mathbb{Q}_p)$. These spherical functions are the essential building blocks of the local Langlands correspondence at place $p$ -- they are the matrix coefficients of the unramified principal series representations (5).

In the Cooley--Tukey FFT, the radix-$p$ stage applies a $p \times p$ Fourier matrix to combine the results of smaller transforms. On the Bruhat--Tits tree, the **Hecke operator** $T_p$ (the adjacency operator) plays the role of the radix-$p$ stage: it maps functions on vertices at depth $k$ to functions at depth $k+1$, exactly as the radix-$p$ butterfly combines sub-transforms in the FFT.

The structural analogy is precise:

| FFT Component | $p$-adic Analog |
|:--------------|:----------------|
| Group order $n$ | $p$-adic depth $k_p$ (truncation $\mathbb{Z}/p^{k_p}\mathbb{Z}$) |
| Radix-$p$ factorisation | Bruhat--Tits tree depth $k_p$ |
| Radix-$p$ butterfly | Hecke operator $T_p$ on tree |
| Twiddle factors $e^{-2\pi i/n}$ | Spherical functions (local Langlands L-factors) |
| Bit-reversal permutation | Natural ordering by $p$-adic valuation |

This analogy suggests that the Cooley--Tukey FFT is not merely a clever algorithm for abelian groups -- it is a **special case** of a more general algorithm: hierarchical harmonic analysis on the Bruhat--Tits building of a reductive group, which reduces to radix-$p$ FFTs when the group is $\mathrm{GL}(1)$ (whose building is a point -- there is no geometry to exploit, only the abelian character theory).

### 5.3 The Walsh--Hadamard Transform at $p=2$

For $p = 2$, the Bruhat--Tits tree is a $3$-regular tree, and the local FFT on $\mathbb{Z}/2^k\mathbb{Z}$ reduces to the **Walsh--Hadamard transform** -- the binary Fourier transform:

$$
\hat{f}(w) = \sum_{x=0}^{2^k-1} f(x) \, (-1)^{\langle x, w \rangle},
\tag{8}
$$

where $\langle x, w \rangle$ is the dot product of the binary representations of $x$ and $w$. The Walsh--Hadamard transform has a butterfly structure with $k \cdot 2^{k-1}$ additions and *zero complex multiplications* -- it is substantially cheaper than the general complex FFT. For $p=2$, which dominates the adelic FFT asymptotically (since $p=2$ has the deepest truncation for a given $N$), the adelic FFT reduces to a tower of Walsh--Hadamard transforms coupled by the global constraint.

---

## 6. Ultrametric Quantum Computation as the Computational Substrate

### 6.1 Bruhat--Tits Qudits

The QNFO ultrametric quantum computation framework (6) proposes that the Bruhat--Tits tree can serve as a computational substrate:

- **Physical qudits** (quantum systems of dimension $p$) reside at vertices of the tree.
- **Hecke operators** $T_p$ act as unitary gates moving quantum information along edges.
- The **passive geometric error correction** provided by the ultrametric ($p$-adic) distance -- under which small errors cannot accumulate (the non-Archimedean property $\|x + y\|_p \leq \max(\|x\|_p, \|y\|_p)$) -- protects quantum information during computation.

The $p$-adic quantum Fourier transform -- the quantum analog of the $p$-adic FFT -- is realised as a sequence of radix-$p$ quantum gates on Bruhat--Tits qudits.

### 6.2 The Adelic FFT Processor

An adelic FFT processor -- a physical device that performs harmonic analysis on the adele ring -- would operate as follows (following the companion specification [ALP §5.2]):

1. **Local preparation:** Encode the input function $f_p$ in qudits on the Bruhat--Tits tree for each prime $p \leq N$.
2. **Local transform:** Apply $p$-adic quantum Fourier transform gates. For $p = 2$, this is the Walsh--Hadamard transform with no complex multiplications.
3. **Hecke coupling:** Apply Hecke operators to enforce the global restricted-product constraint -- this step couples all places simultaneously and is the computational bottleneck.
4. **Archimedean readout:** The physical measurement occurs at the Archimedean place, producing $\hat{f}_\infty$ as the observable output.

The key architectural insight is a **hardware/software co-design**: p-adic computations are noise-protected by the ultrametric (passive QEC), while the Archimedean readout interfaces with human observers. The physical realisation of place-crossing amplitudes -- established in ALP Phase 4.1 (7) -- provides the mechanism for coupling the p-adic and Archimedean components.

### 6.3 Open Path to the Non-Abelian Case

The generalisation from $\mathrm{GL}(1)$ to $\mathrm{GL}(n)$ for $n \geq 2$ in the ultrametric quantum computation framework involves:

1. **Bruhat--Tits buildings** -- higher-dimensional simplicial complexes generalising the tree, on which $\mathrm{GL}(n, \mathbb{Q}_p)$ acts. These buildings have chambers (maximal simplices) as the natural computational units, with adjacency relations generalising the tree's edge structure.
2. **Hecke algebras** -- the non-abelian generalisation of the Hecke operator $T_p$, now acting on functions on the building's chambers. The irreducible representations of the Hecke algebra correspond (via the Satake isomorphism) to unramified representations of $\mathrm{GL}(n, \mathbb{Q}_p)$.
3. **Langlands dual gates** -- if the Langlands correspondence identifies automorphic representations of $G$ with Galois representations into ${}^L G$, then physical gates on $G$'s Bruhat--Tits building should have dual interpretations as operations on the Galois side -- a computational realisation of the duality at the core of the Langlands program.

The complexity of this generalisation remains the central open question. The optimistic hypothesis is that the recursive (building-theoretic) structure of Bruhat--Tits buildings provides a natural hierarchical decomposition for $\mathrm{GL}(n)$ analogous to the Cooley--Tukey factorisation for $\mathrm{GL}(1)$, yielding a complexity of $O(N^{c_n} \log N)$ for some exponent $c_n$ depending on $n$. The pessimistic bound -- direct diagonalisation of the Hecke algebra -- would be exponential in $n$ and $N$. Determining which bound is correct is the Computational Langlands Problem.

---

## 7. Discussion

### 7.1 Summary of Results

We have established the following chain of identifications:

1. **Harmonic analysis on a group $G$** = decomposition of functions $f: G \to \mathbb{C}$ into irreducible representations.
2. For $G = \mathbb{Z}/n\mathbb{Z}$ (abelian, $\mathrm{GL}(1)$): the irreducible representations are one-dimensional characters; the decomposition is the discrete Fourier transform; the fast algorithm is the Cooley--Tukey FFT, complexity $O(n \log n)$.
3. For $G = G(\mathbb{Q})\backslash G(\mathbb{A})$ (non-abelian reductive, general): the irreducible representations are automorphic representations; the decomposition is the Langlands program; **the fast algorithm is not known**.
4. The Bruhat--Tits tree for $G = \mathrm{GL}(2, \mathbb{Q}_p)$ provides the natural hierarchical ($p$-adic) decomposition -- the analog of the Cooley--Tukey factorisation -- with Hecke operators as the generalised radix-$p$ stages.
5. The QNFO ultrametric quantum computation framework provides the physical architecture to implement this generalised FFT, with passive geometric error correction as a theorem of the $p$-adic metric.

### 7.2 The Computational Langlands Problem as a Research Program

The Computational Langlands Problem is more than a complexity-theoretic question. It defines a research program at the intersection of:

- **Computational harmonic analysis:** Generalising the FFT beyond abelian groups. The $p$-adic FFT tower and the adelic Poisson summation constraint are the first concrete formalisms.
- **The Langlands program:** Extracting the computational content from a mathematical edifice that has historically been presented as a structural correspondence rather than an algorithmic one.
- **Ultrametric quantum computation:** Building the physical substrate -- qudits on Bruhat--Tits buildings, Hecke operators as gates, place-crossing amplitudes as interconnects -- on which the non-abelian FFT can be implemented.

The open problems enumerated in the companion specification [ALP §5.2] -- the global constraint algorithm (P3), the $p$-adic depth truncation error (P2), the physical Bruhat--Tits qudit realisation (P4) -- constitute the technical agenda.

### 7.3 Gauss's Adelic Instinct

[PHILOSOPHY] Gauss's 1805 asteroid interpolation was adelic before adeles were invented. He had discrete observations at finitely many times (the finite places -- $p$-adic completions of the rational timeline) and a continuous trajectory to reconstruct (the Archimedean place -- the real completion). The FFT was born at the intersection of the finite and the infinite, of arithmetic and analysis. It took 160 years for Cooley and Tukey to rediscover the algorithm, and another 60 years for the Langlands program to reveal what that algorithm was really computing: the spectral decomposition of the automorphic spectrum of $\mathrm{GL}(1)$. Gauss, working with pencil and paper on an asteroid's orbit, was performing the first computational instance of the Langlands program. He just did not know it.

---

## Declarations

**Funding.** No external funding was received for this research.

**Conflicts of Interest.** The authors declare no conflicts of interest.

**Ethics Approval.** Not applicable -- this is theoretical research with no human subjects, animal subjects, or environmental impact.

**Consent to Participate.** Not applicable.

**Author Contributions.** QNFO Research (Rowan Brad Quni-Gudzinas): conceptualisation, formal analysis, writing.

**Data Availability.** All source materials are available in the Adelic Langlands Physics repository (GitHub: QNFO/adelic-langlands-physics, branch feature/alp-phase1) and at papers.qnfo.org (https://papers.qnfo.org/papers).

**Code Availability.** Computational specifications are provided in the companion document [ALP §5.2]. No empirical code was developed for this theoretical paper.

**Materials Availability.** Not applicable -- no materials were used.

**Use of Artificial Intelligence.** This paper was authored with AI-assisted drafting and revision. The mathematical content, conceptual framework, and all non-trivial claims were formulated by the human author and verified against the published literature. AI tools were used for formatting, copyediting, and exposition.

---

## References

[1] J. W. Cooley and J. W. Tukey, "An Algorithm for the Machine Calculation of Complex Fourier Series," *Mathematics of Computation*, vol. 19, no. 90, pp. 297--301, 1965. DOI: 10.2307/2003354.

[2] M. T. Heideman, D. H. Johnson, and C. S. Burrus, "Gauss and the History of the Fast Fourier Transform," *IEEE ASSP Magazine*, vol. 1, no. 4, pp. 14--21, 1984. DOI: 10.1109/MASSP.1984.1162257.

[3] R. P. Langlands, "Problems in the Theory of Automorphic Forms," in *Lectures in Modern Analysis and Applications III*, Springer Lecture Notes in Mathematics, vol. 170, pp. 18--61, 1970.

[4] J.-P. Serre, *Trees*, Springer-Verlag, 1980. Translated from the French *Arbres, Amalgames, $\mathrm{SL}_2$* (1977).

[5] P. Cartier, "Representations of $p$-adic Groups: A Survey," in *Automorphic Forms, Representations and $L$-Functions*, Proc. Symp. Pure Math., vol. 33, part 1, pp. 111--155, AMS, 1979.

[6] QNFO Research, "Ultrametric Quantum Computation and the Langlands Program," v0.2, 2026. Available at: https://papers.qnfo.org/papers/reassessing-the-foundations-of-quantum-computation

[7] QNFO Research, "Place-Crossing Amplitudes: Correlation Functions Across Completions of $\mathbb{Q}$," Adelic Langlands Physics, Phase 4.1, 2026. the QNFO archive https://papers.qnfo.org/papers.

[ALP §5.2] QNFO Research, "Computational Harmonic Analysis on the Adele Ring -- Toward an Adelic Fast Fourier Transform," Adelic Langlands Physics, Phase 5.2 (companion specification), 2026. Available in the ALP repository at `artifacts/phase5.2-adelic-fft-spec.md`.
