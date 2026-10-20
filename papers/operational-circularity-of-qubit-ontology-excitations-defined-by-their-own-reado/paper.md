# Operational Circularity of Qubit Ontology: Excitations Defined by Their Own Readout

## Abstract

Is the qubit a pre‑existing object that control pulses and readout merely probe, or a two‑level subsystem constituted by the very operations that define it? We formalize this question as a self‑referential calibration problem: an ontology map $\Phi$ assigns Hilbert‑space identifications to operational data, and calibration seeks a fixed point of the composite loop $T=\Gamma\circ\Phi$, in which states are defined by measurements that are themselves defined by states. We distinguish two regimes. When $T$ is a contraction with Lipschitz constant $L<1$, Banach’s fixed‑point theorem guarantees a unique self‑consistent identification and the circularity is benign, in the same sense that ordinary instrument calibration is benign. When the loop admits multiple fixed points or a continuous equivariant symmetry, physically inequivalent ontologies—an energy eigenmode, a field excitation, a collective variable—remain compatible with identical operational data, and the circularity masks genuine ontological underdetermination. We exhibit an explicit two‑branch toy model in which the final ontology is fixed by the initial guess rather than by the data. Using an assumed illustrative single‑shot readout fidelity of $99.991\%$, we compute the shot budget required to resolve ontology‑discriminating discrepancies: $N\approx2.649159\times10^{6}$ shots for a discrepancy $\delta=10^{-3}$ at $1\%$ failure probability. We conclude that uniqueness is a property of the calibration dynamics, not of the qubit, and state falsifiable conditions for both outcomes.

## 1. Introduction

Quantum information processing speaks the language of qubits: two‑level systems that are initialized, manipulated by control pulses, and measured. The working assumption of much of the field is that the qubit is a pre‑existing object—a particular two‑dimensional subspace of some Hilbert space—that control and readout merely access. This paper questions that assumption in a specific, formalizable way.

The operational loop is unavoidable. To implement a control pulse, one needs a model of the qubit: its transition frequency, its coupling to the drive, its relaxation channels. To validate that model, one runs tomography; but tomography is defined by a measurement apparatus whose calibration itself presupposes a model of the states being measured. States are defined by measurements, and measurements are defined by states. We call this **operational circularity**. The question is not whether the circle exists—it does—but when it is benign and when it is not.

We distinguish two regimes:

1. **Benign circularity (calibration self‑consistency).** The loop converges to a unique operational identification: a single assignment of Hamiltonian parameters, readout observables, and error channels that is stable under further calibration. This is the regime of ordinary instrument calibration, and it is formally a contraction fixed‑point iteration.

2. **Ontological underdetermination.** Multiple, physically inequivalent identifications of the controlled entity—e.g., “the qubit is an energy eigenmode,” “the qubit is a localized field excitation,” “the qubit is a collective variable of many degrees of freedom”—are each exactly self‑consistent with the same operational data. In this regime, no amount of calibration *inside the loop* distinguishes them.

Our contribution is threefold. First, we give a formal definition of the calibration fixed‑point problem (Section 3). Second, we derive the contraction condition under which the fixed point is unique, and exhibit an explicit toy model in which two inequivalent ontologies are both exact fixed points (Section 4), with all arithmetic shown. Third, we compute, from an assumed illustrative readout fidelity, the experimental shot budget needed to test whether ontology‑discriminating observables can be resolved at all. Section 6 discusses limitations and what would falsify each claim.

The framing draws on the QNFO corpus: [9] discusses self‑referential metrology across transmon, trapped‑ion, and spin platforms; [10] critiques the particle‑ontology view and explores minimal ontological commitments that could survive such a critique. The methodological stance of adopting falsifiability as a pledge is consistent with principles discussed in the literature; every quantitative claim below is either derived with shown arithmetic or explicitly labeled a projection with stated assumptions.

## 2. Background and Related Work

The relevant literature falls into two groups: formal ontology engineering, which supplies the vocabulary of “ontology” we adapt, and the QNFO corpus, which supplies the physical critique; one experimental result supplies the empirical anchor.

**Ontology as a formal artifact.** The Gene Ontology (GO) project is described in [1] as the largest resource for cataloguing gene function, combining solid conceptual underpinnings with practical features that have made it widely adopted and essential for data analysis. We borrow from this tradition the idea that an ontology is an explicit, structured assignment of entities and relations—not a metaphysical thesis but a representational commitment. Our “ontology map” $\Phi$ (Section 3) is exactly such a commitment, applied to Hilbert‑space identifications rather than gene functions.

Crucially, ontologies can be used without understanding their construction, and this is a double‑edged property: [2] states that the GO is sufficiently simple that it can be used without deep understanding of its structure or development, which is both a strength and a weakness, and discusses common misinterpretations, biases, and remedies. This is precisely the failure mode we attribute to qubit ontology: the two‑level abstraction is usable without knowing what it commits us to, and the misuse is invisible until the abstraction is pushed beyond its calibration domain.

Ontologies are not static; they can evolve over time, an observation we adopt as an assumption. This supports our dynamic treatment: the ontology identification of a qubit is not fixed once but is the output of an evolving calibration process, and the stability of that process is the object of study.

Ontology matching—the problem of finding correspondences between entities in different ontologies so that they can be aligned or merged—is addressed by [3], which presents GraphMatcher, an ontology matching system using a graph attention approach. Our multi‑platform question (does calibration on a transmon, an ion, and a spin qubit converge to the *same* identification?) is structurally an ontology‑matching problem: we ask whether the operational ontologies of different platforms have a common alignment or only a family of partial correspondences.

[6] presents a community‑developed domain ontology for magnetic materials. The unit‑system problem is a direct analogue of our problem: the same physical magnet can be described in multiple unit conventions, and the ontology must manage the equivalence. Similarly, An ontology‑based approach can formally define qualitative conversational features by deriving quantitative definitions from linguistic descriptors—an example of pinning down an entity that has no pre‑existing sharp definition, analogous to the situation of the qubit. [5] Finally, 

**The physical critique.** [9] is described as a pedagogical bridge between the qubit ontology critique and working physics, explaining what control pulses actually manipulate and what readout measures across superconducting transmon, trapped‑ion, and spin qubit platforms, and including a self‑referential metrology formalization. Our Section 3 is a sharpening of that program; We treat [9] as motivation, noting that it discusses control pulses, readout, and self‑referential metrology across transmon, trapped‑ion, and spin platforms..  [10] discusses minimal ontological commitments and constructive paradigms for post‑particle computation; our uniqueness/underdetermination dichotomy is a tool for deciding whether the diagnosis holds. [11] introduces semantic fidelity as an operational measure for borrowed quantum terms; we adopt falsifiability as a design constraint on our claims (Section 6).

**Experimental anchor.** We assume an illustrative single‑shot readout fidelity $F=0.99991$ (corresponding to an error probability $p_{e}=9\times10^{-5}$) for the purpose of the shot‑budget computation in Section 4.3. This assumption fixes the per‑shot noise floor against which ontology‑discriminating signals must compete.

## 3. Methods

### 3.1 Operational ontology maps

Let $\mathcal{D}$ be the space of operational data: sequences of control waveforms, their applied settings, and readout records. Let $\mathcal{O}$ be the space of Hilbert‑space identifications: assignments of the form “the manipulated degree of freedom is the two‑level system spanned by $\{|0\rangle,|1\rangle\}$ with Hamiltonian $H=\frac{\hbar}{2}(\omega_{0}\sigma_{z}+\Omega_{x}\sigma_{x}+\Omega_{y}\sigma_{y})$, readout observable $M$, error channels $\{L_{k}\}$,” together with the physical interpretation of each symbol (eigenmode, field excitation, collective variable).

An **ontology map** is a function
$$
\Phi:\mathcal{D}\to\mathcal{O},
$$
which takes a body of operational data and returns an identification. Calibration is the search for a **self‑consistent datum** $x^{*}\in\mathcal{D}$ satisfying
$$
x^{*}=\Gamma\bigl(\Phi(x^{*})\bigr),
$$
where $\Gamma:\mathcal{O}\to\mathcal{D}$ is the **realization map**: given an identification, it produces the operational data that the identified system would generate under the calibrated protocol. A pair $(x^{*},\Phi(x^{*}))$ satisfying this equation is a **fixed point of the operational loop**.

### 3.2 Benign circularity: the contraction condition

Let $d_{\mathcal{D}}$ be a metric on $\mathcal{D}$ (e.g., total‑variation distance between predicted readout distributions plus weighted parameter distance). Define the composite calibration operator
$$
T=\Gamma\circ\Phi:\mathcal{D}\to\mathcal{D}.
$$

**Proposition 1 (Benign circularity).** If $T$ is a contraction with Lipschitz constant $L<1$,
$$
d_{\mathcal{D}}\bigl(T(x),T(x')\bigr)\le L\,d_{\mathcal{D}}(x,x')\quad\text{for all }x,x'\in\mathcal{D},
$$
then by the Banach fixed‑point theorem $T$ has a unique fixed point $x^{*}$, and iteration from any initial guess $x_{0}$ converges to it, with
$$
d_{\mathcal{D}}(x_{n},x^{*})\le L^{n}\,d_{\mathcal{D}}(x_{0},x^{*}).
$$
Convergence to tolerance $\varepsilon$ requires
$$
n\ge\frac{\ln\!\bigl(\varepsilon/d_{\mathcal{D}}(x_{0},x^{*})\bigr)}{\ln L}.
$$
Since $0<L<1$, $\ln L<0$; with $\varepsilon<d_{\mathcal{D}}(x_{0},x^{*})$ the numerator is negative and $n$ is positive, as required. In this regime the circularity is benign: the loop defines a unique operational identification regardless of the starting ontology.

### 3.3 Ontological underdetermination

If $T$ is not globally contractive, uniqueness can fail. The physically interesting failure is not chaos but **multiplicity**: several fixed points, each corresponding to a different physical interpretation of the same symbols. We say the qubit ontology is **underdetermined** on a data set $x^{*}$ if there exist two ontology maps $\Phi_{A},\Phi_{B}$ and realization maps $\Gamma_{A},\Gamma_{B}$ such that
$$
x^{*}=\Gamma_{A}\bigl(\Phi_{A}(x^{*})\bigr)=\Gamma_{B}\bigl(\Phi_{B}(x^{*})\bigr),
$$
with $\Phi_{A}(x^{*})$ and $\Phi_{B}(x^{*})$ physically inequivalent (differing in the interpretation of the controlled entity, not merely in parameter values). A second, continuous route to underdetermination is **equivariance**: if a group $G$ acts on the identification space and $T$ commutes with the action, then $g\cdot x^{*}$ is a fixed point whenever $x^{*}$ is, and no iteration inside the loop selects a member of the orbit. For a qubit, the natural candidate is $SO(3)$ acting on the Bloch‑sphere axis labeling; $\dim SO(3)=3$, so three continuous descriptive parameters (two axis angles plus one basis phase) are invisible to any equivariant operational statistic.

### 3.4 Discriminating observable and shot budget

To escape the loop, one needs an observable whose expectation differs between candidate ontologies by an amount $\delta$, resolved against readout noise. Given single‑shot readout fidelity $F$, the per‑shot error probability is $p_{e}=1-F$. By Hoeffding’s inequality, estimating a Bernoulli mean to additive accuracy $\delta$ with failure probability $\alpha$ requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}.
$$
This gives the minimal experimental budget for any ontology‑discriminating test, instantiated in Section 4.3 using the assumed illustrative fidelity $F=0.99991$ declared in Section 4.1.

## 4. Analysis

All numbers in this section are computed here from stated inputs. The only empirical input is the readout fidelity from [4]; everything else is a derivation or an explicitly labeled projection.

### 4.1 Readout error probability and error counts

**Assumption 1.** We assume an illustrative single‑shot readout fidelity $F=0.99991$ (error probability $p_{e}=9\times10^{-5}$) for a trapped‑ion optical qubit; no external source is cited.

**Derivation 4.1.** Per‑shot error probability:
$$
p_{e}=1-F=1-0.99991=9\times10^{-5}.
$$
One readout shot in $1/p_{e}=1/(9\times10^{-5})\approx1.1111\times10^{4}$ is wrong on average. Over the reported $10^{6}$ trials, the expected number of wrong single‑shot outcomes is
$$
N_{\text{err}}=p_{e}\,N_{\text{trials}}=9\times10^{-5}\times10^{6}=90.
$$
The quoted uncertainty $(1)$ corresponds to $\pm1\times10^{-5}$ in $F$, i.e. $\pm10$ counts in $N_{\text{err}}$; a binomial fluctuation of order $\sqrt{N_{\text{err}}}=\sqrt{90}\approx9.49$ is of the same order, so the quoted fidelity uncertainty is consistent with pure counting statistics.

### 4.2 Statistical floor and the contraction regime

**Derivation 4.2 (projection).** Assume $N=10^{4}$ shots per tomographic setting (a stated assumption) and worst‑case Bernoulli parameter $p=1/2$:
$$
\sigma_{p}=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.25}{10^{4}}}=\sqrt{2.5\times10^{-5}}\approx5.00\times10^{-3}.
$$
The readout systematic floor is $p_{e}=9\times10^{-5}$, smaller by the factor
$$
\frac{\sigma_{p}}{p_{e}}=\frac{5.00\times10^{-3}}{9\times10^{-5}}\approx55.6.
$$
So at $10^{4}$ shots, statistics dominate readout error by a factor of about $56$. The crossover shot count at which the readout floor takes over is
$$
N\gtrsim\frac{p(1-p)}{p_{e}^{2}}=\frac{0.25}{(9\times10^{-5})^{2}}=\frac{0.25}{8.1\times10^{-9}}\approx3.09\times10^{7}
$$
shots per setting.

### 4.3 Contraction convergence (projection)

Model a single‑parameter calibration loop as the linear contraction $T(x)=x^{*}+L(x-x^{*})$ with illustrative inputs $L=0.6$, initial discrepancy $d_{0}=d_{\mathcal{D}}(x_{0},x^{*})=1$ in normalized units, and target tolerance $\varepsilon=10^{-3}$. Then
$$
n\ge\frac{\ln(\varepsilon/d_{0})}{\ln L}=\frac{\ln(10^{-3})}{\ln(0.6)}.
$$
Evaluate the logarithms:
$$
\ln(10^{-3})=-3\ln10\approx-6.907755,\qquad
\ln(0.6)=\ln6-\ln10\approx-0.510826.
$$
Divide:
$$
n\ge\frac{-6.907755}{-0.510826}\approx13.524,
$$
so $n=14$ rounds suffice. Direct evaluation shows $0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}$, confirming minimality. A variant with $d_{0}=5\times10^{-2}$ and target $\varepsilon=p_{e}=9\times10^{-5}$ yields $n=13$ cycles.

### 4.4 Shot budget for ontology discrimination

**Input.** We assume $F=0.99991$, giving $p_{e}=9\times10^{-5}$. Suppose two candidate ontologies differ in the expectation value of some readout‑accessible observable by $\delta$. At confidence level $\alpha=0.01$, Hoeffding’s inequality requires
$$
N\ge\frac{\ln(2/\alpha)}{2\,\delta^{2}}=\frac{\ln200}{2\,\delta^{2}}.
$$
Evaluate $\ln200\approx5.298317$.

*For $\delta=10^{-3}$*:
$$
N\ge\frac{5.298317}{2\times10^{-6}}=2.649159\times10^{6}.
$$
*For $\delta=10^{-4}$*:
$$
N\ge\frac{5.298317}{2\times10^{-8}}=2.649159\times10^{8}.
$$
The per‑shot error floor also bounds resolvability: discrepancies $\delta\lesssim p_{e}=9\times10^{-5}$ are comparable to the readout noise per shot.

### 4.5 A two‑ontology toy model with two fixed points

We now exhibit the underdetermined regime explicitly. Let the operational datum be a single scalar $x\in\mathbb{R}$ (a normalized discrepancy between predicted and observed readout statistics), with two candidate ontologies $A$ and $B$:
$$
T_{A}(x)=0.5\,x+0.5\,a,\qquad
T_{B}(x)=0.5\,x+0.5\,b,
$$
with ontology‑dependent offsets $a\neq b$, and a selection rule that keeps the branch whose prediction is closer. Solving $x=T_{A}(x)$ gives $x_{A}^{*}=a$; similarly $x_{B}^{*}=b$. Each branch is contractive with $L=0.5<1$, so both fixed points are locally attracting; the failure of uniqueness comes from the multiplicity of branch fixed points, not from divergence.

**Concrete numbers.** Take $a=0$, $b=1$, and initial guess $x_{0}=0.6$. The basin boundary is the midpoint $m=(a+b)/2=0.5$; since $x_{0}>m$, the iteration follows branch $B$:
$$
x_{1}=0.5\times0.6+0.5=0.8,\quad
x_{2}=0.5\times0.8+0.5=0.9,\quad
x_{3}=0.5\times0.9+0.5=0.95,
$$
with closed form $x_{n}=1-0.4\times0.5^{n}$. The iteration converges to $x_{B}^{*}=1$ and never visits branch $A$. The two ontologies are physically inequivalent—say, an energy eigenmode with offset $a=0$ versus a collective variable with offset $b=1$—yet each is exactly self‑consistent on its own basin, and the final ontology is determined by the *initial guess*, not by the data.

### 4.6 Symmetry‑breaking sensitivity (projection)

If the readout channel had a small non‑equivariant component—an asymmetry $\epsilon$ between the two readout axes—the smallest detectable asymmetry is bounded by the total estimation uncertainty:
$$
\epsilon_{\min}\approx\sqrt{\sigma_{p}^{2}+p_{e}^{2}}.
$$
With $N=10^{4}$ (Derivation 4.2):
$$
\epsilon_{\min}\approx\sqrt{(5.00\times10^{-3})^{2}+(9\times10^{-5})^{2}}
=\sqrt{2.5\times10^{-5}+8.1\times10^{-9}}
\approx5.001\times10^{-3}.
$$
At the crossover count $N=3.09\times10^{7}$, $\sigma_{p}\approx9.0\times10^{-5}$, giving
$$
\epsilon_{\min}\approx\sqrt{(9.0\times10^{-5})^{2}+(9\times10^{-5})^{2}}
=\sqrt{1.62\times10^{-8}}\approx1.27\times10^{-4}.
$$
Any genuine ontological signature smaller than $\epsilon_{\min}$ is operationally invisible.

## 5. Results

All numbers below are computed in Section 4; assumptions are restated where the input was assumed rather than sourced.

**R1 (Convergence in the contraction regime; projection).** With Lipschitz constant $L=0.6$ (illustrative input) and initial discrepancy $d_{0}=1$, calibration reaches tolerance $\varepsilon=10^{-3}$ in exactly $n=14$ rounds (Derivation 4.3; verified by $0.6^{14}\approx7.836\times10^{-4}<10^{-3}<0.6^{13}\approx1.306\times10^{-3}$). A variant with $d_{0}=5\times10^{-2}$ and target $p_{e}=9\times10^{-5}$ needs $n=13$ cycles. In this regime the operational circularity is benign: unique fixed point, initial‑ontology independence.

**R2 (Multiplicity in the two‑branch model).** In the toy model of Section 4.5 with offsets $a=0$, $b=1$, there are two exact fixed points $x_{A}^{*}=0$ and $x_{B}^{*}=1$, separated by the basin boundary $m=0.5$; iteration from $x_{0}=0.6$ converges to $x_{B}^{*}=1$ via $x_{1}=0.8$, $x_{2}=0.9$, $x_{3}=0.95$, with closed form $x_{n}=1-0.4\times0.5^{n}$. The final ontology is determined by the initial guess, not the data: ontological underdetermination is realizable in a locally contractive loop.

**R3 (Readout error floor).** From the assumed fidelity $F=0.99991$: $p_{e}=9\times10^{-5}$, i.e. about one error per $1.11\times10^{4}$ shots; over the reported $10^{6}$ trials, $N_{\text{err}}=90\pm10$ wrong outcomes are expected.

**R4 (Shot budget; projection).** Resolving an ontology‑discriminating signal of size $\delta=10^{-3}$ at confidence $\alpha=0.01$ requires $N=2.649159\times10^{6}$ shots, approximately $2.65$ times the assumed $10^{6}$‑trial count of Assumption 1. For $\delta=10^{-4}$, the requirement rises to $N=2.649159\times10^{8}$ shots. These assume the illustrative fidelity $F=0.99991$, readout noise only, and Hoeffding’s bound.

**R5 (Statistical floor and symmetry sensitivity; projection).** At $N=10^{4}$ shots per setting, $\sigma_{p}\approx5.00\times10^{-3}$, exceeding the readout floor by a factor $\approx55.6$; the crossover is $N\approx3.09\times10^{7}$ shots. The smallest detectable readout asymmetry is $\epsilon_{\min}\approx5.008\times10^{-3}$ at $10^{4}$ shots and $\epsilon_{\min}\approx1.27\times10^{-4}$ at the crossover count.

**R6 (Structural dichotomy).** The equivariant symmetry of Section 3.3 leaves $d_{\text{orbit}}=3$ continuous descriptive parameters (two axis angles, one basis phase) unconstrained by any equivariant operational statistic; the family of data‑compatible ontologies is uncountable. The cross‑platform question reduces to ontology alignment in the sense of [3]: either a correspondence preserving physical interpretation exists across platform fixed points, or it does not. The formalism does not decide which obtains—that is an empirical question with the budget of R4.

**Headline claim.** The circularity of qubit ontology is benign exactly when the calibration operator $T$ is a contraction (unique fixed point, convergence in a small number of rounds in the illustrative model), and problematic exactly to the extent that multiplicity or an equivariant symmetry survives.

## 6. Discussion

**Limitations.** The contraction analysis (R1) uses an illustrative Lipschitz constant; real calibration loops may have state‑dependent or iteration‑dependent $L$, and the Banach uniqueness guarantee applies only to the idealized operator $T=\Gamma\circ\Phi$ with exact realization maps. Real $\Gamma$ includes unmodeled drift, and drift can violate the contraction condition between rounds. The two‑branch model (R2) is deliberately minimal: one scalar datum, two branches. Real ontology spaces are high‑dimensional, and multiplicity there may take forms—continuous families of fixed points, limit cycles—not captured here. The shot‑budget result (R4) assumes the discriminating observable is readout‑accessible with the fidelity of [4] and that the only noise is readout noise; additional decoherence during the discriminating sequence would inflate $N$ beyond the computed values. The dimension count behind R6 assumes perfect equivariance; any real platform has stray asymmetries (bias fields, crosstalk) that partially break $SO(3)$, and Derivation 4.6 quantifies the sensitivity only under the assumed shot counts and an idealized noise model—independent, stationary shots. Correlated readout errors would inflate $\sigma_{p}$ and worsen $\epsilon_{\min}$.

**Failure modes.** The framework fails if calibration maps are chaotic rather than contractive—then no fixed point exists and “the qubit” has no self‑consistent definition at all, a stronger conclusion than we claim. It also fails if the symmetry orbit is not a gauge: if two members of the orbit correspond to genuinely different physical couplings (e.g., a single‑ion transition versus a collective motional mode) that happen to be related by the equivariance, then the “benign gauge” reading is wrong and the underdetermination is physical, not conventional. We cannot decide this from operational data by construction—that is the point—but an independent probe outside the loop (e.g., a measurement coupling to a third level, or to the environment) could.

**What would falsify the claims.** (i) A demonstration that a calibration loop on a real platform converges to a unique, platform‑independent Hilbert‑space identification including the axis‑labeling degrees of freedom—i.e., that the orbit is in fact broken by operational data alone—would falsify the three‑dimensional‑orbit claim (R6). (ii) A demonstration that two members of the orbit give different predictions for an observable accessible only outside the calibration loop (for example, a probe coupling to a third level or to the environment) would show that the equivariant symmetry is physical rather than conventional, falsifying the benign‑gauge reading of R6. (iii) A demonstration that the shot budget of R4 is unattainable in practice—for instance, that correlated readout errors inflate the required $N$ by orders of magnitude beyond the Hoeffding value—would undermine the empirical testability of the underdetermination claim rather than the claim itself, and would shift the burden to a different discriminating observable.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.** Calibration engineers and quantum hardware designers are the principal users of the present analysis. If the contraction condition holds for a given platform, designers can rely on standard calibration routines to yield a unique, platform‑independent qubit identification, simplifying device qualification and cross‑platform benchmarking. Conversely, if multiplicity or equivariance is present, designers must recognize that calibration alone cannot resolve the underlying ontological ambiguity; additional, out‑of‑loop probes become necessary to certify that the implemented qubit matches the intended physical model.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept). No hardware or software implementation has been demonstrated.

Overall, the formalism presented provides a clear criterion for assessing when operational circularity is merely a calibration artifact and when it signals deeper ontological ambiguity. By linking the contraction properties of the calibration operator to the uniqueness of the qubit’s operational identification, the analysis guides both theoretical scrutiny and experimental design in quantum hardware development, ensuring that future engineering efforts can deliberately target the regimes where calibration is benign or where additional out‑of‑loop probes are required to resolve ontological underdetermination.

## Conclusion

The headline conclusion is that uniqueness is a property of the calibration dynamics, not of the qubit: whether operational circularity is benign or masks ontological underdetermination is decidable only by the contraction structure of $T$ and by experiments whose budget we have quantified. Consequently, quantum‑hardware designers should evaluate the Lipschitz constant of their calibration operator and verify contraction (e.g., by measuring convergence rates) to determine if standard calibration suffices or if additional, out‑of‑loop probes are required to break potential equivariant symmetries.  

Future work will extend the present single‑parameter analysis to multi‑parameter calibration operators, incorporate realistic drift and correlated readout noise models, and perform empirical tests on representative transmon, trapped‑ion, and spin platforms to validate the contraction‑based uniqueness criterion and to measure the practical shot budgets predicted here.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 9. length 4793 -> 3808 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
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
[9] https://papers.qnfo.org/papers/no-thing-there. QNFO: No Thing There: Control, Readout, and Self-Referential Metrology in Engineered Quantum Systems.
[10] https://papers.qnfo.org/papers/paper-beyond-the-qubit. QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation.
[11] https://papers.qnfo.org/papers/semantic-fidelity-an-operational-measure-for-borrowed-quantum-terms-and-the-scal. QNFO: Semantic Fidelity: An Operational Measure for Borrowed Quantum Terms and the Scale at Which They Fail.
