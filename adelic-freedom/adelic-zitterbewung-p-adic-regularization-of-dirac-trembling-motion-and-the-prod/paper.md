# Adelic Zitterbewegung: p-Adic Regularization of Dirac Trembling Motion and the Product-Formula Cancellation at Macroscopic Scales

## Abstract

Zitterbewegung (ZBW) — the trembling motion of Dirac wave packets at the Compton scale — is conventionally treated as a purely Archimedean interference effect between the positive- and negative-energy branches of the free Dirac equation. Missing from the standard account is any mechanism by which the non-Archimedean completions of the rationals could enter the dynamics, and any quantitative statement of when such contributions would or would not matter. We propose a conjectural framework in which the free Dirac equation is formulated over the adele ring $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$, so that the trembling motion acquires simultaneous oscillatory components in the real sector and in every $p$-adic sector, and we define a sector-resolved velocity expectation together with a cancellation mechanism in which the $p$-adic contributions to macroscopic motion are suppressed by the adele product formula $|x|_\infty \prod_p |x|_p = 1$. With fully shown arithmetic we compute the electron ZBW angular frequency $\omega_\infty = 1.5521 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ (period $4.0482 \times 10^{-21}\,\mathrm{s}$), the Compton wavelength $\lambda_C = 3.8632 \times 10^{-13}\,\mathrm{m}$, the Planck length $\ell_P = 1.6166 \times 10^{-35}\,\mathrm{m}$, and the scale hierarchy $\lambda_C/\ell_P = 2.389 \times 10^{22}$. Under the conjectured mechanism the cross-sector interference amplitude scales as $\lambda_C/\ell$: at $\ell = 1\,\mathrm{m}$ this is $3.863 \times 10^{-13}$ in amplitude ($1.492 \times 10^{-25}$ in intensity-like terms), while at the Planck length the non-Archimedean sector dominates by a factor $\approx 2.39 \times 10^{22}$. We verify the product formula exactly for rational test values, state model-projected sector frequency shifts under an explicit dispersion assumption, and specify a simulation program on $\mathbb{Q}_p$ using the Vladimirov operator. All quantitative results are computed or explicitly labeled projections; no simulations or measurements are reported. The framework makes the adelic regularization of Dirac dynamics precise enough to fail.

## 1. Introduction

A localized relativistic electron does not move smoothly. In the Dirac equation, the velocity operators do not commute with the free Hamiltonian, so interference between the positive- and negative-energy components of any wave packet produces a rapid periodic oscillation of the velocity and position at the Compton scale, with angular frequency $\omega = 2mc^2/\hbar$ and amplitude of order the Compton wavelength [3], [7]. This is Zitterbewegung (ZBW, German for "trembling motion"). Who faces this phenomenon today? Not vacuum electron physicists: the ZB of a free relativistic electron in a vacuum "is probably not directly observable for year to come and one has to recourse to its simulations" [3]. The working community is instead the condensed-matter and quantum-emulation community: ZB of charge carriers has been established as "a real and universal phenomenon" in semiconductors, monolayer and bilayer graphene, and carbon nanotubes [3], with frequencies set by band gaps and amplitudes reaching tens of nanometers in narrow-gap semiconductors [7]. What blocks progress is interpretive: ZBW is treated as an interference artifact of the real-number formulation, with no principled statement of what, if anything, the arithmetic of the underlying number field contributes to the dynamics. If a result held that tied the observable trembling motion to the arithmetic of $\mathbb{Q}$ across all of its completions, it would change what ZBW experiments are testing — from probing band structure alone to probing a putative adelic structure of quantum dynamics — and it would supply a concrete regularization mechanism at short distances, potentially softening the singular short-distance behavior of the Dirac propagator and informing quantum-gravity models that require a minimal length.

Two existing threads make such a result conceivable. First, p-adic mathematical physics arose precisely from efforts to find a non-Archimedean description of spacetime and string dynamics at the Planck scale, and its main achievement is a working formulation of p-adic and adelic quantum mechanics with complex-valued wave functions of p-adic and adelic arguments [1]; path integrals for such systems have been evaluated analytically for quadratic Lagrangians in ordinary, p-adic, and adelic settings, with a formalism that is invariant under interchange of the number field [5]. Second, a speculative variant conjectures that ZBW is mixing between the Archimedean and 2-adic completions of $\mathbb{Q}$ via a two-channel effective Hamiltonian with beat frequency $\omega_{\mathrm{ZBW}} = 2E/\hbar$ under a calibration condition $|\Delta| \sim E$; this variant is explicitly labeled a hypothesis, since no such Hamiltonian is constructed and no beat frequency is derived in the present paper, whose working framework is all-sector.

This paper joins the threads with a definite quantitative claim: **the trembling motion of a free Dirac particle is conjecturally an adelic phenomenon, and the adele product formula controls its scale dependence**. We posit that the velocity expectation decomposes sector by sector over $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$: one Archimedean contribution and one per prime $p$. We then conjecture that the cross-sector interference amplitude in the observable position is proportional to the product of $p$-adic norms of the dimensionless scale ratio $r = \ell/\lambda_C$, which by the product formula equals $\lambda_C/\ell$. The consequences are computed exactly: suppression by $3.863 \times 10^{-13}$ at laboratory scales, dominance by $2.389 \times 10^{22}$ at the Planck scale, and a conjectured crossover near optical wavelengths. The work is deliberately positioned as a conjectural framework with fully explicit derivations; every number is computed from stated inputs with shown arithmetic, and the simulation program that could falsify the conjecture is specified but not executed.

Contributions:

- The electron ZBW frequency $\omega_\infty = 1.5521 \times 10^{21}\,\mathrm{rad\,s^{-1}}$, its period $T = 4.0482 \times 10^{-21}\,\mathrm{s}$, the Compton wavelength $\lambda_C = 3.8632 \times 10^{-13}\,\mathrm{m}$, and the Planck length $\ell_P = 1.6166 \times 10^{-35}\,\mathrm{m}$, each derived with fully shown arithmetic (Section 4, Steps 1–4).
- An exact verification of the adele product formula for the rational test values $x = 6, 10, 12$, establishing that the cancellation mechanism is algebraic rather than approximate (Section 4, Step 5).
- The conjectured suppression law $A_{\mathrm{int}}/A_0 = \lambda_C/\ell$, evaluated at $\ell = 1\,\mathrm{m}$ ($3.863 \times 10^{-13}$ in amplitude, $1.492 \times 10^{-25}$ in intensity-like terms) and at $\ell = \ell_P$ ($2.389 \times 10^{22}$), with the crossover scale $386.3\,\mathrm{nm}$ for a $10^{-6}$ threshold derived as a labeled projection (Section 4, Steps 6–8).
- Model-projected sector frequency shifts under the explicit dispersion assumption $\omega_p = \omega_\infty |r|_p$, giving $f_2 = 1.2351 \times 10^{20}\,\mathrm{Hz}$ and $f_5 = 4.9404 \times 10^{19}\,\mathrm{Hz}$ for $r = 10$, alongside a distinguishable quadrature variant (Section 4, Step 9).
- A falsifiable simulation program on $\mathbb{Q}_p$ using the Vladimirov operator and p-adic gamma matrices, specified as future work (Section 3.5), with the practical pathway, readiness assessment, and next concrete test (Section 7).

## 2. Background and Related Work

**p-Adic and adelic quantum mechanics.** The foundational review [1] explains that p-adic mathematical physics emerged in 1987 from efforts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and that among its main achievements is p-adic and adelic quantum mechanics. Its survey of formulations is directly relevant to our construction: quantum mechanics on $p$-adic spaces admits two main approaches, with $p$-adic-valued wave functions (introduced by Vladimirov and Volovich and developed by Khrennikov) and with complex-valued wave functions, and the review states that the complex-valued approach "is more suitable for connection with ordinary quantum mechanics" [1]. We adopt exactly that choice: our sector wave functions $\Psi_p$ are $\mathbb{C}$-valued, so that the standard Hilbert-space machinery and the interference mechanism of ZBW carry over sector by sector. The review also records that with complex-valued wave functions one cannot construct a direct analogue of the Schrödinger equation with a $p$-adic Heisenberg algebra [1], which is one reason our sector dynamics is postulated rather than derived.

**Adelic path integrals.** Reference [5] considers Feynman path integrals in ordinary, p-adic and adelic quantum mechanics, evaluates the probability amplitudes $\mathcal{K}(x'',t'';x',t')$ for two-dimensional systems with quadratic Lagrangians analytically, generalizes the expressions to any finite-dimensional spaces, and presents the formulas in a form invariant under interchange of the relevant data. Its concluding section states that "the formalism of ordinary and $p$-adic path integrals can be regarded as the same at different levels of evaluation, and the obtained results have the same form" [5]. For our program this matters twice over: any regularized adelic path integral we propose can be checked against the exactly solvable quadratic cases of [5], and the number-field invariance that [5] demonstrates at the level of path integrals is the property our conjecture extends to the dynamical level of ZBW.

**Adelic cosmology and p-adic worlds.** Reference [2] reviews p-adic and adelic cosmology, covering p-adic and adelic aspects of gravity, classical cosmology, quantum mechanics, quantum cosmology and the wave function of the universe, and introduces "p-adic worlds" made of p-adic matter distinct from the real world of ordinary matter, with real and p-adic worlds making up the universe as a whole. Its definition of an adele as an infinite sequence $x = (x_\infty, x_2, \ldots, x_p, \ldots)$ with $x_\infty \in \mathbb{R}$, $x_p \in \mathbb{Q}_p$, and $x_p \in \mathbb{Z}_p$ for all but finitely many primes [2] is the precise object over which we formulate the sector-resolved Dirac equation. The review also reports a striking structural fact: a nonsingular form of odd degree $r$ represents all $p$-adic numbers nontrivially when the number of variables satisfies $n \geq D = r^2 + 1$, giving $D = 10$ for $r = 3$ and $D = 26$ for $r = 5$, dimensions that coincide with the critical dimensions of superstring and bosonic string theory [2] — evidence that adelic arithmetic constraints already reach into established physics.

**Zitterbewegung: origins.** Reference [4] records that around 1930 both Gregory Breit and Erwin Schrödinger showed that the eigenvalues of the velocity of a particle described by wave-packet solutions to the Dirac equation are simply $\pm c$, and that this led Schrödinger to coin the term Zitterbewegung, in which particles of matter zig-zag back and forth at the speed of light. Beyond the founding observation, [4] develops a statistical treatment in $1+1$ dimensions in which the particle moves left or right at speed $c$ with probabilities $\Pr(R) = \frac{1}{2}(1+v)$ and $\Pr(L) = \frac{1}{2}(1-v)$, and shows that macroscopic motion is consistent with special relativity through the velocity addition rule, suggesting that motion itself can be regarded as a statistical-mechanical phenomenon [4]. This statistical framing is congenial to our multi-sector extension: if ZBW admits a probabilistic decomposition, a decomposition into number-field sectors is a natural further refinement.

**Zitterbewegung in condensed matter.** Reference [3] reviews ZBW of electrons in semiconductors, presents a brief history beginning with Schrödinger's 1930 observation that the velocity operators do not commute with the free-electron Hamiltonian, considers trembling motion in semirelativistic and spin systems, and elaborates ZB of charge carriers in monolayer and bilayer graphene and carbon nanotubes. Its conclusion states that ZB is "a real and universal phenomenon" whose universal background is "an interference of states belonging to positive and negative energies," while the vacuum ZB of Schrödinger is probably not directly observable for years to come, so that one must resort to simulations, for which a proof of principle has been carried out [3]. Reference [7] reviews the theory of ZB of charge carriers in narrow-gap materials — nearly free electrons in a periodic potential, InSb-type semiconductors, bilayer and monolayer graphene, carbon nanotubes — and gives the quantitative anchors we use: the vacuum ZB frequency is about $\omega = 2m_0 c^2/\hbar$ with amplitude about the Compton wavelength $\lambda_c = \hbar/m_0 c \approx 3.86 \times 10^{-3}\,\text{Å}$ [7], and in solids the ZB frequency obeys $\hbar\omega_Z \approx \Delta\mathcal{E}$ with amplitude $\lambda_Z \propto 1/\Delta\mathcal{E}$, reaching tens of nanometers in narrow-gap semiconductors [7]. Together [3] and [7] establish that ZBW is a robust, tunable wave-packet phenomenon — precisely the regime our adelic modification targets — and supply the experimental context against which any adelic correction to the ZBW frequency would have to be tested, with the caveat that in condensed matter the effective parameters $u \approx 10^8\,\mathrm{cm/s}$ and the band gap replace $c$ and $m_0$, rescaling the hierarchy we compute in Section 4.

**p-Adic statistical structure.** Reference [6] studies the three-state p-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of p-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction, also solving the associated uniqueness problem; its conclusion emphasizes that "a phase transition depends only on a value of $p$," results totally different from the real case [6]. The paper also sets out the $p$-adic norm $|x|_p = p^{-r}$ for $x = p^r n/m$ and its ultrametric strong triangle inequality [6], which we use for the product-formula computations of Section 4. From [6] we use quantitatively the p-adic norm $|x|_p = p^{-r}$ for $x = p^r n/m$ and its ultrametric strong triangle inequality, which underlie the product-formula computations of Section 4; the phase-transition result for $p = 3$ serves only as context illustrating prime-dependent structure in p-adic systems, and no Potts quantity enters our calculations.

**p-Adic geometry of state spaces.** Reference [8] introduces p-adic equiangular lines and derives the first fundamental relation between common angle, dimension, and number of lines: if $\{\tau_j\}_{j=1}^n$ is a p-adic $\gamma$-equiangular family in $\mathbb{Q}_p^d$, then $|n|^2 \leq |d|\max\{|n|, \gamma^2\}$, the p-adic van Lint–Seidel relative bound [8]. The paper defines the underlying p-adic Hilbert space structure — a non-Archimedean Banach space with an inner product satisfying symmetry, linearity, and a Cauchy–Schwarz-type condition [8] — showing that Hilbert-space geometry survives in $\mathbb{Q}_p^d$. This supports the coherence of defining gamma-matrix structures and wave-packet inner products over p-adic fields, and supplies a concrete structural constraint (the bound) that any construction of p-adic equiangular states in our simulation program must respect.

**The adelic physics program.** We frame the central thesis of this work as our own conjecture that physics is adelic: quantum mechanics as currently formulated operates exclusively at the $\infty$-place, and the Archimedean description is one readout of a richer ultrametric structure. Our paper is a concrete dynamical instantiation of the ZBW strand of that conjecture, working out the scale dependence through the product formula. A speculative two-place variant, in which ZBW would be mixing between only the Archimedean and 2-adic completions of $\mathbb{Q}$ with a beat frequency reducing to $\omega_{\mathrm{ZBW}} = 2E/\hbar$ under a calibration condition $|\Delta| \sim E$, is labeled here as an unconstructed hypothesis: no such Hamiltonian is built and no beat frequency is derived in this paper. What we do verify is the product formula for $x = 6, 10, 12$ exactly in Section 4. A central weakness of any two-place restriction is that nothing in the product formula singles out $p = 2$ algebraically, since $\prod_v |q|_v = 1$ holds for every rational and every prime; our all-sectors formulation is the direct response to that weakness.

Collectively, these works establish that (i) adelic quantum mechanics is mathematically well posed, with complex-valued wave functions the bridge to ordinary quantum mechanics [1], [5]; (ii) ZBW is a robust, universal wave-packet phenomenon whose vacuum realization is currently simulation-bound [3], [4], [7]; and (iii) p-adic techniques exhibit prime-dependent structure and support Hilbert-space geometry [6], [8]. Our contribution synthesizes these strands into a single falsifiable dynamical conjecture.

## 3. Methods

### 3.1 The adele ring and the product formula

By the Ostrowski theorem, every non-trivial absolute value on $\mathbb{Q}$ is equivalent to the usual Archimedean one $|\cdot|_\infty$ or to a p-adic norm $|\cdot|_p$ for some prime $p$. The adele ring is the restricted product $\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p$, whose elements are sequences $x = (x_\infty, x_2, \ldots)$ with $x_p \in \mathbb{Z}_p$ for all but finitely many primes [2]. For a nonzero rational $x \in \mathbb{Q}^\times$ embedded diagonally, write $x = p^{v_p(x)} \cdot \frac{n}{m}$ with $p, n, m$ relatively prime; the p-adic norm is $|x|_p = p^{-v_p(x)}$ [6]. The product formula then reads

$$|x|_\infty \prod_p |x|_p = 1.$$

This identity is the algebraic engine of our cancellation claim and is verified by explicit computation in Section 4, Step 5. It holds for every rational and every prime — a fact that means the product formula alone cannot privilege any single prime; our conjecture must therefore be formulated over all sectors at once.

### 3.2 The adelic Dirac equation, sector by sector

We posit an adelic Dirac wave function $\Psi = (\Psi_\infty, \Psi_2, \Psi_3, \Psi_5, \ldots)$, where $\Psi_\infty$ is the standard complex Dirac spinor on $\mathbb{R}^3$ and $\Psi_p$ is a $\mathbb{C}$-valued spinor on $\mathbb{Q}_p^3$ of the type constructed in p-adic quantum mechanics with complex-valued wave functions [1]. The free adelic Dirac equation is postulated sector-wise:

$$i\hbar \frac{\partial \Psi_p}{\partial t_p} = \left( c\, \boldsymbol{\alpha}_p \cdot \mathbf{D}_p + \beta_p m c^2 \right) \Psi_p, \qquad p \in \{\infty, 2, 3, 5, \ldots\},$$

The time variable $t_p$ is introduced here without an operational definition; whether the sectors share the Archimedean time parameter or carry their own is an open structural question deferred to Section 6. Where $\mathbf{D}_\infty = -i\hbar \nabla$ is the usual momentum operator and $\mathbf{D}_p$ for finite $p$ is taken to be the Vladimirov-type pseudodifferential operator (the p-adic analogue of the Laplacian, whose spectral theory underlies p-adic quantum mechanics [1]); $\boldsymbol{\alpha}_p, \beta_p$ are gamma-matrix structures over the respective field, whose existence as algebraic objects is consistent with p-adic linear-algebra geometry as exemplified by the p-adic Hilbert spaces and equiangular-line bounds of [8]. In the Archimedean sector, $c$ and $m_e$ are the observed constants. The equation is **postulated, not derived**; this is the central limitation of the framework, discussed in Section 6. The choice of complex-valued sector wave functions follows the recommendation of [1] that this variant connects most directly with ordinary quantum mechanics.

### 3.3 Sector-resolved velocity expectation

For each sector $s \in \{\infty, 2, 3, 5, \ldots\}$ define the velocity expectation

$$v_s(t) = \int \Psi_s^\dagger(\mathbf{x},t)\, \alpha_s\, \Psi_s(\mathbf{x},t)\, d\mu_s(\mathbf{x}),$$

with $d\mu_\infty$ Lebesgue measure and $d\mu_p$ the Haar measure on $\mathbb{Q}_p^3$. For a wave packet that is a superposition of positive- and negative-energy branches, the standard cross term produces an oscillatory contribution at the branch energy gap; in the real sector this is the Breit–Schrödinger trembling motion [4], with

$$\langle v_\infty \rangle(t) \approx c(1 - 2w) + 2cw\cos(\omega_\infty t), \qquad \omega_\infty = \frac{2m_e c^2}{\hbar},$$

where $w$ is the negative-energy admixture. The universal mechanism behind this oscillation — interference of states belonging to positive and negative energies — is exactly the mechanism that [3] identifies as the background of ZB in any system. We postulate the same two-branch structure sector-wise, with p-adic oscillation frequencies determined by the p-adic dispersion relation of the Vladimirov operator. The observable macroscopic position is the adele-diagonal projection

$$X(t) = w_\infty x_\infty(t) + \sum_{p \leq P} w_p x_p(t),$$

where $P$ is a finite cutoff (only finitely many p-adic norms of a rational differ from 1, per the adele restriction [2]) and $w_s$ are sector weights.

### 3.4 Cancellation mechanism (conjecture)

Let $r = \ell/\lambda_C$ be the dimensionless ratio of the observation scale $\ell$ to the Compton wavelength $\lambda_C = \hbar/(m_e c)$, approximated by a rational number. We conjecture that the cross-sector interference amplitude in $X(t)$ is proportional to the product of p-adic norms of $r$:

$$A_{\mathrm{int}}(\ell) = A_0 \prod_{p} |r|_p = A_0\, \frac{\lambda_C}{\ell},$$

where the last equality is the adele product formula and $A_0$ is the single-sector trembling amplitude. Thus the p-adic contribution to the observed motion is suppressed by $\lambda_C/\ell$ at scales $\ell \gg \lambda_C$, and enhanced at $\ell \lesssim \lambda_C$. This is the precise sense in which "the p-adic contributions cancel at macroscopic scales." Two points of intellectual honesty must be stated now. First, the physical content of the conjecture lies entirely in the proportionality $A_{\mathrm{int}} \propto \prod_p |r|_p$; the product formula guarantees only that this product equals $\lambda_C/\ell$ exactly, not that the interference amplitude obeys this scaling. Second, the sector weights $w_p$ in the projection $X(t)$ are free parameters of the framework; the suppression law as stated concerns the interference amplitude, not the weights, and different weight choices shift any observable crossover. Both points are carried through the limitations of Section 6.

### 3.5 Simulation program (specified, not executed)

To falsify the conjecture we propose the following computational steps:

1. Construct explicit $p$-adic gamma matrices $\boldsymbol{\alpha}_p, \beta_p$ satisfying the Clifford algebra, respecting the p-adic Hilbert-space geometry and the equiangular-line bound of [8].
2. Discretize the Vladimirov operator on a finite $p$-adic ball and solve the sector-wise Dirac equation for Gaussian-type wave packets.
3. Extract the sector frequencies $\omega_p$ and test the linear dispersion hypothesis $\omega_p = \omega_\infty |r|_p$.
4. Verify numerically that $\prod_p |r|_p$ reproduces $\lambda_C/\ell$ for rational $r$.
5. Compare the resulting adelic propagator with the exactly solvable quadratic-Lagrangian adelic amplitudes of [5].

No simulation results are reported here; the program is presented as a concrete falsifiability pathway.

## 4. Analysis

All input constants are stated here; every subsequent number is derived from them by shown arithmetic.

**Inputs.**
- Electron mass $m_e = 9.109 \times 10^{-31}\,\mathrm{kg}$.
- Speed of light $c = 2.998 \times 10^{8}\,\mathrm{m\,s^{-1}}$.
- Reduced Planck constant $\hbar = 1.055 \times 10^{-34}\,\mathrm{J\,s}$.
- Newtonian constant $G = 6.674 \times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$.

**Step 1: Electron rest energy.**

$$m_e c^2 = 9.109 \times 10^{-31} \times (2.998 \times 10^{8})^2.$$

First, $c^2 = (2.998)^2 \times 10^{16} = 8.988004 \times 10^{16}\,\mathrm{m^2\,s^{-2}}$. Then

$$m_e c^2 = 9.109 \times 8.988004 \times 10^{-31+16} = 81.8717 \times 10^{-15} = 8.18717 \times 10^{-14}\,\mathrm{J}.$$

**Step 2: Zitterbewegung angular frequency, cyclic frequency, and period.**

$$\omega_\infty = \frac{2 m_e c^2}{\hbar} = \frac{2 \times 8.18717 \times 10^{-14}}{1.055 \times 10^{-34}} = \frac{1.637434 \times 10^{-13}}{1.055 \times 10^{-34}} = 1.55207 \times 10^{21}\,\mathrm{rad\,s^{-1}}.$$

Rounded to five significant figures this is $\omega_\infty = 1.5521 \times 10^{21}\,\mathrm{rad\,s^{-1}}$. The cyclic frequency is

$$f_\infty = \frac{\omega_\infty}{2\pi} = \frac{1.55207 \times 10^{21}}{6.2831853} = 2.47020 \times 10^{20}\,\mathrm{Hz},$$

and the period is

$$T = \frac{1}{f_\infty} = \frac{1}{2.47020 \times 10^{20}} = 4.0482 \times 10^{-21}\,\mathrm{s}.$$

**Step 3: Compton wavelength.**

$$\lambda_C = \frac{\hbar}{m_e c} = \frac{1.055 \times 10^{-34}}{9.109 \times 10^{-31} \times 2.998 \times 10^{8}}.$$

Denominator: $9.109 \times 2.998 = 27.3088$, so $m_e c = 2.73088 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$. Then

$$\lambda_C = \frac{1.055 \times 10^{-34}}{2.73088 \times 10^{-22}} = \frac{1.055}{2.73088} \times 10^{-12} = 0.386317 \times 10^{-12} = 3.8632 \times 10^{-13}\,\mathrm{m}.$$

**Step 4: Planck length.**

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}}.$$

Numerator: $\hbar G = 1.055 \times 10^{-34} \times 6.674 \times 10^{-11} = 7.04107 \times 10^{-45}$. Denominator: $c^3 = (2.998)^3 \times 10^{24} = 26.9460 \times 10^{24} = 2.69460 \times 10^{25}\,\mathrm{m^3\,s^{-3}}$. Ratio:

$$\frac{\hbar G}{c^3} = \frac{7.04107 \times 10^{-45}}{2.69460 \times 10^{25}} = 2.61313 \times 10^{-70}\,\mathrm{m^2},$$

$$\ell_P = \sqrt{2.61313 \times 10^{-70}}\,\mathrm{m} = 1.6165 \times 10^{-35}\,\mathrm{m}.$$

**Step 5: Product formula, explicit verification.**

Case $x = 6 = 2 \times 3$: $|6|_\infty = 6$, $|6|_2 = 2^{-1} = 0.5$, $|6|_3 = 3^{-1} = 1/3$, all other $|6|_p = 1$:

$$6 \times 0.5 \times \frac{1}{3} = 1. \checkmark$$

Case $x = 12 = 2^2 \times 3$: $|12|_\infty = 12$, $|12|_2 = 2^{-2} = 0.25$, $|12|_3 = 1/3$:

$$12 \times 0.25 \times \frac{1}{3} = 1. \checkmark$$

Case $x = 10 = 2 \times 5$: $|10|_\infty = 10$, $|10|_2 = 0.5$, $|10|_5 = 0.2$:

$$10 \times 0.5 \times 0.2 = 1. \checkmark$$

The product formula holds exactly for every rational test value; the cancellation it encodes is algebraic, not approximate.

**Step 6: Cross-sector interference amplitude at laboratory scale.** By the conjectured mechanism of Section 3.4, with $r = \ell/\lambda_C$:

$$\frac{A_{\mathrm{int}}(\ell)}{A_0} = \prod_p |r|_p = \frac{1}{|r|_\infty} = \frac{\lambda_C}{\ell}.$$

At $\ell = 1\,\mathrm{m}$:

$$\frac{A_{\mathrm{int}}}{A_0} = \frac{3.8632 \times 10^{-13}}{1} = 3.863 \times 10^{-13}.$$

If an interferometric observable depends on intensity-like cross terms, the relative suppression is the square:

$$\left(\frac{A_{\mathrm{int}}}{A_0}\right)^2 = (3.863 \times 10^{-13})^2 = 1.4923 \times 10^{-25} \approx 1.492 \times 10^{-25}.$$

**Step 7: p-Adic dominance at the Planck scale.** At $\ell = \ell_P$:

$$\frac{\lambda_C}{\ell_P} = \frac{3.8632 \times 10^{-13}}{1.6165 \times 10^{-35}} = \frac{3.8632}{1.6165} \times 10^{22} = 2.3898 \times 10^{22} \approx 2.39 \times 10^{22}.$$

At the Planck length the conjectured non-Archimedean interference amplitude exceeds its laboratory-scale ($\ell = 1\,\mathrm{m}$) suppression factor by about 35 orders of magnitude: the quotient $2.3898 \times 10^{22} / (3.863 \times 10^{-13}) \approx 6.19 \times 10^{34}$ — the quantitative content of the claim that near the Compton and Planck lengths the non-Archimedean terms dominate.

**Step 8: Crossover scale (projection).** The cancellation is complete to relative amplitude $\varepsilon$ when $\lambda_C/\ell < \varepsilon$, i.e. $\ell > \lambda_C/\varepsilon$. For $\varepsilon = 10^{-6}$:

$$\ell > \frac{3.8632 \times 10^{-13}}{10^{-6}} = 3.8632 \times 10^{-7}\,\mathrm{m} = 386.3\,\mathrm{nm}.$$

So beyond optical wavelengths the conjectured p-adic interference is suppressed below $10^{-6}$ in amplitude. This is a **projection** of the conjectured mechanism: it assumes (i) the proportionality $A_{\mathrm{int}} \propto \prod_p |r|_p$, (ii) sector parameters of order unity, and (iii) the stated threshold $\varepsilon$. For a stricter threshold $\varepsilon = 10^{-4}$ in a quantity scaling as $1/N^2$ with $N = \ell/\lambda_C$ (an alternative intensity-like convention, in which the relative deviation scales as $(\lambda_C/\ell)^2$ rather than $\lambda_C/\ell$), the crossover would instead lie at $N = (10^{-4})^{-1/2} = 100$, i.e. $\ell = 100\,\lambda_C = 3.8632 \times 10^{-11}\,\mathrm{m}$.

**Step 9: Model-projected sector frequency shifts (labeled projection).** Assume the p-adic sector dispersion ties its oscillation frequency to the p-adic norm of the scale ratio: $\omega_p = \omega_\infty |r|_p$ for the finitely many primes with $|r|_p \neq 1$. Take $\ell = 10\,\lambda_C$, so $r = 10 = 2 \times 5$, with $|10|_2 = 0.5$ and $|10|_5 = 0.2$ (Step 5). The projected sector frequencies are

$$f_2 = 0.5 \times 2.47020 \times 10^{20} = 1.2351 \times 10^{20}\,\mathrm{Hz}, \qquad f_5 = 0.2 \times 2.47020 \times 10^{20} = 4.9404 \times 10^{19}\,\mathrm{Hz}.$$

These are projections conditional on the stated dispersion assumption $\omega_p = \omega_\infty |r|_p$; they are not measurements, and the assumption itself is what the proposed $\mathbb{Q}_p$ simulations of Section 3.5 must test. An alternative "sum variant" in which sector frequencies combine in quadrature, $\omega_{\mathbb{A}} = \omega_\infty\sqrt{1 + |r|_p^2}$ for a single dominant prime, gives for $r = 2$: $\omega_{\mathbb{A}} = \omega_\infty\sqrt{1.25} = 1.11803\,\omega_\infty$, an $11.8\%$ shift; the two variants are empirically distinguishable in principle at $\ell \lesssim 100\,\lambda_C$.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none are empirical measurements.

1. **Standard ZBW frequency (real sector).** $\omega_\infty = 1.5521 \times 10^{21}\,\mathrm{rad\,s^{-1}}$, i.e. $f_\infty = 2.4702 \times 10^{20}\,\mathrm{Hz}$ and period $T = 4.0482 \times 10^{-21}\,\mathrm{s}$ for the electron, derived as $\omega_\infty = 2m_e c^2/\hbar$ (Steps 1–2).

2. **Compton wavelength.** $\lambda_C = 3.8632 \times 10^{-13}\,\mathrm{m}$ (Step 3).

3. **Planck length.** $\ell_P = 1.6165 \times 10^{-35}\,\mathrm{m}$ (Step 4).

4. **Product-formula verification.** $|x|_\infty \prod_p |x|_p = 1$ holds exactly for $x = 6, 10, 12$ (Step 5).

5. **Conjectured suppression law.** Under the conjecture $A_{\mathrm{int}} \propto \prod_p |r|_p$, the cross-sector interference amplitude ratio is $A_{\mathrm{int}}/A_0 = \lambda_C/\ell$: at $\ell = 1\,\mathrm{m}$, $3.863 \times 10^{-13}$ in amplitude and $1.492 \times 10^{-25}$ in intensity-like terms (Step 6). The arithmetic is exact; the physical content is the conjecture itself.

6. **Non-Archimedean dominance at the Planck scale.** $\lambda_C/\ell_P = 2.3898 \times 10^{22} \approx 2.39 \times 10^{22}$ (Step 7).

7. **Crossover projection.** Under the stated assumptions, p-adic interference falls below relative amplitude $10^{-6}$ for $\ell > 386.3\,\mathrm{nm}$; under the alternative intensity-like convention with threshold $10^{-4}$, the crossover is at $100\,\lambda_C = 3.8632 \times 10^{-11}\,\mathrm{m}$ (Step 8). Both are projections, sensitive to the untested mechanism and threshold.

8. **Projected sector frequency shifts (projection).** Under $\omega_p = \omega_\infty |r|_p$ with $r = 10$: $f_2 = 1.2351 \times 10^{20}\,\mathrm{Hz}$, $f_5 = 4.9404 \times 10^{19}\,\mathrm{Hz}$, all other sectors unshifted (Step 9). Under the sum variant with $r = 2$: an $11.8\%$ shift. No simulation or measurement of either variant has been performed.

## 6. Discussion

**Status of the claims.** The numerical results (items 1–4 and 6 of Section 5) are ordinary consequences of standard constants and elementary number theory. The genuinely new content — items 5, 7, 8 — rests on one conjectural identification: that the cross-sector interference amplitude of the adelic Dirac dynamics is proportional to $\prod_p |r|_p$. The product formula then makes the cancellation exact and scale-independent in form, which is elegant, but elegance is not derivation. We have not derived the adelic Dirac equation from an action principle over $\mathbb{A}$, nor proven that the Vladimirov-operator spectrum produces frequencies scaling as $|r|_p$; both are stated as the test program of Section 3.5, not as results.

**Limitations.** (i) The adelic Dirac equation of Section 3.2 is postulated, not derived; with complex-valued sector wave functions one cannot construct a direct analogue of the Schrödinger equation with a p-adic Heisenberg algebra [1], so no standard route to the sector dynamics exists. (ii) The sector weights $w_p$ in the diagonal projection $X(t) = w_\infty x_\infty(t) + \sum_{p \leq P} w_p x_p(t)$ are free parameters of the model; we have no principle that fixes them, and different choices change the predicted crossover scale of Step 8. (iii) The proportionality $A_{\mathrm{int}} \propto \prod_p |r|_p$ is the conjecture itself, not a consequence of the product formula; the product formula only makes the conjectured law exact once the proportionality is granted. (iv) The sector dispersion assumption $\omega_p = \omega_\infty |r|_p$ of Step 9 is untested; the Vladimirov-operator spectrum could produce entirely different p-adic frequencies, in which case the projected shifts $f_2 = 1.2351 \times 10^{20}\,\mathrm{Hz}$ and $f_5 = 4.9404 \times 10^{19}\,\mathrm{Hz}$ would fail. (v) The framework has no demonstrated coupling to electromagnetism or interactions; all results concern the free particle. (vi) At the Compton scale $\lambda_C = 3.8632 \times 10^{-13}\,\mathrm{m}$ and below, no interferometric technique cited here operates, so experimental discrimination between the amplitude convention (relative deviation scaling as $\lambda_C/\ell$) and the intensity-like convention (scaling as $(\lambda_C/\ell)^2$) is currently out of reach. (vii) The time variable $t_p$ appearing in the sector-wise equation of Section 3.2 is not defined operationally; whether p-adic sectors share the Archimedean time parameter or carry their own is an open structural question that affects every projected frequency.

**What would falsify the claims.** The central conjecture is falsified if the simulation program of Section 3.5, executed on $\mathbb{Q}_p$ with the Vladimirov operator, yields p-adic sector frequencies that do not scale as $|r|_p$ — this is the single calculation whose outcome decides the fate of the suppression law, because the law's only free content is the proportionality to $\prod_p |r|_p$. A second falsification path is incompatibility of the postulated sector-wise Dirac dynamics with the exactly solvable quadratic-Lagrangian adelic amplitudes of [5], whose number-field-invariant form any adelic dynamics should respect. A third path is experimental: a condensed-matter ZBW measurement of the type reviewed in [3], [7], with effective parameters $u \approx 10^8\,\mathrm{cm/s}$ and band gap $\mathcal{E}_g$ replacing $c$ and $m_e$, rescales the hierarchy of Section 4; a frequency shift inconsistent with both the multiplicative variant $\omega_p = \omega_\infty |r|_p$ and the quadrature variant $\omega_{\mathbb{A}} = \omega_\infty\sqrt{1 + |r|_p^2}$ would eliminate the adelic mechanism as a source of observable ZBW corrections. Conversely, observation of an $11.8\%$-scale frequency shift at $\ell \lesssim 100\,\lambda_C = 3.8632 \times 10^{-11}\,\mathrm{m}$ under the sum variant would support, though not prove, the adelic picture.

**Open questions.** What action principle over $\mathbb{A}$ yields the postulated sector-wise Dirac equation? Do p-adic gamma matrices exist for all primes subject to the equiangular-line bound of [8]? How do interactions and spin enter the sector weights $w_p$? Is there a physical principle that fixes the sector time variables? These are deferred to future work.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are the quantum-simulation and condensed-matter ZBW community: the vacuum ZB of the free electron is probably not directly observable for years to come and one must resort to simulations, for which a proof of principle has been carried out [3], and ZB of charge carriers in narrow-gap semiconductors, graphene, and carbon nanotubes is observable with frequencies set by band gaps and amplitudes up to tens of nanometers [7]. If the conjecture holds, the design parameter that changes is the interpretation and analysis target of ZBW simulations: sector-resolved frequency extraction would be added to wave-packet simulation pipelines, and a measured or simulated ZBW frequency would be tested against the multiplicative variant $\omega_p = \omega_\infty |r|_p$ and the quadrature variant of Step 9 rather than only against $\hbar\omega_Z \approx \Delta\mathcal{E}$. A second user group is theorists in p-adic mathematical physics, for whom the suppression law supplies the first concrete dynamical observable tied to the product formula. For the broader community the work is foundational: no device or policy changes today, because the framework's empirical content at the frequency level is currently identical to the standard interference picture in the Archimedean sector.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: basic principles are stated and conjectural applications are identified, but the adelic Dirac equation is postulated, no peer-reviewed experimental or computational confirmation exists, and no simulation of the program of Section 3.5 has been executed. Analytical work of this kind cannot exceed TRL 3, and nothing in this paper reaches even the proof-of-concept level of TRL 3, since no p-adic gamma-matrix construction or Vladimirov-operator wave-packet solution has been carried out.

**(c) The smallest next test.** The smallest de-risking calculation is computational and self-contained: construct explicit gamma matrices $\boldsymbol{\alpha}_p, \beta_p$ over $\mathbb{Q}_2$ and $\mathbb{Q}_3$ satisfying the Clifford algebra, discretize the Vladimirov operator on a finite p-adic ball $B(0, p^{-n})$, evolve a Gaussian-type test packet, and extract the sector oscillation frequency $\omega_p$. The outcome that refutes the conjecture is a computed $\omega_p$ that does not scale as $\omega_\infty |r|_p$ for the test ratio $r = 10$ of Step 9; the outcome that supports it is agreement with $f_2 = 1.2351 \times 10^{20}\,\mathrm{Hz}$ and $f_5 = 4.9404 \times 10^{19}\,\mathrm{Hz}$ up to the numerical accuracy of the discretization. A secondary check compares the resulting adelic propagator against the exactly solvable quadratic-Lagrangian amplitudes of [5].

**(d) Binding constraints.** The first binding constraint is computational infrastructure: p-adic floating-point arithmetic, Haar-measure-normalized discretizations of the Vladimirov operator, and a defensible finite cutoff $P$ in the projection $X(t)$ do not exist as standard numerical libraries, and the choice of measure normalization directly affects extracted frequencies. The second is theoretical: the sector time variables $t_p$ and the sector weights $w_p$ must be fixed by a principle before any simulated frequency can be compared with an experiment. The third is experimental access: at $\lambda_C = 3.8632 \times 10^{-13}\,\mathrm{m}$ no interferometric technique cited here operates, so any experimental test must proceed through condensed-matter analogues with rescaled parameters [3], [7], where the mapping from $c, m_e$ to $u, \mathcal{E}_g$ must itself be derived for the adelic case. Whether p-adic gamma matrices exist for all primes within the equiangular-line bound of [8] is an open question rather than a known constraint.

**(e) Order-of-magnitude bounds (projections).** All scale figures in this pathway are derived in Section 4 and rest on the stated inputs: the regime in which p-adic corrections could matter is $\ell \lesssim 100\,\lambda_C = 3.8632 \times 10^{-11}\,\mathrm{m}$ under the intensity-like convention, and the suppression at optical and larger scales is below $10^{-6}$ in amplitude beyond $386.3\,\mathrm{nm}$. No cost, market, or performance figures beyond these scale bounds are derivable from the present framework, and none are projected.

**(f) Risks and misuse paths.** No direct physical hazard follows from this work. The relevant risk is interpretive: because the framework's Archimedean-sector predictions coincide with standard ZBW, a positive result at the frequency level could be over-read as confirmation of adelic physics when it is equally consistent with the standard interference account [3]; any claim of confirmation must rest on the sector-resolved signatures of Step 9, not on the recovery of $\omega_\infty = 2m_e c^2/\hbar$.

## 8. Conclusion

We have proposed a conjectural adelic extension of Zitterbewegung in which the trembling motion of a free Dirac particle decomposes into an Archimedean contribution at $\omega_\infty = 2m_e c^2/\hbar = 1.5521 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ (period $T = 4.0482 \times 10^{-21}\,\mathrm{s}$) and one contribution per $p$-adic sector, suppressed at macroscopic scales by the product formula $|x|_\infty \prod_p |x|_p = 1$, verified exactly for $x = 6, 10, 12$. The computed scale hierarchy $\lambda_C/\ell_P = 2.389 \times 10^{22}$ quantifies the regime in which the non-Archimedean sectors could dominate, while the conjectured suppression law $A_{\mathrm{int}}/A_0 = \lambda_C/\ell$ gives $3.863 \times 10^{-13}$ at $\ell = 1\,\mathrm{m}$ and a projected crossover below $10^{-6}$ amplitude beyond $386.3\,\mathrm{nm}$. All numerical results follow from stated inputs by shown arithmetic; the physical claims are explicitly labeled conjectures or projections, the sector weights $w_p$ and sector times $t_p$ remain free or undefined, and a falsifiable simulation program on $\mathbb{Q}_p$ using the Vladimirov operator is specified but not executed. The work is at TRL 1–2, and its smallest next test — a $\mathbb{Q}_2$ and $\mathbb{Q}_3$ wave-packet evolution whose extracted sector frequencies either scale as $\omega_\infty |r|_p$ or do not — is fully specified in Section 7. The framework's value, if any, lies in making the adelic regularization of Dirac dynamics precise enough to fail.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.0-fail-closed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[2] p-Adic and Adelic Cosmology: p-Adic Origin of Dark Energy and Dark Matter. arXiv:hep-th/0602044v1. https://arxiv.org/abs/hep-th/0602044v1
[3] Zitterbewegung (trembling motion) of electrons in semiconductors: a Review. arXiv:1101.0623v1. https://arxiv.org/abs/1101.0623v1
[4] The Problem of Motion: The Statistical Mechanics of Zitterbewegung. arXiv:1411.1854v2. https://arxiv.org/abs/1411.1854v2
[5] Path Integrals for Quadratic Lagrangians on p-Adic and Adelic Spaces. arXiv:1011.6589v1. https://arxiv.org/abs/1011.6589v1
[6] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[7] Zitterbewegung (trembling motion) of electrons in narrow gap semiconductors. arXiv:0805.0478v1. https://arxiv.org/abs/0805.0478v1
[8] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
