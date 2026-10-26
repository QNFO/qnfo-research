# Zitterbewegung as an Archimedean–2-adic Adelic Mixing Signature: Spectral-Gap Formalization, Numerical Anchors, and a Falsifiable Simulation Program

## Abstract

Zitterbewegung (ZBW) — the trembling motion of a Dirac wave packet at angular frequency $\omega = 2mc^{2}/\hbar$ — is conventionally treated as an interference artifact of the Dirac Hamiltonian. We propose and partially formalize a stronger claim: ZBW is the observable trace of mixing between the Archimedean place $\mathbb{R}$ (denoted $\infty$) and the 2-adic place $\mathbb{Q}_2$ of the rationals, in the framework of adelic quantum mechanics. We (i) prove a spectral-gap proposition showing that any operator coupling an $\infty$-localized sector to a $p$-adic sector forces an oscillation at $\Delta E/\hbar$, with the exact two-level frequency $\Omega = \sqrt{(\Delta E)^2 + 4|g|^2}/\hbar$; (ii) derive the electron ZBW frequency $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ and reduced Compton wavelength $3.8616 \times 10^{-13}\,\mathrm{m}$ with full arithmetic; (iii) argue that the prime 2 is structurally distinguished because the Bruhat–Tits tree of $\mathbb{Q}_2$ is 3-regular, the smallest degree any prime admits; and (iv) specify a trapped-ion Dirac simulation test, labeled throughout as a projection, in which the oscillation amplitude is regressed against a 2-adic delocalization measure $\mu_2(2^n\mathbb{Z}_2) = 2^{-n}$, yielding a projected factor-of-$4$ suppression per confinement step. We report no new experimental data; every quantitative result is computed here from stated constants or explicitly flagged as a projection with stated assumptions.

## 1. Introduction

The position operator of relativistic quantum mechanics is notoriously ill-behaved: a wave-packet solution of the Dirac equation exhibits velocity eigenvalues $\pm c$ and a rapid oscillation at the Compton scale, named Zitterbewegung ("trembling motion") by Schrödinger [8]. The standard reading is that this trembling is an interference artifact of superposing positive- and negative-energy branches of the Dirac Hamiltonian, with no independent physical content.

This paper develops an alternative reading, taken from a research program on adelic physics [10, 11]: ZBW is a signature of mixing between the Archimedean place $\mathbb{R}$ and the 2-adic place $\mathbb{Q}_2$. In adelic quantum mechanics, wave functions may carry complex values on $p$-adic and adelic arguments, and the Archimedean and non-Archimedean places are treated on an equal footing [1]. Under this reading, a wave packet localized at an Archimedean position $x_{\infty}$ necessarily carries Fourier components that are delocalized on $\mathbb{Q}_2$, and the Compton-scale oscillation at $\omega = 2E/\hbar$ is the observable trace of the $\infty \leftrightarrow 2$ channel.

The claim matters because it would give a basis-independent, number-theoretic origin for a relativistic quantum phenomenon. It is also falsifiable: if a $p \geq 3$ sector reproduces the observed amplitude scaling, or if the oscillation amplitude in a controlled Dirac simulator fails to track a 2-adic delocalization measure, the claim fails.

Our contributions are:

1. **A spectral-gap proposition** (Section 3): any operator coupling an $\infty$-localized sector to a $p$-adic sector with gap $\Delta E$ forces oscillations at $\Omega/\hbar \geq \Delta E/\hbar$. This is elementary but makes the mixing claim precise enough to test.
2. **A necessity argument from the adelic product formula** (Section 4): Archimedean localization cannot be "pure" in the adelic sense; some $p$-adic norm must be nontrivial.
3. **A structural-selection argument for $p = 2$**: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular, so $p = 2$ gives degree $3$, the smallest possible among primes.
4. **Explicit numerical anchors** (Section 4): the electron ZBW frequency, reduced Compton wavelength, 2-adic ball measures, and mixing-amplitude tables, all computed with shown arithmetic.
5. **A simulation protocol** (Sections 3 and 5), labeled as a projection: a trapped-ion Dirac simulator in the style named in the source research idea, in which the Compton-scale oscillation amplitude is regressed against an engineered 2-adic delocalization measure.

We emphasize the epistemic status of each result: items 1–4 are mathematical derivations or computations from stated constants; item 5 is a design and a projection, not a measurement.

## 2. Background and Related Work

**Adelic and $p$-adic quantum mechanics.** Reference [1] reviews the emergence of $p$-adic mathematical physics from attempts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and describes the successful formulation of $p$-adic and adelic quantum mechanics with complex-valued wave functions of $p$-adic and adelic arguments respectively. This is the mathematical framework in which our $\infty \leftrightarrow 2$ mixing channel is defined: the adelic wave function is a single object with an Archimedean factor and $p$-adic factors, so "mixing" between places is meaningful rather than a category error. Dragovich's review [2] surveys applications of non-Archimedean geometry, $p$-adic numbers, and adeles in modern mathematical physics; we use it as evidence that adelic methods are an established, if minority, toolset, and we note that its supplied summary is a brief review giving no specific results we can lean on quantitatively.

**Arithmetic equidistribution and adelic measures.** Reference [3] concerns quasi-adelic measures on $\mathbb{P}^1$: it records that Baker–Rumely and Favre–Rivera-Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure, and that Chambert–Loir proved a more general version for curves. The relevance to us is methodological: adelic measures on projective spaces provide a rigorous way to speak about how mass distributes across places, which is exactly the bookkeeping our delocalization measure imitates at a toy level. The supplied summary describes the theorems but not their proofs' details, so we cite it only for the existence of this equidistribution framework.

**Fractal strings and complex dimensions.** Reference [4] surveys the theory of complex dimensions of real (Archimedean) fractal strings via the Cantor string and gives a detailed survey of $p$-adic (non-Archimedean) fractal strings, including an explicit volume formula for the tubular neighborhood of a $p$-adic fractal string. This matters because the geometry of $\mathbb{Q}_2$-supported sets — ultrametric, self-similar, tree-like — is precisely the geometry our 2-adic sector lives on, and this formalism is one of the few places where Archimedean and non-Archimedean fractal geometry are compared side by side.

**Arithmetic Hodge theory.** Reference [5] proves an arithmetic Hodge index theorem for adelic line bundles, extending prior results from number fields to finitely generated fields, and applies it to obtain a rigidity property of sets of preperiodic points of polarizable algebraic dynamical systems. We cite it as an example of the general pattern that adelic objects carry rigidity statements their local components lack — the same pattern our spectral-gap proposition instantiates locally: coupling to a $p$-adic sector constrains the Archimedean dynamics (forcing an oscillation) rather than merely decorating it.

**Adelic Lie theory.** Reference [6] proves that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) *is* the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential, and the work extends the definition of non-Archimedean dimension. This supplies the group-theoretic language in which a "phase oscillation across places" can be stated: an adelic torus carries both an Archimedean circle factor and $p$-adic factors, and the exponential sequence governs how phases lift. We use no results beyond the categorical equivalence and the exponential sequence stated in its summary.

**Non-Archimedean Hilbert-space geometry.** Reference [7] proves continuous non-Archimedean (resp. $p$-adic) Banach space and Hilbert space versions of Welch bounds previously proved by M. Krishna, and formulates continuous non-Archimedean and $p$-adic functional Zauner conjectures. For us this is a sanity check that the Hilbert-space formalism (inner products, frames, coherence bounds) survives the passage to $\mathbb{Q}_2$, which our model of a delocalized 2-adic sector requires.

**Zitterbewegung.** Reference [8] records the historical core: around 1930, Breit and Schrödinger showed that the velocity eigenvalues of Dirac wave-packet solutions are simply $\pm c$, leading Schrödinger to coin "Zitterbewegung" for the resulting trembling motion of fermions at the speed of light. The supplied summary is truncated mid-sentence, so we cannot cite it for any further results; we use it only for the historical framing and the $\pm c$ velocity-eigenvalue fact, both of which we re-derive in Section 4.

**The QNFO research chain.** Reference [9] computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement — directly relevant because it shows ZBW observables can carry topological, not merely kinematic, content, consistent with our $\mathbb{Z}_2$-flavored ($\infty \leftrightarrow 2$) channel. Reference [10] locates the structural underdetermination of the relativistic position operator in a "Silent Parameter Principle," notes that $\mathrm{SU}(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and states that the 2-adic ZBW frequency deviates from the Archimedean value; its supplied summary is cut off before quantifying the deviation, so we treat the existence (not the magnitude) of that deviation as its claim. Reference [11] consolidates a six-paper adelic physics chain — ZBW as a $p$-adic observable, Majorana correlators, Bruhat–Tits readout protocols, $p$-adic anyon braiding, and Ostrowski-based quantum error correction — into a unified research program, of which this paper is a sharpened, falsifiable fragment. Finally, [12] reports that five independent research programs converge on the structural insight that ultrametric (non-Archimedean) mathematics provides the correct state-space geometry for fundamental physics, quantum computation, and optimization; we cite it as corpus-level motivation, not as evidence for any specific claim of ours.

Collectively, these works establish that adelic and non-Archimedean structures are mathematically robust and already applied to quantum-mechanical contexts. None of the cited papers directly formalizes mixing between the Archimedean and 2-adic sectors as a spectral-gap statement with a falsifiable amplitude test, leaving the gap this study addresses.

## 3. Methods

### 3.1 Adelic setup

Let $\mathbb{A}_{\mathbb{Q}}$ be the adele ring of $\mathbb{Q}$, with places $\infty$ (Archimedean, $\mathbb{R}$) and primes $p$ ($\mathbb{Q}_p$). Following the adelic quantum-mechanics framework [1], a state is a complex wave function $\Psi = (\psi_{\infty}, \psi_2, \psi_3, \ldots)$ with $\psi_{\infty} \in L^2(\mathbb{R})$ and $\psi_p \in L^2(\mathbb{Q}_p)$, the latter equipped with the standard $p$-adic Hilbert-space structure whose existence is confirmed by the non-Archimedean Welch bounds of [7]. The $p$-adic sector inherits ultrametric, tree-like geometry: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular.

We work with a two-sector truncation,

$$
\mathcal{H} = \mathcal{H}_{\infty} \oplus \mathcal{H}_2,
$$

with a mixing Hamiltonian

$$
H = \begin{pmatrix} H_{\infty} & V \\ V^{\dagger} & H_2 \end{pmatrix}, \qquad V: \mathcal{H}_{\infty} \to \mathcal{H}_2 .
$$

### 3.2 Spectral-gap proposition

**Proposition (mixing forces oscillation).** Let $H_{\infty}$ and $H_2$ have reference energies $E_{\infty}$ and $E_2$ with gap $\Delta E = |E_2 - E_{\infty}| > 0$, and let $V \neq 0$ couple the sectors with off-diagonal matrix element $g = \langle \infty | V | 2 \rangle$. Then an initial state localized in $\mathcal{H}_{\infty}$ evolves with a component oscillating between sectors at angular frequency

$$
\Omega = \frac{\sqrt{(\Delta E)^2 + 4|g|^2}}{\hbar} \;\geq\; \frac{\Delta E}{\hbar}.
$$

*Derivation.* In the two-level reduction, the Hamiltonian on the subspace spanned by one state from each sector is

$$
H = \begin{pmatrix} E_{\infty} & g \\ g^* & E_2 \end{pmatrix}.
$$

Diagonalizing, the eigenvalues are $E_{\pm} = \tfrac{1}{2}(E_{\infty} + E_2) \pm \tfrac{1}{2}\sqrt{(\Delta E)^2 + 4|g|^2}$, so the splitting is $E_+ - E_- = \sqrt{(\Delta E)^2 + 4|g|^2}$. The probability of returning to the $\infty$-sector is the standard two-level Rabi formula

$$
P_{\infty}(t) = 1 - \frac{4|g|^2}{(\Delta E)^2 + 4|g|^2}\sin^2\!\left(\frac{\Omega t}{2}\right),
$$

which oscillates at $\Omega/\hbar$. In the weak-coupling limit $|g| \ll |\Delta E|$, $\Omega \to \Delta E/\hbar$. In the free Dirac theory the positive- and negative-energy branches are split by $2E_p$ with $E_p = \sqrt{m^2c^4 + p^2c^2}$, so $\Delta E = 2E_p$ and $\omega_{\mathrm{mix}} = 2E_p/\hbar$, reproducing the ZBW frequency [8]. $\square$

This proposition is deliberately modest: it says mixing *forces* an oscillation at the gap frequency; it does not say the observed ZBW frequency *fixes* the mixing partner. That inference — that the coincidence $\Delta E = 2E_p$ is causal rather than accidental — is the hypothesis under test.

### 3.3 The 2-adic delocalization measure

Let $\mu_2$ be the Haar measure on $\mathbb{Q}_2$ normalized by $\mu_2(\mathbb{Z}_2) = 1$, where $\mathbb{Z}_2 = \{x \in \mathbb{Q}_2 : |x|_2 \leq 1\}$ is the ring of 2-adic integers. The ball of radius $2^{-n}$ is $2^n\mathbb{Z}_2$, and $\mathbb{Z}_2 / 2^n\mathbb{Z}_2$ has exactly $2^n$ cosets, so

$$
\mu_2(2^n \mathbb{Z}_2) = 2^{-n}.
$$

We define the 2-adic delocalization measure of a packet whose 2-adic support is confined to the ball $2^n\mathbb{Z}_2$ as $D_2(n) = 2^{-n}$: tighter 2-adic confinement (larger $n$) means smaller delocalization measure. This mirrors the Archimedean/$p$-adic fractal-string comparison of [4], where tubular volumes of $p$-adic strings are computed explicitly. A complementary dimensionless weight for a full two-sector state,

$$
\mu_2(\Psi) = \frac{\|\hat{\psi}_2\|_{2}^{2}}{\|\hat{\psi}_{\infty}\|^{2} + \|\hat{\psi}_2\|_{2}^{2}} \in [0,1],
$$

with $\hat{\psi}_2$ the 2-adic Fourier transform (defined via the standard additive character on $\mathbb{Q}_2$ [1]), serves as the regression variable in the simulation protocol; the equidistribution framework for adelic measures [3] is the rigorous analogue of this bookkeeping on $\mathbb{P}^1$.

### 3.4 Bruhat–Tits tree regularity and prime selection

For a non-Archimedean local field $\mathbb{Q}_p$, the Bruhat–Tits tree is $(p+1)$-regular: each vertex has $p+1$ incident edges. For $p = 2$ the valence is $2 + 1 = 3$, the smallest possible valence among primes. In the Proposition of Section 3.2 the frequency $\Omega$ depends only on $\Delta E$ and $g$, not on $p$; hence the model predicts that no prime other than 2 changes the frequency scaling, and prime selection can only manifest through the coupling amplitude $g$ (Section 4.4). This is the falsifiable content of the prime-comparison test.

### 3.5 Trapped-ion test protocol (projection)

We propose a hypothetical trapped-ion-style Dirac simulator, explicitly labeled as a design and not attributed to any cited experimental platform: a single ion whose internal states encode the Dirac spinor, with laser-driven couplings implementing the Dirac Hamiltonian and an effective rest energy $\Delta_{\mathrm{eff}}$ playing the role of $mc^2$, so the simulated ZBW frequency is $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar$. The protocol: (a) prepare a wave packet with controlled 2-adic delocalization $D_2(n)$ (implemented as a tunable delocalization parameter in the simulator); (b) measure the ZBW oscillation amplitude $A(n)$; (c) test the model's projection $A(n) \propto 4^{-n}$ (Section 4.3); (d) vary the tree-valence analogue of the coupling geometry and check that the frequency $\omega_{\mathrm{sim}}$ is unchanged, as the Proposition requires.

## 4. Analysis

All constants below are standard values stated here as inputs; every arithmetic step is shown.

**Input constants.** Electron rest mass $m_e = 9.1093837 \times 10^{-31}\,\mathrm{kg}$; speed of light $c = 2.99792458 \times 10^{8}\,\mathrm{m\,s^{-1}}$ (exact, SI definition); reduced Planck constant $\hbar = 1.054571817 \times 10^{-34}\,\mathrm{J\,s}$.

**Derivation 1: electron rest energy.**

$$
E_0 = m_e c^2 = \left(9.1093837 \times 10^{-31}\right) \times \left(2.99792458 \times 10^{8}\right)^2 .
$$

First, $c^2 = (2.99792458)^2 \times 10^{16} = 8.98755179 \times 10^{16}\,\mathrm{m^2\,s^{-2}}$. Then

$$
E_0 = 9.1093837 \times 8.98755179 \times 10^{-31+16} = 81.871058 \times 10^{-15} = 8.1871058 \times 10^{-14}\,\mathrm{J}.
$$

**Derivation 2: ZBW angular and ordinary frequency.** The Dirac positive/negative branch splitting at rest ($p=0$, so $E_p = E_0$) is $2E_0$, so

$$
\omega_{\mathrm{ZBW}} = \frac{2E_0}{\hbar} = \frac{2 \times 8.1871058 \times 10^{-14}}{1.054571817 \times 10^{-34}}\,\mathrm{rad\,s^{-1}}.
$$

Numerator: $2 \times 8.1871058 \times 10^{-14} = 1.63742116 \times 10^{-13}\,\mathrm{J}$. Dividing:

$$
\omega_{\mathrm{ZBW}} = \frac{1.63742116}{1.054571817} \times 10^{-13+34} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}.
$$

In cycles per second:

$$
f_{\mathrm{ZBW}} = \frac{\omega_{\mathrm{ZBW}}}{2\pi} = \frac{1.55268 \times 10^{21}}{6.283185307} = 2.4710 \times 10^{20}\,\mathrm{Hz}.
$$

**Derivation 3: reduced Compton wavelength.**

$$
\lambda_C = \frac{\hbar}{m_e c} = \frac{1.054571817 \times 10^{-34}}{(9.1093837 \times 10^{-31}) \times (2.99792458 \times 10^{8})}.
$$

Denominator: $9.1093837 \times 2.99792458 = 27.309245$, so $m_e c = 2.7309245 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$. Then

$$
\lambda_C = \frac{1.054571817}{2.7309245} \times 10^{-34+22} = 0.386159 \times 10^{-12} = 3.8616 \times 10^{-13}\,\mathrm{m}.
$$

A packet localized at $\sigma \sim \lambda_C$ has momentum spread $\Delta p \sim \hbar/(2\sigma) = 1.054571817 \times 10^{-34} / (2 \times 3.8616 \times 10^{-13}) = 1.054571817 \times 10^{-34} / 7.7232 \times 10^{-13} = 1.3654 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$, i.e. $\Delta p \sim m_e c/2$: localization at the Compton scale is exactly where the two Dirac branches become inseparable, which is why the mixing channel becomes observable there.

**Derivation 4: product-formula necessity.** For $x \in \mathbb{Q}^{\times}$, the adelic product formula reads

$$
|x|_{\infty} \prod_{p} |x|_p = 1 .
$$

Hence if $|x|_{\infty} \neq 1$, then $\prod_p |x|_p \neq 1$, so at least one prime $p$ has $|x|_p \neq 1$: nontrivial Archimedean scaling cannot be adelic-neutral; some $p$-adic norm must compensate. For the prime 2 specifically, $|2^n|_2 = 2^{-n}$, so the 2-adic norm is the most sensitive of all primes to dyadic (binary) structure — the same binary structure that underlies the two-branch (positive/negative energy) Dirac splitting. This is suggestive, not decisive; the decisive structural fact is Derivation 5.

**Derivation 5: minimality of the 2-adic tree.** The Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular. For $p = 2$: degree $= 2 + 1 = 3$. For $p = 3$: degree $= 4$. For any prime $p \geq 3$: degree $= p + 1 \geq 4 > 3$. Since 2 is the smallest prime, $\deg(T_2) = 3 < \deg(T_p)$ for all $p \neq 2$: the 2-adic tree is the unique minimal-degree Bruhat–Tits tree among primes. The number of vertices at distance $n$ from a fixed vertex in a 3-regular tree is $N(n) = 3 \cdot 2^{n-1}$ (each new vertex adds two further branches beyond its parent); for $n = 4$: $N(4) = 3 \times 2^{3} = 24$.

**Derivation 6: weak-coupling correction and modulation depth.** Take a model gap $\Delta E = 2E_0 = 1.63742116 \times 10^{-13}\,\mathrm{J}$ and a coupling $|g| = 10^{-3}\,\Delta E$ (assumption, for illustration). Then

$$
\sqrt{(\Delta E)^2 + 4|g|^2} = \Delta E \sqrt{1 + 4 \times 10^{-6}} \approx \Delta E \times 1.000002.
$$

So $\Omega = (\Delta E/\hbar) \times 1.000002$: the weak-coupling correction to the ZBW frequency is at the $2 \times 10^{-6}$ relative level, i.e. $\delta\omega = 2 \times 10^{-6} \times 1.55268 \times 10^{21} = 3.11 \times 10^{15}\,\mathrm{rad\,s^{-1}}$ — a frequency shift far beyond current spectroscopic resolution for free electrons, which is why the amplitude channel, not the frequency channel, is the experimentally accessible signature. The population modulation depth from the Rabi formula is

$$
A_{\mathrm{pop}} = \frac{4|g|^2}{(\Delta E)^2 + 4|g|^2} \approx \frac{4 \times 10^{-6}}{1 + 4 \times 10^{-6}} \approx 4.0 \times 10^{-6}.
$$

**Derivation 7: delocalization measure and amplitude projection (labeled projection).** From Section 3.3, $D_2(n) = 2^{-n}$. Explicit values: $D_2(0) = 1$; $D_2(1) = 0.5$; $D_2(2) = 0.25$; $D_2(3) = 0.125$; $D_2(10) = 2^{-10} = 9.77 \times 10^{-4}$. Assume the inter-sector coupling scales linearly with the delocalization measure, $|g|(n) = g_0\, 2^{-n}$, with $g_0$ a simulator-dependent constant. Then, in the weak-coupling regime,

$$
A_{\mathrm{pop}}(n) \approx \frac{4 g_0^2\, 2^{-2n}}{(\Delta E)^2} = A_0\, 4^{-n}, \qquad A_0 = \frac{4 g_0^2}{(\Delta E)^2}.
$$

Assumption for a concrete number: $g_0 = 10^{-3}\,\Delta E$, giving $A_0 = 4 \times 10^{-6}$. Then:

- $A_{\mathrm{pop}}(0) = 4 \times 10^{-6} \times 4^{0} = 4.0 \times 10^{-6}$;
- $A_{\mathrm{pop}}(1) = 4 \times 10^{-6} \times 4^{-1} = 1.0 \times 10^{-6}$;
- $A_{\mathrm{pop}}(2) = 4 \times 10^{-6} \times 4^{-2} = 2.5 \times 10^{-7}$;
- $A_{\mathrm{pop}}(3) = 4 \times 10^{-6} \times 4^{-3} = 6.25 \times 10^{-8}$;
- $A_{\mathrm{pop}}(10) = 4 \times 10^{-6} \times 4^{-10} = 4 \times 10^{-6} / 1048576 \approx 3.81 \times 10^{-12}$.

Each confinement step $n \to n+1$ suppresses the projected oscillation amplitude by a factor of $4$: this factor-of-$4$ suppression per step is the falsifiable projection of the model.

## 5. Results

All values below are computed in Section 4 from the stated input constants $m_e = 9.1093837 \times 10^{-31}\,\mathrm{kg}$, $c = 2.99792458 \times 10^{8}\,\mathrm{m\,s^{-1}}$, $\hbar = 1.054571817 \times 10^{-34}\,\mathrm{J\,s}$, or are explicitly labeled projections.

**Computed results (derivations, not projections).**

1. Electron rest energy: $E_0 = 8.1871058 \times 10^{-14}\,\mathrm{J}$ (Derivation 1).
2. ZBW angular frequency: $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$; ordinary frequency $f_{\mathrm{ZBW}} = 2.4710 \times 10^{20}\,\mathrm{Hz}$ (Derivation 2).
3. Reduced Compton wavelength: $\lambda_C = 3.8616 \times 10^{-13}\,\mathrm{m}$; the associated momentum spread at localization $\sigma \sim \lambda_C$ is $\Delta p \approx 1.3654 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}} \approx m_e c / 2$ (Derivation 3).
4. Weak-coupling frequency correction for $|g| = 10^{-3}\,\Delta E$: relative shift $2 \times 10^{-6}$, i.e. $\delta\omega \approx 3.11 \times 10^{15}\,\mathrm{rad\,s^{-1}}$, and population modulation depth $A_{\mathrm{pop}} \approx 4.0 \times 10^{-6}$ (Derivation 6; the coupling value is an illustrative assumption, the arithmetic is exact given it).
5. Tree combinatorics: $\deg(T_2) = 3 < \deg(T_p) = p+1$ for all primes $p \geq 3$; vertex count at distance $n = 4$ in the 3-regular tree is $N(4) = 24$ (Derivation 5).

**Projected results (labeled projections).** Under the stated assumptions $|g|(n) = g_0\,2^{-n}$ with $g_0 = 10^{-3}\,\Delta E$ and weak coupling $|g| \ll |\Delta E|$, the projected oscillation amplitude is $A_{\mathrm{pop}}(n) = 4 \times 10^{-6} \times 4^{-n}$:

| $n$ | $D_2(n) = 2^{-n}$ | $A_{\mathrm{pop}}(n)$ (projection) |
|---|---|---|
| 0 | $1$ | $4.0 \times 10^{-6}$ |
| 1 | $0.5$ | $1.0 \times 10^{-6}$ |
| 2 | $0.25$ | $2.5 \times 10^{-7}$ |
| 3 | $0.125$ | $6.25 \times 10^{-8}$ |
| 10 | $9.77 \times 10^{-4}$ | $3.81 \times 10^{-12}$ |

Uncertainty on these projections is dominated by the unknown simulator constant $g_0$; the factor-of-$4$ suppression per step is independent of $g_0$ within the assumed linear scaling. No experimental data are reported in this paper.

## 6. Discussion

**Limitations.** The spectral-gap Proposition is elementary two-level quantum mechanics; its only content is that mixing forces an oscillation at $\Omega/\hbar \geq \Delta E/\hbar$. The strong claim — that the observed ZBW frequency is caused by $\infty \leftrightarrow 2$ adelic mixing rather than by the standard positive/negative-energy interference of the Dirac Hamiltonian — is not derived here and is not fixed by the frequency coincidence $\Delta E = 2E_p$, which the standard theory already reproduces without any adelic input. The prime-selection argument via Bruhat–Tits valence is structural, not dynamical: since $\Omega$ is independent of $p$ in the Proposition, prime choice can only manifest through the coupling amplitude $g$, and we have no derivation that $g$ actually depends on the delocalization measure $D_2(n)$ as assumed in Derivation 7.

**Failure modes.** The program fails if (i) a simulator with a $p \geq 3$ sector reproduces the same amplitude scaling, contradicting the 2-adic specificity; (ii) the measured amplitude $A(n)$ in the trapped-ion protocol does not scale as $4^{-n}$ under the engineered delocalization parameter; or (iii) the frequency $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar$ changes when the coupling geometry is varied, contradicting the Proposition's $p$-independence.

**What would falsify the claims.** A direct demonstration that the ZBW amplitude is insensitive to the delocalization parameter while all other simulator settings are held fixed would falsify the mixing-amplitude hypothesis. Conversely, observation of the projected factor-of-$4$ suppression would not prove adelic mixing — it would only show consistency; the frequency channel is inaccessible ($\delta\omega \approx 3.11 \times 10^{15}\,\mathrm{rad\,s^{-1}}$ relative to $\omega_{\mathrm{ZBW}} \approx 1.55 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ is a $2 \times 10^{-6}$ relative shift, and absolute free-electron spectroscopy at this resolution is unavailable).

**Open questions.** Whether the linear ansatz $|g|(n) = g_0\,2^{-n}$ has a first-principles derivation; whether the adelic equidistribution framework of [3] can upgrade the toy measure $D_2(n)$ to a rigorous state on $\mathbb{P}^1$; and whether the $\mathbb{Z}_2$ topological distinction of the Majorana correlator result [9] connects to the $\infty \leftrightarrow 2$ channel beyond analogy.

## 7. Conclusion

We formalized Zitterbewegung as a candidate observable signature of mixing between the Archimedean place and the 2-adic place: a spectral-gap Proposition shows any such coupling forces an oscillation at $\Omega = \sqrt{(\Delta E)^2 + 4|g|^2}/\hbar$; explicit derivations give $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ and $\lambda_C = 3.8616 \times 10^{-13}\,\mathrm{m}$; the prime 2 is structurally minimal via its 3-regular Bruhat–Tits tree; and a trapped-ion protocol with projected factor-of-$4$ amplitude suppression per confinement step makes the claim falsifiable. The causal adelic interpretation remains a hypothesis; the simulation program is its test.

## References

[1] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[2] Non-Archimedean Geometry and Physics on Adelic Spaces. arXiv:math-ph/0306023v1. https://arxiv.org/abs/math-ph/0306023v1
[3] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$. arXiv:1502.04660v3. https://arxiv.org/abs/1502.04660v3
[4] The Geometry of p-Adic Fractal Strings: A Comparative Survey. arXiv:1105.2966v1. https://arxiv.org/abs/1105.2966v1
[5] The arithmetic Hodge index theorem for adelic line bundles II. arXiv:1304.3539v2. https://arxiv.org/abs/1304.3539v2
[6] Finite-Dimensional Protori Are Adelic Tori. arXiv:2411.16000v44. https://arxiv.org/abs/2411.16000v44
[7] Continuous Non-Archimedean and p-adic Welch Bounds. arXiv:2209.12833v1. https://arxiv.org/abs/2209.12833v1
[8] The Problem of Motion: The Statistical Mechanics of Zitterbewegung. arXiv:1411.1854v2. https://arxiv.org/abs/1411.1854v2
[9] https://papers.qnfo.org/papers/zbw-majorana-tqc-p2-majorana-zbw-correlator/. QNFO: Majorana Zitterbewegung Current Correlator: Vanishing ZBW Signal as a Z2 Topological Invariant.
[10] https://papers.qnfo.org/papers/zbw-adelic-observable/. QNFO: Zitterbewegung: From Archimedean Puzzle to Adelic Observable.
[11] https://papers.qnfo.org/papers/zbw-majorana-tqc-p7-grand-synthesis/. QNFO: The Adelic Physics Program: A Grand Synthesis.
[12] https://papers.qnfo.org/papers/wbs-6-five-pillars-consilient-synthesis/. QNFO: Five Pillars, One Structure: Consilient Convergence in QNFO Research.
