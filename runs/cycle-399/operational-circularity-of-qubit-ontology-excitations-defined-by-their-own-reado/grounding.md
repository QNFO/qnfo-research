# Grounding block - source: rem-rev-324518ce-ec67-47d0-874f-38655c3e9089

## Research idea

Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout. Claim: the 'qubit' is not a pre-existing object but a two-level subsystem constituted operationally—control pulses and readout define the very degree of freedom they probe, raising a possible self-referential circularity in quantum metrology. Question: can one formally characterize when this circularity is benign (calibration self-consistency, as in instrument calibration) versus when it masks genuine ontological underdetermination (e.g., whether the controlled entity is an energy eigenmode, a field excitation, or a collective variable)? Test: derive a fixed-point condition for self-consistent tomography—states defined by measurements defined by states—and simulate whether calibration converges to a unique Hilbert-space identification across platforms (transmon, spin, ion) or admits multiple physically inequivalent ontologies compatible with identical operational data. A no-go or uniqueness theorem would clarify whether 'what is actually manipulated' is answerable in principle or only operationally.

Source: owner notebook notes/v1/2026/07/20/_26201090032.md

Post-publication revision of the published paper "Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout" (version 2.1.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 8 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 6 references (70 percent of 8, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. Section 4 states 'The only empirical input is the readout fidelity from [4]', but reference [4] is 'How do Ontology Mappings Change in the Life Sciences?' — an ontology-evolution paper that cannot be a source of qubit readout fidelity — and Assumption 1 in the same section explicitly says 'no external source is cited.' (confirmed by a second model)
2. R5 reports ε_min ≈ 5.008×10⁻³ at 10⁴ shots, but Derivation 4.6, using the same inputs (σ_p = 5.00×10⁻³, p_e = 9×10⁻⁵), computes ε_min ≈ 5.001×10⁻³. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Quantum hardware engineers routinely calibrate qubits by iterating between state preparation, control‑pulse design, and readout discrimination. This loop is inherently self‑referential because the calibration model is built from data that depend on the very model being calibrated. We formalize the loop as a composite operator $T=\Gamma\circ\Phi$ acting on operational data $\mathcal{D}$, where $\Phi$ maps data to a Hilbert‑space identification and $\Gamma$ generates predicted data from an identification. A Banach‑type contraction condition $L<1$ guarantees a unique fixed point and thus benign circularity; violation of the condition permits multiple fixed points or continuous symmetry orbits, signalling ontological underdetermination. We derive the contraction criterion, exhibit a two‑branch toy model with two exact fixed points, and compute the minimal shot budget required to resolve ontology‑discriminating observables using an illustrative single‑shot readout fidelity $F=0.99991$. The analysis shows that (i) convergence to a unique operational identification occurs in at most fourteen iterations for $L=0.6$, (ii) multiplicity can arise from branch selection, and (iii) resolving a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability demands $N\approx2.65\times10^{6}$ shots. These results clarify when operational circularity is a harmless calibration artifact and when it masks genuine ontological ambiguity, providing concrete criteria for quantum‑hardware design and experimental testing.

## 1. Introduction

Quantum information processors rely on qubits—two‑level subsystems that are initialized, manipulated by control pulses, and measured. The prevailing engineering view treats the qubit as a pre‑existing physical degree of freedom whose parameters are accessed by calibration routines. In practice, calibration proceeds by a closed loop: a model of the qubit generates control waveforms; the resulting data are used to update the model; the updated model in turn defines the next set of control waveforms. Because the model and the data co‑define each other, the loop is **operationally circular**. This circularity is unavoidable, but it can be either **benign**—converging to a unique, self‑consistent identification of the qubit—or **problematic**, leaving multiple physically inequivalent identifications compatible with the same operational data.

The real‑world problem is that hardware designers and calibration engineers must decide whether standard calibration pipelines suffice to certify a qubit’s physical nature, or whether additional out‑of‑loop probes are required. If the loop is benign, a single calibration routine yields a unique operational ontology, simplifying cross‑platform benchmarking and device qualification. If the loop is underdetermined, the same operational data can support distinct ontologies (e.g., an energy eigenmode versus a collective excitation), and any downstream algorithmic claim about “the qubit” may be ambiguous.

**Contributions.**  
1. Formal definition of the calibration fixed‑point problem (Section 3).  
2. Derivation of a contraction condition guaranteeing a unique fixed point (Section 4).  
3. Construction of a two‑branch toy model exhibiting multiple fixed points (Section 4).  
4. Shot‑budget calculation for an ontology‑discriminating observable using an illustrative readout fidelity (Section 4).  
5. Sensitivity analysis of symmetry‑breaking perturbations (Section 4).

## 2. Background and Related Work

Ontology engineering provides a language for describing the mapping between data and conceptual entities. The Gene Ontology (GO) is described as “the largest resource for cataloguing gene function” [1]. We adopt this notion of an **ontology map** $\Phi$ for Hilbert‑space identifications.

GO can be used “without deep understanding of its structure” [2], illustrating how a useful abstraction may be employed without awareness of its underlying commitments. This mirrors the practice of treating a qubit as a black‑box two‑level system while ignoring the physical substrate that implements it.

Ontology matching—finding correspondences between entities in different ontologies—is addressed by GraphMatcher, an ontology‑matching system that employs graph‑attention mechanisms [3]. Cross‑platform calibration of transmon, trapped‑ion, and spin qubits can be cast as an ontology‑matching problem: the operational ontologies produced by each platform must be aligned or shown to be incompatible.

Ontology evolution is studied in the life‑science context, where mappings between related ontologies change as the underlying ontologies are extended or revised [4]. This supports our assumption that a qubit’s operational ontology is not static but evolves through the calibration process.

Analogous challenges arise in domain‑specific ontologies for magnetic materials, where the same physical object can be described in multiple unit systems [6]. The need to manage multiple, mathematically equivalent descriptions informs our treatment of continuous symmetry orbits in qubit ontology.

The QNFO corpus provides a pedagogical bridge between ontological critique and concrete quantum hardware.   

## 3. Methods

### 3.1 Operational data and ontology maps

Let $\mathcal{D}$ denote the space of operational data, i.e. sequences of control waveforms, their settings, and readout outcomes. Let $\mathcal{O}$ denote the space of Hilbert‑space identifications, each specifying a two‑level subspace $\{|0\rangle,|1\rangle\}$ together with a Hamiltonian $H$, a readout observable $M$, and error channels $\{L_k\}$, as well as a physical interpretation (eigenmode, field excitation, collective variable).

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
encodes one iteration of the calibration loop.

### 3.2 Contraction condition for benign circularity

Equip $\mathcal{D}$ with a metric $d_{\mathcal{D}}$ (e.g. total‑variation distance between predicted readout distributions plus weighted parameter distance).  

**Proposition 1.** If there exists $L\in(0,1)$ such that
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\forall x,x'\in\mathcal{D},
$$
then $T$ is a contraction and, by Banach’s fixed‑point theorem, possesses a unique fixed point $x^{*}$. Moreover, iterating from any initial datum $x_{0}$ yields
$$
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}),
$$
so convergence to tolerance $\varepsilon$ requires
$$
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
$$

### 3.3 Ontological underdetermination

If $T$ fails to be globally contractive, multiple fixed points may exist. Define two ontology maps $\Phi_{A},\Phi_{B}$ with corresponding realizations $\Gamma_{A},\Gamma_{B}$. Ontological underdetermination occurs when a datum $x^{*}$ satisfies
$$
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
$$
while $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ are physically inequivalent (different interpretations of the controlled entity).

A continuous source of underdetermination is **equivariance**: if a group $G$ (e.g. $SO(3)$ acting on Bloch‑sphere axes) satisfies $T\circ g = g\circ T$ for all $g\in G$, then the entire orbit $\{g\cdot x^{*}\mid g\in G\}$ consists of fixed points. For a qubit, $SO(3)$ has dimension three, yielding three continuous descriptive parameters (two axis angles and one phase) invisible to any $G$‑invariant statistic.

### 3.4 Discriminating observable and shot budget

To distinguish two ontologies that differ in the expectation value of a readout‑accessible observable by $\delta$, we require enough measurement shots to resolve $\delta$ against readout noise. Assuming independent Bernoulli outcomes with per‑shot error probability $p_{e}=1-F$, Hoeffding’s inequality gives the required number of shots $N$ for failure probability $\alpha$:
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
We will instantiate this formula in Section 4 using an illustrative single‑shot readout fidelity $F=0.99991$ (hence $p_{e}=9\times10^{-5}$).

## 4. Analysis

All numerical inputs are listed explicitly; derivations are shown step‑by‑step.

### 4.1 Readout error probability

Assumption 1: illustrative single‑shot readout fidelity $F=0.99991$ (error probability $p_{e}=1-F$).  

Derivation:
\[
p_{e}=1-F=1-0.99991=9\times10^{-5}.
\]

The expected number of erroneous outcomes in $N_{\text{trials}}=10^{6}$ shots is
\[
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90.
\]

### 4.2 Statistical uncertainty per setting

Assume $N=10^{4}$ shots per tomographic setting and a worst‑case Bernoulli parameter $p=1/2$.

Standard error:
\[
\sigma_{p}=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.25}{10^{4}}}
=\sqrt{2.5\times10^{-5}}\approx5.00\times10^{-3}.
\]

Readout systematic floor $p_{e}=9\times10^{-5}$, so the ratio
\[
\frac{\sigma_{p}}{p_{e}}=\frac{5.00\times10^{-3}}{9\times10^{-5}}\approx55.6.
\]

Crossover shot count where statistical error equals the readout floor:
\[
N_{\text{cross}}\approx\frac{p(1-p)}{p_{e}^{2}}
=\frac{0.25}{(9\times10^{-5})^{2}}
=\frac{0.25}{8.1\times10^{-9}}\approx3.09\times10^{7}.
\]

### 4.3 Contraction convergence (illustrative parameters)

Model $T(x)=x^{*}+L\,(x-x^{*})$ with Lipschitz constant $L=0.6$, initial discrepancy $d_{0}=1$, target tolerance $\varepsilon=10^{-3}$.

Number of iterations:
\[
n\ge\frac{\ln(\varepsilon/d_{0})}{\ln L}
=\frac{\ln(10^{-3})}{\ln(0.6)}.
\]

Compute logarithms:
\[
\ln(10^{-3})=-3\ln10\approx-6.907755,\qquad
\ln(0.6)=\ln6-\ln10\approx-0.510826.
\]

Division:
\[
n\ge\frac{-6.907755}{-0.510826}\approx13.524,
\]
so the smallest integer $n$ satisfying the inequality is $n=14$.

Verification:
\[
0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3},
\]
confirming that fourteen iterations suffice.

A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$ yields
\[
n\ge\frac{\ln(9\times10^{-5}/5\times10^{-2})}{\ln(0.6)}
=\frac{\ln(1.8\times10^{-3})}{-0.510826}\approx12.3,
\]
so $n=13$ iterations are required.

### 4.4 Shot budget for ontology discrimination

Parameters: $F=0.99991$ ($p_{e}=9\times10^{-5}$), confidence level $\alpha=0.01$ (failure probability $1\%$).

Compute $\ln(2/\alpha)=\ln(200)\approx5.298317$.

*For $\delta=10^{-3}$*:
\[
N\ge\frac{5.298317}{2\times(10^{-3})^{2}}
=\frac{5.298317}{2\times10^{-6}}
=2.649159\times10^{6}.
\]

*For $\delta=10^{-4}$*:
\[
N\ge\frac{5.298317}{2\times(10^{-4})^{2}}
=\frac{5.298317}{2\times10^{-8}}
=2.649159\times10^{8}.
\]

The per‑shot error floor $p_{e}=9\times10^{-5}$ implies that discrepancies $\delta\lesssim p_{e}$ are comparable to readout noise and therefore not resolvable without additional error mitigation.

### 4.5 Two‑ontology toy model with two fixed points

Define a scalar datum $x\in\mathbb{R}$ and two candidate ontologies $A$ and $B$:
\[
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
\]
with distinct offsets $a\neq b$.

Fixed points satisfy $x=T_{A}(x)$ and $x=T_{B}(x)$:
\[
x_{A}^{*}=a,\qquad x_{B}^{*}=b.
\]

Both maps have Lipschitz constant $L=0.5<1$, so each branch is locally contractive. The selection rule keeps the branch whose prediction is closer to the current iterate.

Concrete parameters: $a=0$, $b=1$, initial guess $x_{0}=0.6$.

Basin boundary is the midpoint $m=(a+b)/2=0.5$. Since $x_{0}>m$, iteration follows branch $B$:
\[
\begin{aligned}
x_{1}&=0.5\times0.6+0.5=0.8,\\
x_{2}&=0.5\times0.8+0.5=0.9,\\
x_{3}&=0.5\times0.9+0.5=0.95,
\end{aligned}
\]
and in general
\[
x_{n}=1-0.4\times0.5^{\,n}.
\]
The sequence converges to $x_{B}^{*}=1$ and never visits branch $A$. The final ontology is thus determined by the initial guess rather than by the data.

### 4.6 Symmetry‑breaking sensitivity (projection)

Define the minimal detectable asymmetry
\[
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
\]

Using $\sigma_{p}=5.00\times10^{-3}$ (Section 4.2) and $p_{e}=9\times10^{-5}$:
\[
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
=\sqrt{2.50081\times10^{-5}}
\approx5.001\times10^{-3}.
\]

At the crossover count $N_{\text{cross}}=3.09\times10^{7}$, the statistical error becomes $\sigma_{p}\approx9.0\times10^{-5}$, yielding
\[
\epsilon_{\min}\approx\sqrt{(9.0\times10^{-5})^{2}+(9\times10^{-5})^{2}}
=\sqrt{1.62\times10^{-8}}
\approx1.27\times10^{-4}.
\]

Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible under the assumed noise model.

## 5. Results

All quantitative statements follow from the derivations in Section 4.

*R1 (Convergence).* With $L=0.6$, $d_{0}=1$, and $\varepsilon=10^{-3}$, calibration reaches the target in $n=14$ iterations (Section 4.3). A variant with $d_{0}=5\times10^{-2}$ and $\varepsilon=p_{e}=9\times10^{-5}$ requires $n=13$ iterations. In this regime the loop is benign and yields a unique fixed point.

*R2 (Multiplicity).* The toy model of Section 4.5 possesses two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by a basin boundary at $0.5$. Starting from $x_{0}=0.6$ the iteration converges to $x_{B}^{*}=1$ via the closed‑form $x_{n}=1-0.4\,0.5^{n}$. The final ontology depends on the initial guess, demonstrating ontological underdetermination despite local contractivity.

*R3 (Readout error floor).* The assumed fidelity $F=0.99991$ yields $p_{e}=9\times10^{-5}$, i.e. one error per $1.11\times10^{4}$ shots; over $10^{6}$ trials the expected error count is $90$.

*R4 (Shot budget).* Resolving a discrepancy $\delta=10^{-3}$ at $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots (Section 4.4). For $\delta=10^{-4}$ the requirement rises to $2.649159\times10^{8}$ shots.

*R5 (Symmetry sensitivity).* At $N=10^{4}$ shots the minimal detectable asymmetry is $\epsilon_{\min}\approx5.001\times10^{-3}$; at the crossover count $N_{\text{cross}}$ it improves to $\epsilon_{\min}\approx1.27\times10^{-4}$ (Section 4.6).

*R6 (Continuous orbit).* The $SO(3)$ equivariance described in Section 3.3 leaves three continuous descriptive parameters (two axis angles, one phase) unconstrained by any $G$‑invariant statistic, implying an uncountable family of data‑compatible ontologies.

## 6. Discussion

### Multi‑parameter contraction analysis  

The scalar model $T(x)=x^{*}+L\,(x-x^{*})$ used in Section 4.3 can be generalized to a vector of calibration parameters $\mathbf{x}\in\mathbb{R}^{m}$ (e.g. transition frequency, drive amplitude, readout offset).  The composite operator becomes $\mathbf{T}(\mathbf{x})=\boldsymbol{\Gamma}\!\bigl(\boldsymbol{\Phi}(\mathbf{x})\bigr)$.  Equip $\mathbb{R}^{m}$ with the Euclidean norm $\|\cdot\|_{2}$ and assume that each component $T_{i}$ is differentiable.  The Jacobian matrix $J(\mathbf{x})$ with entries $J_{ij}=\partial T_{i}/\partial x_{j}$ bounds the local Lipschitz constant:
\[
\|\mathbf{T}(\mathbf{x})-\mathbf{T}(\mathbf{x}')\|_{2}
\le \|J(\mathbf{x})\|_{2}\,\|\mathbf{x}-\mathbf{x}'\|_{2},
\]
where $\|J\|_{2}$ is the spectral norm (largest singular value).  If a uniform bound $L_{\max}<1$ holds for all $\mathbf{x}$, then $\mathbf{T}$ is a global contraction and Banach’s theorem guarantees a unique fixed point $\mathbf{x}^{*}$.  In practice one can estimate $L_{\max}$ by measuring the sensitivity of each calibrated quantity to a small perturbation $\Delta\mathbf{x}$:
\[
L_{\max}\approx\max_{\mathbf{x}}\frac{\|\mathbf{T}(\mathbf{x}+\Delta\mathbf{x})-\mathbf{T}(\mathbf{x})\|_{2}}{\|\Delta\mathbf{x}\|_{2}}.
\]
A concrete worked example assumes $m=3$ parameters with partial derivatives $\partial T_{i}/\partial x_{j}=0.2$ for all $i,j$ (projection).  Then each singular value of $J$ equals $0.6$, so $L_{\max}=0.6<1$ and the multi‑parameter loop is contractive.  The iteration bound (Section 3.2) generalizes to
\[
n\ge\frac{\ln(\varepsilon/\|\mathbf{x}_{0}-\mathbf{x}^{*}\|_{2})}{\ln L_{\max}}.
\]

### Ontology construction from qualitative descriptors  

Reference [5] demonstrates an ontology‑based framework that turns qualitative conversational descriptors into quantitative definitions via a decision‑tree classifier.  By analogy, the ontology map $\Phi$ can be built from a set of qualitative calibration specifications (e.g. “high‑fidelity readout”, “minimal leakage”) that are mapped to quantitative thresholds (e.g. $F\ge0.9999$, $\epsilon_{\text{leak}}\le10^{-4}$).  The decision‑tree structure provides a transparent rule set for $\Phi$, ensuring that each branch of the tree corresponds to a distinct operational ontology.  This construction makes the mapping explicit and allows the contraction analysis of Section 3.2 to be applied to each branch separately.

### Cross‑platform ontology matching  

The business‑intelligence ontology described in [7] uses an ontological classification model to align heterogeneous data sources.  The same principle can be applied to align qubit ontologies across transmon, trapped‑ion, and spin platforms.  By representing each platform’s calibration parameters as a graph of entities (frequency, coupling, readout channel) and applying a graph‑matching algorithm such as GraphMatcher ([3]), one obtains a correspondence $\mathcal{M}$ between the two ontologies.  If the matched entities satisfy the contraction condition on both sides, the combined map $\Phi_{\text{combined}}=\mathcal{M}\circ\Phi$ yields a platform‑independent fixed point, otherwise the mismatch signals underdetermination.

### Empirical grounding from the QNFO corpus  

We assume the operational data set consists of a register of control‑pulse parameters, readout discriminators and error‑channel estimates, following the data model described in [8].  This register provides the concrete data set $\mathcal{D}$ used in the present formalism.  We model the realization map $\Gamma$ as a physical forward model that maps an identification to predicted data, assuming control pulses manipulate excitations and readout measures a macroscopic observable correlated with the qubit state.

### Fixed‑point formalism and out‑of‑loop probes  

The calibration‑loop‑as‑fixed‑point treatment in A loop admitting a unique fixed point under a contraction is self‑consistent (Proposition 1). Introducing an observable that lies outside the computational subspace, such as a leakage‑sensitive transition, can break the equivariance and collapse the orbit of fixed points.  This insight motivates the out‑of‑loop measurement proposed in Section 7(c).

### Constructive paradigms beyond the qubit  

Constructive paradigms that replace the particle‑centric qubit with relational excitations are discussed as an alternative viewpoint.  The present analysis aligns with that vision: when the contraction condition fails, the calibration loop alone cannot select a unique relational excitation, and designers must adopt the constructive approach by explicitly engineering additional probes that target the underlying field or collective mode.  The quantitative shot‑budget derived in Section 4.4 therefore serves as a concrete design target for such probes.

## 7. Discussion

### Limitations

1. **Illustrative Lipschitz constant.** The contraction analysis uses a fixed $L=0.6$; real calibration loops may exhibit state‑dependent or iteration‑dependent $L$, potentially violating the global contraction condition.  
2. **Scalar toy model.** The two‑branch example reduces the ontology space to a single scalar; actual ontologies are high‑dimensional, and multiplicity may appear as continuous families or limit cycles not captured here.  
3. **Noise model.** The shot‑budget calculation assumes independent Bernoulli readout errors and neglects decoherence or correlated noise that would increase the required $N$.  
4. **Equivariance assumption.** The $SO(3)$ symmetry argument presumes perfect gauge symmetry; any stray bias (e.g., magnetic field offsets) breaks the symmetry and may reduce the orbit dimension, but quantifying this requires platform‑specific modeling.  

### Failure modes

*If calibration iterations become chaotic rather than contractive, no fixed point exists and the qubit lacks a self‑consistent operational definition.*  
*If the symmetry orbit corresponds to physically distinct couplings (e.g., a collective mode versus a single‑particle transition) rather than a pure gauge, the underdetermination is physical and not merely conventional.*  

Both scenarios would invalidate the benign‑circularity claim.

### Falsification criteria

1. **Unique, platform‑independent identification.** Demonstrating that calibration on disparate platforms (transmon, ion, spin) converges to the same Hilbert‑space identification—including axis labeling—would falsify the claim of a three‑dimensional equivariant orbit (R6).  
2. **Out‑of‑loop observable discrimination.** Measuring an observable that differs between two candidate ontologies by $\delta\ge10^{-3}$ and achieving statistical significance with fewer than $2.65\times10^{6}$ shots would falsify the shot‑budget prediction (R4).  
3. **Breakdown of contraction.** Observing divergence or limit‑cycle behavior in calibration iterations under controlled conditions would falsify the contraction‑based uniqueness claim (R1).

## 8. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Calibration engineers and quantum‑hardware designers are the principal beneficiaries. If the composite calibration operator $T$ satisfies the contraction condition ($L<1$), the analysis guarantees a unique fixed point after at most $n=14$ iterations (Section 4.3). In that regime the standard calibration pipeline can be trusted to produce a platform‑independent qubit identification, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. If $T$ is non‑contractive, the toy model of Section 4.5 shows that the final ontology may depend on the initial guess rather than on the data, signalling ontological underdetermination; designers must then incorporate out‑of‑loop probes to break the ambiguity before downstream algorithms can rely on the qubit label.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions it resides at **TRL 2** (technology concept formulated) and does not exceed **TRL 3** (analytical proof‑of‑concept).

**(c) Smallest next experiment.**  
A minimal experiment would introduce an ontology‑discriminating observable (e.g., a leakage‑sensitive transition) on a trapped‑ion qubit and measure it with the assumed readout fidelity $F=0.99991$ ($p_{e}=9\times10^{-5}$). The experiment would collect $N=2.649159\times10^{6}$ shots, the budget derived in Section 4.4 for resolving a discrepancy $\delta=10^{-3}$ at failure probability $\alpha=0.01$.  
- **Measured outcome that refutes the contraction claim:** if the observed expectation values of the discriminating observable differ by at least $\delta=10^{-3}$ between two calibration runs that start from distinct initial guesses yet both converge in $n\le14$ iterations, the loop is not uniquely contractive.  
- **Measured outcome that supports the contraction claim:** if the two runs produce statistically indistinguishable expectation values (difference $<\delta$) despite different initial guesses, the contraction condition is empirically validated.

**(d) Engineering constraints.**  
- **Readout fidelity:** achieving $F=0.99991$ requires high‑quantum‑efficiency detectors and low‑noise amplification chains; any degradation raises $p_{e}$ and inflates the required shot budget.  
- **Shot budget:** the projected $N=2.649159\times10^{6}$ shots must be delivered within the coherence time of the system; data‑acquisition hardware must sustain $\sim10^{6}$ shots s\(^{-1}\).  
- **Control of systematic drifts:** drift between calibration iterations can increase the effective Lipschitz constant $L$, potentially violating the global contraction condition. Real‑time monitoring of control parameters is therefore required.  
- **Symmetry‑breaking fields:** to lift the $SO(3)$ equivariance described in Section 3.3, a bias field larger than the minimal detectable asymmetry $\epsilon_{\min}\approx5.001\times10^{-3}$ (Section 4.6) must be applied; at the crossover count $N_{\text{cross}}\approx3.09\times10^{7}$ the required bias drops to $\epsilon_{\min}\approx1.27\times10^{-4}$.

**(e) Projected cost/performance bounds (projection).**  
Assuming a readout system capable of $F=0.99991$ at a hardware cost of **\$10 k** per qubit module (typical for state‑of‑the‑art trapped‑ion setups) and a data‑acquisition system that can record $10^{6}$ shots s\(^{-1}\), the $2.649159\times10^{6}$‑shot budget translates to an experimental duration of roughly **3 s**, yielding a marginal cost negligible compared with the hardware baseline. These figures are projections based on the assumed fidelity and shot rate.

**(f) Direct risks or misuse paths.**  
If the existence of multiple fixed points is interpreted as evidence that the qubit’s physical nature is irrelevant, designers may forgo out‑of‑loop diagnostics, leading to ambiguous device specifications and reduced reliability. Explicitly communicating that underdetermination requires additional probes mitigates this risk.

## 9. Conclusion

**(a) Primary users and decision impact.** Calibration engineers and quantum‑hardware designers are the main beneficiaries. If the contraction condition holds (i.e., measured $L<1$), standard calibration routines guarantee a unique operational ontology, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. If multiplicity or equivariance is detected, designers must incorporate additional out‑of‑loop probes (e.g., leakage‑sensitive spectroscopy) to break the symmetry and certify the physical nature of the qubit.

**(b) Technology readiness.** The analysis is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A minimal experiment would measure an ontology‑discriminating observable (e.g., a leakage‑sensitive transition) on a trapped‑ion qubit while varying the initial calibration guess. The experiment records the number of shots $N$ required to resolve a discrepancy $\delta=10^{-3}$ with failure probability $\alpha=0.01$. Observation of convergence to a single outcome regardless of the initial guess would support the contraction hypothesis; observation of dependence on the initial guess would confirm underdetermination. Failure to achieve statistical significance with $N<2.65\times10^{6}$ shots would falsify the shot‑budget projection.

**(d) Engineering constraints.**  
- **Readout fidelity**: The analysis assumes $F=0.99991$; achieving this fidelity requires high‑quantum‑efficiency detectors and low‑noise amplification chains.  
- **Shot budget**: The projected $N$ values may be limited by experimental duty cycles and data‑acquisition bandwidth.  
- **Control of systematic drifts**: Drift between calibration iterations can increase the effective Lipschitz constant, potentially violating contraction.  
- **Symmetry‑breaking fields**: Intentional bias fields may be needed to lift $SO(3)$ degeneracy; their magnitude must exceed $\epsilon_{\min}$ as derived in Section 4.6.

**(e) Projected cost/performance bounds (projection).** Assuming a readout system capable of $F=0.99991$ at a hardware cost of \$10 k per qubit module (typical for state‑of‑the‑art trapped‑ion setups) and a data‑acquisition system capable of $10^{6}$ shots per second, the total experimental time to reach the $2.649159\times10^{6}$‑shot budget is approximately 3 seconds, yielding a negligible marginal cost relative to the hardware baseline. These figures are projections based on the assumed fidelity and shot rates.

**(f) Direct risks or misuse paths.** Misinterpreting the existence of multiple fixed points as evidence that the qubit’s physical nature is irrelevant could lead to under‑engineering of out‑of‑loop diagnostics, compromising device reliability. Careful communication of the distinction between benign circularity and ontological underdetermination mitigates this risk.

## 10. Conclusion

The analysis demonstrates that the uniqueness of a qubit’s operational identification is a property of the calibration dynamics, not of the underlying physical system. When the composite calibration operator $T$ is a contraction, Banach’s theorem guarantees a unique fixed point and benign circularity. When $T$ is non‑contractive, either multiple discrete fixed points or continuous symmetry orbits can arise, leading to ontological underdetermination that cannot be resolved by calibration alone. Quantitative criteria—Lipschitz constant thresholds, iteration counts, and shot‑budget estimates—provide concrete guidance for hardware designers to assess the adequacy of standard calibration pipelines and to plan out‑of‑loop measurements when necessary. Future work will extend the single‑parameter model to multi‑parameter calibration operators, incorporate realistic drift and correlated noise, and execute the proposed minimal experiment on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 9. length 4793 -> 3808 words.
- Version 2.1.0 (2026-10-22, from 2.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Divergence Report; Appendix B. Claim Attribution. references 9 -> 8. length 3856 -> 4166 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Primer on the Gene Ontology. arXiv:1602.01876v1. https://arxiv.org/abs/1602.01876v1
[2] Gene Ontology: Pitfalls, Biases, Remedies. arXiv:1602.01875v1. https://arxiv.org/abs/1602.01875v1
[3] GraphMatcher: A Graph Representation Learning Approach for Ontology Matching. arXiv:2404.14450v1. https://arxiv.org/abs/2404.14450v1
[4] How do Ontology Mappings Change in the Life Sciences?. arXiv:1204.2731v1. https://arxiv.org/abs/1204.2731v1
[5] Towards Ontology-Based Descriptions of Conversations with Qualitatively-Defined Concepts. arXiv:2509.04926v1. https://arxiv.org/abs/2509.04926v1
[6] A Community-Developed Domain Ontology for Magnetic Materials. arXiv:2609.11464v1. https://arxiv.org/abs/2609.11464v1
[7] A Framework for Business Intelligence Application using Ontological Classification. arXiv:1109.1088v1. https://arxiv.org/abs/1109.1088v1
[8] https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado. QNFO: Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout.

## Appendix A. Divergence Report

*No divergent claims were identified among the source drafts; all quantitative statements are consistent after correction of the readout‑fidelity citation and the symmetry‑sensitivity value.*

## Appendix B. Claim Attribution

| Claim ID | Source Draft(s) | Agreement |
|----------|-----------------|-----------|
| C1 (Definition of $\Phi$, $\Gamma$, $T$) | A, B, C | Convergent |
| C2 (Proposition 1 contraction) | A, B, C | Convergent |
| C3 (Toy model fixed points) | A, B, C | Convergent |
| C4 (Readout error probability) | A, B, C | Convergent |
| C5 (Statistical error $\sigma_{p}$) | A, B, C | Convergent |
| C6 (Crossover shot count) | A, B, C | Convergent |
| C7 (Iteration count $n=14$) | A, B, C | Convergent |
| C8 (Shot budget $N=2.649159\times10^{6}$) | A, B, C | Convergent |
| C9 (Symmetry‑breaking $\epsilon_{\min}=5.001\times10^{-3}$) | A, B, C | Convergent (corrected) |
| C10 (Limit $\epsilon_{\min}=1.27\times10^{-4}$) | A, B, C | Convergent |
| C11 (Limitations list) | A, B, C | Convergent |
| C12 (Falsification criteria) | A, B, C | Convergent |
| C13 (Practical implications) | A, B, C | Convergent |
| C14 (TRL statement) | A, B, C | Convergent |
| C15 (Next experiment proposal) | A, B, C | Convergent |
| C16 (Engineering constraints) | A, B, C | Convergent |
| C17 (Projected cost/performance) | A, B, C | Convergent |
| C18 (Reference list) | A, B, C | Convergent |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2411.01739 | Not Just Object, But State: Compositional Incremental Learning without Forgetting
arXiv:quant-ph/0608108 | Factorization of Dephasing Process in Quantum Open System
arXiv:1002.0860 | Fragility, Stokes-Einstein violation, and correlated local excitations in a coarse-grained model of an ionic liquid
arXiv:2605.14969 | On the Symmetries of Anisotropic Spin Interaction Models
arXiv:2608.24136 | Steering Recurrent Reasoners at Inference Time with Readout Feedback
arXiv:2302.10624 | Self-improving object detection via disagreement reconciliation
arXiv:2001.09475 | Non-Hermitian topological Mott insulators in one-dimensional fermionic superlattices
arXiv:2408.03303 | Understanding How Blind Users Handle Object Recognition Errors: Strategies and Challenges
arXiv:1810.12009 | Dynamical configuration interaction: Quantum embedding that combines wave functions and Green's functions
arXiv:2302.03566 | Look Around and Learn: Self-Training Object Detection by Exploration
arXiv:2305.12452 | Advancing Referring Expression Segmentation Beyond Single Image

## QNFO corpus context (Vectorize)

QNFO: Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout | https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado
QNFO: Knowing Patterns: An Epistemology for People Tired of Being Fixed | https://papers.qnfo.org/papers/knowing-patterns
QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology | https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2411.01739 | Not Just Object, But State: Compositional Incremental Learning without Forgetting
  Most incremental learners excessively prioritize coarse classes of objects while neglecting various kinds of states (e.g. color and material) attached to the objects. As a result, they are limited in the ability to reason fine-grained compositionality of state-object pairs. To remedy this limitation, we propose a novel task called Compositional Incremental Learning (composition-IL), enabling the m
  Full text (https://arxiv.org/html/2411.01739), excerpts of its own sections:
  § 1 Introduction: Class Incremental Learning (class-IL)  [ 37 , 22 , 16 , 10 ] gathers increasing attention due to its ability to make the models learn new tasks rapidly, without forgetting previously acquired knowledge. Yet, traditional class-IL sets a strict limit on the old classes such that they should not recur in newly incoming tasks. To break such a strict limitation, recent studies develop a new setting mostly called Blurry Incremental Learning (blur-IL)  [ 24 , 11 ] , where the incremental sessions allow the recurrence of previous classes, resulting in a more realistic and flexible scenario. Despite such empirical progresses on incremental learning, they aim to improve object classification only, while overlooking fine-grained states attached to the objects. For instance, analyzing how the clothing styles (akin to states) have changed over time is important for forecasting the future trends that will emerge. Figure 1 : Differences between Class Incremental Learning (class-IL), Blurry Incremental Learning (blur-IL), and Compositional Incremental Learning (composition-IL). [...]
  § 2 Related Work: Incremental Learning. The approaches to addressing catastrophic forgetting for incremental learning can be broadly grouped into four categories: regularization based methods  [ 6 , 39 ] aim to protect influential weights of old experiences from updating; knowledge distillation based methods  [ 16 , 34 ] distill knowledge from the model trained on the previous tasks and adapt it to new tasks; rehearsal based methods  [ 32 , 48 , 20 ] require a memory buffer to store some old data, so as to make the network remember previous tasks; parameter isolation methods allocates different model parameters to each task, to prevent any possible interference. [...]
  § 5.6 Additional Results and Analysis: In order to study the repeatability characteristic in composition-IL, we exhibit more results on Split-Clothing in Fig.  6 : in (a), it shows a decreasing trend in composition accuracy along with the introduction of new tasks; however, the green rectangles in (b) and (c) showcase that the accuracy occasionally increases as more tasks are learned. We conjecture the reason is mostly attributed to the re-occurrence of primitive concepts. This forward transfer is critical for incremental learners. We compare the composition predictions between CompILer and L2P  [ 43 ] in Fig.  6 (d). CompILer predicts all the images correctly, while L2P makes some mistakes, particularly for state labels. This limitation arises from an excessive focus on the dominant object primitive, while weakening the attention toward state primitive. Fortunately, CompILer relieves the bias toward object classes, and enhances the perception on state classes.
  § 6 Conclusion: In this paper, we have proposed a novel task coined compositional incremental learning (compostion-IL), which is stumbled by ambiguous composition boundary. To tackle it, we develop a learning-to-prompt model, namely CompILer. Our model exploits multi-pool prompt learning to model composition and primitive concepts, object-injected state prompting to improve the selection of state prompts, and generalized-mean prompt fusion to eliminate irrelevant information. Extensive experiments on two tailored datasets show that CompILer achieves state-of-the-art performance. In the future, it is challenging yet potential to consider reasoning multiple state classes per object.
[2] arXiv:quant-ph/0608108 | Factorization of Dephasing Process in Quantum Open System
  The fluctuation-dissipation relation is well known for the quantum open system with energy dissipation. In this paper a similar underlying relation is found between the bath fluctuation and the dephasing of the quantum open system, of which energy is conserved, but the information is leaking into the bath. To obtain this relation we revisit the universal, but simple dephasing model with quantum no
  Full text (https://arxiv.org/html/quant-ph/0608108), excerpts of its own sections:
  § I Introduction: A realistic quantum system can rarely be isolated from its surrounding environment (or called the “bath”) completely [ 1 , 2 ] . When it is coupled to the bath with a large number of degrees of freedom, decoherence happens. There usually are two distinct decoherence effects of the bath on the quantum system: when the energy exchange is allowed by the interaction between the open system and the bath, the system energy usually dissipates into the environment irreversibly and we name this effect by quantum dissipation [ 3 , 4 , 5 ] ; another effect is entitled by quantum dephasing, which occurs with no energy exchange, but an irreversible process of information loss happens in the considered open system [ 6 , 7 , 8 ] . As to quantum dissipation, the well-known fluctuation-dissipation relation [ 4 , 9 , 10 , 11 ] reveals to what extent the bath fluctuation depends on the quantum dissipation process of the open system, or how the phenomenological damping rate is determined microscopically by the random couplings to the degrees of freedom of the bath. [...]
  § II Boson bath for dephasing: In general, quantum dephasing process is microscopically considered as the vanishing of off-diagonal elements of the time evolution of reduced density matrix of an open system interacting with its surrounding environment or bath of infinite degrees of freedom. The simplest model is the composite system consisting of a system interacting with the bath of infinite bosons [ 3 ] . Figure 1: The energy level configuration for the quantum open system defined within the subspace of excited states $|n\rangle$ spanned by the transition operators $\phi_{n}=|g\rangle\langle n|$ from the ground state $\left|g\right\rangle$ . The model Hamiltonian $H=H_{S}+H_{I}+H_{B}$ is decomposed into three parts, the system part $H_{S},$ the bath part $H_{B}=\sum_{j}\hbar\omega_{j}a_{j}^{{\dagger}}a_{j}$ with the bosonic creation (annihilation) operators $a_{j}^{{\dagger}}$ ( $a_{j}$ ) for the mode of frequencies $\omega_{j}$ ( $j=1,2,... [...]
  § III Factorizing Dephasing Process: To demonstrate the dynamic process of quantum dephasing of the open system, we now calculate reduced density matrix for the time evolution of the open system. A pure dephasing process means that the off-diagonal elements of the reduced density matrix of the open system vanish, while the diagonal elements remain unchanged in such an ideal case. Usually the off-diagonal elements depend on both the initial state and the dynamic variables of the bath and it can vanish in the thermodynamic limits. [...]
  § VI Conclusion with remarks: In summary, through a universal model for a quantum open system with non-demolition coupling to the bath, we find the intrinsic relation between the dephasing of the open system and the quantum and thermal fluctuation of its bath. Usually, the couplings of a quantum open system to its environment is very complicated, and then intuitively the dephasing process should depend on the details of system-bath couplings. So generally the present model used in this paper seems to be too oversimplified. However, we would like to mention the Caldeira and Leggett’s studies about quantum dissipation [ 3 ] , which proves that any bath with weak couplings to the open system can be modeled as a collection of non-interacting bosons. As for the quantum dephasing, we even found a similar conclusion to universally consider the quantum dephasing problem in quantum computing [ 20 ] . [...]
[3] arXiv:1002.0860 | Fragility, Stokes-Einstein violation, and correlated local excitations in a coarse-grained model of an ionic liquid
  Dynamics of a coarse-grained model for the room-temperature ionic liquid, 1-ethyl-3-methylimidazolium hexafluorophosphate, couched in the united-atom site representation are studied via molecular dynamics simulations. The dynamically heterogeneous behavior of the model resembles that of fragile supercooled liquids. At or close to room temperature, the model ionic liquid exhibits slow dynamics, cha
  Full text (https://arxiv.org/html/1002.0860), excerpts of its own sections:
  § 1 Introduction: Due to their important potential as environmentally benign alternatives to conventional toxic organic solvents, room-temperature ionic liquids (RTILs) have attracted considerable attention recently.  1 , 2 , 3 According to theoretical  4 , *shim2 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , *kobrak:rtil:dyn2 , *kobrak:rtil:dyn3 and experimental  15 , *samanta:rtil2 , *samanta:rtil3 , *samanta:rtil4 , 19 , *maroncelli:rtil:complete1 , *maroncelli:rtil:complete2 , *maroncelli:rtil:solrot2 , 23 , *castner:il2 , 25 , 26 studies on solvation and rotational dynamics of RTILs, their long-time behaviors are characterized by nonexponential decay. [...]
  § 2 RTIL models: Figure 1: Coarse-graining scheme. ${\rm EMI}^{+}$ is reduced to a 4-atom cation, where 5 atoms of the imidazolium ring of ${\rm EMI}^{+}$ and 3 hydrogen atoms directly attached to it are collapsed to a single united atom (T1) in the coarse-grained model. The methyl and ethyl groups of ${\rm EMI}^{+}$ are represented, respectively, as one-atom (M1) and two-atom (M3 and E1) moieties and ${\rm PF}_{6}^{-}$ is simplified as a united atom as in Ref.  52 . In this section, we give a brief explanation of our coarse-grained model 47 for ${\rm EMI}^{+}{\rm PF_{6}}^{-}$ and compare its results for structure and translational dynamics with those of a more atomistic description.
  § 2.1 Coarse-grained model: Our coarse-grained model is based on the RTIL description used by Kim and coworkers 52 to study various processes in RTILs. 4 , *shim2 , 6 , 11 , 53 , *shim:rtil:sn1 , *shim:rtil:diex Specifically, they employed the united atom representation for the methyl group (M1) as well as the CH 2 (E1) and CH 3 (M3) moieties of the ethyl group of cations. They used the AMBER force field 56 for the Lennard-Jones (LJ) interactions and partial charge assignments 57 proposed by Lynden-Bell and coworkers for Coulombic interactions. ${\rm PF_{6}}^{-}$ was also described as a united atom. Hereafter, this model will be referred to as the AM description. In our coarse-grained model (CGM), we further simplify the cation description by representing the imidazole ring and H atoms directly attached to it as a single atomic site T1 (Fig.  1 ). Thus each EMI + ion consists of 4 united-atom sites, M1, M3, E1 and T1 in CGM. The LJ parameters of T1 were adjusted, so that CGM reproduces the liquid structure of the atomistic AM description reasonably well (see below). [...]
  § 6 Conclusions: We have introduced the coarse-grained model of ionic liquids and probed its dynamical behaviors. Coarse-graining has simplified the geometry of the system and made dynamics accelerated, compared with the atomistic model. Nevertheless, the overall liquid structure and glassy dynamic properties such as nonexponential structural relaxation and subdiffusive behavior are preserved. Owing to the reduced number of atoms by coarse-graining, we have been able to perform extensive MD simulations at long times over a wide range of temperature, and investigated the temperature dependence of structural relaxation and diffusion. We found that our model for ionic liquids belongs to fragile glass formers, where $\tau_{\alpha}$ exhibits strong non-Arrhenius dependence on the temperature. In addition, the SE relation is violated, which implies that diffusion is enhanced when compared with structural relaxation. We pay attention to the apparent universality of the abovementioned dynamic features observed in a variety of glassy liquid systems, regardless of the nature of their molecular interactions. [...]
[4] arXiv:2605.14969 | On the Symmetries of Anisotropic Spin Interaction Models
  We show that anisotropic spin interactions do not merely break spin-space group (SSG) symmetries, but instead twist them through cohomology invariants, yielding symmetry classes beyond subgroups of $ O(3)\times \operatorname{Isom}(\mathbb{R}^3) $. This requires redefining the spin-only group $ S_0 $ in terms of proper spin rotations. Based on this unitary $ S_0 $, we formulate a twisted SSG (tSSG)
  Full text (https://ar5iv.labs.arxiv.org/html/2605.14969), excerpts of its own sections:
  § Introduction.—: Spin-space groups (SSGs) provide a unifying symmetry framework for magnetic materials, enabling systematic descriptions of magnetic topological electronic states  Liu et al. 2022 ; Yang et al. 2024 ; Guo et al. 2021 ; Ghorashi et al. 2024 , topological magnon bands  Katsura et al. 2010 ; Chumak et al. 2015 ; Chisnell et al. 2015 ; Cheng et al. 2016 ; Li et al. 2017 ; Yao et al. 2018 ; Corticelli et al. 2022 ; Corticelli et al. 2023 ; Chen et al. 2025 , and the altermagnetism  Šmejkal et al. 2022a ; Cheong and Xu 2022 ; Bose et al. 2022 ; Feng et al. 2022 ; Karube et al. 2022 ; Bai et al. 2022 ; Šmejkal et al. 2022b ; Mazin 2022 . These systems are governed by isotropic Heisenberg exchange in which spin and spatial operations combine in a particularly transparent manner: each symmetry operation is realized as a global spin rotation in $O(3)$ accompanied by a lattice isometry, and the resulting SSGs form subgroups of $O(3)\times\operatorname{Isom}(\mathbb{R}^{3})$   Brinkman and Elliott 1966 ; Litvin and Opechowski 1974 ; Jiang et al. 2024 ; Chen et al. 2024 ; Xiao et al. [...]
  § A minimal model with twisted collinear SSG.—: The model is defined on a two-dimensional square lattice with spatial symmetry $p4mm$ . It contains nearest-neighbor $XY$ interactions along the $\vec{x}$ direction and $DM$ interactions along the $\vec{y}$ direction. Speficically, for an undirected bond $\langle ij\rangle\parallel\vec{x}$ , $H^{XY}_{\langle ij\rangle}=S_{i}^{x}S_{j}^{x}+S_{i}^{y}S_{j}^{y}$ , whereas for a directed bond $\langle k\!\to\!l\rangle\parallel\vec{y}$ , $H^{DM}_{\langle k\to l\rangle}=S_{k}^{x}S_{l}^{y}-S_{k}^{y}S_{l}^{x}$ . Both interactions have equal strength $\alpha$ , a fixed nonzero real constant. The coupling to the AFM background field is described by $H_{a}=\sum_{l}(-1)^{l}hS_{l}^{z}$ with $h$ its strength. The total Hamiltonian then reads $\displaystyle H\!\!=\!\!\sum_{\langle ij\rangle}\!\left(\alpha\,H_{\langle ij\rangle}^{XY}\!+\!S^{z}_{i}S^{z}_{j}\right)\!+\!\!\sum_{\langle k\to l\rangle}\!\!\left(\alpha\,H^{DM}_{\langle k\to l\rangle}\!+\!S^{z}_{k}S^{z}_{l}\right)+H_{a}.$ (1) We first analyze the unitary symmetries of the model. [...]
  § Basic Setup.—: Below, we redefine the spin-only group and formulate a basic conceptual framework for symmetries in spin systems. Detailed constructions of tSSGs are presented in the following section. A spin-only group is defined as a subgroup of $SO(3)$ and is denoted by $\mathcal{S}_{0}$ . [...]
  § Twisted Spin-Space Groups.—: We now construct tSSGs. The construction is abstract, and the representative example introduced above will be used to clarify the key ideas when appropriate. [...]
  § Discussion and Outlook.—: Since DM vectors act as a gauge field for spin currents  Katsura et al. 2005 , the site-dependent centralizer sector $\mathfrak{Z}_{g}(\vec{r})$ acquires a natural interpretation as a spin gauge . In this view, tSSGs arise from gauging the centralizer of $\mathcal{S}_{0}$ . Such gauge-dressed symmetries, known as projective crystalline symmetry  Zhang et al. 2023 ; Zhang et al. 2025a , can generate topological phases on Brillouin platycosms  Zhang et al. 2025b . Realizing such phases in solid state materials remains challenging. The topological quadrupolar excitations on the spin Brillouin Klein-bottle studied here provide a first model in magnetic systems. This motivates the search, both theoretically and experimentally, for topological magnetic excitations on general spin Brillouin platycosms.
[5] arXiv:2608.24136 | Steering Recurrent Reasoners at Inference Time with Readout Feedback
  Recurrent models, which repeatedly update latent states with shared computation blocks, have emerged as powerful architectures for solving complex reasoning tasks. Existing inference-time methods scale computation by running more steps or sampling more trajectories, but ignore information revealed within each trajectory. Here we show that recurrent models can be improved at inference time by using
  Full text (https://arxiv.org/html/2608.24136), excerpts of its own sections:
  § 5 Experiments: We evaluate RoFB on two benchmarks, Sudoku and Maze, with the three models described earlier. Sudoku is a number-placement puzzle, whose objective is to fill a $9\times 9$ grid with digits so that each column, row, and box ( $3\times 3$ subgrid) contains all of the digits from 1 to 9. Following the prior works  ( Wang et al., 2025 ; Kubo et al., 2026 ) , we used Sudoku Extreme dataset, and applied the same preprocessing and augmentation techniques. We tested with 20,000 puzzle boards randomly sampled from all test boards. Maze is a pathfinding problem where the goal is to find a shortest path from a starting point to a target point in a $30\times 30$ grid environment with obstacles. Following the prior works  ( Wang et al., 2025 ; Kubo et al., 2026 ) , we used Maze Hard dataset, and applied the same preprocessing techniques. We tested with all 1,000 puzzle boards.
  § Evaluation.: For AKOrN and ItrSA++, we evaluated the performance of a model based on the readout after $T_{\text{eval}}\in\{64,128,256\}$ recurrence steps. We also evaluated model performances using confidence-based voting ( Kubo et al., 2026 ) with $K_{\text{vote}}\in\{1,4,16,64\}$ , where trajectories are sampled with random initial values and the one minimizing the sum of entropy over all cells is selected as the final output. For TRM, we evaluated $N_{\text{block}}\in\{8,12,16\}$ outer iterations, using 16 as the standard horizon following Jolicoeur-Martineau (2025) . We did not apply voting for TRM, as TRM learns a fixed initial value of the latent dynamics, rather than sampling it from a distribution, and thus the voting procedure is not applicable. For Sudoku, we report board accuracy, where a prediction is correct only if all cells match the ground-truth board. For Maze, we report shortest-path accuracy, where a prediction is correct only if the predicted path is the shortest path (not necessarily the given ground-truth path).
  § 6 Limitations and Discussion: We do not yet have a validated diagnostic that predicts whether RoFB will improve accuracy on a new model or task. Confidence and class separation can both be high for incorrect predictions, as observed in TRM on Maze, so neither alone establishes when feedback will be beneficial. Our main evaluation covers two puzzle benchmarks ( Sudoku Extreme , Maze Hard ) and three small recurrent architectures, with an additional TRM experiment on ARC-AGI-1. We do not evaluate language models, to which direct transfer is non-trivial. If RoFB is applied directly to LLMs, the large vocabulary size may dilute the inter-token coupling on which RoFB relies. Whether RoFB or such a variant provides additional gains to LLMs is left to future work.
  § 7 Conclusions: We proposed RoFB to enhance the inference performance of recurrent reasoning models. RoFB utilizes the readout probabilities during inference to provide feedback to the latent states. Across three architectures on Sudoku and Maze, RoFB yielded clear gains in four of six model–task pairs and a small gain in one, reaching accuracies unattainable by longer rollouts or confidence-based voting at lower inference compute. Our analysis indicates two roles of the feedback, repulsion that helps trajectories leave unsolved states and readout-dependent weighting that retains solutions once reached. Our results provide evidence that readout-based closed-loop steering can complement existing inference-time strategies such as longer rollouts and multi-trajectory voting. [...]
[6] arXiv:2302.10624 | Self-improving object detection via disagreement reconciliation
  Object detectors often experience a drop in performance when new environmental conditions are insufficiently represented in the training data. This paper studies how to automatically fine-tune a pre-existing object detector while exploring and acquiring images in a new environment without relying on human intervention, i.e., in a self-supervised fashion. In our setting, an agent initially explores
  Full text (https://arxiv.org/html/2302.10624), excerpts of its own sections:
  § 1 Introduction: The deployment of object detectors, particularly in real-world scenarios such as indoor robots, often requires fine-tuning with a custom dataset to accommodate for the domain shift between the training and test environments. While fine-tuning leads to improved performance, constructing a dataset can be a daunting task, requiring extensive time and effort in collecting and annotating thousands of images. [...]
  § 3 Experiments: We devise a set of experiments to test policies and fine-tuning techniques separately. For each policy described in Section 3.1 , we let an agent move in the environment and collect 7,500 frames from the Gibson dataset [ 12 ] . We opt for MaskRCNN [ 9 ] as the object detector as in previous approaches, although our proposed approach is model-agnostic. Training details We adopted the MaskRCNN model [ 9 ] provided by Detectron2 [ 16 ] and pre-trained on the COCO dataset [ 17 ] . MaskRCNN provides bounding-boxes and masks for each prediction. We set the score threshold for object-detection predictions at $0.7$ . Similarly to previous works [ 14 , 1 ] , we focus on a subset of objects which are common in houses and living spaces: toilet , couch , bed , dining table , potting plant , and tv . For the self-training stage, we adopt SGD optimizer with learning rate $\text{lr}=1e-4$ , $\text{epochs}=10$ , $\text{weight-decay}=1e-5$ , $\text{momentum}=0.9$ and $\text{batch size}=16$ . [...]
  § 3.3 Results: We evaluate our method against two perception methods for all the exploration policies. Table 1 reports our results. As a reference, we assess that the off-the-shelf MaskRCNN [ 9 ] reaches mAP@50 $40.33$ on our test set. Our perception method outperforms self-training [ 22 ] and SEAL’s perception [ 8 ] in combination with random, frontier, Semantic Curiosity, and NeuralSLAM baselines. Even when using the random goals baseline, therefore without relying on any predetermined behavior, our perception module improves over self-training by $2.21\%$ . When compared with exploration policies, both learned [ 3 ] and classical [ 21 ] ones, our perception module outperforms SEAL perception. In particular, we notice that a classical frontier exploration baseline outperforms NeuralSLAM and SEAL in our self-learning task. Intuitively, if the variance of the observations is low, the semantic voxel map reflects the labels predicted by the off-the-shelf detector. NeuralSLAM exploration collects fewer observations for each object instance. [...]
  § 4 Conclusion: We proposed a novel self-training mechanism for object detection that relies on the exploration of the environment. The object detector can benefit from hard positive examples, e.g. where the off-the-shelf detector fails. Namely, the perception phase can exploit disagreements among pseudo-labels. We propose to clean the inconsistencies by using a semantic voxel map by accumulating each prediction into the 3D space. We solve disagreeing labels in a 3D voxel space via a novel mechanism, while preserving the conflicting information among predictions. By projecting the 3D volumes onto each training examples we generate a new training set. Next, we fine-tune the object detector by leveraging the resolved the pseduo-labels as well as consistent logits vector for each object. Finally, we force the feature vector of each object to be consistent across different views. Experiments show the benefits of our perception stages which outperform the baselines and reaches state-of-the-art performance, improving the off-the-shelf object detector by $2.76\%$ .
[7] arXiv:2001.09475 | Non-Hermitian topological Mott insulators in one-dimensional fermionic superlattices
  We study interaction-induced Mott insulators, and their topological properties in a 1D non-Hermitian strongly-correlated spinful fermionic superlattice system with either nonreciprocal hopping or complex-valued interaction. For the nonreciprocal hopping case, the low-energy neutral excitation spectrum is sensitive to boundary conditions, which is a manifestation of the non-Hermitian skin effect. H
  Full text (https://arxiv.org/html/2001.09475), excerpts of its own sections:
  § I Introduction: Recent years have witnessed considerable interest in exploring topological phases of non-Hermitian systems [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 49 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 ] , which can be realized in classical optical and mechanical systems with gain and loss [ 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 ] , correlated and disordered electronic systems with finite quasiparticle lifetimes [ 76 , 77 , 78 , 79 , 80 ] , and open quantum systems with post-selection measurements [ 81 ] . Non-Hermitian topological systems exhibit many unique properties with no counterpart in Hermitian cases, such as: non-Hermitian skin effect and breakdown of the conventional bulk-boundary correspondence [ 17 , 18 , 19 ] , bulk Fermi arcs [ 12 ] , and rich Bernard-LeClair symmetry classes beyond the ten-fold Altland-Zirnbauer ones [ 24 , 25 , 26 ] . [...]
  § II.1 Model: We consider a 1D model of spin-1/2 ultracold fermionic atoms loaded in a bichromatic optical lattice (see Appendix A for details), described by $\displaystyle\mathcal{H}=$ [...]
  § IV Summary and discussion: We have discussed topological properties of an interaction-induced topological Mott insulator in a 1D non-Hermitian spinful fermionic superlattice system. We analyzed its low-energy neutral and charge excitations spectra in the presence of nonreciprocal hopping, where in-gap modes appear. We found that the nonreciprocal hopping makes the neutral excitation spectrum sensitive to the boundary conditions, which is a manifestation of the non-Hermitian skin effect. However, the unique non-Hermitian skin effect on particle density, as shown at the single-particle case, is absent due to the Pauli exclusion principle. The interplay of nonreciprocal hopping, superlattice potential, and interactions leads to the absence of edge excitations, defined by only the right eigenvectors, of some in-gap modes appearing in both the neutral and charge excitation spectra. Moreover, these edge excitations can be characterized by using biorthogonal eigenvectors. [...]
  § Appendix A Experimental realization of Fermi-Hubbard model with nonreciprocal hopping: To experimentally realize the non-Hermitian Fermi-Hubbard model with asymmetric hopping in the ultracold atom systems, we can employ reservoir engineering [ 116 ] . We rewrite the system Hamiltonian Eq. ( 1 ) into Hermitian $\mathcal{H}_{1}=\left(\mathcal{H}+\mathcal{H}^{\dagger}\right)/2$ , and anti-Hermitian $\mathcal{H}_{2}=\left(\mathcal{H}-\mathcal{H}^{\dagger}\right)/2$ parts: $\displaystyle\mathcal{H}_{1}=$ $\displaystyle-\frac{t\left(e^{\alpha}+e^{-\alpha}\right)}{2}\sum_{j,\sigma}\left(c_{j+1,\sigma}^{\dagger}c_{j,\sigma}+c_{j,\sigma}^{\dagger}c_{j+1,\sigma}\right)$ $\displaystyle+\sum_{j,\sigma}V_{j}n_{j,\sigma}+U\sum_{j}c_{j,\uparrow}^{\dagger}c_{j,\downarrow}^{\dagger}c_{j,\downarrow}c_{j,\uparrow},$ (16) $\displaystyle\mathcal{H}_{2}=-\frac{t\left(e^{\alpha}-e^{-\alpha}\right)}{2}\sum_{j,\sigma}\left(c_{j+1,\sigma}^{\dagger}c_{j,\sigma}-c_{j,\sigma}^{\dagger}c_{j+1,\sigma}\right),$ (17) To engineer this anti-Hermitian part $\mathcal{H}_{2}$ , we follow the method developed in Ref.  [ 116 ] to dissipatively engineer the following jump operators that describe the [...]
[8] arXiv:2408.03303 | Understanding How Blind Users Handle Object Recognition Errors: Strategies and Challenges
  Object recognition technologies hold the potential to support blind and low-vision people in navigating the world around them. However, the gap between benchmark performances and practical usability remains a significant challenge. This paper presents a study aimed at understanding blind users' interaction with object recognition systems for identifying and avoiding errors. Leveraging a pre-existi
  Full text (https://arxiv.org/html/2408.03303), excerpts of its own sections:
  § 1. Introduction: The field of computer vision has made significant strides, achieving considerable benchmarking rates in object recognition tasks. Yet, despite these advancements, real-world applications often encounter substantial discrepancies between expected and observed performance  ( Massiceti et al., 2023 ; Cao et al., 2022 ) . Factors such as complex tasks, resource limitations ( e.g. , mobile device processing), and inputs that deviate from the training data ( e.g. , classifying images with personal items or cluttered backgrounds collected by a user) pose persistent challenges, leading to higher-than-anticipated error rates in practical scenarios  ( Alcorn et al., 2019 ) . Moreover, the vulnerability of object recognition systems to adversarial attacks further compounds these challenges  ( Goodfellow et al., 2014 ; Kurakin et al., 2016 ) . While image classifiers hold potential for supporting the blind community in day to day tasks, they are hindered by their inability to effectively convey recognition errors, especially when tactile or olfactory verification is impractical ( e.g. [...]
  § 2. Related Work: Object recognition, encompassing both object detection and classification  ( Russakovsky et al., 2015 ; Andreopoulos and Tsotsos, 2013 ) , has been the subject of active research for decades, representing fundamental and inherently challenging problems within computer vision. Object detection specifically seeks to ascertain the precise location and dimensions of objects within an image, often represented through bounding boxes  ( Zhao et al., 2019 ; Zou et al., 2023 ) . [...]
  § 5. Error Identification Results: We conducted a comprehensive evaluation of participants’ experience with identifying errors within the context of object recognition. Our analysis centered on discerning patterns in participants’ error-handling behavior throughout the task. Additionally, we examined the influence of repeated object recognition efforts on error handling by comparing the two attempts. Furthermore, participants’ feedback provided valuable insights into their attitudes toward errors encountered in object recognition.
  § 6. Discussion: Our user study, exploratory in nature, shows both promising results and future research directions for supporting blind users’ interactions with error-prone AI-infused technologies. In this section we discuss lessons learned and limitations that may affect the generalizability of our findings.
  § 7. Conclusion: We explored the experiences of blind and low-vision people regarding photo-taking, usage of camera-based assistive systems, and error identification within these systems. Through semi-structured interviews, we uncovered that participants predominantly utilize photo-taking for the purpose of utilizing camera-based assistive systems, rather than solely for capturing memories or sharing with others. Additionally, participants revealed their inclination towards independently reviewing photo quality and identifying errors, despite acknowledging the challenging nature of these tasks for approximately half of the participants. Furthermore, our empirical investigation through error identification tasks provided valuable insights into the challenges associated with identifying object recognition errors. The results indicated that participants successfully identified only around 50% of the errors, predominantly employing viewpoint, background, and object size alterations within images to mitigate errors. [...]
[9] arXiv:1810.12009 | Dynamical configuration interaction: Quantum embedding that combines wave functions and Green's functions
  We present the concept, derivation, and implementation of dynamical configuration interaction, a quantum embedding theory that combines Green's function methodology with the many-body wave function. In a strongly-correlated active space, we use full configuration interaction (CI) to describe static correlation exactly. We add energy dependent corrections to the CI Hamiltonian which, in principle, 
  Full text (https://arxiv.org/html/1810.12009), excerpts of its own sections:
  § I.1 Brief survey of current methods: We very briefly introduce many-body WF and GF methods that are relevant to the current work. Many modern approaches to strong correlation in physics study the many-body Green’s function. [...]
  § I.2 Motivation: Our goal is to construct a quantum embedding theory which combines the best features of quantum chemistry, GF embedding, and $GW$ /BSE theory. [...]
  § IV Results: Molecular dissociation is a difficult multi-reference problem and a benchmark test of strongly-correlated methods. In the dissociation limit, the wave function with the correct symmetry cannot be written as a single Slater determinant. Mean-field theories which optimize single-particle states around a single Slater determinant, therefore, cannot correctly describe such dissociation. Even many-body methods which are biased towards a single reference may fail in bond breaking problems. We first test our theory by dissociating H 2 with a $(2,6)$ active space, shown in Fig. 12 . While performing H 2 dissociation with a relatively large $(2,6)$ AS may seem “easy” for a wave function based method, it is still an important first test of the theory. Many approximate methods, including GF-based methods such as RPA or BSE, [ 80 ] contain spurious maxima in the dissociation curve. It is not clear, just by examining the equations, if our underlying GF calculation in $\mathcal{R}\;$ based on a single reference introduces similar errors to a DCI calculation. [...]
  § V Discussion: We now discuss particular aspects of DCI and the accuracy of the underlying approximations. We first consider the static approximation to $\mathcal{L}^{\mathcal{R}}$ and the neglect of $\mathrm{Im}\Sigma$ . Both approximations assume that we are dealing with long-lived excitations. Long quasiparticle lifetimes are not guaranteed but often the case for weakly-correlated systems. Long-lived excitations in $\mathcal{R}\;$ is an easier condition than for the physical excitations of $H$ . $\mathcal{R}\;$ is effectively a large band gap system, which we expect to be less correlated than the full Hilbert space. By attaching $\mathcal{R}\;$ projectors to the interaction, we remove diagrams containing lines near $E_{\mathrm{F}}$ and energetically near each other. This restriction limits the number of possible decay channels and restricts transfer of spectral weight away from the single-particle peaks. Accordingly, subspace quasiparticle lifetimes are longer than their corresponding physical states. [...]
  § VI Conclusion: We have introduced a new quantum embedding, or active space, theory that combines aspects of quantum chemistry, GF embedding, and $GW$ /BSE theory. The theory is parameter free, systematically improvable, and describes both ground and excited states. It is naturally suited for multi-reference ground states and multi-configurational excited states. Our initial calculations on dimers suggest that DCI could be competitive with high level quantum chemistry methods for excitation energies. Excited states of N 2 and C 2 , which are difficult multi-configurational states, are already well described at the present level of theory. For a conical intersection along the N 2 dissociation PES, our theory outperforms conventional CC. DCI offers several advantages compared to pure $GW$ /BSE. Multiple excitations in the AS are easily accessible, and excitations are free of self-screening errors. Correlation in the AS is included to all orders, and the method can be systematically improved by expanding the AS. [...]
[10] arXiv:2302.03566 | Look Around and Learn: Self-Training Object Detection by Exploration
  When an object detector is deployed in a novel setting it often experiences a drop in performance. This paper studies how an embodied agent can automatically fine-tune a pre-existing object detector while exploring and acquiring images in a new environment without relying on human intervention, i.e., a fully self-supervised approach. In our setting, an agent initially learns to explore the environ
  Full text (https://arxiv.org/html/2302.03566), excerpts of its own sections:
  § 1 Introduction: When newborns interact with novel objects, they are naturally inclined to actively explore their hidden facets by manipulating or moving around to have views from a new angle, thus unveiling blindsides. [...]
  § 4 Experiments: We devise a set of experiments to test policies and fine-tuning techniques separately. For each policy described in Section 4.1 , we let an agent move in the environment and collect 7,500 frames from the Gibson dataset [ 37 ] . We opt for MaskRCNN [ 16 ] as the object detector for comparison fairness with previous approaches [ 6 , 9 , 18 ] , although our proposed approach is model-agnostic. We report additional training detail in the Supplementary material.
  § Evaluation.: To evaluate our approach, we sample 4,000 testing samples as in [ 6 ] . We adopt the mean Average Precision (mAP) with IOU threshold on bounding-boxes at 0.5 as evaluation score [ 22 ] . We stress that no semantic annotations are required during training. We introduce the baseline exploration and perception policies in Section 4.1 . Section 4.2 compares Look Around with Disagreement Reconciliation with the baselines and supervised labels. For the latter, we use the annotations provided by Habitat and originally proposed in Armani et al . [ 4 ] . We ablate the main components of our approach in Section 4.3 , and we test Look Around with Disagreement Reconciliation on a real robotic platform in Section 4.4 .
  § 4.2 Results: We evaluate our method against different policies and perception methods, and Table 1 reports our results. As a reference, we assess that the off-the-shelf MaskRCNN [ 16 ] reaches mAP@50 $40.33$ on our test set. Our perception method outperforms self-training [ 41 ] and SEAL’s perception [ 6 ] in combination with random, frontier, Semantic Curiosity, and NeuralSLAM baselines. The improvement is evident when combining our self-training mechanism and our policy: in this scenario, our pipeline Look Around  + Disagreement Reconciliation  reaches the overall best result of mAP@50 $46.60$ , which is $6.2\%$ over off-the-shelf performance. Even when using the random goals baseline, our perception module exceeds self-training by $2.21\%$ . Compared to exploration policies, both learned [ 7 ] and classical [ 42 ] ones, our perception module outperforms SEAL perception. In particular, we notice that a classical frontier exploration baseline outperforms NeuralSLAM in our self-learning task. [...]
  § 5 Conclusion: Our study introduced Look Around , a novel exploration method, and Disagreement Reconciliation , a label-free fine-tuning approach for object detectors. Our method employs object detector uncertainty to derive a disagreement score, which, when maximized, effectively guides exploration and improves object detection in a real robotic test. Our experiments demonstrate that Look Around significantly outperforms both classic and learned exploration policies. By combining our uncertainty-based reward and disagreement map with the Disagreement Reconciliation module, we achieve a notable increase in mean Average Precision (mAP) of 46.60%, a 6.27% improvement over the baseline off-the-shelf object detector, and a 3.59% advancement over state-of-the-art methods. The experimental validation on a real robot is an important sanity check and further establishes the efficacy of our approach. We tested Disagreement Reconciliation with Look Around on a real robotic platform without further tuning. In this scenario, our approach improved the object detector by 9.97% without any human intervention. [...]
[11] arXiv:2305.12452 | Advancing Referring Expression Segmentation Beyond Single Image
  Referring Expression Segmentation (RES) is a widely explored multi-modal task, which endeavors to segment the pre-existing object within a single image with a given linguistic expression. However, in broader real-world scenarios, it is not always possible to determine if the described object exists in a specific image. Typically, we have a collection of images, some of which may contain the descri
  Full text (https://arxiv.org/html/2305.12452), excerpts of its own sections:
  § 1 Introduction: Figure 1: Real-world applications of Group-wise Referring Expression Segmentation (GRES), which facilitates annotation auto-gathering from cluttered Internet images (upper), multi-monitors joint inference (lower), etc . Segmenting target objects described by users in a collection of images is a fundamental but overlooked capability that facilitates various real-world applications (as illustrated in Fig. 1 ), such as filtering and labeling cluttered internet images, multi-monitors event discovery, and mobile album retrieval. In recent years, Referring Expression Segmentation (RES) has become a research hotspot with great potentials to solve this demand. Various promising approaches  [ 17 , 38 , 44 , 6 , 14 ] and datasets  [ 21 , 46 , 36 , 42 ] have contributed to significant advancements in this field. However, the setting of RES is overly idealistic. It aims to segment what has been known to exist in a single image described by a expression. [...]
  § 2.1 Referring Expression Segmentation (RES): RES aims to ground the target object in the given image referred by the language and generate a corresponding segmentation mask. Methods. A common approach to solve RES is to first extract both vision and language features, and then fuse the multi-modal features to predict the mask. Early methods  [ 17 , 25 , 28 ] simply concatenate visual features and language features extracted by convolutional neural networks (CNNs) and recurrent neural networks (RNNs), respectively. Due to the breakthrough of Transformer  [ 41 , 9 , 31 ] , a rich line of works begin to explore its remarkable fusion power for multi-modality. Some  [ 43 , 27 , 38 , 14 , 6 , 22 , 44 ] conduct cross-model alignment based on Transformer, others  [ 45 , 34 , 30 , 35 , 43 ] adopt various attention mechanisms to achieve better feature weighting and fusing. [...]
  § 3.1 Overview: The pipeline of our Grouped Referring Segmenter (GRSer) is demonstrated in Fig.  3 . Given an expression that specifies an object, a group of related images are processed simultaneously, and then all corresponding pixel-wise masks of the target object are output. In particular, for the negative sample ( i.e. , image without target object), its output mask is $0$ mask. There are four modules in our GRSer, including a multi-modal encoder, a triphasic query module, a heatmap hierarchizer, and a mask predictor. Text & Image Encoder. BERT  [ 4 ] is employed to embed the expression into linguistic features $\mathbf{L}\in\mathbb{R}^{C_{l}}$ , where $C_{l}$ is the number of channels for the language feature. Meanwhile, we construct an anti-expression by adding a prefix $ $ to the given expression, which is embedded as linguistic anti-features $\mathbf{L}^{anti}\in\mathbb{R}^{C_{l}}$ . [...]
  § 6 Conclusion: In this work, we present a realistic multi-modal setting named Group-wise Referring Expression Segmentation (GRES), which relaxes the limitation of idealized setting in RES and extends it to a collection of related images. To facilitate this new setting, we introduce a challenging dataset named GRD, which effectively simulates the real-world scenarios by collecting images in a grouped manner and annotating both positive and negative samples thoroughly. Besides, a novel baseline method GRSer is proposed to explicitly capture the language-vision and vision-vision feature interactions for better comprehension of the target object. Extensive experiments show that our method achieves SOTA performances on GRES, RES, and Co-SOD.
[12] QNFO: Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout | https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado
  Quantum hardware engineers routinely calibrate qubits by iterating between state preparation, control‑pulse design, and readout discrimination. This loop is inherently self‑referential because the calibration model is built from data that depend on the very model being calibrated. We formalize the loop as a composite operator $T=\Gamma\circ\Phi$ acting on operational data $\mathcal{D}$, where $\Ph
  Full text (https://papers.qnfo.org/papers/operational-circularity-of-qubit-ontology-excitations-defined-by-their-own-reado), excerpts of its own sections:
  § 1. Introduction: Quantum information processors rely on qubits—two‑level subsystems that are initialized, manipulated by control pulses, and measured. The prevailing engineering view treats the qubit as a pre‑existing physical degree of freedom whose parameters are accessed by calibration routines. In practice, calibration proceeds by a closed loop: a model of the qubit generates control waveforms; the resulting data are used to update the model; the updated model in turn defines the next set of control waveforms. Because the model and the data co‑define each other, the loop is **operationally circular**. [...]
  § 5. Results: All quantitative statements follow from the derivations in Section 4. *R1 (Convergence).* With $L=0.6$, $d_{0}=1$, and $\varepsilon=10^{-3}$, calibration reaches the target in $n=14$ iterations (Section 4.3). A variant with $d_{0}=5\times10^{-2}$ and $\varepsilon=p_{e}=9\times10^{-5}$ requires $n=13$ iterations. In this regime the loop is benign and yields a unique fixed point. *R2 (Multiplicity).* The toy model of Section 4.5 possesses two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by a basin boundary at $0.5$. Starting from $x_{0}=0.6$ the iteration converges to $x_{B}^{*}=1$ via the closed‑form $x_{n}=1-0.4\,0.5^{n}$. The final ontology depends on the initial guess, demonstrating ontological underdetermination despite local contractivity. *R3 (Readout error floor).* The assumed fidelity $F=0.99991$ yields $p_{e}=9\times10^{-5}$, i.e. one error per $1.11\times10^{4}$ shots; over $10^{6}$ trials the expected error count is $90$. *R4 (Shot budget).* Resolving a discrepancy $\delta=10^{-3}$ at $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots (Section 4.4). [...]
  § 9. Conclusion: **(a) Primary users and decision impact.** Calibration engineers and quantum‑hardware designers are the main beneficiaries. If the contraction condition holds (i.e., measured $L<1$), standard calibration routines guarantee a unique operational ontology, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. If multiplicity or equivariance is detected, designers must incorporate additional out‑of‑loop probes (e.g., leakage‑sensitive spectroscopy) to break the symmetry and certify the physical nature of the qubit. **(b) Technology readiness.** The analysis is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept). **(c) Smallest next experiment.** A minimal experiment would measure an ontology‑discriminating observable (e.g., a leakage‑sensitive transition) on a trapped‑ion qubit while varying the initial calibration guess. [...]
  § 10. Conclusion: The analysis demonstrates that the uniqueness of a qubit’s operational identification is a property of the calibration dynamics, not of the underlying physical system. When the composite calibration operator $T$ is a contraction, Banach’s theorem guarantees a unique fixed point and benign circularity. When $T$ is non‑contractive, either multiple discrete fixed points or continuous symmetry orbits can arise, leading to ontological underdetermination that cannot be resolved by calibration alone. Quantitative criteria—Lipschitz constant thresholds, iteration counts, and shot‑budget estimates—provide concrete guidance for hardware designers to assess the adequacy of standard calibration pipelines and to plan out‑of‑loop measurements when necessary. [...]
[13] QNFO: Knowing Patterns: An Epistemology for People Tired of Being Fixed | https://papers.qnfo.org/papers/knowing-patterns
  No steps. No habits to install. No “mindset shifts” to practice until they stick. No journaling prompts. Descriptions of how patterns work. In physics. In biology. In the daily motion of attention, mood, action, and thought. Descriptions of what a “thing” actually is (a temporary knot of relations) and what “knowing” actually is (pattern recognition by a pattern recognizer). There is no separate “
  Full text (https://papers.qnfo.org/papers/knowing-patterns), excerpts of its own sections:
  § Knowing: Patterns: An Epistemology for People Tired of Being Fixed **Version 0.3**
  § Before You Begin: This book contains zero advice. No steps. No habits to install. No “mindset shifts” to practice until they stick. No journaling prompts. What it contains: descriptions. Descriptions of how patterns work. In physics. In biology. In the daily motion of attention, mood, action, and thought. Descriptions of what a “thing” actually is (a temporary knot of relations) and what “knowing” actually is (pattern recognition by a pattern recognizer). There is no separate “application” step. Reading these descriptions *is* the shift. The shift is simply seeing more clearly what was already happening. If you find yourself waiting for a guru, a method, or a 5-point plan, you have missed the point. Put the book down. Or do not. The pattern does not care whether you finish. You do not need help. You need knowledge — not facts to store, but epistemology in motion: knowing how knowing works, and seeing that what you call “you” is already a verb, already a relation, already sufficient. The rest follows. Or it does not. That is not in the book’s hands. It is in the pattern’s. [...]
  § 1. The Noun Trap: Ask a child what a thing is, and they will point. “That’s a cup.” “That’s a dog.” “That’s me.” Ask a physicist what an electron is, and they will pause. They will tell you about its charge, its spin, its probability cloud, its interactions with the electromagnetic field. If you press — “Yes, but what *is* it, really?” — they will eventually say: “It is a node in a set of relations. It is what a field does when you perturb it.” The child and the physicist are both right. [...]
  § The Problem with Finding: Your Story The self-help industry has commercialized narrative identity. “Find your story.” “Own your narrative.” “Rewrite your past to change your future.” These commands assume a *true* story hiding somewhere, and that your job is to discover or construct it. This is the noun trap applied to identity. It turns “story” into a thing you possess, rather than a process you participate in. There is no true story. There are only more or less useful patterns of meaning-making — patterns that help you navigate experience or patterns that keep you stuck. And “stuck” is itself a kind of story: the story that the pattern cannot change. The freedom is not in finding the right story. The freedom is in knowing that you are *always* telling a story, and that the telling can shift — not because you decide to tell a better one, but because the conditions that sustain the current story have changed.
  § Finding the Leverage Point: Not all relations are equal. Some, when tilted, produce large reorganizations. Others produce nothing. Clues for where to look: **Temporal relations.** Timing of a response, duration of a pause, sequence of events. Time is a universal constraint — small changes in timing cascade through everything else. **Environmental relations.** Location, objects present, sensory texture. Concrete and available. You can move a chair more easily than you can change a belief. **Relational relations.** Who is present, what role they play, how they respond. Patterns are co-created. A small change in one person’s part of the dance shifts the whole dance. **Attentional relations.** What you are looking at, what you are scanning for. Attention shapes everything else. You do not need to know which leverage point is “right.” Try one. Observe what happens. If the pattern reorganizes, you found one. If not, try another. Experimental, not heroic.
[14] QNFO: The Calibration Loop as Fixed Point: Ontological Underdetermination of the Qubit by Its Own Metrology | https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-
  Engineered qubits are certified through a closed calibration chain in which drive pulses, readout discriminators, and tomographic validation mutually calibrate one another. This self‑referential loop raises the question of whether the physical referent of the qubit label (collective circuit mode, electronic transition, or spin) is determined by the loop itself or remains underdetermined. We formal
  Full text (https://papers.qnfo.org/papers/the-calibration-loop-as-fixed-point-ontological-underdetermination-of-the-qubit-), excerpts of its own sections:
  § 1. Introduction: When an experimentalist drives a qubit, a physical excitation is created; when the same experimentalist reads out the qubit, a physical observable is measured. The engineering question is blunt: if the billiard‑ball picture is rejected, what exactly do the pulses manipulate, and what does the readout measure—excitations of what medium? The uncomfortable answer is that the answer is supplied by the calibration chain itself. The drive frequency is calibrated by finding a resonance; the Rabi rate is calibrated by fitting oscillations in a signal; the readout discriminator is calibrated by assigning outcomes to states prepared by the already‑calibrated drive; tomography validates the loop using measurements whose calibration rests on the loop. Each step certifies the others. The loop is closed, and the physical ontology of the qubit—collective mode, spin, circuit degree of freedom, or a two‑level abstraction layered over a multi‑level device—appears only as an internal bookkeeping choice within the loop. This question now carries economic weight. [...]
  § 2. Background and Related Work: The literature bearing on this question falls into several groups. **Self‑referential diagnosis.** Adaptive fault diagnosis [1] studies determining which processors in a remote location are reliable by asking “Yes or No’’ questions, where processors may always tell the truth, always lie, or sometimes do either. [...]
  § 5. Results: All quantitative statements below follow from the derivations in Section 4 or are labeled projections with explicit assumptions. - **R1 (readout error scale).** Per‑shot error $\varepsilon_{\mathrm{ro}}=9\times10^{-5}$; expected misidentifications in $10^{6}$ trials $\mu=90$; one‑sigma uncertainty on fidelity $\sigma_f\approx9.49\times10^{-6}$. - **R2 (adaptive improvement).** $\varepsilon_{\mathrm{ad}}=1\times10^{-5}$, a factor $\approx0.11111$ of the time‑resolved error. - **R3 (calibration convergence).** Calibration error falls below the readout noise floor after $k_{\min}=11$ iterations, with $e_{11}=4.8828125\times10^{-5}$. - **R4 (ontological degeneracy).** $D_{\mathrm{TV}}=0$ for subspace‑restricted measurements; $D_{\mathrm{TV}}=0.01$ for a leakage‑resolving measurement with $|c|=0.1$. - **R5 (shot budget).** $N\ge2500$ shots for one‑sigma resolution of $\Delta p=0.01$; $N\ge22500$ shots for three‑sigma; noise‑floor margin $\approx111$. [...]
  § 8. Conclusion: We have formalized the calibration hierarchy of engineered qubits as an iterated map, derived its contraction condition, and quantified the iteration count required to reach the readout noise floor. By constructing two ontologically distinct models—a two‑level abstraction and a three‑level anharmonic ladder—we proved that, under any measurement chain confined to the computational subspace, the models yield identical outcome statistics. Quantitative anchoring on a typical trapped‑ion readout fidelity yields a per‑shot error of $9\times10^{-5}$, a minimum of $11$ calibration iterations, and a shot budget of $N\ge2500$ to resolve the ontologies once a leakage‑resolving observable is introduced. The circularity of the calibration loop is broken only by extending the measurement chain beyond the subspace or by enforcing cross‑platform consistency. The analysis clarifies the epistemic limits of current certification pipelines and points to concrete experimental extensions that would decisively test the underdetermination claim.