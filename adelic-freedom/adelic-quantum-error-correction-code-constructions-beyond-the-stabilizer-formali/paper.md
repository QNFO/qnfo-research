# Adelic Quantum Error Correction: Code Constructions Beyond the Stabilizer Formalism

## Abstract

Heydeman, Marcolli, Parikh, and Saberi (2018) demonstrated that holographic quantum error-correcting codes can be constructed on a single $p$-adic Bruhat-Tits tree using perfect tensor networks. This paper extends their result to the **adelic setting**: the simultaneous use of ALL $p$-adic completions via the ring of adeles $\mathbb{A}_{\mathbb{Q}}$. We define adelic quantum error-correcting codes as codes constructed on the adelic product of Bruhat-Tits trees $\prod_p \mathrm{BT}_p$, and we ask: can such codes exhibit properties NOT accessible through the standard CSS/stabilizer formalism? We present two candidate mechanisms for genuine novelty — (1) $p$-varying code distance enabling protection against errors that manifest differently at different primes, and (2) adelic tensor network codes whose logical operators span multiple $p$-adic geometries simultaneously — and we identify the mathematical obstacles to proving that these mechanisms produce genuinely non-stabilizer codes. The adelic setting raises connections to class field theory (via the adelic reciprocity map), the Langlands program (via automorphic representations on $\mathrm{PGL}(2,\mathbb{A}_{\mathbb{Q}})$), and $p$-adic holography. We do not claim to have constructed a provably non-stabilizer adelic QEC code; rather, we define the problem, establish the mathematical framework, and identify the specific constructions whose non-stabilizer status remains to be proven or refuted.

## 1. Introduction

### 1.1 The Single-$p$ Baseline

The starting point is Heydeman et al. (2018) [1], who construct holographic quantum error-correcting codes from perfect tensors arranged on the Bruhat-Tits tree $\mathrm{BT}_p$ of $\mathrm{PGL}(2,\mathbb{Q}_p)$. The $\mathrm{BT}_p$ tree is a $(p+1)$-regular infinite tree whose boundary is the $p$-adic projective line $\mathbb{P}^1(\mathbb{Q}_p)$. Their key result: perfect tensor networks on $\mathrm{BT}_p$ yield holographic states satisfying a $p$-adic Ryu-Takayanagi formula, with the tree geometry encoding the entanglement structure [established].

The construction uses a single prime $p$. But the $p$-adic numbers for different primes $p$ are different geometries — different branching factors $(p+1)$, different valuation structures, different completions of $\mathbb{Q}$. What happens when we combine ALL of them?

### 1.2 The Adelic Idea

The ring of adeles $\mathbb{A}_{\mathbb{Q}}$ is the restricted product of all $p$-adic completions $\mathbb{Q}_p$ together with the real completion $\mathbb{R}$:

$$\mathbb{A}_{\mathbb{Q}} = \left\{(x_p) \in \prod_p \mathbb{Q}_p : x_p \in \mathbb{Z}_p \text{ for all but finitely many } p\right\}$$

The adelic approach has been powerful in number theory — it is the natural setting for class field theory, automorphic forms, and the Langlands program [established]. Applying it to quantum error correction means: construct codes on the adelic product of Bruhat-Tits trees $\prod_p \mathrm{BT}_p$, where a logical qubit is encoded simultaneously across ALL $p$-adic geometries.

### 1.3 The Central Question

**Can adelic QEC produce code constructions not accessible through the standard CSS/stabilizer formalism?** [my conjecture — to be verified or refuted by the construction program outlined here]

The CSS (Calderbank-Shor-Steane) construction and its generalization to stabilizer codes [2, 3] encompass all known quantum error-correcting codes used in practice, including surface codes, color codes, and their generalizations. The question is whether the adelic product introduces genuinely new structure or re-expresses known codes in adelic language.

### 1.4 Structure of This Paper

Section 2 reviews the single-$p$ construction of Heydeman et al. Section 3 defines the adelic generalization. Section 4 presents two candidate mechanisms for non-stabilizer codes. Section 5 identifies proof obligations. Section 6 discusses connections to number theory. Section 7 concludes with the research program.

---

## 2. Single-$p$ QEC on Bruhat-Tits Trees (Review)

### 2.1 The Bruhat-Tits Tree

For a prime $p$, the Bruhat-Tits tree $\mathrm{BT}_p$ of $\mathrm{PGL}(2,\mathbb{Q}_p)$ is a $(p+1)$-regular infinite tree. Vertices correspond to homothety classes of lattices in $\mathbb{Q}_p^2$. The tree is the discrete analog of hyperbolic 3-space $\mathbb{H}^3$ [4]. Its boundary $\partial \mathrm{BT}_p \cong \mathbb{P}^1(\mathbb{Q}_p)$ is the $p$-adic projective line [established].

### 2.2 Perfect Tensor Codes

A perfect tensor $T_{a_1 \ldots a_n}$ is an $n$-index tensor such that for any bipartition of the indices into $k$ and $n-k$ legs, with $k \leq n/2$, the tensor defines an isometry from the $k$ legs to the $n-k$ legs. Perfect tensors are the building blocks of holographic codes [1, 5].

On $\mathrm{BT}_p$, Heydeman et al. arrange perfect tensors at vertices, with legs connecting along edges of the tree. A subset of legs at the boundary encodes logical qubits; the bulk legs correspond to physical qubits. The error correction property emerges from the holographic structure: errors at the boundary are correctable because the logical information lives deep in the bulk.

### 2.3 Key Properties

For a single-$p$ Bruhat-Tits tree code with perfect tensors of bond dimension $D$:

- Code distance: determined by the graph distance between boundary points on the tree [1].
- Encoding rate: determined by the ratio of bulk to boundary legs [1].
- Entanglement wedge reconstruction: boundary subregions reconstruct bulk operators in their entanglement wedge [established, holographic principle].
- Error set: local errors at the boundary (defined by the AdS/CFT UV-IR relation) are correctable.

---

## 3. The Adelic Generalization

### 3.1 The Adelic Product of Trees

Define the adelic Bruhat-Tits tree as the product:

$$\mathrm{BT}_{\mathbb{A}} = \prod_p \mathrm{BT}_p$$

This is NOT a tree — it is a product of trees, each with different branching factor $(p+1)$. The boundary is:

$$\partial \mathrm{BT}_{\mathbb{A}} = \prod_p \mathbb{P}^1(\mathbb{Q}_p)$$

A point on the adelic boundary is a sequence $(x_p)$, one coordinate for each prime $p$, with $x_p \in \mathbb{P}^1(\mathbb{Q}_p)$. [my conjecture — the precise definition of the restricted product boundary requires care about the adelic topology]

### 3.2 Adelic Perfect Tensor Networks

Place a perfect tensor at each vertex of $\mathrm{BT}_{\mathbb{A}}$. A vertex is a tuple $(v_p)$ where $v_p$ is a vertex in $\mathrm{BT}_p$ for each $p$. The tensor network is a “product” of the single-$p$ networks, but with interactions between the $p$-components.

**Naive construction [speculative]:** Take the tensor product of the perfect tensors at each $p$:

$$T^{\mathbb{A}}_{(v_p)} = \bigotimes_p T^{(p)}_{v_p}$$

This produces a code where the physical qubits are labeled by tuples $(p, \text{leg})$ — one qubit per prime per tree leg. Logical qubits live at the product boundary.

**Problem:** The naive tensor product does not couple different $p$-components. To obtain genuinely new codes, we need cross-$p$ interactions. Two approaches:

1. **Adelic constraint:** Impose that the net state is invariant under simultaneous transformations across all $p$ — a kind of “adelic gauge symmetry.” The adelic reciprocity map (class field theory) provides a natural candidate for this symmentry: the global field $\mathbb{Q}$ embedded diagonally in $\mathbb{A}_{\mathbb{Q}}$ defines a constraint relating $p$-adic components.

2. **Adelic entanglement:** Use perfect tensors that mix legs from different $p$-components. This requires generalizing the notion of perfect tensor to multi-graph structures where edges carry $p$-labels.

### 3.3 Adelic Code Parameters

For an adelic code constructed on $\mathrm{BT}_{\mathbb{A}}$:

- **Physical qubits:** Infinite family indexed by $(p, e)$ where $e$ is an edge in $\mathrm{BT}_p$ at a given cutoff radius.
- **Logical qubits:** Encoded at the product boundary $\prod_p \mathbb{P}^1(\mathbb{Q}_p)$.
- **Code distance $d_p$:** For a given prime $p$, the distance of the restriction to the $p$-subcode. The adelic distance is $d_{\mathbb{A}} = \min_p d_p$ in the worst case, but can be larger if errors must be simultaneously correctable across multiple $p$ [speculative].
- **Error model:** An error is a sequence $(E_p)$ of errors on each $p$-component. An adelic error is correctable if and only if each $E_p$ is correctable in the single-$p$ code AND the cross-$p$ constraints are satisfied.

---

## 4. Candidate Mechanisms for Non-Stabilizer Codes

We propose two mechanisms by which adelic QEC might produce codes not expressible within the CSS/stabilizer formalism. Neither is proven; both are research hypotheses.

### 4.1 Mechanism 1: $p$-Varying Code Distance

In a CSS code, the distance against $X$ errors ($d_X$) and $Z$ errors ($d_Z$) are fixed by the classical codes used in the construction [2]. But in an adelic code, the code distance can vary with $p$.

**Concrete proposal [my conjecture]:** Construct a code where:

- For $p=2$: strong protection against $X$ errors ($d_X = 7$) but weak against $Z$ errors ($d_Z = 3$)
- For $p=3$: strong protection against $Z$ errors ($d_Z = 7$) but weak against $X$ errors ($d_X = 3$)
- The adelic product: strong protection against BOTH ($d_X = 7, d_Z = 7$) because an undetectable error must be undetectable at EVERY $p$

This is a property that no CSS code can achieve from a single classical code pair, because CSS distance parameters are fixed by the two classical codes. The adelic construction allows DIFFERENT classical codes at different primes, and the adelic product enforces simultaneous error correction across all primes.

**Status:** Construction sketch exists; needs explicit tensor network realization.

### 4.2 Mechanism 2: Adelic Logical Operators Spanning Multiple Geometries

In the standard stabilizer formalism, logical operators are tensor products of Pauli operators on physical qubits. The stabilizer group is abelian — all stabilizers commute [3].

In an adelic code, a logical operator might be a product of operators on the $p=2$ tree AND operators on the $p=3$ tree that do not individually have well-defined logical action. [my conjecture]

**Concrete proposal [speculative]:** Define a logical $X$ operator $\bar{X}$ that, when restricted to any single $p$, acts as a non-logical error (detectable by the single-$p$ code), but whose product across all $p$ preserves the logical subspace.

This would be genuinely non-stabilizer: in a stabilizer code, every logical operator decomposes as a product of single-qubit Paulis, and any operator that is non-logical on a subsystem cannot be part of a logical operator. The adelic structure permits operators that are “non-logical locally but logical globally” [my conjecture].

**Why this might NOT work:** The adelic product of stabilizer codes might simply be a larger stabilizer code with a bigger qubit count. If the single-$p$ codes are stabilizer codes (which they are — perfect tensor codes on trees are stabilizer codes [6]), then their tensor product is also a stabilizer code, and Mechanism 2 reduces to a standard stabilizer construction. The burden of proof is to show that the adelic constraint breaks the stabilizer structure.

---

## 5. Proof Obligations

To establish that adelic QEC produces genuinely non-stabilizer codes, the following must be proven:

### 5.1 Negative Proof (Refutation Test)

**Obligation 1:** Exhibit an explicit adelic code with parameters $(n, k, d)$ that cannot be achieved by any stabilizer code on $n$ qubits with distance $d$ encoding $k$ logical qubits.

**Difficulty:** The stabilizer code parameter space is well-studied but not fully characterized [7]. Proving non-existence requires lower bounds on stabilizer code parameters that are currently unknown for many $(n, k, d)$.

**Pragmatic approach:** Use the quantum singleton bound $n - k \geq 2(d - 1)$ [established]. If an adelic construction saturates this bound in a regime where no known stabilizer code does, that constitutes evidence (but not proof) of non-stabilizer status.

### 5.2 Positive Proof (Construction Test)

**Obligation 2:** Exhibit a logical operator in an adelic code that does not factor as a product of single-qubit Paulis modulo the stabilizer group.

**Difficulty:** For finite codes, this can be checked by exhaustive enumeration. For infinite (thermodynamic limit) codes as in holography, the logical operator structure requires analytic characterization.

**Pragmatic approach:** Construct small explicit examples ($p=2$ and $p=3$ with cutoff radius 2–3) and enumerate the logical operator group. Compare to the stabilizer group of the tensor product code.

### 5.3 Structural Test

**Obligation 3:** Show that the adelic constraint (diagonal embedding of $\mathbb{Q}$ in $\mathbb{A}_{\mathbb{Q}}$) introduces relations not present in the product of individual stabilizer groups.

**Difficulty:** The constraint is a global condition on the infinite product. Finite approximations lose the adelic structure.

**Pragmatic approach:** Work in the finite approximation where only finitely many primes are included, and the constraint is approximated by simultaneous congruence conditions (Chinese Remainder Theorem). In this approximation, the constraint reduces to a classical linear code, and the overall code remains a stabilizer code. The genuinely non-stabilizer behavior emerges only in the infinite limit — analogous to how topological order emerges only in the thermodynamic limit [speculative].

---

## 6. Connections to Number Theory

### 6.1 Class Field Theory

The adelic reciprocity map provides a canonical isomorphism between the idele class group and the abelianized absolute Galois group. In physical terms: global symmetries of the adelic code correspond to automorphisms of the number field. This suggests that adelic QEC codes might encode arithmetic information — logical qubits could represent Galois-invariant quantities [my conjecture, not yet falsifiable].

### 6.2 The Langlands Program

Automorphic representations of $\mathrm{PGL}(2,\mathbb{A}_{\mathbb{Q}})$ act on the adelic Bruhat-Tits tree. Different automorphic representations correspond to different “boundary conditions” for the tensor network. The Langlands correspondence maps these representations to Galois representations — a connection between the code's logical structure and arithmetic geometry [speculative].

### 6.3 The $D=4$ Constraint

The silent-radix $D=4$ embedding theorem [8] restricts which ultrametric structures can be realized in physical spacetime. For adelic QEC, this means: which subsets of the product $\prod_p \mathrm{BT}_p$ are embeddable in 4 dimensions? The constraint may limit the number of primes that can simultaneously contribute to a physically realizable code [speculative].

---

## 7. Conclusion: A Research Program, Not a Result

This paper does NOT claim to have constructed a provably non-CSS adelic quantum error-correcting code. What it does is:

1. **Define** the adelic generalization of Heydeman's single-$p$ holographic QEC [1].
2. **Identify** two candidate mechanisms for genuine novelty ($p$-varying code distance and adelic logical operators).
3. **Specify** the proof obligations required to establish or refute non-stabilizer status.
4. **Synthesize** connections to class field theory, the Langlands program, and the $D=4$ constraint.

The central question — “Can adelic QEC produce codes beyond CSS/stabilizer?” — remains open. The research program outlined here provides the conceptual framework and proof strategy for answering it. The pragmatic next step is:

- **Phase 1:** Construct explicit small adelic codes ($p \in \{2, 3\}$, cutoff radius 2) as tensor networks on finite subtrees.
- **Phase 2:** Enumerate logical operators and compare to the stabilizer formalism.
- **Phase 3:** If non-stabilizer structure is found: prove code parameters. If not: prove that all finite adelic codes are stabilizer-equivalent, and investigate whether the infinite limit can differ.

---

## References

1. Heydeman, M., Marcolli, M., Parikh, S., & Saberi, I. (2018). Nonarchimedean Holographic Entropy from Networks of Perfect Tensors. arXiv:1812.04057. [EXTERNAL-SOURCE]

2. Calderbank, A. R. & Shor, P. W. (1996). Good Quantum Error-Correcting Codes Exist. *Physical Review A*, 54, 1098. [established]

3. Gottesman, D. (1997). Stabilizer Codes and Quantum Error Correction. arXiv:quant-ph/9705052. [established]

4. Heydeman, M., Marcolli, M., Saberi, I., & Stoica, B. (2016). Tensor Networks, $p$-adic Fields, and Algebraic Curves. arXiv:1605.07639. [EXTERNAL-SOURCE]

5. Pastawski, F., Yoshida, B., Harlow, D., & Preskill, J. (2015). Holographic Quantum Error-Correcting Codes: Toy Models for the Bulk/Boundary Correspondence. *JHEP*, 06, 149. [EXTERNAL-SOURCE]

6. Hayden, P., Nezami, S., Qi, X.-L., Thomas, N., Walter, M., & Yang, Z. (2016). Holographic Duality from Random Tensor Networks. *JHEP*, 11, 009. [EXTERNAL-SOURCE]

7. Grassl, M. & Roetteler, M. (2015). Quantum Error Correction: An Introduction to the State of the Art. *Proceedings of the IEEE*. [established]

8. Quni-Gudzinas, R. B. (2026). The Silent Radix: Positional Notation as Ultrametric Tree and the Calculus of Indications as Remedy. the QNFO archive. https://papers.qnfo.org/papers. [EXTERNAL-SOURCE: silent-radix]

9. Quni-Gudzinas, R. B. (2026). Ultrametric Information Geometry: From $p$-Adic Spaces to Quantum Error Correction. the QNFO archive. https://papers.qnfo.org/papers. [EXTERNAL-SOURCE]

10. Quni-Gudzinas, R. B. (2026). The Calculus of Distinction: A Formal Isomorphism Between Laws of Form and Ultrametric Trees. the QNFO archive. https://papers.qnfo.org/papers. [EXTERNAL-SOURCE]

---

*This paper directly addresses Open Question 2 of the Ultrametric Information Geometry synthesis [9]. It is a research program definition, not a completed construction — the central question of whether adelic QEC produces genuinely non-stabilizer codes remains open and is specified with proof obligations.*
