# Why the Fusion Category of SU(2)_k Chern–Simons Theory Demands a Complex Root of Unity: q = e^{iπ/(k+2)} as an Arithmetic Necessity

## Abstract

Chern–Simons theory with gauge group SU(2) at level k underlies anyon models, topological quantum computation, and the Jones polynomial, yet textbook treatments insert the deformation parameter q = e^{iπ/(k+2)} as a convention. This paper argues that the choice is not conventional but forced, and that the force is arithmetic. We show that the truncation of the representation ring of SU(2) to finitely many simple objects — the defining property of a fusion category — is equivalent to the vanishing of the quantum integer [k+2]_q, which holds if and only if q^{2(k+2)} = 1 with q ≠ ±1. Real values of q fail in opposite ways: q = 1 gives no truncation at all, while q = −1 annihilates every quantum integer and collapses the S-matrix. We carry out explicit derivations for k = 3: the quantum dimensions d = (1, φ, φ, 1) with φ = (1+√5)/2, the total quantum dimension D² = 5 + √5 ≈ 7.2361, the topological spin θ = e^{4πi/5} of the spin-1 anyon, and the verification that the even-spin subcategory is Fibonacci. We interpret the result through the arithmetic program of QNFO: q is an Archimedean artifact, a root of unity whose non-Archimedean reductions carry the same braid phases, supporting the view that anyons are arithmetic patterns rather than particles. The analysis is fully deductive; no simulation or experimental data are used or claimed.

## 1. Introduction

The fusion category Fib_k = SU(2)_k assigns to each anyon type a label a ∈ {0, 1, …, k} and a braided tensor structure. Every construction in the literature — the modular S-matrix, the quantum dimensions, the Jones polynomial at roots of unity, the anyon models used in topological quantum computation — begins with the substitution

  q = e^{iπ/(k+2)}.

The exponent π/(k+2) is usually motivated physically (the Wess–Zumino–Witten action at level k) or representation-theoretically (the path to the Jones polynomial at e^{iπ/(k+2)} and e^{−iπ/(k+2)}). What is rarely stated plainly is why q must be complex at all, and why it must be a root of unity of exactly the right order. A deformation parameter could in principle be any nonzero complex number; the claim that topology on a three-manifold selects e^{iπ/(k+2)} out of ℂ^× demands a proof.

This paper supplies such a proof, in three moves. First, we isolate the property that does the work: the quantum integer [n]_q, and the requirement that [k+2]_q = 0, which is what makes the (k+1)-dimensional SU(2) representation decompose and the truncated category close under fusion with finitely many simples. Second, we solve the condition exactly: [k+2]_q = 0 together with non-degeneracy forces q^{2(k+2)} = 1 and q ∉ {±1}, i.e., q is a primitive 2(k+2)-th root of unity, hence non-real for every k ≥ 1. Third, we verify the resulting structure numerically and symbolically for the simplest nontrivial case with interesting anyons, k = 3, deriving every number from first principles.

The interpretation we develop connects this necessity to the arithmetic program of the QNFO corpus. In [9], anyons are proposed to be *adelic patterns* — structures living simultaneously at all places of a number field, not particles in space. In [10], the roots of unity that carry braid phases are read as arithmetic objects tied to bounded-occupation (Gentile) statistics. In [11], Tate's thesis supplies the template: local computations at each place, glued globally, with the Archimedean place producing "artifacts" — objects like e^{iπ/(k+2)} that look analytic but encode arithmetic. Our result is a concrete instance of that template: the complex phase q is the Archimedean shadow of a root-of-unity condition that is fundamentally number-theoretic. The consilience argument of [12] — that ultrametric geometry is the correct substrate — gains a small but exact piece of evidence: the one number Chern–Simons theory cannot avoid choosing is a root of unity, the native inhabitant of both the Archimedean circle and every non-Archimedean residue field.

Chern–Simons theory itself is a broad subject; the bibliography samples its monopole operators [1], noncommutative deformations [2, 3], Wilson and Seifert loops [5], string-theoretic origins [6], supergravity extensions [7], and matter-coupled collective dynamics [8], alongside the fusion-category literature [4]. Our question cuts across all of these: whatever the embedding, the category of line operators at level k is the same fusion category, and its existence pins down q.

## 2. Background and Related Work

We review the twelve works of the bibliography in order, extracting what each contributes to the question of q's arithmetic character.

[1] studies monopole operators in three-dimensional Chern–Simons–matter theories via the state-operator map, as states on ℝ × S² with background magnetic flux, with gauge-invariant dressings by matter modes supplying the monopoles' spin. The relevance is structural: even when matter is added and operators are constructed on ℝ³ rather than S², the spin and statistics of the resulting objects are quantized by the same root-of-unity arithmetic that fixes q in the pure theory. Monopole operators are the matter-coupled cousins of the anyons whose fusion category we analyze.

[2] proves one-loop finiteness of the non-Abelian noncommutative supersymmetric Chern–Simons action with U(N) gauge group, for gauge superpotential in the fundamental representation. Noncommutative deformations of Chern–Simons are a parallel deformation axis to the q-deformation studied here; the finiteness result shows that the gauge-theoretic side tolerates deformation, while the fusion-category side, we will show, does not tolerate deformation away from roots of unity. The contrast sharpens our claim: q is rigid where other parameters are soft.

[3] constructs a Chern–Simons action on noncommutative spaces, with SU_q(2) as the leading example (the paper's content is contained in its companion arXiv:1204.0418v2). This is the closest relative to our subject: SU_q(2) is precisely the Hopf algebra whose representation category is the fusion category SU(2)_k when q is a root of unity of order 2(k+2). That a noncommutative-space action exists specifically for SU_q(2) confirms that the root-of-unity value of q is not an artifact of canonical quantization but survives in deformation-based formulations.

[4] determines the fusion rules of equivariantizations of a fusion category ℂ under a finite group G, in terms of the fusion rules of ℂ and group-theoretic data, with a pointed-fusion-category application. Equivariantization is one of the standard operations that build new anyon theories from old. Our analysis supplies the input such operations require: a semisimple, finite fusion category in the first place. The truncation condition q^{2(k+2)} = 1 is the gate through which every equivariantization of SU(2)_k-type categories must pass, and the Galois-type label permutations we discuss in Section 6 are of exactly the kind [4] systematizes.

[5] gives Wilson and Seifert loop observables in Chern–Simons theory on Seifert three-manifolds a symplectic interpretation, analogously to the Atiyah–Bott reading of Yang–Mills as the norm-square of a moment map. Wilson loops are the line operators whose category is SU(2)_k; the symplectic viewpoint makes the quantization of the loop phase — a root of unity — visible as an integrality condition on a coadjoint orbit, prefiguring the arithmetic necessity we prove algebraically.

[6] shows that near degenerating three-cycles in Calabi–Yau moduli space, the low-energy effective action of type IIA string theory contains Chern–Simons terms whose world-volume description is Chern–Simons theory on the cycle. This situates SU(2)_k Chern–Simons inside string theory, where the level k and hence the root of unity q = e^{iπ/(k+2)} arise from geometry (the Chern class of the cycle). The geometric origin and the arithmetic necessity are compatible: both select integers, and integers select roots of unity.

[7] constructs exact selfdual-curvature solutions in five-dimensional N=2 Chern–Simons supergravity on M₄ × ℝ, with a fine-tuned Kaluza–Klein reduction setting the four-dimensional cosmological constant to zero. Selfdual fields are the higher-dimensional analogues of the holomorphic anyon data: their phases are quantized, and the quantization again lands on roots of unity. The paper illustrates how broadly the root-of-unity phenomenon repeats across Chern–Simons family members.

[8] derives, from a large-N Chern–Simons matter theory (the attractive Jackiw–Pi model) in collective-field form, that density excitations around the ground state obey Calogero or Sutherland Hamiltonians depending on soliton configuration symmetry. The Calogero–Sutherland connection is significant for us because those models are themselves tied to root-of-unity parameter values (the coupling at rational values), echoing the arithmetic selectivity we prove for q.

[9] (DOI 10.5281/zenodo.22741636) proposes the adelic synthesis: anyons are adelic patterns rather than particles, unifying place-specific constructions, and proposes Adelic Topological Quantum Computation. Our theorem is a local instance of its program: the Archimedean place produces the complex phase e^{iπ/(k+2)}, and we show this phase is forced by a condition — q^{2(k+2)} = 1 — that is simultaneously a statement about roots of unity in every residue field.

[10] (DOI 10.5281/zenodo.22124744) reads the two three-dimensional exchange statistics as maximum-entropy occupations of one integer lattice under two multiplicity rules, and identifies the roots of unity that carry braid phases, closing with the bounded-occupation family correspondence. Our explicit computation of θ = e^{4πi/5} for the k = 3 spin-1 anyon is exactly one of the roots of unity that [10] argues carry braid phases; the present paper derives it from the truncation condition rather than the entropy argument, an independent route to the same arithmetic object.

[11] (DOI 10.5281/zenodo.21600741) proposes Tate's 1950 thesis as a structural template for adelic quantum mechanics, noting the Dragovich program's realization for free theories and the independent proof-of-concept of Huang, Stoica, and Zhong (2022) in CFT. We adopt the template's key vocabulary: q = e^{iπ/(k+2)} is an *Archimedean artifact* — a manifestly complex number whose defining property (being a root of unity) is arithmetic and whose non-Archimedean reductions ζ mod 𝔭 are roots of unity in finite fields, where the same fusion rules can be written.

[12] (DOI 10.5281/zenodo.21603374) documents consilient convergence of five QNFO research programs on the insight that ultrametric mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization. The present paper contributes a sixth, exactly-checkable data point: the unique parameter of SU(2)_k Chern–Simons is an ultrametric-native object (a root of unity) wearing Archimedean dress.

## 3. Methods

The method is exact symbolic derivation from the standard construction of the SU(2)_k fusion category, which we recall in the notation used throughout.

**Setup.** The simple objects of SU(2)_k are labeled a = 0, 1, …, k, corresponding to the spin-j = a/2 irreducible representations of SU(2). The deformation parameter q enters through the quantum integer

  [n]_q = (q^n − q^{−n}) / (q − q^{−1}),

the q-analogue of the dimension n of the spin-0… the (n−1)-symmetric-tensor representation. The fusion rules are

  a × b = ⊕_c N_{ab}^c · c,  N_{ab}^c = 1 if |a − b| ≤ c ≤ min(a + b, 2k − a − b) and a + b + c even, else 0.

The quantum dimension of object a is d_a = [a+1]_q, the modular S-matrix is S_{ab} = √(2/(k+2)) · sin((a+1)(b+1)π/(k+2)), and the topological spin is θ_a = exp(2πi h_a) with h_a = a(a+2)/(4(k+2)).

**Method, step 1: identify the load-bearing condition.** A fusion category must be ℂ-linear semisimple with finitely many simple objects and simple unit. For the q-deformed representation category of SU(2), finiteness of the simple-object set fails at generic q: the symmetric tensors of every degree remain simple and pairwise non-isomorphic, giving infinitely many simples. The category becomes a fusion category precisely when the degree-(k+2) symmetric tensor becomes reducible, which happens exactly when its quantum dimension [k+2]_q vanishes. We therefore take as the defining condition:

  (T): [k+2]_q = 0, with the category non-degenerate (not all [n]_q = 0).

**Method, step 2: solve (T) exactly.** We solve the equation [k+2]_q = 0 over ℂ^× by direct algebra, distinguishing the real and complex cases, and derive the order of q as a root of unity.

**Method, step 3: verify consequences for k = 3.** With q = e^{iπ/5} fixed by step 2, we compute: (i) all four quantum dimensions d_0, d_1, d_2, d_3 exactly and numerically; (ii) the total quantum dimension D² = Σ_a d_a², both by direct summation and by the closed formula (k+2)/(2 sin²(π/(k+2))), as a consistency check; (iii) the topological spin of the a = 2 anyon; (iv) the fusion rules of the even-spin subcategory {0, 2} and the check that its fusion coefficients match its quantum dimensions (Fibonacci structure). Every input number is either a definition, a standard identity (sin(2x) = 2 sin x cos x; cos(π/5) = (1+√5)/4), or derived in-line.

**Method, step 4: interpret.** We place the solved condition in the arithmetic frame of [9, 10, 11, 12]: q as an Archimedean artifact whose defining property is place-independent.

No numerical simulation, sampling, or experimental data are used anywhere; every number in Section 5 is produced by the arithmetic of Sections 3–4.

## 4. Analysis

### 4.1 The truncation condition and its exact solution

**Input (definition).** [n]_q = (q^n − q^{−n})/(q − q^{−1}) for q ∈ ℂ^×, q ≠ ±1 (at q = ±1 the expression is 0/0 and must be treated separately, below).

**Condition (T):** [k+2]_q = 0.

  [k+2]_q = 0
  ⟺ q^{k+2} − q^{−(k+2)} = 0   (numerator vanishes; denominator q − q^{−1} ≠ 0 by assumption)
  ⟺ q^{k+2} = q^{−(k+2)}
  ⟺ q^{2(k+2)} = 1.

So (T) holds if and only if q is a 2(k+2)-th root of unity. **Non-degeneracy** excludes the cases where every [n]_q vanishes: that happens iff q = q^{−1}, i.e., q = ±1, both of which satisfy q^{2(k+2)} = 1 trivially but are excluded by q ≠ ±1 in the definition. Hence:

  **(Necessity):** q is a root of unity with q^{2(k+2)} = 1 and q ≠ ±1.

**q is non-real for every k ≥ 1.** The real roots of unity are ±1, both excluded. The order of q divides 2(k+2) ≥ 6 for k ≥ 1; a real number of order ≥ 3 does not exist (the only real elements of any cyclic root-of-unity group are of order 1 and 2). Therefore q ∉ ℝ for all k ≥ 1. For k = 0, 2(k+2) = 2 and q = −1, the degenerate excluded case; the k = 0 theory has a single simple object and no braiding content, so no nontrivial theory is lost. ∎

**Why q = 1 fails (no truncation).** At q = 1, the limit [n]_1 = n (L'Hôpital or the defining limit of the q-integer): lim_{q→1} (q^n −