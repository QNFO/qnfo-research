---
title: 'A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation'
author: 'Rowan Brad Quni-Gudzinas'
date: '2026-08-16'
license: 'QNFO Unified License Agreement (QNFO-ULA)'
doi: '10.5281/zenodo.21970454'
status: 'published'
---


**Subtitle:** The Electron as a Hook

**Contact:** rowan.quni@qnfo.org · **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**Version:** v0.1

### Abstract

The electron is the most precisely measured particle in physics and the workhorse of modern computation, yet the theoretical structure in which it lives rests on a series of assumptions that are load-bearing but rarely interrogated: the complex Hilbert-space postulate, the spin-statistics theorem's dependence on $3+1$ dimensions and Poincaré invariance, the Archimedean real-number valuation of every measured quantity, the thermodynamic foundations of irreversible computation, and the identification of the electron itself as a fixed, elementary object rather than a vacuum- and environment-dependent excitation. This treatise does not reject any of these assumptions; it maps them. Each assumption is stated explicitly, the edifices built on it are identified, its confirmed predictions are separated from its postulates, alternative formulations are catalogued, and falsifiability conditions are defined. **Why a reader should care:** every one of the assumptions examined here bears directly on a live technological or experimental frontier — energy-efficient computation, topological quantum computing, high-temperature superconductivity, precision metrology, and quantum gravity — and several of them (the reality of quasiparticles with fractional charge and statistics, the failure of the spin-statistics theorem in $2+1$ dimensions, the emergence of particles from different vacua) are already known to be false as universal statements. **Premise-depth disclosure:** the claims of this treatise are analytical and taxonomic rather than axiomatic-deductive; it introduces no new physical postulate, and its conclusions are as deep as the published physics it cites — its own unanalyzable primitives are ordinary set theory, the standard model of measurement practice, and the requirement of empirical adequacy, all named here rather than hidden. The treatise concludes with a consolidated falsifiability map and a registry of open questions, so that the assumptions themselves can be promoted from articles of faith to objects of experiment.

**Keywords:** quantum foundations, spin-statistics theorem, quasiparticles, Landauer's principle, Ostrowski's theorem, Hilbert space, anyons, thermodynamics of computation, premise depth, falsifiability

---

### Preface

#### Why the electron?

No object in physics carries more load than the electron. It carries the precision tests of quantum electrodynamics, the entire edifice of solid-state electronics, the thermodynamic limits of computation, and — through the spin-statistics theorem — the stability of matter itself. Precisely because the electron is everywhere in physics, the assumptions that support our description of the electron are load-bearing for physics as a whole. Pulling on the electron means pulling on Hilbert space, on unitarity, on the Pauli exclusion principle, on the real-number continuum, on the second law, and on the notion of "particle" itself.

#### What this treatise is, and is not

This treatise is an assumption audit. For each load-bearing assumption it states the assumption, identifies what is built on it, distinguishes what is experimentally confirmed from what is postulated, catalogues alternatives, and defines conditions under which the assumption could be shown to fail. It is **not** a claim that current physics is wrong. It is **not** a claim that any alternative framework is correct. It is **not** an exercise in philosophy dressed as physics. Every question raised here is raised because it is either already experimentally visible (anyons, quasiparticles, vacuum-dependent particle content) or practically consequential (the energy cost of computation, the design space of quantum devices).

#### The danger of treating frameworks as dogma

A framework that has never failed within its tested domain is a successful framework, not a complete one. The history of physics is a sequence of frameworks whose domains of validity were discovered to have edges: Newtonian mechanics, classical electrodynamics, and local hidden-variable theories all failed at their edges in measurable ways. The frameworks examined in this treatise — Hilbert-space quantum mechanics, exact Lorentz invariance, Archimedean valuation, ergodicity — each have proposed edges. Mapping those edges is not disloyalty to the framework; it is the ordinary scientific procedure by which domains of validity are established rather than assumed.

#### How this treatise is organized

Part I presents the full architecture of the treatise: nine parts and fifty-one chapters spanning the electron as object, Hilbert-space dogma, spin and statistics, thermodynamics and computation, measurement and valuation, vacuum and dimensionality, cross-cutting foundational assumptions, a critical research programme, and a consolidated register of open questions. Parts II and III present the first two substantive research notes of the programme: a study of the quantum surface and the thermodynamic meaning of scale, and an adversarial assumption audit of the most ordinary object in electrical engineering, the copper wire. Part IV consolidates the open questions into a falsifiability map.

### Methodology

For every assumption examined, the treatise applies a fixed six-step procedure:

1. **State the assumption explicitly**, in its strongest, most standard form.
2. **Identify what is built on it** — theories, technologies, and theorems that depend on the assumption.
3. **Distinguish confirmed predictions from postulates** — what is measured, what is derived, what is assumed.
4. **List alternative formulations** that preserve the confirmed predictions while relaxing the assumption.
5. **Define falsifiability conditions** — experiments or theorems that would discriminate the assumption from its alternatives.
6. **Record open questions** in the consolidated register.

Only scientific criteria are used: predictive power, empirical adequacy, internal consistency, and domain of validity. No assumption is rejected by default; no assumption is retained by tradition.

---

## Part I — The Architecture of the Treatise

### I.1 Front Matter

The treatise proper opens with an abstract, a preface on the danger of treating scientific frameworks as dogma, acknowledgments, and a notation-and-conventions section that fixes the distinction between **postulate**, **theorem**, **empirical fact**, and **open question** — the four categories that all subsequent analysis depends on.

### I.2 Introduction

**Motivation.** The electron is the most precisely measured particle in physics: its charge, mass, and magnetic moment are among the best-determined numbers in science. It is simultaneously the basis of modern electronics and computation. The very success of the electron conceals the assumptions on which its description rests, and foundational questions about the electron are not separate from practical technology — they are the design constraints of the next generation of devices.

**The central claim.** The electron is a point of convergence — and a point of potential failure — for many deep assumptions of physics. Examining those assumptions is scientifically necessary, not merely philosophical. The goal is not to reject current physics but to map the domains of validity of its load-bearing postulates.

**Methodology.** The six-step procedure of the preceding section, applied uniformly.

**Structure.** Nine parts, fifty-one chapters, four appendices, with every part closing on its own list of open questions.

### I.3 Part I (of the treatise): The Electron as Known and as Probe

**Chapter 1 — The Standard Model Electron.** Definition and quantum numbers: spin-$1/2$, charge $-e$, lepton number, mass; the Dirac field and its free-particle solutions; the electron's place in the Standard Model Lagrangian.

**Chapter 2 — Measured Properties.** Charge from Millikan to modern precision; mass from Penning-trap cyclotron-frequency ratios; the magnetic moment anomaly $g-2$; upper bounds on the electric dipole moment; stability limits on the electron lifetime. What is confirmed: the agreement between theory and experiment for $g-2$ at the level of parts per trillion, constraints on compositeness, and lepton-number conservation.

**Chapter 3 — The Electron as a Renormalized Excitation.** The bare versus the dressed electron: renormalization in QED, the running coupling and mass, the electron as an excitation of the vacuum. The electron in a material: the quasiparticle concept, effective mass, lifetime, dispersion, dressing by phonons, magnons, and plasmons. Fermi-liquid theory and its breakdown: the electron as an emergent, environment-dependent object.

**Chapter 4 — Open Questions about the Electron Itself.** Is charge quantization exact and derivable? Is the electron absolutely stable? Is it elementary or composite? What fixes its mass? Can a finite region of a finite-dimensional Hilbert space describe it without conflict?

### I.4 Part II (of the treatise): Hilbert Space Dogma and Its Alternatives

**Chapter 5 — The von Neumann Postulate.** States as vectors in a complex Hilbert space; observables as self-adjoint operators; tensor-product composition; unitary evolution; the Born rule. Historical origin in von Neumann's *Mathematical Foundations of Quantum Mechanics* and the reasons the axiomatization became standard.

**Chapter 6 — Hidden Assumptions Inside the Hilbert-Space Framework.** Six assumptions that ride inside the standard axiomatization: complex linear superposition; exact unitarity; tensor-product factorization; infinite-dimensional state spaces; the identification of every observable with a self-adjoint operator; and real, Archimedean probability.

**Chapter 7 — Alternatives to Hilbert Space.** Real quantum mechanics; quaternionic quantum mechanics; algebraic quantum theory; generalized probabilistic theories; finite-dimensional Hilbert spaces; path-integral formulations without an explicit Hilbert space.

**Chapter 8 — Falsifiability and Open Questions.** Can real, complex, and quaternionic quantum mechanics be distinguished experimentally? Does a finite-dimensional Hilbert space for a causal diamond conflict with observation? Can the Born rule be derived without assuming Hilbert-space geometry? Does quantum gravity require abandoning the tensor-product structure? What experiment would reveal a failure of the Hilbert-space assumption?

### I.5 Part III (of the treatise): Spin, Statistics, and the Pauli Exclusion Principle

**Chapter 9 — What Spin Is Mathematically.** Spin as a label for irreducible representations of the Poincaré group; spin-$1/2$ and $SU(2)$; the observation that spin is not literal rotation.

**Chapter 10 — The Spin-Statistics Theorem.** Statement of the theorem; its assumptions — Lorentz invariance, microcausality, positive energy, positive norm, $3+1$ dimensions; its consequences, including the Pauli exclusion principle and the stability of matter.

**Chapter 11 — Where the Theorem Fails.** $2+1$ dimensions and anyons; the fractional quantum Hall effect; the braid group versus the permutation group; the experimental evidence for anyons.

**Chapter 12 — Statistics as Emergent, Not Intrinsic.** Quasiparticle statistics in condensed matter; the electron as a quasiparticle in different ground states; the implications for the word "elementary."

**Chapter 13 — Open Questions.** Why no parastatistics in $3+1$ dimensions? Are anyons only effective, or can they be elementary? Can spin emerge from a more primitive degree of freedom? Does spin-statistics survive in nonlocal or Lorentz-violating theories? How do anyonic quasiparticles alter the definition of particle identity?

### I.6 Part IV (of the treatise): The Electron in Thermodynamics and Computation

**Chapter 14 — The Physical Basis of Modern Computation.** The transistor and electron control; band theory and Fermi-Dirac statistics; semiconductors and CMOS.

**Chapter 15 — Thermodynamic Limits of Computation.** Landauer's principle; Shannon information versus physical implementation; measured dissipation versus the Landauer bound; reversible computing.

**Chapter 16 — Nonequilibrium Thermodynamics of Electrons.** Equilibrium statistical mechanics; fluctuation theorems; quantum thermodynamics; many-body localization and ergodicity breaking; strongly correlated electron systems.

**Chapter 17 — Electron-Based Quantum Computation.** Spin qubits; superconducting qubits; topological qubits from electron systems; the thermodynamic overhead of quantum computation.

**Chapter 18 — Open Questions.** What is the true minimum energy cost of an irreversible electron device? Can reversible computing approach the Landauer limit in practice? How do quantum correlations affect entropy production? Can spin-based logic outperform charge-based logic in energy efficiency? What is the ultimate heat-dissipation limit in a quantum many-electron system? Can fluctuation theorems be extended to strongly correlated electrons? Is the Church-Turing thesis empirically valid for all physical computation?

### I.7 Part V (of the treatise): Measurement Theory and Valuation Structure

**Chapter 19 — How Electron Observables Are Measured.** Interaction with classical instruments; the finite precision of real measurement; real numbers as an idealization.

**Chapter 20 — Ostrowski's Theorem and the Choice of Valuation.** Statement of Ostrowski's theorem; Archimedean versus $p$-adic absolute values; the adelic approach; the fact that mathematics does not select $\mathbb{R}$ — the real numbers are only one completion of $\mathbb{Q}$ among infinitely many inequivalent ones.

**Chapter 21 — Why Physics Currently Selects Archimedean Structure.** The empirical success of real-valued measurement; additivity and ordering; quantum mechanics and real probabilities.

**Chapter 22 — Hidden Assumptions in Measurement Theory.** That physical observables form an Archimedean ordered field; that spacetime is modelled on $\mathbb{R}^n$; that probabilities obey the Kolmogorov axioms; that measurement reduces to additive numerical comparison; that relevant closeness is magnitude-based.

**Chapter 23 — Alternatives and Testable Consequences.** $p$-adic quantum mechanics; adelic formulations; finite-precision physics; non-Kolmogorov probability; generalized measurement theory.

**Chapter 24 — Open Questions.** Are there physical variables naturally described by $p$-adic or ultrametric structure? Does the continuum have more structure than measurement requires? Can quantum measurement be formulated without the continuum? Is there an experiment that distinguishes Archimedean from non-Archimedean valuation? What is the minimal measurement-theoretic structure needed to encode all empirical content? Does finite-precision measurement imply a discrete or finite formulation of quantum mechanics?

### I.8 Part VI (of the treatise): Vacuum, Dimensionality, Holography, and Emergence

**Chapter 25 — Vacuum Dependence of Particle Content.** Particles as excitations of a chosen vacuum; the Unruh effect; cosmological particle creation; the absence of a unique vacuum in curved spacetime.

**Chapter 26 — Quasiparticles and Anyons in Condensed Matter.** Electron quasiparticles; fractional charge and fractional statistics; topological order; the fact that the same underlying electrons support different emergent particles in different ground states.

**Chapter 27 — Dimensionality and Physical Law.** Behaviour in one, two, and three dimensions; the Mermin-Wagner theorem; the Kosterlitz-Thouless transition; the upper critical dimension; the quantum-classical mapping.

**Chapter 28 — The Holographic Principle.** Statement of the principle; AdS/CFT as a precise duality; bulk versus boundary; applications to strongly correlated electrons; the caution that holography is not simply "2D applies to 3D."

**Chapter 29 — Open Questions.** Is the electron fundamental or emergent? What are the true primitives if particle number and statistics are vacuum-dependent? Can topological quantum computation use electron-derived quasiparticles? Does holography imply that local quantum field theory is only effective? Are there observable consequences of treating the electron as a quasiparticle in high-energy physics? What is the correct description of electron states without a global vacuum?

### I.9 Part VII (of the treatise): Cross-Cutting Foundational Assumptions

**Chapter 30 — The Axiom of Choice.** Statement; its use in functional analysis, topology, and measure theory; its independence from ZF; constructive alternatives; potential physical relevance.

**Chapter 31 — The Church-Turing Thesis.** Statement; the physical version; quantum computation and Turing computability; the possibility of hypercomputation; empirical status.

**Chapter 32 — The Real Number Continuum.** Infinite divisibility and Archimedean order; Ostrowski's theorem recapped; empirical support and limits; possible discreteness or non-Archimedean structure.

**Chapter 33 — Microcausality and Locality.** Statement; role in spin-statistics and CPT; the distinction from Bell's theorem; nonlocal corrections from quantum gravity; falsifiability.

**Chapter 34 — Fixed Spacetime Background.** Standard QFT reliance; background independence in quantum gravity; emergent spacetime.

**Chapter 35 — Unitarity as Absolute.** Open-system non-unitarity; black-hole information; objective collapse models; tests.

**Chapter 36 — The Path Integral as Well-Defined.** Successes and rigor issues; lattice regularization; nonperturbative alternatives.

**Chapter 37 — Symmetry as Fundamental.** Gauge symmetries; emergent gauge fields; symmetries as redundant descriptions; possible compositeness.

**Chapter 38 — Ergodicity and the Eigenstate Thermalization Hypothesis.** Violations: many-body localization, quantum scars; implications for thermodynamics; open questions.

**Chapter 39 — Global Hyperbolicity.** Predictability in general relativity; alternatives: closed timelike curves, naked singularities; quantum-gravity implications.

**Chapter 40 — Extensivity of Entropy.** Black-hole area law; entanglement entropy; generalized entropies.

**Chapter 41 — Exact Lorentz Invariance.** Tests; Planck-scale violation; emergent Lorentz symmetry.

**Chapter 42 — Kolmogorov Probability Axioms.** Quantum probability generalization; non-Kolmogorov frameworks; measurement implications.

**Chapter 43 — Smooth Manifold Spacetime.** Planck-scale breakdown; causal sets, noncommutative geometry; observability.

**Chapter 44 — The Assumption That Mathematics Is the Language of Nature.** Galileo and Wigner; computational and information-theoretic alternatives; limits of formalization.

### I.10 Part VIII (of the treatise): A Critical Research Programme

**Chapter 45 — Guiding Principles.** Every load-bearing assumption is a falsifiable postulate; domain-of-validity mapping; no assumption is rejected by default; alternatives must be empirically distinguishable.

**Chapter 46 — Experimental Probes.** Precision electron measurements ($g-2$, EDM, stability); anyon interferometry; quantum simulation of non-Archimedean or finite-dimensional structures; tests of Lorentz violation; spin-statistics tests; quantum thermodynamics of single-electron devices; entropy production in strongly correlated systems; engineered $p$-adic or adelic quantum models; probes of spacetime smoothness at Planck scales.

**Chapter 47 — Theoretical Probes.** Real and quaternionic quantum mechanics with observable signatures; model-independent frameworks; finite-dimensional quantum mechanics for causal diamonds; measurement theory without Kolmogorov probability; $p$-adic and adelic models of known physics; deriving spin-statistics from information principles; thermodynamics without ergodicity; emergent spacetime and holographic models.

**Chapter 48 — Milestones and Decision Points.** Short-term: precision tests of existing assumptions. Medium-term: distinguishing alternative quantum frameworks. Long-term: replacing or confirming foundational postulates.

### I.11 Part IX (of the treatise): Consolidated Open Questions

**Chapter 49 — List of All Open Questions.** Organized by theme; each question tied to a chapter and to a possible experiment or theoretical development.

**Chapter 50 — Questions Most Likely to Yield Practical Advances.** Energy-efficient computation; high-temperature superconductors; topological quantum computing; nanoscale thermodynamics; spintronics.

**Chapter 51 — Questions Most Likely to Yield Foundational Advances.** The nature of Hilbert space; the origin of spin and statistics; the valuation structure of physical quantities; the emergence of spacetime; the nature of entropy and time.

### I.12 Conclusion (of the treatise)

The argument in summary: the electron is a hook for foundational assumptions; many of those assumptions are load-bearing but unproven; domains of validity must be mapped empirically. What the treatise does **not** claim: that current physics is wrong, that alternatives are correct, that philosophy replaces experiment. What it **does** claim: the assumptions are contingent, they are testable in principle, and investigating them is scientifically necessary. Final statement: pulling on the electron may open the entire foundation.

### I.13 Appendices

**Appendix A — Mathematical Background.** Hilbert spaces; representation theory; Ostrowski's theorem; the braid group; $p$-adic numbers; adeles.

**Appendix B — Experimental Techniques.** Penning traps; anyon interferometry; quantum simulation; precision measurement.

**Appendix C — Glossary of Terms.** Quasiparticle, anyon, vacuum, Hilbert space, valuation, and related terms.

**Appendix D — Bibliography.** Primary sources, reviews, and experimental papers, as given in the References of this document and its accompanying `references.bib`.

This architecture is the skeleton of the treatise. Each chapter is designed to be expanded with rigorous definitions, equations, experimental summaries, and explicit open questions. The overall thesis: the electron — far from being a closed chapter — is a live diagnostic for the foundations of physics and computation.

---

## Part II — Research Note A: The Quantum Surface and the Thermodynamics of Scale

*This note condenses a working analysis (Obsidian source note `_26228215041.md`, deposited verbatim with this record) of the surface-versus-bulk distinction in conductors, stated in natural units so that the invariant dimensionless content is visible.*

### II.1 Conductance as a count of modes

The conductance quantum is

$$G_0 = \frac{2e^2}{h},$$

and in natural units ($\hbar = c = 1$) this is not a new dimensionful constant but a pure number proportional to the fine-structure constant, $G_0 \sim \alpha$ up to convention-dependent factors. Ballistic conductance quantization then reads

$$G = n G_0 = n \frac{2e^2}{h},$$

where $n$ is an integer: the number of open transverse conduction channels. Conductivity is the same statement with geometry included — conductivity is $(e^2/h)$ times a dimensionless material number; in a diffusive metal,

$$\sigma \sim \frac{e^2}{h}\, k_F^2 \ell,$$

with $k_F = 2\pi/\lambda_F$ and $\ell$ the mean free path. The important object is not conductivity as a continuum but the dimensionless ratio $\sigma/(e^2/h) \sim k_F^2 \ell$. Transport becomes "quantum" when this ratio is of order one or when the channel count becomes small. Conductance quantization is therefore a counting statement: integer multiples of a fundamental ratio, not a continuum reading.

### II.2 Thermodynamics enters as an inverse scale

In natural units the thermal energy $k_B T$ is a frequency, and temperature defines an inverse length and inverse time:

$$T \sim \text{energy} \sim \text{frequency} \sim \frac{1}{\text{time}} \sim \frac{1}{\text{length}}.$$

The corresponding scale is the thermal de Broglie wavelength

$$\lambda_T = \frac{h}{\sqrt{2\pi m k_B T}},$$

which for free electrons at room temperature is on the order of $4$ nm — an order of magnitude above the copper Fermi wavelength ($\lambda_F \approx 0.46$ nm) and an order of magnitude below the room-temperature mean free path ($\ell \approx 40$ nm). Temperature is not merely "heat": it is the inverse scale that tells us which spatial and temporal distinctions are thermally resolved and which are washed out. A spatial structure of scale $L$ is compared to the thermal scale: for $L \gg \lambda_T$ thermal fluctuations average over the structure and a thermodynamic description applies; for $L \sim \lambda_T$ quantum and thermal scales compete and the spatial coordinate cannot be separated from the thermodynamic state; near a critical point a correlation length $\xi(T)$ diverges and spatial order becomes explicitly temperature-dependent. The physics lives in the dimensionless ratios — $L/\lambda_T$, $\lambda/\lambda_T$, $\lambda_F/\ell$ — not in meters and seconds.

### II.3 Electrical and thermal transport share the same channel count

Each ballistic channel carries not only a conductance quantum but a thermal conductance quantum,

$$G_{th} = \frac{\pi^2 k_B^2}{3h}\, T,$$

so that in natural units thermal conductance per channel is a pure number times temperature. The proportionality of the two transport coefficients is the Wiedemann–Franz law,

$$\frac{\kappa}{\sigma T} = L_0 = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2,$$

the Lorentz number — again a pure number in natural units, $\pi^2/(3\alpha)$ up to the fine-structure constant. Electrical and thermal transport are two views of the same integer channel count, and their ratio is a statement about the coupling constant rather than about the material.

### II.4 Surface versus bulk: the thermodynamic meaning

Two different notions of "surface" are routinely conflated, and they have different thermodynamic content.

**Skin effect.** The classical skin effect is a field redistribution inside a conductor: alternating current is expelled toward the outer region with skin depth $\delta = \sqrt{2\rho/(\omega\mu)}$. It is dissipative — AC resistance rises as the effective cross-section shrinks, and Joule heating is concentrated near the surface. It is not a mode-confinement effect: no protected boundary mode exists, and the current density decays smoothly rather than being localized by topology. When the skin depth falls below the mean free path (anomalous skin effect), the classical picture acquires nonlocal corrections, but the category — classical field redistribution — survives.

**Topological surface state.** A topological surface state is genuinely quantum and genuinely boundary-localized: it is a mode confined to the boundary and protected by the topology of the bulk band structure. Its conductance is quantized in integer multiples of $G_0$, and the quantization is robust to disorder as long as the bulk gap remains. Its protection, however, is itself thermodynamic: when $k_B T$ approaches the bulk gap, bulk states become thermally populated and the boundary distinction blurs. The dimensionless ratio $\Delta_{gap}/(k_B T)$ is the control parameter of topological protection.

The distinction between the two surfaces therefore survives the nanoscale: the skin effect is a classical field redistribution inside a conductor, while the topological boundary is a mode-confinement effect protected by bulk topology — the former dissipative, the latter dissipationless within its protected window. They are not the same kind of surface.

### II.5 The dimensionless ratios that actually matter

Strip away units and every transition discussed above becomes a statement about which dimensionless ratio crosses one:

| Transition | Control ratio |
|:-----------|:--------------|
| Classical $\to$ quantum transport | $G/G_0 \sim k_F^2 \ell \sim 1$ |
| Degenerate $\to$ classical statistics | $k_B T / E_F$ |
| Diffusive $\to$ ballistic | $\ell / L$ |
| Phase-coherent $\to$ thermally averaged | $L / L_T$ |
| Classical $\to$ anomalous skin effect | $\delta / \ell$ |
| Topologically protected $\to$ thermally destroyed | $\Delta_{gap} / (k_B T)$ |

This is the invariant, unit-free content of conductivity and thermodynamics: temperature assigns a scale to the world, and spatial coordinates become physically meaningful only relative to that scale. The quantized quantities themselves — channel counts, winding numbers, topological invariants — are integers, and the natural home of integer counts is the rational numbers, not the Archimedean real line. As noted in the treatise architecture (Chapter 20), Ostrowski's theorem leaves the metric completion of those counts as a choice: the Archimedean completion is the one selected by continuous phase and time measurement, but the underlying object is the count.

### II.6 Entropy as the primary count

The closing sections of the note develop the thermodynamic ontology that Part I's Chapter 15-18 rely on. The claims, in compressed form:

1. **Thermodynamics is the right coarse-grained language** for many-electron systems because it keeps only what is invariant under the loss of microstate detail: scale ratios and state counts.
2. **Temperature is not motion; it is a derivative.** Temperature is defined by $1/T = \partial S/\partial E$; it is an inverse energy scale, not an average kinetic energy per particle.
3. **Entropy is the primary count.** The extensive variable that survives coarse-graining is the logarithm of a state count; energy, temperature, and their conjugates are derived from it.
4. **The Compton frequency at $T=0$ is not a temperature.** An intrinsic oscillation scale ($\omega_C = mc^2/\hbar$) sets a frequency, not a thermodynamic state; temperature requires a distribution and a derivative of entropy.
5. **Residual and entanglement entropy.** Even at zero temperature, ground states of strongly correlated and topologically ordered systems carry residual entanglement entropy; entropy is not merely thermal disorder.
6. **$G$ is not fundamental.** The Newton constant is a conversion factor between energy density and curvature; in natural units it can be absorbed, and the note argues it should not be granted primitive status in a list of load-bearing structures.
7. **The minimal primitive set.** The note's provisional conclusion is that the minimal set of primitives is: state counts and their entropy, the coupling ratios (of which $\alpha$ is the prototype), and the metric places at which measurements are performed — with the real continuum demoted from primitive to a selected completion.

These seven points are the note's contribution to Part IV of the treatise (the thermodynamic limits of computation) and Part V (valuation structure): computation costs entropy because irreversibility destroys state count, and measurement reports real numbers because the Archimedean place is the one our instruments select — not because $\mathbb{R}$ is ontologically required.

---

## Part III — Research Note B: The Copper Wire as a Load-Bearing Example

*This note condenses a working analysis (Obsidian source note `_26228180242.md`, deposited verbatim with this record) that runs the treatise's assumption-audit procedure on the most ordinary object in electrical engineering — a copper wire — and then generalizes the procedure into a catalogue of load-bearing assumptions. The question that triggered the audit: "Is it fair to say a copper wire doesn't conduct electrons through it, but on it?"*

### III.1 The question, answered

At DC and low-frequency AC, a copper wire conducts electrons through its volume: conduction electrons move through the whole cross-section, and the current density is essentially uniform. At high frequency, the skin effect confines the alternating current to an outer layer of thickness $\delta = \sqrt{2\rho/(\omega\mu)}$ — still inside the metal, not on the geometric surface. At 60 Hz the skin depth in copper is about $8.5$ mm, so ordinary household wire conducts through essentially its whole cross-section. The statement "electricity flows on the wire" is therefore false as a general claim, and its partial truth at radio frequency is a statement about a current-density distribution, not about a geometric surface.

The deeper correction, however, concerns what travels where. The conduction electrons drift at millimeters per second; the electrical energy travels at a substantial fraction of light speed. The energy does not flow through the copper like water through a pipe: it flows in the electromagnetic fields in the space around the wire, guided by the surface charges and currents that the wire's electrons maintain (the Poynting-vector picture). So the accurate inversion of the naive claim is:

> The copper wire does not conduct electrical energy *through* its interior like a pipe. The energy travels in the fields outside the wire; the electrons inside merely drift slowly, and their currents and surface charge distributions *guide* the fields.

This is the territory. The remainder of the note is an audit of the scaffolds that hid it.

### III.2 The hidden scaffolds

The naive claim rests on several invisible scaffolds, each of which is an instance of a load-bearing assumption elsewhere in physics:

1. **The plumbing/container metaphor** — electricity imagined as a substance moving inside a pipe.
2. **The inside/outside binary** — "through" versus "on" presupposes a clean boundary between the wire's interior and its surface.
3. **The electron-as-billiard-ball model** — electrons imagined as discrete particles traveling along a path.
4. **The wire as a passive channel** — the wire treated as a container for moving charges rather than as part of a larger electromagnetic system.
5. **Conflation of visible stranding with electrical function** — because wires are stranded or bundled, it is assumed the strands carry current on their surfaces.
6. **Frequency blindness** — the claim ignores whether the regime is DC, mains AC, or radio frequency.

The scaffold is classical, mechanical, and spatial; it is useful and misleading at once.

### III.3 Where the map is mistaken for the territory

The map is the language of "through" and "on." The territory is a current-density distribution inside a conductor, plus an energy flux in the surrounding fields. At DC the current density is roughly uniform across the cross-section; at high frequency the skin effect pushes it outward — still within the metal. "On it" mistakes the geometric surface for the conductive region, and mistakes the visible stranding for the current path. More deeply, the map "electrons moving through a wire" is mistaken for the territory of energy transfer: the energy does not travel inside the copper; the fields do the transport, and the electrons maintain the boundary conditions.

### III.4 The wobbles

Four observations do not fit the pipe model, and each is a diagnostic:

1. **The oxide layer.** If electricity only flowed on the surface, the insulating copper-oxide layer would seriously degrade conduction; ordinary copper wire works because conduction is bulk, not surface.
2. **The skin effect exists.** If electricity only flowed through the bulk, the skin effect would not exist; at high frequency current demonstrably concentrates near the surface.
3. **Drift versus signal.** Electron drift speed is millimeters per second while a signal travels at a large fraction of light speed; the "flow" metaphor cannot hold both numbers.
4. **Bulk heating.** A DC-carrying wire warms throughout its volume — bulk dissipation, not surface-only conduction.

The central wobble: **the charge moves slowly inside the wire, but the energy moves quickly outside it.** That does not fit the pipe model, and the failure of the metaphor is measurable.

### III.5 The inversion

The opposite claim — "a copper wire conducts electrons only through its interior, not on its surface" — is also false for DC, because the surface region is part of the bulk cross-section and carries current too. The illuminating inversion is the Poynting-vector statement given above. It shifts attention from "electrons as carriers" to "fields as carriers," and it dissolves the through/on binary entirely: the correct partition is between *charge transport inside the conductor* and *energy transport in the surrounding fields*, two different things that the pipe model conflates.

### III.6 Where quantum effects actually enter

The note's companion analysis locates the quantum entry points precisely: quantum physics becomes explicit for surface-versus-bulk questions when a length scale approaches the Fermi wavelength ($\lambda_F \approx 0.46$ nm in copper) or the mean free path ($\approx 40$ nm at room temperature) — conductance quantization in integer multiples of $G_0 = 2e^2/h$, ballistic transport, quantum confinement, and, genuinely quantum and genuinely boundary-localized, the topological surface states protected by bulk topology. The skin effect and the topological boundary are not the same kind of "surface": the former is a classical field redistribution inside a conductor, the latter a mode-confinement effect. The category distinction survives the nanoscale.

### III.7 The load-bearing assumptions: a catalogue

The note generalizes the wire audit into a catalogue of fifteen load-bearing assumptions, each stated with what is built on it, its logical status, and what would follow if it failed. The catalogue is the raw material for Part VII of the treatise.

1. **Hilbert space as the universal quantum state space.** *Assertion:* every quantum system is a vector in a complex Hilbert space with self-adjoint observables. *Built on it:* all of quantum mechanics, QFT, quantum information, quantum computing, measurement theory, most of quantum gravity. *Status:* a modeling choice, not a theorem — it assumes complex linearity, unitarity, tensor-product composition, and unbounded self-adjoint operators. *If wrong:* reformulation in real, quaternionic, algebraic, or generalized-probabilistic frameworks would be required; proposals exist but none yet replaces the standard framework.

2. **The Axiom of Choice.** *Assertion:* every collection of nonempty sets admits a choice function. *Built on it:* large portions of functional analysis, topology, measure theory, algebra, logic. *Status:* independent of Zermelo–Fraenkel set theory; a convention, not a necessity. *If wrong:* choice-free reformulations of functional analysis and mathematical physics, including theorems essential to QFT, would be required.

3. **The Church–Turing thesis.** *Assertion:* every effectively computable function is Turing-computable; equivalently, every physical process is simulable by a Turing machine. *Built on it:* the theory of computation, algorithmic information theory, complexity theory, digital physics. *Status:* not a theorem — "effectively computable" is informal; the physical version is an empirical conjecture. *If wrong:* hypercomputation would be physically real; no experiment has demonstrated it.

4. **The real-number continuum as the model for physical quantities.** *Assertion:* space, time, and observables take values in $\mathbb{R}$. *Built on it:* calculus, differential equations, Riemannian geometry, path integrals, probability theory, the standard formulation of every fundamental theory. *Status:* a modeling choice; Ostrowski's theorem shows $\mathbb{R}$ is one completion of $\mathbb{Q}$ among infinitely many. *If wrong:* $p$-adic, adelic, finite, or discrete reformulations would move from fringe to necessity.

5. **Microcausality as exact.** *Assertion:* spacelike-separated observables commute. *Built on it:* the spin-statistics theorem, CPT, dispersion relations. *Status:* confirmed within experimental resolution; violation would not immediately conflict with macroscopic causality. *If wrong:* spin-statistics and CPT would lose their axiomatic footing.

6. **Fixed spacetime background.** *Assertion:* fields propagate on a pre-existing spacetime. *Built on it:* standard QFT. *Status:* an idealization; quantum gravity expects background independence. *If wrong:* QFT is effective, not fundamental.

7. **Unitarity as absolute.** *Assertion:* time evolution is exactly unitary. *Built on it:* probability conservation, the Born rule's consistency, black-hole thermodynamics' current formulations. *Status:* a postulate; open systems are effectively non-unitary. *If wrong:* information loss or objective collapse would be physical, with observable signatures.

8. **The path integral as well-defined.** *Assertion:* amplitudes are given by a functional integral over all histories. *Built on it:* most modern QFT calculations. *Status:* mathematically non-rigorous in the continuum; rigorous only after lattice regularization. *If wrong:* nonperturbative definitions must come from elsewhere.

9. **A unique Poincaré-invariant vacuum.** *Assertion:* the ground state is unique and Poincaré-invariant. *Built on it:* the particle interpretation of QFT. *Status:* false in general — curved spacetime and interacting theories admit inequivalent vacua. *If dropped:* particle content becomes observer- and background-dependent (Unruh effect, cosmological particle creation), as Part I Chapter 25 details.

10. **The ergodic hypothesis / eigenstate thermalization.** *Assertion:* closed systems thermalize; observables relax to microcanonical averages. *Built on it:* equilibrium statistical mechanics, thermodynamics of finite quantum systems. *Status:* known to fail in many-body localized systems and quantum scars. *If wrong in general:* thermodynamics must be rebuilt on weaker premises.

11. **Global hyperbolicity.** *Assertion:* spacetime admits a Cauchy surface; predictability holds. *Built on it:* classical general relativity's initial-value formulation. *Status:* a postulate; closed timelike curves and naked singularities are not excluded a priori. *If wrong:* retrodiction and prediction lose their standard footing.

12. **Extensivity of entropy.** *Assertion:* entropy scales with volume. *Built on it:* classical thermodynamics. *Status:* violated by black holes (area law) and by area-law entanglement in ground states. *If wrong:* generalized entropies and holographic counting are required.

13. **Exact Lorentz invariance.** *Assertion:* Lorentz symmetry is exact. *Built on it:* the Standard Model, spin-statistics. *Status:* tested to extreme precision; Planck-scale violation is an open possibility. *If wrong:* preferred-frame effects at high energy.

14. **Kolmogorov probability axioms.** *Assertion:* probabilities are measures on a $\sigma$-algebra obeying additivity. *Built on it:* classical statistics, standard measurement theory. *Status:* quantum interference violates classical additivity at the level of amplitudes; non-Kolmogorov generalizations exist. *If wrong:* measurement theory and statistics need non-additive or non-Archimedean formulations.

15. **$C^\infty$ smooth manifold spacetime.** *Assertion:* spacetime is a smooth Lorentzian manifold. *Built on it:* general relativity, the differential geometry of physics. *Status:* an idealization; Planck-scale breakdown expected. *If wrong:* causal sets, noncommutative geometry, or emergent spacetime replace the manifold.

### III.8 The dogma list

A companion section enumerates sixteen items that function as *dogmas* — assumptions elevated to orthodoxy without being theorems: the von Neumann axiomatization; the Copenhagen interpretation as orthodoxy; the Born rule as unexplained axiom; unitarity as sacred; microcausality and strict locality; the fixed spacetime background; spacetime as a smooth manifold; exact Lorentz invariance; the path integral as fundamental; symmetry as fundamental; the particle concept as fundamental; the Big Bang singularity as a creation event; the cosmological constant as constant; ergodicity and equilibrium thermodynamics; the real number continuum as physical; and the assumption that mathematics is the language of nature. Each is a candidate for reclassification from dogma to testable postulate, and each maps onto a chapter of Part VII.

### III.9 The electron's conditional status

The note closes with the argument that the electron is best regarded as a *conditional* object:

1. **The Standard Model taxonomy is not false, but it is conditional.** The fermion/boson classification is experimentally confirmed for known elementary particles, but it holds under four conditions: a Poincaré-invariant vacuum, $3+1$ dimensions, perturbative asymptotic states, and no ground-state-modifying background medium. Those conditions are a special case, not a universal law.

2. **The electron as observed is not a bare particle.** In a metal, the "electron" is a quasiparticle: its effective mass differs from the free mass, it has a finite lifetime, its dispersion is modified by the lattice, and it is dressed by phonons, magnons, and other electrons. In the fractional quantum Hall effect the excitation is not even an electron but a quasiparticle carrying fractional charge ($e/3$). The identity "electron" depends on the ground state and the probing scale.

3. **Anyons show that statistics is a property of the system, not the particle.** In $3+1$ dimensions exchange gives phase $\pm 1$ only; in $2+1$ dimensions the braid group replaces the permutation group and the phase $\psi \to e^{i\theta}\psi$ is arbitrary. Fractional quantum Hall experiments have observed fractional charge, fractional statistics, and anyonic braiding signatures. The spin-statistics theorem does not apply because its premises — $3+1$ dimensions, Lorentz invariance — fail.

4. **Particle content is frame- and vacuum-dependent.** An inertial observer sees the Minkowski vacuum as empty; a uniformly accelerated observer sees a thermal bath at the Unruh temperature $T_U = \hbar a/(2\pi k_B c)$; an expanding universe produces particles cosmologically. Particle number is not a relativistic invariant.

5. **Condensed matter and particle physics use the same formalism, not different realities.** Both describe excitations above a ground state with effective fields, quasiparticles, effective masses, gauge fields, symmetry breaking, and renormalization-group flow. The difference is the ground state, not the mathematics.

6. **What this calls into question.** If the same mathematical structure produces different "particles" under different vacua, the particle concept is not fundamental. Better candidates for primitives: quantum states and Hilbert space (possibly themselves emergent), symmetries and conservation laws, causality and locality, effective field theory and the renormalization group, and measurement relations — including the choice of valuation structure.

7. **The precise bottom line.** The fermion/boson split is valid in a $3+1$-dimensional Poincaré-invariant vacuum; in $2$ dimensions or nontrivial ground states statistics changes and anyons emerge; the electron in a solid is not the electron in vacuum. Particles are emergent patterns in a quantum many-body state — real patterns, but not the ultimate primitives.

## Part IV — Consolidated Open Questions and the Falsifiability Map

### IV.1 Open questions most likely to yield practical advances

1. What is the true minimum energy cost of an irreversible electron device, and can reversible computing approach the Landauer limit in practice?
2. Can spin-based logic be more energy-efficient than charge-based logic, given that the thermal scale $k_B T$ sets the resolution of both?
3. Can topological quantum computation use electron-derived quasiparticles, and over what temperature window does topological protection survive?
4. How do quantum correlations alter entropy production in strongly correlated systems, and can fluctuation theorems be extended to them?
5. What is the ultimate heat-dissipation limit in a quantum many-electron system?

### IV.2 Open questions most likely to yield foundational advances

1. Can real, complex, and quaternionic quantum mechanics be distinguished experimentally?
2. Does finite-dimensional Hilbert space for a causal diamond conflict with observation?
3. Are there physical variables naturally described by $p$-adic or ultrametric structure, and is there an experiment that distinguishes Archimedean from non-Archimedean valuation?
4. Is the electron fundamental or emergent, and what are the true primitives if particle number and statistics are vacuum-dependent?
5. Does spin-statistics survive in nonlocal or Lorentz-violating theories, and why is there no parastatistics in $3+1$ dimensions?
6. Does holography imply that local quantum field theory is only effective?
7. Is the Church-Turing thesis empirically valid for all physical computation?

### IV.3 Falsifiability map

Each assumption in the III.7 catalogue admits a discriminating observation or theorem:

| Assumption | Discriminating test |
|:-----------|:--------------------|
| Complex Hilbert space | Interference experiments distinguishing complex, real, and quaternionic amplitudes (generalized interference) |
| Axiom of Choice | Choice-free reconstruction of the physical theorems; operational anomalies of non-measurable sets |
| Church-Turing thesis | Demonstration of a physical process producing a non-Turing-computable output |
| Real continuum | Finite-precision physics; $p$-adic signatures in hierarchical or resonant systems |
| Microcausality | Limits on spacelike commutators at ever higher precision |
| Unitarity | Collapse-model bounds; black-hole information tests |
| Unique vacuum | Unruh effect; cosmological particle creation (already established as non-unique in curved spacetime) |
| Ergodicity | Many-body localization and quantum-scar platforms (already established as violations) |
| Extensivity of entropy | Area-law measurements in gravity and ground-state entanglement |
| Exact Lorentz invariance | Preferred-frame searches at Planck-scale sensitivity |
| Kolmogorov axioms | Quantum-logic and generalized-probability operational tests |
| Smooth manifold | Planck-scale dispersion, causal-set signatures |

The falsifiability map is the operational form of the treatise's central claim: the load-bearing assumptions of quantum mechanics, thermodynamics, and computation are contingent, testable in principle, and already failing at known edges. Mapping their domains of validity is the programme.

## Conclusion

The electron was chosen as the hook because no other object concentrates so many of physics' load-bearing assumptions in one place: the Hilbert-space postulate, the spin-statistics theorem, the Archimedean valuation of measurement, the thermodynamic limits of computation, and the particle concept itself. The treatise's method is uniform: state the assumption, catalogue what is built on it, separate the confirmed from the postulated, list the alternatives, define falsifiability, and record the open question. The first two research notes demonstrate the method in action — one on the quantum surface and the thermodynamics of scale, one on the humble copper wire — and show that even the most ordinary objects conceal the deepest scaffolds.

The treatise does not claim current physics is wrong. It does not claim any alternative is correct. It claims, on the evidence assembled here, that the assumptions are contingent, that several of them are already known to fail outside special domains (anyons, quasiparticles, vacuum-dependent particle content, broken ergodicity), and that investigating the rest is scientifically necessary rather than merely philosophical. Pulling on the electron may open the entire foundation; the purpose of this treatise is to make the pull precise, itemized, and falsifiable.

### Declarations

**Author contributions.** Single-author work. The author directed the research programme; AI-assisted tooling was used for literature retrieval, drafting assistance, and checking under human supervision, per the disclosure principles of the QNFO AI-assisted research pipeline.

**Funding.** Self-funded. No external grants.

**Competing interests.** None declared.

**Data availability.** All source notes, build artifacts, and evidence files are deposited with this record (see `source-notes/` and `artifacts/`).

**AI-use disclosure.** AI assistance was used and is disclosed, consistent with the QNFO Unified License Agreement and the epistemic-legibility principles of the QNFO pipeline.

**License.** QNFO Unified License Agreement (QNFO-ULA).

**Prior publication.** None. This is the first release (v0.1).

**Peer review.** Post-publication adversarial audit documented in `artifacts/post-publication-audit.md`.

**Version history.** v0.1 — initial release, 2026-08-16.

## References

1. Dirac, P. A. M. (1928). The quantum theory of the electron. *Proceedings of the Royal Society A* 117(778), 610–624.
2. von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik.* Springer, Berlin.
3. Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung $\varphi(x)\varphi(y) = \varphi(xy)$. *Acta Mathematica* 41, 271–284.
4. Wigner, E. P. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40(1), 149–204.
5. Pauli, W. (1940). The connection between spin and statistics. *Physical Review* 58(8), 716–722.
6. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development* 5(3), 183–191.
7. Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development* 17(6), 525–532.
8. Unruh, W. G. (1976). Notes on black-hole evaporation. *Physical Review D* 14(4), 870–892.
9. Leinaas, J. M., & Myrheim, J. (1977). On the theory of identical particles. *Il Nuovo Cimento B* 37(1), 1–23.
10. Tsui, D. C., Stormer, H. L., & Gossard, A. C. (1982). Two-dimensional magnetotransport in the extreme quantum limit. *Physical Review Letters* 48(22), 1559–1562.
11. Wilczek, F. (1982). Quantum mechanics of fractional-spin particles. *Physical Review Letters* 49(14), 957–959.
12. Laughlin, R. B. (1983). Anomalous quantum Hall effect: an incompressible quantum fluid with fractionally charged excitations. *Physical Review Letters* 50(18), 1395–1398.
13. Arovas, D., Schrieffer, J. R., & Wilczek, F. (1984). Fractional statistics and the quantum Hall effect. *Physical Review Letters* 53(7), 722–723.
14. Halperin, B. I. (1984). Statistics of quasiparticles and the hierarchy of fractional quantized Hall states. *Physical Review Letters* 52(18), 1583–1586.
15. Mermin, N. D., & Wagner, H. (1966). Absence of ferromagnetism or antiferromagnetism in one- or two-dimensional isotropic Heisenberg models. *Physical Review Letters* 17(22), 1133–1136.
16. Kosterlitz, J. M., & Thouless, D. J. (1973). Ordering, metastability and phase transitions in two-dimensional systems. *Journal of Physics C* 6(7), 1181–1203.
17. Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). Theory of superconductivity. *Physical Review* 108(5), 1175–1204.
18. Wigner, E. P. (1960). The unreasonable effectiveness of mathematics in the natural sciences. *Communications on Pure and Applied Mathematics* 13(1), 1–14.
19. Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika* 1(3), 195–200.
20. Feynman, R. P. (1948). Space-time approach to non-relativistic quantum mechanics. *Reviews of Modern Physics* 20(2), 367–387.
21. Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D* 7(8), 2333–2346.
22. Deutsch, J. M. (1991). Quantum statistical mechanics in a closed system. *Physical Review A* 43(4), 2046–2049.
23. Srednicki, M. (1994). Chaos and quantum thermalization. *Physical Review E* 50(2), 888–901.
24. 't Hooft, G. (1993). Dimensional reduction in quantum gravity. arXiv:gr-qc/9310026.
25. Susskind, L. (1995). The world as a hologram. *Journal of Mathematical Physics* 36(11), 6377–6396.
26. Maldacena, J. (1998). The large $N$ limit of superconformal field theories and supergravity. *Advances in Theoretical and Mathematical Physics* 2(2), 231–252.
27. Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information.* Cambridge University Press.
28. Dragovich, B., Khrennikov, A., Kozyrev, S. V., & Volovich, I. V. (2009). On $p$-adic mathematical physics. *p-Adic Numbers, Ultrametric Analysis and Applications* 1(1), 1–17.
29. Bartolomei, H., et al. (2020). Fractional statistics in anyon collisions. *Science* 368(6487), 173–177.
30. Nakamura, J., Liang, S., Gardner, G. C., & Manfra, M. J. (2020). Direct observation of anyonic braiding statistics. *Nature Physics* 16, 931–936.

## Appendix A — Source Notes Index

The following Obsidian working notes are deposited verbatim with this record under `source-notes/` and constitute the primary source material for Parts II and III:

1. `_26228215046.md` — the detailed outline of the treatise (the basis of Part I).
2. `_26228215041.md` — research note on the quantum surface distinction and the thermodynamics of scale (the basis of Part II).
3. `_26228180242.md` — research note on copper-wire conduction and the load-bearing assumption catalogue (the basis of Part III).

Deposit provenance: see `PROJECT-PLAN.md`, `README.md`, and `artifacts/` for the full pipeline trail.
