# Ultrametric Quantum Error Correction on Bruhat–Tits Trees: Energy Barriers, Classical Evidence, and the Quantization Question

## Abstract

Passive fault tolerance—protection of logical qubits by encoding geometry alone, without repeated syndrome measurement—would remove the dominant overhead in scalable quantum computing if it could be made to work for quantum information rather than only for classical bits. We study a conjectured scheme in which logical qubits are encoded on a Bruhat–Tits tree, the infinite homogeneous tree of a non-Archimedean local field whose metric satisfies the strong triangle inequality. The conjecture states that the energy barrier against a logical error grows as $E_{\text{barrier}}(d)=2^{d}$ in tree depth $d$; the supporting evidence is a classical simulation report of zero logical errors at a physical error rate $p=0.4$ for depth $d\geq3$ under majority-vote decoding. Two claims of the prior version of this analysis require correction, and we correct them here. First, the barrier $E_{\text{barrier}}(d)=2^{d}$ is not derived from the ultrametric cut structure: the minimal-cut count $2^{d}$ holds for any rooted binary tree and uses no property of the strong triangle inequality, so we treat the barrier as a posited model, consistent with the values $B(3)=8$ and $B(4)=16$ reported in [9], [10], and [11] but not a consequence of ultrametricity. Second, the iterated majority-vote cascade at $p=0.4$—which we compute explicitly as $0.1736704\to0.0055485\to2.905\times10^{-10}$ over three levels—is a generic property of recursive majority voting on any branching structure and cannot confirm a threshold mechanism specific to the Bruhat–Tits geometry. We further show that the zero-error report bounds the logical error probability only at $p_{L}\leq2.9957\times10^{-5}$ even for $N=10^{5}$ trials, derive a thermal-activation projection $p_{L}\leq e^{-2^{d}}$ under the stated barrier model, and state the quantization gap—whether the strong triangle inequality confines quantum errors under superposition, entanglement, and coherent noise—as an explicit falsifiable hypothesis with named tests. If the conjecture holds, syndrome-extraction hardware could be replaced by a static energy landscape; nothing in the present evidence yet supports that step.

## 1. Introduction

Scalable quantum computing is presently blocked by error-correction overhead. Active stabilizer codes such as the surface code require repeated syndrome extraction, low-latency real-time decoding, and large ancilla qubit counts, and the engineering cost of these cycles limits the size of computation that can be run on near-term hardware. A cloud-based quantum service provider faces this cost directly: every logical qubit demands a physical-to-logical overhead on the order of $10^{2}$–$10^{4}$ (an assumption stated and labeled as such in [10], which uses an internal estimate of $10^{3}\!:\!1$ for the surface code), continuous measurement infrastructure, and power for decoding. A design that suppressed logical errors passively—by the geometry of the encoding itself, with no measurement cycle—would change the architecture: syndrome-extraction hardware and decoders could be replaced by a static Hamiltonian whose energy landscape blocks error propagation, and the physical-to-logical overhead could fall accordingly.

This paper investigates one specific passive proposal: encode logical information on a Bruhat–Tits tree. A Bruhat–Tits tree is the infinite $(q+1)$-regular tree associated with a local field $k$ complete with respect to a non-Archimedean absolute value; its path metric is ultrametric, satisfying the strong triangle inequality $d_{\mathrm{BT}}(x,z)\le\max\{d_{\mathrm{BT}}(x,y),\,d_{\mathrm{BT}}(y,z)\}$, so every triangle is isosceles with a unique long side. The tree is not an arbitrary graph: for a local field $k$ and the matrix algebra $\mathbb{M}_{2}(k)$, the set of maximal orders containing a given suborder is a subtree of the Bruhat–Tits tree called the branch of the order, and branches have been applied to the global selectivity problem and to computing local embeddings [3]. The conjecture under study asserts (i) that the energy barrier against a logical error on a tree of depth $d$ scales as $E_{\text{barrier}}(d)=2^{d}$, and (ii) that this scaling yields passive fault tolerance with thresholds exceeding those of surface codes, without active syndrome measurement.

Two corrections relative to the prior version of this analysis frame the whole paper, and both concern what the existing evidence actually establishes.

**Correction 1: the barrier is a conjecture, not a derivation.** The prior version stated that the barrier $E_{\text{barrier}}(d)=2^{d}\,\epsilon$ was "derived from the ultrametric cut structure." That statement does not hold. The argument counts sites on a level of a rooted binary tree: a minimal separating set at depth $d$ has size $2^{d}$ because the tree branches in two at every node. This count is a property of any rooted binary tree—a classical repetition structure with no non-Archimedean content—and it invokes the strong triangle inequality nowhere. The follow-up literature is consistent with this reading: [9] states that its exponential-cut claim is a *model* of the strong triangle inequality, not a theorem derived from it, and [10] reports that its distance result is conditional on an encoder that is not constructed. We therefore treat $E_{\text{barrier}}(d)=2^{d}$ throughout as a posited barrier model, compatible with the values $B(3)=8$, $B(4)=16$ reported in [9] and [11] and $E_{\text{barrier}}(3)=8$ in [10], but not derived from ultrametric geometry.

**Correction 2: the voting cascade is generic, not ultrametric.** The prior version concluded from its iterated-vote computation that the cascade "confirms a genuine recursive threshold mechanism of the tree geometry." That conclusion also does not hold. The computed cascade is a property of the majority-vote function $f$ iterated on a branching structure: $f(p)<p$ for every $p<\tfrac12$ on a binary tree of any provenance, and the fixed-point behavior follows from the binomial arithmetic alone. Nothing in the computation uses the Bruhat–Tits tree, its $(q+1)$-regularity, or the strong triangle inequality; an ordinary binary repetition hierarchy would produce the same numbers. The cascade therefore confirms that recursive majority voting suppresses errors at $p=0.4$—a classical, decoder-level fact—and is silent about whether ultrametric geometry contributes anything.

With these corrections in place, the supporting evidence must be stated plainly. The claim that classical simulations using majority-vote decoding on classical bits found zero logical errors at a $40\%$ physical error rate for $d\geq3$ is an unverified report from the proposal's notebook notes; no cited work documents the simulation, its trial count, or its decoder. We treat it as a working assumption and analyze what it would imply if true. The central open question is whether the strong triangle inequality confines quantum errors—superpositions of error paths, entangled error states, and coherent noise—or whether the classical advantage is a decoding artifact that evaporates under full quantum channels. The survey literature states that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes [4], which is precisely the epistemic gap between the classical evidence and the quantum claim.

If the conjecture holds, the decision that changes is architectural: hardware designers could allocate resources to engineering a static energy landscape rather than to measurement cycles and decoders. If it fails—specifically, if coherent error paths interfere across tree branches in a way that reconverge paths the ultrametric separates classically—the proposal is dead, and the failure mode itself would be a sharpened statement of why passive protection requires active measurement.

Our contributions are:

1. A corrected status for the barrier conjecture $E_{\text{barrier}}(d)=2^{d}\,\epsilon$: presented as a posited model with an explicit demonstration that the cut-counting argument does not use ultrametricity (Section 3).
2. An explicit arithmetic analysis of the classical majority-vote cascade at $p=0.4$, giving $0.1736704\to0.0055485\to2.905\times10^{-10}$ over three levels, together with the corrected interpretation that this cascade is generic to recursive majority voting and not evidence for a Bruhat–Tits-specific mechanism (Section 4).
3. A statistical reinterpretation of the reported "zero logical errors" as a confidence bound $p_{L}\le\ln20/N$, not a proof of a vanishing error rate (Section 4).
4. A thermal-activation projection $p_{L}\le e^{-2^{d}}$ under the stated barrier model, with the quantization gap stated as explicit Hypothesis Q rather than a result (Section 4).
5. A specification of the quantum Monte Carlo and tensor-network simulations, and of the theorem that would need to be proved, that would resolve the open question, together with the engineering pathway and the smallest next experiment (Sections 5 and 7).

Throughout we separate what is posited, what is computed from stated inputs, what is reported by cited works, and what is conjecture. The corrected framing also matters beyond this proposal: any program that claims a geometric origin for an error barrier must show that the barrier calculation uses the geometry in question, and the same discipline applies to classical coding hierarchies and to adiabatic gap arguments alike. The quantization gap defined here is the same question any classical-to-quantum transfer claim must answer.

## 2. Background and Related Work

**Continuous-time QEC.** Reference [1] investigates continuous-time quantum error correction (CTQEC), in which both noise and error-correcting operations are processes continuous in time, based on continuous weak measurements and feedback, analyzed from the subsystem principle—the statement that protected information is identified with a subsystem $\mathcal{H}^{A}$ of the system Hilbert space such that a CPTP recovery map $\mathcal{R}$ restores the reduced state after the noise map $\mathcal{E}$. Its outlook notes that constructing optimal CTQEC protocols remains open and that the equilibrium code-space fidelity could be useful for assessing performance under non-Markovian decoherence, where stochastic evolutions are generally too complicated for analytical treatment. CTQEC is the nearest active foil to our proposal: it removes the discrete measurement circuit but retains the feedback loop, whereas a genuinely passive scheme would rely on the energy landscape of the encoding geometry alone.

**Entanglement-assisted codes.** Reference [2] gives a self-contained introduction to entanglement-assisted quantum error-correcting codes (EAQECCs), in which the encoder may append not only ancillas but also ebits—pre-shared entanglement between sender and receiver—before the encoding unitary. Its conclusions state that this entanglement can increase either the communication rate or the number of correctable errors, and that the framework extends the stabilizer formalism while allowing quantum codes to be built from classical linear codes without the dual-containing constraint. The relevance here is structural: if ultrametric confinement fails for independent quantum errors, pre-shared entanglement across distant tree branches is one candidate mechanism for restoring correction capacity, and the EAQECC formalism of [2] is the language in which such a modification would be expressed.

**Bruhat–Tits trees in arithmetic.** Reference [3] treats the Bruhat–Tits tree of a local field $k$, the geometric object we encode on: the tree is the incidence geometry of arithmetic over a non-Archimedean field. We use the tree itself—its vertex set, its symmetric neighborhood relation, and its $(q+1)$-regularity—as the encoding geometry; the arithmetic theory of orders and branches on the tree is background framing that this paper does not rely on, and no error barrier is attributed to it. We stress, per Correction 1, that nothing in the arithmetic theory of the tree supplies an error barrier; the tree supplies a geometry, and the barrier is an additional physical posit about dynamics on that geometry.

**From classical to quantum codes.** Reference [4] surveys error-correcting codes from the classical to the quantum setting, and states that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes, while classical error control methods are well developed. Its classical section introduces the binary symmetric channel with parameter $p$, which flips each transmitted bit with probability $p$ independent of all other events, as the model sufficient to illustrate the basic ideas of error correction; its conclusions note that both quantum and classical schemes add ancillary bits and measure a syndrome, with similar conditions for error detectability and correctability. This is exactly the epistemic gap we interrogate: the $p=0.4$ evidence is a classical-channel result on a binary symmetric channel of the kind [4] uses to illustrate classical correction, and the survey's warning is the generic form of the quantization question we pose as Hypothesis Q.

**Pauli structure of quantum noise.** Reference [5] introduces the main ideas of QEC—encoding, syndrome extraction, error operators, and code construction—and shows that general noise and relaxation of two-state systems can always be understood as a combination of Pauli operators acting on the system, with each code correcting a subset of these errors. Its background records that Shor proved 9 qubits protect a single qubit against general errors and Steane achieved the same with 7, and its three-bit-code section analyzes the simplest case under independent noise that applies $\sigma_{x}$ with probability $p$. This Pauli decomposition is the technical hinge of our analysis: any local quantum channel admits an operator-sum expansion in Pauli terms, so the quantum question reduces to whether ultrametric confinement holds for each Pauli component and whether the coherent superposition of error paths—which has no classical analogue—preserves or destroys the confinement.

**Adiabatic error suppression.** Reference [6] treats error suppression and correction in adiabatic quantum computation, modeling a many-body system undergoing adiabatic evolution coupled to an environment through single-qubit Pauli error operators $E_{j}\otimes B_{j}$, and deriving a dynamical master equation for the encoded dynamics. Its discussion states that the model unifies previously proposed techniques—error suppression, energy gap protection, and dynamical decoupling—under one dynamical framework, allows calculation of rates of leakage from the codespace, and extends to error correction by local cooling. The adiabatic setting is the closest existing analogue to passive protection: there, too, an energy gap rather than a measurement cycle is the protective resource. Our posited barrier $E_{\text{barrier}}(d)=2^{d}\,\epsilon$ is structurally an adiabatic-style gap statement transplanted to an ultrametric geometry, and the tension between gap protection and thermal excitation analyzed in [6] is exactly the failure mode we bound in Section 4—with the caveat, per Correction 1, that no Hamiltonian with this gap has been constructed on the tree.

**Non-standard Hilbert spaces and thresholds.** Reference [7] proposes quaternion-based strategies for QEC by extending quantum mechanics into quaternionic Hilbert spaces, defining quaternionic analogues of Pauli operators and gates that ensure inner-product preservation, and building a quaternionic $[[5,1,3]]$ code. Its text reports a threshold of approximately $p_{\text{th}}\approx0.015$ for the five-qubit quaternionic code, situated between prior reported values, and cites a logical error suppression factor of $\lambda=2.14\pm0.02$ from increasing code distance on a superconducting processor, with an upper bound of $0.189$ for surface codes under correlated noise. These numbers calibrate the competitive landscape: any ultrametric threshold claim must be compared against thresholds in this range, and the suppression factor $\lambda\approx2.14$ per distance increment is the empirical benchmark that a passive scheme claiming thresholds "far exceeding surface codes" would need to beat.

**The prior version of this analysis.** The prior version of this paper stated in its abstract and conclusion that the barrier conjecture was derived from the ultrametric cut structure, and its iterated-vote discussion tied the suppression to the Bruhat–Tits structure. Both statements are corrected in the present revision, on the grounds set out in Section 1; the quantitative computations of the prior version that we reproduce here are unchanged by the correction.

**Quantitative follow-ups.** Reference [9] analyzes passive error correction on regular odd-$p$ Bruhat–Tits trees and reports barrier heights $B(3)=8$ and $B(4)=16$, logical error bounds $p_{L}(3)=6.5536\times10^{-4}$ and $p_{L}(4)=4.29\times10^{-7}$, suppression factors $\approx6.10\times10^{2}$ and $\approx9.31\times10^{5}$, and the concatenated majority-vote values $0.1736704$, $5.5489\times10^{-3}$, and $2.905\times10^{-10}$; its background section states the strong triangle inequality as established in [3] and models it as implying an exponentially growing cut, and its falsification section defines Hypothesis Q with three criteria, including a depth-independent plateau in $p_{L}(d)$ and correlated multi-qudit errors exceeding the majority threshold. Reference [10] analytically encodes logical information on a $p$-adic Bruhat–Tits tree, derives the ball size $n_{1}=5$ for $p=3$, $t=1$ by direct substitution, and reports a passive logical failure $P_{\mathrm{pass}}=9.97\times10^{-6}$ with suppression factor $S=100.3$, a second-level failure $P_{\mathrm{pass}}^{(2)}=6.71\times10^{-7}$ for $t=2$, the barrier $E_{\text{barrier}}(3)=8$, a thermal activation bound $p_{\text{thermal}}=3.35\times10^{-4}$, and a projected logical error after hyperfine scattering of $2.08\times10^{-7}$; its extended insights include the linear sensitivity $\partial P_{\mathrm{pass}}/\partial\varepsilon=20\varepsilon$ for $t=1$, a QND-monitoring proposal, and the explicit statement that no encoder is constructed and that the weight-$\le t$ correctability claim fails if no branch-permutation-symmetric encoder exists. Reference [11] provides an analytic derivation with quantitative projections, reporting $P_{\mathrm{pass}}=5.992003\times10^{-6}$ and suppression factor $166.9$ for the same $t=1$, $\varepsilon=10^{-3}$ configuration, $P_{\mathrm{pass}}^{(2)}=3.997\times10^{-9}$ for $t=2$, and energy barriers $E_{\text{barrier}}(3)=8$ and $E_{\text{barrier}}(5)=32$; it also states the economic motivation (physical-to-logical overhead on the order of $10^{2}$–$10^{4}$, labeled an assumption) and a five-atom $^{87}\mathrm{Rb}$ tweezer experiment with the falsification threshold "logical error rate $>2\times10^{-5}$ would falsify the model."

We note that [10] and [11] report different values of $P_{\mathrm{pass}}$ for the same nominal configuration ($9.97\times10^{-6}$ versus $5.992003\times10^{-6}$); we attribute each number to its source and do not adjudicate between them, since neither derivation is reproduced here. No cited work contains a threshold theorem for ultrametric geometries, a quantum Monte Carlo study of tree codes, or a proof that the strong triangle inequality confines quantum error operators. The gap this paper targets is genuine.

## 3. Methods

### 3.1 The Bruhat–Tits tree and its ultrametric

Let $k$ be a local field with residue field of size $q$, and let $T_{q}$ denote the Bruhat–Tits tree of $k$: the infinite tree in which every vertex has degree $q+1$ [3]. We use only the tree structure, defined as in [3] by a vertex set and a symmetric neighborhood relation. Define the path-length distance $d_{\mathrm{BT}}(v,w)$ as the number of edges on the unique path from $v$ to $w$. The ultrametric consequence we exploit throughout: from any vertex $v$ at depth $d$, two error paths that diverge at depth $d_{0}$ remain separated by $d_{\mathrm{BT}}\ge d-d_{0}$ for all deeper depths—divergence is permanent and distance grows monotonically, unlike in Euclidean lattices where error paths can reconverge. Per Correction 1, this permanence of divergence is a property of trees in general, not a distinctive consequence of the strong triangle inequality; what ultrametricity adds is the global hierarchical structure in which every triangle is isosceles with a unique long side.

### 3.2 Encoding

We encode one logical bit (classical analysis) or, prospectively, one logical qubit (quantum proposal) on a depth-$d$ rooted binary subtree $\mathcal{T}_{d}$ with $2^{d}$ leaves. The classical encoding writes the bit on every leaf; decoding is recursive majority vote, with each internal node taking the majority of its children's values. For $d=3$ this is a single eight-fold majority vote over the leaves; deeper trees apply the vote iteratively. The quantum proposal is the repetition-like map

$$
|0\rangle_{L}\mapsto|0\rangle^{\otimes2^{d}},\qquad
|1\rangle_{L}\mapsto|1\rangle^{\otimes2^{d}},
$$

which is deliberately minimal; whether this code space corrects a nontrivial set of single-qubit Pauli errors is left as an open condition (Section 4.5). The qudit-on-a-ball variant of [10], with parameters $n_{t}=1+(p+1)(p^{t}-1)/(p-1)$ and conditional distance $d=2t+1$, is the more refined encoding in the literature; we use the minimal repetition-like encoding because its failure modes are sharpest.

### 3.3 The barrier as a posited model

We posit a Hamiltonian $H_{d}$ on $\mathcal{T}_{d}$ in which the two logical configurations are degenerate ground states and every configuration differing from a ground state on $m$ leaves carries energy at least $m\,\epsilon$, with $\epsilon$ the single-site excitation cost. A logical error requires flipping a connected set of sites separating the two logical basins. Because the tree branches, the minimal separating set ("cut") at depth $d$ has size $2^{d}$: an error path must at some depth flip an entire level, and the number of sites at level $\ell$ is $2^{\ell}$. The posited barrier is therefore

$$
E_{\text{barrier}}(d)=2^{d}\,\epsilon,
$$

which we take as $E_{\text{barrier}}(d)=2^{d}$ with $\epsilon=1$ as the energy unit, matching the values $E_{\text{barrier}}(3)=8$ and $E_{\text{barrier}}(5)=32$ reported in [11] and $B(3)=8$, $B(4)=16$ in [9]. Per Correction 1, this scaling is a posited model, not a derivation from ultrametricity: the cut count $2^{d}$ is a property of any rooted binary tree, and [9] itself frames the exponential cut as a model of the strong triangle inequality rather than a theorem following from it. This is the ultrametric analogue of an adiabatic gap argument [6]: protection by energy landscape rather than by measurement. We emphasize that no Hamiltonian realizing this barrier on the tree has been constructed; [10] likewise reports that its distance result $d=2t+1$ is conditional on an unconstructed symmetric encoder.

### 3.4 Noise models

For the classical analysis we use the binary symmetric channel with flip probability $p$ per leaf, the standard illustrative channel of classical coding theory [4]. For the quantum projections we use the depolarizing channel on each physical site,

$$
\mathcal{E}_{p}(\rho)=(1-p)\,\rho+\frac{p}{3}\bigl(X\rho X+Y\rho Y+Z\rho Z\bigr),
$$

and a coherent $Z$-rotation error $\mathcal{C}_{\theta}(\rho)=e^{-i\theta Z}\,\rho\,e^{i\theta Z}$. By the Pauli decomposition of general noise on two-state systems [5], the depolarizing analysis extends term-by-term to arbitrary local noise channels; the coherent case is treated separately because it has no classical analogue.

### 3.5 Method of analysis

This paper performs no simulation, measurement, or hardware experiment. Its method is: (i) state every input number with its source or as a declared assumption; (ii) present the barrier as a posited model and demonstrate explicitly that the cut-counting argument does not use ultrametricity; (iii) compute the classical majority-vote cascade, the confidence bounds, and the thermal-activation projections by explicit arithmetic; (iv) attribute all reported numbers from the literature to their sources; and (v) state the quantum question as a falsifiable hypothesis with named tests, which remain proposals in the conditional mood.

## 4. Analysis

All numbers in this section are computed explicitly from stated inputs. The single empirical input is the reported zero logical errors at a $40\%$ physical error rate ($p=0.4$) for $d\geq3$ under majority-vote decoding on classical bits. We emphasize that this result is an unverified report—no cited source documents the simulation, the trial count, or the decoder details—and every conclusion downstream is conditional on it. The trial count $N$ of the reported simulation is not stated; we therefore compute confidence bounds for two declared scenarios, $N=10^{4}$ and $N=10^{5}$.

### 4.1 Single-level majority vote at $p=0.4$

**Input:** $n=8$ leaves (depth $d=3$ binary tree, $2^{3}=8$), independent bit-flip probability $p=0.4$, so $1-p=0.6$. The majority vote fails when at least $5$ of $8$ bits flip:

$$
f(p)=\sum_{k=5}^{8}\binom{8}{k}p^{k}(1-p)^{8-k}.
$$

Compute each term:

- $\binom{8}{5}=56$; $p^{5}=0.4^{5}=0.01024$; $(0.6)^{3}=0.216$; term $=56\times0.01024\times0.216=56\times0.00221184=0.12386304$.
- $\binom{8}{6}=28$; $p^{6}=0.4^{6}=0.004096$; $(0.6)^{2}=0.36$; term $=28\times0.004096\times0.36=28\times0.00147456=0.04128768$.
- $\binom{8}{7}=8$; $p^{7}=0.4^{7}=0.0016384$; $(0.6)^{1}=0.6$; term $=8\times0.0016384\times0.6=8\times0.00098304=0.00786432$.
- $\binom{8}{8}=1$; $p^{8}=0.4^{8}=0.00065536$; term $=0.00065536$.

Summing the four terms:

$$
f(0.4)=0.12386304+0.04128768+0.00786432+0.00065536=0.1736704.
$$

One level of eight-fold majority voting therefore maps $p=0.4$ to $p^{(1)}=0.1736704$, a suppression factor of $0.4/0.1736704\approx2.303$.

### 4.2 Iterated (concatenated) majority vote

Apply $f$ again with input $p^{(1)}=0.1736704$ and $1-p^{(1)}=0.8263296$. The failure probability of the second level is $f(p^{(1)})=\sum_{k=5}^{8}\binom{8}{k}(p^{(1)})^{k}(1-p^{(1)})^{8-k}$. Compute each term:

- $(p^{(1)})^{2}=0.1736704^{2}=0.030161414$; $(p^{(1)})^{4}=(0.030161414)^{2}=0.000909691$; $(p^{(1)})^{5}=0.000909691\times0.1736704=0.000157982$.
- $(1-p^{(1)})^{2}=0.8263296^{2}=0.68282058$; $(1-p^{(1)})^{3}=0.68282058\times0.8263296=0.564233$.
- Term $k=5$: $56\times0.000157982\times0.564233=56\times0.000089135=0.00499156$.
- $(p^{(1)})^{6}=0.000157982\times0.1736704=0.000027437$; term $k=6$: $28\times0.000027437\times0.68282058=28\times0.000018735=0.00052458$.
- $(p^{(1)})^{7}=0.000027437\times0.1736704=0.000004765$; term $k=7$: $8\times0.000004765\times0.8263296=8\times0.000003938=0.00003150$.
- $(p^{(1)})^{8}=0.000004765\times0.1736704=0.000000827$; term $k=8$: $0.00000083$.

Sum:

$$
p^{(2)}=0.00499156+0.00052458+0.00003150+0.00000083\approx0.0055485.
$$

Third level, with input $p^{(2)}=0.0055485$. The sum is dominated by the $k=5$ term:

- $(p^{(2)})^{2}=0.0055485^{2}=0.000030786$; $(p^{(2)})^{4}=(0.000030786)^{2}=9.478\times10^{-10}$; $(p^{(2)})^{5}=9.478\times10^{-10}\times0.0055485=5.259\times10^{-12}$.
- Term $k=5$: $56\times5.259\times10^{-12}\times(1-0.0055485)^{3}\approx56\times5.259\times10^{-12}\times0.98345=2.897\times10^{-10}$.
- Higher terms shrink by at least a factor $p^{(2)}/(1-p^{(2)})\approx0.00558$ each: the $k=6$ term is $\binom{8}{6}(p^{(2)})^{6}(1-p^{(2)})^{2}\approx28\times2.918\times10^{-14}\times0.98896\approx8.09\times10^{-13}$, and the remainder is below $10^{-14}$.

$$
p^{(3)}\approx2.897\times10^{-10}+8.09\times10^{-13}\approx2.905\times10^{-10}.
$$

**Interpretation, corrected.** The map $f$ has a stable fixed point below $0.5$: $f(0.4)=0.1737<0.4$ and $f(0.1737)=0.00555<0.1737$, so iterated majority voting on the depth-$3$ tree exhibits genuine threshold behavior at $p=0.4$, with the logical error rate decreasing super-exponentially in concatenation depth. The cascade values computed in Sections 4.1–4.2 ($0.1736704$, $0.0055485$, $2.905\times10^{-10}$) coincide with the values reported in [9]; the sequence above is this paper's own computation. Per Correction 2, however, this cascade is a property of the majority-vote function iterated on any branching structure: $f(p)<p$ for every $p<\tfrac12$ follows from the binomial arithmetic alone, and nothing in the computation uses the Bruhat–Tits tree, its $(q+1)$-regularity, or the strong triangle inequality. The cascade confirms that recursive majority voting suppresses errors at $p=0.4$—a classical, decoder-level fact—and is silent about whether ultrametric geometry contributes anything. It says nothing about quantum errors; that gap is the subject of Sections 4.3–4.5.

### 4.3 Statistical interpretation of "zero logical errors"

**Input:** zero logical errors observed; the trial count $N$ is not stated by any source, so we declare two scenarios, $N=10^{4}$ and $N=10^{5}$. If the true logical error probability per trial is $p_{L}$, the probability of zero errors in $N$ independent trials is $(1-p_{L})^{N}$. Requiring this to be at least $0.05$ (a 95 % one-sided confidence statement) gives

$$
p_{L}\leq1-0.05^{1/N}\approx\frac{\ln20}{N},
$$

using $-\ln(0.05)=\ln20=2.995732$.

**Scenario $N=10^{4}$:** $p_{L}\leq\frac{2.995732}{10^{4}}=2.9957\times10^{-4}$.

**Scenario $N=10^{5}$:** $p_{L}\leq\frac{2.995732}{10^{5}}=2.9957\times10^{-5}$.

**Interpretation.** Even under the generous assumption $N=10^{5}$ trials, the reported zero-error result bounds the logical error probability only at $p_{L}\leq2.9957\times10^{-5}$ — five orders of magnitude above the third-level concatenated value $p^{(3)}\approx2.905\times10^{-10}$ computed in Section 4.2. "Zero logical errors" in a finite simulation is a confidence statement, not evidence that the logical error rate vanishes; the trial count must be reported before any threshold claim can be quantified.

### 4.4 Thermal-activation projection under the barrier model

**Inputs:** the posited barrier $E_{\text{barrier}}(d)=2^{d}$ (Section 3.3, with $\epsilon=1$), and the assumption that logical errors are thermally activated over the barrier with rate proportional to the Boltzmann factor $e^{-E_{\text{barrier}}(d)/k_{\mathrm{B}}T}$. Setting $k_{\mathrm{B}}T=1$ in energy units, the logical error probability per unit attempt is bounded by

$$
p_{L}(d)\leq e^{-2^{d}}.
$$

Computing values:

- $d=3$: $e^{-8}=3.3546\times10^{-4}$, since $e^{8}=2980.958$ and $1/2980.958=3.35463\times10^{-4}$.
- $d=5$: $e^{-32}=1.2664\times10^{-14}$, since $e^{32}=7.8963\times10^{13}$.
- $d=10$: $e^{-1024}=10^{-1024/\ln10}=10^{-1024\times0.434294}=10^{-444.7}$.

Each doubling of depth squares the suppression exponent. This bound is a **projection under a stated model** (thermal activation, $k_{\mathrm{B}}T=1$, degenerate ground states, no resonant tunnelling paths): it is not a measurement, and coherent error paths that tunnel through rather than over the barrier would invalidate it entirely. That possibility is examined in Section 6. The same functional form appears in the follow-up literature — [10] reports a thermal activation bound $p_{\text{thermal}}=3.35\times10^{-4}$ at $d=3$, matching $e^{-8}$, and [11] reports $E_{\text{barrier}}(3)=8$ and $E_{\text{barrier}}(5)=32$ — but per Correction 1 the barrier itself is a posit, so these agreements confirm consistency of the model, not its truth.

### 4.5 The quantization gap as an explicit hypothesis

For the quantum proposal of Section 3.2, correctness requires two conditions that the classical analysis does not supply. First, the code space spanned by $|0\rangle^{\otimes2^{d}}$ and $|1\rangle^{\otimes2^{d}}$ must correct the relevant single-site Pauli errors; by the Pauli decomposition of general noise [5], it suffices to check the $X$, $Y$, and $Z$ components, and the repetition-like encoding corrects at most one $Z$-type error but no $X$-type errors without additional structure — a known limitation of repetition encodings that the ultrametric geometry must be shown to overcome. Second, the strong triangle inequality must confine the *propagation* of quantum errors: two error paths that diverge on the tree remain separated, but a coherent superposition of the two paths is a single quantum object about which the classical majority-vote analysis says nothing. We therefore state the central hypothesis explicitly:

> **Hypothesis Q (quantization gap).** The ultrametric confinement that yields the classical threshold at $p=0.4$ extends to quantum channels if and only if the coherent superposition of divergent error paths does not create interference terms that effectively reconverge the paths.

Hypothesis Q is established by no cited work; it is the open question this paper is designed to resolve. We take the repetition-like encoding as the primary test object under the convention that the sharpest failure modes should be analyzed first; the qudit-on-a-ball encoding of [10], with its conditional distance $d=2t+1$ and its own unconstructed symmetric encoder, is the fallback if the minimal encoding fails for structural rather than geometric reasons. The falsification criteria of [9] — a depth-independent plateau in $p_{L}(d)$, coherent error paths surviving majority voting, and correlated multi-qudit errors exceeding the majority threshold — are adopted here as the operational tests of Hypothesis Q.

## 5. Results

We report only numbers computed in Section 4, plus clearly labeled projections.

**Computed results (from stated inputs):**

1. Single-level eight-fold majority vote at $p=0.4$: failure probability $p^{(1)}=0.1736704$ (Section 4.1), suppression factor $0.4/0.1736704\approx2.303$.
2. Two concatenated levels: $p^{(2)}\approx0.0055485$ (Section 4.2).
3. Three concatenated levels: $p^{(3)}\approx2.905\times10^{-10}$ (Section 4.2).
4. Confidence bound on the reported zero-error simulation: $p_{L}\leq2.9957\times10^{-4}$ for $N=10^{4}$ and $p_{L}\leq2.9957\times10^{-5}$ for $N=10^{5}$ (Section 4.3).

**Labeled projections (assumptions stated in Section 4.4):**

5. Under the thermal-activation model with $k_{\mathrm{B}}T=1$: $p_{L}(3)\leq3.3546\times10^{-4}$, $p_{L}(5)\leq1.2664\times10^{-14}$, $p_{L}(10)\leq10^{-444.7}$. Uncertainty: these bounds hold only if the barrier model is correct; any tunnelling or coherent path invalidates them entirely.

The classical recursive threshold is genuine as a property of the decoder: the map $f$ iterated three times suppresses $p=0.4$ to $\approx2.9\times10^{-10}$, which is statistically compatible with the (unverified) report of zero logical errors at $d\geq3$ for any plausible trial count, since zero observed errors requires only $N\lesssim1/p^{(3)}\approx3.4\times10^{9}$. Per Correction 2, this suppression is attributable to recursive majority voting on any branching structure, not to the Bruhat–Tits geometry. No quantum result is claimed. For context, the follow-up literature reports, under its own models and assumptions, a passive failure probability $P_{\mathrm{pass}}=9.97\times10^{-6}$ per epoch with suppression factor $S=100.3$ for the $p=3$, $t=1$ ball code [10], and $P_{\mathrm{pass}}=5.992003\times10^{-6}$ with suppression $166.9$ for the same nominal configuration [11]; we attribute each number to its source and do not adjudicate between them, since neither derivation is reproduced here.

## 6. Discussion

**Limitations.** The single empirical input — zero logical errors at $p=0.4$ for $d\geq3$ — is an unverified report from the proposal's notebook notes; no cited work documents the simulation, its trial count, or its decoder. Every quantitative conclusion above is conditional on that report. The barrier scaling $E_{\text{barrier}}(d)=2^{d}$ is a posited model (Section 3.3) whose cut-counting justification uses no ultrametric property; [10] likewise reports that its distance result $d=2t+1$ is conditional on an unconstructed branch-permutation-symmetric encoder. The thermal-activation projections assume $k_{\mathrm{B}}T=1$ and no tunnelling; the confidence bounds assume independent trials and an unstated $N$. The majority-vote cascade assumes independent leaf errors, which correlated noise — for example a gate fault coupling two neighboring vertices, the correlated-error limitation stated in [10] — would violate. The list of assumptions on which the main results rest, with their sensitivity: (i) the zero-error report (all downstream conclusions are conditional on it); (ii) the barrier posit (the thermal projections $p_{L}\leq e^{-2^{d}}$ collapse entirely if it fails); (iii) error independence (the cascade values change under correlated leaf errors, and no bound is available for the correlated case); (iv) the declared trial counts $N=10^{4}$ and $N=10^{5}$ (the confidence bound scales as $\ln20/N$, so it is linearly sensitive to $N$); (v) the repetition-like encoding (its inability to correct $X$-type errors is a structural limitation independent of geometry).

**Failure modes.** Three ways the proposal can fail: (i) the repetition-like quantum encoding does not correct $X$-type errors, so the classical threshold does not transfer; (ii) coherent error paths interfere across branches, effectively reconverging paths that the ultrametric separates classically — this would falsify Hypothesis Q; (iii) the barrier is over-the-barrier only, and resonant tunnelling through the $2^{d}$-site cut restores a depth-independent error channel.

**What would falsify the claims.** A quantum Monte Carlo simulation of the depolarizing channel $\mathcal{E}_{p}$ on $\mathcal{T}_{d}$ showing a logical error rate that does not decrease with $d$ at fixed $p\leq0.4$ would falsify the transfer of the classical threshold. A demonstration that logical operators on the tree need not traverse an entire level would falsify the barrier conjecture, since the cut count $2^{d}$ is the whole content of the posit. Conversely, a proof that the strong triangle inequality confines Pauli error propagation term-by-term, using the decomposition of [5], would establish the conjecture. The falsification criterion is sharp: if the logical error rate at $d=4$ exceeds that at $d=3$ under depolarizing noise, Hypothesis Q is dead and the classical advantage is a decoding artifact. The main result of this paper — that the existing evidence establishes a generic classical decoder property and nothing about ultrametric quantum dynamics — would itself be falsified if a derivation were produced showing that the barrier $2^{d}$ follows from the strong triangle inequality in a way that an ordinary binary tree does not satisfy, or if the classical cascade were shown to depend on a property of the Bruhat–Tits tree beyond its branching.

**Open questions.** Does the $(q+1)$-regularity of the Bruhat–Tits tree [3] admit non-binary qudit encodings matched to the tree degree, as the ball-code parameters $n_{1}=5$, $n_{2}=17$, $n_{3}=53$ of [10] suggest? Can entanglement-assisted methods [2] restore quantum capacity if independent-error confinement fails? Does the adiabatic gap-protection framework of [6] provide a rigorous Hamiltonian whose gap equals $2^{d}\epsilon$? These are precise, testable questions, and the tensor-network and quantum Monte Carlo protocols specified in Section 7 are the tools that would answer them.

**Arguing against ourselves.** The strongest objection to this program is that the classical evidence is exactly the kind of result that does not survive quantization: classical majority voting exploits the ordering of the reals (bits are $0$ or $1$, and majority is well-defined), while quantum errors are operators on a Hilbert space where no such ordering exists. The survey literature states plainly that quantum channels behave differently from classical channels, creating difficulties in developing robust quantum codes [4], and the entire edifice of Section 4 rests on a classical binary symmetric channel of the kind [4] uses to illustrate classical correction. A second objection is internal to the classical evidence: the suppression factor of a single vote, $\approx2.303$, is modest, and the cascade's power depends entirely on the tree being deep enough to iterate — so the claimed advantage over surface codes rests on depths whose quantum realization is untested. A third objection is the discrepancy between the follow-up analyses: [10] and [11] report different passive failure probabilities ($9.97\times10^{-6}$ versus $5.992003\times10^{-6}$) for the same nominal configuration, which shows that even the classical-analogue modeling of these codes is not yet settled. A fourth objection is the calibration from [7]: the empirical suppression factor per distance increment on a superconducting processor is $\lambda=2.14\pm0.02$, and a passive scheme must beat the established scaling of active codes, not merely match a classical cascade. Until Hypothesis Q is tested, the honest position is that this is a conjecture with a suggestive classical analogue, not a fault-tolerance scheme.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The prospective users are quantum hardware architects and cloud quantum service providers: [10] states that hardware developers and cloud-service providers assume achieving fault tolerance requires $10^{2}$–$10^{4}$ physical qubits per logical qubit, inflating system size, power consumption, and cost, and that a passive protection scheme suppressing logical errors without extra qubits would let designers allocate the saved resources to deeper circuits, higher connectivity, or larger problem instances. If the conjecture holds, the design parameter that changes is architectural: syndrome-extraction circuits, ancilla factories, and decoders are replaced by a static Hamiltonian whose energy landscape blocks error propagation, and the overhead budget is re-allocated to engineering that landscape. Until Hypothesis Q is resolved, no design decision should change; the result as it stands is a sharpened specification of what must be tested.

**(b) Current readiness.** This work is analytical and not peer reviewed: under the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; technology concept formulated). The barrier is a posited model, not a proved property of quantum dynamics, and no hardware, simulation, or prototype work was performed here; analytical work of this kind does not exceed TRL 3 even after peer review. The related proposals of [9], [10], and [11] are likewise analytical, with proposed but unbuilt experiments.

**(c) The smallest next experiment.** Two candidate first tests exist in the literature, both proposals rather than performed measurements. Reference [9] proposes a depth-$3$, $p=3$ neutral-atom experiment: prepare a logical state on a five-atom ball plus two additional layers, expose it to engineered depolarizing noise at $p_{\mathrm{err}}=0.40$, perform a single majority-vote decoding pass, and record the logical error rate over $N=10^{4}$ trials; observation of a logical error rate exceeding $p_{L}(3)=6.55\times10^{-4}$ by more than three standard deviations would falsify the passive-barrier hypothesis. Reference [11] proposes a five-atom $^{87}\mathrm{Rb}$ tweezer experiment at $\varepsilon=10^{-3}$ with the falsification threshold "logical error rate $>2\times10^{-5}$ would falsify the model." The smallest test this paper adds is cheaper still and purely computational: a classical Monte Carlo of the depolarizing channel $\mathcal{E}_{p}$ on the depth-$3$ and depth-$4$ trees $\mathcal{T}_{d}$, measuring whether the logical error rate decreases with $d$ at fixed $p$. An outcome in which the depth-$4$ rate fails to improve on the depth-$3$ rate refutes the transfer of the classical threshold and, with it, the practical interest of the scheme.

**(d) Binding constraints.** The constraints that would bind first, in order: (i) the encoder — [10] states that no explicit encoder (state vectors, stabilizer generators, or logical operators) is constructed and that the weight-$\leq t$ correctability claim fails if no branch-permutation-symmetric encoder exists; this is the first blocker for any hardware realization. (ii) Error independence — the $P_{\mathrm{pass}}$ computations of [10] and [11] assume independent depolarizing noise per vertex per epoch, and correlated errors could defeat the weight counting. (iii) Coherent noise — the $Z$-rotation channel $\mathcal{C}_{\theta}$ has no classical analogue, and its effect on the tree encoding is unbounded by any result here. (iv) Calibration of the Hamiltonian — realizing $H_{d}$ with a gap $2^{d}\epsilon$ requires energy scales that grow exponentially in depth, an open engineering question no cited work addresses; [10] notes a coherence-time ceiling $\tau_{\mathrm{H}}\sim2^{L}/(JL)$ from QND monitoring that limits practical depth to $t\leq1$ on current hardware. Data, compute, cost, and regulatory constraints cannot be stated quantitatively from the grounding and remain open questions.

**(e) Order-of-magnitude bounds.** The only quantitative performance bounds available are those derived in Section 4 and those reported by the cited analyses: the classical cascade suppression $0.4\to2.905\times10^{-10}$ over three concatenation levels (Section 4.2), the thermal-activation projections $p_{L}(d)\leq e^{-2^{d}}$ (Section 4.4, projection under the stated barrier model), and the reported passive failure probabilities $9.97\times10^{-6}$ [10] and $5.992003\times10^{-6}$ [11] at $\varepsilon=10^{-3}$ for the $p=3$, $t=1$ ball code. No cost figure, market figure, or hardware performance figure is derivable from the grounding, and we state none.

**(f) Risks and misuse paths.** The main risk is overclaiming: the classical zero-error report at $p=0.4$ could be cited — as it already is in the proposal notes — as evidence for passive quantum fault tolerance, when Section 4.3 shows it bounds $p_{L}$ only at $2.9957\times10^{-5}$ even for $N=10^{5}$ trials and establishes nothing about quantum channels. A secondary risk is resource diversion: if the barrier conjecture is false for quantum dynamics, effort spent engineering a static energy landscape on this geometry is effort not spent on active codes whose thresholds are established.

## 8. Conclusion

We analyzed a conjectured passive fault-tolerance scheme on the Bruhat–Tits tree and corrected two claims of the prior version of this analysis. First, the barrier $E_{\text{barrier}}(d)=2^{d}$ is a posited model, not a derivation from ultrametric geometry: the cut-counting argument counts sites on a level of any rooted binary tree and invokes the strong triangle inequality nowhere, and [9] itself frames the exponential cut as a model of ultrametricity rather than a theorem following from it. Second, the iterated majority-vote cascade at $p=0.4$ — computed here as $0.1736704\to0.0055485\to2.905\times10^{-10}$ over three levels — is a generic property of recursive majority voting on any branching structure and confirms a decoder-level classical fact, not a mechanism of the tree geometry. The reported zero-error result bounds the logical error probability only at $2.9957\times10^{-5}$ even for $N=10^{5}$ trials, and the thermal-activation projections $p_{L}(d)\leq e^{-2^{d}}$ hold only under the posited barrier. The quantum question — whether the strong triangle inequality confines superposed and entangled error paths — remains open, stated as Hypothesis Q with explicit falsification criteria and a named smallest test: a classical Monte Carlo of the depolarizing channel on depth-$3$ versus depth-$4$ trees, whose outcome either transfers the threshold or kills the proposal. The contribution is a precise, testable formulation of the quantization gap, not a resolution of it.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 10 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[2] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[3] On the missing branches of the Bruhat-Tits tree. arXiv:1712.01463v2. https://arxiv.org/abs/1712.01463v2
[4] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[5] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[6] Error suppression and error correction in adiabatic quantum computation II: non-equilibrium dynamics. arXiv:1307.5892v4. https://arxiv.org/abs/1307.5892v4
[7] Quantum Error Correction in Quaternionic Hilbert Spaces. arXiv:2504.19833v1. https://arxiv.org/abs/2504.19833v1
[9] https://papers.qnfo.org/papers/ultrametric-passive-error-correction-on-p-ary-bruhat-tits-trees-barrier-analysis. QNFO: Ultrametric Passive Error Correction on \(p\)-ary Bruhat–Tits Trees: Barrier Analysis and Recursive Thresholds.
[10] https://papers.qnfo.org/papers/ultrametric-passive-fault-tolerance-on-bruhat-tits-trees-analytic-derivation-and. QNFO: Ultrametric Passive Fault Tolerance on Bruhat–Tits Trees: Analytic Derivation and Numerical Projections.
[11] https://papers.qnfo.org/papers/passive-quantum-error-correction-via-ultrametric-geometry-on-bruhat-tits-trees. QNFO: Passive Quantum Error Correction via Ultrametric Geometry on Bruhat–Tits Trees.
