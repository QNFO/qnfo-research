# Why Vertices, Not Points? Vertex-Anchored Braiding, Stabilizer Arithmetic, and Displacement Gaps on Bruhat–Tits Buildings

## Abstract

Bruhat–Tits buildings are the canonical combinatorial-geometric objects attached to reductive groups over non-Archimedean local fields, and the recent QNFO constructions of p-adic braid groups [12], p-adic anyon models [13], and a p-adic Temperley–Lieb parameter [14] anchor their discrete braiding data at the *vertex set* of the building rather than at arbitrary points of its geometric realization. This paper answers the question posed in the title with a combination of exact arithmetic and explicit metric computation in the rank-one case, where the building of SL₂ over ℚ_p is a (p+1)-regular tree. We compute ball growth exactly (for p = 3: a radius-2 ball contains 17 vertices and 16 edges; a radius-3 ball contains 53 vertices and 52 edges), we compute the finite stabilizer layers exactly (|SL₂(𝔽_p)| = p(p²−1), edge-stabilizer index p+1, pro-p Iwahori filtration index p²−1), and we compute a displacement gap: a point at distance d from the nearest vertex is moved by exactly 2d by the Weyl element of the vertex stabilizer, so the covering radius of the vertex set is 1/2 and any vertex-stabilizer-equivariant structure supported in a ball of radius r < 1/2 is vertex-supported. We show that the vertex set is the unique G-orbit whose stabilizer surjects onto the full finite group SL₂(𝔽_p), yielding p+1 fusion channels per vertex, while generic edge points cost a stabilizer factor of p+1, collapse the finite layer to the Borel of order p(p−1), and supply no new braid generators. Limitations (rank one, finite radius, projected higher-rank bounds) and falsification criteria are stated explicitly.

## 1. Introduction

Let F be a non-Archimedean local field (e.g. ℚ_p) and G a connected reductive F-group. The Bruhat–Tits building X = X(G, F) is a polysimplicial complex on which G(F) acts by isometries; its apartments are Coxeter complexes, its maximal simplices correspond to Iwahori subgroups, and its vertices correspond to parahoric subgroups — compact open subgroups that play the role of integral models of G. In the real symmetric space G/K no point is special: G acts transitively and structures are defined on the whole space. In the p-adic setting the building is not homogeneous in that sense: vertices have larger, more arithmetic stabilizers, and a large literature implicitly or explicitly works with vertex-supported data.

The question *why vertices, not points?* is not rhetorical. The QNFO corpus makes it vivid: the p-adic braid groups on Bruhat–Tits buildings [12] attach braid generators to the discrete vertex structure; the p-adic anyon models [13] and the p-adic Temperley–Lieb and Jones constructions [14] inherit this vertex dependence through fusion and braiding data defined on the same discrete scaffolding.

This paper has three goals. First, we give a unified account of the vertex-rigidity phenomenon across compactification theory, tropical geometry, representation theory, and Hecke-module theory (Section 2). Second, we supply two complementary quantitative mechanisms (Sections 3–5): (i) an *orbit-and-stabilizer* argument — the vertex set is the minimal G-stable skeleton and the unique orbit carrying the full finite quotient layer SL₂(𝔽_p) — verified by exact arithmetic; and (ii) a *metric displacement-gap* argument — vertex stabilizers move non-vertex points by a quantified amount, forcing locally supported equivariant structures to concentrate at vertices. Third, we state honest limitations and falsification criteria (Section 6).

Every number in Sections 4–5 is derived by explicit arithmetic from stated standard inputs; nothing is simulated or measured. Claims that extend beyond the computed cases are labeled projections with stated assumptions.

## 2. Background and Related Work

We review the literature in four clusters.

**Tropical and lattice methods.** In [1], stabilizers of points in Bruhat–Tits buildings and in certain compactifications are described by tropical linear algebra, and the compactifying fans arise from algebraic representations of G. This treats *pointwise* stabilizers — exactly the "points" side of our question — and shows they are governed by tropical data; our claim refines this by isolating which point stabilizers support discrete braiding. The SL-specialized companion [6] shows that the fans compactifying apartments are given by tropical Schur polynomials, which are integral on integral data; the vertices of the building are exactly the points whose stabilizers are described by integral lattice data rather than fractional translates. In a related lattice-theoretic register, [3] proves a compression-of-angles theorem for buildings of type A: for the set Lat(V) of lattices in a p-adic vector space, the complex distance is a complete system of invariants for pairs under the full linear group, and a Nazarov-semigroup element compresses configurations toward apartments. Compression is the mechanism by which braiding data on the building reduces to apartment-level data; our vertex claim identifies the fixed points at which the compressed data becomes discrete.

**Group-theoretic and wonderful compactifications.** The convergence theorem of [2] for sequences of parahoric subgroups in the Chabauty topology compactifies the *vertex set* of the building directly, together with a structure theorem for the buildings of Levi factors. That this compactification is built on vertices, not arbitrary points, is structural: parahoric subgroups are attached to facets, and vertices are the facets whose stabilizers are maximal among the parahorics. The non-split case is treated in [5], where the maximal Satake–Berkovich compactification of the building is identified with an embedding into the Berkovich analytification of the wonderful compactification. Notably, the Berkovich analytification fills in all "points," including infinitesimal directions, yet the boundary structure is still controlled by facet (vertex-type) stabilizers — reinforcing rather than dissolving the vertex/point distinction.

**Representation theory on the building.** Fixed point sets in buildings are used in [4] to give two complementary sufficient conditions, formulated via building geometry, for irreducible components of the restriction of an essentially tame supercuspidal representation to a maximal compact subgroup to occur in non-inertially-equivalent representations. Fixed-point sets of parahoric-type subgroups are unions of facets whose vertices are the load-bearing points — the representation-theoretic shadow of our claim. The functor of [7] sends admissible locally analytic G-representations with prescribed infinitesimal character to equivariant sheaves on the building; for smooth representations it recovers coefficient systems, which are functors on the facet category — sheaf-theoretic data is facet-supported by construction, with stalks at vertices and transition maps along edges. The correspondence of [8] between pro-p Iwahori–Hecke modules over a quasi-Frobenius ring and coefficient systems on the building is the formal reason fusion idempotents live at the pro-p Iwahori level, which our arithmetic (Section 4) shows is a vertex phenomenon. On the arithmetic side, [9] identifies the set of maximal orders containing a given suborder with a subtree of the Bruhat–Tits tree — the "branch" of the order; maximal orders correspond to vertices, so the branch formalism is itself vertex-anchored combinatorics, and the "missing branches" phenomenon illustrates what is lost when one leaves the vertex set.

**Unitarity and cuspidal support.** The parameterization of irreducible representations of p-adic GL by cuspidal-line data [10] and Jantzen's correspondence for classical groups, with the question of whether it preserves unitarizability [11], provide the representation-theoretic context in which discrete invariants play the role that vertices play geometrically: a discrete skeleton carrying the classification, with continuous families reducible to it.

**The QNFO corpus.** The p-adic braid groups on Bruhat–Tits buildings [12] establish the geometry of discrete braiding that this paper grounds; the anyon models of [13] (restricted quantum groups at roots of unity, Verma modules, ultrametric fusion) supply the fusion-side requirement of a finite set of anyon types with F- and R-matrices; and the p-adic Temperley–Lieb parameter as cyclotomic units with the p-adic Jones polynomial [14] supplies the diagrammatic algebra whose Markov trace evaluations require a finite Temperley–Lieb category. All three inherit the vertex scaffolding; our results supply the geometric mechanism that any such vertex-based construction implicitly relies on.

## 3. Methods

**Setting.** Let F = ℚ_p, G = SL₂(F), and let X be the Bruhat–Tits building of G, the (p+1)-regular tree. Vertices correspond to homothety classes of ℤ_p-lattices in F²; take v₀ = [ℤ_p²] as base vertex. The geometric realization is a metric tree with each edge isometric to [0,1]; "points" of X include all interior edge points. The standard apartment through v₀ is the line {(s, −s) : s ∈ ℝ} in e-coordinates, with vertex set {(m, −m) : m ∈ ℤ} and metric d((s,−s),(s′,−s′)) = |s − s′|/2, so adjacent vertices are at distance 1.

**Inputs and sources.** All inputs are standard structure theorems for SL₂ over p-adic fields:

- (I1) The building of SL₂(ℚ_p) is a tree of valence p+1 (standard; consistent with the tropical descriptions of [1],[6]).
- (I2) Stab(v₀) = SL₂(ℤ_p), and G acts transitively on vertices (standard lattice theory; the Lat(V) framework of [3]).
- (I3) Reduction mod p surjects SL₂(ℤ_p) → SL₂(𝔽_p) with pro-p kernel.
- (I4) The stabilizer of an edge e with endpoint v₀ reduces mod p to the standard Borel B(𝔽_p).
- (I5) The pro-p Iwahori subgroup I is the preimage of B(𝔽_p); its pro-p radical I₁ is the preimage of the unipotent radical U(𝔽_p) ≅ (𝔽_p, +).
- (I6) The Weyl element w = [[0,−1],[1,0]] ∈ SL₂(ℤ_p) swaps the apartment coordinate s ↦ −s.

**Protocol.** From (I1)–(I6) we compute: (a) sphere and ball sizes; (b) orders of SL₂(𝔽_p), B(𝔽_p), U(𝔽_p) by direct counting; (c) stabilizer indices; (d) the orbit decomposition of the point set; (e) the displacement of non-vertex points under vertex stabilizers. We instantiate at p = 3 throughout.

## 4. Analysis

**4.1 Ball growth.** By (I1), the sphere of radius n ≥ 1 has size |S_n| = (p+1)p^{n−1} (each vertex at distance n−1 has p forward edges, one edge returning). Hence

|B_N| = 1 + Σ_{n=1}^{N} (p+1)p^{n−1} = 1 + (p+1)(p^N − 1)/(p − 1),

and, X being a tree, the number of edges in B_N is |B_N| − 1.

For p = 3 (valence 4):
- |S₁| = 4, |S₂| = 12, |S₃| = 36.
- **Radius 2:** V(2) = 1 + 4·(9−1)/2 = 1 + 16 = 17 vertices; E(2) = 16 edges.
- **Radius 3:** V(3) = 1 + 4·(27−1)/2 = 1 + 52 = 53 vertices; E(3) = 52 edges.
- Radius 4: V(4) = 1 + 4·80/2 = 161.

Asymptotically V(N) ~ ((p+1)/(p−1))·p^N, so all vertex-anchored counts grow exponentially with base p.

**4.2 The finite layer.** By (I3), the finite quotient at v₀ is SL₂(𝔽_p). It acts transitively on the p+1 lines of 𝔽_p²; the stabilizer of a line has order p(p−1), so |SL₂(𝔽_p)| = (p+1)·p(p−1) = p(p²−1). For p = 3: 3·8 = 24. The Borel B(𝔽_p) = {[[a,b],[0,a⁻¹]]} has p(p−1) elements (p−1 choices of a, p of b): 6 for p = 3. The unipotent radical U(𝔽_p) has order p: 3 for p = 3.

**4.3 Stabilizer indices.** By (I2)–(I4), Stab(e) is the preimage of B(𝔽_p), so

[Stab(v₀) : Stab(e)] = p(p²−1)/p(p−1) = p+1 (4 for p = 3),

which must equal the valence, since Stab(v₀) acts transitively on the p+1 edges at v₀. By (I5):

[I : I₁] = p(p−1)/p = p−1 (2 for p = 3);  [Stab(v₀) : I₁] = (p+1)(p−1) = p²−1 (8 for p = 3).

Cross-check: |SL₂(𝔽₃)|/|U(𝔽₃)| = 24/3 = 8 ✓.

**4.4 Orbit decomposition.** Every point of the tree is a vertex or an edge interior. G is transitive on vertices and on oriented edges, hence on edge interiors. So the point set decomposes into exactly two G-orbits: X = X⁰ ⊔ X^gen, with stabilizers SL₂(ℤ_p) and Stab(e) of index p+1 in Stab(v₀). "Using all points instead of vertices" adds exactly one orbit while shrinking the stabilizer by the factor p+1.

**4.5 Displacement gap.** By (I6), w·(s,−s) = (−s, s), so d(x, w·x) = |s| for x = (s,−s). Conjugating w by the translation moving v₀ to v_m (which exists by (I2)), the nontrivial Weyl element in P_{v_m} moves x = (s,−s) by d(x, w_m·x) = |s − (2m − s)|/2 = |s − m| = 2d, where d = d(x, v_m). Since min_{m∈ℤ}|s−m| ranges over [0, 1/2], the **covering radius of the vertex set is 1/2**, attained at edge midpoints, where the displacement is exactly 1 (a full edge length). Hence: *no point of the tree is moved by less than twice its distance to the vertex set, and vertices are moved by 0.*

**4.6 Vertex-rigidity bound.** Let S be a P_v-equivariant structure supported in B(x, r). Some g ∈ P_v moves x by δ(x) = 2·d(x, X⁰); if r < δ(x)/2, the ball B(x, r) and its g-translate are disjoint, so an equivariant structure supported in B(x, r) must be supported in the intersection of all such translates — i.e., at v. Since the covering radius is 1/2, δ(x) ≥ 1 off the vertex set only at midpoints; more precisely δ(x) = 2d(x, X⁰) > 0 for every non-vertex x, and the binding case is the edge midpoint with δ = 1, giving: **any P_v-equivariant structure supported in a ball of radius r < 1/2 is vertex-supported.**

**4.7 What the quotient layers contain.** The vertex stabilizer has finite quotient SL₂(𝔽_p) of order p(p²−1), containing idempotents for all p+1 lines of 𝔽_p² — the p+1 fusion channels out of each vertex. The generic-point stabilizer has finite quotient only B(𝔽_p) of order p(p−1), with a single stabilized line: one channel, no permutation of the p+1 channels. The anyon model of [13] requires a finite fusion ring with nontrivial braiding on its object set; the smallest non-abelian such structure available here needs the full SL₂(𝔽_p) layer, i.e., a vertex. The Temperley–Lieb parameter of [14] requires a diagram category counting channels through a finite object set; the p+1 channels per vertex are exactly the p+1 lines of 𝔽_p², whereas a generic point sees one.

**4.8 Why not all points?** If x is a vertex, nothing changes. If x is a generic edge point, the braid generators of [12], which exchange adjacent vertices across an edge, cannot be indexed at x: the exchange moves x off its stabilizer while the vertex set is preserved setwise by every such exchange. Formally, X⁰ is G-stable and the braid action of [12] is an action on X⁰-permutations; the added orbit X^gen contributes no new braid generators (one orbit, no branching) and destroys the finite-layer arithmetic of §4.7. Hence vertices are not merely sufficient but, among G-stable anchoring sets supporting the fusion data of [13] and [14], minimal and canonical.

**4.9 Higher-rank projection.** For SL_n, the chamber barycenter is e = (n−1, −1, …, −1)/n (up to permutation), displaced by a transposition by |s₁ − s₂| = (n−1)/n + 1/n = 1 — exactly 1 for all n. Its distance to the nearest vertex is ‖e‖/√2 = √((n−1)n)/(n√2) = √((n−1)/(2n)). Check: n = 2 gives 1/2 ✓ (§4.5); n = 3 gives √(2/6) = 1/√3 ≈ 0.577 ✓ (independent Voronoi-cell computation for the A₂ lattice: the hexagonal cell with unit minimal distance has circumradius 1/√3 ≈ 0.5774). The displacement-to-distance ratio at the barycenter is √(2n/(n−1)), decreasing from 2 (n = 2) through √3 ≈ 1.732 (n = 3) toward √2 as n → ∞. **Projection (labeled):** if the chamber barycenter is the worst case for all n — assumed, not proved here — the ratio exceeds √2 uniformly, and a vertex-rigidity bound of the same qualitative form holds throughout type A. Uncertainty: if the worst-case assumption fails, the uniform ratio could fall below √2 by an amount we cannot bound without further computation.

## 5. Results

All numbers are computed in Section 4 from inputs (I1)–(I6); none are simulated or measured.

| Quantity | General | p = 3 | Source |
|---|---|---|---|
| Ball vertices V(2) | 1 + (p+1)(p²−1)/(p−1) | 17 | §4.1 |
| Ball edges E(2) | V(2) − 1 | 16 | §4.1 |
| Ball vertices V(3) | 1 + (p+1)(p³−1)/(p−1) | 53 | §4.1 |
| Ball edges E(3) | V(3) − 1 | 52 | §4.1 |
| Vertex finite layer | p(p²−1) | 24 | §4.2 |
| Generic-point finite layer | p(p−1) | 6 | §4.2 |
| [Stab(v₀) : Stab(e)] | p+1 | 4 | §4.3 |
| [Stab(v₀) : I₁] | p²−1 | 8 | §4.3 |
| Covering radius of X⁰ | 1/2 | 1/2 | §4.5 |
| Displacement gap | δ(x) = 2·d(x, X⁰) | — | §4.5 |
| Vertex-rigidity bound | r < 1/2 forces vertex support | — | §4.6 |
| Fusion channels per vertex / generic point | p+1 / 1 | 4 / 1 | §4.7 |

**R1 (Skeleton efficiency).** The vertex set meets every chamber and is minimal with this property; edges = vertices − 1 in every finite subtree (52/53 ≈ 0.981 edge-to-vertex ratio at N = 3, tending to 1).

**R2 (Finite layer).** The vertex stabilizer surjects onto SL₂(𝔽_p) of order p(p²−1); the generic-point stabilizer surjects only onto the Borel of order p(p−1).

**R3 (Stabilizer cost).** Passing from vertices to generic points multiplies the stabilizer index by p+1 and collapses the finite quotient layer from dimension p(p²−1) to p(p−1).

**R4 (Displacement gap and rigidity).** A point at distance d from the nearest vertex is moved by exactly 2d by the vertex stabilizer's Weyl element; any P_v-equivariant structure supported in a ball of radius r < 1/2 is vertex-supported.

**R5 (Orbit count).** The point set decomposes into exactly two G-orbits; the extra orbit adds no braid generators and no fusion channels.

**R6 (Projection, labeled).** For all SL_n, the chamber-barycenter displacement is exactly 1 and the displacement-to-distance ratio is √(2n/(n−1)) > √2, under the stated worst-case assumption (§4.9).

No empirical measurements or data from the QNFO corpus are reported; [12],[13],[14] are used as motivation and as the constructions whose vertex dependence our results explain.

## 6. Discussion

**What the results do and do not show.** We have shown, by exact arithmetic and explicit metric computation, that the vertex set is the minimal G-stable skeleton, the unique orbit carrying the full finite quotient layer, and the anchoring set forced by the displacement gap for locally supported equivariant structures. This is a mechanism, not a theorem about the QNFO constructions: [12],[13],[14] define their structures on vertices by choice, and our results explain why that choice is natural — indeed nearly forced — but do not prove that alternative point-based constructions are impossible.

**Limitations.** (1) *Rank-one restriction:* the exact arithmetic is confined to SL₂; higher-rank buildings involve higher-dimensional apartment combinatorics, and the type-A displacement statement is a labeled projection (R6). (2) *Generator bound vs. exact count:* the edge count E(r) is an upper bound on elementary braid generators in the sense of [12]; braid relations may reduce the minimal generating set, so the bound is not an exact count of independent generators. (3) *Boundary behavior:* in the non-split setting of [5], limit points may carry essential data that vertices alone do not; our analysis does not address boundary behavior. (4) *Necessity:* a fully formal proof that the SL₂(𝔽_p) layer is necessary (not merely sufficient) for the anyon model would require the machinery of [8] made explicit for the QNFO fusion rules.

**Falsification criteria.** A construction of a p-adic anyon model in the sense of [13] whose fusion ring is faithfully realized by the stabilizer of a generic edge point (a Borel-type subgroup) would falsify R2–R5. A braid group in the sense of [12] with generators not conjugate into the vertex-anchored system would falsify the minimality claim of §4.8. Conversely, discovering braid relations reducing the generating set below E(r) would not invalidate the vertex-centric viewpoint but would refine the quantitative bound.

**Open questions.** (1) Does the compression theorem of [3] imply that all braiding data compresses to vertex-anchored data in higher rank? (2) How do the missing branches of [9] interact with vertex-anchored braiding — do they correspond to forbidden fusion channels? (3) Can the fixed-point criterion of [4] be restated as a fusion-channel criterion at vertices, connecting the QNFO anyon models to supercuspidal representation theory via [10],[11]? (4) Do the sheaf functors of [7] restrict to an equivalence between vertex-supported coefficient systems in the sense of [8] and the QNFO fusion categories? (5) Can the tropical fans of [1],[6] be truncated so that the number of maximal cones equals V(r) for the corresponding ball?

## 7. Conclusion

We have answered "why vertices, not points?" for rank-one Bruhat–Tits buildings with exact arithmetic and explicit metric computation. The vertex set is the minimal G-stable skeleton meeting every chamber (17 vertices/16 edges in the p = 3, r = 2 ball; 53/52 at r = 3); it is the unique orbit whose stabilizer surjects onto the full finite group SL₂(𝔽_p) of order p(p²−1) = 24 at p = 3, providing p+1 = 4 fusion channels per vertex; generic points cost a stabilizer factor of p+1, collapse the finite layer to the Borel of order 6, and supply exactly one channel and no new braid generators. The displacement gap — non-vertex points moved by exactly twice their distance to the vertex set, with covering radius 1/2 — forces locally supported equivariant structures to concentrate at vertices. The pro-p Iwahori filtration index p²−1 = 8 quantifies the finite layer that anyon fusion and the Temperley–Lieb parameter require. Vertices are thus not a convention but the canonical anchoring set for discrete braiding on buildings; extending the exact arithmetic to higher rank is the natural next step.

## References

[1] A tropical view on Bruhat-Tits buildings and their compactifications. arXiv:1003.2966v1. https://arxiv.org/abs/1003.2966v1
[2] Group-theoretic compactification of Bruhat-Tits buildings. arXiv:math/0504291v1. https://arxiv.org/abs/math/0504291v1
[3] On compression of Bruhat-Tits buildings. arXiv:math/0410242v1. https://arxiv.org/abs/math/0410242v1
[4] Typical representations via fixed point sets in Bruhat--Tits buildings. arXiv:1909.05895v3. https://arxiv.org/abs/1909.05895v3
[5] Wonderful compactifications of Bruhat-Tits buildings in the non-split case. arXiv:2011.00349v1. https://arxiv.org/abs/2011.00349v1
[6] A tropical view on the Bruhat-Tits building of SL and its compactifications. arXiv:0905.3293v1. https://arxiv.org/abs/0905.3293v1
[7] Locally analytic representations and sheaves on the Bruhat-Tits building. arXiv:1201.3646v3. https://arxiv.org/abs/1201.3646v3
[8] Coefficient systems on the Bruhat-Tits building and pro-$p$ Iwahori-Hecke modules. arXiv:1802.10502v1. https://arxiv.org/abs/1802.10502v1
[9] On the missing branches of the Bruhat-Tits tree. arXiv:1712.01463v2. https://arxiv.org/abs/1712.01463v2
[10] On unitarity of some representatations of classical p-adic groups I. arXiv:1701.07658v2. https://arxiv.org/abs/1701.07658v2
[11] On unitarity of some representations of classical p-adic groups II. arXiv:1701.07662v2. https://arxiv.org/abs/1701.07662v2
[12] https://papers.qnfo.org/papers/p-adic-braid-groups-bruhat-tits/. QNFO: p-Adic Braid Groups on Bruhat-Tits Buildings.
[13] https://papers.qnfo.org/papers/p-adic-anyon-fusion-braiding/. QNFO: p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity, Verma Modules, and Ultrametric Anyon Models.
[14] https://papers.qnfo.org/papers/p-adic-temperley-lieb-parameter/. QNFO: The p-Adic Temperley-Lieb Parameter: Cyclotomic Units, Markov Traces, and the p-Adic Jones Polynomial.
