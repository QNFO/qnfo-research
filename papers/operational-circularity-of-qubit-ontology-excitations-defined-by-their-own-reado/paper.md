# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Quantum hardware engineers certify qubits through a closed calibration loop in which control pulses, readout discriminators, and tomographic validation mutually calibrate one another. Because the calibration model is built from data that depend on the very model being calibrated, the loop is operationally circular, and it is unclear whether it certifies the qubit's physical nature or merely fixes an internal bookkeeping choice. We formalize the loop as a composite operator $T=\Gamma\circ\Phi$ acting on operational data $\mathcal{D}$, where $\Phi$ maps data to a Hilbert-space identification and $\Gamma$ generates predicted data from an identification. A contraction condition $L<1$ guarantees a unique fixed point and thus benign circularity; its violation permits multiple fixed points or continuous symmetry orbits, signalling ontological underdetermination. We derive the contraction criterion, exhibit a two-branch toy model with two exact fixed points, and compute the shot budget required to resolve ontology-discriminating observables under an assumed single-shot readout fidelity $F=0.99991$. The analysis shows that (i) convergence to a unique operational identification occurs in at most fourteen iterations for $L=0.6$, (ii) multiplicity can arise from branch selection alone, and (iii) resolving a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability demands $N\approx2.65\times10^{6}$ shots, while the minimal detectable asymmetry at $10^{4}$ shots is $\epsilon_{\min}\approx5.001\times10^{-3}$. These results separate harmless calibration circularity from genuine ontological ambiguity and give hardware designers concrete criteria for when out-of-loop probes are required.

## 1. Introduction

Quantum information processors rely on qubits—two-level subsystems that are initialized, manipulated by control pulses, and measured. The prevailing engineering view treats the qubit as a pre-existing physical degree of freedom whose parameters are accessed by calibration routines. In practice, calibration proceeds by a closed loop: a model of the qubit generates control waveforms; the resulting data are used to update the model; the updated model in turn defines the next set of control waveforms. Because the model and the data co-define each other, the loop is operationally circular. The question of what the pulses actually manipulate—an energy eigenmode, a field excitation, a collective circuit variable, or a two-level abstraction layered over a multi-level device—is answered, if at all, only by the loop itself [14].

The real-world problem is that calibration engineers and hardware designers must decide whether standard calibration pipelines suffice to certify a qubit's physical nature, or whether additional out-of-loop probes are required. This decision carries economic weight: device qualification, cross-platform benchmarking, and error-budget allocation all presuppose that "the qubit" named in a specification sheet refers to a well-defined physical entity. If the calibration loop is benign—converging to a unique, self-consistent identification—a single calibration routine yields a unique operational ontology, and certification reduces to a solved problem. If the loop is underdetermined, the same operational data can support physically inequivalent ontologies (for example, an energy eigenmode versus a collective excitation), and any downstream algorithmic claim about "the qubit" inherits that ambiguity. A criterion that separates the two cases changes the design decision directly: it tells the engineer whether the existing pipeline is sufficient or whether a leakage-resolving or otherwise out-of-loop observable must be engineered into the device.

This circularity is unavoidable, but it can be either benign—converging to a unique, self-consistent identification of the qubit—or problematic, leaving multiple physically inequivalent identifications compatible with the same operational data. The present paper characterizes the boundary between the two regimes formally, and quantifies the measurement cost of escaping underdetermination once it is detected.

**Contributions.**
1. A formal definition of the calibration fixed-point problem, with the composite operator $T=\Gamma\circ\Phi$ and the notion of operational circularity (Section 3).
2. A derivation of the contraction condition that guarantees a unique fixed point, with explicit iteration counts for illustrative parameters (Section 4.3).
3. A two-branch toy model exhibiting multiple exact fixed points, demonstrating that ontological underdetermination can arise from branch selection alone despite local contractivity (Section 4.5).
4. A shot-budget calculation for an ontology-discriminating observable under an assumed readout fidelity, with the minimal detectable asymmetry computed at two shot counts (Sections 4.4 and 4.6).
5. A sensitivity analysis of symmetry-breaking perturbations and a discussion of the continuous $SO(3)$ orbit of data-compatible ontologies (Sections 4.6 and 6).

## 2. Background and Related Work

This paper formalizes the calibration loop as the composite operator $T=\Gamma\circ\Phi$ and derives its contraction criterion in Sections 3 and 4. The problem of ontological underdetermination of the qubit by its own metrology is posed in [14]; to make it concrete, we construct here an illustrative degeneracy model of our own: a two-level abstraction and a three-level anharmonic ladder that yield identical outcome statistics under any measurement chain confined to the computational subspace, with a total-variation distance $D_{\mathrm{TV}}=0$ for subspace-restricted measurements and $D_{\mathrm{TV}}=0.01$ for a leakage-resolving measurement at an assumed coupling $|c|=0.1$. This construction is an assumption of the present paper, not a proved result of [14], and the fixed-point and shot-budget analysis below is designed to quantify the cost of breaking it.

The noise model used here treats readout errors as an irreversible loss of information without energy exchange. The dephasing literature provides the physical template: for a quantum open system with non-demolition coupling to a bosonic bath, the dephasing of the open system is tied to the quantum and thermal fluctuation of the bath, and any bath with weak couplings to the open system can be modeled as a collection of non-interacting bosons [2]. We use this structure as justification for modeling per-shot readout errors as independent Bernoulli events in the weak-coupling regime, while noting in Section 6 that correlated bath fluctuations would violate that independence.

The continuous-orbit result of Section 3.3 rests on equivariance under spin rotations. We take as a working assumption of this paper that spin-space symmetries need not be plain subgroups of $O(3)\times\mathrm{Isom}(\mathbb{R}^{3})$; the symmetries of anisotropic spin interaction models are the subject of [4]. This matters for the qubit-ontology question because a calibration loop that is equivariant under a spin-rotation group cannot distinguish points on the group orbit; if the relevant symmetry class in an anisotropic system is larger than the naive rotation group, the family of data-compatible identifications can be richer than the three-parameter $SO(3)$ orbit we treat as the base case.

The question of whether the controlled entity is an energy eigenmode or a collective variable is a question of coarse-graining. In the molecular-dynamics literature, [3] studies a coarse-grained model of an ionic liquid that exhibits fragility, Stokes-Einstein violation, and correlated local excitations. By analogy, the two-level qubit abstraction is a coarse-graining of a multi-level device: a reduced description can carry correlated local structure of its own, as in the coarse-grained ionic-liquid model of [3], and this is the pattern that makes ontological underdetermination possible in quantum hardware.

The closed-loop structure of calibration also has an analogue in machine-learning systems that improve themselves by feeding their own readout back into their internal state. Recurrent reasoners can be steered at inference time using readout feedback, the mechanism studied in [5]. This is a computational echo of the calibration loop: the readout both reports on and steers the state it reports on, and the loop's self-consistency alone is no guarantee that its output is correct.

Self-supervised loops that reconcile disagreement among their own predictions provide a second analogy. In object detection, an agent can fine-tune a pre-existing detector while exploring a new environment without human intervention, resolving disagreeing pseudo-labels by accumulating predictions into a three-dimensional voxel space and retraining on the reconciled labels [6]. The reconciliation step is an out-of-loop consistency check in miniature: it uses structure external to the detector's own outputs to adjudicate among them, which is the role we propose for leakage-resolving observables in Section 7. A related exploration-driven variant fine-tunes a pre-existing detector by combining an uncertainty-based exploration reward with the same disagreement-reconciliation module [10]; the design point—that adding an active probe to the self-training loop is the mechanism that work studies—supports the design pattern of Section 7(c).

Practical deployments of automated recognition systems also exhibit error-handling gaps: a study of how blind users handle object-recognition errors documents strategies and challenges arising when automated recognition fails in deployment [8]. The analogy for calibration is that operational data can be ambiguous in ways the operating loop itself does not flag, which motivates explicit out-of-loop diagnostics rather than reliance on the loop's own success signals.

Finally, embedding theory in quantum chemistry offers a structural precedent for defining a subsystem by projection. Dynamical configuration interaction combines Green's-function methodology with a many-body wave function in a strongly-correlated active space, adding energy-dependent corrections to the CI Hamiltonian [9]. The active space is not a pre-existing object but a chosen subspace whose effective Hamiltonian is constructed to reproduce the observables of interest; In such an embedding, the chosen subspace is not a pre-existing object but a constructed effective system whose observables the embedding is built to reproduce. The qubit's computational subspace plays exactly this role, and the ontology question—eigenmode, field excitation, or collective variable—is the question of which physical embedding realizes the chosen active space.

The epistemological background of [13] is an epistemology of knowing as patterns; as a framing assumption of this paper, a "thing" is a temporary knot of relations rather than a noun-like substrate, and knowing is pattern recognition by a pattern recognizer. Applied to qubits, this framing says that the qubit label names a stable pattern of control-readout relations, and that asking what the qubit "really is" beyond those relations may be ill-posed unless additional relations are engineered. The present paper's contribution is to make that epistemological claim operational: the fixed-point condition states exactly when the knot of relations is self-consistent and unique.

## 3. Methods

### 3.1 Operational data and ontology maps

Let $\mathcal{D}$ denote the space of operational data, i.e. sequences of control waveforms, their settings, and readout outcomes. Let $\mathcal{O}$ denote the space of Hilbert-space identifications, each specifying a two-level subspace $\{|0\rangle,|1\rangle\}$ together with a Hamiltonian $H$, a readout observable $M$, and error channels $\{L_k\}$, as well as a physical interpretation (eigenmode, field excitation, collective variable).

An **ontology map**
$$
\Phi:\mathcal{D}\to\mathcal{O}
$$
assigns to any datum $x\in\mathcal{D}$ an identification $\Phi(x)$.

A **realization map**
$$
\Gamma:\mathcal{O}\to\mathcal{D}
$$
produces the predicted data that would be observed if the identification were correct.

Calibration seeks a **fixed point** $x^{*}\in\mathcal{D}$ satisfying
$$
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr).
$$
The composite operator
$$
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}
$$
encodes one iteration of the calibration loop. The present paper introduces this formalization and sharpens its consequences.

### 3.2 Contraction condition for benign circularity

Equip $\mathcal{D}$ with a metric $d_{\mathcal{D}}$ (for example, total-variation distance between predicted readout distributions plus a weighted parameter distance).

**Proposition 1.** If there exists $L\in(0,1)$ such that
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\forall x,x'\in\mathcal{D},
$$
then $T$ is a contraction and, by Banach's fixed-point theorem, possesses a unique fixed point $x^{*}$. Moreover, iterating from any initial datum $x_{0}$ yields
$$
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}),
$$
so convergence to tolerance $\varepsilon$ requires
$$
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
$$

When Proposition 1 holds, the circularity is benign: the loop converges to one self-consistent identification regardless of the starting point. When it fails, the loop may still converge, but the limit can depend on the initial datum, as the toy model of Section 4.5 shows.

### 3.3 Ontological underdetermination

If $T$ fails to be globally contractive, multiple fixed points may exist. Define two ontology maps $\Phi_{A},\Phi_{B}$ with corresponding realizations $\Gamma_{A},\Gamma_{B}$. Ontological underdetermination occurs when a datum $x^{*}$ satisfies
$$
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
$$
while $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ are physically inequivalent (different interpretations of the controlled entity). This is the operational version of the illustrative degeneracy constructed in Section 2, in which a two-level abstraction and a three-level anharmonic ladder yield identical outcome statistics under any measurement chain confined to the computational subspace.

A continuous source of underdetermination is **equivariance**: if a group $G$ (for example $SO(3)$ acting on Bloch-sphere axes) satisfies $T\circ g = g\circ T$ for all $g\in G$, then the entire orbit $\{g\cdot x^{*}\mid g\in G\}$ consists of fixed points. For a qubit, $SO(3)$ has dimension three, yielding three continuous descriptive parameters (two axis angles and one phase) invisible to any $G$-invariant statistic. As noted in Section 2, if the relevant symmetry class in an anisotropic spin system exceeds subgroups of $O(3)\times\mathrm{Isom}(\mathbb{R}^{3})$, the three-parameter orbit is a lower bound on the continuous ambiguity in the general case.

### 3.4 Discriminating observable and shot budget

To distinguish two ontologies that differ in the expectation value of a readout-accessible observable by $\delta$, we require enough measurement shots to resolve $\delta$ against readout noise. Assuming independent Bernoulli outcomes with per-shot error probability $p_{e}=1-F$, Hoeffding's inequality gives the required number of shots $N$ for failure probability $\alpha$:
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
Section 4 instantiates this formula using an assumed single-shot readout fidelity $F=0.99991$, hence $p_{e}=9\times10^{-5}$. The fidelity is an assumption of this paper, chosen as an illustrative high-performance value; no external source is cited for it, and all results that depend on it scale with $p_{e}$ in the ways made explicit in Section 4.

## 4. Analysis

All numerical inputs are listed explicitly; derivations are shown step by step. The only stochastic-model inputs are the assumed readout fidelity (Assumption 1) and the shot counts, both stated here; no empirical measurement is cited.

### 4.1 Readout error probability

Assumption 1: illustrative single-shot readout fidelity $F=0.99991$ (error probability $p_{e}=1-F$). This value is an assumption of the model, not a measurement reported by any cited source.

Derivation:
$$
p_{e}=1-F=1-0.99991=9\times10^{-5}.
$$

The expected number of erroneous outcomes in $N_{\text{trials}}=10^{6}$ shots is
$$
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90.
$$

Equivalently, one error is expected every $1/p_{e}=1/(9\times10^{-5})\approx1.11\times10^{4}$ shots.

### 4.2 Statistical uncertainty per setting

Assume $N=10^{4}$ shots per tomographic setting and a worst-case Bernoulli parameter $p=1/2$.

Standard error:
$$
\sigma_{p}=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.25}{10^{4}}}
=\sqrt{2.5\times10^{-5}}\approx5.00\times10^{-3}.
$$

Readout systematic floor $p_{e}=9\times10^{-5}$, so the ratio
$$
\frac{\sigma_{p}}{p_{e}}=\frac{5.00\times10^{-3}}{9\times10^{-5}}\approx55.6.
$$

Crossover shot count where statistical error equals the readout floor:
$$
N_{\text{cross}}\approx\frac{p(1-p)}{p_{e}^{2}}
=\frac{0.25}{(9\times10^{-5})^{2}}
=\frac{0.25}{8.1\times10^{-9}}\approx3.09\times10^{7}.
$$

At this count the statistical error is $\sigma_{p}=\sqrt{0.25/(3.09\times10^{7})}=\sqrt{8.09\times10^{-9}}\approx9.0\times10^{-5}$, matching the floor by construction.

### 4.3 Contraction convergence (illustrative parameters)

Model $T(x)=x^{*}+L\,(x-x^{*})$ with Lipschitz constant $L=0.6$, initial discrepancy $d_{0}=1$, target tolerance $\varepsilon=10^{-3}$.

Number of iterations:
$$
n\ge\frac{\ln(\varepsilon/d_{0})}{\ln L}
=\frac{\ln(10^{-3})}{\ln(0.6)}.
$$

Compute logarithms:
$$
\ln(10^{-3})=-3\ln10\approx-6.907755,\qquad
\ln(0.6)=\ln6-\ln10\approx-0.510826.
$$

Division:
$$
n\ge\frac{-6.907755}{-0.510826}\approx13.524,
$$
so the smallest integer $n$ satisfying the inequality is $n=14$.

Verification:
$$
0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3},
$$
confirming that fourteen iterations suffice.

A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$ yields
$$
n\ge\frac{\ln(9\times10^{-5}/5\times10^{-2})}{\ln(0.6)}
=\frac{\ln(1.8\times10^{-3})}{-0.510826}\approx12.3,
$$
so $n=13$ iterations are required. Both counts are far below any practical re-calibration budget, and the second count drives the residual discrepancy down to the assumed readout error floor $p_{e}=9\times10^{-5}$ itself.

### 4.4 Shot budget for ontology discrimination

Parameters: $F=0.99991$ ($p_{e}=9\times10^{-5}$), confidence level $\alpha=0.01$ (failure probability $1\%$).

Compute $\ln(2/\alpha)=\ln(200)\approx5.298317$.

For $\delta=10^{-3}$:
$$
N\ge\frac{5.298317}{2\times(10^{-3})^{2}}
=\frac{5.298317}{2\times10^{-6}}
=2.649159\times10^{6}.
$$

For $\delta=10^{-4}$:
$$
N\ge\frac{5.298317}{2\times(10^{-4})^{2}}
=\frac{5.298317}{2\times10^{-8}}
=2.649159\times10^{8}.
$$

The per-shot error floor $p_{e}=9\times10^{-5}$ implies that discrepancies $\delta\lesssim p_{e}$ are comparable to readout noise and therefore not resolvable without additional error mitigation. The budgets here scale as $\delta^{-2}$: a ten-times-larger target discrepancy $\delta=10^{-2}$ would lower the requirement to $N\ge2.649159\times10^{4}$ shots at the same $\alpha=0.01$, and replacing the conservative Hoeffding bound by a one-sigma criterion would lower it further by a constant factor.

### 4.5 Two-ontology toy model with two fixed points

Define a scalar datum $x\in\mathbb{R}$ and two candidate ontologies $A$ and $B$:
$$
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
$$
with distinct offsets $a\neq b$.

Fixed points satisfy $x=T_{A}(x)$ and $x=T_{B}(x)$:
$$
x_{A}^{*}=a,\qquad x_{B}^{*}=b.
$$

Both maps have Lipschitz constant $L=0.5<1$, so each branch is locally contractive. The selection rule keeps the branch whose prediction is closer to the current iterate.

Concrete parameters: $a=0$, $b=1$, initial guess $x_{0}=0.6$.

The basin boundary is the midpoint $m=(a+b)/2=0.5$. Since $x_{0}>m$, iteration follows branch $B$:
$$
\begin{aligned}
x_{1}&=0.5\times0.6+0.5=0.8,\\
x_{2}&=0.5\times0.8+0.5=0.9,\\
x_{3}&=0.5\times0.9+0.5=0.95,
\end{aligned}
$$
and in general
$$
x_{n}=1-0.4\times0.5^{\,n}.
$$
The sequence converges to $x_{B}^{*}=1$ and never visits branch $A$. The final ontology is thus determined by the initial guess rather than by the data. This is the discrete analogue of the subspace-restricted degeneracy constructed in Section 2: both branches are internally consistent, and no datum inside the loop selects between them.

### 4.6 Symmetry-breaking sensitivity (projection)

Define the minimal detectable asymmetry
$$
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
$$

Using $\sigma_{p}=5.00\times10^{-3}$ (Section 4.2) and $p_{e}=9\times10^{-5}$:
$$
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
=\sqrt{2.50081\times10^{-5}}
\approx5.001\times10^{-3}.
$$

At the crossover count $N_{\text{cross}}=3.09\times10^{7}$, the statistical error becomes $\sigma_{p}\approx9.0\times10^{-5}$, yielding
$$
\epsilon_{\min}\approx\sqrt{(9.0\times10^{-5})^{2}+(9\times10^{-5})^{2}}
=\sqrt{1.62\times10^{-8}}
\approx1.27\times10^{-4}.
$$

Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible under the assumed noise model. Because $\sigma_{p}\approx55.6\,p_{e}$ at $N=10^{4}$, the statistical term dominates $\epsilon_{\min}$ there, and the readout floor contributes only at the level of $p_{e}^{2}/(2\sigma_{p}^{2})\approx1.6\times10^{-4}$ in relative terms; the sensitivity is therefore governed almost entirely by the shot count until $N$ approaches $N_{\text{cross}}$.

## 5. Results

All quantitative statements follow from the derivations in Section 4.

*R1 (Convergence).* With $L=0.6$, $d_{0}=1$, and $\varepsilon=10^{-3}$, calibration reaches the target in $n=14$ iterations (Section 4.3). A variant with $d_{0}=5\times10^{-2}$ and $\varepsilon=p_{e}=9\times10^{-5}$ requires $n=13$ iterations. In this regime the loop is benign and yields a unique fixed point.

*R2 (Multiplicity).* The toy model of Section 4.5 possesses two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by a basin boundary at $0.5$. Starting from $x_{0}=0.6$ the iteration converges to $x_{B}^{*}=1$ via the closed form $x_{n}=1-0.4\times0.5^{n}$. The final ontology depends on the initial guess, demonstrating ontological underdetermination despite local contractivity.

*R3 (Readout error floor).* The assumed fidelity $F=0.99991$ yields $p_{e}=9\times10^{-5}$, i.e. one error per $1.11\times10^{4}$ shots; over $10^{6}$ trials the expected error count is $90$.

*R4 (Shot budget).* Resolving a discrepancy $\delta=10^{-3}$ at $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots (Section 4.4). For $\delta=10^{-4}$ the requirement rises to $2.649159\times10^{8}$ shots.

*R5 (Symmetry sensitivity).* At $N=10^{4}$ shots the minimal detectable asymmetry is $\epsilon_{\min}\approx5.001\times10^{-3}$; at the crossover count $N_{\text{cross}}\approx3.09\times10^{7}$ it improves to $\epsilon_{\min}\approx1.27\times10^{-4}$ (Section 4.6).

*R6 (Continuous orbit).* The $SO(3)$ equivariance described in Section 3.3 leaves three continuous descriptive parameters (two axis angles, one phase) unconstrained by any $G$-invariant statistic, implying an uncountable family of data-compatible ontologies; under the working assumption that anisotropic couplings can enlarge the symmetry class beyond plain rotation subgroups—a setting whose symmetries are studied in [4]—three is a lower bound on the orbit dimension in the general case.

## 6. Discussion

### Multi-parameter contraction analysis

The scalar model $T(x)=x^{*}+L\,(x-x^{*})$ used in Section 4.3 generalizes to a vector of calibration parameters $\mathbf{x}\in\mathbb{R}^{m}$ (for example transition frequency, drive amplitude, readout offset). The composite operator becomes $\mathbf{T}(\mathbf{x})=\boldsymbol{\Gamma}\!\bigl(\boldsymbol{\Phi}(\mathbf{x})\bigr)$. Equip $\mathbb{R}^{m}$ with the Euclidean norm $\|\cdot\|_{2}$ and assume that each component $T_{i}$ is differentiable. The Jacobian matrix $J(\mathbf{x})$ with entries $J_{ij}=\partial T_{i}/\partial x_{j}$ bounds the local Lipschitz constant:
$$
\|\mathbf{T}(\mathbf{x})-\mathbf{T}(\mathbf{x}')\|_{2}
\le \|J(\mathbf{x})\|_{2}\,\|\mathbf{x}-\mathbf{x}'\|_{2},
$$
where $\|J\|_{2}$ is the spectral norm (largest singular value). If a uniform bound $L_{\max}<1$ holds for all $\mathbf{x}$, then $\mathbf{T}$ is a global contraction and Banach's theorem guarantees a unique fixed point $\mathbf{x}^{*}$. In practice one can estimate $L_{\max}$ by measuring the sensitivity of each calibrated quantity to a small perturbation $\Delta\mathbf{x}$:
$$
L_{\max}\approx\max_{\mathbf{x}}\frac{\|\mathbf{T}(\mathbf{x}+\Delta\mathbf{x})-\mathbf{T}(\mathbf{x})\|_{2}}{\|\Delta\mathbf{x}\|_{2}}.
$$
A concrete worked example assumes $m=3$ parameters with partial derivatives $\partial T_{i}/\partial x_{j}=0.2$ for all $i,j$ (projection). Then each singular value of $J$ equals $0.6$, so $L_{\max}=0.6<1$ and the multi-parameter loop is contractive. The iteration bound of Section 3.2 generalizes to
$$
n\ge\frac{\ln(\varepsilon/\|\mathbf{x}_{0}-\mathbf{x}^{*}\|_{2})}{\ln L_{\max}}.
$$

### Limitations

The results of Sections 4 and 5 rest on the following assumptions, each of which the conclusions inherit.

1. **Illustrative Lipschitz constant.** The convergence count $n=14$ uses a fixed $L=0.6$; real calibration loops may exhibit state-dependent or iteration-dependent $L$, and a value of $L$ closer to unity inflates the count as $n\sim1/(1-L)$.
2. **Scalar toy model.** The two-branch example of Section 4.5 reduces the ontology space to a single scalar; in high dimension, multiplicity may appear as continuous families or limit cycles that the discrete two-point analysis does not capture.
3. **Assumed readout fidelity.** The value $F=0.99991$ is an assumption of this paper, not a measurement reported by any cited source; every shot budget and $\epsilon_{\min}$ scales with $p_{e}=1-F$ as shown in Section 4, and a worse fidelity raises $N_{\text{cross}}$ as $p_{e}^{-2}$.
4. **Independent Bernoulli noise.** The shot-budget calculation assumes independent per-shot errors. Correlated bath fluctuations, of the kind the dephasing analysis of [2] treats through the bath's quantum and thermal fluctuation, would invalidate the Hoeffding bound and generally increase the required $N$.
5. **Equivariance assumption.** The $SO(3)$ orbit argument presumes perfect rotational equivariance of the loop; any stray bias breaks the symmetry and can reduce the orbit dimension, and quantifying that reduction requires platform-specific modeling.
6. **Hoeffding looseness.** The bound $N\ge\ln(2/\alpha)/(2\delta^{2})$ is conservative; exact binomial sizing would lower the budgets in R4 by a constant factor, though not their $\delta^{-2}$ scaling.

### Failure modes

If calibration iterations become chaotic rather than contractive, no fixed point exists and the qubit lacks a self-consistent operational definition. If the symmetry orbit corresponds to physically distinct couplings—a collective mode versus a single-particle transition—rather than to a pure relabeling, the underdetermination is physical and not merely conventional. Both scenarios would invalidate the benign-circularity claim of R1 in its strong form.

### Falsification

The main result most vulnerable to falsification is R4, the shot-budget claim. A single demonstration that an ontology-discriminating observable differing by $\delta=10^{-3}$ between two candidate identifications is resolved at failure probability $\alpha=0.01$ with substantially fewer than $2.65\times10^{6}$ shots, under the stated noise model, would falsify the Hoeffding-based budget. Complementary falsifiers are: (i) convergence of calibration on disparate platforms to the same Hilbert-space identification including axis labeling, which would falsify the three-parameter equivariant orbit of R6; and (ii) observation of divergence or limit-cycle behavior in calibration iterations under controlled conditions, which would falsify the contraction-based uniqueness claim of R1. Conversely, if the toy model's branch selection is shown never to occur in a real calibration pipeline—because the loop's metric always separates the branches by more than the basin width—the multiplicity claim R2 loses its practical force, though it remains valid as a mathematical possibility.

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** Calibration engineers and quantum-hardware designers are the principal users. If the composite calibration operator $T$ satisfies the contraction condition, the analysis guarantees a unique fixed point reached in at most $n=14$ iterations for the illustrative parameters of Section 4.3; in that regime the standard pipeline suffices for device qualification, cross-platform benchmarking, and error-budget allocation, and no additional probe is required. If $T$ is non-contractive, the toy model of Section 4.5 shows that the final ontology can depend on the initial guess; the design decision that changes is then to engineer an out-of-loop, leakage-resolving observable into the device before downstream algorithms rely on the qubit label. The illustrative degeneracy constructed in Section 2—$D_{\mathrm{TV}}=0$ for subspace-restricted measurements versus $D_{\mathrm{TV}}=0.01$ for a leakage-resolving measurement at the assumed coupling $|c|=0.1$—identifies the specific observable class that breaks the ambiguity.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; under the NASA Technology Readiness Level definitions it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof of concept). No manufacturing readiness is claimed.

**(c) Smallest next test.** A minimal experiment would introduce an ontology-discriminating observable, such as a leakage-sensitive transition, on a trapped-ion qubit and measure it while varying the initial calibration guess. The experiment would collect $N=2.649159\times10^{6}$ shots, the budget derived in Section 4.4 for resolving $\delta=10^{-3}$ at $\alpha=0.01$. An outcome that refutes the contraction claim is a difference of at least $\delta$ between two runs starting from distinct initial guesses that both converge within $n\le14$ iterations; an outcome that supports it is a statistically indistinguishable difference $<\delta$ across initial guesses.

**(d) Binding constraints.** The constraints that bind first, in the order derived or grounded here, are: readout fidelity, since any degradation of $F$ raises $p_{e}$ and inflates the shot budget as $p_{e}^{-2}$ through $N_{\text{cross}}$ (Section 4.2); data-acquisition throughput, since delivering $2.65\times10^{6}$ shots requires sustaining roughly $10^{6}$ shots per second to complete acquisition in seconds; control of systematic drifts, since drift between iterations can raise the effective Lipschitz constant above unity and void Proposition 1; and symmetry-breaking bias fields, which must exceed $\epsilon_{\min}\approx5.001\times10^{-3}$ at $10^{4}$ shots, dropping to $\approx1.27\times10^{-4}$ at $N_{\text{cross}}\approx3.09\times10^{7}$ (Section 4.6). Whether coherence times permit the full budget at the required throughput is an open question this paper does not model.

**(e) Projected performance bounds (projection).** Under the stated assumptions—$F=0.99991$ and a data-acquisition rate of $10^{6}$ shots per second—the $2.649159\times10^{6}$-shot budget corresponds to an acquisition duration of approximately $2.65$ s. No cost figure is derivable from the inputs stated in this paper and none is projected.

**(f) Risks and misuse paths.** If the existence of multiple fixed points is misread as evidence that the qubit's physical nature is irrelevant, designers may forgo out-of-loop diagnostics, producing ambiguous device specifications. The mitigation is explicit: underdetection of multiplicity is a certification failure, and the criterion of Proposition 1 should be tested, not assumed, before a pipeline is trusted.

## 8. Conclusion

The uniqueness of a qubit's operational identification is a property of the calibration dynamics, not of the underlying physical system. When the composite operator $T=\Gamma\circ\Phi$ is a contraction, Banach's theorem guarantees a unique fixed point and the circularity is benign: for the illustrative parameters $L=0.6$, $d_{0}=1$, $\varepsilon=10^{-3}$, convergence takes $n=14$ iterations. When $T$ is non-contractive, either multiple discrete fixed points, as in the two-branch model with fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, or continuous $SO(3)$ symmetry orbits can arise, and the resulting ontological underdetermination cannot be resolved by the loop alone. The quantitative criteria derived here—an iteration count, a shot budget of $N=2.649159\times10^{6}$ for $\delta=10^{-3}$ at $\alpha=0.01$, and a minimal detectable asymmetry $\epsilon_{\min}\approx5.001\times10^{-3}$ at $10^{4}$ shots—give hardware designers concrete thresholds for deciding when the standard pipeline suffices and when an out-of-loop, leakage-resolving probe must be engineered. Future work would extend the scalar analysis to multi-parameter loops with measured Jacobians, incorporate correlated noise of the kind the dephasing literature treats, and execute the minimal discriminating experiment proposed in Section 7(c) on representative transmon, trapped-ion, and spin platforms.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.39.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[2] Factorization of Dephasing Process in Quantum Open System. arXiv:quant-ph/0608108. https://arxiv.org/abs/quant-ph/0608108
[3] Fragility, Stokes-Einstein violation, and correlated local excitations in a coarse-grained model of an ionic liquid. arXiv:1002.0860. https://arxiv.org/abs/1002.0860
[4] On the Symmetries of Anisotropic Spin Interaction Models. arXiv:2605.14969. https://arxiv.org/abs/2605.14969
[5] Steering Recurrent Reasoners at Inference Time with Readout Feedback. arXiv:2608.24136. https://arxiv.org/abs/2608.24136
[6] Self-improving object detection via disagreement reconciliation. arXiv:2302.10624. https://arxiv.org/abs/2302.10624
[8] Understanding How Blind Users Handle Object Recognition Errors: Strategies and Challenges. arXiv:2408.03303. https://arxiv.org/abs/2408.03303
[9] Dynamical configuration interaction: Quantum embedding that combines wave functions and Green's functions. arXiv:1810.12009. https://arxiv.org/abs/1810.12009
[10] Look Around and Learn: Self-Training Object Detection by Exploration. arXiv:2302.03566. https://arxiv.org/abs/2302.03566
[13] https://papers.qnfo.org/papers/knowing-patterns. QNFO: Knowing Patterns: An Epistemology for People Tired of Being Fixed.
[14] https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-. QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology.
