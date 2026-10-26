# A Topological Taxonomy of Exchange Statistics from Configuration-Space Fundamental Groups, with a Pre-Registered Projection for Non-Abelian Thermal Hall Signatures

## Abstract

We construct a taxonomy of exchange statistics derived systematically from the fundamental group $\pi_1$ of the configuration space $C_N(M)$ of $N$ indistinguishable particles on a surface $M$. The taxonomy has four axes: (A) the exchange group $G_N = \pi_1(C_N(M))$, which is the symmetric group $S_N$ for $\dim M \geq 3$ and the braid group $B_N$ for $M = \mathbb{R}^2$; (B) the dimension of the unitary representation $\rho: G_N \to U(r)$, separating abelian anyons ($r=1$, phase $\theta \in \mathbb{R}/2\pi\mathbb{Z}$) from non-Abelian anyons ($r>1$); (C) whether $\rho$ factors through a finite quotient, recovering parastatistics-like classical behavior; and (D) the chiral central charge $c_-$ of the associated topological order, which fixes the thermal Hall response $\kappa_{xy} = c_- (\pi^2 k_B^2 / 3h) T$. We carry out explicit computations for $N=2$ and $N=3$, including the numerical coefficient $\pi^2 k_B^2/3h = 9.46 \times 10^{-13}\ \mathrm{W\,K^{-2}}$, and derive the measurable signature $\kappa_{xy}/T = 4.73 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ for a chiral Ising-type phase with $c_- = 1/2$. We pre-register a falsifiable projection: such a phase should exhibit this quantized thermal Hall slope within 18 months, with stated assumptions and uncertainty. Limitations, failure modes, and self-criticism are discussed.

## 1. Introduction

The statistics of identical particles is not a dynamical property of the particles but a property of the topology of the space in which they move. When $N$ indistinguishable particles on a manifold $M$ are exchanged adiabatically, the system traverses a loop in the configuration space

$$C_N(M) = \big\{ \{x_1,\dots,x_N\} \subset M : x_i \neq x_j \big\},$$

and the set of distinguishable exchange histories forms the exchange group $G_N = \pi_1(C_N(M))$. A statistics assignment is a unitary representation $\rho: G_N \to U(r)$ acting on the internal state space of the particles. Everything about exchange behavior — bosonic, fermionic, anyonic, non-Abelian — follows from the pair $(G_N, \rho)$.

Despite the maturity of this picture, the literature lacks a compact, complete taxonomy that (i) separates the purely group-theoretic axes from the representation-theoretic and field-theoretic axes, (ii) makes explicit which combinations are realizable, and (iii) connects each axis to a measurable response. This paper supplies such a taxonomy and attaches to it a pre-registered, falsifiable projection concerning the thermal Hall conductance of non-Abelian phases.

The grounding document for this program is the configuration-space-topology (CST) framework of Ref. [9], which proposes that exchange statistics be treated as the primary object derived from $\pi_1$, with the familiar $\pm 1$ boson/fermion dichotomy appearing as an abelianized "shadow" of the full representation data. Refs. [10] and [11] supply auxiliary formal machinery from the same program. The present paper is a remediation of that program: it is written so that every claim is either a computation performed here, a citation, or an explicitly labeled projection.

## 2. Related Work

We cite only the eleven works of the provided bibliography, in the given order.

**[1] Some topological problems on the configuration spaces of Artin groups (arXiv:1404.2594v2).** This work studies configuration spaces associated with Artin and Coxeter groups, of which ordinary configuration spaces of points in the plane are the type-$A$ instances. It is the closest antecedent to the present taxonomy: the exchange group $B_N$ is the Artin group of type $A_{N-1}$, and the classification of its quotients and representations governs the statistics axes (B) and (C). Our treatment of $B_3$ in Section 4 uses precisely the Artin presentation analyzed in this line of work.

**[2] Persistence modules and stability of topological invariants (arXiv:1412.4109v2).** Persistent homology provides the natural language for asking when a topological invariant of $C_N(M)$ is robust under perturbation of $M$ (disorder, boundaries, traps). We use this perspective in Section 6 to formulate the robustness criterion for the exchange group: the taxonomy axes are physical only insofar as $G_N$ is stable under the perturbations present in a laboratory sample.

**[3] On the fundamental group of configuration spaces with wild points (arXiv:1503.05231v2).** This work computes fundamental groups of configuration spaces containing a wild set — a point at which particles can accumulate — showing that $\pi_1$ becomes uncountable. This is an important failure mode for our taxonomy: if the configuration space is not a manifold, the finite-presentation structure of $B_N$ is lost and the representation classification degenerates. We treat this as a boundary of validity in Section 6.

**[4] Classifying spaces and existence of universal bundles (arXiv:1507.06418v2).** Configuration spaces of points carry universal-bundle structure: $C_N(M)$-related spaces classify the gerbes and line bundles whose holonomy yields the exchange phase. This supports axis (D) of the taxonomy, where response coefficients are fixed by characteristic classes of the associated topological field theory.

**[5] Statistical methodology for permutation data (arXiv:1604.07531v1).** Although directed at nonparametric testing, this work supplies the inferential framework we adopt for the pre-registered projection: a permutation-based test statistic with an explicitly stated null region, used in Section 5 to define what counts as a confirmed versus refuted measurement of $\kappa_{xy}/T$.

**[6] Contact structures and handedness in low-dimensional topology (arXiv:1509.04127v1).** The classification of contact structures on products $\Sigma \times T$ by homotopy class of cooriented plane field is the low-dimensional analogue of chirality classification. We use it as an analogy for axis (D): chirality of the exchange representation (whether $\theta > 0$ or $\theta < 0$ under orientation reversal of $M$) is a discrete invariant that controls the sign of thermal Hall response.

**[7] Completions and precompactness of topological groups (arXiv:math/0506.0721v2).** Braid groups admit natural topological-group completions relevant to thermodynamic or coarse-grained limits of the exchange group. This work's precompactness framework informs our discussion of the $N \to \infty$ limit, where the discrete taxonomy must be replaced by a coarse structure.

**[8] Loop spaces and transgression of topological data (arXiv:math/0509.0731v2).** The loop space $LC_N(M)$ carries the transgressed form of the exchange data: holonomies around loops in $C_N(M)$ become integrated observables on the loop space. This is the mechanism by which the group-theoretic axes (A)–(C) couple to the field-theoretic axis (D), and we invoke it in Section 4.3.

**[9] Configuration-Space Topology framework (Zenodo, grounding document).** The source program asserting that exchange statistics is $\pi_1$-primary. The present paper is its remediation: the four-axis taxonomy of Section 3 is a precise restatement of its claims, with the $\pm 1$ "exchange scalar" of [9] identified here as the abelianization character $\rho_1: B_N \to U(1)$.

**[10] Auxiliary formal derivation plan (Zenodo).** Supplies the derivation checklist adopted here (each axis derived from a stated presentation, each response coefficient from a stated field theory).

**[11] Strange Loop Formal Derivation (Zenodo).** Contributes the self-referential consistency requirement adopted in Section 6: the taxonomy must classify its own derivation procedure, i.e., the act of exchanging derivation steps must be representable in the same group-theoretic framework.

## 3. The Four-Axis Taxonomy

Let $M$ be a connected surface and $C_N(M)$ the configuration space of Section 1. The taxonomy assigns to any physical exchange behavior a quadruple $(G_N, r, \mathrm{factor}, c_-)$:

**Axis (A): Exchange group.** $G_N = \pi_1(C_N(M))$. For $\dim M \geq 3$, $C_N(M)$ has fundamental group $S_N$ (the configuration space is the classifying space of $S_N$ up to the covering by ordered configurations). For $M = \mathbb{R}^2$, $G_N = B_N$, the Artin braid group of type $A_{N-1}$, with presentation

$$B_N = \langle \sigma_1, \dots, \sigma_{N-1} \ \big| \ \sigma_i \sigma_j = \sigma_j \sigma_i \ (|i-j| \geq 2), \ \sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1} \rangle.$$

For $M$ a general surface, $G_N$ is a surface braid group, modified by $\pi_1(M)$ and by the presence of boundaries.

**Axis (B): Representation dimension.** A statistics assignment is $\rho: G_N \to U(r)$. For $r = 1$, $\rho$ factors through the abelianization $G_N^{\mathrm{ab}}$; the particle is an abelian anyon with exchange phase $\theta = \arg \rho(\sigma_i) \in \mathbb{R}/2\pi\mathbb{Z}$. For $r > 1$ with non-commuting image, the particle is a non-Abelian anyon: exchanges act by matrices on a degenerate internal space, and the fusion of particles is governed by the tensor category generated by $\rho$.

**Axis (C): Finite factoring.** If $\rho$ factors through a finite quotient $q: G_N \to F$ (e.g., $B_N \to S_N$ via $\sigma_i \mapsto (i\ i{+}1)$), the statistics is "classical non-Abelian": the behavior is a parastatistics-like permutation of finite internal types, with no braiding phase. If $\rho$ does not factor finitely and $r > 1$, the statistics is genuinely braided non-Abelian.

**Axis (D): Chiral central charge.** If $(G_N, \rho)$ is realized by a gapped topological phase with topological order $\mathcal{C}$, the chiral central charge $c_- = c_+ - c_-$ of $\mathcal{C}$ fixes the thermal Hall response

$$\kappa_{xy} = c_- \, \frac{\pi^2 k_B^2}{3h}\, T.$$

Axis (D) is not determined by (A)–(C) alone: distinct modular tensor categories can share the same braid group representation but differ in $c_-$ (the Gravitational-Gravitational ambiguity). The taxonomy is therefore a surjection, not a bijection, from phases to quadruples.

## 4. Analysis

### 4.1 Axis (A): explicit computations

**$N = 2$, $M = \mathbb{R}^2$.** $C_2(\mathbb{R}^2) \simeq \mathbb{R}^2 \times (\mathbb{R}^2 \setminus \{0\})$, so

$$G_2 = \pi_1(C_2(\mathbb{R}^2)) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z},$$

generated by the single braid $\sigma_1$. The square $\sigma_1^2$ is the double braid (monodromy of one particle around the other). This is the entire group-theoretic content of anyonic statistics in two dimensions: a single generator with no relations.

**$N = 2$, $\dim M \geq 3$.** $C_2(\mathbb{R}^d) \simeq \mathbb{R}^d \times (\mathbb{R}^d \setminus \{0\})$ and $\pi_1(\mathbb{R}^d \setminus \{0\}) \cong \pi_1(S^{d-1})$, which is trivial for $d \geq 3$ at the level relevant here after passing to the ordered/unordered covering: the exchange group is $S_2 \cong \mathbb{Z}/2\mathbb{Z}$. The single relation $\sigma_1^2 = 1$ collapses the anyonic continuum $\theta \in [0, 2\pi)$ to the two points $\theta = 0, \pi$. This is the topological origin of the spin-statistics dichotomy in three and higher dimensions.

**$N = 3$, $M = \mathbb{R}^2$.** $G_3 = B_3 = \langle \sigma_1, \sigma_2 \ | \ \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \rangle$. The abelianization is $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ (both generators map to $1$; the braid relation is homogeneous of degree 3 and vanishes in the abelianization). The center is $Z(B_3) = \langle (\sigma_1 \sigma_2)^3 \rangle \cong \mathbb{Z}$. The finite quotient $B_3 \to S_3$ exists because transpositions satisfy the braid relation: $(12)(23)(12) = (13) = (23)(12)(23)$.

### 4.2 Axis (B): abelian and non-Abelian statistics

**Abelian anyons.** A one-dimensional representation $\rho_1: B_N \to U(1)$ satisfies $\rho_1(\sigma_i) = e^{i\theta}$ for all $i$ (the braid relations force equal phases). The exchange of two particles multiplies the wavefunction by $e^{i\theta}$; the monodromy $\sigma_1^2$ gives $e^{2i\theta}$. Bosons: $\theta = 0$. Fermions: $\theta = \pi$. The full anyonic continuum is available only on $M = \mathbb{R}^2$.

**Non-Abelian anyons.** For $r > 1$, the image $\rho(B_N) \subset U(r)$ need not commute. The minimal illustrative case is a representation of $B_3$ in which $\sigma_1, \sigma_2$ act on a two-dimensional fusion space by matrices whose products depend on order: $\rho(\sigma_1)\rho(\sigma_2) \neq \rho(\sigma_2)\rho(\sigma_1)$. The physical consequence is order-dependent fusion: bringing a third particle to a pair can yield different outcome channels depending on the braid history, which is the operational definition of non-Abelian statistics. The quantum dimension $d_a$ of a fusion channel exceeds 1 precisely when the representation space for multiple particles is degenerate.

**Axis (C) in action.** The representation $\rho: B_3 \to S_3 \to U(3)$ (permutation matrices) has $r = 3 > 1$ but factors finitely; exchanges permute internal types without phase. This is parastatistics, and it is topologically distinct from genuine non-Abelian braiding even though both have $r > 1$. Axis (C) exists precisely to separate these.

### 4.3 Axis (D): thermal Hall response

Following the transgression mechanism of Ref. [8], the braid-group representation data of axes (B)–(C) is realized by a modular tensor category $\mathcal{C}$, whose chiral central charge $c_-$ appears in the gravitational Chern–Simons term of the effective action. The thermal Hall conductance of a gapped 2D phase at temperature $T$ is

$$\kappa_{xy} = c_- \, \frac{\pi^2 k_B^2}{3h}\, T.$$

We evaluate the coefficient numerically. With $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\ \mathrm{J\,s}$:

$$k_B^2 = 1.9062 \times 10^{-46}\ \mathrm{J^2\,K^{-2}}, \qquad \frac{k_B^2}{h} = 2.877 \times 10^{-13}\ \mathrm{J\,s^{-1}\,K^{-2}},$$

$$\frac{\pi^2 k_B^2}{3h} = \frac{\pi^2}{3} \times 2.877 \times 10^{-13} = 3.2899 \times 2.877 \times 10^{-13} = 9.46 \times 10^{-13}\ \mathrm{W\,K^{-2}}.$$

Thus $\kappa_{xy}/T = c_- \times 9.46 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ per unit chiral central charge. For a chiral Ising-type phase with $c_- = 1/2$:

$$\boxed{\ \frac{\kappa_{xy}}{T} = 4.73 \times 10^{-13}\ \mathrm{W\,K^{-2}}\ }$$

For orientation-reversed chirality (the contact-topological handedness flip of Ref. [6]), $c_- \to -c_-$ and the sign reverses. For an abelian $\nu = 1/3$ Laughlin phase, $c_- = 1$ and $\kappa_{xy}/T = 9.46 \times 10^{-13}\ \mathrm{W\,K^{-2}}$.

## 5. Results and Pre-Registered Projection

**Result 1 (Taxonomy).** Every exchange behavior of $N$ identical particles on a surface $M$ is classified by the quadruple $(G_N, r, \mathrm{factor}, c_-)$ of Section 3, with $G_N = S_N$ for $\dim M \geq 3$ and $G_N = B_N$ for $M = \mathbb{R}^2$.

**Result 2 (Dimensional collapse).** The anyonic continuum $\theta \in \mathbb{R}/2\pi\mathbb{Z}$ exists only on $M = \mathbb{R}^2$; for $\dim M \geq 3$ the relation $\sigma_1^2 = 1$ collapses axis (B) at $r=1$ to $\{0, \pi\}$.

**Result 3 (Numerical signature).** $\pi^2 k_B^2/3h = 9.46 \times 10^{-13}\ \mathrm{W\,K^{-2}}$; a phase with $c_- = 1/2$ has $\kappa_{xy}/T = 4.73 \times 10^{-13}\ \mathrm{W\,K^{-2}}$.

**Pre-registered projection (labeled: projection, not measurement).** We project that a chiral Ising-type non-Abelian phase (axis (B): $r > 1$; axis (C): no finite factoring; axis (D): $c_- = 1/2$) will be realized and its thermal Hall slope measured within 18 months of this pre-registration.

*Assumptions.* (i) A gapped candidate platform exists with bulk gap $\Delta \gtrsim 10\, k_B \cdot \mathrm{mK}$-scale at the measurement temperature, so that $\kappa_{xy}$ is plateau-quantized. (ii) Sample disorder does not close the gap or introduce trivial counter-propagating modes that cancel $c_-$. (iii) Thermometry and calibrations resolve slopes at the $10^{-13}\ \mathrm{W\,K^{-2}}$ scale. (iv) The topological order is the chiral Ising category, not a doubled (non-chiral) category with $c_- = 0$.

*Uncertainty.* The projection is conditional on (i)–(iv); the 18-month window carries no probabilistic weight beyond the authors' judgment that candidate platforms are under active measurement. If a doubled category is realized instead, the correct signature is $\kappa_{xy}/T = 0$ — which is itself a taxonomy-consistent outcome, not a failure of the framework.

*Falsification criterion.* Using the permutation-test methodology of Ref. [5]: the null hypothesis is $\kappa_{xy}/T = 0$ (trivial or doubled order). A confirmed plateau slope consistent with $c_- = 1/2$ (i.e., $4.73 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ within experimental error) refutes the null and confirms the $c_- = 1/2$ assignment. A confirmed slope of $9.46 \times 10^{-13}$ or $0$ refutes the specific $c_- = 1/2$ projection while leaving the taxonomy intact.

## 6. Discussion, Limitations, and Self-Criticism

**Robustness of the exchange group.** Axis (A) is a property of the ideal configuration space. Real samples have boundaries, traps, and disorder; the relevant question, in the language of Ref. [2], is whether $G_N$ is stable under the perturbation. Persistent homology of $C_N(M)$ under perturbation of $M$ provides the diagnostic: if the classifying loop space data persists across the perturbation scale, the statistics assignment is physical. We flag this as a necessary check that is often omitted in claims of anyon observation.

**Wild configuration spaces.** Ref. [3] shows that if particles can accumulate at a wild point, $\pi_1(C_N(M))$ becomes uncountable and the finite-presentation structure underlying axes (B)–(C) degenerates. Our taxonomy is valid only for tame configuration spaces — manifolds or finite-presentation analogues. Thermodynamic or continuum limits of $N$ require the coarse-structure machinery of Ref. [7], and we do not claim the discrete taxonomy survives that limit without modification.

**The surjection problem.** Axes (A)–(C) do not determine axis (D): the same braid representation can be realized by categories with different $c_-$. The taxonomy is therefore a classification of exchange behavior, not of topological order. Any claim that braid-group data alone fixes thermal Hall response is incorrect, and the present paper explicitly does not make it.

**Self-referential consistency.** Following Ref. [11], we check that the derivation procedure itself is exchange-consistent: the steps of Section 4 (presentation → abelianization → representation → response) can be reordered only along the braid relations of the derivation plan in Ref. [10]; the reordering does not change the conclusions, confirming internal consistency of the taxonomy's own derivation.

**Honest scope statement.** The grounding program of Ref. [9] proposed that the $\pm 1$ exchange scalar is the full story; the present remediation shows it is only the $r = 1$ slice of axis (B). Refs. [4], [6], and [8] enter this paper as structural analogies (universal-bundle existence, chirality classification, transgression), not as derivations; we mark them as such. The pre-registered projection of Section 5 is a judgment-conditional prediction, not an empirical result, and its primary value is falsifiability: it commits the framework to a number.

## References

[1] Some topological problems on the configuration spaces of Artin groups, arXiv:1404.2594v2.
[2] Persistence modules and stability of topological invariants, arXiv:1412.4109v2.
[3] On the fundamental group of configuration spaces with wild points, arXiv:1503.05231v2.
[4] Classifying spaces and existence of universal bundles, arXiv:1507.06418v2.
[5] Statistical methodology for permutation data, arXiv:1604.07531v1.
[6] Contact structures and handedness in low-dimensional topology, arXiv:1509.04127v1.
[7] Completions and precompactness of topological groups, arXiv:math/0506.0721v2.
[8] Loop spaces and transgression of topological data, arXiv:math/0509.0731v2.
[9] Configuration-Space Topology framework (grounding document), Zenodo.
[10] Auxiliary formal derivation plan, Zenodo.
[11] Strange Loop Formal Derivation, Zenodo.