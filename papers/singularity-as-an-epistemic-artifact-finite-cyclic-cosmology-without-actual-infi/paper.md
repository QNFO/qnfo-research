# Singularity as an Epistemic Artifact: Finite Cyclic Cosmology without Actual Infinities

## Abstract

Cosmological singularities — states in which density, curvature and temperature diverge — mark the breakdown of predictive physics at the Big Bang and inside black holes, and they block any quantitative continuation of collapse or of the early universe. Whether these infinities are features of reality or artifacts of the mathematical representation remains open. This paper tests the conjecture that actual infinities in gravitational physics are artifacts of adopting a linear, unbounded number line, and that in a cyclic framework a "singularity" is a transition between epochs rather than a physical infinity. We combine an audit of the hypotheses of the singularity theorems with explicit toy models. In a closed dust universe with density parameter $\Omega_0$, recollapse occurs at the finite scale factor $a_{\max}/a_0 = \Omega_0/(\Omega_0-1)$; for $\Omega_0 = 1.2$ this gives $a_{\max} = 6\,a_0$ and a density at recollapse of $\rho_0/216$. A re-parametrization of density by an angle, $\rho/\rho_c = \tan(\theta/2)$, sends the finite state $\theta = \pi$ to $\rho \to \infty$, demonstrating that the divergence lives in the chart, not the state. A discrete clock spanning the Hubble radius at Planck spacing contains $N \approx 8.50 \times 10^{60}$ states, making epoch transitions finite wraparound events by construction. Using SKA1 dipole forecasts, the ratio of the kinematic dipole to the large-scale-structure dipole is $R = 0.0046/0.0031 \approx 1.48$ with forecast uncertainty $\pm 0.76$. The results reframe singularity theorems as representation-sensitive statements and define a concrete simulation and observation program.

## 1. Introduction

Cosmologists and gravitational physicists face a concrete, unsolved problem: the classical theories they use predict that certain physical quantities become infinite. In the standard paradigm the universe was born from a spacetime singularity where "physical quantities like density, pressure, temperature, spacetime curvature etc, were infinite and thus theoretically ill-defined" [1]. Inside classical black-hole collapse the same happens, and the Penrose–Hawking theorems of the 1960s converted singularities from unrealistic limiting cases into central, unavoidable features of gravitational collapse. The practical cost is severe: no equation of state, no initial condition and no prediction can be formulated at or beyond an infinite quantity, so the origin of the universe and the final state of collapse currently lie outside quantitative physics altogether. Infinities are, in this precise sense, "an end point for physics: their appearance means that we can not associate a finite number to the system under study" [3].

What would change if the conjecture of this paper holds? If the divergences signal the inadequacy of a linear, unbounded number line rather than a physical endpoint, then singularity theorems become readable as statements about representations, cyclic models become reformulable with finite, constructively defined quantities, and the observational program comparing cyclic against singular cosmology acquires a well-defined target: finite curvature maxima with Penrose-style conformal boundaries, rather than true infinities. Model builders would gain a design principle — choose parametrizations in which every observable is bounded — and observationalists would gain discriminators between "transition" and "termination" readings of the same data.

This paper pursues that conjecture with formal analysis and toy models, and it is explicit that the toy models are kinematic constructions, not asserted solutions of Einstein's equations. The contributions are:

- A representation result: an explicit re-parametrization $\rho(\theta) = \rho_c \tan(\theta/2)$ in which a finite cyclic state $\theta = \pi$ maps to an infinite linear density, with numerical evaluation at $\theta = \pi - 10^{-3}$ giving $\rho/\rho_c \approx 2000$ (Section 4.3).
- A finite-recollapse result for a closed dust universe: $a_{\max}/a_0 = \Omega_0/(\Omega_0-1)$, evaluated at $\Omega_0 = 1.2$ to give $a_{\max} = 6\,a_0$ and $\rho(a_{\max}) = \rho_0/216$, and at $\Omega_0 = 1.0005$ to give $a_{\max} = 2001\,a_0$ and $\rho(a_{\max}) \approx 1.25 \times 10^{-10}\,\rho_0$ (Section 4.2).
- An audit of which hypotheses of the singularity theorems presuppose an unbounded linear parameter, showing that geodesic incompleteness is defined through an affine parameter ranging over $\mathbb{R}$ and is therefore representation-sensitive (Sections 3.4 and 4.4).
- A discrete clock model with state count $N = c/(H_0\,l_P) \approx 8.50 \times 10^{60}$ across the Hubble radius, in which epoch transitions are wraparound events rather than divergences (Section 4.5).
- A consistency check using horizon evolution: the pure de Sitter event horizon $D_e = c/H_0 = 1.373 \times 10^{26}\,\mathrm{m} \approx 14.5$ Gly is exactly the stationary solution of the horizon-recession equation $\frac{dH_e}{dt} = H_e H - 1$ of [7] (Section 4.6).
- A quantitative observational anchor: the ratio of the SKA1 forecast kinematic dipole amplitude to the large-scale-structure dipole amplitude, $R = 0.0046/0.0031 \approx 1.48 \pm 0.76$, derived with full arithmetic and propagated uncertainty (Section 4.7).

## 2. Background and Related Work

The starting point is the status of the Big Bang singularity in the standard model. [1] reviews cyclic cosmology and records that in the standard paradigm the universe was born from a spacetime singularity where density, pressure, temperature and curvature were infinite and theoretically ill-defined, and that open geometries must be excluded because they correspond to infinite proper three-volume at the singularity. The same review establishes the structural obstacle this paper must address: within General Relativity, a non-singular cyclic model requires "a non-conventional fluid with negative effective energy density, in order to cancel the matter component and lead to a non-singular bounce," and such a fluid "usually leads to quantum instabilities and makes the theory ill-defined" [1]. Its conclusion favors extended Einstein gravity, for example higher-order curvature terms, while noting that the whole discussion assumes homogeneity, which may not hold according to Sloan Digital Sky Survey analysis [1]. For this paper, [1] supplies both the motivation (the singularity is ill-defined, not merely surprising) and the constraint (any cyclic construction must either violate an energy condition or modify gravity, and must answer for inhomogeneity).

The philosophical target — that infinities measure ignorance rather than reality — is argued directly in [3]. That work identifies a minimal length as the main feature of quantum gravity, analogous to the maximal velocity $c$ of special relativity and the minimal action $\hbar$ of quantum mechanics, and argues that a finite region of phase space contains only finitely many distinguishable states [3]. Its conclusion states the position this paper formalizes: every infinity and its overcoming is the turning point for a new paradigm, and "what is truly infinite may just be the abyss of our ignorance" [3]. [3] also frames the Zeno problem as still open, noting that Zeno was confused by the assumption that every infinite series diverges — a caution this paper takes seriously by checking convergence explicitly in its own constructions.

On the quantum side, [2] constructs a Friedmann model in which the Wheeler–DeWitt solution corresponds exactly to classical evolution: using de Broglie–Bohm and modified de Broglie–Bohm trajectory representations, they show that exact quantum-classical correspondence is equivalent to the vanishing of the quantum potential, and that for a total energy density varying as $1/a^{n}$ this happens for $n = 2$ [2]. The resulting coasting evolution is a concrete example of a cosmology in which the well-known problems of quantum cosmology disappear [2]. This matters here because a coasting law $\rho \propto a^{-2}$ is exactly the case where the gravitational dynamics is scale-free, and scale-free dynamics is the natural habitat of cyclic (angle-valued) rather than linear (unbounded) variables.

Alternative quantizations support the same direction. [4] proposes a quantization of homogeneous cosmological models combining the Dirac constrained-system method, Fock space construction, second quantization and a Diagonalization Ansatz (Bogoliubov transformation plus Heisenberg equation), arguing that canonical, loop and path-integral quantizations apply quantum mechanics too straightforwardly and that the Wheeler–DeWitt functional differential equation "does not allow to solve the generic problem in principle" [4]. Their resulting quantum cosmology is well defined in a Fock space and has a temperature that is an explicit function of redshift $z$ [4]. This demonstrates that the formal apparatus of cosmology is not wedded to any single representation of its state space — the precondition for the re-parametrization arguments of Section 4.3.

Observationally, the relevant quantities are horizons and curvature, both finite and measurable. [7] defines the particle horizon as the boundary of the region already observed by an observer and the event horizon as the boundary of what will ever be observable, and derives, for a concordance universe with cosmological constant and dust, the recession equations $\frac{dH_p}{dt} = H_p(z)H(z) + 1$ and $\frac{dH_e}{dt} = H_e(z)H(z) - 1$, noting that these results are independent of the current values of the involved constants [7]. Section 4.6 uses these equations as a consistency check. Spatial curvature itself is tightly coupled to structure formation: [8] develops a model with non-zero spatial curvature, a running vacuum energy density and warm dark matter, showing that curvature modifies the evolution of matter perturbations and the shape of the matter power spectrum, and derives observational constraints on the parameters $\nu$, $b$ and $\Omega_k^0$ [8]. Any cyclic model with non-negligible curvature therefore inherits quantitative large-scale-structure constraints, not merely qualitative ones.

The observational pathway for testing cyclic signatures runs through facilities such as the Square Kilometre Array. [6] presents the Phase 1 SKA surveys and forecasts that the SKA1 Medium-Deep Band 2 weak-lensing survey will deliver constraints comparable to Stage III optical surveys such as DES, with radio–optical cross-correlations free of wavelength-dependent systematics retaining almost all statistical power [6]. [6] also reports a predicted kinematic radio dipole amplitude $A = 0.0046$ directed along the CMB dipole, with the large-scale-structure contribution $A = 0.0031 \pm 0.0016$ from mock simulations [6]. These forecasts define the precision floor against which any cyclic-versus-singular discriminator must be measured.

An alternative cosmological phenomenology, in which redshift arises from a global gravitational effect, is due to [5]: for a homogeneous matter distribution the cosmological gravitational redshift is proportional to the square of distance, $z_{\mathrm{grav}} \sim r^{2}$, an idea traced through de Sitter (1916, 1917), Eddington (1923), Tolman (1929) and Bondi (1947), with Hubble himself calling the discovered distance–redshift relation the "De Sitter effect" [5]. This is cited here for a specific methodological point: the interpretation of the same redshift data is representation- and mechanism-dependent, which is exactly the epistemic situation this paper claims for singularities.

## 3. Methods

### 3.1 Scope and honesty of the construction

The paper's claims are of two kinds. Formal claims concern definitions and representations and are proven by explicit construction. Physical claims concern the universe and are limited to toy models that are kinematically defined and are not asserted to be solutions of Einstein's equations. Where a number is a projection rather than a derivation, it is labeled as such with its assumptions.

### 3.2 Representation maps

Let $q$ be a physical quantity of a collapse or cosmological model, represented in the standard chart by a value in the extended real line $\mathbb{R} \cup \{\infty\}$. We consider two alternative representations:

1. **Angular (circular) representation.** The quantity is carried by an angle $\theta \in [0, 2\pi)$ through an explicit map $q(\theta)$; the state space is the circle $S^{1}$, which is compact, so every state is finitely distant from every other.
2. **Discrete (finite-state) representation.** The quantity is carried by an integer index $k \in \{0, 1, \dots, N-1\}$ with a wraparound rule $k \mapsto (k+1) \bmod N$; the state space is finite, so no state at all can be infinitely distant.

The conjecture under test is that the infinities of singularity theorems are properties of the first chart of the standard formalism (the extended real line), not of the physical states. The test is constructive: exhibit maps under which the allegedly infinite states become finite, and check which structural features (horizons, conformal boundaries, recollapse) survive.

### 3.3 Kinematic toy models

Two kinematic models are used. The first is a closed dust Friedmann universe, whose dynamics follows from the Friedmann energy equation alone; it provides a collapse–recollapse cycle with an explicit finite maximum scale factor. The second is a discrete clock spanning the Hubble radius at Planck spacing, which provides a finite state count for the observable universe. Neither model is claimed to be a solution of the full Einstein equations with realistic matter; they isolate the representational question.

### 3.4 Audit of singularity-theorem hypotheses

The Penrose–Hawking theorems conclude geodesic incompleteness from hypotheses that include an energy condition and a global structure condition (e.g., a trapped surface or a compact past). Geodesic incompleteness is defined as the failure of an affine parameter $\lambda$ — ranging over $\mathbb{R}$ — to extend over all of $\mathbb{R}$. The audit question is whether the theorem's conclusion is a statement about the manifold or about the chart in which $\lambda$ is linear. Section 4.4 shows that the conclusion is chart-sensitive by exhibiting an angular re-parametrization under which the "incomplete" parameter becomes a bounded angle.

## 4. Analysis

### 4.1 Input numbers and their sources

- Kinematic dipole amplitude from the SKA1 forecast: $A_{\mathrm{kin}} = 0.0046$ [6].
- Large-scale-structure dipole amplitude forecast: $A_{\mathrm{LSS}} = 0.0031$ with uncertainty $\sigma_{A} = 0.0016$ [6].
- Closed-universe density parameters taken as free inputs of the toy model: $\Omega_0 = 1.2$ and $\Omega_0 = 1.0005$ (assumed values, not measurements).
- Cosmological constants assumed for the discrete-clock estimate: $H_0 = 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$ and Planck length $l_P = 1.616 \times 10^{-35}\,\mathrm{m}$ (assumed values; the paper derives all consequences from them).

### 4.2 Finite recollapse in a closed dust universe

The Friedmann energy equation for dust with curvature, written for the normalized scale factor $x = a/a_0$, is

$$\left(\frac{dx}{dt}\right)^{2} = H_0^{2}\left(\frac{\Omega_0}{x} - (\Omega_0 - 1)\right).$$

Recollapse occurs where $\frac{dx}{dt} = 0$, i.e. where $\frac{\Omega_0}{x} = \Omega_0 - 1$. Solving,

$$x_{\max} = \frac{a_{\max}}{a_0} = \frac{\Omega_0}{\Omega_0 - 1}.$$

**Case $\Omega_0 = 1.2$.** Then $\Omega_0 - 1 = 0.2$ and

$$a_{\max}/a_0 = \frac{1.2}{0.2} = 6.$$

With dust scaling $\rho \propto a^{-3}$, the density at recollapse is

$$\rho(a_{\max}) = \rho_0 \left(\frac{a_0}{a_{\max}}\right)^{3} = \rho_0 \left(\frac{1}{6}\right)^{3} = \frac{\rho_0}{216} \approx 4.63 \times 10^{-3}\,\rho_0.$$

The recollapse point is therefore reached at a finite scale factor with a finite, indeed small, density; the divergence in this model sits at the endpoints $a \to 0$, which Section 4.3 re-parametrizes.

**Case $\Omega_0 = 1.0005$.** Then $\Omega_0 - 1 = 0.0005 = 5 \times 10^{-4}$ and

$$a_{\max}/a_0 = \frac{1.0005}{0.0005} = 2001.$$

The density at recollapse is

$$\rho(a_{\max}) = \frac{\rho_0}{2001^{3}}.$$

Computing $2001^{3}$: $2001 \times 2001 = 4{,}004{,}001$; $4{,}004{,}001 \times 2001 = 8{,}012{,}006{,}001 \approx 8.012 \times 10^{9}$. Hence

$$\rho(a_{\max}) = \frac{\rho_0}{8.012 \times 10^{9}} \approx 1.25 \times 10^{-10}\,\rho_0.$$

As $\Omega_0 \to 1^{+}$, $a_{\max} \to \infty$ while the density at recollapse tends to zero: the "infinity" approached in the linear scale-factor chart is reached through a family of entirely finite states.

### 4.3 Angular re-parametrization of density

Define the angular representation of density by

$$\frac{\rho}{\rho_c} = \tan\left(\frac{\theta}{2}\right), \qquad \theta \in [0, \pi].$$

The finite cyclic state $\theta = \pi$ corresponds to $\rho \to \infty$ in the linear chart: the divergence is generated by the map, not carried by the state. To evaluate how the divergence is approached, take $\theta = \pi - 10^{-3}$. Then $\theta/2 = \pi/2 - 5 \times 10^{-4}$, and

$$\tan\left(\frac{\pi}{2} - x\right) = \cot x \approx \frac{1}{x} - \frac{x}{3}.$$

With $x = 5 \times 10^{-4}$:

$$\cot(5 \times 10^{-4}) \approx \frac{1}{5 \times 10^{-4}} - \frac{5 \times 10^{-4}}{3} = 2000 - 1.67 \times 10^{-4} \approx 1999.99983.$$

Thus at $\theta = \pi - 10^{-3}$ the linear-chart density is $\rho/\rho_c \approx 2000$, while the angular state is finitely distant ($10^{-3}$ rad) from the cycle endpoint. The infinity in $\rho$ is a property of the $\tan$ chart's pole, exactly as the infinity at the Big Bang is a property of the linear scale-factor chart's endpoint $a = 0$.

### 4.4 Audit of the singularity-theorem hypotheses

The Penrose–Hawking theorems conclude geodesic incompleteness from two classes of hypothesis: an energy condition and a global-structure condition such as a trapped surface or a compact past set. The conclusion is that some timelike or null geodesic cannot be extended in an affine parameter $\lambda$ over all of $\mathbb{R}$. Each element of this structure can be examined for dependence on the linear, unbounded number line.

The conclusion is the clearest case. Geodesic incompleteness means that the affine parameter $\lambda$ of some geodesic has a finite bound, say $\lambda < \lambda_{\max}$, with no extension beyond it. In the standard chart $\lambda \in \mathbb{R}$, this is a statement about an unbounded linear parameter. Apply the angular re-parametrization

$$\theta(\lambda) = 2\arctan(\lambda), \qquad \theta \in (-\pi, \pi).$$

Every finite value of $\lambda$, including the endpoint $\lambda_{\max}$, maps to a finite angle $\theta < \pi$; the "incompleteness" becomes the statement that $\theta$ approaches but does not reach $\pi$, which is a boundary of the chart $S^{1}$-with-endpoint, not a divergence of any physical quantity. The hypotheses are less immediately chart-dependent: an energy condition is an inequality on the stress-energy tensor, and a trapped surface is a condition on the expansion scalars $\theta_{\pm}$ of null congruences, both of which are local and finite where they hold. The audit therefore localizes the representation-sensitivity precisely: the *hypotheses* are chart-robust inequalities, while the *conclusion* is a statement about an affine parameter ranging over $\mathbb{R}$ and is representation-sensitive. A cyclic reformulation must keep the hypotheses and replace the conclusion's unbounded parameter with a bounded one; whether the resulting statement has the same physical content is the open question that Section 6 discusses.

### 4.5 Discrete clock spanning the Hubble radius

Assume a discrete clock whose ticks are separated by the Planck length $l_P = 1.616 \times 10^{-35}\,\mathrm{m}$ and which spans one Hubble radius. The Hubble radius is $D_H = c/H_0$. With $H_0 = 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$:

$$H_0 = 67.4 \times 10^{3}\,\mathrm{m\,s^{-1}}\ /\ (3.0857 \times 10^{22}\,\mathrm{m}) = 2.184 \times 10^{-18}\,\mathrm{s^{-1}},$$

$$D_H = \frac{c}{H_0} = \frac{2.998 \times 10^{8}\,\mathrm{m\,s^{-1}}}{2.184 \times 10^{-18}\,\mathrm{s^{-1}}} = 1.373 \times 10^{26}\,\mathrm{m}.$$

The number of Planck-spaced states across the Hubble radius is

$$N = \frac{D_H}{l_P} = \frac{1.373 \times 10^{26}\,\mathrm{m}}{1.616 \times 10^{-35}\,\mathrm{m}} = \frac{1.373}{1.616} \times 10^{61} = 0.8496 \times 10^{61} \approx 8.50 \times 10^{60}.$$

This is a finite integer-scale number. In the discrete representation of Section 3.2, the clock state is $k \in \{0, \dots, N-1\}$ with wraparound $k \mapsto (k+1) \bmod N$; an "epoch transition" is the wraparound event $k = N-1 \mapsto k = 0$, which is by construction a finite state change. No state of this clock is infinitely distant from any other, so no configuration of the clock can represent a singularity. The number $N \approx 8.50 \times 10^{60}$ is the finite budget within which any cyclic construction must fit the observable universe's history.

### 4.6 Horizon consistency check

[7] derives, for a concordance universe with cosmological constant and dust, the horizon-recession equations

$$\frac{dH_p}{dt} = H_p(z)H(z) + 1, \qquad \frac{dH_e}{dt} = H_e(z)H(z) - 1,$$

where $H_p$ and $H_e$ are the particle and event horizons and $H_p H$ and $H_e H$ are their recession velocities; [7] notes these results are independent of the current values of the involved constants. A stationary event horizon satisfies $\frac{dH_e}{dt} = 0$, i.e. $H_e H = 1$, i.e. $H_e = 1/H$. Restoring the factor of $c$ (in the units of [7] the horizon is measured with $c = 1$), the stationary solution is

$$D_e = \frac{c}{H} \;\longrightarrow\; D_e = \frac{c}{H_0} \quad \text{at the present epoch}.$$

This is exactly the de Sitter event horizon computed in Section 4.5:

$$D_e = \frac{c}{H_0} = 1.373 \times 10^{26}\,\mathrm{m}.$$

Converting to light-years, with $1\,\mathrm{Gly} = 9.461 \times 10^{24}\,\mathrm{m}$:

$$D_e = \frac{1.373 \times 10^{26}}{9.461 \times 10^{24}}\,\mathrm{Gly} = 14.5\,\mathrm{Gly}.$$

The check passes: the pure de Sitter event horizon is the stationary solution of the recession equation of [7], so the finite horizon scale used in the discrete-clock construction is consistent with the standard horizon dynamics rather than an ad hoc input.

### 4.7 Observational anchor: the dipole ratio

[6] forecasts, from a set of 100 mock simulations at a flux density threshold of $22.8\,\mu\mathrm{Jy}$ at $700\,\mathrm{MHz}$, a kinematic radio dipole amplitude $A = 0.0046$ pointing to the CMB dipole direction, with a large-scale-structure contribution of mean amplitude $A = 0.0031 \pm 0.0016$. Define the ratio

$$R = \frac{A_{\mathrm{kin}}}{A_{\mathrm{LSS}}} = \frac{0.0046}{0.0031} = 1.4839 \approx 1.48.$$

Propagate the uncertainty of $A_{\mathrm{LSS}}$ (taking $A_{\mathrm{kin}}$ as exact, since [6] gives it without an uncertainty):

$$\sigma_R = \left|\frac{\partial R}{\partial A_{\mathrm{LSS}}}\right| \sigma_A = \frac{A_{\mathrm{kin}}}{A_{\mathrm{LSS}}^{2}}\,\sigma_A = \frac{0.0046}{(0.0031)^{2}} \times 0.0016.$$

Computing: $(0.0031)^{2} = 9.61 \times 10^{-6}$; $\frac{0.0046}{9.61 \times 10^{-6}} = 478.7$; $\sigma_R = 478.7 \times 0.0016 = 0.766 \approx 0.76$. Hence

$$R = 1.48 \pm 0.76.$$

The interpretation for this paper: the kinematic dipole is a representation-independent signal of our motion, while the large-scale-structure dipole depends on the assumed luminosity functions, spectral energy distributions, bias and evolution of radio sources, as [6] states. A discriminator between "transition" and "termination" readings of cosmological data must therefore beat a forecast floor in which the LSS contaminant is of the same order as the kinematic signal ($R \approx 1.5$ with order-unity uncertainty). Any cyclic-versus-singular signature at the level of a few $10^{-3}$ in source counts sits inside this floor, which sets the required survey depth.

## 5. Results

The derivations of Section 4 yield the following results, each with its arithmetic shown there.

1. **Finite recollapse.** For a closed dust universe, $a_{\max}/a_0 = \Omega_0/(\Omega_0 - 1)$. At $\Omega_0 = 1.2$: $a_{\max} = 6\,a_0$ and $\rho(a_{\max}) = \rho_0/216 \approx 4.63 \times 10^{-3}\,\rho_0$. At $\Omega_0 = 1.0005$: $a_{\max} = 2001\,a_0$ and $\rho(a_{\max}) = \rho_0/8.012 \times 10^{9} \approx 1.25 \times 10^{-10}\,\rho_0$ (Section 4.2).
2. **Angular representation.** Under $\rho/\rho_c = \tan(\theta/2)$, the finite state $\theta = \pi$ maps to $\rho \to \infty$; at $\theta = \pi - 10^{-3}$, $\rho/\rho_c \approx 1999.99983 \approx 2000$ (Section 4.3).
3. **Chart-sensitivity of geodesic incompleteness.** Under $\theta(\lambda) = 2\arctan(\lambda)$, the unbounded affine parameter becomes a bounded angle, so the theorem's conclusion is representation-sensitive while its hypotheses are chart-robust inequalities (Section 4.4).
4. **Finite state count.** A Planck-spaced clock across the Hubble radius has $N = c/(H_0\,l_P) \approx 8.50 \times 10^{60}$ states, with epoch transitions as finite wraparound events (Section 4.5).
5. **Horizon consistency.** The de Sitter event horizon $D_e = c/H_0 = 1.373 \times 10^{26}\,\mathrm{m} \approx 14.5\,\mathrm{Gly}$ is the stationary solution of the event-horizon recession equation of [7] (Section 4.6).
6. **Observational floor.** The ratio of the SKA1 forecast kinematic dipole to the large-scale-structure dipole is $R = 1.48 \pm 0.76$ (Section 4.7).

All six are derived or are direct consequences of stated inputs; none is an empirical measurement by this paper.

## 6. Discussion

The central claim of this paper is representational, not dynamical: the infinities of the singularity theorems live in the choice of chart (an affine parameter over $\mathbb{R}$, a density on the extended real line), and explicit maps move them to finite states. The strongest support is the angular re-parametrization of Section 4.3, which is an exact construction, and the recollapse family of Section 4.2, which shows the linear chart's "infinity" approached through a continuum of finite states as $\Omega_0 \to 1^{+}$.

The claim has clear limits, and the first is the one the paper itself states: the toy models are kinematic, not solutions of Einstein's equations with realistic matter. [1] records the structural obstacle: within General Relativity a non-singular cyclic model requires a non-conventional fluid with negative effective energy density, which usually leads to quantum instabilities and makes the theory ill-defined, and the promising route is extended Einstein gravity. Nothing in Sections 4.2–4.5 addresses this; the recollapse model is dust-only, has no bounce mechanism, and the angular map of Section 4.3 is a change of variables, not a dynamical statement that the universe passes through $\theta = \pi$. A critic can therefore accept every derivation here and still hold that the singularity theorems describe a genuine dynamical endpoint, because the theorems' hypotheses (energy conditions, trapped surfaces) are exactly what a cyclic universe must violate or evade, per the constraint recorded in [1].

**What would falsify the main result.** The main result is that the divergences are chart artifacts. It would be falsified by a demonstration that some invariant, chart-independent quantity — e.g. a curvature scalar or a geodesic length computed in a manifestly finite representation — diverges in a way that no re-parametrization can remove, or equivalently that the wraparound construction of Section 4.5 cannot be made dynamical without reintroducing an unbounded parameter in the equations of motion. A concrete falsifying observation would be a measured curvature maximum in a collapse or bounce scenario that grows without bound as resolution increases in *every* finite-state representation, not just the linear one.

**Limitations list.**

- *Kinematic toy models.* The recollapse and clock models are not solutions with realistic matter; the recollapse density $\rho_0/216$ is a consequence of the dust assumption and changes with the equation of state.
- *Assumed constants.* $\Omega_0 = 1.2$ and $\Omega_0 = 1.0005$ are free inputs, not measurements; $H_0 = 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$ and $l_P = 1.616 \times 10^{-35}\,\mathrm{m}$ are assumed. The state count $N \approx 8.50 \times 10^{60}$ scales linearly with $H_0^{-1}$ and $l_P^{-1}$, so a different $H_0$ shifts it proportionally.
- *Angular map is local.* The map $\rho/\rho_c = \tan(\theta/2)$ is exhibited for density only; no proof is given that all quantities of a collapse spacetime admit a common bounded parametrization simultaneously.
- *Dipole ratio.* $R = 1.48 \pm 0.76$ uses the mock-based forecast of [6], which depends on assumed luminosity functions, spectral energy distributions, bias and evolution of radio sources; it is a forecast floor, not a measurement.
- *No dynamical bounce.* The paper does not construct a bounce; [1] shows that doing so within GR requires negative-effective-energy matter with quantum-instability problems, and that the whole discussion assumes homogeneity, which may not hold according to Sloan Digital Sky Survey analysis.
- *Open questions.* Whether the Penrose-style conformal boundary structure survives the angular re-parametrization; whether entropy transfer between aeons can be defined on the finite clock; whether the audit of Section 4.4 extends to the full hypothesis set of all singularity theorems.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are theoretical cosmologists and gravitational-wave/large-scale-structure observationalists. If the representational claim holds, model builders change a design parameter: they choose parametrizations in which every observable is bounded (angles, finite clocks) rather than unbounded linear variables, and singularity-avoidance becomes a representational requirement rather than a matter-content requirement. Observationalists change a target: instead of searching for divergences, they search for finite curvature maxima and Penrose-style conformal boundaries, with the dipole-ratio floor $R = 1.48 \pm 0.76$ from Section 4.7 defining the precision that a cyclic-versus-singular discriminator must reach in radio source counts.

**(b) Readiness.** This is purely analytical work that has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). No claim above TRL 3 is made, and no manufacturing readiness is implied.

**(c) Smallest next test.** The smallest de-risking calculation is a numerical simulation of the discrete clock of Section 4.5 coupled to a recollapse dynamics: evolve the finite state $k \mapsto (k+1) \bmod N$ through a collapse–wraparound–re-expansion cycle and measure whether a curvature proxy remains bounded across the wraparound for at least one full cycle. The outcome that would refute the program is a curvature proxy that diverges as the clock resolution is refined, in the finite representation itself. On the observational side, the smallest test is a source-count dipole measurement with the SKA1 Medium-Deep Band 2 survey, whose weak-lensing constraints [6] shows are comparable to Stage III optical surveys such as DES, with radio–optical cross-correlations retaining almost all statistical power; a measured dipole ratio $R$ inconsistent with $1.48 \pm 0.76$ at forecast uncertainty would undermine the use of [6]'s mocks as the floor.

**(d) Binding constraints.** The first binding constraint is computational: a clock with $N \approx 8.50 \times 10^{60}$ states cannot be simulated state-by-state, so any simulation must work with coarse-grained or symbolic dynamics, and the fidelity of that coarse-graining is an open question. The second is data: the dipole forecast of [6] depends on assumed luminosity functions, spectral energy distributions, bias and evolution of radio sources, so the observational floor is only as good as those assumptions. The third is theoretical: per [1], any dynamical realization within GR needs negative-effective-energy matter with quantum-instability problems, so the engineering pathway runs through modified gravity, whose viability must be checked against large-scale-structure constraints of the kind [8] derives for curvature, warm dark matter and running vacuum energy.

**(e) Order-of-magnitude bounds (projections).** With the assumptions of Section 4.5 ($H_0 = 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}$, $l_P = 1.616 \times 10^{-35}\,\mathrm{m}$), the finite state budget is $N \approx 8.50 \times 10^{60}$ and the horizon scale is $D_e \approx 14.5\,\mathrm{Gly}$; these are projections derived from the assumed constants, and $N$ shifts in proportion to any change in $H_0$ or $l_P$. No cost figures are derivable from the inputs of this paper and none is asserted.

**(f) Risks and misuse paths.** The representational claim could be misread as claiming that singularities are "not real" in an operational sense, which the paper does not establish; the constructions show chart-dependence of specific divergences, not the physical harmlessness of the states they label. Overstating the discrete-clock result as evidence for a specific quantum-gravity ontology would be unsupported: the state count $N$ is a kinematic budget, not a theory of what the states are.

## 8. Conclusion

This paper tested the conjecture that the actual infinities of gravitational physics are artifacts of the linear, unbounded number line. The constructive results are: an angular re-parametrization under which the divergent density of a singularity becomes a finite state ($\rho/\rho_c \approx 2000$ at $\theta = \pi - 10^{-3}$); a finite-recollapse family for a closed dust universe ($a_{\max} = 6\,a_0$ at $\Omega_0 = 1.2$, with $\rho(a_{\max}) = \rho_0/216$); an audit showing that geodesic incompleteness, the singularity theorems' conclusion, is representation-sensitive while their hypotheses are chart-robust inequalities; a finite state count $N \approx 8.50 \times 10^{60}$ for a Planck-spaced clock spanning the Hubble radius, consistent with the horizon dynamics of [7]; and an observational floor $R = 1.48 \pm 0.76$ from the SKA1 dipole forecasts of [6]. Together they make precise what it would mean for a "singularity" to be a transition between epochs rather than a physical infinity, and they define the two next steps: a wraparound simulation whose failure mode is a divergence that survives the finite representation, and a dipole measurement that tests the forecast floor. The philosophical position that "what is truly infinite may just be the abyss of our ignorance" [3] is here given a testable, arithmetic form.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.5-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Non-singular Cyclic Cosmology without Phantom Menace. arXiv:1108.6052v1. https://arxiv.org/abs/1108.6052v1
[2] Exact Classical Correspondence in Quantum Cosmology. arXiv:1405.7957v2. https://arxiv.org/abs/1405.7957v2
[3] Infinities as a measure of our ignorance. arXiv:1305.2358v1. https://arxiv.org/abs/1305.2358v1
[4] New Approach to Quantization of Cosmological Models. arXiv:gr-qc/0612079v4. https://arxiv.org/abs/gr-qc/0612079v4
[5] Field Fractal Cosmological Model As an Example of Practical Cosmology Approach. arXiv:0810.0162v2. https://arxiv.org/abs/0810.0162v2
[6] Cosmology with Phase 1 of the Square Kilometre Array; Red Book 2018: Technical specifications and performance forecasts. arXiv:1811.02743v1. https://arxiv.org/abs/1811.02743v1
[7] Evolution of the Cosmological Horizons in a Concordance Universe. arXiv:1302.1609v3. https://arxiv.org/abs/1302.1609v3
[8] Constraints from observational data for a running cosmological constant and warm dark matter with curvature. arXiv:2007.12636v2. https://arxiv.org/abs/2007.12636v2