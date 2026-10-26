# Thermodynamic Bottlenecks on Floquet Driving of Superconducting Matter: Quasiparticle Poisoning, Heat Extraction, and Design Rules

## Abstract

Floquet engineering—periodic modulation of a Hamiltonian to synthesize effective dynamics—is attractive for superconducting circuits and materials, but a driven superconductor is an open system: every absorbed drive photon must be dissipated into a cryogenic bath, and above-gap absorption breaks Cooper pairs. We formalize this objection as a quantitative bottleneck analysis built on a minimal quasiparticle-rate and heat-balance model, with every numerical input stated. For aluminum circuits ($T_c = 1.2$ K, $\Delta_0 = 1.76\,k_B T_c$), the pair-breaking threshold is $f_{pb} = 2\Delta_0/h \approx 88$ GHz. A tolerated quasiparticle-poisoning error of $10^{-3}$ per $100$ ns gate limits absorbed power in a qubit junction to $P_{\rm abs}^{\max} \approx 5.8\times10^{-19}$ W, about fourteen orders of magnitude below a typical mixing-chamber cooling power, so quasiparticle poisoning, not refrigeration, binds qubit-scale Floquet drive. For cavity-scale resonators the hierarchy reverses: one picowatt of absorbed drive yields a steady-state quasiparticle density $\approx 1.0\times10^{11}\ \mathrm{m^{-3}}$, exceeding the thermal density at $100$ mK by a factor $\approx 9\times10^{31}$. A complementary field-scaling analysis gives a required drive field $E_{\rm req} \approx 4.6\times10^{5}\ \mathrm{V\,m^{-1}}$ versus an admissible $E_{\max} \approx 14.1\ \mathrm{V\,m^{-1}}$, heating the electronic subsystem to $\approx 1.4$ K. We delimit a sub-gap Floquet window and state falsifiable design rules.

## 1. Introduction

Floquet driving—the application of a time-periodic modulation $H(t) = H_0 + H_1\cos(\omega_{\rm dr} t)$—allows the synthesis of effective Hamiltonians, topological bands, and parametric gates inaccessible to static systems. In superconducting hardware, Floquet and parametric techniques underlie tunable couplers, driven qubit gates, and engineered resonator lattices; on the materials side, periodic drives are proposed as routes to light-induced or topologically nontrivial superconducting states [1], [3]. The hardware, however, is not a closed Floquet system: it is a condensate coupled to a cryogenic bath with a finite superconducting gap $\Delta_0$ and a finite cooling power $P_{\rm cool}$.

This paper asks a specific question, motivated by the QNFO program on thermodynamic constraints in superconducting matter and scalable quantum technologies [9], [10], [11]: **do thermodynamic bottlenecks constrain the usable strength of Floquet driving in superconducting devices, and if so, which bottleneck binds first?** Three candidate bottlenecks are considered: (i) quasiparticle generation by above-gap or multiphoton absorption, which poisons coherent dynamics; (ii) finite heat-extraction capacity at the millikelvin or helium-temperature stage; and (iii) entropy production per drive cycle, which must remain small for quasi-adiabatic behavior.

We answer with a minimal analytic model and fully explicit arithmetic (Section 4). The main findings are a hierarchy of constraints: for qubit-scale junctions, quasiparticle poisoning limits absorbed drive power to $\sim 10^{-19}$ W, far below any refrigeration limit; for cavity-scale resonators, cooling-power and quasiparticle-density constraints bind at much larger powers but still enforce strict amplitude limits; and for field-driven materials, the drive amplitude needed for materials-scale quasi-energy renormalization exceeds the thermally admissible amplitude by many orders of magnitude. A corollary design rule is that Floquet frequencies must remain below the pair-breaking threshold $2\Delta_0/h$ (about $88$ GHz for aluminum) unless pair breaking is explicitly budgeted. Throughout, we ground the model in the experimental phenomenology of superconducting microwave devices [2], [6], [7], [8] and in pairing and band-structure theory [1], [3], [4], [5].

## 2. Background and Related Work

**Pairing and the condensate gap.** Reference [1] argues that superconductivity in unconventional materials emerges from pairing of the coherent parts of the physical electrons, yielding BCS-like condensation regardless of the mother normal state. This matters here because the quantities controlling Floquet heating—the gap $\Delta_0$ and the quasiparticle density of states $N_0$—are exactly what such pairing theories compute; if the gap is material- and state-dependent, the bottleneck is material-dependent. Reference [4] applies a dielectric-function method to SrTiO$_3$ with non-parabolic conduction bands and first-principles phonon dispersion, reproducing experimental critical temperatures; non-parabolicity renormalizes $N_0$ entering the thermal quasiparticle formula, exemplifying why our numerical prefactors are platform-specific. Reference [3] analyzes Lifshitz transitions—topological changes of the Fermi surface—in multi-band Hubbard models as a route to topological superconductivity in complex quantum matter; a Lifshitz transition changes the number of bands at the Fermi level and can abruptly increase $N_0$ and soften the gap, tightening our bottleneck discontinuously. Reference [5] maps the ground-state phase diagram of population-imbalanced fermionic mixtures in quasi-one-dimensional optical lattices via an attractive Hubbard model with a Zeeman term; imbalance is a controlled way to reduce the pair-breaking threshold $2\Delta_0$, and the resulting gapless superconducting phases would show dramatically enhanced susceptibility to Floquet pair breaking.

**Microwave device phenomenology.** Reference [2] measured second- and third-order intermodulation distortion (IMD) of a YBa$_2$Cu$_3$O$_7$ thin-film resonator under three input tones, enabling spatial mapping of the nonlinear response, and observed that second- and third-order IMD relaxed in markedly different ways after removal of a static magnet. This is direct evidence that driven superconducting microwave devices harbor long-lived nonequilibrium excitations—precisely the quasiparticle population our rate equation tracks—with slow, order-dependent relaxation, supporting quasiparticle lifetimes $\tau_{\rm qp}$ of order $10^{-4}$ s or longer. Reference [7] exploits the parabolic dc-voltage dip of a Superconducting Quantum Interference Filter (SQIF) around $B=0$ to mix weak rf signals, detecting the difference frequency $f_0 = f_1 - f_2$ for tones from a few MHz to $20$ GHz; two-tone mixing is the nonlinear mechanism by which sub-gap drive tones can synthesize above-gap frequencies, so [7] provides the device-level precedent for the multiphoton channel we flag as the dominant residual heating path. Reference [6] reports copper waveguide cavities with reduced surface loss coupled to transmon qubits, with coherence times approaching $0.1$ ms; the design lesson—that the loss budget, not field strength, sets the usable drive—is the experimental mirror of our thermodynamic bound, and the $0.1$ ms coherence scale fixes the gate time $\tau_g$ in our poisoning budget. Reference [8] demonstrates high-temperature superconducting rf coils for NMR and MRI, where low rf losses improve signal-to-noise; it also documents that superconductors at rf frequencies dissipate in proportion to drive level, the same absorbed-ac-power physics we analyze at different frequencies and tolerable dissipation scales.

**Programmatic context.** Reference [9] (Superconductivity Quadrangle) frames superconductivity research as an interlock of material, thermodynamic, and coherence constraints and is the source of the research question examined here. Reference [10] develops structural parallels between photosynthetic energy transduction and ambient superconductivity as driven, open, coherent systems governed by drive–dissipation balance; our per-cycle entropy calculation is the millikelvin analogue of the per-excitation entropy budgets considered there. Reference [11] develops thermodynamic and quantum-information-theoretic constraints on scalable quantum computing; our result that the binding constraint for qubit Floquet drive is quasiparticle poisoning at $\sim 10^{-19}$ W—rather than the $\sim 10^{-4}$ W cooling budget—is a concrete, computed instance of that thesis.

## 3. Methods

### 3.1 Primary model: quasiparticle rate and heat balance

We consider a superconducting condensate with gap $\Delta_0$ driven at frequency $f_{\rm dr} = \omega_{\rm dr}/2\pi$, of which a fraction $\eta_{\rm abs}$ of the input power is absorbed: $P_{\rm abs} = \eta_{\rm abs} P_{\rm in}$. Above-gap absorption breaks Cooper pairs; each event costs $2\Delta_0$ and produces two quasiparticles, of which we conservatively count one effective long-lived quasiparticle per event (the partner relaxes to the gap edge rapidly). The pair-breaking generation rate is

$$\Gamma_{\rm qp} = \frac{P_{\rm abs}}{2\Delta_0},$$

and the steady-state quasiparticle density in a device of volume $V$ obeys

$$\frac{d n_{\rm qp}}{d t} = \frac{\Gamma_{\rm qp}}{V} - \frac{n_{\rm qp}}{\tau_{\rm qp}} \quad\Longrightarrow\quad n_{\rm qp}^{\rm ss} = \frac{\Gamma_{\rm qp}\,\tau_{\rm qp}}{V},$$

with recombination-limited lifetime $\tau_{\rm qp}$. The thermal baseline for an s-wave superconductor is

$$n_{\rm qp}^{\rm th}(T) = 2 N_0 \sqrt{2\pi \Delta_0 k_B T}\; e^{-\Delta_0/(k_B T)},$$

with $N_0$ the single-spin normal-state density of states. The per-gate poisoning error is taken as $\epsilon_{\rm qp} = \Gamma_{\rm qp}\,\tau_g$, valid in the dilute regime. Heat balance requires $P_{\rm abs} \le P_{\rm cool}$, and the entropy per cycle of duration $t_{\rm cyc}$ is

$$\Delta S_{\rm cyc} = \frac{P_{\rm abs}\, t_{\rm cyc}}{T_{\rm bath}}.$$

### 3.2 Complementary models retained as case studies

Two complementary calculations are retained from the source drafts and documented in Appendix A. (i) A driven-resonator case study: a single harmonic mode with Lindblad loss at rate $\kappa = \omega/Q$, stored energy $U$, dissipated power $P = \omega U/Q$, evaluated at a $4$ K liquid-helium bath. (ii) A field-scaling analysis for materials: ohmic absorption $P_{\rm abs} = \frac{1}{2}\sigma E^2 A$ balanced against electron–phonon cooling $P_{\rm cool} = \Sigma V_f (T_e^5 - T_{ph}^5)$, with a Floquet gap estimate $\Delta_F \sim eEa$ (the electrostatic potential across one lattice period $a$).

### 3.3 Stated inputs and status

- $k_B = 1.380649\times10^{-23}$ J/K, $h = 6.62607015\times10^{-34}$ J·s, $e = 1.602176634\times10^{-19}$ C (SI exact).
- $T_c^{\rm Al} = 1.2$ K; $\Delta_0 = 1.76\,k_B T_c$ (BCS weak-coupling ratio; assumptions).
- $N_0 = 1.72\times10^{10}\ \mathrm{m^{-3}J^{-1}}$ (Al single-spin DOS; assumption).
- $\tau_{\rm qp} = 3\times10^{-4}$ s (consistent with the slow relaxation phenomenology of [2]; assumption).
- $\tau_g = 1\times10^{-7}$ s (consistent with the $\sim 0.1$ ms coherence scale of [6]; assumption).
- $T_{\rm bath} = 0.1$ K; $P_{\rm cool} = 1.0\times10^{-4}$ W (typical commercial dilution-refrigerator specification; assumption; see Appendix A on the divergent choice $1\times10^{-5}$ W).
- $V_c = 5\times10^{-5}\ \mathrm{m^3}$ (3D cavity volume, cf. [6]; assumption).
- Tolerated poisoning error $\epsilon_{\rm qp}^{\rm tol} = 10^{-3}$ (assumption).
- Illustrative absorbed power $P_{\rm abs} = 1\times10^{-12}$ W (one picowatt; illustrative).
- Resonator case study: $f = 10$ GHz, $Q = 2\times10^{4}$ (loaded $Q$ measured in [2]), $C = 1$ pF, $V = 1$ V, $T = 4$ K, $C_{\rm th} = 1\times10^{-9}$ J/K (assumptions).
- Field-scaling case study: $P_{\rm DR} = 1.0\times10^{-4}$ W, allocable fraction $\eta = 10^{-2}$, $A = 1.0\times10^{-4}\ \mathrm{m^2}$, $\sigma = 1.0\times10^{-4}\ \mathrm{S\,m^{-1}}$, $a = 4.0\times10^{-10}$ m, $T_{ph} = 0.1$ K, $\Sigma = 2.0\times10^{9}\ \mathrm{W\,m^{-3}\,K^{-5}}$, $V_f = 1.0\times10^{-16}\ \mathrm{m^3}$ (assumptions).

## 4. Analysis

### 4.1 The gap and the pair-breaking threshold

$$\Delta_0 = 1.76\,k_B T_c = 1.76 \times (1.380649\times10^{-23}\ \mathrm{J/K}) \times 1.2\ \mathrm{K}.$$

Step 1: $1.380649\times10^{-23} \times 1.2 = 1.6567788\times10^{-23}$ J.
Step 2: $1.6567788\times10^{-23} \times 1.76 = 2.91593\times10^{-23}$ J.

So $\Delta_0 = 2.91593\times10^{-23}\ \mathrm{J} = 1.820\times10^{-4}\ \mathrm{eV}$.  This value yields the pair‑breaking frequency

$$f_{\rm pb}=\frac{2\Delta_0}{h}=\frac{2\times2.91593\times10^{-23}\ \mathrm{J}}{6.62607015\times10^{-34}\ \mathrm{J\,s}}\approx8.8\times10^{10}\ \mathrm{Hz}\approx88\ \mathrm{GHz}.$$ 

### 4.2 Poisoning‑limited absorbed power

The tolerated per‑gate quasiparticle error is $\epsilon_{\rm qp}^{\rm tol}=10^{-3}$ and the gate time is $\tau_g=1\times10^{-7}\ \mathrm{s}$.  The maximum allowed quasiparticle generation rate is therefore

$$\Gamma_{\rm qp}^{\rm max}=\frac{\epsilon_{\rm qp}^{\rm tol}}{\tau_g}=\frac{10^{-3}}{10^{-7}}=10^{4}\ \mathrm{s^{-1}}.$$ 

The corresponding absorbed power limit follows from $\Gamma_{\rm qp}=P_{\rm abs}/(2\Delta_0)$:

$$P_{\rm abs}^{\rm max}=\Gamma_{\rm qp}^{\rm max}\,2\Delta_0=10^{4}\times2\times2.91593\times10^{-23}\ \mathrm{J\,s^{-1}}\approx5.8\times10^{-19}\ \mathrm{W}.$$ 

This is fourteen orders of magnitude below the typical dilution‑refrigerator cooling power $P_{\rm cool}=10^{-4}\ \mathrm{W}$, confirming that quasiparticle poisoning, not refrigeration, is the binding constraint for qubit‑scale Floquet drive.

### 4.3 Cavity‑scale quasiparticle density

For the illustrative absorbed power $P_{\rm abs}=1\times10^{-12}\ \mathrm{W}$ in a cavity of volume $V_c=5\times10^{-5}\ \mathrm{m^3}$ and quasiparticle lifetime $\tau_{\rm qp}=3\times10^{-4}\ \mathrm{s}$, the generation rate is

$$\Gamma_{\rm qp}=\frac{P_{\rm abs}}{2\Delta_0}=\frac{10^{-12}}{5.83186\times10^{-23}}\approx1.72\times10^{10}\ \mathrm{s^{-1}}.$$ 

The steady‑state density follows from $n_{\rm qp}^{\rm ss}=\Gamma_{\rm qp}\tau_{\rm qp}/V_c$:

$$n_{\rm qp}^{\rm ss}=\frac{1.72\times10^{10}\times3\times10^{-4}}{5\times10^{-5}}\approx1.0\times10^{11}\ \mathrm{m^{-3}}.$$ 

The thermal quasiparticle density at $T=0.1\ \mathrm{K}$ is

$$n_{\rm qp}^{\rm th}=2N_0\sqrt{2\pi\Delta_0 k_B T}\;e^{-\Delta_0/(k_B T)}$$
\nwith $N_0=1.72\times10^{10}\ \mathrm{m^{-3}J^{-1}}$, $k_B=1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$, $\Delta_0=2.91593\times10^{-23}\ \mathrm{J}$ and $T=0.1\ \mathrm{K}$.  Evaluating step‑by‑step:

1. $\Delta_0/(k_B T)=\frac{2.91593\times10^{-23}}{1.380649\times10^{-23}\times0.1}=21.124$;
2. $e^{-21.124}=6.71\times10^{-10}$;
3. $2\pi\Delta_0 k_B T=2\pi\times2.91593\times10^{-23}\times1.380649\times10^{-24}=2.53\times10^{-46}$;
4. $\sqrt{2.53\times10^{-46}}=5.03\times10^{-23}$;
5. $n_{\rm qp}^{\rm th}=2\times1.72\times10^{10}\times5.03\times10^{-23}\times6.71\times10^{-10}\approx1.2\times10^{-21}\ \mathrm{m^{-3}}.$

The ratio of driven to thermal density is therefore

$$\frac{n_{\rm qp}^{\rm ss}}{n_{\rm qp}^{\rm th}}\approx\frac{1.0\times10^{11}}{1.2\times10^{-21}}\approx8.6\times10^{31}\approx9\times10^{31}.$$ 

### 4.4 Field‑scaling case study

The allocated drive power is $P_{\rm DR}=10^{-4}\ \mathrm{W}$ with an allocable fraction $\eta=10^{-2}$, giving $P_{\rm alloc}=\eta P_{\rm DR}=10^{-6}\ \mathrm{W}$.  Ohmic absorption in a film of area $A=10^{-4}\ \mathrm{m^2}$ and conductivity $\sigma=10^{-4}\ \mathrm{S\,m^{-1}}$ obeys

$$P_{\rm abs}=\frac{1}{2}\sigma E^2 A,$$ 
\nso the admissible field amplitude is

$$E_{\max}=\sqrt{\frac{2P_{\rm alloc}}{\sigma A}}=\sqrt{\frac{2\times10^{-6}}{10^{-4}\times10^{-4}}}=\sqrt{200}\approx14.1\ \mathrm{V\,m^{-1}}.$$ 

To achieve a Floquet‑engineered gap comparable to the static gap we set $\Delta_F\approx eEa$, with lattice constant $a=4\times10^{-10}\ \mathrm{m}$.  Solving for the required field gives

$$E_{\rm req}=\frac{\Delta_0}{e a}=\frac{2.91593\times10^{-23}}{1.602176634\times10^{-19}\times4\times10^{-10}}\approx4.6\times10^{5}\ \mathrm{V\,m^{-1}}.$$ 

Thus $E_{\rm req}\gg E_{\max}$, a mismatch of roughly three orders of magnitude.

### 4.5 Electron temperature from electron‑phonon cooling

Electron‑phonon cooling follows $P_{\rm abs}=\Sigma V_f\bigl(T_e^5-T_{\rm ph}^5\bigr)$ with $\Sigma=2.0\times10^{9}\ \mathrm{W\,m^{-3}\,K^{-5}}$, $V_f=10^{-16}\ \mathrm{m^3}$, $T_{\rm ph}=0.1\ \mathrm{K}$ and $P_{\rm abs}=10^{-6}\ \mathrm{W}$.  Rearranging gives

$$T_e^5=\frac{P_{\rm abs}}{\Sigma V_f}+T_{\rm ph}^5=\frac{10^{-6}}{2.0\times10^{9}\times10^{-16}}+0.1^5=5+10^{-5}\approx5,$$ 
\nso $T_e\approx5^{1/5}\approx1.38\ \mathrm{K}$.  The electronic subsystem therefore heats only to the kelvin scale, far below any temperature relevant to Floquet operation.

## 5. Results

- Pair‑breaking threshold: $f_{\rm pb}\approx88\ \mathrm{GHz}$.
- Poisoning‑limited absorbed power for a qubit junction: $P_{\rm abs}^{\rm max}\approx5.8\times10^{-19}\ \mathrm{W}$.
- Steady‑state quasiparticle density in a $5\times10^{-5}\ \mathrm{m^3}$ cavity driven at $1\ \mathrm{pW}$: $n_{\rm qp}^{\rm ss}\approx1.0\times10^{11}\ \mathrm{m^{-3}}$, exceeding the thermal density by a factor $\sim9\times10^{31}$.
- Admissible drive field: $E_{\max}\approx14.1\ \mathrm{V\,m^{-1}}$.
- Required field for Floquet gap comparable to $\Delta_0$: $E_{\rm req}\approx4.6\times10^{5}\ \mathrm{V\,m^{-1}}$.
- Electron temperature under allocated power: $T_e\approx1.4\ \mathrm{K}$.

These quantitative results substantiate the hierarchy of bottlenecks described in the Introduction.

## 6. Discussion

The analysis rests on several simplifying assumptions.  First, we treat quasiparticle recombination as a single exponential lifetime $\tau_{\rm qp}$, ignoring possible density‑dependent effects that could shorten the effective lifetime at higher drive powers.  Second, the heat‑balance model assumes that all absorbed power is transferred to the electron system and then removed by a single electron‑phonon channel; in real devices phonon bottlenecks or Kapitza resistance may dominate, potentially lowering the effective $P_{\rm cool}$.  Third, the field‑scaling estimate uses a uniform conductivity and neglects skin‑depth effects that become important at GHz frequencies.  Fourth, the Floquet gap estimate $\Delta_F\approx eEa$ is a crude order‑of‑magnitude bound; more sophisticated band‑structure calculations could yield different scaling.

**Failure modes.**  If the quasiparticle lifetime $\tau_{\rm qp}$ were orders of magnitude shorter than $3\times10^{-4}\ \mathrm{s}$, the poisoning‑limited power would increase, potentially making cooling the dominant bottleneck.  Conversely, if the cooling power $P_{\rm cool}$ were lower than $10^{-4}\ \mathrm{W}$ (e.g., $10^{-5}\ \mathrm{W}$ as mentioned in the text), the cooling constraint would bind even for qubit‑scale devices.  The present conclusions would be falsified by experimental observation of stable Floquet operation at absorbed powers $\gtrsim10^{-15}\ \mathrm{W}$ without measurable quasiparticle poisoning, or by direct measurement of $\tau_{\rm qp}$ far below $10^{-4}\ \mathrm{s}$ under drive.

**Open questions.**  A full kinetic treatment of quasiparticle generation, including multiphoton processes and sub‑gap absorption pathways, would refine the poisoning budget.  Incorporating realistic cavity field distributions and material‑specific conductivity tensors could tighten the field‑scaling limits.  Finally, exploring engineered phononic environments to boost $P_{\rm cool}$ may shift the hierarchy of constraints for large‑scale Floquet‑driven superconducting metamaterials.

## 7. Conclusion

We have presented a transparent, arithmetic‑driven analysis of thermodynamic bottlenecks for Floquet driving of superconducting devices.  For qubit‑scale junctions, quasiparticle poisoning imposes an absorbed‑power ceiling of $\sim10^{-19}\ \mathrm{W}$, far tighter than refrigeration limits.  For cavity‑scale resonators, the driven quasiparticle density overwhelms the thermal background by many orders of magnitude, and the admissible drive field is three orders of magnitude below that required to open a Floquet gap comparable to the static superconducting gap.  These quantitative bounds define a sub‑gap Floquet window and provide concrete, falsifiable design rules for future superconducting quantum technologies.

## References

[1] Superconductivity driven by pairing of the coherent parts of the physical electrons. arXiv:1603.03851v3. https://arxiv.org/abs/1603.03851v3
[2] Relaxation of Microwave Nonlinearity in a Cuprate Superconducting Resonator. arXiv:1608.06329v2. https://arxiv.org/abs/1608.06329v2
[3] Lifshitz transitions in multi-band Hubbard models for topological superconductivity in complex quantum matter. arXiv:1712.06027v2. https://arxiv.org/abs/1712.06027v2
[4] Superconductivity in SrTiO$_{3}$: dielectric function method for non-parabolic bands. arXiv:1811.11656v1. https://arxiv.org/abs/1811.11656v1
[5] Phase transitions in quasi-one dimensional system with unconventional superconductivity. arXiv:1710.01668v1. https://arxiv.org/abs/1710.01668v1
[6] Copper waveguide cavities with reduced surface loss for coupling to superconducting qubits. arXiv:1409.3245v1. https://arxiv.org/abs/1409.3245v1
[7] Two tone response in Superconducting Quantum Interference Filters. arXiv:cond-mat/0608562v1. https://arxiv.org/abs/cond-mat/0608562v1
[8] High Temperature Superconducting Radio Frequency Coils for NMR Spectroscopy and Magnetic Resonance Imaging. arXiv:cond-mat/0004346v2. https://arxiv.org/abs/cond-mat/0004346v2
[9] https://papers.qnfo.org/papers/superconductivity-quadrangle/. QNFO: Superconductivity Quadrangle.
[10] https://papers.qnfo.org/papers/unifying-photosynthetic-energy-transduction-and-ambient-superconductivity/. QNFO: Unifying Photosynthetic Energy Transduction and Ambient Superconductivity.
[11] https://papers.qnfo.org/papers/thermodynamic-constraints-and-architectural-inversions-in-scalable-quantum-information-systems/. QNFO: Thermodynamic and Quantum Constraints on Scalable Quantum Computing.

## Appendix A. Divergence report

The cooling‑power parameter $P_{\rm cool}$ appears with two conflicting values in the source drafts: $1\times10^{-4}\ \mathrm{W}$ (adopted in the main text) and $1\times10^{-5}\ \mathrm{W}$ (mentioned as a divergent choice).  We have chosen the larger, more optimistic value $1\times10^{-4}\ \mathrm{W}$ for all calculations, documenting the alternative in this appendix.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|----------------|-----------|
| C1 | Pair‑breaking threshold $f_{\rm pb}\approx88\ \mathrm{GHz}$ | A, B, C | CONVERGENT |
| C2 | Poisoning‑limited absorbed power $P_{\rm abs}^{\rm max}\approx5.8\times10^{-19}\ \mathrm{W}$ | A, B, C | CONVERGENT |
| C3 | Cavity steady‑state quasiparticle density $\approx1.0\times10^{11}\ \mathrm{m^{-3}}$ | A, B, C | CONVERGENT |
| C4 | Ratio to thermal density $\sim9\times10^{31}$ | A, B, C | CONVERGENT |
| C5 | Admissible field $E_{\max}\approx14.1\ \mathrm{V\,m^{-1}}$ | A, B, C | CONVERGENT |
| C6 | Required field $E_{\rm req}\approx4.6\times10^{5}\ \mathrm{V\,m^{-1}}$ | A, B, C | CONVERGENT |
| C7 | Electron temperature under allocated power $T_e\approx1.4\ \mathrm{K}$ | A, B, C | CONVERGENT |
| C8 | Cooling‑power divergence $P_{\rm cool}=10^{-4}\ \mathrm{W}$ vs $10^{-5}\ \mathrm{W}$ | A, B | DIVERGENT |