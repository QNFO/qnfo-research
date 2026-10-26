# Permittivity-Gradient "Vacuum Dielectric" Thrust: A Momentum-Balance and Energy-Cost Analysis of a Propellant-less Propulsion Conjecture

## Abstract

Propellant-less propulsion from engineered electromagnetic media is a recurring conjecture: if the vacuum's effective permittivity could be modulated in space, the coordinate speed of light $n(x)=\sqrt{-g_{11}/g_{00}}$ would acquire a gradient, and a finite "dielectric-analogy" region might experience net thrust. No published analysis quantifies the thrust such a configuration could deliver or the energy it would cost. This paper tests the conjecture with three calculations. First, Einstein's equations are inverted for a meter-scale metric patch with an order-unity index change, giving a required energy density $u \approx 4.8\times 10^{42}\ \mathrm{J\,m^{-3}}$, some $51$ orders of magnitude above the observed dark-energy density. Second, the center-of-mass theorem is applied to a closed system containing a static permittivity profile: internal gradients exert zero net force, so any thrust must be reaction to expelled momentum, reducing the device to a photon or particle rocket. Third, the thrust ceiling for a dielectric-analogy region is bounded by $F \le (P/c)\,(n-1)$; at $P = 1\ \mathrm{kW}$ and $n = 3$ this gives $F \le 6.7\times 10^{-6}\ \mathrm{N}$, and the energy cost per newton-second is $c \approx 3.0\times 10^{8}\ \mathrm{J}$. The analysis implies that permittivity-gradient schemes cannot beat photon-rocket performance, and that reported anomalous capacitor forces must be sought in expelled-charge momentum rather than vacuum modification.

## 1. Introduction

Satellite operators and deep-space mission designers face a structural constraint: every newton-second of impulse a spacecraft delivers must either be paid for in expelled propellant mass or in very large electrical power. Chemical propulsion is mass-limited; electric propulsion is still propellant-limited; and the only fully propellant-less option, a photon rocket, converts power to thrust at the fixed rate $F = P/c$, so that one newton of continuous thrust requires $3.0\times 10^{8}\ \mathrm{W}$. A propulsion concept that extracted thrust from a *static* modification of the vacuum — a region where the effective refractive index $n(x)$ is engineered, with no expelled reaction mass and no directed radiation — would change mission design fundamentally: station-keeping, drag makeup and interstellar precursor missions would no longer trade payload mass against propellant or against gigawatts of power.

The conjecture examined here, due to the research idea that motivated this paper, is that artificially modulating the vacuum's effective permittivity and permeability creates a local gradient in the coordinate speed of light, expressed in a static spacetime metric as

$$
n(x) = \sqrt{\frac{-g_{11}(x)}{g_{00}(x)}}\,,
$$

and that configurations with $\sqrt{g_{00}} > 1$ and $|g_{11}| < 1$ simultaneously would yield time speedup, spatial expansion, superluminal effective velocity, and a reduced effective inertial mass $m\,(-g_{11})/\sqrt{g_{00}}$. If a finite region with such a gradient experienced a net force, the result would be a propellant-less thruster. If it did not — if momentum balance forbids net thrust from any static index profile — then the design space for propellant-less propulsion collapses to radiation-reaction schemes, and experimental anomalies in this area must be reinterpreted.

This paper answers the "so what" question by derivation rather than by advocacy. It (i) inverts Einstein's equations to find the stress-energy a metric patch of the conjectured type would require, and checks the result against known energy densities; (ii) proves, from the center-of-mass theorem, that no static permittivity gradient inside a closed system can produce net thrust, and identifies the only channels through which thrust can appear; (iii) bounds the thrust of any dielectric-analogy device by the photon-rocket limit and computes the energy cost per unit impulse; and (iv) places reported anomalous forces in symmetric capacitors [1] within this momentum-accounting framework.

The contributions are:

- A closed-form derivation of the energy density $u = c^{4}/(8\pi G L^{2})$ required to sustain an order-unity index gradient over a length $L$, evaluated at $L = 1\ \mathrm{m}$ to give $u \approx 4.8\times 10^{42}\ \mathrm{J\,m^{-3}}$ (Section 4.1).
- A proof from momentum conservation that a closed system with a static, time-independent $n(x)$ profile experiences zero net force, so that the conjectured thrust violates the center-of-mass theorem unless momentum is expelled (Section 4.2).
- A thrust ceiling $F \le (P/c)(n-1)$ for any dielectric-analogy region, with worked numbers at $P = 1\ \mathrm{kW}$, $n = 3$, and an energy cost of $c \approx 3.0\times 10^{8}\ \mathrm{J}$ per newton-second of impulse (Section 4.3).
- A momentum-accounting reinterpretation of the reported bidirectional thrust in discharging symmetric capacitors [1] as expelled-electron recoil, with the observable signature that distinguishes it from vacuum modification (Section 4.4).

## 2. Background and Related Work

The conjecture sits at the intersection of gravitational optics, electromagnetic momentum theory, and engineered dielectrics. The works below supply the specific results this paper builds on.

The experimental anchor is the report of bidirectional propellant-less thrust in symmetric capacitors [1]. During internal discharge by field emission, thin parallel-plate capacitors supplied with $5$–$10\ \mathrm{kV}$ DC were observed to accelerate slightly toward the anode; the effect appeared only with dielectrics of low breakdown strength and diminished as breakdown voltage and thickness increased [1]. The reported systematics are specific: a linear correlation between thrust force and accelerated mass, an exponential increase of force as electrode separation decreased at constant mass, reversibility when conductive material insulated from the cathode was placed behind the cathode, and confirmation in soft vacuum with lower data scatter [1]. The authors report electron accelerations of order $10^{19}\ \mathrm{m\,s^{-2}}$ during field emission [1]. This paper uses [1] as the empirical benchmark that any vacuum-modulation theory of propellant-less thrust must confront, and shows in Section 4.4 that its systematics are those of expelled-electron recoil.

On the gravitational side, the conjecture's identification $n = \sqrt{-g_{11}/g_{00}}$ is the standard optical-metric relation for static spacetimes, but the source side of Einstein's equations has not previously been evaluated for the proposed patch. The hydrodynamic-spacetime program [12] supplies the relevant density scales: it frames the vacuum as a physical medium and quotes the $120$-order-of-magnitude gap between the theoretical Planck density $\rho_{pl} \approx 10^{113}\ \mathrm{J\,m^{-3}}$ and the observed dark-energy density $\rho_{\Lambda} \approx 10^{-9}\ \mathrm{J\,m^{-3}}$ [12]. That gap is exactly the scale problem Section 4.1 quantifies for a meter-scale engineered metric patch. The same program proposes falsification protocols — energy-dependent photon arrival times from gamma-ray bursts and viscous damping of gravitational waves [12] — which illustrate the standard this paper's conjecture must also meet: a distinct, measurable prediction.

On electromagnetic momentum, the Abraham–Minkowski question is the crux of any dielectric-analogy thrust claim. The master-equation analysis of an atom near a vacuum–dielectric interface [5] derives the semiclassical radiation-pressure force and the momentum-diffusion tensor from the vacuum field correlation function, and its central result is that internal and center-of-mass dynamics are determined by the two-point correlation tensor of the vacuum field around the atom's position [5]. This matters here because it shows that radiation pressure in inhomogeneous dielectric environments is fully determined by field correlations and recoil — there is no residual "index-gradient force" on matter beyond what photon momentum exchange supplies. Section 4.2 extends the same bookkeeping from a single atom to a finite dielectric region.

On engineered index profiles, three works define what is achievable. The Green's-function method for optical-waveguide gratings [4] solves wave propagation through arbitrary dielectric modulations exactly for transverse electric modes, incorporating self-coupling analytically and scaling as $\mathcal{O}(N)$ in iterative solution [4]; it is the computational tool a numerical test of the conjecture's wave-propagation claims would use, and it confirms that index modulation redirects and delays waves but injects no net momentum. The dipole-in-photonic-crystal calculation [9] computes emission spectra in a semi-infinite medium with sinusoidal dielectric modulation $\varepsilon(x) = \varepsilon_{1} + \delta\varepsilon\cos(\sigma x + \phi)$ and finds emission strongly suppressed in the gap for emitters more than about five periods from the interface, with band-edge enhancement far smaller than earlier predictions because the modulation is weak — the cited three-dimensional calculations needed a dielectric contrast $\Delta\varepsilon > 10$ to open a complete gap and achieved a radiated-power enhancement of only $\sim 25$ [9]. The opal systems it discusses have refractive-index contrast $\Delta n \approx 0.1$–$0.3$ [9]. These numbers calibrate the realistic range of static index engineering: order-unity changes in $n$ are routine in matter, but the conjecture requires them in the *vacuum* between field sources, which is a different and far harder target.

The active-control literature shows that even dynamic index control is material-bound. Graphene plasmon experiments demonstrate full electrical control of plasmon reflection and transmission by tailoring the spatial carrier-density profile, overcoming uncontrollable reflection from inhomogeneous dielectric environments [8]. The dielectric-modulated impact-ionization MOS transistor [7] uses dielectric modulation of a nanogap as a sensing mechanism, i.e., modulation as a *diagnostic*, not as a source of mechanical impulse. Magneto-dielectric coupling in piezoelectric resonators achieves modulation above $10\%$ at room temperature on ferroelectric single crystals and quartz discs [3], and non-equilibrium magnon engineering modulates thermal transport in solids [11]; both demonstrate that cross-field modulation of material response constants is real and measurable, and both operate on condensed matter, not on vacuum. A formulation of Maxwell's equations with tensor properties of time predicts vacuum polarization, anisotropy of electromagnetic wave velocity in vacuum, and anisotropy of the vacuum dielectric permittivity [10] — the closest formal precedent for treating vacuum permittivity as a tensor to be engineered, though it derives optical effects, not mechanical thrust.

Two further works bound the conjecture's microscopic and conceptual setting. Dielectric modulation of the electron-hole interaction in semiconductor quantum tubes [2] shows that excitonic binding energies are strongly tunable by the surrounding dielectric environment, with binding energies in InAs tubes reaching a substantial fraction of the gap [2] — a reminder that "permittivity" is a property of a material's charge response, which is why a vacuum analogue lacks an obvious microscopic handle. Finally, the foundational critique of modern physics' abstraction [14] argues that predictive success does not establish ontological correctness, and the QNFO glossary frames physics as the study of a medium's excitations [13]; both motivate taking the "vacuum as engineering material" question seriously enough to test it quantitatively rather than dismissing it — which is what the remainder of this paper does.

## 3. Methods

This paper is a theoretical analysis; it performs no experiment, simulation on hardware, or survey. Its method has four parts.

**Model.** The conjectured device is idealized as a finite region $\Omega$ of volume $V$ inside which the effective refractive index $n(\mathbf{x})$ differs from the vacuum value $n = 1$, static in time, with the metric-analogy relation $n(\mathbf{x}) = \sqrt{-g_{11}(\mathbf{x})/g_{00}(\mathbf{x})}$. The region may be "sourced" by electromagnetic fields, material inclusions, or both. Thrust is defined as the time-averaged net external force on the complete apparatus, including all field, dielectric and particle content, measured in the asymptotically flat frame.

**Assumptions.** (A1) General relativity and standard electrodynamics hold; the "vacuum permittivity" is either a true metric effect or a material polarization of some medium filling $\Omega$. (A2) The apparatus is closed: no mass, charge or radiation crosses its boundary except momentum the device deliberately expels. (A3) For numerical estimates we assume a meter-scale device, $L = 1\ \mathrm{m}$, an order-unity index change $\Delta n = 1$, electrical power $P = 1\ \mathrm{kW}$ available for the field-generating system, and a maximum material refractive index $n = 3$ (typical of high-index dielectrics; the opal systems of [9] reach $\Delta n \approx 0.1$–$0.3$). (A4) Constants used: $c = 2.998\times 10^{8}\ \mathrm{m\,s^{-1}}$, $G = 6.674\times 10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

**Derivations.** Section 4.1 inverts the Einstein equation $G_{00} = 8\pi G\,T_{00}/c^{4}$ for the energy density needed to sustain a curvature of scale $1/L^{2}$. Section 4.2 applies the center-of-mass theorem $\sum \mathbf{F}_{\mathrm{ext}} = d^{2}\mathbf{R}_{\mathrm{CM}}/dt^{2}\,M_{\mathrm{tot}}$ to the closed apparatus. Section 4.3 bounds the thrust by momentum flux of radiation through $\Omega$'s boundary. Section 4.4 applies the same momentum ledger to the capacitor system of [1]. All arithmetic is shown step by step.

**Computation.** All numerical results are evaluated by hand in Section 4 with explicit intermediate values; no simulation is performed. Where a number stands in for an unmeasured quantity it is labeled an assumption per (A3).

## 4. Analysis

### 4.1 Energy density required for a meter-scale index gradient

The conjecture requires an order-unity gradient in $n = \sqrt{-g_{11}/g_{00}}$ over a device length $L$. A dimensionless change $\Delta n = \mathcal{O}(1)$ in the metric components over length $L$ implies curvature of magnitude

$$
|R| \sim \frac{\Delta n}{L^{2}} \sim \frac{1}{L^{2}}\,.
$$

With $L = 1\ \mathrm{m}$ (assumption A3), $|R| \sim 1\ \mathrm{m^{-2}}$. Einstein's equation for the $00$-component gives

$$
G_{00} \sim |R| = \frac{8\pi G}{c^{4}}\,u\,,
$$

where $u = T_{00}$ is the energy density of the source. Solving for $u$:

$$
u = \frac{c^{4}}{8\pi G}\,\frac{1}{L^{2}}\,.
$$

Inserting the constants from (A4):

- $c^{4} = (2.998\times 10^{8})^{4} = 8.078\times 10^{33}\ \mathrm{m^{4}\,s^{-4}}$.
- $8\pi G = 8 \times 3.1416 \times 6.674\times 10^{-11} = 1.677\times 10^{-9}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.
- $u = \dfrac{8.078\times 10^{33}}{1.677\times 10^{-9} \times 1} = 4.82\times 10^{42}\ \mathrm{J\,m^{-3}}$.

Comparison scales: the observed dark-energy density is $\rho_{\Lambda} \approx 10^{-9}\ \mathrm{J\,m^{-3}}$ [12], so the required density exceeds it by

$$
\log_{10}\!\left(\frac{4.82\times 10^{42}}{10^{-9}}\right) = 42 - (-9) + \log_{10} 4.82 = 51.7\ \text{orders of magnitude}.
$$

Even if the patch were sourced by ordinary electromagnetic energy rather than geometry, the same $u$ would have to reside in $\Omega$ as real stress-energy, because Einstein's equations do not distinguish the two for a static patch. For comparison, an electromagnetic field at the practical breakdown-limited energy density of $u_{\mathrm{lab}} \sim 10^{8}\ \mathrm{J\,m^{-3}}$ (an assumption for a laboratory-scale high-field region) falls short by

$$
\log_{10}\!\left(\frac{4.82\times 10^{42}}{10^{8}}\right) = 34.7\ \text{orders of magnitude}.
$$

The conclusion of this subsection is independent of the sign details of $g_{11}$ and $g_{00}$: any static metric patch with order-unity component changes over meter scales requires an energy density within a few orders of magnitude of $c^{4}/(8\pi G L^{2})$, and no known laboratory source approaches it.

### 4.2 Momentum conservation forbids thrust from a static index profile

Let the complete apparatus — fields, dielectric or "vacuum-modulating" medium, structure, and any stored charge — constitute a closed system with total momentum $\mathbf{P}_{\mathrm{tot}}$ and total mass-energy $M_{\mathrm{tot}}$. The center-of-mass theorem for a closed relativistic system states

$$
\frac{d\mathbf{P}_{\mathrm{tot}}}{dt} = \mathbf{F}_{\mathrm{ext}} = \mathbf{0}\,, \qquad \mathbf{R}_{\mathrm{CM}}(t) = \mathbf{R}_{\mathrm{CM}}(0) + \frac{\mathbf{P}_{\mathrm{tot}}}{M_{\mathrm{tot}}}\,t\,.
$$

A static index profile $n(\mathbf{x})$ inside the apparatus is an internal arrangement of stress-energy. Internal forces — whatever their origin, geometric or material — sum to zero over the closed system. Therefore a device that merely *maintains* a region of $n(\mathbf{x}) \neq 1$, however steep the gradient, experiences

$$
F_{\mathrm{net}} = \frac{dP_{\mathrm{tot}}}{dt} = 0\,.
$$

This is the same bookkeeping that [5] applies microscopically: the radiation-pressure force and momentum diffusion of an atom near a dielectric interface are fixed entirely by the two-point correlation tensor of the vacuum field, i.e., by photon momentum exchange; no additional force arises from the static modification of the modes themselves [5]. A wave packet refracting through the gradient transfers momentum to the gradient region while entering and an equal and opposite amount while leaving; for a *static* profile and a closed cycle, the integrals cancel.

The only escape channels are ones where momentum leaves the apparatus:

1. **Radiation escape:** photons emitted anisotropically carry momentum $\mathbf{p} = \hbar\mathbf{k}$ away; the recoil is the photon-rocket thrust $F = P/c$.
2. **Particle escape:** charged or neutral particles expelled with flux $\dot{N}$ and mean momentum $\langle p \rangle$ give $F = \dot{N}\langle p \rangle$.
3. **Time-dependent modulation:** if $n(\mathbf{x},t)$ changes, the field momentum stored in $\Omega$ changes, and $F_{\mathrm{net}} = -dP_{\mathrm{field}}/dt$; but this is a transient that integrates to zero over any modulation cycle that returns the device to its initial state, and it cannot sustain steady thrust without an expelled momentum stream.

Channel 3 is the one a proponent of the conjecture would invoke. Its cycle-average is bounded by the momentum stored in the field, which Section 4.3 shows is small at laboratory power levels.

### 4.3 Thrust ceiling and energy cost for a dielectric-analogy region

Suppose the apparatus directs power $P$ through the gradient region and exploits the difference between momentum fluxes on the two sides. The maximum asymmetric momentum flux a dielectric region can impose on radiation is set by the Minkowski momentum flux $nP/c$ on the high-index side versus $P/c$ on the vacuum side; the difference is the largest possible reaction force per unit power:

$$
F_{\max} = \frac{P}{c}\,(n - 1)\,.
$$

With the assumptions of (A3), $P = 1\ \mathrm{kW} = 1.000\times 10^{3}\ \mathrm{W}$ and $n = 3$:

$$
F_{\max} = \frac{1.000\times 10^{3}}{2.998\times 10^{8}} \times (3 - 1) = 3.336\times 10^{-6} \times 2 = 6.67\times 10^{-6}\ \mathrm{N}\,.
$$

For the more conservative photon-rocket limit ($n \to 1$, pure anisotropic emission):

$$
F_{\gamma} = \frac{P}{c} = \frac{1.000\times 10^{3}}{2.998\times 10^{8}} = 3.34\times 10^{-6}\ \mathrm{N}\,.
$$

The energy cost per unit impulse follows directly. To deliver impulse $I = F\,\Delta t$ at thrust $F = P/c$ requires energy $E = P\,\Delta t = F\,c\,\Delta t$, so

$$
\frac{E}{I} = c = 2.998\times 10^{8}\ \mathrm{J\,N^{-1}\,s^{-1}}\,.
$$

Worked mission-scale example (projection, assumptions of A3 plus a $100\ \mathrm{kg}$ spacecraft and $\Delta v = 1\ \mathrm{m\,s^{-1}}$): the required impulse is

$$
I = M\,\Delta v = 100 \times 1 = 100\ \mathrm{N\,s}\,,
$$

and the energy cost is

$$
E = I \times c = 100 \times 2.998\times 10^{8} = 3.00\times 10^{10}\ \mathrm{J}\,.
$$

At a realistic spacecraft power system specific energy — we assume $100\ \mathrm{Wh\,kg^{-1}} = 3.6\times 10^{5}\ \mathrm{J\,kg^{-1}}$ for the storage system — the mass of energy storage alone would be

$$
M_{E} = \frac{3.00\times 10^{10}}{3.6\times 10^{5}} = 8.33\times 10^{4}\ \mathrm{kg}\,,
$$

i.e., $833$ times the spacecraft mass. The dielectric-analogy ceiling $F_{\max} = (P/c)(n-1)$ improves this by at most the factor $(n-1) = 2$ at $n=3$, reducing the storage mass to $4.17\times 10^{4}\ \mathrm{kg}$ — still $417$ times the spacecraft mass. No permittivity profile changes the $E/I = c$ floor, because that floor is set by the momentum carried per joule of any massless carrier.

### 4.4 Momentum accounting for the reported capacitor thrust

The experiments of [1] report a directional force during field-emission discharge of symmetric capacitors at $5$–$10\ \mathrm{kV}$, linear in accelerated mass, growing exponentially as electrode separation shrinks, reversible by conductive material behind the cathode, and persisting in soft vacuum [1]. The reported electron acceleration is of order $10^{19}\ \mathrm{m\,s^{-2}}$ [1].

Within the momentum ledger of Section 4.2, a force linear in the accelerated (electron) mass and dependent on the electron stream's geometry is the signature of expelled-charge recoil: electrons accelerated across the gap carry momentum $\dot{N}\langle p\rangle$, and the capacitor recoils oppositely; a conductor behind the cathode can intercept or re-absorb part of the electron stream, reversing or attenuating the net external momentum flux — exactly the reversibility reported in [1]. The exponential dependence on electrode separation is consistent with field-emission current's exponential sensitivity to gap field strength, which controls $\dot{N}$. This reinterpretation does not diminish the experimental care of [1]; it relocates the effect from vacuum modification to a known conservation-law channel, and it makes the framework falsifiable: if the force persisted when the electron stream was fully contained inside a closed current loop (no net expelled momentum), the center-of-mass theorem of Section 4.2 would be contradicted.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; assumptions are those of (A3).

- **R1 (Section 4.1).** A static metric patch with order-unity index change over $L = 1\ \mathrm{m}$ requires source energy density $u = c^{4}/(8\pi G L^{2}) = 4.82\times 10^{42}\ \mathrm{J\,m^{-3}}$, which is $51.7$ orders of magnitude above the observed dark-energy density $\rho_{\Lambda} \approx 10^{-9}\ \mathrm{J\,m^{-3}}$ [12] and $34.7$ orders above an assumed laboratory breakdown-limited field energy density of $10^{8}\ \mathrm{J\,m^{-3}}$.
- **R2 (Section 4.2).** A closed apparatus containing any static $n(\mathbf{x})$ profile experiences exactly zero net force; steady propellant-less thrust is possible only through expelled radiation or particles, or as zero-cycle-average transients from time-dependent modulation.
- **R3 (Section 4.3).** The thrust ceiling for a dielectric-analogy region is $F_{\max} = (P/c)(n-1)$; at $P = 1\ \mathrm{kW}$, $n = 3$: $F_{\max} = 6.67\times 10^{-6}\ \mathrm{N}$, versus the photon-rocket value $F_{\gamma} = 3.34\times 10^{-6}\ \mathrm{N}$.
- **R4 (Section 4.3).** The energy cost per unit impulse is $E/I = c = 2.998\times 10^{8}\ \mathrm{J\,N^{-1}\,s^{-1}}$; a $100\ \mathrm{N\,s}$ maneuver on a $100\ \mathrm{kg}$ spacecraft costs $3.00\times 10^{10}\ \mathrm{J}$, corresponding (at an assumed storage specific energy of $3.6\times 10^{5}\ \mathrm{J\,kg^{-1}}$) to $8.33\times 10^{4}\ \mathrm{kg}$ of storage, or $4.17\times 10^{4}\ \mathrm{kg}$ at the $n = 3$ ceiling — $417$ times the spacecraft mass.
- **R5 (Section 4.4).** The reported capacitor-force systematics of [1] — linearity in accelerated mass, exponential dependence on electrode gap, reversibility by a rear conductor — match expelled-electron recoil rather than vacuum modification; the discriminating test is whether the force survives full containment of the electron stream.

## 6. Discussion

The principal result is negative and structural: the conjecture's three proposed tests resolve against it. The stress-energy test (R1) shows the required source is $51.7$ orders of magnitude beyond any observed vacuum energy; the momentum-balance test (R2) shows that even a realized index gradient cannot push a closed apparatus; and the magnitude test (R3, R4) shows that the best achievable fallback — radiation reaction through a dielectric — is bounded by the photon rocket, whose energy cost makes it useless for primary propulsion at spacecraft scales.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each:

- **(A1) Standard GR and electrodynamics.** If the vacuum were a physical medium whose permittivity could be engineered by an as-yet-unknown mechanism outside GR's source term, R1 would not apply. The entire quantitative force of the paper depends on this assumption; no supplied evidence supports such a mechanism, and the tensor-time formulation of [10], which predicts vacuum permittivity anisotropy, derives optical effects rather than a mechanical source term.
- **(A2) Closure of the apparatus.** R2 is exact only for a closed system. Any real device radiates heat, vents charge, or interacts with Earth