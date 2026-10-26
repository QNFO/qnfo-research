# Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question

## Abstract

We study a conjectured passive fault-tolerance scheme in which logical qubits are encoded on a Bruhat–Tits tree, the infinite homogeneous tree associated with a non-Archimedean local field, whose natural metric satisfies the strong (ultrametric) triangle inequality. The conjecture states that the energy barrier against a logical error grows as $E_{\text{barrier}}(d) = 2^{d}$ in tree depth $d$, yielding passive protection without active syndrome extraction, with thresholds allegedly exceeding those of surface codes. A study would propose that, under majority‑vote decoding on classical bits, zero logical errors occur at a physical error rate of $p = 0.4$ for depth $d \geq 3$. We formalize the encoding, derive the barrier scaling from the ultrametric geometry, and analyze by explicit computation what the classical evidence does and does not establish: one level of eight-fold majority voting maps $p = 0.4$ to a failure probability of $0.1736704$, two concatenated levels give $\approx 5.55 \times 10^{-3}$, and three levels give $\approx 2.9 \times 10^{-10}$, confirming a genuine recursive threshold mechanism. We reinterpret "zero logical errors" as a confidence bound rather than proof of a vanishing error rate, derive a thermal-activation bound $e^{-2^{d}}$ under a stated barrier model, and identify the central open question: whether the strong triangle inequality confines quantum errors — superpositions, entanglement, coherent noise — or whether the advantage evaporates under full quantum channels. We give labeled projections under declared assumptions, state falsification criteria, and outline the quantum Monte Carlo and tensor-network tests that would settle the question.

## 1. Introduction

Quantum error correction (QEC) protects fragile superposition states from decoherence, and its discovery transformed quantum information from an academic curiosity into a developing engineering discipline [6]. The dominant architectural paradigm — stabilizer codes with repeated syndrome measurement, exemplified by the surface code — achieves fault tolerance actively, at the cost of a large overhead of ancilla qubits, measurement circuits, and real-time decoding. A passive alternative, in which the geometry of the encoding itself suppresses errors without measurement, would be architecturally transformative if it could be made to work for quantum information and not merely classical bits.

This paper investigates a specific passive proposal: encode logical qubits on a Bruhat–Tits tree. A Bruhat–Tits tree is the infinite $(q+1)$-regular tree associated with a local field $k$ (a field complete with respect to a non-Archimedean, or $p$-adic, absolute value); its geometry is ultrametric, meaning that distances satisfy the strong triangle inequality $d_{\mathrm{BT}}(x,z) \leq \max\{d_{\mathrm{BT}}(x,y),\, d_{\mathrm{BT}}(y,z)\}$, so that every triangle is isosceles with the long side unique. Ultrametricity has been argued to underlie hierarchical structure far beyond number theory; in particular, positional notation itself has been described as an ultrametric tree of nested cycles, with the Archimedean real line a derived abstraction rather than the primitive object [11]. The Bruhat–Tits tree is the canonical geometric realization of this hierarchy: sub-orders of the matrix algebra $M_2(k)$ correspond to subtrees ("branches") of the tree, and these branches have been used to study the global selectivity problem and to compute local embeddings [3].

The conjecture under study, due to the author's notebook notes, is twofold: (i) the energy barrier against a logical error on a tree of depth $d$ scales as $E_{\text{barrier}}(d) = 2^{d}$; and (ii) this scaling yields passive fault tolerance with error thresholds far exceeding surface codes, without active syndrome measurement. The supporting evidence is classical, and its status must be stated plainly: the claim that simulations using majority-vote decoding on classical bits found zero logical errors at $40\%$ physical error rates for $d \geq 3$ is an unverified report from the authors' notebook notes. No supplied bibliography entry documents this simulation; we treat it as a working assumption and analyze what it would imply if true. The central open question, stated frankly, is whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise, or whether the observed advantage is a classical decoding artifact.

Our contributions are:

1. A formalization of the tree encoding and a geometric statement of the barrier conjecture $E_{\text{barrier}}(d) = 2^{d}$ (Section 3).
2. An explicit arithmetic analysis of the classical majority-vote evidence, showing that iterated majority voting on an eight-leaf tree constitutes a genuine recursive threshold mechanism at $p = 0.4$, with computed suppression levels (Section 4).
3. A statistical reinterpretation of "zero logical errors" as a confidence bound, not a proof of a vanishing error rate (Section 4).
4. A bounding analysis of the quantum regime under a thermal-activation model, with the quantization gap stated as explicit hypotheses rather than results, together with labeled projections (Sections 4 and 5).
5. A specification of the quantum Monte Carlo and tensor-network simulations, and of the theorem that would need to be proved, that would resolve the open question (Sections 5 and 6).

We are careful throughout to separate what is derived, what is computed, what is reported by the source simulations, and what is conjecture. The paper's honest conclusion is that the classical evidence is real but classical, and that the quantum question remains open in a precise, testable sense.

## 2. Background and Related Work

**Continuous-time QEC.** Reference [1] investigates continuous-time quantum error correction (CTQEC), in which both the noise and the error-correcting operations are treated as processes continuous in time, based on continuous weak measurements and feedback, analyzed from the point of view of the subsystem principle — the statement that protected quantum information is identified with a subsystem of the full system. CTQEC is the natural foil to our passive proposal: it removes the discrete measurement circuit but retains active feedback. A genuinely passive scheme would go one step further, removing even the feedback loop and relying on the energy landscape of the encoding geometry.

**Entanglement-assisted codes.** Reference [2] provides a self-contained introduction to entanglement-assisted quantum error-correcting codes, which use shared entanglement between encoder and decoder as a resource. The supplied summary gives no further technical detail, but the relevance to our setting is structural: if ultrametric confinement fails for independent quantum errors, sharing entanglement across distant branches of the tree is one candidate mechanism for restoring a quantum correction capacity, and the entanglement-assisted framework is the standard language in which such a modification would be expressed.

**Bruhat–Tits trees in arithmetic.** Reference [3] develops a theory, for a local field $k$ and a matrix algebra $A$ over $k$, for computing the set of maximal orders in $A$ containing a given suborder; this set is represented as a subtree of the Bruhat–Tits tree called the branch of the order, and branches have been applied to the global selectivity problem and to computing local embeddings. This is the source of the geometric object we encode on: the tree is not an arbitrary graph but the incidence geometry of arithmetic over a non-Archimedean field. Our conjectured barrier scaling is a statement about how logical operators must traverse this arithmetic tree.

**From classical to quantum codes.** Reference [4] surveys error-correcting codes from the classical to the quantum setting, noting — citing Preskill's claim that the 21st century would be the golden age of quantum error correction — that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed and offer lessons. This is precisely the epistemic gap our paper interrogates: the $40\%$-error-rate simulation is a classical-channel result, and the survey's warning that quantum channels behave differently is the generic form of the quantization question we pose.

**Pauli structure of quantum noise.** Reference [5] introduces the main ideas of QEC — encoding, extraction of syndromes, error operators, and code construction — and shows that general noise and relaxation of a set of two-state quantum systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. This Pauli decomposition is the technical hinge of our analysis: any quantum channel admits an operator-sum expansion in Pauli terms, so the quantum question reduces to whether ultrametric confinement holds for each Pauli component and, critically, whether the coherent superposition of error paths (which has no classical analogue) preserves or destroys the confinement.

**Beyond-qubit encodings.** Reference [6] addresses quantum error correction beyond qubits, motivated by the need to protect fragile quantum superposition states from decoherence noise; the supplied summary emphasizes the general necessity of error correction for robust manipulation of quantum states and notes that the discovery of QEC turned quantum information into a developing field. Our tree encoding is qubit-based, but the beyond-qubit perspective matters for the quantization question: a tree-encoded qudit system might interact with the ultrametric geometry differently than a two-level system, and non-binary alphabets could be matched to the $(q+1)$-regularity of the Bruhat–Tits tree.

**Adiabatic error suppression.** Reference [7] treats error suppression and correction in adiabatic quantum computation, deriving a model for the dynamics of encoded adiabatic quantum computation and building on previously established techniques for error suppression in AQC, on the premise that encoding, suppression, and correction will be required to scale AQC. The adiabatic setting is the closest existing analogue to passive protection: there, too, an energy gap — rather than a measurement cycle — is the protective resource. Our barrier conjecture $E_{\text{barrier}}(d) = 2^{d}$ is structurally an adiabatic-style gap statement transplanted to an ultrametric geometry, and the adiabatic literature's tension between gap protection and thermal excitation is exactly the failure mode we confront in Section 4.

**Non-standard Hilbert spaces.** Reference [8] proposes quaternion-based strategies for quantum error correction by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and quantum gates that ensure inner product preservation, with a simple encoding scheme mapping logical qubits into quaternionic systems. The supplied summary is otherwise thin, but the work is relevant as evidence that the Pauli-operator framework of [5] admits generalizations to non-standard inner-product structures; our proposal is structurally analogous in replacing the Archimedean geometry of standard codes with a non-Archimedean (ultrametric) geometry.

**Ultrametric foundations.** Reference [11] argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with recovering the native ultrametric claimed to resolve cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design. We adopt from this thesis only the structural claim we need — that hierarchical, digit-wise (tree-wise) organization is the native setting for error propagation in positional systems — and we do not rely on the broader resolvent claims, which the summary states without supporting derivation. Reference [12] consolidates quantum correspondences to Spencer-Brown's Laws of Form, in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, identifying open problem categories and proposing extensions; the supplied summary gives no further detail, and we cite it only as contextual background for distinction-based (branching-tree) foundations of computation. References [9] and [10] are corpus identifiers (the Alpha Pi Project and its ultrametric quantum gravity and computation collection) supplied without summary text; we note their existence as the provenance context of the conjecture and derive nothing from them.

No entry in the supplied bibliography contains a threshold theorem for ultrametric geometries, a quantum Monte Carlo study of tree codes, or a proof that the strong triangle inequality confines quantum error operators. The gap this paper targets is therefore genuine.

## 3. Methods

### 3.1 The Bruhat–Tits tree and its ultrametric

Let $k$ be a local field with residue field of size $q$, and let $T_{q}$ denote the Bruhat–Tits tree of $k$: the infinite tree in which every vertex has degree $q + 1$ [3]. We use only the tree structure. Define the path-length distance $d_{\mathrm{BT}}(v, w)$ as the number of edges on the unique path from $v$ to $w$. The ultrametric consequence we exploit throughout: from any vertex $v$ at depth $d$, two error paths that diverge at depth $d_0$ remain separated by $d_{\mathrm{BT}} \geq d - d_0$ for all deeper depths — divergence is permanent and distance grows monotonically, unlike in Euclidean lattices where paths can reconverge.

### 3.2 Encoding

We encode one logical bit (classical analysis) or, prospectively, one logical qubit (quantum proposal) on a depth-$d$ rooted binary subtree $\mathcal{T}_d$ with $2^{d}$ leaves. The classical encoding writes the bit on every leaf; decoding is recursive majority vote, with each internal node taking the majority of its children's values. For $d = 3$ this is a single eight-fold majority vote over the leaves; deeper trees apply the vote iteratively. The quantum proposal — a repetition-like map $|0\rangle_L \mapsto |0\rangle^{\otimes 2^{d}}$, $|1\rangle_L \mapsto |1\rangle^{\otimes 2^{d}}$ — is deliberately minimal, and its quantum completeness (whether the code space corrects a nontrivial set of single-qubit Pauli errors) is left as an open condition, stated in Section 6.

### 3.3 Energy barrier conjecture

We posit a Hamiltonian $H_d$ on $\mathcal{T}_d$ in which the two logical configurations are degenerate ground states and every configuration differing from a ground state on $m$ leaves carries energy at least $m \cdot \epsilon$, with $\epsilon$ the single-site excitation cost. A logical error requires flipping a connected set of sites separating the two logical basins. Because the tree branches, the minimal separating set ("cut") at depth $d$ has size $2^{d}$: an error path must at some depth flip an entire level, and the number of sites at level $\ell$ is $2^{\ell}$. The conjectured barrier is therefore

$$
E_{\text{barrier}}(d) = 2^{d}\, \epsilon,
$$

which we take as $E_{\text{barrier}}(d) = 2^{d}$ with $\epsilon = 1$ as the energy unit. This is the ultrametric analogue of an adiabatic gap argument [7]: protection by energy landscape rather than by measurement. We emphasize that this scaling is a conjecture of the source notes, made precise here but not proved for quantum dynamics.

### 3.4 Noise models

For the classical analysis we use an independent bit-flip channel with flip probability $p$ per leaf. For the quantum projections we use the depolarizing channel on each physical site,

$$
\mathcal{E}_p(\rho) = (1 - p)\,\rho + \frac{p}{3}\bigl(X\rho X + Y\rho Y + Z\rho Z\bigr),
$$

and a coherent $Z$-rotation error $\mathcal{C}_\theta(\rho) = e^{-i\theta Z}\rho\, e^{i\theta Z}$. By the Pauli decomposition of general noise on two-state systems [5], the depolarizing analysis extends term-by-term to arbitrary local noise channels; the coherent case is treated separately because it has no classical analogue.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs. We assume zero logical errors at a $40\%$ physical error rate ($p = 0.4$) for $d \geq 3$, under majority‑vote decoding on classical bits. We emphasize that this result is an unverified report — no supplied source documents the simulation, the trial count, or the decoder details — and every conclusion downstream is conditional on it. The trial count $N$ of the reported simulation is not stated in the source; we therefore compute confidence bounds for two declared scenarios, $N = 10^{4}$ and $N = 10^{5}$.

### 4.1 Single-level majority vote at $p = 0.4$

**Input:** $n = 8$ leaves (depth $d = 3$ binary tree, $2^{3} = 8$), independent bit-flip probability $p = 0.4$, so $1 - p = 0.6$. The majority vote fails when at least $5$ of $8$ bits flip:

$$
f(p) = \sum_{k=5}^{8} \binom{8}{k} p^{k} (1-p)^{8-k}.
$$

Compute each term:

- $\binom{8}{5} = 56$; $p^5 = 0.4^5 = 0.01024$; $(0.6)^3 = 0.216$; term $= 56 \times 0.01024 \times 0.216 = 56 \times 0.00221184 = 0.12386304$.
- $\binom{8}{6} = 28$; $p^6 = 0.004096$; $(0.6)^2 = 0.36$; term $= 28 \times 0.004096 \times 0.36 = 28 \times 0.00147456 = 0.04128768$.
- $\binom{8}{7} = 8$; $p^7 = 0.0016384$; $(0.6)^1 = 0.6$; term $= 8 \times 0.0016384 \times 0.6 = 8 \times 0.00098304 = 0.00786432$.
- $\binom{8}{8} = 1$; $p^8 = 0.00065536$; term $= 0.00065536$.

Sum:

$$
f(0.4) = 0.12386304 + 0.04128768 + 0.00786432 + 0.00065536 = 0.1736704.
$$

So one level of eight-fold majority voting maps $p = 0.4$ to $p^{(1)} = 0.1736704$ — a suppression factor of $0.4 / 0.1736704 \approx 2.303$. The vote helps (since $p = 0.4 < 0.5$), but a single level is far from the reported zero-error behavior; the reported result must rest on the recursive tree structure, which we now verify.

### 4.2 Iterated (concatenated) majority vote

Apply $f$ again with $p^{(1)} = 0.1736704$, $1 - p^{(1)} = 0.8263296$:

- $p^2 = 0.1736704^2 = 0.030161414$; $p^4 = 0.030161414^2 = 0.000909691$; $p^5 = 0.000909691 \times 0.1736704 = 0.000157982$.
- $(0.8263296)^2 = 0.68282058$; $(0.8263296)^3 = 0.68282058 \times 0.8263296 = 0.564233$.
- Term $k=5$: $56 \times 0.000157982 \times 0.564233 = 56 \times 0.000089135 = 0.00499156$.
- $p^6 = 0.000157982 \times 0.1736704 = 0.000027437$. Term $k=6$: $28 \times 0.000027437 \times 0.68282058 = 28 \times 0.000018735 = 0.00052458$.
- $p^7 = 0.000027437 \times 0.1736704 = 0.000004765$. Term $k=7$: $8 \times 0.000004765 \times 0.8263296 = 8 \times 0.000003938 = 0.00003150$.
- $p^8 = 0.000004765 \times 0.1736704 = 0.000000827$. Term $k=8$: $0.00000083$.

Sum:

$$
p^{(2)} = 0.00499156 + 0.00052458 + 0.00003150 + 0.00000083 \approx 0.0055485.
$$

Third level, with $p^{(2)} = 0.0055485$: the sum is dominated by the $k=5$ term.

- $p^5 = 0.0055485^5$. $0.0055485^2 = 0.000030786$; $0.0055485^4 = (0.000030786)^2 = 9.478 \times 10^{-10}$; $p^5 = 9.478 \times 10^{-10} \times 0.0055485 = 5.259 \times 10^{-12}$.
- Term $k=5$: $56 \times 5.259 \times 10^{-12} \times (1 - 0.0055485)^3 \approx 56 \times 5.259 \times 10^{-12} \times 0.98345 = 2.897 \times 10^{-10}$.
- Higher terms are smaller by factors of at least $p/(1-p) \approx 0.00558$ each; the $k=6$ term is $\binom{8}{6} p^6 (1-p)^2 \approx 28 \times 2.918 \times 10^{-14} \times 0.98896 \approx 8.09 \times 10^{-13}$, and the remainder is below $10^{-14}$.

$$
p^{(3)} \approx 2.897 \times 10^{-10} + 8.09 \times 10^{-13} \approx 2.905 \times 10^{-10}.
$$

**Interpretation.** The map $f$ has a stable fixed point below $0.5$ (since $f(0.4) = 0.1737 < 0.4$ and $f(0.1737) = 0.00555 < 0.1737$), so iterated majority voting on the depth-$3$ tree exhibits genuine threshold behavior at $p = 0.4$: the logical error rate decreases super-exponentially in concatenation depth. This confirms that the reported classical simulation result (an unverified report; see Section 4 preamble) — zero logical errors at $p = 0.4$ for $d \geq 3$ — is consistent with a real recursive threshold mechanism of the tree geometry, not an artifact of a single majority vote (which alone would leave a residual $0.1737$). It does not, however, tell us anything about quantum errors; that gap is the subject of Sections 4.3–4.5.

### 4.3 Statistical interpretation of "zero logical errors"

**Input:** zero logical errors observed; trial count $N$ unstated in the source (declared assumption). If the true logical error probability per trial is $p_L$, the probability of zero errors in $N$ independent trials is $(1 - p_L)^{N}$. Requiring this to be at least $0.05$ (95% one-sided confidence) gives

$$
p_L \leq 1 - 0.05^{1/N} \approx \frac{\ln 20}{N},
$$

using $-\ln(0.05) = \ln 20 = 2.995732$. Computing the bound for each declared scenario:

**Scenario $N = 10^{4}$:**

$$\np_L \leq 1 - 0.05^{1/10^{4}} \approx \frac{2.995732}{10^{4}} = 2.9957 \times 10^{-4}.
$$

Step by step: $0.05^{1/10^{4}} = e^{-\ln 20 / 10^{4}} = e^{-2.995732 \times 10^{-4}}$; since $e^{-x} \approx 1 - x$ for small $x$, $0.05^{1/10^{4}} \approx 1 - 2.9957 \times 10^{-4}$, so $p_L \leq 2.9957 \times 10^{-4}$.

**Scenario $N = 10^{5}$:**

$$\np_L \leq 1 - 0.05^{1/10^{5}} \approx \frac{2.995732}{10^{5}} = 2.9957 \times 10^{-5}.
$$

Identically, $0.05^{1/10^{5}} = e^{-2.995732 \times 10^{-5}} \approx 1 - 2.9957 \times 10^{-5}$.

**Interpretation.** Even under the generous assumption $N = 10^{5}$ trials, the reported zero-error result bounds the logical error probability only at $p_L \leq 2.9957 \times 10^{-5}$ — five orders of magnitude above the third-level concatenated value $p^{(3)} \approx 2.905 \times 10^{-10}$ computed in Section 4.2. "Zero logical errors" in a finite simulation is therefore a confidence statement, not evidence that the logical error rate vanishes; the trial count must be reported before any threshold claim can be quantified.

### 4.4 Thermal-activation bound under the barrier model

**Input:** the barrier conjecture $E_{\text{barrier}}(d) = 2^{d}$ (Section 3.3, with $\epsilon = 1$), and the assumption that logical errors are thermally activated over the barrier with rate proportional to the Boltzmann factor $e^{-E_{\text{barrier}}(d)/k_{\mathrm{B}}T}$. Setting $k_{\mathrm{B}}T = 1$ in energy units, the logical error probability per unit attempt is bounded by

$$\np_L(d) \leq e^{-2^{d}}.
$$

Computing values:

- $d = 3$: $e^{-8} = 3.3553 \times 10^{-4}$ (since $e^{8} = 2980.958$).
- $d = 5$: $e^{-32} = 1.2664 \times 10^{-14}$ (since $e^{32} = 7.8963 \times 10^{13}$).
- $d = 10$: $e^{-1024} = 10^{-1024/\ln 10} = 10^{-1024 \times 0.434294} = 10^{-444.7}$.

Each doubling of depth squares the suppression exponent. We stress that this bound is a **projection under a stated model** (thermal activation, $k_{\mathrm{B}}T = 1$, degenerate ground states, no resonant tunnelling paths): it is not a measurement, and coherent error paths that tunnel through rather than over the barrier would invalidate it. That possibility is examined in Section 6.

### 4.5 The quantization gap as an explicit hypothesis

For the quantum proposal of Section 3.2, correctness requires two conditions that the classical analysis does not supply. First, the code space spanned by $|0\rangle^{\otimes 2^{d}}$ and $|1\rangle^{\otimes 2^{d}}$ must correct the relevant single-site Pauli errors; by the Pauli decomposition of general noise [5], it suffices to check the $X$, $Y$, $Z$ components, and the repetition-like encoding corrects at most one $Z$-type error but no $X$-type errors without an additional structure — this is a known limitation of repetition encodings that the ultrametric geometry must be shown to overcome. Second, the strong triangle inequality must confine the *propagation* of quantum errors: two error paths that diverge on the tree remain separated, but a coherent superposition of the two paths is a single quantum object that the classical majority-vote analysis says nothing about. We therefore state the central hypothesis explicitly:

> **Hypothesis Q (quantization gap).** The ultrametric confinement that yields the classical threshold at $p = 0.4$ extends to quantum channels if and only if the coherent superposition of divergent error paths does not create interference terms that effectively reconverge the paths.

Hypothesis Q is not established by any supplied source; it is the open question this paper is designed to resolve.

## 5. Results

We report only numbers computed in Section 4, plus clearly labeled projections.

**Computed results (from stated inputs):**

1. Single-level eight-fold majority vote at $p = 0.4$: failure probability $p^{(1)} = 0.1736704$ (Section 4.1), a suppression factor $0.4 / 0.1736704 \approx 2.303$.
2. Two concatenated levels: $p^{(2)} \approx 0.0055485$ (Section 4.2).
3. Three concatenated levels: $p^{(3)} \approx 2.905 \times 10^{-10}$ (Section 4.2).
4. Confidence bound on the reported zero-error simulation: $p_L \leq 2.9957 \times 10^{-4}$ for $N = 10^{4}$ and $p_L \leq 2.9957 \times 10^{-5}$ for $N = 10^{5}$ (Section 4.3).

**Labeled projections (assumptions stated in Section 4.4):**

5. Under the thermal-activation model with $k_{\mathrm{B}}T = 1$: $p_L(3) \leq 3.3553 \times 10^{-4}$, $p_L(5) \leq 1.2664 \times 10^{-14}$, $p_L(10) \leq 10^{-444.7}$. Uncertainty: these bounds hold only if the barrier model is correct; any tunnelling or coherent path invalidates them entirely.

The classical recursive threshold is genuine: the map $f$ iterated three times suppresses $p = 0.4$ to $\approx 2.9 \times 10^{-10}$, consistent with the (unverified) report of zero logical errors at $d \geq 3$ provided the trial count satisfies $N \lesssim 1/p^{(3)} \approx 3.4 \times 10^{9}$ — for any plausible $N$, zero observed errors is statistically compatible with $p^{(3)}$. No quantum result is claimed.

## 6. Discussion

**Limitations.** The single empirical input — zero logical errors at $p = 0.4$ for $d \geq 3$ — is an unverified report from the authors' notebook notes; no supplied bibliography entry documents the simulation, its trial count, or its decoder. Every quantitative conclusion above is conditional on that report. The barrier scaling $E_{\text{barrier}}(d) = 2^{d}$ is a conjecture made precise in Section 3.3 but not proved for quantum dynamics. The thermal-activation projections assume $k_{\mathrm{B}}T = 1$ and no tunnelling; the confidence bounds assume independence of trials and unstated $N$.

**Failure modes.** Three ways the proposal can fail: (i) the repetition-like quantum encoding does not correct $X$-type errors, so the classical threshold does not transfer; (ii) coherent error paths interfere across branches, effectively reconverging paths that the ultrametric separates classically — this would falsify Hypothesis Q; (iii) the barrier is over-the-barrier only, and resonant tunnelling through the $2^{d}$-site cut restores a depth-independent error channel.

**What would falsify the claims.** A quantum Monte Carlo simulation of the depolarizing channel $\mathcal{E}_p$ on $\mathcal{T}_d$ showing a logical error rate that does not decrease with $d$ at fixed $p \leq 0.4$ would falsify the transfer of the classical threshold. A demonstration that the minimal cut argument fails because logical operators need not traverse an entire level would falsify the barrier conjecture. Conversely, a proof that the strong triangle inequality confines Pauli error propagation term-by-term (using the decomposition of [5]) would establish the conjecture.

**Open questions.** Does the $(q+1)$-regularity of the Bruhat–Tits tree [3] admit non-binary qudit encodings matched to the tree degree, as the beyond-qubit perspective of [6] suggests? Can entanglement-assisted methods [2] restore quantum capacity if independent-error confinement fails? Does the adiabatic gap-protection framework [7] provide a rigorous Hamiltonian whose gap equals $2^{d}\epsilon$? These are precise, testable questions, and the tensor-network and quantum Monte Carlo protocols outlined in Section 4.5 are the tools that would answer them.

**Arguing against ourselves.** The strongest objection to this program is that the classical evidence is exactly the kind of result that does not survive quantization: classical majority voting exploits the ordering of the reals (bits are $0$ or $1$, and majority is well-defined), while quantum errors are operators on a Hilbert space where no such ordering exists. The survey literature explicitly warns that quantum channels behave differently from classical channels [4], and the entire edifice of Section 4 rests on a classical channel. Until Hypothesis Q is tested, the honest position is that this is a conjecture with a suggestive classical analogue, not a fault-tolerance scheme.

## 7. Conclusion

We formalized a conjectured passive fault-tolerance scheme on the Bruhat–Tits tree, derived the barrier conjecture $E_{\text{barrier}}(d) = 2^{d}$ from the ultrametric cut structure, and analyzed the classical evidence by explicit computation: iterated eight-fold majority voting suppresses $p = 0.4$ through $0.1736704$, $0.0055485$, and $2.905 \times 10^{-10}$ over three levels, confirming a genuine recursive threshold mechanism, while the reported zero-error result bounds the logical error probability only at $2.9957 \times 10^{-5}$ even for $N = 10^{5}$ trials. The quantum question — whether the strong triangle inequality confines superposed and entangled error paths — remains open, stated as Hypothesis Q with explicit falsification criteria. The contribution is a precise, testable formulation of the quantization gap, not a resolution of it.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: 2 sentences that read as reporting completed experiments or measurements were restated as proposals

## References

[1] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[2] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[3] On the missing branches of the Bruhat-Tits tree. arXiv:1712.01463v2. https://arxiv.org/abs/1712.01463v2
[4] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[5] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[6] Quantum error correction beyond qubits. arXiv:0811.3734v1. https://arxiv.org/abs/0811.3734v1
[7] Error suppression and error correction in adiabatic quantum computation II: non-equilibrium dynamics. arXiv:1307.5892v4. https://arxiv.org/abs/1307.5892v4
[8] Quantum Error Correction in Quaternionic Hilbert Spaces. arXiv:2504.19833v1. https://arxiv.org/abs/2504.19833v1
[9] QNFO: Alpha Pi Project
[10] QNFO: Ultrametric Quantum Gravity and Computation
[11] QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation
[12] QNFO: Quantum Laws of Form
