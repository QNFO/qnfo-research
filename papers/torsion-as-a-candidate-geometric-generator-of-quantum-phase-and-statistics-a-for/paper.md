# Torsion as a Candidate Geometric Generator of Quantum Phase and Statistics: A Formalization and Falsifiability Analysis

## Abstract

Quantum mechanics rests on postulates—the complex phase of the wavefunction, the quadratic scaling of state-space dimension, and the boson/fermion restriction on exchange symmetry—that are empirically successful but deductively unexplained. A conjecture in current circulation holds that spacetime torsion in Einstein–Cartan gravity generates all three: the axial torsion vector supplies the wavefunction's phase gradient, and the topology of torsional exchange paths permits only $\pm 1$ exchange phases. This paper formalizes the claimed deductive chain link by link. We show that the exchange-phase restriction $e^{i\varphi}=\pm 1$ follows from the double-swap identity alone, that the normalized state space of an $N$-level system carries $K=N^{2}-1$ real parameters ($3$, $8$, and $15$ for $N=2,3,4$), and that the integral of the Lorentz factor over physical velocities evaluates to $\pi/2\approx 1.5707963$. We write the Madelung form of a torsion-coupled probability current and show that the identification of the axial torsion vector with the phase gradient is dimensionally consistent but unproven. As a labeled projection built on the gate fidelities of the Tianyan platform [4], a simple gate-count model yields a total error probability of $99.66\%$ for a 74-qubit, 24-cycle random-circuit sampling experiment; this figure characterizes the hardware error budget and is not a torsion-specific prediction. The chain is partially derivable: statistics and state-space dimension reduce to topology and counting, while the torsion-phase identification is the load-bearing unproven link. We specify the calculation that would confirm or break it.

## 1. Introduction

Physicists who design quantum experiments and interpret quantum data currently accept three structural facts as postulates rather than derivations. First, the state of a quantum system lives in a complex Hilbert space, so an $N$-level system's normalized state carries $K=N^{2}-1$ real parameters; no accepted derivation of this count from deeper structure exists. Second, exchanging two identical particles multiplies the wavefunction by $e^{i\varphi}$ with $\varphi\in\{0,\pi\}$ only—bosons or fermions—a restriction imposed as the symmetrization postulate. Third, the wavefunction's complex phase has no accepted geometric origin; it is inserted by hand. These gaps have practical costs. Anyon-like "transtatistics" generalizations are proposed and searched for without a principled criterion for which modifications geometry forbids [2]; quantum state estimation theory must assume the Hilbert-space geometry whose origin it cannot explain [1]; and hardware error budgets on cloud-accessible processors are interpreted without a foundational account of the phase that makes interference possible [4].

If the torsion conjecture holds, these postulates become theorems of Einstein–Cartan geometry, and the design criterion for exotic-statistics searches changes from "look everywhere" to "look only where torsional topology allows it." If it fails, the failure localizes exactly which link breaks—the phase generation, the dimension count, or the exchange restriction—and tells reconstruction programs what any geometric foundation of quantum mechanics must supply instead. Either outcome is decision-relevant for the quantum foundations and quantum-statistics communities.

This paper does not claim to prove the conjecture. It does three things that a proof attempt requires first. It separates the conjecture's claimed links and derives the ones derivable from standard mathematics and the cited literature. It writes the torsion-coupled Madelung equations explicitly, so that the phase-generation link has a definite mathematical form that can be checked or refuted. It states, with shown arithmetic, the quantitative content of each derived link, and it reports one hardware error projection, clearly labeled, that characterizes the experimental substrate on which any torsion-sensitive test would eventually run.

The contributions are:

- A derivation, from the double-swap identity stated in [2], that exchange phases in the permutation-group setting are restricted to $e^{i\varphi}=\pm 1$, with the arithmetic shown, and an analysis of what remains open for torsion to explain (Section 4.1).
- A derivation of the real parameter count $K=N^{2}-1$ of the normalized quantum state space from the Hermiticity and trace constraints written in [1], evaluated for $N=2,3,4$, with a documented convention for reconciling the count with the conjecture's $K=N^{2}$ phrasing (Section 4.2).
- A derivation that the integral of the Lorentz factor $\gamma(\beta)=(1-\beta^{2})^{-1/2}$ over $\beta\in[0,1]$ equals $\pi/2\approx 1.5707963$, reproducing the conjecture's claimed angular normalization (Section 4.3).
- The explicit Madelung form of a torsion-coupled probability current, with the axial-torsion/phase-gradient identification stated as a dimensionally consistent ansatz and its unproven status made precise (Section 4.4).
- A labeled numerical projection of total error probability, $99.66\%$, for a 74-qubit random-circuit sampling experiment, computed from the gate fidelities reported in [4] under stated assumptions (Sections 3.6 and 4.5).
- A falsifiability analysis: the specific calculation whose outcome would confirm or break the torsion-phase link, and the observations that would falsify each derived link (Sections 5, 6, and 7).

## 2. Background and Related Work

The torsion conjecture sits at the intersection of quantum statistical mechanics, quantum reconstruction, geometric phase theory, and geometric approaches to phase transitions. We review the works that supply the specific results our analysis uses.

Gill and Levit [1] develop quantum statistics on finite-dimensional Hilbert spaces and state the geometric substrate on which the field rests: a $d$-dimensional system's state is a $d\times d$ density matrix $\rho$, Hermitian, non-negative, with trace 1, and for $d=2$ every state is $\rho=\frac{1}{2}(\mathbf{1}+\theta_{1}\sigma_{1}+\theta_{2}\sigma_{2}+\theta_{3}\sigma_{3})$ with $\theta_{1}^{2}+\theta_{2}^{2}+\theta_{3}^{2}\leq 1$—a three-real-parameter ball. Their derivation of asymptotic Bayes-risk lower bounds via the quantum Cramér–Rao bound, including the collective-measurement advantage over separate measurements, presupposes this geometry rather than explaining it. Our Section 4.2 takes their explicit parameterization as the input and counts the parameters for general $N$; the conjecture's claim that this count is geometrically forced is tested against their stated structure.

The statistics-reconstruction work of [2] gives the sharpest available statement of the exchange-phase problem. Its Introduction derives the two-statistics restriction in one line: if $\psi(x_{2},x_{1})=e^{i\varphi}\psi(x_{1},x_{2})$, then applying the swap twice gives $e^{i\varphi}=\pm 1$—bosons and fermions. The work notes that the physical motivation for the symmetrization postulate remains poorly understood, that exotic statistics have never been observed in nature, and that its operational reconstruction, following Hardy's instrumentalist approach with single-particle unitary channels and number-only detectors, makes the Fock-space structure emerge rather than assume it. Its partition theorem shows that not every $U(1)$-character induces a valid $U(d)$-character: the example $\chi_{1}(x)=1+x^{2}$ produces a negative expansion coefficient $c_{(1,1)}$ for two modes, so candidate generalized statistics are already constrained by positivity. Our Section 4.1 reproduces the double-swap arithmetic as the core of the exchange link, and Section 6 asks whether torsional topology adds anything beyond it.

Le Hur [3] treats quantum phase transitions in spin-boson systems, where a two-level system couples to a bath of harmonic oscillators and dissipation drives or modifies phase transitions; in the ohmic case the order parameter $\langle\sigma_{z}\rangle$ jumps by a non-universal amount $\sqrt{1/\alpha_{c}}$ along the quantum critical line with $\alpha_{c}=1+\mathcal{O}(\Delta/\omega_{c})$. This supplies a worked example of a quantum statistical structure—the bosonic bath—whose existence the torsion conjecture would ultimately derive; we cite it as the phenomenological end point that any derivation of bosonic statistics must reproduce.

The Tianyan platform paper [4] reports a 105-qubit superconducting processor with single-qubit gate, two-qubit gate, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$ respectively, cloud-accessible, and demonstrates random circuit sampling with 74 qubits and 24 cycles. We use its fidelity figures in Sections 4.5 and 5 as the quantitative input to a labeled error-accumulation projection, and we cite it in Section 7 as the class of currently available testbed on which statistics-sensitive interference experiments could be specified, without claiming any torsion-specific capability for it.

Sarandy and collaborators [5] extend geometric phases to open quantum systems: for cyclic adiabatic evolution under a Lindblad master equation, they derive Abelian and non-Abelian geometric phase expressions that generalize the Berry and Wilczek–Zee phases, prove their gauge invariance, and find robustness against dephasing and spontaneous emission for a spin-1/2 in a magnetic field—robustness that fails for the bit-flip channel because it does not commute with the Hamiltonian superoperator. This matters for our program because if torsion generates the quantum phase, the phase is geometric in precisely the Berry sense, and [5] supplies the machinery for asking whether a torsion-generated phase survives decoherence.

Simpson and collaborators [6] argue for fusing statistics with network science in complex functional brain network analysis, a case study in combining statistical inference with geometric and graph-theoretic structure. We cite it for the specific methodological point that network science—an interdisciplinary offshoot of graph theory—enabled examining the brain as an integrated system, as an analogy for how statistical and geometric descriptions of the same system must be fused rather than juxtaposed; our Madelung analysis in Section 4.4 performs the analogous fusion for probability currents.

Kastner and collaborators [7] propose, against the topological hypothesis, that a substantial change in the geometry—not the topology—of the accessible configuration space is the necessary condition for a phase transition, with a conjecture that a discontinuity in the mixing time on configuration space is necessary for a first-order transition in the thermodynamic limit; their hard-disk and hard-sphere quotient-space results found that discontinuity locations in the diffusion diameter were robust under changes of the quotienting symmetry group. This is directly relevant: the torsion conjecture is a claim that geometry generates quantum structure, and [7] provides a worked precedent for geometry-versus-topology adjudication in a neighboring problem, including the caution that geometric and topological features can change dramatically with symmetry choices while the physically relevant discontinuities do not.

The Riemannian superdeterministic Bell-violations work [8] proposes that Bell-inequality violations emerge from intrinsic curvature of a discretized state-space manifold, violating measurement independence through a global geometric constraint, and identifies entanglement saturation, fractal jitter, and gravitational variance in Bell-test correlations as falsification channels. We cite it for its specific argument that flat-space Hilbert geometry is an approximation whose breakdown has observable signatures—the same methodological bet as the torsion conjecture, applied to correlations rather than to phase and statistics.

## 3. Methods

Our method is analytic decomposition of the conjecture into links, each of which is either derived, formalized, or declared open. We state the links and the tools used on each.

**Link L1 (exchange statistics).** Claim: torsional topology permits only $\pm 1$ exchange symmetries in $3+1$ dimensions. Tool: the double-swap identity for the exchange operator, as written in [2], plus the topology of the exchange path space in three spatial dimensions. We derive the phase restriction from the identity alone and then ask what, if anything, torsion adds.

**Link L2 (state-space dimension).** Claim: Hardy-type continuity axioms force the quadratic state space with $K=N^{2}$ parameters. Tool: direct counting of the real degrees of freedom of a $d\times d$ Hermitian trace-one matrix, using the density-matrix definition stated in [1]. We resolve the count precisely and reconcile it with the conjecture's $K=N^{2}$ phrasing by an explicit convention.

**Link L3 (angular normalization).** Claim: a $\pi/2$ normalization arises from integrating the Lorentz factor, interpreted in the conjecture as a Möbius map on the Riemann sphere. Tool: direct evaluation of the integral of the Lorentz factor over its physical domain. We evaluate the integral exactly and note what part of the Möbius/Riemann-sphere claim remains interpretive.

**Link L4 (phase generation).** Claim: the axial component of the Einstein–Cartan torsion tensor reproduces the wavefunction's phase gradient. Tool: the Madelung transformation of the Schrödinger equation, written for a probability current with a torsion coupling, followed by a dimensional consistency check of the identification of the axial torsion vector with the phase gradient. This link we can formalize but not derive; we state the ansatz and its status explicitly.

**Link L5 (torsion lumps as dark matter).** Claim: stable torsion lumps in Einstein–Cartan solutions have the mass spectrum and collisionless dynamics of cold dark matter. Tool: none available within our derivations. We treat this link as an open hypothesis and specify in Section 7 what calculation would begin to test it.

**Error-accumulation projection (hardware context).** To characterize the experimental substrate on which any torsion-sensitive test would run, we construct a gate-count error model for the random-circuit sampling experiment reported in [4]. The assumptions are: (i) each of the 24 cycles applies one single-qubit gate to every qubit; (ii) qubits are paired arbitrarily, yielding $74/2=37$ two-qubit gates per cycle; (iii) gate errors are independent and multiplicative. Every figure produced under these assumptions is labeled a projection and characterizes the hardware error budget only; no torsion-specific prediction is derived from it.

Throughout, every number we report is either computed in Section 4 with shown arithmetic, quoted from a cited work with its stated value, or labeled a projection with stated assumptions. We use natural units $\hbar=c=1$ except where $\hbar$ is displayed to track dimensions.

## 4. Analysis

### 4.1 Link L1: exchange phases from the double-swap identity

The input is the exchange relation stated in [2]: for a two-particle state $\psi(x_{1},x_{2})$, exchange acts as

$$\psi(x_{2},x_{1})=e^{i\varphi}\,\psi(x_{1},x_{2}).$$

Applying the swap a second time returns the original configuration, so

$$\psi(x_{1},x_{2})=e^{i\varphi}\,\psi(x_{2},x_{1})=e^{i\varphi}\,e^{i\varphi}\,\psi(x_{1},x_{2})=e^{2i\varphi}\,\psi(x_{1},x_{2}).$$

For a nonzero state this requires $e^{2i\varphi}=1$, i.e. $2\varphi=2\pi k$ for $k\in\mathbb{Z}$, hence

$$\varphi=\pi k,\qquad e^{i\varphi}=(-1)^{k}\in\{+1,-1\}.$$

The two cases $k$ even and $k$ odd are bosons and fermions. This is the arithmetic [2] presents, and it is the entire content of the exchange restriction at the level of the wavefunction: the square of the exchange operator is the identity, and the one-dimensional unitary representations of $\mathbb{Z}_{2}$ are exactly $\pm 1$.

What this derivation does not fix is why only one-dimensional representations occur in $3+1$ dimensions—in two spatial dimensions, the exchange group is the braid group rather than $\mathbb{Z}_{2}$, and arbitrary phases $e^{i\theta}$ are allowed (anyons). The torsion conjecture's specific claim is that torsional topology of the exchange path space enforces the $\mathbb{Z}_{2}$ restriction. Our derivation shows the restriction is already a consequence of the permutation group's structure as stated in [2]; the torsion mechanism would be an explanation of why physical exchange realizes the permutation group rather than the braid group, not an independent derivation of $\pm 1$. We return to this distinction in Section 6.

### 4.2 Link L2: the real parameter count of the quantum state space

The input is the density-matrix definition in [1]: the state of a $d$-dimensional system is a $d\times d$ matrix $\rho$ that is self-adjoint ($\rho^{*}=\rho$), non-negative ($\rho\geq\mathbf{0}$), and normalized ($\mathrm{trace}(\rho)=1$). Non-negativity is an inequality constraint that does not reduce the dimension of the ambient space, so we count the Hermitian trace-one matrices.

A $d\times d$ Hermitian matrix has real diagonal entries: $d$ real parameters. Its off-diagonal entries satisfy $\rho_{ij}=\rho_{ji}^{*}$ for $i\neq j$, so each conjugate pair $(i,j)$ and $(j,i)$ carries one complex number, i.e. 2 real parameters. The number of pairs with $i<j$ is

$$\binom{d}{2}=\frac{d(d-1)}{2},$$

so the off-diagonal contribution is

$$2\cdot\frac{d(d-1)}{2}=d(d-1)$$

real parameters. The total for the Hermitian matrix is

$$d+d(d-1)=d^{2}.$$

The trace constraint $\mathrm{trace}(\rho)=1$ is one linear equation, removing one parameter:

$$K=d^{2}-1.$$

Check against the $d=2$ case stated in [1]: $K=2^{2}-1=3$, matching the Bloch vector $(\theta_{1},\theta_{2},\theta_{3})$ with $\theta_{1}^{2}+\theta_{2}^{2}+\theta_{3}^{2}\leq 1$. Further values:

$$K(2)=3,\qquad K(3)=9-1=8,\qquad K(4)=16-1=15.$$

The conjecture as stated says "Hardy's continuity axiom forces the $K=N^{2}$ quadratic state space." Our count gives $K=N^{2}-1$ for normalized states; the $N^{2}$ figure is recovered if one counts the unnormalized positive matrices (trace unconstrained), or equivalently the cone before normalization. We adopt the convention $K=N^{2}-1$ for physical states and record this as a definitional reconciliation, not a disagreement about substance: both counts describe the same cone, differing by whether the normalization is imposed before or after counting.

The substantive question the conjecture raises is not the count itself—the count is bookkeeping—but whether a continuity axiom can be shown to force the quadratic scaling $K\sim N^{2}$ rather than, say, a linear simplex $K=N-1$ (classical probability) or another scaling. That forcing argument is Hardy-type reconstruction machinery of the kind [2] employs operationally; we do not reproduce it here and mark it as the unproven part of L2.

### 4.3 Link L3: the Lorentz-factor integral and the $\pi/2$ normalization

The conjecture claims a $\pi/2$ angular normalization from integrating the Lorentz factor. The Lorentz factor for velocity fraction $\beta=v/c$ is

$$\gamma(\beta)=\frac{1}{\sqrt{1-\beta^{2}}}.$$

We evaluate its integral over the full physical subluminal range $\beta\in[0,1]$:

$$\int_{0}^{1}\frac{d\beta}{\sqrt{1-\beta^{2}}}=\Bigl[\arcsin\beta\Bigr]_{0}^{1}=\arcsin(1)-\arcsin(0)=\frac{\pi}{2}-0=\frac{\pi}{2}.$$

Numerically,

$$\frac{\pi}{2}\approx 1.5707963.$$

This is the claimed angular normalization: the Lorentz factor, integrated over its physical domain, yields exactly a quarter turn. The conjecture's further claim—that this arises from treating the Lorentz factor as a Möbius map on the Riemann sphere—is consistent with the fact that the substitution $\beta=\sin\theta$ converts the integral to $\int_{0}^{\pi/2}d\theta$, a quarter of the full circle, but we have not derived the Möbius-map interpretation from independent structure; the exact value $\pi/2$ is the derived content, and the geometric interpretation of why the domain ends at $\beta=1$ (the light cone) supplying a quarter-turn is the interpretive remainder.

### 4.4 Link L4: the Madelung form and the torsion-phase ansatz

Write the wavefunction in polar form, $\psi=\sqrt{\rho}\,e^{iS/\hbar}$, where $\rho$ is the probability density and $S$ the phase action. The Schrödinger equation $i\hbar\,\partial_{t}\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+V\psi$ separates, on substituting the polar form and splitting real and imaginary parts, into

$$\partial_{t}\rho+\nabla\cdot\left(\rho\frac{\nabla S}{m}\right)=0,$$

$$\partial_{t}S+\frac{|\nabla S|^{2}}{2m}+V+Q=0,\qquad Q=-\frac{\hbar^{2}}{2m}\,\frac{\nabla^{2}\sqrt{\rho}}{\sqrt{\rho}}.$$

The first is a continuity equation for the probability current $j=\rho\,\nabla S/m$; the second is a Hamilton–Jacobi equation with the quantum potential $Q$. The phase gradient $\nabla S$ is the velocity field of the probability flow.

The conjecture's L4 claim is that the axial torsion vector of Einstein–Cartan geometry reproduces this phase gradient. In Einstein–Cartan theory the torsion tensor $T^{\lambda}{}_{\mu\nu}$ (the antisymmetric part of the affine connection) has an irreducible axial part, conventionally

$$A_{\mu}=\epsilon_{\mu\nu\rho\sigma}\,T^{\nu\rho\sigma},$$

a pseudovector with dimension of inverse length. The phase gradient divided by $\hbar$, $\nabla S/\hbar$, also has dimension of inverse length: $S$ has dimension of action (energy $\times$ time), so $\nabla S$ has dimension of momentum, and momentum$/\hbar$ is inverse length. We therefore state the ansatz

$$\frac{\nabla_{\mu}S}{\hbar}\;\overset{?}{=}\;\kappa\,A_{\mu},$$

with $\kappa$ a dimensionless coupling to be fixed by dynamics. Dimensionally the ansatz is consistent: both sides are covectors of dimension inverse length. Substituting into the Madelung current gives a torsion-coupled flow

$$j_{\mu}=\frac{\rho\,\hbar\,\kappa\,A_{\mu}}{m},$$

and the continuity equation becomes a statement that probability flows along the axial torsion field.

This is where the derivation stops. Three things are unproven. First, the proportionality $\nabla_{\mu}S=\hbar\kappa A_{\mu}$ is an ansatz, not a consequence of the Einstein–Cartan field equations; deriving it would require showing that the torsion-coupled action for a spinning fluid reproduces the Schrödinger Lagrangian with the identification forced. Second, the coupling $\kappa$ is undetermined; the conjecture predicts $\kappa$ is fixed (perhaps $\kappa=\pm 1$ or a known constant), but no derivation exists here. Third, in standard Einstein–Cartan matter coupling, torsion is algebraically determined by the spin density of matter and is negligible at laboratory scales; whether a torsion field of the magnitude the ansatz requires can exist without contradicting known torsion bounds is an open question we flag in Section 6 rather than resolve.

### 4.5 Error-accumulation projection for the Tianyan random-circuit sampling experiment

The input numbers, each with its source, are:

- Single-qubit gate fidelity $F_{1}=99.90\%$, hence error $\epsilon_{1}=1-F_{1}=0.0010$ (reported in [4]).
- Two-qubit gate fidelity $F_{2}=99.56\%$, hence error $\epsilon_{2}=1-F_{2}=0.0044$ (reported in [4]).
- Number of active qubits $Q=74$ and number of cycles $C=24$ (the random-circuit sampling demonstration in [4]).
- Two-qubit gates per cycle $G_{2}=Q/2=37$ and single-qubit gates per cycle $G_{1}=Q=74$ (model assumptions of Section 3).

The gate counts are

$$N_{2}=G_{2}\times C=37\times 24=888,$$

$$N_{1}=G_{1}\times C=74\times 24=1776.$$

Under the independence assumption, the success probability that every gate in the circuit acts correctly is

$$P_{\mathrm{succ}}=(1-\epsilon_{1})^{N_{1}}\,(1-\epsilon_{2})^{N_{2}}.$$

Taking the logarithm and using $\ln(1-x)\approx -x$ for $x\ll 1$ (here $x\leq 0.0044$, so the correction is of order $x^{2}/2\leq 10^{-5}$ per gate and negligible at the precision quoted):

$$\ln P_{\mathrm{succ}}=N_{1}\ln(1-\epsilon_{1})+N_{2}\ln(1-\epsilon_{2})\approx -1776\times 0.0010-888\times 0.0044.$$

The two terms are

$$1776\times 0.0010=1.776,$$

$$888\times 0.0044=3.9072,$$

so

$$\ln P_{\mathrm{succ}}\approx -(1.776+3.9072)=-5.6832.$$

Exponentiating:

$$P_{\mathrm{succ}}\approx e^{-5.6832}\approx 0.0034.$$

The total error probability is therefore

$$P_{\mathrm{err}}=1-P_{\mathrm{succ}}\approx 1-0.0034=0.9966,$$

i.e. $99.66\%$. This is a projection under the stated assumptions; it quantifies how deeply the reported circuit sits inside the hardware error budget and nothing more. In particular, it is not evidence for or against any torsion-induced dephasing channel, since no torsion coupling has been derived (Section 4.4).

### 4.6 Link L5 status

The torsion-lump dark-matter conjecture requires: (i) existence of stable localized Einstein–Cartan solutions, (ii) a mass spectrum, (iii) collisionless dynamics at galactic scales. None of these is derivable from the tools of this paper, and we make no quantitative claim about any of them. We carry the link forward only as a specification of what a future calculation must demonstrate (Section 7).

## 5. Results

We report only numbers derived in Section 4 or quoted from cited works.

**R1 (exchange phases).** From the double-swap identity of [2], the exchange phase satisfies $\varphi=\pi k$, so $e^{i\varphi}=\pm 1$: exactly two statistics in the permutation-group setting (Section 4.1). The torsion conjecture's exchange link is consistent with, but not additionally required by, this arithmetic; the open part is why the exchange group is $\mathbb{Z}_{2}$ rather than the braid group in $3+1$ dimensions.

**R2 (state-space dimension).** The normalized state space of an $N$-level system carries

$$K=N^{2}-1$$

real parameters, derived from the Hermitian trace-one count in Section 4.2, with values $K=3,8,15$ for $N=2,3,4$, and the $N=2$ value matching the Bloch-ball parameterization stated in [1]. The conjecture's $K=N^{2}$ is recovered for the unnormalized cone; the two conventions describe the same structure.

**R3 (angular normalization).** The Lorentz-factor integral over the physical domain evaluates to

$$\int_{0}^{1}\frac{d\beta}{\sqrt{1-\beta^{2}}}=\frac{\pi}{2}\approx 1.5707963,$$

reproducing the conjecture's claimed $\pi/2$ normalization exactly (Section 4.3).

**R4 (Madelung/torsion ansatz).** The Madelung transformation of the Schrödinger equation yields a continuity equation for the current $j=\rho\,\nabla S/m$ and a Hamilton–Jacobi equation with quantum potential $Q$ (Section 4.4). The identification $\nabla_{\mu}S/\hbar=\kappa A_{\mu}$ with the axial torsion vector $A_{\mu}$ is dimensionally consistent—both sides are covectors of dimension inverse length—but is an ansatz with undetermined $\kappa$, not a derived result. The status of this link is therefore: formalized, not derived.

**R5 (error projection).** Under the assumptions of Section 3 (one single-qubit gate per qubit per cycle, $37$ two-qubit gates per cycle, independent multiplicative errors), the 74-qubit, 24-cycle random-circuit sampling experiment of [4] has an estimated total error probability

$$P_{\mathrm{err}}\approx 1-e^{-5.6832}\approx 99.66\%,$$

computed from the reported fidelities $F_{1}=99.90\%$ and $F_{2}=99.56\%$ (Section 4.5). This characterizes the hardware error budget only.

## 6. Discussion

The principal finding is a split verdict on the torsion conjecture. Two of its three mathematical links—exchange-phase restriction and state-space dimension count—reduce to standard mathematics that does not require torsion: the double-swap identity gives $e^{i\varphi}=\pm 1$ from the permutation group alone, and $K=N^{2}-1$ follows from Hermiticity and normalization alone. The third link, the generation of the wavefunction's phase by the axial torsion vector, is the load-bearing one, and it is exactly the link this paper could only formalize. We discuss what this split means, how it could be wrong, and what remains open.

**What the derivable links do and do not establish.** The double-swap derivation shows that the $\mathbb{Z}_{2}$ restriction is a theorem of the permutation-group setting, not a fact awaiting geometric explanation at that level. What torsion would explain is one level up: why physical exchange in $3+1$ dimensions realizes the permutation group rather than the braid group, so that only one-dimensional representations occur. Anyon phases $e^{i\theta}$ with arbitrary $\theta$ are consistent with two-dimensional topology, and the conjecture's exchange claim is best read as a topological-censorship statement about the exchange path space, not as an independent derivation of $\pm 1$. Similarly, the parameter count $K=N^{2}-1$ is bookkeeping once the density-matrix definition is granted; the substantive unproven part of L2 is whether a Hardy-type continuity axiom forces the quadratic scaling against alternatives such as the classical simplex $K=N-1$. The reconstruction machinery of [2], which makes the Fock-space structure emerge from operational primitives, is the kind of argument that would be needed; we did not reproduce it.

**The phase-generation link is the falsifiable core.** The ansatz $\nabla_{\mu}S/\hbar=\kappa A_{\mu}$ makes three commitments that can each fail. First, the proportionality could fail to follow from the Einstein–Cartan field equations: torsion in minimal Einstein–Cartan coupling is algebraically determined by the spin density of matter, so for ordinary matter the axial torsion field is confined to matter interiors and negligible outside them, whereas the wavefunction phase gradient is defined wherever the probability flow extends. If the field equations force $A_{\mu}$ to vanish wherever $\nabla S$ is nonzero for free particles, the ansatz is dead. Second, the coupling $\kappa$ is undetermined; a derivation that leaves $\kappa$ free, or that yields different $\kappa$ for different systems, breaks the claim that phase is geometrically fixed. Third, existing bounds on torsion-induced effects constrain the magnitude of any laboratory-accessible axial torsion field; if those bounds force $|A_{\mu}|$ below the value the ansatz requires for a free particle's de Broglie phase gradient, the identification fails empirically even if it is formally consistent.

**Falsification of the main result.** The main result of this paper is the split verdict itself, and the observation that would falsify it is a published derivation of the Schrödinger Lagrangian from a torsion-coupled action in which the identification $\nabla_{\mu}S=\hbar\kappa A_{\mu}$ is forced with a fixed, system-independent $\kappa$. Such a derivation would collapse our "formalized, not derived" status for L4 into "derived," and the conjecture would stand as a candidate foundation. Conversely, a proof that the Einstein–Cartan field equations with minimally coupled spinning matter admit no solution in which $A_{\mu}$ matches a free-particle phase gradient would break L4 definitively and, with it, the conjecture's central claim.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each:

- The double-swap derivation assumes the exchange operator acts as a scalar phase on the two-particle wavefunction, as written in [2]. If exchange acts nontrivially on internal degrees of freedom (parastatistics-like structures), the derivation does not apply; the partition theorem of [2] shows candidate generalized statistics are already constrained by positivity, but the full space of exceptions is not mapped here.
- The parameter count assumes non-negativity is an inequality constraint that does not reduce the ambient dimension. This is standard, but the count says nothing about whether the quadratic scaling is forced; sensitivity is total, since the unproven forcing argument is the substantive content of L2.
- The $\pi/2$ result is an exact integral evaluation; the interpretive claim that it constitutes an "angular normalization" of quantum structure is not derived, and the Möbius-map/Riemann-sphere reading remains unformalized. Sensitivity: the number is robust, its interpretation is not.
- The Madelung analysis assumes a single-particle Schrödinger equation and neglects spin, electromagnetic coupling, and multi-particle entanglement; a torsion-phase mechanism for entangled states would need the many-body Madelung form, which we do not write.
- The error projection assumes independent, multiplicative gate errors, arbitrary qubit pairing, and no crosstalk, leakage, or readout error contribution. Real devices violate all of these to some degree; the projection is an error-budget scale, not a prediction of experimental fidelity.
- The paper does not review experimental torsion bounds quantitatively; the claim that standard Einstein–Cartan torsion is negligible at laboratory scales is qualitative.

**Open questions.** Whether the braid group can be excluded by torsional topology in a precisely stated manifold; whether a continuity axiom forces $K\sim N^{2}$; whether $\kappa$ can be fixed; whether stable torsion lumps exist in Einstein–Cartan solutions with cold-dark-matter phenomenology (Link L5, untouched here); and whether the geometric-phase robustness results of [5] extend to a torsion-generated phase under realistic decoherence channels—the bit-flip counterexample in [5] shows such robustness is not universal.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are quantum-foundations researchers and reconstruction-program authors: the split verdict tells them that effort on exchange statistics and state-space dimension should target the forcing arguments (why $\mathbb{Z}_{2}$, why quadratic scaling), not the arithmetic, which is settled. A second user group is experimentalists planning exotic-statistics searches: if the torsion mechanism were established, the search criterion would change from unbounded scanning to torsional-topology-allowed regions only; since it is not established, no search protocol changes today. A third group is quantum-hardware benchmarking teams, who can reuse the gate-count error model of Section 4.5 as a first-order error-budget scale for random-circuit sampling experiments, with the stated assumptions made explicit. No policy or regulatory decision is affected by this work.

**(b) Readiness.** This is purely analytical work that has not been peer reviewed: it corresponds to TRL 1–2 (basic principles observed and formulated; concept formulated). The Madelung ansatz is at most a TRL 3 candidate (proof of concept, here only dimensional consistency). No experimental demonstration, component development, or manufacturing readiness is claimed or claimable for a torsion-phase mechanism on the basis of this paper.

**(c) The smallest next calculation.** The smallest de-risking step is a pencil-and-paper calculation, not an experiment: take the Einstein–Cartan action with a minimally coupled spinning ideal fluid, derive the torsion-coupled Madelung equations, and check whether the field equations force $\nabla_{\mu}S=\hbar\kappa A_{\mu}$ with a unique $\kappa$. The outcome that refutes the conjecture is a demonstration that the field equations admit free-particle solutions with $\nabla S\neq 0$ but $A_{\mu}=0$ (or with $A_{\mu}$ not proportional to $\nabla S$). The outcome that de-risks it is a forced identification with fixed $\kappa$; the next step after that would be a comparison of the predicted $\kappa$-dependent corrections to interference phases against laboratory torsion bounds.

**(d) Binding constraints.** For any eventual experimental test, the binding constraint is sensitivity: standard Einstein–Cartan torsion scales with spin density and is confined to matter, so a torsion-phase signal, if it exists at all, is expected to be far below current interferometric sensitivity; no quantitative bound is derived here, so the size of the gap is an open question. For the error-budget model, the binding assumptions are independence and complete pairing; crosstalk and correlated errors would raise the true error probability above the $99.66\%$ projection. For Link L5 (torsion lumps as dark matter), the binding constraints are cosmological—mass spectrum and collisionless dynamics at galactic scales—and no calculation pathway exists in this paper. Regulatory constraints do not apply.

**(e) Order-of-magnitude bounds.** The only quantitative projection this paper offers beyond its derivations is the error-budget figure of Section 4.5: $P_{\mathrm{err}}\approx 99.66\%$ for the 74-qubit, 24-cycle circuit, under the assumptions listed in Section 3 and labeled a projection. Its uncertainty is dominated by the independence assumption; correlated errors would increase $P_{\mathrm{err}}$, and the figure should be read as a lower bound on the error scale of an all-gates-correct model. No cost, market, or performance figure beyond this is derivable from the paper's inputs.

**(f) Risks and misuse paths.** The main misuse is overclaiming: the $99.66\%$ figure could be quoted as evidence that quantum-advantage experiments are dominated by error, or conversely that torsion effects are hidden in the error budget. Neither follows; the figure is a model output under stated assumptions, and no torsion coupling has been derived. A second misuse is citing the $\pi/2$ integral as "explaining" quantum normalization; the integral is exact arithmetic, and its interpretive role is unestablished.

## 8. Conclusion

We formalized the torsion conjecture's claimed deductive chain and found it partially derivable. The exchange-phase restriction $e^{i\varphi}=\pm 1$ follows from the double-swap identity stated in [2]; the state-space parameter count $K=N^{2}-1$ follows from the density-matrix definition stated in [1], with values $3$, $8$, and $15$ for $N=2,3,4$; and the Lorentz-factor integral over the physical domain equals $\pi/2\approx 1.5707963$ exactly. These results show that two of the conjecture's three mathematical links are already theorems of standard structure, so torsion's potential contribution is confined to explaining why the exchange group is $\mathbb{Z}_{2}$ in $3+1$ dimensions and why the quadratic scaling is forced. The phase-generation link—the identification of the axial torsion vector with the wavefunction's phase gradient—was written in explicit Madelung form as a dimensionally consistent ansatz with undetermined coupling $\kappa$, and its unproven status was made precise: it stands or falls on whether the Einstein–Cartan field equations force the identification with a fixed $\kappa$, which is the single calculation this paper specifies as decisive. A labeled projection computed from the fidelities reported in [4] gives a total error probability of $99.66\%$ for the 74-qubit, 24-cycle random-circuit sampling experiment, characterizing the hardware error budget on which any future torsion-sensitive test would run. The conjecture survives formalization in weakened form: statistics and dimension are counting theorems, phase generation is the open geometric question, and the torsion-lump dark-matter link remains an unquantified hypothesis.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Conciliation of Bayes and Pointwise Quantum State Estimation: Asymptotic information bounds in quantum statistics. arXiv:math/0512443v6. https://arxiv.org/abs/math/0512443v6
[2] Reconstruction of Quantum Particle Statistics: Bosons, Fermions, and Transtatistics. arXiv:2306.05919v2. https://arxiv.org/abs/2306.05919v2
[3] Quantum Phase Transitions in Spin-Boson Systems: Dissipation and Light Phenomena. arXiv:0909.4822v1. https://arxiv.org/abs/0909.4822v1
[4] Tianyan: Cloud services with quantum advantage. arXiv:2512.10504v2. https://arxiv.org/abs/2512.10504v2
[5] Abelian and non-Abelian geometric phases in adiabatic open quantum systems. arXiv:quant-ph/0507012v3. https://arxiv.org/abs/quant-ph/0507012v3
[6] Analyzing complex functional brain networks: fusing statistics and network science to understand the brain. arXiv:1302.5721v3. https://arxiv.org/abs/1302.5721v3
[7] A geometric conjecture about phase transitions. arXiv:2203.03154v1. https://arxiv.org/abs/2203.03154v1
[8] QNFO: Riemannian-Geometric Approach to Superdeterministic Bell-Violations