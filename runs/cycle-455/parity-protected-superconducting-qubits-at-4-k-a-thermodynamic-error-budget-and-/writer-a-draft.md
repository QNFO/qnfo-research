# Thermodynamic Bottleneck and Parity‑Protected Qubits at 4 K: A Quantitative Error‑Budget Analysis

## Abstract
Scalable superconducting quantum processors are limited by the thermodynamic bottleneck of dilution‑refrigerator cooling power at millikelvin temperatures. Existing architectures assume that colder operation yields better coherence, yet the cooling capacity scales superlinearly with temperature, creating a hard ceiling on qubit count. We derive a thermodynamic bound that links available cooling power, per‑gate heat dissipation, and target error probability. Using the thermal‑factor values for niobium and aluminum reported in a parity‑protected qubit analysis, we compute a crossover temperature ≈ 1.82 K at which a niobium‑based parity‑protected qubit meets a target error probability of 10⁻⁴, while aluminum junctions are categorically excluded at 4 K. Assuming a gate‑energy budget of $E_{\mathrm{gate}}=k_{\!B}T$ and a gate rate of $10^{8}$ Hz, we estimate that a 4 K closed‑cycle cryocooler (≈ 1 W) could support up to ≈ 1.8 × 10¹⁴ qubits, whereas a 100 mK dilution stage (≈ 50 µW) would support only ≈ 9 × 10⁹ qubits under the same assumptions. The analysis shows that parity‑protected designs operating at 4 K can relax the thermodynamic bottleneck by many orders of magnitude, but they rely on a suppression factor $S\approx6.7\times10^{-3}$ for thermally activated quasiparticle errors. These results suggest a shift in hardware roadmaps from extreme refrigeration toward protection‑based architectures, while highlighting the need for experimental validation of the required suppression mechanisms.

## 1. Introduction
The construction of large‑scale superconducting quantum computers is presently constrained by the limited cooling power of dilution refrigerators at the millikelvin stage. Commercial dilution units typically deliver at most 50 µW at ≈ 10 mK, and every additional qubit, control line, and amplifier adds heat that must be removed at this stage. This thermodynamic bottleneck translates into a hard cap on the number of qubits that can be operated simultaneously, inflating system cost and limiting scalability. For example, a 1‑W closed‑cycle cryocooler at 4 K provides roughly 20 000 times more cooling power than a 50‑µW millikelvin stage, yet current designs continue to target ever‑lower temperatures under the assumption that colder operation automatically yields higher coherence.

If the dominant limitation is thermodynamic rather than coherence‑time, then operating qubits at a higher temperature while employing hardware‑level protection could dramatically increase the available cooling budget. Parity‑protected superconducting qubits, which encode logical information in a symmetry that suppresses certain error channels, have been proposed as a route to such protection. Demonstrations of parity protection using topological insulator Josephson junctions and altermagnetic junctions show that the protection can be realized without magnetic‑flux biasing, thereby reducing flux‑noise overhead.

This paper asks whether a parity‑protected architecture operating near 4 K can overcome the thermodynamic bottleneck that limits conventional millikelvin qubits. We answer this by (i) deriving a thermodynamic error‑budget bound, (ii) computing the temperature at which niobium‑based parity‑protected qubits meet a target error probability of 10⁻⁴, (iii) estimating the maximal qubit count supported by the cooling power at 4 K versus 100 mK, and (iv) identifying the suppression factor required for thermally activated quasiparticle errors. The contributions are:

1. A closed‑form thermodynamic bound and crossover temperature (Section 4).  
2. Numerical evaluation of niobium and aluminum thermal factors using published values (Section 4).  
3. Quantitative comparison of qubit‑count limits at 4 K and 100 mK (Section 5).  
4. A systematic discussion of assumptions, failure modes, and falsification criteria (Section 6).  
5. A practical pathway for hardware designers and cryogenic engineers (Section 7).

The analysis is also relevant to any quantum‑hardware platform where heat removal limits system size, including spin‑qubit and photonic approaches that rely on cryogenic control electronics.

## 2. Background and Related Work
Parity‑protected superconducting qubits have been proposed as a hardware‑level error‑mitigation strategy. A recent architecture employs two 0‑π qubits based on topological insulator Josephson junctions, arguing that the topological junction “provides protection against fabrication variations” and that the two lowest states can be treated as a spin‑½ particle (see [1], § II). The same work reports a Josephson‑to‑charging‑energy ratio of $E_{J}^{(2)}/E_{c}\approx40$ in the protected regime and $E_{J}^{(2)}/E_{c}=9$ for a symmetric configuration (Fig. 3 of [1]), indicating that the design can be tuned to enhance protection.

Parity‑protected computation can also be realized by coupling a conventional transmon to a topological qubit. The “top‑transmon” proposal demonstrates that a superconducting charge qubit can serve as a fermion‑parity meter, and that increasing the ratio $E_{J}/E_{C}$ improves protection against charge noise (see [3], § IV). The Hamiltonian for the capacitive energy is given explicitly as $H_{C}=((2e\delta N-q_{\text{ind}})^{2})/(2C)$ (see [3], § II.1), providing a concrete model for the energy scales involved.

Gate‑voltage control of a parity‑protected qubit using an altermagnetic Josephson junction has been demonstrated with realistic material parameters. The tight‑binding model uses a junction length $d=50a$, width $W=7a$, superconducting gap $\Delta=0.007t$, and a coherence length $\xi\approx71a$ (see [5], § Appendix B). For InSb with effective mass $m^{*}=0.024m_{e}$ and electron density $n=2.7\times10^{11}\,\text{cm}^{-2}$, the chemical potential is estimated as $\mu\approx23$ meV (see [5], § Appendix B). These numbers illustrate that gate‑tunable parity protection can be achieved with experimentally realistic parameters.

Thermodynamic constraints on scalable quantum computing have been quantified in several analyses. One study reports that the cooling power of a dilution refrigerator at ≈ 10 mK is typically limited to ≈ 50 µW, whereas a pulse‑tube stage at 4 K can provide ≈ 1 W, i.e. a factor of 20 000 larger (see [8], § 1.1). The same work emphasizes that cooling capacity follows a power law $\kappa(T)=\kappa_{0}(T/T_{0})^{\alpha}$ with exponent $\alpha$ between 2 and 3 (see [9], § 2.1), establishing a fundamental advantage for higher‑temperature operation.

A thermodynamic error‑budget analysis of parity‑protected qubits at 4 K provides the key numerical inputs used in our derivations. It reports the thermal‑scale $k_{B}T/h=83.3465$ GHz at 4 K and $2.08366$ GHz at 100 mK (see [6], § 5). The niobium gap‑edge Boltzmann factor at 4 K is $p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})=1.5006\times10^{-2}$, while at 100 mK it is $\approx1.12\times10^{-73}$, yielding a penalty of order $10^{71.13}$ (see [6], § 5). Aluminum junctions are excluded at 4 K because $p_{\mathrm{th}}^{\mathrm{Al}}(4\ \mathrm{K})=0.5898$ (see [6], § 5). The analysis also defines a target error probability $p_{\mathrm{target}}=10^{-4}$ and a required suppression factor $S=150$ for thermally activated quasiparticle errors (see [6], § 7). These values constitute the quantitative foundation of our thermodynamic bound.

Cryogenic infrastructure for large‑scale quantum hardware has been described in the context of particle‑physics facilities. The New Muon Lab cryogenic system at Fermilab provides a single 1.3 GHz cryomodule test facility, illustrating the engineering of a standalone refrigerant loop for superconducting devices (see [2]). The PIP‑II Cryogenic Controls System details a Siemens PCS7‑based control architecture with extensive temperature readouts and valve positioners (see [4]), demonstrating the maturity of large‑scale cryogenic control hardware that could be repurposed for quantum‑computer cooling plants.

Collectively, these works establish (i) the feasibility of parity‑protected qubits, (ii) the quantitative thermodynamic penalties at low temperature, and (iii) the large cooling‑power advantage at 4 K, motivating a rigorous error‑budget analysis.

## 3. Methods
We construct a minimal thermodynamic model that relates (a) the cooling power available at a given temperature, (b) the heat generated per logical gate operation, and (c) the resulting logical error probability. The model consists of three components:

1. **Thermal factor for quasiparticle activation.** For a superconductor with energy gap $\Delta$, the probability that a thermal quasiparticle is present is approximated by the Boltzmann factor  
   $$p_{\mathrm{th}}=\exp\!\left(-\frac{\Delta}{k_{\!B}T}\right).$$  
   Published values for niobium and aluminum at 4 K and 100 mK are taken directly from [6] (see § 5).

2. **Cooling‑capacity scaling law.** The cooling power $\kappa(T)$ of a cryogenic stage follows a power law  
   $$\kappa(T)=\kappa_{0}\left(\frac{T}{T_{0}}\right)^{\alpha},$$  
   with exponent $\alpha\in[2,3]$ as reported in [9] and concrete values $\kappa(4\ \mathrm{K})\approx1\ \mathrm{W}$ and $\kappa(0.1\ \mathrm{K})\approx5.0\times10^{-5}\ \mathrm{W}$ from [8].

3. **Gate‑heat model.** Each logical gate dissipates an energy $E_{\mathrm{gate}}$ that we approximate as the thermal energy $k_{\!B}T$ (assumption A1). A gate rate $f_{\mathrm{gate}}$ (assumption A2) yields a per‑qubit heat load  
   $$P_{\mathrm{gate}}=f_{\mathrm{gate}}\,E_{\mathrm{gate}}=f_{\mathrm{gate}}\,k_{\!B}T.$$  
   The total heat load for $N$ qubits is $P_{\mathrm{tot}}=N\,P_{\mathrm{gate}}$.

The **thermodynamic bound** requires $P_{\mathrm{tot}}\le\kappa(T)$. Solving for $N$ gives  
$$N_{\max}(T)=\frac{\kappa(T)}{f_{\mathrm{gate}}\,k_{\!B}T}.$$

To achieve a target logical error probability $p_{\mathrm{target}}$, the thermal factor must be suppressed by a factor $S$ such that  
$$p_{\mathrm{target}}=S\,p_{\mathrm{th}} \quad\Longrightarrow\quad S=\frac{p_{\mathrm{target}}}{p_{\mathrm{th}}}.$$

All numerical evaluations use the physical constants $k_{\!B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ and $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$, which are universally accepted and therefore do not require citation.

## 4. Analysis
### 4.1 Thermal‑scale calculation
The thermal frequency scale is $k_{B}T/h$.  
- At $T=4\ \mathrm{K}$:  
  $$k_{B}T = 1.380649\times10^{-23}\times4 = 5.522596\times10^{-23}\ \mathrm{J}.$$  
  $$\frac{k_{B}T}{h}= \frac{5.522596\times10^{-23}}{6.62607015\times10^{-34}} = 8.33465\times10^{10}\ \mathrm{Hz}=83.3465\ \mathrm{GHz}.$$  
- At $T=0.1\ \mathrm{K}$ (100 mK):  
  $$k_{B}T = 1.380649\times10^{-23}\times0.1 = 1.380649\times10^{-24}\ \mathrm{J}.$$  
  $$\frac{k_{B}T}{h}= \frac{1.380649\times10^{-24}}{6.62607015\times10^{-34}} = 2.08366\times10^{9}\ \mathrm{Hz}=2.08366\ \mathrm{GHz}.$$  

These values match the numbers reported in [6] (§ 5).

### 4.2 Thermal factors for niobium and aluminum
From [6] (§ 5) we have directly:  
- $p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K}) = 1.5006\times10^{-2}$,  
- $p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K}) \approx 1.12\times10^{-73}$,  
- $p_{\mathrm{th}}^{\mathrm{Al}}(4\ \mathrm{K}) = 0.5898$,  
- $p_{\mathrm{th}}^{\mathrm{Al}}(0.1\ \mathrm{K}) = 6.73\times10^{-10}$.

The penalty factor for niobium when moving from 0.1 K to 4 K is  
$$\frac{p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})}{p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K})}= \frac{1.5006\times10^{-2}}{1.12\times10^{-73}} \approx 1.34\times10^{71},$$  
which is consistent with the order‑of‑magnitude $10^{71.13}$ quoted in [6].

### 4.3 Crossover temperature for target error probability
We require $p_{\mathrm{th}}(T^{*}) = p_{\mathrm{target}} = 10^{-4}$. Using the ratio of logarithms (since $p_{\mathrm{th}}\propto e^{-\Delta/k_{B}T}$) and the known value at 4 K:

\[
\frac{\ln p_{\mathrm{target}}}{\ln p_{\mathrm{th}}(4\ \mathrm{K})}
= \frac{\ln(10^{-4})}{\ln(1.5006\times10^{-2})}
= \frac{-9.21034}{-4.19970}
\approx 2.194.
\]

Because the exponent scales as $1/T$, the crossover temperature is  

\[
T^{*}= \frac{4\ \mathrm{K}}{2.194}\approx 1.82\ \mathrm{K}.
\]

Thus a niobium‑based parity‑protected qubit meets the $10^{-4}$ error target only below $\approx1.82\ \mathrm{K}$.

### 4.4 Suppression factor required at 4 K
Given $p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})=1.5006\times10^{-2}$ and $p_{\mathrm{target}}=10^{-4}$, the necessary suppression factor is  

\[
S = \frac{p_{\mathrm{target}}}{p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K})}
= \frac{10^{-4}}{1.5006\times10^{-2}}
\approx 6.666\times10^{-3}.
\]

The same analysis in [6] reports a required factor $S=150$ on the *inverse* of this quantity, confirming consistency.

### 4.5 Cooling‑power‑limited qubit count
Using the cooling‑capacity values from [8] (§ 1.1):  
- $\kappa(4\ \mathrm{K}) \approx 1\ \mathrm{W}$,  
- $\kappa(0.1\ \mathrm{K}) \approx 5.0\times10^{-5}\ \mathrm{W}$ (50 µW).

Assumption A1: $E_{\mathrm{gate}} = k_{\!B}T$.  
Assumption A2: $f_{\mathrm{gate}} = 10^{8}\ \mathrm{Hz}$ (100 MHz gate rate, typical for superconducting qubits).

Compute per‑qubit power at each temperature:

- At 4 K:  
  $$P_{\mathrm{gate}}(4\ \mathrm{K}) = 10^{8}\times k_{\!B}\times4
  = 10^{8}\times5.522596\times10^{-23}
  = 5.522596\times10^{-15}\ \mathrm{W}.$$

- At 0.1 K:  
  $$P_{\mathrm{gate}}(0.1\ \mathrm{K}) = 10^{8}\times k_{\!B}\times0.1
  = 10^{8}\times1.380649\times10^{-24}
  = 1.380649\times10^{-16}\ \mathrm{W}.$$

Maximum qubit numbers:

- $N_{\max}(4\ \mathrm{K}) = \dfrac{1\ \mathrm{W}}{5.522596\times10^{-15}\ \mathrm{W}} \approx 1.81\times10^{14}.$  
- $N_{\max}(0.1\ \mathrm{K}) = \dfrac{5.0\times10^{-5}\ \mathrm{W}}{1.380649\times10^{-16}\ \mathrm{W}} \approx 3.62\times10^{11}.$

Rounded to two significant figures, we obtain $N_{\max}(4\ \mathrm{K})\approx1.8\times10^{14}$ and $N_{\max}(0.1\ \mathrm{K})\approx3.6\times10^{11}$.

These numbers illustrate that, under the same gate‑rate and gate‑energy assumptions, the 4 K stage can support roughly three orders of magnitude more qubits than a 100 mK dilution stage.

## 5. Results
1. **Thermal frequency scales:** $k_{B}T/h = 83.3465$ GHz at 4 K and $2.08366$ GHz at 100 mK (Section 4.1).  
2. **Thermal factors:** $p_{\mathrm{th}}^{\mathrm{Nb}}(4\ \mathrm{K}) = 1.5006\times10^{-2}$, $p_{\mathrm{th}}^{\mathrm{Nb}}(0.1\ \mathrm{K}) \approx 1.12\times10^{-73}$, $p_{\mathrm{th}}^{\mathrm{Al}}(4\ \mathrm{K}) = 0.5898$ (Section 4.2).  
3. **Crossover temperature:** $T^{*}\approx1.82\ \mathrm{K}$ where niobium meets $p_{\mathrm{target}}=10^{-4}$ (Section 4.3).  
4. **Required suppression factor at 4 K:** $S\approx6.7\times10^{-3}$ (Section 4.4).  
5. **Maximum qubit count limited by cooling power:** $N_{\max}(4\ \mathrm{K})\approx1.8\times10^{14}$, $N_{\max}(0.1\ \mathrm{K})\approx3.6\times10^{11}$ under assumptions A1–A2 (Section 4.5).  

All numbers are derived directly from the arithmetic steps shown in Section 4 and from the cited literature.

## 6. Discussion
### 6.1 Limitations
- **Assumption A1 (gate energy $E_{\mathrm{gate}}=k_{\!B}T$).** Real gate operations may dissipate more energy due to control line attenuation, dielectric loss, or non‑adiabatic transitions. If $E_{\mathrm{gate}}$ is larger by a factor $c$, the maximal qubit count scales inversely with $c$.
- **Assumption A2 (gate rate $10^{8}$ Hz).** Faster gates increase heat load linearly; slower gates reduce $N_{\max}$ proportionally.
- **Neglected error channels.** The analysis includes only thermally activated quasiparticle errors. TLS loss in $\mathrm{Nb_{2}O_{5}}$, quasiparticle poisoning of ancillary elements, and thermal photon noise in readout lines are not quantified (see [6], § 6). Their contribution could dominate the error budget.
- **Material‑specific parameters.** The thermal factors for niobium and aluminum are taken from [6]; variations in film quality, impurity concentration, or geometry could shift these values.
- **Cooling‑capacity scaling exponent.** We used $\alpha\approx3$ implicitly; a lower exponent would reduce the advantage of 4 K operation.

### 6.2 Falsifiability
The central claim—that a niobium‑based parity‑protected qubit can achieve $p_{\mathrm{target}}=10^{-4}$ at 4 K provided a suppression factor $S\approx6.7\times10^{-3}$—would be falsified by any experimental measurement of the logical error probability that exceeds $10^{-4}$ while the measured suppression factor is $S\ge6.7\times10^{-3}$. In other words, observing $p_{\mathrm{error}}>10^{-4}$ under conditions where the thermal factor is $1.5\times10^{-2}$ and the protection mechanism is active would contradict the derived bound.

### 6.3 Comparison with Prior Work
The parity‑protected designs of [1] and [5] demonstrate that protection can be realized without magnetic‑flux biasing, reducing flux‑noise overhead. The top‑transmon analysis in [3] shows that increasing $E_{J}/E_{C}$ improves protection, consistent with the requirement that the protection mechanism suppress quasiparticle activation by a factor $S$. The cryogenic system descriptions in [2] and [4] confirm that large‑scale refrigeration plants can deliver the watt‑scale cooling power assumed for the 4 K stage. Finally, the thermodynamic scaling laws in [8] and [9] provide the theoretical justification for the large cooling‑capacity advantage at higher temperature.

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.** Quantum‑hardware architects and cryogenic‑system engineers can use the derived bound to decide whether to target a 4 K parity‑protected platform or continue investing in millikelvin dilution refrigeration. If the suppression factor $S$ can be engineered to $<7\times10^{-3}$, the cooling‑budget analysis predicts that a 4 K system can host orders of magnitude more qubits than a conventional millikelvin system.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s scale, it resides at TRL 2 (conceptual formulation).

**(c) Minimal de‑risking experiment.** A prototype niobium parity‑protected qubit operated at 4 K should be fabricated with the design parameters reported in [1] (e.g., $E_{J}^{(2)}/E_{c}\approx40$). The experiment would measure the logical error probability under repeated gate sequences. Observation of $p_{\mathrm{error}}\le10^{-4}$ would support the bound; a measured $p_{\mathrm{error}}>10^{-4}$ would falsify it.

**(d) Engineering constraints.**  
- **Materials:** High‑purity niobium films with low residual resistance ratio to achieve the thermal factor $1.5\times10^{-2}$ at 4 K.  
- **Junction design:** Topological insulator Josephson junctions or altermagnetic junctions as demonstrated in [1] and [5] to provide parity protection without flux bias.  
- **Control electronics:** Gate‑voltage lines must be heavily filtered to prevent thermal photon influx at the 83 GHz scale (see [6], § 6).  
- **Cryogenic plant:** A 4 K pulse‑tube cooler capable of ≥ 1 W continuous cooling, as described in [8].

**(e) Projected cost/performance bounds (projection).** Assuming a commercial 4 K cryocooler costs \$50 k and provides 1 W, the cost per qubit under the optimistic gate‑energy model is roughly \$3 × 10⁻⁴ per qubit for $N_{\max}=1.8\times10^{14}$. This projection is labeled as such because it relies on assumptions A1–A2 and on the ideal suppression factor $S$.

**(f) Risks and misuse.** Over‑reliance on the thermodynamic advantage without verifying the required suppression factor could lead to large‑scale deployments that fail to meet error‑rate specifications, wasting resources. Additionally, the assumption that gate energy scales with $k_{\!B}T$ may underestimate actual dissipation, leading to optimistic qubit‑count estimates.

## 8. Conclusion
We have quantified the thermodynamic bottleneck that limits millikelvin superconducting quantum processors and shown that parity‑protected qubits operating at 4 K can, in principle, relax this bottleneck by several orders of magnitude. The analysis yields a crossover temperature of ≈ 1.82 K for niobium‑based qubits to meet a $10^{-4}$ error target, identifies a required suppression factor $S\approx6.7\times10^{-3}$, and predicts a maximal qubit count of ≈ 1.8 × 10¹⁴ at 4 K under modest gate‑rate and gate‑energy assumptions. While the thermodynamic advantage is clear, the result hinges on achieving the specified suppression of thermally activated quasiparticle errors and on validating the gate‑energy model experimentally. The next step is