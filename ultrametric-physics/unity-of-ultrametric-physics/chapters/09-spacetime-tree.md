---
layout: chapter
title: "Chapter 9: Spacetime as a Bruhat-Tits Tree"
permalink: /chapters/09-spacetime-tree/
previous_chapter: /chapters/08-adelic-theory/
previous_title: "Chapter 8: Adelic Theory"
next_chapter: /chapters/10-standard-model/
next_title: "Chapter 10: Standard Model"
---

## Chapter 9: Spacetime as a Bruhat-Tits Tree

General relativity describes spacetime as a smooth Lorentzian manifold — a continuum of Archimedean distinctions. At the Planck scale ($\ell_P \approx 1.6 \times 10^{-35}$ m), the smooth picture breaks down. The ultrametric proposal: **spacetime at the Planck scale is a Bruhat-Tits tree** — the geometric form of nested distinctions introduced in Chapter 5.

The continuous manifold is an approximation. The distinction tree is the thing itself.

### 9.1 The Tree as Discrete Spacetime

<div class="definition">
<div class="label">Definition 9.1 (Tree spacetime)</div>
$T_{N,q}$ vertices are Planck-scale "atoms of spacetime" — fundamental distinctions. Edges carry weight $\log q$ encoding proper time/distance. Tree depth maps to energy scale: deeper = higher energy = shorter distance. Moving from leaves toward the root is coarse-graining (Wilson RG flow) — progressively blurring fine distinctions.
</div>

Each vertex is a distinction at a specific scale. The tree encodes the entire hierarchy of spacetime distinctions from Planck to cosmological scales.

### 9.2 Causal Structure

<div class="theorem">
<div class="label">Theorem 9.2 (Unique geodesics = deterministic causality)</div>
In a tree there is exactly one simple path between any two vertices. Therefore: (1) causal propagation is deterministic — there is a unique causal route between any two spacetime distinctions, (2) no closed timelike curves (trees are cycle-free — distinctions cannot contain themselves), (3) the sum-over-histories has a unique saddle point — a geometric solution to the problem of time.
</div>

In Archimedean spacetime, the path integral sums over infinitely many geometries. On the tree, the unique geodesic provides a natural saddle point — the tree's distinction structure selects a preferred causal ordering.

### 9.3 The Boundary

The boundary $\partial T_{N,q}$ (equivalence classes of infinite geodesic rays) is a Cantor set with Hausdorff dimension $\dim_H = \log N / \log q$. It is the interface between the discrete bulk (quantum realm of nested distinctions) and the continuous world of classical observers. Physically, it is $\mathbb{P}^1(\mathbb{Q}_p) \cong \mathbb{Q}_p \cup \{\infty\}$.

### 9.4 Tree Holographic Principle

Boundary degrees of freedom encode bulk physics — a discrete realization of AdS/CFT. The number of boundary points within distance $\varepsilon$ grows as $\varepsilon^{-\dim_H(\partial T)}$, while bulk vertices grow as $N^d$. Boundary has fewer DOF, consistent with the holographic principle and Bekenstein-Hawking entropy $S = A/4G\hbar$.

### 9.5 Tensor Network Realization

MERA (Multiscale Entanglement Renormalization Ansatz) tensor networks have the exact structure of a Bruhat-Tits tree. This is not coincidence — the tree is the optimal architecture for representing scale-invariant quantum states. The distinction hierarchy provides the natural entanglement structure.

### 9.6 Black Holes

A black hole on the tree is a **horizon subtree** — a rooted subtree from which all geodesics to the boundary are blocked. Information is trapped within a distinction that cannot communicate outward. Entropy: $S_{BH} = \log|\partial H| / \log q$ — the logarithm of the number of boundary distinctions trapped behind the horizon.

### 9.7 Emergent Lorentz Symmetry

Tree automorphisms ($\mathrm{PGL}(2,\mathbb{Q}_p)$) approximate Lorentz symmetry in the continuum limit. Violations are suppressed by $\delta c/c \sim q^{-d}$ — safely below current bounds. Lorentz symmetry is not fundamental; it emerges from the symmetries of the distinction tree at large depth.

**Key result:** Continuous spacetime is not fundamental. It is a shadow — an effective description above the Planck scale. The continuous manifold is an approximation to the distinction tree, valid only when we coarse-grain over many levels. The tree is the thing itself.

---

**Next: [Chapter 10: From Trees to the Standard Model →]({{ '/chapters/10-standard-model' | relative_url }})**
