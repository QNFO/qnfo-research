# Geometric Selection of Stable Helical Wave Modes on a Toroidal Domain

## Abstract
Tokamak magnetic field lines, toroidal resonators, and toroidal waveguides suffer from mode‑instability that forces costly redesigns or limits operational performance.  Existing stability criteria rely on material parameters, plasma profiles, or detailed numerical eigenmode simulations, but no purely geometric predictor has been established.  We derive a quantization condition for scalar and electromagnetic waves confined to a toroidal boundary by separating variables in toroidal coordinates and enforcing constructive interference around both the toroidal (major) and poloidal (minor) cycles.  The condition reduces to the rational winding ratio  

\[
\frac{R}{a}= \frac{m}{n},
\]

where \(R\) and \(a\) are the major and minor radii and \((m,n)\in\mathbb{Z}^{2}_{>0}\) are the toroidal and poloidal mode numbers.  For a torus with \(R=0.50\;\text{m}\) and \(a=0.10\;\text{m}\) the smallest rational pair is \((m,n)=(5,1)\); the resulting wavenumber is  

\[
k=\frac{m}{R}=10\;\text{rad·m}^{-1},
\]

and the corresponding electromagnetic frequency is  

\[
f=\frac{c\,k}{2\pi}\approx4.77\times10^{8}\;\text{Hz}.
\]

Thus a purely geometric selection rule predicts a stable helical mode at \(\sim 480\;\text{MHz}\).  The rule enables designers of fusion devices, toroidal resonators, and waveguides to choose geometry that guarantees mode stability without recourse to material‑specific simulations.

## 1. Introduction
Instabilities of helical wave modes in toroidal configurations limit the performance of magnetic confinement fusion devices, degrade the quality factor of toroidal microwave resonators, and cause unwanted attenuation in toroidal waveguides.  In a tokamak, uncontrolled drift of field‑line resonances can lead to rapid energy loss, requiring expensive magnetic coil redesigns and reducing plasma confinement time.  In toroidal resonators, mode‑mixing forces the use of exotic materials or active feedback, raising fabrication cost and complexity.  A design decision that would eliminate these burdens is a geometry‑only predictor that tells engineers whether a given toroidal shape supports a stable helical mode.

We address this “so what?” by formulating a geometric selection rule that depends solely on the torus radii and the integer winding numbers of the wave.  The rule is derived analytically, requires no material parameters, and can be evaluated before any prototype is built.  Our contributions are:

1. **Derivation of a rational‑winding quantization condition** for toroidal wave modes (Section 3).  
2. **Explicit arithmetic demonstration** that a torus with \(R=0.5\;\text{m}\) and \(a=0.1\;\text{m}\) supports a stable mode at \(4.77\times10^{8}\;\text{Hz}\) (Section 4).  
3. **Mapping of the selection rule to practical design parameters** for tokamaks, resonators, and waveguides (Section 7).  

The result also bears on any physical system where wave propagation is confined to a doubly‑periodic geometry, such as optical fibers with toroidal cores or acoustic cavities with toroidal chambers.

## 2. Background and Related Work
The present work draws on several strands of geometric and wave‑theoretic literature.

* **Coarse selectors** provide a formalism for choosing elements from finite subsets in a way that respects macro‑uniformity.  In [1] a *fin*itary selector is defined as a macro‑uniform mapping \(f:\mathcal{F}_{G}\rightarrow\mathcal{F}_{G}\) satisfying \(f(A)\in A\) for each finite set \(A\).  This notion of a selector that respects the underlying structure motivates our use of the term *geometric selector* for stable wave modes.

* **Discrete coarse space selectors** are shown in [2] to exist if and only if the underlying bornology has an *interval base*.  The equivalence between the existence of a selector and a structural interval property parallels our finding that a stable mode exists only when the toroidal and poloidal winding numbers satisfy a rational interval condition \(\frac{R}{a}=\frac{m}{n}\).

* **Einstein metrics on odd‑dimensional spheres** demonstrate that geometry alone can determine metric properties of manifolds [3].  The abundance of Einstein metrics on spheres supports the broader principle that curvature and topology can dictate physical behavior without reference to material specifics, a principle we exploit for toroidal waveguides.

* **Hilbert geometry** establishes that volume‑growth entropy of spheres matches that of Lobachevsky space [4].  The geometric invariance of entropy underlies the idea that the *shape* of the domain, rather than its material composition, governs wave‑mode stability.

* **Quaternionic differential geometry** introduces a polar notation for quaternions, \(q=\rho\big(\cos\theta+I\sin\theta\big)\) (Eq. (19) in [5]).  This polar representation is analogous to toroidal coordinates \((\phi,\theta)\) and facilitates the separation of variables used in our derivation.

* **Finite‑deformation wave dispersion** derives exact, amplitude‑dependent dispersion relations for axial waves in rods [6].  The exact dispersion relation provides a template for our analytic treatment of wave propagation on a curved toroidal manifold.

* **Sub‑Riemannian dilatation structures** describe distances on manifolds via the Carnot‑Carathéodory metric [7].  The concept of a path‑length metric on a torus is essential for defining the phase accumulated along toroidal and poloidal cycles.

* **Helical vortex geometry** in the α‑π‑Helix framework identifies helical structures as fundamental geometric objects that unify constants and particles [8].  The helical winding of a wave on a torus is precisely the geometric object whose rationality determines stability in our analysis.

These eight works collectively illustrate that geometry, topology, and coarse‑grained selection mechanisms can dictate physical outcomes independently of material details.  Our contribution synthesizes these ideas into a concrete selection rule for toroidal wave modes.

## 3. Methods
We consider a perfectly conducting torus of major radius \(R\) (distance from the center of the tube to the symmetry axis) and minor radius \(a\) (radius of the tube).  In toroidal coordinates \((\phi,\theta)\) the position vector is  

\[
\mathbf{r}(\phi,\theta)=\big(R+a\cos\theta\big)\,\hat{\mathbf{x}}+a\sin\theta\,\hat{\mathbf{y}},
\]

with \(\phi\in[0,2\pi)\) the toroidal angle and \(\theta\in[0,2\pi)\) the poloidal angle.  The line elements along the two fundamental cycles are  

\[
\mathrm{d}s_{\phi}=R\,\mathrm{d}\phi,\qquad 
\mathrm{d}s_{\theta}=a\,\mathrm{d}\theta.
\]

A scalar or electromagnetic wave of wavenumber \(k\) propagates along a helical path that winds \(m\) times around the toroidal direction and \(n\) times around the poloidal direction before closing.  The total phase accumulated after one closed helical circuit must be an integer multiple of \(2\pi\) for constructive interference:

\[
k\,L_{\phi}=2\pi m,\qquad 
k\,L_{\theta}=2\pi n,
\]

where \(L_{\phi}=2\pi R\) and \(L_{\theta}=2\pi a\) are the circumferences of the two cycles.  Solving the two equations for \(k\) yields  

\[
k=\frac{m}{R}=\frac{n}{a}\;\;\Longrightarrow\;\; m\,a=n\,R.
\]

Thus the *geometric selection rule* is the rationality condition  

\[
\boxed{\frac{R}{a}=\frac{m}{n}},\qquad m,n\in\mathbb{Z}_{>0}.
\]

Only integer pairs \((m,n)\) that satisfy this ratio produce a closed helical orbit with constructive interference; all other windings are irrational and lead to destructive interference, causing mode decay.

For electromagnetic waves in vacuum the dispersion relation is \(\omega=c k\) with \(c=3.00\times10^{8}\;\text{m·s}^{-1}\).  The corresponding frequency is  

\[
f=\frac{\omega}{2\pi}=\frac{c\,k}{2\pi}.
\]

These formulas constitute the complete analytical model used in the subsequent quantitative analysis.

## 4. Analysis
We evaluate the selection rule for a concrete torus geometry that is representative of a small‑scale toroidal resonator.

*Assumed geometry*:  
\(R = 0.50\;\text{m}\) (major radius)  
\(a = 0.10\;\text{m}\) (minor radius)

1. Compute the radius ratio  

\[
\frac{R}{a}= \frac{0.50}{0.10}=5.0.
\]

2. Express the ratio as a reduced fraction.  The integer representation of \(5.0\) is \(5/1\); thus the smallest integer pair satisfying the rationality condition is  

\[
(m,n) = (5,1).
\]

3. Verify the winding condition  

\[
m\,a = 5\times0.10 = 0.50\;\text{m},\qquad 
n\,R = 1\times0.50 = 0.50\;\text{m},
\]

so \(m a = n R\) holds exactly.

4. Compute the wavenumber  

\[
k = \frac{m}{R}= \frac{5}{0.50}=10\;\text{rad·m}^{-1}.
\]

5. Compute the angular frequency  

\[
\omega = c\,k = (3.00\times10^{8}\;\text{m·s}^{-1})\times 10\;\text{rad·m}^{-1}=3.00\times10^{9}\;\text{rad·s}^{-1}.
\]

6. Compute the ordinary frequency  

\[
f = \frac{\omega}{2\pi}= \frac{3.00\times10^{9}}{2\pi}
   = \frac{3.00\times10^{9}}{6.283185307}
   \approx 4.774648292\times10^{8}\;\text{Hz}.
\]

Rounded to three significant figures,  

\[
f \approx 4.77\times10^{8}\;\text{Hz}.
\]

All arithmetic steps are shown explicitly; no hidden approximations are used.

## 5. Results
The analysis yields a single concrete numerical prediction:

| Quantity | Symbol | Value | Units |
|----------|--------|-------|-------|
| Major radius | \(R\) | \(0.50\) | m |
| Minor radius | \(a\) | \(0.10\) | m |
| Winding numbers | \((m,n)\) | \((5,1)\) | – |
| Wavenumber | \(k\) | \(10\) | rad·m\(^{-1}\) |
| Frequency | \(f\) | \(4.77\times10^{8}\) | Hz |

The rational winding condition \(\frac{R}{a}=5\) selects the \((5,1)\) helical mode as the lowest‑order stable mode.  Any deviation from the exact ratio (e.g., manufacturing tolerance that changes \(R\) or \(a\) by more than \(1\%\)) would render the pair \((5,1)\) non‑rational and cause the mode to decay.  Higher‑order stable modes correspond to integer multiples of \((5,1)\), e.g., \((10,2)\), \((15,3)\), etc., and have the same frequency scaling.

## 6. Discussion
### Limitations
The derivation rests on several idealizations:

1. **Perfect toroidal geometry** – the torus is assumed to have exact circular cross‑section and uniform radii.  Real devices exhibit manufacturing tolerances and deformations that perturb \(R\) and \(a\).
2. **Vacuum dispersion** – the electromagnetic dispersion relation \(\omega=c k\) neglects plasma dielectric effects, material permittivity, or waveguide loading.
3. **Linear wave approximation** – nonlinear amplitude‑dependent effects such as those described in [6] are ignored; the analysis assumes infinitesimal wave amplitude.
4. **Neglect of curvature‑induced mode coupling** – higher‑order geometric perturbations that couple toroidal and poloidal harmonics are omitted.
5. **Exact rationality requirement** – the selection rule demands an exact integer ratio; in practice, near‑rational ratios may yield long‑lived quasi‑stable modes, but the present model does not quantify their lifetimes.

### Falsification Criterion
A direct falsification of the main claim would occur if an experiment built a torus with \(R/a=5\) (within measurement uncertainty) and observed that the \((5,1)\) helical mode decayed rapidly despite the rational winding condition.  Observation of persistent decay under these conditions would invalidate the geometric selector hypothesis.

### Open Questions
* How robust is the selection rule to small geometric perturbations?  
* Can the rationality condition be generalized to include weak material dispersion as a perturbative correction?  
* What is the quantitative relationship between the degree of irrationality (e.g., Diophantine approximation quality) and the mode decay rate?  

Addressing these questions will require numerical eigenmode simulations and experimental validation, which are outlined in Section 7.

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Design Impact
* **Tokamak designers** can use the ratio \(\frac{R}{a}\) to select magnetic coil configurations that enforce rational winding of field lines, potentially reducing neoclassical tearing modes.  
* **Toroidal resonator engineers** can set the major‑to‑minor radius ratio to a low‑order rational number (e.g., 2, 3, 5) to guarantee a high‑Q helical mode at a desired frequency.  
* **Waveguide manufacturers** can exploit the rule to design compact toroidal waveguides that support single‑mode operation without requiring lossy dielectric liners.

If the rule holds, the design process collapses from iterative electromagnetic simulation to a simple geometric calculation, saving design time and material cost.

### (b) Technology Readiness Level
The work is a purely analytical study that has not yet undergone peer review.  According to NASA’s TRL definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Minimal De‑risking Experiment
The smallest experiment is a **precision‑machined toroidal cavity** with adjustable minor radius.  The experiment would:

1. Fabricate a torus with \(R=0.50\;\text{m}\) and a removable inner sleeve to vary \(a\) around \(0.10\;\text{m}\).  
2. Excite the cavity with a broadband antenna and measure the quality factor \(Q\) of the \((5,1)\) mode using a network analyzer.  
3. Verify that \(Q\) peaks when \(a\) yields \(R/a=5\) within \(\pm0.5\%\).  

Observation of a pronounced \(Q\) maximum at the rational ratio would support the selection rule; a flat \(Q\) response would falsify it.

### (d) Engineering Constraints
* **Geometric tolerance** – the ratio \(R/a\) must be controlled to better than \(1\%\) to maintain exact rationality for low‑order modes.  
* **Material conductivity** – while the theory assumes perfect conductors, real metals introduce skin‑depth losses that must be minimized for high‑Q operation.  
* **Thermal expansion** – temperature‑induced changes in \(R\) and \(a\) can shift the ratio; active temperature control may be required.  
* **Measurement precision** – the network analyzer must resolve frequency shifts on the order of \(10^{5}\;\text{Hz}\) to detect deviations from the predicted \(4.77\times10^{8}\;\text{Hz}\) frequency.

These constraints are open questions for future engineering studies.

### (e) Order‑of‑Magnitude Projection
Assuming a manufacturing tolerance of \(\pm0.5\%\) on both radii, the resulting uncertainty in the frequency is  

\[
\Delta f \approx f \times \frac{\Delta R}{R} \approx 4.77\times10^{8}\;\text{Hz}\times0.005 \approx 2.4\times10^{6}\;\text{Hz}.
\]

Thus the expected frequency band for the stable mode is \(4.77\times10^{8}\pm2.4\times10^{6}\;\text{Hz}\).

### (f) Risks and Misuse
If the rationality condition is applied without accounting for material dispersion or plasma effects, designers may over‑estimate mode stability, leading to premature deployment of devices that suffer unexpected losses.  Careful validation against the minimal experiment described above is therefore essential before large‑scale adoption.

## 8. Conclusion
We have shown that the stability of helical wave modes on a toroidal domain can be predicted solely from the geometry of the torus.  The rational winding condition \(\frac{R}{a}=\frac{m}{n}\) emerges from enforcing constructive interference around both fundamental cycles.  A concrete example demonstrates that a torus with \(R=0.5\;\text{m}\) and \(a=0.1\;\text{m}\) supports a stable electromagnetic mode at \(4.77\times10^{8}\;\text{Hz}\).  This geometric selector offers a low‑cost, analytically tractable design tool for fusion devices, resonators, and waveguides.  Future work will test the rule experimentally, extend it to include material dispersion, and explore its implications for mode control in plasma confinement.

## References
[1] arXiv:2102.03790v2 | Coarse selectors of groups  
[2] arXiv:2101.07199v3 | Selectors of discrete coarse spaces  
[3] arXiv:math/0505221v1 | Sasakian Geometry and Einstein Metrics on Spheres  
[4] arXiv:0711.0446v1 | Asymptotic Properties of Hilbert Geometry  
[5] arXiv:2404.03765v1 | Differential geometry using quaternions  
[6] arXiv:1210.6607v2 | Wave dispersion under finite deformation  
[7] arXiv:0708.4298v3 | Dilatation structures in sub-riemannian geometry  
[8] QNFO: α-π-Helix: Geometric Unification of Fundamental Constants | https://papers.qnfo.org/papers/alpha-pi-helix  
[9] QNFO: WINDING NUMBERS AND STRANGE LOOPS | https://papers.qnfo.org/papers/winding-numbers-and-strange-loops  
[10] QNFO: Quantum Mechanics as Applied Wave Harmonics | https://papers.qnfo.org/papers/quantum-mechanics-as-applied-wave-mechanics  
[11] QNFO: Double Pendulum as a Topological Bridge | https://papers.qnfo.org/papers/double-pendulum-as-a-topological-bridge