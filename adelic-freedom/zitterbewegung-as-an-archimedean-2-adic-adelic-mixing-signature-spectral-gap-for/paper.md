# Zitterbewegung as an Archimedean–2-adic Adelic Mixing Signature: Spectral-Gap Formalization, Numerical Anchors, and a Falsifiable Simulation Program

## Abstract

Zitterbewegung (ZBW) — the trembling motion of a Dirac wave packet at angular frequency $\omega = 2mc^{2}/\hbar$ — is conventionally treated as an interference artifact of the Dirac Hamiltonian, with no independent physical content. A gap remains: no existing framework makes precise, in a falsifiable way, what it would mean for ZBW to carry structure beyond that interference. We propose and partially formalize a stronger claim: ZBW is the observable trace of mixing between the Archimedean place $\mathbb{R}$ (denoted $\infty$) and the 2-adic place $\mathbb{Q}_2$ of the rationals, in the framework of adelic quantum mechanics. We (i) prove a spectral-gap proposition showing that any operator coupling an $\infty$-localized sector to a $p$-adic sector forces an oscillation at $\Delta E/\hbar$, with the exact two-level frequency $\Omega = \sqrt{(\Delta E)^2 + 4|g|^2}/\hbar$; (ii) derive the electron ZBW frequency $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ and reduced Compton wavelength $3.8616 \times 10^{-13}\,\mathrm{m}$ with full arithmetic; (iii) argue that the prime 2 is structurally distinguished because the Bruhat–Tits tree of $\mathbb{Q}_2$ is 3-regular, the smallest degree any prime admits; and (iv) specify a trapped-ion Dirac simulation test, labeled throughout as a projection, in which the oscillation amplitude is regressed against a 2-adic delocalization measure $\mu_2(2^n\mathbb{Z}_2) = 2^{-n}$, yielding a projected factor-of-$4$ suppression per confinement step. We report no new experimental data; every quantitative result is computed here from stated constants or explicitly flagged as a projection with stated assumptions. If the projection holds, ZBW amplitude becomes a number-theoretic diagnostic; if it fails, the adelic interpretation is eliminated.

## 1. Introduction

The position operator of relativistic quantum mechanics is notoriously ill-behaved: a wave-packet solution of the Dirac equation exhibits velocity eigenvalues $\pm c$ and a rapid oscillation at the Compton scale, named Zitterbewegung ("trembling motion") by Schrödinger after the work of Breit [8]. The standard reading is that this trembling is an interference artifact of superposing positive- and negative-energy branches of the Dirac Hamiltonian, with no independent physical content. This reading leaves practitioners without a decision procedure: an experimentalist building a Dirac simulator, or a theorist asking whether ZBW carries any invariant information, has no falsifiable alternative to the interference picture against which to calibrate an interpretation. What is missing is a precise statement of what non-interference structure would look like and a measurable quantity that could confirm or eliminate it.

This paper develops an alternative reading, taken from a research program on adelic physics [9, 10, 11]: ZBW is a signature of mixing between the Archimedean place $\mathbb{R}$ and the 2-adic place $\mathbb{Q}_2$. In adelic quantum mechanics, wave functions may carry complex values on $p$-adic and adelic arguments, and the Archimedean and non-Archimedean places are treated on an equal footing [1]. Under this reading, a wave packet localized at an Archimedean position $x_{\infty}$ necessarily carries Fourier components that are delocalized on $\mathbb{Q}_2$, and the Compton-scale oscillation at $\omega = 2E/\hbar$ is the observable trace of the $\infty \leftrightarrow 2$ channel.

The claim matters because it would give a basis-independent, number-theoretic origin for a relativistic quantum phenomenon. If it holds, the design of a Dirac-simulation experiment changes: the 2-adic delocalization of the simulated packet becomes a control knob whose setting predicts the oscillation amplitude, and the prime 2 acquires a dynamical, not merely conventional, role. It is also falsifiable: if a $p \geq 3$ sector reproduces the observed amplitude scaling, or if the oscillation amplitude in a controlled Dirac simulator fails to track a 2-adic delocalization measure, the claim fails.

Our contributions are:

1. **A spectral-gap proposition** (Section 3): any operator coupling an $\infty$-localized sector to a $p$-adic sector with gap $\Delta E$ forces oscillations at $\Omega/\hbar \geq \Delta E/\hbar$. This is elementary but makes the mixing claim precise enough to test.
2. **A necessity argument from the adelic product formula** (Section 4): Archimedean localization cannot be "pure" in the adelic sense; some $p$-adic norm must be nontrivial.
3. **A structural-selection argument for $p = 2$**: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular, so $p = 2$ gives degree $3$, the smallest possible among primes.
4. **Explicit numerical anchors** (Section 4): the electron ZBW frequency, reduced Compton wavelength, 2-adic ball measures, and mixing-amplitude tables, all computed with shown arithmetic.
5. **A simulation protocol** (Sections 3 and 7), labeled as a projection: a trapped-ion Dirac simulator in the style of the platform described in [12], in which the Compton-scale oscillation amplitude is regressed against an engineered 2-adic delocalization measure.

We emphasize the epistemic status of each result: items 1–4 are mathematical derivations or computations from stated constants; item 5 is a design and a projection, not a measurement.

## 2. Background and Related Work

**Adelic and $p$-adic quantum mechanics.** Reference [1] reviews the emergence of $p$-adic mathematical physics from attempts to find a non-Archimedean approach to spacetime and string dynamics at the Planck scale, and describes the successful formulation of $p$-adic and adelic quantum mechanics with complex-valued wave functions of $p$-adic and adelic arguments respectively. Its treatment of ordinary quantum mechanics on $L_2(\mathbb{R}^D)$ with the Heisenberg algebra $[\hat{x}_i, \hat{k}_j] = i\hbar\,\delta_{ij}$ is the baseline against which the $p$-adic generalization is defined, and it records that quantum mechanics on $p$-adic spaces admits two main approaches — $p$-adic-valued and complex-valued wave functions — of which the complex-valued one is more suitable for connection with ordinary quantum mechanics. We adopt exactly that complex-valued setting: our $\infty \leftrightarrow 2$ mixing channel is defined in a framework where the adelic wave function is a single object with an Archimedean factor and $p$-adic factors, so "mixing" between places is meaningful rather than a category error.

**Non-Archimedean geometry on adelic spaces.** Reference [2] is a review of applications of non-Archimedean geometry, $p$-adic numbers and adeles in modern mathematical physics. It gives the explicit construction we rely on: an adele is an infinite sequence $x = (x_{\infty}, x_2, \ldots, x_p, \ldots)$ with $x_{\infty} \in \mathbb{R}$ and $x_p \in \mathbb{Q}_p$, restricted so that $x_p \in \mathbb{Z}_p$ for all but finitely many primes, and the adele ring decomposes as $\mathcal{A} = \bigcup_{\mathbf{S}} \mathcal{A}(\mathbf{S})$ with $\mathcal{A}(\mathbf{S}) = \mathbb{R} \times \prod_{p \in \mathbf{S}} \mathbb{Q}_p \times \prod_{p \notin \mathbf{S}} \mathbb{Z}_p$. It also records the defining contrast between Archimedean and ultrametric spaces: the strong triangle inequality $d(x,y) \leq \max\{d(x,z), d(z,y)\}$ that characterizes non-Archimedean metrics. This is the bookkeeping substrate for our two-sector truncation: the adele structure guarantees that an Archimedean component and a 2-adic component of one rational point coexist in a single object.

**Arithmetic equidistribution and adelic measures.** Reference [3] concerns quasi-adelic measures on $\mathbb{P}^1$: it records that Baker–Rumely and Favre–Rivera-Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure, and that Chambert–Loir proved a more general version for curves. Its proofs proceed by controlling the $\mu_v$-energy of Galois-invariant point sets at every place $v$, showing $\lim_{n \to \infty} ([S_n]_v, [S_n]_v)_{\mu_v} = 0$ for each place. The relevance to us is methodological: adelic measures on projective spaces provide a rigorous way to speak about how mass distributes across places, which is exactly the bookkeeping our delocalization measure imitates at a toy level; the per-place energy decomposition in [3] is the rigorous analogue of our per-place amplitude budget.

**Fractal strings and complex dimensions.** Reference [4] surveys the theory of complex dimensions of real (Archimedean) fractal strings via the ordinary Cantor string and gives a detailed survey of $p$-adic (non-Archimedean) fractal strings, including an explicit volume formula for the tubular neighborhood of a $p$-adic fractal string. It sets the real ternary Cantor set — built from $2^n$ intervals of length $3^{-n}$ at scale $n$ — against its non-Archimedean counterpart, the 3-adic Cantor set and string. This matters because the geometry of $\mathbb{Q}_2$-supported sets — ultrametric, self-similar, tree-like — is precisely the geometry our 2-adic sector lives on, and this formalism is one of the few places where Archimedean and non-Archimedean fractal geometry are compared side by side; our delocalization measure $D_2(n) = 2^{-n}$ is a ball-volume count of the same self-similar type its tube formulas quantify.

**Arithmetic Hodge theory.** Reference [5] proves an arithmetic Hodge index theorem for adelic line bundles, extending prior results from number fields to finitely generated fields, and applies it to obtain a rigidity property of sets of preperiodic points of polarizable algebraic dynamical systems. Its argument proceeds by showing that admissible extensions of ample classes are nef and then applying a fundamental inequality for nef adelic line bundles. We cite it as an example of the general pattern that adelic objects carry rigidity statements their local components lack — the same pattern our spectral-gap proposition instantiates locally: coupling to a $p$-adic sector constrains the Archimedean dynamics (forcing an oscillation) rather than merely decorating it.

**Adelic Lie theory.** Reference [6] proves that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) *is* the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence $0 \to \mathbb{Q}^n \to \mathcal{L}(G) \xrightarrow{\exp} G \to 0$ with $\exp$ the adelic exponential, and it extends the definition of non-Archimedean dimension. This supplies the group-theoretic language in which a "phase oscillation across places" can be stated: an adelic torus carries both an Archimedean circle factor and $p$-adic factors, and the exponential sequence governs how phases lift. We use the categorical equivalence and the exponential sequence, not the ultraproduct machinery of its earlier sections.

**Non-Archimedean Hilbert-space geometry.** Reference [7] proves continuous non-Archimedean (resp. $p$-adic) Banach space and Hilbert space versions of Welch bounds previously proved by M. Krishna, and formulates continuous non-Archimedean and $p$-adic functional Zauner conjectures. Its Theorem 3.1 gives a first-order continuous $p$-adic functional Welch bound for collections in a $d$-dimensional $p$-adic Banach space over $\mathbb{Q}_p$ under explicit measurability and tight-frame conditions. For us this is a sanity check that the Hilbert-space formalism (inner products, frames, coherence bounds) survives the passage to $\mathbb{Q}_2$, which our model of a delocalized 2-adic sector requires: the sector $\mathcal{H}_2$ is a genuine Hilbert space, not a formal placeholder.

**Zitterbewegung.** Reference [8] records the historical core: around 1930, Breit and Schrödinger showed that the velocity eigenvalues of Dirac wave-packet solutions are simply $\pm c$, leading Schrödinger to coin "Zitterbewegung" for the resulting trembling motion of fermions at the speed of light. It develops a statistical treatment in $1+1$ dimensions in which the particle moves left or right at speed $c$ with probabilities $Pr(R) = \tfrac{1}{2}(1+v)$ and $Pr(L) = \tfrac{1}{2}(1-v)$, and argues in its conclusion that macroscopic motion is consistent with special relativity under this zig-zag picture, suggesting an observer-based entropy for the particle. We use the $\pm c$ velocity-eigenvalue fact, which we re-derive in Section 4, and we take its statistical reading as a reminder that the interference picture is not the only internally consistent account of ZBW kinematics.

**The QNFO research chain.** Reference [9] develops the conjecture that ZBW is the observable signature of mixing between the Archimedean and 2-adic completions of $\mathbb{Q}$, builds a two-channel effective Hamiltonian whose beat frequency reduces to the standard $\omega_{\mathrm{ZBW}} = 2E/\hbar$ under an explicit calibration condition, computes the electron-scale numbers ($\omega_{\mathrm{ZBW}} = 1.5521 \times 10^{21}\,\mathrm{s^{-1}}$, $\nu_{\mathrm{ZBW}} = 2.4702 \times 10^{20}\,\mathrm{Hz}$, $T_{\mathrm{ZBW}} = 4.0483 \times 10^{-21}\,\mathrm{s}$), verifies the adelic product formula for $q = 2$ and $q = 12$ exactly, and argues that the beat frequency is invariant under Foldy–Wouthuysen transformation. Its own discussion states that the restriction to two places $v \in \{\infty, 2\}$ is an assumption and that nothing in the product formula singles out $p = 2$ algebraically — a limitation we inherit and address structurally rather than algebraically. Reference [10] formulates a conjectural ultrametric readout in which the ZBW observable is a $\mathbb{Z}_2$ invariant $\chi$ carried by the current correlator on a Bruhat–Tits tree over $\mathbb{Q}_2$; for the electron it computes $\omega_C = 7.7636 \times 10^{20}\,\mathrm{s^{-1}}$, $\log_2 \omega_C = 69.3951$, $\nu(\omega_C) = 69$, $\chi = 1$, and a tree distance of $111$ against the Archimedean $\log_2 c = 28.1594$, giving a non-additivity $\Delta = 82.8406$ proposed as the distinguishing observable. Its discussion flags that the scale map $\nu(x) = \lfloor \log_2 x \rfloor$ is a convention, so the specific value $\chi = 1$ is convention-dependent even if the discreteness of the signature is not — a caution we adopt for our own prime-selection argument. Reference [11] computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition $\psi = \psi^c$ enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement; its numerical section shows the ZBW spinor-bilinear term $|\bar{u}\gamma^0 v|^2$ is the same order as the static term at all momenta (identical at $p = 0$, ratio $1.0000$). This is directly relevant because it shows ZBW observables can carry topological, not merely kinematic, content, consistent with our $\mathbb{Z}_2$-flavored ($\infty \leftrightarrow 2$) channel. Reference [12] locates the structural underdetermination of the position operator in a "Silent Parameter Principle," proves that $\mathrm{SU}(2)$ and $\mathbb{Z}_2^{\times}$ are isomorphic at the fusion-ring level via three theorems, establishes the $\mathrm{SL}(2,\mathbb{C}) \cong \mathrm{SL}(2,\mathbb{Q}_2)$ correspondence via the Satake/Langlands isomorphism, and states that the 2-adic ZBW frequency at the first Bruhat–Tits edge is $\omega_2(1) = \sqrt{2}\,\omega_{\infty}$, a $41.4\%$ deviation from the Archimedean value; its minimal viable experiment specifies a single $^{40}\mathrm{Ca}^+$ ion in a linear Paul trap with Ramsey interferometry between tree-depth states and $N = 10^6$ shots. We use its platform specification as the concrete instantiation of our simulation protocol, while treating the $\sqrt{2}$ frequency deviation as that work's claim, not ours.

Collectively, these works establish that adelic and non-Archimedean structures are mathematically robust and already applied to quantum-mechanical contexts. None of the cited papers directly formalizes mixing between the Archimedean and 2-adic sectors as a spectral-gap statement with a falsifiable amplitude test, leaving the gap this study addresses.

## 3. Methods

### 3.1 Adelic setup

Let $\mathbb{A}_{\mathbb{Q}}$ be the adele ring of $\mathbb{Q}$, with places $\infty$ (Archimedean, $\mathbb{R}$) and primes $p$ ($\mathbb{Q}_p$). Following the adelic quantum-mechanics framework [1], a state is a complex wave function $\Psi = (\psi_{\infty}, \psi_2, \psi_3, \ldots)$ with $\psi_{\infty} \in L^2(\mathbb{R})$ and $\psi_p \in L^2(\mathbb{Q}_p)$, the latter equipped with the standard $p$-adic Hilbert-space structure whose existence is confirmed by the non-Archimedean Welch bounds of [7]. The $p$-adic sector inherits ultrametric, tree-like geometry: the Bruhat–Tits tree of $\mathbb{Q}_p$ is $(p+1)$-regular, and the adele decomposition $\mathcal{A}(\mathbf{S}) = \mathbb{R} \times \prod_{p \in \mathbf{S}} \mathbb{Q}_p \times \prod_{p \notin \mathbf{S}} \mathbb{Z}_p$ of [2] justifies treating a finite set of places at a time.

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

This proposition is deliberately modest: it says mixing *forces* an oscillation at the gap frequency; it does not say the observed ZBW frequency *fixes* the mixing partner. That inference — that the coincidence $\Delta E = 2E_p$ is causal rather than accidental — is the hypothesis under test. We take this two-place restriction as an explicit assumption, following [9], which states that nothing in the product formula singles out $p = 2$ algebraically; our selection argument for $p = 2$ is structural (Section 3.4), not algebraic.

### 3.3 The 2-adic delocalization measure

Let $\mu_2$ be the Haar measure on $\mathbb{Q}_2$ normalized by $\mu_2(\mathbb{Z}_2) = 1$, where $\mathbb{Z}_2 = \{x \in \mathbb{Q}_2 : |x|_2 \leq 1\}$ is the ring of 2-adic integers. The ball of radius $2^{-n}$ is $2^n\mathbb{Z}_2$, and $\mathbb{Z}_2 / 2^n\mathbb{Z}_2$ has exactly $2^n$ cosets, so

$$
\mu_2(2^n \mathbb{Z}_2) = 2^{-n}.
$$

We define the 2-adic delocalization measure of a packet whose 2-adic support is confined to the ball $2^n\mathbb{Z}_2$ as $D_2(n) = 2^{-n}$: tighter 2-adic confinement (larger $n$) means smaller delocalization measure. This mirrors the Archimedean/$p$-adic fractal-string comparison of [4], where tubular volumes of $p$-adic strings are computed explicitly and where self-similar scaling of neighborhood volumes is the central quantity. A complementary dimensionless weight for a full two-sector state,

$$
\mu_2(\Psi) = \frac{\|\hat{\psi}_2\|_{2}^{2}}{\|\hat{\psi}_{\infty}\|^{2} + \|\hat{\psi}_2\|_{2}^{2}} \in [0,1],
$$

with $\hat{\psi}_2$ the 2-adic Fourier transform (defined via the standard additive character on $\mathbb{Q}_2$ [1]), serves as the regression variable in the simulation protocol; the per-place energy decomposition of the equidistribution framework [3] is the rigorous analogue of this bookkeeping on $\mathbb{P}^1$.

### 3.4 Bruhat–Tits tree regularity and prime selection

For a non-Archimedean local field $\mathbb{Q}_p$, the Bruhat–Tits tree is $(p+1)$-regular: each vertex has $p+1$ incident edges. For $p = 2$ the valence is $2 + 1 = 3$, the smallest possible valence among primes. In the Proposition of Section 3.2 the frequency $\Omega$ depends only on $\Delta E$ and $g$, not on $p$; hence the model predicts that no prime other than 2 changes the frequency scaling, and prime selection can only manifest through the coupling amplitude $g$ (Section 4.4). This is the falsifiable content of the prime-comparison test. We note the convention-dependence caution of [10]: just as its $\mathbb{Z}_2$ invariant $\chi$ depends on the choice of scale map, our selection argument fixes a *structural* minimality (tree degree), not a dynamical uniqueness; a dynamics in which $g$ depends on tree geometry is required to convert minimality into a physical preference, and we do not derive such a dynamics here.

### 3.5 Trapped-ion test protocol (projection)

We propose a hypothetical trapped-ion-style Dirac simulator, explicitly labeled as a design and instantiated concretely only by the platform specification of [12]: a single $^{40}\mathrm{Ca}^+$ ion in a linear Paul trap whose internal states encode the Dirac spinor or, in the tree-encoding variant of [12], the Bruhat–Tits tree vertices at depths $d = 0$ and $d = 1$, with laser-driven couplings implementing the Dirac Hamiltonian and an effective rest energy $\Delta_{\mathrm{eff}}$ playing the role of $mc^2$, so the simulated ZBW frequency is $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar$. The protocol: (a) prepare a wave packet with controlled 2-adic delocalization $D_2(n)$ (implemented as a tunable delocalization parameter in the simulator); (b) measure the ZBW oscillation amplitude $A(n)$; (c) test the model's projection $A(n) \propto 4^{-n}$ (Section 4.3); (d) vary the tree-valence analogue of the coupling geometry and check that the frequency $\omega_{\mathrm{sim}}$ is unchanged, as the Proposition requires. This paper performs no simulation; the protocol is a proposal written for future execution.

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
f_{\mathrm{ZBW}} = \frac{\omega_{\mathrm{ZBW}}}{2\pi} = \frac{1.55268 \times 10^{21}}{6.283185307} = 2.4712 \times 10^{20}\,\mathrm{Hz}.
$$

The corresponding period is $T_{\mathrm{ZBW}} = 1/f_{\mathrm{ZBW}} = 4.047 \times 10^{-21}\,\mathrm{s}$, consistent with the value $T_{\mathrm{ZBW}} = 4.0483 \times 10^{-21}\,\mathrm{s}$ computed in [9].

**Derivation 3: reduced Compton wavelength.**

$$
\lambda_C = \frac{\hbar}{m_e c} = \frac{1.054571817 \times 10^{-34}}{(9.1093837 \times 10^{-31}) \times (2.99792458 \times 10^{8})}.
$$

Denominator: $9.1093837 \times 2.99792458 = 27.309245$, so $m_e c = 2.7309245 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}}$. Then

$$
\lambda_C = \frac{1.054571817}{2.7309245} \times 10^{-34+22} = 0.386159 \times 10^{-12} = 3.8616 \times 10^{-13}\,\mathrm{m}.
$$

A packet localized at $\sigma \sim \lambda_C$ has momentum spread

$$
\Delta p \sim \frac{\hbar}{2\sigma} = \frac{1.054571817 \times 10^{-34}}{2 \times 3.8616 \times 10^{-13}} = \frac{1.054571817 \times 10^{-34}}{7.7232 \times 10^{-13}} = 1.3654 \times 10^{-22}\,\mathrm{kg\,m\,s^{-1}},
$$

i.e. $\Delta p \sim m_e c/2$: localization at the Compton scale is exactly where the two Dirac branches become inseparable, which is why the mixing channel becomes observable there.

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

So $\Omega = (\Delta E/\hbar) \times 1.000002$:

the weak-coupling correction to the ZBW frequency is at the $2 \times 10^{-6}$ relative level, i.e. $\delta\omega = 2 \times 10^{-6} \times 1.55268 \times 10^{21} = 3.11 \times 10^{15}\,\mathrm{rad\,s^{-1}}$. Since this relative shift is small compared with the frequency itself, the amplitude channel, which scales as $|g|^2/(\Delta E)^2$ rather than as a frequency offset, is the channel the protocol targets. The population modulation depth from the Rabi formula is

$$
A_{\mathrm{pop}} = \frac{4|g|^2}{(\Delta E)^2 + 4|g|^2} \approx \frac{4 \times 10^{-6}}{1 + 4 \times 10^{-6}} \approx 4.0 \times 10^{-6}.
$$

**Derivation 7: delocalization measure and amplitude projection (labeled projection).** From Section 3.3, $D_2(n) = 2^{-n}$. Explicit values: $D_2(0) = 1$; $D_2(1) = 0.5$; $D_2(2) = 0.25$; $D_2(3) = 0.125$; $D_2(10) = 2^{-10} = 9.77 \times 10^{-4}$. Assume the inter-sector coupling scales linearly with the delocalization measure, $|g|(n) = g_0\,2^{-n}$, with $g_0$ a simulator-dependent constant. Then, in the weak-coupling regime,

$$
A_{\mathrm{pop}}(n) \approx \frac{4 g_0^2\,2^{-2n}}{(\Delta E)^2} = A_0\,4^{-n}, \qquad A_0 = \frac{4 g_0^2}{(\Delta E)^2}.
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
2. ZBW angular frequency: $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$; ordinary frequency $f_{\mathrm{ZBW}} = 2.4712 \times 10^{20}\,\mathrm{Hz}$; period $T_{\mathrm{ZBW}} = 4.047 \times 10^{-21}\,\mathrm{s}$ (Derivation 2).
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

**Limitations.** The spectral-gap Proposition is elementary two-level quantum mechanics; its only content is that mixing forces an oscillation at $\Omega/\hbar \geq \Delta E/\hbar$. The strong claim — that the observed ZBW frequency is caused by $\infty \leftrightarrow 2$ adelic mixing rather than by the standard positive/negative-energy interference of the Dirac Hamiltonian — is not derived here and is not fixed by the frequency coincidence $\Delta E = 2E_p$, which the standard theory already reproduces without any adelic input. The prime-selection argument via Bruhat–Tits valence is structural, not dynamical: since $\Omega$ is independent of $p$ in the Proposition, prime choice can only manifest through the coupling amplitude $g$, and we have no derivation that $g$ actually depends on the delocalization measure $D_2(n)$ as assumed in Derivation 7. The two-place restriction $v \in \{\infty, 2\}$ is an explicit assumption, inherited from [9], which states that nothing in the product formula singles out $p = 2$ algebraically; and the convention-dependence caution of [10] applies to any discrete signature extracted with a chosen scale map.

**Failure modes.** The program fails if (i) a simulator with a $p \geq 3$ sector reproduces the same amplitude scaling, contradicting the 2-adic specificity; (ii) the measured amplitude $A(n)$ in the trapped-ion protocol does not scale as $4^{-n}$ under the engineered delocalization parameter; or (iii) the frequency $\omega_{\mathrm{sim}} = 2\Delta_{\mathrm{eff}}/\hbar$ changes when the coupling geometry is varied, contradicting the Proposition's $p$-independence.

**What would falsify the claims.** A direct demonstration that the ZBW amplitude is insensitive to the delocalization parameter while all other simulator settings are held fixed would falsify the mixing-amplitude hypothesis. Conversely, observation of the projected factor-of-$4$ suppression would not prove adelic mixing — it would only show consistency; the frequency channel is a $2 \times 10^{-6}$ relative shift ($\delta\omega \approx 3.11 \times 10^{15}\,\mathrm{rad\,s^{-1}}$ against $\omega_{\mathrm{ZBW}} \approx 1.55 \times 10^{21}\,\mathrm{rad\,s^{-1}}$), and we assume, as an explicit instrumentation assumption this paper does not establish, that free-electron spectroscopy at that relative resolution is unavailable.

**Open questions.** Whether the linear ansatz $|g|(n) = g_0\,2^{-n}$ has a first-principles derivation; whether the adelic equidistribution framework of [3] can upgrade the toy measure $D_2(n)$ to a rigorous state on $\mathbb{P}^1$; and whether the $\mathbb{Z}_2$ topological distinction of the Majorana correlator result [11] connects to the $\infty \leftrightarrow 2$ channel beyond analogy.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The prospective users are experimentalists building Dirac simulators in trapped-ion and related platforms, and theorists assessing whether ZBW observables carry invariant information. If the projection holds, the design of a Dirac-simulation experiment changes in one specific way: the 2-adic delocalization parameter of the simulated packet becomes a control knob whose setting predicts the oscillation amplitude as $A_{\mathrm{pop}}(n) = A_0\,4^{-n}$, and the amplitude regression replaces frequency measurement as the diagnostic channel. If the projection fails, the adelic interpretation is eliminated and the interference reading stands as the sole account, which is itself a usable decision outcome for experiment design.

**(b) Current readiness.** This work is purely analytical: a proposition, derivations from stated constants, and a protocol design. Against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept and application formulated), and analytical work of this kind does not exceed TRL 3 (proof of concept) until the oscillation-amplitude regression has been demonstrated on a physical simulator. No manufacturing or deployment readiness is claimed.

**(c) The smallest next test.** The minimal de-risking experiment is the tree-encoding variant specified in [12]: a single $^{40}\mathrm{Ca}^+$ ion in a linear Paul trap, internal states encoding Bruhat–Tits tree vertices at depths $d = 0$ and $d = 1$, Ramsey interferometry between the depth states, and $N = 10^6$ shots to extract the population oscillation frequency. The amplitude version proposed here adds one step: repeat the Ramsey sequence under $K$ settings of a tunable delocalization parameter and regress the extracted amplitude $A(n)$ against $4^{-n}$. The outcome that refutes the model is a measured $A(n)$ flat in $n$ (or scaling with an exponent other than $-2$ in $2^{-n}$) while all other simulator settings are held fixed; the outcome that supports it is suppression by a factor close to $4$ per confinement step, within the uncertainty set by $g_0$ and shot noise.

**(d) Binding constraints.** The first binding constraints, in the order they bind: (i) the unknown coupling constant $g_0$, which sets the absolute amplitude scale $A_0 = 4g_0^2/(\Delta E)^2$ — if $g_0$ is much smaller than the assumed $10^{-3}\,\Delta E$, the modulation depth falls proportionally to $g_0^2$, and whether it remains resolvable depends on the shot budget and readout noise, which this paper does not quantify; (ii) coherence time of the ion against the simulated ZBW period $T_{\mathrm{sim}} = \pi\hbar/\Delta_{\mathrm{eff}}$, which must satisfy $T_2^* \gg T_{\mathrm{sim}}$ for the oscillation to be resolved; (iii) the fidelity of the engineered delocalization parameter as a faithful analogue of $D_2(n) = 2^{-n}$, which is a modeling assumption, not a derived property of any hardware. Whether a tunable delocalization parameter with the required $2^{-n}$ ladder can be implemented in a specific trap is an open question this paper does not answer.

**(e) Order-of-magnitude performance bounds (projections).** With the stated assumption $g_0 = 10^{-3}\,\Delta E$ and weak coupling, the projected modulation depth is $A_0 \approx 4.0 \times 10^{-6}$ at $n = 0$, falling to $\approx 3.81 \times 10^{-12}$ at $n = 10$. With $N = 10^6$ shots, the statistical uncertainty on the extracted amplitude is of order $1/\sqrt{N} = 10^{-3}$ on the accumulated estimate, so the shot-noise floor $10^{-3}$ exceeds every projected amplitude under the assumed $g_0 = 10^{-3}\,\Delta E$ — from $A(0) = 4.0 \times 10^{-6}$ down to $A(10) \approx 3.81 \times 10^{-12}$ — and none of the rungs is resolvable at that shot budget; resolution would require a larger $g_0$, a larger shot budget, or repeated averaging. These figures are projections under the stated assumptions, not measured values.

**(f) Risks and misuse paths.** The main misuse is overclaiming: a factor-of-$4$ amplitude suppression observed in a simulator would be consistent with the adelic mixing hypothesis but would not establish it, since any coupling mechanism with amplitude $\propto 2^{-n}$ produces the same scaling. Reporting a confirmation without the prime-comparison control (item (d) of the protocol) would misrepresent the evidential content of the test.

## 8. Conclusion

We formalized Zitterbewegung as a candidate observable signature of mixing between the Archimedean place and the 2-adic place: a spectral-gap Proposition shows any such coupling forces an oscillation at $\Omega = \sqrt{(\Delta E)^2 + 4|g|^2}/\hbar$; explicit derivations give $\omega_{\mathrm{ZBW}} = 1.55268 \times 10^{21}\,\mathrm{rad\,s^{-1}}$ and $\lambda_C = 3.8616 \times 10^{-13}\,\mathrm{m}$; the prime 2 is structurally minimal via its 3-regular Bruhat–Tits tree; and a trapped-ion protocol with projected factor-of-$4$ amplitude suppression per confinement step makes the claim falsifiable. The causal adelic interpretation remains a hypothesis; the simulation program is its test.

## Version History

- Version 2.0.0 (2026-10-27, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 12. length 4022 -> 5940 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.39.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 13 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[2] Non-Archimedean Geometry and Physics on Adelic Spaces. arXiv:math-ph/0306023v1. https://arxiv.org/abs/math-ph/0306023v1
[3] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$. arXiv:1502.04660v3. https://arxiv.org/abs/1502.04660v3
[4] The Geometry of p-Adic Fractal Strings: A Comparative Survey. arXiv:1105.2966v1. https://arxiv.org/abs/1105.2966v1
[5] The arithmetic Hodge index theorem for adelic line bundles II. arXiv:1304.3539v2. https://arxiv.org/abs/1304.3539v2
[6] Finite-Dimensional Protori Are Adelic Tori. arXiv:2411.16000v44. https://arxiv.org/abs/2411.16000v44
[7] Continuous Non-Archimedean and p-adic Welch Bounds. arXiv:2209.12833v1. https://arxiv.org/abs/2209.12833v1
[8] The Problem of Motion: The Statistical Mechanics of Zitterbewegung. arXiv:1411.1854v2. https://arxiv.org/abs/1411.1854v2
[9] https://papers.qnfo.org/papers/zitterbewegung-as-archimedean-2-adic-channel-mixing-a-conjectural-adelic-framewo. QNFO: Zitterbewegung as Archimedean–2-adic Channel Mixing: A Conjectural Adelic Framework and Its Testable Consequences.
[10] https://papers.qnfo.org/papers/zitterbewegung-as-a-p-adic-ultrametric-observable-a-mathbb-z-2-invariant-on-the-. QNFO: Zitterbewegung as a $p$-Adic Ultrametric Observable: A $\mathbb{Z}_2$ Invariant on the Bruhat–Tits Tree, Its Readout, and Its Non-Additivity Signature.
[11] https://papers.qnfo.org/papers/zbw-majorana-tqc-p2-majorana-zbw-correlator. QNFO: Majorana Zitterbewegung Current Correlator: Vanishing ZBW Signal as a Z2 Topological Invariant.
[12] https://papers.qnfo.org/papers/zbw-adelic-observable. QNFO: Zitterbewegung: From Archimedean Puzzle to Adelic Observable.
