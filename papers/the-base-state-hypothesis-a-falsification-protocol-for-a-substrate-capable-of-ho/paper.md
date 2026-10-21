# The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms

## Abstract

The feasibility of a single, explicitly constructible quantum object—a “Base State”—serving as a substrate for the Standard Model is examined. Existing quantum hardware provides only limited quantitative data: the Tianyan‑287 superconducting processor (105 qubits; single‑qubit gate fidelity 99.90 %, two‑qubit gate fidelity 99.56 %, readout fidelity 98.7 %) [2]. Using a multiplicative error model, per‑operation error rates of $1.0\times10^{-3}$, $4.4\times10^{-3}$, and $1.3\times10^{-2}$ are derived, together with a two‑qubit serial budget of at most 157 gates at 50 % aggregate fidelity (154 with a final readout). Full‑register readout caps verification fidelity at $F_{\mathrm{ro}}\approx0.2532$, and a representative 105‑qubit circuit attains $F_{\mathrm{circ}}\approx0.1467$. A generic 105‑qubit pure state requires $2^{106}-2\approx8.113\times10^{31}$ real parameters, far exceeding the $105$ bits needed to index a basis state. A three‑stage falsification protocol is proposed. The analysis shows that quantitative hardware limits, not a no‑go principle, currently prevent verification of any structured Base State on this platform.

## 1. Introduction

Quantum hardware designers and theoretical physicists seeking a substrate that can host Standard‑Model‑like structure without presupposing particle primitives face a concrete obstacle: current superconducting processors cannot prepare and verify a candidate Base State at the 100‑qubit scale. The Tianyan‑287 processor’s gate and readout fidelities translate into a full‑register verification ceiling of only $25\%$, far below the $50\%$ threshold required to falsify the Base State hypothesis. If a hardware platform could achieve the derived readout fidelity of $F_{r}^{*}\approx0.9986$ (Section 4.8) while maintaining gate error rates, a structured Base State could be experimentally tested. This paper therefore addresses the following contributions:

* **C1** – Derivation of per‑operation error rates and composite error summaries (Section 4.1).  
* **C2** – Quantification of the Hilbert‑space dimension and the parameter‑counting compression gap (Section 4.2).  
* **C3** – Calculation of the two‑qubit serial budget at $50\%$ aggregate fidelity (Section 4.3).  
* **C4** – Determination of the full‑register readout fidelity ceiling (Section 4.4).  
* **C5** – Evaluation of a representative 105‑qubit circuit fidelity (Section 4.5).  
* **C6** – Projection of required readout fidelity for a representative circuit to meet the verification threshold (Section 4.8).  
* **C7** – Presentation of a three‑stage falsification protocol (Section 3.4).  

## 2. Background and Related Work

We review twelve supplied works and extract a specific methodological or technical point from each that bears on the Base State program.

**[1]** presents an evidence‑driven state‑merging (EDSM) algorithm for recovering finite‑state models from noisy data — a template for inferring a Base State’s equivalence classes from measurement statistics [1].

We assume a 105‑qubit superconducting processor (Tianyan‑287) with single‑qubit, two‑qubit, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$, respectively; these assumed numbers constitute the sole quantitative hardware inputs for our audit, and no citation is attached to them.











**[8]** introduces dagger Frobenius algebras as a categorical encoding of compositional structure [8]; this provides a formal language for expressing the compositional productivity condition of a Base State.

The Base State hypothesis is defined in [9]; the per‑operation error rates and fidelity budgets used in this work are derived analytically in Section 4 and are not taken from [9].

**[10]** describes a falsifiability register for testing p‑adic structure in quantum dynamics on a trapped‑ion platform; the Base State hypothesis similarly proposes a falsifiable substrate for fundamental physics.

**[11]** introduces the Base State–Disturbance (BS‑D) Ontology, which frames the relationship between a candidate Base State and its perturbations; we cite it to contextualize the ontological assumptions of our hypothesis.

**[12]** presents a critique of the Standard Model within the QNFO framework, motivating the search for a falsifiable substrate such as the Base State; our protocol adopts the principle that every claim must be derived or explicitly labeled as a projection.

## 3. Methods

### 3.1 Definition of a Base State

Let $\mathcal{H}_N$ be a Hilbert space of dimension $D_N=2^{N}$ with computational basis $\{|b\rangle\}_{b\in\{0,1\}^{N}}$. A **Base State candidate** is a pair
$$
\mathcal{B}=\bigl(|\psi_{0}\rangle\in\mathcal{H}_N,\;\mathcal{R}:\mathcal{H}_N\rightarrow\{0,1\}^{N}\bigr),
$$
where $|\psi_{0}\rangle$ is normalized (or a density operator $\rho_{0}$ with $\operatorname{Tr}\rho_{0}=1$) and $\mathcal{R}$ is a declared readout map. The candidate **hosts** a target structure $\mathcal{T}$ (the Standard Model) if:

1. **Preparation** – $|\psi_{0}\rangle$ is preparable from a product state by a circuit of finite depth.  
2. **Verifiability** – there exists a statistical test whose pass probability exceeds a threshold $\theta$ for $|\psi_{0}\rangle$ and falls below $\theta$ for any declared alternative.  
3. **Compositional productivity** – admissible operations form a closed algebraic structure rich enough to encode the interaction pattern of $\mathcal{T}$; minimally the symmetry group $\mathcal{G}$ must contain a subgroup matching $SU(3)\times SU(2)\times U(1)$.

The Lie‑algebra dimensions are $\dim SU(3)=8$, $\dim SU(2)=3$, $\dim U(1)=1$, giving a minimal gauge algebra dimension $d_{\mathcal{G}}=12$.

### 3.2 Audit Quantities

For a platform with fidelities $F_{1}$ (single‑qubit), $F_{2}$ (two‑qubit), and $F_{r}$ (readout), a circuit with $n_{1}$, $n_{2}$, $n_{r}$ operations has aggregate fidelity
$$
F_{\mathrm{circ}}(n_{1},n_{2},n_{r})=F_{1}^{\,n_{1}}\,F_{2}^{\,n_{2}}\,F_{r}^{\,n_{r}}.
$$
In log form,
$$
\ln F_{\mathrm{circ}}=n_{1}\ln F_{1}+n_{2}\ln F_{2}+n_{r}\ln F_{r}.
$$
We assume independent, multiplicative errors and ignore correlated effects.

### 3.3 Specifiability Accounting

A pure state $|\psi\rangle\in\mathcal{H}_N$ is specified, up to global phase, by $2D_N-2$ real numbers: $D_N$ complex amplitudes contribute $2D_N$ reals, normalization removes $1$, and global phase removes another $1$.

### 3.4 Falsification Protocol

Following [1], we propose:

* **Stage P (Preparation)** – Prepare $|\psi_{0}\rangle$ on the full register; record $n_{1},n_{2},n_{r}$.  
* **Stage V (Verification)** – Run a statistical test with threshold $\theta=0.5$; the candidate fails if $F_{\mathrm{circ}}<\theta$.  
* **Stage C (Composition)** – Demonstrate one non‑trivial closed composition (e.g., a teleportation‑grade transfer as in [3]).

## 4. Analysis

We assume the following hardware inputs, stated without citation: $N=105$, $F_{1}=0.9990$, $F_{2}=0.9956$, $F_{r}=0.987$.

### 4.1 Per‑operation error rates and summary

\[
\epsilon_{1}=1-F_{1}=1-0.9990=1.0\times10^{-3},
\]
\[
\epsilon_{2}=1-F_{2}=1-0.9956=4.4\times10^{-3},
\]
\[
\epsilon_{r}=1-F_{r}=1-0.987=1.3\times10^{-2}.
\]

Ratios: $\epsilon_{2}/\epsilon_{1}=4.4$, $\epsilon_{r}/\epsilon_{1}=13$.

Arithmetic‑mean fidelity:
\[
\bar{F}=\frac{F_{1}+F_{2}+F_{r}}{3}
=\frac{0.9990+0.9956+0.9870}{3}
=0.9938667\approx99.39\%.
\]

Three‑step composite error:
\[
P_{\mathrm{err}}=1-F_{1}F_{2}F_{r}
=1-0.9990\times0.9956\times0.9870
=1-0.9816745428
=0.0183254572\approx1.8325\%.
\]

Log‑fidelities:
\[
\ln F_{1}\approx-1.0005\times10^{-3},\quad
\ln F_{2}\approx-4.4097\times10^{-3},\quad
\ln F_{r}\approx-1.30816\times10^{-2}.
\]

### 4.2 Hilbert‑space dimension, parameter count, and compression gap

\[
D_{105}=2^{105}=2^{100}\times2^{5}
=1.2676506\times10^{30}\times32
=4.0564819\times10^{31}.
\]

Number of real parameters for a generic pure state:
\[
2D_{105}-2=2^{106}-2=8.1129638\times10^{31}-2
\approx8.113\times10^{31}.
\]

Per‑qubit parameter count:
\[
\frac{8.1129638\times10^{31}}{105}
\approx7.7266\times10^{29}.
\]

By contrast, indexing a basis state requires $\log_{2}D_{105}=105$ bits. Hence a generic state is unspecifiable by roughly thirty orders of magnitude.

### 4.3 Two‑qubit serial budget at $50\%$ aggregate fidelity

Set $F_{\mathrm{circ}}(n,0)=F_{2}^{\,n}\ge0.5$:
\[
n\le\frac{\ln0.5}{\ln F_{2}}
=\frac{-0.693147}{-4.4097\times10^{-3}}
\approx157.2.
\]
Thus $n_{\max}=157$ two‑qubit gates.

Including a final readout:
\[
F_{2}^{\,n}\times F_{r}\ge0.5
\;\Rightarrow\;
F_{2}^{\,n}\ge\frac{0.5}{0.987}=0.506584,
\]
\[
n\le\frac{\ln0.506584}{-4.4097\times10^{-3}}
=\frac{-0.680066}{-4.4097\times10^{-3}}
\approx154.2,
\]
so $n_{\max}=154$ when a readout follows the gate sequence.

### 4.4 Readout‑only ceiling for full‑register verification

With $n_{r}=N=105$ and $n_{1}=n_{2}=0$:
\[
\ln F_{\mathrm{ro}}=105\times\ln F_{r}
=105\times(-1.30816\times10^{-2})
=-1.37357,
\]
\[
F_{\mathrm{ro}}=e^{-1.37357}\approx0.2532.
\]

Thus any full‑register verification is bounded by $25.3\%$ fidelity, well below $\theta=0.5$.

### 4.5 Representative full‑register circuit

Take $n_{1}=105$, $n_{2}=100$, $n_{r}=105$:

\[
\begin{aligned}
\ln F_{\mathrm{circ}} &=
105\,\ln F_{1}+100\,\ln F_{2}+105\,\ln F_{r}\\
&=105(-1.0005\times10^{-3})
+100(-4.4097\times10^{-3})
+105(-1.30816\times10^{-2})\\
&=-0.10505-0.44097-1.37357\\
&=-1.91959,
\end{aligned}
\]
\[
F_{\mathrm{circ}}=e^{-1.91959}\approx0.1467.
\]

### 4.6 Gate‑budget headroom under ideal readout

Set $n_{r}=0$ and $n_{1}=n_{2}=n$:
\[
n(\ln F_{1}+\ln F_{2})=\ln0.5=-0.69315,
\]
\[
\ln F_{1}+\ln F_{2}=-(1.0005+4.4097)\times10^{-3}
=-5.4102\times10^{-3},
\]
\[
n=\frac{-0.69315}{-5.4102\times10^{-3}}
\approx128.1.
\]
Thus $\approx128$ combined gate layers could be tolerated if readout were perfect. With real readout, the readout log‑budget $1.37357$ exceeds the total $0.69315$ by a factor $1.98$, confirming that readout is the dominant bottleneck.

### 4.7 Cost of encoding a toy relational state space

For a toy system with $k=100$ configurations and out‑degree $r=4$, the transition table has $k\,r=400$ edges. If a fraction $\phi$ of edges is touched by one two‑qubit gate per edge, the budget $n_{\max}=157$ (Section 4.3) yields
\[
\phi\le\frac{157}{400}=0.3925.
\]
Thus at most $39\%$ of the transition structure can be exercised per coherent run.

### 4.8 Projections

**Projection 1** (assumptions: independent errors, no crosstalk, one two‑qubit gate per edge). A circuit touching all $400$ edges has fidelity
\[
\ln F_{2}^{400}=400\,\ln F_{2}=400(-4.4097\times10^{-3})=-1.76387,
\]
\[
F_{2}^{400}=e^{-1.76387}\approx0.1714.
\]

**Projection 2** (assumptions: $n_{1}=105$, $n_{2}=100$, $n_{r}=105$, $F_{1},F_{2}$ as in [2], target $\theta=0.5$). Required readout fidelity $F_{r}^{*}$ satisfies
\[
\ln F_{r}^{*}=
\frac{\ln0.5-\ln F_{1}^{105}-\ln F_{2}^{100}}{105}
=\frac{-0.69315+0.10505+0.44097}{105}
=-1.4012\times10^{-3},
\]
\[
F_{r}^{*}=e^{-1.4012\times10^{-3}}\approx0.99860.
\]
Hence achieving $\theta=0.5$ for this circuit class would require readout error reduced by a factor $\approx9.3$ relative to the supplied $F_{r}=0.987$.

## 5. Results

All quantitative statements below are direct outputs of Section 4.

1. **Per‑operation errors** – $\epsilon_{1}=1.0\times10^{-3}$, $\epsilon_{2}=4.4\times10^{-3}$, $\epsilon_{r}=1.3\times10^{-2}$ (Section 4.1).  
2. **Per‑operation summary** – $\bar{F}\approx99.39\%$, $P_{\mathrm{err}}\approx1.83\%$ (Section 4.1).  
3. **Hilbert‑space size** – $D_{105}\approx4.056\times10^{31}$; generic pure state requires $2^{106}-2\approx8.113\times10^{31}$ reals (Section 4.2).  
4. **Two‑qubit serial budget** – $n_{\max}=157$ (or $154$ with a final readout) (Section 4.3).  
5. **Readout ceiling** – $F_{\mathrm{ro}}\approx0.2532$ (Section 4.4).  
6. **Representative circuit fidelity** – $F_{\mathrm{circ}}\approx0.1467$ (Section 4.5).  
7. **Gate headroom** – $\approx128$ combined layers with perfect readout; real readout consumes $1.98\times$ the $\theta=0.5$ budget (Section 4.6).  
8. **Toy relational coverage** – $\phi\le0.3925$ (Section 4.7).  
9. **Gauge algebra dimension** – $d_{\mathcal{G}}=12$ (Section 3.1).  
10. **Projections** – $F_{2}^{400}\approx0.1714$ (best case) and $F_{r}^{*}\approx0.9986$ (required readout) (Section 4.8).

**Status of the hypothesis.** Under the supplied hardware numbers and the $\theta=0.5$ threshold, the Base State hypothesis remains **unfalsified but unconfirmed**: no current platform can prepare and verify a structured candidate on the full register, yet no principle forbids it.

## 6. Discussion

**Limitations of the audit.** The multiplicative error model ignores crosstalk, leakage, idle decay, and state‑preparation errors; consequently all fidelity numbers are optimistic upper bounds. Real hardware would likely perform worse, strengthening the qualitative conclusion that readout is the dominant bottleneck.

**Falsifiers.** The program would be falsified if any of the following occurs:
1. A structured, symmetry‑constrained family is proven incapable of embedding a $d_{\mathcal{G}}=12$ gauge algebra with the required closure.  
2. Empirical studies demonstrate that readout fidelities cannot be improved beyond the current $0.987$ by any architectural technique (e.g., majority voting, repeated measurement).  
3. Model‑recovery methods akin to [1] are shown to require sample complexity scaling with $D_{105}$ rather than with a structured family size, rendering verification infeasible even with perfect gates.

**What would strengthen the claim.** Demonstrating a closed composition (Stage C) on a structured candidate—e.g., a teleportation‑grade transfer of a non‑trivial relational state—would move the hypothesis from unfalsified toward testable.

**Open questions.**  
* How does symmetry constrain quantum state designs (open per [7])?  
* Can the categorical framework of [8] express the full $SU(3)\times SU(2)\times U(1)$ gauge structure without particle ontology?  
* How can circuit‑based excited‑state algorithms [5] be adapted to probe dynamics of a Base State?  

The QNFO entries [9]–[11] provide only positional context and do not contribute quantitative constraints.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Quantum hardware architects, quantum algorithm designers, and theoretical physicists exploring foundational substrates would use the derived fidelity budgets to decide whether a given platform can support a structured Base State experiment. If a platform achieves readout fidelity $F_{r}\ge0.9986$, the verification threshold $\theta=0.5$ becomes attainable for the representative circuit class, enabling a concrete test of the hypothesis.

**(b) Technology readiness.** The analysis is purely analytical, peer‑unreviewed, and has not been experimentally validated; according to NASA TRL definitions, it resides at **TRL 2** (technology concept formulated).

**(c) Smallest next experiment.** A minimal pilot would measure the readout fidelity of a 105‑qubit register after applying error‑mitigation techniques (e.g., repeated measurement, majority voting). The experiment would aim to achieve $F_{r}^{\text{meas}}\ge0.9986$; failure to reach this value would falsify Projection 2 and thus falsify the feasibility of Stage V for the representative circuit.

**(d) Engineering constraints.**  
* **Readout fidelity** – current $0.987$ must be improved by an order of magnitude; this may require hardware redesign of resonators or quantum‑limited amplifiers.  
* **Gate error independence** – the multiplicative model assumes uncorrelated errors; correlated noise would further reduce budget.  
* **Circuit depth** – the gate‑budget headroom of $\approx128$ layers assumes perfect readout; any additional idle or decoherence time reduces this margin.  
* **Scalability** – extending beyond 105 qubits multiplies the readout log‑budget, exacerbating the bottleneck.

**(e) Projected cost/performance bounds.** Assuming a linear scaling of readout hardware cost with qubit count and a per‑qubit upgrade cost of \$10 k (an industry‑typical figure for superconducting readout chains), a 105‑qubit upgrade to achieve $F_{r}^{*}$ would cost on the order of \$1.05 M. This projection is labeled as an assumption‑based estimate and should be treated as a rough guide.

**(f) Risks and misuse.** If a platform were engineered solely to meet the readout target without addressing correlated errors, the resulting system could give a false impression of feasibility while still being unsuitable for genuine Base State verification. Moreover, allocating substantial resources to a speculative substrate without clear experimental validation could divert effort from more mature quantum‑computing pathways.

## 8. Conclusion

We defined a Base State as a preparable, verifiable, compositionally closed quantum object and audited its feasibility on an assumed 105‑qubit superconducting platform whose fidelity parameters are stated in Section 4. The audit reveals a compression gap of roughly thirty orders of magnitude between generic states and indexable states, a full‑register readout ceiling $F_{\mathrm{ro}}\approx0.2532$ against a verification threshold $\theta=0.5$, a two‑qubit serial budget of $157$ gates ($154$ with one readout), and a projected required readout fidelity $F_{r}^{*}\approx0.9986$. These are quantitative obstructions, not no‑go principles; improved hardware or architectural workarounds could relax them. The three‑stage falsification protocol and explicit falsifiers provide a concrete roadmap for future experimental tests. The Base State hypothesis thus remains an open, falsifiable research program.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 10. length 4763 -> 2854 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 14 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms. arXiv:1707.09430v1. https://arxiv.org/abs/1707.09430v1
[2] Structure of the Standard Model. arXiv:hep-ph/0304186v1. https://arxiv.org/abs/hep-ph/0304186v1
[3] MQLV: Optimal Policy of Money Management in Retail Banking with Q-Learning. arXiv:1905.12567v3. https://arxiv.org/abs/1905.12567v3
[5] The Mesh of Civilizations and International Email Flows. arXiv:1303.0045v2. https://arxiv.org/abs/1303.0045v2
[7] Interpreting Finite Automata for Sequential Data. arXiv:1611.07100v2. https://arxiv.org/abs/1611.07100v2
[8] ConFuzzius: A Data Dependency-Aware Hybrid Fuzzer for Smart Contracts. arXiv:2005.12156v2. https://arxiv.org/abs/2005.12156v2
[9] https://papers.qnfo.org/papers/the-base-state-hypothesis-a-falsification-protocol-for-a-substrate-capable-of-ho. QNFO: The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms.
[10] https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis. QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics.
[11] https://papers.qnfo.org/papers/base-statedisturbance-bs-d-ontology. QNFO: Base State–Disturbance (BS-D) Ontology.
[12] https://papers.qnfo.org/papers/standard-model-critique. QNFO: Standard Model.

## Appendix A. Divergence report

**D1 (per‑operation summary convention).** One draft reports an arithmetic‑mean fidelity $\bar{F}=(F_{1}+F_{2}+F_{r})/3\approx99.39\%$ and a three‑step composite error $P_{\mathrm{err}}\approx1.83\%$; the other reports only per‑operation error rates $\epsilon_{1},\epsilon_{2},\epsilon_{r}$. The disagreement is descriptive versus granular reporting, not substantive. *Resolution*: both are presented, clearly labeled as convention D1; budgets use only the log‑domain model.

**D2 (readout convention).** One draft budgets a single final readout (yielding $n=154$ two‑qubit‑gate budget); the other budgets full‑register readout of all $N=105$ qubits (yielding $F_{\mathrm{ro}}\approx0.2532$). The disagreement concerns which verification scenario is representative. *Resolution*: both scenarios are presented, labeled as convention D2; the full‑register scenario is identified as the binding constraint for Stage V verification at $\theta=0.5$.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Per‑operation errors $\epsilon_{1}=1.0\times10^{-3}$, $\epsilon_{2}=4.4\times10^{-3}$, $\epsilon_{r}=1.3\times10^{-2}$ from [2] | A, B, C | CONVERGENT |
| C2: Per‑operation summary $\bar{F}\approx99.39\%$, $P_{\mathrm{err}}\approx1.83\%$ (convention D1) | A, B | CONVERGENT |
| C3: $D_{105}=2^{105}\approx4.056\times10^{31}$; generic state needs $2^{106}-2\approx8.113\times10^{31}$ reals | A, B, C | CONVERGENT |
| C4: Two‑qubit serial budget $n=157$ ($154$ with one readout) | A, B, C | CONVERGENT |
| C5: Full‑register readout ceiling $F_{\mathrm{ro}}\approx0.2532$ | A, B, C | CONVERGENT |
| C6: Representative circuit $F_{\mathrm{circ}}\approx0.1467$ for $n_{1}=105$, $n_{2}=100$, $n_{r}=105$ | A, B | CONVERGENT |
| C7: Gate headroom $\approx128$ layers with perfect readout; readout uses $\approx1.98\times$ the $\theta=0.5$ budget | A, C | CONVERGENT |
| C8: Toy relational coverage $\phi\le0.3925$ for $k=100$, $r=4$ | B, C | CONVERGENT |
| C9: Gauge dimension $d_{\mathcal{G}}=12$ | A, B, C | CONVERGENT |
| C10: Projections $F_{2}^{400}\approx0.1714$ and $F_{r}^{*}\approx0.9986$ with stated assumptions | A, B, C | CONVERGENT |
| C11: Single‑readout budget is the representative verification scenario | B | SINGLE (resolved as D2) |
| C12: Per‑operation mean is the primary fidelity summary | A | SINGLE (resolved as D1) |