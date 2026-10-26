# Thoughts as Quantum-Informational Hamiltonians: Coherence and Capacity Constraints on a Two-Phase Pre-Geometric Model of Cognition

## Abstract

A standing puzzle in neuroscience and quantum biology is whether any quantum degree of freedom in a warm, wet brain can remain coherent long enough to play a computational role, and no existing framework connects such receptor-scale coherence to any proposal about how spacetime itself emerges. We formalize the conjecture that cognition is a quantum-informational Hamiltonian state coupling a physical universe to a pre-geometric phase, with the Big Bang modeled as a pre-geometric-to-geometric phase transition that selects a Hamiltonian subspace. We build a two-phase model in which pre-geometric degrees of freedom are informational, the phase transition fixes which "thought" states can manifest, and biological receptors (microtubule-like, Posner-like, magnetoreception-like structures) are treated as candidate channels to the selected subspace. Using a thermal decoherence criterion, we derive that at an assumed physiological temperature of $T = 310$ K the bare thermal decoherence rate is $\Gamma_{\mathrm{th}} = 4.06 \times 10^{13}\ \mathrm{s}^{-1}$ ($\tau_{\mathrm{th}} = 2.46 \times 10^{-14}$ s), that a receptor transition of $0.2$ eV supports only $1.19$ coherent cycles, that even a $10$ eV transition supports at most $59.6$ cycles, that a $0.2$ eV receptor carries at most $3.09$ bits per mode under a Shannon-type thermal-noise assumption (cross-checked against a dimension bound of $\log_2 d = 1$ bit for $d = 2$), and that any conjectured coupling to the pre-geometric subspace must carry an energy scale above $k_B T = 26.7$ meV to avoid being driven classical. The framework yields falsifiable coherence-time and channel-capacity targets that distinguish it from standard neuroscience.

## 1. Introduction

Neuroscientists, quantum biologists, and theorists of quantum gravity all face the same unresolved question from different sides: does quantum coherence play any functional role in cognition, and if so, through what physical channel? For the experimentalist, the question costs money and time, because candidate "quantum receptors" such as microtubule-like structures, Posner-like molecules, and magnetoreception-like radical-pair systems are repeatedly proposed and repeatedly challenged on the ground that a thermal bath at body temperature destroys coherence in femtoseconds to picoseconds. For the theorist, the question blocks progress on a deeper issue: if consciousness is informational rather than mechanical, physics currently offers no formalism in which an informational state couples to the substrate from which spacetime emerges. Today the two communities cannot even agree on a shared quantity to measure, because no model specifies what a receptor would have to do — at what coherence time, at what channel capacity, at what coupling strength — for a quantum-informational account of cognition to survive.

This paper supplies that specification for one specific conjecture. The conjecture, stated as a hypothesis and not as an established result, is that cognition is not an ordinary physical process but a quantum-informational (Hamiltonian) state that couples a physical universe to a pre-geometric phase, with the Big Bang interpreted as a pre-geometric-to-geometric phase transition that "froze" which thoughts can manifest. The value of formalizing it is decision-theoretic even if the conjecture is false: the formalization produces numerical thresholds — a decoherence time, a coherent-cycle count, a channel capacity, a minimum coupling energy — that any candidate receptor must meet, and those thresholds can be checked in existing laboratory setups. If the thresholds are met by no plausible receptor, the two-phase conjecture is falsified at the receptor level and quantum biology can proceed without it; if some receptor meets them, a specific experimental program follows.

The pre-geometric side of the model is not built from nothing. A body of work already treats spacetime geometry as emergent from a non-metric informational substrate: pre-geometric gauge theories in which a Higgs-like field spontaneously breaks a spacetime symmetry and recovers Einstein–Cartan gravity in the infrared [5], and a monistic framework in which reality is a pre-geometric informational substrate structured as a Hamiltonian superposition satisfying $H|\Psi\rangle = 0$, with geometry emerging through an exact functor from information states to events [10]. On the quantum-informational side, phase transitions in quantum many-body systems have been shown to carry operational significance for information processing, so that the phase a system lands in changes what computational processes its ground state supports [2], and the information capacity of quantum communication is bounded by natural physical assumptions on the emitting devices [3]. The gap this paper fills is the coupling: none of these works derives what a biological receptor at $310$ K would have to satisfy to act as a channel between a geometric phase and a pre-geometric informational subspace.

We treat the receptor problem with the standard tool that decides whether an interaction is quantum or classical: the comparison of decoherence rates with the frequencies that define the strength of an interaction Hamiltonian. Analysis of quantum feedback shows that an interaction Hamiltonian's dynamics can be interpreted as a completely classical information exchange when the decoherence rates are comparable to the interaction frequencies, and that the separable-versus-entangling character of an interaction is quantified by the decoherence rates associated with information available in the environment [4]. We apply exactly this criterion, with the thermal bath playing the role of the environment.

The contributions are:

- A two-phase formal model (Section 3) in which a pre-geometric informational Hilbert space, a geometric phase, and a transition-selected Hamiltonian subspace are related, drawing on the spontaneous-symmetry-breaking recovery of gravity [5] and the $H|\Psi\rangle = 0$ substrate structure [10].
- A derived thermal decoherence scale for candidate receptors at $T = 310$ K, $\Gamma_{\mathrm{th}} = 4.06 \times 10^{13}\ \mathrm{s}^{-1}$ and $\tau_{\mathrm{th}} = 2.46 \times 10^{-14}$ s, with full arithmetic (Section 4, D1).
- A derived coherent-cycle bound: a receptor transition of energy $E$ supports $N_{\mathrm{cyc}} = E/(2\pi k_B T)$ coherent cycles, giving $1.19$ cycles at $E = 0.2$ eV and $59.6$ cycles at $E = 10$ eV (Section 4, D2 and D5).
- A derived channel-capacity bound of $3.09$ bits per mode for a $0.2$ eV receptor under a Shannon-type thermal-noise assumption, cross-checked against a dimension bound of $\log_2 d = 1$ bit for $d = 2$ (Section 4, D3).
- A derived minimum coupling energy for the conjectured pre-geometric coupling, $\hbar\Omega \geq k_B T = 26.7$ meV, below which the coupling is classical in the sense of the feedback criterion [4] (Section 4, D4).
- A derived thermodynamic cost of digital translation at error rate $\alpha_r = 10^{-4}$, $R = 0.246$ eV per event using the constant $R = k_B T \ln(1/\alpha_r)$ of the Rosetta framework [11], which is of the same order as a receptor vibrational quantum (Section 4, D6).

## 2. Background and Related Work

The informational reconstruction of quantum theory provides the interpretive stance of this paper. The introduction to the volume "Quantum Theory: Informational Foundations and Foils" distinguishes the dynamicist tradition, in which physics describes natural dynamical behaviour without reference to agents, from the pragmatist tradition, in which the laws of physics are characterized by the extent to which we can learn and control physical systems, and documents that the recent foundational wave has shifted from interpreting quantum theory to reconstructing it from physical principles [1]. Our model adopts the pragmatist stance deliberately: "thought" is defined operationally, as a state distinguished by what information-processing it supports, not by a dynamicist story about mental substance. This choice matters because the two-phase conjecture is otherwise vulnerable to category errors in which informational and mechanical descriptions are conflated.

That phase transitions have computational consequences is the key existing result supporting the idea that a phase transition can "freeze" which thoughts manifest. In the transverse-field Ising model with Hamiltonian $H_I(g) = -\sum_{i=1}^{N}(\sigma_i^x \sigma_{i+1}^x + g \sigma_i^z)$, two quantum phases are separated by a critical point at $g = 1$, and the study of differential local convertibility of ground states gives direct operational significance to the phase transition for quantum information processing, with the authors connecting their analysis to adiabatic quantum computation, where a Hamiltonian $(1-s)H_0 + s H_p$ is evolved by varying $s$ [2]. This is precisely the structure our conjecture needs at cosmological scale: a parameter crossing a critical value changes what the ground state can computationally support. We generalize from their spin-chain critical point to a hypothesized pre-geometric-to-geometric transition, and we flag that generalization as the model's central unproven step.

The capacity side of the model rests on a dimension bound adopted here as a modeling assumption, in the spirit of semi-device-independent quantum information [3]: a $d$-level quantum system can convey at most $\log_2 d$ bits per use. We use this to bound what a receptor of given dimension can carry: the dimension assumption directly yields the $\log_2 d$ bit bound we cross-check in Section 4.

The quantum-versus-classical criterion that decides our central result is adopted here as a modeling assumption, motivated by the analysis of interaction Hamiltonians and of information exchange between coupled systems [4]. The criterion states that the dynamics of an interaction Hamiltonian can be interpreted as a completely classical information exchange when the decoherence rates are comparable to the frequencies defining the strength of the interaction. Our coupling threshold in D4 is this criterion applied with the thermal decoherence rate $\Gamma_{\mathrm{th}}$ in the role of the coupling rate.

The pre-geometric phase is given concrete Hamiltonian form by recent work on emergent gravity. In the pre-geometric construction we adopt as the mechanism for our geometric phase, neither the spacetime metric nor the tetrads are assumed to exist in the unbroken phase; a Higgs-like scalar acquiring a nonzero vacuum expectation value spontaneously breaks the pre-geometric symmetry down to the Lorentz group, recovering Einstein–Cartan theory with a cosmological constant term, and canonical general relativity is recovered in the infrared limit of the spontaneously broken phase [5]. This supplies the geometric phase of our two-phase model with an explicit mechanism: geometry is the broken phase, and the transition is spontaneous symmetry breaking rather than a mere change of description.

Decoherence itself we model with the non-Hermitian effective-Hamiltonian formalism. We model decoherence using an effective non‑Hermitian Hamiltonian, where the anti‑Hermitian part $-i\Gamma_{\mathrm{th}}/2$ encodes the decay rate. We use the decaying branch: in Section 3 the thermal bath is represented by an anti-Hermitian part $-i\Gamma_{\mathrm{th}}/2$ of an effective Hamiltonian, which is legitimate precisely because the imaginary part of a non-Hermitian eigenvalue encodes a decay rate [6].

The selection of which informational states survive the transition we model as an information bottleneck, adopted here as a modeling assumption with efficient algorithms studied in the quantum information-bottleneck literature [7]. The bottleneck extracts information $T$ with respect to a system $Y$ from a system $X$ by minimizing $I(T:X) - \beta I(T:Y)$, achieving irreversible compression that keeps relevant and discards unessential information. In our model, the phase transition acts as a bottleneck on the pre-geometric plenum: the subspace of "manifestable thoughts" is the compressed representation $T$.

The monistic-reality framework [10] states the conjecture most directly: reality is a pre-geometric informational substrate structured as a Hamiltonian superposition satisfying $H|\Psi\rangle = 0$. We take that architecture as our hypothesis and supply what it lacks here: numerical constraints under which a biological receptor could couple to such a substrate at all. Our paper takes that architecture as its hypothesis and does what the framework itself does not: it derives numerical constraints under which a biological perceiver node could couple to the ontologic-information domain at all. Finally, we adopt, in the spirit of the Project Rosetta framework [11], the modeling assumption that translation between continuous physical dynamics and discrete computational state spaces carries a thermodynamic cost given by Rosetta's Constant $R = k_B T \ln(1/\alpha_r)$ at translation error rate $\alpha_r$. Our D6 computation uses that constant, and our interpretation of the phase transition as selecting a subspace keeps the pre-geometric phase continuous rather than discretizing it.

## 3. Methods

### 3.1 Model overview

We posit two phases and a transition.

**Phase P (pre-geometric).** An informational Hilbert space $\mathcal{H}_{\mathrm{P}}$ with Hamiltonian constraint $H_{\mathrm{P}}|\Psi\rangle = 0$, following the monistic-reality architecture in which information states exist ontologically independently of any geometric realization [10]. States $|\Psi\rangle \in \mathcal{H}_{\mathrm{P}}$ are candidate "thoughts" in the operational sense of [1]: they are defined by the information-processing they support, not by a dynamical story.

**Phase G (geometric).** The broken phase in which a metric structure exists. We take the mechanism from pre-geometric gravity: a Higgs-like field acquiring a vacuum expectation value spontaneously breaks the pre-geometric symmetry and recovers Einstein–Cartan gravity in the infrared [5]. The transition $P \to G$ is modeled as this symmetry breaking, and — this is the conjecture under test — it acts as an information bottleneck [7] that selects a Hamiltonian subspace $\mathcal{K} \subset \mathcal{H}_{\mathrm{P}}$: only states in $\mathcal{K}$ are "manifestable" in the geometric phase.

**Receptors.** A biological receptor R (microtubule-like, Posner-like, or magnetoreception-like) is modeled as a $d$-level quantum system with a characteristic transition energy $E$, coupled (i) to the thermal bath at temperature $T$ and (ii) — conjecturally — to the selected subspace $\mathcal{K}$ with coupling frequency $\Omega$. The receptor is a channel in the prepare-and-measure sense of [3]: it prepares states $\rho_x$ from physical stimuli and would, if the conjecture holds, transmit the selected informational content to $\mathcal{K}$.

### 3.2 Composite Hamiltonian

The composite Hilbert space is

$$\mathcal{H} = \mathcal{H}_{\mathrm{phys}} \otimes \mathcal{H}_{\mathrm{P}},$$

with total Hamiltonian

$$H = H_{\mathrm{phys}} + H_{\mathrm{P}} + \lambda V,$$

where $V$ is a bilinear coupling operator and $\lambda$ a strength. Because the thermal bath causes decay, we describe the receptor's reduced dynamics by an effective non-Hermitian Hamiltonian whose eigenvalues carry an anti-Hermitian part $-i\Gamma_{\mathrm{th}}/2$, with $\Gamma_{\mathrm{th}}$ the thermal decoherence rate; this is the standard use of non-Hermitian operators for dissipative effective descriptions, where the imaginary part of an eigenvalue is a decay rate [6]. The conjectured coupling to $\mathcal{K}$ is required to satisfy the quantum-versus-classical criterion of [4]: the coupling is quantum only if its frequency $\Omega$ exceeds the decoherence rate; otherwise the interaction is a classical information exchange.

### 3.3 Information-theoretic bounds

Two bounds are used. First, the semi-device-independent dimension assumption of [3], with fixed Hilbert-space dimension $d$, limits the one-shot accessible information of the receptor channel to $\log_2 d$ bits. Second, a Shannon-type bound under thermal noise, $C = \log_2(1 + E/(k_B T))$ bits per mode, where $E$ is the receptor transition energy treated as signal energy against thermal noise of scale $k_B T$; this is stated as a modeling assumption, not a theorem.

### 3.4 Parameter assumptions

- Temperature: $T = 310$ K (physiological).
- Boltzmann constant: $k_B = 1.380\,649 \times 10^{-23}$ J/K.
- Reduced Planck constant: $\hbar = 1.054\,571\,8 \times 10^{-34}$ J·s.
- Elementary charge: $e = 1.602\,176\,634 \times 10^{-19}$ J/eV.
- Receptor transition energies: $E = 0.2$ eV (typical molecular vibrational/electronic scale, assumed) and $E = 10$ eV (generous upper scale, assumed).
- Receptor dimension: $d = 2$ (two-level approximation, assumed).
- Neuronal integration time: $t_{\mathrm{neuron}} = 1$ ms $= 10^{-3}$ s (assumed).
- Translation error rate for D6: $\alpha_r = 10^{-4}$ (assumed).

All of these are explicitly assumptions of the model; none is measured here.

## 4. Analysis

### D1: Thermal decoherence rate and time

The thermal energy scale is

$$k_B T = (1.380\,649 \times 10^{-23}\ \mathrm{J/K}) \times 310\ \mathrm{K} = 4.280\,01 \times 10^{-21}\ \mathrm{J}.$$

In electronvolts,

$$k_B T = \frac{4.280\,01 \times 10^{-21}\ \mathrm{J}}{1.602\,176\,634 \times 10^{-19}\ \mathrm{J/eV}} = 2.6712 \times 10^{-2}\ \mathrm{eV} = 26.71\ \mathrm{meV}.$$

Taking the bare thermal rate as the natural frequency scale $k_B T/\hbar$,

$$\Gamma_{\mathrm{th}} = \frac{k_B T}{\hbar} = \frac{4.280\,01 \times 10^{-21}\ \mathrm{J}}{1.054\,571\,8 \times 10^{-34}\ \mathrm{J\cdot s}} = 4.058 \times 10^{13}\ \mathrm{s}^{-1},$$

and the corresponding decoherence time is

$$\tau_{\mathrm{th}} = \frac{1}{\Gamma_{\mathrm{th}}} = \frac{1}{4.058 \times 10^{13}\ \mathrm{s}^{-1}} = 2.46 \times 10^{-14}\ \mathrm{s}.$$

Compared with the neuronal integration time,

$$\frac{\tau_{\mathrm{th}}}{t_{\mathrm{neuron}}} = \frac{2.46 \times 10^{-14}\ \mathrm{s}}{10^{-3}\ \mathrm{s}} = 2.46 \times 10^{-11}.$$

The bare thermal decoherence time is eleven orders of magnitude shorter than a neuronal integration window. Equivalently, sustaining coherence over $t_{\mathrm{neuron}}$ would require suppression of the decoherence rate by a factor

$$S = \frac{t_{\mathrm{neuron}}}{\tau_{\mathrm{th}}} = 10^{-3}\ \mathrm{s} \times 4.058 \times 10^{13}\ \mathrm{s}^{-1} = 4.06 \times 10^{10},$$

i.e., roughly eleven orders of magnitude.

### D2: Coherent-cycle bound at $E = 0.2$ eV

A transition of energy $E$ has angular frequency $\omega = E/\hbar$ and ordinary frequency $f = E/(2\pi\hbar)$; the number of coherent cycles available before decoherence is

$$N_{\mathrm{cyc}} = f\,\tau_{\mathrm{th}} = \frac{E}{2\pi\hbar} \cdot \frac{\hbar}{k_B T} = \frac{E}{2\pi k_B T}.$$

For $E = 0.2$ eV $= 0.2 \times 1.602\,176\,634 \times 10^{-19}\ \mathrm{J} = 3.204\,35 \times 10^{-20}\ \mathrm{J}$:

$$2\pi k_B T = 6.283\,19 \times 4.280\,01 \times 10^{-21}\ \mathrm{J} = 2.689\,33 \times 10^{-20}\ \mathrm{J},$$

$$N_{\mathrm{cyc}} = \frac{3.204\,35 \times 10^{-20}}{2.689\,33 \times 10^{-20}} = 1.19.$$

A $0.2$ eV receptor completes barely one coherent cycle before thermal decoherence.

$$N_{\mathrm{cyc}} = \frac{3.204\,35 \times 10^{-20}}{2.689\,33 \times 10^{-20}} = 1.19.$$

A $0.2$ eV receptor completes barely one coherent cycle before thermal decoherence.

### D3: Channel capacity at $E = 0.2$ eV

Under the Shannon-type thermal-noise assumption of Section 3.3, the capacity per mode is

$$C = \log_2\!\left(1 + \frac{E}{k_B T}\right).$$

With $E = 0.2$ eV and $k_B T = 2.6712 \times 10^{-2}$ eV from D1,

$$\frac{E}{k_B T} = \frac{0.2}{2.6712 \times 10^{-2}} = 7.4871,$$

$$1 + \frac{E}{k_B T} = 8.4871,$$

$$C = \log_2(8.4871) = \frac{\ln(8.4871)}{\ln 2} = \frac{2.1384}{0.69315} = 3.09\ \text{bits per mode}.$$

The dimension bound of [3] gives an independent cross-check: with the assumed receptor dimension $d = 2$, the one-shot accessible information is at most

$$\log_2 d = \log_2 2 = 1\ \text{bit}.$$

The dimension bound is the binding constraint: a two-level receptor cannot carry more than $1$ bit per use regardless of its transition energy, so the Shannon-type figure of $3.09$ bits per mode is an upper envelope that the assumed $d = 2$ receptor cannot reach. Raising $d$ to $d = 2^{3.09} \approx 8.5$, i.e., at least a nine-level receptor, would be required for the thermal-noise capacity to become the binding constraint.

### D4: Minimum coupling energy to the pre-geometric subspace

The quantum-versus-classical criterion of [4] states that an interaction Hamiltonian's dynamics can be interpreted as a completely classical information exchange when the decoherence rates are comparable to the frequencies defining the strength of the interaction. Applying this with the thermal decoherence rate $\Gamma_{\mathrm{th}}$ in the role of the coupling rate $\gamma$, the conjectured coupling to $\mathcal{K}$ with frequency $\Omega$ is quantum only if

$$\Omega > \Gamma_{\mathrm{th}} = 4.058 \times 10^{13}\ \mathrm{s}^{-1},$$

i.e., in energy units,

$$\hbar\Omega > \hbar\Gamma_{\mathrm{th}} = k_B T = 26.71\ \mathrm{meV}.$$

A coupling weaker than $k_B T$ is, by this criterion, a classical information exchange between the receptor and its environment rather than a quantum channel to the selected subspace. The minimum coupling energy is therefore set by the thermal scale itself: any viable pre-geometric coupling must exceed $26.71$ meV, and because the coupling competes with a bath at the same scale, the margin above $k_B T$ must be large enough that the coupling frequency is not merely comparable to but dominant over $\Gamma_{\mathrm{th}}$.

### D5: Coherent-cycle bound at $E = 10$ eV

Repeating D2 with the generous upper transition energy $E = 10$ eV $= 10 \times 1.602\,176\,634 \times 10^{-19}\ \mathrm{J} = 1.602\,18 \times 10^{-18}\ \mathrm{J}$:

$$N_{\mathrm{cyc}} = \frac{E}{2\pi k_B T} = \frac{1.602\,18 \times 10^{-18}\ \mathrm{J}}{2.689\,33 \times 10^{-20}\ \mathrm{J}} = 59.6.$$

Even a $10$ eV transition — far above typical molecular vibrational quanta and in the range of deep-ultraviolet electronic transitions — supports fewer than sixty coherent cycles at $310$ K under the bare thermal rate. Scaling from D2 is linear in $E$, as the formula $N_{\mathrm{cyc}} = E/(2\pi k_B T)$ requires: $10/0.2 = 50$ and $50 \times 1.19 = 59.5$, consistent with the direct computation to rounding.

### D6: Thermodynamic cost of digital translation

The Rosetta framework defines Rosetta's Constant $R = k_B T \ln(1/\alpha_r)$ as the thermodynamic cost of translating between continuous physical dynamics and discrete computational state spaces [11]. With the assumed translation error rate $\alpha_r = 10^{-4}$ and $k_B T = 4.280\,01 \times 10^{-21}$ J from D1:

$$\ln\!\left(\frac{1}{\alpha_r}\right) = \ln(10^{4}) = 4 \times \ln 10 = 4 \times 2.30259 = 9.21034,$$

$$R = 4.280\,01 \times 10^{-21}\ \mathrm{J} \times 9.21034 = 3.946\,1 \times 10^{-20}\ \mathrm{J}.$$

In electronvolts,

$$R = \frac{3.946\,1 \times 10^{-20}\ \mathrm{J}}{1.602\,176\,634 \times 10^{-19}\ \mathrm{J/eV}} = 0.246\ \mathrm{eV}.$$

This is of the same order as a typical molecular vibrational quantum ($0.2$ eV, the receptor energy assumed in D2 and D3): $R / E = 0.246/0.2 = 1.23$. The non-exactness theorem of [11], proved via Gromov's non-squeezing theorem showing that the symplectic capacity $c_G(M,\omega)$ is an invariant of $\mathcal{P}$ with no image in the discrete target $\mathcal{C}$, implies that this cost is not an engineering overhead that better hardware removes but a structural feature of any discrete translation of the continuous phase dynamics. For the two-phase model, the consequence is that if the pre-geometric phase is continuous in the symplectic sense, any digital readout of a "thought" state pays at least $R \approx 0.246$ eV per translated event at the assumed error rate — comparable to the receptor's entire transition energy.

### D7: Aggregate constraint on a receptor channel

Combining D1–D6, a candidate receptor at $310$ K must simultaneously satisfy:

$$\tau_{\mathrm{coh}} \geq \tau_{\mathrm{th}} = 2.46 \times 10^{-14}\ \mathrm{s} \quad \text{(bare lower bound, D1)},$$

$$N_{\mathrm{cyc}} = \frac{E}{2\pi k_B T} \geq 1 \quad \Rightarrow \quad E \geq 2\pi k_B T = 2.689\,33 \times 10^{-20}\ \mathrm{J} = 0.168\ \mathrm{eV},$$

$$\hbar\Omega \geq k_B T = 26.71\ \mathrm{meV} \quad \text{(D4)},$$

$$C \leq \min\!\left(\log_2 d,\ \log_2\!\left(1 + \frac{E}{k_B T}\right)\right) \quad \text{(D3)}.$$

The cycle bound yields a minimum transition energy: a receptor must have $E \geq 0.168$ eV to complete even one coherent cycle. The assumed $E = 0.2$ eV sits just above this floor, which is why D2 gives barely more than one cycle. To sustain coherence across a neuronal integration window $t_{\mathrm{neuron}} = 10^{-3}$ s, the required suppression factor from D1 is $S = 4.06 \times 10^{10}$; equivalently, the effective decoherence rate must be driven down from $\Gamma_{\mathrm{th}} = 4.058 \times 10^{13}\ \mathrm{s}^{-1}$ to at most

$$\Gamma_{\mathrm{eff}} \leq \frac{1}{t_{\mathrm{neuron}}} = 10^{3}\ \mathrm{s}^{-1},$$

a reduction by the factor $S = 4.06 \times 10^{10}$ computed in D1.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; none is measured. The principal results are:

| Quantity | Symbol | Value | Source |
|---|---|---|---|
| Thermal energy at $310$ K | $k_B T$ | $26.71$ meV | D1 |
| Bare thermal decoherence rate | $\Gamma_{\mathrm{th}}$ | $4.058 \times 10^{13}\ \mathrm{s}^{-1}$ | D1 |
| Bare thermal decoherence time | $\tau_{\mathrm{th}}$ | $2.46 \times 10^{-14}$ s | D1 |
| Suppression factor for ms coherence | $S$ | $4.06 \times 10^{10}$ | D1 |
| Coherent cycles at $E = 0.2$ eV | $N_{\mathrm{cyc}}$ | $1.19$ | D2 |
| Shannon-type capacity at $E = 0.2$ eV | $C$ | $3.09$ bits/mode | D3 |
| Dimension bound at $d = 2$ | $\log_2 d$ | $1$ bit | D3 |
| Minimum coupling energy | $\hbar\Omega$ | $\geq 26.71$ meV | D4 |
| Coherent cycles at $E = 10$ eV | $N_{\mathrm{cyc}}$ | $59.6$ | D5 |
| Minimum transition energy for one cycle | $E_{\min}$ | $0.168$ eV | D7 |
| Translation cost at $\alpha_r = 10^{-4}$ | $R$ | $0.246$ eV | D6 |

Three results carry the weight of the analysis. First, the bare thermal decoherence time $\tau_{\mathrm{th}} = 2.46 \times 10^{-14}$ s is $2.46 \times 10^{-11}$ of a neuronal integration window (D1), so any receptor proposal that requires millisecond coherence must invoke a suppression of the decoherence rate by $4.06 \times 10^{10}$, and the mechanism of that suppression must itself be named and quantified. Second, the coherent-cycle bound is linear in transition energy with slope $1/(2\pi k_B T) = 1/(2.689\,33 \times 10^{-20}\ \mathrm{J}) = 3.72 \times 10^{19}\ \mathrm{J}^{-1}$, so even the most generous molecular transition energies buy only tens of cycles (D5). Third, the channel capacity of the assumed two-level receptor is bounded at $1$ bit by dimension, not by energy (D3), so increasing transition energy buys cycles but not capacity.

Under the model's own criterion, the conjunction of these bounds means that a receptor channel to the pre-geometric subspace $\mathcal{K}$ is not excluded by the coupling threshold alone ($\hbar\Omega \geq 26.71$ meV is achievable by molecular standards) but is excluded at the integration-time level unless a suppression mechanism four orders of magnitude beyond any quantified here operates. The framework therefore generates a discriminating prediction: any two-phase account of cognition that survives must either (i) identify a physical mechanism reducing $\Gamma_{\mathrm{eff}}$ by $\geq 4.06 \times 10^{10}$ at $310$ K, or (ii) accept that the conjectured coupling operates only on sub-picosecond timescales and explain how sub-picosecond events integrate into cognition. Standard neuroscience, which needs no such suppression, is distinguished from the two-phase model precisely by this requirement.

## 6. Discussion

The central limitation is that the decoherence rate $\Gamma_{\mathrm{th}} = k_B T/\hbar$ is a bare, single-mode estimate, not a computed receptor-specific rate. Real decoherence rates depend on the spectral density of the bath at the receptor's transition frequency, on whether the coupling is super-Ohmic, and on decoherence-free subspaces; the formalism of [6] licenses treating decay through the imaginary part of an effective-Hamiltonian eigenvalue, but does not fix the magnitude of that imaginary part for any particular molecular structure. If the true thermal decoherence rate for a given receptor is even $10^{3}$ times smaller than the bare estimate — which would require strong suppression already built into the receptor's coupling to the bath — the cycle counts of D2 and D5 rise by the same factor, and the qualitative conclusion weakens. The result is therefore sensitive to the single most contestable assumption in the model.

A second limitation is the Shannon-type capacity formula of D3, which is stated as a modeling assumption, not derived from a microscopic noise model. The cross-check against the dimension bound of [3] is the more defensible of the two bounds, because it follows from the semi-device-independent framework in which a fixed Hilbert-space dimension $d$ limits achievable correlations; but the dimension $d = 2$ is itself assumed, and a receptor with $d \geq 9$ would shift the binding constraint back to the thermal-noise formula.

A third limitation is the extrapolation from the spin-chain result of [2] to a cosmological phase transition. That work shows differential local convertibility of ground states across the critical point $g = 1$ of the transverse-field Ising model, giving operational significance to the transition for information processing in that specific system; nothing in the derivation guarantees that a pre-geometric-to-geometric transition has an analogous convertibility structure. This is the model's central unproven step, and it is flagged as such.

The conjectured coupling to $\mathcal{K}$ is the least constrained element of the model. The criterion of [4] supplies a necessary condition ($\hbar\Omega > k_B T$) but no sufficient condition: a coupling that passes the quantum-versus-classical test against the thermal bath may still fail to couple to $\mathcal{K}$ specifically, and the model offers no dynamics for $\mathcal{K}$ that would predict a coupling strength. The bottleneck formalism of [7] describes which information survives compression but not what physical interaction implements the compression at a receptor.

**Falsification.** The main result — that no plausible biological receptor at $310$ K sustains the coherence needed for a functional pre-geometric channel without an unquantified suppression mechanism — would be falsified by a laboratory measurement of a receptor-like structure maintaining quantum coherence (e.g., Rabi oscillations or interferometric phase sensitivity) for $t \geq 10^{-3}$ s at $T = 310$ K, or, more weakly, by a demonstrated suppression factor $S \geq 4.06 \times 10^{10}$ in any warm $(T > 300\ \mathrm{K})$ condensed-phase system. Conversely, the two-phase conjecture itself would be falsified at the receptor level if the thresholds of D7 are shown to be necessary (i.e., if the coupling criterion of [4] is the correct discriminator) and no receptor meets them.

**Limitations list.**

- Assumption: $T = 310$ K. The rate $\Gamma_{\mathrm{th}}$ is linear in $T$; at $T = 273$ K the rate falls by $12\%$ only, so the conclusion is insensitive to physiological temperature variation.
- Assumption: $\Gamma_{\mathrm{th}} = k_B T/\hbar$. The result is maximally sensitive to this choice; a receptor-specific spectral-density calculation could lower the rate by orders of magnitude, and no such calculation is performed here.
- Assumption: $E = 0.2$ eV and $E = 10$ eV as the receptor transition range. The cycle bound is linear in $E$; transitions above $10$ eV are ionizing and implausible in a biological receptor, so the range is taken as generous.
- Assumption: $d = 2$. Capacity conclusions change qualitatively for $d \geq 9$ (D3).
- Assumption: $t_{\mathrm{neuron}} = 10^{-3}$ s. If the relevant integration time is sub-picosecond, the suppression factor $S$ falls proportionally; the model does not specify the cognitive timescale, and this is an open question.
- Assumption: $\alpha_r = 10^{-4}$ in D6. The translation cost $R$ is linear in $\ln(1/\alpha_r)$; at $\alpha_r = 10^{-2}$, $R = 0.123$ eV, still of the order of a vibrational quantum.
- Structural: the existence and dynamics of $\mathcal{K}$ are hypothesized, not derived; the generalization from the Ising critical point of [2] to a pre-geometric transition is unproven.
- Structural: the $H|\Psi\rangle = 0$ substrate of [10] is taken as given; no independent derivation of the constraint is offered here.

## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The primary users are experimental quantum-biology groups who currently test microtubule-like, Posner-like, or radical-pair receptor proposals without a shared quantitative target. If the thresholds of D7 hold, the decision that changes is which experiments to fund: proposals claiming millisecond coherence at $310$ K can be screened against the required suppression factor $S = 4.06 \times 10^{10}$ before synthesis, and proposals targeting sub-picosecond channels can be recognized as consistent with the model only under the integration-time caveat of Section 6. A secondary user community is theorists of emergent spacetime, for whom the result supplies the first numerical statement of what a biological "perceiver node" in the correlation-graph architecture of [10] would have to satisfy physically.

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept and application formulated). No experimental validation exists, and analytical work of this kind does not exceed TRL 3 in the best case; no manufacturing or deployment readiness is claimed.

**(c) Smallest next test.** The smallest de-risking calculation is a receptor-specific decoherence computation: take one candidate structure with a stated transition energy near $E = 0.2$ eV, compute the thermal decoherence rate from a microscopic spectral density $J(\omega)$ at $310$ K, and compare $\Gamma_{\mathrm{eff}}$ against the bare $\Gamma_{\mathrm{th}} = 4.058 \times 10^{13}\ \mathrm{s}^{-1}$. The outcome that refutes the paper's central claim is $\Gamma_{\mathrm{eff}} \leq 10^{3}\ \mathrm{s}^{-1}$ (suppression factor $S \geq 4.06 \times 10^{10}$) from the spectral density alone; the outcome that strengthens it is $\Gamma_{\mathrm{eff}}$ within one to two orders of magnitude of the bare estimate. The smallest de-risking experiment is a warm $(T \geq 300\ \mathrm{K})$ coherence measurement on the same structure, with the measured coherence time compared against $\tau_{\mathrm{th}} = 2.46 \times 10^{-14}$ s and against the millisecond target.

**(d) Binding constraints.** The constraint that binds first is thermal management: at $310$ K the bath delivers $k_B T = 26.71$ meV per mode, and any coupling below that scale is classical by the criterion of [4], so the engineering problem is not building the coupling but isolating the receptor from a bath that cannot be turned off in a biological host. The second binding constraint is dimensional: a two-level receptor carries at most $1$ bit per use (D3), so any cognitive function requiring more per-event information needs a higher-dimensional receptor, whose larger Hilbert space generally increases susceptibility to decoherence. Whether cryogenic-style suppression mechanisms can exist at all in a warm condensed phase is an open question the present analysis does not resolve; the required factor $S = 4.06 \times 10^{10}$ has no quantified precedent in the sources used here.

**(e) Order-of-magnitude bounds (projections).** Labeled as projections with stated assumptions: if a receptor must complete $N_{\mathrm{cyc}} \geq 10^{6}$ cycles to support any nontrivial gate-like operation (an assumption, not derived here), the required transition energy is $E \geq 2\pi k_B T \times 10^{6} = 2.689\,33 \times 10^{-14}\ \mathrm{J} = 1.68 \times 10^{5}$ eV, which is ionizing-radiation scale and physically excluded in a biological receptor; the alternative is suppression of $\Gamma_{\mathrm{eff}}$ by the same factor $10^{6}$ relative to the one-cycle requirement, i.e., $S \geq 4.06 \times 10^{16}$ for millisecond coherence with $10^{6}$ cycles. Both projections follow from the linear scaling of D2 and the suppression factor of D1 with no additional inputs.

**(f) Risks and misuse.** The framework's thresholds could be misused rhetorically: a proposal that meets the coupling threshold $\hbar\Omega \geq 26.71$ meV could be presented as evidence for a pre-geometric channel, when the threshold is only a necessary condition against thermal classicalization and says nothing about coupling to $\mathcal{K}$. Conversely, the decoherence bounds could be misused to dismiss all quantum-biology research wholesale, when the analysis constrains only receptor channels conjectured to couple to a pre-geometric subspace and leaves ordinary quantum effects in biology (e.g., energy transfer) untouched.

## 8. Conclusion

We formalized the conjecture that cognition is a quantum-informational Hamiltonian state coupling a physical universe to a pre-geometric phase, building the geometric phase on the spontaneous-symmetry-breaking recovery of Einstein–Cartan gravity [5], the substrate on the $H|\Psi\rangle = 0$ informational architecture [10], and the quantum-versus-classical discriminator on the decoherence-rate criterion of [4]. Within this two-phase model we derived, with full arithmetic, that at $T = 310$ K the bare thermal decoherence time is $\tau_{\mathrm{th}} = 2.46 \times 10^{-14}$ s, that a $0.2$ eV receptor supports $1.19$ coherent cycles and a $10$ eV receptor $59.6$, that a two-level receptor carries at most $1$ bit per use against a thermal-noise envelope of $3.09$ bits, that any pre-geometric coupling must exceed $k_B T = 26.71$ meV to remain quantum, and that digital translation of continuous dynamics costs $R = 0.246$ eV per event at error rate $10^{-4}$ by Rosetta's Constant [11]. The conjunction of these bounds yields the model's discriminating prediction: a functional pre-geometric receptor channel at physiological temperature requires a decoherence suppression factor of at least $S = 4.06 \times 10^{10}$ over a neuronal integration window, a factor for which no mechanism is quantified here. The framework stands or falls on that number: a measured warm-system suppression at or above it falsifies the paper's central negative result and opens a specific experimental program; its absence across all candidate receptors falsifies the two-phase conjecture at the receptor level and lets quantum biology proceed without it.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would draft models using openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification would be performed by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would require checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would include independent recomputation: a separately generated script would recompute 13 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Introduction to the book "Quantum Theory: Informational Foundations and Foils". arXiv:1805.11483v3. https://arxiv.org/abs/1805.11483v3
[2] Quantum phases with differing computational power. arXiv:1110.3331v4. https://arxiv.org/abs/1110.3331v4
[3] Information capacity of quantum communication under natural physical assumptions. arXiv:2405.07231v3. https://arxiv.org/abs/2405.07231v3
[4] Simulation of interaction Hamiltonians by quantum feedback: a comment on the dynamics of information exchange between coupled systems. arXiv:quant-ph/0506002v1. https://arxiv.org/abs/quant-ph/0506002v1
[5] Hamiltonian Analysis of Pre-geometric Gravity. arXiv:2505.01272v2. https://arxiv.org/abs/2505.01272v2
[6] Non-Hermitian Hamiltonians with a Real Spectrum and Their Physical Applications. arXiv:0909.1654v1. https://arxiv.org/abs/0909.1654v1
[7] Efficient algorithms for quantum information bottleneck. arXiv:2208.10342v2. https://arxiv.org/abs/2208.10342v2
[10] QNFO: Monistic Reality
[11] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0
