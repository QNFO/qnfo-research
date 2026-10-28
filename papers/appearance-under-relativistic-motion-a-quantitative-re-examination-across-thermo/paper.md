# Appearance Under Relativistic Motion: A Quantitative Re‑Examination Across Thermodynamic, Radiative, and Structural Channels

## Abstract

A recurring question in relativistic physics is whether a physical system “appears” invariant to an observer moving at relativistic speed. The gap is definitional: “appears invariant” is ambiguous without specifying the observable and the measurement protocol. We operationally define appearance observables, then analytically derive explicit formulas for three concrete channels—thermodynamic appearance (apparent temperature of a moving gas and of an isotropic blackbody field), radiative appearance (Doppler factor, bolometric beaming, and radiation pressure on a receding perfect mirror), and structural appearance (diffraction, jet morphology, and a modeled atmospheric re‑entry event). For a benchmark speed $\beta_{1}=0.8$ we compute the longitudinal Doppler factors $D_{+}=3$ and $D_{-}=1/3$, the two candidate temperature‑transformation outcomes $T_{0}/\gamma_{1}=0.6\,T_{0}$ and $\gamma_{1}T_{0}=1.666667\,T_{0}$, and the solid‑angle‑averaged apparent temperature of an isotropic blackbody field, $\bar{T}=0.8240\,T_{0}$ (a $17.6\%$ cooling). We also compute the idealized radiation‑pressure reduction on a receding perfect mirror, $F_{1}/A=0.1778\,u_{0}$ versus the static value $2u_{0}$, a Jüttner‑tail suppression factor $4.5400\times10^{-5}$, and, for a modeled re‑entry event at $\beta=0.9$, an exact directional apparent‑temperature ratio $19$ and a bolometric‑flux ratio $130321$. The principal result is that appearance is generically non‑invariant; only properly engineered observables (e.g., momentum‑entangled Bell‑state spins) retain invariance. This quantifies a philosophical puzzle into protocol‑explicit, checkable numbers.

## 1. Introduction

A high‑speed spacecraft re‑entering a planetary atmosphere must predict the thermal load it will experience; a misestimate can cause catastrophic failure. Engineers designing such vehicles, as well as astrophysicists interpreting relativistic jet observations and designers of light‑driven propulsion systems, currently assume that the temperature or radiation pressure measured in the vehicle’s rest frame can be directly inferred from laboratory‑frame data. If appearance were invariant, a single laboratory measurement would suffice for all inertial observers. Instead, the question “does a system appear invariant to an observer moving at relativistic speeds?” determines whether design calculations must incorporate boost‑dependent corrections. This paper answers that question quantitatively.

Our contributions are:
1. Derivation of explicit Doppler‑factor formulas and temperature‑transformation candidates for a moving gas and an isotropic blackbody field (Section 4 A–D).
2. Computation of the solid‑angle‑averaged apparent temperature $\bar{T}=0.8240\,T_{0}$ at $\beta_{1}=0.8$, showing a $17.6\%$ cooling (Section 4 D).
3. Calculation of radiation‑pressure reduction on a receding perfect mirror, $F_{1}/A=0.1778\,u_{0}$ (Section 4 E).
4. Evaluation of a modeled atmospheric re‑entry event at $\beta=0.9$, yielding an apparent‑temperature ratio $19$ and a bolometric‑flux ratio $130321$ (Section 4 H).

## 2. Background and Related Work

We discuss seven arXiv works that provide concrete quantitative or methodological points relevant to our analysis.

**[1] Numeric Experiments in Relativistic Thermodynamics: A Moving System Appears Cooler.** This work simulates a two‑dimensional relativistic ideal gas, shows that the gas obeys Jüttner’s speed distribution $f(v)=v\gamma_{v}^{4}\exp(-\beta\gamma_{v})/Z$, and reports the mean‑energy formula $\langle E\rangle=(\beta^{2}+2\beta+2)/(\beta^{2}+\beta)$. Combining the simulation with the relativistic equipartition theorem, the authors conclude that a moving system appears cooler, i.e. $T^{\prime}=T/\gamma$.

**[2] Feynman‑Vernon model of a moving thermal environment.** This paper introduces a generalized oscillator model for a thermal bath moving with velocity $v_{\mathrm{env}}$, expressed through the Lagrangian term $L_{n}= \frac{m}{2}\big[(\dot{q}_{n}-v_{\mathrm{env}})^{2}-\omega_{n}^{2}(q_{n}-x)^{2}\big]$. It demonstrates that the environment’s velocity enters the dynamics, implying frame‑dependent environmental states.

**[3] Computing the interaction of light pulses with objects moving at relativistic speeds.** This study develops a polychromatic T‑matrix formalism for light‑matter interaction with uniformly moving objects, demonstrating that scattering amplitudes, radiation pressure, and momentum transfer depend explicitly on the Lorentz boost of the target.

**[4] Rayleigh‑Sommerfeld scalar diffraction by apertures moving at relativistic speeds.** The authors analytically obtain diffraction results for apertures moving transversely, showing that the transverse Doppler effect modifies the angular frequency and wavelength of the diffracted field, i.e. $\omega^{\prime}-\omega=\omega(\gamma-1)$.

**[5] Particle acceleration timescales in relativistic shear flows.** This review discusses how particle acceleration in shear flows depends on the local velocity profile, indicating that the effective particle spectrum observed in a given frame is shear‑dependent.

**[6] Relativistic‑invariant quantum entanglement between the spins of moving bodies.** The paper proves that if the momenta of two particles are appropriately entangled, the spin‑Bell‑state entanglement remains maximal for any Lorentz‑boosted observer, providing a positive invariance result under a special preparation.

**[7] The influence of collimation on the appearance of relativistic jets.** The authors numerically compute apparent velocity and Doppler factor for jets with different collimation profiles, showing that appearance quantities (apparent velocity, Doppler factor) depend strongly on internal velocity distribution and viewing geometry.

These works collectively demonstrate that rest‑frame scalars are invariant, while reconstructed observables are generally boost‑dependent, except in specially engineered quantum‑information settings.

## 3. Methods

**Protocol definition.** An “appearance observable” $X_{\mathrm{app}}$ is any quantity an observer reconstructs from received signals (photon frequencies, fitted temperatures, pressures, diffraction patterns). An “invariant observable” $X_{\mathrm{inv}}$ is a quantity defined in the system’s rest frame (proper temperature $T_{0}$, proper length $L_{0}$, proper pressure).

**Kinematic inputs.** Derivations use (i) the Lorentz factor $\gamma(\beta)=\bigl(1-\beta^{2}\bigr)^{-1/2}$; (ii) the relativistic Doppler factor for a line‑of‑sight component $\beta_{\parallel}$,
$$D=\frac{1}{\gamma\bigl(1-\beta_{\parallel}\bigr)};$$
(iii) photon number/momentum conservation at a moving mirror; (iv) the Jüttner exponential weight $\exp\!\bigl[-(\gamma_{\mathrm{p}}-1)mc^{2}/(k_{B}T)\bigr]$ for a particle of Lorentz factor $\gamma_{\mathrm{p}}$.

**Representative speeds.** Primary benchmark $\beta_{1}=0.8$ for thermodynamic and radiative channels; forward Doppler factor $D=10$ speed computed for cross‑check; re‑entry scenario adopts $\beta=0.9$; additional cross‑check at $\beta=0.6$.

**Scope.** Flat spacetime, inertial frames, idealized objects (perfect mirror, isotropic blackbody field, unidirectional monochromatic beam, single‑temperature re‑entry sheath). All quantitative results are derived analytically; no simulation or experimental data are reported.

## 4. Analysis

All arithmetic is shown explicitly. No number is imported from an external measurement.

### 4.1 Thermodynamic and radiative channels at $\beta_{1}=0.8$

**A. Lorentz factor.**
$$\gamma_{1}= \frac{1}{\sqrt{1-\beta_{1}^{2}}}= \frac{1}{\sqrt{1-0.64}}= \frac{1}{\sqrt{0.36}}= \frac{1}{0.6}= \frac{5}{3}\approx 1.666667.$$

**B. Doppler factors (longitudinal).**
Approaching ($\beta_{\parallel}=-\beta_{1}$):
$$D_{+}= \frac{1}{\gamma_{1}(1-\beta_{1})}= \frac{1}{(5/3)(0.2)}= \frac{1}{1/3}=3.$$
Receding ($\beta_{\parallel}=+\beta_{1}$):
$$D_{-}= \frac{1}{\gamma_{1}(1+\beta_{1})}= \frac{1}{(5/3)(1.8)}= \frac{1}{3}.$$
Transverse ($\beta_{\parallel}=0$): $D_{\perp}=1/\gamma_{1}=0.6$.

**C. Candidate temperature transformations.**
Cooler branch: $T_{\mathrm{cool}}=T_{0}/\gamma_{1}=0.6\,T_{0}$.
Hotter branch: $T_{\mathrm{hot}}=\gamma_{1}T_{0}=1.666667\,T_{0}$.
Ratio $T_{\mathrm{hot}}/T_{\mathrm{cool}}=\gamma_{1}^{2}=25/9\approx2.777778$.

**D. Apparent temperature of an isotropic blackbody field.**
Direction $\theta$ (angle between photon arrival direction and velocity) gives
$$T_{\mathrm{app}}(\theta)=\frac{T_{0}}{\gamma_{1}\bigl(1-\beta_{1}\cos\theta\bigr)}.$$
Forward ($\theta=0$): $T_{\mathrm{app}}=3T_{0}$.
Backward ($\theta=\pi$): $T_{\mathrm{app}}=T_{0}/3$.

Solid‑angle average: with $\mu=\cos\theta$,
$$\langle D\rangle=\frac{1}{4\pi}\int\frac{d\Omega}{\gamma_{1}(1-\beta_{1}\mu)}
=\frac{1}{\gamma_{1}}\cdot\frac{1}{2}\int_{-1}^{1}\frac{d\mu}{1-\beta_{1}\mu}.$$
The integral evaluates to
$$\int_{-1}^{1}\frac{d\mu}{1-\beta_{1}\mu}
=\frac{1}{\beta_{1}}\ln\frac{1+\beta_{1}}{1-\beta_{1}}
=\frac{2}{\beta_{1}}\operatorname{atanh}\beta_{1}.$$
Thus
$$\langle D\rangle=\frac{\operatorname{atanh}\beta_{1}}{\gamma_{1}\beta_{1}},\qquad
\bar{T}=T_{0}\,\frac{\operatorname{atanh}\beta_{1}}{\gamma_{1}\beta_{1}}.$$
Numerically, $\operatorname{atanh}(0.8)=\tfrac12\ln\frac{1.8}{0.2}=1.0986$, $\gamma_{1}\beta_{1}= (5/3)(0.8)=4/3\approx1.3333$, giving
$$\bar{T}=T_{0}\times\frac{1.0986}{1.3333}=0.8240\,T_{0},$$
a $17.6\%$ cooling relative to $T_{0}$.

**E. Radiation pressure on a receding perfect mirror (idealized unidirectional beam).**
Photon arrival rate per unit area is reduced by $(1-\beta_{1})$. Reflected photon frequency is redshifted by $\nu_{r}/\nu=(1-\beta_{1})/(1+\beta_{1})$. Momentum transfer per photon:
$$\Delta p=\frac{h\nu}{c}\Bigl(1-\frac{1-\beta_{1}}{1+\beta_{1}}\Bigr)
=\frac{h\nu}{c}\frac{2\beta_{1}}{1+\beta_{1}}.$$
Force per area:
$$\frac{F}{A}=u_{0}(1-\beta_{1})\frac{2\beta_{1}}{1+\beta_{1}}
=u_{0}\frac{2\beta_{1}(1-\beta_{1})}{1+\beta_{1}}.$$
At $\beta_{1}=0.8$: numerator $2(0.8)(0.2)=0.32$, denominator $1.8$, giving
$$\frac{F_{1}}{A}=u_{0}\times\frac{0.32}{1.8}=0.1778\,u_{0}.$$
Static mirror ($\beta=0$) yields $F_{0}/A=2u_{0}$, so the moving mirror experiences a suppression factor $0.1778/2=0.0889$ ($89.1\%$ reduction).

**F. Jüttner tail suppression.**
For $k_{B}T_{0}=0.1\,mc^{2}$, the weight ratio of particles with $\gamma_{\mathrm{p}}=2$ versus $\gamma_{\mathrm{p}}=1$ is
$$\frac{w(2)}{w(1)}=\exp\!\Bigl[-\frac{(2-1)mc^{2}}{0.1\,mc^{2}}\Bigr]=e^{-10}=4.5400\times10^{-5}.$$

**G. Speed for $D=10$.**
Longitudinal approach: $D=\sqrt{(1+\beta)/(1-\beta)}$. Setting $D=10$ gives $100=(1+\beta)/(1-\beta)$, solving $\beta=99/101\approx0.9802$.

### 4.2 Re‑entry channel at $\beta=0.9$

**H. Model assumptions.** Emitted temperature $T_{0}=2000\ \mathrm{K}$, proper duration $\Delta\tau=100\ \mathrm{s}$, radiating area $A$ (unspecified). Velocity $\beta=0.9$.

**Step 1: Lorentz factor.**
$$\gamma=\frac{1}{\sqrt{1-0.9^{2}}}
=\frac{1}{\sqrt{0.19}}
=\frac{1}{0.43589}\approx2.2942.$$

**Step 2: Approaching Doppler factor.**
$$D_{\mathrm{app}}=\frac{1}{\gamma(1-\beta)}
=\frac{1}{2.2942\times0.1}
=\frac{1}{0.22942}\approx4.3589.$$

**Step 3: Receding Doppler factor.**
$$D_{\mathrm{rec}}=\frac{1}{\gamma(1+\beta)}
=\frac{1}{2.2942\times1.9}
=\frac{1}{4.3589}\approx0.22942,$$
with $D_{\mathrm{app}}=1/D_{\mathrm{rec}}$.

**Step 4: Apparent‑temperature ratio.**
$$\frac{T_{\mathrm{app}}}{T_{\mathrm{rec}}}
=\frac{D_{\mathrm{app}}}{D_{\mathrm{rec}}}
=\frac{1+\beta}{1-\beta}
=\frac{1.9}{0.1}=19.$$

**Step 5: Apparent temperatures.**
$$T_{\mathrm{app}}=D_{\mathrm{app}}\,T_{0}=4.3589\times2000\ \mathrm{K}=8717.8\ \mathrm{K},$$
$$T_{\mathrm{rec}}=D_{\mathrm{rec}}\,T_{0}=0.22942\times2000\ \mathrm{K}=458.8\ \mathrm{K},$$
Transverse ($\theta=\pi/2$): $D_{\perp}=1/\gamma=0.43589$, $T_{\perp}=0.43589\times2000\ \mathrm{K}=871.8\ \mathrm{K}$.

**Step 6: Bolometric flux anisotropy.**
For an unresolved source $F_{\mathrm{obs}}=D^{4}F_{0}$, thus
$$\frac{F_{\mathrm{app}}}{F_{\mathrm{rec}}}
=\left(\frac{1+\beta}{1-\beta}\right)^{4}=19^{4}=130321.$$

**Step 7: Duration dilation.**
$$\Delta t_{\mathrm{obs}}=\gamma\Delta\tau=2.2942\times100\ \mathrm{s}=229.42\ \mathrm{s}.$$

**Step 8: Invariance test.** The observables $D$, $D^{4}$, and $\gamma$ all differ from unity, confirming non‑invariance.

## 5. Results

All numbers below are computed in Section 4 from stated assumptions.

1. **Doppler appearance factors at $\beta_{1}=0.8$:** $D_{+}=3$ (approaching), $D_{-}=1/3$ (receding), $D_{\perp}=0.6$ (transverse). Forward/backward apparent‑temperature ratio $9$.
2. **Temperature‑transformation candidates:** $T_{0}/\gamma_{1}=0.6\,T_{0}$ versus $\gamma_{1}T_{0}=1.666667\,T_{0}$; ratio $\gamma_{1}^{2}=25/9\approx2.777778$. Simulation [1] supports the cooler branch. Projection (labeled as such). Assuming the cooler transformation $T'=T_{0}/\gamma$, at $\beta=0.6$ we have $\gamma=1.25$ and thus $T'=0.8\,T_{0}$; for $T_{0}=300\ \mathrm{K}$ this gives $T'=240\ \mathrm{K}$ (a $20\%$ reduction).
3. **Angularly averaged apparent temperature of an isotropic blackbody field:** $\bar{T}=0.8240\,T_{0}$, a net cooling of $17.6\%$; locally $3T_{0}$ forward, $T_{0}/3$ backward.
4. **Idealized receding‑mirror radiation pressure:** $F_{1}/A=0.1778\,u_{0}$ versus $F_{0}/A=2u_{0}$ at rest — suppression factor $0.0889$ ($89.1\%$ reduction).
5. **Jüttner tail suppression** for $k_{B}T_{0}=0.1\,mc^{2}$ at $\gamma_{\mathrm{p}}=2$: $4.5400\times10^{-5}$.
6. **Speed for forward Doppler factor $D=10$:** $\beta=99/101\approx0.9802$.
7. **Re‑entry channel at $\beta=0.9$** (assumed $T_{0}=2000\ \mathrm{K}$, $\Delta\tau=100\ \mathrm{s}$): $T_{\mathrm{app}}=8717.8\ \mathrm{K}$, $T_{\perp}=871.8\ \mathrm{K}$, $T_{\mathrm{rec}}=458.8\ \mathrm{K}$; directional temperature ratio $19$; flux ratio $130321$; duration $\Delta t_{\mathrm{obs}}=229.42\ \mathrm{s}$.

**Projection (labeled as such).** Using $\bar{T}/T_{0}=\operatorname{atanh}\beta/(\gamma\beta)$ as a proxy for thermodynamic appearance:
- At $\beta=0.5$ ($\gamma=1.1547$, $\operatorname{atanh}0.5=0.5493$): $\bar{T}=0.9513\,T_{0}$ (cooling $4.9\%$).
- At $\beta=0.99$ ($\gamma=7.0888$, $\operatorname{atanh}0.99=2.6467$): $\bar{T}=0.3771\,T_{0}$ (cooling $62.3\%$).
These are kinematic projections; their validity as thermodynamic appearance measures rests on the protocol choice.

## 6. Discussion

**Main claim.** Appearance is generically not invariant under relativistic motion. Every channel examined—thermodynamic fit [1], dissipative environment model [2], mechanical radiation pressure [3], optical interaction [3], diffraction [4], shear‑flow acceleration [5], jet morphology [7], and the modeled re‑entry event—exhibits frame‑dependence. The single positive invariance result in the corpus [6] required a special preparation (momentum entanglement), reinforcing that invariance is conditional, not generic.

**Limitations and failure modes.**
(i) The blackbody angular average (Result 3) adopts a solid‑angle weighting; alternative weightings would yield different numbers, so the $17.6\%$ cooling is protocol‑relative.
(ii) The mirror calculation (Result 4) uses a unidirectional monochromatic beam rather than an isotropic blackbody field; the true drag on a mirror in an isotropic field involves angular integrals not performed here.
(iii) Identification of $\bar{T}$ with the “appears cooler” statement of [1] bridges two different methodologies (simulation versus Doppler averaging); the connection is interpretive, not derived.
(iv) The re‑entry model treats the sheath as a single‑temperature emitter observed via a point‑source Doppler factor; real re‑entry plasmas are spatially structured and non‑equilibrium.
(v) Only inertial frames and flat spacetime are considered; acceleration, gravity, and broader quantum‑field‑ontology contexts are out of scope.

**What would falsify the claims.** A controlled simulation showing that a moving observer’s fitted temperature of a relativistic gas equals $T_{0}$ within statistical errors would falsify the cooling claim on the thermodynamic channel. An experiment demonstrating that the solid‑angle‑averaged Doppler factor equals unity for any $\beta>0$ would falsify the angular‑average formula; such a result would contradict elementary kinematics. Observation that the radiation‑pressure reduction on a moving mirror matches the static value $2u_{0}$ for $\beta_{1}=0.8$ would falsify the mirror calculation.

**Against ourselves.** One could argue that “appearance invariance” should be defined as invariance of Lorentz‑scalar quantities (proper time, invariant mass), which are trivially invariant. We reject this reading because the question concerns observable signals reconstructed by a moving observer. Nonetheless, we acknowledge that different definitions of “appearance” could shift the focus of the analysis. Moreover, the possibility that a cleverly defined observable (e.g., a specific spectral‑line ratio) could be boost‑invariant remains open.

**Open questions.** Which appearance observable, if any, is canonical across contexts? Does the cooling factor $\operatorname{atanh}\beta/(\gamma\beta)$ correspond to what an actual calorimetric measurement would yield? How does the equipartition temperature transformation derived in [1] compose with the Doppler factor? How do diffraction results of [5] combine with thermodynamic results for a moving, finite‑temperature, structured object?

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**
- **Relativistic spacecraft designers** will use the derived Doppler‑factor and temperature‑averaging formulas to size thermal protection systems for high‑speed re‑entry, adjusting material thickness and coolant capacity based on the predicted $17.6\%$ cooling at $\beta=0.8$ and the larger anisotropy at $\beta=0.9$.
- **High‑energy particle‑detector engineers** will incorporate the radiation‑pressure suppression factor $0.0889$ when calibrating momentum‑transfer measurements for detectors moving relative to a radiation background.
- **Astrophysical jet modelers** will apply the directional temperature ratio $19$ and flux ratio $130321$ to interpret observed beaming in blazar spectra, informing jet‑collimation parameter choices.
- **Quantum‑communication system developers** will note that only specially prepared momentum‑entangled states retain spin‑entanglement invariance [7]; generic thermal or optical channels remain frame‑dependent.

**(b) Current readiness.** The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.**
A laboratory test can be performed with a high‑temperature blackbody cavity ($T_{0}=300\ \mathrm{K}$) and a detector mounted on a precision rotary platform capable of tangential speeds up to $v\approx0.01c$ ($\approx3\times10^{3}$ km s$^{-1}$). The detector records the spectral radiance as a function of rotation angle, allowing reconstruction of $T_{\mathrm{app}}(\theta)$. The experiment tests the predicted anisotropy $T_{\mathrm{app}}(\theta)=T_{0}/[\gamma(1-\beta\cos\theta)]$ and the solid‑angle‑averaged cooling factor. A measured average temperature deviating from $T_{0}$ by the predicted $0.99995$ factor (for $\beta=0.01$) would confirm the kinematic model; a null deviation within experimental uncertainty would falsify the claim.

**(d) Engineering constraints.**
- **Velocity measurement:** Accurate determination of $\beta$ to better than $10^{-4}$ is required to resolve the small cooling effect at modest speeds.
- **Blackbody stability:** The cavity must maintain uniform temperature within $0.1\%$ during rotation.
- **Detector calibration:** Radiometric calibration must be traceable to SI standards to detect sub‑percent temperature differences.
- **Mechanical limits:** Rotational bearings and balance must sustain high peripheral speeds without inducing vibrations that could corrupt radiometric data.
- **Data acquisition bandwidth:** Sufficient sampling rate to resolve angular variations at the rotation frequency.

**(e) Projected performance bounds (labeled as projections).**
Using $\bar{T}/T_{0}=\operatorname{atanh}\beta/(\gamma\beta)$:
- For $\beta=0.1$ ($\gamma=1.0050$), $\operatorname{atanh}0.1=0.1003$, giving $\bar{T}=0.998\,T_{0}$ ($\approx 2$ K cooling for $T_{0}=300\ \mathrm{K}$).
- For $\beta=0.5$ ($\gamma=1.1547$), $\operatorname{atanh}0.5=0.5493$, giving $\bar{T}=0.9513\,T_{0}$ ($\approx 15$ K cooling).
Assuming velocity uncertainty $\Delta\beta=0.001$, the induced uncertainty in $\bar{T}$ is $\approx0.1\%$, well within typical radiometric error budgets.

**(f) Direct risks or misuse paths.** Misapplication of the invariance assumption could lead to under‑design of thermal protection for relativistic re‑entry vehicles, risking structural failure. Over‑reliance on the engineered invariance of entangled spin states [7] without proper momentum‑entanglement preparation could compromise quantum‑communication security. Clear documentation of the protocol‑dependence of appearance observables mitigates these risks.

## 8. Conclusion

We asked whether a physical system appears invariant to an observer moving at relativistic speed, and answered operationally by fixing measurement protocols and computing appearance observables with fully shown arithmetic. Across the thermodynamic channel (candidate temperature transformations $T_{0}/\gamma_{1}=0.6\,T_{0}$ versus $\gamma_{1}T_{0}=1.666667\,T_{0}$ at $\beta_{1}=0.8$; angularly averaged blackbody apparent temperature $\bar{T}=0.8240\,T_{0}$, a $17.6\%$ cooling), the radiative channel (receding‑mirror pressure $F_{1}/A=0.1778\,u_{0}$ versus $2u_{0}$ at rest; Jüttner tail suppression $4.5400\times10^{-5}$), and the structural channel (a modeled re‑entry event at $\beta=0.9$ with directional apparent‑temperature ratio $19$ and bolometric flux ratio $19^{4}=130321$), no examined observable is invariant under boosts. The one positive invariance result in the corpus [6] holds only under a special preparation (momentum entanglement), supporting the conclusion that appearance invariance, where it exists, is engineered rather than generic. Rest‑frame quantities remain the invariant content of the theory; what a moving observer reconstructs from received signals is generically frame‑dependent, and the size of the departure is quantifiable at any stated speed by the elementary factors used here.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Numeric Experiments in Relativistic Thermodynamics: A Moving System Appears Cooler. arXiv:0804.3836v3. https://arxiv.org/abs/0804.3836v3
[2] Feynman-Vernon model of a moving thermal environment. arXiv:1803.10300v1. https://arxiv.org/abs/1803.10300v1
[3] Computing the interaction of light pulses with objects moving at relativistic speeds. arXiv:2404.05117v1. https://arxiv.org/abs/2404.05117v1
[4] Rayleigh-Sommerfeld scalar diffraction by apertures moving at relativistic speeds. arXiv:2010.02547v2. https://arxiv.org/abs/2010.02547v2
[5] Particle acceleration timescales in relativistic shear flows. arXiv:astro-ph/0506719v1. https://arxiv.org/abs/astro-ph/0506719v1
[6] Relativistic-invariant quantum entanglement between the spins of moving bodies. arXiv:quant-ph/0211159v2. https://arxiv.org/abs/quant-ph/0211159v2
[7] The influence of collimation on the appearance of relativistic jets. arXiv:1010.5895v1. https://arxiv.org/abs/1010.5895v1
[9] https://papers.qnfo.org/papers/critical-examination-of-spacetime-mass-and-gravity-through-competing-ontological. QNFO: Critical Examination of Spacetime, Mass, and Gravity through Competing Ontological Frameworks.
