# Gauge-Structured Photonic Lattices as Synthetic Vacua: A Feasibility Analysis of Room-Temperature Fibonacci Anyon Computing

## Abstract

Large-scale fault-tolerant quantum computing currently requires cryogenic operation and heavy active error-correction overhead, which constrains scalability and cost. A conjectured alternative is a room-temperature solid-state photonic lattice—a "synthetic vacuum"—engineered so that an emergent SU(2)-like gauge symmetry hosts Fibonacci anyons as edge excitations, with braiding performing universal logic protected by the medium's gauge structure rather than by active correction. The specific gap addressed here is that no published analysis quantifies whether such a gauge-protected substrate can be thermally stable at 300 K and whether gauge constraints suppress or merely relocate error channels. We model the lattice as a gapped photonic band structure with a topological edge sector, derive the gap required for thermal robustness, and account error channels by their gauge transformation properties. We find that a gap of at least $\Delta \approx 15\,k_B T \approx 0.388\ \mathrm{eV}$ (photon frequency $\approx 93.8\ \mathrm{THz}$, wavelength $\approx 3.20\ \mu\mathrm{m}$) holds the probability of any thermally excited stray anyon below $\approx 6.1\times 10^{-4}$ for a $10^3$-mode device, and that gauge invariance reduces but does not eliminate the error budget: with a gauge-invariant fraction $f_{\mathrm{gp}} = 2/3$ of local operators, a physical error rate $p$ is reduced to $p_{\mathrm{eff}} \approx (2/3)p$ plus a suppressed term. The conclusion is conditional: gauge protection is a rate reducer, not a replacement for correction, and the proposal remains at the level of analytical feasibility.

## 1. Introduction

The practical problem is the overhead of fault-tolerant quantum computation. Error-corrected machines demand physical error rates far below what current hardware delivers, and the correction machinery itself—ancilla qubits, repeated syndrome extraction, magic-state distillation—dominates the resource count. The fault-tolerant framework is well understood theoretically [1], yet the same source notes that experimental efforts had fabricated arrays of only about ten functional qubits at the time of writing, a gap between theory and hardware that persists in motivating new substrates. Every proposed route to universal logic carries a specific tax: transversal gates cannot supply a universal set by the Eastin–Knill theorem, so non-Clifford resources must be manufactured, and even optimized flag-qubit magic-state preparation uses ten qubits and accepts a state only about $80\%$ of the time to reach logical error rates near $10^{-4}$ at physical error rates near $3\times 10^{-3}$ [4]. Flag-based error correction lowers ancilla counts relative to Shor-style schemes, which require as many ancillas as the maximum stabilizer weight [6], but the overhead remains multiplicative in code distance.

Who faces this problem: any team designing a scalable quantum processor, and more broadly the field's roadmaps, which must budget for correction hardware that grows with every reduction in logical error rate. What it costs or blocks today: the correction layer sets the floor on device size, cycle time, and energy, and it is the reason scaling arguments terminate at the thermodynamic limits of continuous active surveillance of a quantum state, an argument made explicitly in the non-Archimedean architecture literature [7]. What would change if this paper's central conditional result holds: if a passive, gauge-structured medium could hold topological degrees of freedom stable at room temperature, the correction layer would shrink from an active control stack to a materials-design problem, and the operating envelope would move from millikelvin cryogenics to ambient temperature.

The conjecture under examination, due to the source research idea, is that a room-temperature solid-state photonic lattice—a "synthetic vacuum"—can instantiate a non-Abelian, SU(2)-like gauge symmetry such that Fibonacci anyons appear as edge excitations and their braiding implements universal quantum logic intrinsically, with protection arising from the gauge structure of the medium itself. This idea connects to a broader program of making the physics carry the computation: Hamiltonian engineering as computation, formalized as the "Inverted Church-Turing-Deutsch" thesis and tested in silico for Ising-type (Class A) and spectral-synthesis (Class B) engines over problem sizes $N=3$ to $12$ [10]; vectorial topological encoding in which computational results are embodied as Chern-number vectors in moiré superlattices, dissolving the Residue Number System reconstruction bottleneck [8]; and the operationalization of generalized (non-invertible) symmetries in Fractional Chern Insulators into falsifiable experimental protocols, including a halo-radius diagnostic proposed as a proxy for the abstract quantum dimension [9].

This paper does not claim to demonstrate such a device. It performs what a theoretical feasibility paper can do: state the model, derive the quantitative conditions the conjecture must satisfy, and analyze whether gauge constraints genuinely suppress error channels or merely relocate them. The honest answer developed below is that gauge structure converts some errors into energetically suppressed processes while leaving a residual gauge-respecting error channel untouched, so gauge protection is a prefactor, not a substitute, for error correction.

Contributions:

- A thermal-stability derivation showing that a photonic topological gap of $\Delta \geq 15\,k_B T \approx 0.388\ \mathrm{eV}$ at $T = 300\ \mathrm{K}$ suppresses stray thermally excited anyons below $\approx 6.1\times 10^{-4}$ per $10^3$-mode device, with the corresponding mid-infrared operating frequency $\approx 93.8\ \mathrm{THz}$ derived in Section 4.1 and reported in Section 5.
- A fusion-space scaling analysis for Fibonacci anyons showing Hilbert-space growth as $\varphi^n$ with $\varphi = (1+\sqrt{5})/2 \approx 1.618$, quantifying the computational density advantage over qubit registers (Section 4.2, Section 5).
- An error-channel accounting model that splits local errors into gauge-violating (energetically suppressed by the gap) and gauge-respecting (unsuppressed) classes, deriving $p_{\mathrm{eff}} \approx f_{\mathrm{gp}}\,p$ with $f_{\mathrm{gp}} = 2/3$ for a qutrit-based local gauge constraint, and concluding that gauge protection reduces error rates by a constant factor rather than eliminating them (Section 4.3, Section 5).
- A comparison of this passive-protection budget against active fault-tolerance overheads documented in the literature, including the flag-qubit magic-state numbers of [4] and the fault-tolerant input/output error bounds of [3] (Section 4.4, Section 5).
- An identification of the falsifiers and binding engineering constraints for the synthetic-vacuum conjecture, including the specific observation that would refute the thermal-stability claim (Sections 6 and 7).

The analysis here may also bear on classical fault-tolerant system synthesis, where fault-tolerant mechanisms are inserted as pattern choices under a fault hypothesis and solved as a game [2], and on reliability modeling for many-core interconnect, where fault models and mitigation strategies are catalogued for 2D bus-based and 3D network-on-chip systems [5]; in both cases the question of whether a structural constraint reduces or relocates faults is the same question this paper asks of gauge symmetry.

## 2. Background and Related Work

**Active fault tolerance and its overhead.** The standard framework of fault-tolerant quantum computation rests on quantum error-correcting codes, which must be designed around two quantum-specific obstacles: the no-cloning theorem, which forbids protecting an unknown state by copying it, and the collapse of the state under measurement of an encoded block [1]. The same source emphasizes that uncontrolled error propagation during circuit execution can overwhelm a code, which is why fault-tolerant circuit design, not just code existence, is the operative discipline [1]. Every scheme built in this framework pays an overhead tax at the point where universality is restored. Because transversal gates can never cover a universal set (Eastin–Knill, as cited within [4]), non-Clifford resources must be prepared fault-tolerantly; the flag-qubit scheme of [4] prepares magic states directly with ten qubits, an acceptance rate around $80\%$, and logical error rates near $10^{-4}$ at physical error rates near $3\times 10^{-3}$, an improvement of orders of magnitude over distillation in some error regimes but still a resource-consuming active procedure [4]. On the correction side, flag techniques detect high-weight errors from a few faults using few ancillas, and the distinguishability of the resulting fault set depends on circuit structure, gate ordering, and the choice of stabilizer generators [6]. These works define the baseline against which any "passive" protection claim must be measured: the passive scheme must beat $(2/3)p$-style prefactor protection plus whatever residual correction remains.

**Fault tolerance as a boundary problem.** In distributed and input/output settings, noise at the first and last circuit layers is unavoidable, and the best achievable fault-tolerant realization of a circuit with quantum input/output reproduces the ideal circuit up to residual noisy channels on the input and output systems, with detrimental effects characterized as adversarial or local stochastic channels and diamond-norm bounds of the form $O(\theta\sqrt{(c\delta)^k})$ for state preparation [3]. This result matters for the synthetic-vacuum conjecture because any photonic device must inject and extract quantum information through its boundary—the very edge where the anyons live—so the boundary-noise results of [3] describe exactly the interface where gauge protection is weakest.

**Passive and structural protection proposals.** The non-Archimedean quantum architecture program proposes replacing continuous (Archimedean) state spaces with $p$-adic, ultrametric ones, arguing that the strong triangle inequality natively absorbs low-energy perturbations and that passive geometric fault tolerance was sustained over $10^5$ operational cycles in simulation, with the caveat, stated in that work itself, that the exactly $1.0$ simulated fidelity is an artifact of Boolean threshold dynamics and physical substrates would yield fidelities of roughly $0.999$ [7]. That work also argues that passive geometric protection shifts the energy profile from active microwave pulses to static power, moving thermal dissipation below cryogenic cooling limits [7]. The synthetic-vacuum conjecture is structurally analogous—protection from geometry rather than feedback—but operates in real space with a spectral gap rather than in number space with an ultrametric, and this paper's error accounting (Section 4.3) applies the same skepticism that work applies to itself: simulated threshold behavior is not physical gap behavior.

**Computation by physics.** The Inverted Church-Turing-Deutsch framework treats computation as the time evolution of engineered Hamiltonians, distinguishing Class A (Ising-based optimization) from Class B (spectral synthesis), and validates scaling claims in silico over $N=3$ to $12$ spin variables with $20$ replicates per size, using synthetic relaxation data [10]. The framework explicitly acknowledges thermodynamic constraints on physical realization [10], which is the same constraint this paper quantifies for the photonic case. The morphological-computing framework proposes encoding computational results as vectors of Chern numbers in moiré superlattices, dissolving the serial Chinese-Remainder-Theorem reconstruction bottleneck of Residue Number System arithmetic, and grounds computation in relaxation of a constrained physical system to a minimum-energy ground state [8]. That grounding is directly relevant: a synthetic vacuum that hosts anyons in its ground-state sector is a computation-by-relaxation device in exactly the sense of [8], and the same source's warning—via its cited critique literature—that claims of physical computation risk unverifiability without a formal process-to-computation map [8] applies with full force to braiding-based logic, where the map is the braid group representation.

**Symmetry as an operational resource.** The classification of topological phases by generalized symmetries, described by fusion categories rather than groups, provides the language in which non-Abelian anyon content is specified [9]. That work operationalizes these abstract structures into falsifiable protocols for Fractional Chern Insulators in moiré superlattices, proposing the anyon density-wave halo and establishing, through its reported ANOVA simulations with F-statistics in the hundreds, the halo radius as a high-fidelity proxy for the quantum dimension [9]. It also extends the diagnostic to domain walls, predicting structured screening charge along the wall measurable in imaging and transport [9]. For the present conjecture, this matters twice: first, the quantum dimension $\varphi$ of Fibonacci anyons is the quantity whose measurement would confirm the edge sector; second, the halo protocol of [9] is a template for the experimental falsifier this paper proposes in Section 7.

**Classical fault-tolerant synthesis and fault modeling.** In embedded-systems synthesis, fault tolerance is treated as the algorithmic insertion of predefined fault-tolerant mechanism patterns under an explicit fault hypothesis, translated into a distributed game and solved with incomplete search; the prototype engine reports search results in about $3$ seconds and constraint solving within $1$ second on small examples, with the authors noting that exponential blowups from variables to states remain unavoidable [2]. The structural lesson for the synthetic-vacuum design flow is that fault tolerance must be specified as a hypothesis plus a mechanism pool before synthesis; a gauge structure is precisely such a mechanism, and Section 4.3 evaluates it as one. On the modeling side, the survey of fault models and fault-tolerance methods for 2D bus-based multi-core and 3D network-on-chip many-core systems frames reliability as requiring explicit fault and failure models before mitigation can be strategized [5]; the present paper follows the same discipline by enumerating error channels by their gauge transformation property before claiming suppression.

## 3. Methods

This is an analytical feasibility study. No experiment, simulation on hardware, or measurement was performed; all numbers below are derived from stated inputs by explicit arithmetic, or labeled as assumptions.

**Model.** We model the synthetic vacuum as a two-dimensional photonic lattice whose bulk band structure is gapped by $\Delta$, with a topologically ordered edge sector supporting anyonic excitations with fusion rules of the Fibonacci type: two anyon types $\{1, \tau\}$ with $\tau \times \tau = 1 + \tau$ and quantum dimension $d_\tau = \varphi$. The conjectured mechanism is an engineered gauge constraint—locally, a Gauss-law-like projector $G_i$ at each site $i$ enforcing $G_i \lvert \psi \rangle = \lvert \psi \rangle$—such that physical states are gauge-invariant and local gauge-violating operators cost energy at least $\Delta$.

**Assumptions.** We make the following assumptions, each stated explicitly because no source supplies it:

- (A1) The lattice supports a gapped topological phase with Fibonacci edge anyons; this is the conjecture under test, not a result.
- (A2) The device operates at $T = 300\ \mathrm{K}$.
- (A3) The device contains $N_{\mathrm{mode}} = 10^3$ photonic modes, each with $g = 2$ internal states contributing to the anyon sector; this is a small-device scale chosen for concreteness.
- (A4) Local physical error processes occur at a per-mode rate $p$ per operation, left symbolic; the gauge structure partitions them into gauge-violating and gauge-respecting classes.
- (A5) The local Hilbert space is qutrit-like, $\dim \mathcal{H}_{\mathrm{local}} = 3$, with a gauge-invariant subspace of dimension $2$; this models the minimal gauge constraint that removes one local degree of freedom.

**Derivation procedure.** Section 4.1 computes the thermal stability condition from the Boltzmann factor; Section 4.2 computes the Fibonacci fusion-space scaling; Section 4.3 performs the error-channel accounting; Section 4.4 compares against documented active fault-tolerance overheads from [4], [6], and [3]. All arithmetic is shown step by step.

## 4. Analysis

### 4.1 Thermal stability: the required gap

**Input numbers.** Boltzmann constant $k_B = 8.617333\times 10^{-5}\ \mathrm{eV/K}$ (physical constant); operating temperature $T = 300\ \mathrm{K}$ (Assumption A2); Planck constant $h = 4.135668\times 10^{-15}\ \mathrm{eV \cdot s}$ (physical constant); speed of light $c = 2.99792458\times 10^8\ \mathrm{m/s}$ (physical constant); number of modes $N_{\mathrm{mode}} = 10^3$ and internal states $g = 2$ (Assumption A3).

**Step 1: thermal energy.**

$$k_B T = (8.617333\times 10^{-5}) \times 300 = 2.5852\times 10^{-2}\ \mathrm{eV} = 25.85\ \mathrm{meV}.$$

**Step 2: thermal occupation of a gapped mode.** A bosonic mode of energy $\Delta$ above the band edge has thermal occupation

$$\bar{n}(\Delta) = \frac{1}{e^{\Delta / k_B T} - 1}.$$

At $\Delta = 10\,k_B T$: $e^{10} = 22026.47$, so $\bar{n} = 1/(22026.47 - 1) = 1/22025.47 = 4.540\times 10^{-5}$.

**Step 3: probability of at least one stray thermal anyon.** Treating the $N_{\mathrm{mode}} \cdot g = 2000$ modes as independent, the probability that at least one thermally excited anyon exists is, to leading order in $\bar{n}$,

$$P_{\mathrm{thermal}} \approx N_{\mathrm{mode}} \cdot g \cdot \bar{n}(\Delta).$$

At $\Delta = 10\,k_B T$: $P_{\mathrm{thermal}} \approx 2000 \times 4.540\times 10^{-5} = 9.08\times 10^{-2}$. This is too high for a computation: roughly one computation in eleven would begin with a stray anyon.

At $\Delta = 15\,k_B T$: $e^{15} = 3.269017\times 10^{6}$, so $\bar{n} = 1/(3269017 - 1) = 3.059\times 10^{-7}$, and

$$P_{\mathrm{thermal}} \approx 2000 \times 3.059\times 10^{-7} = 6.12\times 10^{-4}.$$

**Step 4: the gap in physical units.** At $\Delta = 15\,k_B T$:

$$\Delta = 15 \times 2.5852\times 10^{-2}\ \mathrm{eV} = 0.38778\ \mathrm{eV}.$$

The corresponding photon frequency and free-space wavelength:

$$\nu = \frac{\Delta}{h} = \frac{0.38778}{4.135668\times 10^{-15}} = 9.376\times 10^{13}\ \mathrm{Hz} = 93.76\ \mathrm{THz},$$

$$\lambda = \frac{c}{\nu} = \frac{2.99792458\times 10^8}{9.376\times 10^{13}} = 3.198\times 10^{-6}\ \mathrm{m} \approx 3.20\ \mu\mathrm{m}.$$

The required operating window is therefore the mid-infrared. We note that the mid-infrared is a technologically developed spectral region for photonic integrated circuits, which is favorable for feasibility; we make no claim about specific device platforms, as no source supplies one.

### 4.2 Fibonacci fusion-space scaling

**Input.** Fibonacci fusion $\tau \times \tau = 1 + \tau$ implies the quantum dimension $d_\tau = \varphi$, where $\varphi$ is the positive root of $\varphi^2 = \varphi + 1$:

$$\varphi = \frac{1 + \sqrt{5}}{2} = \frac{1 + 2.2360680}{2} = 1.6180340.$$

**Step 1: fusion-space growth.** The dimension of the fusion space of $n$ $\tau$ anyons with total charge $\tau$ grows as $\varphi^{n}$ up to polynomial prefactors. For $n = 100$ anyons:

$$\varphi^{100} = e^{100 \ln \varphi} = e^{100 \times 0.4812118} = e^{48.12118}.$$

Computing: $e^{48} = 7.0167\times 10^{20}$ (since $e^{48} = e^{50}/e^{2} = 5.1847\times 10^{21}/7.3891 = 7.0167\times 10^{20}$), and $e^{0.12118} = 1.1288$, so

$$\varphi^{100} \approx 7.0167\times 10^{20} \times 1.1288 = 7.920\times 10^{20}.$$

**Step 2: comparison with a qubit register.** A register of $n = 100$ qubits spans $2^{100} = 1.2677\times 10^{30}$ states; the fusion space is smaller in raw dimension but is not the relevant comparison. The relevant point is that the fusion space is the *protected* computational space: its dimension grows exponentially while the system's local Hilbert space grows only polynomially in $n$ for a fixed lattice, meaning the anyonic encoding packs an exponentially large protected space into a physical footprint that scales linearly with anyon number. The ratio of protected-space dimension to anyon number for $n = 100$:

$$\frac{\varphi^{100}}{n} = \frac{7.920\times 10^{20}}{100} = 7.92\times 10^{18}\ \text{protected states per anyon}.$$

**Step 3: braid group richness.** The braid group on $n$ strands has $(n-1)!$ generators' words of arbitrary length; for Fibonacci anyons, braiding alone is dense in the unitary group on the fusion space (universality), so no extra non-Clifford resource—no magic states of the kind prepared in [4]—is required in principle. This is the structural advantage the conjecture targets: the universality tax paid by stabilizer codes via magic-state preparation [4] is, for Fibonacci anyons, absorbed into the physics of the anyons themselves. Whether the photonic lattice actually realizes this anyon content is Assumption A1 and remains unproven here.

### 4.3 Error-channel accounting: suppression or relocation?

This is the central analysis. The question is whether the gauge constraint reduces the error rate or merely moves errors into a sector it cannot touch.

**Setup (Assumptions A4, A5).** Local Hilbert space dimension $q = 3$; gauge-invariant subspace dimension $q_{\mathrm{inv}} = 2$. A local error operator $E$ acting on one mode either commutes with the Gauss-law projector (gauge-respecting) or anticommutes with it (gauge-violating). We assume, as a maximally favorable partition for the conjecture, that the gauge-violating operators constitute the fraction

$$f_{\mathrm{gv}} = \frac{q - q_{\mathrm{inv}}}{q} = \frac{3-2}{3} = \frac{1}{3},$$

and gauge-respecting operators the fraction

$$f_{\mathrm{gp}} = \frac{q_{\mathrm{inv}}}{q} = \frac{2}{3}.$$

**Step 1: fate of gauge-violating errors.** A gauge-violating error creates an excitation costing at least the gap $\Delta$. Its thermal activation weight is the Boltzmann factor $e^{-\Delta/k_B T}$. At the operating point $\Delta = 15\,k_B T$ (Section 4.1):

$$e^{-15} = 3.059\times 10^{-7}.$$

The effective rate of gauge-violating errors is then

$$p_{\mathrm{gv}} = f_{\mathrm{gv}} \cdot p \cdot e^{-\Delta/k_B T} = \frac{1}{3} \cdot p \times 3.059\times 10^{-7} = 1.020\times 10^{-7}\, p.$$

**Step 2: fate of gauge-respecting errors.** A gauge-respecting error acts within the gauge-invariant subspace and costs no gap energy. The gauge structure provides no suppression:

$$p_{\mathrm{gp}} = f_{\mathrm{gp}} \cdot p = \frac{2}{3}\,p = 0.6667\,p.$$

**Step 3: total effective error rate.**

$$p_{\mathrm{eff}} = p_{\mathrm{gp}} + p_{\mathrm{gv}} = 0.6667\,p + 1.020\times 10^{-7}\,p \approx 0.6667\,p.$$

**Interpretation.** The gauge constraint suppresses one-third of error channels by a factor of $e^{15} \approx 3.27\times 10^{6}$, but the remaining two-thirds pass through essentially untouched: $p_{\mathrm{eff}} \approx (2/3)p$. The gauge structure is a constant-factor reducer, not an eliminator. This is the "relocation" answer to the conjecture's third question: gauge symmetry genuinely suppresses the channels it can see (gauge-violating ones) and is blind to the channels it cannot (gauge-respecting ones, including dephasing within the fusion space and edge-coupled noise of the kind characterized in [3]).

**Step 4: what residual correction must achieve.** To reach a logical error rate of $10^{-4}$ per operation—the level the flag-qubit magic-state scheme attains at physical error rate $3\times 10^{-3}$ with active machinery [4]—a purely gauge-protected device with $p_{\mathrm{eff}} \approx (2/3)p$ would need

$$p \leq \frac{10^{-4}}{2/3} = 1.5\times 10^{-4}.$$

That is, the physical photonic error rate would have to be $1.5\times 10^{-4}$ per mode per operation, twenty times better than the $3\times 10^{-3}$ at which the active scheme of [4] already achieves $10^{-4}$. The passive scheme does not remove the correction requirement; it shifts the burden to raw material quality.

### 4.4 Comparison with active fault-tolerance overheads

**Input numbers from the literature.** From [4]: the flag-qubit magic-state preparation circuit uses a total of $10$ qubits, accepts around $80\%$ of the time, and reaches logical error rates near $10^{-4}$ at physical error rates near $3\times 10^{-3}$. From [6]: flag-based fault-tolerant error correction reduces ancilla counts relative to the Shor scheme, which requires as many ancillas as the maximum stabilizer generator weight. From [3]: fault-tolerant realizations of circuits with quantum input/output inevitably leave residual noisy channels on input and output, with state-preparation diamond-norm error bounded as $O(\theta\sqrt{(c\delta)^k})$.

**Step 1: overhead comparison per logical operation.** The active route to one reliable non-Clifford operation costs, at the level-1 flag scheme, one magic state per attempt with acceptance $0.80$, so the expected number of preparation attempts per accepted state is

$$\frac{1}{0.80} = 1.25\ \text{attempts},$$

each consuming a $10$-qubit circuit. The passive route, if the synthetic vacuum worked as conjectured, would cost zero preparation overhead because braiding is intrinsically universal—but pays instead the raw-error requirement $p \leq 1.5\times 10^{-4}$ derived in Section 4.3, Step 4.

**Step 2: boundary exposure.** The residual input/output channels of [3] are exactly the vulnerability of an anyonic device: anyons live on the edge, and every injection or readout touches the edge. The bound $O(\theta\sqrt{(c\delta)^k})$ of [3] shows that even ideal fault-tolerant design leaves boundary noise that scales with the circuit's distance-$k$ structure; a gauge-protected edge has no additional mechanism against it, because boundary coupling is precisely a gauge-respecting process in the sense of Section 4.3. We therefore expect the effective boundary error rate of a synthetic-vacuum device to scale as $(2/3)p_{\mathrm{edge}}$ with no exponential suppression, where $p_{\mathrm{edge}}$ is the edge-coupling error rate—an unquantified quantity that no available source supplies, and which we flag as the key open parameter.

**Step 3: energy comparison, qualitative with one computed anchor.** The non-Archimedean architecture literature argues that passive geometric protection replaces active microwave surveillance with static power, lowering the thermal dissipation envelope below cryogenic cooling limits [7]. The same logic applies to a gapped photonic vacuum: no continuous syndrome extraction is needed for the gauge-violating sector because the gap does the suppression. However, the gauge-respecting sector of Section 4.3 still requires either extremely low raw error ($p \leq 1.5\times 10^{-4}$) or some active correction, so the energy advantage is partial, not total. We do not compute an energy figure because no source supplies the per-operation energy of photonic mode control, and inventing one would violate the paper's evidentiary standard.

## 5. Results

All