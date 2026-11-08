# Quantum Kolmogorov Complexity: A Family of Uncomputable Description‑Length Measures

## Abstract
Quantum information processing demands a notion of algorithmic description length that applies directly to quantum states. Existing proposals either rely on classical descriptions of quantum objects or suffer from ill‑defined infinities. We therefore define **quantum Kolmogorov complexity** (QKC) as the length of the shortest quantum program that, when executed on a universal quantum Turing machine (UQTM), outputs a target state within a prescribed fidelity. This definition yields a *family* of measures distinguished by the choice of fidelity parameter, the nature of the program (pure versus mixed), and the allowed auxiliary resources. We prove an invariance theorem showing that any two UQTMs differ by at most an additive constant, and we demonstrate uncomputability by reduction from classical Kolmogorov complexity. As a concrete illustration we assume a universal machine description length of 120 bits and compute explicit additive bounds for the QKC of a state whose classical Kolmogorov complexity is 500 bits, obtaining a QKC interval of [380 bits, 620 bits]. The result clarifies how QKC can quantify quantum randomness, entanglement, and circuit complexity, and it establishes a rigorous foundation for future quantitative studies of quantum informational resources.

## 1. Introduction
Quantum technologies such as fault‑tolerant quantum computers, quantum key distribution networks, and quantum‑enhanced sensing platforms are limited by the lack of a principled, state‑level measure of informational content. Engineers must decide how many qubits to allocate for error‑correction, protocol designers must assess the randomness of generated states, and theorists need a tool to compare the intrinsic difficulty of preparing different quantum resources. Currently, these decisions rely on indirect proxies such as circuit depth, entanglement entropy, or classical description length, each of which either ignores quantum superposition or yields infinite values for generic states. If a *quantum Kolmogorov complexity* (QKC) measure were available, one could directly compare the algorithmic content of two quantum states, decide whether a given state is “simple” enough to be generated on near‑term hardware, or certify that a source produces truly quantum‑random outputs.

In this work we formalize QKC, prove its fundamental properties, and derive explicit numerical bounds that illustrate its behaviour. Our contributions are:
- **C1.** A definition of QKC based on the shortest quantum program that outputs a target state within fidelity ε (Section 2).  
- **C2.** An invariance theorem proving that any two universal quantum Turing machines differ by at most an additive constant c (Section 3).  
- **C3.** A reduction showing that computability of QKC would imply computability of classical Kolmogorov complexity, establishing uncomputability of all QKC variants (Section 3).  
- **C4.** A concrete numerical example: assuming a universal machine description length L_U = 120 bits and a classical Kolmogorov complexity K = 500 bits, we derive the QKC interval [380 bits, 620 bits] (Section 4).  
- **C5.** A discussion of limitations, falsifiability conditions, and practical pathways for employing QKC in quantum engineering (Sections 5–7).

The framework may also impact adjacent fields such as quantum thermodynamics (where algorithmic entropy plays a role) and quantum cryptography (where randomness certification is essential).

## 2. Background and Related Work
The algorithmic information‑theoretic approach to quantum states has been explored in several recent works. Vitányi’s definition, which augments a classical description with a fidelity term, is adopted as a starting point because it avoids the infinity problem noted by Svozil [1, § II]. Specifically, Vitányi adds a penalty proportional to the logarithm of the inverse fidelity, thereby ensuring finite values for all states.

Berthiaume, van Dam and Laplante defined QKC as the length of the shortest *quantum* program that outputs a target state, a formulation we extend to include mixed‑state inputs and a fidelity parameter (see also the dcq‑TM model of [6, § 1.1]). The criteria for a “good” definition listed in [2, § 2]—robustness under change of universal machine, relationship to quantum information theory, and compatibility with classical complexity on classical strings—guide our construction.

The invariance property proved for deterministic‑control quantum Turing machines in [6, § 1.1] shows that the Kolmogorov complexity defined in that model is machine‑independent up to an additive constant. This result directly inspires our invariance theorem for the broader family of QKC measures.

In the classical setting, Kolmogorov complexity quantifies randomness and underlies many lower‑bound arguments in formal language theory [4, § 1.2] and computational complexity [5]. The same incompressibility arguments can be transferred to the quantum domain, as discussed in the comparison of Shannon and algorithmic information in [7, § 1].

Finally, the multitime bi‑probability framework of [3] illustrates that quantum descriptions often require multiple correlated trajectories, reinforcing the need for a description‑length measure that can capture such correlations without collapsing to classical infinities.

## 3. Methods
### 3.1 Model of Computation
We adopt the deterministic‑control quantum Turing machine (dcq‑TM) of [6] as our universal model. A dcq‑TM consists of a classical control unit and a quantum tape; it can accept mixed‑state inputs and produce mixed‑state outputs. The machine halts in a unique halting state, ensuring a well‑defined output density matrix ρ_out.

### 3.2 Definition of Quantum Kolmogorov Complexity
Let U be a fixed universal dcq‑TM. For a target quantum state ρ (pure or mixed) and a fidelity parameter ε ∈ (0,1], define

$$
K_U^{\varepsilon}(\rho) \;=\; \min_{p}\bigl\{\,|p| \;+\; \lceil -\log_2 \varepsilon \rceil \;\big|\; U(p) \text{ halts with output } \sigma,\; F(\sigma,\rho) \ge 1-\varepsilon \,\bigr\},
$$

where |p| is the length (in bits) of the classical description of the quantum program p, and \(F(\sigma,\rho)=\bigl(\operatorname{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\bigr)^2\) is the fidelity. The term \(\lceil -\log_2 \varepsilon \rceil\) penalizes low fidelity, following Vitányi’s approach [1, § II].

### 3.3 Invariance Theorem
Let U and U′ be two universal dcq‑TMs. There exists a constant c = |⟨p_{U→U′}⟩|, the length of a fixed translator program that simulates U on U′. For any state ρ and any ε,

$$
K_{U}^{\varepsilon}(\rho) \;\le\; K_{U′}^{\varepsilon}(\rho) \;+\; c,
\qquad
K_{U′}^{\varepsilon}(\rho) \;\le\; K_{U}^{\varepsilon}(\rho) \;+\; c.
$$

*Proof.* Given a program p′ that makes U′ output σ′ with fidelity ≥ 1 − ε, prepend the translator p_{U→U′} to obtain a program p that makes U output the same σ′ (the translator simulates U′). The length of p is |p_{U→U′}| + |p′|, establishing the first inequality. Symmetry yields the second. ∎

Thus the choice of universal machine affects QKC by at most an additive constant c, which is independent of ρ.

### 3.4 Uncomputability Reduction
Assume, for contradiction, that there exists an algorithm A that computes \(K_U^{\varepsilon}(\rho)\) for all ρ and a fixed ε. Consider a classical binary string x and its associated computational basis state \(|x\rangle\). By construction, \(K_U^{\varepsilon}(|x\rangle)\) differs from the classical Kolmogorov complexity K(x) by at most the constant c of the invariance theorem (since a classical program that outputs x can be embedded as a quantum program that prepares \(|x\rangle\)). Therefore A would compute K(x) up to an additive constant, contradicting the classical uncomputability of Kolmogorov complexity. Hence QKC is uncomputable for every ε.

## 4. Analysis
We now instantiate the invariance bound with concrete numbers to illustrate its magnitude.

### 4.1 Assumed Parameters
- Description length of the translator program between any two universal dcq‑TMs:  
  \(L_U = 120\) bits (assumption, denoted as an additive constant c).  
- Classical Kolmogorov complexity of a specific binary string x of length 256:  
  \(K(x) = 500\) bits (taken from a hypothetical but concrete example).  

### 4.2 Derivation of QKC Bounds
From the invariance theorem (Section 3.3) we have for any ε:

$$
K_U^{\varepsilon}(|x\rangle) \;\in\; [\,K(x) - L_U,\; K(x) + L_U\,].
$$

Plugging the numbers:

1. Lower bound:  
   \(K_{\text{low}} = K(x) - L_U = 500 - 120 = 380\) bits.  

2. Upper bound:  
   \(K_{\text{high}} = K(x) + L_U = 500 + 120 = 620\) bits.  

Thus

$$
380 \;\le\; K_U^{\varepsilon}(|x\rangle) \;\le\; 620 \quad\text{bits}.
$$

The interval width is \(2L_U = 240\) bits, reflecting the machine‑dependence.

### 4.3 Fidelity Penalty Example
Choose ε = \(2^{-10}\) (i.e., fidelity loss of 1 − \(2^{-10}\)). The penalty term is

\[
\lceil -\log_2 \varepsilon \rceil = \lceil -\log_2 2^{-10} \rceil = \lceil 10 \rceil = 10 \text{ bits}.
\]

If a program p of length 400 bits produces a state σ with fidelity ≥ 1 − \(2^{-10}\) to \(|x\rangle\), then

\[
K_U^{2^{-10}}(|x\rangle) \le 400 + 10 = 410 \text{ bits},
\]

which lies within the interval derived above, confirming consistency.

## 5. Results
The only quantitative result derived from the analysis is the explicit QKC interval for the example state:

- **Result R1.** For a target computational basis state \(|x\rangle\) with classical Kolmogorov complexity 500 bits, any quantum Kolmogorov complexity measure based on a universal dcq‑TM with translator length 120 bits satisfies  

  \[
  380 \;\le\; K_U^{\varepsilon}(|x\rangle) \;\le\; 620 \quad\text{bits},
  \]

  for any fidelity parameter ε.  

- **Result R2.** With ε = \(2^{-10}\), a concrete program of length 400 bits yields a QKC upper bound of 410 bits, illustrating how fidelity penalties tighten the bound.

These numbers are direct consequences of the arithmetic in Section 4 and do not rely on any external data.

## 6. Discussion
### 6.1 Limitations
- **L1.** The additive constant c = L_U depends on the specific encoding of the translator program; different encoding schemes could change c.  
- **L2.** The analysis assumes a fixed fidelity parameter ε; varying ε changes the penalty term linearly in \(\lceil -\log_2 \varepsilon \rceil\).  
- **L3.** The example uses a classical string x; extending the numeric illustration to genuinely entangled states would require additional assumptions about their classical description lengths.  
- **L4.** Uncomputability holds for exact QKC; approximations within a bounded additive error remain uncomputable by the same reduction.

### 6.2 Falsifiability
The main theorem—that QKC is uncomputable—would be falsified if an algorithm were exhibited that, for every quantum state ρ and fixed ε, outputs the exact value of \(K_U^{\varepsilon}(\rho)\). Such an algorithm would also compute classical Kolmogorov complexity via the embedding described in Section 3.4, contradicting the known impossibility result.

### 6.3 Open Questions
- How tight are the additive constants for realistic quantum programming languages?  
- Can QKC be related quantitatively to von Neumann entropy for mixed states?  
- What is the impact of allowing ancillary entanglement resources on the description length?  
- Are there natural subclasses of quantum states (e.g., stabilizer states) for which QKC becomes computable?

## 7. Practical Implications and Engineering Pathways
**(a) Intended Users and Decision Impact.** Quantum hardware designers can use QKC to estimate the minimal program size required to prepare a target state, informing resource allocation for qubit count and gate depth. Cryptographers can employ QKC as a certification metric for quantum random number generators, ensuring that generated states have high algorithmic complexity and thus resist classical prediction.

**(b) Technology Readiness.** The present work is a purely analytical study that has not undergone peer review; according to NASA’s scale, it resides at TRL 1 (basic principles observed) and, at most, TRL 2 (technology concept formulated).

**(c) Next Smallest Experiment.** A minimal prototype would implement a simple dcq‑TM on a small quantum processor (e.g., 5‑qubit superconducting device) and attempt to prepare a known computational basis state \(|x\rangle\) using a program of length 400 bits. The experiment would measure the fidelity of the output and verify that the observed program length plus fidelity penalty respects the bound \(K_U^{\varepsilon}(|x\rangle) \le 410\) bits. Observation of a violation would falsify the additive‑constant model.

**(d) Engineering Constraints.**  
- *Program Encoding:* The translation constant L_U depends on the chosen instruction set and encoding scheme; standardization is required.  
- *Fidelity Measurement:* Accurate estimation of fidelity F(σ, ρ) demands quantum state tomography, which scales exponentially with qubit number.  
- *Resource Limits:* The universal machine must support arbitrary unitary operations; physical gate sets may impose additional overhead not captured by L_U.

**(e) Projected Cost/Performance Bounds.** Assuming a gate error rate of 10⁻³ and a compiler that adds 20 bits of overhead per logical gate, preparing a state with QKC ≈ 500 bits would require roughly 500 / (1 − 0.02) ≈ 510 logical gates, translating to a circuit depth of order 10³ for a 5‑qubit device. The cost of running such a circuit on current cloud quantum platforms is on the order of a few dollars per shot; scaling to higher QKC values would increase both time and monetary cost linearly with the additive constant.

**(f) Risks and Misuse.** An adversary could attempt to infer the program length of a secret quantum state by probing its preparation circuit, potentially leaking information about the underlying algorithmic description. Proper isolation of the preparation process and limiting access to program metadata mitigate this risk.

## 8. Conclusion
We have introduced a family of quantum Kolmogorov complexity measures grounded in the universal dcq‑TM model, proved an invariance theorem that bounds machine dependence by an additive constant, and established uncomputability via reduction from classical Kolmogorov complexity. A concrete numerical illustration shows how the additive constant translates into explicit QKC intervals for specific states. These results lay a rigorous foundation for quantifying quantum informational resources, opening avenues for algorithmic analysis of quantum randomness, entanglement, and circuit complexity. Future work will explore tighter bounds for specialized state families, connections to thermodynamic entropy, and experimental validation on near‑term quantum processors.

## References
[1] arXiv:1101.2946v3 | Quantum Kolmogorov Complexity and Information-Disturbance Theorem  
[2] arXiv:quant-ph/0005018v1 | Quantum Kolmogorov Complexity  
[3] arXiv:2402.01218v3 | Double or nothing: a Kolmogorov extension theorem for multitime (bi)probabilities in quantum mechanics  
[4] arXiv:cs/0110040v1 | A New Approach to Formal Language Theory by Kolmogorov Complexity  
[5] arXiv:2511.23445v2 | Quantum Polymorphisms and the Complexity of Quantum Constraint Satisfaction  
[6] arXiv:2305.14252v3 | Quantum Kolmogorov complexity and quantum correlations in deterministic-control quantum Turing machines  
[7] arXiv:cs/0410002v1 | Shannon Information and Kolmogorov Complexity  
[8] QNFO: Scale-Invariant Reality | https://papers.qnfo.org/papers/scale-invariant-physics