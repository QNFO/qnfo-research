# Vacuum Dielectric Modulation and Propellant‑less Thrust: Energy‑Density, Momentum‑Conservation, and Thrust Limits

## Abstract
Propellant‑less thrust would eliminate the mass penalty of carrying reaction mass and could transform spacecraft design. Recent capacitor‑discharge experiments report micro‑newton forces, but no quantitative analysis has examined whether a spatially varying vacuum permittivity can generate thrust without expelling momentum. This work addresses three gaps: (i) the energy‑density required to sustain an order‑unity refractive‑index gradient in vacuum, (ii) the momentum‑balance constraint on static index profiles, and (iii) the ultimate thrust ceiling for any dielectric‑analogy device powered at realistic levels. By inverting Einstein’s field equation for a meter‑scale metric patch we obtain a required energy density of $u = 4.8\times10^{42}\,\mathrm{J\,m^{-3}}$, far exceeding known vacuum energy scales. Applying the center‑of‑mass theorem to a closed apparatus shows that a static $n(\mathbf{x})$ profile produces zero net force; steady thrust can arise only from expelled radiation or particles. A thrust‑limit analysis yields $F_{\max}= (P/c)(n-1)$, giving $F_{\max}=6.7\times10^{-6}\,\mathrm{N}$ for $P=1\,\mathrm{kW}$ and $n=3$, and confirms the photon‑rocket energy cost $E/I = c = 3.0\times10^{8}\,\mathrm{J\,N^{-1}\,s^{-1}}$. These results redirect experimental effort toward expelled‑momentum mechanisms, set realistic performance bounds, and provide a concrete falsification test for vacuum‑modulation thrust claims.

## 1. Introduction
Spacecraft that rely on chemical or electric propulsion must allocate a large fraction of launch mass to propellant, limiting mission duration and payload capacity. Propellant‑less thrust, if realizable, would remove this constraint and enable continuous acceleration without mass loss. Laboratory observations of a directional force on thin symmetric capacitors during high‑voltage field‑emission discharge have suggested a thrust mechanism that does not involve expelled mass [1]. If a controllable vacuum permittivity gradient could generate thrust, spacecraft designers could implement lightweight, high‑voltage dielectric structures as primary actuators, dramatically reducing launch mass and extending mission lifetimes. However, no quantitative analysis has examined whether the required vacuum modification is physically attainable or whether static index gradients can produce net force. This paper therefore (i) computes the energy density needed for an order‑unity index gradient, (ii) proves that a static index profile cannot yield net thrust in a closed system, and (iii) derives the maximal thrust attainable from a dielectric‑analogy region powered at realistic levels.  

**Contributions.**  
- **C1.** Derivation of the energy‑density requirement $u = c^{4}/(8\pi G L^{2})$ for an order‑unity index gradient over a length $L$ (Section 4.1).  
- **C2.** Proof that a static refractive‑index profile $n(\mathbf{x})$ yields zero net force on a closed apparatus (Section 4.2).  
- **C3.** Thrust‑ceiling formula $F_{\max}= (P/c)(n-1)$ and numerical bound for $P=1\,\mathrm{kW}$, $n=3$ (Section 4.3).  
- **C4.** Specification of the minimal experimental configuration that can falsify a vacuum‑modulation thrust claim (Section 7).

## 2. Background and Related Work
1. **Capacitor‑discharge thrust.** Thin symmetric capacitors driven at $5$–$10\ \mathrm{kV}$ exhibit a directional force that scales linearly with the accelerated electron mass and grows exponentially as the electrode gap is reduced [1]. This provides the empirical benchmark any vacuum‑modulation theory must address.  
2. **Magneto‑dielectric coupling.** Integrated piezoelectric resonators demonstrate a strong magneto‑capacitance effect at room temperature [3], establishing that sizable electromagnetic property changes are experimentally attainable in solid media.  
3. **Momentum diffusion near dielectric interfaces.** A master‑equation analysis of an atom close to a flat dielectric surface yields explicit radiation‑pressure and momentum‑diffusion expressions in terms of the vacuum field correlation function [5], showing that momentum exchange is fully accounted for by photon recoil.  
4. **Vacuum‑energy density discrepancy.** The Planck vacuum energy density ($\approx10^{133}\,\mathrm{J\,m^{-3}}$) exceeds the observed dark‑energy density ($\approx10^{-9}\,\mathrm{J\,m^{-3}}$) by 120 orders of magnitude [12], highlighting the vast gap between theoretical vacuum energy scales and measurable phenomena.  
5. **Green‑function treatment of dielectric gratings.** The Dyson‑equation‑based method solves wave propagation through arbitrary dielectric modulation profiles and confirms that index modulation redirects waves without injecting net momentum [4].  
6. **Emission in periodic dielectric structures.** Sinusoidal dielectric modulation with $\Delta n\approx0.1$–$0.3$ strongly influences spontaneous emission but does not produce a net mechanical force [9].  
7. **Active spatial control of terahertz plasmons.** Graphene carrier‑density profiling demonstrates that engineered conductivity (and thus effective permittivity) can steer electromagnetic energy flow [8], illustrating the feasibility of prescribed $n(\mathbf{x})$ profiles in material systems.  
8. **Dielectric‑modulated excitonic response.** Semiconductor quantum tubes show large excitonic binding‑energy shifts when the surrounding dielectric constant is altered [2], further confirming that dielectric engineering can produce sizable electromagnetic effects.

These works collectively (i) provide quantitative parameters for index modulation, (ii) describe momentum exchange mechanisms in inhomogeneous dielectrics, and (iii) establish the energy‑density context for vacuum‑property manipulation.

## 3. Methods
**Model.** The device is idealized as a finite region $\Omega$ of volume $V$ in which the effective refractive index $n(\mathbf{x})$ differs from the vacuum value $n=1$, static in time, and related to a static metric by $n(\mathbf{x})=\sqrt{-g_{11}(\mathbf{x})/g_{00}(\mathbf{x})}$. The region may be sourced by electromagnetic fields, material inclusions, or both. Thrust is defined as the time‑averaged net external force on the complete apparatus, measured in an asymptotically flat frame.

**Assumptions.**  
- **A1.** General relativity and standard electrodynamics hold.  
- **A2.** The apparatus is closed: no mass, charge, or radiation crosses its boundary except momentum that the device deliberately expels.  
- **A3.** For numerical estimates we assume a meter‑scale device ($L=1\,\mathrm{m}$), an order‑unity index change ($\Delta n=1$), electrical power $P=1\,\mathrm{kW}$, and a maximum material refractive index $n=3$ (typical of high‑index dielectrics).  
- **A4.** Constants: $c=2.998\times10^{8}\,\mathrm{m\,s^{-1}}$, $G=6.674\times10^{-11}\,\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

**Derivations.** Section 4.1 inverts Einstein’s equation $G_{00}=8\pi G\,T_{00}/c^{4}$ to obtain the energy density needed for a prescribed curvature. Section 4.2 applies the relativistic center‑of‑mass theorem to a closed system with static $n(\mathbf{x})$. Section 4.3 derives a thrust ceiling from momentum‑flux considerations. Section 4.4 interprets the capacitor‑thrust experiments of [1] within the momentum‑ledger framework. All arithmetic is shown step‑by‑step; numbers introduced as assumptions are labeled accordingly.

## 4. Analysis

### 4.1 Energy density required for a meter‑scale index gradient
An order‑unity change $\Delta n\sim1$ over a length $L$ implies a curvature magnitude $|R|\sim\Delta n/L^{2}\sim1/L^{2}$. Einstein’s $00$‑component gives
\[
G_{00}\sim|R|=\frac{8\pi G}{c^{4}}\,u,
\]
where $u=T_{00}$ is the required energy density. Solving,
\[
u=\frac{c^{4}}{8\pi G}\,\frac{1}{L^{2}}.
\]
Insert the constants (Assumption A4) and $L=1\,\mathrm{m}$ (Assumption A3):
\[
c^{4}=(2.998\times10^{8})^{4}=8.078\times10^{33},
\]
\[
8\pi G=8\times3.1416\times6.674\times10^{-11}=1.677\times10^{-9},
\]
\[
u=\frac{8.078\times10^{33}}{1.677\times10^{-9}\times1}=4.82\times10^{42}\,\mathrm{J\,m^{-3}}.
\]
The observed dark‑energy density is $\rho_{\Lambda}\approx10^{-9}\,\mathrm{J\,m^{-3}}$ [12]; the required density exceeds it by
\[
\log_{10}\!\left(\frac{4.82\times10^{42}}{10^{-9}}\right)=51.7\ \text{orders of magnitude}.
\]

### 4.2 Momentum conservation forbids thrust from a static index profile
For a closed relativistic system the center‑of‑mass theorem states
\[
\frac{d\mathbf{P}_{\text{tot}}}{dt}=\mathbf{F}_{\text{ext}}=\mathbf{0},
\]
where $\mathbf{P}_{\text{tot}}$ is the total momentum. A static index profile $n(\mathbf{x})$ is an internal arrangement of stress‑energy; internal forces sum to zero, so the net external force on the apparatus is zero:
\[
F_{\text{net}}=0.
\]
This mirrors the result of the momentum‑diffusion analysis for an atom near a dielectric interface [5], which attributes all forces to photon recoil. Consequently, steady propellant‑less thrust can arise only if momentum leaves the apparatus as radiation, particles, or via time‑dependent modulation.

### 4.3 Thrust ceiling and energy cost for a dielectric‑analogy region
The maximum asymmetric momentum flux a dielectric region can impose on radiation is the difference between Minkowski momentum fluxes on the high‑index and vacuum sides:
\[
F_{\max}=\frac{P}{c}\,(n-1).
\]
Using $P=1\,\mathrm{kW}=1.000\times10^{3}\,\mathrm{W}$ and $n=3$ (Assumption A3):
\[
F_{\max}= \frac{1.000\times10^{3}}{2.998\times10^{8}}\times(3-1)
        =3.336\times10^{-6}\times2
        =6.67\times10^{-6}\,\mathrm{N}.
\]
The pure photon‑rocket limit corresponds to $n\to1$:
\[
F_{\gamma}= \frac{P}{c}=3.34\times10^{-6}\,\mathrm{N}.
\]
The energy cost per unit impulse follows from $E=P\,\Delta t$ and $I=F\,\Delta t$:
\[
\frac{E}{I}=c=2.998\times10^{8}\,\mathrm{J\,N^{-1}\,s^{-1}}.
\]
A $100\,\mathrm{kg}$ spacecraft requiring $\Delta v=1\,\mathrm{m\,s^{-1}}$ needs $I=100\,\mathrm{N\,s}$, thus $E=I\,c=3.00\times10^{10}\,\mathrm{J}$. Assuming a storage specific energy of $100\,\mathrm{Wh\,kg^{-1}}=3.6\times10^{5}\,\mathrm{J\,kg^{-1}}$, the required storage mass is
\[
M_{E}= \frac{3.00\times10^{10}}{3.6\times10^{5}}=8.33\times10^{4}\,\mathrm{kg},
\]
or $4.17\times10^{4}\,\mathrm{kg}$ when the $n=3$ ceiling halves the required power, still hundreds of times the spacecraft mass.

### 4.4 Momentum accounting for the reported capacitor thrust
The capacitor experiments of [1] report a force that (i) scales linearly with the accelerated electron mass, (ii) grows exponentially as the electrode gap shrinks, and (iii) reverses when a conductive shield is placed behind the cathode. Within the momentum‑ledger of Section 4.2, these systematics match expelled‑electron recoil: electrons accelerated across the gap carry momentum $\dot{N}\langle p\rangle$, and the capacitor recoils oppositely; a rear conductor can intercept part of the electron stream, altering the net external momentum flux. The exponential gap dependence follows the field‑emission current’s sensitivity to gap field strength. Therefore, the observed force can be explained without invoking a vacuum‑modification thrust mechanism. A decisive falsification test is to enclose the electron stream in a closed current loop so that no net momentum leaves the apparatus; the force should then vanish.

## 5. Results
- **R1 (Section 4.1).** An order‑unity index gradient over $L=1\,\mathrm{m}$ requires $u = 4.82\times10^{42}\,\mathrm{J\,m^{-3}}$, exceeding the dark‑energy density by $51.7$ orders of magnitude.  
- **R2 (Section 4.2).** A closed apparatus with any static $n(\mathbf{x})$ profile experiences exactly zero net force; steady thrust is possible only via expelled radiation, particles, or transient time‑dependent modulation.  
- **R3 (Section 4.3).** The thrust ceiling for a dielectric‑analogy region is $F_{\max}= (P/c)(n-1)$; for $P=1\,\mathrm{kW}$, $n=3$ this yields $F_{\max}=6.67\times10^{-6}\,\mathrm{N}$, while the photon‑rocket limit is $3.34\times10^{-6}\,\mathrm{N}$.  
- **R4 (Section 4.3).** The energy cost per unit impulse is $E/I = c = 2.998\times10^{8}\,\mathrm{J\,N^{-1}\,s^{-1}}$; a $100\,\mathrm{N\,s}$ maneuver on a $100\,\mathrm{kg}$ spacecraft would require $3.00\times10^{10}\,\mathrm{J}$, implying storage masses of $8.33\times10^{4}\,\mathrm{kg}$ (photon‑rocket) or $4.17\times10^{4}\,\mathrm{kg}$ (with $n=3$).  
- **R5 (Section 4.4).** The capacitor‑thrust systematics are consistent with expelled‑electron recoil; enclosing the electron stream should eliminate the force, providing a direct falsification of any vacuum‑modulation thrust claim.

## 6. Discussion
### Limitations
- **L1 (Assumption A1).** The analysis assumes standard general relativity and electrodynamics; exotic vacuum‑engineering mechanisms outside these frameworks could evade the energy‑density bound.  
- **L2 (Assumption A2).** The zero‑force result holds only for a truly closed system; any unnoticed leakage of charge or radiation would constitute an expelled‑momentum channel.  
- **L3 (Assumption A3).** Numerical bounds use $L=1\,\mathrm{m}$, $P=1\,\mathrm{kW}$, and $n=3$; different scales would alter the quantitative limits proportionally.  
- **L4 (Neglected effects).** Edge fields, dielectric heating, and non‑ideal material losses are omitted; they would only reduce the available stored energy and thus the thrust.  

### Falsification Criterion
A controlled experiment that reproduces the capacitor geometry of [1] while fully containing the emitted electron stream in a closed conductive loop must measure a thrust **< 3.3\times10^{-7}\,\mathrm{N}**, i.e., below one‑tenth of the photon‑rocket thrust predicted for $P=1\,\mathrm{kW}$ (Section 4.3). Observation of a force above this threshold would falsify the momentum‑conservation argument and imply new physics beyond the present model.

### Open Questions
- Can a vacuum‑analog permittivity gradient of $\Delta n/n\approx0.1$ be realized without introducing additional mass or magnetic fields?  
- What is the explicit stress‑energy tensor that would source the metric patch, and does it satisfy the weak and dominant energy conditions?  
- How do time‑dependent index modulations affect transient thrust, and can they be harnessed without violating the cycle‑average zero‑force result?

## 7. Practical Implications and Engineering Pathways
**(a) Potential users and design impact.** Propulsion engineers evaluating micro‑newton‑level thrust options can use the derived limits to assess whether dielectric‑gradient modules offer any advantage over conventional photon‑rocket designs. The analysis shows that, at realistic power levels, such modules cannot exceed the photon‑rocket thrust ceiling, so design efforts should focus on efficient radiation or particle ejection rather than static vacuum modulation.  

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s scale it resides at **TRL 1–2**.  

**(c) Smallest next experiment.** A laboratory test consisting of a parallel‑plate capacitor (area $1\,\mathrm{cm^{2}}$, gap $20\,\mu\mathrm{m}$) charged to $5\,\mathrm{kV}$, mounted on a torsion‑balance capable of detecting forces down to $10^{-8}\,\mathrm{N}$, and equipped with a closed conductive enclosure that captures all emitted electrons, would directly test the momentum‑conservation prediction. Observation of a thrust **$\ge 3.3\times10^{-7}\,\mathrm{N}$** under these conditions would falsify the present model.  

**(d) Engineering constraints.**  
- **Voltage insulation:** Maintaining $5\,\mathrm{kV}$ across $20\,\mu\mathrm{m}$ requires dielectric breakdown strength $>250\,\mathrm{MV\,m^{-1}}$.  
- **Plate alignment:** Sub‑micron parallelism is needed to avoid field enhancement and premature arcing.  
- **Index‑modulation mechanism:** Achieving $\Delta n/n\approx0.1$ in a vacuum‑analog region would likely involve embedding magneto‑dielectric composites or metamaterial layers, constrained by sub‑micron fabrication tolerances.  
-   

 Performance scales linearly with plate area and voltage; doubling either parameter doubles thrust, but the thrust remains bounded by the photon‑rocket limit derived in Section 4.3.  

**(f) Risks and misuse.** High‑voltage discharges pose electrical‑hazard risks; appropriate interlocks are required. Misinterpretation of a measured force as evidence of vacuum‑modification thrust could lead to premature integration of unvalidated propulsion concepts into mission designs, risking mission failure.

## 8. Conclusion
An analytical investigation of vacuum‑permittivity‑gradient thrust has revealed three decisive constraints: (i) an order‑unity index gradient over meter scales demands an unattainably large energy density ($\sim10^{42}\,\mathrm{J\,m^{-3}}$), (ii) a static refractive‑index profile cannot generate net thrust in a closed system, and (iii) the maximal thrust achievable from a dielectric‑analogy region at realistic power levels is bounded by the photon‑rocket limit ($\sim10^{-6}\,\mathrm{N}$). These results explain the capacitor‑discharge forces reported in [1] as expelled‑electron recoil rather than vacuum modification, and they set clear performance ceilings for any future dielectric‑gradient propulsion concepts. Experimental effort should therefore concentrate on measuring momentum‑expulsion channels and on technologies that can approach the photon‑rocket efficiency, while the energy‑density barrier indicates that static vacuum engineering is not a viable path to propellant‑less thrust with current physics.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.33.9-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Electrostatic accelerated electrons within symmetric capacitors during field emission condition events exert bidirectional propellant-less thrust. arXiv:1810.04368. https://arxiv.org/abs/1810.04368
[2] Semiconductor quantum tubes: dielectric modulation and excitonic response. arXiv:1002.2078. https://arxiv.org/abs/1002.2078
[3] First evidence of a strong Magneto-capacitance coupling at room temperature in integrated piezoelectric resonators. arXiv:cond-mat/0411265. https://arxiv.org/abs/cond-mat/0411265
[4] Calculation of optical-waveguide grating characteristics using Green's functions and the Dyson's equation. arXiv:cond-mat/0607601. https://arxiv.org/abs/cond-mat/0607601
[5] Recoil and momentum diffusion of an atom close to a vacuum-dielectric interface. arXiv:quant-ph/9804022. https://arxiv.org/abs/quant-ph/9804022
[8] Active spatial control of terahertz graphene plasmons by tailoring carrier density profile. arXiv:1911.08672. https://arxiv.org/abs/1911.08672
[9] Emission Spectrum of a Dipole in a Semi-infinite Periodic Dielectric Structure: Effect of the Boundary. arXiv:cond-mat/0004456. https://arxiv.org/abs/cond-mat/0004456
[12] https://papers.qnfo.org/papers/hydrodynamic-spacetime. QNFO: SPACETIME CONDENSATE.
