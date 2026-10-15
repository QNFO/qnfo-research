# Time as Bruhat-Tits Tree Depth: Discrete $p$-Adic Temporal Ordering and Tree-Geodesic Causality

## Abstract

We develop a conjectural but internally precise model in which physical time is not a continuous real parameter but a discrete depth coordinate on a Bruhat-Tits tree: an event is a vertex of a rooted $(p+1)$-regular tree, and its time is the integer depth $d\in\mathbb{N}$, identified conjecturally with the $p$-adic valuation $v_{p}(x)$. The gap addressed is that no existing framework derives quantization of time, partial temporal order, and acyclic causality from a single non-Archimedean geometric structure with exact, checkable combinatorics. Our approach is purely analytical: every consequence is an exact count on the rooted tree, derived with fully shown arithmetic and no simulation. Principal results, for the depth-$D$ ball with $p=2$, $D=10$: the ball contains $V_{10}=3070$ events; only $C_{10}=27651$ of the $\binom{3070}{2}=4710915$ pairs are temporally ordered, a fraction $f_{10}=27651/4710915\approx5.8696\times10^{-3}$, with asymptotic $f_{D}\sim 2(p-1)D/((p+1)p^{D})\to0$; the mean depth is $\bar{d}=27651/3070\approx9.0068$; the future cone of an event contains $(p^{\Delta+1}-p)/(p-1)$ events within $\Delta$ ticks ($62$ for $p=2$, $\Delta=5$; $363$ for $p=3$); and tree-geodesic causality admits no causal cycles by a strict-decrease argument on depth. In practice, the work gives quantum-gravity researchers a falsifiable, exactly solvable skeleton in which discreteness, partial order, and acyclicity are theorems of the proposed structure rather than assumptions, with continuum recovery stated only as a labeled projection.

## 1. Introduction

Physicists constructing a quantum theory of gravity face a concrete unresolved decision: what is the time variable of the theory? Quantum mechanics assumes a fixed external background time parameter to govern unitary evolution, while general relativity treats spacetime, including its time coordinate, as dynamical. Until the time variable is specified, a non-perturbative quantum theory of gravity cannot even enumerate its observables. The cost of the status quo is structural: every candidate theory must import a time continuum from calculus, and every such import re-creates the tension between a dynamical spacetime and a background clock. A derivation of the time variable from a discrete combinatorial structure would change this decision problem at its root: it would replace the choice of a continuum with the choice of a graph, whose consequences are theorems rather than postulates.

The continuum model of time — a real parameter $t\in\mathbb{R}$ with a total order — is inherited from calculus, not from measurement. We adopt, as an explicitly labeled modeling postulate, that no operational procedure resolves time below the Planck scale, and that the real line is therefore not forced as the temporal substrate; this postulate is not established here. This paper takes seriously an alternative suggested by non-Archimedean geometry: that time is a discrete depth coordinate on a Bruhat-Tits tree, the combinatorial tree on which $p$-adic valuation becomes literal distance.

A Bruhat-Tits tree is an infinite $(p+1)$-regular tree (a connected acyclic graph in which every vertex has exactly $p+1$ neighbors) associated with the $p$-adic field $\mathbb{Q}_{p}$; in the $p$-adic AdS/CFT literature it serves as the bulk geometry whose isometry is the conformal group of a CFT over $\mathbb{Q}_{p}$ [2]. The core conjecture is

$$t\;\leftrightarrow\;v_{p}(x),\qquad d(v)\in\mathbb{N},$$

where $v_{p}$ is the $p$-adic valuation on $\mathbb{Q}_{p}$ and $d(v)$ is the depth of the vertex $v$ representing an event, counted as the number of edges on the unique path from a distinguished root $v_{0}$. The root is the vertex of minimal depth and is provisionally identified with the Planck-scale origin of a causal history.

Three consequences are developed:

1. **Quantization.** Depth is integer-valued, so time comes in indivisible steps of a fundamental tick $t_{0}$; all measurable durations are integer multiples of $t_{0}$.
2. **Partial ordering.** Two vertices neither of which is an ancestor of the other have no intrinsic temporal relation. Temporal order is a partial order, not a total order.
3. **Tree-geodesic causality.** $A$ causes $B$ iff $A$ lies on the unique tree path from $B$ to the root. Because the tree is acyclic and every vertex has exactly one parent, this relation is automatically acyclic and antisymmetric.

The strong triangle inequality of the $p$-adic valuation, $|x+y|_{p}\leq\max\{|x|_{p},|y|_{p}\}$, whose ultrametric character is reviewed in [3], has as its combinatorial shadow the fact that tree distance between two events is determined by the depth of their most recent common ancestor — a fact with no Archimedean analogue.

We stress the epistemic status of the proposal: it is a conjecture. The contributions are:

- **(i)** A precise formalization of time as tree depth, with definitions of event, temporal order, tree-geodesic causality, and tree distance (Section 3).
- **(ii)** Exact combinatorial consequences derived with full arithmetic: the growth law $N_{d}=(p+1)p^{d-1}$, the ball size $V_{10}=3070$, the comparability count $C_{10}=27651$ and fraction $f_{10}\approx5.8696\times10^{-3}$ with the exact asymptotic constant, the mean depth $\bar{d}\approx9.0068$, future-cone counts $62$ and $363$, and a proof that causal cycles are impossible (Section 4, reported in Section 5).
- **(iii)** A mapping of the Bruhat-Tits-tree literature onto the questions the conjecture must answer, including the boundary-theoretic route by which a $p$-adic continuum emerges from tree bulk degrees of freedom (Section 2), and an explicit statement of who could use the result, at what readiness level, and what the smallest falsifying test is (Section 7).

No experiment is proposed that has been run, and no simulation is reported; the tree is exactly solvable, so closed-form statistics replace Monte Carlo.

## 2. Background and Related Work

We discuss eight works, each for a specific result its text states, and relate each to the tree-time conjecture.

**[1] On the missing branches of the Bruhat-Tits tree.** For a local field $k$ and the algebra $\mathfrak{A}=\mathbb{M}_{2}(k)$, this work computes the set $S(\Omega)$ of maximal orders containing a given order $\Omega$; this set is realized as a sub-tree of the Bruhat-Tits tree called the *branch* of the order, and branches have been used to study the selectivity problem and normalizers of Eichler orders [1]. The text also fixes graph conventions — full subgraphs, valency of a vertex — and works with a valuation $\nu:k^{*}\to\mathbb{Z}$ normalized by $\nu(\pi)=1$, so that one unit of valuation is one unit of tree distance [1]. Two points matter here. First, the normalization $\nu(\pi)=1$ is the precise mathematical precedent for identifying one valuation step with one edge, which is exactly our Definition 3.2. Second, the branch construction shows that sub-trees of the Bruhat-Tits tree selected by algebraic conditions are well-defined and computable; the causal past of an event in our model is precisely such a sub-tree (the set of ancestors), so [1] supplies the precedent that our central objects are mathematically legitimate.

**[2] Bending the Bruhat-Tits Tree II.** In the $p$-adic AdS/CFT correspondence, an $n$-dimensional CFT lives on $\mathbb{Q}_{p^{n}}$ and the dual bulk is the Bruhat-Tits tree, the analogue of pure AdS space; Witten diagrams on the tree satisfy the expected features of the $p$-adic CFT [2]. The work introduces coordinates on the tree in which the asymptotic boundary is the $\mathbb{Q}_{p}$ line and the "radial coordinate" encodes the accuracy to which the boundary coordinate is defined [2]. Its conclusion demonstrates that a BTZ-type black hole connection can be transplanted to a $\mathrm{PGL}(2,\mathbb{Q}_{p})$ connection, that the resulting Wilson-line expectation values relate to a $p$-adic CFT at finite temperature, and that this black-hole background is related to the pure tree by a local diffeomorphism reflecting a non-trivial Weyl transformation [2]. This is the strongest existing precedent that gravitational-type causal infrastructure — horizons, connections, thermal states — lives consistently on tree geometry, which any tree-time model must eventually reproduce.

**[3] Phase transitions for the $p$-adic Potts model on a Cayley tree.** This paper studies the three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p=3$ for any nonzero interaction; for $p\neq3$ the Gibbs measure is unique [3]. The text also reviews the $p$-adic norm $|x|_{p}=p^{-r}$ and its strong triangle inequality, the defining ultrametric property our distance formula exploits [3]. For us, [3] establishes two things: that ensemble statistics on regular trees is mathematically mature, with exact criteria rather than approximations; and that specific primes can be dynamically distinguished — here $p=3$ — a hint, though for a Potts system and not for temporal ordering, that the free prime of our model may not remain free in a dynamical extension.

**[4] Mumford dendrograms and discrete $p$-adic symmetries.** This work encodes dendrograms — trees arising in hierarchical classification of data — by embedding them into Bruhat-Tits trees of $p$-adic fields, shows that any dendrogram can be viewed as a subtree of the Bruhat-Tits tree for $\mathrm{PGL}_{2}(K)$ over a field $K$ chosen large enough to capture the maximal number of children, without changing the prime $p$, and proves that the dendrogram is uniquely determined by a suitable $p$-adic encoding, with the $p$-adic distance coinciding with the Baire distance for strings [4]. This is a representational completeness result of direct use: arbitrary hierarchical partial orders of the kind our model assigns to event sets embed faithfully into Bruhat-Tits trees.

**[5] $p$-adic colligations and 'rational maps' of Bruhat-Tits trees.** This work considers matrices of order $k+N$ over a $p$-adic field up to conjugation by $\mathrm{GL}$ over the $p$-adic integers, defines a product of such conjugacy classes, constructs analogues of characteristic (transfer) functions as maps from Bruhat-Tits trees to Bruhat-Tits buildings, and proves, for the case $\alpha=1$, that the semigroup $[\mathrm{Coll}_{\infty}(1)]$ is commutative [5]. The tree-to-building transfer maps are the natural language for composing local tree structure into larger geometries; if the single-trunk tree-time model must be upgraded to a building to recover spatial degrees of freedom (Section 6), [5] is the existing mathematical machinery for that upgrade.

**[6] Boundary theory of a spinor field theory on the Bruhat-Tits tree.** For a spinor field theory on the tree $\mathrm{T}_{p}$, this work calculates the action and partition function of the boundary theory by integrating out the interior of the tree, following the scalar-field method of taking a cut-off boundary $E_{R}$ and the limit $R\to+\infty$, in which the boundary becomes $\mathbb{Q}_{p}$ [6]. The findings state that although the bulk kinetic term has spinor form, the boundary kinetic term takes the scalar-like form $\varphi^{*}D^{2\Delta-1}\varphi$, and that the factor $p^{\Delta}-p^{1-\Delta}$ appears throughout, with its zero point corresponding to the BF bound [6]. This is the closest existing result to our continuum-recovery question: bulk tree degrees of freedom integrate out to a boundary theory on $\mathbb{Q}_{p}$, i.e., a $p$-adic continuum emerges from the tree in a controlled field-theoretic sense. Our Projection P1 (Section 4.9) adopts exactly this mechanism as a hypothesis for the time coordinate.

**[7] Effective field theories on subspaces of the Bruhat-Tits tree.** For a free massless scalar field on $\mathrm{T}_{p}$, this work calculates effective actions on two subspaces $\Sigma_{1N}$ and $\Sigma_{2N}$ and finds that their limits, as the subspaces are taken to the boundary ($N\to+\infty$), are the same conformal field theory over $\mathbb{Q}_{p}$ [7]. The text motivates the study of physics over $\mathbb{Q}_{p}$ by two points: the possibility that spacetime is non-Archimedean at small scales, and the number-field invariance principle [7]. This reinforces [6] from a second direction: different tree subspaces yield the same boundary conformal field theory, suggesting a robustness of the tree-to-$\mathbb{Q}_{p}$ limit that a tree-time model would want to exploit — the observable content of time may live at the boundary, where the exponential bulk is projected out.

**[8] $p$-adic equiangular lines and the $p$-adic van Lint-Seidel bound.** This work introduces $p$-adic equiangular lines in $p$-adic Hilbert spaces — defined by an inner product satisfying the non-Archimedean analogues of the usual axioms — and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_{j}\}_{j=1}^{n}$ is a set of $p$-adic $\gamma$-equiangular lines in $\mathbb{Q}_{p}^{d}$, then $|n|^{2}\leq|d|\max\{|n|,\gamma^{2}\}$, the $p$-adic van Lint-Seidel relative bound [8]. This shows that $p$-adic magnitude arithmetic supports packing bounds parallel to the Archimedean ones; in a tree-time model, such bounds would constrain how many mutually distinguishable branch directions can coexist at a given angular scale, a constraint relevant if the model is extended with internal state spaces.

## 3. Methods

### 3.1 Definitions

**Definition 3.1 (Event).** An *event* is a vertex $v$ of the Bruhat-Tits tree $\mathcal{T}_{p}$, a $(p+1)$-regular tree with a distinguished root $v_{0}$.

**Definition 3.2 (Time).** The *time* of an event $v$ is its depth $d(v)\in\mathbb{N}$, the number of edges on the unique path from $v_{0}$ to $v$. Under the conjectured identification, $d(v)$ corresponds to the $p$-adic valuation of the associated coordinate — the same normalization $\nu(\pi)=1$ that [1] uses to make one valuation step one unit of distance — and we set $t(v)=d(v)\,t_{0}$ with fundamental tick $t_{0}$.

**Definition 3.3 (Temporal order).** For events $A,B$, we write $A\prec B$ iff $A$ lies on the unique path from $B$ to the root (proper ancestor). If neither $A\prec B$ nor $B\prec A$, we write $A\parallel B$ (incomparable).

**Definition 3.4 (Tree-geodesic causality).** $A$ causes $B$ iff $A\prec B$. Causality coincides with ancestry on the tree.

**Definition 3.5 (Tree distance).** The graph distance $\delta(A,B)$ is the number of edges on the unique path between $A$ and $B$; with least common ancestor $w$ at depth $d_{w}$,

$$\delta(A,B)=d(A)+d(B)-2d_{w}.$$

This formula is the combinatorial shadow of the ultrametric inequality reviewed in [3]: the distance is governed entirely by the most recent common ancestor.

### 3.2 Method of analysis

All results are obtained by exact combinatorial enumeration on the rooted $(p+1)$-regular tree. Induction on depth and direct summation of geometric series are the only tools; no simulation is performed. The only free parameters are the prime $p$ and the depth cutoff $D$ used for finite-horizon calculations. Every input number in Section 4 is either a structural constant of the model (the regularity $p+1$) or an explicit modeling choice ($D$). Continuum-recovery statements are labeled as explicit projections (Section 4.9).

## 4. Analysis

### 4.1 Vertex counts by depth

**Claim 4.1.** The number of vertices at depth $d$ is

$$N_{d}=(p+1)\,p^{d-1}\quad\text{for }d\geq1,\qquad N_{0}=1.$$

*Derivation.* The root $v_{0}$ has $p+1$ neighbours, so $N_{1}=p+1$. Each vertex at depth $d-1$ has $p$ children (all neighbours except its parent), giving the recurrence $N_{d}=p\,N_{d-1}$. Solving by induction: $N_{d}=p\,N_{d-1}=p^{2}N_{d-2}=\cdots=p^{d-1}N_{1}=(p+1)p^{d-1}$. $\blacksquare$

*Worked instance ($p=2$).* $N_{1}=3$, $N_{2}=6$, $N_{3}=12$, $N_{4}=24$, $N_{5}=48$, $N_{6}=96$, $N_{7}=192$, $N_{8}=384$, $N_{9}=768$, $N_{10}=1536$.

### 4.2 Total vertices up to depth $D$

**Claim 4.2.** The total number of vertices with $d(v)\leq D$ is

$$V_{D}=1+\sum_{d=1}^{D}(p+1)p^{d-1}=1+(p+1)\,\frac{p^{D}-1}{p-1}.$$

*Derivation.* Sum the geometric series $\sum_{d=1}^{D}p^{d-1}=\frac{p^{D}-1}{p-1}$, multiply by $p+1$, and add the root. $\blacksquare$

*Worked instance ($p=2$, $D=10$).*

$$V_{10}=1+3\,(2^{10}-1)=1+3\cdot1023=3070.$$

Direct summation of the $N_{d}$ from Section 4.1 gives $3+6+12+24+48+96+192+384+768+1536=3070$, confirming the closed form by two independent routes.

### 4.3 Comparable pairs between two depths

**Claim 4.3.** For depths $d_{1}<d_{2}$, the number of unordered comparable pairs $\{A,B\}$ with $d(A)=d_{1}$, $d(B)=d_{2}$ equals $N_{d_{2}}$, independent of $d_{1}$.

*Derivation.* Each vertex at depth $d_{1}$ has exactly $p^{d_{2}-d_{1}}$ descendants at depth $d_{2}$. Hence

$$N_{d_{1}}\cdot p^{d_{2}-d_{1}}=(p+1)p^{d_{1}-1}\,p^{d_{2}-d_{1}}=(p+1)p^{d_{2}-1}=N_{d_{2}}.$$

$\blacksquare$

### 4.4 Total comparable pairs up to depth $D$

**Claim 4.4.** The total number of unordered comparable pairs among vertices of depth $\leq D$ is

$$C_{D}=\sum_{d=1}^{D}d\,N_{d}=(p+1)\sum_{d=1}^{D}d\,p^{d-1}.$$

*Derivation.* A vertex at depth $d$ has exactly $d$ proper ancestors, contributing $d$ comparable pairs as the deeper member. Summing over all vertices yields the claim. $\blacksquare$

*Closed form (general $p$).* The standard finite sum is

$$\sum_{d=1}^{D}d\,p^{d-1}=\frac{D\,p^{D+1}-(D+1)p^{D}+1}{(p-1)^{2}},$$

so

$$C_{D}=(p+1)\,\frac{D\,p^{D+1}-(D+1)p^{D}+1}{(p-1)^{2}}.$$

*Worked instance ($p=2$, $D=10$).* The numerator is $10\cdot2^{11}-11\cdot2^{10}+1=20480-11264+1=9217$, and $(p-1)^{2}=1$, so

$$C_{10}=3\cdot9217=27651.$$

Cross-check by the recursion $S_{D}=\sum_{d=1}^{D}d\,2^{d-1}$: induction gives $S_{D}=(D-1)2^{D}+1$, so $S_{10}=9\cdot1024+1=9217$, and $C_{10}=3\cdot9217=27651$. Both routes agree.

### 4.5 Fraction of comparable pairs and its asymptotics

**Claim 4.5.** For $p=2$, $D=10$,

$$f_{10}=\frac{C_{10}}{\binom{V_{10}}{2}}.$$

*Derivation.* $\binom{3070}{2}=\frac{3070\cdot3069}{2}=4710915$. Hence

$$f_{10}=\frac{27651}{4710915}\approx5.8696\times10^{-3}.$$

*Asymptotic constant (general $p$).* For large $D$, $V_{D}=1+(p+1)\frac{p^{D}-1}{p-1}\approx\frac{p+1}{p-1}p^{D}$, so

$$\binom{V_{D}}{2}\approx\frac{1}{2}\left(\frac{p+1}{p-1}p^{D}\right)^{2}=\frac{(p+1)^{2}p^{2D}}{2(p-1)^{2}}.$$

$$C_D \approx \frac{p+1}{p-1}\,D\,p^{D},$$

since the sum $\sum_{d=1}^{D} d\,p^{d-1}$ is dominated by its last terms. Therefore

$$f_D \approx \frac{\dfrac{p+1}{p-1}D p^{D}}{\dfrac{(p+1)^{2}p^{2D}}{2(p-1)^{2}}} = \frac{2(p-1)\,D}{(p+1)\,p^{D}} \longrightarrow 0.$$

*Worked instance ($p=2$, $D=10$).* The asymptotic formula gives $f_{10} \approx 2\cdot1\cdot10/(3\cdot1024) = 20/3072 \approx 6.5104\times10^{-3}$, against the exact $f_{10} = 27651/4710915 \approx 5.8696\times10^{-3}$ computed above; the asymptotic form overestimates by a factor $6.5104/5.8696 \approx 1.109$ at $D=10$, as expected for a large-$D$ approximation used slightly below its asymptotic regime. The qualitative content is exact in both routes: $f_D \to 0$ faster than any power, because $p^{D}$ grows exponentially in $D$ while $D$ grows linearly. Temporal comparability is exponentially rare in depth; almost all pairs of events in this model are unordered. This is the quantitative content of the statement that time is only partially ordered.

### 4.6 Mean depth

**Claim 4.6.** Under the uniform distribution on the depth-$D$ ball, the mean depth is

$$\bar{d} = \frac{\sum_{d=0}^{D} d\,N_d}{V_D} = \frac{C_D}{V_D}.$$

*Derivation.* The numerator $\sum_{d=0}^{D} d\,N_d = \sum_{d=1}^{D} d\,(p+1)p^{d-1} = C_D$ is exactly the sum computed in Claim 4.4, since $N_0 = 1$ contributes $0\cdot1 = 0$. The denominator is $V_D$ from Claim 4.2. $\blacksquare$

*Worked instance ($p=2$, $D=10$).*

$$\bar{d} = \frac{27651}{3070} \approx 9.0068.$$

The mean sits within roughly $10\%$ of the cutoff $D=10$. The gap is

$$\frac{D - \bar{d}}{D} = \frac{10 - 27651/3070}{10} = \frac{10 - 9.0068}{10} = \frac{0.9932}{10} \approx 9.932\%.$$

The reason is that the outermost shell dominates the ball: $N_{10} = 1536$ of the $3070$ vertices lie at maximal depth, a fraction $1536/3070 \approx 0.50033$. A testable structural consequence follows: a uniform-on-ball event distribution has an exponentially growing depth histogram $N_d = (p+1)p^{d-1}$, not a flat or polynomial one.

### 4.7 Acyclicity of tree-geodesic causality

**Claim 4.7.** The causality relation of Definition 3.4 admits no causal cycles.

*Derivation.* Suppose a closed chain $A_1 \to A_2 \to \cdots \to A_k \to A_1$ with $A_{i+1} \prec A_i$ for each $i$. By Definition 3.3, $A_{i+1} \prec A_i$ means $A_{i+1}$ is a proper ancestor of $A_i$, and a proper ancestor has strictly smaller depth. Hence

$$d(A_1) > d(A_2) > \cdots > d(A_k) > d(A_1),$$

which is impossible for integers. Equivalently, transitivity of ancestry would force $A_1 \prec A_1$, contradicting irreflexivity: a vertex is not a proper ancestor of itself, because the unique path from a vertex to the root has length $d(v) \geq 0$ and contains the vertex itself only as the endpoint, never as a proper ancestor. $\blacksquare$

This addresses the closed-timelike-curve concern at the kinematic level. Going back in time would require revisiting an ancestor, but every vertex has exactly one parent, so no alternative route to any ancestor exists; the causal graph is a sub-forest of a tree and is acyclic by construction.

### 4.8 Future-cone size

**Claim 4.8.** The future of an event $u$ at depth $d$ consists of its descendants. Within $\Delta$ additional ticks (depths $d+1$ through $d+\Delta$), their number is

$$C(\Delta) = \sum_{k=1}^{\Delta} p^{k} = \frac{p^{\Delta+1} - p}{p-1}.$$

*Derivation.* At depth $d+k$ relative to $u$, the number of descendants is $p^{k}$ (each descendant at relative depth $k-1$ has $p$ children). Summing the geometric series gives the closed form. $\blacksquare$

*Worked instances.* For $p=2$, $\Delta=5$: $C(5) = 2+4+8+16+32 = 62$, and $(2^{6}-2)/(2-1) = 62$. For $p=3$, $\Delta=5$: $C(5) = 3+9+27+81+243 = 363$, and $(3^{6}-3)/2 = (729-3)/2 = 363$.

The past cone contrasts sharply: the past of an event at depth $d$ is the chain of its $d$ proper ancestors, linearly ordered among themselves. In a $1+1$-dimensional continuum light cone with unit lattice spacing, the number of future lattice points grows quadratically, $\sim \Delta^{2}/2$, whereas the tree future cone grows exponentially, $p^{\Delta}$. The structural mismatch with the relativistic light cone — whose past is a solid cone with a continuum of directions, whereas the tree past is a finite chain — is discussed in Section 6; we do not claim recovery.

### 4.9 Continuum limit (labeled projection)

**Projection P1, with stated assumptions.** Assume (i) the physical tick is $t_0$ and observable durations $T$ correspond to depth $D = T/t_0$; (ii) the number of distinguishable events at resolution $t_0$ in an interval $T$ is $V_D$. Then, using Claim 4.2,

$$V_D \approx \frac{p+1}{p-1}\,p^{D} = \frac{p+1}{p-1}\,p^{T/t_0},$$

i.e., exponential growth in $T/t_0$. For this to match continuum-like polynomial scaling, either $t_0$ must run (a dynamical tick) or the observable must be a boundary quantity. The results of [6] and [7], in which integrating out the tree interior yields a $p$-adic boundary theory on $\mathbb{Q}_p$, suggest that continuum-relevant observables live at the tree boundary, where the exponential bulk is projected out. **Uncertainty:** this is a structural projection, not a measurement; its validity hinges on assumption (ii), and no numerical value of $t_0$ is asserted, because no input in this paper fixes the physical scale of one depth step.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are measured or simulated.

**R1 (Vertex growth).** The number of events at time-step $d$ is $N_d = (p+1)p^{d-1}$ (Claim 4.1). For $p=2$: $N_1 = 3$, $N_{10} = 1536$.

**R2 (Event budget).** For $p=2$, $D=10$: $V_{10} = 3070$ (Claim 4.2, verified by two independent summations).

**R3 (Comparability scarcity).** For $p=2$, $D=10$: $C_{10} = 27651$ ordered pairs out of $\binom{3070}{2} = 4710915$ total pairs, a fraction $f_{10} = 27651/4710915 \approx 5.8696\times10^{-3}$ (Claims 4.4–4.5). Asymptotically $f_D \sim 2(p-1)D/((p+1)p^{D}) \to 0$: almost all pairs of events are temporally incomparable.

**R4 (Depth-independence).** The number of ordered pairs between depth $d_1$ and depth $d_2 > d_1$ is $N_{d_2}$, independent of $d_1$ (Claim 4.3) — an exact ultrametric signature.

**R5 (Temporal statistics).** Mean depth $\bar{d} = 27651/3070 \approx 9.0068$; the depth histogram is exactly $N_d = (p+1)p^{d-1}$, exponentially growing, with the outermost shell holding $1536/3070 \approx 50.03\%$ of the ball at $D=10$.

**R6 (No causal cycles).** Tree-geodesic causality is a strict partial order; causal cycles, including closed-timelike-curve analogues, are impossible by construction (Claim 4.7).

**R7 (Future-cone counts).** $C(\Delta) = (p^{\Delta+1}-p)/(p-1)$; for $p=2$, $\Delta=5$: $C=62$; for $p=3$, $\Delta=5$: $C=363$. The past cone of an event at depth $d$ contains exactly $d$ events, linearly ordered.

**R8 (Distance formula).** $\delta(A,B) = d(A) + d(B) - 2d_w$, where $d_w$ is the depth of the least common ancestor (Definition 3.5).

**Projection P1 (not a result).** Under assumptions (i)–(ii) of Section 4.9, event count scales as $V_D \approx \frac{p+1}{p-1}p^{T/t_0}$; recovery of continuum statistics is not established here and is delegated to the boundary-theory mechanism of [6] and [7] as a hypothesis.

**Projection P2 (not a result).** If the root corresponds to the Planck scale and one depth step to one Planck time, a horizon of $D$ steps spans $D$ Planck times. This conversion is an assumption, not a derivation, since no input in this paper fixes the physical scale of one depth step.

## 6. Discussion

**Limitations.** The model as constructed is a kinematic skeleton: it fixes ordering and counting but assigns no dynamics. The identification $t \leftrightarrow v_p(x)$ is a conjecture, not a derivation; nothing in the combinatorics above forces the root to be a cosmological origin or one depth step to be a Planck time (Projection P2 is explicitly assumption-laden). The prime $p$ is a free parameter with no observed value; the $p=3$ phase-transition threshold found in the Potts analysis [3] is the only hint in the works surveyed here that specific primes may be dynamically distinguished, and that result concerns a Potts system on a Cayley tree, not temporal ordering. The model also has no spatial degrees of freedom: the light-cone question is answered only in the limited sense of cone counting (Section 4.8), not by a derivation of relativistic light-cone structure.

**Failure modes.** The most serious structural mismatch is with relativity. In special relativity, the causal past of an event is a solid cone — a continuum of directions — and ordering is partial but dense along every timelike curve. In the tree model, the causal past of an event is a finite chain of $d$ ancestors: linear, not conical, and totally ordered internally. The scarcity result R3 is cone-like in spirit (most pairs unordered), but the shape of the past is a chain, not a cone. If empirical causal structure requires a continuum of causal directions at every event, the single-trunk tree model fails, and one would need either a product structure (tree $\times$ internal degrees of freedom) or a building rather than a tree — the direction suggested by the tree-to-building transfer maps of [5], which construct maps from Bruhat-Tits trees to Bruhat-Tits buildings but were not developed there for causal structure.

A second failure mode is dynamical: the model says nothing about which events exist or how probabilities are assigned over the tree. The $p$-adic Gibbs-measure machinery of [3] shows that ensemble statistics on regular trees can be solved exactly, but importing it would require a Hamiltonian or constraint, which this paper does not supply. A third is observational: the depth histogram R5 is a prediction only under the uniform-on-ball sampling assumption; a different natural measure on the tree (for example, one weighted toward a single branch) changes the histogram while leaving the ordering structure intact.

**What would falsify the main result.** The central structural claims are quantization, partial order, and acyclicity. The single observation that would falsify the acyclicity claim is an empirically demonstrated closed causal chain with genuine information flow: Claim 4.7 forbids cycles by a strict-decrease argument on depth, so one confirmed cycle refutes the identification of causality with ancestry. Falsifiers for the other claims: (i) two events incomparable under Definition 3.3 shown to have an intrinsic, empirically accessible temporal order (not a convention or clock-synchronization artifact) would refute the partial-order claim; (ii) an operational time measurement resolving intervals finer than a single tick $t_0$, with $t_0$ fixed by the model, would refute quantization; (iii) a measured flat or polynomial event-depth histogram under the stated sampling would refute the tree structure or the sampling assumption; (iv) an empirically quadratic future-cone growth law $\sim \Delta^{2}/2$ at the finest resolvable scale would refute the tree-geodesic cone structure, since the tree predicts exponential growth $C(\Delta) = (p^{\Delta+1}-p)/(p-1)$.

**Limitations list.** The result rests on the following assumptions, each with a distinct sensitivity:

- *The core conjecture $t \leftrightarrow v_p(x)$.* The entire paper is conditional on it; no derivation is given, and the result is exactly as strong as this conjecture.
- *The root identification.* Associating the root with a Planck-scale origin is a labeled assumption (Projection P2); the combinatorics are indifferent to it.
- *The prime $p$.* Free and unfixed; all counts scale with $p$, and the cone counts $62$ versus $363$ at $\Delta=5$ differ by a factor $\approx 5.85$, so the choice of $p$ is empirically consequential if any of these counts becomes observable.
- *Uniform-on-ball sampling.* The mean depth $\bar{d} \approx 9.0068$ and the depth-histogram prediction hold only under this measure; the ordering structure (R3, R4, R6) holds for any measure.
- *No dynamics, no space.* The model is a kinematic skeleton; every dynamical or spatial claim is outside its scope.
- *Continuum recovery.* Rests entirely on Projection P1 and the boundary mechanism of [6] and [7]; it is a hypothesis, not a result.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The intended users are researchers in quantum gravity and in discrete/causal-set approaches to spacetime. If the conjecture holds, the decision that changes is the choice of the time variable itself: instead of postulating a continuum $\mathbb{R}$ and then fighting to remove it, one postulates a rooted $(p+1)$-regular tree and obtains quantization, partial order, and acyclicity as theorems (Claims 4.1, 4.3–4.5, 4.7). Concretely, a researcher building a spin-foam, causal-set, or $p$-adic AdS/CFT model could adopt tree depth as the time coordinate and inherit the exact counting laws R1–R8 as consistency checks on any dynamics added on top. No experimentalist, engineer, or policy maker can act on this result today; the work is foundational, and its value is that it converts three postulates into three theorems of a specified structure, which is the precondition for any later empirical program.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: it is purely analytical, unreviewed, and describes the basic properties of a proposed structure and their exact combinatorial consequences. Analytical work never exceeds TRL 3, and nothing here approaches it: no physical system has been identified whose behavior the tree-time model describes, no $t_0$ has been fixed, and no measurement protocol exists.

**(c) The smallest next test.** The smallest de-risking calculation is not an experiment but a derivation: extend the exactly solvable skeleton with the simplest nontrivial dynamics — for example, a free scalar field on $\mathcal{T}_p$ as in [7] — and check whether the boundary two-point functions, when reinterpreted as temporal correlators, reproduce any standard temporal statistic (a decaying correlator, a well-defined spectral density). The outcome that refutes the pathway is a boundary theory whose correlators are incompatible with any probabilistic temporal interpretation (for instance, no well-defined limit as the cutoff is removed). A second, cheaper check is combinatorial: verify the counts $V_{10} = 3070$, $C_{10} = 27651$, and $C(5) = 62, 363$ by direct enumeration on a computer for $p \in \{2,3\}$; any mismatch with the closed forms of Section 4 would falsify the derivations.

**(d) Binding constraints.** For the mathematical program itself, the binding constraint is conceptual, not material: the chain-versus-cone mismatch of Section 6 must be resolved before any physics can be built, and the candidate resolutions (product with internal degrees of freedom, or a building as in the tree-to-building maps of [5]) each require new mathematics that does not yet exist in the literature surveyed here. For any eventual empirical program, the binding constraint is the absence of a fixed $t_0$: without an independent determination of the tick, none of the counts R1–R8 maps to an observable number. Data and compute constraints are absent at this stage because the model is exactly solvable; no simulation is needed for anything derived here.

**(e) Order-of-magnitude bounds (projections).** Under Projection P2's assumptions (root at the Planck scale, one depth step = one Planck time), a depth-$D$ ball contains $V_D \approx \frac{p+1}{p-1}p^{D}$ events. For $p=2$ and $D$ corresponding to $10^{-23}$ s (about $10^{20}$ Planck times), this is $V_D \approx 3\cdot2^{10^{20}}$, a number with roughly $10^{20}\log_{10}2 \approx 3.01\times10^{19}$ decimal digits. This projection is stated only to show that bulk event counts are physically unmanageable at macroscopic durations, which is the motivation for the boundary mechanism of Projection P1; its assumptions are those of P2 and are not established.

**(f) Risks and misuse paths.** The main misuse is rhetorical: the exactness of the combinatorics can be mistaken for empirical support of the conjecture. Every number in this paper is a theorem about a proposed structure, not evidence about nature; the conjecture $t \leftrightarrow v_p(x)$ has no experimental basis in this work. A secondary risk is overclaiming the acyclicity result: Claim 4.7 shows that a specific proposed causal relation is acyclic by construction, which is a consistency property of the proposal, not a prediction that closed causal chains are impossible in nature.

## 8. Conclusion

We have formalized a conjectural model in which time is the depth coordinate $d(v) \in \mathbb{N}$ on a rooted $(p+1)$-regular Bruhat-Tits tree, conjecturally identified with the $p$-adic valuation $v_p(x)$. The model's virtues are that discreteness (integer ticks $t_0$), partial temporal ordering (ancestry on the tree, with incomparability across branches), and acyclicity of causality (Claim 4.7) are theorems of the structure rather than added assumptions. The exact combinatorial consequences computed here — $V_{10} = 3070$ events in the depth-$10$ ball for $p=2$, $C_{10} = 27651$ ordered pairs out of $\binom{3070}{2} = 4710915$, a comparability fraction $f_{10} = 27651/4710915 \approx 5.8696\times10^{-3}$ with asymptotics $f_D \sim 2(p-1)D/((p+1)p^{D}) \to 0$, mean depth $\bar{d} = 27651/3070 \approx 9.0068$, and future-cone counts $C(5) = 62$ ($p=2$) and $363$ ($p=3$) — are all derived with shown arithmetic and require no simulation.

The model's central weakness, argued in Section 6, is the mismatch between the chain-shaped tree past and the cone-shaped relativistic past; the boundary-theoretic route of [6] and [7], by which a $p$-adic continuum emerges from tree bulk degrees of freedom, is adopted only as Projection P1, an explicitly labeled hypothesis. The prime $p$ is unfixed, the root-to-Planck-scale identification (Projection P2) is an assumption, and the falsification criteria of Section 6 make the proposal empirically exposed rather than insulated. The contribution is precision about a conjecture: the tree-time skeleton is exactly solvable, and its predictions are stated in a form that observation can attack.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 14 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the missing branches of the Bruhat-Tits tree. arXiv:1712.01463v2. https://arxiv.org/abs/1712.01463v2
[2] Bending the Bruhat-Tits Tree II: the p-adic BTZ Black hole and Local Diffeomorphism on the Bruhat-Tits Tree. arXiv:2102.12024v2. https://arxiv.org/abs/2102.12024v2
[3] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[4] Mumford dendrograms and discrete p-adic symmetries. arXiv:0809.1570v1. https://arxiv.org/abs/0809.1570v1
[5] On $p$-adic colligations and 'rational maps' of Bruhat-Tits trees. arXiv:1301.5453v1. https://arxiv.org/abs/1301.5453v1
[6] The boundary theory of a spinor field theory on the Bruhat-Tits tree. arXiv:1910.09397v2. https://arxiv.org/abs/1910.09397v2
[7] Effective field theories on subspaces of the Bruhat-Tits tree. arXiv:2402.03730v2. https://arxiv.org/abs/2402.03730v2
[8] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
