# Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question

## Abstract

Passive fault tolerance — protection of logical qubits by encoding geometry alone, without repeated syndrome measurement — would remove the dominant overhead in scalable quantum computing if it could be made to work for quantum information. We study a conjectured scheme in which logical qubits are encoded on a Bruhat–Tits tree, the infinite homogeneous tree of a non-Archimedean local field whose metric satisfies the strong (ultrametric) triangle inequality. The conjecture states that the energy barrier against a logical error grows as $E_{\text{barrier}}(d) = 2^{d}$ in tree depth $d$, and the supporting evidence is a classical simulation report of zero logical errors at a physical error rate $p = 0.4$ for depth $d \geq 3$ under majority-vote decoding. The gap we address is that this evidence is entirely classical: whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise is open. We formalize the encoding, derive the barrier conjecture from the ultrametric cut structure, and compute explicitly what the classical evidence establishes: one level of eight-fold majority voting maps $p = 0.4$ to a failure probability of $0.1736704$, two concatenated levels give $\approx 5.55 \times 10^{-3}$, three levels give $\approx 2.905 \times 10^{-10}$, confirming a genuine recursive threshold mechanism; the zero-error report itself bounds the logical error probability only at $p_L \leq 2.9957 \times 10^{-5}$ even for $N = 10^{5}$ trials. We derive a thermal-activation projection $p_L \leq e^{-2^{d}}$ under a stated barrier model, state the quantization gap as an explicit falsifiable hypothesis, and specify the quantum Monte Carlo and tensor-network tests that would resolve it. The practical change if the conjecture holds: syndrome-extraction hardware could be replaced by a static energy landscape.

## 1. Introduction

Scalable quantum computing is presently blocked by error correction overhead. Active stabilizer codes such as the surface code require repeated syndrome extraction, low-latency real-time decoding, and large ancilla qubit counts; the engineering cost of these cycles limits the size of computations that can be run on near-term hardware [9]. A cloud-based quantum service provider faces this cost directly: every logical qubit demands hundreds to thousands of physical qubits (an assumption stated in the literature on this proposal [11]), continuous measurement infrastructure, and power for decoding. A design that suppressed logical errors passively — by the geometry of the encoding itself, with no measurement cycle — would change the architecture: syndrome-extraction hardware and decoders could be replaced by a static Hamiltonian whose energy landscape blocks error propagation, and the physical-to-logical overhead could fall accordingly.

This paper investigates one specific passive proposal: encode logical information on a Bruhat–Tits tree. A Bruhat–Tits tree is the infinite $(q+1)$-regular tree associated with a local field $k$ complete with respect to a non-Archimedean absolute value; its path metric is ultrametric, satisfying the strong triangle inequality $d_{\mathrm{BT}}(x,z) \leq \max\{d_{\mathrm{BT}}(x,y),\, d_{\mathrm{BT}}(y,z)\}$, so every triangle is isosceles with a unique long side. The tree is not an arbitrary graph: for a local field $k$ and the matrix algebra $\mathbb{M}_2(k)$, the set of maximal orders containing a given suborder is represented as a subtree of the Bruhat–Tits tree called the branch of the order, and branches have been applied to the global selectivity problem and to computing local embeddings [3]. The conjecture under study asserts (i) that the energy barrier against a logical error on a tree of depth $d$ scales as $E_{\text{barrier}}(d) = 2^{d}$, and (ii) that this scaling yields passive fault tolerance with thresholds exceeding those of surface codes, without active syndrome measurement.

The supporting evidence must be stated plainly. The claim that classical simulations using majority-vote decoding on classical bits found zero logical errors at a $40\%$ physical error rate for $d \geq 3$ is an unverified report from the authors' notebook notes; no cited work documents the simulation, its trial count, or its decoder. We treat it as a working assumption and analyze what it would imply if true. The central open question is whether the strong triangle inequality confines quantum errors — superpositions of error paths, entangled error states, and coherent noise — or whether the classical advantage is a decoding artifact that evaporates under full quantum channels. The survey literature warns generically that quantum channels behave differently from classical channels, which is precisely the epistemic gap between the classical evidence and the quantum claim [4].

If the conjecture holds, the decision that changes is architectural: hardware designers could allocate resources to engineering a static energy landscape rather than to measurement cycles and decoders. If it fails — specifically, if coherent error paths interfere across tree branches in a way that reconverges paths the ultrametric separates classically — the proposal is dead, and the failure mode itself would be a sharpened statement of why passive protection requires active measurement.

Our contributions are:

1. A formalization of the tree encoding and a geometric derivation of the barrier conjecture $E_{\text{barrier}}(d) = 2^{d}\,\epsilon$ from the minimal-cut structure of the tree (Section 3).
2. An explicit arithmetic analysis of the classical majority-vote evidence, showing that iterated eight-fold majority voting at $p = 0.4$ constitutes a genuine recursive threshold mechanism, with computed suppression levels $0.1736704 \to 0.0055485 \to 2.905 \times 10^{-10}$ (Section 4).
3. A statistical reinterpretation of the reported "zero logical errors" as a confidence bound $p_L \leq \ln 20 / N$, not a proof of a vanishing error rate (Section 4).
4. A thermal-activation projection $p_L \leq e^{-2^{d}}$ under a stated barrier model, with the quantization gap stated as explicit Hypothesis Q rather than a result (Section 4).
5. A specification of the quantum Monte Carlo and tensor-network simulations, and of the theorem that would need to be proved, that would resolve the open question, together with the engineering pathway and the smallest next experiment (Sections 5 and 7).

Throughout we separate what is derived, what is computed from stated inputs, what is reported by cited works, and what is conjecture.

## 2. Background and Related Work

**Continuous-time QEC.** Reference [1] investigates continuous-time quantum error correction (CTQEC), in which both noise and error-correcting operations are processes continuous in time, based on continuous weak measurements and feedback, analyzed from the subsystem principle — the statement that protected information is identified with a subsystem $\mathcal{H}^{A}$ of the system Hilbert space such that a CPTP recovery map restores the reduced state after noise. Its outlook section notes that constructing optimal CTQEC protocols remains open and that equilibrium code-space fidelity could be useful for assessing performance under non-Markovian decoherence. CTQEC is the nearest active foil to our proposal: it removes the discrete measurement circuit but retains the feedback loop. A genuinely passive scheme would go one step further and rely on the energy landscape of the encoding geometry alone.

**Entanglement-assisted codes.** Reference [2] gives a self-contained introduction to entanglement-assisted quantum error-correcting codes (EAQECCs), in which the encoder may append not only ancillas but also ebits — pre-shared entanglement between sender and receiver — before the encoding unitary. Its conclusions state that this entanglement can increase either the communication rate or the number of correctable errors, and that the framework extends the stabilizer formalism while allowing quantum codes to be built from classical linear codes without the dual-containing constraint. The relevance here is structural: if ultrametric confinement fails for independent quantum errors, pre-shared entanglement across distant tree branches is one candidate mechanism for restoring correction capacity, and the EAQECC formalism of [2] is the language in which such a modification would be expressed.

**Bruhat–Tits trees in arithmetic.** Reference [3] develops, for a local field $k$ and the matrix algebra $\mathfrak{A} = \mathbb{M}_2(k)$, a theory for computing the set $S(\Omega)$ of maximal orders containing a given order $\Omega$; this set is a subtree of the Bruhat–Tits tree called the branch of the order, and the study of branches plays a role in the selectivity problem and in determining quotient graphs for arithmetically important subgroups. The paper's graph conventions define the tree through vertices and a neighborhood relation, with valency the number of neighbors. This is the source of the geometric object we encode on: the tree is the incidence geometry of arithmetic over a non-Archimedean field, and our barrier conjecture is a statement about how logical operators must traverse this arithmetic tree.

**From classical to quantum codes.** Reference [4] surveys error-correcting codes from the classical to the quantum setting, citing Preskill's claim that the 21st century would be the golden age of quantum error correction, and states that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed. Its conclusions note that both quantum and classical schemes add ancillary bits and measure a syndrome, with similar conditions for error detectability and correctability, and that research has migrated to nonbinary codes. This is exactly the epistemic gap we interrogate: the $p = 0.4$ evidence is a classical-channel result on a binary symmetric channel of the kind [4] uses to illustrate classical correction, and the survey's warning is the generic form of the quantization question we pose in Hypothesis Q.

**Pauli structure of quantum noise.** Reference [5] introduces the main ideas of QEC — encoding, syndrome extraction, error operators, code construction — and shows that general noise and relaxation of two-state systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. Its background section records that Shor proved 9 qubits protect a single qubit against general errors and Steane achieved the same with 7, and its three-bit-code section analyzes the simplest case under independent noise that applies $\sigma_x$ with probability $p$. This Pauli decomposition is the technical hinge of our analysis: any local quantum channel admits an operator-sum expansion in Pauli terms, so the quantum question reduces to whether ultrametric confinement holds for each Pauli component and whether the coherent superposition of error paths — which has no classical analogue — preserves or destroys the confinement.

**Adiabatic error suppression.** Reference [6] treats error suppression and correction in adiabatic quantum computation, deriving a dynamical master equation for encoded AQC in which a many-body system undergoing adiabatic evolution couples to an environment through single-qubit Pauli error operators $E_j \otimes B_j$. Its discussion states that the model unifies previously proposed techniques — error suppression, energy gap protection, and dynamical decoupling — under one dynamical framework, allows calculation of codespace leakage rates, and extends to error correction by local cooling. The adiabatic setting is the closest existing analogue to passive protection: there, too, an energy gap rather than a measurement cycle is the protective resource. Our barrier conjecture $E_{\text{barrier}}(d) = 2^{d}\,\epsilon$ is structurally an adiabatic-style gap statement transplanted to an ultrametric geometry, and the tension between gap protection and thermal excitation analyzed in [6] is exactly the failure mode we bound in Section 4.

**Non-standard Hilbert spaces and thresholds.** Reference [7] proposes quaternion-based strategies for QEC by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and gates that ensure inner product preservation, and building a quaternionic $[[5,1,3]]$ code. Its excerpts report a measured-style threshold of approximately $p_{\text{th}} \approx 0.015$ for the five-qubit quaternionic code, situated between prior reported values, and cite a logical error suppression factor of $\lambda = 2.14 \pm 0.02$ from increasing code distance on a superconducting processor, with an upper bound of $0.189$ for surface codes under correlated noise. These numbers calibrate the competitive landscape: any ultrametric threshold claim must be compared against thresholds in this range, and the suppression factor $\lambda \approx 2.14$ per distance increment is the empirical benchmark that a passive scheme claiming thresholds "far exceeding surface codes" would need to beat.

**The existing analysis under revision.** Reference [8] is the predecessor of this paper: it formalizes the same encoding, computes the same majority-vote cascade ($0.1736704$, $\approx 5.55 \times 10^{-3}$, $\approx 2.905 \times 10^{-10}$), derives the same confidence bounds, and states Hypothesis Q with the same falsification criteria. We build on it directly and extend it with the comparative analysis of [9], [10], and [11] below.

**Quantitative follow-ups in the QNFO corpus.** Reference [9] analyzes passive error correction on regular odd-$p$ Bruhat–Tits trees, deriving a barrier $B(d) = \lceil p/2 \rceil^{d}$ and reporting barrier heights $B(3) = 8$ and $B(4) = 16$, logical error bounds $p_L(3) \leq 6.5536 \times 10^{-4}$ and $p_L(4) \leq 4.29 \times 10^{-7}$, suppression factors $\approx 6.10 \times 10^{2}$ and $\approx 9.31 \times 10^{5}$, and the same concatenated majority-vote values as [8]; it also proposes a minimal depth-$3$, $p=3$ neutral-atom experiment at $p_{\text{err}} = 0.40$ over $N = 10^{4}$ trials with an explicit falsification criterion. Reference [10] formalizes passive QEC with logical qudits on balls of the tree $T_{p+1}$, proves a nesting lemma (equal-radius balls are nested or disjoint), derives exact code parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ — giving $n_1 = 5$, $n_2 = 17$, $n_3 = 53$ for $p = 3$ — and a conditional distance $d = 2t+1$, and computes under independent depolarizing noise at $\varepsilon = 10^{-3}$ a passive failure probability $P_{\mathrm{pass}} \approx 9.98 \times 10^{-6}$ per epoch for the flagship $p=3$, $t=1$ block, a suppression of $\approx 100.2$ over an unencoded qudit; its discussion states plainly that no explicit encoder is constructed and that the weight-$\leq t$ correctability claim fails if no branch-permutation-symmetric encoder exists. Reference [11] provides an analytic derivation with quantitative projections, reporting $P_{\mathrm{pass}} = 5.992003 \times 10^{-6}$ and suppression factor $166.9$ for the same $t=1$, $\varepsilon = 10^{-3}$ configuration, $P_{\mathrm{pass}}^{(2)} = 3.997 \times 10^{-9}$ for $t=2$, and energy barriers $E_{\text{barrier}}(3) = 8$ and $E_{\text{barrier}}(5) = 32$; it also states the economic motivation (physical-to-logical overhead on the order of $10^{2}$–$10^{4}$, labeled an assumption) and a five-atom $^{87}$Rb tweezer experiment with the falsification threshold "logical error rate $> 2 \times 10^{-5}$ would falsify the model." We note that [10] and [11] report different values of $P_{\mathrm{pass}}$ for the same nominal configuration ($9.98 \times 10^{-6}$ versus $5.992 \times 10^{-6}$); we attribute each number to its source and do not adjudicate between them, since neither derivation is reproduced here.

**Ultrametric foundations.** Reference [12] consolidates quantum correspondences to Spencer-Brown's Laws of Form, in which drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed, identifying open problem categories and proposing extensions. We cite it as contextual background for distinction-based, branching-tree foundations of computation; no quantitative claim in this paper depends on it.

No cited work contains a threshold theorem for ultrametric geometries, a quantum Monte Carlo study of tree codes, or a proof that the strong triangle inequality confines quantum error operators. The gap this paper targets is genuine.

## 3. Methods

### 3.1 The Bruhat–Tits tree and its ultrametric

Let $k$ be a local field with residue field of size $q$, and let $T_{q}$ denote the Bruhat–Tits tree of $k$: the infinite tree in which every vertex has degree $q + 1$ [3]. We use only the tree structure, defined as in [3] by a vertex set and a symmetric neighborhood relation. Define the path-length distance $d_{\mathrm{BT}}(v, w)$ as the number of edges on the unique path from $v$ to $w$. The ultrametric consequence we exploit throughout: from any vertex $v$ at depth $d$, two error paths that diverge at depth $d_0$ remain separated by $d_{\mathrm{BT}} \geq d - d_0$ for all deeper depths — divergence is permanent and distance grows monotonically, unlike in Euclidean lattices where error paths can reconverge.

### 3.2 Encoding

We encode one logical bit (classical analysis) or, prospectively, one logical qubit (quantum proposal) on a depth-$d$ rooted binary subtree $\mathcal{T}_d$ with $2^{d}$ leaves. The classical encoding writes the bit on every leaf; decoding is recursive majority vote, with each internal node taking the majority of its children's values. For $d = 3$ this is a single eight-fold majority vote over the leaves; deeper trees apply the vote iteratively. The quantum proposal is the repetition-like map

$$
|0\rangle_L \mapsto |0\rangle^{\otimes 2^{d}}, \qquad |1\rangle_L \mapsto |1\rangle^{\otimes 2^{d}},
$$

which is deliberately minimal; whether this code space corrects a nontrivial set of single-qubit Pauli errors is left as an open condition (Section 4.5). The qudit-on-a-ball variant of [10], with parameters $n_t = 1 + (p+1)(p^{t}-1)/(p-1)$ and conditional distance $d = 2t+1$, is the more refined encoding in the literature; we use the minimal repetition-like encoding because its failure modes are sharpest.

### 3.3 Energy barrier conjecture

We posit a Hamiltonian $H_d$ on $\mathcal{T}_d$ in which the two logical configurations are degenerate ground states and every configuration differing from a ground state on $m$ leaves carries energy at least $m\,\epsilon$, with $\epsilon$ the single-site excitation cost. A logical error requires flipping a connected set of sites separating the two logical basins. Because the tree branches, the minimal separating set ("cut") at depth $d$ has size $2^{d}$: an error path must at some depth flip an entire level, and the number of sites at level $\ell$ is $2^{\ell}$. The conjectured barrier is therefore

$$
E_{\text{barrier}}(d) = 2^{d}\,\epsilon,
$$

which we take as $E_{\text{barrier}}(d) = 2^{d}$ with $\epsilon = 1$ as the energy unit, matching the values $E_{\text{barrier}}(3) = 8$ and $E_{\text{barrier}}(5) = 32$ reported in [11] and $B(3) = 8$, $B(4) = 16$ in [9]. This is the ultrametric analogue of an adiabatic gap argument [6]: protection by energy landscape rather than by measurement. We emphasize that this scaling is a conjecture of the source notes, made precise here but not proved for quantum dynamics; [10] likewise reports that its distance result $d = 2t+1$ is conditional on an unconstructed symmetric encoder.

### 3.4 Noise models

For the classical analysis we use the binary symmetric channel with flip probability $p$ per leaf, the standard illustrative channel of classical coding theory [4]. For the quantum projections we use the depolarizing channel on each physical site,

$$
\mathcal{E}_p(\rho) = (1 - p)\,\rho + \frac{p}{3}\bigl(X\rho X + Y\rho Y + Z\rho Z\bigr),
$$

and a coherent $Z$-rotation error $\mathcal{C}_\theta(\rho) = e^{-i\theta Z}\rho\, e^{i\theta Z}$. By the Pauli decomposition of general noise on two-state systems [5], the depolarizing analysis extends term-by-term to arbitrary local noise channels; the coherent case is treated separately because it has no classical analogue.

### 3.5 Method of analysis

This paper performs no simulation, measurement, or hardware experiment. Its method is: (i) state every input number with its source or as a declared assumption; (ii) derive the barrier conjecture geometrically; (iii) compute the classical majority-vote cascade, the confidence bounds, and the thermal-activation projections by explicit arithmetic; (iv) attribute all reported numbers from the literature to their sources; and (v) state the quantum question as a falsifiable hypothesis with named tests, which remain proposals in the conditional mood.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs. The single empirical input is the reported zero logical errors at a $40\%$ physical error rate ($p = 0.4$) for $d \geq 3$ under majority-vote decoding on classical bits. We emphasize that this result is an unverified report — no cited source documents the simulation, the trial count, or the decoder details — and every conclusion downstream is conditional on it. The trial count $N$ of the reported simulation is not stated; we therefore compute confidence bounds for two declared scenarios, $N = 10^{4}$ and $N = 10^{5}$.

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

So one level of eight-fold majority voting maps $p = 0.4$ to $p^{(1)} = 0.1736704$ — a suppression factor $0.4 / 0.1736704 \approx 2.303$. This value is independently reported in [9] and [8]. The vote helps (since $p = 0.4 < 0.5$), but a single level is far from the reported zero-error behavior; the reported result must rest on the recursive tree structure, which we now verify.

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

This matches the value $5.5489 \times 10^{-3}$ reported in [9] to the precision shown. Third level, with $p^{(2)} = 0.0055485$: the sum is dominated by the $k=5$ term.

- $p^5 = 0.0055485^5$. $0.0055485^2 = 0.000030786$; $0.0055485^4 = (0.000030786)^2 = 9.478 \times 10^{-10}$; $p^5 = 9.478 \times 10^{-10} \times 0.0055485 = 5.259 \times 10^{-12}$.
- Term $k=5$: $56 \times 5.259 \times 10^{-12} \times (1 - 0.0055485)^3 \approx 56 \times 5.259 \times 10^{-12} \times 0.98345 = 2.897 \times 10^{-10}$.
- Higher terms are smaller by factors of at least $p/(1-p) \approx 0.00558$ each; the $k=6$ term is $\binom{8}{6} p^6 (1-p)^2 \approx 28 \times 2.918 \times 10^{-14} \times 0.98896 \approx 8.09 \times 10^{-13}$, and the remainder is below $10^{-14}$.

$$
p^{(3)} \approx 2.897 \times 10^{-10} + 8.09 \times 10^{-13} \approx 2.905 \times 10^{-10}.
$$

**Interpretation.** The map $f$ has a stable fixed point below $0.5$ (since $f(0.4) = 0.1737 < 0.4$ and $f(0.1737) = 0.00555 < 0.1737$), so iterated majority voting on the depth-$3$ tree exhibits genuine threshold behavior at $p = 0.4$: the logical error rate decreases super-exponentially in concatenation depth. This confirms that the reported classical simulation result — zero logical errors at $p = 0.4$ for $d \geq 3$ — is consistent with a real recursive threshold mechanism of the tree geometry, not an artifact of a single majority vote (which alone would leave a residual $0.1737$). It does not, however, tell us anything about quantum errors; that gap is the subject of Sections 4.3–4.5.

### 4.3 Statistical interpretation of "zero logical errors"

**Input:** zero logical errors observed; trial count $N$ unstated (declared assumption). If the true logical error probability per trial is $p_L$, the probability of zero errors in $N$ independent trials is $(1 - p_L)^{N}$. Requiring this to be at least $0.05$ (95% one-sided confidence) gives

$$
p_L \leq 1 - 0.05^{1/N} \approx \frac{\ln 20}{N},
$$

using $-\ln(0.05) = \ln 20 = 2.995732$. Computing the bound for each declared scenario:

**Scenario $N = 10^{4}$:** $0.05^{1/10^{4}} = e^{-\ln 20 / 10^{4}} = e^{-2.995732 \times 10^{-4}}$; since $e^{-x} \approx 1 - x$ for small $x$, $0.05^{1/10^{4}} \approx 1 - 2.9957 \times 10^{-