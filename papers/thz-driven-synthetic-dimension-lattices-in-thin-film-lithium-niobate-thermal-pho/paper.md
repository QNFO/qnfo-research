# THz-Driven Synthetic-Dimension Lattices in Thin-Film Lithium Niobate: Thermal-Photon Occupation Limits and the Operating-Point Criterion at 3.5 THz

## Abstract

Synthetic-dimension photonics uses the frequency modes of a single optical waveguide as the sites of an artificial lattice, promising high-dimensional photonic circuits without three-dimensional fabrication. Progress toward interaction-capable synthetic lattices in thin-film lithium niobate (TFLN) is blocked by a specific gap: the electro-optic drive that couples adjacent frequency sites must operate at a frequency whose band is not flooded with thermal photons, and no published criterion fixes the temperature at which this holds. We derive the effective tight-binding Hamiltonian of a 1550 nm traveler photon in a TFLN waveguide driven at 3.5 THz through the Pockels effect, obtaining a hopping rate $J = 36.06$ GHz for a drive field of $10^{7}$ V/m under stated device assumptions. We evaluate the Bose-Einstein thermal occupation at 3.5 THz: $n = 1.333$ at 300 K but $n = 0.1396$ at 80 K, a $9.55\times$ reduction, because $h\nu/k_B = 167.9$ K exceeds the 80 K thermal energy by a factor of 2.10. Propagating these occupancies through a per-hop scattering model with an assumed branching ratio of $10^{-3}$, transport fidelity over 100 lattice hops is 0.986 at 80 K versus 0.875 at 300 K. The results establish a concrete thermodynamic operating criterion — drive frequency above roughly $2.4\,k_B T/h$ — and identify the 3.5 THz source power, not the lattice physics, as the binding engineering constraint.

## 1. Introduction

Quantum photonic processors, microwave-to-optical transducers, and simulation engines for high-dimensional physics all need a substrate in which photons interact strongly and controllably while remaining low-loss. Synthetic-dimension photonics addresses this by treating the discrete frequency modes of an optical resonator or waveguide as the sites of a lattice, so that a "4D" or higher-dimensional lattice lives inside a one-dimensional optical path. The practitioners who face the cost of this problem today are designers of integrated quantum photonic circuits: without a synthetic lattice, realizing a genuinely high-dimensional connected graph on-chip requires stacking physical waveguides and couplers in three dimensions, which fabrication tolerance and routing congestion block at even modest graph sizes. If a single driven TFLN waveguide can host a well-resolved, low-noise synthetic lattice, the routing problem collapses into a frequency-domain design problem, and the capability that changes is the ability to build large connected photonic graphs — the raw material for boson sampling, topological pumping demonstrations, and frequency-multiplexed quantum channels — on one chip.

The obstacle is noise, and it is thermodynamic in origin. The same electro-optic (Pockels) modulation that couples adjacent frequency modes is driven by a strong radio-frequency or terahertz field. If the drive frequency sits in a spectral region where the thermal photon occupation is of order unity, the drive band is populated by incoherent thermal photons that are indistinguishable, from the traveler photon's point of view, from the coherent modulation field; they scatter the traveler, dephase the synthetic lattice, and set a temperature-dependent fidelity ceiling. No published analysis fixes the temperature at which a TFLN synthetic lattice driven at a given terahertz frequency becomes thermally clean. This paper supplies that analysis for the concrete case of a 3.5 THz drive on a 1550 nm traveler in thin-film lithium niobate, and shows that the criterion selects cryogenic operation near 80 K rather than room temperature.

TFLN is the natural host platform. Thin-film lithium tantalate modulators — the chemically closest sibling platform — reach a half-wave voltage-length product of 2.3 V·cm, optical loss of 3 dB/m, and electro-optic bandwidths beyond 100 GHz [1], and the LN-on-insulator platform supports low-loss waveguides, high-$Q$ resonators, and efficient second-order nonlinear conversion at wafer scale [2]. Cryogenic operation of TFLN photonics down to 5 K has been demonstrated, including electro-optic modulators and nonlinear frequency converters, with on-chip thermalization monitoring [4], so the cryogenic operating point this paper derives is reachable with existing packaging practice. Terahertz-range fields on TFLN have been demonstrated wirelessly: antenna-coupled electro-optic modulation with measured reflection coefficients of approximately 0.69 and 0.61 near 100 and 270 GHz, coupling efficiencies up to 8%, and source powers up to 100 mW in the WR9.0 band and 5 mW in the WR2.8 band [9]. The jump from 270 GHz to 3.5 THz is precisely where the feasibility question lives, both for source power and for thermal occupation.

This paper makes four contributions:

- It derives the effective tight-binding Hamiltonian mapping the THz-driven Pockels response of a TFLN waveguide onto a synthetic-dimension lattice, with the hopping rate expressed in device parameters and evaluated numerically (Sections 3 and 4.3).
- It computes the thermal photon occupation $n(3.5\ \text{THz}, T)$ at 300 K and 80 K with full arithmetic, obtaining $n = 1.333$ and $n = 0.1396$ respectively, and states the resulting thermodynamic operating criterion in closed form (Section 4.2).
- It propagates the two occupancies through an explicit per-hop scattering model to give transport fidelities of 0.986 (80 K) and 0.875 (300 K) over 100 lattice hops under a stated branching-ratio assumption, and it computes the coherent photon-flux parity threshold $P = n\,h\nu\,\Delta\nu$ for a 1 GHz bandwidth (Sections 4.5 and 4.6).
- It identifies, from these numbers, the feasibility thresholds in drive field, drive power, and temperature, and names the 3.5 THz source power as the first binding engineering constraint (Sections 5 and 7).

## 2. Background and Related Work

Synthetic dimensions in photonics couple discrete internal degrees of freedom — most commonly frequency modes — so that a single physical waveguide or resonator behaves as a multidimensional lattice. The electro-optic effect is the standard coupling mechanism because it shifts an optical mode's phase coherently at a radio-frequency rate, transferring population between neighboring frequency bins. The platform questions and the noise questions of this paper are each addressed by specific prior results, which we review here.

On the platform side, thin-film lithium niobate has become the leading electro-optic integrated photonics material. The review of integrated photonics on thin-film lithium niobate documents the maturation of wafer-scale manufacturing of lithium-niobate-on-insulator [2].  Thin-film lithium tantalate itself offers $r_{33} \sim 30$ pm/V, a bandgap of 3.93 eV, $5\times$ lower photorefraction than LN at visible wavelengths, and $10\times$ lower RF loss tangent than LN; its sub-volt near-IR modulator at 737 nm ($V_\pi L = 0.65$ V·cm, 30 dB extinction, 5.3 dB device loss) shows how far electrode and waveguide engineering can push the Pockels interaction, and its superior DC stability (<1 dB fluctuation versus the 5 dB TFLN figure over 46 hours) is directly relevant to holding a synthetic lattice's flux and detuning constants over a measurement [8]. Mid‑infrared LN‑on‑sapphire modulators demonstrate that Pockels engineering can extend across wavelength bands [5].

On the drive side, the highest-frequency electro-optic drive demonstrated on TFLN with published numbers is the wireless millimeter-wave modulator of [9], which couples free-space mmWave/THz radiation directly to the chip through an integrated antenna, eliminating impedance-matched transmission lines, and reports coupling efficiencies up to 8% with reflection coefficients of $\approx 0.69$ and $\approx 0.61$ near 100 and 270 GHz; its source chain delivers up to 100 mW in the WR9.0 band and up to 5 mW in the WR2.8 band. These numbers anchor our projection of the drive power available at 3.5 THz (Section 4.4), because the same work documents that all-electronic terahertz generation faces signal-integrity and bandwidth limits. Acoustic devices provide a complementary high‑frequency actuation route on the same material; TFLN acoustic filters and lattice XBAR filters demonstrate operation in the tens‑of‑GHz range [6,3], still two orders of magnitude below the 3.5 THz drive this paper requires, which is why we take the drive to be electromagnetic rather than acoustic.

On the cryogenics side, [4] demonstrates TFLN photonic integrated circuits operating from room temperature down to 5 K, including electro-optic modulators and sum-frequency-generation converters, and shows with an on-chip micro-resistor and racetrack resonator that chip thermalization can be monitored during cooldown — the resonance shift and resistor stabilize simultaneously while the mount sensor reads base temperature earlier. This establishes both that the 80 K operating point we derive is experimentally accessible and that verifying the actual chip temperature during high-power operation requires on-chip sensing, a point we return to in Section 7. Material loss sets the traveler photon's budget independently of temperature: measurements on TFLN waveguides show that the nonlinear index $n_2$ inferred from common techniques can differ from the true value by an order of magnitude because cascaded $\chi^{(2)}$ contributions nearly cancel the electronic $n_2$ [7], a caution we adopt by keeping our fidelity model's scattering parameters explicitly assumed rather than borrowed. Active components round out the platform: erbium-doped thin-film lithium niobate waveguide amplifiers provide on-chip gain [11], and electrically pumped soliton microcombs on TFLN show that lasers, resonators, and modulators co-integrate on the same die [10], so a future synthetic-lattice chip need not be a passive subsystem.

On the architecture side, a cryogenically stabilized synthetic lattice proposal outlines a multilayer stack and hybrid terahertz drive, and uses Floquet‑Bloch theory to derive an effective Hamiltonian [12]. That work states the target — a 4D synthetic lattice at 80 K under high-power optical drive — but does not publish the thermodynamic occupancy calculation that decides whether 80 K is the right temperature; our Section 4 supplies exactly that calculation for the 3.5 THz drive frequency. Our treatment locates the heating penalty not in the drive's absorbed power alone but in the thermal occupation of the drive band, which is a function of temperature and can be engineered downward by cooling — a distinction with direct design consequences, since it converts an intrinsic Floquet limitation into a cryogenics specification.

What no prior work in this set provides is the junction of the two threads: a numerical thermal-occupation criterion at the drive frequency that selects the operating temperature of an electro-optically synthesized lattice. Sections 3 and 4 close that gap.

## 3. Methods

### 3.1 Physical system and assumptions

We consider a single-mode TFLN waveguide carrying a 1550 nm traveler photon, with the waveguide's optical frequency modes separated by the drive frequency $\Omega/2\pi = 3.5$ THz serving as synthetic-lattice sites. The drive is a coherent 3.5 THz electric field applied across the optical mode via electrodes or an antenna-coupled structure, modulating the refractive index through the Pockels effect. We state the device assumptions used throughout, since no single prior work fixes all of them:

- Pockels coefficient $r_{33} = 30.8$ pm/V and ordinary index $n_0 = 2.2$ at 1550 nm, consistent with the LN electro-optic parameters quoted for the platform ($r_{33} \sim 30$ pm/V) [8].
- RF-to-optical field overlap factor $\Gamma = 0.5$, a mid-range value for electrode geometries of the type fabricated in [1] and [8].
- Traveler photon carrier frequency $\nu_0 = 193.5$ THz (1550 nm); synthetic lattice site spacing $\Omega/2\pi = 3.5$ THz, per the research conjecture under test.
- Drive field amplitude $E_{\text{THz}} = 10^{7}$ V/m (10 V/$\mu$m) as the reference operating point, justified in Section 4.4 against the demonstrated source powers of [9].
- Thermal scattering branching ratio $p_{\text{sc}} = 10^{-3}$ per lattice hop, an explicitly assumed parameter (Section 4.5); no measurement of thermal-photon-induced scattering in a driven synthetic lattice exists to our knowledge, so we carry it as a labeled assumption and test sensitivity in Section 6.

### 3.2 Effective Hamiltonian

The Pockels effect changes the refractive index by

$$\Delta n = -\frac{1}{2} n_0^{3} r_{33} \Gamma E_{\text{THz}} \cos(\Omega t),$$

which shifts the optical carrier frequency by

$$\delta\nu(t) = \nu_0 \frac{\Delta n(t)}{n_0} = -\frac{1}{2}\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}} \cos(\Omega t).$$

Writing the traveler field in the frequency-mode basis $\{|m\rangle\}$ with site $m$ at frequency $\nu_0 + m\Omega$, the phase modulation $e^{i\beta \sin \Omega t}$ with modulation index $\beta = \frac{1}{2}\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}} / (\Omega/2\pi)$ generates the standard frequency-lattice Hamiltonian in the rotating-wave limit $J \ll \Omega$:

$$H_{\text{synth}} = \sum_{m} m \hbar \Omega\, |m\rangle\langle m| + \hbar J \sum_{m} \left( |m+1\rangle\langle m| + \text{h.c.} \right),$$

with nearest-neighbor hopping

$$J = \frac{\delta\nu_{\text{pk}}}{2} = \frac{\nu_0 n_0^{2} r_{33} \Gamma E_{\text{THz}}}{4},$$

where $\delta\nu_{\text{pk}}$ is the peak frequency shift. This is the Floquet-Bloch mapping of temporal modulation onto a tight-binding chain, in the form used for synthetic-dimension lattices; the same mapping underlies the 4D Hamiltonian construction of [12], which applies Floquet-Bloch theory to temporal modulation of a lattice but does not evaluate the hopping rate for TFLN device parameters, which we do in Section 4.3.

### 3.3 Thermal occupation criterion

The drive band at frequency $\nu = 3.5$ THz contains thermal photons with Bose-Einstein occupation

$$n(\nu, T) = \frac{1}{e^{h\nu / k_B T} - 1}.$$

The thermodynamic operating criterion is that the coherent drive field dominate the incoherent thermal population of its own band. We operationalize this as $h\nu \gtrsim 2.4\, k_B T$, i.e. $n(\nu,T) \lesssim 0.1$, so that fewer than one thermal photon in ten occupies each drive-band mode. Solving for temperature:

$$T_{\text{op}} \le \frac{h\nu}{2.4\, k_B}.$$

This criterion is the quantitative content of the conjecture under test — that the drive must exceed the thermal photon occupation at 3.5 THz, forcing cryogenic operation — and Section 4.2 evaluates it numerically.

### 3.4 Transport fidelity model

A traveler photon traversing $N$ lattice hops accumulates scattering errors from thermal photons in the drive band. With per-hop thermal scattering probability $\epsilon = p_{\text{sc}}\, n(\nu, T)$, where $p_{\text{sc}}$ is the branching ratio for a drive-band thermal photon to scatter the traveler out of its synthetic-lattice path, the transport fidelity is

$$F(N, T) = \left(1 - \epsilon\right)^{N} \approx e^{-N p_{\text{sc}} n(\nu,T)}.$$

The model deliberately excludes drive-induced heating of the chip (treated separately in Section 4.7) and any temperature dependence of $r_{33}$ or optical loss; the cryogenic study of [4] found electro-optic operation feasible down to 5 K, supporting the assumption that the Pockels coefficient remains functional across the range considered.

## 4. Analysis

### 4.1 Drive-band energy scale

Input: $\nu = 3.5 \times 10^{12}$ Hz (research conjecture), $h = 6.626 \times 10^{-34}$ J·s, $k_B = 1.381 \times 10^{-23}$ J/K.

$$h\nu = (6.626 \times 10^{-34})(3.5 \times 10^{12}) = 2.3191 \times 10^{-21}\ \text{J}.$$

Converting to electronvolts: $2.3191 \times 10^{-21}\ \text{J} / (1.602 \times 10^{-19}\ \text{J/eV}) = 0.01448$ eV $= 14.48$ meV.

The characteristic temperature of the drive band is

$$\frac{h\nu}{k_B} = \frac{2.3191 \times 10^{-21}}{1.381 \times 10^{-23}} = 167.9\ \text{K}.$$

So a 3.5 THz photon carries an energy equal to $k_B$ at 167.9 K. At room temperature (300 K) the drive band sits below the thermal energy scale; at 80 K it sits above it by a factor $167.9/80 = 2.10$.

### 4.2 Thermal occupation at 300 K and 80 K

At $T = 300$ K:

$$\frac{h\nu}{k_B T} = \frac{167.9}{300} = 0.5597,$$
$$e^{0.5597} = 1.7504,$$
$$n(3.5\ \text{THz}, 300\ \text{K}) = \frac{1}{1.7504 - 1} = \frac{1}{0.7504} = 1.333.$$

At $T = 80$ K:

$$\frac{h\nu}{k_B T} = \frac{167.9}{80} = 2.099,$$
$$e^{2.099} = 8.161,$$
$$n(3.5\ \text{THz}, 80\ \text{K}) = \frac{1}{8.161 - 1} = \frac{1}{7.161} = 0.1396.$$

The ratio is

$$\frac{n(300\ \text{K})}{n(80\ \text{K})} = \frac{1.333}{0.1396} = 9.55.$$

Cooling from 300 K to 80 K therefore reduces the thermal photon population of the drive band by a factor of 9.55, and — more importantly qualitatively — moves the band from the classical regime ($n > 1$, thermal photons more populous than the quantum ground state) to the quantum regime ($n < 1$).

The operating-temperature criterion of Section 3.3 gives

$$T_{\text{op}} \le \frac{167.9}{2.4} = 69.9\ \text{K}.$$

Two consequences follow. First, the conjectured 80 K operating point sits marginally above the strict $n \le 0.1$ criterion: at 80 K the occupation is 0.1396, about 40% above the 0.1 target, so 80 K delivers a $9.55\times$ noise reduction but not full entry into the $n < 0.1$ regime; operation at or below 69.9 K is required for that. Second, the criterion is linear in $\nu$: a drive at 7 THz would satisfy it at $T \le 139.8$ K, so raising the drive frequency relaxes the cryogenic requirement proportionally. We carry both observations into Sections 5 and 6.

### 4.3 Hopping rate for TFLN device parameters

The hopping rate of Section 3.2 is

$$J = \frac{\nu_0\, n_0^{2}\, r_{33}\, \Gamma\, E_{\text{THz}}}{4}.$$

Inputs (Section 3.1): $\nu_0 = 193.5 \times 10^{12}$ Hz, $n_0 = 2.2$, $r_{33} = 30.8 \times 10^{-12}$ m/V, $\Gamma = 0.5$, $E_{\text{THz}} = 10^{7}$ V/m.

Step 1 — index factor:
$$n_0^{2} = (2.2)^{2} = 4.84.$$

Step 2 — product of optical frequency and index factor:
$$\nu_0\, n_0^{2} = (193.5 \times 10^{12})(4.84) = 9.3654 \times 10^{14}\ \text{Hz}.$$

Step 3 — Pockels response per unit field:
$$9.3654 \times 10^{14} \times 30.8 \times 10^{-12} = 2.8845 \times 10^{4}\ \text{Hz}\cdot\text{m/V}.$$

Step 4 — overlap factor:
$$2.8845 \times 10^{4} \times 0.5 = 1.4423 \times 10^{4}\ \text{Hz}\cdot\text{m/V}.$$

Step 5 — apply the drive field and the factor $1/4$:
$$J = \frac{(1.4423 \times 10^{4})(10^{7})}{4} = \frac{1.4423 \times 10^{11}}{4} = 3.606 \times 10^{10}\ \text{Hz} = 36.06\ \text{GHz}.$$

The rotating-wave condition $J \ll \Omega$ holds with $J/\Omega = 36.06/3500 = 0.0103$, so the tight-binding mapping is self-consistent at the reference operating point. The hopping rate scales linearly in $E_{\text{THz}}$, $\Gamma$, and $r_{33}$: at half the drive field, $J = 18.03$ GHz and $J/\Omega = 0.00515$.

### 4.4 Drive power required at the reference operating point

The hopping rate of Section 4.3 requires a peak electric field of $10^{7}$ V/m across the optical mode. We convert this field to a required on-chip terahertz power under explicitly stated assumptions, because no published experiment delivers a calibrated 3.5 THz field on a TFLN chip.

Assumptions: (i) the terahertz field is applied across an electrode gap $g = 1\ \mu\text{m}$, comparable to the sub-micron TFLN film thicknesses used in the platform's demonstrated devices [1]; (ii) the driven structure presents an effective impedance $Z_{\text{eff}} = 50\ \Omega$ at 3.5 THz, the standard matched value for the coplanar electrode geometries fabricated in [1]; (iii) the antenna-coupling efficiency at 3.5 THz equals the best demonstrated value of 8% from the wireless millimeter-wave modulator work [9], which measured that efficiency at 100–270 GHz.

Step 1 — required voltage:
$$V_{\text{pk}} = E_{\text{THz}}\, g = (10^{7})(10^{-6}) = 10\ \text{V}.$$

Step 2 — required on-chip power into the matched termination (peak voltage $V_{\text{pk}}$ of a sinusoid delivers average power $V_{\text{pk}}^{2}/(2 Z_{\text{eff}})$):
$$P_{\text{chip}} = \frac{V_{\text{pk}}^{2}}{2 Z_{\text{eff}}} = \frac{10^{2}}{2 \times 50} = \frac{100}{100} = 1.0\ \text{W}.$$

Step 3 — required source power at 8% coupling efficiency:
$$P_{\text{src}} = \frac{P_{\text{chip}}}{0.08} = \frac{1.0}{0.08} = 12.5\ \text{W}.$$

For comparison, the source chain demonstrated in [9] emits up to 100 mW in the WR9.0 band and up to 5 mW in the WR2.8 band (near 270 GHz). The shortfall at the reference operating point is

$$\frac{P_{\text{src}}}{P_{\text{WR2.8}}} = \frac{12.5}{0.005} = 2500.$$

Even at the reduced drive field $E_{\text{THz}} = 10^{6}$ V/m (giving $J = 3.606$ GHz, still $\gg$ the $\sim$MHz–GHz linewidths of interest), the requirement scales down by $100\times$ to $P_{\text{src}} = 125$ mW, which exceeds the assumed 5 mW band power at 270 GHz by a factor of 25 and is itself unproven at 3.5 THz. This is the quantitative basis for identifying source power, not lattice physics, as the binding constraint.

### 4.5 Transport fidelity at 300 K and 80 K

With $\epsilon = p_{\text{sc}}\, n(\nu, T)$, $p_{\text{sc}} = 10^{-3}$ (assumed, Section 3.1) and $N = 100$ hops:

At 300 K: $\epsilon_{300} = 10^{-3} \times 1.333 = 1.333 \times 10^{-3}$,
$$F(100, 300\ \text{K}) = e^{-100 \times 1.333 \times 10^{-3}} = e^{-0.1333} = 0.8752.$$

At 80 K: $\epsilon_{80} = 10^{-3} \times 0.1396 = 1.396 \times 10^{-4}$,
$$F(100, 80\ \text{K}) = e^{-100 \times 1.396 \times 10^{-4}} = e^{-0.01396} = 0.9861.$$

The fidelity gain from cooling is $0.9861/0.8752 = 1.127$ in fidelity, but the error probability falls by the full factor of 9.55: the per-100-hop error is $1 - 0.8752 = 0.1248$ at 300 K versus $1 - 0.9861 = 0.0139$ at 80 K, a reduction of $0.1248/0.0139 = 8.98\times$ (slightly below 9.55 because the exponential compresses small errors).

Sensitivity to the assumed branching ratio: if $p_{\text{sc}} = 10^{-2}$ instead, then at 80 K
$$F = e^{-100 \times 10^{-2} \times 0.1396} = e^{-0.1396} = 0.8697,$$
and at 300 K $F = e^{-1.333} = 0.2637$. The 80 K advantage survives in direction but the absolute fidelity collapses, so the model's usefulness hinges on $p_{\text{sc}} \lesssim 10^{-3}$, which no measurement constrains (Section 6).

### 4.6 Coherent photon-flux parity threshold

A second, drive-side noise channel is thermal photons entering the drive band through the source's own noise floor. A coherent drive at bandwidth $\Delta\nu$ delivering mean photon flux $\Phi$ into the band has, per bandwidth mode, a coherent occupation $n_{\text{coh}} = \Phi / \Delta\nu$. Requiring $n_{\text{coh}} \ge n(\nu, T)$ gives the parity power

$$P_{\text{par}} = n(\nu, T)\, h\nu\, \Delta\nu.$$

With $\Delta\nu = 1\ \text{GHz}$ and $h\nu = 2.3191 \times 10^{-21}$ J (Section 4.1):

At 80 K:
$$P_{\text{par}} = 0.1396 \times 2.3191 \times 10^{-21} \times 10^{9} = 3.238 \times 10^{-13}\ \text{W} = 0.324\ \text{pW}.$$

At 300 K:
$$P_{\text{par}} = 1.333 \times 2.3191 \times 10^{-21} \times 10^{9} = 3.091 \times 10^{-12}\ \text{W} = 3.09\ \text{pW}.$$

These thresholds are many orders of magnitude below the milliwatt source powers of [9], so a coherent source overwhelms thermal-band occupation trivially; the parity criterion is therefore not the binding constraint, and the binding constraints are, in order, source power (Section 4.4) and the unmeasured branching ratio $p_{\text{sc}}$ (Section 4.5).

### 4.7 Drive-induced chip heating

The model of Section 3.4 excludes heating of the chip by the absorbed drive. The cryogenic study of [4] shows that during high-power operation the chip temperature must be verified on-chip: its racetrack-resonance shift and micro-resistor readings stabilize simultaneously while the sample-mount sensor reaches base temperature earlier, so the mount sensor overreports thermalization during transients. If a fraction $\eta_{\text{abs}}$ of the $P_{\text{chip}} = 1.0$ W on-chip drive power (Section 4.4) is absorbed as heat, the cooling load is $\eta_{\text{abs}} \times 1.0$ W; at $\eta_{\text{abs}} = 0.01$ this is 10 mW, which is within the lift of small Stirling-stage coolers but must be budgeted against the 80 K specification. We do not have a measured $\eta_{\text{abs}}$ for a 3.5 THz drive on TFLN and carry it as an open parameter.

## 5. Results

All numbers below are computed in Section 4 under the assumptions stated there; none is a measurement.

| Quantity | 300 K | 80 K | Source |
|---|---|---|---|
| $h\nu/k_B$ at 3.5 THz | 167.9 K | 167.9 K | § 4.1 |
| Thermal occupation $n(3.5\ \text{THz}, T)$ | 1.333 | 0.1396 | § 4.2 |
| Occupation ratio | $9.55\times$ reduction on cooling | $9.55\times$ reduction on cooling | § 4.2 |
| Operating temperature for $n \le 0.1$ | \multicolumn{2}{c|}{$T_{\text{op}} \le 69.9$ K} | § 4.2 |
| Hopping rate $J$ at $E_{\text{THz}} = 10^{7}$ V/m | \multicolumn{2}{c|}{36.06 GHz ($J/\Omega = 0.0103$)} | § 4.3 |
| Transport fidelity $F(100)$, $p_{\text{sc}} = 10^{-3}$ | 0.8752 | 0.9861 | § 4.5 |
| Per-100-hop error probability | 0.1248 | 0.0139 | § 4.5 |
| Parity power $P_{\text{par}}$, $\Delta\nu = 1$ GHz | 3.09 pW | 0.324 pW | § 4.6 |
| Required on-chip drive power | \multicolumn{2}{c|}{1.0 W (projection)} | § 4.4 |
| Required source power at 8% coupling | \multicolumn{2}{c|}{12.5 W (projection)} | § 4.4 |

Three results carry the paper's claim. First, the thermodynamic criterion is met with margin only below 69.9 K; the conjectured 80 K point reduces the drive-band thermal occupation by $9.55\times$ but leaves $n = 0.1396$, above the $n \le 0.1$ target. Second, at the reference drive field the synthetic lattice is deep in the tight-binding regime ($J/\Omega = 0.0103$) with a hopping rate of 36.06 GHz, fast enough that 100 hops traverse in a time of order $100/J = 2.77$ ns. Third, the fidelity model projects $F = 0.986$ at 80 K versus $F = 0.875$ at 300 K over 100 hops, but this projection rests on an assumed branching ratio $p_{\text{sc}} = 10^{-3}$ with no experimental anchor; a tenfold larger $p_{\text{sc}}$ degrades the 80 K fidelity to 0.870. The engineering conclusion is that the 3.5 THz source power — a projected 12.5 W at the reference field against 5 mW demonstrated at 270 GHz [9] — binds before any lattice physics does.

## 6. Discussion

The central result — that a 3.5 THz-driven TFLN synthetic lattice must operate below roughly 69.9 K to hold drive-band thermal occupation under 0.1, and that source power rather than lattice physics is the first binding constraint — is a calculation, not a demonstration, and its weaknesses should be stated plainly.

**What would falsify the main result.** The operating-point criterion rests on the Bose-Einstein occupation of the drive band and would be falsified by any of three observations: (i) a measurement of traveler-photon scattering in a driven synthetic lattice showing that thermal drive-band photons do not couple to the traveler with the assumed branching-ratio structure, i.e. that the effective $p_{\text{sc}}\, n(\nu,T)$ scaling fails — for example, if scattering saturates at low temperature because a non-thermal noise channel (laser RIN, electrode Johnson noise, pump leakage) dominates; (ii) a demonstration of high-fidelity synthetic-lattice transport at 300 K with a 3.5 THz-band drive, which would show the occupation criterion is not the operative noise limit; or (iii) a first-principles calculation showing the relevant noise mode is not at $\nu = 3.5$ THz but at a difference or sum frequency where the occupation differs. Any of these would remove the basis for the 69.9 K figure.

**Limitations list.** Each assumption below names its sensitivity.

- *Branching ratio $p_{\text{sc}} = 10^{-3}$ per hop* (Section 3.1): unmeasured. The 80 K fidelity result is linear in it: $F = e^{-N p_{\text{sc}} n}$. At $p_{\text{sc}} = 10^{-2}$, $F(100, 80\ \text{K})$ falls from 0.986 to 0.870; at $p_{\text{sc}} = 10^{-4}$ it rises to 0.9986. The qualitative 80 K advantage survives any $p_{\text{sc}}$, but the absolute fidelity — the number a designer would use — is uncertain by an order of magnitude in either direction.
- *Drive field $10^{7}$ V/m and gap $g = 1\ \mu$m, impedance 50 $\Omega$* (Sections 3.1, 4.4): the required source power scales as $E_{\text{THz}}^{2} g^{2} / (2 Z_{\text{eff}} \eta_{\text{coup}})$. A 5 $\mu$m gap raises the required on-chip power $25\times$ to 12.5 W; a 10 $\Omega$ antenna impedance lowers it $5\times$ to 0.1 W. The conclusion that source power binds is robust to these factors of a few to tens, because the demonstrated source power at 270 GHz is 5 mW [9] and the gap to 3.5 THz sources is at least a factor of 25 even at $10^{6}$ V/m.
- *Coupling efficiency 8% at 3.5 THz* (Section 4.4): measured at 100–270 GHz in [9]; the reflection coefficient there worsens from $\approx 0.69$ to $\approx 0.61$ between 100 and 270 GHz, and no measurement exists at 3.5 THz. If coupling falls to 1%, the required source power rises $8\times$ to 50 W.
- *Temperature-independent $r_{33}$ and optical loss* (Section 3.4): supported qualitatively by the demonstration of electro-optic operation from room temperature to 5 K [4], but no published measurement quantifies $r_{33}(T)$ in thin-film LN below 100 K; a strong temperature dependence would shift the fidelity numbers without changing the occupation criterion.
- *Excluded heating channel* (Section 4.7): the absorbed drive fraction $\eta_{\text{abs}}$ is unknown; if chip heating pushes the local waveguide temperature above the cryostat setpoint, the effective occupation is $n(3.5\ \text{THz}, T_{\text{chip}})$ with $T_{\text{chip}} > T_{\text{set}}$, eroding the cooling benefit. On-chip thermalization sensing of the kind demonstrated in [4] is required to close this loop.
- *Single-mode, ideal-lattice assumption* (Section 3.1): the model ignores disorder in $J$ along the chain, mode walk-off, and the slow charge-dynamics drift documented in TFLN modulators (5 dB quadrature fluctuation over 46 hours [1]); any of these adds a decoherence channel independent of temperature, which would flatten the 300 K versus 80 K fidelity contrast.
- *Material-parameter caution*: nonlinear-index measurements on TFLN can differ from true values by an order of magnitude because cascaded $\chi^{(2)}$ contributions nearly cancel the electronic response [7]; by analogy, any parameter borrowed from bulk LN rather than measured in the thin-film geometry carries that level of uncertainty. We have kept $r_{33}$ and $\Gamma$ as stated assumptions for this reason.

**Open questions.** What is the actual absorption of a 3.5 THz field in gold electrodes on TFLN at 80 K? Does the Pockels coefficient of x-cut thin-film LN change measurably between 300 K and 80 K? Can antenna-coupled wireless delivery [9] be extended from 270 GHz to 3.5 THz with any useful efficiency, or must the drive be generated on-chip? Is there a lower-drive-frequency operating point (e.g. 0.35 THz, where $h\nu/k_B = 16.8$ K and $n \gg 1$ at any reachable temperature) whose thermal noise is tolerable because $p_{\text{sc}}$ itself falls with frequency? The last question is the most dangerous to the paper's premise: if thermal scattering at sub-THz drive frequencies is negligible in practice, cryogenic operation is unnecessary and the criterion, while correct, is not binding.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The direct users are designers of integrated quantum photonic circuits and of electro-optic synthetic-dimension devices, who currently lack a rule for choosing the operating temperature of a frequency-lattice experiment. If the criterion holds, the design decision that changes is the thermal specification of the experiment package: a 3.5 THz-driven TFLN lattice is specified for $T \le 69.9$ K rather than room temperature, and the cryostat requirement becomes a first-order line item in the architecture rather than an afterthought. The result also reorders engineering priorities: it says the limiting development task is a 3.5 THz source delivering of order 0.1–1 W on chip, not the lattice itself, whose hopping physics at 36 GHz is straightforward Pockels engineering of the kind already demonstrated at lower frequencies [1], [8].

**(b) Readiness.** This work is purely analytical and not peer reviewed: by the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). No TFLN synthetic lattice driven at 3.5 THz has been built; the highest published electro-optic drive on the platform with characterized coupling is near 270 GHz [9], and the platform's demonstrated acoustic actuation reaches 38.7 GHz [6] and above 18 GHz in lattice XBAR filters [3] — both far below the required drive. Nothing in this paper constitutes component or manufacturing readiness, and no claim above TRL 3 is made or supportable without a laboratory demonstration.

**(c) Smallest next experiment.** The cheapest test that de-risks or falsifies the fidelity model is not a 3.5 THz lattice but a scattering-calibration measurement: drive an existing TFLN Mach-Zehnder or ring modulator at a frequency in the 100–270 GHz band already accessible with the wireless-coupling apparatus of [9], hold the chip at 300 K and at 80 K using the cryogenic probe-station practice of [4], and measure the temperature dependence of the traveler photon's noise-equivalent scattering (e.g. via the modulation sideband noise floor or resonator linewidth). The model predicts a sideband-noise or scattering reduction tracking the Bose-Einstein factor between the two temperatures at the drive frequency used; a measured temperature dependence flat, or inconsistent with the $n(\nu, T)$ scaling, refutes the per-hop scattering model and with it the fidelity projections. A second, complementary test is a low-frequency synthetic lattice (drive $\le 100$ GHz, where sources are mature) operated at 80 K versus 300 K to bound $p_{\text{sc}}$ directly.

**(d) Binding constraints in order.** First, the 3.5 THz source: all-electronic terahertz generation faces documented signal-integrity and bandwidth limits [9], and the projected 12.5 W source requirement (Section 4.4) exceeds demonstrated band powers by three orders of magnitude. Second, coupling: the 8% antenna efficiency is unproven above 270 GHz, and the worsening reflection coefficient from 100 to 270 GHz suggests degradation, not improvement, at 3.5 THz. Third, thermal budget: absorbed drive power at the 1.0 W on-chip level must be lifted by the cryo-cooler while holding $T_{\text{chip}} \le 69.9$ K, requiring on-chip thermalization sensing as demonstrated in [4]. Fourth, materials and fabrication: electrode gap and overlap factor $\Gamma$ set the field per watt; sub-micron gaps at 3.5 THz push against the fabrication tolerances of the platform's demonstrated processes [1], [8]. Fifth, data: no measurement of $p_{\text{sc}}$, $r_{33}(T)$, or $\eta_{\text{abs}}$ exists; each is an open question rather than a bounded constraint.

**(e) Order-of-magnitude projections.** Labeled as projections with the assumptions of Section 4.4 (gap 1 $\mu$m, $Z_{\text{eff}} = 50\ \Omega$, coupling 8%): on-chip drive power 1.0 W at $E_{\text{THz}} = 10^{7}$ V/m; source power 12.5 W; at a reduced field of $10^{6}$ V/m ($J = 3.6$ GHz), on-chip 10 mW and source 125 mW. Cooling load projection with assumed $\eta_{\text{abs}} = 0.01$: 5 mW at the reference field, 50 $\mu$W at the reduced field. These bounds span the plausible design space; they are not measurements and inherit the factor-of-several uncertainty in $g$, $Z_{\text{eff}}$, and $\eta_{\text{coup}}$ stated in Section 6.

**(f) Risks and misuse paths.** No dual-use risk is apparent: the result is a temperature specification for a photonic research device. The main misuse is rhetorical rather than physical — citing the 80 K figure as an established feasibility result when it is a projection resting on an unmeasured branching ratio and an undemonstrated source; this paper labels those dependencies explicitly to prevent that.

## 8. Conclusion

For a 1550 nm traveler photon in a thin-film lithium niobate waveguide driven at 3.5 THz through the Pockels effect, the effective synthetic-dimension lattice has a hopping rate of 36.06 GHz at a drive field of $10^{7}$ V/m under stated device assumptions, deep in the tight-binding regime. The drive band's thermal photon occupation is 1.333 at 300 K and 0.1396 at 80 K — a $9.55\times$ reduction that moves the band from the classical to the quantum regime — and the strict criterion $n \le 0.1$ requires $T \le 69.9$ K, so the conjectured 80 K operating point is close but not sufficient. Propagating these occupancies through an explicit per-hop scattering model with an assumed branching ratio of $10^{-3}$ gives transport fidelities of 0.986 at 80 K and 0.875 at 300 K over 100 hops. The decisive engineering constraint is not the lattice physics but the 3.5 THz source: the reference operating point projects a 12.5 W source requirement against 5 mW demonstrated at 270 GHz. The paper's deliverable is a concrete, falsifiable thermodynamic operating criterion — drive frequency above roughly $2.4\,k_B T/h$ — plus a ranked list of what must be measured next: the thermal scattering branching ratio, the temperature dependence of the Pockels response below 100 K, and the absorption of a terahertz drive on a cryogenic TFLN chip.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.19.2-retry-not-error). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Stable electro-optic modulators using thin-film lithium tantalate. arXiv:2405.05169. https://arxiv.org/abs/2405.05169
[2] Integrated photonics on thin-film lithium niobate. arXiv:2102.11956. https://arxiv.org/abs/2102.11956
[3] Lattice XBAR Filters in Thin-Film Lithium Niobate. arXiv:2602.14937. https://arxiv.org/abs/2602.14937
[4] Cryogenic nonlinear processes in thin-film lithium niobate. arXiv:2607.29176. https://arxiv.org/abs/2607.29176
[5] Integrated thin film lithium niobate mid-infrared modulator. arXiv:2505.23632. https://arxiv.org/abs/2505.23632
[6] 38.7 GHz Thin Film Lithium Niobate Acoustic Filter. arXiv:2311.05712. https://arxiv.org/abs/2311.05712
[7] Reduced Material Loss in Thin-film Lithium Niobate Waveguides. arXiv:2203.17133. https://arxiv.org/abs/2203.17133
[8] A sub-volt near-IR lithium tantalate electro-optic modulator. arXiv:2505.00906. https://arxiv.org/abs/2505.00906
[9] Wireless millimeterwave electro-optics on thin film lithium niobate. arXiv:2505.04585. https://arxiv.org/abs/2505.04585
[10] Electrically-pumped soliton microcombs on thin-film lithium niobate. arXiv:2510.00371. https://arxiv.org/abs/2510.00371
[11] Efficient erbium-doped thin-film lithium niobate waveguide amplifiers. arXiv:2101.06994. https://arxiv.org/abs/2101.06994
[12] QNFO: CRYOGENICALLY STABILIZED SYNTHETIC LATTICE