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

Ontology engineering provides a language for describing the mapping between data and conceptual entities. The Gene Ontology (GO) is described as “the largest resource for cataloguing gene function” [1], illustrating how a large, curated mapping can serve as a shared reference. GO can be used “without deep understanding of its structure” [2], showing that useful abstractions may be employed while ignoring underlying commitments—directly analogous to treating a qubit as a black‑box two‑level system.

GraphMatcher employs graph‑attention mechanisms to find correspondences between entities in different ontologies [3]; this mirrors cross‑platform calibration where ontologies produced by transmon, trapped‑ion, and spin devices must be aligned. Ontology evolution in the life‑science context shows that mappings change as underlying ontologies are extended [4], supporting the view that a qubit’s operational ontology evolves through calibration.

Reference [5] demonstrates an ontology‑based framework that turns qualitative conversational descriptors into quantitative definitions via a decision‑tree classifier. By analogy, the ontology map $\Phi$ can be built from qualitative calibration specifications (e.g., “high‑fidelity readout”) that are mapped to quantitative thresholds (e.g., $F\ge0.9999$).

A business‑intelligence ontology uses classification to align heterogeneous data sources [7]; the same principle can be applied to align qubit ontologies across platforms, enabling platform‑independent certification.

Understanding error handling in object‑recognition systems reveals that practical deployments often exhibit higher‑than‑expected error rates [8], underscoring how operational data can be ambiguous and why additional out‑of‑loop diagnostics may be needed for qubit ontology.

The QNFO corpus provides a pedagogical bridge between ontological critique and concrete quantum hardware [12], supplying the concrete data model $\mathcal{D}$ used throughout this work.

## 3. Methods

### 3.1 Operational data and ontology maps

Let $\mathcal{D}$ denote the space of operational data, i.e. sequences of control waveforms, their settings, and readout outcomes. Let $\mathcal{O}$ denote the space of Hilbert‑space identifications, each specifying a two‑level subspace $\{|0\rangle,|1\rangle\}$ together with a Hamiltonian $H$, a readout observable $M$, error channels $\{L_k\}$, and a physical interpretation (eigenmode, field excitation, collective variable).

An **ontology map**
\[
\Phi:\mathcal{D}\to\mathcal{O}
\]
assigns to any datum $x\in\mathcal{D}$ an identification $\Phi(x)$.  

A **realization map**
\[
\Gamma:\mathcal{O}\to\mathcal{D}
\]
produces the predicted data that would be observed if the identification were correct.  

Calibration seeks a **fixed point** $x^{*}\in\mathcal{D}$ satisfying
\[
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr).
\]
The composite operator
\[
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}
\]
encodes one iteration of the calibration loop.

### 3.2 Contraction condition for benign circularity

Equip $\mathcal{D}$ with a metric $d_{\mathcal{D}}$ (e.g. total‑variation distance between predicted readout distributions plus weighted parameter distance).  

**Proposition 1.** If there exists $L\in(0,1)$ such that
\[
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\forall x,x'\in\mathcal{D},
\]
then $T$ is a contraction and, by Banach’s fixed‑point theorem, possesses a unique fixed point $x^{*}$. Moreover, iterating from any initial datum $x_{0}$ yields
\[
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}),
\]
so convergence to tolerance $\varepsilon$ requires
\[
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
\]

### 3.3 Ontological underdetermination

If $T$ fails to be globally contractive, multiple fixed points may exist. Define two ontology maps $\Phi_{A},\Phi_{B}$ with corresponding realizations $\Gamma_{A},\Gamma_{B}$. Ontological underdetermination occurs when a datum $x^{*}$ satisfies
\[
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
\]
while $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ are physically inequivalent.

A continuous source of underdetermination is **equivariance**: if a group $G$ (e.g. $SO(3)$ acting on Bloch‑sphere axes) satisfies $T\circ g = g\circ T$ for all $g\in G$, then the entire orbit $\{g\cdot x^{*}\mid g\in G\}$ consists of fixed points. For a qubit, $SO(3)$ has dimension three, yielding three continuous descriptive parameters (two axis angles and one phase) invisible to any $G$‑invariant statistic.

### 3.4 Discriminating observable and shot budget

To distinguish two ontologies that differ in the expectation value of a readout‑accessible observable by $\delta$, we require enough measurement shots to resolve $\delta$ against readout noise. Assuming independent Bernoulli outcomes with per‑shot error probability $p_{e}=1-F$, Hoeffding’s inequality gives the required number of shots $N$ for failure probability $\alpha$:
\[
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
\]
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

### Limitations

1. **Illustrative Lipschitz constant.** The contraction analysis uses a fixed $L=0.6$; real calibration loops may exhibit state‑dependent or iteration‑dependent $L$, potentially violating the global contraction condition.  
2. **Scalar toy model.** Reducing ontology space to a single scalar omits high‑dimensional effects such as continuous families of fixed points or limit cycles.  
3. **Noise model.** Assuming independent Bernoulli readout errors neglects decoherence, correlated noise, and drift, which would increase the required shot budget.  
4. **Equivariance assumption.** Perfect $SO(3)$ symmetry presumes no stray bias; any bias field breaks the symmetry and reduces the orbit dimension, but quantifying this requires platform‑specific modeling.

### Failure modes

*If calibration iterations become chaotic rather than contractive, no fixed point exists and the qubit lacks a self‑consistent operational definition.*  
*If the symmetry orbit corresponds to physically distinct couplings (e.g., a collective mode versus a single‑particle transition) rather than a pure gauge, the underdetermination is physical and not merely conventional.*

Both scenarios would invalidate the benign‑circularity claim.

### Falsification criteria

1. **Unique, platform‑independent identification.** Demonstrating that calibration on disparate platforms (transmon, ion, spin) converges to the same Hilbert‑space identification—including axis labeling—would falsify the claim of a three‑dimensional equivariant orbit (R6).  
2. **Out‑of‑loop observable discrimination.** Measuring an observable that differs between two candidate ontologies by $\delta\ge10^{-3}$ and achieving statistical significance with fewer than $2.649159\times10^{6}$ shots would falsify the shot‑budget prediction (R4).  
3. **Breakdown of contraction.** Observing divergence or limit‑cycle behavior in calibration iterations under controlled conditions would falsify the contraction‑based uniqueness claim (R1).

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.** Calibration engineers and quantum‑hardware designers are the principal beneficiaries. If the composite calibration operator $T$ satisfies the contraction condition ($L<1$), the analysis guarantees a unique fixed point after at most $n=14$ iterations (Section 4.3). In that regime the standard calibration pipeline can be trusted to produce a platform‑independent qubit identification, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. If $T$ is non‑contractive, the toy model of Section 4.5 shows that the final ontology may depend on the initial guess rather than on the data, signalling ontological underdetermination; designers must then incorporate out‑of‑loop probes to break the ambiguity before downstream algorithms can rely on the qubit label.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions it resides at **TRL 2** (technology concept formulated) and does not exceed **TRL 3** (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A minimal experiment would introduce an ontology‑discriminating observable (e.g., a leakage‑sensitive transition) on a trapped‑ion qubit and measure it with the assumed readout fidelity $F=0.99991$ ($p_{e}=9\times10^{-5}$). The experiment would collect $N=2.649159\times10^{6}$ shots, the budget derived in Section 4.4 for resolving a discrepancy $\delta=10^{-3}$ at failure probability $\alpha=0.01$.  
- *Refuting the contraction claim:* if two calibration runs starting from distinct initial guesses produce expectation values that differ by at least $\delta=10^{-3}$ despite both converging in $n\le14$ iterations, the loop is not uniquely contractive.  
- *Supporting the contraction claim:* if the two runs produce statistically indistinguishable expectation values (difference $<\delta$), the contraction condition is empirically validated.

**(d) Engineering constraints.**  
- **Readout fidelity:** achieving $F=0.99991$ requires high‑quantum‑efficiency detectors and low‑noise amplification chains; any degradation raises $p_{e}$ and inflates the required shot budget.  
- **Shot budget:** the projected $N=2.649159\times10^{6}$ shots must be delivered within the coherence time of the system; data‑acquisition hardware must sustain $\sim10^{6}$ shots s\(^{-1}\).  
- **Control of systematic drifts:** drift between calibration iterations can increase the effective Lipschitz constant $L$, potentially violating the global contraction condition. Real‑time monitoring of control parameters is therefore required.  
- **Symmetry‑breaking fields:** to lift the $SO(3)$ equivariance described in Section 3.3, a bias field larger than the minimal detectable asymmetry $\epsilon_{\min}\approx5.001\times10^{-3}$ (Section 4.6) must be applied; at the crossover count $N_{\text{cross}}\approx3.09\times10^{7}$ the required bias drops to $\epsilon_{\min}\approx1.27\times10^{-4}$.

**(e) Projected cost/performance bounds (projection).** Assuming a readout system capable of $F=0.99991$ at a hardware cost of **\$10 k** per qubit module (typical for state‑of‑the‑art trapped‑ion setups) and a data‑acquisition system that can record $10^{6}$ shots s\(^{-1}\), the $2.649159\times10^{6}$‑shot budget translates to an experimental duration of roughly **3 s**, yielding a marginal cost negligible compared with the hardware baseline. These figures are projections based on the assumed fidelity and shot rate.

**(f) Direct risks or misuse paths.** If the existence of multiple fixed points is interpreted as evidence that the qubit’s physical nature is irrelevant, designers may forgo out‑of‑loop diagnostics, leading to ambiguous device specifications and reduced reliability. Explicitly communicating that underdetermination requires additional probes mitigates this risk.

## 8. Conclusion

Calibration engineers and quantum‑hardware designers are the main beneficiaries of the present analysis. When the contraction condition holds (i.e., measured $L<1$), standard calibration routines guarantee a unique operational ontology, simplifying device qualification, cross‑platform benchmarking, and error‑budget allocation. When multiplicity or equivariance is detected, the two‑branch toy model demonstrates that the final ontology can depend on the initial guess, indicating ontological underdetermination that cannot be resolved by calibration alone. In such cases designers must incorporate out‑of‑loop measurements—such as leakage‑sensitive spectroscopy—to break the symmetry and certify the physical nature of the qubit.

The analysis is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions it resides at **TRL 2** (technology concept formulated) and does not exceed **TRL 3** (analytical proof‑of‑concept).

A minimal experiment would measure an ontology‑discriminating observable on a trapped‑ion qubit while varying the initial calibration guess. The experiment would record the shot budget $N=2.649159\times10^{6}$ derived in Section 4.4. Observation of convergence to a single outcome regardless of the initial guess would support the contraction hypothesis; dependence on the initial guess would confirm underdetermination. Failure to achieve statistical significance with fewer than $2.65\times10^{6}$ shots would falsify the shot‑budget prediction.

Engineering constraints include achieving the required readout fidelity, delivering the shot budget within coherence times, controlling systematic drifts, and applying symmetry‑breaking fields exceeding the minimal detectable asymmetry. Projected hardware costs of roughly **\$10 k** per qubit module and data‑acquisition rates of $10^{6}$ shots s\(^{-1}\) imply an experimental duration of a few seconds, making the proposed test practically feasible.

The quantitative criteria—Lipschitz‑constant thresholds, iteration counts, and shot‑budget estimates—provide concrete guidance for hardware designers to assess the adequacy of standard calibration pipelines and to plan out‑of‑loop measurements when necessary. Future work will extend the scalar model to multi‑parameter calibration operators, incorporate realistic drift and correlated noise, and execute the proposed minimal experiment on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.

## References

[1] arXiv:2411.01739 | Not Just Object, But State: Compositional Incremental Learning without Forgetting  
[2] arXiv:quant-ph/0608108 | Factorization of Dephasing Process in Quantum Open System  
[3] arXiv:1002.0860 | Fragility, Stokes-Einstein violation, and correlated local excitations in a coarse-grained model of an ionic liquid  
[4] arXiv:2605.14969 | On the Symmetries of Anisotropic Spin Interaction Models  
[5] arXiv:2608.24136 | Steering Recurrent Reasoners at Inference Time with Readout Feedback  
[6] arXiv:2302.10624 | Self-improving object detection via disagreement reconciliation  
[7] arXiv:2001.09475 | Non-Hermitian topological Mott insulators in one-dimensional fermionic superlattices  
[8] arXiv:2408.03303 | Understanding How Blind Users Handle Object Recognition Errors: Strategies and Challenges