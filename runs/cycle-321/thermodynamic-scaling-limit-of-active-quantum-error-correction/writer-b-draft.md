# A Kapitza-Limited Critical Qubit Density for Active Quantum Error Correction

## Abstract

Gate-based quantum computing relies on active quantum error correction (QEC), in which syndrome extraction runs continuously and every control pulse dissipates heat into a cryogenic substrate whose extraction capacity is finite. The field lacks an explicit criterion stating at what qubit density this dissipation overwhelms the thermal link between the quantum plane and its refrigerator. We derive such a criterion from a modified Caldeira-Leggett picture in which control-pulse dissipation at rate $\nu_{\rm cycle}$ and energy $E_{\rm pulse}$ per qubit is balanced against Kapitza thermal conductance $H_K(T) = h_{K0}T^3$ into a substrate of area $A$. The model yields a critical density $n_c = H_K(T)\,\Delta T_{\rm max}/(\nu_{\rm cycle}E_{\rm pulse})$ and a device-level critical count $N_c = P_{\rm MC}/(\nu_{\rm cycle}E_{\rm pulse})$. Using a dilution-refrigerator mixing-chamber budget of $50\ \mu{\rm W}$ and a syndrome cycle of $\tau_c = 1\ \mu{\rm s}$, we find that at $E_{\rm pulse} = 10^{-15}$ J the local Kapitza limit is $n_c = 2.7\times 10^{8}\ {\rm m}^{-2}$ (center-to-center spacing $61\ \mu{\rm m}$), which a $10^{6}$-qubit chip of area $1\ {\rm cm}^{2}$ exceeds by a factor of $\approx 37$; at $E_{\rm pulse} = 10^{-9}$ J the limit collapses to $270\ {\rm m}^{-2}$. We further derive a thermal-runaway threshold and show the feedback gain required to trigger it at $300$ mK is $81\ {\rm W\,m^{-2}K^{-1}}$. The result converts QEC scalability from a decoding problem into a stated thermal-architecture constraint and identifies per-pulse energy as the decisive measurable parameter.

## 1. Introduction

Superconducting and other gate-based quantum processors protect their information by active quantum error correction: every logical qubit is encoded in many physical qubits, and a classical control layer measures syndromes and applies feedback on a fixed cycle, indefinitely. This activity is not free. Each syndrome round drives microwave pulses, switches Josephson elements, and dissipates energy in resistive elements and in the substrate itself, all within a cryostat whose cooling power at the mixing chamber is physically capped — for standard commercial dilution refrigerators near $10$ mK, at roughly $50\ \mu{\rm W}$, against roughly $1$ W available at the $4$ K stage, a ratio of about $2\times 10^{4}$ [11]. The engineers who design these cryostats, the wiring that feeds them, and the roadmaps that promise million-qubit devices currently lack a closed-form criterion that tells them at what qubit density, pulse energy, and cycle rate the quantum plane overheats. Today the question is answered, when it is answered at all, by per-design thermal budgets assembled ad hoc; a roadmap decision made without such a criterion can commit to a qubit density that no refrigerator can sustain.

The cost of not having this criterion is concrete. Wiring alone already imports heat: every qubit's control and readout path bridges $300$ K to $10$ mK, and because electrical and thermal conductivity are coupled by the Wiedemann-Franz law, the parasitic heat load scales linearly with qubit count whether or not the qubits are active [11]. On top of that standing load, active QEC adds a dissipation term that scales with qubit count, cycle rate, and per-pulse energy. Scaling analyses of the QEC resource burden show what this means at the logical level: a distance-21 surface code running at a $1\ \mu{\rm s}$ cycle moves $4.40\times 10^{8}$ syndrome bits per second per logical qubit and, under a stated $10^{-9}$ J per-qubit-per-cycle assumption, costs $1.8501\times 10^{-5}$ J per logical operation — about $6.4\times 10^{18}$ times the Landauer limit at 300 mK [10]. If the paper's result holds, architects gain a single inequality that partitions design space into sustainable and unsustainable regions before any cryostat is built, and the field gains one clearly identified measurement target — per-pulse dissipated energy at millikelvin temperature — whose value decides whether dense active QEC is thermodynamically viable at all.

The physical mechanism we formalize is localized. Heat deposited by control pulses must cross the solid-solid interface between the qubit-bearing film and its substrate through the Kapitza conductance, which is small at millikelvin temperatures and scales as $T^3$. When the areal density of actively cycled qubits pushes the local heat flux beyond what this interface can carry within a permitted temperature rise $\Delta T_{\rm max}$, the local temperature climbs, quasiparticle populations grow, decoherence accelerates, and the correction duty cycle — and with it the heat load — increases. We show that this feedback has a sharp threshold, so the failure is a transition rather than a graceful degradation. This motivates, though it does not in this paper demonstrate, interest in passive protection strategies that avoid continuous control dissipation altogether [8], [9].

Our contributions are:

- A derivation of the critical qubit density $n_c = H_K(T)\,\Delta T_{\rm max}/(\nu_{\rm cycle}E_{\rm pulse})$ from a heat-balance model coupling control-pulse dissipation to Kapitza substrate response, with all inputs stated (Section 3, evaluated in Section 4).
- Numerical values of $n_c$ and of the corresponding critical qubit spacing at three per-pulse energies spanning six orders of magnitude, and a comparison against a projected million-qubit chip density showing an exceedance factor of $\approx 37$ even at the most optimistic pulse energy (Section 4, reported in Section 5).
- A device-level critical count $N_c = P_{\rm MC}/(\nu_{\rm cycle}E_{\rm pulse})$ against the $50\ \mu{\rm W}$ mixing-chamber budget, which bounds the whole-chip problem independently of the local interface analysis (Section 4).
- An explicit thermal-runaway criterion $g_c = h_{K0}T_*^2(4T_* - 3T_b)$ for the feedback gain $g = \partial P/\partial T$, with the numerical threshold $81\ {\rm W\,m^{-2}K^{-1}}$ at $T_* = 0.3$ K, $T_b = 0.1$ K (Section 4).
- An assessment of what would falsify the model, which engineering constraints bind first, and the smallest next calculation or experiment that would de-risk it (Sections 6 and 7).

## 2. Background and Related Work

The theoretical foundations of QEC are mature. Early surveys establish the classical-to-quantum transfer of coding ideas: redundancy, encoding, syndrome extraction, and correction, with the binary symmetric channel as the classical prototype and stabilizer codes as the quantum workhorse [4]. Introductory treatments show that the first codes — Shor's 9-qubit code and Steane's 7-qubit code — protect one logical qubit against arbitrary single-qubit errors, that general noise on qubits digitizes into Pauli errors, and that the stabilizer formalism due to Gottesman generated most subsequent code constructions [5]. A modern overview frames QEC as storing information in a code subspace of a larger Hilbert space, designed so that the most common errors move the state into an orthogonal, correctable error space [6]. These works establish that codes exist and under what conditions they correct; none of them prices the continuous physical cost of running the correction machinery, which is the gap this paper addresses.

The cost of running a code is the subject of a recent explicit scaling analysis [10]. That work computes, with every input stated, that a target logical error rate $P = 10^{-12}$ at physical error rate $p = 10^{-3}$ demands a distance-21 surface code with $881$ physical qubits per logical qubit, $9240$ syndrome bits per logical operation ($4.40\times 10^{8}$ bits per second per logical qubit at $\tau_c = 1\ \mu{\rm s}$), and $1.8501\times 10^{-5}$ J per logical operation under a $10^{-9}$ J per-qubit-per-cycle energy assumption — $6.445\times 10^{18}$ times the Landauer limit at 300 mK [10]. Its discussion concludes that active QEC converts a hardware error-rate problem into a throughput-and-energy problem and identifies per-qubit energy as the critical measurement target for the field [10]. We take its cycle rate and per-pulse energy as the central inputs of our thermal model and add the substrate heat-transfer physics that its accounting stops short of.

The thermodynamic framing has precedents. A study of thermodynamic constraints on scalable quantum computing documents the scaling asymmetry that motivates our device-level bound: mixing-chamber cooling power capped near $50\ \mu{\rm W}$ at $10$ mK versus roughly $1$ W at the $4$ K pulse-tube stage, a factor near $2\times 10^{4}$, and a wiring bottleneck in which each qubit's coaxial signal path imports heat that scales linearly with qubit count, with the Wiedemann-Franz law tying electrical conductivity — which the signal path needs — to the thermal conductivity the cold stage must not receive [11]. That work argues for an architectural inversion, offloading control electronics to the warmer stage; our analysis complements it by showing that even with perfect offloading, the dissipation generated at the quantum plane itself is limited by the Kapitza interface, a term absent from its accounting.

A stronger thesis appears in work on the thermodynamic viability of universal quantum computation, which argues that active error correction faces a "thermodynamic wall" — a phase transition where entropy produced by control operations overwhelms the system — and quantifies a "Protection Deficit" of approximately $10^{12}$ between biological metabolic efficiency and the energy cost of state-of-the-art engineered quantum processors [9]. That work proposes replacing forced discrete control with geodesic evolution on a quantum information manifold [9]. Our contribution is narrower and more conservative: we do not need the full geodesic program to locate a transition, because a two-term heat balance with a $T^3$ interface conductance already produces a critical density; we thereby give the thermodynamic-wall intuition a concrete, checkable formula.

On the protocol side, continuous-time QEC replaces discrete syndrome rounds with continuous weak measurement and feedback, treating both noise and correction as continuous processes and analyzing them through the subsystem principle; its quantum-jump scheme reaches a quasi-equilibrium code-space fidelity that estimates performance, and its outlook flags the construction of optimal protocols and non-Markovian decoherence as open problems [1]. For our model, continuous-time operation changes the meaning of $\nu_{\rm cycle}$ from a discrete round rate to a continuous measurement rate, but the dissipation-versus-Kapitza balance is unchanged in form. Entanglement-assisted codes allow the sender to append pre-shared ebits before encoding, extending the stabilizer formalism so that quantum codes can be built from classical linear codes without the dual-containing constraint, and in many cases improving rate or correctable-error count [2]. Entanglement assistance reduces ancilla overhead per logical qubit and therefore the number of actively cycled physical qubits — it shifts the prefactor of our heat load, not the existence of the Kapitza limit. Error suppression in adiabatic quantum computation faces a structurally analogous problem: its error-handling analysis introduces protected Hamiltonians and local cooling as techniques for correcting errors without circuit-model gates or syndrome measurements, but its authors state that they cannot prove a threshold theorem for adiabatic fault tolerance because controlling the encoded computation with slowly varying Hamiltonians appears to require high-weight Hamiltonians [7]. Their "local cooling" is, in our language, an active heat-management term with its own dissipation budget, so the adiabatic paradigm does not escape the balance we derive; it relocates it.

Two further works bear on alternatives to active correction. A p-adic architecture proposal argues that continuous analog fragility in Archimedean state spaces forces massive active correction overheads, and reports simulated passive fault tolerance over $10^{5}$ operational cycles with no continuous logical degradation, while noting that the exactly $1.0$ simulated fidelity is an artifact of Boolean threshold simulation and that physical substrates would show fidelities near $0.999$ [8]. Its evaluation metrics explicitly benchmark against surface-code operational requirements for projecting energetic efficiency and thermodynamic scaling [8]; our $n_c$ supplies exactly the kind of thermal baseline such a comparison needs, though we make no claim for the p-adic hardware itself. Finally, a quantum-processor demonstration of thermodynamic recycling shows that failure branches of algorithms, usually discarded, form an athermal bath that can lower the heat dissipated by erasure below the tight thermal bound $Q_{\rm tight}$, with the gain analyzed as a function of branch entropy and demonstrated on hardware whose calibrated single- and two-qubit gate times are $32$ ns and $68$ ns [3]. Recycling attacks the erasure-cost side of the ledger; our analysis shows the control-pulse side remains, so the two are complementary rather than competing.

## 3. Methods

### 3.1 Model

We model one qubit-bearing chip of area $A$ at bath (mixing-chamber) temperature $T_b$, carrying $N_q$ actively cycled physical qubits at areal density $n = N_q/A$. Each qubit dissipates, per syndrome cycle of duration $\tau_c$, an energy $E_{\rm pulse}$ in control and readout pulses, plus an ohmic term $I^2R\,\tau_c$ in its bias or signal line. The cycle rate is $\nu_{\rm cycle} = 1/\tau_c$. The areal power density is then

$$p = n\,\nu_{\rm cycle}\left(E_{\rm pulse} + I^2 R\,\tau_c\right) = n\,\nu_{\rm cycle}\,E_{\rm pulse} + n\,I^2 R.$$

Heat leaves the quantum plane only through the film-substrate interface, whose Kapitza conductance per unit area we take in the standard low-temperature form

$$H_K(T) = h_{K0}\,T^3,$$

with $h_{K0}$ a material-dependent constant. The local steady-state temperature rise is

$$\Delta T_{\rm local} = \frac{p}{H_K(T)} = \frac{n\,\nu_{\rm cycle}\,E_{\rm pulse} + n\,I^2R}{h_{K0}T^3}.$$

This is the modified Caldeira-Leggett picture promised in the title of the model: the control pulses are a classical dissipative bath coupled to the qubit, and the substrate is the low-temperature reservoir whose response is governed by the interface conductance rather than by bulk thermal conductivity. The qubit's decoherence rate increases with local temperature (through, e.g., quasiparticle population), which raises the required correction activity; we treat this feedback in Section 4.4.

### 3.2 Definitions of the two critical quantities

We define two distinct limits.

**Local (Kapitza) limit.** The plane may not exceed a permitted temperature rise $\Delta T_{\rm max}$ above the operating point $T$, set by the decoherence budget. Solving $\Delta T_{\rm local} \le \Delta T_{\rm max}$ for $n$ gives the critical density

$$n_c = \frac{h_{K0}\,T^3\,\Delta T_{\rm max}}{\nu_{\rm cycle}\,E_{\rm pulse} + I^2R} \approx \frac{H_K(T)\,\Delta T_{\rm max}}{\nu_{\rm cycle}\,E_{\rm pulse}},$$

where the approximation drops the ohmic term when $\nu_{\rm cycle}E_{\rm pulse} \gg I^2R$ (checked case by case in Section 4). The corresponding critical center-to-center spacing is $a_c = n_c^{-1/2}$.

**Device (refrigerator) limit.** Independently of how well the interface conducts, the whole chip's dissipation cannot exceed the mixing-chamber cooling power $P_{\rm MC}$:

$$N_c = \frac{P_{\rm MC}}{\nu_{\rm cycle}\,E_{\rm pulse} + I^2R}.$$

The local limit binds first when $N_c/A < n_c$; the device limit binds first otherwise.

### 3.3 Inputs and their status

Every input below is either taken from a cited work or explicitly labeled an assumption of this paper.

- $P_{\rm MC} = 50\ \mu{\rm W} = 5\times 10^{-5}$ W: mixing-chamber cooling power of standard commercial dilution refrigerators near 10 mK [11].
- $\tau_c = 1\ \mu{\rm s}$, i.e., $\nu_{\rm cycle} = 10^{6}\ {\rm s}^{-1}$: syndrome-cycle time used in the surface-code scaling analysis [10].
- $E_{\rm pulse}$: per-qubit-per-cycle dissipated energy. The scaling analysis adopts $10^{-9}$ J as its stated assumption [10]; because that value is itself an assumption there and is likely pessimistic for optimized pulses, we evaluate $n_c$ at three values, $E_{\rm pulse} \in \{10^{-15}, 10^{-12}, 10^{-9}\}$ J, treating all three as scenario assumptions of this paper.
- $h_{K0} = 10^{3}\ {\rm W\,m^{-2}\,K^{-4}}$: Kapitza prefactor. **Assumption of this paper.** It yields $H_K(1\ {\rm K}) = 10^{3}\ {\rm W\,m^{-2}K^{-1}}$, a representative order of magnitude for solid-solid interfaces at 1 K; the $T^3$ scaling is the standard low-temperature form. Section 6 quantifies the sensitivity of the results to this prefactor.
- $T = 0.3$ K operating point, $T_b = 0.1$ K bath temperature for the runaway analysis: **assumptions of this paper**, chosen to sit in the millikelvin regime where the cited cooling budgets apply [11].
- $\Delta T_{\rm max} = 10$ mK: permitted temperature rise. **Assumption of this paper**, representing a decoherence budget of a few percent of the operating temperature.
- $I = 1\ \mu{\rm A}$, $R = 50\ \Omega$: bias-line current and impedance. **Assumptions of this paper**, used only to check that the ohmic term is subdominant.
- Million-qubit reference density: we assume a target of $N_q = 10^{6}$ qubits on a chip of area $A = 1\ {\rm cm}^{2} = 10^{-4}\ {\rm m}^{2}$, i.e., $n_{\rm target} = 10^{10}\ {\rm m}^{-2}$. **Assumption of this paper**, used only as a comparison point.
- Superconducting gap parameter for the runaway analysis: $\Delta/k_B = 3.5$ K. **Assumption of this paper**, a representative superconducting gap scale; no result in Section 5 depends on its precise value (Section 6).

### 3.4 Method of computation

All results in Section 4 follow from the closed-form expressions of Section 3.2 by direct substitution of the inputs of Section 3.3, with every arithmetic step shown. No simulation, measurement, or hardware experiment is performed or reported in this paper; the heat-diffusion study over dense arrays that the research program calls for is specified as a proposal in Section 7.

## 4. Analysis

### 4.1 Kapitza conductance at the operating point

With $h_{K0} = 10^{3}\ {\rm W\,m^{-2}K^{-4}}$ and $T = 0.3$ K:

$$H_K(0.3\ {\rm K}) = h_{K0}T^3 = 10^{3} \times (0.3)^3 = 10^{3} \times 2.7\times 10^{-2} = 27\ {\rm W\,m^{-2}K^{-1}}.$$

For reference at $T_b = 0.1$ K: $H_K(0.1\ {\rm K}) = 10^{3}\times 10^{-3} = 1\ {\rm W\,m^{-2}K^{-1}}$. The interface is therefore roughly $27$ times more conductive at 300 mK than at 100 mK; the $T^3$ law makes the thermal margin collapse rapidly as operating points are lowered.

### 4.2 Ohmic term check

With the assumptions $I = 1\ \mu{\rm A} = 10^{-6}$ A and $R = 50\ \Omega$:

$$I^2R = (10^{-6})^2 \times 50 = 10^{-12}\times 50 = 5\times 10^{-11}\ {\rm W}.$$

Compare with the pulse term $\nu_{\rm cycle}E_{\rm pulse}$ at the smallest scenario energy $E_{\rm pulse} = 10^{-15}$ J:

$$\nu_{\rm cycle}E_{\rm pulse} = 10^{6}\times 10^{-15} = 10^{-9}\ {\rm W},$$

which is $10^{-9}/(5\times 10^{-11}) = 20$ times the ohmic term. At $E_{\rm pulse} = 10^{-12}$ J the ratio is $2\times 10^{4}$; at $10^{-9}$ J it is $2\times 10^{7}$. The ohmic term is at most a $5\%$ correction in the most favorable scenario and negligible elsewhere, so we drop it and use $n_c = H_K(T)\Delta T_{\rm max}/(\nu_{\rm cycle}E_{\rm pulse})$ throughout, noting the bound is then optimistic by at most $5\%$.

### 4.3 Critical density and critical spacing

Numerator, common to all scenarios:

$$H_K(T)\,\Delta T_{\rm max} = 27\ {\rm W\,m^{-2}K^{-1}} \times 10^{-2}\ {\rm K} = 0.27\ {\rm W\,m^{-2}}.$$

**Scenario 1: $E_{\rm pulse} = 10^{-15}$ J.**

$$n_c = \frac{0.27}{10^{6}\times 10^{-15}} = \frac{0.27}{10^{-9}} = 2.7\times 10^{8}\ {\rm m}^{-2}.$$

Critical spacing:

$$a_c = n_c^{-1/2} = (2.7\times 10^{8})^{-1/2} = \frac{1}{1.643\times 10^{4}} = 6.09\times 10^{-5}\ {\rm m} \approx 61\ \mu{\rm m}.$$

($\sqrt{2.7\times 10^{8}}