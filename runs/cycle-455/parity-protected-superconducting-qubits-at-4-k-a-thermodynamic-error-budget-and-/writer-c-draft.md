# The Thermodynamic Bottleneck of Millikelvin Quantum Computing: A Case for Parity-Protected Qubits at 4 K

## Abstract

The dominant engineering assumption in superconducting quantum computing is that colder is better: qubits are cooled toward absolute zero to suppress thermal excitation errors. We argue that this assumption collides with a strict thermodynamic bottleneck. Using the Carnot coefficient of performance degraded by a realistic second-law efficiency, we derive the wall-plug power required to remove heat at cryogenic temperatures and show that it diverges as $T_c \to 0$ K. We further derive a crossover temperature $T^* = \Delta/(k_B \ln(1/\varepsilon_{\mathrm{prot}}))$ at which thermal errors of a conventional qubit with gap $\Delta$ fall below the intrinsic error floor $\varepsilon_{\mathrm{prot}}$ of a parity-protected qubit; for a transmon-like gap $\Delta/k_B = 0.24$ K and a protection floor of $10^{-4}$, we obtain $T^* \approx 26$ mK. Combining these results, we estimate that a parity-protected qubit array operating at 4 K consumes roughly $16\times$ less wall-plug energy per physical gate, and with reduced error-correction overhead roughly $1.6\times 10^{3}\times$ less energy per logical gate, than a conventional array at 10 mK. We review the parity-protected qubit literature and cryogenic infrastructure constraints, derive all quantitative claims explicitly, and discuss the assumptions under which the 4 K architecture would fail.

## 1. Introduction

Scalable quantum computing faces a systems-level constraint that is rarely foregrounded in qubit-focused research: every watt of heat removed at millikelvin temperatures must be pumped uphill against a thermodynamic gradient that grows without bound as the cold stage approaches 0 K. Large-scale cryogenic facilities such as the PIP-II cryogenic system, which supplies 23 superconducting radio-frequency cryomodules at 2 K, 5 K, and 40 K temperature levels from a single warm compressor system [1], and the IB-1 cryogenic test facility, which required a dedicated new helium liquefier to serve quantum-system testing demand [3], illustrate the industrial reality: cryogenic infrastructure is expensive, power-hungry, and scales poorly with the number of cold devices.

Against this backdrop, a family of qubit proposals offers an alternative route: instead of cooling until thermal errors vanish, encode the qubit so that its logical states are protected by a conserved quantity, namely fermion parity. Proposals include the top-transmon, which couples minimally to the fermion parity of Majorana modes [6]; the parity-protected superconductor-semiconductor qubit based on voltage-controlled nanowire Josephson junctions [4]; the parity-protected superconducting qubit built from two $0$-$\pi$ qubits with topological Josephson junctions [2]; and a gate-voltage-controlled parity-protected qubit using an altermagnetic Josephson junction that removes the need for flux biasing [8]. These devices aim at intrinsically long coherence, which in principle relaxes the temperature requirement.

This paper makes a specific, falsifiable claim: there exists a crossover temperature above which parity-protected qubits at 4 K are thermodynamically superior to brute-force cooling of conventional qubits, and that crossover lies far above the millikelvin operating points of today's dilution refrigerators. We derive the bound, compute the crossover, and compare energy budgets per gate. The argument challenges the "colder is better" roadmap and, if correct, would redirect hardware investment from extreme refrigeration toward error-protecting encodings. The thermodynamic framing follows the QNFO analyses of thermodynamic imperatives and quantum constraints on scalable computation [9], [10], with the encoding-as-computation perspective informed by syntactic-generation models of physical information processing [11].

## 2. Background and Related Work

**Cryogenic infrastructure.** The PIP-II warm compressor system overview documents a single compressor plant supplying 23 SRF cryomodules at three temperature levels (2 K, 5 K, 40 K) [1]; this demonstrates that multi-temperature cryogenic distribution is mature engineering, but also that each temperature level multiplies plant complexity. The IB-1 cryogenic liquefier integration paper reports that growth in quantum-system, SRF-cavity, magnet, and fusion testing forced the addition of an entirely new helium cryogenic plant [3] — direct evidence that cryogenic capacity, not qubit fabrication, is becoming the throughput bottleneck for quantum hardware programs. The New Muon Lab cryomodule test facility at Fermilab describes cooling a single 1.3 GHz cryomodule with a standalone Tevatron-style refrigerator [5], showing the scale of plant needed even for one cryomodule. The PIP-II cryogenic controls system paper details 26 remote-IO cabinets and 48 relay racks solely for temperature readouts, valve positioners, and level instrumentation [7]; the controls overhead alone indicates how much engineering mass sits between the qubit and the wall plug. Collectively [1], [3], [5], [7] establish the empirical premise of this paper: refrigeration toward the millikelvin regime is a capital- and energy-intensive industrial activity.

**Parity-protected qubits.** The top-transmon proposal [6] introduced the parity-protected computation paradigm: rather than fully topological computation, one couples directly to fermion parity in a minimally invasive way, so that quasiparticle excitations — the dominant thermally activated error channel — do not decohere the logical state. The superconductor-semiconductor parity-protected qubit [4] implements parity protection with a symmetric interferometer of few-channel nanowire Josephson junctions, exploiting higher-harmonic energy-phase relations to suppress charge noise; this demonstrates that parity protection is compatible with voltage control, a scalability advantage over flux-biased designs. The topological-insulator $0$-$\pi$ qubit architecture [2] uses two $0$-$\pi$ qubits built on topological Josephson junctions, whose fabrication robustness addresses the identical-junction requirement that historically blocked $0$-$\pi$ hardware; the even/odd parity ground states of the $0$-$\pi$ qubit serve as the protected logical basis. Most recently, the altermagnetic-junction proposal [8] achieves full gate-voltage control of a parity-protected superconducting qubit, eliminating flux bias and its associated flux noise, control overhead, and scalability limits. Together [2], [4], [6], [8] show a clear trajectory: parity protection is moving from concept to controllable, potentially manufacturable devices.

**Thermodynamic framing.** The QNFO Thermodynamic Imperative monograph [9] and the QNFO treatment of thermodynamic and quantum constraints on scalable quantum computing [10] develop the position that energy and entropy flows, not gate counts alone, bound scalable computation; our cooling-power bound in Section 3 is a concrete instantiation of that thesis for the qubit-temperature axis. The syntactic-generation framework [11] supplies the abstract model in which an error-correcting encoding is treated as a computation whose cost must be booked against the physical layer — the basis for our error-correction-overhead accounting in Section 4.

## 3. Methods

### 3.1 Thermodynamic model of cryogenic cooling

A refrigerator removing heat rate $\dot{Q}_c$ from a cold stage at temperature $T_c$ and rejecting it to a hot stage at $T_h$ has Carnot coefficient of performance

$$\mathrm{COP}_{\mathrm{Carnot}} = \frac{T_c}{T_h - T_c}.$$

Real cryogenic systems achieve only a fraction $\eta$ of Carnot (the second-law efficiency). We adopt $\eta_{4\,\mathrm{K}} = 0.02$ for 4 K cryocooler stages and $\eta_{\mathrm{mK}} = 0.005$ for dilution-refrigerator stages; both are stated assumptions, consistent with the engineering reality that dilution refrigerators operate far below Carnot [1], [3]. The wall-plug power per watt of removed heat is then

$$P_{\mathrm{wall}}(\dot{Q}_c = 1\ \mathrm{W}) = \frac{T_h - T_c}{\eta\, T_c}.$$

With $T_h = 300$ K:

- At $T_c = 4$ K, $\eta = 0.02$:
$$P_{\mathrm{wall}}^{4\,\mathrm{K}} = \frac{300 - 4}{0.02 \times 4} = \frac{296}{0.08} = 3.70\times 10^{3}\ \mathrm{W/W}.$$
- At $T_c = 0.010$ K (10 mK), $\eta = 0.005$:
$$P_{\mathrm{wall}}^{10\,\mathrm{mK}} = \frac{300 - 0.010}{0.005 \times 0.010} = \frac{299.99}{5.0\times 10^{-5}} = 6.00\times 10^{6}\ \mathrm{W/W}.$$

The ratio is

$$\frac{P_{\mathrm{wall}}^{10\,\mathrm{mK}}}{P_{\mathrm{wall}}^{4\,\mathrm{K}}} = \frac{6.00\times 10^{6}}{3.70\times 10^{3}} \approx 1.62\times 10^{3}.$$

That is, removing one watt at 10 mK costs about $1.6\times 10^{3}$ times more wall-plug power than removing one watt at 4 K under these assumptions. As $T_c \to 0$, $P_{\mathrm{wall}} \propto 1/T_c$ diverges — this is the thermodynamic bottleneck.

### 3.2 Thermal error model and crossover temperature

For a conventional qubit with excitation gap $\Delta$, the thermally excited error probability per operation cycle is bounded by the Boltzmann factor

$$p_{\mathrm{th}}(T) = \exp\!\left(-\frac{\Delta}{k_B T}\right),$$

where $k_B$ is the Boltzmann constant. A parity-protected qubit does not rely on a large gap against thermal excitation; its residual error floor is $\varepsilon_{\mathrm{prot}}$, set by parity-breaking channels (e.g., quasiparticle poisoning, control-induced parity flips) rather than by temperature. The crossover temperature $T^{*}$ is where the conventional qubit's thermal error just equals the protected qubit's floor:

$$\exp\!\left(-\frac{\Delta}{k_B T^{*}}\right) = \varepsilon_{\mathrm{prot}}
\quad\Longrightarrow\quad
T^{*} = \frac{\Delta}{k_B \ln(1/\varepsilon_{\mathrm{prot}})}.$$

For a transmon-like gap $\Delta/h \approx 5$ GHz, i.e. $\Delta/k_B = h \times 5\ \mathrm{GHz}/k_B$. Using $h/k_B = 4.7992\times 10^{-11}\ \mathrm{K\,s}$:

$$\frac{\Delta}{k_B} = 4.7992\times 10^{-11} \times 5\times 10^{9} = 0.240\ \mathrm{K}.$$

With $\varepsilon_{\mathrm{prot}} = 10^{-4}$ (a stated design assumption for parity-protected devices [4], [6]):

$$\ln(1/\varepsilon_{\mathrm{prot}}) = \ln(10^{4}) = 9.2103,$$
$$T^{*} = \frac{0.240}{9.2103} = 0.0261\ \mathrm{K} \approx 26\ \mathrm{mK}.$$

Below $T^{*}$, brute-force cooling wins on error rate; above $T^{*}$, the conventional qubit's thermal errors exceed the protection floor and cooling buys nothing that encoding cannot.

### 3.3 Energy-per-gate comparison model

Let $q$ be the heat dissipated per qubit per unit time at the cold stage and $f_g$ the gate rate. Wall-plug energy per physical gate:

$$E_{\mathrm{gate}} = \frac{q\, P_{\mathrm{wall}}(1\ \mathrm{W})}{f_g}.$$

We adopt stated assumptions: conventional qubits at 10 mK dissipate $q_{\mathrm{conv}} = 10\ \mathrm{nW}$ per qubit (attenuator and control-line heat at the mixing chamber); parity-protected qubits at 4 K dissipate $q_{\mathrm{par}} = 1\ \mathrm{\mu W}$ per qubit (cryo-control electronics at 4 K are more power-hungry per device, but the stage is far cheaper to hold). Both operate at $f_g = 1\ \mathrm{MHz}$.

For logical-gate accounting, we apply error-correction overhead factors $N_{\mathrm{phys}}$: $N_{\mathrm{conv}} = 1000$ physical qubits per logical qubit for conventional qubits at millikelvin (surface-code scale at realistic physical error rates), versus $N_{\mathrm{par}} = 10$ for parity-protected qubits whose physical error rate is already near the protection floor (stated assumption; the reduction factor is the hypothesis under test, motivated by the intrinsic-coherence claims of [2], [4], [6], [8]). Energy per logical gate:

$$E_{\mathrm{logical}} = N_{\mathrm{phys}}\, E_{\mathrm{gate}}.$$

### 3.4 Sanity check: Landauer floor

The Landauer erasure bound $k_B T \ln 2$ at 4 K is

$$k_B T \ln 2 = 1.3806\times 10^{-23} \times 4 \times 0.6931 = 3.83\times 10^{-23}\ \mathrm{J},$$

and at 10 mK is $9.57\times 10^{-26}$ J. Both are more than ten orders of magnitude below the per-gate energies computed in Section 4, so the Landauer bound does not constrain this comparison; refrigeration overhead, not information-theoretic limits, dominates.

## 4. Analysis

We now execute every arithmetic step explicitly.

**Step 1: Wall-plug power per watt (from Section 3.1).**
Inputs: $T_h = 300$ K (ambient heat-rejection assumption); $T_c = 4$ K and $T_c = 0.010$ K (operating points); $\eta_{4\,\mathrm{K}} = 0.02$, $\eta_{\mathrm{mK}} = 0.005$ (second-law efficiencies, stated assumptions).

$$P_{\mathrm{wall}}^{4\,\mathrm{K}} = \frac{296}{0.08} = 3.70\times 10^{3}\ \mathrm{W/W},$$
$$P_{\mathrm{wall}}^{10\,\mathrm{mK}} = \frac{299.99}{5.0\times 10^{-5}} = 6.00\times 10^{6}\ \mathrm{W/W}.$$

Ratio: $6.00\times 10^{6} / 3.70\times 10^{3} = 1621.6 \approx 1.62\times 10^{3}$.

**Step 2: Gap in temperature units.**
Input: $\Delta/h = 5$ GHz (standard transmon-like gap, stated assumption). With $h/k_B = 4.7992\times 10^{-11}\ \mathrm{K\,s}$:

$$\Delta/k_B = 5\times 10^{9} \times 4.7992\times 10^{-11} = 0.23996\ \mathrm{K} \approx 0.240\ \mathrm{K}.$$

**Step 3: Crossover temperature.**
Input: $\varepsilon_{\mathrm{prot}} = 10^{-4}$ (protection floor, stated assumption).

$$\ln(10^{4}) = 4 \times \ln 10 = 4 \times 2.302585 = 9.21034,$$
$$T^{*} = \frac{0.23996}{9.21034} = 0.02605\ \mathrm{K} \approx 26\ \mathrm{mK}.$$

**Step 4: Thermal error of the conventional qubit at 10 mK and at 4 K.**
At $T = 0.010$ K: $\Delta/(k_B T) = 0.240/0.010 = 24.0$, so

$$p_{\mathrm{th}} = e^{-24.0} \approx 3.8\times 10^{-11}.$$

At $T = 4$ K: $\Delta/(k_B T) = 0.240/4 = 0.06$, so

$$p_{\mathrm{th}} = e^{-0.06} \approx 0.942.$$

This confirms the obvious: a conventional transmon cannot operate at 4 K; the entire benefit of 4 K operation must come from the protected encoding, whose error floor $\varepsilon_{\mathrm{prot}} = 10^{-4}$ is temperature-independent by construction.

**Step 5: Wall-plug power per qubit.**
Inputs: $q_{\mathrm{conv}} = 10\ \mathrm{nW} = 1.0\times 10^{-8}$ W; $q_{\mathrm{par}} = 1\ \mathrm{\mu W} = 1.0\times 10^{-6}$ W.

$$P_{\mathrm{qubit}}^{\mathrm{conv}} = 1.0\times 10^{-8} \times 6.00\times 10^{6} = 6.00\times 10^{-2}\ \mathrm{W} = 60\ \mathrm{mW},$$
$$P_{\mathrm{qubit}}^{\mathrm{par}} = 1.0\times 10^{-6} \times 3.70\times 10^{3} = 3.70\times 10^{-3}\ \mathrm{W} = 3.7\ \mathrm{mW}.$$

**Step 6: Energy per physical gate at $f_g = 1\ \mathrm{MHz} = 10^{6}\ \mathrm{s^{-1}}$.**

$$E_{\mathrm{gate}}^{\mathrm{conv}} = \frac{6.00\times 10^{-2}}{10^{6}} = 6.00\times 10^{-8}\ \mathrm{J} = 60\ \mathrm{nJ},$$
$$E_{\mathrm{gate}}^{\mathrm{par}} = \frac{3.70\times 10^{-3}}{10^{6}} = 3.70\times 10^{-9}\ \mathrm{J} = 3.7\ \mathrm{nJ}.$$

Physical-gate ratio:

$$\frac{E_{\mathrm{gate}}^{\mathrm{conv}}}{E_{\mathrm{gate}}^{\mathrm{par}}} = \frac{60}{3.7} = 16.2.$$

**Step 7: Energy per logical gate with error-correction overhead.**
Inputs: $N_{\mathrm{conv}} = 1000$, $N_{\mathrm{par}} = 10$ (stated assumptions, Section 3.3).

$$E_{\mathrm{logical}}^{\mathrm{conv}} = 1000 \times 6.00\times 10^{-8} = 6.00\times 10^{-5}\ \mathrm{J} = 60\ \mathrm{\mu J},$$
$$E_{\mathrm{logical}}^{\mathrm{par}} = 10 \times 3.70\times 10^{-9} = 3.70\times 10^{-8}\ \mathrm{J} = 37\ \mathrm{nJ}.$$

Logical-gate ratio:

$$\frac{E_{\mathrm{logical}}^{\mathrm{conv}}}{E_{\mathrm{logical}}^{\mathrm{par}}} = \frac{6.00\times 10^{-5}}{3.70\times 10^{-8}} = 1622 \approx 1.6\times 10^{3}.$$

**Step 8: Scaling to a data-center-scale machine.**
For a hypothetical $10^{4}$-logical-qubit machine running $10^{6}$ logical gates per second per qubit, total logical gate rate $= 10^{10}\ \mathrm{s^{-1}}$. Wall-plug power attributable to qubit-stage heat removal:

- Conventional at 10 mK: $10^{10} \times 6.00\times 10^{-5} = 6.00\times 10^{5}$ W $= 0.60$ MW.
- Parity-protected at 4 K: $10^{10} \times 3.70\times 10^{-8} = 3.70\times 10^{2}$ W $= 370$ W.

These are projections under the stated assumptions of Section 3.3, excluding non-qubit cryogenic loads (radiation, wiring, readout hardware), which scale similarly with temperature but are not quantified here.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are empirical measurements.

1. **Wall-plug cost of cold.** Removing 1 W at 10 mK requires $6.00\times 10^{6}$ W of wall power ($\eta = 0.005$), versus $3.70\times 10^{3}$ W at 4 K ($\eta = 0.02$): a factor of $1.62\times 10^{3}$.
2. **Crossover temperature.** $T^{*} \approx 26$ mK for a transmon-like gap $\Delta/k_B = 0.240$ K and protection floor $\varepsilon_{\mathrm{prot}} = 10^{-4}$. Below 26 mK, brute-force cooling matches the protection floor; above it, only encoding does.
3. **Thermal error bracket.** $p_{\mathrm{th}} \approx 3.8\times 10^{-11}$ at 10 mK versus $p_{\mathrm{th}} \approx 0.942$ at 4 K for the conventional qubit — confirming that 4 K operation is viable only for protected encodings.
4. **Per-physical-gate energy.** $60$ nJ (10 mK conventional) versus $3.7$ nJ (4 K parity-protected): a $16.2\times$ advantage for the 4 K architecture.
5. **Per-logical-gate energy.** $60\ \mathrm{\mu J}$ versus $37$ nJ with overhead factors $N_{\mathrm{conv}} = 1000$ and $N_{\mathrm{par}} = 10$: a $1.6\times 10^{3}\times$ advantage.
6. **Projection (labeled).** Under the stated assumptions, a $10^{4}$-logical-qubit machine at $10^{6}$ logical gates/s/qubit would draw $\sim 0.60$ MW of qubit-stage cooling power at 10 mK versus $\sim 370$ W at 4 K. Uncertainty is dominated by the assumed second-law efficiencies ($\eta$) and overhead factors ($N_{\mathrm{phys}}$); varying $\eta_{\mathrm{mK}}$ over $0.002$–$0.01$ changes the 10 mK figure by a factor of $2.5$ in either direction, and the comparison remains favorable to 4 K for any $\eta_{\mathrm{mK}} < 0.02 \times (q_{\mathrm{par}}/q_{\mathrm{conv}})^{-1} \times (N_{\mathrm{par}}/N_{\mathrm{conv}})^{-1} \approx 2$ — i.e., for all physically realistic efficiencies.

## 6. Discussion

**Limitations and failure modes.** The comparison rests on three sensitive assumptions. First, the second-law efficiencies $\eta$ are stated, not measured for any specific machine; the facilities literature [1], [3], [5], [7] documents plant architectures but not per-watt figures at the millikelvin stage, so $\eta_{\mathrm{mK}} = 0.005$ could be optimistic or pessimistic by several-fold. Second, the per-qubit dissipation figures $q_{\mathrm{conv}} = 10$ nW and $q_{\mathrm{par}} = 1\ \mathrm{\mu W}$ are order-of-magnitude engineering guesses; if 4 K cryo-control per parity qubit were $100\ \mathrm{\mu W}$ rather than $1\ \mathrm{\mu W}$, the physical-gate advantage would invert ($E_{\mathrm{gate}}^{\mathrm{par}} = 370$ nJ $> 60$ nJ), and the logical-gate advantage would then hinge entirely on the overhead ratio $N_{\mathrm{conv}}/N_{\mathrm{par}} = 100$. Third, the protection floor $\varepsilon_{\mathrm{prot}} = 10^{-4}$ is a design aspiration; if quasiparticle poisoning or junction fabrication disorder [2] limits real devices to $10^{-2}$, the crossover temperature rises to $T^{*} = 0.240/\ln(100) = 0.052$ K $= 52$ mK — still far above dilution operating points, but the logical-overhead advantage $N_{\mathrm{par}} = 10$ would collapse.

**What would falsify the claims.** (i) A demonstration that dilution-refrigerator second-law efficiency improves dramatically with scale, flattening the $1/T_c$ divergence. (ii) A parity-protected qubit with a demonstrated error floor worse than the thermal error of a conventional qubit at an economically achievable temperature, i.e., $\varepsilon_{\mathrm{prot}} > e^{-\Delta/(k_B T)}$ at $T \gtrsim 20$ mK. (iii) Evidence that 4 K cryo-control dissipation cannot be brought below $\sim 10\ \mathrm{\mu W}$ per qubit, erasing the physical-gate advantage. Any of these would overturn the headline conclusion.

**Open questions.** Does parity protection survive the wiring and readout heat loads that dominate real cryostats [7]? Can gate-voltage control [8] be exercised with 4 K electronics at the required fidelity? Is the $0$-$\pi$/topological-junction fabrication robustness [2] manufacturable at the $N_{\mathrm{par}} = 10$ overhead assumed here? We flag these as unresolved and essential to the architecture's viability.

## 7. Conclusion

Cooling toward absolute zero is thermodynamically self-defeating: the wall-plug cost of removing heat diverges as $1/T_c$, and beyond a computable crossover temperature ($\approx 26$ mK for transmon-like gaps and a $10^{-4}$ protection floor), additional cooling buys no error-rate improvement that a parity-protected encoding does not already provide. Under explicit, stated assumptions, a parity-protected qubit array at 4 K is projected to use $\sim 16\times$ less wall-plug energy per physical gate and $\sim 1.6\times 10^{3}\times$ less per logical gate than a conventional millikelvin array. The claim is falsifiable on the three axes identified above, and the decisive experiments — measuring real protection floors and 4 K control dissipation — are within reach of current hardware programs [2], [4], [6], [8].

## References

[1] arXiv:2308.11045v1 | Warm Compressor system Overview and status of the PIP-II cryogenic system
[2] arXiv:2308.12027v1 | Parity-protected superconducting qubit based on topological insulators
[3] arXiv:2308.15610v1 | Integration of a new Cryogenic Liquefier into the IB-1 Cryogenic Test Facility
[4] arXiv:2004.03975v2 | A Parity-Protected Superconductor-Semiconductor Qubit
[5] arXiv:1206.6796v1 | Design and testing of the New Muon Lab cryogenic system at Fermilab
[6] arXiv:1105.0315v1 | Top-transmon: hybrid superconducting qubit for parity-protected quantum computation
[7] arXiv:2509.15369v1 | Fermilab PIP-II CDS and CM Cryogenic Controls System
[8] arXiv:2607.04097v1 | Full Gate-Voltage Control of a Parity-Protected Superconducting Qubit with an Altermagnetic Josephson Junction
[9] QNFO: Thermodynamic Imperative | DOI 10.5281/zenodo.17928156
[10] QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing | DOI 10.5281/zenodo.17937531
[11] QNFO: Syntactic Generation | DOI 10.5281/zenodo.22758173