---
title: 'A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation'
author: 'Rowan Brad Quni-Gudzinas'
date: '2026-08-16'
license: 'QNFO Unified License Agreement (QNFO-ULA)'
doi: '10.5281/zenodo.21971503'
status: 'published'
---

**Subtitle:** The Electron as a Hook — Full Edition (nine parts, fifty-one chapters)
**Author:** Rowan Brad Quni-Gudzinas · QNFO Research Foundation
**Contact:** rowan.quni@qnfo.org · **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**Version:** v0.2.2 · **Supersedes:** v0.1 (architecture + two research notes), v0.2 (Full Edition), v0.2.1 (prose correction)

## Abstract

The electron is the most precisely measured particle in physics and the workhorse of modern computation, yet the theoretical structure in which it lives rests on assumptions that are load-bearing but rarely interrogated: the complex Hilbert-space postulate, the spin-statistics theorem's premises, the Archimedean valuation of every measured quantity, the thermodynamic foundations of irreversible computation, and the identification of the electron itself as a fixed elementary object rather than a vacuum- and environment-dependent excitation. This Full Edition expands the v0.1 architecture into the treatise proper: nine parts and fifty-one chapters. Every assumption examined is subjected to a fixed six-step procedure — state the assumption in its strongest form; identify what is built on it; separate confirmed predictions from postulates; list alternatives that preserve the confirmed predictions while relaxing the assumption; define falsifiability conditions; record open questions. **Why a reader should care:** each assumption examined bears directly on a live frontier — energy-efficient computation, topological quantum computing, high-temperature superconductivity, precision metrology, and quantum gravity — and several are already known to fail as universal statements (anyons in $2+1$ dimensions, quasiparticle dressing, vacuum-dependent particle content, broken ergodicity). **Premise-depth disclosure:** the treatise introduces no new physical postulate; its unanalyzable primitives — ordinary set theory, the standard model of measurement practice, the requirement of empirical adequacy — are named rather than hidden, and its conclusions are as deep as the published physics they cite. The treatise does not reject any assumption by default and does not endorse any alternative; it maps domains of validity and promotes the assumptions themselves from articles of faith to objects of experiment.

**Keywords:** quantum foundations, spin-statistics theorem, quasiparticles, Landauer's principle, Ostrowski's theorem, Hilbert space, anyons, thermodynamics of computation, premise depth, falsifiability

---

## Preface

### Why the electron?

No object in physics carries more load than the electron. It carries the precision tests of quantum electrodynamics, the entire edifice of solid-state electronics, the thermodynamic limits of computation, and — through the spin-statistics theorem — the stability of matter itself. Precisely because the electron is everywhere, the assumptions supporting its description are load-bearing for physics as a whole. Pulling on the electron means pulling on Hilbert space, on unitarity, on the exclusion principle, on the real-number continuum, on the second law, and on the notion of "particle" itself.

### What this treatise is, and is not

This treatise is an assumption audit. For each load-bearing assumption it states the assumption, identifies what is built on it, distinguishes what is experimentally confirmed from what is postulated, catalogues alternatives, and defines conditions under which the assumption could be shown to fail. It is **not** a claim that current physics is wrong. It is **not** a claim that any alternative framework is correct. It is **not** philosophy dressed as physics. Every question raised is raised because it is either already experimentally visible (anyons, quasiparticles, vacuum-dependent particle content) or practically consequential (the energy cost of computation, the design space of quantum devices).

### The danger of treating frameworks as dogma

A framework that has never failed within its tested domain is a successful framework, not a complete one. The history of physics is a sequence of frameworks whose domains of validity were discovered to have edges: Newtonian mechanics, classical electrodynamics, and local hidden-variable theories all failed at their edges in measurable ways. The frameworks examined here — Hilbert-space quantum mechanics, exact Lorentz invariance, Archimedean valuation, ergodicity — each have proposed edges. Mapping those edges is not disloyalty; it is the ordinary scientific procedure by which domains of validity are established rather than assumed.

### How this treatise is organized

Part I establishes the electron as known and as probe. Parts II through VI audit the load-bearing assumptions in five domains: the Hilbert-space framework, spin and statistics, thermodynamics and computation, measurement and valuation, and vacuum-dependence with dimensionality and holography. Part VII audits fifteen cross-cutting assumptions, each with the full six-step treatment. Part VIII converts the audit into a research programme; Part IX consolidates every open question; Chapter 51 states what the treatise does and does not claim. Four appendices provide the mathematical, experimental, and bibliographic scaffolding.

## Acknowledgments

Self-funded, single-author work. The author thanks the open-science communities whose repositories made the live verification of every citation possible (Crossref, arXiv, Zenodo), and the anonymous adversarial reviewers whose criticisms shaped Part VII.

## Notation and Conventions

Four categories are used throughout, and no statement may slide between them unannounced:

1. **Postulate** — an assumption adopted as the starting point of a framework.
2. **Theorem** — a statement derived within a framework from its postulates.
3. **Empirical fact** — a measurement result with an experimental uncertainty.
4. **Open question** — a proposition for which no framework yet commands the evidence.

Units: measured quantities are given in SI where that is the instrument's native output, with the dimensionless equivalent stated whenever a physical law is discussed (the Ostrowski dimensionlessness mandate): $\hbar = c = k_B = 1$ conversions are shown inline. Mathematics uses $(\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{Q}_p, \mathbb{A}_{\mathbb{Q}})$ with the standard meanings. "Confidence" is calibrated language, never a number unless a number is given by experiment.

---

## Introduction

### 0.1 Motivation

The electron is the most precisely measured particle in physics: its charge is exact in the modern SI, its mass is known to eleven significant figures, and its magnetic moment tests quantum electrodynamics to parts per trillion. It is simultaneously the basis of modern electronics and computation. The very success of the electron conceals the assumptions on which its description rests — and foundational questions about the electron are not separate from practical technology; they are the design constraints of the next generation of devices.

### 0.2 The Central Claim

The electron is a point of convergence — and a point of potential failure — for many deep assumptions of physics. Examining those assumptions is scientifically necessary, not merely philosophical. The goal is not to reject current physics but to map the domains of validity of its load-bearing postulates.

### 0.3 Methodology

For every assumption examined, the treatise applies a fixed six-step procedure:

1. **State the assumption explicitly**, in its strongest, most standard form.
2. **Identify what is built on it** — theories, technologies, and theorems that depend on the assumption.
3. **Distinguish confirmed predictions from postulates** — what is measured, what is derived, what is assumed.
4. **List alternative formulations** that preserve the confirmed predictions while relaxing the assumption.
5. **Define falsifiability conditions** — experiments or theorems that would discriminate the assumption from its alternatives.
6. **Record open questions** in the consolidated register (Part IX).

Only scientific criteria are used: predictive power, empirical adequacy, internal consistency, and domain of validity. No assumption is rejected by default; no assumption is retained by tradition.

### 0.4 Structure of the Treatise

Nine parts, fifty-one chapters, four appendices. Every part closes on its own open questions; Part IX consolidates them; Chapter 51 states the bounds of the claims.

---

## Part I — The Electron as Known and as Probe

### Chapter 1 — The Standard Model Electron

#### 1.1 Definition and quantum numbers

The Standard Model electron is a spin-$1/2$ Dirac field $\psi$ with electric charge $-e$, lepton number $+1$, and mass $m_e = 510.99895000(15)\ \mathrm{keV}$, coupled to the photon and weak gauge fields. Its kinetic term is

$$\mathcal{L}_e = \bar\psi (i\gamma^\mu D_\mu - m_e)\psi,$$

with $D_\mu = \partial_\mu + i e A_\mu + \ldots$ the gauge-covariant derivative. Everything distinctive about the electron — the exclusion principle, antimatter, the magnetic moment — follows from this single field together with the framework's quantization rules.

#### 1.2 Measured properties

- **Charge.** Millikan's oil-drop experiment established charge quantization; the modern SI fixes $e = 1.602176634\times10^{-19}\ \mathrm{C}$ exactly. The electron charge equals the proton charge in magnitude to better than one part in $10^{21}$ (neutrality bounds on atomic hydrogen).
- **Mass.** Penning-trap cyclotron-frequency comparisons give $m_e = 9.1093837015(28)\times10^{-31}\ \mathrm{kg}$.
- **Magnetic moment.** The anomaly $a_e = (g-2)/2 = 0.00115965218059(13)$; QED theory (ten loops) agrees to roughly one part in $10^{12}$ — the most stringent test of any quantum field theory. The muon analogue shows a persistent $\sim4\sigma$ tension, an open question of the same framework.
- **Electric dipole moment.** No signal; the bound $|d_e| < 4.1\times10^{-30}\ e\cdot\mathrm{cm}$ (ACME) is the tightest constraint on $T$-violation in a lepton.
- **Lifetime.** Stability lower bound $\tau > 6.6\times10^{28}\ \mathrm{yr}$ (Borexino); no compositeness down to $10^{-19}\ \mathrm{m}$.

#### 1.3 Status: what is confirmed

Confirmed: the field-theoretic description and the precision agreement for $a_e$; charge quantization; lepton-number conservation at the tested level; the absence of an EDM at the tested level. Postulated: the Dirac-field ontology itself, exact unitarity, the continuum valuation of these numbers, and the stability of the vacuum that defines the electron.

#### 1.4 The assumption audited: "the electron is a stable elementary Dirac fermion"

1. **The assumption.** The electron is a pointlike, structureless, stable spin-$1/2$ excitation of a unique Poincaré-invariant vacuum, described exactly by a single Dirac field.
2. **What is built on it.** All of QED precision physics; the electron mass and charge as universal constants; lepton universality in the electroweak sector; atomic and molecular theory.
3. **Confirmed vs postulated.** Confirmed: the predictions computed from the Dirac field (spectrum, $g-2$, EDM bounds). Postulated: pointlikeness below the tested scale, absolute stability, uniqueness of the vacuum, and the identification of the field with "the particle."
4. **Alternatives.** Composite-electron models (preon theories) that reproduce the Dirac phenomenology at low energy; electrons as emergent excitations of a more fundamental medium; environment-dependent "electrons" (Chapter 2).
5. **Falsifiability.** A nonzero EDM beyond the Standard Model prediction, an observed decay, or a measured substructure would each falsify the assumption at a known sensitivity; a demonstrated environment-dependence of the *free-space* electron mass would falsify universality.
6. **Open questions.** See Chapter 3.

### Chapter 2 — The Electron as a Renormalized Excitation

#### 2.1 Bare vs dressed electron

In QED the parameters of the Dirac field are bare quantities; the measured mass and charge are renormalized. The running coupling $\alpha(Q^2)$ grows from $\alpha \approx 1/137.036$ at low energy to $\alpha(M_Z^2) \approx 1/127.9$. The "electron" of experiments is the dressed excitation: bare field plus its self-energy cloud.

#### 2.2 The electron in a material

In a solid the excitation is a quasiparticle: its effective mass differs from $m_e$ (e.g., $m^* \approx 1.3\,m_e$ in copper at the Fermi surface), it acquires a finite lifetime from scattering, its dispersion is set by the lattice, and it is dressed by phonons, magnons, and other electrons. The bare parameters are renormalized again by the material environment.

#### 2.3 The electron as a collective pattern

Landau's Fermi-liquid theory organizes the quasiparticle picture for weakly interacting metals; its breakdown (cuprates, strange metals with Planckian dissipation, heavy-fermion quantum critical points) shows that even the *quasiparticle* is not guaranteed. The fractional quantum Hall effect goes further: the elementary excitations carry charge $e/3$, $e/5$ — the "electron" of that ground state is not the electron at all.

#### 2.4 The assumption audited: "particle identity is scale- and environment-independent"

1. **The assumption.** What is called "the electron" is one fixed object; dressing and renormalization are cosmetic changes to the same entity.
2. **What is built on it.** The particle-data-group ontology; the language of particle physics ("the electron mass"); the transfer of vacuum physics to condensed matter.
3. **Confirmed vs postulated.** Confirmed: the free-space electron's properties are stable and universal. Postulated: that this stability is identity rather than emergent robustness, and that the label survives across vacua.
4. **Alternatives.** Particles as emergent patterns of a many-body state (the view this treatise adopts as a *language*); the quasiparticle as the more honest general concept, with the free electron as a special case.
5. **Falsifiability.** A measured dependence of the free-space electron's properties on environment or history; a demonstrated failure of the renormalization-group expectation that low-energy physics is fixed by symmetry and a few parameters.
6. **Open questions.** Q3.1–Q3.5 (Chapter 3).

### Chapter 3 — Open Questions about the Electron Itself

- **Q3.1** Is charge quantization exact and derivable (e.g., from anomaly cancellation or topology), or is it an independent input?
- **Q3.2** Is the electron absolutely stable, and what would a nonzero decay rate mean for lepton number?
- **Q3.3** Is the electron elementary or composite below $10^{-19}\ \mathrm{m}$?
- **Q3.4** What fixes the electron mass — is it a vacuum expectation value, a landscape accident, or something else?
- **Q3.5** Can a finite region of a finite-dimensional Hilbert space describe the electron without conflict (Chapter 6.5)?

---

## Part II — Hilbert Space Dogma and Its Alternatives

### Chapter 4 — The von Neumann Postulate

#### 4.1 Statement of the postulate

A quantum system is described by a ray in a complex Hilbert space $\mathcal{H}$; observables are self-adjoint operators on $\mathcal{H}$; composite systems live in the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$; time evolution is unitary, $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$; and measurement outcomes obey the Born rule, $P(a) = \langle\psi| \Pi_a |\psi\rangle$ for a projector $\Pi_a$.

#### 4.2 Historical origin

von Neumann's *Mathematische Grundlagen der Quantenmechanik* (1932) axiomatized the matrix mechanics of Heisenberg, Born, and Jordan and the wave mechanics of Schrödinger into one structure. The axiomatization succeeded because it unified the two formalisms, accommodated continuous and discrete spectra, and gave quantum logic a home. It became "standard" by adoption, not by uniqueness: Dirac's formalism predates it and the algebraic formulations postdate it.

#### 4.3 What is built on it

All of nonrelativistic quantum mechanics, quantum field theory, quantum information, quantum computing, quantum measurement theory, and the mathematical core of most quantum-gravity programmes. The edifice is vast; the foundation is six assumptions examined next.

### Chapter 5 — Hidden Assumptions Inside the Hilbert-Space Framework

#### 5.1 Complex linear superposition

1. **The assumption.** Amplitudes are complex numbers and state space is closed under $\mathbb{C}$-linear combination; relative complex phases are physical.
2. **What is built on it.** Interference theory, the band theory of solids, quantum information protocols that exploit complex phases (e.g., certain oracle separations), the standard form of the path integral.
3. **Confirmed vs postulated.** Confirmed: two-slit interference, diffraction, the success of complex amplitudes in every precision calculation. Postulated: that the field of amplitudes is exactly $\mathbb{C}$ — $\mathbb{R}$ and $\mathbb{H}$ would produce different interference.
4. **Alternatives.** Real quantum mechanics (Stueckelberg; an additional observable must commute with everything to reproduce predictions); quaternionic quantum mechanics (Finkelstein, Jauch, Adler — locally equivalent in scattering but differing in multiparticle interference).
5. **Falsifiability.** Multipath interference experiments (three or more slits with tunable phases) are sensitive to the number field; any violation of the complex-amplitude sum rules for triple interference would discriminate the fields.
6. **Open questions.** Q7.1 (Chapter 7).

#### 5.2 Exact unitarity

1. **The assumption.** Time evolution is exactly unitary on a closed system; probability is exactly conserved.
2. **What is built on it.** The consistency of the Born rule, conservation laws via Noether symmetry, the unitarity bounds of scattering theory, the current (information-preserving) understanding of black-hole evaporation.
3. **Confirmed vs postulated.** Confirmed: unitarity of effective evolution at tested precision; decay-law consistency. Postulated: exactness at all scales, including horizons and the entire universe.
4. **Alternatives.** Open-system (GKSL/Lindblad) dynamics as fundamental with unitarity emergent; objective-collapse models (Ghirardi-Rimini-Weber, continuous spontaneous localization); non-unitary horizon dynamics.
5. **Falsifiability.** Collapse-model bounds on spontaneous localization; information-loss signatures in black-hole mergers; precision tests of probability conservation.
6. **Open questions.** Q7.2; Chapter 34 gives the full treatment.

#### 5.3 Tensor-product factorization

1. **The assumption.** The state space of a composite system factorizes: $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$.
2. **What is built on it.** Entanglement theory, quantum error correction, the subsystem structure of statistical mechanics, decoherence theory.
3. **Confirmed vs postulated.** Confirmed: factorization in every experimentally accessible composite (particles, modes, lattice sites). Postulated: exact factorization in regimes where the "subsystems" are not operationally separable (interior of a black hole, early universe, gauge-invariant subsystems).
4. **Alternatives.** Algebraic QFT with local algebras instead of global tensor products; crossed-product constructions where subsystem algebras are emergent.
5. **Falsifiability.** Any operational setting in which predicted entanglement measures disagree with observation; type-III von Neumann algebra signatures in gravitational systems (an active research programme).
6. **Open questions.** Q7.3.

#### 5.4 Infinite-dimensional state spaces

1. **The assumption.** Physical state spaces are infinite-dimensional (position, momentum, field configurations).
2. **What is built on it.** The continuum spectral theory of self-adjoint operators; renormalization theory; the standard treatment of scattering.
3. **Confirmed vs postulated.** Confirmed: no finite-dimensional truncation has failed an experiment. Postulated: that the infinite-dimensional idealization is physical rather than a limit of finite descriptions.
4. **Alternatives.** Finite-dimensional quantum mechanics per causal diamond (bounded by entropy $\sim A/4$); continuous-variable systems treated as limits of finite qubit lattices.
5. **Falsifiability.** A causally-bounded region whose physically accessible Hilbert-space dimension provably exceeds the covariant entropy bound would be decisive; so would any operational deviation of continuum limits.
6. **Open questions.** Q7.4.

#### 5.5 Every observable is a self-adjoint operator

1. **The assumption.** All measurable quantities correspond one-to-one with self-adjoint operators (equivalently, projection-valued measures).
2. **What is built on it.** The spectral theorem's central role; the textbook formulation of measurement; quantum statistics.
3. **Confirmed vs postulated.** Confirmed: the PVM model covers every tested observable. Postulated: that no generalized measurement (POVM) or no operator-free quantity is fundamental.
4. **Alternatives.** Positive operator-valued measures as the primitive (necessary already for non-ideal measurements); algebraic formulations where observables are elements of a $C^*$-algebra; operational formulations without Hilbert space (Chapter 6.4).
5. **Falsifiability.** An observable whose statistics provably require a POVM with no PVM dilation in the accessible Hilbert space — effectively a test of whether ideal measurements are always accessible.
6. **Open questions.** Q7.5.

#### 5.6 Real and Archimedean probability

1. **The assumption.** Probabilities are real numbers in $[0,1]$ obeying Kolmogorov's axioms, including countable additivity on an Archimedean ordered field.
2. **What is built on it.** The Born rule's interpretation, statistical mechanics, decision-theoretic derivations of quantum probability.
3. **Confirmed vs postulated.** Confirmed: every frequency test ever performed is consistent with real-valued additive probability. Postulated: that the valuation field of probability is exactly $\mathbb{R}$ (Part V treats this in depth — Chapters 19–22).
4. **Alternatives.** Non-Kolmogorov (quantum-logic) probability; $p$-adic probability for hierarchically structured outcome spaces.
5. **Falsifiability.** A designed experiment whose outcome statistics violate additivity in a way quantum theory predicts but Kolmogorov cannot represent — already essentially true for interference, which is precisely why amplitudes (not probabilities) add.
6. **Open questions.** Q23.1–Q23.6 (Chapter 23).

### Chapter 6 — Alternatives to Hilbert Space

#### 6.1 Real quantum mechanics
Same structure with $\mathbb{R}$-linearity; requires an extra superselected observable (Stueckelberg's antiunitary operator) to match complex predictions — testable in multipath interference.

#### 6.2 Quaternionic quantum mechanics
$\mathbb{H}$-linear state spaces; local scattering predictions identical to complex QM in most regimes, but multiparticle interference and some bound-state spectra can differ — the tightest known constraint comes from triple-slit-class experiments.

#### 6.3 Algebraic quantum theory
Observables as a $C^*$-algebra; states as positive functionals. Reproduces quantum mechanics on finite systems and generalizes to quantum fields where Hilbert-space constructions are ill-defined (Haag's theorem).

#### 6.4 Generalized probabilistic theories
Operational frameworks (preparations, transformations, measurements) with no imposed Hilbert space. Quantum theory is one point in the GPT polytope; "which GPT is Nature" is itself an experimental question.

#### 6.5 Finite-dimensional Hilbert spaces
Quantum mechanics per finite causal region; motivated by entropy bounds. Reproduces all tested predictions as limits; differs in principle at the largest scales.

#### 6.6 Path-integral formulation without explicit Hilbert space
Feynman's sum-over-histories can be formulated without ever naming a Hilbert space — the state space emerges from the measure. The question "which is fundamental" is open and likely undecidable by observation alone (Chapter 35).

### Chapter 7 — Falsifiability and Open Questions

- **Q7.1** Can real, complex, and quaternionic quantum mechanics be distinguished experimentally, and at what significance has that been attempted?
- **Q7.2** Does unitarity break at horizons, at collapse, or nowhere?
- **Q7.3** Does quantum gravity force abandonment of tensor-product factorization?
- **Q7.4** Does finite-dimensional Hilbert space for a causal diamond conflict with observation?
- **Q7.5** Is every physical observable a PVM; or are POVMs fundamental?
- **Q7.6** Can the Born rule be derived without assuming Hilbert-space geometry (Gleason-style theorems and their limits)?

---

## Part III — Spin, Statistics, and the Pauli Exclusion Principle

### Chapter 8 — What Spin Is Mathematically

#### 8.1 Spin as a label for Poincaré representations

Wigner's classification (1939) identifies elementary quantum systems with irreducible unitary representations of the Poincaré group, labeled by mass and spin. Spin is a *label of a representation*, not a property of a little ball: spin-$j$ describes how states transform under rotations — phases under $2\pi$ rotation, $e^{-2\pi i s}$ for spin-$s$. The theorem part is exact; the interpretive part (what is "spinning") is the assumption.

#### 8.2 Spin-$1/2$ and $SU(2)$

The double cover $SU(2) \to SO(3)$ is forced by projective representations: the electron carries the defining representation of $SU(2)$, acquiring a phase $-1$ under a $2\pi$ rotation. That this phase is physically real is confirmed by neutron interferometry (the $4\pi$ symmetry experiments of Rauch, Werner, and later precision work).

#### 8.3 Spin is not literal rotation

The classical image of a spinning charged sphere fails quantitatively (surface velocity would exceed $c$ for the observed magnetic moment) and structurally (spin is intrinsic, pointlike, and quantized). Spin is the transformation law, nothing more; every classical intuition about it is a map, not the territory.

### Chapter 9 — The Spin-Statistics Theorem

#### 9.1 Statement

In a relativistic quantum field theory in $3+1$ spacetime dimensions with Lorentz invariance, microcausality, positive energy, and positive norm, integer-spin particles quantize as bosons (symmetric states, commutators) and half-integer-spin particles as fermions (antisymmetric states, anticommutators). First derived by Fierz and Pauli (1939–40); modern proofs (e.g., via the Euclidean rotation argument) make the assumptions explicit.

#### 9.2 Assumptions of the theorem

1. Lorentz (Poincaré) invariance; 2. microcausality — spacelike-separated fields (anti)commute; 3. positive energy (spectrum condition); 4. positive-norm Hilbert space (no ghosts); 5. exactly $3+1$ dimensions. The premises are audited where each is load-bearing: Lorentz invariance in Chapter 40 and microcausality in Chapter 32 (Part VII); positive energy and positive norm in §9.5 and §9.6 below; the $3+1$-dimensional premise in §9.7 (with Chapter 26). Here they are premises of a theorem, not of the universe.

#### 9.3 Consequences

The Pauli exclusion principle — no two identical fermions share a quantum state — and with it: atomic shell structure, the periodic table, the incompressibility of matter, the Fermi statistics of conduction electrons (Part IV), degeneracy pressure in white dwarfs and neutron stars. The stability of matter (Dyson–Lenard, Lieb–Thirring) rests on it.

#### 9.4 The assumption audited: "the spin-statistics connection is a law of nature"

1. **The assumption.** The fermion/boson dichotomy follows necessarily from first principles and holds everywhere.
2. **What is built on it.** All of atomic and condensed-matter physics; the particle-taxonomy of the Standard Model; chemistry.
3. **Confirmed vs postulated.** Confirmed: the theorem *given its premises*, and the phenomenology in every $3+1$D Poincaré-invariant setting tested. Postulated: the premises themselves (exact Lorentz invariance, microcausality, positive norm, $3+1$ dimensions).
4. **Alternatives.** Anyonic statistics where the premises fail (Chapter 10); parastatistics (which the algebraic framework allows but nature, in $3+1$D, appears not to use); emergent-statistics programmes in which exchange phases are derived from deeper structures.
5. **Falsifiability.** Anyons are already observed in effective $2+1$D systems — the theorem's *domain* is thereby shown to have an edge. Falsifying the premises in $3+1$D (Lorentz violation at Planck scales, microcausality violation) would falsify the theorem's conclusions in that domain.
6. **Open questions.** Chapter 12.

#### 9.5 Positive energy (spectrum condition)

1. **The assumption.** The energy spectrum is bounded below and the vacuum is the state of lowest energy.
2. **What is built on it.** The stability of matter and of the vacuum; the theorem's analytic-continuation argument; dispersion relations; the thermal interpretation of Euclidean field theory.
3. **Confirmed vs postulated.** Confirmed: no system has ever exhibited an unbounded-below spectrum; vacuum stability is empirical to the extent of every precision test. Postulated: exactness of the spectrum condition in the deep ultraviolet and in quantum gravity, where energy is frame-dependent and horizons complicate the notion.
4. **Alternatives.** Ghost-free constructions that avoid the spectrum condition by design; horizon thermodynamics where the operative positivity is that of entropy rather than energy; non-perturbative formulations where the Hamiltonian is secondary.
5. **Falsifiability.** A physical system with a demonstrably unbounded-below spectrum (a runaway ground state) would falsify the assumption as universal; in quantum gravity the discriminator is whether horizon-entropy bounds replace the spectrum condition.
6. **Open questions.** Q12.4 (the theorem's premises); is the spectrum condition derivable from unitarity and causality alone?

#### 9.6 Positive-norm Hilbert space (no ghosts)

1. **The assumption.** The state space carries a positive-definite inner product; no negative-norm ("ghost") state is physical.
2. **What is built on it.** The probability interpretation of the Born rule; unitarity's self-consistency; the spin-statistics theorem's proof.
3. **Confirmed vs postulated.** Confirmed: no ghost state has ever been detected; gauge theories are consistently quantized with ghosts confined to intermediate lines (Faddeev–Popov, Kugo–Ojima). Postulated: positivity of the physical subspace at all scales.
4. **Alternatives.** Indefinite-metric (Krein-space) formulations with a physical subspace selected by subsidiary conditions — already standard for gauge fields; formulations where positivity is emergent in the infrared.
5. **Falsifiability.** A measurable ghost-mediated signature beyond the gauge-artifact level; a demonstration that no physical subspace can be consistently selected in some regime.
6. **Open questions.** Is the physical-subspace construction always available? Does quantum gravity require relaxing positivity (several approaches do)?

#### 9.7 Exactly $3+1$ dimensions as a premise

1. **The assumption.** Spacetime has exactly $3+1$ dimensions — the case in which the spin-statistics theorem holds.
2. **What is built on it.** The theorem itself; the dichotomy of statistics; the stability of atomic matter in our universe.
3. **Confirmed vs postulated.** Confirmed: all observations are consistent with $3+1$ macroscopic dimensions (compact extra dimensions, if any, are unobserved). Postulated: that no regime — early universe, Planck scale, holographic duals — is effectively lower-dimensional in a way that changes statistics.
4. **Alternatives.** $2+1$-dimensional physics as realized in engineered systems (Chapter 10); holographic descriptions where the boundary dimension is the operative one; compactification scenarios.
5. **Falsifiability.** Observational evidence of macroscopic non-$3+1$ dimensionality; more sharply, the engineered systems of Chapter 10 have already shown the premise is *not necessary* — anyons exist where it fails.
6. **Open questions.** Q12.1, Q12.2; does holography make the effective dimension of statistics environment-dependent (Chapter 27)?

### Chapter 10 — Where the Theorem Fails

#### 10.1 $2+1$ dimensions and anyons

In $2+1$ dimensions the exchange of two identical particles is described by the braid group, not the permutation group. Braiding twice need not return the system to its original state; the exchange phase $e^{i\theta}$ is unconstrained. Particles with $\theta \neq 0, \pi$ are anyons. The theorem does not apply because its premises fail — the spatial dimension is wrong.

#### 10.2 The fractional quantum Hall effect

At filling factor $\nu = 1/3$ in a two-dimensional electron gas under strong magnetic field, transport shows an exactly quantized plateau at $\sigma_{xy} = \frac{1}{3} e^2/h$ (Tsui, Stormer, Gossard, 1982; Laughlin's theory, 1983). The quasiparticles carry charge $e/3$ (measured by shot noise) and fractional exchange statistics.

#### 10.3 Braid group vs permutation group

The permutation group $S_N$ has only two one-dimensional representations (bosons/fermions); the braid group $B_N$ has a continuous family. The topology of configuration space — which pairs of histories are homotopic — differs between $d \ge 3$ and $d = 2$, and this topological fact is what the statistics theorem ultimately counts on.

#### 10.4 Experimental evidence for anyons

Direct braiding signatures in anyon colliders (Bartolomei et al., 2020, Science) and interferometry (Nakamura et al., 2020, Nature Physics) support fractional statistics at the few-percent-to-strong significance level. The evidence is now widely regarded as decisive for $\nu = 1/3$ quasiparticles, and the hunt for *non-abelian* anyons (Ising, Fibonacci) — the platform for topological quantum computing — is ongoing.

### Chapter 11 — Statistics as Emergent, Not Intrinsic

#### 11.1 Quasiparticle statistics in condensed matter

The "particles" of a quantum Hall sample are not electrons: they are quasiparticles of the ground state, and their statistics is a property of the many-body wavefunction and the dimensionality — not of any intrinsic label. Statistics is a property of the *state*, not of the particle.

#### 11.2 The electron as a quasiparticle in different ground states

The same underlying electron liquid supports different emergent particles in different ground states: Landau quasiparticles in metals, Cooper pairs in superconductors (bosonic composites), $e/3$ quasiparticles at $\nu=1/3$. "The electron" is a name with a domain of validity, not a universal object.

#### 11.3 Implications for "elementary"

If the fermion/boson dichotomy is the $3+1$D Poincaré-vacuum special case of a more general braided/statistical structure, then "elementary particle" is itself a vacuum-relative concept. Part VI (Chapter 25) develops this into the vacuum-dependence of particle content.

### Chapter 12 — Open Questions

- **Q12.1** Why is there no observed parastatistics in $3+1$ dimensions when the algebraic framework permits it?
- **Q12.2** Are anyons only effective, or can they be elementary in $2+1$D?
- **Q12.3** Can spin emerge from a more primitive degree of freedom (preons, string modes, topological order)?
- **Q12.4** Does spin-statistics survive in nonlocal or Lorentz-violating theories, and how much Lorentz violation is excluded by the *absence* of anyonic signatures in $3+1$D?
- **Q12.5** How do anyonic quasiparticles alter the definition of particle identity — and what does that mean for quantum statistics as a primitive?
- **Q12.6** Can non-abelian anyons be demonstrated at the level required for topological quantum computation?

---

## Part IV — The Electron in Thermodynamics and Computation

### Chapter 13 — Physical Basis of Modern Computation

#### 13.1 The transistor and electron control

Modern computation is electron control. The field-effect transistor is a gate that changes the electron density of a channel by electrostatic action; a bit is a charge configuration, and logic is the orchestrated motion of electron ensembles. Everything in Part IV follows from asking what thermodynamics has to say about that motion.

#### 13.2 Band theory and Fermi-Dirac statistics

Band structure — the energy bands and gaps that make a semiconductor — is a consequence of electrons in a periodic potential obeying Fermi-Dirac statistics (Part III). Doping moves the Fermi level into the bands; the thermal occupation of states at the Fermi edge is set by the dimensionless ratio $k_B T / E_F$ — at room temperature, a part-per-thousand-scale window of thermal smearing that nonetheless sets transistor leakage.

#### 13.3 Semiconductors and CMOS

CMOS logic uses complementary n- and p-channel transistors so that static power is minimized: current flows only during switching. The dynamic energy per switch scales as $C V^2$; the limits are therefore (a) the minimum capacitance and voltage compatible with reliable state distinction, and (b) the thermal noise floor that determines the minimum distinguishable charge — the thermodynamic limits of Chapter 14.

### Chapter 14 — Thermodynamic Limits of Computation

#### 14.1 Landauer's principle

Logical irreversibility has a physical price: erasing one bit of information in a heat bath at temperature $T$ costs at least $k_B T \ln 2$ of dissipated heat (Landauer, 1961). The principle is a theorem of statistical mechanics *given* the identification of logical states with physical macrostates; that identification is the assumption to audit.

#### 14.2 Shannon information vs physical implementation

Shannon information is abstract — a distribution over messages. Landauer's bound attaches only when a logical state is *physically implemented* in a configurational degree of freedom whose erasure compresses phase-space volume. Abstract information is free; implemented information is thermodynamic. The gap between the two is where the engineering happens.

#### 14.3 Measured dissipation vs the Landauer bound

Real devices dissipate orders of magnitude above $k_B T \ln 2$ (≈ $3\times10^{-21}$ J at 300 K) — CMOS switches at roughly $10^{-17}$ to $10^{-14}$ J, thousands to millions of times the bound. Experimental demonstrations of Landauer-erasure (Bérut et al. 2012) verified the bound's validity in single-particle systems, not its attainability in logic.

#### 14.4 Reversible computing

Bennett (1973) showed logical reversibility suffices: any computation can in principle be done with arbitrarily small dissipation. The programme (adiabatic CMOS, reversible logic families) is technically real but commercially marginal — the thermodynamic insight is sound; the practical questions are latency, error rates, and clocking overhead.

#### 14.5 The assumption audited: "the thermodynamic limit of computation is $k_B T \ln 2$ per erased bit"

1. **The assumption.** Landauer's bound is the fundamental floor of irreversible computation in all physical settings.
2. **What is built on it.** The entire field of thermodynamic computing limits; chip power budgets; reversible-computing roadmaps.
3. **Confirmed vs postulated.** Confirmed: the bound in ideal, classical, heat-bath-coupled erasure (experimentally verified). Postulated: that the bound applies unchanged under quantum coherence, at strong coupling, in non-ergodic reservoirs, and at cryogenic temperatures where quantum fluctuations dominate.
4. **Alternatives.** Strong-coupling corrections (the bound becomes a bound on *total* entropy production including system-bath correlations); quantum-coherent erasure where information is moved rather than destroyed; measurement-feedback erasure with demon-like protocols.
5. **Falsifiability.** A device that reliably erases a bit with *total* entropy production below $k_B \ln 2$ in a well-characterized bath would falsify the naive bound (while leaving the generalized bound intact); conversely, a demonstration that no protocol can even approach the bound under coherence would falsify the quantum-extension optimism.
6. **Open questions.** Q17.1, Q17.5.

### Chapter 15 — Nonequilibrium Thermodynamics of Electrons

#### 15.1 Equilibrium statistical mechanics

The equilibrium theory of electrons — Fermi-Dirac distributions, Sommerfeld expansion, the specific heat $c_V \sim T$ of metals — is among the best-verified theories in physics. Its foundation is the identification of time averages with ensemble averages: ergodicity (Chapter 37).

#### 15.2 Fluctuation theorems

Jarzynski, Crooks, and their successors replaced the *second law as inequality* with *equalities over ensembles of nonequilibrium trajectories*: $\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}$. Verified in single-molecule pulling, colloidal traps, and electronic devices. These theorems require no ergodicity assumption — they hold trajectory-by-trajectory — which is precisely what makes them foundational tests of the *weaker* premises thermodynamics actually needs.

#### 15.3 Quantum thermodynamics

For quantum systems, work, heat, and entropy production are defined through measurement and feedback; quantum engines, refrigerators, and information-powered devices (Maxwell demons with quantum memory) have been demonstrated. The open frontier is coherence as a *resource* — can quantum coherence beat classical thermal machines?

#### 15.4 Many-body localization and ergodicity breaking

Many-body localized (MBL) systems fail to thermalize: local observables remember initial conditions forever (in idealized models), entanglement grows logarithmically, and eigenstate thermalization fails. Ergodicity is therefore *false in general*; it holds in a regime, not universally (Chapter 37).

#### 15.5 Strongly correlated electron systems

Strange metals, cuprates, heavy fermions: systems where quasiparticle language fails and where the "electron" (Chapter 2) is replaced by collective physics. Their thermodynamics (linear-in-$T$ resistivity, Planckian scattering $\hbar/k_B T$) may be teaching the framework itself what its limits are.

### Chapter 16 — Electron-Based Quantum Computation

#### 16.1 Spin qubits

Electron spin in gate-defined quantum dots: single- and two-qubit fidelities above 99.9%; the leading silicon-based route. The qubit is an electron spin; the platform is all of Part III's physics made operational.

#### 16.2 Superconducting qubits

Transmon and fluxonium qubits are circuits of supercurrents — billions of electrons moving as one collective (bosonic) degree of freedom. Fidelities are the highest demonstrated (two-qubit gates > 99.9%); coherence limits are set by dielectric loss and quasiparticle poisoning — the *unpaired* electrons that thermodynamics will not fully eliminate.

#### 16.3 Topological qubits from electron systems

Non-abelian anyons (Chapter 10.4) would encode quantum information in braiding operations that depend only on topology — errors would be exponentially suppressed by design rather than by correction. The physics is real (FQHE, Majorana candidate platforms); the demonstration of topological protection is the field's central open problem.

#### 16.4 Thermodynamic overhead of quantum computation

Error correction is refrigeration of information: syndrome extraction and feedback export entropy, and the overhead scales with code distance. The thermodynamic cost of *useful* quantum computation — including control electronics at cryogenic temperatures — is a live engineering and physics question (Q17.2).

### Chapter 17 — Open Questions

- **Q17.1** What is the true minimum energy cost of an irreversible electron device — is $k_B T \ln 2$ attainable, and under what coherence conditions?
- **Q17.2** What is the ultimate heat-dissipation limit in a quantum many-electron system performing error correction?
- **Q17.3** Can reversible computing reach the Landauer limit in practice, and at what latency cost?
- **Q17.4** How do quantum correlations affect entropy production — can entanglement assist or must it hinder?
- **Q17.5** Can spin-based logic be more energy-efficient than charge-based logic, given that the thermal scale $k_B T$ sets the resolution of both?
- **Q17.6** Can nonequilibrium fluctuation theorems be extended to strongly correlated electrons and MBL systems?
- **Q17.7** Is the Church–Turing thesis empirically valid for all physical computation (Chapter 30)?

---

## Part V — Measurement Theory and Valuation Structure

### Chapter 18 — How Electron Observables Are Measured

#### 18.1 Interaction with classical instruments

Every number in Chapter 1 was produced by a classical instrument — a trap electrode, a laser interferometer, a counter — whose output is a *length, time, or frequency*, ultimately a count of ticks compared to a reference oscillator. Measurement is comparison; the comparison is performed with classical macroscopic apparatus; the reported value is a real number because the apparatus reports real numbers.

#### 18.2 Finite precision of real measurement

No measurement yields an exact real. Every reported value is a rational interval: $a_e = 0.00115965218059(13)$ means "the anomaly lies in a rational interval of width $1.3\times10^{-13}$." The real numbers enter as the *idealization of the limit* of shrinking intervals — a completion, not an observation.

#### 18.3 Real numbers as idealization

The Archimedean real line $\mathbb{R}$ is the unique complete Archimedean ordered field, the completion of $\mathbb{Q}$ under the usual absolute value. Its use in physics is a choice — extremely successful, but a choice — and the next chapter states the theorem that makes this precise.

### Chapter 19 — Ostrowski's Theorem and the Choice of Valuation

#### 19.1 Statement of Ostrowski's theorem

Every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the usual Archimedean absolute value $|\cdot|_\infty$ or to a $p$-adic absolute value $|\cdot|_p$ for exactly one prime $p$ (Ostrowski, 1918). There is one Archimedean completion — $\mathbb{R}$ — and one non-Archimedean completion per prime — $\mathbb{Q}_p$. Together with the adeles $\mathbb{A}_{\mathbb{Q}}$ they exhaust the metric possibilities for the rationals.

#### 19.2 Archimedean vs $p$-adic absolute values

The Archimedean norm measures *size*: many small steps accumulate, $|x+y| \le |x|+|y|$. The $p$-adic norm measures *divisibility by $p$*: $|x+y|_p \le \max(|x|_p, |y|_p)$, the ultrametric inequality. In an ultrametric world, "close" means "congruent modulo high powers of $p$" — a hierarchical, tree-like notion of nearness in which all triangles are isosceles and small differences never accumulate.

#### 19.3 The adelic approach

The adele ring $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$ keeps all completions simultaneously, with the Archimedean place and every prime place on equal footing. Modern number theory (class field theory, the Langlands programme) is formulated adelically; a physical theory that treated all places as measurement-accessible would be the adelic analogue of standard physics.

#### 19.4 Mathematics does not select $\mathbb{R}$

The theorem's lesson for physics: nothing in the rational structure of counts and ratios — the home of frequency, channel counts, and winding numbers (Research Note A, v0.1 record doi:10.5281/zenodo.21970454) — selects the Archimedean completion. Physics selects it operationally (Chapter 20); mathematics merely enumerates the options.

### Chapter 20 — Why Physics Currently Selects Archimedean Structure

#### 20.1 Empirical success of real-valued measurement

Lengths, times, and frequencies combine additively in every experiment: interferometers add phases along continuous paths; clocks accumulate ticks without hierarchy. The Archimedean triangle inequality is the geometry of accumulated small differences — and accumulated small differences are what every laboratory instrument exploits.

#### 20.2 Additivity and ordering

The real line carries a total order compatible with addition: energies can be added, compared, and bisected. Thermodynamics — temperature as an intensive variable, entropy as an extensive one — is written in the language of ordered additive quantities. The Archimedean place is the one where *addition* and *order* coexist.

#### 20.3 Quantum mechanics and real probabilities

Born-rule probabilities are real numbers in $[0,1]$; expectation values of observables are real; the spectral theorem delivers real spectra for self-adjoint operators. The framework of Part II is itself Archimedean through and through — amplitudes may be complex, but the *valuations* they produce are real.

### Chapter 21 — Hidden Assumptions in Measurement Theory

#### 21.1 Physical observables form an Archimedean ordered field

1. **The assumption.** The values of physical quantities lie in $\mathbb{R}$ (an Archimedean ordered field), and "closeness" of values is magnitude-based.
2. **What is built on it.** Calculus, differential equations, Riemannian geometry, path integrals, probability theory — the mathematical form of every fundamental theory.
3. **Confirmed vs postulated.** Confirmed: real-valued modeling reproduces every precision measurement. Postulated: that no observable is natively ultrametric (divisibility-valued).
4. **Alternatives.** $p$-adic quantum mechanics (Vladimirov, Volovich; Dragovich, Khrennikov and successors); adelic formulations; finite-precision ("integer-scale") physics.
5. **Falsifiability.** A physical observable whose natural combination law is $\max$ rather than sum — a resonance or counting structure in which "near" means "congruent mod $p^n$" — demonstrated in a designed experiment would open the door to non-Archimedean description (Chapter 22.1).
6. **Open questions.** Q23.1–Q23.6.

#### 21.2 Spacetime is modeled on $\mathbb{R}^n$

1. **The assumption.** Spacetime is a real manifold — coordinates are real, topology is locally Euclidean.
2. **What is built on it.** General relativity, the Standard Model's spacetime structure, all of continuum physics.
3. **Confirmed vs postulated.** Confirmed down to the finest probed scales ($\sim 10^{-18}$ m). Postulated: continuity below the Planck scale.
4. **Alternatives.** Causal sets, noncommutative geometry, $p$-adic spacetime models, discrete Planck-scale structure (Chapter 42).
5. **Falsifiability.** Planck-scale dispersion in gamma-ray bursts or gravitational waves; causal-set signatures; noncommutative corrections.
6. **Open questions.** Q23.3, Q23.6; Chapter 42.

#### 21.3 Probabilities obey the Kolmogorov axioms

1. **The assumption.** Probabilities are $\sigma$-additive measures on an event algebra, with values in $[0,1] \subset \mathbb{R}$.
2. **What is built on it.** Classical statistics, stochastic processes, statistical mechanics' foundations.
3. **Confirmed vs postulated.** Confirmed for classical systems. Postulated: for quantum systems, where interference shows that *amplitudes* — not probability measures — compose.
4. **Alternatives.** Quantum logic (non-distributive event algebras), GPT state spaces, negative/quasi-probabilities (Wigner).
5. **Falsifiability.** Already falsified in the strict reading by interference — the surviving claim is only that *frequencies* obey Kolmogorov axioms, which every test confirms.
6. **Open questions.** Q23.4.

#### 21.4 Measurement reduces to additive numerical comparison

1. **The assumption.** All measurement is ultimately comparison against a standard on a common additive scale.
2. **What is built on it.** Metrology, the SI, the very definition of physical units.
3. **Confirmed vs postulated.** Confirmed in the operational sense: all current instruments are additive comparators. Postulated: that no measurement requires a non-additive (hierarchical) comparator.
4. **Alternatives.** Ultrametric comparators for hierarchical observables (tree-depth, divisibility rank); counting-based (integer) metrology as primitive with real values as limits (Research Note A, v0.1 record doi:10.5281/zenodo.21970454).
5. **Falsifiability.** An experiment whose outcome ordering is provably tree-like — where Archimedean "closer than" transitivity fails but ultrametric closeness holds.
6. **Open questions.** Q23.5.

#### 21.5 Relevant closeness is magnitude-based

1. **The assumption.** Two measured values are "close" when their difference is small in absolute value.
2. **What is built on it.** Error analysis, confidence intervals, the entire practice of precision physics.
3. **Confirmed vs postulated.** Confirmed: magnitude-closeness is the operative notion in every published measurement. Postulated: that divisibility-closeness is never operative.
4. **Alternatives.** $p$-adic closeness for resonant structures (frequencies in rational ratio, $p$-divisibility of level spacings).
5. **Falsifiability.** A system whose statistical correlations cluster by congruence rather than by magnitude — e.g., pair correlations with $p$-adic clustering signatures (the Monna-map programme).
6. **Open questions.** Q23.2.

### Chapter 22 — Alternatives and Testable Consequences

#### 22.1 $p$-adic quantum mechanics
Wavefunctions on $\mathbb{Q}_p$, $p$-adic Schrödinger and Dirac equations, ultrametric diffusion; the mathematics is well developed (Vladimirov, Volovich, Zelenov; Dragovich et al.). The open question is whether any physical system is *natively* $p$-adic. Candidate regimes: hierarchical disorder, spin-glass replicas, protein folding landscapes, adelic string amplitudes.

#### 22.2 Adelic formulations
Treating real and $p$-adic places together; physical predictions require a rule for what is observable at which place. The honest position: adelic physics is a formalism in search of an experiment — and the experiment would be the discovery of a quantity whose natural completion is not Archimedean.

#### 22.3 Finite-precision physics
Formulating dynamics on finite integer grids (no reals at all): automatic error control, no infinities. Reproduces continuum physics as a limit; differs only in regimes the continuum cannot probe.

#### 22.4 Non-Kolmogorov probability
Quantum logic and GPTs already reformulate probability; the remaining question is whether *frequency statistics* ever needs non-additivity — no experiment says yes.

#### 22.5 Generalized measurement theory
POVMs, weak measurements, and sequential-measurement frameworks (Chapter 5.5) show that the classical measurement postulates are already too narrow for quantum practice — the valuation question is the same question one level up: which field do the *numbers* live in?

### Chapter 23 — Open Questions

- **Q23.1** Are there physical variables naturally described by $p$-adic or ultrametric structure, and where should experiment look first?
- **Q23.2** Does the continuum have more structure than measurement requires — is $\mathbb{R}$ over-modeling?
- **Q23.3** Can quantum measurement be formulated without the continuum?
- **Q23.4** Is there an experiment that distinguishes Archimedean from non-Archimedean valuation of a physical quantity?
- **Q23.5** What is the minimal measurement-theoretic structure needed to encode all empirical content?
- **Q23.6** Does finite-precision measurement imply a discrete or finite formulation of quantum mechanics?

---

## Part VI — Vacuum, Dimensionality, Holography, and Emergence

### Chapter 24 — Vacuum Dependence of Particle Content

#### 24.1 Particles as excitations of a chosen vacuum

In quantum field theory a particle is an excitation of a chosen ground state. The ground state is a choice of representation of the field algebra; different choices support different excitation spectra. "Particle" is therefore a two-argument concept — particle *of* a vacuum — and the second argument is usually suppressed.

#### 24.2 The Unruh effect

A uniformly accelerated observer in the Minkowski vacuum detects a thermal bath at $T_U = \hbar a / (2\pi k_B c)$. What is empty for the inertial observer is occupied for the accelerated one: particle number is observer-dependent even in flat spacetime (Unruh, 1976).

#### 24.3 Cosmological particle creation

An expanding universe changes the vacuum adiabatically; modes that start as vacuum fluctuations end as particles. Inflation's amplification of quantum fluctuations into the density perturbations that seeded galaxies is this mechanism writ large — the "empty" early universe populated itself.

#### 24.4 No unique vacuum in curved spacetime

In general curved spacetimes there is no Poincaré group, hence no unique Poincaré-invariant vacuum; inequivalent representations abound (Haag's theorem already kills the interaction-picture uniqueness in flat spacetime). Particle content is a *derived* concept that requires a background to define.

#### 24.5 The assumption audited: "there is a unique vacuum and a unique particle interpretation"

1. **The assumption.** One vacuum, one set of particles, one ontology.
2. **What is built on it.** The Standard Model's particle list; the universality of particle properties; the textbook language of "the vacuum."
3. **Confirmed vs postulated.** Confirmed: the Minkowski vacuum's particle spectrum in inertial frames. Postulated: uniqueness across frames, backgrounds, and regimes.
4. **Alternatives.** Vacuum-relative particle concepts; algebraic QFT where states and representations are the primitives; the condensed-matter view where the ground state is the theory's real object.
5. **Falsifiability.** The Unruh effect and cosmological particle creation are established physics — the assumption is already falsified as a universal claim; what remains is the claim that *our* vacuum's particle list is the final ontology, falsified if a deeper ground state is identified.
6. **Open questions.** Q28.1, Q28.4.

### Chapter 25 — Quasiparticles and Anyons in Condensed Matter

#### 25.1 Electron quasiparticles
The electron of a metal is a dressed, mass-renormalized, finite-lifetime excitation of the Fermi sea (Chapter 2).

#### 25.2 Fractional charge and fractional statistics
The $\nu = 1/3$ FQHE quasiparticle carries charge $e/3$ and anyonic statistics (Chapter 10): the same electron liquid, a different ground state, different "particles."

#### 25.3 Topological order
Ground states with long-range entanglement, anyonic excitations, and degenerate ground states on nontrivial topology: order beyond Landau's symmetry-breaking paradigm. The classification of topological orders is the modern extension of the periodic table of phases.

#### 25.4 Same underlying electrons, different emergent particles
Superconductors (Cooper pairs), quantum Hall states ($e/3$ quasiparticles), metals (Landau quasiparticles), strange metals (no quasiparticles): the underlying electrons are identical; the emergent particles are not. The formalism is the same (effective fields above a ground state); the ground state is the difference.

### Chapter 26 — Dimensionality and Physical Law

#### 26.1 1D, 2D, 3D behavior
Dimensionality changes physics categorically: no phase transitions in 1D at finite temperature (for short-ranged interactions), no long-range order in 2D isotropic Heisenberg models (Mermin–Wagner), different critical exponents, different statistics (Chapter 10).

#### 26.2 Mermin-Wagner theorem
Continuous symmetries cannot break spontaneously in $d \le 2$ at finite temperature for short-range interactions: Goldstone fluctuations destroy long-range order. A theorem with a visible domain: magnetism in two dimensions is genuinely different.

#### 26.3 Kosterlitz-Thouless transition
The 2D $XY$ model orders without symmetry breaking via vortex-antivortex unbinding — a topological transition. BKT physics is realized in 2D superfluids, films, and Josephson arrays: dimensionality again changing the *kind* of law.

#### 26.4 Upper critical dimension
Above $d_c$ (e.g., $d_c = 4$ for Ising) mean-field theory becomes exact: the law *simplifies* with dimension. Physical law is dimension-dependent in a controlled, mathematically understood way.

#### 26.5 Quantum-classical mapping
A $d$-dimensional quantum system at $T=0$ maps to a $(d+1)$-dimensional classical system: the imaginary-time axis is a genuine extra dimension. Dimensionality is not a background given; it is partly a *perspective*.

### Chapter 27 — The Holographic Principle

#### 27.1 Statement
The information content of a region is bounded by its boundary area in Planck units ($S \le A/4G\hbar$; Bekenstein's bound and its refinements). If true in its strong form, a $(d+1)$-dimensional theory of gravity is equivalently described by a $d$-dimensional theory without gravity on the boundary.

#### 27.2 AdS/CFT as a precise duality
Maldacena's correspondence realizes holography exactly: type IIB strings on $AdS_5 \times S^5$ $\leftrightarrow$ $\mathcal{N}=4$ super-Yang-Mills in 4D. One theory, two descriptions, dimension shifting between them.

#### 27.3 Bulk vs boundary
Radial direction in the bulk maps to energy scale on the boundary: the renormalization group is geometric. This is the deepest known instance of "dimension as perspective" (Chapter 26.5).

#### 27.4 Applications to strongly correlated electrons
Holographic strange metals reproduce linear-in-$T$ resistivity and Planckian scattering — the very regime where quasiparticles fail (Chapter 2.3). Holography is currently the only framework producing Planckian transport from a solvable model.

#### 27.5 Holography is not simply "2D applies to 3D"
The slogan misleads: holography is a specific duality with a negative-curvature, extra-dimensional bulk; it does not license naive dimensional reduction, and no general proof exists for realistic spacetimes. It is a load-bearing *possibility*, not an established law of all physics.

### Chapter 28 — Open Questions

- **Q28.1** Is the electron fundamental or emergent — and what are the true primitives if particle number and statistics are vacuum-dependent?
- **Q28.2** Can topological quantum computation use electron-derived quasiparticles, and over what temperature window does protection survive?
- **Q28.3** Does holography imply that local quantum field theory is only effective?
- **Q28.4** Are there observable consequences of treating the electron as a quasiparticle in high-energy physics?
- **Q28.5** What is the correct description of electron states without a global vacuum — and what replaces the Fock space when no vacuum is unique?

---

## Part VII — Cross-Cutting Foundational Assumptions

Fifteen assumptions are audited here, each with the full six-step procedure of §0.3. These are the assumptions that cut across Parts II–VI; they are the load-bearing members of the structure.

### Chapter 29 — The Axiom of Choice

1. **The assumption.** Every collection of nonempty sets admits a choice function; equivalently, every vector space has a basis, every surjection has a section, and Zorn's lemma holds.
2. **What is built on it.** Large portions of functional analysis (Hahn–Banach in full generality, Banach–Alaoglu), topology (Tychonoff), measure theory (existence of non-measurable sets), and the operator theory that quantum mechanics rests on. Physics inherits AC through its mathematics.
3. **Confirmed vs postulated.** AC is independent of ZF — neither provable nor refutable; it is a convention with constructive competitors. Nothing *empirical* confirms it; its role is infrastructural.
4. **Alternatives.** ZF + determinacy; choice-free (constructive) analysis (Bishop); predicative mathematics. Most physics theorems have choice-free versions under weaker hypotheses.
5. **Falsifiability.** The assumption is mathematical, not physical: it is "falsified" only by adopting a foundation where the physical theorems fail — a research programme whose output would be a constructive reformulation of QFT, not an experiment. The physical relevance is indirect but real: which theorems survive without AC is a precise question, and its answer bounds how much mathematics physics actually needs.
6. **Open questions.** **Q29.1**  Which quantum-field-theoretic results genuinely require AC, and can they be replaced by constructive versions with identical physical content?

### Chapter 30 — The Church–Turing Thesis

1. **The assumption.** Every effectively computable function is Turing-computable; the physical version: every physical process can be simulated by a Turing machine.
2. **What is built on it.** The theory of computation, algorithmic information theory, complexity theory, digital physics, and the claim that the universe is in principle simulable.
3. **Confirmed vs postulated.** The mathematical thesis is definitional ("effectively computable" is informal — the thesis is the definition's test). The physical version is an empirical conjecture, supported by every physical computation ever performed and by the equivalence of all known computational models.
4. **Alternatives.** Hypercomputation (real-valued analog computers exploiting exact reals, Malament–Hogarth spacetimes, closed-timelike-curve computation); quantum computation (not hypercomputation — still Turing-equivalent in power, different in complexity).
5. **Falsifiability.** A reproducible physical process producing a non-Turing-computable output (e.g., a reliably correct halting oracle) would falsify the physical thesis. No such demonstration exists; the negative result is a standing empirical fact.
6. **Open questions.** **Q30.1**  Does any physical setting (spacetime structure, exact-continuum machines) realize hypercomputation? What is the complexity-theoretic thesis's physical status under quantum gravity?

### Chapter 31 — The Real Number Continuum

1. **The assumption.** Space, time, and observable values are modeled by $\mathbb{R}$ — complete, Archimedean, infinitely divisible.
2. **What is built on it.** Calculus, differential equations, Riemannian geometry, path integrals, probability theory, and the standard formulation of every fundamental theory (Part V develops the full treatment).
3. **Confirmed vs postulated.** Confirmed: real-valued modeling at every probed scale. Postulated: infinite divisibility below the Planck scale and the Archimedean character of all closeness.
4. **Alternatives.** $p$-adic and adelic models (Chapter 22); causal sets and discrete structures; finite-precision physics.
5. **Falsifiability.** Planck-scale dispersion or discreteness signatures; an observable with native ultrametric closeness (Chapter 21.1).
6. **Open questions.** **Q31.1**  Q23.1–Q23.6.

### Chapter 32 — Microcausality and Locality

1. **The assumption.** Spacelike-separated observables commute (bosonic) or anticommute appropriately — no signal, and more: no *statistical* influence, propagates faster than light.
2. **What is built on it.** The spin-statistics theorem and CPT (Chapter 9), dispersion relations, the S-matrix programme, and the causal structure of QFT.
3. **Confirmed vs postulated.** Confirmed to experimental precision: no superluminal signaling has ever been observed. Postulated: exact commutativity at all spacelike separations, including trans-Planckian ones.
4. **Alternatives.** Noncommutative field theories with modified microcausality; string-theoretic nonlocality (softened light-cone); "wedge" locality of algebraic QFT.
5. **Falsifiability.** A measured spacelike statistical correlation between local observables beyond quantum prediction; a violation of the dispersion relations derived from microcausality.
6. **Open questions.** **Q32.1**  How much microcausality violation is excluded by the *absence* of anyonic signatures in $3+1$D (Q12.4)? Does quantum gravity soften the light-cone observably?

### Chapter 33 — Fixed Spacetime Background

1. **The assumption.** Fields propagate on a pre-existing, fixed spacetime; the background is not itself dynamical.
2. **What is built on it.** Standard QFT, the Standard Model, perturbative quantum gravity as an effective field theory.
3. **Confirmed vs postulated.** Confirmed: background-dependent QFT is empirically superb in all regimes probed. Postulated: the fixedness — quantum gravity expects the background to be dynamical (background independence).
4. **Alternatives.** Loop quantum gravity (background-independent kinematics); string theory (background emerges); causal-set gravity.
5. **Falsifiability.** Observing gravitational backreaction of quantum states beyond the semiclassical Einstein equation in a regime where background-dependent theory fails; or demonstrating that no background-independent completion exists.
6. **Open questions.** **Q33.1**  Is the effective-field-theory treatment of quantum gravity complete for all non-Planckian regimes, or does background independence impose observable corrections?

### Chapter 34 — Unitarity as Absolute

1. **The assumption.** Closed-system evolution is exactly unitary; information is exactly conserved.
2. **What is built on it.** Probability conservation, the Born rule's self-consistency, black-hole thermodynamics as information-preserving, the reconstruction of spacetime from entanglement.
3. **Confirmed vs postulated.** Confirmed: unitarity of effective evolution at tested precision. Postulated: exactness at horizons and for the whole universe.
4. **Alternatives.** Objective-collapse models; information-loss (non-unitary horizon) scenarios; open-system fundamental dynamics.
5. **Falsifiability.** Collapse-model bounds (spontaneous localization signatures in matter-wave interferometry); information-loss signatures in gravitational-wave and black-hole observations; precision tests of probability conservation.
6. **Open questions.** **Q34.1**  Q7.2. Does the resolution of the information paradox require modifying unitarity, or modifying the spacetime picture (remnants, fuzzballs, islands)?

### Chapter 35 — The Path Integral as Well-Defined

1. **The assumption.** Quantum amplitudes are given by a functional integral $\int \mathcal{D}\phi\, e^{iS[\phi]/\hbar}$ over all histories, and this object is well-defined in the continuum.
2. **What is built on it.** Most modern QFT calculations, lattice field theory (where the measure is defined), the Euclidean approach to quantum gravity, instanton and topological physics.
3. **Confirmed vs postulated.** Confirmed: lattice-regularized and perturbation-theoretic results to remarkable precision. Postulated: the continuum measure's existence (unproven in general; the Euclidean measure exists in some cases via constructive field theory).
4. **Alternatives.** Operator/Hilbert-space formulations; algebraic QFT; resummation-free nonperturbative definitions (conformal bootstrap, integrability).
5. **Falsifiability.** The assumption is mathematical: it fails if no continuum measure exists for a theory whose observables are nevertheless defined — in which case the path integral is a *tool*, not a foundation. The physical discriminator is whether any prediction relies on an ill-defined measure in a way alternatives cannot reproduce.
6. **Open questions.** **Q35.1**  Is there a theory of physical interest whose path integral provably has no continuum definition while the physics is well-defined?

### Chapter 36 — Symmetry as Fundamental

1. **The assumption.** Symmetries — gauge and global — are fundamental inputs of nature; laws are invariants, and particles are representations of symmetry groups.
2. **What is built on it.** The Standard Model (a list of gauge groups and representations), Noether's conserved charges, the Wigner classification (Chapter 8), modern effective field theory.
3. **Confirmed vs postulated.** Confirmed: the predictive power of symmetry-organized dynamics (the SM is arguably the most tested structure in science). Postulated: that symmetries are primitive rather than emergent or descriptive.
4. **Alternatives.** Emergent gauge fields (lattice gauge theory: gauge fields as dynamics of links, symmetry as redundancy); symmetry as bookkeeping for redundant descriptions; Levin-Wen style emergence of gauge structure from entanglement.
5. **Falsifiability.** A physical regime where a "fundamental" symmetry provably cannot be emergent — hard to construct because gauge symmetry is known to be emergible in principle; the sharper question is whether *all* of nature's symmetries are emergible.
6. **Open questions.** **Q36.1**  Which symmetries, if any, must be assumed? Can the SM gauge group itself emerge from entanglement structure?

### Chapter 37 — Ergodicity and the Eigenstate Thermalization Hypothesis

1. **The assumption.** Closed many-body systems thermalize: time averages equal ensemble averages, and individual eigenstates locally reproduce microcanonical statistics (ETH).
2. **What is built on it.** Equilibrium statistical mechanics; the second law as emergent; the justification for the ensembles of Chapter 15.
3. **Confirmed vs postulated.** Confirmed: thermalization in generic interacting systems, ETH numerically in chaotic models. Falsified in general: many-body localization and quantum many-body scars are counterexamples — ergodicity holds in a *regime*, not universally.
4. **Alternatives.** Weaker premises: eigenstate decorrelation, generalized ETH (eigenstates of one observable look thermal in another), typicality arguments that avoid ergodicity entirely.
5. **Falsifiability.** The assumption is already falsified as a universal claim (MBL); the surviving content is the classification of the thermalizing regime — falsified if a natural isolated system fails to thermalize without localization or integrability.
6. **Open questions.** **Q37.1** What is the precise boundary of the thermalizing regime? **Q37.2** Can thermodynamics be rebuilt on weaker premises than ergodicity (fluctuation theorems suggest yes)?

### Chapter 38 — Global Hyperbolicity

1. **The assumption.** Spacetime admits a Cauchy surface: initial data determine the future everywhere (predictability), and closed timelike curves are absent.
2. **What is built on it.** The initial-value formulation of general relativity; quantum field theory on globally hyperbolic spacetimes; the very notion of a "prediction" in gravitational physics.
3. **Confirmed vs postulated.** Confirmed: all observed spacetime is consistent with global hyperbolicity. Postulated: that it holds universally — naked singularities (weak cosmic censorship) and CTCs are excluded by conjecture, not proof.
4. **Alternatives.** CTC physics (Deutsch's self-consistency condition); firewall/fuzzball structures at horizons; non-globally-hyperbolic completions of black-hole interiors.
5. **Falsifiability.** Observation of a naked singularity or of a CTC-region signature (e.g., through gravitational-wave or lensing evidence) would falsify the universal form.
6. **Open questions.** **Q38.1**  Is weak cosmic censorship a theorem? What replaces predictability where global hyperbolicity fails?

### Chapter 39 — Extensivity of Entropy

1. **The assumption.** Entropy scales with volume; a thermodynamic limit exists in which entropy is extensive.
2. **What is built on it.** Classical thermodynamics; the thermodynamic limit of statistical mechanics; additivity of information in composite systems.
3. **Confirmed vs postulated.** Confirmed: extensivity for ordinary matter. Falsified in general: black holes carry Bekenstein–Hawking entropy $S = A/4G\hbar$ — an *area* law — and ground-state entanglement entropy in local systems obeys area laws; additivity fails for entangled subsystems (subadditivity replaces it).
4. **Alternatives.** Holographic entropy bounds; generalized entropies (Rényi, Tsallis); entanglement entropy as the primitive with thermodynamic entropy emergent.
5. **Falsifiability.** A black hole whose entropy provably scales with volume would falsify the holographic reading; conversely the area law is already established for horizons.
6. **Open questions.** **Q39.1** Is the covariant entropy bound a law of quantum gravity? **Q39.2** Does area-law entanglement select the dimension of space?

### Chapter 40 — Exact Lorentz Invariance

1. **The assumption.** Lorentz symmetry is exact — no preferred frame at any scale.
2. **What is built on it.** The Standard Model, the spin-statistics theorem, relativistic kinematics, the equivalence principle's local Lorentz frames.
3. **Confirmed vs postulated.** Confirmed: Lorentz invariance to extreme precision (modern bounds exclude preferred-frame effects at levels far below Planck-suppressed naive estimates in many sectors). Postulated: exactness at the Planck scale.
4. **Alternatives.** Lorentz-violating effective field theory (Standard-Model Extension); doubly special relativity (deformed kinematics with invariant scales); emergent Lorentz symmetry (fermionic vacua, condensed-matter analogues).
5. **Falsifiability.** Preferred-frame or sidereal signals in clock-comparison, interferometric, or astrophysical tests; energy-dependent photon speeds from gamma-ray bursts.
6. **Open questions.** **Q40.1**  How far below Planck scale must Lorentz violation be suppressed, and is "emergent Lorentz invariance" testable in condensed-matter analogues?

### Chapter 41 — Kolmogorov Probability Axioms

1. **The assumption.** Probabilities are measures on a Boolean $\sigma$-algebra: distributive logic, countable additivity, real values.
2. **What is built on it.** Classical statistics, stochastic calculus, the interpretation of every frequency measurement.
3. **Confirmed vs postulated.** Confirmed: frequencies behave Kolmogorovly in every test. Postulated: that the event algebra of nature is Boolean — quantum interference shows the algebra of *propositions* is non-distributive, which is why quantum probability generalizes Kolmogorov.
4. **Alternatives.** Quantum logic; GPT probability; quasi-probability representations.
5. **Falsifiability.** The strict (propositional) form is already falsified by interference; the frequency form stands until an experiment shows non-additive frequencies.
6. **Open questions.** **Q41.1**  Q23.4. Is there a natural non-Kolmogorov statistics of *events* (not just propositions) in any physical system?

### Chapter 42 — Smooth Manifold Spacetime

1. **The assumption.** Spacetime is a $C^\infty$ Lorentzian manifold — smooth at all scales.
2. **What is built on it.** General relativity, differential geometry as the language of physics, the continuum treatment of fields.
3. **Confirmed vs postulated.** Confirmed: smooth modeling at all probed scales ($\sim 10^{-18}$ m and below via photon-timing bounds). Postulated: smoothness at the Planck scale, where quantum fluctuations of geometry are expected to dissolve it.
4. **Alternatives.** Causal sets; noncommutative spacetime; group field theory and spin foams; $p$-adic spacetime.
5. **Falsifiability.** Planck-scale dispersion in gamma-ray bursts or gravitational-wave propagation; causal-set Poisson-fluctuation signatures; noncommutative corrections to quantum fields.
6. **Open questions.** **Q42.1**  Is spacetime discrete, noncommutative, or smooth at the Planck scale — and which observable reaches it first?

### Chapter 43 — The Assumption That Mathematics Is the Language of Nature

1. **The assumption.** Nature is *written in* mathematics — mathematical structure is not merely descriptive of physics but constitutive of it (Galileo's book of nature; Wigner's "unreasonable effectiveness").
2. **What is built on it.** The entire formal apparatus of theoretical physics; the practice of deriving existence from consistency (Dirac's positron; the Higgs).
3. **Confirmed vs postulated.** Confirmed: the instrumental success of mathematics in physics (Wigner's datum). Postulated: the *constitutive* claim — that the success reflects ontology rather than the selection effect of our formal tools.
4. **Alternatives.** Computational/informational pictures (the universe as computation); physics-first pictures where mathematics is the residue of our descriptions; the instrumentalist reading where only the empirical adequacy of formal models carries weight.
5. **Falsifiability.** This is a metaphysical assumption: it is not falsified by any single experiment, but it is *bounded* by them — a persistent regime where mathematics fails to describe would force the instrumentalist reading. The treatise's position: the claim is a named premise, not a finding.
6. **Open questions.** **Q43.1**  Is the effectiveness of mathematics a fact about nature or about mathematicians? What would a non-mathematical physics even be?

---

## Part VIII — A Critical Research Programme

### Chapter 44 — Guiding Principles

#### 44.1 Every load-bearing assumption is a falsifiable postulate
The treatise's procedural premise: anything load-bearing that is not experimentally established is a postulate, and postulates deserve falsifiability conditions. Nothing is exempted by tradition.

#### 44.2 Domain of validity mapping
For each assumption, the deliverable is a *map* — where it holds, where it is tested, where it is untested, where it is known to fail. Maps, not verdicts.

#### 44.3 No assumption is rejected by default
Alternatives must *earn* adoption by empirical discrimination; the burden runs both ways — an assumption is not retained by tradition, and an alternative is not adopted by novelty.

#### 44.4 Alternatives must be empirically distinguishable
An alternative that reproduces all predictions with no discriminating experiment is not physics but interpretation; the programme demands operational differences or says so explicitly.

### Chapter 45 — Experimental Probes

#### 45.1 Precision electron measurements
$g-2$ at ever higher precision (electron and muon); EDM searches (ACME-class and beyond); stability and compositeness bounds — the electron as the probe of Chapters 1–3.

#### 45.2 Anyon interferometry
Non-abelian braiding demonstrations; the anyon collider programme; the topological-qubit race (Chapter 10.4).

#### 45.3 Quantum simulation of non-Archimedean or finite-dimensional structures
Simulating ultrametric dynamics on qubit platforms; finite-Hilbert-space physics per causal diamond; the designed-experiment route to Q23.1–Q23.6.

#### 45.4 Tests of Lorentz violation
Clock-comparison and sidereal searches; gamma-ray dispersion tests; SME parameter bounds (Chapter 40).

#### 45.5 Spin-statistics tests
Violation searches for the exclusion principle (Gran Sasso-class experiments); parastatistics searches (Chapter 12).

#### 45.6 Quantum thermodynamics of single-electron devices
Landauer-erasure at the single-electron level; fluctuation theorems in mesoscopic conductors; the direct route to Q17.1.

#### 45.7 Entropy production in strongly correlated systems
Strange metals and MBL platforms as laboratories for the *failure* of ergodicity (Chapter 37).

#### 45.8 Engineered $p$-adic or adelic quantum models
Building the candidate systems of Chapter 22.1 and testing for native ultrametric structure.

#### 45.9 Probing spacetime smoothness at Planck scales
Gamma-ray timing, gravitational-wave dispersion, and interferometric Planck-scale probes (Chapter 42).

### Chapter 46 — Theoretical Probes

#### 46.1 Real and quaternionic quantum mechanics with observable signatures
Deriving the multipath-interference predictions that discriminate the number field (Chapter 5.1).

#### 46.2 Model-independent frameworks
GPT and quantum-logic reformulations of the tested content, to see exactly which axioms carry the predictions.

#### 46.3 Finite-dimensional quantum mechanics for causal diamonds
Entropy-bound-limited Hilbert spaces as the honest finite description (Chapter 5.4).

#### 46.4 Measurement theory without Kolmogorov probability
Quantum-logic statistics and their empirical content (Chapter 41).

#### 46.5 $p$-adic and adelic models of known physics
Reformulating a known system (oscillator, hydrogen atom, Ising chain) over non-Archimedean fields and asking what would be observable (Chapters 19, 22).

#### 46.6 Deriving spin-statistics from information principles
Entanglement-based derivations that trade Lorentz invariance for information axioms — which premise is cheaper? (Chapter 9)

#### 46.7 Thermodynamics without ergodicity
Building the second law on fluctuation theorems and typicality, and testing where the two foundations diverge (Chapter 37).

#### 46.8 Emergent spacetime and holographic models
Background-independent and holographic reconstructions (Chapters 27, 33).

### Chapter 47 — Milestones and Decision Points

#### 47.1 Short term: precision tests of existing assumptions
The next decimal of $g-2$, EDM, Lorentz violation, and exclusion-principle bounds — each digit is a domain-of-validity datum.

#### 47.2 Medium term: distinguishing alternative frameworks
Number-field discrimination in interference; anyon non-abelianity; ultrametric-structure searches.

#### 47.3 Long term: replacing or confirming foundational postulates
Planck-scale probes; topological quantum computing at scale; and whatever the register (Part IX) promotes next.

---

## Part IX — Consolidated Open Questions

### Chapter 48 — List of All Open Questions

Organized by theme; each entry carries its originating chapter and its discriminator.

**The electron itself (Part I).** Q3.1–Q3.5: charge quantization's origin; absolute stability; compositeness; the mass's origin; finite-dimensional description.

**Hilbert space (Part II).** Q7.1–Q7.6: the number field of amplitudes; unitarity's extent; factorization; finite dimension; PVM vs POVM; the Born rule's depth.

**Spin and statistics (Part III).** Q12.1–Q12.6: parastatistics; elementary anyons; emergent spin; theorem's premises; identity; non-abelian demonstrations.

**Thermodynamics and computation (Part IV).** Q17.1–Q17.7: the true erasure cost; error-correction heat; reversible limits; entanglement and entropy production; spin vs charge logic; fluctuation theorems for correlated electrons; the physical Church–Turing thesis.

**Measurement and valuation (Part V).** Q23.1–Q23.6: native ultrametric observables; $\mathbb{R}$ over-modeling; measurement without the continuum; the discriminating experiment; minimal structure; discreteness.

**Vacuum and emergence (Part VI).** Q28.1–Q28.5: electron fundamental or emergent; topological-qubit temperature window; holography's effective status; high-energy quasiparticle consequences; Fock space without a unique vacuum.

**Cross-cutting (Part VII).** Q29.1 (which QFT results genuinely require the Axiom of Choice) · Q30.1 (hypercomputation settings) · Q31.1 (Q23.1–Q23.6) · Q32.1 (microcausality violation excluded by absence of anyonic signatures) · Q33.1 (background-independence observables) · Q34.1 (Q7.2, the information paradox) · Q35.1 (path integrals with no continuum measure) · Q36.1 (which symmetries are irreducibly assumed) · Q37.1–**Q37.2** (thermalizing-regime boundary; thermodynamics without ergodicity) · Q38.1 (cosmic censorship) · Q39.1–**Q39.2** (covariant entropy bound; area law and dimension) · Q40.1 (Lorentz-violation bounds) · Q41.1 (Q23.4, non-Kolmogorov events) · Q42.1 (Planck-scale smoothness) · Q43.1 (effectiveness of mathematics).

### Chapter 49 — Questions Most Likely to Yield Practical Advances

1. **Energy-efficient computation** (Q17.1, Q17.3, Q17.5): the Landauer limit and beyond; spin vs charge logic — directly monetizable physics.
2. **High-temperature superconductors** (Q28.1, Q28.4): what replaces quasiparticles — the route to room-temperature superconductivity runs through Part IV's unknowns.
3. **Topological quantum computing** (Q12.6, Q28.2): non-abelian anyons and protection windows.
4. **Nanoscale thermodynamics** (Q17.2, Q17.6): single-electron engines and fluctuation control.
5. **Spintronics** (Q17.5, Q12.3): spin without charge currents.

### Chapter 50 — Questions Most Likely to Yield Foundational Advances

1. **The nature of Hilbert space** (Q7.1, Q7.4): the number field and the dimension.
2. **The origin of spin and statistics** (Q12.3, Q12.4): emergent or primitive.
3. **The valuation structure of physical quantities** (Q23.1, Q23.4): Archimedean or not.
4. **The emergence of spacetime** (Q28.3, Q28.5): holography and background independence.
5. **The nature of entropy and time** (Q37.1, Q39.1): ergodicity's regime and extensivity's edge.

### Chapter 51 — The Argument in Summary

#### 51.1 Summary of the argument

The electron is a hook for foundational assumptions. Nine parts and fifty-one chapters have applied one procedure — state, catalogue what is built, separate confirmed from postulated, list alternatives, define falsifiability, record open questions — to the assumptions carrying quantum mechanics, thermodynamics, and computation: the Hilbert-space framework and its six hidden premises; the spin-statistics theorem and its five premises; the thermodynamic foundations of computation; the Archimedean valuation of every measured quantity; the unique-vacuum picture of particles; and fifteen cross-cutting assumptions from the Axiom of Choice to the smooth-manifold model of spacetime. The audit's findings are uniform: each assumption is confirmed in a tested domain, unproven at an edge, and in several cases — anyons, quasiparticles, vacuum-dependent particle content, broken ergodicity, area-law entropy — *already known to fail* as universal claims.

#### 51.2 What this treatise does not claim

It does not claim current physics is wrong — the confirmed domains are real and will remain the science's load-bearing floor. It does not claim any alternative framework is correct — alternatives were catalogued, not endorsed. It does not claim philosophy replaces experiment — every question is posed with its discriminator.

#### 51.3 What this treatise does claim

Three claims, each bounded: (1) the assumptions are *contingent* — they are postulates with premises, not necessities; (2) they are *testable in principle* — every one carries a falsifiability condition, and several are already being tested; (3) investigating them is *scientifically necessary* — the practical frontiers (computation, superconductivity, topological qubits) and the foundational ones (spacetime, entropy, valuation) are the same questions viewed at different scales.

#### 51.4 Final statement

Pulling on the electron may open the entire foundation. The purpose of this treatise has been to make the pull precise, itemized, and falsifiable — so that each load-bearing assumption can be promoted from an article of faith to an object of experiment, and each domain of validity can be mapped rather than assumed.

---

## Appendix A — Mathematical Background

- **Hilbert spaces:** complex inner-product spaces complete in the induced norm; the spectral theorem for self-adjoint operators; tensor products.
- **Representation theory:** Wigner's classification; projective representations and $SU(2)$; the braid group $B_N$ vs the permutation group $S_N$.
- **Ostrowski's theorem:** the classification of absolute values on $\mathbb{Q}$; $\mathbb{R}$, $\mathbb{Q}_p$, and the adeles $\mathbb{A}_{\mathbb{Q}}$; ultrametricity.
- **$p$-adic numbers:** completions under $|\cdot|_p$; the ultrametric inequality; tree structure.
- **Adeles:** the restricted product; the place-at-infinity plus all finite places.

## Appendix B — Experimental Techniques

- **Penning traps:** cyclotron-frequency measurements of $m_e$ and $g-2$; the most precise number in physics.
- **Anyon interferometry:** edge-channel colliders and Fabry–Pérot interferometry for fractional statistics.
- **Quantum simulation:** ultrametric and finite-dimensional models on qubit platforms.
- **Precision measurement:** clock comparison, interferometry, single-electron devices.

## Appendix C — Glossary of Terms

**Quasiparticle** — collective excitation of a many-body ground state behaving as a particle with renormalized parameters. **Anyon** — $2+1$D excitation with exchange phase $e^{i\theta}$, $\theta$ arbitrary. **Vacuum** — a chosen ground state of a field theory. **Hilbert space** — the complex vector space of quantum states. **Valuation** — a notion of size/divisibility on a field; by Ostrowski, Archimedean or $p$-adic. **Ergodicity/ETH** — the thermalization hypothesis for closed systems. **Landauer's principle** — $k_B T \ln 2$ minimum dissipation per erased bit. **Holography** — boundary-area encoding of bulk information. **GPT** — generalized probabilistic theory. **MBL** — many-body localization.

## Appendix D — Bibliography

The 42 verified entries (all Crossref exact-DOI or arXiv live-verified; evidence in `citation-audit.md` and `artifacts/external-search/`):

1. Dirac, P. A. M. (1928). The quantum theory of the electron. *Proc. R. Soc. A* 117(778), 610–624. doi:10.1098/rspa.1928.0023
2. von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik.* Springer. doi:10.1007/978-3-642-96048-2
3. Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung $\varphi(x)\varphi(y)=\varphi(xy)$. *Acta Math.* 41, 271–284 (reprint locator doi:10.1007/978-3-0348-9358-9_17).
4. Wigner, E. P. (1939). On unitary representations of the inhomogeneous Lorentz group. *Ann. Math.* 40(1), 149–204. doi:10.2307/1968551
5. Pauli, W. (1940). The connection between spin and statistics. *Phys. Rev.* 58(8), 716–722. doi:10.1103/PhysRev.58.716
6. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM J. Res. Dev.* 5(3), 183–191. doi:10.1147/rd.53.0183
7. Bennett, C. H. (1973). Logical reversibility of computation. *IBM J. Res. Dev.* 17(6), 525–532. doi:10.1147/rd.176.0525
8. Unruh, W. G. (1976). Notes on black-hole evaporation. *Phys. Rev. D* 14(4), 870–892. doi:10.1103/PhysRevD.14.870
9. Leinaas, J. M., & Myrheim, J. (1977). On the theory of identical particles. *Nuovo Cim. B* 37(1), 1–23. doi:10.1007/BF02727953
10. Tsui, D. C., Stormer, H. L., & Gossard, A. C. (1982). Two-dimensional magnetotransport in the extreme quantum limit. *Phys. Rev. Lett.* 48(22), 1559–1562. doi:10.1103/PhysRevLett.48.1559
11. Wilczek, F. (1982). Quantum mechanics of fractional-spin particles. *Phys. Rev. Lett.* 49(14), 957–959. doi:10.1103/PhysRevLett.49.957
12. Laughlin, R. B. (1983). Anomalous quantum Hall effect. *Phys. Rev. Lett.* 50(18), 1395–1398. doi:10.1103/PhysRevLett.50.1395
13. Arovas, D., Schrieffer, J. R., & Wilczek, F. (1984). Fractional statistics and the quantum Hall effect. *Phys. Rev. Lett.* 53(7), 722–723. doi:10.1103/PhysRevLett.53.722
14. Halperin, B. I. (1984). Statistics of quasiparticles and the hierarchy of fractional quantized Hall states. *Phys. Rev. Lett.* 52(18), 1583–1586. doi:10.1103/PhysRevLett.52.1583
15. Mermin, N. D., & Wagner, H. (1966). Absence of ferromagnetism or antiferromagnetism in one- or two-dimensional isotropic Heisenberg models. *Phys. Rev. Lett.* 17(22), 1133–1136. doi:10.1103/PhysRevLett.17.1133
16. Kosterlitz, J. M., & Thouless, D. J. (1973). Ordering, metastability and phase transitions in two-dimensional systems. *J. Phys. C* 6(7), 1181–1203. doi:10.1088/0022-3719/6/7/010
17. Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). Theory of superconductivity. *Phys. Rev.* 108(5), 1175–1204. doi:10.1103/PhysRev.108.1175
18. Wigner, E. P. (1960). The unreasonable effectiveness of mathematics in the natural sciences. *Comm. Pure Appl. Math.* 13(1), 1–14. doi:10.1002/cpa.3160130102
19. Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika* 1(3), 195–200. doi:10.1103/PhysicsPhysiqueFizika.1.195
20. Feynman, R. P. (1948). Space-time approach to non-relativistic quantum mechanics. *Rev. Mod. Phys.* 20(2), 367–387. doi:10.1103/RevModPhys.20.367
21. Bekenstein, J. D. (1973). Black holes and entropy. *Phys. Rev. D* 7(8), 2333–2346. doi:10.1103/PhysRevD.7.2333
22. Deutsch, J. M. (1991). Quantum statistical mechanics in a closed system. *Phys. Rev. A* 43(4), 2046–2049. doi:10.1103/PhysRevA.43.2046
23. Srednicki, M. (1994). Chaos and quantum thermalization. *Phys. Rev. E* 50(2), 888–901. doi:10.1103/PhysRevE.50.888
24. 't Hooft, G. (1993). Dimensional reduction in quantum gravity. arXiv:gr-qc/9310026.
25. Susskind, L. (1995). The world as a hologram. *J. Math. Phys.* 36(11), 6377–6396. doi:10.1063/1.531249
26. Maldacena, J. (1998). The large $N$ limit of superconformal field theories and supergravity. *Adv. Theor. Math. Phys.* 2(2), 231–252. doi:10.4310/ATMP.1998.v2.n2.a1
27. Nielsen, M. A., & Chuang, I. L. (2000). *Quantum Computation and Quantum Information.* Cambridge University Press. doi:10.1017/CBO9780511976667
28. Dragovich, B., Khrennikov, A., Kozyrev, S. V., & Volovich, I. V. (2009). On $p$-adic mathematical physics. *p-Adic Numbers Ultrametric Anal. Appl.* 1(1), 1–17. doi:10.1134/S2070046609010014
29. Bartolomei, H., et al. (2020). Fractional statistics in anyon collisions. *Science* 368(6487), 173–177. doi:10.1126/science.aaz5601
30. Nakamura, J., Liang, S., Gardner, G. C., & Manfra, M. J. (2020). Direct observation of anyonic braiding statistics. *Nat. Phys.* 16, 931–936. doi:10.1038/s41567-020-1019-1
31. Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Z. Phys.* 37(12), 863–867. doi:10.1007/BF01397477
32. Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung.* Springer, Berlin. doi:10.1007/978-3-642-49888-6
33. Church, A. (1936). An unsolvable problem of elementary number theory. *Amer. J. Math.* 58(2), 345–363. doi:10.2307/2371045
34. Turing, A. M. (1937). On computable numbers, with an application to the Entscheidungsproblem. *Proc. London Math. Soc.* s2-42(1), 230–265 (received 1936). doi:10.1112/plms/s2-42.1.230
35. Millikan, R. A. (1913). On the elementary electrical charge and the Avogadro constant. *Phys. Rev.* 2(2), 109–143. doi:10.1103/PhysRev.2.109
36. Sommerfeld, A. (1928). Zur Elektronentheorie der Metalle auf Grund der Fermischen Statistik. *Z. Phys.* 47(1-2), 1–32. doi:10.1007/BF01391052
37. Shannon, C. E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* 27(3), 379–423. doi:10.1002/j.1538-7305.1948.tb01338.x
38. Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *J. Math. Mech.* 6(6), 885–893. doi:10.1512/iumj.1957.6.56050
39. Dyson, F. J., & Lenard, A. (1967). Stability of matter. I. *J. Math. Phys.* 8(3), 423–434. doi:10.1063/1.1705209
40. Hawking, S. W. (1974). Black hole explosions? *Nature* 248(5443), 30–31. doi:10.1038/248030a0
41. Lieb, E. H., & Thirring, W. E. (1975). Bound for the kinetic energy of fermions which proves the stability of matter. *Phys. Rev. Lett.* 35(11), 687–689. doi:10.1103/PhysRevLett.35.687
42. Vladimirov, V. S., & Volovich, I. V. (1989). p-adic quantum mechanics. *Comm. Math. Phys.* 123(4), 659–676. doi:10.1007/BF01218590

## Index

**Subject index.** Anyons (10.1, 25.2); braid group (10.3); Church–Turing thesis (30); ergodicity (37); falsifiability map (§IV.3 of the v0.1 record; Part VII); Fermi liquid (2.3); fractional quantum Hall effect (10.2); Hilbert space (4, 5); holography (27); Landauer (14); Lorentz invariance (40); measurement (18); microcausality (32); Ostrowski (19); path integral (35); quasiparticles (2.2, 25); spin-statistics (9); ultrametric (19.2, 21); unitarity (34); vacuum (24).

**Author index.** Bekenstein; Bell; Bennett; Dirac; Dragovich; Feynman; Halperin; Kosterlitz–Thouless; Landauer; Laughlin; Leinaas–Myrheim; Maldacena; Mermin–Wagner; Nakamura; Nielsen–Chuang; Ostrowski; Pauli; Srednicki; Susskind; 't Hooft; Tsui–Stormer–Gossard; Unruh; von Neumann; Wigner; Wilczek.










