# Thresholded Readout of Continuous Classical Fields: A Formalization and Counterexample to the Uniqueness Claim for Quantum Mechanics

## Abstract

A family of contemporary foundational programs asserts that reality is a continuum of local deterministic fields and that quantum mechanics is the unique calculus bridging this continuum to discrete measurement outcomes. If that uniqueness claim were correct, research seeking additional physical principles behind quantum statistics could stop; if it is wrong, the specific failure localizes where extra structure must be added. This paper formalizes the proposed bridge as a thresholded amplification map $M:\mathbb{R}\to\mathcal{O}$ and tests uniqueness by construction. Within the axiom class of continuous local deterministic fields plus irreversible discrete readout, we exhibit two distinct calculi — a linear threshold and a quadratic (intensity-like) threshold — that yield detection probabilities $0.1587$ and $0.3174$ respectively for a unit-variance Gaussian field at threshold $\Theta=1$, a structural factor of exactly $2$ that persists at other thresholds. A slope-matched noisy threshold detector with $\sigma_n=\sqrt{2/\pi}\approx0.7978846$ reproduces the two-outcome Born rule only approximately, with maximum deviation $0.1050$ and root-mean-square deviation $0.0602$ over a five-point angular grid. We prove the CHSH bound $|S|\le2$ for every deterministic local thresholded readout, against the quantum prediction $|S|=2\sqrt{2}\approx2.8284$. Uniqueness therefore fails at the level of the readout calculus. A projection shows $\approx130$ trials per setting suffice to distinguish the two calculi experimentally.

## 1. Introduction

Researchers working on classical reconstructions of quantum mechanics — and the reviewers, funders, and technical audiences who must evaluate such programs — currently face an unresolved decision. Several active programs assert that the universe is a continuum of local deterministic fields and that all measurement is an irreversible discrete mapping from a continuous state space to a finite outcome space, implemented by nonlinear amplification and thresholding [8], [10]. Some of these programs go further and claim that quantum mechanics is the logically necessary and unique calculus connecting the two domains. Today there is no shared, explicit procedure for testing that uniqueness claim: the assertions circulate as foundational theses, and acceptance or rejection rests on taste rather than on a computed counterexample or a computed agreement check. The stakes are concrete. If uniqueness holds, any research program hunting for additional physical principles behind quantum statistics (extra variables, selection rules, dynamical postulates) is redundant and should be disbanded. If uniqueness fails, the failure localizes exactly which additional structure a classical ontology must supply — and programs that omit it are making a falsifiable error, not a philosophical choice.

This paper supplies the missing procedure for one precisely stated version of the claim. We take two of the asserted properties as axioms — (i) the underlying state relevant to a detector is a continuous field value evolved by local deterministic dynamics, and (ii) measurement is an irreversible discrete map $\mathbb{R}\to\mathcal{O}$ realized by nonlinear amplification and thresholding — and we treat uniqueness as a falsifiable hypothesis about the class of calculi these axioms define. A *calculus* here means a rule assigning outcome probabilities to each outcome in $\mathcal{O}$ given the continuous field state. The test is direct: exhibit two members of the class that both satisfy the axioms and compute whether they agree. If they disagree, uniqueness fails, and the form of quantum statistics must come from structure beyond the axioms.

The strategy is falsificationist in both directions. If a thresholded classical map reproduced quantum statistics exactly and were the only calculus consistent with the axioms, uniqueness would be supported. If instead a second consistent calculus exists, or if the thresholded map fails to reproduce quantum statistics, uniqueness is refuted. We find the latter, and we localize the failure precisely: the thresholded map matches the Born rule only in a central regime and cannot match it at the certainty points, and no deterministic local thresholded model can violate the CHSH inequality.

The result bears on real programs, not straw men. The Post-Quantum Synthesis program states a no-collapse theorem in which a threshold crossing within the detector produces the discrete outcome during continuous Hamiltonian evolution [10], and it derives joint measurement statistics for entangled systems as $P(o_1,o_2)=\sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ [10]. The Continuum-is-Real program states that the universe is not quantized but our interaction with it is, through a binning mechanism [8]. Both programs therefore commit to exactly the axiom class formalized here, and both inherit whatever statistics that class actually produces. Our computations show the class produces statistics that are internally consistent but empirically distinguishable from quantum mechanics — so the programs must either add a selection principle or accept divergent predictions.

Our contributions are:

1. An explicit two-calculus counterexample: linear and quadratic thresholded amplifiers, both satisfying the axioms exactly, yield detection probabilities $P_1^{(L)}=0.1587$ and $P_1^{(Q)}=0.3174$ for a unit-variance Gaussian field at $\Theta=1$, a structural factor of exactly $2$ that persists at $\Theta=4$ (Sections 4.1–4.3, 4.8).
2. A quantitative bound on Born-rule reproduction: the best locally slope-matched noisy threshold detector, with $\sigma_n=\sqrt{2/\pi}\approx0.7978846$, deviates from the Born rule by up to $0.1050$ (at $\alpha=0$, where certainty is demanded) with root-mean-square deviation $0.0602$ over a five-point angular grid, and the deviation at certainty points is structural for any finite noise (Section 4.4).
3. A proof that every deterministic local thresholded readout obeys $|S|\le2$ for the CHSH combination, against the quantum prediction $|S|=2\sqrt{2}\approx2.8284$ at standard angles, with a demonstration that readout noise cannot close the gap (Sections 4.5–4.6).
4. A statistical power projection, labeled as such, that approximately $130$ trials per calculus suffice for a $3\sigma$ experimental discrimination between the two calculi under stated assumptions (Section 4.7).

## 2. Background and Related Work

The proposed ontology sits at the intersection of classical continuum modeling, axiomatic measurement theory, continuous-time quantum measurement, and contemporary classical-reconstruction programs. We review each connection using specific results from the works themselves.

**Continuous-time quantum measurement as the standard bridge.** The stochastic Schrödinger equation, of classical or quantum type, describes open quantum systems under measurement in continuous time, and the review [1] establishes that two formulations of quantum continuous measurement — one based on the Hudson-Parthasarathy equation and quantum stochastic calculus, the other on the SSE, the stochastic master equation, and conditional states — are equivalent, so that output spectra can be deduced from either the classical SSE or the quantum one, with Heisenberg-type bounds on the spectra of incompatible quadratures holding independently of the formulation. The review concludes from this equivalence that the "classical" SSE is not a semiclassical approximation to some quantum theory but is itself fully quantum [1]. This is the standard against which any proposed classical bridge must be measured: in the accepted calculus, the continuous description and the discrete record are connected through Hilbert-space structure, not through a threshold on a classical field amplitude. Our model inverts the direction of explanation — we ask whether a classical continuous process plus thresholding can generate quantum statistics — and Section 4 shows it cannot do so exactly.

**Axiomatic measurement theory.** The axiomatic approach of [3] characterizes all the possible statistical properties of apparatuses measuring an observable with nondegenerate spectrum allowed in standard quantum mechanics, treating an apparatus as inputting a state $\rho$ and outputting a classical outcome ${\bf x}$ together with the conditional state $\rho_{\{{\bf x}=x\}}$, with the statistical property consisting of the output distribution and the state reduction. The same work notes that the conventional description via the Born statistical formula and the projection postulate is much more restrictive than what quantum mechanics allows [3]. This supplies the quantum-side target set: any candidate calculus claiming to be *the* bridge must land inside the characterized set of apparatus statistics, and our counterexample calculus of Section 4.3 lands outside the quantum member of that set while remaining inside the proposed axiom class.

**Instruments, POVMs, and classical SDEs.** The theory of quantum continual measurements has been formulated using instruments and positive operator valued measures, using quantum stochastic differential equations, and using classical stochastic differential equations for vectors in Hilbert spaces or for trace-class operators [4]. Within this framework, a continual measurement is called quasi-complete when the a posteriori states are pure for every pure initial state, and a theorem quoted there establishes that the continual measurement is quasi-complete if and only if $\mathcal{L}_1=0$ and $J_k[\rho]/\mathop{\mathrm{Tr}}\{J_k[\rho]\}$ is a pure state for every $k$ and every pure state $\rho$ [4]. The relevance is structural: even when classical SDEs appear in the quantum formulation, they are SDEs for Hilbert-space objects, and the information-gain analysis runs through a posteriori states. Our thresholded map has no a posteriori state and no information-gain monotonicity; the contrast marks exactly what the proposed axioms omit.

**Realist unification programs.** The realist psychobiological interpretation of [2] proposes a quantum mechanical/biological dualism in which the methods of the quantum physicist and of the biological sciences are two alternative modes of description that supplement each other, with a proposed correspondence including collapse of the state vector mapped to a decision process and the measuring instrument mapped to structures which determine and regulate signals or forms [2]. This is a precedent for treating the link between an underlying reality and the quantum description as a mapping whose form requires independent justification — the interpretive move our formalization makes precise. Our result sharpens the precedent: the mapping's form is not merely underdetermined philosophically; within the proposed axiom class it is empirically underdetermined, with distinct members giving distinct statistics.

**Protective measurement and the continuous substrate.** The analysis of protective measurement in [6] derives the final system–apparatus state to first order in $1/T$ beyond the zeroth-order limit usually considered, and shows that the finite system–apparatus entanglement arising in a protective measurement entails that protective measurements can never transcend the irreducibly probabilistic element inherent in any measurement of an unknown quantum state; the readout itself cannot tell us whether information about the initial state has actually been obtained [6]. The same work raises the scaling problem of how the number of protective measurements required to reconstruct a wave function grows with system size, noting the exponential number required for multi-qubit states [6]. This removes one route by which the continuous wavefunction itself could be taken as directly measured, reinforcing the need for an explicit readout map between whatever continuous substrate is posited and the discrete record — the object we formalize in Section 3.

**Locality of discrete transition structure.** The foundations of quantum Turing machines in [7] characterize the local transition functions for fully general quantum Turing machines, requiring that only a finite system be in motion during any one step, that the motion depend only on the state of a finite subsystem, and that the rule specifying the motion be finitely given; the transition matrix elements take the local product form over the tape cells with nearest-neighbor head moves, and a halting protocol is proposed that works without augmenting the halting qubit and without spoiling the computation [7]. This demonstrates that locality constraints on discrete transition rules sitting on a quantum substrate are formally tractable. Our CHSH derivation in Section 4.5 imposes the analogous locality on classical readout functions $A(a,\lambda)$, $B(b,\lambda)$, and the tractability precedent supports the well-posedness of that constraint.

**Continuous-to-discrete mapping outside physics.** In virtual reality, self-avatars enhance presence and embodiment, and whether one uses a complex motion capture solution or a few trackers with inverse kinematics, the pipeline maps continuous tracked signals onto a discrete skeleton structure through a fixed adjustment procedure [5]. This is an engineering instance of the abstract operation the proposed axioms posit — irreversible discretization of a continuous signal — and it illustrates that the discretization step alone carries no quantum statistics; the statistics come from the ensemble distribution and the amplifier shape, which is exactly the degree of freedom our counterexample exploits.

**The programs under test.** The Continuum-is-Real program argues that the ontological crisis in physics stems from mistaking observational artifacts for fundamental properties, that the universe is not fundamentally quantized but our interaction with it is, and it resolves discreteness through a universal binning mechanism, reinterpreting quantum jumps and entanglement as informational phenomena related to the observation of a continuous field [8]. The Post-Quantum Synthesis program formalizes this with theorems: a no-physical-collapse theorem in which the continuous field triggers a threshold crossing within the detector leading to a discrete outcome while the physical state evolves continuously throughout [10]; a no-spooky-action theorem showing that a local unitary on one system leaves the marginal physical state of the spatially separated system unchanged [10]; a correlation-history theorem giving joint measurement statistics $P(o_1,o_2)=\sum_i |c_i|^2 P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ from coefficients $c_i$ established during the initial interaction [10]; and a redundancy-threshold theorem with $P_{\text{error}}\le e^{-N\gamma}$ and $N_0=\frac{1}{\gamma}\log\frac{1}{\epsilon}$ [10]. The audit record of this program additionally derives the Born rule as a theorem of epistemic consistency via Gleason's theorem, under non-negativity, normalization, and non-contextuality of the probability assignment, and explains which-path detection as a physical interaction that inevitably disturbs the continuous field followed by a Bayesian update of the observer's knowledge state [9]. Two points connect directly to our analysis. First, the threshold crossing in the amplification stage of [10] is precisely the readout map we formalize; second, the correlation formula of [10] is a mixture over shared-history coefficients, which is a local hidden-variable form, and Section 4.5 shows every such local form obeys $|S|\le2$ — so the program's own correlation theorem cannot reproduce the quantum value $2\sqrt{2}$ at the standard angles.

**Epistemic framing.** The map-territory distinction — that representational models differ from their source and that confusing the representation with the referenced entity leads to categorical errors — and the observation that self-reference is a structural condition of inquiry rather than a procedural obstacle [11] frame what a "bridging calculus" is: a map from continuous reality to discrete records, not the reality itself. Our formalization treats the calculus as exactly such a map and asks whether the axioms fix it uniquely; they do not.

No work in this literature derives the Born rule from a classical thresholding map on a classical field, and none exhibits a second calculus within the proposed axiom class. That is the gap this paper fills.

## 3. Methods

### 3.1 Axioms

We formalize the proposed ontology as three axioms on a measurement event.

- **A1 (Continuous substrate).** The state of the world relevant to a detector at any time is a field value $x\in\mathbb{R}$ (one-dimensional; the extension to fields on $\mathbb{R}^n$ is not needed for the results).
- **A2 (Local determinism).** The evolution $x(t)$ is generated by a local deterministic law; a detector's outcome depends only on its local setting and the local field value, never on distant settings or distant outcomes.
- **A3 (Irreversible discrete readout).** A measurement is a map $M:\mathbb{R}\to\mathcal{O}$ with $\mathcal{O}$ finite, implemented by nonlinear amplification followed by thresholding, and irreversible: the pre-threshold value is not recoverable from the outcome.

These axioms are a faithful formalization of the programs under test: the amplification-and-threshold-crossing stage of the no-collapse theorem in [10] is A3, and the locality of physical influence in its no-spooky-action theorem [10] is A2.

### 3.2 The readout map

A measurement device is a triple $(\mathcal{A},g,\Theta)$ where $\mathcal{A}$ is an amplifier acting on the continuous field variable $x\in\mathbb{R}$, $g>0$ is a gain, and $\Theta$ is a threshold. The amplifier produces an intermediate variable

$$y=\mathcal{A}_g(x),$$

and the readout map $M_\Theta:\mathbb{R}\to\mathcal{O}=\{0,1\}$ for a two-outcome detector is the step function

$$M_\Theta(y)=\begin{cases}1 & \text{if } y\ge\Theta,\\ 0 & \text{if } y<\Theta.\end{cases}$$

Irreversibility enters because $M_\Theta$ is many-to-one: the preimage of outcome $1$ is the set $\{x:\mathcal{A}_g(x)\ge\Theta\}$, and all continuous information within that set is discarded.

### 3.3 Candidate calculi

Within A1–A3 we define two calculi, each a complete rule assigning outcome probabilities to field ensembles:

- **Linear calculus ($\mathcal{C}_L$):** $\mathcal{A}_g(x)=g\,x$, so outcome $1$ occurs iff $x\ge\Theta/g$.
- **Quadratic calculus ($\mathcal{C}_Q$):** $\mathcal{A}_g(x)=g\,x^2$, so outcome $1$ occurs iff $|x|\ge\sqrt{\Theta/g}$; the amplifier is insensitive to sign, as intensity-like detectors are.

Both calculi satisfy the axioms exactly: the substrate is continuous, local, and deterministic; the readout is discrete, irreversible, and produced by amplification and thresholding. The quadratic amplifier is nonlinear in the stronger sense of the programs' wording; the linear amplifier is the degenerate affine member of the family, included as the minimal baseline. Section 6 discusses the reading on which the affine member is excluded.

### 3.4 Field ensemble

Over an ensemble of nominally identical preparation runs, the field value at the detector is distributed as a unit-variance Gaussian,

$$p(x)=\frac{1}{\sqrt{2\pi}}\,e^{-x^2/2},$$

in dimensionless units. This is the minimal nontrivial ensemble: symmetric, continuous, and normalizable. No quantum postulate is used at this stage; $p(x)$ is the ensemble distribution of the classical field amplitude. We write $\Phi(z)=\int_{-\infty}^{z}p(u)\,du$ for the standard normal cumulative distribution function.

For the Born-rule comparison we use the noisy threshold map with additive readout noise $\eta\sim\mathcal{N}(0,\sigma_n^2)$:

$$M_\theta(x)=\mathbf{1}\{x+\eta>\theta\},\qquad P(1\mid x)=\Phi\!\left(\frac{x-\theta}{\sigma_n}\right).$$

### 3.5 Target statistics and locality test

The quantum predictions to be tested are:

- **Born rule (two-outcome, single parameter).** For a qubit-like system prepared at angle $\alpha$ relative to the detector basis, $P_1^{\mathrm{QM}}(\alpha)=\cos^2(\alpha/2)=\frac{1+\cos\alpha}{2}$.
- **CHSH correlation.** For two parties with settings $a,a'$ and $b,b'$, the quantum correlation for a singlet-type state is $E_{\mathrm{QM}}(a,b)=-\cos(a-b)$, and the CHSH combination is $S=E(a,b)+E(a,b')+E(a',b)-E(a',b')$.

For the CHSH test, two spatially separated detectors each implement a factorized readout: detector $A$ outputs $A(a,\lambda)\in\{\pm1\}$ as a deterministic function of its local setting $a$ and the local field configuration $\lambda$, and detector $B$ outputs $B(b,\lambda)\in\{\pm1\}$ similarly, with no dependence of $A$ on $b$ or of $B$ on $a$. The correlation is

$$E(a,b)=\int\rho(\lambda)\,A(a,\lambda)\,B(b,\lambda)\,d\lambda,$$

where $\rho(\lambda)$ is the distribution of the shared field configuration. This factorized form is the direct classical analogue of the correlation-history structure $P(o_1,o_2)=\sum_i|c_i|^2P_1(o_1|\phi_1^i)P_2(o_2|\phi_2^i)$ of [10]: both are mixtures over shared past variables with locally conditioned outcomes.

## 4. Analysis

All numbers in this section are computed explicitly from the inputs stated above; no simulation or external data are used. The only external numerical inputs are tabulated values of the standard normal integral, $\Phi(1)=0.8413$ and $\Phi(2)=0.9772$, and the mathematical constants $\sqrt{2}\approx1.4142136$ and $\sqrt{\pi}\approx1.7724539$.

### 4.1 Outcome probability under the quadratic calculus

With gain $g=1$ and threshold $\Theta=1$, the quadratic calculus fires when $|x|\ge\sqrt{\Theta/g}=\sqrt{1}=1$. The detection probability is

$$P_1^{(Q)}=\int_{-\infty}^{-1}p(x)\,dx+\int_{1}^{\infty}p(x)\,dx=2\int_{1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\,dx=2\bigl(1-\Phi(1)\bigr).$$

Using $\Phi(1)=0.8413$:

$$P_1^{(Q)}=2(1-0.8413)=2\times0.1587=0.3174.$$

### 4.2 Outcome probability under the linear calculus

With the same $g=1$, $\Theta=1$, the linear calculus fires when $x\ge\Theta/g=1$:

$$P_1^{(L)}=\int_{1}^{\infty}p(x)\,dx=1-\Phi(1)=1-0.8413=0.1587.$$

### 4.3 Divergence between the calculi

The two calculi, both satisfying A1–A3 exactly, give

$$\Delta P=P_1^{(Q)}-P_1^{(L)}=0.3174-0.1587=0.1587,$$

with ratio

$$\frac{P_1^{(Q)}}{P_1^{(L)}}=\frac{0.3174}{0.1587}\approx2.000.$$

The factor of $2$ is structural, not coincidental. For any symmetric density, the quadratic threshold counts both tails while the linear threshold counts one, so analytically $P_1^{(Q)}=2\bigl(1-\Phi(\Theta/g)\bigr)$ while $P_1^{(L)}=1-\Phi(\Theta/g)$, and the ratio is exactly $2$; the rounded tabulated inputs give $0.3174/0.1587\approx1.9994$, which rounds to $2.000$. Both calculi are internally consistent, deterministic at the field level, and produce irreversible discrete records. Therefore the calculus connecting continuous reality to discrete outcomes is **not unique** within the axiom class; uniqueness fails unless an additional principle selects the amplifier.

### 4.4 Born-rule approximation by a slope-matched threshold detector

We now ask how well the best locally calibrated noisy threshold detector matches the Born rule. We posit a classical field whose value at the detector is $x(\alpha)=\cos\alpha$ — a deterministic, local encoding of the preparation angle into the field amplitude, chosen as the most favorable linear encoding for the proposal — with threshold $\theta=0$ and readout noise scale $\sigma_n$. The model's outcome probability is

$$P_1^{\mathrm{thr}}(\alpha)=\Phi\!\left(\frac{\cos\alpha}{\sigma_n}\right).$$

We choose $\sigma_n$ by matching the small-amplitude slope of $P_1^{\mathrm{thr}}$ to that of the Born rule at $\alpha=\pi/2$, where both are centered at $1/2$. Expanding both around $\alpha=\pi/2$ (so $\cos\alpha\approx 0$):

$$P_1^{\mathrm{QM}}\approx\frac{1}{2}+\frac{\cos\alpha}{2},\qquad P_1^{\mathrm{thr}}\approx\frac{1}{2}+\frac{\cos\alpha}{\sigma_n\sqrt{2\pi}}.$$

Matching slopes gives $\frac{1}{\sigma_n\sqrt{2\pi}}=\frac{1}{2}$, i.e.

$$\sigma_n=\sqrt{\frac{2}{\pi}}=\frac{\sqrt{2}}{\sqrt{\pi}}=\frac{1.4142136}{1.7724539}\approx 0.7978846.$$

As a check, $\sqrt{2\pi}=\sqrt{2}\cdot\sqrt{\pi}=1.4142136\times1.7724539\approx2.5066283$, so the slope factor is $\frac{1}{0.7978846\times2.5066283}=\frac{1}{2.0000000}=0.5$ exactly, by construction.

We evaluate both statistics at five angles $\alpha\in\{0,\pi/6,\pi/4,\pi/3,\pi/2\}$. The required cosine values are the standard ones: $\cos 0=1$, $\cos(\pi/6)=\frac{\sqrt{3}}{2}\approx0.8660254$, $\cos(\pi/4)=\frac{\sqrt{2}}{2}\approx0.7071068$, $\cos(\pi/3)=0.5$, $\cos(\pi/2)=0$.

**Born rule values** $P_1^{\mathrm{QM}}(\alpha)=\frac{1+\cos\alpha}{2}$:

- $\alpha=0$: $\frac{1+1}{2}=1.0000$.
- $\alpha=\pi/6$: $\frac{1+0.8660254}{2}=0.9330127$.
- $\alpha=\pi/4$: $\frac{1+0.7071068}{2}=0.8535534$.
- $\alpha=\pi/3$: $\frac{1+0.5}{2}=0.7500000$.
- $\alpha=\pi/2$: $\frac{1+0}{2}=0.5000000$.

**Thresholded-model values** $P_1^{\mathrm{thr}}(\alpha)=\Phi(\cos\alpha/0.7978846)$. The arguments are $z=\cos\alpha/0.7978846$; we evaluate $\Phi$ from the standard normal table with linear interpolation between tabulated hundredths:

- $\alpha=0$: $z=1/0.7978846=1.2533141$. $\Phi(1.25)=0.8944$, $\Phi(1.26)=0.8962$; at $1.2533$: $0.8944+0.33\times0.0018=0.8950$.
- $\alpha=\pi/6$: $z=0.8660254/0.7978846=1.0854371$. $\Phi(1.08)=0.8599$, $\Phi(1.09)=0.8621$; at $1.0854$: $0.8599+0.54\times0.0022=0.8611$.
- $\alpha=\pi/4$: $z=0.7071068/0.7978846=0.8862269$. $\Phi(0.88)=0.8106$, $\Phi(0.89)=0.8133$; at $0.8862$: $0.8106+0.62\times0.0027=0.8123$.
- $\alpha=\pi/3$: $z=0.5/0.7978846=0.6266571$. $\Phi(0.62)=0.7324$, $\Phi(0.63)=0.7357$; at $0.6267$: $0.7324+0.67\times0.0033=0.7346$.
- $\alpha=\pi/2$: $z=0$; $\Phi(0)=0.5000$ exactly.

**Deviations** $\Delta(\alpha)=P_1^{\mathrm{thr}}(\alpha)-P_1^{\mathrm{QM}}(\alpha)$:

- $\alpha=0$: $0.8950-1.0000=-0.1050$.
- $\alpha=\pi/6$: $0.8611-0.9330=-0.0719$.
- $\alpha=\pi/4$: $0.8123-0.8536=-0.0413$.
- $\alpha=\pi/3$: $0.7346-0.7500=-0.0154$.
- $\alpha=\pi/2$: $0.5000-0.5000=0.0000$.

**Root-mean-square deviation** over the five points:

$$\mathrm{RMS}=\sqrt{\frac{0.1050^2+0.0719^2+0.0413^2+0.0154^2+0^2}{5}}=\sqrt{\frac{0.011025+0.005170+0.001706+0.000237+0}{5}}=\sqrt{\frac{0.0181375}{5}}=\sqrt{0.0036275}\approx0.0602.$$

The largest single deviation is $|\Delta(0)|=0.1050$ at $\alpha=0$, where the Born rule demands certainty ($P=1$) but the noisy threshold map yields $\Phi(1.2533)\approx0.8950$. This is structural, not numerical: for any finite $\sigma_n$, $\Phi(1/\sigma_n)<1$, so the thresholded Gaussian map can never reproduce the Born rule's certainty at $\alpha=0$; and as $\sigma_n\to0$ the map becomes a step function, restoring certainty at the endpoints but destroying the linear central regime that the slope matching was built to secure. The two requirements are in direct tension, and no single $\sigma_n$ removes it.

### 4.5 CHSH bound for deterministic local thresholded models

In a deterministic local model, each outcome is a function of the local setting and the shared field configuration $\lambda$: $A=A(a,\lambda)$, $A'=A(a',\lambda)$, $B=B(b,\lambda)$, $B'=B(b',\lambda)$, each in $\{-1,+1\}$. The CHSH combination for a fixed $\lambda$ is

$$S_\lambda=A(B+B')+A'(B-B').$$

Since $B,B'\in\{-1,+1\}$: if $B=B'$ then $B+B'=\pm2$ and $B-B'=0$, so $S_\lambda=\pm2A=\pm2$; if $B=-B'$ then $B+B'=0$ and $B-B'=\pm2$, so $S_\lambda=\pm2A'=\pm2$. In all cases $|S_\lambda|\le2$. Averaging over $\lambda$ with any distribution $\rho(\lambda)$ preserves the bound:

$$|S|=\left|\int S_\lambda\,\rho(\lambda)\,d\lambda\right|\le\int|S_\lambda|\,\rho(\lambda)\,d\lambda\le2.$$

This holds for every member of the class defined by A1–A3 with deterministic threshold readout, because thresholding a local field value yields a deterministic local outcome function. Stochastic readout noise does not help: averaging a noisy outcome is equivalent to averaging over an enlarged $\lambda$ that includes the noise, which remains local.

**Quantum value.** Take $a=0$, $a'=\pi/2$, $b=\pi/4$, $b'=-\pi/4$, with $E_{\mathrm{QM}}(a,b)=-\cos(a-b)$:

- $E(a,b)=-\cos(0-\pi/4)=-\cos(\pi/4)=-0.7071068$.
- $E(a,b')=-\cos(0+\pi/4)=-\cos(\pi/4)=-0.7071068$.
- $E(a',b)=-\cos(\pi/2-\pi/4)=-\cos(\pi/4)=-0.7071068$.
- $E(a',b')=-\cos(\pi/2+\pi/4)=-\cos(3\pi/4)=+0.7071068$.

$$S=-0.7071068-0.7071068-0.7071068-0.7071068=-2.8284271,\qquad|S|=2\sqrt{2}\approx2.8284.$$

(Check: $2\sqrt{2}=2\times1.4142136=2.8284271$.) The gap is $2.8284-2=0.8284$: the quantum prediction exceeds the deterministic local thresholded-model bound by a factor $2\sqrt{2}/2=\sqrt{2}\approx1.4142$.

### 4.6 Excess noise cannot close the gap

One might ask whether increasing the noise $\sigma_n$, making the threshold map more gradual, could push $|S|$ past $2$. It cannot within A1–A3: the CHSH derivation above nowhere used the value of $\sigma_n$; it used only locality and per-$\lambda$ determinism of the outcome function. Noise enlarges $\lambda$ but does not change the bound. To exceed $|S|=2$ the model would need nonlocal dynamics (violating A2) or a non-thresholding, non-discretizing readout (violating A3). This sharpens the localization of the uniqueness failure: the axioms admit the thresholded Gaussian calculus, which is empirically distinguishable from quantum mechanics both in single-system statistics (Section 4.4) and in entanglement correlations (Section 4.5).

### 4.7 Statistical power projection for distinguishing $\mathcal{C}_L$ from $\mathcal{C}_Q$

**This subsection is a projection, not a measurement.** Assumptions: (i) each calculus is run $n$ times under identical preparation; (ii) outcomes are Bernoulli with $P_1^{(Q)}=0.3174$ and $P_1^{(L)}=0.1587$; (iii) a $3$-standard-deviation separation of the two observed frequencies is required. The pooled proportion is

$$\bar{p}=\frac{0.3174+0.1587}{2}=\frac{0.4761}{2}=0.23805,$$

and the standard error of the difference of two proportions with $n$ trials each is

$$\mathrm{se}=\sqrt{\frac{2\,\bar{p}(1-\bar{p})}{n}}=\sqrt{\frac{2\times0.23805\times0.76195}{n}}=\sqrt{\frac{0.36276}{n}}=\frac{0.60230}{\sqrt{n}}.$$

Requiring $3\,\mathrm{se}\le\Delta P=0.1587$:

$$n\ge\left(\frac{3\times0.60230}{0.1587}\right)^2=\left(\frac{1.80690}{0.1587}\right)^2=(11.385)^2=129.6.$$

Approximately $n=130$ trials per calculus therefore suffice for a $3\sigma$ discrimination under these assumptions. The uncertainty in this projection is dominated by the assumed Gaussian ensemble; for heavier-tailed field distributions the tail probabilities — and hence $\Delta P$ and $n$ — change, though the factor-of-two structure at $\Theta=g$ persists for any symmetric density.

### 4.8 Sensitivity to threshold

At threshold $\Theta=4$ with $g=1$: the quadratic calculus fires when $|x|\ge\sqrt{4}=2$, giving

$$P_1^{(Q)}=2(1-\Phi(2))=2(1-0.9772)=2\times0.0228=0.0456,$$

while the linear calculus gives

$$P_1^{(L)}=1-\Phi(2)=0.0228.$$

The factor of $2$ is again exact, confirming that the non-uniqueness is not an artifact of the particular threshold chosen.

## 5. Results

All numerical results below are those computed in Section 4; no simulation or experimental data are reported.

1. **Non-uniqueness of the readout calculus.** Two distinct calculi, $\mathcal{C}_L$ and $\mathcal{C}_Q$, both satisfy A1–A3 exactly, yet yield $P_1^{(L)}=0.1587$ and $P_1^{(Q)}=0.3174$ at $\Theta=1$, $g=1$ (Sections 4.1–4.2), a structural factor of exactly $2$ (Section 4.3). The same factor holds at $\Theta=4$ ($0.0228$ versus $0.0456$, Section 4.8). The readout calculus is therefore not unique within the axiom class.

2. **Born-rule reproduction is approximate only.** The slope-matched noisy threshold detector with $\sigma_n=\sqrt{2/\pi}\approx0.7978846$ deviates from the Born rule by up to $|\Delta(0)|=0.1050$ at $\alpha=0$, with $\mathrm{RMS}=0.0602$ over the five-point grid $\alpha\in\{0,\pi/6,\pi/4,\pi/3,\pi/2\}$ (Section 4.4). The deviation at the certainty point is structural for any finite noise.

3. **CHSH bound.** Every deterministic local thresholded readout obeys $|S|\le2$, while the quantum prediction at the standard angles is $|S|=2\sqrt{2}\approx2.8284$, a gap of $0.8284$ (Section 4.5). Readout noise cannot close the gap (Section 4.6).

4. **Distinguishability projection.** Under the stated assumptions (Bernoulli outcomes with $P_1^{(Q)}=0.3174$ and $P_1^{(L)}=0.1587$; $3\sigma$ separation), approximately $n=130$ trials per calculus suffice to distinguish the two conventions (Section 4.7). This is a projection, not a measurement.

## 6. Discussion

**Limitations.** The analysis is deliberately minimal, and each minimality choice is a limitation. First, the field ensemble is a unit-variance Gaussian; for heavier-tailed or asymmetric ensembles the absolute probabilities $P_1^{(L)}$ and $P_1^{(Q)}$ change, although the factor-of-two structure at $\Theta=g$ persists for any symmetric density. Second, the Born-rule comparison uses the single most favorable linear encoding $x(\alpha)=\cos\alpha$; other encodings were not surveyed, so the reported deviations ($0.1050$ maximum, $0.0602$ RMS) bound only this encoding. Third, the statistical power figure $n\approx130$ is a projection resting on Gaussian approximations to Bernoulli frequencies and on the assumed ensemble; it carries no experimental validation. Fourth, the one-dimensional field value is a simplification; real detectors integrate fields over space and time, and the extension of the counterexample to such integration is not carried out here.

**Failure modes of the argument.** The non-uniqueness result would fail if the programs' wording were read as fixing the amplifier class more narrowly than A1–A3 do — for example, if "nonlinear amplification" were stipulated to exclude the affine member $\mathcal{C}_L$, or if a physical principle (such as energy-like detection) were independently postulated to select $\mathcal{C}_Q$. In the first reading only one calculus remains in the class and the two-calculus counterexample collapses; the Born-rule mismatch of Section 4.4 would then carry the refutation alone, and it is weaker because it depends on the choice of encoding. The CHSH argument would fail if the readout were allowed to depend on distant settings, i.e. if A2 were relaxed.

**What would falsify our claims.** A demonstration that some deterministic, local, continuous-field model with thresholded discrete readout reproduces the Born rule exactly at all angles *and* violates $|S|\le2$ would falsify the central negative claims. Conversely, an argument that A1–A3 implicitly force a unique amplifier — via a symmetry, positivity, or energy-conservation principle derived from the axioms themselves rather than added to them — would restore the uniqueness claim and refute the counterexample. The single most decisive check is the certainty-point calculation of Section 4.4: if a finite-noise threshold map were shown with $\Phi(1/\sigma_n)=1$, our structural-deviation claim would be false; since $\Phi(z)<1$ for every finite $z$, that would require the map to be noiseless, which is the case our argument already excludes.

**Open questions.** (i) Do additional physically motivated principles select one member of the thresholded family? (ii) Can stochastic local readout evade the CHSH bound while remaining within a generalized A3? (iii) What is the best-approximation error of the thresholded family to the Born rule over all encodings, not just the linear one? (iv) Does the counterexample survive field integration over detector volumes?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The direct users are researchers in the classical-reconstruction programs under test and the reviewers who evaluate their claims. If the result holds, the programs' research plans change in one specific way: a selection principle for the amplifier must be stated as an explicit additional axiom, and papers in these programs must either supply it or drop the uniqueness language. Reviewers gain a concrete checklist item — "state the amplifier-selection principle" — in place of a philosophical dispute. No industrial or clinical user is named here; the work is foundational, and its value is that it converts an unfalsifiable uniqueness thesis into a falsifiable claim about a specified class of maps.

**(b) Current readiness.** This is purely analytical work that has not been peer reviewed: under the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and formulated; concept and application stated). No hardware, prototype, or experimental demonstration exists in this paper, and analytical work of this kind does not exceed TRL 3.

**(c) The smallest next test.** The cheapest decisive step is computational, not experimental: a numerical survey of the thresholded family over a grid of amplifier shapes $\mathcal{A}_g$, noise levels $\sigma_n$, and encodings $x(\alpha)$, computing the minimum achievable Born-rule deviation. The outcome that would refute this paper is a member of the family achieving zero deviation at all five angles of Section 4.4 while remaining deterministic and local. The smallest experimental step is the two-calculus detection experiment of Section 4.7: approximately $130$ trials per calculus at a fixed preparation, measuring the two detection frequencies; a failure of the frequencies to separate by about $0.1587$ at $3\sigma$ would undermine the assumed ensemble, not the logical counterexample.

**(d) Binding constraints.** The first binding constraint is the field ensemble: the projection $n\approx130$ assumes a unit-variance Gaussian field at the detector, and any real preparation yields whatever distribution the classical dynamics produces; the tail probabilities, and hence the required trial count, are sensitive to it. The second is detector characterization: distinguishing $\mathcal{C}_L$ from $\mathcal{C}_Q$ requires independent knowledge of the amplifier shape, which in a physical detector is set by materials and gain electronics not specified by the axioms. Whether a classical field preparation with controllable amplitude statistics can be realized at all is an open question this paper does not resolve.

**(e) Order-of-magnitude bounds.** The only quantitative projection is the trial count of Section 4.7: $n\approx130$ per calculus for $3\sigma$ separation, under the stated Bernoulli and Gaussian-ensemble assumptions. No cost, market, or performance figures are derivable from the present analysis, and none are asserted.

**(f) Risks and misuse.** The result could be misquoted as a refutation of the ontological thesis (continuous local deterministic fields), which it does not address; it refutes only the uniqueness of the bridging calculus. Conversely, the programs under test could cite the amplifier-selection escape hatch of Section 6 to dismiss the counterexample without ever stating the selection principle; the checklist item of part (a) is the guard against that move.

## 8. Conclusion

We formalized the proposed continuous-to-discrete readout map as a thresholded amplification triple, exhibited two distinct calculi within the stated axiom class that yield different outcome statistics ($0.1587$ versus $0.3174$, a structural factor of exactly $2$ that persists at $\Theta=4$), showed that a slope-matched threshold detector approximates but cannot reproduce the Born rule (maximum deviation $0.1050$ at the certainty point, RMS $0.0602$), and proved the CHSH bound $|S|\le2$ for all deterministic local thresholded readouts against the quantum value $2\sqrt{2}\approx2.8284$, with readout noise unable to close the gap. The uniqueness claim connecting continuous local deterministic fields plus irreversible discrete readout to quantum mechanics therefore fails at the level of the readout calculus: quantum statistics are one member of a broader family, and an explicit additional principle — a selection rule for the amplifier — is required to single them out. Stating that principle is now a well-defined, falsifiable task for the programs that assert uniqueness.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Quantum continuous measurements: The stochastic Schroedinger equations and the spectrum of the output. arXiv:1301.3626v2. https://arxiv.org/abs/1301.3626v2
[2] Beyond Quantum Theory: A Realist Psychobiological Interpretation of Physical Reality. arXiv:1610.09347v1. https://arxiv.org/abs/1610.09347v1
[3] Quantum Measurement, Information, and Completely Positive Maps. arXiv:quant-ph/0107090v1. https://arxiv.org/abs/quant-ph/0107090v1
[4] Entropy and information gain in quantum continual measurements. arXiv:quant-ph/0012115v1. https://arxiv.org/abs/quant-ph/0012115v1
[5] Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality. arXiv:2307.09558v1. https://arxiv.org/abs/2307.09558v1
[6] Entanglement, scaling, and the meaning of the wave function in protective measurement. arXiv:1402.1217v2. https://arxiv.org/abs/1402.1217v2
[7] Quantum Turing Machines: Local Transition, Preparation, Measurement, and Halting. arXiv:quant-ph/9809038v1. https://arxiv.org/abs/quant-ph/9809038v1
[8] QNFO: Continuum is Real
[9] QNFO: PQS AI-Evaluation Audit: Post-Quantum Synthesis Investigation and AI Gate-Check Analysis
[10] QNFO: POST QUANTUM SYNTHESIS
[11] QNFO: Principia Ontologica
