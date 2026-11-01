# Grounding block - source: rem-3b4c2f4d-8c18-4128-aa53-ffc31e1ed6e8

## Research idea

Correct the published paper 'paper-beyond-the-qubit' for erratum pl-paper-beyond-the-qubit-2.1.0-0: 'The existence of non-abelian anyons --- the type needed for universal quantum computation --- was only experimentally confirmed in 2020 in fractional quantum Hall systems.' (Section 3.3)
Also: pl-paper-beyond-the-qubit-2.1.0-1: 'Coherent Ising machines [@Marandi2014] have demonstrated solving combinatorial optimization problems orders of magnitude faster than classical heuristics for certain problem classes.' (Section 5.2)

## Existing paper under revision (remediation only)

# Beyond the Qubit: Constructive Paradigms for Post-Particle Computation

## Abstract

If "The Qubit Delusion" diagnosed the epistemic failure at the heart of quantum computing --- the projection of particle ontology onto a relational, field-theoretic reality --- then this companion paper asks the constructive question: what comes next? We begin with an ontological stripping: what does quantum mechanics actually demand of a computational substrate, once all anthropocentric and classical baggage is removed? From this foundation we survey alternative computational paradigms (measurement-based, continuous-variable, topological, field-theoretic, analog) that are more faithful to quantum reality than the qubit-gate-circuit scaffold. We then assess which of these are commercially manufacturable --- not in theory, but under the actual constraints of materials, thermodynamics, and industrial economics. [...]

# 1. The Question Behind the Critique

"The Qubit Delusion" advanced a diagnosis: the quantum computing industry's
failure to deliver commercially viable machines is not primarily an engineering
problem but an epistemic one. The qubit-gate-circuit model imports a particle
ontology into quantum mechanics --- as if qubits were little quantum billiard
balls that we poke with gates --- and this ontology is inconsistent with quantum
field theory, relational quantum mechanics, and the physics of continuous,
correlated quantum systems.

But diagnosis without prescription is incomplete. If the qubit is a scaffold,
not an invariant, then what IS the invariant? If the gate-circuit model is a
map-territory confusion, what does the territory actually look like? And ---
most practically --- if $35 billion and two decades of global effort have
produced zero commercially viable quantum computers under the incumbent
paradigm, are there alternative architectures that might actually deliver
commercially useful computation?

This paper addresses four questions:

1. **What is "quantum," really?** Stripped of particle ontology, measurement
 metaphysics, and anthropocentric baggage, what does the quantum formalism
 actually demand of a computational substrate?

2. **What is the solution space?** Which alternative computational paradigms ---
 measurement-based, continuous-variable, topological, field-theoretic, analog
 --- are faithful to quantum reality, and how mature are they?

3. **What can actually be built?** Of these alternatives, which are commercially
 manufacturable under real engineering, thermodynamic, and economic
 constraints?

4. **Is "quantum computing" even the right frame?** Or does the deeper lesson ---
 that computation IS a physical process, and the substrate determines what
 can be computed efficiently --- point toward architectures where the physics
 does the computing directly, without being forced into a discrete symbolic
 scaffold?

# 2. What Is "Quantum," Really? An Ontological Stripping

Before we can ask what a "quantum computer" should look like, we must ask what
"quantum" actually means --- not as a set of mathematical tools, but as a
statement about what the world is made of and how it behaves.

## 2.1 The Textbook Picture and Its Projections

Most physicists learn quantum mechanics from textbooks that present it as a
puzzle: "particles behave like waves, waves behave like particles, measurement
collapses the wavefunction, and nobody knows why." This framing --- which Feynman
called the "central mystery" --- is pedagogically useful but ontologically
misleading. It takes classical categories (particle, wave, measurement,
observer) as primitive and then expresses perplexity when quantum systems fail
to conform to them.

The projection runs deep. We talk about "an electron" as if it were a tiny
billiard ball with a position and momentum that we happen to be unable to
measure simultaneously. We talk about "measurement" as if it were a passive
observation that reveals pre-existing properties. We talk about "the observer"
as if consciousness played a special role in physics. None of these are
demanded by the formalism. All of them are classical intuitions we project onto
a reality that operates differently.

## 2.2 The Minimal Ontological Commitments of Quantum Mechanics

If we strip away all classical projections --- particles, waves, measurement as
revelation, observers as special --- what remains? What does the quantum
formalism actually commit us to, ontologically?

The answer, distilled from seventy years of foundational work (relational
quantum mechanics [@Rovelli1996], QBism [@Fuchs2014], consistent histories
[@Griffiths1984], and the decoherence program [@Zurek2003]), is remarkably
sparse:

**1. States are vectors in a complex Hilbert space.** A quantum system is
described by a ray in a complex projective Hilbert space. This is the minimal
mathematical structure needed to encode superposition, interference, and the
Born rule. Nothing in this structure requires "particles," "waves," or
"observers." It requires only a linear space with an inner product.

**2. Composite systems live in the tensor product, not the Cartesian product.**
The state space of a composite system is NOT the set of all pairs of states of
its components. It is a strictly larger space --- the tensor product --- that
contains entangled states that cannot be factored. This is the formal statement
of non-separability: the whole is not the sum of its parts.

**3. Properties are contextual.** The Kochen-Specker theorem [@Kochen1967]
proves that quantum systems cannot have pre-existing values for all observables
simultaneously. A "property" of a quantum system is not an attribute of the
system alone but of the system-in-measurement-context. Properties are
relational, not intrinsic. This is not a limitation of our knowledge --- it is a
structural fact about quantum reality.

**4. Evolution is unitary (when the system is isolated).** Isolated quantum
systems evolve deterministically according to the Schrödinger equation. The
"measurement problem" --- the apparent conflict between unitary evolution and
wavefunction collapse --- is not a problem of physics but of insisting that
measurement is something other than physical interaction between systems.

**5. Probabilities are Born-rule. Not ignorance probabilities.** The
probabilities that appear in quantum mechanics are not epistemic (reflecting
our ignorance of pre-existing values) but structural (reflecting the
geometry of the Hilbert space). An electron in a superposition of spin-up and
spin-down is not "really" spin-up or spin-down with us not knowing which. It
is in a state that is genuinely neither, and the Born rule gives the
probability of finding it in one or the other upon interaction with a
measurement apparatus.

## 2.3 What Is NOT There: The Absent Ontology

Equally revealing is what these minimal commitments do NOT include:

- **No particles.** Nothing in the formalism requires that quantum systems be
 localized in space, have trajectories, or persist as identifiable individuals.
 Quantum field theory, the more fundamental theory, explicitly rejects particle
 ontology: particles are excitations of fields, not fundamental entities.

- **No classical measurement apparatus.** The "Heisenberg cut" --- the boundary
 between quantum system and classical measuring device --- is a pragmatic
 convenience, not an ontological boundary. Every measuring device is itself a
 quantum system. The appearance of classicality emerges from decoherence: the
 irreversible leakage of phase information into environmental degrees of
 freedom [@Zurek2003].

- **No observers.** Consciousness plays no role in the formalism. The
 "observer" is simply a physical system that becomes correlated with the
 measured system through interaction. QBism [@Fuchs2014] correctly identifies
 that probabilities are agent-relative --- they encode an agent's expectations
 about future experiences --- but this does not make consciousness
 ontologically special. It makes probability theory agent-relative, which it
 already was.

- **No "collapse."** The projection postulate --- that measurement "collapses"
 the wavefunction --- is not a dynamical law but a bookkeeping rule for updating
 probabilities conditional on new information. In decoherence-based
 interpretations, collapse is replaced by the physical process of
 environmental monitoring: the system becomes entangled with its environment,
 and the reduced density matrix of the system alone becomes effectively
 diagonal in the pointer basis. No collapse required [@Schlosshauer2007].

## 2.4 The Relational Core: Quantum Mechanics as a Theory of Correlations

The positive ontological content that survives stripping is this: **quantum
mechanics is a theory of correlations --- specifically, of the structure and
dynamics of entanglement in composite quantum systems.**

Consider what the quantum formalism is actually good at predicting:
correlation statistics. The Bell inequalities, the CHSH game, quantum
teleportation, superdense coding, quantum key distribution --- all of these
are fundamentally about correlations between measurement outcomes on
spatially separated subsystems. The "quantumness" lies not in the individual
systems but in the correlation structure that connects them.

This is the insight of relational quantum mechanics [@Rovelli1996]: the
properties of a quantum system are not intrinsic but are relative to another
system with which it interacts. There are no "states of the electron." There
are only "states of the electron relative to the measurement apparatus." This
is not idealism or anti-realism --- it is a structural claim about what kinds
of facts quantum mechanics can encode.

From this perspective, the qubit-as-particle picture is not just empirically
inadequate but categorically wrong. It treats quantum systems as objects with
intrinsic properties that gates manipulate, when the actual quantum ontology
is one of relational properties that emerge only through interaction. **The
computational primitive is not the qubit but the correlation.**

## 2.5 The Physical Meaning of "Quantum"

So what does "quantum" actually mean, physically? Three irreducible features:

**Discreteness of interaction.** The word "quantum" comes from the Latin
*quantus* ("how much") and refers to the fact that certain physical quantities
 --- energy levels in bound systems, angular momentum, charge --- come in discrete
units. This is not a statement about the nature of reality being "granular."
It is a statement about the spectrum of certain operators being discrete, which
follows from boundary conditions on the Schrödinger equation. Discreteness is
an emergent property of confined systems, not a fundamental axiom.

**Superposition and interference.** The linearity of the Schrödinger equation
means that if state A is possible and state B is possible, then any complex
linear combination is also possible. This is the source of interference effects
 --- the double-slit experiment, the Aharonov-Bohm effect --- and it has no
classical analog. Superposition is not a statement about a particle "being in
two places at once." It is a statement about the vector space structure of
quantum states.

**Entanglement.** The tensor product structure of composite systems means that
the state of a composite system is not determined by the states of its
components. This is the most radical departure from classical physics and the
one most directly relevant to computation. Entanglement is what makes quantum
systems computationally interesting: the dimension of the state space grows
exponentially with the number of components, but this exponential space is not
freely accessible --- it is structured by the geometry of entanglement.

These three features --- discreteness, superposition, entanglement --- are the
invariants. Everything else --- qubits, gates, circuits, measurements, error
correction --- is scaffold.

# 3. The Solution Space: Computational Paradigms Faithful to Quantum Reality

If the qubit-gate-circuit scaffold is a map-territory confusion, what are the
alternatives? What would a computational paradigm faithful to the ontological
commitments of quantum mechanics actually look like? We survey five
paradigms, ordered from most to least mature.

## 3.1 Measurement-Based Quantum Computing (MBQC)

**Core idea:** The computation IS the entanglement structure. Prepare a highly
entangled resource state (a cluster state or graph state), then perform a
sequence of single-qubit measurements whose outcomes --- and the choice of
measurement bases, adapted to prior outcomes --- implement the computation.
There are no gates. The "algorithm" is encoded in the pattern of measurements
on the entangled substrate.

**Ontological fidelity:** High. In MBQC, entanglement is not a side effect or a
resource to be managed --- it IS the computational primitive. The cluster state
is a single, massively entangled state that encodes the entire computation.
Gates are replaced by measurement patterns, which are inherently contextual
(the basis choice at each step depends on prior outcomes). This aligns with
the relational picture: computation proceeds through a sequence of contextual
interactions (measurements) rather than through the manipulation of
intrinsically-valued objects (qubits).

**Maturity:** MBQC is theoretically well-understood. Raussendorf and Briegel
proved in 2001 that cluster-state MBQC is computationally universal
[@Raussendorf2001]. The framework has been extended to continuous-variable
systems [@Menicucci2006] and to fault-tolerant architectures. Experimental
demonstrations exist at small scale (a few qubits in photonic systems).

**Limitations:** MBQC requires preparing large-scale entangled resource states,
which is itself a major experimental challenge. The resource state must be
prepared with high fidelity before computation begins, and any errors in the
state propagate through the measurement sequence. However, topological cluster
states --- which encode the resource state in a topologically protected subspace
 --- offer a path to fault tolerance that may be more natural than surface-code
error correction in the circuit model.

**Commercial traction:** PsiQuantum's "fusion-based" quantum computing
architecture is essentially an MBQC implementation using photonic qubits,
where small entangled states are probabilistically fused into larger cluster
states. This represents the most commercially advanced MBQC effort.

## 3.2 Continuous-Variable Quantum Computing (CV-QC)

**Core idea:** Replace discrete qubits --- two-level quantum systems --- with
continuous quantum variables: the quadrature amplitudes of the electromagnetic
field (position and momentum analogs). Qumodes --- the CV analog of qubits ---
live in an infinite-dimensional Hilbert space, and computation proceeds through
Gaussian operations (squeezing, displacement, beam-splitting) supplemented by
non-Gaussian operations for universality.

**Ontological fidelity:** Very high. CV-QC treats the computational substrate
as genuinely continuous --- a quantum field --- rather than discretizing it into
artificial two-level systems. This is more faithful to the field-theoretic
nature of quantum electrodynamics, where the fundamental entities are
continuous field modes, not particles. The infinite-dimensional Hilbert space
of a qumode encodes information in the continuous amplitude and phase of a
field quadrature, which is closer to how quantum information is actually
carried in physical systems (photons, phonons, collective excitations).

**Maturity:** CV-QC is theoretically well-developed but experimentally less
mature than discrete-variable (qubit) approaches. Gottesman-Kitaev-Preskill
(GKP) states provide a path to fault-tolerant CV computation by encoding
discrete logical qubits in the continuous Hilbert space of a harmonic
oscillator [@Gottesman2001]. CV cluster states extend MBQC to the CV domain.
Experimental demonstrations of CV entanglement, squeezing, and small-scale
computation exist in optical systems.

**Commercial traction:** Xanadu is the leading commercial CV-QC company,
developing photonic quantum processors based on squeezed-light qumodes.
Their "Borealis" processor demonstrated Gaussian boson sampling at a scale
that (arguably) exceeds classical simulability. The photonic platform is
attractive because it operates at room temperature, integrates with existing
fiber-optic infrastructure, and avoids the cryogenic requirements of
superconducting qubits.

**The CV advantage:** Because CV systems encode information in continuous
degrees of freedom, they can represent certain classes of functions --- Gaussian
states and operations --- with exponentially fewer resources than discrete
systems. This suggests that for problems with continuous structure
(optimization over continuous variables, simulation of bosonic systems,
machine learning with continuous data), CV architectures may have a natural
advantage over qubit-based ones.

## 3.3 Topological Quantum Computing (TQC)

**Core idea:** Encode quantum information in globally-defined, topologically
protected degrees of freedom --- specifically, the fusion and braiding
properties of anyons (quasiparticle excitations in two-dimensional systems
that are neither bosons nor fermions). Computation is performed by braiding
anyons around each other; the result depends only on the topological class
of the braid, not on the detailed trajectory, providing intrinsic protection
against local noise.

**Ontological fidelity:** High, in a specific sense. TQC recognizes that
quantum information is fundamentally about global, relational structure ---
the topology of particle trajectories --- rather than about local states of
individual particles. The "qubit" in TQC is not a physical two-level system
but a topological degree of freedom that is distributed across multiple
anyons. The information is stored non-locally, which is why it is protected
from local perturbations.

This aligns with the relational picture: the computational DOF are
relationships (braiding patterns), not objects (individual anyons). The
topological protection arises precisely because the information is encoded
in the global structure, not in any local degree of freedom.

**Maturity:** TQC is theoretically elegant but experimentally extremely
challenging. The existence of non-abelian anyons --- the type needed for
universal quantum computation --- was only experimentally confirmed in 2020
in fractional quantum Hall systems. Microsoft has invested heavily in
Majorana zero modes (a type of non-abelian anyon) in semiconductor-superconductor
heterostructures, but the experimental evidence has been contested and retracted
[@Frolov2021]. As of 2026, topological qubits have not been demonstrated at
a level that would enable computation.

**The universality challenge:** The simplest non-abelian anyons (Ising anyons)
support only a restricted set of gates (Clifford group) and require
non-topological operations (magic state distillation) for universality. More
exotic anyons (Fibonacci anyons) are universal but have not been experimentally
realized. This means TQC may face the same error-correction overhead problem as
the circuit model, just at a different level.

## 3.4 Quantum Field Computation: The Speculative Frontier

**Core idea:** If quantum field theory is the fundamental theory --- particles
are excitations of fields, not fundamental entities --- then the ultimate
computational substrate is not a collection of qubits but a quantum field.
Computation would proceed by engineering the Hamiltonian of a quantum field
such that its dynamics (ground state, time evolution, correlation functions)
encode the solution to a computational problem.

**What this might look like:** A "quantum field computer" would be an analog
device: a physical system --- perhaps an array of coupled superconducting
resonators, a cold atom gas in an optical lattice, or a engineered
metamaterial --- whose quantum field theory is designed so that measuring its
correlation functions yields the answer to a hard computational problem.
The "programming" would consist of shaping the Hamiltonian --- the interactions,
couplings, and boundary conditions --- rather than specifying a sequence of
gates.

**Ontological fidelity:** Maximal. This is the paradigm most faithful to
quantum field theory, since it treats the field --- rather than its particle
excitations --- as fundamental. The computational resource is the continuum of
degrees of freedom of the field, and the computation is encoded in the
field's correlation structure.

**Maturity:** Essentially zero. This is a speculative research direction. Some
elements exist: quantum simulation (Feynman's original vision) can be seen as
a primitive form of field computation, where one quantum system (the simulator)
is designed to have the same Hamiltonian as another (the target system). But
the idea of programming a quantum field theory as a general-purpose computer
is unexplored.

**Why it might matter:** If the qubit is a scaffold and the field is the
reality, then the most natural computational primitive is not the two-level
system but the continuum field mode. The infinite-dimensional Hilbert space
of a quantum field encodes vastly more information than a collection of
qubits, and --- crucially --- it encodes it in a way that is physically natural,
avoiding the artificial discretization that creates the error-correction
overhead of the circuit model.

## 3.5 Analog Quantum Computing and Quantum Simulation

**Core idea:** Instead of building a universal digital quantum computer, build
a special-purpose analog device whose natural dynamics solve a specific class
of problems. Quantum simulation --- using one controllable quantum system to
simulate another --- is the paradigm case. Quantum annealing (D-Wave's approach)
is another: encode the problem in the energy landscape of a quantum system and
let the system's natural relaxation dynamics find the ground state.

**Ontological fidelity:** Mixed. Analog approaches are faithful to the
continuous, dynamical nature of quantum systems --- they let the physics do the
computing rather than imposing a discrete symbolic scaffold. But they typically
encode problems in a classical cost function (e.g., Ising Hamiltonian for
optimization), which is itself a scaffold.

**Maturity:** D-Wave has deployed quantum annealers with thousands of qubits,
and quantum simulators (cold atoms in optical lattices, trapped ions, Rydberg
atom arrays) have simulated quantum many-body systems beyond the reach of
classical computation. However, no analog quantum device has yet demonstrated
a commercially relevant speedup over classical alternatives for a problem of
practical interest.

**The fundamental limitation:** Analog quantum computers are not universal.
Each device is designed for a specific class of problems, and the mapping
between problem and device is itself a scaffold. For optimization problems,
the question is whether quantum annealing offers an asymptotic advantage over
classical heuristic solvers --- and the evidence to date suggests it does not
[@Ronnow2014; @Denchev2016].

# 4. What Can Actually Be Built? Commercially Manufacturable Paths

Theoretical fidelity to quantum ontology is necessary but not sufficient.
A computational paradigm must also be physically realizable, scalable, and
 --- for commercial viability --- manufacturable under industrial constraints.
We assess the leading physical platforms against these criteria.

## 4.1 Photonic Quantum Computing

**Platform:** Photons as qubits/qumodes; linear optical elements (beam
splitters, phase shifters) for gates; single-photon detectors for measurement.

**Key players:** PsiQuantum (fusion-based MBQC with silicon photonics),
Xanadu (CV squeezed-light qumodes), QuiX (integrated photonics).

**Advantages:**
- Room-temperature operation (no cryogenics).
- Existing semiconductor photonics manufacturing infrastructure.
- Natural fit for CV and MBQC paradigms.
- Photons are naturally decoherence-free for short propagation distances.
- Inherently networked: photons are the natural carrier of quantum information.

**Challenges:**
- Photon loss is the dominant error mechanism and scales exponentially with
 circuit depth. While error correction can handle loss below a threshold,
 that threshold is demanding (~few percent per component).
- Single-photon sources and detectors are inefficient and noisy.
- Deterministic two-qubit gates are difficult in linear optics; most
 architectures rely on probabilistic entanglement generation followed by
 multiplexing, which imposes enormous resource overhead.
- PsiQuantum's fusion-based approach requires millions of physical components
 for a useful logical qubit, though they claim this is feasible in silicon
 photonics at wafer scale.

**Manufacturability verdict:** High. Silicon photonics leverages the existing
semiconductor fabrication ecosystem. If the component-level performance
thresholds can be met, photonic quantum computers could be manufactured at
scale using existing fabs. This is the strongest commercial case in the
quantum computing landscape as of 2026.

## 4.2 Neutral Atom Arrays

**Platform:** Individual neutral atoms (rubidium, strontium, ytterbium) trapped
in optical tweezer arrays; Rydberg blockade for entangling gates; optical
readout.

**Key players:** QuEra, Atom Computing, Pasqal.

**Advantages:**
- Atoms are identical (no fabrication variability).
- Long coherence times (seconds for hyperfine qubits).
- Reconfigurable: atoms can be rearranged during computation.
- Natural fit for analog quantum simulation (Rydberg atom arrays can simulate
 Ising and XY models).
- Scaling to thousands of atoms demonstrated.

**Challenges:**
- Gate fidelities, while improving, are below fault-tolerance thresholds for
 many architectures (~99.5% for two-qubit gates, need >99.9%).
- Atomic rearrangement is slow (~milliseconds), limiting clock speed.
- Optical access for individual addressing becomes challenging at scale.
- Vacuum and laser infrastructure is bulky and expensive.

**Manufacturability verdict:** Medium. The components (lasers, vacuum chambers,
optics) are commercial-off-the-shelf, and atom arrays scale well in principle.
But the system integration complexity is high, and the cost per qubit is
currently orders of magnitude above what would be needed for commercial
deployment. This platform is most promising for specialized scientific
applications (quantum simulation) in the near term.

## 4.3 Superconducting Qubits: The Incumbent

**Platform:** Josephson junction-based superconducting circuits (transmon,
fluxonium, etc.) operated at millikelvin temperatures.

**Key players:** IBM, Google, Rigetti.

**Advantages:**
- Most mature platform by investment and engineering effort.
- Leverages semiconductor fabrication techniques.
- Fast gate speeds (~10-100 ns).
- Demonstrated error correction below threshold (Google's Willow, 2024).

**Challenges:**
- Cryogenic operation at ~10 mK requires dilution refrigerators, which are
 expensive, bulky, and power-hungry.
- Qubit coherence times are fundamentally limited by materials defects
 (two-level systems in amorphous dielectrics).
- Crosstalk between qubits increases with density.
- The error correction overhead --- ~1000 physical qubits per logical qubit
 for surface codes --- means that a useful fault-tolerant machine would
 require millions of physical qubits, each individually controlled.
- The thermodynamic cost of operating a million-qubit cryogenic system may
 be prohibitive.

**Manufacturability verdict:** Low for commercially useful scale. While
small processors (100-1000 qubits) can be manufactured, the scaling
requirements for fault-tolerant computation --- millions of physical qubits
at millikelvin, each with individual control lines --- appear incompatible
with commercial deployment at any plausible cost point. The superconducting
platform may prove that fault-tolerant quantum computation is *possible in
principle* while being commercially and thermodynamically impractical.

## 4.4 Trapped Ions

**Platform:** Individual atomic ions confined in electromagnetic traps; qubits
encoded in electronic or hyperfine states; gates via laser or microwave pulses;
readout via fluorescence.

**Key players:** IonQ, Quantinuum (Honeywell).

**Advantages:**
- Highest gate fidelities of any platform (>99.9% for two-qubit gates).
- Long coherence times (seconds to minutes).
- All-to-all connectivity (ions can be shuttled).
- Quantinuum has demonstrated repeated error correction cycles.

**Challenges:**
- Gate speeds are slow (~microseconds to milliseconds) compared to
 superconducting qubits.
- Scaling to large numbers of ions in a single trap is limited by motional
 mode crowding.
- Photonic interconnects for modular architectures add complexity and loss.
- System size, cost, and complexity scale poorly.

**Manufacturability verdict:** Low to medium. The exquisite control achieved
in academic and industrial labs does not translate easily to high-volume
manufacturing. Each ion trap is a precision instrument requiring ultra-high
vacuum, stabilized lasers, and careful calibration. While trapped ions are
excellent for demonstrating quantum algorithms at small scale, the path to
commercial deployment at useful scale is unclear.

## 4.5 The Common Scaling Problem

Across all platforms, a common challenge emerges. To perform useful quantum
computation --- solving a problem of genuine commercial value faster or cheaper
than classical alternatives --- fault tolerance is required. Fault tolerance
requires quantum error correction, which imposes an overhead of roughly 10²
to 10³ physical qubits per logical qubit. Useful computation requires perhaps
100-1000 logical qubits. This means a useful fault-tolerant quantum computer
needs 10⁵ to 10⁶ physical qubits, each controlled with high fidelity.

No platform has demonstrated a credible path to manufacturing, cooling,
controlling, and reading out a million high-fidelity qubits at a cost that
would make commercial deployment viable. This is not merely an engineering
challenge --- it may be a thermodynamic one. The entropy generated by
controlling and reading out a million quantum degrees of freedom,
multiplied by the error correction overhead, may exceed what can be dissipated
in a practical device.

# 5. Post-Quantum: The Next Computational Frontier

If the qubit-gate-circuit paradigm is epistemically flawed and the alternative
quantum paradigms face daunting engineering challenges, what comes next? Here
we step back from "quantum computing" entirely and ask: what does the deeper
lesson --- that computation IS a physical process and the substrate determines
what can be computed --- imply for the future of computing?

## 5.1 The Fundamental Insight: Substrate IS Algorithm

The qubit delusion is a specific case of a broader pattern in computer science:
the tendency to treat computation as abstract symbol manipulation, independent
of the physical substrate that performs it. This abstraction --- the Church-Turing
thesis, the von Neumann architecture, the distinction between hardware and
software --- has been enormously productive. But it is, itself, a scaffold.

The deeper insight, which quantum computing inadvertently exposed, is that
**the physical substrate IS part of the algorithm.** A quantum computer is not
just a faster classical computer --- it accesses a different computational
resource (entanglement, superposition) that has no classical analog. The
"software-hardware" distinction breaks down when the physics of the hardware
is the computational primitive.

This suggests that the next major advances in computing will come not from
making faster transistors but from finding physical substrates whose natural
dynamics solve computationally hard problems directly. The substrate IS the
algorithm.

## 5.2 Thermodynamic Computing

**Core idea:** Treat computation as a thermodynamic process. Physical systems
evolve toward thermal equilibrium by minimizing a free energy functional. If
we can encode a computational problem as the free energy landscape of a
physical system, the system's natural relaxation dynamics will "compute" the
solution by finding the free energy minimum.

This is not a new idea --- it is how nature "computes" protein folding, crystal
growth, phase separation, and neural dynamics. What is new is the possibility
of engineering thermodynamic systems specifically for computation.

**Physical implementations:**
- **Ising machines:** Arrays of coupled oscillators (optical parametric
 oscillators, CMOS LC oscillators) that naturally minimize an Ising
 Hamiltonian. Coherent Ising machines [@Marandi2014] have demonstrated
 solving combinatorial optimization problems orders of magnitude faster
 than classical heuristics for certain problem classes --- not by being
 "quantum" but by being analog and massively parallel.
- **Probabilistic bits (p-bits):** Stochastic nanomagnetic devices that
 fluctuate between states with probabilities governed by a Boltzmann
 distribution. Networks of p-bits can perform probabilistic inference,
 optimization, and sampling by exploiting thermal fluctuations rather than
 fighting them [@Camsari2017].
- **Memristive neural networks:** Crossbar arrays of memristive devices that
 perform matrix-vector multiplication in the analog domain via Ohm's law
 and Kirchhoff's current law. This is not quantum --- it's classical physics
 --- but it leverages the physical substrate (resistive switching, charge
 transport) for computation directly.

**Commercial traction:** Several companies are developing Ising machines and
p-bit architectures for optimization and machine learning. These are not
"quantum computers" in the gate-model sense, but they exploit physical
dynamics --- thermal fluctuations, phase transitions, collective modes --- for
computation. They do not require cryogenics, error correction, or isolation
from the environment. In fact, they USE the environment (thermal bath) as a
computational resource.

## 5.3 Neuromorphic Computing

**Core idea:** Build computers that operate on the same principles as
biological neural systems: massively parallel, asynchronous, analog,
event-driven, and co-locating memory and computation.

**Key principles:**
- **Spike-based coding:** Information is encoded in the timing of discrete
 electrical pulses (spikes), not in continuous voltage levels. This is
 energy-efficient because spikes consume power only when they occur.
- **Event-driven computation:** Neurons compute only when they receive input,
 not on a global clock cycle. This eliminates the wasted energy of clock
 distribution in synchronous digital systems.
- **In-memory computation:** Synaptic weights are stored and updated at the
 point of computation (the synapse), eliminating the von Neumann bottleneck
 of shuttling data between memory and processor.
- **Stochastic dynamics:** Neural systems exploit noise --- synaptic
 stochasticity, ion channel fluctuations --- for exploration, learning,
 and robustness.

**Physical implementations:**
- **CMOS neuromorphic chips:** Intel's Loihi 2, IBM's TrueNorth, and
 SpiNNaker use conventional CMOS technology with neuromorphic architectures.
 Loihi 2 achieves ~15 pJ per synaptic operation, compared to ~100 pJ for
 equivalent operations on conventional processors.
- **Memristive neuromorphic systems:** Memristors --- resistors with memory ---
 can implement synapses directly in analog hardware, performing
 matrix-vector multiplication with O(1) energy per operation regardless
 of matrix size.
- **Photonic neuromorphic systems:** Optical neural networks perform linear
 operations (matrix multiplication) through free-space or integrated
 photonic interference, at the speed of light and with minimal energy
 dissipation.

**Why this matters:** Neuromorphic computing is not "quantum computing lite."
It represents a genuinely different computational paradigm --- one where the
physical substrate (analog electronics, photonics, memristive materials)
performs the computation directly, rather than being forced into a digital,
clocked, von Neumann scaffold. The ~10⁴× energy efficiency advantage of
biological neural systems over conventional computers is not a quirk of
evolution --- it reflects the efficiency of analog, event-driven, in-memory
computation.

## 5.4 Optical Computing (Classical)

**Core idea:** Use light --- photons propagating through free space, fibers, or
integrated waveguides --- to perform computation. Linear optical elements
(lenses, beam splitters, spatial light modulators) perform Fourier transforms,
convolutions, and matrix multiplications at the speed of light, with zero
energy dissipation in the optical path.

**Key principles:**
- **Fourier optics:** A lens performs a spatial Fourier transform --- an O(N log N)
 operation in digital --- in a single pass of light, at the speed of light, with
 zero computational energy.
- **Interference-based computation:** Interference between coherent optical
 fields naturally computes inner products, the fundamental operation of
 linear algebra.
- **Wavelength-division multiplexing:** Different wavelengths can carry
 independent computational channels through the same physical medium.

**Commercial traction:** Several startups (Lightmatter, Lightelligence,
Optalysys) are developing optical processors for matrix multiplication and
convolution --- the dominant operations in deep learning. These are not
"quantum" --- they use classical (coherent) light --- but they exploit the
physical properties of light for computation.

Optical matrix multipliers can, in principle, perform matrix-vector products
with O(1) energy scaling in the optical path (the energy cost is dominated by
the input/output conversion, not the computation itself). For sufficiently
large matrices (>1000×1000), optical processors may offer orders-of-magnitude
energy advantages over digital electronics.

## 5.5 What Unifies These Paradigms

Thermodynamic, neuromorphic, and optical computing share a common philosophical
core: **let the physics do the computing.** Instead of forcing computation into
a universal digital scaffold (logic gates, clock cycles, von Neumann
architecture), find a physical system whose natural dynamics solve the problem
directly.

This is the same insight that motivated Feynman's original proposal for quantum
simulation --- "let the quantum system simulate itself" --- but applied more
broadly. A quantum computer is a special case: a physical system whose
(substrate, Hamiltonian, dynamics) are engineered to perform a specific class
of computations that exploit quantum superposition and entanglement. But there
are many other physical systems --- thermal baths, optical fields, neural
networks, chemical reaction networks --- whose natural dynamics solve
computationally hard problems.

The future of computing, we suggest, is not a "quantum computer" in the
qubit-gate sense but a **physical computation ecosystem**: a diverse set of
special-purpose devices --- thermodynamic optimizers, neuromorphic inference
engines, optical matrix processors, analog quantum simulators --- each exploiting
the physics of its substrate for the class of problems it is naturally suited
to solve.

# 6. Principles for Post-Particle Computation

From the analysis above, we distill five principles that should guide the
development of post-qubit computational architectures:

**Principle 1: The substrate IS the algorithm.** Choose physical substrates
whose natural dynamics compute the target problem class directly, rather
than forcing generic substrates into universal computation.

**Principle 2: Correlation over particle.** Encode information in correlation
structures (entanglement, phase coherence, collective modes) rather than in
local states of individual degrees of freedom.

**Principle 3: Noise as resource, not enemy.** Exploit thermal fluctuations,
stochastic dynamics, and environmental coupling for exploration, error
tolerance, and energy efficiency, rather than fighting them with active
error correction.

**Principle 4: Analog where natural, digital where necessary.** Use analog
physical dynamics for the computationally hard part (optimization, sampling,
matrix multiplication) and digital control for programmability and
reconfigurability.

**Principle 5: Manufacturability as first-class constraint.** A computational
paradigm that requires a million cryogenic control lines is not commercially
viable regardless of its theoretical elegance. Design for the manufacturing
ecosystem that actually exists.

# 7. The Research Agenda, Operationalized

We close with specific, falsifiable research directions that operationalize
these principles. Each is tagged with feasibility `[near-term: 1-3 years]`,
`[medium-term: 3-7 years]`, or `[speculative: 7+ years]`.

## 7.1 Thermodynamic Optimization Engines `[near-term]`

Build and benchmark Ising machines, p-bit networks, and coupled oscillator
arrays on practically relevant optimization problems (supply chain
optimization, portfolio allocation, molecular docking). The key metric is not
"quantum advantage" but "thermodynamic advantage": does the physical system
find better solutions faster than classical heuristics at lower energy cost?

**Falsification criterion:** If thermodynamic optimizers consistently fail to
outperform classical heuristics (simulated annealing, genetic algorithms) on
real-world optimization instances, the paradigm is invalid.

## 7.2 Entanglement-First Quantum Architectures `[medium-term]`

Design quantum processors where the computational primitive is the preparation
and manipulation of entanglement structure, not individual qubits. This means:
- MBQC architectures with cluster states as the fundamental resource.
- CV architectures where Gaussian entanglement is the computational substrate.
- Architectures where the physical DOF is a continuum field mode, not a
 two-level system.

**Falsification criterion:** If an MBQC or CV architecture consistently
underperforms a circuit-model architecture with the same physical resources,
the paradigm is not superior.

## 7.3 Neuromorphic Inference at Scale `[near-term]`

Deploy neuromorphic systems (CMOS or memristive) for large-scale inference
in deep learning, where the energy advantage of analog, in-memory computation
is most pronounced. The target: a 10³× energy reduction for transformer
inference compared to GPU-based systems, validated on standard benchmarks.

**Falsification criterion:** If neuromorphic systems cannot achieve >10×
energy advantage on at least one commercially relevant inference workload,
the paradigm is not commercially viable.

## 7.4 Optical Linear Algebra Accelerators `[near-term]`

Develop integrated photonic processors for matrix multiplication and
convolution at scale (>1000×1000 matrices). The target: demonstrating
a 10²× energy-per-operation advantage over digital electronics at a scale
relevant to deep learning inference.

**Falsification criterion:** If optical matrix multipliers cannot maintain
an accuracy-appropriate precision (>4 bits effective) at scale while
achieving >10× energy advantage, the paradigm is not viable.

## 7.5 Field-Theoretic Computation `[speculative]`

Investigate whether quantum field theories --- lattice gauge theories, conformal
field theories, tensor network representations --- can serve as computational
substrates. The question: can we design a physical system whose Hamiltonian
is the QFT of a computationally hard problem, and whose correlation functions
directly encode the solution?

**Falsification criterion:** If no mapping between a computationally hard
problem class and a physically realizable QFT is found within five years of
serious investigation, the paradigm should be downgraded to "speculative
foundations research."

# 8. Conclusion

This paper has argued that the diagnosis offered by "The Qubit Delusion"
implies a constructive research program that extends beyond merely fixing
the qubit-gate-circuit model. The deeper lesson is that computation is an
inherently physical process: the substrate matters, and the choice of
computational scaffold is never ontologically neutral.

The qubit-gate-circuit scaffold projects particle ontology onto a relational
reality. The error-correction paradigm fights decoherence rather than
harnessing it. The commercial quantum computing industry has optimized for
narrative production rather than physical fidelity. These are symptoms of a
deeper pattern: the tendency to treat computation as abstract symbol
manipulation, independent of the physical world that performs it.

The constructive alternative is not a single new computational paradigm but
a **physical computation ecosystem**: a diverse portfolio of special-purpose
devices --- thermodynamic optimizers, neuromorphic inference engines, optical
matrix processors, entanglement-first quantum simulators, and ultimately
field-theoretic computers --- each matched to the problem class that its
physical substrate naturally solves.

This ecosystem will not emerge from the incumbent quantum computing industry,
whose institutional incentives reward the appearance of progress over
falsifiable results. It will emerge from research programs that take
seriously the ontological commitments of quantum mechanics and the physical
constraints of actual manufacturing --- programs that ask not "how do we build
a better qubit?" but "what physical system, if any, can solve this problem
faster, cheaper, or more energy-efficiently than any classical alternative?"

The qubit delusion is not the end of quantum computing. It is the beginning
of honest computation --- computation that respects what physics actually says
about the world.

---

**Acknowledgments**

This work builds on the foundational insights of Rovelli (relational QM),
Fuchs (QBism), Zurek (quantum Darwinism), Raussendorf & Briegel (MBQC),
and Feynman (quantum simulation as physical computation).

**References**

- @Rovelli1996: C. Rovelli, "Relational Quantum Mechanics," Int. J. Theor. Phys. 35, 1637 (1996).
- @Fuchs2014: C. A. Fuchs et al., "An Introduction to QBism with an Application to the Locality of Quantum Mechanics," Am. J. Phys. 82, 749 (2014).
- @Griffiths1984: R. B. Griffiths, "Consistent Histories and the Interpretation of Quantum Mechanics," J. Stat. Phys. 36, 219 (1984).
- @Zurek2003: W. H. Zurek, "Decoherence, Einselection, and the Quantum Origins of the Classical," Rev. Mod. Phys. 75, 715 (2003).
- @Kochen1967: S. Kochen and E. P. Specker, "The Problem of Hidden Variables in Quantum Mechanics," J. Math. Mech. 17, 59 (1967).
- @Schlosshauer2007: M. Schlosshauer, "Decoherence and the Quantum-to-Classical Transition" (Springer, 2007).
- @Raussendorf2001: R. Raussendorf and H. J. Briegel, "A One-Way Quantum Computer," Phys. Rev. Lett. 86, 5188 (2001).
- @Menicucci2006: N. C. Menicucci et al., "Universal Quantum Computation with Continuous-Variable Cluster States," Phys. Rev. Lett. 97, 110501 (2006).
- @Gottesman2001: D. Gottesman et al., "Encoding a Qubit in an Oscillator," Phys. Rev. A 64, 012310 (2001).
- @Frolov2021: S. Frolov, "Majorana Fiasco," Nature 591, 526 (2021).
- @Ronnow2014: T. F. Ronnow et al., "Defining and Detecting Quantum Speedup," Science 345, 420 (2014).
- @Denchev2016: V. S. Denchev et al., "What is the Computational Value of Finite-Range Tunneling?" Phys. Rev. X 6, 031015 (2016).
- @Marandi2014: A. Marandi et al., "Network of Time-Multiplexed Optical Parametric Oscillators as a Coherent Ising Machine," Nat. Photonics 8, 937 (2014).
- @Camsari2017: K. Y. Camsari et al., "Stochastic p-Bits for Invertible Logic," Phys. Rev. X 7, 031014 (2017).

## Prior Work and Related Literature

The present work is the constructive companion to the diagnosis advanced in [The Qubit Delusion: How Particle Ontology Sabotaged Quantum Computing](https://papers.qnfo.org/papers/paper-the-qubit-delusion). That earlier paper argued that the qubit-gate-circuit model imports a particle ontology inconsistent with quantum field theory and relational quantum mechanics, and that the field's failure to deliver viable hardware stems from this epistemic confusion rather than from mere engineering delay. It identified superposition, entanglement, and correlation structure as the invariants that survive the removal of the qubit-as-particle scaffold, and it surveyed alternative paradigms—measurement-based, continuous-variable, topological, and field-theoretic—as more faithful to quantum reality. The present paper takes that critique as its starting point and asks the constructive question that the earlier work left open: if the qubit is a scaffold, what is the invariant, and which alternative architectures can actually be built? It extends the earlier analysis by operationalizing the "correlation-first" research agenda that the Qubit Delusion proposed, moving from ontological deconstruction to a survey of manufacturable platforms—photonic, neutral atom, superconducting, and trapped ion—and then beyond quantum computing altogether to thermodynamic, neuromorphic, and optical systems where the physics does the computing directly.

The present paper also builds directly on the thermodynamic analysis introduced in [Thermodynamic Imperative](https://papers.qnfo.org/papers/thermodynamic-imperative). That work argued that cooling capacity scales superlinearly with temperature (roughly \(T^2\) to \(T^3\)), creating a severe heat-removal bottleneck at millikelvin operation that limits system size regardless of qubit quality. It proposed a hybrid architecture combining parity-protected qubits with 4 Kelvin operation, leveraging the roughly 20,000-fold increase in cooling power available at that regime to expand thermodynamic headroom by orders of magnitude. The present paper generalizes this insight beyond the specific superconducting platform that the Thermodynamic Imperative examined. It treats manufacturability as a first-class constraint for any computational paradigm, as Principle 5 states, and it applies the thermodynamic analysis across platforms: superconducting qubits are judged "low" for commercially useful scale because the entropy generated by controlling and reading out a million quantum degrees of freedom, multiplied by error-correction overhead, may exceed what can be dissipated in a practical device. The present paper also extends the Thermodynamic Imperative's identification of heat management as the primary scalability barrier into a broader argument that the substrate is the algorithm—that computation is a physical process, and the choice of substrate determines what can be computed efficiently. Where the Thermodynamic Imperative focused on engineering a specific path to scalable quantum computing, the present paper uses the same thermodynamic reasoning to argue for a pluralistic "physical computation ecosystem" that includes non-quantum architectures such as Ising machines, probabilistic bits, and memristive neural networks.

The present paper departs from the [Thermodynamic Imperative](https://papers.qnfo.org/papers/thermodynamic-imperative) in a crucial respect. The Thermodynamic Imperative remains within the quantum computing frame: it proposes a specific quantum architecture—parity-protected qubits at 4 Kelvin—as the solution to the scalability problem. The present paper, by contrast, questions whether "quantum computing" is even the right frame at all. It argues that the deeper lesson—that the substrate IS the algorithm—points toward wholly different computational architectures where the physics does the computing directly, rather than being force-fit into a discrete symbolic scaffold. This is not a rejection of the Thermodynamic Imperative's engineering insights but a radicalization of its thermodynamic logic. If the primary barrier to scalability is heat management, and if warmer operation combined with intrinsic protection is the answer, then the question becomes: why stop at 4 Kelvin? Why not exploit thermal fluctuations as a computational resource, as in p-bit networks and Ising machines, which the present paper discusses in Section 5.2? The Thermodynamic Imperative treats noise as something to be suppressed through parity protection; the present paper's Principle 3 inverts this, treating noise as a resource to be exploited for exploration, error tolerance, and energy efficiency. This is a genuine departure, not merely an extension: the Thermodynamic Imperative's hybrid architecture is one entry in the ecosystem the present paper envisions, but the present paper argues that the same thermodynamic reasoning that motivates 4 Kelvin operation also motivates architectures that abandon the quest for isolation altogether.

The relationship between the present paper and the [Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons](https://papers.qnfo.org/papers/adelic-synthesis-pattern-particle) is more complex and involves both continuity and tension. The Adelic Synthesis paper constructed a unified framework in which an anyon is an adelic object—a single arithmetic pattern that manifests differently at each completion of \(\mathbb{Q}\), with the familiar archimedean Fibonacci anyon being merely the \(\infty\)-place avatar. It proposed the Adelic Topological Quantum Computation (ATQC) paradigm, in which computational gates exploit place-crossing transitions (adelic Hecke operators) rather than continuous braiding, potentially eliminating the Solovay-Kitaev overhead entirely. The present paper's survey of topological quantum computing in Section 3.3 acknowledges the theoretical elegance of encoding information in global, relational structures—the topology of particle trajectories—and notes that this aligns with the relational picture of computation. However, the present paper assesses TQC as experimentally extremely challenging, noting that the existence of non-abelian anyons was only confirmed in 2020, and that Microsoft's Majorana program has faced contested evidence. The present paper does not engage with the adelic extension of TQC at all; it treats topological quantum computing as a paradigm that is theoretically elegant but not commercially manufacturable, without reference to the p-adic or adelic constructions.

This silence is telling. The Adelic Synthesis paper is, in a sense, the most radical expression of the "correlation-first" principle that the present paper advocates: it rejects the particle-qubit in favor of a relational, global, topological substrate, and it explicitly frames the anyon as an adelic pattern rather than a particle. The present paper's Principle 2—"Correlation over particle: Encode information in correlation structures (entanglement, phase coherence, collective modes) rather than in local states of individual degrees of freedom"—could be read as a direct endorsement of the adelic perspective. Yet the present paper's Principle 5—"Manufacturability as first-class constraint"—implicitly judges the adelic program as premature. The Adelic Synthesis paper itself acknowledges that its experimental realization is an open question, proposing Bethe lattice quantum spin liquids and ultrametric cold atom systems as candidate platforms, but conceding that these are speculative. The present paper, by contrast, insists that a computational paradigm must be "physically realizable, scalable, and—for commercial viability—manufacturable under industrial constraints." The adelic program, whatever its ontological fidelity, has no such pathway. The present paper's survey of alternative quantum paradigms in Section 3 includes measurement-based, continuous-variable, topological, and analog approaches, but not the adelic or p-adic frameworks; these are absent because they lack the engineering maturity that the present paper demands. The present paper thus both inherits and disciplines the Adelic Synthesis's core insight: the correlation structure is the computational primitive, but that insight must be realized in systems that can actually be built, which is why the present paper ultimately moves beyond quantum computing altogether to thermodynamic, neuromorphic, and optical architectures.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1802.06176 | Introduction to topological quantum computation with non-Abelian anyons
arXiv:0906.2748 | Universal quantum computation with a non-Abelian topological memory
arXiv:0707.1889 | Non-Abelian Anyons and Topological Quantum Computation
arXiv:1811.06738 | Universal quantum computation in the surface code using non-Abelian islands
arXiv:1307.4403 | Universal topological quantum computation from a superconductor/Abelian quantum Hall heterostructure
arXiv:1508.04033 | Continuous error correction for Ising anyons
arXiv:2411.08093 | Spin-liquid-based topological qubits
arXiv:1602.05035 | Topological Quantum Computation with Non-Abelian Anyons in Fractional Quantum Hall States
arXiv:2301.11614 | Non-Abelian Anyons and Non-Abelian Vortices in Topological Superconductors
arXiv:1210.5452 | Braiding of non-Abelian anyons using pairwise interactions
arXiv:2602.15324 | Universal Quantum Gate Compilation in $SU(2)_k$ Anyon Models via Multiple-Braiding

## QNFO corpus context (Vectorize)

QNFO: Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, and the Roots of Unity That Carry Braid Phases | https://papers.qnfo.org/papers/arithmetic-anyon-contact
QNFO: Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction | https://papers.qnfo.org/papers/zbw-p5-capstone-synthesis
QNFO: The Exchange Phase as a Logical Scalar: R = e^(2 pi i s) from the Re-Entrant Calculus | https://papers.qnfo.org/papers/exchange-phase-logical-scalar

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1802.06176 | Introduction to topological quantum computation with non-Abelian anyons
  Topological quantum computers promise a fault tolerant means to perform quantum computation. Topological quantum computers use particles with exotic exchange statistics called non-Abelian anyons, and the simplest anyon model which allows for universal quantum computation by particle exchange or braiding alone is the Fibonacci anyon model. One classically hard problem that can be solved efficiently
  Full text (https://arxiv.org/html/1802.06176), excerpts of its own sections:
  § I Introduction: The exponential growth observed over the past decades in information processing capacity of digital computers, and as quantified by Moore’s law, is unsustainable and will eventually be complemented or surpassed by quantum technologies [ 89 , 65 ] . Quantum computing is a field of much interest because it promises to outperform regular, classical computing for many otherwise intractable problems. [...]
  § VII Intermediate Summary: Before detailing our numerical implementation of the topological quantum computer and using it to perform the AJL algorithm, we shall summarise the essential steps for using a topological quantum computer. Before any computation can begin, certain necessary preprocessing steps must be taken: 1. Determine the braiding matrices for the chosen anyon model (Sec.  V.2 ) and define how many anyons are in a qubit (Sec.  V.3 ). 2. Construct single qubit braids approximating the required operations to a desired accuracy, by brute force or another method (Sec.  V.4 ). The minimum length of the braids scales as $\mathcal{O}(\log(1/\epsilon))$ . 3. Construct controlled operations by a technique such as the weaving method by [ 18 ] , using phase gates to correct for unintended phase differences (Sec.  V.4 ). After this preprocessing is complete, a quantum algorithm can be performed. In particular, we are investigating the AJL algorithm for finding the Jones polynomial: 1. Convert the knot or link $K$ under investigation into either the plat closure or trace closure of a braid $B$ . [...]
  § VIII.3 Discussion: Convergence of the AJL algorithm to the Jones polynomial is determined by multiple factors. The precision is determined primarily by the number of iterations of the Hadamard test, with more iterations and repeated measurements resulting in a convergence at a rate proportional to $1/\sqrt{N}$ . The precision is also influenced by the size of the knot. The output of the quantum computer is scaled by $d^{n-1}$ or $d^{\tfrac{n}{2}-1}$ for trace or plat closures respectively, where $2>d>1$ for $k>3$ . The breadth of the confidence interval, or the uncertainty produced by the stochastic nature of the measurement, is also scaled by that factor, meaning knots with more strands and thus higher $n$ would have larger uncertainties in the measurement of the Jones polynomial, all else being equal. This is why the error bars for the trace closure of the figure-eight knot which has $n=3$ , shown in Fig.  51 (e), are approximately 0.2 wide while other knots with $n=2$ have error bars under 0.1 in width. [...]
  § IX Conclusions: Topological quantum computation is a rich field of study due to its potential fault tolerance imparted by the topological nature of the underlying systems. Fibonacci anyons are a model of particular interest due to their capacity to perform universal quantum computation by braiding alone. Here we have discussed the operations braiding performs, how a quantum computer can be defined for Fibonacci anyons, and how to construct arbitrary unitary operations from the braiding of Fibonacci anyons. We have also provided an explanation of the AJL algorithm for determining the Jones polynomial, and how it may be applied as a quantum algorithm. By performing simulations in MatLab, we have explicitly demonstrated the braiding operations required to perform quantum computation with Fibonacci anyons. We have shown how topological quantum computers can be used to compute the Jones polynomial at roots of unity and discussed how to generalise these principles to generic quantum algorithms. [...]
[2] arXiv:0906.2748 | Universal quantum computation with a non-Abelian topological memory
  An explicit lattice realization of a non-Abelian topological memory is presented. The correspondence between logical and physical states is seen directly by use of the stabilizer formalism. The resilience of the encoded states against errors is studied and compared to that of other memories. A set of non-topological operations are proposed to manipulate the encoded states, resulting in universal q
  Full text (https://arxiv.org/html/0906.2748), excerpts of its own sections:
  § 1 Introduction: Anyons are quasiparticles with topological, and therefore non-local, properties [ 1 , 2 ] , that may be realized on two-dimensional systems [ 3 , 4 , 5 , 6 , 7 , 8 , 9 ] . There has been a number anyon-based proposals for the storage and manipulation of quantum information. Many of these proposals deal with so-called Abelian anyons, encoding quantum information in quasiparticle occupancies [ 10 , 11 , 12 ] or ground state degeneracies [ 15 ] . Others utilize cluster state quantum computation [ 16 ] . In all cases one obtains a topologically protected quantum memory, but this protection does not extend to the processing of the stored information. Non-Abelian anyon models possess quasiparticles with more complex behaviour than their Abelian counterparts [ 17 ] . Specifically, local measurements on two such quasiparticles cannot determine how they will behave if brought together as composite object. [...]
  § 1.1 The $D(S_{3})$ anyon model: Stabilizer codes, strictly defined, are based on lattices of two level spins and the corresponding Pauli group of operators [ 22 ] . The quantum double models of anyons, proposed by Kitaev [ 17 ] , use a generalization of this concept. Spins of higher dimensions are employed, with operators based upon group structures. Abelian groups give rise to Abelian anyons, while non-Abelian groups lead to non-Abelian anyons. Here we consider the simplest non-Abelian model, $D(S_{3})$ , whose explicit lattice realization was outlined in [ 20 ] . This provides the tools with which we build our computational scheme. The relevant aspects of the model are summarized below. The $D(S_{3})$ anyon model is defined on an oriented two-dimensional square lattice. On each edge there resides a six-level spin spanned by the states $\left|\,g\right\rangle$ , where $g$ is an element of $S_{3}$ , the permutation group of three objects. We express every element in terms of generators $t$ and $c$ , which satisfy $t^{2}=c^{3}=e$ and $tc=c^{2}t$ . $e$ denotes the trivial element. [...]
  § 2 The computation with $\Lambda$ charges alone: Though we are using a stabilizer code, the encoding described above is not within the stabilizer space. This allows similar protection from errors, yet easier manipulation. The basic principles of our scheme for universal quantum computation are first presented using the $\Lambda$ charges alone. [...]
  § 4 Conclusions and further work: We have proposed a novel scheme for fault-tolerant quantum computation, utilizing a non-Abelian topological memory. As a result of this work, we have an explicit form for the logical states stored non-locally in terms of the physical states of the underlying lattice model, an understanding of what kinds of memories are possible and their relations to other topological memories. Specifically, we have found two means to encode qubits in the fusion channels of the model’s anyons. Though both fault-tolerant and indistinguishable to local operations, these encodings have a crucial difference. One has states distinguishable to LOCC protocols, and is equivalent to encodings using Abelian anyons. The other has states distinguishable only to non-local operations. Hence, by showing exactly how these encodings differ, we have demonstrated the true difference between Abelian and non-Abelian anyons from a quantum information perspective. Furthermore, we harness these states to give the non-topological operations required for universality while remaining below the energy gap. [...]
[3] arXiv:0707.1889 | Non-Abelian Anyons and Topological Quantum Computation
  Topological quantum computation has recently emerged as one of the most exciting approaches to constructing a fault-tolerant quantum computer. The proposal relies on the existence of topological states of matter whose quasiparticle excitations are neither bosons nor fermions, but are particles known as {\it Non-Abelian anyons}, meaning that they obey {\it non-Abelian braiding statistics}. Quantum 
  Full text (https://arxiv.org/html/0707.1889), excerpts of its own sections:
  § II.3.3 Interference Experiments: While numerics give useful insight about the topological nature of observed quantum Hall states, experimental measurements will ultimately play the decisive role. So far, rather little has been directly measured experimentally about the topological nature of the $\nu=5/2$ state and even less is known about other putative non-Abelian quantum Hall states such as $\nu=12/5$ . In particular, there is no direct experimental evidence for the non-Abelian nature of the quasiparticles. The existence of a degenerate, or almost degenerate, subspace of ground states leads to a zero-temperature entropy and heat capacity, but those are very hard to measure experimentally. Furthermore, this degeneracy is just one requirement for non-Abelian statistics to take place. How then does one demonstrate experimentally that fractional quantum Hall states, particularly the $\nu=5/2$ state, are indeed non-Abelian? The fundamental quasiparticles (i.e. the ones with the smallest electrical charge) of the Moore-Read Pfaffian state have charge $e/4$ [ 233 , 143 ] . [...]
  § III.3.2 Combinatorial Evaluation of Link Invariants and Quasiparticle Properties: The Jones polynomial [ 175 ] $V_{L}(q)$ is a formal Laurent series in a variable $q$ which is associated to a link $L={\gamma_{1}}\cup\ldots\cup{\gamma_{n}}$ . It can be computed recursively using ( 88 ). We will illustrate how this is done by showing how to use a skein relation to compute a related quantity called the Kauffman bracket $K_{L}(q)$ [ 179 ] , which differs from the Jones polynomial by a normalization: $V_{L}(q)=\frac{1}{d}\,(-q^{3/2})^{w(L)}\,K_{L}(q)$ (90) where $w(L)$ is the writhe of the link. (The Jones polynomial is defined for an oriented link. Given an orientation, each crossing can be assigned a sign $\pm 1$ ; the writhe is the sum over all crossings of these signs.) The link $L$ embedded in three-dimensional space (or, rather, three-dimensional space-time in our case) is projected onto the plane. This can be done faithfully if we are careful to mark overcrossings and undercrossings. Such a projection is not unique, but the same Kauffman bracket is obtained for all possible $2D$ projections of a knot (we will see an example of this below). [...]
  § V Future Challenges for Theory and Experiment: Quantum mechanics represented a huge revolution in thought. It was such a stretch of the imagination that many great minds and much experimental information were required to put it into place. Now, eighty years later, another collaborative effort is afoot to revolutionize computation by a particularly rich use of quantum mechanics. The preceding information revolution, which was based on the MOSFET, rested on the 1-electron physics of semiconductors. The revolution which we advocate will require the understanding and manipulation of strongly-interacting electron systems. Modern condensed matter physics has powerful tools to analyze such systems: renormalization group (RG), CFT, Bethe Ansatz, dualities, and numerics. Even without the quantum computing connection, many of the most interesting problems in physics lie in this direction. Prominent here is the problem of creating, manipulating, and classifying topological states of matter. There is a second “richness” in the connection between quantum mechanics and computation. The kind of computation which will emerge is altogether new. [...]
[4] arXiv:1811.06738 | Universal quantum computation in the surface code using non-Abelian islands
  The surface code is currently the primary proposed method for performing quantum error correction. However, despite its many advantages, it has no native method to fault-tolerantly apply non-Clifford gates. Additional techniques are therefore required to achieve universal quantum computation. Here we propose a hybrid scheme which uses small islands of a qudit variant of the surface code to enhance
  Full text (https://arxiv.org/html/1811.06738), excerpts of its own sections:
  § IV A domain wall between $D(\mathbb{Z}_{2})$ and $D(S_{3})$: Let us now consider a domain wall separating the lattice into two regions $\mathfrak{R}_{1}$ and $\mathfrak{R}_{2}$ , where $\mathfrak{R}_{1}$ ( $\mathfrak{R}_{2}$ ) is associated with the $D(\mathbb{Z}_{2})$ [ $D(S_{3})$ ] quantum double model. The domain wall is chosen to lie on the edges of the lattice, and both a qubit and a six-level spin are placed on each domain wall edge, see Fig.  2 (a). The possible gapped domain walls for this setup are parametrized by the subgroups $K$ of $\mathbb{Z}_{2}\times S_{3}$ and a 2-cocycle $\varphi\in H^{2}(K,\mathbb{C}^{\times})$   [ 22 ] . For reasons that will become clear later, we choose the subgroup $K=\{(e,e),(e,c),(e,c^{2}),(x,t),(x,ct),(x,c^{2}t)\}$ with the trivial 2-cocycle and where we used the notation $\mathbb{Z}_{2}=\{e,x\}$ . [...]
  § VIII Conclusions and Outlook: While the theory of domain walls between different quantum double models is well established, we have presented an explicit application of such a domain wall for computational purposes. In particular, we have demonstrated the ability to create a non-stabilizer state in the qubit surface code by transferring information with a patch of qudit surface code based on the non-Abelian group $S_{3}$ . Combined with the Clifford gates of the surface code  [ 7 ] , this provides universal quantum computation. Fault-tolerance for this scheme depends on the ability to efficiently and effectively decode the non-Abelian syndrome of the $D(S_{3})$ quantum double model. Specifically, it must be shown that the logical error rate can be reduced arbitrarily by increasing the size of the islands. While it is widely believed that this can be done for such systems of non-Abelian anyons, most studies have only been done for certain special cases  [ 12 , 13 , 14 , 26 ] . The only current proof for full fault-tolerance concerns so-called non-cyclic anyon models  [ 27 ] . [...]
  § Appendix D Gapped domain walls between the $D(S_{3})$ phase and the $D(\mathbb{Z}_{2})$ phase: In this Appendix, we comment on the considerations that allowed us to find a suitable domain wall for the hybrid architecture introduced in Sec. IV. Let us again consider a lattice which is separated into two half-planes, where the left (right) half-plane is associated with the $D(\mathbb{Z}_{2})$ [ $D(S_{3})$ ] quantum double model. The possible gapped domain walls separating the two phases can be determined by employing the folding trick, see Ref.  [ 22 ] . This theorem states that the gapped domain walls between two arbitrary phases $D(G)$ and $D(G^{\prime})$ are in one-to-one correspondence with the gapped boundaries of $D(G\times G^{\prime})$ , which can be parametrized by subgroups $K$ of $G\times G^{\prime}$ and a 2-cocycle $\varphi\in H^{2}(K,\mathbb{C}^{\times})$ . In our case, there are 10 different subgroups of $\mathbb{Z}_{2}\times S_{3}$ up to conjugation, which are listed in Table  1 . [...]
  § Appendix F Transporting logical information across the domain wall: Let us now comment upon some details regarding the fault-tolerance of the transport of logical information across the domain wall. Again, we assume that there is a way to perform non-Abelian error correction for the $D(S_{3})$ model in a sufficiently reliable way. Given that large holes enjoy an intrinsic topological protection, the only critical steps in the transfer are those shown in Figs. 3(a) and 3(c). [...]
[5] arXiv:1307.4403 | Universal topological quantum computation from a superconductor/Abelian quantum Hall heterostructure
  Non-Abelian anyons promise to reveal spectacular features of quantum mechanics that could ultimately provide the foundation for a decoherence-free quantum computer. A key breakthrough in the pursuit of these exotic particles originated from Read and Green's observation that the Moore-Read quantum Hall state and a (relatively simple) two-dimensional p+ip superconductor both support so-called Ising 
  Full text (https://arxiv.org/html/1307.4403), excerpts of its own sections:
  § I Introduction: The emergence of anyons that exhibit richer exchange statistics than the constituent electrons and ions in a material is among the most remarkable illustrations of ‘more is different’. Such particles fall into two broad categories: Abelian and non-Abelian. Interchanging Abelian anyons alters the system’s wavefunction by a phase $e^{i\theta}$ intermediate between that acquired for bosons and fermions  [ 1 , 2 ] . Richer still are non-Abelian anyons, whose exchange rotates the system’s quantum state amongst a degenerate set of locally indistinguishable ground states produced by the anyons  [ 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 ] . The latter variety realize the most exotic form of exchange statistics that nature in principle permits, which by itself strongly motivates their pursuit. Non-Abelian anyons are further coveted, however, because they provide a route to fault-tolerant topological quantum computation  [ 14 , 15 , 16 , 17 , 18 ] . Here, qubits are embedded in the system’s ground states and, by virtue of non-Abelian statistics, manipulated through anyon exchanges. [...]
  § II Trial application: $p+ip$ superconductivity from the integer quantum Hall effect: The first proposal for germinating Ising anyons in an integer quantum Hall system was introduced by Qi, Hughes, and Zhang  [ 91 ] ; these authors showed that in the vicinity of a plateau transition, proximity-induced Cooper pairing effectively generates spinless $p+ip$ superconductivity in the fluid. [...]
  § III Overview of $\mathbb{Z}_{3}$ parafermion criticality: One useful way of viewing Sec.  II.2 is that we dissected a $\nu=1$ quantum Hall system to construct a non-local representation of the transverse-field Ising model—i.e., a Majorana chain. In preparation for treating the more theoretically challenging $\nu=2/3$ fractionalized setup, here we review an analogous $\mathbb{Z}_{3}$ -invariant chain corresponding to the three-state quantum clock model. This clock model realizes a critical point described by a $\mathbb{Z}_{3}$ parafermion conformal field theory (CFT), which provides the building blocks for the Read-Rezayi wavefunction and plays a central role in describing the edge modes of this state. Studying the chain will enhance our understanding of the symmetries, phase structure, and perturbations of this CFT. Furthermore, much of the groundwork necessary for our subsequent quantum Hall analysis will be developed here. The $\mathbb{Z}_{3}$ quantum clock model is comprised of a chain of three-component ‘spins’. [...]
  § VIII Summary and Discussion: The introduction to this paper provided a broad overview of the main physical results derived here. Having now completed the rather lengthy analysis, we will begin this discussion with a complementary and slightly more technical summary: Our setup begins with a spin-unpolarized $\nu=2/3$ Abelian fractional quantum Hall state—also known as the (112) state—as the backbone of our heterostructure. The (112) state is a strongly correlated phase built from spin-up and spin-down electrons partially occupying their lowest Landau level. At the boundary with the vacuum its edge structure consists of a charge mode (described by $\phi_{\uparrow}+\phi_{\downarrow}$ ) and a counterpropagating neutral mode (described by $\phi_{\uparrow}-\phi_{\downarrow}$ ). We first showed that a long rectangular hole—a ‘trench’—in this fractional quantum Hall system realizes a $\mathbb{Z}_{3}$ parafermion critical point when coupled to an ordinary $s$ -wave superconductor. [...]
[6] arXiv:1508.04033 | Continuous error correction for Ising anyons
  Quantum gates in topological quantum computation are performed by braiding non-Abelian anyons. These braiding processes can presumably be performed with very low error rates. However, to make a topological quantum computation architecture truly scalable, even rare errors need to be corrected. Error correction for non-Abelian anyons is complicated by the fact that it needs to be performed on a cont
  Full text (https://arxiv.org/html/1508.04033), excerpts of its own sections:
  § I Introduction: Besides revealing spectacular features of quantum physics, non-Abelian anyons are sought for their potential application in topological quantum computing [ 1 , 2 , 3 , 4 , 5 ] . Ising anyons are the most well-studied non-Abelian anyon model, since they describe the exchange statistics of localized Majorana fermions [ 4 ] and are expected as elementary excitations of the $\nu=\frac{5}{2}$ fractional quantum Hall state [ 6 , 7 ] . A variety of condensed-matter systems have been proposed as potential hosts of Majorana fermions, see Refs.  [ 8 , 9 , 10 , 11 ] for reviews. Ising anyons also appear as excitations [ 12 , 13 , 14 , 15 ] or ends of defect lines [ 16 , 17 , 18 , 19 ] in several spin-lattice models. The set of quantum gates that can be performed topologically, i.e. by braiding anyons, depends on how qubits are encoded into the fusion space of a number of Ising anyons. However, the gate set will not allow for universal quantum computation for any encoding [ 20 ] . [...]
  § II Continuous error correction for Ising anyons: Following Ref.  [ 25 ] , we consider a square lattice of size $L\times L$ with periodic boundary conditions which hosts Ising anyons . Anyons are quasi-particles that live in 2D space, and this space needs to be discretized to allow for measurements of the local anyonic charge. [...]
  § III Proof of the main result: Our proof is similar in nature to the proofs for the correctability of the toric code by means of MWPM [ 30 , 45 ] . As long as we only consider the (non-Abelian) anyons, the error model for them is exactly identical to the one for the toric code [ 1 , 30 ] with bit-flip rate $p$ and perfect syndrome measurements. The correctabiliy of the anyons thus follows from the correctability of this (very well-studied) error model. Indeed, Ref.  [ 30 ] contains an analytical proof that for this problem $p_{c}\geq 3.7\%$ . Our main difficulty is correcting the fermions which may be produced or “swallowed” during the continuous correction of the anyons, leading to a more involved, correlated effective error model for the fermions. Fig.  2 shows two examples of such processes. From here on, we consider the hypothetical completion of $W$ . That is, we consider the hypothetical world-lines $W$ that we would obtain if we could complete error correction in accordance with our hypothesis $H$ at a given time and bring all anyons to fusion, without any further errors occurring. [...]
  § IV Conclusions: Topological quantum computing holds the promise of processing quantum information with hardware which has intrinsically low error rates. Still, these rare errors need to be corrected in a truly large-scale computation. Here, we have demonstrated the feasibility of this task for Ising anyons under the realistic assumption that errors keep happening as we correct those from previous rounds. Note that another approach towards error correction would be to use qubits encoded in non-Abelian anyons as physical qubits for a further round of error correction. This would lead to a standard decoding problem, although perhaps with a rather complex error model due to the underlying topological processes. In such a case, the available gate set on the final logical qubits would be restricted by the code used in the additional round of error correction. This would remove some of the advantages of using non-Abelian anyons, and may carry a large resource overhead in comparison to standard proposals for physical qubits. [...]
[7] arXiv:2411.08093 | Spin-liquid-based topological qubits
  Topological quantum computation relies on control of non-Abelian anyons for inherently fault-tolerant storage and processing of quantum information. By now, blueprints for topological qubits are well developed for electrically active topological superconductor and fractional quantum Hall platforms. We leverage recent insights into the creation and detection of non-Abelian anyons in electrically in
  Full text (https://arxiv.org/html/2411.08093), excerpts of its own sections:
  § I Introduction: Topological phases of matter hosting non-Abelian anyons (or closely related non-Abelian defects) can emerge in experimental platforms including topological superconductors  [ 1 , 2 ] , fractional quantum Hall systems  [ 3 ] , and quantum spin liquids  [ 4 , 5 , 6 , 7 , 8 , 9 , 10 ] . Interest in these settings is fueled in large part by their potential utility for intrinsically fault-tolerant topological quantum information processing  [ 11 , 12 ] . Three deeply related non-Abelian-anyon characteristics [ 13 ] underlie this technological promise: First, a collection of non-Abelian anyons nucleated in a host platform encodes a degeneracy consisting of locally indistinguishable states. Qubits encoded in that manifold correspondingly enjoy built-in resilience against dephasing errors from local environmental noise. Second, adiabatically braiding non-Abelian anyons nontrivially rotates the system’s wavefunction within the degenerate subspace—enacting a set of ‘rigid’ quantum gates on the protected qubits. [...]
  § II Review of anyon generation and detection schemes: Figure 1: Topological properties of the non-Abelian Kitaev spin liquid phase. The boundary between the spin-liquid phase and a trivial phase hosts a chiral Majorana edge mode. The gapped bulk supports three types of quasiparticles enumerated in (a); their nontrivial fusion rules and braiding statistics are summarized in (b) and (c), respectively. The non-Abelian Kitaev spin liquid phase hosts a gapless chiral Majorana edge mode described by a chiral Ising CFT with central charge $c=1/2$ . In the bulk, three gapped quasiparticle types can appear: topologically trivial local bosons ( $I$ ), emergent fermions ( $\psi$ ), and non-Abelian Ising anyons ( $\sigma$ ) that correspond to $\mathbb{Z}_{2}$ flux excitations [see Fig.  1 (a)]. Non-Abelian properties of the Ising anyons descend from an emergent Majorana zero mode that binds to a $\mathbb{Z}_{2}$ flux in this phase. [...]
  § II.1 Detection via local probes: Detecting individual anyons in non-Abelian Kitaev spin liquids poses a daunting task because of the limited way in which the fractionalized degrees of freedom couple to local probes. For instance, electrons from a lead can not directly hybridize with emergent Majorana fermions born in the spin liquid (contrary to the situation for topological superconductors where Majorana fermions arise from physical electron and hole superpositions). [...]
  § VI Discussion: Quantum spin liquids have persisted as a topic of great theoretical and experimental interest for decades, yet the question ‘What does a topological qubit based on non-Abelian spin liquids look like?’ has remained largely unanswered. Building on recent theory insights, we have proposed two classes of potentially scalable topological qubit designs for non-Abelian spin liquids realized in Kitaev materials—and potentially other families of magnetic insulators. The first class uses Kitaev materials integrated into magnetic tunnel junction arrays that enable dynamically tuning select patches of the system between spin-liquid and trivial phases. The second class couples Kitaev materials to semiconductors—binding the non-Abelian anyons to electric charges and enabling all-electrical control of the charge-anyon composites. Figure 20: Scalable qubit architecture in the magnetic tunnel junction setup. Generalizing the single-qubit braiding scheme from Fig.  13 , this architecture consists of a series of storage points where Ising anyons are held between braiding operations. [...]
[8] arXiv:1602.05035 | Topological Quantum Computation with Non-Abelian Anyons in Fractional Quantum Hall States
  We review the general strategy of topologically protected quantum information processing based on non-Abelian anyons, in which quantum information is encoded into the fusion channels of pairs of anyons and in fusion paths for multi-anyon states, realized in two-dimensional fractional quantum Hall systems. The quantum gates which are needed for the quantum information processing in these multi-qubi
  Full text (https://arxiv.org/html/1602.05035), excerpts of its own sections:
  § 1 Introduction: Quantum Computation in general: Quantum Computation (QC) is a relatively new field [ 1 ] of computational research in which information is encoded in two-level quantum systems called qubits , or qu antum bits , in analogy with the classical bits. In contrast with the classical bits, which can have only two states ‘0’ and ‘1’, the qubit is an arbitrary linear combination of the two basic quantum states $|0\rangle$ and $|1\rangle$ $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,\quad\mathrm{with}\quad\alpha,\beta\in{\mathbb{C}}\quad\mathrm{and}\quad|\alpha|^{2}+|\beta|^{2}=1,$ (1) i.e., a qubit $|\psi\rangle$ belongs to the projective ${\mathbb{C}}^{2}$ space which is called the Bloch sphere [ 1 ] . In order to prepare one qubit state for QC we have to define first an orthonormal basis $|0\rangle$ , $|1\rangle$ , which could be for example the two spin-projection states of a spin 1/2 particle, and then construct physically the state $|\psi\rangle=|0\rangle$ or $|\psi\rangle=|1\rangle$ . [...]
  § 2 Non-Abelian anyons and topological QC: In this section we will explain the new concept of non-Abelian exchange statistics of particles and will try to give an idea of what it can be used for. Consider a system of indistinguishable particles at fixed positions in space. One of their important statistical characteristics is their statistical angle $\theta_{A}/\pi$ , which can be defined in the following way: the quantum state of the system with many indistinguishable particles of type ‘A’ can be expressed as a correlation function (or a vacuum expectation value) of some quantum filed operators $\psi_{A}(z)$ which represent the act of creation of a particle of type ‘A’ at position $z$ in the space. Let us focus only on two particles of type ‘A’, at positions $z_{1}$ and $z_{2}$ in space, although the system may contain more particles. [...]
  § 2.1 Construction of $n$ -particle states: the braid group: Another important distinction between the three-dimensional coordinate space and the two-dimensional one can be seen in the many-particle states. The many-particle quantum states in three-dimensional space are built as representations of the symmetric group $\mathcal{S}_{n}$ , which are symmetric for bosons and antisymmetric for fermions. The symmetric group $\mathcal{S}_{n}$ , which is the group of permutation of $n$ objects, is a finite group generated by $n-1$ elementary transpositions of neighboring objects i.e., $\sigma_{i}:i\leftrightarrow i+1$ and obviously satisfy $\sigma_{i}=\sigma_{i}^{-1}$ . Like any finite group $\mathcal{S}_{n}$ can be defined by its genetic code, i.e., the relations between its generators [ 7 ] $\sigma_{i}\sigma_{j}=\sigma_{j}\sigma_{i},\quad|i-j|\geq 2,$ which means that the disjoint transpositions commute with each other, and $\sigma_{i}\ \sigma_{i+1}\ \sigma_{i}=\sigma_{i+1}\ \sigma_{i}\ \sigma_{i+1},\quad\left(\sigma_{i}\right)^{2}={\mathbb{I}}. [...]
  § 5 The Pfaffian state: comparison with the experiment at $\nu_{H}=2/3$: A recent experiment [ 31 ] brought a new hope for the possibility to measure some thermoelectric characteristics of SETs and eventually detect “upstream neutral modes” in the fractional quantum Hall regime. In this section we will calculate and plot the conductance, thermopower and thermoelectric power factor for the Pfaffian FQH state and will compare these quantities with the measured ones in the experiment [ 31 ] . It appears that there two distinct cases: even number of quasiparticles localized in the bulk and odd number, which we shall consider separately.
[9] arXiv:2301.11614 | Non-Abelian Anyons and Non-Abelian Vortices in Topological Superconductors
  Anyons are particles obeying statistics of neither bosons nor fermions. Non-Abelian anyons, whose exchanges are described by a non-Abelian group acting on a set of wave functions, are attracting a great attention because of possible applications to topological quantum computations. Braiding of non-Abelian anyons corresponds to quantum computations. The simplest non-Abelian anyons are Ising anyons 
  Full text (https://arxiv.org/html/2301.11614), excerpts of its own sections:
  § Key points/objectives: • Unlike fermions and bosons, the exchange of non-Abelian anyons is described by unitary transformations that operate on topologically protected degenerate ground states. The adiabatic exchanges of two or more non-Abelian anyons manipulate quantum information stored in a set of degenerate ground states, leading to topological quantum computations. • The simplest non-Abelian anyons are Ising anyons which are predicted to exist as Majorana zero modes in topological superconductors, fractional quantum Hall states, Kitaev materials, and dense quark matter. • Another non-Abelian anyons are vortex anyons, which are constructed from non-Abelian vortices supported by a non-Abelian first homotopy group. Such vortex anyons exist in liquid crystals, superfluid 3 He, spinor Bose-Einstein condensates, and high density quark matter. • ${}^{3}P_{2}$ superfluids, which are expected to be realized in neutron stars, provide unique systems simultaneously admitting two kinds of non-Abelian anyons, i.e., Ising anyons and vortex anyons.
  § 1 Introduction: In three spatial dimensions, all particles are either bosons or fermions in quantum physics, that is, a wave function of multi-particle states is symmetric (antisymmetric) under the exchanges of two bosons (fermions). On contrary, in two spatial dimensions, there exist exotic particles classified to neither bosons nor fermions, anyons . A wave function of two anyons receives a nontrivial phase factor under their exchanges  Leinaas & Myrheim (1977) ; Wilczek (1982) . Such exotic particles play essential roles in fractional quantum Hall states  Halperin (1984) ; Arovas et al. (1984) , and have been experimentally observed for $\nu=1/3$ fractional quantum Hall states  Bartolomei et al. (2020) ; Nakamura et al. (2020) . Recently, yet exotic particles attracted great attention, that is, non-Abelian anyons . Non-Abelian anyons are described by a set of multiple wave functions, and the exchanges of two non-Abelian anyons lead to unitary matrix operations on a set of wave functions. [...]
  § 2.1 Braid group and quantum statistics: Here we consider pointlike topological defects (e.g., vortices in two-dimensional spinless SCs) which behave as identical particles in a two-dimensional plane. [...]
  § 5.1 Overview of ${}^{3}P_{2}$ topological SFs: Study of ${}^{3}P_{2}$ SFs was initiated since 1970s  Hoffberg et al. (1970) ; Tamagaki (1970) ; Takatsuka & Tamagaki (1971) ; Takatsuka (1972) ; Richardson (1972) ; Sedrakian & Clark (2018) . [...]
  § 6 Summary: We have presented various types of non-Abelian anyons in topological SCs/SFs and other systems. Non-Abelian anyons are attracting a great attention because of possible applications to topological quantum computations, where quantum computations are realized by braiding of non-Abelian anyons. The simplest non-Abelian anyons are Ising anyons realized by Majorana fermions hosted by vortices (or edges) of topological superconductors, $\nu=5/2$ quantum Hall states, spin liquids, and high density quark matter. These are, however, insufficient for universal quantum computations. The other anyons which can be used for universal quantum computations is given by Fibonacci anyons which exist in $\nu=12/5$ quantum Hall states. There are also Yang-Lee anyons which are non-unitary counterparts of Fibonacci anyons. Another class of non-Abelian anyons of the bosonic origin can be given by non-Abelian vortex anyons realized by non-Abelian vortices supported by a non-Abelian first homotopy group. [...]
[10] arXiv:1210.5452 | Braiding of non-Abelian anyons using pairwise interactions
  The common approach to topological quantum computation is to implement quantum gates by adiabatically moving non-Abelian anyons around each other. Here we present an alternative perspective based on the possibility of realizing the exchange (braiding) operators of anyons by adiabatically varying pairwise interactions between them rather than their positions. We analyze a system composed by four an
  Full text (https://arxiv.org/html/1210.5452), excerpts of its own sections:
  § I Introduction: The purpose of topological quantum computation (TQC) is to realize a reliable quantum computer, exploiting the existence of special quasiparticles, known as non-Abelian anyons, in certain exotic condensed matter systems [ 1 , 2 ] . The presence of several such particles gives rise to degenerate ground states which cannot be distinguished by local measurements. The ground state manifold is then adopted as the computational space, and quantum gates can be performed by braiding (exchanging the positions of the anyons), as shown in Fig.  1 a). The resulting unitary transformation of the wave function depends only on the order of the exchanges and not on the details of their paths, thus these quantum gates are said to be topologically protected. In the standard scheme of TQC [ 2 ] , there are two main ingredients needed to implement braiding. First, it must be possible to change the positions of anyons in such a way that the wave function of the system always belongs to the space of the degenerate ground states. [...]
  § II The T-junction: We consider a system of four anyons with the same topological charge t in a T-junction geometry, with a central anyon (labeled $\mathsf{t_{C}}$ ) coupled to other three (labeled $\mathsf{t_{L}}$ , $\mathsf{t_{R}}$ , $\mathsf{t_{B}}$ for left, right and bottom), as shown in Fig. 1 c and Fig. 2 . We assume that they have fusion rules $\mathsf{t}\times\mathsf{t}=\sum_{i=1}^{n}\,\mathsf{f}_{i}$ (1) with $\{\mathsf{f}_{i}\}$ the set of the $n$ possible fusion channels (see Refs. [ 27 , 2 , 28 , 29 ] for introductions on non-Abelian anyons and their fusion rules). We also assume that the anyons do not move, and we focus on the pairwise interactions between them. These interactions result in the fusion channels $\mathsf{f}_{i}$ having different energies, so that the Hamiltonian can be written as a sum of projectors onto different fusion outcomes. [...]
  § II.1 Ground state degeneracy: To prove that the Hamiltonian ( 2 ) is of any use for TQC, we must identify a degenerate manifold of its ground states, at least in some regions of the parameter space spanned by the energies $\epsilon_{i,\mathsf{K}}$ . It has been shown that tunneling couplings between anyons lift completely the topological degeneracy of the ground state [ 31 ] , and the Hamiltonian ( 2 ) makes no exception if all $\epsilon_{\mathsf{a,K}}$ are non-zero. On the other hand, if all the couplings are zero, the ground state manifold coincides with the whole Hilbert space of the anyon system. [...]
  § IV.2 Summary: In summary, we have investigated an approach to topological quantum computation. In order to implement the necessary braiding operations of non-Abelian anyons, we couple the anyons instead of moving them or measuring their state. We have considered a simple system composed of four interacting non-Abelian anyons in a T-junction geometry and we have shown how adiabatic control over the interactions results in the Berry matrix expected when two anyons are moved around each other. If the coupling between the anyons cannot be completely turned off, errors are introduced in the braiding operations due to the residual splitting of the ground state degeneracy. We have discussed how these errors can be limited by means of enlarging the number of anyons involved in the adiabatic evolution. The protection is exponential in the number of anyons which are added to the system, so the whole procedure is similar to increasing the separation between anyons in the original approach. [...]
[11] arXiv:2602.15324 | Universal Quantum Gate Compilation in $SU(2)_k$ Anyon Models via Multiple-Braiding
  We investigate the capability of multiple-braiding in $SU(2)_k$ anyon models to realize universal quantum computation. The multiple elementary braiding matrices (MEBMs) are derived from the $q$-deformed representation theory of $SU(2)$. Through a general analysis of the MEBMs, we find that multiple-braiding loses its universality only when the braiding multiplicity $m$ causes the MEBMs to collapse
  Full text (https://ar5iv.labs.arxiv.org/html/2602.15324), excerpts of its own sections:
  § Submission history: From: Jiangwei Long [ view email ] [v1] Tue, 17 Feb 2026 03:11:09 UTC (1,080 KB) [v2] Wed, 22 Apr 2026 11:52:08 UTC (979 KB) [v3] Tue, 8 Sep 2026 08:39:59 UTC (1,444 KB) [v4] Thu, 24 Sep 2026 01:48:19 UTC (1,450 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Universal Quantum Gate Compilation in $SU(2)_k$ Anyon Models via Multiple-Braiding, by Jiangwei Long and 2 other authors View PDF view license
  § Current browse context:: quant-ph < prev | next > new | recent | 2026-02
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[12] QNFO: Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, and the Roots of Unity That Carry Braid Phases | https://papers.qnfo.org/papers/arithmetic-anyon-contact
  Three spatial dimensions admit exactly two exchange statistics for identical particles, and a recent record reads the two occupation distributions as maximum-entropy occupations of one integer lattice under two multiplicity rules, closing with an open correspondence: the bounded-occupation family interpolates between the fermionic and bosonic cases and is proposed as the arithmetic object that int
  Full text (https://papers.qnfo.org/papers/arithmetic-anyon-contact), excerpts of its own sections:
  § 1. Introduction: A system of identical particles in three or more spatial dimensions admits exactly two exchange statistics. In two dimensions the configuration-space argument yields the braid group and a continuum of fractional phases — the anyons realized in the fractional quantum Hall regime [@leinaas1977; @wilczek1982] and measured in anyon colliders [@heiblum2022]. Two readings of the two-statistics binary meet in a recent record: the occupation distributions are read as maximum-entropy occupations of the integer lattice, the unrestricted lattice giving the Riemann zeta function and the squarefree lattice the ratio of two zeta values [@qnfo22123068]. That record closes with an open correspondence: the bounded-occupation family $$\sum_{v_p(n) \le m} n^{-s} \;=\; \prod_p \left(1 + p^{-s} + \dots + p^{-ms}\right) \;=\; \frac{\zeta(s)}{\zeta((m+1)s)}$$ interpolates from the fermionic case at $m = 1$ to the bosonic case as $m \to \infty$, and is proposed as the arithmetic object that intermediate (anyonic) statistics must contact. [...]
  § 2. The bounded-occupation family: Let $\zeta(s)$ be the Riemann zeta function. The two Dirichlet identities at the center of the family are $$\sum_{n \text{ squarefree}} n^{-s} = \prod_p (1 + p^{-s}) = \frac{\zeta(s)}{\zeta(2s)}, \qquad \sum_{n \ge 1} n^{-s} = \prod_p (1 - p^{-s})^{-1} = \zeta(s).$$ The first counts integers whose prime exponents obey $a_p \in \{0,1\}$; the second counts every exponent. The Euler factors are single-mode partition functions: $(1 + p^{-s})$ is the partition function of a two-state mode, $(1 - p^{-s})^{-1}$ that of an unbounded mode, when $s$ is read as an inverse temperature multiplying the mode energy $\ln p$. The identification of these generating structures with the two quantum statistics has a long history in the Riemann-gas literature [@julia1990; @spector1990; @bakas1991; @hartnoll2025; @makhaldiani2018], and its per-place form was established in this program at fixed fugacity [@qnfo22035210]. [...]
  § 3. The family carries no exchange phase: Exchange statistics is a datum of the multi-particle state space: a representation of the braid group (two dimensions) or the symmetric group (three and more dimensions) on the states of identical particles. The bounded-occupation family is a generating function of counting: a real-valued Dirichlet series whose coefficients are the number of configurations. The two layers — counting and phase — are distinct, and the computation shows the family contains only the first. **Occupation-label exchange.** Take two distinguishable modes $p$ and $q$ and the two-particle sector of the capped Fock space: states $|a_p, a_q\rangle$ with $a_p + a_q = 2$, namely $(2,0)$, $(1,1)$, $(0,2)$ for any cap $m \ge 2$, and $(1,1)$ alone at $m = 1$. Particle exchange maps $|a_p, a_q\rangle \mapsto |a_q, a_p\rangle$. This is a permutation of the sector: a swap of $(2,0)$ with $(0,2)$ and a fixed point at $(1,1)$. Its eigenvalues are $\{1, 1, -1\}$ for every $m \ge 2$, and $\{1\}$ at $m = 1$. [...]
  § 4. Gentile statistics is not Haldane exclusion statistics: The exclusion-type constraint that the condensed-matter literature has actually related to braid phases is Haldane's fractional exclusion statistics [@haldane1991; @speliotopoulos1995]. In the g-form, a mode whose occupation is $n$ leaves $g$ fewer states for the next particle, and the occupation at fugacity parameter $x$ solves $$w^{g} (1 + w)^{1-g} = 1/x, \qquad n_g = \frac{1}{w + g},$$ with $g = 1$ the Fermi case and $g = 0$ the Bose case. [...]
[13] QNFO: Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction | https://papers.qnfo.org/papers/zbw-p5-capstone-synthesis
  The ZBW-Majorana hypothesis, developed across four companion papers (P1--P4), establishes that Zitterbewegung (ZBW) --- the rapid trembling motion of Dirac fermions at the Compton scale --- is a $\mathbb{Z}_2$ topological observable that distinguishes Dirac from Majorana fermions at the hardware level. This capstone paper synthesises the six central claims of the ZBW-Majorana framework into a sing
  Full text (https://papers.qnfo.org/papers/zbw-p5-capstone-synthesis), excerpts of its own sections:
  § Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction: **Author:** Rowan Quni | **Date:** 2026-07-25 | **License:** QNFO-ULA: https://legal.qnfo.org/ ---
  § 1. Introduction: The Dirac equation predicts that a free relativistic electron undergoes a rapid oscillatory motion at the Compton frequency $\omega_C = 2mc^2/\hbar \approx 1.55 \times 10^{21}$ Hz, with amplitude $\lambda_C/2 = \hbar/(2mc) \approx 1.93 \times 10^{-13}$ m [established]. This Zitterbewegung (ZBW) has resisted direct experimental observation for nearly a century, largely because the Compton wavelength lies below the resolution of any imaging technology [established]. The QNFO ZBW-Majorana research programme, documented in four papers [1--4], advances a different explanation: ZBW is best understood as a $\mathbb{Z}_2$ topological observable whose information content resides in the ultrametric (p-adic) connectivity of momentum-spin eigenstates, not in the amplitude of real-valued oscillations. This framework makes a specific, falsifiable prediction: the ZBW contribution to the current-current correlator $\langle j^\mu(x) j^\nu(0) \rangle$ vanishes identically for Majorana fermions while remaining non-zero for Dirac fermions --- a $\mathbb{Z}_2$ distinction with no intermediate values. [...]
  § 6. Claim 5: Experimental Protocols: **Three experimental protocols (A, B, and C) are proposed to measure the ZBW $\mathbb{Z}_2$ invariant in Majorana systems.**
  § 10. Integrated Experimental Roadmap: | Phase | Protocol | Milestone | Timeline | |:------|:---------|:----------|:---------| | **I** | C (Gromov $\delta$) | Reconstruct ZBW transition graph from tunnelling spectroscopy; verify tree-like structure and edge reduction | 6--12 months | | **II** | A (Spin noise) | Detect ultrametric clustering in spin-flip waiting times ($10^4$ events) | 3--6 months (parallel with I) | | **III** | B (EELS/RIXS) | Measure $\mathcal{O}_{\text{ZBW}}(p)$ as function of momentum transfer; verify zero for Majorana, growing for Dirac control | 1--2 years | | **IV** | A+B combined | Test topological protection: measure $\mathcal{O}_{\text{ZBW}}$ under controlled continuous perturbation; verify invariance | +6 months after III | | **V** | All three | Adelic synthesis: compare Archimedean (interferometric braiding) and p-adic (ZBW spectroscopy) channels for same system | +1 year after IV | **Go/no-go gates:** - **Phase I gate:** If $\delta \gg 0$ for ZBW graph, re-evaluate the ultrametric hypothesis before committing to Phase III beamtime. [...]
  § 12. Conclusion: The ZBW-Majorana framework establishes six interconnected claims spanning from the vanishing of the ZBW current-current correlator for Majorana fermions (Claim 1) to hardware-level topological quantum computing without active QEC (Claim 6). Each claim is independently documented in the companion papers [1--4] and verified through a combination of analytical derivation and numerical computation. The framework is falsifiable at multiple points (see §9) and provides a concrete experimental roadmap with estimated timelines (see §10). The $\mathbb{Z}_2$ topological invariant $\mathcal{O}_{\text{ZBW}}$ is the central organising concept: it bridges the abstract Majorana constraint $\psi = \psi^c$ with the concrete experimental observable (Protocol B), the geometric manifestation (Protocol C), and the quantum computing application (Claim 6). [...]
[14] QNFO: The Exchange Phase as a Logical Scalar: R = e^(2 pi i s) from the Re-Entrant Calculus | https://papers.qnfo.org/papers/exchange-phase-logical-scalar
  The boson/fermion dichotomy is conventionally presented as a primitive classification of nature. Recent work established that the underlying invariant is the relation between the exchange phase of identical particles and their topological spin, R = e^{2πis}, with the dichotomy as its shadow in three spatial dimensions where the involutive braiding quantizes the spin parameter. This paper examines 
  Full text (https://papers.qnfo.org/papers/exchange-phase-logical-scalar), excerpts of its own sections:
  § 1. Introduction: The spin-statistics theorem is among the most robust laws of physics: integer-spin particles obey Bose–Einstein statistics and half-integer-spin particles obey Fermi–Dirac statistics [Pauli 1940]. The QNFO research program has pursued the structural reading of this law. In [Quni-Gudzinas 2026b] it was established that the primitive content is not the dichotomy itself but the relation $$R = e^{2\pi i s} \quad [\text{ESTABLISHED}]$$ between the exchange phase of identical particles and their topological spin, where the boson/fermion binary is a dimension-dependent shadow of this relation in three spatial dimensions [ESTABLISHED]. The same work identified a derivation target: a distinction-based foundation of physics must derive exchange statistics from the primitive act of drawing a boundary, rather than importing the relation as an axiom. [...]
  § 2. So What? Why Should a Reader Care About This Research?: **The stakes.** The spin-statistics theorem is among the most robust laws of physics: integer-spin particles obey Bose–Einstein statistics and half-integer-spin particles obey Fermi–Dirac statistics [Pauli 1940]. Yet the standard derivation imports Lorentz invariance, microcausality, and positive energy — and it takes the *form* of the exchange phase for granted. The constants e and π enter physics as brute inputs. This paper asks whether they are outputs: if the exchange phase is the (2s)-fold half-turn of the re-entrant mark, then e, π, and R = e^{2πis} form a single scalar family generated by the act of drawing a distinction. The two most famous constants in physics would not be axioms of nature but consequences of a more primitive logical act. [...]
  § 3.1 The invariant R = e^{2πis}: The exchange of two identical particles is a loop in their configuration space. The phase acquired is a representation of the fundamental group of that space: π₁ = ℤ₂ in dimension d ≥ 3, and π₁ = B₂ ≅ ℤ in dimension d = 2 [Leinaas and Myrheim 1977]. The spin-statistics relation states which phase is realized: η = (−1)^{2s}, where s is the spin [Pauli 1940; Duck and Sudarshan 1998]. In dimension d ≥ 3 the involutive braiding forces 2s ∈ ℤ, so the exchange phase is ±1 and particles are bosons or fermions; in dimension d = 2 the quantization collapses to continuity, and arbitrary exchange phases e^{2πis} describe anyons [Wilczek 1982; Kitaev 2006]. [ESTABLISHED]
  § 9. Conclusions: The exchange phase R = e^{2πis} is the (2s)-fold half-turn of the re-entrant mark: R = (e^{iπ})^{2s} = (−1)^{2s}. The boson/fermion dichotomy is the parity of 2s. The claim is scoped with an explicit status ladder: the arithmetic is established, the identification is a model, and the full logical derivation within the traced differential cohesive linear type theory of the treatise is a conjecture with concrete falsifiability conditions. If the derivation succeeds, e, π, and R form a single family of logical scalars of the re-entrant mark — fixed point, trace, and monodromy power — and the spin-statistics connection is the arithmetic of the half-turn. If it fails, the failure mode is precisely specified: the calculus cannot generate the exchange phase without importing it as an axiom. The consistency result with the p-adic anyon program (FQ2, §8) adds a second, independent anchor: the same monodromy-power form (e^{iπ})^{2s} governs both the archimedean continuum and the non-archimedean rational-spin sector.