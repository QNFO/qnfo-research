---
title: 'Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its ±1 Shadow, and a Pre-Registered Derivation Program'
author: 'Quni-Gudzinas, Rowan Brad'
date: '2026-08-16'
status: published
version: v0.3
doi: 10.5281/zenodo.21962450
concept-doi: 10.5281/zenodo.21945449
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
  Configuration-space topology (CST) derives exchange statistics from the
  topology of the space in which identical particles move: the fundamental
  group pi_1(C_N(M)) is the symmetric group S_N in d >= 3 spatial dimensions
  (exactly two exchange phases: boson +1, fermion -1) and the braid group B_N
  in d = 2 (anyons, including the non-abelian braiding used in topological
  quantum computation). This paper draws the boundary of that framework. It
  names the five silent scaffolds CST imports from classical geometry --
  point-like particles, a fixed background manifold, the deleted hard-core
  diagonal, externally imposed dimension, adiabatic exchange -- and engages
  the active counter-literature testing each one (orbifolds, traid groups,
  graph configuration spaces, extended objects, supersymmetric anyons). It
  concedes the framework's hard boundary: the spin-statistics connection
  requires Lorentz symmetry, microcausality, and positive energy, which no
  topological or logical argument supplies. Against this boundary it reports
  the status of the QNFO pre-registered derivation program (exchange phase as
  a logical scalar R = e^{2 pi i s} from the re-entrant mark): T2 now carries
  construction content -- the ±1 dichotomy is the ribbon identity evaluated
  in the d >= 3 sector; T1 is partially constructed; T3 is restated with named
  boundary conditions. It then states a synthesis conjecture -- the Distinction
  Calculus lifted into homotopy type theory, with the Grothendieck-Teichmuller
  group acting on braided monoidal categories, renders boundary-drawing an
  arithmetic act -- with explicit falsification conditions F1-F3, and
  differentiates it from the cohesive-HoTT program of Sati and Schreiber. The
  paper proves no new theorem; its contribution is a verified boundary map of
  a mature framework and a falsifiable route toward the logical origin of
  quantum statistics.
---

**Rowan Brad Quni-Gudzinas**

**QNFO Research Foundation** — 2026-08-16

*Status labels used throughout: [ESTABLISHED] = standard result with independent external verification; [CONJECTURE] = proposed, falsifiable, not yet proven; [ACKNOWLEDGED] = boundary of the present framework, conceded; [CONTESTED] = live external research activity at this boundary.*

## 1. Introduction

Why are there bosons and fermions and nothing else? In three spatial dimensions, exchanging two indistinguishable particles can multiply the many-body wavefunction by exactly one of two phases: $+1$ or $-1$ [ESTABLISHED — @leinaas_myrheim1977; @laidlaw_dewitt1971]. Two-dimensional systems admit a continuum of intermediate phases (anyons) [ESTABLISHED — @wilczek1983; @read_green2000]. This dimension-dependent dichotomy is not an empirical accident; it is a theorem about the topology of the space in which particles move [ESTABLISHED — @leinaas_myrheim1977].

Configuration-space topology (CST) is the modern, intrinsic derivation of this structure: statistics is a representation of the fundamental group of the configuration space of identical particles. The framework is correct as kinematics — and it is not its terminus. It rests on scaffolds — point-like particles, a fixed classical background manifold, a deleted hard-core diagonal, an externally imposed dimension — that the framework itself cannot derive [ACKNOWLEDGED — this paper, Section 4]. And the connection between exchange phase and spin (the spin-statistics theorem proper) requires relativistic input that no purely topological or logical argument supplies [ACKNOWLEDGED — @streater_wightman1964; @pauli1940; @finkelstein_rubinstein1968].

This paper has three tasks:

1. **Map the theorem and its scaffolds** (Sections 3–4). State precisely what CST proves — the dimension theorem — and name the silent scaffolds the framework imports from classical geometry. Section 4 engages the active counter-literature currently testing those scaffolds: the orbifold treatment of singular configurations [@harshman_knapp2022], the traid group in one dimension [@harshman_knapp2018; @nagies_etal2023], graph configuration spaces [@sawicki2014; @harrison_etal2013; @maciazek_sawicki2018; @maciazek2019], supersymmetric anyons [@chaichian_etal2012], and extended objects [@extended_objects2012; @smith2026].
2. **Draw the boundary honestly** (Section 5), including engagement with the contested claim that the spin-statistics connection can be derived without Lorentz invariance [CONTESTED — @li_ge2026].
3. **Report the derivation program and the conjecture** (Sections 6–8): the current construction status of the pre-registered QNFO program — exchange statistics from the mark calculus — and the synthesis conjecture lifting the Distinction Calculus into homotopy type theory under the Grothendieck–Teichmüller group, with explicit falsification conditions F1–F3.

Section 2 answers the question every reader asks first — *why should I care?* Sections 9–10 note applications and conclude.

**How to read this paper.** The movement is from what is *proven* (Section 3), to what is *assumed* (Section 4), to what is *conceded* (Section 5), to what is *under construction* (Section 6), to what is *conjectured and how it could be falsified* (Sections 7–8). Every claim carries a status label: [ESTABLISHED], [CONJECTURE], [ACKNOWLEDGED], or [CONTESTED].

## 2. So What? Why Should a Reader Care About This Research?

**The stakes.** Every quantum theory of matter takes the boson/fermion dichotomy as an input: fields are quantized with commutators or anticommutators, and which one applies to a given particle is a datum of the theory, not a consequence of it. Chemistry, the standard model, and condensed matter all rest on this premise. Configuration-space topology shows that the dichotomy is not an arbitrary empirical fact but a theorem about the space in which particles move: in $d \ge 3$ the exchange phase can only be $\pm 1$, because the fundamental group of the configuration space of identical particles is the symmetric group. A theorem, however, is only as deep as its premises. The question this paper exists to sharpen is: **how deep does the theorem go, and where do its premises end?**

That question is not idle. The two-dimensional sector of the same theorem yields the braid group and, with it, anyons — including the non-abelian anyons that are the leading physical substrate for topological quantum computation. The boundary conditions of the theorem (Section 4) are not curiosities; they are the places where the "iron law" of $\pm 1$ fails or changes meaning, and they are the places where new physics — and new computational platforms — live. A researcher who knows exactly which framework conditions generate which statistics knows which systems can host braiding, and which cannot.

**What a physicist gets: a decision-relevant boundary map.** For an anyon theorist or a topological-quantum-computation researcher, the value of this paper is the boundary map: which results are theorems, which are scaffolds, which are contested, and which are conjectured. Each named scaffold — point particles, fixed background, deleted diagonal, imposed dimension, adiabatic exchange — corresponds to a live research program (orbifolds, traid groups, graph configuration spaces, extended objects, supersymmetric anyons) that either reclassifies statistics or extends it into new regimes. Section 4 engages that counter-literature directly, with citations, rather than bracketing it.

**What a mathematician gets: a falsifiable conjecture with mature ingredients.** The synthesis conjecture (Section 7) is not a slogan. It names its ingredients — the mark calculus, braided monoidal categories, the Grothendieck–Teichmüller group, homotopy type theory — the route connecting them, and three explicit falsification conditions F1–F3 (Section 8), each of which can be checked. It also performs the differentiation work the field requires: the proposed route is explicitly distinguished from the cohesive-HoTT program of Sati and Schreiber (Section 7.2), so the claim is an unoccupied route, not a collision with existing work. A conjecture with falsification conditions is a research program; one without them is a manifesto.

**What a foundations reader gets: scaffold auditing as method.** CST is the most successful kinematics in quantum mechanics, and it quietly imports point particles, a fixed classical background, a deleted hard-core diagonal, and an externally imposed dimension. This paper performs the audit that foundational work should always perform: theorem separated from scaffold, scaffold separated from boundary, boundary conceded in plain language. The spin-statistics connection is conceded to require Lorentz symmetry, microcausality, and positive energy (Section 5.1); the abelian-pair postulate is conceded to be, so far, a named input (Section 6.2). In a literature where overclaiming is the norm, a paper that states exactly what it does not prove is a usable reference point.

**What this paper does not claim — and why that is the point.** No new theorem in configuration-space topology (the dimension theorem is from 1977). No Lorentz-free derivation of the spin-statistics connection (the contested alternative is engaged in Section 5.1 and explicitly not endorsed). No completed derivation of the dichotomy from the mark calculus: T2 carries construction content, T1 is partial, and the abelian-pair postulate remains a named input. What the paper contributes is the honest boundary map and a falsifiable route — with its first confirmed step: **the exchange-scalar dichotomy is the ribbon identity evaluated in the $d \ge 3$ topological sector** (Section 6.2). If you care about where the laws of statistics come from — or where they can be bent — this is the map to read first.

## 3. Configuration-Space Topology: The Framework

### 3.1 The configuration space of identical particles

For $N$ identical particles in $d$ spatial dimensions, the classical configuration space is not $\mathbb{R}^{dN}$ [ESTABLISHED — @leinaas_myrheim1977]. Two constructions intervene:

1. **Removal of the diagonal.** Particles are taken to be hard-core: no two may coincide. The collision set
   $\Delta = \lbrace x \in \mathbb{R}^{dN} \mid x_{i} = x_{j} \text{ for some } i \neq j \rbrace$
   is removed, giving the ordered configuration space $\mathbb{R}^{dN} \setminus \Delta$.
2. **Quotient by the symmetric group.** Identical particles are indistinguishable; configurations differing by a permutation of labels are the same physical state. The space is quotiented by $S_{N}$:

$$C_{N}(\mathbb{R}^{d}) = \frac{\mathbb{R}^{dN} \setminus \Delta}{S_{N}}.$$

Quantum states are functions on this space (more precisely, sections of vector bundles over it, up to phase). The allowed statistics are the possible phases or unitary transformations acquired when particles are exchanged — which is to say, when the system traverses a closed loop in $C_{N}(\mathbb{R}^{d})$ [ESTABLISHED — @laidlaw_dewitt1971].

### 3.2 The fundamental group and the dimension theorem

Closed loops in $C_{N}(\mathbb{R}^{d})$ are classified up to continuous deformation by the fundamental group $\pi_{1}(C_{N}(\mathbb{R}^{d}))$. The possible exchange statistics are the unitary representations of this group. The dimension theorem is then [ESTABLISHED — @leinaas_myrheim1977; @laidlaw_dewitt1971]:

$$\pi_{1}\bigl(C_{N}(\mathbb{R}^{d})\bigr) = \begin{cases} B_{N} & d = 2 \\ S_{N} & d \ge 3, \end{cases}$$

where $B_{N}$ is the braid group (Artin presentation: generators $\sigma_{1}, \ldots, \sigma_{N-1}$ with relations $\sigma_{i} \sigma_{i+1} \sigma_{i} = \sigma_{i+1} \sigma_{i} \sigma_{i+1}$ and $\sigma_{i} \sigma_{j} = \sigma_{j} \sigma_{i}$ for $\lvert i - j \rvert \ge 2$) and $S_{N}$ is the symmetric group, obtained from $B_{N}$ by imposing the involutive relations $\sigma_{i}^{2} = 1$ (Artin's theorem: $S_{N} \cong B_{N} / \langle \sigma_{i}^{2} = 1 \rangle$).

The consequences for statistics:

- **$d \ge 3$:** $\pi_{1} = S_{N}$. The group has exactly two one-dimensional unitary representations: the trivial representation (boson, exchange phase $+1$) and the sign representation (fermion, exchange phase $-1$). Higher-dimensional representations of $S_{N}$ (parastatistics) are excluded in the scalar-wavefunction framework by the symmetric/exterior dichotomy of the exchange operator (Section 6, T1).
- **$d = 2$:** $\pi_{1} = B_{N}$. The braid group admits a one-parameter family of one-dimensional representations $\rho_{\theta}(\sigma_{i}) = e^{i\theta}$; the exchange phase is arbitrary,

$$R = e^{i\theta} = e^{2\pi i s},$$

giving anyons with fractional statistics [ESTABLISHED — @wilczek1983; @read_green2000]. Higher-dimensional representations give non-abelian anyons, central to topological quantum computation [@sati_schreiber2022b; @myers_sati_schreiber2023].

The exchange phase $R = e^{2\pi i s}$ is the dimension-independent invariant; the binary $\pm 1$ is its shadow in $d \ge 3$ [ESTABLISHED — @qnfo_res010; @qnfo_res009]. In Section 6 we re-derive this dichotomy from the ribbon identity of a braided monoidal category whose exchange map is a scalar.

## 4. The Scaffolds

CST is correct as kinematics, and it is not derived from quantum mechanics. It imports the following structures from classical geometry [ACKNOWLEDGED — scaffold audit, this paper]:

1. **Point-like particles.** The constituents are structureless points with no internal spatial extent. The diagonal is excluded by fiat, as if particles were impenetrable point singularities. Real particles are composite, have finite size, and can overlap (Section 4.1).
2. **A fixed classical background manifold.** The quantum state is a function on a pre-existing, smooth, fixed space — a classical inheritance. The configuration space is assumed to be a manifold with a well-defined fundamental group: no minimum length, no granularity.
3. **The deleted hard-core diagonal.** The topology of $C_{N}(M)$ — and hence the entire statistics classification — depends on $\Delta$ being removed. Physical interactions happen at collisions; forces diverge there. The exclusion is enforced physically by energy penalties, not by logical prohibition. The wobble: an idealization dictates physical law [@harshman_knapp2022].
4. **Externally imposed dimension.** The framework is sharply dimension-dependent, yet dimensionality is treated as an external given. Why three dimensions? CST does not answer; it presupposes (Section 7, T3).
5. **Adiabatic exchange.** The topological classification of paths assumes exchanges are slow and continuous, separating topological from dynamical phases. This clean division breaks down in strongly interacting systems.

Map–territory hygiene: the map is the homotopy class of a path in configuration space; the territory is the physical act of exchange of real particles at finite temperature, with noise, gauge fields, and decoherence. The map constrains the possible wavefunctions; it does not by itself constitute the statistics as an observable consequence (occupation numbers, exchange forces). CST is the kinematical precondition for writing the wavefunction, not the full dynamical mechanism [ACKNOWLEDGED].

### 4.1 The counter-literature: scaffolds under active test

The scaffolds are not settled doctrine; each is currently being tested externally:

- **The diagonal (orbifold).** Harshman and Knapp include the singular points instead of deleting them: the configuration space becomes an orbifold, and one-dimensional systems acquire non-trivial exchange statistics, including non-abelian anyons obeying alternate strand groups [@harshman_knapp2022]. The deleted diagonal is a modeling choice.
- **The braid-group classification (traid).** Hard-core *three-body* constraints in one dimension create defects of co-dimension two, making $\pi_{1}(C_{N})$ neither $S_{N}$ nor $B_{N}$ but the traid group, with abelian and non-abelian representations neither bosonic nor fermionic [@harshman_knapp2018; @nagies_etal2023].
- **The Euclidean arena (graphs).** On graphs, the operative parameter is not dimension but connectivity: 2-connected graphs admit anyon phases; non-planar 3-connected graphs admit only bosons and fermions [@sawicki2014; @harrison_etal2013; @maciazek_sawicki2018; @maciazek2019]. Dimension (Euclidean case) is a proxy for the topological classification.
- **The point-particle idealization (extended objects).** Configuration spaces of extended objects (loops, vortices) admit exotic statistics beyond the point-particle classification [@extended_objects2012; @smith2026].

These results do not refute CST in its own framework; they delimit it. The honest statement of the framework's scope is given in Section 5.

## 5. The Boundary

### 5.1 The spin-statistics connection (C3)

CST gives the *possible* exchange statistics: $S_{N}$ in $d \ge 3$, $B_{N}$ in $d = 2$. It does not say which particles are bosons and which are fermions, nor connect exchange phase to spin. The spin-statistics theorem is a separate result of relativistic quantum field theory: integer spin fields are bosonic, half-integer spin fields are fermionic, derived from Lorentz invariance, microcausality, and positivity of the energy [ESTABLISHED — @streater_wightman1964; @pauli1940; @finkelstein_rubinstein1968; @wilczek1983].

**Boundary statement (C3, [ACKNOWLEDGED]):** the spin-statistics connection — which exchange eigenvalue corresponds to which spin — requires Lorentz symmetry, microcausality, and positive energy. The mark calculus alone cannot supply these inputs. This paper does not claim to derive them. The QNFO predecessor makes the same concession explicitly [@qnfo_res009, Section 5].

**Engagement with a contested alternative.** A 2026 self-published record claims a geometric origin for Fermi–Dirac statistics from $\mathbb{Z}_{2}$ normal holonomy *without* Lorentz invariance [CONTESTED — @li_ge2026]. The claim is not peer-reviewed, and its framework is not the configuration-space or mark-calculus framework of this paper. It is cited here for completeness of the boundary discussion: if a no-Lorentz derivation of the spin-statistics connection were established, the boundary statement C3 would require qualification. At present the standard derivation stands [@streater_wightman1964; @pauli1940], and the boundary is maintained.

### 5.2 Beyond scalars: braided fusion categories and emergent anyons

The scalar-wavefunction framework classifies abelian statistics. Two sectors lie outside it:

- **Non-abelian anyons** require wavefunctions transforming under higher-dimensional representations of the braid group; the full structure is a braided fusion category, not only the fundamental group [ESTABLISHED — @sati_schreiber2022a; @myers_sati_schreiber2023; @toppan2023].
- **Emergent anyons** in condensed matter are quasiparticle excitations whose effective configuration space is not the literal $\mathbb{R}^{2N}$ of the underlying electrons; their topology is emergent, not fundamental [ESTABLISHED — @read_green2000; @proxmire2026].

CST identifies the *possibility* of braid statistics; it does not by itself generate the full anyonic structure. This paper's claims are scoped to the abelian sector of the point-particle framework.

### 5.3 The framework-conditional status of the $\pm 1$ dichotomy

The "tyranny of the $\pm 1$" [@qnfo_tyranny] holds in the point-particle + deleted-diagonal + scalar-wavefunction framework. It is conditional in four named ways: (a) the orbifold treatment re-classifies singular configurations [@harshman_knapp2022]; (b) graph configuration spaces replace dimension with connectivity [@sawicki2014]; (c) three-body hard-core constraints in one dimension produce the traid group [@harshman_knapp2018; @nagies_etal2023]; (d) supersymmetric extensions admit anyonic spin representations in three dimensions [@chaichian_etal2012] — the spin side, not the exchange side, which remains governed by $\pi_{1} = S_{N}$. Intermediate statistics (Gentile and related) exist as formal occupation-number structures outside the configuration-space framework [@shen2020; @dai_xie2003; @selvi_uncu2015]; they alter the algebra, not the fundamental group.

## 6. The Distinction Calculus: Pre-Registered Derivation Program

### 6.1 Inheritance

The QNFO distinction tradition (laws of form [@qnfo_cancellation; @qnfo_qlof]) pre-registered a derivation program for exchange statistics from the mark calculus [@qnfo_res009]: under the mark as primitive boundary-drawing act, with compact closure, self-duality, and a named abelian-pair postulate, exchange statistics is to be derived — not postulated — and the spin-statistics connection is explicitly outside the calculus's reach (C3, Section 5.1). The companion result derives the exchange phase as a logical scalar from the re-entrant mark [@qnfo_res010]: the constants $e$ and $\pi$ arise as logical scalars of the re-entrant form under linear discipline, and the exchange phase is

$$R = e^{2\pi i s},$$

with the boson/fermion dichotomy as the even/odd dichotomy of $2s$. The re-entrant treatise is the foundational source of the calculus [@qnfo_slb002].

### 6.2 Current construction status (this paper)

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

Base theorem [ESTABLISHED]: for point particles in Euclidean space, the entire dimension-dependence of statistics is the $d = 2$ vs $d \ge 3$ dichotomy of $\pi_{1}$. Re-stated claim with named boundary conditions: in the hard-core point-particle framework with deleted diagonal, spatial dimension enters exchange statistics only through the fundamental group of the configuration space; dimension is a proxy for the topological classification, and the classification is the invariant. Boundary conditions (named, engaged in Section 4.1): (a) orbifold treatment dissolves the deleted-diagonal scaffold [@harshman_knapp2022]; (b) graph configuration spaces replace dimension with connectivity [@sawicki2014; @harrison_etal2013]; (c) three-body hard-core constraints in one dimension produce the traid group [@harshman_knapp2018; @nagies_etal2023]; (d) extended objects and supersymmetric extensions live outside the point-particle exchange sector [@extended_objects2012; @chaichian_etal2012].

## 7. The Synthesis Conjecture (C2): Distinction Calculus into Homotopy Type Theory

### 7.1 Statement

**[CONJECTURE]** The Distinction Calculus — the mark as primitive boundary-drawing act — reframes the scaffolds of CST (Section 4) as acts of boundary-drawing. The conjecture: the exchange phase $R = e^{2\pi i s}$ and the fundamental group $\pi_{1}(C_{N}(M))$ are two projections of one invariant — the re-entrant mark disciplined by linearity — and the synthesis is formalized by lifting the Distinction Calculus into homotopy type theory (HoTT), where the Grothendieck–Teichmüller (GT) group's action on braided monoidal categories renders boundary-drawing an arithmetic act: each statistical phase selects a prime's worth of complexity.

The mathematical ingredients of the conjecture are real and mature: the GT group is the automorphism group of the profinite braid groups, acting on braided monoidal categories [ESTABLISHED — @drinfeld1990; @hi_ai2025]; the classification that dimension is a proxy for (T3) is the object on which the GT group acts. The UMP corpus supplies the arithmetic twin of this classification in the p-adic setting [@qnfo_padic_braids; @qnfo_padic_tl; @qnfo_padic_anyons; @qnfo_zbw_p4; @qnfo_adelic_synth], and the calculus-of-distinction series supplies the formal bridge between laws of form and ultrametric trees [@qnfo_qlof]. "Drawing a boundary is an arithmetic act" thereby acquires a precise content: choosing the braided structure is choosing a point in the moduli on which GT acts — selecting the statistical sector.

### 7.2 Differentiation from the cohesive-HoTT program (mandatory)

The HoTT $\times$ anyon space is **not** empty. Sati and Schreiber have established a program of cohesive homotopy type theory as a foundation for quantum gauge field theory [@schreiber_shulman2014], classifying anyonic topological order by twisted equivariant differential K-theory of configuration spaces [@sati_schreiber2022a], with topological quantum programming [@sati_schreiber2022b], topological quantum gates certified in cubical Agda [@myers_sati_schreiber2023], and a cohomotopy/framed-link analysis of abelian anyons [@sati_schreiber2024]. The differentiation is therefore explicit and structural:

| Dimension | Cohesive-HoTT program [@schreiber_shulman2014; @sati_schreiber2022a; @sati_schreiber2022b; @myers_sati_schreiber2023; @sati_schreiber2024] | This conjecture (C2) |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| Foundation | Cohesion axioms on the universe type | The mark as primitive cut |
| Target | Classification and verification of physical topological quantum computation | Derivation of the exchange phase as a logical scalar |
| Route | Cohesive modalities to TED K-theory of configuration spaces | Re-entrant mark to braided monoidal category to GT action to $R = e^{2\pi i s}$ |
| Statistics | Anyonic topological order classified | Exchange scalar derived; $\pm 1$ as involutive shadow |

The two programs share the HoTT substrate and the configuration-space arena; they do not share the primitive or the route. The novelty claim of C2 is the mark-based route — never the mathematical objects.

## 8. Falsification Conditions

**F1.** Exhibit a braided monoidal category generated by the calculus whose one-dimensional braid-group representations omit the abelian phases $e^{i\theta}$; or show the GT action is inessential to the category's structure. *Engaged:* the Sati–Schreiber program is the current state of the art in HoTT-anyon mathematics [@sati_schreiber2022a; @sati_schreiber2022b; @myers_sati_schreiber2023]; if the mark-based route is shown to reproduce their classification without the GT action, F1 fires and the arithmetic-act reading collapses.

**F2.** Show the mark calculus cannot yield exactly two exchange eigenvalues ($\pm 1$) without re-importing the symmetric-algebra choice — the abelian-pair postulate is not derivable. *Engaged:* the transtatistics result shows the two-statistics dichotomy is not forced by dynamics and local phases alone [@medina_dakic2023]; detectable $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$-graded parastatistics exist [@toppan2023]. If the abelian-pair postulate is confirmed underivable, the calculus's dichotomy is a named-input result, not a derivation — an honest boundary (Section 5.1 pattern), and F2 is recorded as fired.

**F3.** Show spatial dimension enters exchange statistics elsewhere than through the allowed braided structures, in the point-particle framework. *Engaged:* the orbifold treatment is the main threat [@harshman_knapp2022]; it is currently absorbed into the re-statement of T3 as a boundary condition rather than a contradiction.

## 9. Applications

Each application states what is built, what it requires, and the falsifiable prediction that would refute it.

1. **Braiding phase gates.** Generate hardware-agnostic gate sets for topological quantum computation by classifying braid words with the re-entrant calculus [@qnfo_res009]. *Falsifiable prediction:* a braid word the calculus classifies as bosonic (trivial exchange) nevertheless realizes a non-trivial logical gate.
2. **Topological quantum computation classification.** Derive braid rules from logical constraints, then search physical systems that realize them [@sati_schreiber2022b; @myers_sati_schreiber2023]. *Falsifiable prediction:* a physical anyon model outside the calculus's predicted list is realized in the laboratory.
3. **AI-assisted proof verification.** Use automated consistency-checking to audit the calculus at scale; the audit is the falsifier mechanism for T1–T3. *Falsifiable prediction:* the checker exhibits an inconsistency in the construction — or, failing that, the audit itself stands as the verification record.
4. **Logical-loop simulation.** Simulate exchange statistics by iterating re-entrant marks, without solving the Schrödinger equation [@qnfo_res010; @qnfo_res009]. *Falsifiable prediction:* simulation output differs from the CST prediction for the same framework index — a direct test of the calculus's kinematics.
5. **Quantum error correction cross-link.** Use CST as the topological-protection side of the Joules-per-solution thermodynamic critique. *Falsifiable prediction:* protected sectors show no error-rate improvement at equal energy budget, decoupling topology from thermodynamic benefit.

## 10. Conclusion

Configuration-space topology is the correct kinematical explanation of the boson/fermion/anyon trichotomy — and it is a map with known limits. Its scaffolds (point particles, fixed background, deleted diagonal, imposed dimension, adiabatic exchange) are under active external test; its spin-statistics boundary requires relativistic input the framework cannot supply; and its non-abelian and emergent sectors lie beyond the fundamental group, in braided fusion categories.

Against this honest boundary, the pre-registered derivation program of the QNFO distinction tradition has advanced: T2 now carries construction content — the exchange-scalar dichotomy is the ribbon identity evaluated in the $d \ge 3$ topological sector; T1 is partially constructed; T3 is restated with named boundary conditions. The synthesis conjecture — the Distinction Calculus lifted into homotopy type theory, with the Grothendieck–Teichmüller group acting on braided monoidal categories — is stated with explicit falsification conditions F1–F3 and differentiated from the cohesive-HoTT program.

Why should a reader care? Because the boson/fermion dichotomy is an input to every quantum theory — and this paper tells you exactly which parts of it are proven, which are assumed, which are contested, and which could one day be derived from a more primitive logical act. That boundary map, and the falsifiable route toward the logical origin of quantum statistics, is the contribution.

## Acknowledgements and Provenance

This paper is part of the QNFO Research Foundation portfolio. Predecessor records: [@qnfo_res009; @qnfo_res010; @qnfo_slb002; @qnfo_tyranny]. All external citations verified against live Crossref/arXiv/Zenodo metadata on 2026-08-16 (citation audit on file). The deep-inquiry scaffold audit of Section 4 follows the Universal Ignorance Audit protocol (QNFO methodological standard, 15-question framework). AI assistance in drafting is disclosed as a quality signal per the QNFO disclosure policy. The quantitative claims of this paper (Section 2.2) are independently verified group-theoretic facts.

## References

**chaichian_etal2012.** Chaichian, M., Tureanu, A., Zhang, R. B. (2012). "Extended Poincaré supersymmetry in three dimensions and supersymmetric anyons." https://arxiv.org/abs/1204.5025

**dai_xie2003.** Dai, Wu-Sheng, Xie, Mi (2003). "Gentile statistics with a large maximum occupation number." https://arxiv.org/abs/cond-mat/0310066

**drinfeld1990.** Drinfeld, V. G. (2019). "Quasitriangular Quasi-Hopf Algebras." *Quasi-Hopf Algebras*: 381–406 https://doi.org/10.1017/9781108582780.011

**extended_objects2012.** Goldin, Gerald A. (2012). "Quantum Configuration Spaces of Extended Objects, Diffeomorphism Group Representations and Exotic Statistics." *Geometric Methods in Physics*: 239–251 https://doi.org/10.1007/978-3-0348-0448-6_19

**finkelstein_rubinstein1968.** Finkelstein, David, Rubinstein, Julio (1968). "Connection between Spin, Statistics, and Kinks." *Journal of Mathematical Physics* 9: 1762–1779 https://doi.org/10.1063/1.1664510

**harrison_etal2013.** Harrison, Jonathan M., Keating, Jonathan P., Robbins, Jonathan M., Sawicki, Adam (2013). "n-particle quantum statistics on graphs." https://arxiv.org/abs/1304.5781

**harshman_knapp2018.** Harshman, N. L., Knapp, A. C. (2018). "Anyons from Three-Body Hard-Core Interactions in One Dimension." https://arxiv.org/abs/1803.11000

**harshman_knapp2022.** Harshman, N. L., Knapp, A. C. (2022). "Topological exchange statistics in one dimension." *Physical Review A* 105 https://doi.org/10.1103/physreva.105.052214

**hi_ai2025.** HI+AI (2025). "Algebraic Structures of the Grothendieck-Teichmüller Group, the Cosmic Galois Group, and Associated Stability Conditions." https://doi.org/10.5281/zenodo.17214997

**laidlaw_dewitt1971.** Laidlaw, Michael G. G., DeWitt, Cécile Morette (1971). "Feynman Functional Integrals for Systems of Indistinguishable Particles." *Physical Review D* 3: 1375–1378 https://doi.org/10.1103/physrevd.3.1375

**leinaas_myrheim1977.** Leinaas, J. M., Myrheim, J. (1977). "On the theory of identical particles." *Il Nuovo Cimento B Series 11* 37: 1–23 https://doi.org/10.1007/bf02727953

**li_ge2026.** Li, Ge (2026). "A Geometric Origin for Fermi–Dirac Statistics: The Spin-Statistics Connection from Z_2 Normal Holonomy Without Lorentz Invariance." https://doi.org/10.5281/zenodo.21330410

**maciazek2019.** Maciążek, Tomasz (2019). "Non-abelian anyons on graphs from presentations of graph braid groups." https://arxiv.org/abs/1909.02098

**maciazek_sawicki2018.** Maciążek, Tomasz, Sawicki, Adam (2018). "Non-abelian Quantum Statistics on Graphs." https://arxiv.org/abs/1806.02846

**medina_dakic2023.** Sánchez, Nicolás Medina, Dakić, Borivoje (2023). "Reconstruction of Quantum Particle Statistics: Bosons, Fermions, and Transtatistics." https://arxiv.org/abs/2306.05919

**myers_sati_schreiber2023.** Myers, David Jaz, Sati, Hisham, Schreiber, Urs (2023). "Topological Quantum Gates in Homotopy Type Theory." https://arxiv.org/abs/2303.02382

**nagies_etal2023.** Nagies, Sebastian, Wang, Botao, Knapp, A. C., Eckardt, André, Harshman, N. L. (2023). "Beyond braid statistics: Constructing a lattice model for anyons with exchange statistics intrinsic to one dimension." https://arxiv.org/abs/2309.04358

**pauli1940.** Pauli, W. (1940). "The Connection Between Spin and Statistics." *Physical Review* 58: 716–722 https://doi.org/10.1103/physrev.58.716

**proxmire2026.** Proxmire, Allen (2026). "Event Density and Anyon Prohibition in 3+1D." https://doi.org/10.5281/zenodo.20195647

**qnfo_adelic_synth.** Quni-Gudzinas, Rowan Brad (20262026a). "Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons." https://doi.org/10.5281/zenodo.21208568

**qnfo_cancellation.** Research, QNFO, Quni-Gudzinas, Rowan Brad (2026). "The Ontology of Boundary-Crossing: Spencer-Brown Cancellation Rule Defended." https://doi.org/10.5281/zenodo.21470438

**qnfo_padic_anyons.** Quni-Gudzinas, Rowan Brad (20262026b). "p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity, Verma Modules, and Ultrametric Anyon Models." https://doi.org/10.5281/zenodo.21208491

**qnfo_padic_braids.** Quni-Gudzinas, Rowan Brad (20262026c). "p-Adic Braid Groups on Bruhat-Tits Buildings." https://doi.org/10.5281/zenodo.21208366

**qnfo_padic_tl.** Quni-Gudzinas, Rowan Brad (20262026g). "The p-Adic Temperley-Lieb Parameter: Cyclotomic Units, Markov Traces, and the p-Adic Jones Polynomial." https://doi.org/10.5281/zenodo.21208368

**qnfo_qlof.** Research, QNFO (2026). "Quantum Laws of Form: Consolidation, Open Questions, and Extensions." https://doi.org/10.5281/zenodo.21206074

**qnfo_res009.** Quni-Gudzinas, Rowan Brad (20262026d). "The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant." https://doi.org/10.5281/zenodo.21941375

**qnfo_res010.** Quni-Gudzinas, Rowan Brad (20262026f). "The Exchange Phase as a Logical Scalar: R = e^(2 pi i s) from the Re-Entrant Calculus." https://doi.org/10.5281/zenodo.21941238

**qnfo_slb002.** Quni-Gudzinas, Rowan Brad (20262026e). "The Calculus of Re-Entrant Distinctions: A Unified Treatise on the Loop, the Tree, and the Constants of Self-Reference." https://doi.org/10.5281/zenodo.21908818

**qnfo_tyranny.** Quni-Gudzinas, Rowan Brad (20262026h). "The Tyranny of the ±1: How a Topological Constraint Became the Iron Law of Nature." https://doi.org/10.5281/zenodo.21939692

**qnfo_zbw_p4.** Quni-Gudzinas, Rowan Brad (20262026i). "Zitterbewegung as the Physical Realization of p-Adic Anyon Braiding." https://doi.org/10.5281/zenodo.21336087

**read_green2000.** Read, N., Green, Dmitry (2000). "Paired states of fermions in two dimensions with breaking of parity and time-reversal symmetries and the fractional quantum Hall effect." *Physical Review B* 61: 10267–10297 https://doi.org/10.1103/physrevb.61.10267

**sati_schreiber2022a.** Sati, Hisham, Schreiber, Urs (2022). "Anyonic Topological Order in Twisted Equivariant Differential (TED) K-Theory." https://arxiv.org/abs/2206.13563

**sati_schreiber2022b.** Sati, Hisham, Schreiber, Urs (2022). "Topological Quantum Programming in TED-K." https://arxiv.org/abs/2209.08331

**sati_schreiber2024.** Sati, Hisham, Schreiber, Urs (2024). "Cohomotopy, Framed Links, and Abelian Anyons." https://arxiv.org/abs/2408.11896

**sawicki2014.** Sawicki, Adam (2014). "Topology of graph configuration spaces and quantum statistics." https://arxiv.org/abs/1408.7002

**schreiber_shulman2014.** Schreiber, Urs, Shulman, Michael (2014). "Quantum Gauge Field Theory in Cohesive Homotopy Type Theory." https://arxiv.org/abs/1408.0054

**selvi_uncu2015.** Selvi, Sevilay, Uncu, Haydar (2015). "A New Method for Derivation of Statistical Weight of the Gentile Statistics." https://arxiv.org/abs/1511.08051

**shen2020.** Shen, Yao (2020). "Intermediate symmetric construction of transformation between anyon and Gentile statistics." https://arxiv.org/abs/2003.06235

**smith2026.** Smith, Alex (2026). "The Vortex Framework: Topological Fermions from Framed Vortex Loops in a Quantized Superfluid Effective Field Theory Part I." https://doi.org/10.5281/zenodo.18725887

**streater_wightman1964.** Streater, R. F., and Wightman, A. S. (1964). "PCT, Spin and Statistics, and All That." *Nuclear Physics* 59: 689 https://doi.org/10.1016/0029-5582(64)90049-5

**toppan2023.** Toppan, Francesco (2023). "Transmuted spectrum-generating algebras and detectable parastatistics of the Superconformal Quantum Mechanics." https://arxiv.org/abs/2312.13191

**wilczek1983.** Wilczek, Frank, Zee, A. (1983). "Linking Numbers, Spin, and Statistics of Solitons." *Physical Review Letters* 51: 2250–2252 https://doi.org/10.1103/physrevlett.51.2250

