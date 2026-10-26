# Grounding block - source: rem-f268a80d-922a-4773-8c30-6df0353a0a21

## Research idea

Re-entry from 10.5281/zenodo.18515457: to instantiate a ‘Base State’ capable of hosting the Standard Model?

## Existing paper under revision (remediation only)

# The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms

## Abstract

We formalize the question of whether a single, explicitly constructible quantum object — a "Base State" — could serve as a substrate on which the structure of the Standard Model is hosted, rather than the Standard Model being assembled from particle-like primitives on a qubit-gate substrate. A Base State is defined as a normalized state (or density operator) in a finite-dimensional Hilbert space, equipped with a declared readout map and a declared symmetry group, such that every empirically accessible structure arises by preparation, measurement, and composition. We audit feasibility using the only quantitative hardware data in our source corpus: the Tianyan-287 superconducting processor (105 qubits; single-qubit gate fidelity $99.90\%$, two-qubit gate fidelity $99.56\%$, readout fidelity $98.7\%$). With full arithmetic we derive: per-operation error rates of $1.0\times10^{-3}$, $4.4\times10^{-3}$, and $1.3\times10^{-2}$; a two-qubit serial budget of at most 157 gates at $50\%$ aggregate fidelity (154 with one final readout); a full-register readout ceiling of $F_{\mathrm{ro}}\approx0.2532$; a representative 105-qubit circuit fidelity of $F_{\mathrm{circ}}\approx0.1467$; and a parameter count of $2^{106}-2\approx8.113\times10^{31}$ real numbers for a generic state, versus 105 bits to index a basis state. We propose a three-stage falsification protocol, state explicit falsifiers, and conclude that the Base State hypothesis is currently unfalsified but unconfirmed: the obstruction is quantitative, not a no-go in principle.

## 1. Introduction

The Standard Model of particle physics is conventionally presented as a list of particles and interactions on a background stage. A dissenting constructive tradition, represented in the supplied corpus by "Beyond the Qubit: Constructive Paradigms for Post-Particle Computation" [10], argues that the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto what is better described as relational, field-theoretic reality. If that critique is accepted even provisionally, the constructive question becomes: what minimal object could host Standard-Model-like structure without presupposing particles? We call this candidate object the **Base State**.

This paper does three things. First, it gives the Base State hypothesis a definition precise enough to be wrong: Section 3 states exactly what object counts as a Base State and what would count as hosting. Second, it performs an honest feasibility audit using only numbers supplied in the grounding material — the fidelities of the Tianyan-287 processor [2] — to determine whether current hardware could prepare and verify a candidate at the 100-qubit scale. Third, it proposes a falsification protocol in the spirit of the automata-learning literature, where a model is recovered from noisy, incomplete data by evidence-driven merging rather than by optimizing a numeric target [1], and in the spirit of the Falsification Pledge of the Manifesto for Honest Computation [12].

Our conclusions are negative in the short term and constructive in the long term. The parameter-counting and fidelity analyses of Section 4 show that (i) a generic 105-qubit state is unspecifiable in any practical sense, so a viable Base State must be highly structured; (ii) current readout fidelity alone caps whole-register verification fidelity near $0.25$; and (iii) a gate-circuit encoding of even a toy relational state space exhausts any plausible two-qubit budget. The hypothesis therefore survives as an open research program, not a result.

## 2. Background and Related Work

We review all twelve supplied works and their bearing on the Base State question.

**[1] Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms (arXiv:1707.09430v1).** This work presents an interactive version of an evidence-driven state-merging (EDSM) algorithm for learning variants of finite state automata, framing learning as recovering or reverse-engineering the model that generated noisy, incomplete, or imperfectly sampled data, with domain expertise injected by a human in the loop. This is directly relevant methodologically: inferring a Base State from measurement data is a model-recovery problem under noise, not a numeric optimization, and the ESDM pattern — merge states when evidence supports it, consult an oracle when it does not — is a template for how a candidate Base State's equivalence classes of measurement outcomes could be inferred.

**[2] Tianyan: Cloud services with quantum advantage (arXiv:2512.10504v2).** This work describes the Tianyan Quantum Cloud Platform, offering cloud services demonstrating quantum advantage capabilities with a Zuchongzhi 3.0-like superconducting processor; the cloud-accessible prototype Tianyan-287 features 105 qubits with single-qubit gate, two-qubit gate, and readout fidelities of $99.90\%$, $99.56\%$, and $98.7\%$, respectively. These are the only hardware performance numbers supplied in our grounding material, and Section 4 uses them as the quantitative basis of the feasibility audit.

**[3] Bell-state measurement and quantum teleportation using linear optics (arXiv:1304.1214v1).** This work reviews and compares Bell-state measurement and quantum teleportation schemes using linear optics with three resource types — two-photon pairs, entangled coherent states, and hybrid entangled states — and reports that perfect teleportation with linear optics is possible in principle based on a hybrid approach combining two-photon pairs and entangled coherent states. For the Base State program this matters because teleportation is the minimal operation by which a state prepared in one physical substrate could be transferred into another; the existence of in-principle perfect transfer with hybrid resources suggests that substrate-independence of a Base State is not obviously blocked at the level of principle.

**[4] Searching for Coherent States: From Origins to Quantum Gravity (arXiv:2003.11810v4).** This work discusses coherent states from three perspectives — Schrödinger's seminal approach, the experimental take of quantum optics, and theoretical developments in quantum gravity — as a comparative study intended to connect the approaches and serve pedagogical purposes. The supplied summary gives no further technical detail; we use it only to justify treating "coherent state" as a unifying object spanning microscopic and gravitational regimes, which is the span a Base State would need. We flag this as analogy, not identity.

**[5] A full circuit-based quantum algorithm for excited-states in quantum chemistry (arXiv:2112.14193v3).** This work proposes a non-variational, full circuit-based quantum algorithm for obtaining excited states, motivated by the role of excited-state determination in predicting and modeling chemical reactions and other physical processes beyond widely studied ground-state problems. The supplied summary truncates before the algorithm's performance claims. This supplies the constructive counterpart to our audit: if a Base State is to host dynamics, machinery for accessing excitations above it must be circuit-native rather than variational, and [5] shows such machinery is an active object of design.

**[6] Interaction of light and semiconductor can generate quantum states required for solid state quantum computing (arXiv:1811.09849v1).** This work investigates the generation of nonclassical states — entangled, steered, and others — in a physical system composed of light and a semiconductor, motivated by the observation that solid-state quantum computing proposals are extremely promising for room-temperature machines and would require in-built sources of nonclassical states. This addresses the preparation side of the Base State problem: the substrate must contain its own sources of the nonclassical states the program needs, not import them.

**[7] Unraveling the emergence of quantum state designs in systems with symmetry (arXiv:2402.08949v3).** This work studies quantum state designs — structures enabling efficient sampling of random quantum states, with applications from circuit design to black hole physics — and the open question of how symmetry, which is expected to reduce the randomness of a state, affects state designs; the summary indicates this remained unresolved. This is the closest technical analogue to our compression-gap argument in Section 4: a hostable Base State cannot be generic and must live in a symmetry-constrained, design-like family, and [7] confirms that the interplay of symmetry and design structure is an open research question rather than settled technology.

**[8] Quantum games and synchronicity (arXiv:2408.15444v4).** This work, in the flavour of categorical quantum mechanics, extends nonlocal games to allow quantum questions and answers, using quantum sets (special symmetric dagger Frobenius algebras) and the quantum functions of Musto, Reutter, and Verdon, with equations presented in a diagrammatic calculus for tensor categories. Dagger Frobenius algebras are the categorical encoding of compositional structure; this is the supplied formal language closest to a relational ontology of interaction, in which a Base State and its admissible interactions could be stated without committing to a particle ontology.

**[9] QNFO: Standard Model (https://papers.qnfo.org/papers/standard-model-critique/).** The supplied entry carries no summary text; only the title and identifier are available. We therefore use it only as the declared reference object for "the Standard Model" as the target structure to be hosted, and make no claim about its contents.

**[10] QNFO: Beyond the Qubit (https://papers.qnfo.org/papers/paper-beyond-the-qubit/).** The supplied summary states that this work is a companion to "The Qubit Delusion" (v1.1, https://papers.qnfo.org/papers/paper-the-qubit-delusion/), asks what comes next if the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto relational, field-theoretic reality — and strips quantum mechanics to its minimal ontological commitments. The Base State hypothesis of this paper is precisely an attempt to answer that "what comes next" question in a falsifiable form.

**[11] QNFO: EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE (https://papers.qnfo.org/papers/emergent-correlation-in-a-local-deterministic-universe/).** The supplied entry likewise carries no summary text; only the title and identifier are available. We rely on it only as a declared position in the emergence-of-correlation debate, without attributing any specific result to it.

**[12] QNFO: Manifesto for Honest Computation (https://papers.qnfo.org/papers/paper-manifesto-honest-computation/).** The supplied summary describes this work as Phase VI (Final Synthesis), containing 5 principles, a concrete portfolio, and the Falsification Pledge. This paper adopts that methodological stance: every claim below is either derived with shown arithmetic or explicitly labeled as a projection with stated assumptions, and Section 6 states what would falsify the program.

## 3. Methods

### 3.1 Definition of a Base State

Let $\mathcal{H}_N$ be a Hilbert space of dimension $D_N = 2^N$, spanned by a declared computational basis $\{|b\rangle\}_{b \in \{0,1\}^N}$. A **Base State candidate** is a pair

$$
\mathcal{B} = \left( |\psi_0\rangle \in \mathcal{H}_N,\; \mathcal{R}: \mathcal{H}_N \rightarrow \{0,1\}^N \right),
$$

where $|\psi_0\rangle$ is a normalized state vector (or, in the mixed generalization, a density operator $\rho_0$ with $\mathrm{Tr}(\rho_0) = 1$) and $\mathcal{R}$ is a declared readout map. Equivalently, in relational terms, the Base State is a labeled transition system $B = (S, \Sigma, \delta, \lambda, \mathcal{G})$ with states $S$, interaction alphabet $\Sigma$, transition function $\delta$, observable labeling $\lambda$, and symmetry group $\mathcal{G}$. We say $\mathcal{B}$ **hosts** a target structure $\mathcal{T}$ (here, nominally, the Standard Model, per [9]) if:

1. **Preparation**: $|\psi_0\rangle$ is preparable from a product initial state by a circuit of finite, stated depth.
2. **Verifiability**: there exists a measurement statistics test whose pass probability, under the hypothesis that the prepared state is $|\psi_0\rangle$, exceeds a declared threshold $\theta$, and whose pass probability under every state in a declared alternative set is below $\theta$.
3. **Compositional productivity**: admissible operations on $\mathcal{B}$ form a closed algebraic structure (in the categorical sense of objects and morphisms, as in [8]) rich enough to encode the interaction pattern of $\mathcal{T}$; minimally, $\mathcal{G}$ should contain a subgroup matching the gauge structure $SU(3)\times SU(2)\times U(1)$.

As pure arithmetic on Lie-algebra dimensions, $\dim SU(3) = 3^2 - 1 = 8$, $\dim SU(2) = 2^2 - 1 = 3$, $\dim U(1) = 1$, so the minimal gauge algebra has dimension $d_{\mathcal{G}} = 8 + 3 + 1 = 12$. This is a counting statement about the target symmetry, not a derivation of the Standard Model. Condition 3 is deliberately left programmatic; conditions 1 and 2 are auditable with hardware numbers, and Section 4 audits them.

### 3.2 Audit quantities

For a platform with single-qubit gate fidelity $F_1$, two-qubit gate fidelity $F_2$, and readout fidelity $F_r$ (all as reported in [2] for Tianyan-287), we model a circuit with $n_1$ single-qubit gates, $n_2$ two-qubit gates, and $n_r$ readout events by the independent-error product

$$
F_{\mathrm{circ}}(n_1, n_2, n_r) = F_1^{\,n_1}\, F_2^{\,n_2}\, F_r^{\,n_r},
$$

or, in log form,

$$
\ln F_{\mathrm{circ}} = n_1 \ln F_1 + n_2 \ln F_2 + n_r \ln F_r.
$$

This is a first-order model: it assumes errors are independent and multiplicative and ignores crosstalk, leakage, and correlated decay. It is conservative for our purposes because it can only overestimate fidelity when correlations are harmful; all circuit-level numbers below are therefore upper bounds on achievable fidelity. As a complementary per-operation summary (Appendix A, Divergence D1), we also report the arithmetic mean fidelity $\bar{F} = (F_1 + F_2 + F_r)/3$ and the three-step composite error $P_{\mathrm{err}} = 1 - F_1 F_2 F_r$.

### 3.3 Specifiability accounting

A pure state $|\psi\rangle \in \mathcal{H}_N$ is specified, up to normalization and global phase, by $2D_N - 2$ real numbers: $D_N$ complex amplitudes contribute $2D_N$ real numbers, normalization removes $1$, and the global phase removes $1$ more. We compare this against the $\log_2 D_N = N$ bits needed to index a single computational basis state, and against the design-family picture of [7], in which one samples structured states efficiently rather than writing them out.

### 3.4 Falsification protocol

Following the model-recovery stance of [1] and the Falsification Pledge of [12], the protocol is:

- **Stage P (Preparation)**: prepare a candidate $|\psi_0\rangle$ on the full register; record circuit depth and gate counts.
- **Stage V (Verification)**: run a statistics test with threshold $\theta = 0.5$; the candidate fails if the achievable $F_{\mathrm{circ}}$ budget falls below $\theta$.
- **Stage C (Composition)**: demonstrate one nontrivial closed composition (e.g., a teleportation-grade transfer as in [3]) out of the Base State.

## 4. Analysis

All hardware inputs in this section come from [2]: $N = 105$ qubits; $F_1 = 0.9990$; $F_2 = 0.9956$; $F_r = 0.987$. All other quantities are derived below with full arithmetic.

### 4.1 Per-operation error rates and per-operation summary

$$
\epsilon_1 = 1 - F_1 = 1 - 0.9990 = 1.0\times10^{-3},
$$
$$
\epsilon_2 = 1 - F_2 = 1 - 0.9956 = 4.4\times10^{-3},
$$
$$
\epsilon_r = 1 - F_r = 1 - 0.987 = 1.3\times10^{-2}.
$$

Ratios: $\epsilon_2/\epsilon_1 = 4.4\times10^{-3}/1.0\times10^{-3} = 4.4$; $\epsilon_r/\epsilon_1 = 1.3\times10^{-2}/1.0\times10^{-3} = 13$.

Per-operation summary (convention of Appendix A, D1): the sum of fidelities is $S = 0.9990 + 0.9956 + 0.9870 = 2.9816$, so

$$
\bar{F} = \frac{2.9816}{3} = 0.9938667\ldots \approx 99.39\%.
$$

The three-step composite: $0.9990 \times 0.9956 = 0.9946044$; $0.9946044 \times 0.9870 = 0.9816745428$; hence

$$
P_{\mathrm{err}} = 1 - 0.9816745428 = 0.0183254572 \approx 1.8325\%.
$$

Log-fidelities (natural log), used throughout:

$$
\ln F_1 = \ln(0.9990) \approx -1.0005\times10^{-3},
$$
$$
\ln F_2 = \ln(0.9956) \approx -4.4097\times10^{-3},
$$
$$
\ln F_r = \ln(0.987) \approx -1.30816\times10^{-2}.
$$

### 4.2 Hilbert-space dimension, parameter count, and the compression gap

Input: $N = 105$ [2]. Then

$$
D_{105} = 2^{105} = 2^{100}\cdot 2^{5} = 1.2676506\times10^{30}\times 32 = 4.0564819\times10^{31}.
$$

The number of real parameters needed to specify a generic pure state (Section 3.3) is

$$
2D_{105} - 2 = 2^{106} - 2 = 8.1129638\times10^{31} - 2 \approx 8.113\times10^{31}.
$$

Per qubit, this is $(2^{106}-2)/105 = 8.1129638\times10^{31}/105 \approx 7.7266\times10^{29}$ real numbers per qubit of register. By contrast, indexing one computational basis state costs $\log_2 D_{105} = 105$ bits. **Interpretation**: a Base State that is generic is unspecifiable by roughly thirty orders of magnitude. Any viable candidate must belong to a structured, efficiently parameterized family — exactly the regime that quantum state designs address [7], and exactly where the effect of symmetry on such families remains, per [7], an open question. Note that the register is large enough in *dimension* to embed any finite state space with $k \le 2^{105}$; the failure analyzed below is in *dynamics*, not capacity.

### 4.3 Two-qubit serial budget at $50\%$ aggregate fidelity

Setting $F_{\mathrm{circ}}(n,0) = F_2^{\,n} \ge 0.5$ and solving for $n$:

$$
n \le \frac{\ln 0.5}{\ln F_2} = \frac{-0.693147}{-4.4097\times10^{-3}} \approx 157.2.
$$

So a purely two-qubit-gate serial circuit on Tianyan-287 retains at least $50\%$ aggregate fidelity for at most $n = 157$ two-qubit gates. Including a single final readout, the budget tightens: $F_2^{\,n}\cdot 0.987 \ge 0.5$ gives $F_2^{\,n} \ge 0.5/0.987 = 0.506584$, so

$$
n \le \frac{\ln 0.506584}{-4.4097\times10^{-3}} = \frac{-0.680066}{-4.4097\times10^{-3}} \approx 154.2,
$$

i.e., $n = 154$ two-qubit gates with one final readout.

### 4.4 Readout-only ceiling for full-register verification

Any verification protocol that reads out all $N = 105$ qubits incurs at least $n_r = 105$ readout events. With no other operations ($n_1 = n_2 = 0$):

$$
\ln F_{\mathrm{ro}} = 105\times(-1.30816\times10^{-2}) = -1.37357,
$$
$$
F_{\mathrm{ro}} = e^{-1.37357} \approx 0.2532.
$$

Readout alone caps full-register verification fidelity at approximately $0.253$, far below the Stage V threshold $\theta = 0.5$. No candidate Base State on this platform can be verified on the full register at $\theta = 0.5$, regardless of how good the gates are. This is a structural bottleneck, not a gate-quality one. (This scenario assumes readout of all 105 qubits; the single-readout scenario of Section 4.3 is the contrasting convention — see Appendix A, D2.)

### 4.5 Representative full-register circuit

Consider a representative preparation circuit using all 105 qubits with $n_1 = 105$ single-qubit gates, $n_2 = 100$ two-qubit gates, and $n_r = 105$ readouts. Term by term:

$$
105\times(-1.0005\times10^{-3}) = -0.10505,
$$
$$
100\times(-4.4097\times10^{-3}) = -0.44097,
$$
$$
105\times(-1.30816\times10^{-2}) = -1.37357.
$$

Sum: $\ln F_{\mathrm{circ}} = -0.10505 - 0.44097 - 1.37357 = -1.91959$, so

$$
F_{\mathrm{circ}} = e^{-1.91959} \approx 0.1467.
$$

Cross-check in the fidelity domain: single-qubit gates alone $e^{-0.10505} \approx 0.9003$; two-qubit gates alone $e^{-0.44097} \approx 0.6434$; readout alone $e^{-1.37357} \approx 0.2532$; and $0.9003\times0.6434\times0.2532 \approx 0.1467$, confirming the log-domain computation.

### 4.6 Gate-budget headroom under ideal readout

To ask how large a circuit the gates alone could support at $\theta = 0.5$, set $n_r = 0$ and $n_1 = n_2 = n$:

$$
n(\ln F_1 + \ln F_2) = \ln 0.5 = -0.69315.
$$

Since $\ln F_1 + \ln F_2 = -1.0005\times10^{-3} - 4.4097\times10^{-3} = -5.4102\times10^{-3}$,

$$
n = \frac{-0.69315}{-5.4102\times10^{-3}} \approx 128.1,
$$

so approximately $n = 128$ combined gate layers could be tolerated at $\theta = 0.5$ if readout were perfect. Restoring real readout ($n_r = 105$) consumes log-budget $1.37357$, which exceeds the total budget $0.69315$ by a factor $1.37357/0.69315 \approx 1.98$: readout alone uses about $1.98$ times the entire $\theta = 0.5$ budget.

### 4.7 Cost of encoding a relational state space (toy model)

Suppose the Base State's relational state space $S$ has $|S| = k$ distinguishable configurations and out-degree $r$ (each state has $r$ outgoing edges), so the transition table has $k\cdot r$ edges. For a toy system with $k = 100$ and $r = 4$, that is $k\cdot r = 400$ edges; if a single coherent computation must touch a fraction $\phi$ of them with one two-qubit gate per edge, the budget of Section 4.3 requires

$$
\phi\cdot 400 \le 157 \quad\Rightarrow\quad \phi \le \frac{157}{400} = 0.3925.
$$

So even a 100-state toy relational system can have at most about $39\%$ of its transition structure touched per coherent circuit run before aggregate fidelity drops below $50\%$.

### 4.8 Projection: full-table circuit fidelity and required readout

**Projection 1** (labeled; assumptions: independent errors, no crosstalk, no state-preparation or idling error, serial compilation, one two-qubit gate per edge). A circuit touching the full 400-edge table needs aggregate fidelity $F_2^{400}$:

$$
\ln F_2^{400} = 400\times(-4.4097\times10^{-3}) = -1.76387,
$$
$$
F_2^{400} = e^{-1.76387} \approx 0.1714.
$$

Uncertainty bound: any additional per-gate error $\epsilon'$ shifts the exponent by $400\,\epsilon'$; e.g., $\epsilon' = 10^{-3}$ gives $e^{-1.76387-0.4} \approx 0.1148$. The projection is robust in concluding that a full-table circuit fails well below any useful threshold.

**Projection 2** (labeled; assumptions: $n_1 = 105$, $n_2 = 100$, $n_r = 105$, $F_1$ and $F_2$ as in [2], target $\theta = 0.5$). The required readout fidelity $F_r^{*}$ satisfies

$$
\ln F_r^{*} = \frac{\ln 0.5 - \ln F_1^{105} - \ln F_2^{100}}{105} = \frac{-0.69315 + 0.10505 + 0.44097}{105} = \frac{-0.14713}{105} = -1.4012\times10^{-3},
$$

$$
F_r^{*} = e^{-1.4012\times10^{-3}} \approx 0.99860.
$$

Full-register verification at $\theta = 0.5$ for this circuit class requires readout fidelity $\approx 0.9986$, versus the supplied $0.987$ [2] — a reduction of readout error from $1.3\times10^{-2}$ to $1.4\times10^{-3}$, a factor $1.3\times10^{-2}/1.4\times10^{-3} \approx 9.3$. This projection inherits the independence assumption; correlated errors would only raise the requirement, so $0.9986$ is a best-case figure.

## 5. Results

All numbers below are computed in Section 4 from the inputs of [2]; the two projections are labeled.

1. **Per-operation errors.** $\epsilon_1 = 1.0\times10^{-3}$, $\epsilon_2 = 4.4\times10^{-3}$, $\epsilon_r = 1.3\times10^{-2}$ (Section 4.1).
2. **Per-operation summary (convention D1).** $\bar{F} \approx 99.39\%$; three-step composite error $P_{\mathrm{err}} \approx 1.83\%$ (Section 4.1).
3. **Dimension and specifiability.** $D_{105} = 2^{105} \approx 4.056\times10^{31}$; a generic pure state requires $2^{106}-2 \approx 8.113\times10^{31}$ real parameters, i.e., $\approx 7.7266\times10^{29}$ per qubit, versus $105$ bits to index a basis state (Section 4.2). Any hostable Base State must be a structured, design-like state, not a generic one.
4. **Two-qubit serial budget.** At most $n = 157$ two-qubit gates at $\ge 50\%$ aggregate fidelity, or $n = 154$ with one final readout (Section 4.3).
5. **Readout ceiling.** Full-register readout of 105 qubits at $F_r = 0.987$ caps verification fidelity at $F_{\mathrm{ro}} \approx 0.2532$ (Section 4.4).
6. **Representative circuit.** With $n_1 = 105$, $n_2 = 100$, $n_r = 105$: $F_{\mathrm{circ}} \approx 0.1467$ (Section 4.5).
7. **Gate headroom.** With perfect readout, $\approx 128$ combined gate layers are tolerable at $\theta = 0.5$; with real readout, readout alone consumes $\approx 1.98\times$ the entire $\theta = 0.5$ budget (Section 4.6).
8. **Toy relational coverage.** For $k = 100$, $r = 4$: at most $\phi \le 0.3925$ of transition structure touched per coherent run (Section 4.7).
9. **Gauge dimension.** $d_{\mathcal{G}} = 12$ for $SU(3)\times SU(2)\times U(1)$ (Section 3.1).
10. **Projections (stated assumptions of Section 4.8).** Full-table circuit: $F_2^{400} \approx 0.1714$ (best case; $\approx 0.1148$ with $\epsilon' = 10^{-3}$). Required readout: $F_r^{*} \approx 0.9986$, a $\approx 9.3\times$ reduction in readout error.

**Fragment availability (qualitative, sourced).** Entanglement distribution without gate overhead: available in principle via hybrid linear-optical teleportation [3]. Coherent-state framing across scales: available as a unifying language [4]. Spectral excitation: available within circuit-based algorithms [5]. Nonclassical state sources: available for light–semiconductor systems [6]. Symmetric state designs: open problem [7]. Compositional categorical structure: available as formal language [8]. No supplied work combines two or more fragments.

**Status of the hypothesis.** Under the stated thresholds ($\theta = 0.5$) and the supplied hardware numbers of [2], the Base State hypothesis is currently **unfalsified but unconfirmed**: no supplied datum contradicts the possibility of a structured Base State hosting Standard-Model-like symmetry (Section 3.1), yet no current platform can prepare and verify even a toy candidate on the full register (Sections 4.4–4.6). The obstruction is quantitative, not a no-go in principle.

## 6. Discussion

**Limitations of the audit.** The fidelity model of Section 3.2 assumes independent, multiplicative errors and ignores crosstalk, leakage, idling decay, and state-preparation error. All circuit-level numbers ($F_{\mathrm{ro}} \approx 0.2532$, $F_{\mathrm{circ}} \approx 0.1467$, $F_2^{400} \approx 0.1714$) are therefore upper bounds under this model; real hardware would do worse, so the qualitative conclusions (readout bottleneck, budget exhaustion) are conservative, but the specific values should not be read as measurements.

**Convention dependence.** The per-operation summary $\bar{F} \approx 99.39\%$ and composite error $P_{\mathrm{err}} \approx 1.83\%$ (convention D1, Appendix A) are descriptive summaries, not inputs to any budget computation; the budgets use only the log-domain products. The single-readout budget of Section 4.3 ($n = 154$) and the full-register ceiling of Section 4.4 ($F_{\mathrm{ro}} \approx 0.2532$) answer different questions under convention D2 (Appendix A); neither contradicts the other.

**Falsifiers.** The program would be falsified if: (i) a structured, symmetry-constrained family were shown incapable of embedding a $d_{\mathcal{G}} = 12$ gauge algebra with the closure required by Section 3.1, Condition 3; (ii) readout fidelities were shown to be bounded well below the projected $F_r^{*} \approx 0.9986$ by a mechanism that no architectural change (e.g., repeated measurement, majority voting) can circumvent; or (iii) the model-recovery approach of [1] were shown to require sample complexity scaling with $D_{105}$ rather than with the structured family size, making verification of any candidate infeasible even with perfect gates.

**What would strengthen the claim.** Demonstrating any single closed composition (Stage C, e.g., a teleportation-grade transfer in the spirit of [3]) on a structured candidate state, or an experimental state-design family in the sense of [7] whose symmetry content is controlled, would move the hypothesis from unfalsified toward testable.

**Open questions.** How symmetry constrains state designs remains open per [7]; whether the categorical language of [8] can express the gauge structure $SU(3)\times SU(2)\times U(1)$ without particle ontology is untested here; and the excited-state machinery of [5] has not been adapted to Base State dynamics. The QNFO entries [9], [10], [11] supply position statements and target definitions but, per their supplied summaries (or lack thereof), no technical results that this audit could use.

## 7. Conclusion

We defined a Base State as a preparable, verifiable, compositionally closed quantum object and audited its feasibility on the only quantitative platform in the corpus, the Tianyan-287 [2]. The audit yields a compression gap of roughly thirty orders of magnitude between generic states and indexable states, a full-register readout ceiling $F_{\mathrm{ro}} \approx 0.2532$ against a verification threshold $\theta = 0.5$, a two-qubit serial budget of $157$ gates ($154$ with one readout), and a projected required readout fidelity $F_r^{*} \approx 0.9986$. None of these constitutes a no-go in principle; all are quantitative obstructions that improved hardware or architectural workarounds could in principle relax. We propose a three-stage falsification protocol and state explicit falsifiers. The Base State hypothesis stands as an open, falsifiable research program.

## References

[1] Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms. arXiv:1707.09430v1. https://arxiv.org/abs/1707.09430v1
[2] Tianyan: Cloud services with quantum advantage. arXiv:2512.10504v2. https://arxiv.org/abs/2512.10504v2
[3] Bell-state measurement and quantum teleportation using linear optics: two-photon pairs, entangled coherent states, and hybrid entanglement. arXiv:1304.1214v1. https://arxiv.org/abs/1304.1214v1
[4] Searching for Coherent States: From Origins to Quantum Gravity. arXiv:2003.11810v4. https://arxiv.org/abs/2003.11810v4
[5] A full circuit-based quantum algorithm for excited-states in quantum chemistry. arXiv:2112.14193v3. https://arxiv.org/abs/2112.14193v3
[6] Interaction of light and semiconductor can generate quantum states required for solid state quantum computing: Entangled, steered and other nonclassical states. arXiv:1811.09849v1. https://arxiv.org/abs/1811.09849v1
[7] Unraveling the emergence of quantum state designs in systems with symmetry. arXiv:2402.08949v3. https://arxiv.org/abs/2402.08949v3
[8] Quantum games and synchronicity. arXiv:2408.15444v4. https://arxiv.org/abs/2408.15444v4
[9] https://papers.qnfo.org/papers/standard-model-critique/. QNFO: Standard Model.
[10] https://papers.qnfo.org/papers/paper-beyond-the-qubit/. QNFO: Beyond the Qubit: Constructive Paradigms for Post-Particle Computation.
[11] https://papers.qnfo.org/papers/emergent-correlation-in-a-local-deterministic-universe/. QNFO: EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE.
[12] https://papers.qnfo.org/papers/paper-manifesto-honest-computation/. QNFO: Manifesto for Honest Computation.

## Appendix A. Divergence report

**D1 (per-operation summary convention).** One draft convention reports a per-operation arithmetic mean fidelity $\bar{F} = (F_1 + F_2 + F_r)/3 \approx 99.39\%$ and a three-step composite error $P_{\mathrm{err}} = 1 - F_1 F_2 F_r \approx 1.83\%$; the other convention reports only per-operation error rates $\epsilon_1 = 1.0\times10^{-3}$, $\epsilon_2 = 4.4\times10^{-3}$, $\epsilon_r = 1.3\times10^{-2}$. The disagreement is one of descriptive summary versus per-operation granularity, not of substance. Resolution: the main text reports both, clearly labeled as convention D1, and uses neither in any budget computation; all budgets use the log-domain product model of Section 3.2.

**D2 (readout convention).** One draft convention budgets a single final readout event (yielding the $n = 154$ two-qubit-gate budget of Section 4.3); the other budgets full-register readout of all $N = 105$ qubits (yielding the ceiling $F_{\mathrm{ro}} \approx 0.2532$ of Section 4.4). The disagreement is about which verification scenario is representative: single-observable tests versus whole-register statistics tests. Resolution: the main text presents both scenarios explicitly labeled, and notes in Section 4.4 that the full-register scenario is the binding constraint for Stage V verification at $\theta = 0.5$.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Per-operation errors $\epsilon_1 = 1.0\times10^{-3}$, $\epsilon_2 = 4.4\times10^{-3}$, $\epsilon_r = 1.3\times10^{-2}$ from [2] | A, B, C | CONVERGENT |
| C2: Per-operation summary $\bar{F} \approx 99.39\%$, $P_{\mathrm{err}} \approx 1.83\%$ (convention D1) | A, B | CONVERGENT |
| C3: $D_{105} = 2^{105} \approx 4.056\times10^{31}$; generic state needs $2^{106}-2 \approx 8.113\times10^{31}$ reals | A, B, C | CONVERGENT |
| C4: Two-qubit serial budget $n = 157$ ($154$ with one readout) | A, B, C | CONVERGENT |
| C5: Full-register readout ceiling $F_{\mathrm{ro}} \approx 0.2532$ | A, B, C | CONVERGENT |
| C6: Representative circuit $F_{\mathrm{circ}} \approx 0.1467$ for $n_1 = 105$, $n_2 = 100$, $n_r = 105$ | A, B | CONVERGENT |
| C7: Gate headroom $\approx 128$ layers with perfect readout; readout uses $\approx 1.98\times$ the $\theta = 0.5$ budget | A, C | CONVERGENT |
| C8: Toy relational coverage $\phi \le 0.3925$ for $k = 100$, $r = 4$ | B, C | CONVERGENT |
| C9: Gauge dimension $d_{\mathcal{G}} = 12$ | A, B, C | CONVERGENT |
| C10: Projections $F_2^{400} \approx 0.1714$ and $F_r^{*} \approx 0.9986$ with stated assumptions | A, B, C | CONVERGENT |
| C11: Single-readout budget is the representative verification scenario | B | SINGLE (resolved as D2: both scenarios reported) |
| C12: Per-operation mean is the primary fidelity summary | A | SINGLE (resolved as D1: both summaries reported, neither used in budgets) |

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1707.09430v1 | Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms
arXiv:hep-ph/0304186v1 | Structure of the Standard Model
arXiv:1905.12567v3 | MQLV: Optimal Policy of Money Management in Retail Banking with Q-Learning
arXiv:2108.10071v3 | Elysium: Context-Aware Bytecode-Level Patching to Automatically Heal Vulnerable Smart Contracts
arXiv:1303.0045v2 | The Mesh of Civilizations and International Email Flows
arXiv:2401.07398v2 | Cross Domain Early Crop Mapping using CropSTGAN
arXiv:1611.07100v2 | Interpreting Finite Automata for Sequential Data
arXiv:2005.12156v2 | ConFuzzius: A Data Dependency-Aware Hybrid Fuzzer for Smart Contracts

## QNFO corpus context (Vectorize)

QNFO: The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms | https://papers.qnfo.org/papers/the-base-state-hypothesis-a-falsification-protocol-for-a-substrate-capable-of-ho
QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics | https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis
QNFO: Base State–Disturbance (BS-D) Ontology | https://papers.qnfo.org/papers/base-statedisturbance-bs-d-ontology
QNFO: Standard Model | https://papers.qnfo.org/papers/standard-model-critique

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1707.09430v1 | Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms
  We present an interactive version of an evidence-driven state-merging (EDSM) algorithm for learning variants of finite state automata. Learning these automata often amounts to recovering or reverse engineering the model generating the data despite noisy, incomplete, or imperfectly sampled data sources rather than optimizing a purely numeric target function. Domain expertise and human knowledge abo
  Full text (https://arxiv.org/html/1707.09430v1), excerpts of its own sections:
  § 1 Introduction: Automata, and finite state machines in particular, have long been a formal model used in computer science to designing software and analyzing computer systems themselves  ( Lee & Yannakakis, 1996 ) . Our knowledge about automata models comes from different source: Firstly, we have studied formal systems in detail and understand them as algebraic systems we can pose decision problems about. Secondly, we have experience lots experience applying them as a model language. In learning, these tasks are done inversely to recover, reverse-engineer, or understand an unknown data source, typically a communication protocol or software controller. The automata models themselves are also seen as suitable to gain epistemic insight into the system of interest ( Hammerschmidt et al., 2016 ; Vaandrager, 2017 ) for humans beyond learning models that minimize a given error function, or are used in model checkers for formal analysis. And while we understand the theory of learning automata fairly well, e.g. [...]
  § 2.1 Automata Models and Finite Automata: The models we consider are variants of deterministic finite state automata, or finite state machines. We provide a conceptual introduction here, and refer to literature for a thorough introduction ( Hopcroft et al., 2013 ) . An automaton consists of a set of states, connected by transitions labeled over an alphabet. There is a special start-state where all computations begin, and and a set of final states where computation ends. It is said to accept a word (string) over the alphabet in a computation if there exists a path of transitions from a predefined start state to one of the predefined final states, using transitions labeled with the letters of the word. Automata are called deterministic when there exists exactly one such path for every possible string. Probabilistic automata include probability values on transitions and compute word probabilities using the product of these values along a path, similar to hidden Markov models, rather than having final states. A Mealy machine is a deterministic finite automata that produces an output at each step.
  § 2.2 Learning Approaches: Learning automata models, and in particular finite state machines, has long been of interest in the field of grammar induction. While the problem can be solved exactly (see  ( Heule & Verwer, 2012 ) ), it is NP-complete. There are two main classes of learning approaches: active learning and passive learning approaches. [...]
  § 4 Conclusion & Future Work: Our experience indicates that a hybrid mode between manual and fully automatic decision is most useful: Especially in cases of large training files (and therefore large initial models which are hard to use visually), automating all decisions until a specific criterion is met (e.g. the best proposed score is below a given threshold, or $n$ merges are executed) takes some burden off the human domain expert while still allowing intervention when necessary. By following the suggestions of the heuristic, the expert can retain learnability guarantees from batch learning algorithms. We have not yet conducted a (formal) analysis to quantify the benefits of interactivity in terms of convergence speed. In Lambeau et al. (2008) , the authors experimentally showcase the positive effect of mandatory merge constraints. Similar information, and thus benefits, are provided by the interaction proposed here. Domain expert can implicitly act as a teacher or oracle active learning, bringing together elements from both active and passive learning approaches to automata.
[2] arXiv:hep-ph/0304186v1 | Structure of the Standard Model
  The structure of the standard model is concisely summarized, including the standard model Lagrangian, spontaneous symmetry breaking, the reexpression of the Lagrangian in terms of mass eigenstates after symmetry breaking, and the gauge interactions. The problems of the standard model are described.
  Full text (https://arxiv.org/html/hep-ph/0304186v1), excerpts of its own sections:
  § 1 The Standard Model Lagrangian: The standard model  [ 2 ] is a gauge theory  [ 3 ] of the microscopic interactions. The strong interaction part (QCD  [ 4 ] ) is described by the Lagrangian ${\cal L}_{SU_{3}}=-\frac{1}{4}F^{i}_{\mu\nu}F^{i\mu\nu}+\sum_{r}\bar{q}_{r\alpha}i\not{\!\!D}^{\alpha}_{\beta}\,q^{\beta}_{r},$ (1) where $g_{s}$ is the QCD gauge coupling constant, $F^{i}_{\mu\nu}=\partial_{\mu}G^{i}_{\nu}-\partial_{\nu}G^{i}_{\mu}-g_{s}f_{ijk}\;G_{\mu}^{j}\;G_{\nu}^{k}$ (2) is the field strength tensor for the gluon fields $G^{i}_{\mu},\;i=1,\cdots,8$ , and the structure constants $f_{ijk}$ $(i,j,k=1,\cdots,8)$ are defined by $[\lambda^{i},\lambda^{j}]=2if_{ijk}\lambda^{k},$ (3) where the $SU_{3}$ $\lambda$ matrices are defined in Table  1 . The $F^{2}$ term leads to three and four-point gluon self-interactions. [...]
  § 2 Spontaneous Symmetry Breaking: Gauge invariance (and therefore renormalizability) does not allow mass terms in the Lagrangian for the gauge bosons or for chiral fermions. Massless gauge bosons are not acceptable for the weak interactions, which are known to be short-ranged. Hence, the gauge invariance must be broken spontaneously  [ 6 ] , which preserves the renormalizability  [ 7 ] . The idea is simply that the lowest energy (vacuum) state does not respect the gauge symmetry and induces effective masses for particles propagating through it. Let us introduce the complex vector $v=\langle 0|\varphi|0\rangle={\rm constant},$ (15) which has components that are the vacuum expectation values of the various complex scalar fields. $v$ is determined by rewriting the Higgs potential as a function of $v$ , $V(\varphi)\rightarrow V(v)$ , and choosing $v$ such that $V$ is minimized. That is, we interpret $v$ as the lowest energy solution of the classical equation of motion 2 2 2 It suffices to consider constant $v$ because any space or time dependence $\partial_{\mu}v$ would increase the energy of the solution. [...]
  § 3 The Gauge Interactions: The major quantitative tests of the electroweak standard model involve the gauge interactions of fermions and the properties of the gauge bosons. The charged current weak interactions of the Fermi theory and its extension to the intermediate vector boson theory are incorporated into the standard model, as is quantum electrodynamics. The theory successfully predicted the existence and properties of the weak neutral current. Here I will summarize the structure of the interactions. Later chapters will discuss the phenomenology and tests in more detail.
  § 3.1 The Charged Current: The interaction of the $W$ bosons to fermions is given by $L=-\frac{g}{2\sqrt{2}}\left(J^{\mu}_{W}W^{-}_{\mu}+J^{\mu{\dagger}}_{W}W^{+}_{\mu}\right),$ (42) where the weak charge-raising current is $\displaystyle J_{W}^{\mu{\dagger}}$ $\displaystyle=$ $\displaystyle\sum^{F}_{m=1}\left[\bar{\nu}_{m}^{0}\gamma^{\mu}(1-\gamma^{5})e^{0}_{m}+\bar{u}_{m}^{0}\gamma^{\mu}(1-\gamma^{5})d^{0}_{m}\right]$ (43) $\displaystyle=$ $\displaystyle(\bar{\nu}_{e}\bar{\nu}_{\mu}\bar{\nu}_{\tau})\gamma^{\mu}(1-\gamma^{5})\left(\begin{array}[]{c}e^{-}\\ \mu^{-}\\ \tau^{-}\end{array}\right)+(\bar{u}\;\bar{c}\;\bar{t})\gamma^{\mu}(1-\gamma^{5})V\left(\begin{array}[]{c}d\\ s\\ b\end{array}\right).$ $J^{\mu{\dagger}}_{W}$ has a $V-A$ form, i.e., it violates parity and charge conjugation maximally. The mismatch between the unitary transformations relating the weak and mass eigenstates for the up and down-type quarks leads to the presence of the $F\times F$ unitary matrix $V=A^{u{\dagger}}_{L}A^{d}_{L}$ in the current. [...]
[3] arXiv:1905.12567v3 | MQLV: Optimal Policy of Money Management in Retail Banking with Q-Learning
  Reinforcement learning has become one of the best approach to train a computer game emulator capable of human level performance. In a reinforcement learning approach, an optimal value function is learned across a set of actions, or decisions, that leads to a set of states giving different rewards, with the objective to maximize the overall reward. A policy assigns to each state-action pairs an exp
  Full text (https://arxiv.org/html/1905.12567v3), excerpts of its own sections:
  § 1 Introduction: A major goal of the reinforcement learning (RL) and Machine Learning (ML) community is to build efficient representations of the current environment to solve complex tasks. In RL, an agent relies on multiple sensory inputs and past experience to derive a set of plausible actions to solve a new situation [ 1 ] . While the initial idea around RL is not new [ 2 , 3 , 4 ] , significant progress has been achieved recently by combining neural networks and Deep Learning (DL) with RL. The progress of DL [ 5 , 6 ] has allowed the development of a novel agent combining RL with a class of deep artificial neural networks [ 1 , 7 ] resulting in Deep Q Network (DQN). The Q refers to the Q-learning algorithm introduced in [ 8 ] . It is an incremental method that successively improves its evaluations of the quality of the state-action pairs. The DQN approach achieves human level performance on Atari video games using unprocessed pixels as inputs. [...]
  § 2 Background: We define $A_{t}\in\mathcal{A}$ the action taken at time $t$ for a given state $X_{t}\in\mathcal{X}$ and the immediate reward by $R_{t+1}$ . The ongoing state is denoted by $X_{t}\in\mathcal{X}$ and the stochastic diffusion process by $S_{t}\in\mathcal{S}$ at time $t$ . The discount factor that trades off the importance of immediate and later rewards is expressed by $\gamma\in[0;1]$ . We recall a policy is a mapping from states to probabilities of selecting each possible action [ 17 ] . [...]
  § 4 Experiments: We empirically evaluate the performance of MQLV. We initially highlight the similarities between historical payment transactions and Vasicek generated transactions. We then underline the MQLV’s capabilities to learn the optimal policy of money management based on the estimation of future event probabilities in comparison to the closed formula of [ 12 , 13 ] , hereinafter denoted by BSM’s closed formula. We rely on synthetic data sets because of the privacy and the confidentiality issues of the retail banking data sets. Data Availability and Data Description One of our contributions is to bring a RL framework designed for retail banking. However, none of the data sets can be released publicly because of the highly sensitive information they contain. We therefore show the similarities between a small sample of anonymized transactions and Vasicek generated transactions [ 16 ] . We then use the Vasicek mean reverting stochastic diffusion process to generate larger synthetic data sets similar to the original retail banking data sets. [...]
  § 6 Conclusion: We introduced Modified Q-Learning for Vasicek or MQLV, a new model-free and off-policy reinforcement learning approach capable of evaluating an optimal policy of money management based on the aggregated transactions of the clients. MQLV is part of a banking strategy that looks to minimize the customer churn by including more transparency and more personalization in the decision process related to bank loan applications or credit card limits. It relies on a digital function, a Heaviside step function expressed in its discrete form, to estimate the future probability of an event such as a payment default. We discuss its relation with the Bellman optimality equation and the Q-learning update. We conducted experiments on synthetic data sets because of the privacy and confidentiality issues related to the retail banking data sets. The generated data sets followed a mean reverting stochastic diffusion process, the Vasicek model, simulating retail banking data sets such as transaction payments. [...]
[4] arXiv:2108.10071v3 | Elysium: Context-Aware Bytecode-Level Patching to Automatically Heal Vulnerable Smart Contracts
  Fixing bugs is easiest by patching source code. However, source code is not always available: only 0.3% of the ~49M smart contracts that are currently deployed on Ethereum have their source code publicly available. Moreover, since contracts may call functions from other contracts, security flaws in closed-source contracts may affect open-source contracts as well. However, current state-of-the-art 
  Full text (https://arxiv.org/html/2108.10071v3), excerpts of its own sections:
  § 1. Introduction: Ideally, bugs in programs should be repaired by simply patching the source code. However, in some cases, the original source code may not be available. [...]
  § 5. Evaluation: In this section, we evaluate Elysium by measuring its effectiveness (RQ1), correctness (RQ2), and costs (RQ3).
  § 5.1. Experimental Setup: Baselines. We compare Elysium to the tools listed in Table  3 . Most tools, including Elysium , have their bug localization outsourced, meaning that they leverage existing security analysis tools to detect and localize bugs. sGuard is the only tool that leverages its own bug localization. While Elysium , EVMPatch , and SmartShield insert their patches at the bytecode level, other tools such as SCRepair and sGuard insert their patches at the source code level. Almost all tools, except for SCRepair , use a template-based approach to introduce their patches. However, some tools such as Elysium , SmartShield , and sGuard use a combination of template-based and semantic-aware patching. The source code of EVMPatch is not publicly available. Nonetheless, the authors released a public dataset with their results for comparison ( UDE Secure Software System Research Group, 2020 ) . SmartShield is only available upon request. While the source code of SCRepair is publicly available, we did not manage to compile it. [...]
  § 5.2. Experimental Results: RQ1: Effectiveness. We first measure the effectiveness of Elysium and the other tools on the SmartBugs dataset. The dataset only consists of annotated contracts and does not contain attacking nor benign transactions. We therefore first run the bug-finding tools (i.e.,  Osiris , Oyente , and Mythril ) on the contracts and match the reported bugs with the annotated bugs. The overlap marks the validated ground truth (see overlap column in Table  5 ). From the 149 annotated bugs, only 79 overlap with the bugs detected by the bug-finding tools. Moreover, 5 false positives have been reported by the bug-finding tools. Next, we patch the contracts by running the patching tools and rerunning the bug-finding tools on the patched version returned by each patching tool, and mark a bug as successfully patched if the bug-finding tool does not report the bug anymore. Table  7 shows that Elysium is able to patch all 79 bugs, whereas SmartShield and sGuard can only patch 45 and 33, respectively. We see that SmartShield has issues in patching reentrancy. [...]
  § 7. Conclusion: In this work, we presented Elysium , a tool to automatically patch smart contracts using context-related information that is inferred at the bytecode level. Elysium is currently able to patch 7 types of vulnerabilities. It can easily be extended by adding further vulnerability detectors and by writing new patch templates using our custom DSL. We compared Elysium to existing tools by patching almost 2,000 smart contracts and replaying more than 500K transactions. Our results show that Elysium is able to effectively and correctly patch at least 30% more contracts than existing tools. Moreover, when compared to existing tools, the resulting transaction overhead is reduced by up to a factor of 1.7. We leave it to future work, to further optimize the overhead in terms of deployment costs. Acknowledgements. We would like to thank our anonymous reviewers and our shepherd Kevin Roundy for their valuable comments and feedback. [...]
[5] arXiv:1303.0045v2 | The Mesh of Civilizations and International Email Flows
  In The Clash of Civilizations, Samuel Huntington argued that the primary axis of global conflict was no longer ideological or economic but cultural and religious, and that this division would characterize the "battle lines of the future." In contrast to the "top down" approach in previous research focused on the relations among nation states, we focused on the flows of interpersonal communication 
  Full text (https://arxiv.org/html/1303.0045v2), excerpts of its own sections:
  § 1 Introduction: Are the world’s countries re-aligning as the buildup to a global culture war? Most research has examined international global alignments from the top down, based on the relations among nation states. Rather than examining the relations among states, we take a bottom-up view by examining the flows of email between countries, to map global patterns of cross-national integration and division based on the structure of interpersonal social ties among the populations of the world’s countries. Our study extends this line of research on spatial and geographic patterns by examining economic, demographic, and cultural correlates of international communication densities. We estimate these densities using an anonymized collection of email exchanges numbering in order- $10^{7}$ of users. To account for the uneven distribution of the email service’s market share, we develop a novel procedure for rescaling the communication densities. To do so we regress the realized between-country density on the number of users in the sample. [...]
  § 2 Related Work: Geo-social datasets . The emergence and growth of internet platforms has enabled researchers to study very large networks recorded through Internet communication [ 29 ] . The scaling properties of large networks – social and otherwise – emerged from analyses made possible by web data [ 6 , 50 ] . Methodological advances have opened up new research questions related to community detection in large social networks [ 15 , 3 ] or to the distribution of shortest paths [ 4 ] . [...]
  § 6 Discussion: Not all civilizations “survive” a regression analysis that controls for the numerous economic and political factors that may impact cross-country communication. The strong effects we see associated with Islamic, Latin American and Orthodox countries demand further explanation however. For one reason or another, the countries in these groups have stronger level of association than the model would predict. In this respect we cautiously assign a level of validity to Huntington’s contentions, with a few caveats. The first issue was already mentioned - overlap between civilizations and other factors contributing to countries’ level of association. Huntington’s thesis is clearly reflected in the graph presented in Figure 3 , but some of these civilizational clusters are found to be explained by other factors in Table 5 . The second limitation concerns the fact that we investigated a communication network. There is no necessary “clash” between countries that do not communicate, and Huntington’s thesis was concerned primarily with ethnic conflict. [...]
  § 7 Conclusion: The reality of globalization has become a commonplace of lay and scientific discourse alike. The promise of Computational Social Science is to help scholars go beyond such observations, enabling careful measurement of the world’s social structures. Newly-available large, global datasets offer the possibility of an account of international relations as observed between nationals rather than among nations. Our study illustrated how such an opportunity could be pursued with one particular dataset. It is even more exciting to consider the possibility of combining insights derived from multiple online datasets to produce a clearer picture of the world’s social networks. We hope our study has shown the promise of the Internet in the study of our global mesh of civilizations.
[6] arXiv:2401.07398v2 | Cross Domain Early Crop Mapping using CropSTGAN
  Driven by abundant satellite imagery, machine learning-based approaches have recently been promoted to generate high-resolution crop cultivation maps to support many agricultural applications. One of the major challenges faced by these approaches is the limited availability of ground truth labels. In the absence of ground truth, existing work usually adopts the "direct transfer strategy" that trai
  Full text (https://arxiv.org/html/2401.07398v2), excerpts of its own sections:
  § IV-D CropSTGAN Domain Mapper: (a) (b) Fig. 6 : The CropSTGAN Domain Mapper Structure. (a) Cycle 1: The training process involves data flowing from the target domain to the source domain and then back to the target domain. The notation $\mathbf{X}_{s}^{{}^{\prime}}$ represents the transformed target domain data, while $\mathbf{X}_{t}^{{}^{\prime}}$ denotes the data transformed back to the target domain. (b) Cycle 2: The training process involves data flowing from the source domain to the target domain and then back to the source domain. The notation $\mathbf{X}_{t}^{{}^{\prime}}$ represents the transformed source domain data, while $\mathbf{X}_{s}^{{}^{\prime}}$ denotes the data transformed back to the source domain.
  § V Experiment setup and Results: TABLE VI : Cross-Year Experiment Metrics Comparison: Targeting Jackson County 2020. The best metrics are indicated in bold, while the second-best metrics of the baseline methods are underlined. CropSTGAN CropTGAN STDAN TempCNN OA F1 Kappa OA F1 Kappa OA F1 Kappa OA F1 Kappa S1 0.9300 0.9311 0.8596 0.9167 0.9142 0.8339 0.9389 0.9386 0.8769 0.6162 0.4304 0.2623 S2 0.9220 0.9218 0.8441 0.8921 0.8920 0.7843 0.9289 0.9285 0.8565 - - - S3 0.9266 0.9274 0.8530 0.8861 0.8828 0.7728 0.9248 0.9249 0.8498 - - - Avg 0.9262 0.9268 0.8522 0.8983 0.8963 0.7970 0.9309 0.9307 0.8611 0.6162 0.4304 0.2623 TABLE VII : Cross-Year Experiment Metrics Comparison: Targeting Jackson County 2021. The best metrics are indicated in bold, while the second-best metrics of the baseline methods are underlined. [...]
  § V-A Experiment Setup: This work designs two sets of experiments to comprehensively evaluate the cross-domain performance of the proposed CropSTGAN method: • The first set of experiments investigates the cross-year scenario, where Jackson County from 2020 to 2021 is considered as the target domain, and Jackson County in 2019 serves as the source domain. The discrepancies in data distribution between these domains are relatively slight. • The second series of experiments explores cross-region scenarios, incorporating a study area in China and Jackson County. When Jackson County 2019 serves as the source domain, the target domain is the study area in China 2019. Conversely, when the study area in China 2019 is the source domain, Jackson County 2019 becomes the target domain. The discrepancies in data distribution across the domains are relatively large. To evaluate the distinct architecture of the CropSTGAN domain mapper, comparative experiments were undertaken utilizing a simpler, analogous structure named CropTGAN. [...]
  § V-C Evaluation Metrics: To assess the performance of the binary corn crop mapping, the following metrics are used:
  § V-D Results: (a) (b) Fig. 11 : The t-SNE Visualization of Corn Data Points for the Cross-Year Experiments: Comparison between Target Domain Data, Transformed Target Domain Data, and Source Domain Data. (a) Jackson County 2020 as the target domain. (b) Jackson County 2021 as the target domain. (a) (b) Fig. 12 : The t-SNE Visualization of Corn Data Points for the Cross-Domain Experiments: Comparison between Target Domain Data, Transformed Target Domain Data, and Source Domain Data. (a) The study area of China as the target domain. (b) Jackson County 2019 as the target domain. Tables VI and VII present the results for the first set of cross-year experiments. Tables VIII and IX present the results for the second set of cross-region experiments. [...]
[7] arXiv:1611.07100v2 | Interpreting Finite Automata for Sequential Data
  Automaton models are often seen as interpretable models. Interpretability itself is not well defined: it remains unclear what interpretability means without first explicitly specifying objectives or desired attributes. In this paper, we identify the key properties used to interpret automata and propose a modification of a state-merging approach to learn variants of finite state automata. We apply 
  Full text (https://arxiv.org/html/1611.07100v2), excerpts of its own sections:
  § 1 Introduction: The demand for explainable machine learning is increasing, driven by the spread of machine learning techniques to sensitive domains like cyber-security, medicine, and smart infrastructure among others. Often, the need is abstract but nevertheless a requirement, e.g., in the recent EU regulation ( Goodman and Flaxman, 2016 ) . Approaches to explanations range from post-hoc explanation systems like Turner (2015) , which provide explanations of decisions taken by black-box systems to the use of linear or specialized white-box systems ( Fiterau et al., 2012 ) that generate models seen as simple enough for non-expert humans to interpret and understand. Lipton (2016) outlines how different motivations and requirements for interpretations lead different notions of interpretable models in supervised learning. Automata models, such as (probabilistic) deterministic finite state automata ((P)DFA) and timed automata (RA) have long been studied ( Hopcroft et al. (2013) ) and are often seen as interpretable models. [...]
  § 2 Preliminaries: Finite automata. The models we consider are variants of deterministic finite state automata, or finite state machines. These have long been key models for the design and analysis of computer systems  ( Lee and Yannakakis, 1996 ) . We provide a conceptual introduction here, and refer to Section B in the appendix for details. An automaton consists of a set of states, connected by transitions labeled over an alphabet. It is said to accept a word (string) over the alphabet in a computation if there exists a path of transitions from a predefined start state to one of the predefined final states, using transitions labeled with the letters of the word. Automata are called deterministic when there exists exactly one such path for every possible string. Probabilistic automata include probability values on transitions and compute word probabilities using the product of these values along a path, similar to hidden Markov models (HMMs). Learning approaches. [...]
  § 3 Flexible State-Merging: The key step in state-merging algorithms is the identification of good merges. A merge of two states is considered good if the possible futures of the two states are very similar. By focusing on application-driven notions of similarity of sequences and sequence elements, we modify the state-merging algorithm as follows: For each possible merge, a heuristic can evaluate an application-driven similarity measure to obtain the merge score. [...]
  § 6 Discussion: The applications surveyed in Section 5 show that interpreting finite state automata as models takes many forms and serves different goals. As such, this interpretation is not a feature inherent in the models or the algorithms themselves. Rather, interpretations are defined by the need and intention of the user. But yet, interpretations of automata models draw from a core set of properties as identified in Section 4 : graphical representations, transparent computation, generative nature, and our understanding of their theory. We note that automata models are particularly useful in unsupervised learning: Applications of automata models often aim at easing the transfer of knowledge about the subject, or related subjects, to the data generating process. In this case, machine learning serves as a tool for exploration, to deal with epistemic uncertainty in observed systems. The goal is not only to obtain a more compact view of the data, but learn how to generalize from the observed data. Often, it is often unclear what the a-priori knowledge is as users rely on experience. [...]
[8] arXiv:2005.12156v2 | ConFuzzius: A Data Dependency-Aware Hybrid Fuzzer for Smart Contracts
  Smart contracts are Turing-complete programs that are executed across a blockchain. Unlike traditional programs, once deployed, they cannot be modified. As smart contracts carry more value, they become more of an exciting target for attackers. Over the last years, they suffered from exploits costing millions of dollars due to simple programming mistakes. As a result, a variety of tools for detecti
  Full text (https://arxiv.org/html/2005.12156v2), excerpts of its own sections:
  § I Introduction: The inception of immutable, blockchain-based smart contracts has shown how to enable multiple mistrusting parties to trade and interact without relying on a centralized, trusted third party. The immutability of a contract is crucial: if at least one of the engaging parties were allowed to modify a digital contract, the contract’s trust would vanish. Unlike traditional legal contracts, smart contracts do not allow a dispute resolution with a neutral third party. Most importantly, smart contracts cannot be nullified — parties cannot revoke any deployed smart contract, even if its code figures undeniable software bugs. [...]
  § V Evaluation: In this section, we evaluate the effectiveness and performance of ConFuzzius by answering the following three research questions: RQ1 Does ConFuzzius achieve higher code coverage than current state-of-the-art symbolic execution and fuzzing tools for smart contracts? RQ2 Does ConFuzzius discover more vulnerabilities than current state-of-the-art symbolic execution and fuzzing tools for smart contracts? RQ3 How relevant are ConFuzzius ’s individual components in terms of code coverage and vulnerability detection? TABLE III: Statistics of our clusters and overall dataset. Dataset LoSC Functions Instructions Min Max Mean Min Max Mean Min Max Mean Small 1 3,584 119 1 81 14 1 3,632 1,763 Large 44 3,148 429 1 190 32 3,633 16,889 5,495 Overall 1 3,584 168 1 190 17 1 16,889 2,353 Datasets. We run our experiments using two different datasets. The purpose of the first dataset is to measure code coverage, whereas the second dataset aims to measure the detection of vulnerabilities 2 2 2 Both datasets are available at https://github.com/christoftorres/ConFuzzius . . [...]
  § V-C Component Evaluation: Fig. 11: Comparison of overall instruction coverage and vulnerabilities detected between ConFuzzius ’s individual components. In the following, we evaluate the importance of ConFuzzius ’s three main components: 1) constraint solving , 2) read-after-write dependency analysis and 3) environmental instrumentation . We randomly selected 100 contracts from each cluster. We then performed three experiments for each contract, where we deactivated a different component for each experiment. For example, in the ”Without Constraint Solving” experiment, we disabled constraint solving but kept RAW dependency analysis, and environmental instrumentation enabled. This means that inputs will be generated following a random uniform distribution, and the constraint solver will not produce inputs. In the ”Without Read-After-Write Dependency” experiment, we disabled RAW dependency analysis but kept constraint solving and environmental instrumentation enabled. [...]
  § VII Conclusion: We presented ConFuzzius , the first hybrid fuzzer for smart contracts. It tackles the three main challenges of smart contract testing: input generation , stateful exploration , and environmental dependencies . We solved the first challenge by combining evolutionary fuzzing with constraint solving to generate meaningful inputs. The second challenge is solved by leveraging data dependency analysis across state variables to generate purposeful transaction sequences. Finally, we solved the third challenge by modeling block related information (e.g. block number) and contract related information (e.g. call return values) as fuzzable inputs. We run ConFuzzius and other state-of-the-art fuzzers and symbolic execution tools for smart contracts against a curated dataset of 128 contracts and a dataset of 21K real-world smart contracts. [...]
[9] QNFO: The Base State Hypothesis: A Falsification Protocol for a Substrate Capable of Hosting the Standard Model, Audited Against Contemporary Quantum Platforms | https://papers.qnfo.org/papers/the-base-state-hypothesis-a-falsification-protocol-for-a-substrate-capable-of-ho
  We formalize the question of whether a single, explicitly constructible quantum object — a "Base State" — could serve as a substrate on which the structure of the Standard Model is hosted, rather than the Standard Model being assembled from particle-like primitives on a qubit-gate substrate. A Base State is defined as a normalized state (or density operator) in a finite-dimensional Hilbert space, 
  Full text (https://papers.qnfo.org/papers/the-base-state-hypothesis-a-falsification-protocol-for-a-substrate-capable-of-ho), excerpts of its own sections:
  § 4.1 Per-operation error rates and per-operation summary: $$ \epsilon_1 = 1 - F_1 = 1 - 0.9990 = 1.0\times10^{-3}, $$ $$ \epsilon_2 = 1 - F_2 = 1 - 0.9956 = 4.4\times10^{-3}, $$ $$ \epsilon_r = 1 - F_r = 1 - 0.987 = 1.3\times10^{-2}. $$ Ratios: $\epsilon_2/\epsilon_1 = 4.4\times10^{-3}/1.0\times10^{-3} = 4.4$; $\epsilon_r/\epsilon_1 = 1.3\times10^{-2}/1.0\times10^{-3} = 13$. Per-operation summary (convention of Appendix A, D1): the sum of fidelities is $S = 0.9990 + 0.9956 + 0.9870 = 2.9816$, so $$ \bar{F} = \frac{2.9816}{3} = 0.9938667\ldots \approx 99.39\%. $$ The three-step composite: $0.9990 \times 0.9956 = 0.9946044$; $0.9946044 \times 0.9870 = 0.9816745428$; hence $$ P_{\mathrm{err}} = 1 - 0.9816745428 = 0.0183254572 \approx 1.8325\%. $$ Log-fidelities (natural log), used throughout: $$ \ln F_1 = \ln(0.9990) \approx -1.0005\times10^{-3}, $$ $$ \ln F_2 = \ln(0.9956) \approx -4.4097\times10^{-3}, $$ $$ \ln F_r = \ln(0.987) \approx -1.30816\times10^{-2}. $$
  § 5. Results: All numbers below are computed in Section 4 from the inputs of [2]; the two projections are labeled. 1. **Per-operation errors.** $\epsilon_1 = 1.0\times10^{-3}$, $\epsilon_2 = 4.4\times10^{-3}$, $\epsilon_r = 1.3\times10^{-2}$ (Section 4.1). 2. **Per-operation summary (convention D1).** $\bar{F} \approx 99.39\%$; three-step composite error $P_{\mathrm{err}} \approx 1.83\%$ (Section 4.1). 3. **Dimension and specifiability.** $D_{105} = 2^{105} \approx 4.056\times10^{31}$; a generic pure state requires $2^{106}-2 \approx 8.113\times10^{31}$ real parameters, i.e., $\approx 7.7266\times10^{29}$ per qubit, versus $105$ bits to index a basis state (Section 4.2). Any hostable Base State must be a structured, design-like state, not a generic one. 4. **Two-qubit serial budget.** At most $n = 157$ two-qubit gates at $\ge 50\%$ aggregate fidelity, or $n = 154$ with one final readout (Section 4.3). 5. **Readout ceiling.** Full-register readout of 105 qubits at $F_r = 0.987$ caps verification fidelity at $F_{\mathrm{ro}} \approx 0.2532$ (Section 4.4). 6. [...]
  § 6. Discussion: **Limitations of the audit.** The fidelity model of Section 3.2 assumes independent, multiplicative errors and ignores crosstalk, leakage, idling decay, and state-preparation error. All circuit-level numbers ($F_{\mathrm{ro}} \approx 0.2532$, $F_{\mathrm{circ}} \approx 0.1467$, $F_2^{400} \approx 0.1714$) are therefore upper bounds under this model; real hardware would do worse, so the qualitative conclusions (readout bottleneck, budget exhaustion) are conservative, but the specific values should not be read as measurements. **Convention dependence.** The per-operation summary $\bar{F} \approx 99.39\%$ and composite error $P_{\mathrm{err}} \approx 1.83\%$ (convention D1, Appendix A) are descriptive summaries, not inputs to any budget computation; the budgets use only the log-domain products. The single-readout budget of Section 4.3 ($n = 154$) and the full-register ceiling of Section 4.4 ($F_{\mathrm{ro}} \approx 0.2532$) answer different questions under convention D2 (Appendix A); neither contradicts the other. [...]
  § 7. Conclusion: We defined a Base State as a preparable, verifiable, compositionally closed quantum object and audited its feasibility on the only quantitative platform in the corpus, the Tianyan-287 [2]. The audit yields a compression gap of roughly thirty orders of magnitude between generic states and indexable states, a full-register readout ceiling $F_{\mathrm{ro}} \approx 0.2532$ against a verification threshold $\theta = 0.5$, a two-qubit serial budget of $157$ gates ($154$ with one [...]
[10] QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics | https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis
  Sixteen published records from a single research program, spanning December 2025 to August 2026, are here organized into one testable claim: trapped-ion quantum simulators are the first near-term platform on which ultrametric (p-adic) structure in quantum dynamics can be accepted or rejected by measurement, and passive, dissipation-structured hardware is the engineering embodiment of that structur
  Full text (https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis), excerpts of its own sections:
  § 1. Introduction: Between December 2025 and August 2026, a research program published twenty-one records on trapped-ion quantum computation, p-adic geometry, and the epistemology of physics. Read individually, they look like three different projects: an experimental physics effort, a mathematical physics effort, and a philosophy-of-science effort. This paper argues they are one project, and that reading them as one project changes what a practitioner should do next. The unifying claim is structural, not metaphysical. [...]
  § 5. Negative Results the Register Must Respect: A testable program is one that keeps its negative results. Five are load-bearing here, and three more are kept on the same ledger with explicit scope rules. First, generic clock-rest coupling does NOT produce ultrametricity. The 8,000-system study found a 29-35 percent violation rate in the generic case [@quni2026pwdistances]. This matters because an earlier, naive version of the program's expectation -- that ultrametricity would emerge generically from any Page-Wootters construction -- is thereby ruled out. The surviving claim is the sharp sufficient condition: diagonal coupling. The trapped-ion protocol is designed around exactly that surviving claim. A reader who only sees the positive claim without the ruled-out generic case would misprice the theory. Second, trapped ions are the wrong economics play. The joules-per-solution competitive landscape ranks trapped ions last among seventeen platforms (8.5-16.3 J/sol) because 50-100 microsecond gate times overwhelm their room-temperature power advantage [@qnfo2026jpcubcl]. [...]
  § 12. Data-Quality Findings: Cross-system identifier audit of the input records surfaced seven findings: the two vortex-feasibility records are cross-wired in the archive's identifier table (each row carrying the other's DOI); three records lack DOI fields entirely; one record carries a generic internal title; and an identifier-type field is systematically mislabeled. The duplicate-record pairs (Section 2) are the archive-level expression of the same disorder. The v1.4 cycle adds three more findings. First, the QEC-Darwinism record's cross-system identifiers drift: the paper_ids registry carries archive_doi 21819232 while the record and concept are 21964674 and 21809888, and the living-paper store title ("Ultrametric Code Spaces: The Bruhat-Tits Tree as a Geometry for Quantum Error Correction") differs from the the QNFO archive v1.11 title ("Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces") [@archimedeanshadows2026]. Second, the records added in this version continue the version-label inconsistency documented above (v0.4, v1.1, v1.11, and unlabeled rows in the same set). [...]
  § 13. Conclusion: Twenty-one records, three movements, one testable structure. The contribution is not the claim that ultrametric structure exists in quantum dynamics; it is the claim that the structure is now cheap to test, and the register that makes the tests concrete. R1 is an eight-week experiment on existing apparatus. R3 runs on a laptop. The architectural movement gives the design language; the methodological movement gives the discipline; the register gives the practitioners something to build, measure, or reject. If the register fills with null results, the program has still contributed: five kill-conditions executed is five pieces of knowledge gained, and the falsifiability discipline the records advocate will have been demonstrated on their own claims.
[11] QNFO: Base State–Disturbance (BS-D) Ontology | https://papers.qnfo.org/papers/base-statedisturbance-bs-d-ontology
  This presents the formalization and computational validation of the Base State–Disturbance (BS-D) Ontology, a framework proposed to resolve the conceptual fragmentation between Quantum Field Theory (QFT) and General Relativity. We posit that physical reality is reducible to two interdependent primitives: a Base State (a topological string-net liquid) and Disturbances (emergent topological defects)
  Full text (https://papers.qnfo.org/papers/base-statedisturbance-bs-d-ontology), excerpts of its own sections:
  § Thermodynamic: Genesis of a Topological Vacuum via Lattice Annealing **Author:** Rowan Brad Quni-Gudzinas **Contact:** rowan.quni@outlook.com **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](https://isni.org/isni/0000000526456062) **URL:** https://papers.qnfo.org/papers/base-statedisturbance-bs-d-ontology/ **Date:** 2025-12-31 **Version:** 1.1 **Abstract**: This presents the formalization and computational validation of the *Base State–Disturbance (BS-D) Ontology*, a framework proposed to resolve the conceptual fragmentation between Quantum Field Theory (QFT) and General Relativity. We posit that physical reality is reducible to two interdependent primitives: a *Base State* (a topological string-net liquid) and *Disturbances* (emergent topological defects). Drawing upon String-Net Condensation theory, the genesis of the vacuum was modeled as a thermodynamic phase transition governed by the cooling of a Toric Code lattice. [...]
  § 1.1 The: Crisis of Fragmentation in Fundamental Physics Contemporary theoretical physics is currently defined by a profound epistemological crisis, often characterized as a tower of Babel scenario where the foundational languages of its two pillars—Quantum Field Theory (QFT) and General Relativity (GR)—remain mutually unintelligible. This fragmentation is not merely a matter of mathematical formalism but represents a deep ontological schism regarding the nature of physical reality itself. On one side, QFT describes a universe of discrete particles and probabilistic fields evolving against a fixed background, treating the vacuum as a passive stage for quantum events (Wen, 2004). On the other, GR posits a dynamic, continuous spacetime geometry that interacts with matter, yet it lacks a consistent quantum description. The persistence of this divide suggests that the current inventory of fundamental primitives—particles, fields, and spacetime metrics—may be insufficient to construct a unified theory. It is argued that a higher-order meta-language is required to bridge these domains. [...]
  § 1.2: String-Net Condensation as the Unifying Mechanism The topological turn in modern condensed matter physics provides the most promising theoretical mechanism for unifying the disparate phenomena of gauge bosons and fermions under a single ontological framework. Specifically, the theory of String-Net Condensation posits that the vacuum is not an empty void but a complex quantum liquid composed of extended, fluctuating networks of strings (Levin & Wen, 2005). Within this framework, elementary particles are not fundamental building blocks but collective excitations—topological defects—of the underlying string-net condensate. This radical shift in perspective resolves the long-standing puzzle of the origin of light and electrons, deriving them as inevitable consequences of the topological order inherent in the Base State. By treating the vacuum as a structured medium, it is mathematically demonstrable that Maxwell’s equations and the Dirac equation emerge naturally from the dynamics of simple bosonic spin systems. [...]
  § 1.3 Ontic: Structural Realism: Relations Before Objects The shift from object-oriented physics to the Base State–Disturbance ontology necessitates a parallel shift in metaphysics, specifically toward Ontic Structural Realism (OSR). OSR posits that the fundamental constituents of reality are not self-subsistent objects with intrinsic properties, but rather relational structures (Ladyman & Ross, 2007). [...]
[12] QNFO: Standard Model | https://papers.qnfo.org/papers/standard-model-critique
  The Standard Model (SM) of particle physics represents the most precise and empirically successful framework devised for describing fundamental particles and their interactions. This rigorous empirical success is intrinsically coupled with severe, formally demonstrable theoretical deficiencies that invalidate its claim to be a complete description of physical reality. This scholarly deconstruction
  Full text (https://papers.qnfo.org/papers/standard-model-critique), excerpts of its own sections:
  § Standard: Model Critique: Formal Deconstruction of an Incomplete Paradigm and the Methodological Imperative for a Successor Theory **Author:** Rowan Brad Quni-Gudzinas **Affiliation:** QNFO **Contact:** rowan.quni@qnfo.org **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000 0005 2645 6062 **DOI:** https://papers.qnfo.org/papers/standard-model-critique/ **Publication Date:** 2025-09-26 **Version:** 1.0 The Standard Model (SM) of particle physics represents the most precise and empirically successful framework devised for describing fundamental particles and their interactions. This rigorous empirical success is intrinsically coupled with severe, formally demonstrable theoretical deficiencies that invalidate its claim to be a complete description of physical reality. [...]
  § I. Formal: Architecture and Consistency The structure of the Standard Model is the source of both its predictive power and its inherent constraints. Its architecture is encapsulated in the Lagrangian density, \(\mathcal{L}_{\text{SM}}\), which rigorously defines the dynamics of all particles and interactions based on the principle of local gauge invariance under the defining symmetry group: \(G_{\text{SM}} = \mathrm{SU(3)}_C \times \mathrm{SU(2)}_L \times \mathrm{U(1)}_Y\) [1]. The total Lagrangian is derived by constructing the most general renormalizable expression invariant under this gauge symmetry and the Poincaré group. It decomposes into four constituent sectors: 1. **Gauge Sector (\(\mathcal{L}_{\text{Gauge}}\)):** Describes force dynamics through their field strength tensors, which must include cubic and quartic self-interaction terms for the non-Abelian subgroups \(\mathrm{SU(3)}_C\) and \(\mathrm{SU(2)}_L\) [1]. 2. [...]
  § II.: Foundational Deficits and Structural Incompleteness The Standard Model’s claim to be a fundamental theory is profoundly undermined by systematic deficits that confirm its status as an incomplete model.
  § II.A.: Ontological Incompleteness and the Cosmological Crisis The SM fails the test of ontological completeness by ignoring gravitational interactions and the vast majority of the universe’s content. **Axiomatic Impasse with General Relativity** The conceptual chasm between the Standard Model (a quantum field theory on a fixed spacetime background) and General Relativity (a theory of dynamical spacetime geometry) precludes the consistent quantization of gravity within the SM framework. This ontological mismatch signals the fundamental inadequacy of both theories at the Planck scale (\(\sim 10^{19}\ \text{GeV}\)) [3]. **Cosmological Constant Problem** The Standard Model’s prediction for the theoretical vacuum energy density (\(\rho_{\text{vac}}^{\text{SM}}\)), derived by summing zero-point energies of quantum fields up to the Planck scale cutoff (\(\Lambda = M_{\text{Planck}}\)), yields a quartic divergence: \[ \rho_{\text{vac}}^{\text{SM}} \approx \frac{1}{8\pi^2} \Lambda^4 \approx 10^{74}\ \text{GeV}^4. [...]
  § II.B. Lack of: Explanatory Closure A fundamental theory must derive its internal structure and constants from first principles. The Standard Model fails this test by requiring at least **19 arbitrary, un-derived parameters** that must be supplied from experimental measurement [3]. This includes the three gauge coupling constants (\(g_s, g, g'\)), the two Higgs potential parameters (\(\mu, \lambda\)), the nine charged fermion masses (related to nine Yukawa couplings), the four CKM quark mixing parameters, the four PMNS lepton mixing parameters, and the strong CP phase (\(\theta_{\text{QCD}}\)) [3]. [...]