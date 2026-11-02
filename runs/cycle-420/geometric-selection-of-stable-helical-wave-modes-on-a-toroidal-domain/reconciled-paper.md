# Geometric Selection of Stable Helical Wave Modes on a Toroidal Domain

## Abstract
Tokamak magnetic field lines, toroidal microwave resonators, and toroidal waveguides all suffer from mode instability that forces costly redesigns or limits operational performance. Existing stability criteria rely on material parameters, plasma profiles, or detailed numerical eigenmode simulations, and no purely geometric predictor of which helical modes persist has been established. We derive a quantization condition for scalar and electromagnetic waves confined to a toroidal boundary by enforcing constructive interference separately around the toroidal (major) and poloidal (minor) cycles. The condition reduces to a rational winding requirement, $R/a = m/n$, where $R$ and $a$ are the major and minor radii and $(m,n)$ are positive integers. For an assumed torus with $R = 0.50\;\text{m}$ and $a = 0.10\;\text{m}$ the smallest admissible pair is $(m,n) = (5,1)$, giving wavenumber $k = 10\;\text{rad·m}^{-1}$ and electromagnetic frequency $f \approx 4.77 \times 10^{8}\;\text{Hz}$. With an assumed manufacturing tolerance of $\pm 0.5\%$ on both radii, the projected frequency uncertainty is $\Delta f \approx 2.4 \times 10^{6}\;\text{Hz}$. If validated, the rule lets designers of fusion devices, resonators, and waveguides guarantee mode stability from geometry alone, before any material-specific simulation or prototype is committed.

## 1. Introduction
Instabilities of helical wave modes in toroidal configurations limit the performance of magnetic confinement fusion devices, degrade the quality factor of toroidal microwave resonators, and cause unwanted attenuation in toroidal waveguides. In a tokamak, uncontrolled drift of field-line resonances leads to rapid energy loss, requiring expensive magnetic-coil redesign and reducing plasma confinement time. In toroidal resonators, mode mixing forces the use of exotic materials or active feedback, raising fabrication cost and complexity. The design decision that would remove these burdens is a geometry-only predictor that tells an engineer, before any simulation or prototype, whether a given toroidal shape supports a stable helical mode.

Current practice evaluates stability through magnetohydrodynamic eigenmode analysis, finite-element electromagnetic solvers, or empirical scaling laws that depend on plasma pressure, wall conductivity, and detailed geometry. These approaches require extensive computation and obscure the role of the torus's intrinsic shape. A selector that depends only on the radii $R$ and $a$ and the integer winding numbers $(m,n)$ could be evaluated on paper, collapsing one stage of the design loop.

We therefore ask: does toroidal geometry alone dictate which helical wave modes are stable? We answer by deriving a selection rule from constructive interference around the two fundamental cycles of the torus, and we state the convention adopted where alternative formulations exist.

**Contributions.**
1. Derivation of a rational-winding quantization condition, $R/a = m/n$, for toroidal wave modes, obtained by enforcing constructive interference on each fundamental cycle (Section 3).
2. Explicit arithmetic demonstration that a torus with $R = 0.50\;\text{m}$ and $a = 0.10\;\text{m}$ satisfies the condition for $(m,n) = (5,1)$ and supports a mode at $k = 10\;\text{rad·m}^{-1}$, i.e. $f \approx 4.77 \times 10^{8}\;\text{Hz}$ (Section 4).
3. A projected frequency tolerance band, $4.77 \times 10^{8} \pm 2.4 \times 10^{6}\;\text{Hz}$, under an assumed $\pm 0.5\%$ radius tolerance (Section 4 and Section 7e).
4. A falsification criterion and a limitations analysis for the selector hypothesis (Section 6).
5. A practical pathway — users, readiness level, minimal de-risking experiment, and binding constraints — for tokamak, resonator, and waveguide design (Section 7).

The selection rule is independent of material specifics, so it may also bear on any system in which waves propagate on a doubly periodic closed surface, such as acoustic cavities with toroidal chambers or optical structures with toroidal symmetry, insofar as the same two-cycle phase-closure argument applies.

## 2. Background and Related Work
The present work draws on several strands of geometric and wave-theoretic literature, each contributing a specific concept that the derivation uses or extends.

Coarse selectors provide a formalism for choosing elements from finite subsets in a way that respects macro-uniformity. In [1] a finitary selector is defined as a macro-uniform mapping $f:\mathcal{F}_{G}\rightarrow\mathcal{F}_{G}$ satisfying $f(A)\in A$ for each finite set $A$. This notion of a structure-respecting choice motivates our use of the term *geometric selector* for stable wave modes: the torus admits only those windings that satisfy the closure condition.

Selectors of discrete coarse spaces are treated in [2], which shows that a selector exists if and only if the underlying bornology has an interval base. The equivalence between selector existence and a structural interval property parallels our finding that a stable mode exists only when the toroidal and poloidal winding numbers satisfy a rational ratio condition $R/a = m/n$.

Einstein metrics on odd-dimensional spheres are constructed in [3] using Sasakian geometry, demonstrating that topology and curvature conditions alone can guarantee the existence of special metric structures on a manifold. We use the same principle — that geometry can dictate admissible structures without reference to material composition — for toroidal wave modes.

Hilbert geometry is analyzed in [4], which establishes that the volume-growth entropy of spheres in a Hilbert geometry matches that of Lobachevsky space. This invariance of an analytic quantity under a purely geometric condition supports the idea that the shape of a domain, rather than its material composition, can govern wave behavior; our quantization condition is the toroidal analogue of such a geometric invariant.

Quaternionic differential geometry is developed in [5], which introduces a polar notation for quaternions, $q=\rho(\cos\theta+I\sin\theta)$, separating a magnitude from angular parameters. This separation of a radial scale from angular variables is analogous to the split between the radii $(R,a)$ and the angles $(\phi,\theta)$ in toroidal coordinates, and it facilitates the variable separation used in our derivation.

Finite-deformation wave dispersion is treated in [6], which derives exact, amplitude-dependent dispersion relations for axial waves in rods and beams under finite strain. That work shows how geometric deformation parameters enter a wave dispersion relation exactly; our analysis adopts the same strategy, treating the torus radii as the geometric parameters that enter the phase-accumulation conditions.

Sub-Riemannian dilatation structures are studied in [7], which describes distances on such manifolds via the Carnot–Carathéodory metric and analyzes how distances scale under anisotropic transformations. A path-length metric on the torus is what allows the phase accumulated along the toroidal and poloidal cycles to be defined; the anisotropic scaling between the two cycle directions is the source of the rational-ratio selection rule.

Helical geometry as a unifying physical structure is argued in [8], the α-π-Helix framework, which presents a helical-torus model for fundamental constants and treats helical winding as underlying quantisation in physics. That work supplies a conceptual precedent for treating helical winding numbers as selectors of stable configurations, which is precisely the role the winding pair $(m,n)$ plays in our condition.

These eight works collectively illustrate that geometry, topology, and coarse-grained selection mechanisms can dictate physical outcomes independently of material details. Our contribution synthesizes them into a concrete, falsifiable selection rule for toroidal wave modes.

## 3. Methods
We consider a perfectly conducting torus of major radius $R$ (distance from the center of the tube to the symmetry axis) and minor radius $a$ (radius of the tube). In toroidal coordinates $(\phi,\theta)$ the surface is parametrised by

$$
\mathbf{r}(\phi,\theta)=\big(R+a\cos\theta\big)\,\hat{\mathbf{x}}+a\sin\theta\,\hat{\mathbf{z}},
$$

with $\phi\in[0,2\pi)$ the toroidal angle and $\theta\in[0,2\pi)$ the poloidal angle. The line elements along the two fundamental cycles are

$$
\mathrm{d}s_{\phi}=R\,\mathrm{d}\phi,\qquad
\mathrm{d}s_{\theta}=a\,\mathrm{d}\theta,
$$

so the circumferences of the two cycles are $L_{\phi}=2\pi R$ and $L_{\theta}=2\pi a$.

A scalar or electromagnetic wave of wavenumber $k$ propagates along a helical path that winds $m$ times around the toroidal direction and $n$ times around the poloidal direction before closing on itself. For the orbit to close and for the wave to interfere constructively with itself after one circuit, the phase accumulated on each fundamental cycle must be an integer multiple of $2\pi$:

$$
k\,L_{\phi}=2\pi m,\qquad
k\,L_{\theta}=2\pi n.
$$

Solving both equations for $k$ and equating the results yields

$$
k=\frac{m}{R}=\frac{n}{a}
\;\;\Longrightarrow\;\;
m\,a=n\,R.
$$

Thus the **geometric selection rule** is the rationality condition

$$
\boxed{\frac{R}{a}=\frac{m}{n}},\qquad m,n\in\mathbb{Z}_{>0}.
$$

Only integer pairs $(m,n)$ satisfying this ratio produce a closed helical orbit with constructive interference on both cycles; windings that do not satisfy it cannot close with a single wavenumber and lead to destructive interference, causing mode decay.

**Convention adopted.** An alternative single-phase formulation, in which the phases of the two cycles are added and the combined phase $2\pi(mR+na)/\lambda$ is required to be an integer multiple of $2\pi$, was also considered. We take the two-cycle condition above as the governing convention, under the assumption that constructive interference must hold independently on each fundamental cycle for a mode to be self-consistent; the combined-phase convention admits wavelengths that violate the per-cycle closure requirement and is therefore the weaker condition. Under the alternative convention, a torus with $R=1.00\;\text{m}$ and $a=0.50\;\text{m}$ for the pair $(m,n)=(1,1)$ and harmonic index $k=1$ yields a minimal wavelength $\lambda_{11}=2\pi(1.00+0.50)\;\text{m}\approx 9.42478\;\text{m}$; we report this value only as the output of the alternative convention and do not use it in the results below.

For electromagnetic waves in vacuum the dispersion relation is $\omega=c\,k$ with $c=3.00\times10^{8}\;\text{m·s}^{-1}$, and the ordinary frequency is

$$
f=\frac{\omega}{2\pi}=\frac{c\,k}{2\pi}.
$$

**Assumptions.**
- A1: The torus surface is perfectly conducting (perfectly reflecting for scalar waves), with exact circular cross-section and uniform radii.
- A2: Propagation is lossless; attenuation and plasma or dielectric loading are neglected, so the vacuum dispersion relation applies.
- A3: The wave amplitude is infinitesimal (linear approximation); nonlinear amplitude-dependent dispersion is ignored.
- A4: The winding numbers $(m,n)$ are exact integers; near-rational ratios are not assigned lifetimes in this model.

## 4. Analysis
We evaluate the selection rule for a concrete torus geometry representative of a small-scale toroidal resonator. All input numbers are assumptions of this paper, stated here: $R = 0.50\;\text{m}$, $a = 0.10\;\text{m}$, $c = 3.00\times10^{8}\;\text{m·s}^{-1}$.

1. Compute the radius ratio:
$$
\frac{R}{a}= \frac{0.50}{0.10}=5.0.
$$

2. Express the ratio as a reduced fraction. The integer representation of $5.0$ is $5/1$; the smallest positive integer pair satisfying the rationality condition is therefore
$$
(m,n) = (5,1).
$$

3. Verify the winding condition $m\,a = n\,R$:
$$
m\,a = 5\times0.10 = 0.50\;\text{m},\qquad
n\,R = 1\times0.50 = 0.50\;\text{m},
$$
so $m\,a = n\,R$ holds exactly.

4. Compute the wavenumber from the toroidal cycle:
$$
k = \frac{m}{R}= \frac{5}{0.50}=10\;\text{rad·m}^{-1}.
$$
Cross-check from the poloidal cycle:
$$
k = \frac{n}{a}= \frac{1}{0.10}=10\;\text{rad·m}^{-1},
$$
which agrees, as it must when $m\,a=n\,R$.

5. Compute the angular frequency:
$$
\omega = c\,k = \big(3.00\times10^{8}\;\text{m·s}^{-1}\big)\times 10\;\text{rad·m}^{-1}=3.00\times10^{9}\;\text{rad·s}^{-1}.
$$

6. Compute the ordinary frequency:
$$
f = \frac{\omega}{2\pi}= \frac{3.00\times10^{9}}{2\pi}
   = \frac{3.00\times10^{9}}{6.283185307}
   \approx 4.774648292\times10^{8}\;\text{Hz}.
$$

Rounded to three significant figures,
$$
f \approx 4.77\times10^{8}\;\text{Hz}.
$$

7. Projected tolerance band (projection). Assuming a manufacturing tolerance of $\pm0.5\%$ on both radii, the relative uncertainty in $k = m/R$ is $\Delta R/R = 0.005$, so
$$
\Delta f \approx f \times \frac{\Delta R}{R} \approx 4.77\times10^{8}\;\text{Hz}\times0.005 \approx 2.4\times10^{6}\;\text{Hz}.
$$
The expected frequency band for the stable mode is $4.77\times10^{8}\pm2.4\times10^{6}\;\text{Hz}$. This projection assumes the tolerance is the dominant error source and that A1–A4 hold.

All arithmetic steps are shown explicitly; no hidden approximations are used.

## 5. Results
The analysis yields the following concrete numerical outputs, all computed in Section 4:

| Quantity | Symbol | Value | Units |
|----------|--------|-------|-------|
| Major radius (assumed) | $R$ | $0.50$ | m |
| Minor radius (assumed) | $a$ | $0.10$ | m |
| Radius ratio | $R/a$ | $5.0$ | – |
| Winding numbers | $(m,n)$ | $(5,1)$ | – |
| Wavenumber | $k$ | $10$ | rad·m$^{-1}$ |
| Angular frequency | $\omega$ | $3.00\times10^{9}$ | rad·s$^{-1}$ |
| Frequency | $f$ | $4.77\times10^{8}$ | Hz |
| Projected frequency uncertainty (assumed $\pm0.5\%$ tolerance) | $\Delta f$ | $2.4\times10^{6}$ | Hz |

The rational winding condition $R/a = 5$ selects the $(5,1)$ helical mode as the lowest-order stable mode. Higher-order stable modes correspond to integer multiples of $(5,1)$ — $(10,2)$, $(15,3)$, and so on — and satisfy the same wavenumber $k = 10\;\text{rad·m}^{-1}$, since $k = m/R = n/a$ is unchanged when both integers are scaled by the same factor. Any deviation from the exact ratio (for example, a manufacturing tolerance that changes $R/a$ beyond its assumed $\pm0.5\%$ band) would render the pair $(5,1)$ inadmissible under the exact condition and, in the idealised model, cause the mode to decay; the model does not quantify the lifetime of near-rational modes (Assumption A4).

## 6. Discussion
### Limitations
The derivation rests on the following idealizations, each with its sensitivity:

1. **Perfect toroidal geometry (A1)** — the torus is assumed to have an exact circular cross-section and uniform radii. Real devices exhibit manufacturing tolerances and deformations that perturb $R$ and $a$; the selection rule is sensitive to these at the level of the tolerance band computed in Section 4 ($\pm0.5\%$ assumed).
2. **Vacuum dispersion (A2)** — the relation $\omega = c\,k$ neglects plasma dielectric effects, material permittivity, and waveguide loading. In a plasma or loaded cavity the dispersion relation changes, and the numerical frequency prediction shifts even if the rationality condition on the winding survives.
3. **Linear wave approximation (A3)** — nonlinear amplitude-dependent effects of the kind treated exactly for rods in [6] are ignored; the analysis assumes infinitesimal wave amplitude.
4. **Exact rationality requirement (A4)** — the selection rule demands an exact integer ratio. In practice, near-rational ratios may yield long-lived quasi-stable modes, but the present model does not quantify their lifetimes or their dependence on the quality of the Diophantine approximation.
5. **Neglect of curvature-induced mode coupling** — higher-order geometric perturbations that couple toroidal and poloidal harmonics are omitted; such coupling can shift effective phase accumulation beyond the two-cycle model.
6. **Convention dependence** — the numerical outputs follow from the two-cycle convention adopted in Section 3. Under the alternative combined-phase convention the admissible wavelength set differs (the $\lambda_{11}\approx 9.42478\;\text{m}$ example in Section 3); the qualitative claim that rationality selects stable modes is common to both conventions, but the specific frequencies are not.

### Falsification Criterion
A direct falsification of the main claim would occur if an experiment built a torus with $R/a = 5$ within measurement uncertainty and observed that the $(5,1)$ helical mode decayed rapidly despite the rational winding condition. Conversely, observation of a pronounced, persistent resonance at the predicted frequency $4.77\times10^{8}\;\text{Hz}$ (within the projected $\pm2.4\times10^{6}\;\text{Hz}$ band) at exactly this ratio, and its absence at nearby irrational ratios, would support the selector. A single well-characterised counterexample — a stable, long-lived mode at a clearly irrational winding ratio under conditions satisfying A1–A3 — would invalidate the geometric selector hypothesis.

### Open Questions
- How robust is the selection rule to small geometric perturbations, and what decay rate follows from a given departure from exact rationality?
- Can the rationality condition be generalised to include weak material dispersion as a perturbative correction to A2?
- What is the quantitative relationship between the degree of irrationality (for example, Diophantine approximation quality) and the mode decay rate?
- Does the two-cycle convention or the combined-phase convention better describe real cavities, and can the distinction be resolved by the minimal experiment of Section 7?

Addressing these questions requires numerical eigenmode simulations and experimental validation, which are outlined in Section 7.

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Design Impact
- **Tokamak designers** can use the ratio $R/a$ to select magnetic-coil configurations that enforce rational winding of field lines, potentially reducing the burden of neoclassical tearing-mode control; if the rule holds, the design process gains a geometry-only screening step before MHD eigenmode scans.
- **Toroidal resonator engineers** can set the major-to-minor radius ratio to a low-order rational number (for example 2, 3, or 5) to target a high-$Q$ helical mode at a desired frequency, replacing iterative electromagnetic simulation with a geometric calculation at the concept stage.
- **Waveguide manufacturers** can exploit the rule to design compact toroidal waveguides that support single-mode operation without lossy dielectric liners.

### (b) Technology Readiness Level
The work is a purely analytical study that has not undergone peer review. According to the NASA TRL definitions it resides at **TRL 2** (technology concept formulation): the basic principles are stated and the concept has been formulated analytically, but no experimental proof of concept exists. Analytical work of this kind cannot exceed TRL 3, and no hardware, manufacturing, or deployment readiness is claimed.

### (c) Minimal De-risking Experiment
The smallest experiment is a precision-machined toroidal cavity with adjustable minor radius. The study would:

1. Fabricate a torus with $R = 0.50\;\text{m}$ and a removable inner sleeve to vary $a$ around $0.10\;\text{m}$.
2. Excite the cavity with a broadband antenna and measure the quality factor $Q$ of the candidate $(5,1)$ mode with a network analyzer as $a$ is varied.
3. Test whether $Q$ peaks when $a$ yields $R/a = 5$ within $\pm0.5\%$, and whether the peak lies near $4.77\times10^{8}\;\text{Hz}$ within the projected $\pm2.4\times10^{6}\;\text{Hz}$ band.

A pronounced $Q$ maximum at the rational ratio would support the selection rule; a flat $Q$ response across ratios, or a resonance peak that does not track the rational ratio, would falsify it.

### (d) Engineering Constraints
- **Geometric tolerance** — the ratio $R/a$ must be controlled to better than $1\%$ to maintain exact rationality for low-order modes; the $\pm0.5\%$ assumption of Section 4 sets the frequency-resolution requirement.
- **Material conductivity** — the theory assumes perfect conductors; real metals introduce skin-depth losses that must be minimised for high-$Q$ operation.
- **Thermal expansion** — temperature-induced changes in $R$ and $a$ can shift the ratio; active temperature control may be required.
- **Measurement precision** — the network analyzer must resolve frequency shifts on the order of $10^{5}\;\text{Hz}$ to detect deviations from the predicted $4.77\times10^{8}\;\text{Hz}$ frequency, well inside the projected $\pm2.4\times10^{6}\;\text{Hz}$ tolerance band.

Whether these constraints bind in practice, and which binds first for a given device class, is an open question for future engineering studies; the present analysis does not rank them.

### (e) Order-of-Magnitude Projection
The only quantitative projection carried from Section 4 is the frequency tolerance band: with an assumed $\pm0.5\%$ tolerance on both radii, $\Delta f \approx 2.4\times10^{6}\;\text{Hz}$ around $f \approx 4.77\times10^{8}\;\text{Hz}$. This projection assumes the tolerance is the dominant error source, that A1–A4 hold, and that no additional dispersion or loading shifts the frequency. No cost, market, or performance figures beyond this band are derived, and none are claimed.

### (f) Risks and Misuse
If the rationality condition is applied without accounting for material dispersion or plasma effects, designers may over-estimate mode stability, leading to premature commitment of designs that suffer unexpected losses. Validation against the minimal experiment above is therefore essential before any large-scale adoption; the selector is a screening rule at the concept stage, not a substitute for full-wave or MHD verification.

## 8. Conclusion
We have shown that the stability of helical wave modes on a toroidal domain can be predicted from geometry alone under the model's assumptions. Enforcing constructive interference on each fundamental cycle yields the rational winding condition $R/a = m/n$, and a concrete example demonstrates that a torus with $R = 0.50\;\text{m}$ and $a = 0.10\;\text{m}$ satisfies it for $(m,n) = (5,1)$, giving $k = 10\;\text{rad·m}^{-1}$ and $f \approx 4.77\times10^{8}\;\text{Hz}$, with a projected tolerance band of $\pm2.4\times10^{6}\;\text{Hz}$ under an assumed $\pm0.5\%$ radius tolerance. This geometric selector offers a low-cost, analytically tractable screening tool for fusion devices, resonators, and waveguides, at TRL 2. Its limitations — perfect geometry, vacuum dispersion, linearity, exact rationality, and convention dependence — are stated explicitly, and a tabletop cavity experiment with a defined falsification criterion provides a clear path from theory to practice.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.44.6-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 10 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Coarse selectors of groups. arXiv:2102.03790v2. https://arxiv.org/abs/2102.03790v2
[2] Selectors of discrete coarse spaces. arXiv:2101.07199v3. https://arxiv.org/abs/2101.07199v3
[3] Sasakian Geometry and Einstein Metrics on Spheres. arXiv:math/0505221v1. https://arxiv.org/abs/math/0505221v1
[4] Asymptotic Properties of Hilbert Geometry. arXiv:0711.0446v1. https://arxiv.org/abs/0711.0446v1
[5] Differential geometry using quaternions. arXiv:2404.03765v1. https://arxiv.org/abs/2404.03765v1
[6] Wave dispersion under finite deformation. arXiv:1210.6607v2. https://arxiv.org/abs/1210.6607v2
[7] Dilatation structures in sub-riemannian geometry. arXiv:0708.4298v3. https://arxiv.org/abs/0708.4298v3
[8] https://papers.qnfo.org/papers/alpha-pi-helix. QNFO: α-π-Helix: Geometric Unification of Fundamental Constants.
