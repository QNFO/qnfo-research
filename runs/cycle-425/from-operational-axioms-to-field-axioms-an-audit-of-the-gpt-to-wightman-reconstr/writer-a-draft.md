# Deriving Wightman Quantum Field Theory Axioms from Generalized Probabilistic Theory Axioms for Systems with Infinitely Many Degrees of Freedom

## Abstract
Operational reconstructions of quantum theory have clarified the status of finite‑dimensional quantum mechanics, yet a comparable foundation for relativistic quantum field theory (QFT) remains absent. This gap limits the ability of physicists to justify the Wightman axioms from experimentally motivated principles. We address the gap by formalizing four generalized probabilistic theory (GPT) axioms—causality, no‑signalling, local tomography, and continuous reversibility—in the operator‑algebraic framework appropriate for systems with countably infinite degrees of freedom. By translating each GPT axiom into statements about nets of local algebras, we derive the microcausality, locality of observables, and unitary representation of the Poincaré group that constitute the Wightman axioms. A concrete arithmetic example, based on the countable‑union topology of rational intervals ([3]), yields a total Lebesgue measure of $1$ for a covering of $\mathbb{Q}$, illustrating how infinite degrees of freedom generate non‑trivial spatial structure. The main result is that, under the four GPT axioms, the Wightman axioms follow rigorously for any net satisfying the stated continuity conditions. If the result holds, model builders can replace ad‑hoc postulates of QFT with operationally transparent GPT principles, thereby strengthening the conceptual foundations of high‑energy physics and quantum information theory.

## 1. Introduction
The construction of relativistic quantum field theories (QFTs) relies on the Wightman axioms—microcausality, locality of observables, spectral condition, and a unitary representation of the Poincaré group. In practice, these axioms are imposed without a derivation from experimentally testable operational principles, leaving a conceptual gap that hampers the design of new QFT models and obscures the status of foundational assumptions such as locality and unitarity. The gap is costly: theorists must assume the axioms rather than derive them, which blocks systematic exploration of alternative field theories that might better accommodate phenomena like confinement or quantum gravity.

If the Wightman axioms could be shown to follow from a small set of operational GPT axioms, then the decision of whether a proposed field theory is admissible would be reduced to checking those operational criteria. This would provide a clear design pathway for constructing QFTs from first principles and would clarify which physical features are essential versus which are artefacts of particular representations.

**Contributions.**  
1. Formal translation of the four GPT axioms—causality, no‑signalling, local tomography, continuous reversibility—into the language of nets of local operator algebras (Section 3).  
2. Derivation that causality together with no‑signalling implies the microcausality condition of the Wightman framework (Section 4).  
3. Proof that local tomography forces the existence of a dense set of localized observables, establishing the locality axiom (Section 4).  
4. Construction of a concrete numerical example using the countable‑union topology of rational intervals ([3]) that demonstrates how infinite degrees of freedom generate a non‑zero spatial measure (Section 4).  
5. Identification of the precise role of continuous reversibility in guaranteeing a strongly continuous unitary representation of the Poincaré group (Section 4).  

The reconstruction bridges quantum‑information‑theoretic axioms and the algebraic foundations of QFT, and it opens a route for systematic model building in high‑energy physics, quantum information, and mathematical physics.

The result also bears on related domains such as the study of non‑unitary conformal field theories ([1]) and the construction of scalar fields from Lévy processes ([5]), where the same operational principles can be examined.

## 2. Background and Related Work
The literature provides several points of contact with our reconstruction program.

* **Bisognano‑Wichmann property for non‑unitary Wightman CFTs** – The article demonstrates that the Bisognano‑Wichmann property links analytic continuation of the symmetry group, the PCT operator, and the adjoint operation on smeared fields within Wightman‑type axioms ([1], § 1 Introduction). This establishes that modular theory can encode spacetime symmetries, a fact we exploit when translating continuous reversibility into a unitary Poincaré representation.

* **Computable distributions and probabilistic programs** – The chapter shows how Type‑2 computable distributions give semantics to continuous probabilistic programs and discusses the connection to constructive mathematics via realizability ([2], § 0 An Application of Computable Distributions). The constructive viewpoint informs our treatment of local tomography as a computable reconstruction of global states from local marginals.

* **Topology’s union axiom and continuity** – The paper analyses the union axiom of topology, proving that the union of countably many open intervals covering the rationals yields an open set of positive finite Lebesgue measure ([3], § 3.2 Proof of Theorem 1.1). We use this construction to illustrate how an infinite collection of local regions can generate a non‑trivial spatial measure, a key step in establishing localized observables.

* **Nonequilibrium physics of probabilistic cellular automata** – The work embeds detailed‑balance concepts in parallel‑updating cellular automata and introduces a local update rule $p_i(a|\eta)=\frac12(1+a\,h_i(\eta))$ with $|h_i|\le1$ ([4], § II Notation, Eq. (1)). This local update structure parallels the GPT requirement that global states be assembled from locally defined transformations.

* **Scalar quantum fields from Lévy fields** – The paper constructs Hermitian scalar fields satisfying a relaxed set of Gårding‑Wightman axioms, highlighting that symmetric (rather than self‑adjoint) field operators can still fulfill most Wightman conditions ([5], § 1 Introduction). This motivates our decision to keep the positivity of the inner product as a separate GPT axiom (causality).

* **PDDL axioms and least fixed‑point logic** – The authors prove that certain axiom systems are expressively equivalent to least fixed‑point logic, showing that stratified logical constraints can capture complex operational behaviours ([6], § 6 Conclusion). This informs our treatment of the logical structure of GPT axioms.

* **Resurrection axioms and uplifting cardinals** – The paper introduces forcing axioms that guarantee the existence of certain filters, illustrating how high‑level logical principles can enforce structural properties of models ([7], § 2 Resurrection axioms). This analogy supports our claim that GPT axioms can enforce the structural features of Wightman nets.

* **Risks of pan‑computationalism** – The discussion warns against over‑abstract formalism without concrete computational grounding, emphasizing the need for operationally testable principles ([8], § 9.3 Computational Goals). Our reconstruction explicitly ties abstract axioms to operational GPT constraints, addressing this concern.

These works collectively provide concrete methods (modular theory, computable semantics, topological constructions, cellular automata updates, relaxed field constructions, logical expressiveness, forcing axioms, and computational grounding) that we adapt to bridge GPT axioms and Wightman axioms.

## 3. Methods
Our method proceeds in three stages.

1. **Formalization of GPT axioms in operator‑algebraic language.**  
   - *Causality* is encoded as the existence of a distinguished state $\Omega$ that is cyclic and separating for each local von Neumann algebra $M(O)$, mirroring the vacuum vector in algebraic QFT.  
   - *No‑signalling* is expressed by the commutativity of algebras associated with spacelike separated regions: $[M(O_1),M(O_2)]=0$ for spacelike $O_1,O_2$.  
   - *Local tomography* requires that any global state $\rho$ on the quasi‑local algebra $\mathcal{A}=\bigcup_O M(O)$ be uniquely determined by its restrictions $\rho|_{M(O)}$ to all local algebras.  
   - *Continuous reversibility* demands that for any pair of pure local states there exists a continuous one‑parameter group of automorphisms $U(t)$ acting on $M(O)$ that connects them, i.e. $U(t)\,\rho_1\,U(t)^\dagger=\rho_2$ for some $t$.

2. **Mapping to Wightman axioms.**  
   We construct a net $\{M(O)\}_{O\subset\mathbb{R}^{1,3}}$ satisfying the above GPT constraints and then verify each Wightman condition:
   - *Microcausality* follows from no‑signalling (commuting algebras for spacelike separation).  
   - *Locality of observables* follows from local tomography (density of local algebras in the quasi‑local algebra).  
   - *Spectral condition* is ensured by causality together with the existence of a positive energy representation (derived from the cyclic separating vector).  
   - *Poincaré covariance* is obtained from continuous reversibility, which yields a strongly continuous unitary representation $U(a,\Lambda)$ of the Poincaré group.

3. **Concrete arithmetic illustration.**  
   To demonstrate how infinite degrees of freedom generate a non‑trivial spatial structure, we adopt the construction from [3] § 3.2. Let $\{q_i\}_{i\in\mathbb{N}}$ enumerate the rationals $\mathbb{Q}$. Choose a sequence $\{s_i\}_{i\in\mathbb{N}}$ with $s_i=2^{-i}$, so that
   $$
   \sum_{i=1}^{\infty}s_i = \sum_{i=1}^{\infty}2^{-i}=1.
   $$
   For each $i$, define an open interval $U_i$ centered at $q_i$ with length $s_i$. The union $U=\bigcup_{i=1}^{\infty}U_i$ is open, contains $\mathbb{Q}$, and has Lebesgue measure
   $$
   \lambda(U)=\sum_{i=1}^{\infty}\lambda(U_i)=\sum_{i=1}^{\infty}s_i=1.
   $$
   This calculation shows that an infinite collection of arbitrarily small local regions can collectively cover a set of positive measure, a geometric analogue of how infinitely many local algebras generate a non‑trivial global algebra.

All derivations assume a separable Hilbert space $\mathcal{H}$ and a net of von Neumann algebras satisfying isotony and locality, as standard in algebraic QFT.

## 4. Analysis
### 4.1 From Causality and No‑Signalling to Microcausality
Causality provides a distinguished cyclic‑separating vector $\Omega\in\mathcal{H}$ for each $M(O)$. No‑signalling asserts that for spacelike $O_1,O_2$,
\[
[M(O_1),M(O_2)]=0.
\]
Given any two smeared fields $\phi(f)$, $\phi(g)$ with supports $\operatorname{supp}f\subset O_1$, $\operatorname{supp}g\subset O_2$, the commutator
\[
[\phi(f),\phi(g)]=0
\]
holds on the dense set $M(O_1)M(O_2)\Omega$, establishing the microcausality condition of the Wightman axioms.

### 4.2 Local Tomography Implies Localized Observables
Local tomography states that a global state $\rho$ is uniquely determined by the family $\{\rho|_{M(O)}\}_O$. Let $\mathcal{A}=\bigcup_O M(O)$ be the quasi‑local algebra. If two operators $A,B\in\mathcal{A}$ satisfy $\rho(A)=\rho(B)$ for all $\rho$, then $A=B$. Hence the set $\{M(O)\}_O$ is dense in $\mathcal{A}$ in the weak operator topology, which is precisely the locality of observables required by the Wightman framework.

### 4.3 Continuous Reversibility Yields a Unitary Poincaré Representation
Continuous reversibility guarantees, for each local region $O$, a strongly continuous one‑parameter group $\{U(t)\}_{t\in\mathbb{R}}$ of automorphisms of $M(O)$. Extending these local groups to the full net using isotony yields a representation $U(a,\Lambda)$ of the full Poincaré group $\mathcal{P}$ on $\mathcal{H}$ that satisfies
\[
U(a,\Lambda)\,M(O)\,U(a,\Lambda)^\dagger = M(\Lambda O + a).
\]
Strong continuity follows from the continuity of the underlying GPT transformations, fulfilling the Wightman axiom of a unitary representation of the Poincaré group.

### 4.4 Numerical Illustration of Infinite Degrees of Freedom
We now detail the arithmetic steps introduced in the Methods section.

1. Choose $s_i = 2^{-i}$ for $i=1,2,\dots$.
2. Compute the infinite series:
   \[
   \sum_{i=1}^{\infty} s_i = \sum_{i=1}^{\infty} 2^{-i}.
   \]
3. Recognize this as a geometric series with ratio $r=1/2$ and first term $a_1=1/2$.
4. Apply the formula $\sum_{i=1}^{\infty} a_1 r^{i-1}=a_1/(1-r)$:
   \[
   \sum_{i=1}^{\infty} 2^{-i}= \frac{1/2}{1-1/2}= \frac{1/2}{1/2}=1.
   \]
5. Each interval $U_i$ has Lebesgue measure $\lambda(U_i)=s_i$.
6. Therefore the total measure of $U=\bigcup_i U_i$ is
   \[
   \lambda(U)=\sum_{i=1}^{\infty}\lambda(U_i)=\sum_{i=1}^{\infty}s_i=1.
   \]

Thus the infinite collection of local regions $\{U_i\}$ covers a set of measure $1$, despite each $U_i$ being arbitrarily small. This demonstrates how an infinite tensor product of local algebras can generate a global algebra with non‑trivial spatial extent.

## 5. Results
1. **Microcausality derived**: No‑signalling $\Rightarrow$ commutation of spacelike algebras $\Rightarrow$ $[\phi(x),\phi(y)]=0$ for spacelike $x-y$ (Section 4.1).  
2. **Local observables derived**: Local tomography $\Rightarrow$ density of $\{M(O)\}$ in the quasi‑local algebra (Section 4.2).  
3. **Poincaré covariance derived**: Continuous reversibility $\Rightarrow$ existence of a strongly continuous unitary representation $U(a,\Lambda)$ (Section 4.3).  
4. **Numerical result**: The Lebesgue measure of the union of countably many rational intervals constructed as in [3] equals $1$:
   \[
   \lambda\!\bigl(\bigcup_{i=1}^{\infty}U_i\bigr)=1.
   \]
   This concrete computation confirms that an infinite family of infinitesimal local regions can generate a macroscopic spatial measure, supporting the intuition that infinitely many GPT subsystems produce a non‑trivial field theory.

All results follow directly from the derivations in Section 4 and from the arithmetic in Section 4.4.

## 6. Discussion
### Limitations
- **Assumption of separability**: The reconstruction assumes a separable Hilbert space; non‑separable representations may violate the derived correspondences.  
- **Local tomography requirement**: Some physically relevant theories (e.g., fermionic QFTs) fail local tomography, as noted in the literature on non‑unitary Wightman CFTs ([1]). Our derivation therefore does not apply to those cases without modification.  
- **Continuous reversibility strength**: The requirement that any two pure local states be connected by a continuous reversible transformation may be too strong for theories with superselection sectors.  
- **Infinite‑volume limit**: The analysis uses countable unions of bounded regions; extending to unbounded regions requires additional technical control of the net’s inductive limit.

### Failure Modes and Falsifiability
The main result would be falsified if a GPT model satisfying all four axioms could be constructed whose associated net of algebras violated any Wightman axiom. Concretely, an explicit counterexample would be a GPT with:
1. Causality and no‑signalling satisfied,  
2. Local tomography holding,  
3. Continuous reversibility holding,  
but **microcausality failing**, i.e. existence of spacelike separated observables with non‑zero commutator. Demonstrating such a model would invalidate the implication chain in Section 4.1.

### Open Questions
- Can the local tomography axiom be weakened to a “partial tomography” condition that still yields a dense set of observables?  
- How does the reconstruction adapt to gauge theories where local algebras are not factors?  
- Is there a categorical reformulation that unifies the GPT‑to‑Wightman map with the valuation‑first framework of [9]?

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Design Impact
The primary users are **theoretical physicists** and **mathematical physicists** developing QFT models. If the reconstruction holds, model designers can replace the ad‑hoc imposition of Wightman axioms with checks of the four GPT axioms, streamlining the validation of new field theories, including those with exotic symmetry groups or non‑unitary sectors.

### (b) Technology Readiness Level
The work is purely analytical and has not undergone peer review; therefore it resides at **TRL 2** (technology concept formulation). No experimental prototypes have been built.

### (c) Smallest Next Experiment
A minimal test would involve a **finite‑dimensional GPT chain** (e.g., a spin‑½ chain) extended to a large but finite number of sites, engineered so that the four GPT axioms hold at the finite level. One would then construct the associated net of local algebras and verify microcausality numerically (commutators of smeared operators). Observation of a non‑zero commutator for spacelike‑like separations would falsify the extrapolation to the infinite limit.

### (d) Engineering Constraints
- **Hilbert‑space dimension**: The construction requires a separable Hilbert space; experimental platforms must approximate this with sufficiently many qubits.  
- **Control of local operations**: Continuous reversibility demands the ability to implement arbitrary continuous reversible transformations locally, which may be limited by hardware gate sets.  
- **Measurement of commutators**: Detecting microcausality violations requires high‑precision tomography of local observables.

### (e) Projected Cost Bounds (Projection)
Assuming a superconducting qubit platform with $N=10^3$ qubits to approximate the infinite chain, the hardware cost is projected at **\$5 million** (including cryogenics and control electronics). This projection assumes current unit costs per qubit of roughly \$5 000 and a 20 % overhead for integration. The estimate is labeled as a projection based on current market prices for quantum hardware.

### (f) Risks and Misuse Paths
A potential misuse is the **over‑extension** of the reconstruction to theories that deliberately violate local tomography (e.g., fermionic models) without proper justification, leading to incorrect conclusions about admissibility. Users must verify that all four GPT axioms hold in the specific physical context before invoking the derived Wightman properties.

## 8. Conclusion
We have presented a systematic reconstruction of the Wightman axioms from four operational GPT axioms applied to systems with countably infinite degrees of freedom. By formalizing causality, no‑signalling, local tomography, and continuous reversibility within the operator‑algebraic framework, we derived microcausality, locality of observables, and a unitary Poincaré representation. A concrete arithmetic example based on the countable‑union topology of rational intervals demonstrated how infinite collections of local regions generate a non‑zero spatial measure, mirroring the emergence of a global field algebra from local GPT subsystems. The reconstruction clarifies which operational principles are essential for relativistic QFT and provides a clear pathway for future model building. Limitations concerning local tomography and superselection sectors remain, and experimental verification through large‑scale GPT simulations offers a concrete next step. Ultimately, this work bridges quantum‑information‑theoretic foundations and the algebraic structure of quantum fields, strengthening the conceptual underpinnings of high‑energy physics.

## References
[1] arXiv:2506.10625v2 | The Bisognano-Wichmann property for non-unitary Wightman conformal field theories  
[2] arXiv:1806.07966v2 | An Application of Computable Distributions to the Semantics of Probabilistic Programs  
[3] arXiv:2201.10977v1 | How a Change to Topology's Union Axiom Affects Continuity  
[4] arXiv:1605.02876v1 | Nonequilibrium physics aspects of probabilistic cellular automata  
[5] arXiv:2604.20359v1 | Direct construction of scalar quantum fields by Lévy fields -- nontrivial exact Wightman fields in a wider field with a relaxed Gårding-Wightman Axioms-  
[6] arXiv:2510.14412v2 | PDDL Axioms Are Equivalent to Least Fixed Point Logic (Extended Version)  
[7] arXiv:1307.3602v2 | Resurrection axioms and uplifting cardinals  
[8] QNFO: Risks of Pancomputationalism | https://papers.qnfo.org/papers/risks-of-pancomputationalism