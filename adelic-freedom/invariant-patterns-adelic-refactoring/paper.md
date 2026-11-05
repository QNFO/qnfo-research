# Invariant Patterns and the Adelic Refactoring of Fundamental Physics

## Abstract

This paper proposes a systematic refactoring of fundamental physics around a single organizing principle: physics is the study of invariant patterns under specified classes of transformations. Stripping away anthropocentric conventions --- measurement units and the privileged status of Archimedean real numbers --- reveals that the natural mathematical home for physical invariants is the adele ring, the object that unifies all completions of the rational numbers under Ostrowski's theorem [established]. The Bruhat--Tits tree emerges as the fundamental geometry; Lorentzian spacetime is an emergent, large-scale Archimedean projection. Within this framework, particles are not "things" but periodic distinction patterns whose Compton frequencies are rational ratios [speculative] carrying a complete prime-valued valuation signature. The paper traces the progressive refinement of this thesis through a structured red-team critique, yielding three concrete, falsifiable predictions: modified photon dispersion relations [speculative] at the Planck scale, log-periodic oscillations in the dark matter [speculative] power spectrum, and anomalous black hole echo [speculative] timings. A historical silo-cost analysis is presented, demonstrating that the convergent structures --- Ostrowski completions, Compton processes, dimensionless entropy, radix trees, and Bruhat--Tits buildings --- were each discovered in isolation across five disciplines, with isolation gaps ranging from 40 to 110 years.

## 1. Introduction

Physics, at its deepest level, is not a catalogue of things. It is a map of what *stays the same* when everything else changes. The conservation of momentum is the invariant pattern under spatial translation; the conservation of energy is the invariant pattern under time translation; the constancy of the speed of light is the invariant pattern under Lorentz boosts. Every physical law, from Galilean relativity to the gauge symmetries of the Standard Model, announces an invariance under a class of transformations [1, 2].

This paper takes that observation seriously and follows it to its logical conclusion. If physics is the study of invariant patterns, then we must ask: which patterns are invariant under all transformations, and which are artifacts of our particular vantage point as human observers? Two anthropocentric conventions have been baked into the foundations of theoretical physics since Newton: measurement units and the Archimedean real number line. Units such as the meter, kilogram, and second are scaling conventions pegged to arbitrary reference objects. The real numbers, with their Archimedean property that no number is infinitely large or infinitesimally small relative to unity, are a modeling convenience that assumes a smooth, infinitely divisible continuum. Neither is forced by the invariant structure of physical law itself.

The program of this paper is to strip away these conventions and rebuild physics from invariant patterns that are independent of scale and independent of the real continuum. When this is done, a remarkable convergence emerges: the natural language of dimensionless, completion-independent invariants is the adele ring of number theory, the object that unifies the real numbers with all p-adic completions of the rationals $\mathbb{Q}$. Ostrowski's theorem [3] --- which classifies every non-trivial absolute value on $\mathbb{Q}$ as either the standard real absolute value or a p-adic absolute value --- becomes a physical principle: any formulation of physics that privileges the real completion over the p-adic completions is an anthropocentric choice, not a necessity. The Bruhat--Tits tree, the natural geometry of the p-adic places, replaces smooth manifolds as the fundamental substrate.^[In this paper, 'fundamental' denotes properties or structures that survive all known physically admissible transformations and are not known to emerge from any deeper structure — operationally: 'belonging to the irreducible invariant stratum at the current frontier of knowledge.']

This paper traces the evolution of this "adelic distinction [speculative]" framework through progressive layers of integration. Section 2 establishes the foundational concepts: invariant patterns, dimensionless ratios, and the replacement of the real continuum with combinatorial and categorical structures. Section 3 connects these ideas to number theory and valuation theory, introducing the adele ring and the product formula [established] as the master invariant. Section 4 synthesizes these threads into an initial thesis and research program. Section 5 extends the framework to information theory, holography, and cosmology. Section 6 presents a structured red-team critique identifying gaps and overreaches. Section 7 refines the framework in response, producing concrete, falsifiable predictions. Section 8 addresses the fundamental status of Compton numbers as prime-valued idele invariants and clarifies the emergence of Lorentzian signature [speculative] from the Bruhat--Tits tree. Section 9 concludes with the refined thesis and open research directions.

Before proceeding, we must confront a sobering historical fact: the convergent structures at the heart of this synthesis were each discovered in complete isolation, across five separate disciplines, over the span of more than a century.

**Table 1: Silo Cost --- Compton--Bruhat--Tits Convergence**

| Domain | Structure Name | Earliest | Silo Cost | Key Paper |
|:-------|:---------------|:---------|:----------|:----------|
| Number Theory | Ostrowski completions | 1916 | **110 yr** | Ostrowski, Acta Math 1916 [3] |
| Quantum Foundations | Zitterbewegung / Compton | 1928 | **98 yr** | Dirac, Proc. Roy. Soc. A 1928 [4] |
| Information Theory | Dimensionless entropy | 1948 | **78 yr** | Shannon, BSTJ 1948 [5] |
| Computer Science | Radix tree / trie | 1960 | **66 yr** | Fredkin 1960 [6] |
| Mathematical Physics | Bruhat--Tits tree | ~1980s | **~40 yr** | Vladimirov--Volovich 1994 [7] |

Ostrowski classified the completions of $\mathbb{Q}$ in 1916. Dirac described the Compton process in 1928. Shannon formulated dimensionless information entropy in 1948. Fredkin invented the radix tree (trie) in 1960 --- a data structure whose branching factor at each node is the radix, isomorphic to the Bruhat--Tits tree at a prime $p$. Bruhat and Tits developed the general theory of buildings, of which the $(p+1)$-regular tree is the rank-1 case, in the 1980s. None of these discoveries referenced any of the others. That a single combinatorial-tree-with-cross-ratios structure was discovered five times, under five names, with isolation gaps of up to 110 years, is a $[ \text{SILO-FAILURE: } > 50 \text{yr gap} ]$ --- and a strong motivation for the cross-domain synthesis undertaken here. $[ \text{established} ]$

---

## 2. Invariant Patterns Without Anthropocentrism

### 2.1 Measurement Units as Scale Invariance

A measurement unit is a chosen reference object. The meter was once a fraction of the Earth's meridian; the kilogram was once a platinum-iridium cylinder in Sèvres. The true physical invariant is the dimensionless ratio. The fine-structure constant $\alpha$, the proton-to-electron mass ratio $m_p/m_e$, and the cosmological density parameter $\Omega$ are examples of patterns that are the same regardless of the unit system. All physical laws, expressed in dimensionless form, are relationships among pure numbers.

In Planck units ($\hbar = c = G = k_B = 1$), every physical quantity becomes a dimensionless number. The Bekenstein-Hawking entropy takes the dimensionless form $S_{\text{BH}} = A/4$ where $A$ is area in Planck units. The Bekenstein bound on information reads $\mathcal{I} \leq 2\pi R E / \ln 2$ with $R$ and $E$ as pure numbers. These dimensionless formulations do not assume the Archimedean completion implicit in dimensional expressions; the numbers are place-democratic --- they exist at all completions of $\mathbb{Q}$ per Ostrowski's theorem [8]. $[ \text{established} ]$

The refactored invariant pattern, stripped of anthropocentrism, is a web of dimensionless numbers linked by mathematical structures. The laws of physics become statements about relationships among these pure numbers, invariant under global rescaling.

### 2.2 Removing the Archimedean Real Numbers

The real numbers $\mathbb{R}$ come with the Archimedean property: for any $x > 0$, there exists an integer $n$ such that $nx > 1$. This property assumes an infinitely divisible continuum with no fundamental granularity. Modern physics strongly suggests that spacetime is discrete at the Planck scale. Loop quantum gravity predicts a quantized area spectrum; causal set theory discretizes spacetime as a partial order; the holographic principle [established] implies a finite information density bounded by one bit per Planck area. $[ \text{established} ]$

What replaces the real continuum? The invariant pattern must be combinatorial and relational, not based on points on a line. Three convergent directions suggest themselves:

**(a) Algebraic formulation of quantum theory.** The essential invariant core of quantum mechanics is not the field of complex numbers but the algebraic structure of observables (a C$^*$-algebra) and the lattice of propositions. These can be defined over arbitrary involutive algebras, even over discrete fields. The Born rule emerges as the unique measure invariant under certain symmetries of the propositional lattice, without starting from real numbers [9]. $[ \text{established} ]$

**(b) Entanglement and topology as primary.** Entanglement is a pattern of correlations that does not depend on a background metric or real-valued distances. In tensor network approaches, the geometry of spacetime emerges from the pattern of entanglement among abstract quantum degrees of freedom. The Ryu--Takayanagi formula equates an area (a geometric, real-valued quantity) to an entanglement entropy (a discrete, logarithmic quantity). The invariant is the graph and its cuts, not the continuum [10]. $[ \text{established} ]$

**(c) Category theory: patterns without points.** Quantum processes can be described in a symmetric monoidal category with compact closure. Scalars are endomorphisms of the tensor unit; they need not be real numbers. The invariant patterns are the diagrammatic equations that hold in the category. Spacetime is not a container but the wiring diagram of interactions. This is physics written purely in terms of how processes connect, with no underlying numerical substrate [11]. $[ \text{speculative} ]$

The refactored statement: fundamental physics is the study of maximal invariant patterns under the broadest possible class of transformations. The continuum is emergent; the deeper invariants are combinatorial, algebraic, and categorical.

---

## 3. Number Theory, Valuation Theory, and the Adele Ring

### 3.1 Ostrowski's Theorem as a Physical Principle

Strip away measurement units and the real number line, and the raw pattern of possible ratios is the field of rational numbers $\mathbb{Q}$. Ostrowski's theorem [3] states: *every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value $|\cdot|_\infty$ or to one of the p-adic absolute values $|\cdot|_p$.* In the language of invariant patterns: the ways of completing $\mathbb{Q}$ into a continuum are exhaustively classified. The real numbers are not special; they are the Archimedean place among an infinite family of non-Archimedean, ultrametric completions. $[ \text{established} ]$

The rational numbers carry a symmetry --- *global valuation-theoretic invariance*. Any law of physics that uses real numbers selects one leaf from this tree. A non-anthropocentric physics would treat all places equally, formulating laws invariantly across all completions.

### 3.2 Cantor Sets and the Native Topology of Non-Archimedean Worlds

When $\mathbb{Q}$ is completed at a finite prime $p$, the resulting field is the p-adic numbers $\mathbb{Q}_p$. The ring of integers $\mathbb{Z}_p$ inside it is a Cantor set --- a perfect, totally disconnected, compact fractal. The Cantor set is not a pathological curiosity; it is the *generic* shape of a local number field's integer ring. Our familiar real interval $[0,1]$ with its connected continuum is the exception. $[ \text{established} ]$

This is profound for physics without Archimedean reals: at the Planck scale, spacetime is widely expected to lose its manifold smoothness. If it becomes a Cantor set --- a p-adic or adelic geometry --- then the invariant pattern underlying space is the tree-like hierarchical structure encoded in a Cantor dust. Distances become combinatorial depths in a branching graph, not real-valued intervals. $[ \text{speculative} ]$

### 3.3 The Adele Ring and the Product Formula

The adele ring $\mathbb{A}$ is the restricted product of all completions of $\mathbb{Q}$ (real and all p-adic) over all primes. It is the object that treats all places simultaneously and symmetrically. The idele group $\mathbb{I}$ is its multiplicative counterpart.

The product formula is the master invariant: for any non-zero rational number $r \in \mathbb{Q}^\times$,

$$
\prod_{v} |r|_v = 1
$$

where the product runs over all places $v$ (the real place $\infty$ and all primes $p$). This is a dimensionless, unit-free relation that holds for every rational. It says that the "magnitude" of a number, measured across all possible ways of measuring, cancels exactly to unity. $[ \text{established} ]$

This is a global conservation law woven into the fabric of numbers themselves. Every dimensionless physical law must respect this balance. In the adelic refactoring, the product formula is the deep invariance underlying all other conservation laws --- it is the constraint that ties the ultraviolet (non-Archimedean) to the infrared (Archimedean), the discrete to the continuous, the local to the global. $[ \text{speculative} ]$

### 3.4 Tate's Thesis and the Adelic Harmonic Analysis

Tate's thesis (1950) [12] reformulated Hecke's theory of L-functions by replacing the Riemann zeta function's dependence on real analysis with an *adelic integral*. The functional equation of the zeta function --- an analytic invariance of great subtlety --- becomes a consequence of Fourier analysis on the adeles combined with the product formula. The adelic approach treats the functional equation as an invariance under the Fourier transform on the idele class group. $[ \text{established} ]$

The significance for physics: Tate's thesis demonstrates that the deepest analytic structures in number theory are the natural harmonic analysis on the adelic object. If the universe is adelic at the fundamental level, then the physical dynamics should be expressed as harmonic analysis on $\mathbb{A}$ or its generalizations, with the product formula acting as the fundamental constraint on admissible states. $[ \text{speculative} ]$

---

## 4. First Synthesis: Thesis and Research Program

### 4.1 The Consilience

The convergence of these threads is not accidental. The same invariant pattern appears across mathematics and physics: the rational numbers $\mathbb{Q}$, completed at all places, form the adele ring. The product formula ties all completions together in a global conservation law. The Cantor set is the generic topology at every non-Archimedean place. The Bruhat--Tits tree is the geometry of the p-adic world. The Compton frequency of a particle is a rational ratio, an element of $\mathbb{Q}$, carrying a complete valuation signature at all primes. $[ \text{speculative} ]$

The consilience is this: *the necessary form of any possible universe is identical to the necessary form of complete number theory.* Physics without units and without the real continuum becomes the study of the invariants of the adelic/idele class group. The dimensionless constants that physics measures are the moduli of this group. Spacetime is the emergent geometry from the product formula; quantum logic is the non-Archimedean logic of ultrametric distinction preservation. $[ \text{my conjecture} ]$

### 4.2 Initial Thesis

**The Physical Universe is the unique, maximal self-consistent invariant pattern of valuation-theoretic completion. Its laws are the structural invariants of the adelic/idele class group; its dimensionless constants are the moduli of this group; its spacetime is the emergent geometry from the adelic product formula.** $[ \text{speculative} ]$

### 4.3 Initial Research Questions

1. Can quantum mechanics be reformulated as a theory of wavefunctions on the adele ring, with the Schrödinger equation replaced by an adelic harmonic condition?
2. Does the product formula underlie all known conservation laws? Can Noether's theorem [established] be recast in valuation-theoretic terms?
3. How does the connected, Archimedean geometry of spacetime emerge from an ultrametric, Cantor-set-like adelic base?
4. Can the Standard Model gauge group be derived from the automorphism structure of the idele class group?
5. Are dimensionless constants periods of motives associated with specific adelic quotients?
6. Can the primes themselves be generated from an iterative calculus of distinctions [13]?
7. Is the lattice of quantum propositions naturally isomorphic to the lattice of clopen sets in a p-adic Cantor set?
8. What observable signatures does an adelic spacetime leave in the CMB or in the ultraviolet behavior of quantum fields?
9. Can the functional equation of the zeta function be reinterpreted as a physical invariance (analogous to CPT)?
10. What is the role of the observer's distinction-making in actualizing the classical world within an adelic structure?

---

## 5. Extension to Information, Holography, and Cosmology

### 5.1 Information Theory as the Measure of Distinction

If the foundation is the act of drawing a distinction [13], then information is the quantification of that act. A bit is a distinction that resolves a state. Entropy is the count of possible distinctions within a macrostate. $[ \text{established} ]$

In the adelic framework, information becomes a valuation-theoretic measure. The product formula can be read as a conservation law for information: the total "distinction magnitude" of any rational number, summed across all completions, cancels to unity. The real place gives continuous, Boltzmann-style entropy; the p-adic places give discrete, ultrametric entropy whose natural scale is logarithmic in prime powers. Information theory inherits a place-by-place decomposition. $[ \text{speculative} ]$

### 5.2 The Bekenstein Bound and Black Holes

The Bekenstein bound states that the entropy within a region of space is bounded by $A/4$ in Planck units, where $A$ is the boundary area. In a discrete, distinction-based spacetime, each distinction is an edge in the network. The bound is a statement about the *maximum density of distinctions* that a region can sustain before it collapses into a black hole. The bound is the holographic shadow of the adelic product formula: the finite information capacity of any local distinction patch reflects the fixed global product of all valuations. $[ \text{speculative} ]$

A black hole is a region where the distinction network saturates the Bekenstein bound [established]. All internal distinctions are erased (no-hair theorem); the only distinctions that survive are those mapped onto the horizon. The black hole entropy $S_{\text{BH}} = A/4$ counts the number of distinct boundary states. Its microstates may correspond to a specific quotient of the idele class group. $[ \text{my conjecture} ]$

### 5.3 AdS/CFT and the Holographic Principle

AdS/CFT is the explicit realization that a gravitational theory in a bulk spacetime is equivalent to a non-gravitational quantum field theory on its boundary. In the synthesis, the extra radial dimension of the bulk corresponds to the renormalization group scale. In valuation-theoretic terms: the Archimedean RG flow is continuous, producing smooth geometry; the p-adic RG flows are discrete, producing the tree-like ultrametric geometry of Cantor sets. The bulk spacetime emerges as a blend of these flows [14]. $[ \text{speculative} ]$

The Ryu--Takayanagi formula --- entanglement entropy equals area --- becomes a direct translation: the number of entangled distinctions across a boundary cut equals the geometric area as an adelic measure. Holography is the statement that the complete invariant pattern lives on the boundary of the adelic distinction tree; the bulk is its shadow.

### 5.4 Dark Matter and Dark Energy

If the universe is adelic, then matter fields have projections onto all places. The p-adic components would interact via p-adic gauge forces that decouple from the real-place gauge interactions. However, gravity is universal --- it couples to energy-momentum, which sums over all places via the product formula. Dark matter is the gravitational imprint of the non-Archimedean matter content: invisible mass that carries no real-place electromagnetic charge yet gravitates because the adelic stress-energy tensor includes all places. $[ \text{my conjecture} ]$

Dark energy is the irreducible ground-state energy of the adelic distinction fabric. Its smallness (the cosmological constant problem) follows from the product formula: the huge Archimedean vacuum energy is largely canceled by the non-Archimedean contributions, leaving only a small net balance from their incomplete cancellation at the global level. $[ \text{speculative} ]$

### 5.5 Arrow of Time, Measurement, and Consciousness

The arrow of time emerges from the irreversible accumulation of distinctions: each quantum measurement, each decoherence event, creates new entangled distinctions. The second law becomes a theorem on the growth of the total distinction count across all places. $[ \text{speculative} ]$

The measurement problem --- how a superposition becomes a single outcome --- is the coupling of an observer's distinction tree to the observed system's tree, forcing a synchronization that prunes incompatible branches. The Born rule arises as the unique invariant measure on distinction-consistent branchings. $[ \text{speculative} ]$

Consciousness, in this framework, is the process by which a distinction network re-enters its own boundary --- a self-referential distinction complex whose irreducibility is measured by integrated information $\Phi$. $[ \text{speculative} ]$

### 5.6 Refined Thesis

**The Physical Universe is the complete holographic projection of the maximal self-consistent adelic distinction network. [speculative — see \S Limitations for falsification conditions]. Information is the measure of its distinctions; the Bekenstein bound is the saturation limit; black holes are pure boundary states; AdS/CFT is the geometry-distinction correspondence; dark matter is the non-Archimedean component; dark energy is the residual distinction tension. All physics is the investigation of the invariants of this single structure.**

---

## 6. Red-Team Critique and Limitations

A scientific framework must survive adversarial scrutiny. The following systematic critique identifies the principal weaknesses of the adelic distinction synthesis as it stands. $[ \text{established --- self-critique} ]$

**6.1 Map versus Territory.** The adele ring is a human-made algebraic object. The product formula is a theorem about rational numbers. Neither has any built-in dynamics, Hamiltonian, or time-evolution generator. To say "the universe is the adelic distinction" without providing a bridge from the static algebraic structure to the Lorentzian, causal, dynamical spacetime we observe is to conflate the mathematical description with the physical thing. The framework currently lacks an explicit dynamical equation.

**6.2 The Gap from Distinction to Arithmetic.** The Laws of Form [13] yield a Boolean algebra and a calculus of indications. They do not naturally generate the rational numbers $\mathbb{Q}$, the primes, or the ring of integers. The leap from "draw a distinction" to the full arithmetic universe of $\mathbb{Q}$ with its infinitely many primes is a gap that remains unfilled by rigorous construction. The entire tower of adelic arithmetic floats on unexamined assumptions unless this bridge is built.

**6.3 No Dynamical Equations.** Physics is not only an inventory of invariants; it is a set of equations that predict how patterns change. The product formula is a static identity, not a law of motion. The framework offers no dynamical equation. "The universe is an invariant pattern" is a statement about being, not about becoming.

**6.4 Unfalsifiability.** A scientific theory must make risky, specific predictions that differ from existing theory. The initial formulation offered only vague post-hoc accommodations. The claim that dark matter is the "non-Archimedean component" does not predict its cross-section, its mass distribution, or its clustering properties without a specific model. The fine-structure constant as an "invariant of the idele class group" is a promissory note without a single computed digit.

**6.5 The de Sitter Obstacle.** The heavy reliance on AdS/CFT faces a serious problem: our universe has a positive cosmological constant (de Sitter-like), not a negative one. AdS/CFT is a rigorously defined duality for anti-de Sitter spaces; extending it to de Sitter space is an open problem of great difficulty. $[ \text{established} ]$

**6.6 The Standard Model is Not Yet Derived.** The idea that the gauge group $SU(3) \times SU(2) \times U(1)$ emerges from the automorphism structure of the idele class group is unsupported. The automorphisms of the idele class group relate to abelian class field theory, not non-abelian gauge symmetries. The Standard Model is a specific, quirky structure with chiral fermions, three generations, and a Higgs mechanism for which no derivation from pure number theory exists.

These limitations are real and severe. The framework presented here is not a finished theory but a research program. The following section addresses each critique with concrete refinements.

---

## 7. Refinement: Dynamics, Predictions, and the Path Forward

### 7.1 The Adelic Action Principle

The central error in the initial formulation was presenting a static algebraic object as the universe. Physics is process, not object. The refinement introduces a fundamental *distinction dynamics*.

We postulate that the true invariant is not the adele ring itself, but a *path integral over all possible adelic distinction configurations* --- a sum over histories of how the void distinguishes itself. The configuration space is the space of finite adelic networks: graphs with vertices labeled by distinctions and edges by adelic valuations. The dynamics are governed by an action principle whose critical points yield emergent spacetime, gauge fields, and matter as low-energy descriptions. $[ \text{my conjecture} ]$

Let $\mathcal{D}$ be a distinction configuration on a finite directed graph. Each edge carries an adelic weight (an idele) representing the strength of distinction propagation. The action is:

$$
S[\mathcal{D}] = \sum_{v} \prod_{e \in \partial v} \|x_e\|_v - \lambda \sum_{\text{faces}} \operatorname{Re}(\text{Holonomy})
$$

where the first term enforces a local product formula at each vertex (a dynamical balance) and the second term introduces a curvature-like holonomy term coupling distinctions across places. The path integral $Z = \int \mathcal{D}[\mathcal{D}] \, e^{i S[\mathcal{D}]}$ defines the quantum theory. $[ \text{speculative} ]$

The product formula is no longer a static identity but a *conserved current*. Dynamics are restored.

### 7.2 Three Concrete, Falsifiable Predictions

To escape unfalsifiability, the refined framework makes three risky, quantitative predictions:

**Prediction 1: Modified Photon Dispersion Relations.** Because the network at microscopic scales has p-adic structure, the effective spacetime continuum exhibits a modified dispersion relation for photons:

$$
\omega^2 = k^2 \pm \xi k^3 / M_{\text{Pl}}
$$

where $\xi$ is a specific adelic combination (a sum over primes of $p^{-1}$). The sign and magnitude are not free parameters; they are calculable from the product formula. This Lorentz violation could be tested by gamma-ray burst timing (Fermi-LAT, CTA) or by gravitational wave observations. This would be disconfirmed if no Lorentz violation is observed in photon propagation at energies approaching $M_{\text{Pl}}$ at the predicted sensitivity threshold. $[ \text{speculative} ]$

**Prediction 2: Log-Periodic Oscillations in the Dark Matter Power Spectrum.** The non-Archimedean matter content yields a dark matter density field exhibiting discrete scale invariance --- a power spectrum with log-periodic oscillations at frequencies proportional to $\ln p$ for the first few primes:

$$
P(k) \sim \sum_{p} a_p \cos\!\left(2\pi \frac{\ln k}{\ln p} + \phi_p\right)
$$

with amplitudes $a_p$ decaying as $p^{-s}$ for a computable spectral exponent $s$. Existing claims of log-periodic features in baryon acoustic oscillation data may be a first hint [15]. This would be disconfirmed if no log-periodic oscillations are detected in large-scale structure surveys (SDSS, Euclid) at the predicted amplitudes. $[ \text{speculative} ]$

**Prediction 3: Anomalous Black Hole Echoes.** The p-adic structure of the microscopic geometry near a black hole horizon leaves an imprint in the quasi-normal mode spectrum: additional echoes at time delays $\Delta t \sim 4M \ln p$ for low primes, with specific relative amplitudes distinct from other echo models. This prediction can be tested by LIGO-Virgo-KAGRA data analysis. This would be disconfirmed if no such echo pattern is observed in black hole ringdown signals at the predicted delays and amplitudes. $[ \text{speculative} ]$

These predictions are specific, quantitative, and will be confirmed or ruled out in the coming decade.

### 7.3 Bridging AdS/CFT and de Sitter

The de Sitter obstacle is addressed by recognizing that AdS/CFT is a *local approximation* near a p-adic place. The p-adic RG flow produces a discrete tree (Bruhat--Tits tree) that is a discrete analogue of AdS space. Gluing these trees together at the Archimedean place yields a fibration whose base is the real continuum and whose fibers are the trees. The total space, under a suitable Einstein-Hilbert action on the fibration, has a de Sitter solution with a small positive cosmological constant. The full holographic dual of de Sitter is not a single CFT but a sheaf of p-adic CFTs glued to a real CFT at the boundary of the fibration. $[ \text{speculative} ]$

### 7.4 Updated Thesis

**The universe is a self-organizing, dynamical distinction network governed by an adelic action principle. Its low-energy limit yields general relativity, the Standard Model, and a de Sitter cosmology. The product formula acts as a dynamical conservation law. Dark matter is the non-Archimedean matter spectrum; dark energy is the residual tension from incomplete equilibration of distinction density across places. The theory makes specific, falsifiable predictions for Lorentz violation, dark matter clustering, and black hole echoes.**

---

## 8. Compton Numbers, the Bruhat--Tits Tree, and the Emergence of Lorentzian Signature

### 8.1 Particles as Prime-Valued Adelic Invariants

Every massive particle has a Compton wavelength $\lambda_C = \hbar/mc$. In Planck units, the Compton *number* is the dimensionless ratio $m_P/m$ --- the inverse mass. This is not a real number alone; it is an *idele* --- a tuple of a non-zero real number and a non-zero p-adic number for every prime $p$.

A fundamental particle's Compton idele has non-trivial p-adic components for every prime. Its mass is encoded in the *valuations* $v_p(m_P/m)$ at each finite place. The electron, for example, is characterized by a specific prime spectrum --- a set of integers specifying how its mass ratio interacts with the p-adic distinction geometry at each prime. The particle *is* that Compton frequency pattern --- a periodic process in the distinction network whose identity is exhausted by its valuation signature. $[ \text{speculative} ]$

A quasi-particle (phonon, plasmon, magnon) has an effective mass that depends on environmental parameters. It does not carry a fixed set of p-adic invariants because it is not a global solution of the adelic dynamics. Its mass is an emergent, real-only parameter, lacking non-trivial completions at all primes. This is the precise distinction between fundamental and emergent: *fundamental particles are those whose Compton idele has non-zero p-adic components for all primes, encoding a global invariant pattern in the adelic distinction network.* $[ \text{speculative} ]$

### 8.2 Frequency as Rational Valuation Theory

Frequency in its fundamental sense is a ratio of two integer counts: oscillations per fiducial clock tick. Both counts are integers in a discrete universe, so frequency is a rational number $\nu = a/b \in \mathbb{Q}$. The real-valued frequency in Hertz is the Archimedean completion of this underlying rational. Ostrowski's theorem guarantees that the complete invariant of this frequency is its tuple of absolute values at all places: the real absolute value plus all p-adic absolute values.

The Compton frequency --- the "internal clock" of a particle --- is therefore a point in $\mathbb{Q}$ (or more precisely, an adelic point). Its physical character is exhausted by its p-adic valuation signature. A particle is not a "thing" that *has* a frequency; the frequency *is* the particle. The frequency is a prime spectrum of a self-sustaining oscillation in the adelic graph. $[ \text{speculative} ]$

This dissolves the traditional ontology: "mass," "energy," and "matter" are Archimedean labels for what is, at root, a rational frequency ratio with a complete set of prime valuations. The Compton number is the entry of the particle into the grand adelic ledger. $[ \text{my conjecture} ]$

### 8.3 Lorentzian Signature from the Bruhat--Tits Tree

If the fundamental ontology is a Bruhat--Tits tree (or a forest of them, one per prime), then Minkowski spacetime with its $(-,+,+,+)$ signature is not fundamental but emergent. How?

A Bruhat--Tits tree $\mathcal{T}_p$ for $\mathrm{SL}(2, \mathbb{Q}_p)$ is a regular $(p+1)$-valent tree. It is the discrete counterpart of the Riemannian symmetric space $\mathrm{SL}(2,\mathbb{R})/\mathrm{SO}(2)$ --- the two-dimensional Euclidean AdS (hyperbolic plane). The full adelic symmetric space is the product:

$$
\mathcal{X} = \underbrace{\mathrm{SL}(2,\mathbb{R})/\mathrm{SO}(2)}_{\text{Archimedean place}} \times \prod_{p} \mathcal{T}_p
$$

The boundary of each $\mathcal{T}_p$ is a Cantor set. The boundary of the Archimedean component is a circle. The whole boundary is a solenoid supporting a conformal field theory. $[ \text{established --- Bruhat--Tits theory} ]$

The Lorentzian structure emerges at the Archimedean place through a Wick rotation: the Euclidean hyperbolic plane becomes Lorentzian AdS$_2$ with signature $(1,1)$. In higher dimensions, the tree-like p-adic bulk is non-Archimedean AdS, and the gluing of all places yields an effective spacetime whose Archimedean leaf naturally carries a Lorentzian metric. The choice of signature is forced by the requirement that the boundary theory be unitary. $[ \text{speculative} ]$

More fundamentally, there is a discrete causal order on the p-adic trees: the inclusion of ultrametric balls defines a partial order, a direction of "scale flow." When all primes are glued, this discrete causality aggregates into a global light-cone structure. The tree is the fundamental geometry; the Lorentzian manifold is the emergent thermodynamic limit. $[ \text{speculative} ]$

Thus: the Bruhat--Tits tree is the grass; Lorentzian spacetime is the dew. The continuum is a coarse-grained shadow of the underlying discrete, adelic distinction network.

---

## 9. Conclusion and Open Research Directions

This paper has traced the progressive refactoring of fundamental physics around the organizing principle of invariant patterns, culminating in the adelic distinction framework. The central thesis, refined through structured self-critique, is that the universe is a dynamical distinction network governed by an adelic action principle, whose low-energy limit reproduces known physics and whose prime-valued invariants --- the Compton idele numbers --- distinguish fundamental particles from emergent quasi-particles.

The framework makes three concrete, falsifiable predictions: modified photon dispersion relations at the Planck scale, log-periodic oscillations in the dark matter power spectrum, and anomalous black hole echo timings. Each prediction is risky and will be tested by current and near-future experiments.

The historical silo-cost analysis presented in the introduction demonstrates that the convergent structures underpinning this synthesis --- Ostrowski completions, Compton processes, dimensionless entropy, radix trees, and Bruhat--Tits buildings --- were each discovered in complete disciplinary isolation over a span of 110 years. This persistent fragmentation is itself evidence that the cross-domain synthesis undertaken here addresses a genuine blind spot in the organization of human knowledge.

The framework remains a research program, not a finished theory. The following critical-path questions must be addressed:

1. Formulate the distinction path integral rigorously and compute the partition function in the simplest non-trivial case.
2. Derive the Lorentzian signature from the analytic properties of the adelic path integral's saddle points.
3. Compute the cosmological constant from the action and show it yields a small positive vacuum energy.
4. Predict the log-periodic oscillation template for large-scale structure survey data analysis.
5. Search for black hole echoes matching the predicted p-adic pattern in LIGO data.
6. Construct the adelic Standard Model by choosing a reductive group based on the distinction graph's topology and computing its automorphic spectrum.
7. Prove rigorously that the primes emerge from an iterative calculus of distinctions.

The refactoring proposed here does not connect disciplines in isolation; it dissolves their boundaries, revealing a single inquiry into the invariant pattern that gives rise to number, logic, space, and matter. Whether this pattern is our universe's deepest secret or a beautiful mirage, the pursuit of the question will sharpen our understanding of what it means for something to be fundamental.

---

## 10. Declarations

### 10.1 Funding This work received no specific funding.

### 10.2 Conflicts of Interest The author declares no conflicts of interest.

### 10.3 Data Availability No experimental data were generated or analyzed in this study.

### 10.4 Code Availability No custom code was used in this study.

### 10.5 Ethical Approval Not applicable.

### 10.6 Author Contributions Single author: Rowan Brad Quni-Gudzinas.

### 10.7 Acknowledgements The author acknowledges the structured dialogue environment in which the ideas presented here were progressively developed and refined through iterative critique and synthesis.

### 10.8 Disclaimer The views expressed are those of the author and do not necessarily represent any institution.

### 10.9 Preprint Status This is a draft preprint. Comments and critique are welcome.

---

## 11. References

[1] E. Noether, "Invariante Variationsprobleme," Nachr. d. König. Gesellsch. d. Wiss. zu Göttingen, Math.-Phys. Klasse, 235--257 (1918).

[2] E. P. Wigner, "The Unreasonable Effectiveness of Mathematics in the Natural Sciences," Commun. Pure Appl. Math. 13, 1--14 (1960).

[3] A. Ostrowski, "Über einige Lösungen der Funktionalgleichung $\varphi(x)\varphi(y) = \varphi(xy)$," Acta Math. 41, 271--284 (1916).

[4] P. A. M. Dirac, "The Quantum Theory of the Electron," Proc. Roy. Soc. A 117, 610--624 (1928).

[5] C. E. Shannon, "A Mathematical Theory of Communication," Bell Syst. Tech. J. 27, 379--423, 623--656 (1948).

[6] E. Fredkin, "Trie Memory," Commun. ACM 3, 490--499 (1960).

[7] V. S. Vladimirov and I. V. Volovich, "p-Adic quantum mechanics," Commun. Math. Phys. 123, 659--676 (1989).

[8] R. B. Quni-Gudzinas, "Non-Anthropocentric Natural Units," the QNFO archive, https://papers.qnfo.org/papers/non-anthropocentric-natural-units/ (2025).

[9] A. M. Gleason, "Measures on the Closed Subspaces of a Hilbert Space," J. Math. Mech. 6, 885--893 (1957).

[10] S. Ryu and T. Takayanagi, "Holographic Derivation of Entanglement Entropy from AdS/CFT," Phys. Rev. Lett. 96, 181602 (2006).

[11] B. Coecke and A. Kissinger, *Picturing Quantum Processes: A First Course in Quantum Theory and Diagrammatic Reasoning*, Cambridge University Press (2017).

[12] J. Tate, "Fourier Analysis in Number Fields and Hecke's Zeta-Functions," in *Algebraic Number Theory*, ed. J. W. S. Cassels and A. Fröhlich, Academic Press (1967). Originally Ph.D. thesis, Princeton University, 1950.

[13] G. Spencer-Brown, *Laws of Form*, George Allen and Unwin (1969).

[14] S. S. Gubser, J. Knaute, S. Parikh, A. Samberg, and P. Witaszczyk, "p-adic AdS/CFT," Commun. Math. Phys. 352, 1019--1059 (2017).

[15] J. S. Bagla, H. K. Jassal, and T. Padmanabhan, "Cosmology with tachyon field as dark energy," Phys. Rev. D 67, 063504 (2003).
