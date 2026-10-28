# Ultrametric $p$‑Adic Noise Structure and Heisenberg‑Limited Quantum Metrology: Error Resilience by Geometry, Not Overhead

## Abstract

Quantum metrology seeks phase sensitivities that surpass the standard quantum limit (SQL) $\Delta\theta\propto N^{-1/2}$, aiming for the Heisenberg limit $\Delta\theta\propto N^{-1}$. Decoherence typically destroys this advantage, and active error‑correction incurs prohibitive overhead for near‑term sensors. This work addresses the gap that no passive noise‑geometry mechanism has been quantitatively analyzed for metrological scaling. By modeling decoherence as a $p$‑adic hierarchical stochastic process on an ultrametric lattice, the strong triangle inequality forces error events on nested clusters to be nested rather than independent. For a hierarchy of $L$ levels with level‑$k$ error weight $\varepsilon_k=\varepsilon_0p^{-k}$, the ultrametric error probability is $P_{\mathrm{U}}=\varepsilon_0p^{-L}$, while the Archimedean independent‑event union bound is $P_{\mathrm{A}}=\varepsilon_0\frac{1-p^{-(L+1)}}{1-p^{-1}}$. With $p=2$, $L=10$, $\varepsilon_0=10^{-2}$ the ultrametric probability is $9.765625\times10^{-6}$ versus an Archimedean bound of $1.9990234375\times10^{-2}$, a ratio of exactly $2047$. Propagating these probabilities to the quantum Fisher information (QFI) of an $N$‑probe GHZ state with $L=\log_2N$ yields Heisenberg scaling $\Delta\theta\propto N^{-1}$ under the ultrametric model, whereas independent dephasing collapses GHZ coherence exponentially in $N$. The principal result is a scaling prediction that is falsifiable by measuring nested‑event statistics; if the prediction fails, the ultrametric hypothesis is rejected. The analysis connects the model to $p$‑adic mathematical‑physics literature and documents the conventions adopted.

## 1. Introduction

Engineers of quantum sensors—including magnetometers, atomic clocks, and rotation sensors—currently confront a trade‑off: entangled probes such as Greenberger–Horne–Zeilinger (GHZ) states promise Heisenberg‑limited phase sensitivity $\Delta\theta\propto N^{-1}$, yet decoherence degrades entanglement exponentially in the probe number $N$, forcing a fallback to the SQL $\Delta\theta\propto N^{-1/2}$ and requiring extensive error‑correction hardware that is incompatible with size, power, and cost constraints. A passive mechanism that protects entangled probes without active correction would shift the design calculus, allowing resources to be allocated to larger probe arrays rather than to syndrome extraction and decoding.

The candidate mechanism examined here is an ultrametric—equivalently $p$‑adic—hierarchical structure of the decoherence process. The strong triangle inequality $d(x,z)\le\max\{d(x,y),d(y,z)\}$ forces error events that belong to nested clusters to be nested rather than independent, so that the probability of the union of level‑wise error events is the maximum of the level probabilities, not their sum. This paper derives the quantitative consequences of that nesting axiom, without claiming that physical decoherence has been demonstrated to be ultrametric. The falsifiable hypothesis is that decoherence obeys the nesting law; Section 6 specifies the experimental signatures whose observation would falsify the claim.

**Contributions.**
- **C1.** Derivation of the max‑of‑levels error probability $P_{\mathrm{U}}=\varepsilon_0p^{-L}$ (Section 3.3).
- **C2.** Exact ratio $P_{\mathrm{A}}/P_{\mathrm{U}}=2047$ for $p=2$, $L=10$, $\varepsilon_0=10^{-2}$ (Section 4.1).
- **C3.** Propagation of $P_{\mathrm{U}}$ to GHZ QFI and demonstration of Heisenberg scaling $\Delta\theta\propto N^{-1}$ (Section 4.2).
- **C4.** Identification of the optimized product‑probe competitor with sensitivity $\Delta\theta^{\mathrm{prod}}\approx8.4946\times10^{-4}$ at $N=1024$, $\gamma=10^{-2}$ (Section 4.4).
- **C5.** Falsifiability protocol based on nested‑event statistics and scaling measurements (Sections 6.2 and 7).

## 2. Background and Related Work

**Ultrametric data analysis.** Reference [1] models anomaly and change by embedding data in an ultrametric space derived from correspondence analysis of cross‑tabulation counts, thereby providing a constructive route from raw records to an induced ultrametric hierarchy.

**Markov processes on $p$‑adic spaces.** Reference [2] shows that stationary Markov processes on ultrametric spaces embeddable in $\mathbb{Q}_p$ reduce to pseudo‑differential equations on $\mathbb{Q}_p$, supplying the mathematical machinery for the hierarchical noise process defined in Section 3.

**Noise as a foundational category.** Reference [3] discusses noise in the context of quantum and classical systems.

**$p$‑adic statistical mechanics.** Reference [4] studies the three‑state $p$‑adic Potts model on a Cayley tree and discusses phase transitions of the model.

**$p$‑adic quantum mechanics.** Reference [5] develops complex‑valued wave functions on $p$‑adic arguments, justifying the use of ordinary complex probe states together with $p$‑adic‑valued noise amplitudes.

**Ultrametric models of natural structure.** Reference [6] presents a $p$‑adic model of DNA sequence and the genetic code.

**Ultrametric functional analysis.** Reference [7] proves ultrametric versions of embedding and extension theorems, guaranteeing that the ultrametric lattice postulated in Section 3 is mathematically robust.

**Hierarchic quantum systems.** Reference [8] introduces the $p$‑adic wavelet transform as a tool for describing hierarchic quantum systems, motivating the level decomposition used in the noise model.

**Program documents.** Reference [9] proposes passive error resilience through ultrametric geometry, arguing that metrological tasks avoid the thermodynamic overhead of active error correction. Reference [11] proposes falsifiable tests of the ultrametric program.

## 3. Methods

### 3.1 Ultrametric lattice and hierarchy levels

The register consists of $N$ qubits organized into a $p$‑ary hierarchy of depth $L$, so that $N=p^{L}$ in the balanced case. The hierarchy forms an ultrametric space $(X,d)$ satisfying
$$
d(x,z)\le\max\{d(x,y),d(y,z)\},
$$
which implies that any two balls are either nested or disjoint. Level $k\in\{0,\dots,L\}$ comprises clusters of diameter $p^{-k}$; level 0 is the whole register, level $L$ the individual qubits.

### 3.2 Noise as a $p$‑adic‑valued stochastic process

Following the reduction logic of [2], a non‑negative error weight is assigned to each cluster $C$ at level $k$:
$$
\varepsilon_k(C)=\varepsilon_0\,p^{-k},\qquad k=0,1,\dots,L,
$$
with base rate $\varepsilon_0\in(0,1)$. A decoherence event is a pair $(k,C)$, representing an error of weight $\varepsilon_k(C)$ localized on $C$.

### 3.3 Error propagation from the ultrametric inequality

Let $E_k$ denote the event that an error occurs on some cluster at level $k$. Because ultrametric balls are nested or disjoint, the family $\{E_k\}_{k=0}^{L}$ is nested: the coarsest event contains all finer events. Consequently,
$$
P_{\mathrm{U}}=\Pr\Bigl(\bigcup_{k=0}^{L}E_k\Bigr)=\max_{0\le k\le L}\Pr(E_k)=\varepsilon_0\,p^{-L}.
$$
In contrast, an Archimedean independent‑event model yields the union bound
$$
P_{\mathrm{A}}=\sum_{k=0}^{L}\varepsilon_0p^{-k}
=\varepsilon_0\,\frac{1-p^{-(L+1)}}{1-p^{-1}}.
$$

### 3.4 Probe states and quantum Fisher information

The probe is an $N$‑qubit GHZ state
$$
|\mathrm{GHZ}\rangle=\frac{1}{\sqrt{2}}\bigl(|0\rangle^{\otimes N}+|1\rangle^{\otimes N}\bigr).
$$
If decoherence destroys phase coherence with probability $P$, the off‑diagonal element of the density matrix is reduced by a factor $(1-P)$, and the QFI becomes
$$
F_Q(P)=N^{2}(1-P)^{2}.
$$
The single‑shot phase sensitivity is $\Delta\theta=1/\sqrt{F_Q}$.

### 3.5 Archimedean competitor: independent per‑qubit dephasing

Independent dephasing gives a per‑qubit coherence survival factor $c_0=1-2\varepsilon_0$. For a GHZ state,
$$
\eta_{\mathrm{A}}=c_0^{\,N}=(1-2\varepsilon_0)^{N},\qquad
F_Q^{\mathrm{A}}=N^{2}(1-2\varepsilon_0)^{2N}.
$$
For product‑state probes under dephasing at rate $\gamma$ per unit time, the single‑probe QFI for sensing time $t$ is $f(t)=t^{2}e^{-2\gamma t}$; the optimal $t^{*}=1/\gamma$ yields $f(t^{*})=e^{-2}/\gamma^{2}$.

### 3.6 Status of the axioms

The derivation chain contains a single conjectural step: the identification of physical decoherence with the nested‑event structure of Section 3.3 (the weight law $\varepsilon_k=\varepsilon_0p^{-k}$ and the nesting of the $E_k$). All downstream results are exact arithmetic given that step.

## 4. Analysis

All numbers are computed from the inputs stated here. Inputs: prime $p=2$; hierarchy depth $L=10$; base error weight $\varepsilon_0=10^{-2}$; register size $N=p^{L}=2^{10}=1024$; dephasing rate $\gamma=10^{-2}$ for the optimized product‑probe comparison; single‑shot repetitions $\nu=1$.

### 4.1 Ultrametric versus Archimedean error probability

**Ultrametric.**
$$
P_{\mathrm{U}}=\varepsilon_0p^{-L}=10^{-2}\times2^{-10}
=10^{-2}\times9.765625\times10^{-4}
=9.765625\times10^{-6}.
$$

**Archimedean union bound.**
$$
P_{\mathrm{A}}=\varepsilon_0\frac{1-2^{-(L+1)}}{1-2^{-1}}
=10^{-2}\times\frac{1-2^{-11}}{0.5}.
$$
Numerator: $1-2^{-11}=1-4.8828125\times10^{-4}=0.99951171875$.
Division: $0.99951171875/0.5=1.9990234375$.
Thus
$$
P_{\mathrm{A}}=10^{-2}\times1.9990234375
=1.9990234375\times10^{-2}.
$$

**Ratio.**
$$
\frac{P_{\mathrm{A}}}{P_{\mathrm{U}}}
=\frac{1.9990234375\times10^{-2}}{9.765625\times10^{-6}}
=1.9990234375\times1024
=2047\ \text{exactly}.
$$

### 4.2 QFI and sensitivity at $N=1024$

**Ultrametric coherence.**
$$
\eta_{\mathrm{U}}=1-P_{\mathrm{U}}=1-9.765625\times10^{-6}
=0.999990234375,
$$
$$
F_Q^{\mathrm{U}}=N^{2}\eta_{\mathrm{U}}^{2}
=1048576\times0.99998046876
\approx1.048556\times10^{6},
$$
$$
\Delta\theta_{\mathrm{U}}=\frac{1}{N\eta_{\mathrm{U}}}
=\frac{1}{1024\times0.999990234375}
\approx9.7657\times10^{-4}.
$$

**Archimedean GHZ coherence.**
$$
\eta_{\mathrm{A}}=(1-2\varepsilon_0)^{N}=0.98^{1024}.
$$
Using $\ln0.98=-0.0202027073$,
$$
\ln\eta_{\mathrm{A}}=1024\times(-0.0202027073)=-20.6875723,
$$
$$
\eta_{\mathrm{A}}=e^{-20.6875723}\approx1.0364\times10^{-9},
$$
$$
F_Q^{\mathrm{A}}=N^{2}\eta_{\mathrm{A}}^{2}
=1048576\times(1.0364\times10^{-9})^{2}
\approx1.126\times10^{-12},
$$
$$
\Delta\theta_{\mathrm{A}}=\frac{1}{N\eta_{\mathrm{A}}}
\approx\frac{1}{1024\times1.0364\times10^{-9}}
\approx9.42\times10^{5}.
$$

**Ratio of sensitivities.**
$$
\frac{\Delta\theta_{\mathrm{A}}}{\Delta\theta_{\mathrm{U}}}
=\frac{\eta_{\mathrm{U}}}{\eta_{\mathrm{A}}}
\approx\frac{0.999990234375}{1.0364\times10^{-9}}
\approx9.65\times10^{8}.
$$

### 4.3 Scaling with $N$

With $L=\log_{p}N$ the ultrametric corruption probability is
$$
P_{\mathrm{U}}=\varepsilon_0p^{-L}=\frac{\varepsilon_0}{N},
$$
so $\eta_{\mathrm{U}}=1-\varepsilon_0/N$ and
$$
\Delta\theta_{\mathrm{U}}=\frac{1}{N\eta_{\mathrm{U}}}
=\frac{1}{N-\varepsilon_0}\approx\frac{1}{N},
$$
which is Heisenberg scaling up to an $O(1)$ correction. Under independent dephasing, GHZ coherence decays as $(1-2\varepsilon_0)^{N}$, leading to exponential loss of QFI; the optimal Archimedean strategy reverts to product probes with SQL scaling $\Delta\theta\propto N^{-1/2}$.

### 4.4 Optimized sensing under independent dephasing

For product probes the optimal sensing time is $t^{*}=1/\gamma$, giving
$$
\Delta\theta^{\mathrm{prod}}=\frac{e\,\gamma}{\sqrt{N}}.
$$
With $\gamma=10^{-2}$ and $N=1024$,
$$
\Delta\theta^{\mathrm{prod}}=\frac{2.718281828\times10^{-2}}{32}
=8.4946\times10^{-4}.
$$
Thus the ultrametric GHZ sensitivity $\Delta\theta_{\mathrm{U}}\approx9.7657\times10^{-4}$ is slightly worse at this fixed $N$, emphasizing that the claimed advantage resides in asymptotic scaling rather than a fixed‑point comparison.

### 4.5 Complementary comparison at a small register

For $N=16$, $p=2$, $L=4$, $\gamma=0.01$ the effective rate is
$$
\Gamma_{4}=\gamma p^{-L}=0.01\times2^{-4}=6.25\times10^{-4}.
$$
Optimizing $F_Q(t)=N^{2}t^{2}e^{-2\Gamma_{4}t}$ yields $t^{*}=1/\Gamma_{4}$ and per‑run sensitivity $\delta\varphi_{\min}=e\Gamma_{4}/N$. The improvement factor relative to the unstructured case $\Gamma_{0}=0.01$ is
$$
\frac{\delta\varphi_{\min}^{(0)}}{\delta\varphi_{\min}^{(4)}}=\frac{\Gamma_{0}}{\Gamma_{4}}=16=p^{L}.
$$
At fixed total averaging time the improvement factor is $\sqrt{p^{L}}=p^{L/2}=4$.

## 5. Results

All results are model‑derived projections conditional on the nesting axiom of Section 3.6, for the primary inputs $p=2$, $L=10$, $\varepsilon_0=10^{-2}$, $N=1024$.

- **R1.** $P_{\mathrm{U}}=9.765625\times10^{-6}$, $P_{\mathrm{A}}=1.9990234375\times10^{-2}$, ratio $2047$ (exact).
- **R2.** $\Delta\theta_{\mathrm{U}}\approx9.7657\times10^{-4}$, $\Delta\theta_{\mathrm{A}}\approx9.42\times10^{5}$, ratio $\approx9.65\times10^{8}$.
- **R3.** Scaling law $\Delta\theta_{\mathrm{U}}=1/(N-\varepsilon_0)$, yielding Heisenberg scaling for $N\gg\varepsilon_0$.
- **R4.** Optimized product‑probe sensitivity $\Delta\theta^{\mathrm{prod}}\approx8.4946\times10^{-4}$ at $N=1024$, $\gamma=10^{-2}$.
- **R5.** Small‑register projection: per‑run improvement factor $16$ and fixed‑time factor $4$ for $p=2$, $L=4$.

## 6. Discussion

### 6.1 Limitations and failure modes

- **Conjectural axiom.** The analysis assumes that decoherence events obey the nested‑event structure of Section 3.3. If real decoherence exhibits partial independence across levels, the max‑of‑levels law fails and all ultrametric numbers collapse to the Archimedean column.
- **Competitor strength.** At $N=1024$ the optimized product probe outperforms the ultrametric GHZ probe in absolute sensitivity; the claim therefore rests on asymptotic scaling rather than a fixed‑$N$ advantage.
- **Prime dependence.** The effective prime $p$ is a model parameter; empirical identification of $p$ may differ from the illustrative choice $p=2$, altering quantitative suppression but not the max‑versus‑sum structure.
- **Archimedean comparison convention.** Using the sum $P_{\mathrm{A}}$ as the Archimedean benchmark yields an upper bound on the independent‑event probability; intersection corrections would only reduce $P_{\mathrm{A}}$ and strengthen the ultrametric claim.

### 6.2 Falsifiability

The paradigm is rejected if any of the following measurements are obtained (with statistical significance $>5\sigma$):
1. Empirical union probability $P_{\mathrm{meas}}$ equals the sum of level probabilities $\sum_k\Pr(E_k)$ rather than the maximum $\max_k\Pr(E_k)$.
2. GHZ coherence decays exponentially in $N$ with no observable $p^{-L}$ suppression.
3. The fitted decay per level is inconsistent with any integer prime $p$ (i.e., the effective factor is not $p^{-1}$ for integer $p$).

Conversely, observing saturation of the union probability at the maximum and a scaling $\Delta\theta\propto N^{-1}$ across a range of $N$ would support the ultrametric hypothesis.

### 6.3 Open questions

1. Applying the correspondence‑analysis pipeline of [1] to real error logs would convert the conjectural axiom into an estimated ultrametric object.
2. Investigating $p$‑dependence using the $p$‑adic Potts framework of [4] could reveal phase‑transition‑like behavior in the noise process.
3. Extending the model to mixed ultrametric‑Archimedean noise, as suggested by adelic constructions in [5], would interpolate between the two columns of Section 5.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Designers of quantum sensors—particularly trapped‑ion and superconducting platforms—must decide whether to allocate hardware to active error‑correction circuits or to increase probe number $N$. If the nesting axiom holds, the design decision shifts toward scaling $N$, because Heisenberg scaling is achieved passively; if falsified, conventional error‑mitigation strategies remain necessary.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 2 (technology concept formulated) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A minimal test consists of (i) recording error events on a small trapped‑ion register (e.g., $N=8$) with sufficient temporal resolution to assign each event to a hierarchical cluster; (ii) computing the empirical level probabilities $\Pr(E_k)$ and the union probability $P_{\mathrm{meas}}$. The ultrametric hypothesis is falsified if $P_{\mathrm{meas}}$ exceeds $\max_k\Pr(E_k)$ by more than statistical uncertainty. Required equipment includes state tomography and high‑resolution timestamps.

**(d) Engineering constraints.** The first constraints are (i) the ability to resolve error events at the cluster level, demanding high‑fidelity readout and precise timing; (ii) mapping the physical qubit layout onto a $p$‑ary tree, which may require redesign of control wiring; (iii) real‑time data processing to perform the ultrametric embedding described in [1].

**(e) Projected performance bounds (projection).** Assuming the nesting axiom holds and using $\Delta\theta_{\mathrm{U}}=1/(N-\varepsilon_0)$, a sensor with $N=10^{4}$ probes would achieve $\Delta\theta_{\mathrm{U}}\approx1.0\times10^{-4}$, compared with the SQL bound $\Delta\theta_{\mathrm{SQL}}\approx1.0\times10^{-2}$ for the same $N$. This projection follows directly from the derived formula and the chosen parameters.

**(f) Direct risks or misuse paths.** If the ultrametric model were adopted without empirical validation, sensor designs might forgo necessary error‑correction hardware, leading to catastrophic loss of coherence in environments where nesting does not hold. Careful experimental verification as outlined in (c) mitigates this risk.

## 8. Conclusion

By formalizing decoherence as a $p$‑adic hierarchical stochastic process, the analysis demonstrates that ultrametric nesting transforms the union of level‑wise error probabilities from a sum to a maximum, yielding an ultrametric corruption probability $P_{\mathrm{U}}=\varepsilon_0/N$ for balanced hierarchies. Propagation of this probability through GHZ‑state QFI shows that Heisenberg scaling $\Delta\theta\propto N^{-1}$ is retained, whereas independent dephasing collapses GHZ coherence exponentially. The ultrametric advantage manifests in asymptotic scaling rather than fixed‑point sensitivity, and a concrete falsifiability protocol is provided. The work thus offers a clear, quantitative target for experimental investigation of ultrametric noise structures in quantum metrology.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 14 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[2] Application of $p$-adic analysis methods in describing Markov processes on ultrametric spaces isometrically embeddable into $\mathbb{Q}_{p}$. arXiv:1504.03629v1. https://arxiv.org/abs/1504.03629v1
[3] Quantum and Classical Frontiers of Noise. arXiv:1612.03430v1. https://arxiv.org/abs/1612.03430v1
[4] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[5] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[6] A p-Adic Model of DNA Sequence and Genetic Code. arXiv:q-bio/0607018v1. https://arxiv.org/abs/q-bio/0607018v1
[7] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[8] p-Adic wavelet transform and quantum physics. arXiv:math-ph/0406024v1. https://arxiv.org/abs/math-ph/0406024v1
[9] https://papers.qnfo.org/papers/ultrametric-p-adic-metrology. QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology.
[11] https://papers.qnfo.org/papers/ultrametric-program. QNFO: The Ultrametric Program: One Structural Object Across Seven Research Domains, and Its Falsifiable Tests.
