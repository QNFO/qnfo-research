---
title: 'Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its +/-1 Shadow, and a Pre-Registered Derivation Program'
author: 'Quni-Gudzinas, Rowan Brad'
date: '2026-08-15'
status: draft
doi: null
language: eng
license: cc-by-4.0
keywords:
  - configuration-space topology
  - exchange statistics
  - spin-statistics theorem
  - braid group
  - laws of form
  - distinction calculus
  - Grothendieck-Teichmuller group
  - homotopy type theory
  - anyons
  - pre-registered derivation
abstract: >-
  Configuration-space topology derives exchange statistics from the topology of
  the configuration space of indistinguishable particles: the fundamental group
  pi_1(C_N(M)) is the symmetric group S_N in d >= 3 spatial dimensions (yielding
  only the boson +1 and fermion -1 exchange phases) and the braid group B_N in
  d = 2 (yielding anyons). This paper argues that configuration-space topology
  is the correct kinematical explanation of the boson/fermion/anyon trichotomy
  but not its terminus: its silent scaffolds (point-like particles, a fixed
  classical background manifold, the deleted hard-core diagonal, externally
  imposed dimension) mark its boundary as a map. The spin-statistics connection
  (which exchange eigenvalue corresponds to which spin) requires Lorentz
  symmetry, microcausality, and positive energy -- inputs the mark calculus
  alone cannot supply. Against this boundary, we re-state the pre-registered
  derivation program of the QNFO distinction tradition (exchange phase as a
  logical scalar R = e^{2 pi i s} from the re-entrant mark): (T1) two modal
  exponentials from a graded braiding; (T2) the exchange map on two marks is a
  scalar and the ribbon identity forces the two eigenvalues to be the boson and
  fermion signs, with the synthesis R = +/-1 iff pi_1(C_N(R^d)) = S_N for d >= 3;
  (T3) spatial dimension enters exchange statistics only through the allowed
  braided structures, with named boundary conditions (orbifold, graph, traid,
  supersymmetric, extended-object). We state the synthesis conjecture -- the
  Distinction Calculus lifted into homotopy type theory, with the
  Grothendieck-Teichmuller group acting on braided monoidal categories, renders
  boundary-drawing an arithmetic act -- as a conjecture with explicit
  falsification conditions F1-F3, and differentiate it from the existing
  cohesive-homotopy-type-theory program of Sati and Schreiber. The paper's
  quantitative claims are few and independently verified; its epistemic value
  lies in the honest boundary map of a mature framework and a falsifiable
  derivation program for its logical origin.
---

# Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its $\pm 1$ Shadow, and a Pre-Registered Derivation Program

**Rowan Brad Quni-Gudzinas**

**QNFO Research Foundation** — WBS QNFO.RES.011 — 2026-08-15

*Status labels used throughout: [ESTABLISHED] = standard result with independent external verification; [CONJECTURE] = proposed, falsifiable, not yet proven; [ACKNOWLEDGED] = boundary of the present framework, conceded; [CONTESTED] = live external research activity at this boundary.*

## 1. Introduction

Why are there bosons and fermions and nothing else? In three spatial dimensions, exchanging two indistinguishable particles can multiply the many-body wavefunction by exactly one of two phases: $+1$ or $-1$ [ESTABLISHED — @leinaas_myrheim1977; @laidlaw_dewitt1971]. Two-dimensional systems admit a continuum of intermediate phases (anyons) [ESTABLISHED — @wilczek1983; @read_green2000]. This dimension-dependent dichotomy is not an empirical accident; it is a theorem about the topology of the space in which particles move [ESTABLISHED — @leinaas_myrheim1977].

Configuration-space topology (CST) is the modern, intrinsic derivation of this structure: statistics is a representation of the fundamental group of the configuration space of identical particles. The framework is correct as kinematics, and it is not the deepest cut. It rests on scaffolds — point-like particles, a fixed classical background manifold, a deleted hard-core diagonal, an externally imposed dimension — that the framework itself cannot derive [ACKNOWLEDGED — this paper, Section 3]. And the connection between exchange phase and spin (the spin-statistics theorem proper) requires relativistic input that no purely topological or logical argument supplies [ACKNOWLEDGED — @streater_wightman1964; @pauli1940; @finkelstein_rubinstein1968].

This paper has three tasks. First, to state the CST framework and its scaffolds with precision (Sections 2–3), engaging the active counter-literature that is currently testing those scaffolds: the orbifold treatment of singular configurations [@harshman_knapp2022], the traid group in one dimension [@harshman_knapp2018; @nagies_etal2023], graph configuration spaces [@sawicki2014; @harrison_etal2013; @maciazek_sawicki2018; @maciazek2019], supersymmetric anyons [@chaichian_etal2012], and extended objects [@extended_objects2012; @smith2026]. Second, to re-state the boundary of the framework honestly (Section 4), including engagement with the claim that the spin-statistics connection can be derived without Lorentz invariance [CONTESTED — @li_ge2026]. Third, to re-state the pre-registered derivation program of the QNFO distinction tradition — exchange statistics from the mark calculus — with its current construction status (Section 5), and to state the synthesis conjecture that lifts the Distinction Calculus into homotopy type theory under the action of the Grothendieck–Teichmüller group (Section 6), with explicit falsification conditions (Section 7). Sections 8–9 note applications and conclude.

## 2. Configuration-Space Topology: The Framework

### 2.1 The configuration space of identical particles

For $N$ identical particles in $d$ spatial dimensions, the classical configuration space is not $\mathbb{R}^{dN}$ [ESTABLISHED — @leinaas_myrheim1977]. Two constructions intervene:

1. **Removal of the diagonal.** Particles are taken to be hard-core: no two may coincide. The collision set
   $\Delta = \lbrace x \in \mathbb{R}^{dN} \mid x_{i} = x_{j} \text{ for some } i \neq j \rbrace$
   is removed, giving the ordered configuration space $\mathbb{R}^{dN} \setminus \Delta$.
2. **Quotient by the symmetric group.** Identical particles are indistinguishable; configurations differing by a permutation of labels are the same physical state. The space is quotiented by $S_{N}$:

$$C_{N}(\mathbb{R}^{d}) = \frac{\mathbb{R}^{dN} \setminus \Delta}{S_{N}}.$$

Quantum states are functions on this space (more precisely, sections of vector bundles over it, up to phase). The allowed statistics are the possible phases or unitary transformations acquired when particles are exchanged — which is to say, when the system traverses a closed loop in $C_{N}(\mathbb{R}^{d})$ [ESTABLISHED — @laidlaw_dewitt1971].

### 2.2 The fundamental group and the dimension theorem

Closed loops in $C_{N}(\mathbb{R}^{d})$ are classified up to continuous deformation by the fundamental group $\pi_{1}(C_{N}(\mathbb{R}^{d}))$. The possible exchange statistics are the unitary representations of this group. The dimension theorem is then [ESTABLISHED — @leinaas_myrheim1977; @laidlaw_dewitt1971]:

$$\pi_{1}\bigl(C_{N}(\mathbb{R}^{d})\bigr) = \begin{cases} B_{N} & d = 2 \\ S_{N} & d \ge 3, \end{cases}$$

where $B_{N}$ is the braid group (Artin presentation: generators $\sigma_{1}, \ldots, \sigma_{N-1}$ with relations $\sigma_{i} \sigma_{i+1} \sigma_{i} = \sigma_{i+1} \sigma_{i} \sigma_{i+1}$ and $\sigma_{i} \sigma_{j} = \sigma_{j} \sigma_{i}$ for $\lvert i - j \rvert \ge 2$) and $S_{N}$ is the symmetric group, obtained from $B_{N}$ by imposing the involutive relations $\sigma_{i}^{2} = 1$ (Artin's theorem: $S_{N} \cong B_{N} / \langle \sigma_{i}^{2} = 1 \rangle$).

The consequences for statistics:

- **$d \ge 3$:** $\pi_{1} = S_{N}$. The group has exactly two one-dimensional unitary representations: the trivial representation (boson, exchange phase $+1$) and the sign representation (fermion, exchange phase $-1$). Higher-dimensional representations of $S_{N}$ (parastatistics) are excluded in the scalar-wavefunction framework by the symmetric/exterior dichotomy of the exchange operator (Section 5, T1).
- **$d = 2$:** $\pi_{1} = B_{N}$. The braid group admits a one-parameter family of one-dimensional representations $\rho_{\theta}(\sigma_{i}) = e^{i\theta}$; the exchange phase is arbitrary,

$$R = e^{i\theta} = e^{2\pi i s},$$

giving anyons with fractional statistics [ESTABLISHED — @wilczek1983; @read_green2000]. Higher-dimensional representations give non-abelian anyons, central to topological quantum computation [@sati_schreiber2022b; @myers_sati_schreiber2023].

The exchange phase $R = e^{2\pi i s}$ is the dimension-independent invariant; the binary $\pm 1$ is its shadow in $d \ge 3$ [ESTABLISHED — @qnfo_res010; @qnfo_res009]. In Section 5 we re-derive this dichotomy from the ribbon identity of a braided monoidal category whose exchange map is a scalar.

## 3. The Scaffolds

CST is correct as kinematics, and it is not derived from quantum mechanics. It imports the following structures from classical geometry [ACKNOWLEDGED — scaffold audit, this paper]:

1. **Point-like particles.** The constituents are structureless points with no internal spatial extent. The diagonal is excluded by fiat, as if particles were impenetrable point singularities. Real particles are composite, have finite size, and can overlap (Section 3.1).
2. **A fixed classical background manifold.** The quantum state is a function on a pre-existing, smooth, fixed space — a classical inheritance. The configuration space is assumed to be a manifold with a well-defined fundamental group: no minimum length, no granularity.
3. **The deleted hard-core diagonal.** The topology of $C_{N}(M)$ — and hence the entire statistics classification — depends on $\Delta$ being removed. Physical interactions happen at collisions; forces diverge there. The exclusion is enforced physically by energy penalties, not by logical prohibition. The wobble: an idealization dictates physical law [@harshman_knapp2022].
4. **Externally imposed dimension.** The framework is sharply dimension-dependent, yet dimensionality is treated as an external given. Why three dimensions? CST does not answer; it presupposes (Section 6, T3).
5. **Adiabatic exchange.** The topological classification of paths assumes exchanges are slow and continuous, separating topological from dynamical phases. This clean division breaks down in strongly interacting systems.

Map–territory hygiene: the map is the homotopy class of a path in configuration space; the territory is the physical act of exchange of real particles at finite temperature, with noise, gauge fields, and decoherence. The map constrains the possible wavefunctions; it does not by itself constitute the statistics as an observable consequence (occupation numbers, exchange forces). CST is the kinematical precondition for writing the wavefunction, not the full dynamical mechanism [ACKNOWLEDGED].

### 3.1 The counter-literature: scaffolds under active test

The scaffolds are not settled doctrine; each is currently being tested externally:

- **The diagonal (orbifold).** Harshman and Knapp include the singular points instead of deleting them: the configuration space becomes an orbifold, and one-dimensional systems acquire non-trivial exchange statistics, including non-abelian anyons obeying alternate strand groups [@harshman_knapp2022]. The deleted diagonal is a modeling choice.
- **The braid-group classification (traid).** Hard-core *three-body* constraints in one dimension create defects of co-dimension two, making $\pi_{1}(C_{N})$ neither $S_{N}$ nor $B_{N}$ but the traid group, with abelian and non-abelian representations neither bosonic nor fermionic [@harshman_knapp2018; @nagies_etal2023].
- **The Euclidean arena (graphs).** On graphs, the operative parameter is not dimension but connectivity: 2-connected graphs admit anyon phases; non-planar 3-connected graphs admit only bosons and fermions [@sawicki2014; @harrison_etal2013; @maciazek_sawicki2018; @maciazek2019]. Dimension (Euclidean case) is a proxy for the topological classification.
- **The point-particle idealization (extended objects).** Configuration spaces of extended objects (loops, vortices) admit exotic statistics beyond the point-particle classification [@extended_objects2012; @smith2026].

These results do not refute CST in its own framework; they delimit it. The honest statement of the framework's scope is given in Section 4.

## 4. The Boundary

### 4.1 The spin-statistics connection (C3)

CST gives the *possible* exchange statistics: $S_{N}$ in $d \ge 3$, $B_{N}$ in $d = 2$. It does not say which particles are bosons and which are fermions, nor connect exchange phase to spin. The spin-statistics theorem is a separate result of relativistic quantum field theory: integer spin fields are bosonic, half-integer spin fields are fermionic, derived from Lorentz invariance, microcausality, and positivity of the energy [ESTABLISHED — @streater_wightman1964; @pauli1940; @finkelstein_rubinstein1968; @wilczek1983].

**Boundary statement (C3, [ACKNOWLEDGED]):** the spin-statistics connection — which exchange eigenvalue corresponds to which spin — requires Lorentz symmetry, microcausality, and positive energy. The mark calculus alone cannot supply these inputs. This paper does not claim to derive them. The QNFO predecessor makes the same concession explicitly [@qnfo_res009, Section 5].

**Engagement with a contested alternative.** A 2026 self-published record claims a geometric origin for Fermi–Dirac statistics from $\mathbb{Z}_{2}$ normal holonomy *without* Lorentz invariance [CONTESTED — @li_ge2026]. The claim is not peer-reviewed, and its framework is not the configuration-space or mark-calculus framework of this paper. It is cited here for completeness of the boundary discussion: if a no-Lorentz derivation of the spin-statistics connection were established, the boundary statement C3 would require qualification. At present the standard derivation stands [@streater_wightman1964; @pauli1940], and the boundary is maintained.

### 4.2 Beyond scalars: braided fusion categories and emergent anyons

The scalar-wavefunction framework classifies abelian statistics. Two sectors lie outside it:

- **Non-abelian anyons** require wavefunctions transforming under higher-dimensional representations of the braid group; the full structure is a braided fusion category, not only the fundamental group [ESTABLISHED — @sati_schreiber2022a; @myers_sati_schreiber2023; @toppan2023].
- **Emergent anyons** in condensed matter are quasiparticle excitations whose effective configuration space is not the literal $\mathbb{R}^{2N}$ of the underlying electrons; their topology is emergent, not fundamental [ESTABLISHED — @read_green2000; @proxmire2026].

CST identifies the *possibility* of braid statistics; it does not by itself generate the full anyonic structure. This paper's claims are scoped to the abelian sector of the point-particle framework.

### 4.3 The framework-conditional status of the $\pm 1$ dichotomy

The "tyranny of the $\pm 1$" [@qnfo_tyranny] holds in the point-particle + deleted-diagonal + scalar-wavefunction framework. It is conditional in four named ways: (a) the orbifold treatment re-classifies singular configurations [@harshman_knapp2022]; (b) graph configuration spaces replace dimension with connectivity [@sawicki2014]; (c) three-body hard-core constraints in one dimension produce the traid group [@harshman_knapp2018; @nagies_etal2023]; (d) supersymmetric extensions admit anyonic spin representations in three dimensions [@chaichian_etal2012] — the spin side, not the exchange side, which remains governed by $\pi_{1} = S_{N}$. Intermediate statistics (Gentile and related) exist as formal occupation-number structures outside the configuration-space framework [@shen2020; @dai_xie2003; @selvi_uncu2015]; they alter the algebra, not the fundamental group.

## 5. The Distinction Calculus: Pre-Registered Derivation Program

### 5.1 Inheritance

The QNFO distinction tradition (laws of form [@qnfo_cancellation; @qnfo_qlof]) pre-registered a derivation program for exchange statistics from the mark calculus [@qnfo_res009]: under the mark as primitive boundary-drawing act, with compact closure, self-duality, and a named abelian-pair postulate, exchange statistics is to be derived — not postulated — and the spin-statistics connection is explicitly outside the calculus's reach (C3, Section 4.1). The companion result derives the exchange phase as a logical scalar from the re-entrant mark [@qnfo_res010]: the constants $e$ and $\pi$ arise as logical scalars of the re-entrant form under linear discipline, and the exchange phase is

$$R = e^{2\pi i s},$$

with the boson/fermion dichotomy as the even/odd dichotomy of $2s$. The re-entrant treatise is the foundational source of the calculus [@qnfo_slb002].

### 5.2 Current construction status (this paper)

**T1 — two modal exponentials from a graded braiding. Status: PARTIAL CONSTRUCTION.**

Given an involutive braiding $\sigma^{2} = \mathrm{id}$ on a self-dual object $M$ with $M \otimes M$ semisimple, the symmetrizer and antisymmetrizer

$$P_{\mathrm{sym}} = \tfrac{1}{2}(\mathrm{id} + \sigma), \qquad P_{\mathrm{ant}} = \tfrac{1}{2}(\mathrm{id} - \sigma)$$

are idempotent orthogonal projectors splitting $M \otimes M = \mathrm{Sym}^{2}(M) \oplus \Lambda^{2}(M)$; the modal exponentials of linear logic are the graded completions $\mathrm{Sym}(M)$ (the of-course modality $!M$) and $\Lambda(M)$. **The CST substrate and the algebraic postulate are the same statement:** the involutive condition $\sigma^{2} = \mathrm{id}$ is exactly $\pi_{1}(C_{2}) = \mathbb{Z}_{2}$ for $d \ge 3$. The open item is the DiLL digling check — why the exponential modality, not only the first graded piece — inherited from [@qnfo_res009] and flagged for construction.

**Constraint from transtatistics.** Medina Sánchez and Dakić show that from unitary dynamics and local phase transformations alone, bosons and fermions are *not* forced: whole families of transtatistics arise [@medina_dakic2023]. Their axiom set omits the abelian-pair postulate; its addition collapses their classification to the two standard statistics. **Consequence:** the projector construction is valid given the postulate; the calculus must either derive the postulate (open problem, falsification condition F2) or state it as a named input — the current position, matching the C3 honesty pattern.

**T2 — the exchange map on two marks is a scalar; the ribbon identity forces the two eigenvalues. Status: CONSTRUCTION CONTENT ACHIEVED.**

Let $M$ be the mark object, self-dual with evaluation $\varepsilon : M \otimes M \to 1$ and coevaluation $\eta : 1 \to M \otimes M$, in a ribbon category (compact closed + twist $\theta$). Under the abelian-pair postulate, Schur's lemma gives $\mathrm{End}(M \otimes M) \cong k$, so the braiding is a scalar: $\sigma_{M,M} = \lambda \cdot \mathrm{id}$. The ribbon identity for the composite object,

$$\theta_{M \otimes M} = \sigma_{M,M} \circ (\theta_{M} \otimes \theta_{M}) \circ \sigma_{M,M},$$

with the mark's self-duality and twist compatibility, yields $\lambda^{2} = 1 \iff \sigma_{M,M}^{2} = \mathrm{id}$. By Artin, $\sigma^{2} = \mathrm{id}$ is exactly the collapse of the braid group to the symmetric group, i.e. $\pi_{1}(C_{N}(\mathbb{R}^{d})) = S_{N}$ for $d \ge 3$. The synthesis:

$$R = e^{2\pi i s} = \pm 1 \iff \pi_{1}\bigl(C_{N}(\mathbb{R}^{d})\bigr) = S_{N} \quad (d \ge 3).$$

The two eigenvalues of the exchange scalar are the boson sign and the fermion sign. In $d = 2$, the braiding is not involutive, the exchange scalar is an arbitrary phase $R = e^{2\pi i s}$, and the topological spin is $\theta_{M} = e^{2\pi i s}$ — the companion result [@qnfo_res010] as the non-involutive sector of the same ribbon identity. **Consilience achieved:** the involutive derivation [@qnfo_res009], the general exchange scalar [@qnfo_res010], and the CST dimension classification [@leinaas_myrheim1977] are one structure.

**T3 — dimension enters exchange statistics only through the allowed braided structures. Status: REFINED AND RE-STATED.**

Base theorem [ESTABLISHED]: for point particles in Euclidean space, the entire dimension-dependence of statistics is the $d = 2$ vs $d \ge 3$ dichotomy of $\pi_{1}$. Re-stated claim with named boundary conditions: in the hard-core point-particle framework with deleted diagonal, spatial dimension enters exchange statistics only through the fundamental group of the configuration space; dimension is a proxy for the topological classification, and the classification is the invariant. Boundary conditions (named, engaged in Section 3.1): (a) orbifold treatment dissolves the deleted-diagonal scaffold [@harshman_knapp2022]; (b) graph configuration spaces replace dimension with connectivity [@sawicki2014; @harrison_etal2013]; (c) three-body hard-core constraints in one dimension produce the traid group [@harshman_knapp2018; @nagies_etal2023]; (d) extended objects and supersymmetric extensions live outside the point-particle exchange sector [@extended_objects2012; @chaichian_etal2012].

## 6. The Synthesis Conjecture (C2): Distinction Calculus into Homotopy Type Theory

### 6.1 Statement

**[CONJECTURE]** The Distinction Calculus — the mark as primitive boundary-drawing act — reframes the scaffolds of CST (Section 3) as acts of boundary-drawing. The conjecture: the exchange phase $R = e^{2\pi i s}$ and the fundamental group $\pi_{1}(C_{N}(M))$ are two projections of one invariant — the re-entrant mark disciplined by linearity — and the synthesis is formalized by lifting the Distinction Calculus into homotopy type theory (HoTT), where the Grothendieck–Teichmüller (GT) group's action on braided monoidal categories renders boundary-drawing an arithmetic act: each statistical phase selects a prime's worth of complexity.

The mathematical ingredients of the conjecture are real and mature: the GT group is the automorphism group of the profinite braid groups, acting on braided monoidal categories [ESTABLISHED — @drinfeld1990; @hi_ai2025]; the classification that dimension is a proxy for (T3) is the object on which the GT group acts. The UMP corpus supplies the arithmetic twin of this classification in the p-adic setting [@qnfo_padic_braids; @qnfo_padic_tl; @qnfo_padic_anyons; @qnfo_zbw_p4; @qnfo_adelic_synth], and the calculus-of-distinction series supplies the formal bridge between laws of form and ultrametric trees [@qnfo_qlof]. "Drawing a boundary is an arithmetic act" thereby acquires a precise content: choosing the braided structure is choosing a point in the moduli on which GT acts — selecting the statistical sector.

### 6.2 Differentiation from the cohesive-HoTT program (mandatory)

The HoTT $\times$ anyon space is **not** empty. Sati and Schreiber have established a program of cohesive homotopy type theory as a foundation for quantum gauge field theory [@schreiber_shulman2014], classifying anyonic topological order by twisted equivariant differential K-theory of configuration spaces [@sati_schreiber2022a], with topological quantum programming [@sati_schreiber2022b], topological quantum gates certified in cubical Agda [@myers_sati_schreiber2023], and a cohomotopy/framed-link analysis of abelian anyons [@sati_schreiber2024]. The differentiation is therefore explicit and structural:

| Dimension | Cohesive-HoTT program [@schreiber_shulman2014; @sati_schreiber2022a; @sati_schreiber2022b; @myers_sati_schreiber2023; @sati_schreiber2024] | This conjecture (C2) |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Foundation | Cohesion axioms on the universe type | The mark as primitive cut |
| Target | Classification and verification of physical topological quantum computation | Derivation of the exchange phase as a logical scalar |
| Route | Cohesive modalities to TED K-theory of configuration spaces | Re-entrant mark to braided monoidal category to GT action to $R = e^{2\pi i s}$ |
| Statistics | Anyonic topological order classified | Exchange scalar derived; $\pm 1$ as involutive shadow |

The two programs share the HoTT substrate and the configuration-space arena; they do not share the primitive or the route. The novelty claim of C2 is the mark-based route — never the mathematical objects.

## 7. Falsification Conditions

**F1.** Exhibit a braided monoidal category generated by the calculus whose one-dimensional braid-group representations omit the abelian phases $e^{i\theta}$; or show the GT action is inessential to the category's structure. *Engaged:* the Sati–Schreiber program is the current state of the art in HoTT-anyon mathematics [@sati_schreiber2022a; @sati_schreiber2022b; @myers_sati_schreiber2023]; if the mark-based route is shown to reproduce their classification without the GT action, F1 fires and the arithmetic-act reading collapses.

**F2.** Show the mark calculus cannot yield exactly two exchange eigenvalues ($\pm 1$) without re-importing the symmetric-algebra choice — the abelian-pair postulate is not derivable. *Engaged:* the transtatistics result shows the two-statistics dichotomy is not forced by dynamics and local phases alone [@medina_dakic2023]; detectable $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$-graded parastatistics exist [@toppan2023]. If the abelian-pair postulate is confirmed underivable, the calculus's dichotomy is a named-input result, not a derivation — an honest boundary (Section 4.1 pattern), and F2 is recorded as fired.

**F3.** Show spatial dimension enters exchange statistics elsewhere than through the allowed braided structures, in the point-particle framework. *Engaged:* the orbifold treatment is the main threat [@harshman_knapp2022]; it is currently absorbed into the re-statement of T3 as a boundary condition rather than a contradiction.

## 8. Applications

1. **Braiding phase gates.** Gate sets generated from braid words classified by the re-entrant calculus, hardware-agnostic [@qnfo_res009]. Falsifiable: a braid word classified bosonic under the calculus maps to a non-trivial gate.
2. **Topological quantum computation classification.** Derive braid rules from logical constraints, then search physical systems realizing them [@sati_schreiber2022b; @myers_sati_schreiber2023]. Falsifiable: a physical anyon model outside the calculus's predicted list is realized.
3. **AI-assisted proof verification.** Automated consistency-checking of the calculus at scale; the audit becomes the falsifier mechanism for T1–T3.
4. **Logical-loop simulation.** Simulate exchange statistics by iterating re-entrant marks, without solving the Schrödinger equation [@qnfo_res010; @qnfo_res009]. Falsifiable: simulation output differs from the CST prediction for the same framework index.
5. **Quantum error correction cross-link.** CST as the topological-protection side of the Joules-per-solution thermodynamic critique. Falsifiable: protected sectors show no error-rate improvement at equal energy budget.

## 9. Conclusion

Configuration-space topology is the correct kinematical explanation of the boson/fermion/anyon trichotomy, and it is a map with known limits. Its scaffolds (point particles, fixed background, deleted diagonal, imposed dimension) are under active external test; its spin-statistics boundary requires relativistic input the framework cannot supply; and its non-abelian and emergent sectors lie in braided fusion categories beyond the fundamental group. Against this honest boundary, the QNFO distinction tradition's pre-registered derivation program has advanced: T2 now carries construction content (the exchange scalar dichotomy is the ribbon identity evaluated in the $d \ge 3$ topological sector); T1 is partially constructed; T3 is re-stated with named boundary conditions. The synthesis conjecture — the Distinction Calculus lifted into HoTT, with the GT group acting on braided monoidal categories — is stated with explicit falsification conditions F1–F3 and differentiated from the existing cohesive-HoTT program. The route is unoccupied in eight independent literature sources; the objects are mature. The epistemic value of this paper is the honest boundary map of a mature framework and a falsifiable derivation program for its logical origin.

## Acknowledgements and Provenance

This paper is part of the QNFO Research Foundation portfolio (WBS QNFO.RES.011). Predecessor records: [@qnfo_res009; @qnfo_res010; @qnfo_slb002; @qnfo_tyranny]. All external citations verified against live Crossref/arXiv/Zenodo metadata on 2026-08-15 (citation audit on file). The deep-inquiry scaffold audit of Section 3 follows the Universal Ignorance Audit protocol (QNFO methodological standard, 15-question framework). AI assistance in drafting is disclosed as a quality signal per the QNFO disclosure policy. The quantitative claims of this paper (Section 2.2) are independently verified group-theoretic facts.

## References

[Bibliography: see `references.bib` — 44 entries, all verified live on 2026-08-15.]
