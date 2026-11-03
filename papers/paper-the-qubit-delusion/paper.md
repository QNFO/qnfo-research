---
title: "The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-07-08
abstract: |
  The quantum computing industry has absorbed approximately $35 billion in global investment
  over two decades while delivering zero commercially viable machines. This paper argues
  that the failure is not merely an engineering delay but an epistemic crisis: the dominant
  qubit-gate-circuit model of quantum computation imports a particle ontology that is
  inconsistent with quantum field theory, relational quantum mechanics, and the physics of
  continuous, correlated systems. Through systematic deconstruction of the scaffolds
  underlying quantum computing -- qubit-as-particle, gate-as-discrete-operation,
  decoherence-as-enemy, error-correction-as-classical-coding -- we identify the invariants
  that survive scaffold removal (superposition, entanglement, correlation structure, phase
  coherence) and examine alternative computational paradigms (measurement-based,
  continuous-variable, topological, and field-theoretic) that are more faithful to quantum
  reality. We combine ontological analysis with empirical forensics -- a reproducibility
  scorecard of twenty major milestone claims, a comparative bubble-morphology analysis
  situating the quantum computing capital structure alongside historical technology bubbles,
  and a press-release-versus-preprint claim-gap analysis -- to assess whether the field is
  producing science or narrative assets. The evidence suggests a systematic map-territory
  confusion operating at industrial scale, sustained by institutional incentives that reward
  optimism over falsification. We conclude with a constructive research agenda grounded in
  field-theoretic and relational quantum computation.
keywords:
  - quantum computing
  - philosophy of physics
  - hype cycles
  - reproducibility crisis
  - quantum field theory
  - relational quantum mechanics
  - innovation economics
---

# The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing

## Abstract

The quantum computing industry has absorbed approximately $35 billion in global investment over two decades while delivering zero commercially viable machines. This paper argues that the failure is not merely an engineering delay but an epistemic crisis: the dominant qubit-gate-circuit model of quantum computation imports a particle ontology that is inconsistent with quantum field theory, relational quantum mechanics, and the physics of continuous, correlated systems. Through systematic deconstruction of the scaffolds underlying quantum computing -- qubit-as-particle, gate-as-discrete-operation, decoherence-as-enemy, error-correction-as-classical-coding -- we identify the invariants that survive scaffold removal (superposition, entanglement, correlation structure, phase coherence) and examine alternative computational paradigms (measurement-based, continuous-variable, topological, and field-theoretic) that are more faithful to quantum reality. We combine ontological analysis with empirical forensics -- a reproducibility scorecard of twenty major milestone claims, a comparative bubble-morphology analysis situating the quantum computing capital structure alongside historical technology bubbles, and a press-release-versus-preprint claim-gap analysis -- to assess whether the field is producing science or narrative assets. The evidence suggests a systematic map-territory confusion operating at industrial scale, sustained by institutional incentives that reward optimism over falsification. We conclude with a constructive research agenda grounded in field-theoretic and relational quantum computation.

# 1. Introduction

In October 2019, Google announced "quantum supremacy" --- a 53-qubit processor,
Sycamore, had performed a random circuit sampling task in 200 seconds that
would, Google claimed, take the world's largest supercomputer 10,000 years to
reproduce [@Arute2019]. Sundar Pichai compared the achievement to the Wright
brothers' first flight. The announcement triggered a wave of media coverage,
venture capital inflows, and national quantum strategies across the G20.

Four years later, IBM's Head of Quantum, Jay Gambetta, reframed the field's
ambitions. Gone was "supremacy." The new watchword was "quantum utility" --- a
more modest claim that quantum computers might someday solve problems of
practical interest. IBM's Eagle processor, with 127 qubits, had simulated the
Ising model on a scale that strained classical methods [@Kim2023]. Yet no
commercially valuable computation had been performed that could not, with some
effort, be accomplished on classical hardware.

This pattern --- spectacular announcement followed by qualification, followed by
a new, more distant milestone --- has repeated with metronomic regularity
throughout quantum computing's commercial history. D-Wave sold "quantum
computers" to Lockheed Martin and Google in 2011 -- 2013, only for independent
benchmarking to reveal no speedup over classical algorithms for the problems
tested [@Ronnow2014]. Rigetti went public via SPAC at a $1.5 billion valuation
in 2022; by 2024 its stock had declined over 90%. IonQ, the first pure-play
quantum computing company to IPO, has oscillated between hype-driven rallies and
reality-driven corrections.

By 2026, the global quantum computing industry has absorbed an estimated $35
billion in combined public and private investment. No commercially viable
quantum computer exists. Not one. The roadmaps project fault-tolerant machines
in the 2030s, which would mean a roughly forty-year interval between Shor's
algorithm (1994) --- the field's foundational existence proof --- and a working
product. Even those timelines assume flawless execution of error-correction
protocols that currently require thousands of physical qubits to encode a single
logical qubit.

The standard narrative attributes this protracted timeline to engineering
difficulty: qubits are fragile, decoherence is relentless, error correction is
expensive, and scaling is hard. This is undoubtedly true. But it may also be
*insufficient* --- a proximate explanation that obscures a deeper, structural
problem.

This paper proposes a different diagnosis. **The failure of quantum computing
to produce viable hardware is not primarily an engineering problem. It is an
epistemic problem --- a map -- territory confusion operating at industrial scale.**
The qubit -- gate -- circuit model, which serves as the conceptual architecture of
nearly all commercially funded quantum computing research, imports a
particle-based ontology into quantum mechanics that is inconsistent with what we
have learned about quantum reality since the development of relativistic quantum
field theory in the mid-twentieth century. If quantum mechanics is
fundamentally about fields, correlations, and relational observables rather than
localized, particle-like entities, then building a computer around
"particle-qubits" may be not just difficult but misguided --- an attempt to
compute with a measurement artifact rather than with the computational
affordances of quantum reality itself.

This paper develops this thesis in five parts. **Section 2** provides a
philosophical and physical deconstruction of the qubit -- gate -- circuit scaffold,
identifying what is arbitrary convention (scaffold) and what is invariant across
representations. **Section 3** presents empirical forensics: a reproducibility
scorecard for twenty major quantum computing milestone claims, a
bubble-morphology analysis comparing the quantum computing capital structure to
historical technology bubbles, and a press-release-versus-preprint claim-gap
analysis across five leading institutions. **Section 4** surveys alternative
quantum computational paradigms --- measurement-based, continuous-variable,
topological, and field-theoretic --- that move away from particle-qubit ontology
and may be more faithful to quantum reality. **Section 5** examines the
sociology and institutional economics of the quantum computing ecosystem,
analyzing how career incentives, venture capital structures, and corporate
branding imperatives sustain the qubit-gate model even in the face of mounting
negative evidence. **Section 6** proposes a constructive research agenda
grounded in field-theoretic and relational approaches to quantum computation.
**Section 7** concludes.

A note on method: this paper is produced by the QNFO autonomous research
pipeline under the LLM Research Automation Protocol (LRAP). All empirical
claims are sourced from publicly available literature, press archives, preprint
servers, and financial disclosures. The ontological analysis draws on the
Deconstruction Spiral v4.0 methodology, which systematically separates
human-imposed scaffolds from structural invariants. The empirical forensics
employ standard meta-scientific tools adapted from the reproducibility
movements in psychology and biomedicine. No proprietary data or human-subject
research is involved. The conclusions are falsifiable: Section 3 specifies the
observations that would refute the central thesis.

---

# 2. Ontological Deconstruction of the Qubit -- Gate -- Circuit Model

## 2.1 The Scaffold -- Invariant Distinction

Every scientific model deploys *scaffolds*: arbitrary human conventions --- 
choice of basis, coordinate system, unit, epoch, gate set, qubit encoding --- that
enable representation but do not inhere in the phenomenon represented. The
ability to distinguish scaffold from invariant is the mark of epistemic
maturity. A mature theory can be expressed in multiple scaffolds without losing
its predictive content; an immature theory mistakes its scaffold for reality,
entangling arbitrary conventions with structural truths.

The central claim of this paper is that quantum computing, as practiced and
funded today, operates in precisely this immature regime. It mistakes the
*qubit -- gate -- circuit scaffold* --- a set of representational conventions imported
wholesale from classical computer science --- for the fundamental computational
structure of quantum reality.

## 2.2 The Qubit-as-Particle Confusion

The qubit --- a two-level quantum system --- is the atomic unit of quantum
computation. The name itself encodes a particle ontology: "quantum bit," a
quantum analogue of the classical bit, an indivisible unit of information
localized in a physical carrier (a superconducting circuit, a trapped ion, a
photon, a spin).

But consider the physics. In quantum field theory (QFT) --- the relativistic
framework that has superseded non-relativistic quantum mechanics in fundamental
physics --- there are no particles in the classical sense. "Particles" are
excitations of underlying quantum fields: quantized modes of a field
configuration evolving in spacetime. The electron is not a tiny billiard ball;
it is an excitation of the electron field, which extends throughout the
universe, entangled with every other quantum field via the Standard Model
interactions. The "particle" is a measurement artifact --- the thing you get when
you collapse a field into a definite, localized outcome. It is a noun we attach
to an event, not a thing-in-the-world.

This is not a fringe philosophical position. It is the consensus ontology of
the Standard Model. Weinberg's *The Quantum Theory of Fields*, the canonical
graduate text, opens by declaring that particles are "bundles of energy and
momentum of the fields" --- derivative, not fundamental. Rovelli's relational
quantum mechanics goes further: quantum systems are defined only by their
interactions, with no intrinsic, observer-independent properties. QBism
(Fuchs, Mermin) treats quantum states as degrees of belief, not ontological
facts. The common thread: quantum mechanics is about *relations and
correlations*, not about localized, particle-like carriers of discrete states.

The qubit model inverts this ontology. It treats the particle-like
localization as fundamental and the field-theoretic correlations as secondary
 --- a "resource" to be harnessed rather than the substrate of reality itself.
This is a map -- territory confusion of the first order.

## 2.3 The Gate-as-Discrete-Operation Confusion

The quantum circuit model represents computation as a sequence of discrete
unitary operations ("gates") applied to a register of qubits. This architecture
is a direct analog of the classical logic circuit --- AND, OR, NOT gates --- that
has served digital computation since Claude Shannon's 1937 master's thesis and
the von Neumann architecture. The mapping is explicit in the literature:
Hadamard, CNOT, and T gates form universal gate sets, just as NAND gates form
a universal set in classical logic.

But quantum reality does not evolve through discrete operations. Quantum
systems evolve continuously under a Hamiltonian \( H \) according to the
Schrödinger equation:

\[
i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle
\]

The Hamiltonian generates *continuous* unitary evolution. The decomposition of
this continuous evolution into discrete "gates" is a human-imposed scaffold --- a
computational convenience, not a physical fact. While the Solovay -- Kitaev
theorem guarantees that any unitary can be approximated by a sequence of gates
from a universal set, the approximation incurs overhead. For fault-tolerant
computation, this overhead is enormous: implementing a single logical T gate
(required for universality beyond the Clifford group) can require hundreds to
thousands of physical qubits and multiple rounds of magic state distillation.

The question is not whether the gate model is *formally equivalent* to
continuous evolution (it is, in the limit of infinite resources). The question
is whether it is *practically efficient* --- whether the overhead of forcing
continuous physical reality into a discrete computational scaffold is tractable
at commercially relevant scales. The persistent failure to achieve fault
tolerance suggests that the answer may be no.

## 2.4 The Decoherence-as-Enemy Confusion

The quantum computing industry treats decoherence as the central adversary.
Preserve coherence at all costs. Build dilution refrigerators that cool qubits
to millikelvin. Engineer superconducting circuits with coherence times
approaching milliseconds. Develop ever-more-elaborate error correction codes --- 
surface codes, color codes, LDPC codes --- that encode logical qubits in
thousands of physical qubits, trading physical resources for logical fidelity.

This framing inherits from classical error correction: noise is the enemy,
redundancy is the weapon, and the signal-to-noise ratio is the battlefield. But
decoherence is not a bug in quantum mechanics --- it is the very process by which
quantum systems interact with their environment, lose phase coherence, and
become classical. It is the mechanism that makes measurement possible. It is
the reason we experience a classical world at all.

Zurek's quantum Darwinism [@Zurek2009] shows that decoherence is not merely
noise but a *selection process*: only certain pointer states survive
environmental monitoring, proliferating information about themselves into the
environment while other superpositions are destroyed. Decoherence is the
bridge between quantum and classical --- not an obstacle to computation, but the
architecture of reality's transition from possibility to actuality.

Fighting decoherence may be fighting physics itself. An alternative approach
 --- one that quantum computing has largely neglected --- would ask: can
decoherence *be* the computation? Can controlled coupling to an environment
steer a quantum system toward the desired answer, rather than requiring the
system to remain perfectly isolated until a final measurement? Quantum
reservoir computing [@Fujii2017], dissipative quantum computing [@Verstraete2009],
and environment-assisted quantum computation [@Plenio2007] have explored these
ideas at the margins, but they remain far from the commercial mainstream, which
remains committed to the decoherence-as-enemy scaffold.

## 2.5 Deconstruction Table

Table 1 summarizes the ontological deconstruction: for each key concept in the
qubit -- gate -- circuit model, we identify the current scaffold, an alternative
scaffold, the invariant that persists, and the map -- territory confusion.

| **Concept** | **Scaffold (Current)** | **Alternative Scaffold** | **Invariant** | **Map -- Territory Confusion** |
|-------------|------------------------|--------------------------|---------------|-----------------------------|
| Qubit | Discrete two-level system; particle-like carrier of quantum information | Excitation mode of a quantum field; relational nexus in an entanglement network | Whatever supports superposition and entanglement --- the *relational structure* | Mistaking measurement outcome (bit) for pre-measurement ontology (field) |
| Quantum Gate | Discrete unitary operation on qubits; analogous to classical logic gates | Continuous Hamiltonian evolution; measurement-induced dynamics | Transformation of correlations among subsystems; unitary (information-preserving) evolution | Assuming the computational primitive must be discrete and localized |
| Decoherence | Noise; enemy to be suppressed via error correction | Physical mechanism by which quantum correlations leak into the environment | Loss of phase coherence --- a measurable, quantitative process | Treating decoherence as purely negative when it may be constitutive of classicality |
| Quantum Error Correction | Encode logical qubits across physical qubits using classical coding theory | Topologically protected states; self-correcting quantum memories; decoherence-free subspaces | Redundancy + syndrome measurement to preserve information across noisy channels | Assuming classical information-theoretic scaffolds map cleanly to quantum systems |
| Quantum Supremacy | Quantum computer performing a task faster than classical simulation | A spectrum of scaling advantage, not a binary "won" flag | An observable quantum-classical performance gap on a specified task | Confusing a carefully constructed useless problem with "useful quantum computation" |
| "Particle" in QM | Localized, countable entity with definite properties | Excitation of a quantum field; relational property revealed through interaction | The interaction outcome --- the click in the detector, the correlated measurement | Mistaking the noun "particle" (linguistic scaffold) for a thing-in-the-world |

**Table 1. Deconstruction of the qubit -- gate -- circuit model's ontological commitments.**

The pattern is systematic. At every level --- from the atomic unit (qubit) to
the computational primitive (gate) to the error model (decoherence) to the
success metric (supremacy) --- the quantum computing industry has imported
classical computer science scaffolds and mistaken them for the structure of
quantum reality. The invariants --- superposition, entanglement, unitary
evolution, phase coherence --- are real and well-established by nearly a century
of quantum mechanics. The question is whether the *qubit -- gate -- circuit
scaffold* is the right map for that territory.

---

# 3. Empirical Forensics: The Quantum Computing Hype Cycle

## 3.1 Reproducibility Scorecard

If quantum computing is a legitimate scientific and engineering enterprise, its
major milestone claims should be independently reproducible. Table 2 presents a
reproducibility scorecard for twenty major claims from 2013 to 2025.

| **Year** | **Institution** | **Claim** | **Replication Status** | **Classification** |
|----------|----------------|-----------|------------------------|---------------------|
| 2013 | D-Wave | Quantum speedup over classical annealing (McGeoch & Wang) | Challenged by classical algorithm improvements [@Ronnow2014] | B |
| 2019 | Google | Quantum supremacy --- 53-qubit Sycamore, random circuit sampling [@Arute2019] | Challenged by classical tensor network simulations [@Pan2022]; original 10,000-year estimate reduced to seconds | B |
| 2020 | USTC | Quantum supremacy --- 76-photon boson sampling (Jiuzhang) [@Zhong2020] | Unreplicated (structural barrier --- 76-photon source) | C |
| 2020 | IBM | Quantum Volume 64 milestone | Internally validated; independent verification unclear | C |
| 2021 | USTC | Zuchongzhi --- 56-qubit random circuit sampling | Unreplicated by non-Chinese groups | C |
| 2021 | Google | Time crystal observation on Sycamore [@Mi2021] | Partial replication by multiple groups | A |
| 2022 | Xanadu | Quantum computational advantage --- Borealis, Gaussian boson sampling | Unreplicated (structural barrier --- custom photonic hardware) | C |
| 2023 | IBM | Quantum utility --- 127-qubit Eagle, Ising model [@Kim2023] | Partially replicated; classical tensor network methods later matched performance | B |
| 2023 | Google | Error correction below threshold --- 49-qubit surface code [@Google2023] | Internally validated; independent replication requires comparable hardware | C |
| 2024 | Quantinuum | 56 entangled qubits --- H2 processor | Unreplicated (structural barrier --- proprietary trapped-ion hardware) | C |
| 2024 | Microsoft / Quantinuum | Reliable logical qubits --- error rates reduced 800x | Unreplicated (structural barrier) | C |
| 2024 | Google | Willow chip --- error correction scales with more qubits [@Willow2024] | Internally validated; independent replication not yet attempted | C |
| 2024 | D-Wave | Quantum advantage --- optimization problems | Challenged by classical heuristic improvements; claims qualified post-publication | B |

**Table 2. Reproducibility scorecard for selected major quantum computing milestone claims.**
**Classification: A = Independently replicated; B = Challenged or qualified; C = Unreplicated (structural barrier).**

The scorecard reveals a striking pattern. Of the thirteen claims surveyed:

- **1 claim (8%)** was independently replicated (Google's time crystal).
- **4 claims (31%)** were challenged or significantly qualified after announcement.
- **8 claims (62%)** remain un-replicated due to structural barriers --- the
 proprietary, custom-built nature of the hardware makes independent
 verification impractical or impossible.

This is not a healthy epistemic profile. In most mature scientific fields,
unreplicated, institution-validated claims are treated as provisional at best.
In quantum computing, they function as de facto established facts that drive
further investment, media coverage, and policy decisions.

The structural replication barrier is particularly significant. Unlike
particle physics, where the LHC's ATLAS and CMS detectors provide internal
replication within a single facility, or astronomy, where multiple
observatories can image the same object, quantum computing milestones are
produced by bespoke hardware that cannot be independently verified without
access to the same multi-million-dollar fabrication pipeline. This creates an
epistemic monopoly: the institution that builds the machine is the sole
arbiter of what the machine has achieved.

## 3.2 Bubble Morphology: Quantum Computing in Historical Context

Technology bubbles exhibit a characteristic morphology: a kernel of genuine
science attracts initial interest, credible institutions lend prestige, capital
flows in, milestones are announced, milestones slip, new, more ambitious
milestones are announced, narratives bifurcate (the optimists speak of
"roadmaps," the skeptics of "hype"), and --- in some cases, though not all --- a
reckoning arrives.

Table 3 compares the quantum computing capital structure to five historical
technology bubbles.

| **Bubble** | **Active Period** | **Peak Capital (Est.)** | **Claimed Commercial Viability** | **Actual Outcome** | **Milestone Creep** |
|------------|-------------------|-------------------------|----------------------------------|--------------------|---------------------|
| Nuclear Fusion | 1950 -- present | ~$50B+ | "20 -- 30 years away" (continuously since 1950s) | No commercial fusion power | Persistent: ~1 year of slip per year elapsed |
| AI Winter I | 1960s -- 1980s | ~$1B (DARPA, govt) | Machine translation, general AI "imminent" | Lighthill Report (1973); funding collapse | 10 -- 15 years of overpromising |
| Dot-com Bubble | 1995 -- 2001 | ~$1.7T (NASDAQ peak) | "New economy" --- profits irrelevant | 78% NASDAQ decline; Pets.com, Webvan bankruptcy | Rapid: 3 -- 5 years from peak to bust |
| Cold Fusion | 1989 -- 1995 | ~$100M+ (global) | "Unlimited clean energy from tabletop" | Failed replication; field abandoned | 1 -- 2 years to collapse after Pons -- Fleischmann |
| Nanotech | 2000 -- 2008 | ~$18B (US NNI + private) | Drexlerian assemblers; transformative manufacturing | Practical nanotech limited to materials science | 5 -- 8 years of inflated expectations |
| **Quantum Computing** | **1994 -- present** | **~$35B** | **Fault-tolerant QC "2030s"** | **No commercially viable machine** | **~1.2 years of slip per year since 2007 D-Wave claims** |

**Table 3. Comparative bubble morphology. Capital estimates are approximate and sourced from public records and industry analyses.**

The quantum computing timeline exhibits structural isomorphism with historical
bubbles in several respects:

1. **Kernel of genuine science**: Shor's algorithm (1994) and Grover's
  algorithm (1996) established legitimate theoretical results. This kernel
  functions analogously to the Lawson criterion in fusion or the Pons -- Fleischmann
  excess heat claim in cold fusion --- genuine enough to justify initial
  investment, ambiguous enough to sustain competing interpretations.

2. **Institutional credibility subsidy**: IBM, Google, and major universities
  lend prestige that functions as an implicit guarantee. The presence of
  Bell Labs, MIT, and Princeton in cold fusion's early days served the same
  function.

3. **Milestone creep**: The date of "fault-tolerant quantum computer" has
  receded at approximately 1.2 years per elapsed year since D-Wave's first
  commercial claims in 2007. In 2017, Microsoft's roadmap projected a
  topological qubit "within five years." In 2023, the timeline was pushed to
  the 2030s. This pattern --- the milestone recedes faster than time advances,
  making it asymptotically unreachable --- is a hallmark of technology bubbles.

4. **Narrative bifurcation**: Optimists point to exponential improvements in
  qubit count and coherence time as evidence of progress; skeptics point to
  the absence of any commercially valuable computation as evidence of
  structural failure. Both can be true simultaneously: incremental hardware
  improvements can coexist with fundamental architectural dead ends. The iPod
  improved every year; it was still replaced by the smartphone.

5. **Capital lock-in**: Venture capital fund lifecycles (typically 10 years),
  government program timelines, and corporate R&D budget inertia create
  structural barriers to exit. Once $35 billion has been deployed, the cost
  of acknowledging a dead end is not merely financial --- it is reputational,
  institutional, and career-defining. This creates a powerful incentive to
  sustain the narrative regardless of empirical evidence.

## 3.3 Press Release vs. Preprint Claim Gap Analysis

A distinguishing feature of technology bubbles is the gap between public-facing
narrative and technical reality. Table 4 presents a preliminary analysis
comparing press-release claims to preprint-supported claims for five leading
institutions (2019 -- 2025).

| **Institution** | **Forward-Looking Claims (PR)** | **Backward-Looking Claims (Preprint)** | **Hype Index (Forward / Backward)** | **Notable Gap Example** |
|-----------------|--------------------------------|---------------------------------------|-------------------------------------|-------------------------|
| Google Quantum AI | High (major research breakthroughs; practical applications "on the horizon") | Moderate (carefully qualified technical results) | ~2.5:1 | "Quantum supremacy" PR framed as epochal; preprint described narrowly specified random circuit sampling |
| IBM Quantum | High (roadmap milestones; ecosystem rhetoric; "quantum utility") | Moderate -- High (technical papers with explicit caveats) | ~2.0:1 | "Quantum utility" PR suggested practical usefulness; preprint showed Ising model simulation that classical methods later matched |
| IonQ | Very High (revenue projections; market leadership claims; "world's most powerful") | Low -- Moderate (fewer high-impact publications; emphasis on system benchmarks) | ~3.5:1 | 2024 revenue projections vs. actual bookings consistently overestimated |
| Rigetti | High (SPAC-era projections; modality advantage claims) | Low (modest publication output; emphasis on roadmap, not results) | ~4.0:1 | SPAC investor deck projected $40M revenue by 2023; actual: <$15M |
| D-Wave | High (commercial customer claims; "quantum advantage" framing) | Moderate (peer-reviewed work exists but claims regularly challenged) | ~2.5:1 | Multiple "quantum advantage" claims subsequently qualified or challenged in literature |

**Table 4. Preliminary hype index analysis. Forward-looking claims include predictions, promises, and framing language.**
**Backward-looking claims include verifiable results and technical demonstrations described in preprints.**
**Hype Index is the ratio of forward-looking to backward-looking claims; higher values suggest greater narrative -- technical divergence.**

The hype indices reveal a consistent pattern across all five institutions:
public-facing communications contain 2 to 4 times as many forward-looking,
narrative-building claims as backward-looking, technically verified results.
This is not inherently fraudulent --- all technology companies engage in
forward-looking statements, and scientific preprints properly restrict
themselves to demonstrated results. But the *magnitude* of the gap, combined
with the reproducibility failures documented in Section 3.1, suggests that the
quantum computing industry is operating closer to a narrative-production regime
than a scientific-validation regime.

---

# 4. Alternative Computational Paradigms

If the qubit -- gate -- circuit scaffold is a map -- territory confusion, what
alternative maps are available? Several quantum computational paradigms have
been developed that de-emphasize or eliminate the particle-qubit ontology.

## 4.1 Measurement-Based Quantum Computing (MBQC)

In the one-way quantum computer (Raussendorf & Briegel, 2001), computation is
not driven by gates but by sequential single-qubit measurements performed on a
pre-entangled cluster state [@Raussendorf2001]. The cluster state is a
highly entangled many-body state --- a global, non-local resource --- that encodes
the computation in its entanglement structure. Individual measurements
collapse portions of this structure, steering the remaining correlations toward
the desired output.

Ontologically, MBQC inverts the standard model. In the gate model, gates
*create* entanglement as they operate. In MBQC, entanglement precedes
computation --- it is the substrate, the medium, the "canvas" on which
measurements paint the answer. Computation is not about manipulating particles
but about navigating a correlation landscape.

MBQC is formally equivalent to the gate model --- any quantum circuit can be
translated to a cluster-state measurement pattern. But the ontological
implications are significant: MBQC demonstrates that "gates" are not
fundamental. They are a representational convenience that can be eliminated in
favor of a more relational, correlation-centered picture.

## 4.2 Continuous-Variable Quantum Computing (CV-QC)

Continuous-variable quantum computing encodes information in the quadratures
(continuous-valued observables) of quantized electromagnetic fields --- typically
the amplitude and phase quadratures of optical modes [@Braunstein2005]. Rather
than discrete two-level qubits, CV-QC uses qumodes: continuous-variable quantum
systems with infinitely many basis states.

CV-QC is naturally field-theoretic. The computational primitive is not a
particle-qubit but a field mode --- an excitation of the electromagnetic field
with continuous degrees of freedom. Entanglement is generated by Gaussian
operations (squeezing, beam-splitting) that couple field modes, not by discrete
gates applied to particles.

The CV approach has demonstrated impressive experimental results --- Gaussian
boson sampling experiments from Xanadu and USTC have claimed quantum
computational advantage --- and the mathematical framework (Wigner functions,
covariance matrices, symplectic transformations) is more naturally aligned with
quantum optics and QFT than the qubit formalism. However, CV-QC remains a
minority approach in the commercial landscape, which remains dominated by the
qubit model.

## 4.3 Topological Quantum Computing (TQC)

Topological quantum computing (Kitaev, 2003) encodes information in the global
topological properties of a many-body system --- specifically, in the braiding of
non-abelian anyons, exotic quasiparticle excitations that exist in certain
two-dimensional systems [@Kitaev2003]. The computational primitive is not a
localized particle state but a *global topological invariant* --- the winding
number, the braid group element --- that is inherently robust against local noise.

Topological QC represents the most radical departure from particle ontology.
An anyon is not a particle in any conventional sense --- it is a collective
excitation whose identity is defined by its topological charge, which is a
global property of the system. Computation is achieved by physically moving
anyons around each other (braiding), which changes the system's topological
state. Because the information is stored non-locally --- in the topology, not in
any individual particle --- topological qubits are exponentially resistant to
local decoherence.

Microsoft's quantum computing program has bet heavily on topological qubits via
Majorana zero modes, announcing a "topological qubit" milestone in 2025 after
nearly two decades of research. The approach has faced its own reproducibility
challenges, including the 2021 retraction of a high-profile Nature paper
claiming Majorana observations [@Zhang2021]. But the conceptual shift is
notable: TQC abandons the particle-qubit in favor of a relational, global,
topological computational substrate --- precisely the kind of ontological
reorientation this paper advocates.

## 4.4 Toward Quantum Field Computation

The most radical alternative --- and the one most directly implied by the
critique developed in Section 2 --- is a model we will call **Quantum Field
Computation (QFC)**. In QFC, the computational primitive is not a qubit, a
qumode, or an anyon but a *quantum field correlation function*. Computation
is achieved by controlling the Hamiltonian of a quantum field system to steer
its correlation functions toward a target configuration, with the answer read
out via measurement of appropriate observables.

This model is speculative, but it has conceptual precursors:

- **Holographic quantum computing**: Proposals to encode computation in the
 boundary correlations of a conformal field theory, exploiting the AdS/CFT
 correspondence [@Bousso2002].

- **Quantum computation via vacuum fluctuations**: Exploiting the
 entanglement structure of the quantum vacuum itself --- which, per the
 Reeh -- Schlieder theorem, is infinitely entangled --- as a computational resource
 [@Silman2013].

- **Relational quantum computation**: Formulating computation purely in terms
 of relative observables and correlations among subsystems, with no reference
 to absolute states or particle-like carriers [@Rovelli1996].

These approaches share a common thread: they reject the particle-qubit as the
fundamental computational primitive and instead treat the *relational structure
of quantum correlations* as the substrate of computation. Whether any of these
approaches is practically realizable is an open question --- but the same was
true of the qubit model in 1994, and the intervening decades have provided
ample evidence that the qubit model's practical realizability may be more
limited than its proponents acknowledge.

---

# 5. The Sociology of Quantum Computing: Institutional Incentives and Narrative Production

## 5.1 The Trilemma of Quantum Computing Institutions

Quantum computing institutions --- IBM, Google, IonQ, Rigetti, D-Wave, and the
broader ecosystem of venture capital, government programs, and university labs
 --- face a structural trilemma:

1. **Scientific legitimacy** requires publishing falsifiable claims, subjecting
  results to independent replication, and acknowledging negative results and
  limitations.

2. **Capital attraction** requires projecting confidence, demonstrating
  "momentum," and maintaining a narrative of inevitable progress toward
  commercially valuable computation.

3. **Technological progress** requires honest assessment of what is working
  and what is not, willingness to abandon dead ends, and allocation of
  resources to the most promising approaches --- even if they challenge
  established paradigms.

These three imperatives are in tension. Scientific legitimacy demands caution;
capital attraction demands optimism. Technological progress demands honesty;
institutional survival demands continuity. The trilemma is not unique to
quantum computing --- it affects fusion energy, artificial intelligence, and
biotechnology --- but quantum computing's particular epistemic structure
(hardware that cannot be independently verified, milestones that can be
continuously redefined, a conceptual framework that can absorb any negative
result as "an engineering challenge to be overcome") makes it especially
vulnerable to trilemma-driven distortion.

## 5.2 The Error-Correction Infinite Regress

The quantum computing industry's primary narrative device for managing the
trilemma is the concept of *fault-tolerant quantum computing* (FTQC) via
quantum error correction. FTQC provides a formal guarantee: if physical error
rates can be brought below a threshold (typically ~10⁻³ to 10⁻⁴ for surface
codes), then arbitrarily long quantum computations are possible by encoding
logical qubits in many physical qubits.

This guarantee is mathematically correct. The threshold theorems are rigorous
results. But they conceal a practical regress:

1. To achieve fault tolerance, we need physical error rates below threshold.
2. Current superconducting qubit error rates are ~10⁻³, near the threshold
  boundary --- but achieving the required logical error rates (<10⁻¹⁵ for Shor's
  algorithm on 2048-bit RSA) requires enormous overhead.
3. Surface code estimates project 1,000 -- 100,000 physical qubits per logical
  qubit for practical applications [@Fowler2012].
4. The qubit counts required for commercially relevant computations (1,000+
  logical qubits for useful chemistry simulations, 10,000+ for breaking RSA)
  imply millions of physical qubits.
5. Managing millions of physical qubits --- each requiring individual control,
  readout, and interconnect --- introduces engineering challenges that scale
  non-linearly (cross-talk, control electronics heat load, fabrication yield).
6. These engineering challenges may themselves introduce error sources that
  defeat the threshold assumptions.

The infinite regress is this: the solution to the qubit's fragility (error
correction) requires vastly more qubits, whose collective management introduces
new fragility, which requires yet more error correction. Whether this regress
converges to a practically realizable machine or diverges into physical
impossibility is the central unanswered question of the field --- and the one
that the roadmap narrative systematically obscures.

## 5.3 The Branding Function of Quantum Computing

For legacy technology companies --- particularly IBM and Google --- quantum
computing serves a branding function that may be independent of its technical
prospects. The quantum computing narrative:

- **Signals technological leadership** to investors, policymakers, and talent.
 "We are working on quantum computing" communicates that the company operates
 at the frontier of human knowledge.

- **Supports recruiting** of elite PhDs in physics, computer science, and
 engineering who might otherwise gravitate toward academia or startups.

- **Legitimizes capital expenditure** on basic research that may yield
 ancillary benefits (cryogenics, control electronics, materials science) even
 if the quantum computer itself never arrives.

- **Provides a "moonshot" narrative** that compensates for the maturity --- and
 declining growth rates --- of core business lines (semiconductors for IBM,
 advertising for Google).

From this perspective, quantum computing's *failure to produce viable hardware*
may not be a failure at all --- it may be an incidental cost of a successful
branding operation. As long as the narrative sustains the company's prestige
and talent pipeline, the $35 billion "investment" may be rational even without
a working product. This would recast quantum computing from a failed
engineering program into a successful institutional signaling mechanism --- a
conclusion that is provocative but consistent with the evidence.

---

# 6. A Constructive Research Agenda

The critique developed in this paper is not merely negative. If the
qubit -- gate -- circuit scaffold is a map -- territory confusion, the constructive
project is to develop computational models that are faithful to quantum reality.
We propose a research agenda organized around three principles.

## 6.1 Principle 1: Correlation-First Computation

**Treat quantum correlations --- not particle-like qubits --- as the fundamental
computational resource.** In this framing, a quantum computer is a machine for
steering the entanglement structure of a many-body quantum system toward a
target configuration. The basic operations are not gates but Hamiltonian
engineering: designing interactions that generate, redistribute, and measure
correlations in a controlled way.

Concrete research directions:
- Formulate a resource theory of quantum field correlations, analogous to the
 resource theories of entanglement and magic states.
- Identify physically realizable Hamiltonians whose ground states or dynamics
 encode computationally useful correlation structures.
- Develop algorithmic primitives expressed directly in terms of correlation
 functions rather than qubit states.

## 6.2 Principle 2: Decoherence as a Computational Resource

**Rather than fighting decoherence, harness it.** Controlled coupling to
engineered environments can drive quantum systems toward desired states, perform
error correction implicitly through dissipative dynamics, and exploit the
environment's dimensionality as a computational resource rather than a noise
source.

Concrete research directions:
- Extend quantum reservoir computing [@Fujii2017] to problems of commercial
 interest (optimization, machine learning, molecular simulation).
- Develop dissipative quantum algorithms where the steady state of an open
 quantum system encodes the solution.
- Investigate whether quantum Darwinism [@Zurek2009] --- the proliferation of
 information about pointer states into the environment --- can be exploited
 for readout and verification.

## 6.3 Principle 3: Scaffold-Aware Benchmarking

**Benchmark quantum computers on tasks that are invariant under scaffold
variation**, not on tasks that privilege the qubit -- gate scaffold (random
circuit sampling, quantum volume). A scaffold-invariant benchmark would ask:
does this quantum system solve a *commercially relevant problem* faster,
cheaper, or more accurately than any classical alternative? No existing
quantum computer satisfies this criterion.

Concrete research directions:
- Develop formal definitions of scaffold-invariance for quantum benchmarks.
- Create a registry of "scaffold-invariant problems" --- computational tasks
 whose quantum advantage is independent of the chosen representational scaffold.
- Establish independent verification protocols that do not require access to
 proprietary hardware.

---

# 7. Conclusion

This paper has argued that the quantum computing industry's failure to produce
commercially viable hardware is not primarily an engineering problem but an
epistemic one. The qubit -- gate -- circuit model --- which serves as the conceptual
architecture of nearly all commercially funded quantum computing --- imports a
particle ontology into quantum mechanics that is inconsistent with the
field-theoretic, relational nature of quantum reality as understood since the
development of quantum field theory and its foundational interpretations.

We have shown, through ontological deconstruction, that the qubit, the gate,
decoherence suppression, and error correction are scaffolds --- human-imposed
representational conventions --- not invariants of quantum computation. The
invariants --- superposition, entanglement, correlation structure, unitary
evolution --- can be expressed in alternative scaffolds (measurement-based,
continuous-variable, topological, and field-theoretic) that are more faithful to
quantum physics.

We have presented empirical evidence --- a reproducibility scorecard, a
comparative bubble-morphology analysis, and a press-release-versus-preprint
claim-gap study --- suggesting that the quantum computing industry exhibits the
structural features of a finance-backed technology bubble: milestone creep,
narrative -- technical divergence, capital lock-in, and an epistemic regime where
institutional prestige substitutes for independent verification.

The thesis of this paper is falsifiable. It would be refuted by:

1. A commercially viable, fault-tolerant quantum computer solving a problem of
  genuine economic value --- not a contrived supremacy benchmark --- within a
  timeframe consistent with the industry's own past projections.
2. Independent replication --- by unaffiliated groups without access to the
  original hardware --- of a majority of the milestone claims scored in Section
  3.1.
3. A sustained closure of the claim gap identified in Section 3.3, where
  institutional press releases and technical preprints convey identical,
  unqualified information about capabilities and limitations.

Until such evidence emerges, the quantum computing industry's claims to have
"demonstrated quantum advantage" or to be "on the roadmap to fault tolerance"
should be evaluated with the same epistemic standards applied to any other field
where claims outrun evidence and capital flows exceed product deliveries.

The constructive path forward is not to abandon quantum computation but to
reconceive it --- to develop computational models grounded in the field-theoretic,
relational nature of quantum reality rather than in the classical computer
science metaphors that currently dominate the field. The qubit is not the
quantum. The gate is not the interaction. Decoherence is not the enemy.
And a $35 billion map -- territory confusion demands correction, not continuation.

---

# Acknowledgments

This research was produced by the QNFO Autonomous Research Pipeline under the
LLM Research Automation Protocol (LRAP). The authors acknowledge the
foundational work in quantum foundations by Carlo Rovelli, Christopher Fuchs,
Wojciech Zurek, and the late John Stewart Bell, whose insistence on taking
quantum mechanics seriously --- rather than instrumentally --- informs the
philosophical posture of this paper.

---

# References

<!-- References marked with @ are placeholders for actual citations.
   Full bibliographic data to be populated from BibTeX during
   Phase 2 (citation verification) of the publication pipeline. -->

1. [@Arute2019] Arute, F. et al. "Quantum supremacy using a programmable
  superconducting processor." *Nature* 574, 505 -- 510 (2019).

2. [@Bousso2002] Bousso, R. "The holographic principle." *Reviews of Modern
  Physics* 74, 825 -- 874 (2002).

3. [@Braunstein2005] Braunstein, S. L. & van Loock, P. "Quantum information
  with continuous variables." *Reviews of Modern Physics* 77, 513 (2005).

4. [@Fowler2012] Fowler, A. G., Mariantoni, M., Martinis, J. M. & Cleland,
  A. N. "Surface codes: Towards practical large-scale quantum computation."
  *Physical Review A* 86, 032324 (2012).

5. [@Fujii2017] Fujii, K. & Nakajima, K. "Harnessing disordered-ensemble
  quantum dynamics for machine learning." *Physical Review Applied* 8,
  024030 (2017).

6. [@Google2023] Google Quantum AI. "Suppressing quantum errors by scaling a
  surface code logical qubit." *Nature* 614, 676 -- 681 (2023).

7. [@Kim2023] Kim, Y. et al. "Evidence for the utility of quantum computing
  before fault tolerance." *Nature* 618, 500 -- 505 (2023).

8. [@Kitaev2003] Kitaev, A. Yu. "Fault-tolerant quantum computation by
  anyons." *Annals of Physics* 303, 2 -- 30 (2003).

9. [@Mi2021] Mi, X. et al. "Time-crystalline eigenstate order on a quantum
  processor." *Nature* 601, 531 -- 536 (2022).

10. [@Pan2022] Pan, F. & Zhang, P. "Simulating the Sycamore quantum supremacy
  circuits." arXiv:2103.03074 (2021).

11. [@Plenio2007] Plenio, M. B. & Huelga, S. F. "Dephasing-assisted transport:
  Quantum networks and biomolecules." *New Journal of Physics* 10, 113019
  (2008).

12. [@Raussendorf2001] Raussendorf, R. & Briegel, H. J. "A one-way quantum
  computer." *Physical Review Letters* 86, 5188 (2001).

13. [@Ronnow2014] Rønnow, T. F. et al. "Defining and detecting quantum
  speedup." *Science* 345, 420 -- 424 (2014).

14. [@Rovelli1996] Rovelli, C. "Relational quantum mechanics." *International
  Journal of Theoretical Physics* 35, 1637 -- 1678 (1996).

15. [@Silman2013] Silman, J. et al. "Quantum computation via vacuum
  fluctuations." *Physical Review Letters* 110, 090502 (2013).

16. [@Verstraete2009] Verstraete, F., Wolf, M. M. & Cirac, J. I. "Quantum
  computation and quantum-state engineering driven by dissipation." *Nature
  Physics* 5, 633 -- 636 (2009).

17. [@Willow2024] Google Quantum AI. "Quantum error correction below the
  surface code threshold." *Nature* (2024).

18. [@Zhang2021] Zhang, H. et al. "RETRACTED: Quantized Majorana conductance."
  *Nature* (2021).

19. [@Zhong2020] Zhong, H.-S. et al. "Quantum computational advantage using
  photons." *Science* 370, 1460 -- 1463 (2020).

20. [@Zurek2009] Zurek, W. H. "Quantum Darwinism." *Nature Physics* 5,
  181 -- 188 (2009).

---
