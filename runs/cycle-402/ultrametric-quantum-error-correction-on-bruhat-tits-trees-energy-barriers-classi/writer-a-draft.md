# Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question

## Abstract

We study a conjectured passive fault‑tolerance scheme in which logical qubits are encoded on a Bruhat–Tits tree, the infinite homogeneous tree associated with a non‑Archimedean local field, whose natural metric satisfies the strong (ultrametric) triangle inequality. The conjecture states that the energy barrier against a logical error grows as $E_{\text{barrier}}(d)=2^{d}$ in tree depth $d$, yielding passive protection without active syndrome extraction, with thresholds allegedly exceeding those of surface codes. A study would propose that, under majority‑vote decoding on classical bits, zero logical errors occur at a physical error rate of $p=0.4$ for depth $d\geq3$. We formalize the encoding, derive the barrier scaling from the ultrametric geometry, and analyze by explicit computation what the classical evidence does and does not establish: one level of eight‑fold majority voting maps $p=0.4$ to a failure probability of $0.1736704$, two concatenated levels give $\approx5.55\times10^{-3}$, and three levels give $\approx2.9\times10^{-10}$, confirming a genuine recursive threshold mechanism. We reinterpret “zero logical errors’’ as a confidence bound rather than proof of a vanishing error rate, derive a thermal‑activation bound $e^{-2^{d}}$ under a stated barrier model, and identify the central open question: whether the strong triangle inequality confines quantum errors—superpositions, entanglement, coherent noise—or whether the advantage evaporates under full quantum channels. We give labeled projections under declared assumptions, state falsification criteria, and outline the quantum Monte‑Carlo and tensor‑network tests that would settle the question.

## 1. Introduction

Quantum error correction (QEC) protects fragile superposition states from decoherence, and its discovery transformed quantum information from an academic curiosity into a developing engineering discipline [6]. The dominant architectural paradigm — stabilizer codes with repeated syndrome measurement, exemplified by the surface code — achieves fault tolerance actively, at the cost of a large overhead of ancilla qubits, measurement circuits, and real‑time decoding. A passive alternative, in which the geometry of the encoding itself suppresses errors without measurement, would be architecturally transformative if it could be made to work for quantum information and not merely classical bits.

This paper investigates a specific passive proposal: encode logical qubits on a Bruhat–Tits tree. A Bruhat–Tits tree is the infinite $(q+1)$‑regular tree associated with a local field $k$ (a field complete with respect to a non‑Archimedean, or $p$‑adic, absolute value); its geometry is ultrametric, meaning that distances satisfy the strong triangle inequality $d_{\mathrm{BT}}(x,z)\le\max\{d_{\mathrm{BT}}(x,y),\,d_{\mathrm{BT}}(y,z)\}$, so that every triangle is isosceles with the long side unique. Ultrametricity has been argued to underlie hierarchical structure far beyond number theory; in particular, positional notation itself has been described as an ultrametric tree of nested cycles, with the Archimedean real line a derived abstraction rather than the primitive object [11]. The Bruhat–Tits tree is the canonical geometric realization of this hierarchy: sub‑orders of the matrix algebra $M_{2}(k)$ correspond to subtrees (“branches”) of the tree, and these branches have been used to study the global selectivity problem and to compute local embeddings [3].

The conjecture under study, due to the author's notebook notes, is twofold: (i) the energy barrier against a logical error on a tree of depth $d$ scales as $E_{\text{barrier}}(d)=2^{d}$; and (ii) this scaling yields passive fault tolerance with error thresholds far exceeding surface codes, without active syndrome measurement. The supporting evidence is classical, and its status must be stated plainly: the claim that simulations using majority‑vote decoding on classical bits found zero logical errors at $40\%$ physical error rates for $d\geq3$ is an unverified report from the authors' notebook notes. No supplied bibliography entry documents this simulation; we treat it as a working assumption and analyze what it would imply if true. The central open question, stated frankly, is whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise, or whether the observed advantage is a classical decoding artifact.

Our contributions are:

1. A formalization of the tree encoding and a geometric statement of the barrier conjecture $E_{\text{barrier}}(d)=2^{d}$ (Section 3).  
2. An explicit arithmetic analysis of the classical majority‑vote evidence, showing that iterated majority voting on an eight‑leaf tree constitutes a genuine recursive threshold mechanism at $p=0.4$, with computed suppression levels (Section 4).  
3. A statistical reinterpretation of “zero logical errors’’ as a confidence bound, not a proof of a vanishing error rate (Section 4).  
4. A bounding analysis of the quantum regime under a thermal‑activation model, with the quantization gap stated as explicit hypotheses rather than results, together with labeled projections (Sections 4 and 5).  
5. A specification of the quantum Monte‑Carlo and tensor‑network simulations, and of the theorem that would need to be proved, that would resolve the open question (Sections 5 and 6).

We are careful throughout to separate what is derived, what is computed, what is reported by the source simulations, and what is conjecture. The paper's honest conclusion is that the classical evidence is real but classical, and that the quantum question remains open in a precise, testable sense.

## 2. Background and Related Work

**Continuous‑time QEC.** Reference [1] investigates continuous‑time quantum error correction (CTQEC), in which both the noise and the error‑correcting operations are treated as processes continuous in time, based on continuous weak measurements and feedback, analyzed from the point of view of the subsystem principle — the statement that protected quantum information is identified with a subsystem of the full system. CTQEC is the natural foil to our passive proposal: it removes the discrete measurement circuit but retains active feedback. A genuinely passive scheme would go one step further, removing even the feedback loop and relying on the energy landscape of the encoding geometry.

**Entanglement‑assisted codes.** Reference [2] provides a self‑contained introduction to entanglement‑assisted quantum error‑correcting codes, which use shared entanglement between encoder and decoder as a resource. The supplied text shows that EAQECCs expand the usual paradigm by allowing ancillas and pre‑shared ebits, thereby increasing rate or correctable errors. The relevance to our setting is structural: if ultrametric confinement fails for independent quantum errors, sharing entanglement across distant branches of the tree is one candidate mechanism for restoring a quantum correction capacity, and the entanglement‑assisted framework is the standard language in which such a modification would be expressed.

**Bruhat–Tits trees in arithmetic.** Reference [3] develops a theory, for a local field $k$ and a matrix algebra $A$ over $k$, for computing the set of maximal orders in $A$ containing a given suborder; this set is represented as a subtree of the Bruhat–Tits tree called the branch of the order, and branches have been applied to the global selectivity problem and to computing local embeddings. This is the source of the geometric object we encode on: the tree is not an arbitrary graph but the incidence geometry of arithmetic over a non‑Archimedean field. Our conjectured barrier scaling is a statement about how logical operators must traverse this arithmetic tree.

**From classical to quantum codes.** Reference [4] surveys error‑correcting codes from the classical to the quantum setting, noting — citing Preskill’s claim that the 21st century would be the golden age of quantum error correction — that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed and offer lessons. This is precisely the epistemic gap our paper interrogates: the $40\%$‑error‑rate simulation is a classical‑channel result, and the survey’s warning that quantum channels behave differently is the generic form of the quantization question we pose.

**Pauli structure of quantum noise.** Reference [5] introduces the main ideas of QEC — encoding, extraction of syndromes, error operators, and code construction — and shows that general noise and relaxation of a set of two‑state quantum systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. This Pauli decomposition is the technical hinge of our analysis: any quantum channel admits an operator‑sum expansion in Pauli terms, so the quantum question reduces to whether ultrametric confinement holds for each Pauli component and, critically, whether the coherent superposition of error paths (which has no classical analogue) preserves or destroys the confinement.

**Beyond‑qubit encodings.** Reference [6] addresses quantum error correction beyond qubits, motivated by the need to protect fragile quantum superposition states from decoherence noise; the supplied summary emphasizes the general necessity of error correction for robust manipulation of quantum states and notes that the discovery of QEC turned quantum information into a developing field. Our tree encoding is qubit‑based, but the beyond‑qubit perspective matters for the quantization question: a tree‑encoded qudit system might interact with the ultrametric geometry differently than a two‑level system, and non‑binary alphabets could be matched to the $(q+1)$‑regularity of the Bruhat–Tits tree.

**Adiabatic error suppression.** Reference [7] treats error suppression and correction in adiabatic quantum computation, deriving a model for the dynamics of encoded adiabatic quantum computation and building on previously established techniques for error suppression in AQC, on the premise that encoding, suppression, and correction will be required to scale AQC. The adiabatic setting is the closest existing analogue to passive protection: there, too, an energy gap — rather than a measurement cycle — is the protective resource. Our barrier conjecture $E_{\text{barrier}}(d)=2^{d}$ is structurally an adiabatic‑style gap statement transplanted to an ultrametric geometry, and the adiabatic literature’s tension between gap protection and thermal excitation is exactly the failure mode we confront in Section 4.

**Non‑standard Hilbert spaces.** Reference [8] proposes quaternion‑based strategies for quantum error correction by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and quantum gates that ensure inner‑product preservation, with a simple encoding scheme mapping logical qubits into quaternionic systems. The supplied text shows that the Pauli‑operator framework of [5] admits generalizations to non‑standard inner‑product structures; our proposal is structurally analogous in replacing the Archimedean geometry of standard codes with a non‑Archimedean (ultrametric) geometry.

**Ultrametric foundations.** Reference [11] argues that positional notation is inherently an ultrametric tree of nested cycles and that the Archimedean line is a derived abstraction, with recovering the native ultrametric claimed to resolve cascading errors across mathematics, physics, epistemology, education, quantum computing, and interface design. We adopt from this thesis only the structural claim we need — that hierarchical, digit‑wise (tree‑wise) organization is the native setting for error propagation in positional systems — and we do not rely on the broader resolvent claims.

**Spencer‑Brown correspondence.** Reference [12] consolidates quantum correspondences to Spencer‑Brown’s Laws of Form, identifying open problem categories and proposing extensions. The supplied excerpt provides contextual background for distinction‑based (branching‑tree) foundations of computation; we cite it only as background.

No entry in the supplied bibliography contains a threshold theorem for ultrametric geometries, a quantum Monte‑Carlo study of tree codes, or a proof that the strong triangle inequality confines quantum error operators. The gap this paper targets is therefore genuine.

## 3. Methods

### 3.1 The Bruhat–Tits tree and its ultrametric

Let $k$ be a local field with residue field of size $q$, and let $T_{q}$ denote the Bruhat–Tits tree of $k$: the infinite tree in which every vertex has degree $q+1$ [3]. We use only the tree structure. Define the path‑length distance $d_{\mathrm{BT}}(v,w)$ as the number of edges on the unique path from $v$ to $w$. The ultrametric consequence we exploit throughout: from any vertex $v$ at depth $d$, two error paths that diverge at depth $d_{0}$ remain separated by $d_{\mathrm{BT}}\ge d-d_{0}$ for all deeper depths — divergence is permanent and distance grows monotonically, unlike in Euclidean lattices where paths can reconverge.

### 3.2 Encoding

We encode one logical bit (classical analysis) or, prospectively, one logical qubit (quantum proposal) on a depth‑$d$ rooted binary subtree $\mathcal{T}_{d}$ with $2^{d}$ leaves. The classical encoding writes the bit on every leaf; decoding is recursive majority vote, with each internal node taking the majority of its children’s values. For $d=3$ this is a single eight‑fold majority vote over the leaves; deeper trees apply the vote iteratively. The quantum proposal — a repetition‑like map $|0\rangle_{L}\mapsto|0\rangle^{\otimes2^{d}}$, $|1\rangle_{L}\mapsto|1\rangle^{\otimes2^{d}}$ — is deliberately minimal, and its quantum completeness (whether the code space corrects a nontrivial set of single‑qubit Pauli errors) is left as an open condition, stated in Section 6.

### 3.3 Energy‑barrier conjecture

We posit a Hamiltonian $H_{d}$ on $\mathcal{T}_{d}$ in which the two logical configurations are degenerate ground states and every configuration differing from a ground state on $m$ leaves carries energy at least $m\cdot\epsilon$, with $\epsilon$ the single‑site excitation cost. A logical error requires flipping a connected set of sites separating the two logical basins. Because the tree branches, the minimal separating set (“cut”) at depth $d$ has size $2^{d}$: an error path must at some depth flip an entire level, and the number of sites at level $\ell$ is $2^{\ell}$. The conjectured barrier is therefore

$$
E_{\text{barrier}}(d)=2^{d}\,\epsilon,
$$

which we take as $E_{\text{barrier}}(d)=2^{d}$ with $\epsilon=1$ as the energy unit. This is the ultrametric analogue of an adiabatic gap argument [7]: protection by energy landscape rather than by measurement. We emphasize that this scaling is a conjecture of the source notes, made precise here but not proved for quantum dynamics.

### 3.4 Noise models

For the classical analysis we use an independent bit‑flip channel with flip probability $p$ per leaf. For the quantum projections we use the depolarizing channel on each physical site,

$$
\mathcal{E}_{p}(\rho)=(1-p)\,\rho+\frac{p}{3}\bigl(X\rho X+Y\rho Y+Z\rho Z\bigr),
$$

and a coherent $Z$‑rotation error $\mathcal{C}_{\theta}(\rho)=e^{-i\theta Z}\rho\,e^{i\theta Z}$. By the Pauli decomposition of general noise on two‑state systems [5], the depolarizing analysis extends term‑by‑term to arbitrary local noise channels; the coherent case is treated separately because it has no classical analogue.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs. We assume zero logical errors at a $40\%$ physical error rate ($p=0.4$) for $d\geq3$, under majority‑vote decoding on classical bits. We emphasize that this result is an unverified report — no supplied source documents the simulation, its trial count, or its decoder details — and every conclusion downstream is conditional on it. The trial count $N$ of the reported simulation is not stated in the source; we therefore compute confidence bounds for two declared scenarios, $N=10^{4}$ and $N=10^{5}$.

### 4.1 Single‑level majority vote at $p=0.4$

**Input:** $n=8$ leaves (depth $d=3$ binary tree, $2^{3}=8$), independent bit‑flip probability $p=0.4$, so $1-p=0.6$. The majority vote fails when at least $5$ of $8$ bits flip:

$$
f(p)=\sum_{k=5}^{8}\binom{8}{k}p^{k}(1-p)^{8-k}.
$$

Compute each term:

- $\binom{8}{5}=56$; $p^{5}=0.4^{5}=0.01024$; $(0.6)^{3}=0.216$; term $=56\times0.01024\times0.216=0.12386304$.  
- $\binom{8}{6}=28$; $p^{6}=0.004096$; $(0.6)^{2}=0.36$; term $=28\times0.004096\times0.36=0.04128768$.  
- $\binom{8}{7}=8$; $p^{7}=0.0016384$; $(0.6)^{1}=0.6$; term $=8\times0.0016384\times0.6=0.00786432$.  
- $\binom{8}{8}=1$; $p^{8}=0.00065536$; term $=0.00065536$.

Sum:

$$
f(0.4)=0.12386304+0.04128768+0.00786432+0.00065536=0.1736704.
$$

Thus one level of eight‑fold majority voting maps $p=0.4$ to $p^{(1)}=0.1736704$ — a suppression factor of $0.4/0.1736704\approx2.303$.

### 4.2 Iterated (concatenated) majority vote

Apply $f$ again with $p^{(1)}=0.1736704$, $1-p^{(1)}=0.8263296$:

- $p^{5}=0.000157982$, $(1-p)^{3}=0.564233$ → term $k=5$: $56\times0.000157982\times0.564233=0.00499156$.  
- $p^{6}=0.000027437$, $(1-p)^{2}=0.68282058$ → term $k=6$: $28\times0.000027437\times0.68282058=0.00052458$.  
- $p^{7}=0.000004765$, $(1-p)=0.8263296$ → term $k=7$: $8\times0.000004765\times0.8263296=0.00003150$.  
- $p^{8}=0.000000827$ → term $k=8$: $0.00000083$.

Sum:

$$
p^{(2)}\approx0.00499156+0.00052458+0.00003150+0.00000083\approx0.0055485.
$$

Third level, with $p^{(2)}=0.0055485$:

- $p^{5}=5.259\times10^{-12}$, $(1-p)^{3}\approx0.98345$ → term $k=5$: $56\times5.259\times10^{-12}\times0.98345\approx2.897\times10^{-10}$.  
- Higher terms are at least two orders of magnitude smaller; the $k=6$ term is $\approx8.09\times10^{-13}$.

Thus

$$
p^{(3)}\approx2.897\times10^{-10}+8.09\times10^{-13}\approx2.905\times10^{-10}.
$$

**Interpretation.** The map $f$ has a stable fixed point below $0.5$, so iterated majority voting on the depth‑$3$ tree exhibits genuine threshold behavior at $p=0.4$: the logical error rate decreases super‑exponentially in concatenation depth. This confirms that the reported classical simulation result (an unverified report; see Section 4 preamble) — zero logical errors at $p=0.4$ for $d\geq3$ — is consistent with a real recursive threshold mechanism of the tree geometry, not an artifact of a single majority vote (which alone would leave a residual $0.1737$). It does not, however, tell us anything about quantum errors; that gap is the subject of Sections 4.3–4.5.

### 4.3 Statistical interpretation of “zero logical errors”

**Input:** zero logical errors observed; trial count $N$ unstated in the source (declared assumption). If the true logical error probability per trial is $p_{L}$, the probability of zero errors in $N$ independent trials is $(1-p_{L})^{N}$. Requiring this to be at least $0.05$ (95 % one‑sided confidence) gives

$$
p_{L}\le1-0.05^{1/N}\approx\frac{\ln20}{N},
$$

using $-\ln(0.05)=\ln20=2.995732$.

**Scenario $N=10^{4}$:**

$$
p_{L}\le1-0.05^{1/10^{4}}\approx\frac{2.995732}{10^{4}}=2.9957\times10^{-4}.
$$

**Scenario $N=10^{5}$:**

$$
p_{L}\le1-0.05^{1/10^{5}}\approx\frac{2.995732}{10^{5}}=2.9957\times10^{-5}.
$$

Thus even with $N=10^{5}$ trials the reported zero‑error result bounds the logical error probability only at $p_{L}\le2.9957\times10^{-5}$, five orders of magnitude above the third‑level concatenated value $p^{(3)}\approx2.905\times10^{-10}$.

### 4.4 Thermal‑activation bound under the barrier model

**Input:** the barrier conjecture $E_{\text{barrier}}(d)=2^{d}$ (Section 3.3, with $\epsilon=1$), and the assumption that logical errors are thermally activated over the barrier with rate proportional to the Boltzmann factor $e^{-E_{\text{barrier}}(d)/k_{\mathrm{B}}T}$. Setting $k_{\mathrm{B}}T=1$ in energy units, the logical error probability per unit attempt is bounded by

$$
p_{L}(d)\le e^{-2^{d}}.
$$

Computing values:

- $d=3$: $e^{-8}=3.3553\times10^{-4}$.  
- $d=5$: $e^{-32}=1.2664\times10^{-14}$.  
- $d=10$: $e^{-1024}=10^{-444.7}$.

Each doubling of depth squares the suppression exponent. This bound is a **projection under a stated model** (thermal activation, $k_{\mathrm{B}}T=1$, degenerate ground states, no resonant tunnelling paths); coherent error paths that tunnel through rather than over the barrier would invalidate it.

### 4.5 The quantization gap as an explicit hypothesis

For the quantum proposal of Section 3.2, correctness requires two conditions that the classical analysis does not supply. First, the code space spanned by $|0\rangle^{\otimes2^{d}}$ and $|1\rangle^{\otimes2^{d}}$ must correct the relevant single‑site Pauli errors; by the Pauli decomposition of general noise [5], it suffices to check the $X$, $Y$, $Z$ components, and the repetition‑like encoding corrects at most one $Z$‑type error but no $X$‑type errors without additional structure — this is a known limitation of repetition encodings that the ultrametric geometry must be shown to overcome. Second, the strong triangle inequality must confine the *propagation* of quantum errors: two error paths that diverge on the tree remain separated, but a coherent superposition of the two paths is a single quantum object that the classical majority‑vote analysis says nothing about. We therefore state the central hypothesis explicitly:

> **Hypothesis Q (quantization gap).** The ultrametric confinement that yields the classical threshold at $p=0.4$ extends to quantum channels if and only if the coherent superposition of divergent error paths does not create interference terms that effectively reconverge the paths.

Hypothesis Q is not established by any supplied source; it is the open question this paper is designed to resolve.

## 5. Results

We report only numbers computed in Section 4, plus clearly labeled projections.

**Computed results (from stated inputs):**

1. Single‑level eight‑fold majority vote at $p=0.4$: failure probability $p^{(1)}=0.1736704$ (Section 4.1), a suppression factor $0.4/0.1736704\approx2.303$.  
2. Two concatenated levels: $p^{(2)}\approx0.0055485$ (Section 4.2).  
3. Three concatenated levels: $p^{(3)}\approx2.905\times10^{-10}$ (Section 4.2).  
4. Confidence bound on the reported zero‑error simulation: $p_{L}\le2.9957\times10^{-4}$ for $N=10^{4}$ and $p_{L}\le2.9957\times10^{-5}$ for $N=10^{5}$ (Section 4.3).

**Labeled projections (assumptions stated in Section 4.4):**

5. Under the thermal‑activation model with $k_{\mathrm{B}}T=1$: $p_{L}(3)\le3.3553\times10^{-4}$, $p_{L}(5)\le1.2664\times10^{-14}$, $p_{L}(10)\le10^{-444.7}$. Uncertainty: these bounds hold only if the barrier model is correct; any tunnelling or coherent path invalidates them entirely.

The classical recursive threshold is genuine: the map $f$ iterated three times suppresses $p=0.4$ to $\approx2.9\times10^{-10}$, consistent with the (unverified) report of zero logical errors at $d\geq3$ provided the trial count satisfies $N\lesssim1/p^{(3)}\approx3.4\times10^{9}$ — for any plausible $N$, zero observed errors is statistically compatible with $p^{(3)}$. No quantum result is claimed.

## 6. Discussion

**Limitations.** The single empirical input — zero logical errors at $p=0.4$ for $d\geq3$ — is an unverified report from the authors' notebook notes; no supplied bibliography entry documents the simulation, its trial count, or its decoder. Every quantitative conclusion above is conditional on that report. The barrier scaling $E_{\text{barrier}}(d)=2^{d}$ is a conjecture made precise in Section 3.3 but not proved for quantum dynamics. The thermal‑activation projections assume $k_{\mathrm{B}}T=1$ and no tunnelling; the confidence bounds assume independence of trials and unstated $N$.

**Failure modes.** Three ways the proposal can fail: (i) the repetition‑like quantum encoding does not correct $X$‑type errors, so the classical threshold does not transfer; (ii) coherent error paths interfere across branches, effectively reconverging paths that the ultrametric separates classically — this would falsify Hypothesis Q;