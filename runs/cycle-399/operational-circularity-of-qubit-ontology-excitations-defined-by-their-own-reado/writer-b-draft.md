# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Quantum hardware engineers certify qubits through a closed calibration loop in which control pulses, readout discriminators, and tomographic validation mutually calibrate one another. Because the calibration model is built from data that depend on the very model being calibrated, the loop is operationally circular, and it is unclear whether it certifies the qubit's physical nature or merely fixes an internal bookkeeping choice. We formalize the loop as a composite operator $T=\Gamma\circ\Phi$ acting on operational data $\mathcal{D}$, where $\Phi$ maps data to a Hilbert-space identification and $\Gamma$ generates predicted data from an identification. A contraction condition $L<1$ guarantees a unique fixed point and thus benign circularity; its violation permits multiple fixed points or continuous symmetry orbits, signalling ontological underdetermination. We derive the contraction criterion, exhibit a two-branch toy model with two exact fixed points, and compute the shot budget required to resolve ontology-discriminating observables under an assumed single-shot readout fidelity $F=0.99991$. The analysis shows that (i) convergence to a unique operational identification occurs in at most fourteen iterations for $L=0.6$, (ii) multiplicity can arise from branch selection alone, and (iii) resolving a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability demands $N\approx2.65\times10^{6}$ shots, while the minimal detectable asymmetry at $10^{4}$ shots is $\epsilon_{\min}\approx5.001\times10^{-3}$. These results separate harmless calibration circularity from genuine ontological ambiguity and give hardware designers concrete criteria for when out-of-loop probes are required.

## 1. Introduction

Quantum information processors rely on qubits—two-level subsystems that are initialized, manipulated by control pulses, and measured. The prevailing engineering view treats the qubit as a pre-existing physical degree of freedom whose parameters are accessed by calibration routines. In practice, calibration proceeds by a closed loop: a model of the qubit generates control waveforms; the resulting data are used to update the model; the updated model in turn defines the next set of control waveforms. Because the model and the data co-define each other, the loop is operationally circular. The question of what the pulses actually manipulate—an energy eigenmode, a field excitation, a collective circuit variable, or a two-level abstraction layered over a multi-level device—is answered, if at all, only by the loop itself [12], [14].

The real-world problem is that calibration engineers and hardware designers must decide whether standard calibration pipelines suffice to certify a qubit's physical nature, or whether additional out-of-loop probes are required. This decision now carries economic weight: device qualification, cross-platform benchmarking, and error-budget allocation all presuppose that "the qubit" named in a specification sheet refers to a well-defined physical entity. If the calibration loop is benign—converging to a unique, self-consistent identification—a single calibration routine yields a unique operational ontology, and certification is a solved problem. If the loop is underdetermined, the same operational data can support physically inequivalent ontologies (for example, an energy eigenmode versus a collective excitation), and any downstream algorithmic claim about "the qubit" inherits that ambiguity. A criterion that separates the two cases changes the design decision directly: it tells the engineer whether the existing pipeline is sufficient or whether a leakage-resolving or otherwise out-of-loop observable must be engineered into the device.

This circularity is unavoidable, but it can be either benign—converging to a unique, self-consistent identification of the qubit—or problematic, leaving multiple physically inequivalent identifications compatible with the same operational data. The present paper characterizes the boundary between the two regimes formally, and quantifies the measurement cost of escaping underdetermination once it is detected.

**Contributions.**
1. A formal definition of the calibration fixed-point problem, with the composite operator $T=\Gamma\circ\Phi$ and the notion of operational circularity (Section 3).
2. A derivation of the contraction condition that guarantees a unique fixed point, with explicit iteration counts for illustrative parameters (Section 4.3).
3. A two-branch toy model exhibiting multiple exact fixed points, demonstrating that ontological underdetermination can arise from branch selection alone despite local contractivity (Section 4.5).
4. A shot-budget calculation for an ontology-discriminating observable under an assumed readout fidelity, with the minimal detectable asymmetry computed at two shot counts (Sections 4.4 and 4.6).
5. A sensitivity analysis of symmetry-breaking perturbations and a discussion of the continuous $SO(3)$ orbit of data-compatible ontologies (Sections 4.6 and 6).

## 2. Background and Related Work

The immediate predecessor of this work is the QNFO paper under revision [12], which formalizes the calibration loop as the composite operator $T=\Gamma\circ\Phi$, derives the contraction criterion, and reports the iteration counts and shot budgets that Sections 4 and 5 of the present paper recompute and correct. A companion QNFO paper [14] develops the same theme from the certification side: it formalizes the calibration hierarchy of engineered qubits as an iterated map, constructs two ontologically distinct models—a two-level abstraction and a three-level anharmonic ladder—and proves that under any measurement chain confined to the computational subspace the models yield identical outcome statistics, with a total-variation distance $D_{\mathrm{TV}}=0$ for subspace-restricted measurements and $D_{\mathrm{TV}}=0.01$ for a leakage-resolving measurement with coupling $|c|=0.1$. That degeneracy result is the sharpest existing statement of the underdetermination problem, and the present paper's fixed-point and shot-budget analysis is designed to quantify the cost of breaking it.

The noise model used here treats readout errors as an irreversible loss of information without energy exchange. The dephasing literature provides the physical template: for a quantum open system with non-demolition coupling to a bosonic bath, the dephasing of the open system is tied to the quantum and thermal fluctuation of the bath, and any bath with weak couplings to the open system can be modeled as a collection of non-interacting bosons [2]. We use this structure as justification for modeling per-shot readout errors as independent Bernoulli events in the weak-coupling regime, while noting in Section 6 that correlated bath fluctuations would violate that independence.

The continuous-orbit result of Section 3.3 rests on equivariance under spin rotations. The symmetry framework of anisotropic spin models shows that spin-space symmetries need not be plain subgroups of $O(3)\times\mathrm{Isom}(\mathbb{R}^{3})$: anisotropic interactions twist them through cohomology invariants, and a spin-only group is defined as a subgroup of $SO(3)$ [4]. This matters for the qubit-ontology question because a calibration loop that is equivariant under a spin-rotation group cannot distinguish points on the group orbit; [4] shows that in anisotropic systems the relevant symmetry class can be strictly larger than the naive rotation group, which means the family of data-compatible identifications can be richer than the three-parameter $SO(3)$ orbit we treat as the base case.

The question of whether the controlled entity is an energy eigenmode or a collective variable is a question of coarse-graining. In the molecular-dynamics literature, coarse-graining a room-temperature ionic liquid to united-atom sites preserves the overall liquid structure and glassy dynamic properties such as nonexponential structural relaxation while accelerating the dynamics [3]. By analogy, the two-level qubit abstraction is a coarse-graining of a multi-level device: [3]'s finding that coarse-grained and atomistic descriptions can agree on the observables actually measured—while differing in the degrees of freedom they posit—is precisely the pattern that makes ontological underdetermination possible in quantum hardware.

The closed-loop structure of calibration also has an analogue in machine learning systems that improve themselves by feeding their own readout back into their internal state. Recurrent reasoning models can be improved at inference time by using the readout probabilities during inference to provide feedback to the latent states, with gains attributed to repulsion that helps trajectories leave unsolved states and readout-dependent weighting that retains solutions once reached [5]. This is a computational echo of the calibration loop: the readout both reports on and steers the state it reports on, and [5]'s observation that confidence and class separation can both be high for incorrect predictions is a warning that a self-consistent loop need not be a correct one.

Self-supervised loops that reconcile disagreement among their own predictions provide a second analogy. In object detection, an agent can fine-tune a pre-existing detector while exploring a new environment without human intervention, resolving disagreeing pseudo-labels by accumulating predictions into a three-dimensional voxel space and retraining on the reconciled labels [6]. The reconciliation step is an out-of-loop consistency check in miniature: it uses structure external to the detector's own outputs to adjudicate among them, which is the role we propose for leakage-resolving observables in Section 7. A related exploration-driven variant reaches a mean Average Precision of $46.60$, a $6.27\%$ improvement over the off-the-shelf detector, by combining an uncertainty-based exploration reward with the same disagreement-reconciliation module [10]; the quantitative point—that adding an active probe improves the self-trained system measurably—supports the design pattern of Section 7(c).

The epistemological background is the claim that a "thing" is a temporary knot of relations rather than a noun-like substrate, and that knowing is pattern recognition by a pattern recognizer [13]. Applied to qubits, this reframing says that the qubit label names a stable pattern of control-readout relations, and that asking what the qubit "really is" beyond those relations may be ill-posed unless additional relations are engineered. The present paper's contribution is to make that epistemological claim operational: the fixed-point condition states exactly when the knot of relations is self-consistent and unique.

Finally, embedding theory in quantum chemistry offers a structural precedent for defining a subsystem by projection. Dynamical configuration interaction combines Green's-function methodology with a many-body wave function in a strongly-correlated active space, adding energy-dependent corrections to the CI Hamiltonian [9]. The active space is not a pre-existing object but a chosen subspace whose effective Hamiltonian is constructed to reproduce the observables of interest; [9] notes that the effective subspace $\mathcal{R}$ is a large-band-gap system expected to be less correlated than the full Hilbert space. The qubit's computational subspace plays exactly this role, and the ontology question—eigenmode, field excitation, or collective variable—is the question of which physical embedding realizes the chosen active space.

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
encodes one iteration of the calibration loop. This is the formalization introduced in [12]; the present paper retains it and sharpens its consequences.

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
while $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ are physically inequivalent (different interpretations of the controlled entity). This is the operational version of the degeneracy proved in [14], where a two-level abstraction and a three-level anharmonic ladder yield identical outcome statistics under any measurement chain confined to the computational subspace.

A continuous source of underdetermination is **equivariance**: if a group $G$ (for example $SO(3)$ acting on Bloch-sphere axes) satisfies $T\circ g = g\circ T$ for all $g\in G$, then the entire orbit $\{g\cdot x^{*}\mid g\in G\}$ consists of fixed points. For a qubit, $SO(3)$ has dimension three, yielding three continuous descriptive parameters (two axis angles and one phase) invisible to any $G$-invariant statistic. As noted in Section 2, [4] shows that in anisotropic spin systems the relevant symmetry classes can exceed subgroups of $O(3)\times\mathrm{Isom}(\mathbb{R}^{3})$, so the three-parameter orbit is a lower bound on the continuous ambiguity in the general case.

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

At this count the statistical error is $\sigma_{p}=\sqrt{0.25/3.09\times10^{7}}=\sqrt{8.09\times10^{-9}}\approx9.0\times10^{-5}$, matching the floor by construction.

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
so $n=13$ iterations are required. For comparison, the companion analysis in [14] reports that calibration error falls below the readout noise floor after $k_{\min}=11$ iterations, with $e_{11}=4.8828125\times10^{-5}$, under its own error-reduction model; the two counts agree in order of magnitude, and both are far below any practical re-calibration budget.

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

The per-shot error floor $p_{e}=9\times10^{-5}$ implies that discrepancies $\delta\lesssim p_{e}$ are comparable to readout noise and therefore not resolvable without additional error mitigation. For reference, [14] reports a one-sigma shot budget of $N\ge2500$ shots to resolve a discrepancy $\Delta p=0.01$ once a leakage-resolving observable is introduced, and $N\ge22500$ shots for three-sigma resolution; the budgets here are larger because the target discrepancy $\delta=10^{-3}$ is ten times smaller and the confidence requirement is a Hoeffding bound rather than a one-sigma criterion.

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
The sequence converges to $x_{B}^{*}=1$ and never visits branch $A$. The final ontology is thus determined by the initial guess rather than by the data. This is the discrete analogue of the subspace-restricted degeneracy proved in [14]: both branches are internally consistent, and no datum inside the loop selects between them.

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

*R6 (Continuous orbit).* The $SO(3)$ equivariance described in Section 3.3 leaves three continuous descriptive parameters (two axis angles, one phase) unconstrained by any $G$-invariant statistic, implying an uncountable family of data-compatible ontologies; by the symmetry analysis of [4], anisotropic couplings can enlarge the symmetry class beyond plain rotation subgroups, so three is a lower bound on the orbit dimension in the general case.

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

### Ontological degeneracy and the role of out-of-loop probes

The sharpest statement of the underdetermination problem comes from [14]: a two-level abstraction and a three-level anharmonic ladder yield identical outcome statistics under any measurement chain confined to the computational subspace, with $D_{\mathrm{TV}}=0$ for subspace-restricted measurements and $D_{\mathrm{TV}}=0.01$ for a leakage-resolving measurement with $|c|=0.1$. The present paper adds the dynamical half of the picture: even when a unique fixed point exists (Proposition 1), the fixed point is unique only within the ontology family spanned by $\Phi$; the toy model of Section 4.5 shows that two internally consistent families can coexist, each with its own attracting fixed point. The circularity of the calibration loop is therefore broken only by extending the measurement chain beyond the computational subspace or by enforcing cross-platform consistency, as [14] concludes.

Introducing an observable that lies outside the computational subspace, such as a leakage-sensitive transition, can break the equivariance and collapse the orbit of fixed points. The quantitative shot budget of Section 4.4 is the design target for such a probe: a leakage-resolving measurement with coupling $|c|=0.1$ produces a discriminating signal $D_{\mathrm{TV}}=0.01$ [14], which at $\delta=10^{-3}$-scale resolution requirements maps to the $N=2.649159\times10^{6}$-shot budget derived here.

### Self-referential loops beyond quantum hardware

The pattern of a readout that both reports on and steers the state it reports on is not unique to quantum hardware. Recurrent reasoning models improved at inference time by feeding readout probabilities back into their latent states show that closed-loop steering can complement longer rollouts and multi-trajectory voting [5]; but the same work reports that confidence and class separation can both be high for incorrect predictions, and that no validated diagnostic yet predicts when the feedback will help [5]. Translated to calibration: self-consistency of the loop is not evidence of correctness, and a diagnostic that distinguishes benign from pathological circularity—which Proposition 1 supplies in the contractive case—is exactly what the machine-learning analogue lacks.

Self-supervised object detection offers a constructive template. A detector fine-tuned in a new environment without human labels resolves disagreements among its own pseudo-labels by accumulating predictions into an external three-dimensional structure and retraining on the reconciled labels [6], and adding an active exploration policy that maximizes detector uncertainty raises mean Average Precision to $46.60$, a $6.27\