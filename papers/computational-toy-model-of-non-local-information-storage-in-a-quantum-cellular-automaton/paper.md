# Computational Toy Model of Non-Local Information Storage in a Quantum Cellular Automaton

## Abstract

Can local, unitary dynamics generate the kind of non-local information storage that holographic quantum error correction requires? This paper revisits that question with a fully reproducible, exact state-vector simulation of a twelve-qubit quantum cellular automaton (QCA) evolving under the particle-conserving Fredkin gate. Two structural facts frame the investigation. First, the standard product-state initializations used in the earlier version of this work — including the all-zeros state — are fixed points of any permutation gate, and the earlier reported results are not reproducible under the methods as stated. Second, the mutual information between two probe qubits is exactly invariant under erasure of the qubits between them, under any erasure protocol; the meaningful quantities are therefore the correlations between the surviving segments and the correlations conditioned on the erased block. With a documented symmetry-breaking initialization, the Fredkin QCA generates substantial entanglement (half-chain entropy up to 2.5 bits at t = 6) and, after erasure of up to two-thirds of the chain, retains residual segment correlations that a swap-gate control loses exactly and immediately. The simulation source is deposited with the paper, and every reported number is reproducible from it. The result is a proof of principle, bounded by its twelve-qubit scale and by the proxy status of its diagnostics: local unitary dynamics can delocalize information across a chain in a way that pure transport dynamics cannot, and this delocalization is measurable with two cheap information-theoretic diagnostics before any decoder is designed.

## 1. Introduction

The holographic principle — the conjecture that the physics of a volume of space can be encoded on its boundary — has been profoundly reinterpreted through the lens of quantum error correction (Almheiri, Dong, and Harlow 2015; Pastawski, Yoshida, Harlow, and Preskill 2015). In this reading, the boundary state is a quantum error-correcting code whose redundancy is what makes bulk geometry robust and local (Harlow 2017). The mathematical machinery of these constructions, however, is heavy: the canonical toy models are static tensor-network codes, engineered by hand rather than grown by dynamics. A complementary line of work asks whether simple local dynamics can generate such redundancy spontaneously. Quantum cellular automata (QCAs) — lattices of qubits evolving under translationally invariant local unitaries — are the natural laboratory for this question, and a specific class of "Goldilocks" rules has been identified that drives product states into highly entangled regimes (Hillberry et al. 2021).

The question this paper addresses is narrow and concrete: *does a complexifying QCA rule generate states whose information is stored non-locally, in a way that simple transport dynamics do not?* The earlier version of this work proposed exactly this hypothesis and reported a striking numerical result: endpoint correlations surviving the erasure of three-quarters of a twelve-qubit chain. That result is not reproducible under the methods as stated, for reasons that turn out to be instructive rather than merely embarrassing: the all-zeros state is a fixed point of the Fredkin gate, and endpoint mutual information is mathematically immune to erasure. This version corrects both issues, replaces the reported results with a verified and fully reproducible simulation, and extracts the genuine content of the original hypothesis — a measurable difference in how Fredkin and swap dynamics distribute information across a chain.

## 2. Theoretical framework

### 2.1 Holographic information storage as redundancy

The functional signature of a holographic quantum error-correcting code is redundancy: information about the logical content is delocalized across the physical degrees of freedom, so that local loss does not destroy it (Almheiri, Dong, and Harlow 2015). The HaPPY code provides the canonical static construction (Pastawski, Yoshida, Harlow, and Preskill 2015), and the entanglement-wedge analysis of Harlow (2017) shows how boundary regions separated by a gap can remain correlated through the bulk. A dynamically generated analog would be a state, reached by local unitary evolution from a simple initial state, whose correlations are not mediated by the physical chain alone.

### 2.2 The proxy problem

A full certification of holographic structure requires demonstrating that logical operators can be recovered from boundary regions — a decoder-level statement. Short of that, mutual information between separated probes is a standard diagnostic of non-local correlation structure: in a locally connected chain, correlations between distant sites typically decay with distance, while in a holographic state the entanglement-wedge connectivity keeps separated regions correlated (Harlow 2017). Mutual information is a *necessary* condition for holographic error correction, not a *sufficient* one: it certifies that the channel exists, not that a message can be read. This proxy status is the permanent boundary of the present work's claims.

### 2.3 Two erasure lemmas

The earlier version of this work defined an "erasure protocol" in which a block of central qubits is removed by a partial trace and the mutual information between the two endpoint qubits is then evaluated. Two elementary facts constrain what any such protocol can measure.

**Lemma 1 (partial-trace erasure leaves endpoint mutual information invariant).** Let $\rho$ be the state of an $N$-qubit system, let $L$ and $R$ be two fixed probe qubits, and let $E$ be any set of qubits disjoint from $\{L,R\}$. Then $\mathrm{Tr}_E(\rho)$ restricted to $L,R$ equals $\rho_{LR} = \mathrm{Tr}_{E\cup\mathrm{rest}}(\rho)$, the reduced state of $L$ and $R$ obtained by tracing everything else. The single-qubit marginals $\rho_L$, $\rho_R$ and the joint marginal $\rho_{LR}$ are therefore all independent of which qubits were erased, and so is $I(L:R) = S(\rho_L) + S(\rho_R) - S(\rho_{LR})$.

**Lemma 2 (measurement with discarded outcomes is a partial trace).** Projectively measuring $E$ and discarding the outcomes produces the mixture $\rho' = \sum_m P_m \rho P_m$ with $P_m$ the projection onto the measurement basis on $E$. Restricting to $L,R$: $\rho'_{LR} = \sum_m \langle m|_E \rho |m\rangle_E = \mathrm{Tr}_E(\rho) \supset \rho_{LR}$, identical to Lemma 1.

Both lemmas are verified numerically in the accompanying source. Their consequence is that *no erasure protocol acting on the middle of the chain can change the endpoint mutual information, in any state, under any dynamics.* The "75% erasure robustness" framing of the earlier version therefore measured a quantity that is robust by definition. The quantities that do depend on erasure are (i) the mutual information between the *surviving segments* left and right of the erased block, and (ii) the conditional mutual information $I(L:R|E)$, which measures how much of the endpoint correlation is mediated through the erased block — the closest finite-system analog of entanglement-wedge connectivity.

## 3. Corrections to version 1.0

This section records, plainly, what was wrong in version 1.0 and what the verification established.

1. **The stated initialization is a fixed point.** Version 1.0 states that the system is initialized in the product state $|00\ldots0\rangle$ and evolved under the Fredkin (controlled-swap) gate. The Fredkin gate is a permutation of the computational basis and conserves excitation number; the all-zeros state is therefore invariant under every gate application. The reported half-chain entropies (≈2.5 bits) and mutual informations (≈0.85) cannot arise from this initialization under any gate arrangement consistent with the text. Verified: the exact simulation returns exactly zero for every quantity at every time step.
2. **The reported erasure decay is not reproducible under the stated protocol.** Lemma 1 shows endpoint mutual information is independent of erasure size; version 1.0's Table 2 reports a decay from 0.85 to 0.42. No trace-based or measurement-discard-based protocol can produce this. The control column (mutual information 0.99 at zero erasure for the swap gate) is likewise impossible for any product initialization, since swap dynamics preserve product states.
3. **The deposited scripts do not contain the simulation.** The v1.0 deposit includes two Python files (E.8.py, S8.12.py); neither implements a quantum cellular automaton or an erasure protocol. They are retained in the version history for transparency. The full simulation source for version 1.1 is deposited with this paper (sim-qca-verification.py).
4. **The "volume-law" characterization is not supported by the data at this scale.** Half-chain entropy saturating near 2.5 bits on a twelve-qubit chain (maximum 6 bits) is substantial but sub-volume; the corrected text describes the observed regime accurately.
5. **A missing reference.** The canonical holographic-code toy model (the HaPPY code) is the natural point of comparison for any "toy model of holographic QEC" claim and is cited here (Pastawski, Yoshida, Harlow, and Preskill 2015).

The purpose of this section is not to retract the underlying hypothesis — the corrected simulation below confirms that the Fredkin dynamics do generate non-trivial delocalized structure where swap dynamics generate none — but to make the evidence honest and the claims bounded by it.

## 4. Methods

### 4.1 System and dynamics

The system is a ring of $N = 12$ qubits evolved in discrete steps $t = 0, \ldots, 24$ by a translationally invariant brickwork of three-qubit gates: each time step applies the Fredkin gate (controlled-swap: swap targets if and only if the control is $|1\rangle$) to the triples $(0,1,2), (3,4,5), (6,7,8), (9,10,11)$ and then to the shifted triples $(1,2,3), (4,5,6), (7,8,9), (10,11,0)$. The control dynamics applies swap gates to adjacent pairs in the same two-sublayer pattern. The state is represented exactly as a complex vector of dimension $2^{12} = 4096$; every result below is exact up to floating-point roundoff and is reproduced by the deposited source.

### 4.2 Initialization

Because permutation gates fix the uniform superposition and every computational-basis product state, the initial state must break the permutation symmetry of the dynamics. The primary initialization used throughout is the *alternating-sign product state*

$$|\psi(0)\rangle = \bigotimes_{i=0}^{11} \frac{|0\rangle + (-1)^i |1\rangle}{\sqrt{2}},$$

a maximally simple state (each qubit a uniform superposition) whose only structure is a site-dependent phase pattern. A random-phase product state (seeded, reproducible) is used as a robustness check in Section 5.4.

### 4.3 Metrics

- **Half-chain entanglement entropy** $S_{1/2}(t)$: the von Neumann entropy of the first six qubits, tracking complexity generation.
- **Endpoint mutual information** $I(L:R)$ with $L = q_0$, $R = q_{11}$: by Lemma 1 erasure-invariant; reported once as the baseline.
- **Segment mutual information** $I(A:B)$: with the central block $E_k = \{6 - k/2, \ldots, 5 + k/2\}$ erased (partial trace), the mutual information between the surviving left segment $A_k = \{0, \ldots, 5 - k/2\}$ and the surviving right segment $B_k = \{6 + k/2, \ldots, 11\}$. Because the full state is pure, $I(A:B) = S(A_k) + S(B_k)$.
- **Conditional mutual information** $I(L:R|E_k) = S(L E_k) + S(R E_k) - S(E_k) - S(L R E_k)$, measuring the endpoint correlation mediated through the erased block.
- **Probe entropy** $S(q_0)$: the entanglement of a single endpoint with the rest.

All quantities are computed by exact partial traces from the state vector. The erasure block is centered; $k \in \{0,2,4,6,8\}$ erases up to two-thirds of the chain.

## 5. Results

### 5.1 Entanglement generation

Table 1 reports the half-chain entropy under the alternating-sign initialization. Entanglement grows rapidly, peaking near 2.5 bits at $t = 6$, then fluctuates between roughly 1.2 and 2.1 bits through $t = 24$ — substantial, structured, and sub-volume (the maximum is 6 bits). The control dynamics (swap gates) leaves every quantity exactly zero at every time step, since swap gates map product states to product states.

**Table 1. Half-chain entanglement entropy (bits), alternating-sign initialization.**

| Time step $t$ | Fredkin rule | Swap control |
|:---:|:---:|:---:|
| 0 | 0.000 | 0.000 |
| 6 | 2.492 | 0.000 |
| 12 | 1.797 | 0.000 |
| 18 | 2.124 | 0.000 |
| 24 | 1.180 | 0.000 |

### 5.2 Erasure structure

Table 2 reports the erasure sweep at $t = 24$. The endpoint mutual information is $I(L:R) = 0.142$ at every erasure size (Lemma 1). The segment mutual information decays from 2.36 bits (no erasure; the two halves of the ring) to 0.37 bits (eight of twelve qubits erased), while the swap control is exactly zero at every erasure size. The conditional mutual information is non-zero and roughly stable at 0.10–0.14 bits, indicating a genuine channel between the endpoints mediated through the erased bulk.

**Table 2. Erasure sweep at $t = 24$ (alternating-sign initialization; all quantities in bits).**

| Erased $k$ | Block $E_k$ | $I(A_k:B_k)$ Fredkin | $I(A_k:B_k)$ control | $I(L:R|E_k)$ | $S(A_k)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | — | 2.359 | 0.000 | — | 1.180 |
| 2 | {5,6} | 1.561 | 0.000 | 0.096 | 1.139 |
| 4 | {4,5,6,7} | 1.064 | 0.000 | 0.122 | 0.997 |
| 6 | {3,4,5,6,7,8} | 0.611 | 0.000 | 0.139 | 0.895 |
| 8 | {2,3,4,5,6,7,8,9} | 0.366 | 0.000 | 0.127 | 0.701 |

### 5.3 The contrast

The verified content of the original hypothesis is the contrast between the two columns. Swap dynamics — pure transport — store no segment correlation that survives erasure at any scale: the control is identically zero. Fredkin dynamics delocalize information across the chain: after erasing two-thirds of the chain, the surviving segments still share 0.37 bits of correlation, and the endpoints retain a bulk-mediated channel of ≈0.13 bits. The difference is not a step function versus a decay curve of a vacuous quantity; it is zero versus non-zero structure at every erasure scale.

### 5.4 Robustness of the qualitative picture

Repeating the Fredkin evolution from a seeded random-phase product state yields the same qualitative structure: half-chain entropy peaks at 2.49 bits at $t = 6$ and fluctuates in the same band (1.05–2.11 bits), endpoint mutual information is 0.124 (erasure-invariant), and the segment mutual information decays over the same range. The qualitative content — substantial entanglement, non-zero erasure-surviving segment correlations, a non-zero conditional channel, and an exactly zero control — is initialization-independent within the class of symmetry-breaking product states.

### 5.5 Comparison with version 1.0

The original reported half-chain entropy 2.45 at $t = 6$; the verified value for the alternating-sign initialization is 2.492 (and 2.485 for the random-phase initialization). The original's t = 6 value is consistent with a symmetry-breaking initialization of the same family; its later "plateau" values (2.51, 2.49, 2.48 at $t = 12, 18, 24$) are not reproduced (verified values 1.80, 2.12, 1.18), and the original's erasure table is not reproducible under any erasure protocol (Section 3.2).

## 6. Discussion

### 6.1 What the verified data show

Three claims survive verification, in corrected form. First, the Fredkin QCA generates genuinely entangled states from simple product states — the entropy growth is real and substantial, though sub-volume at this scale (correcting the earlier characterization). Second, the dynamics produce delocalized information structure: segment correlations survive erasure, and the endpoints maintain a bulk-mediated channel. Third, the contrast with swap dynamics is decisive and exactly zero — the observed structure is a property of the conditional, particle-conserving logic of the Fredkin gate, not of unitary evolution in general.

### 6.2 What the verification cost

The verification also cost something: the headline "75% erasure robustness" of version 1.0 is gone, replaced by the honest statement that endpoint mutual information is erasure-invariant in every state (Lemma 1), and that the meaningful erasure diagnostics are the segment and conditional quantities. The corrected framing is stronger, not weaker: it identifies precisely which information-theoretic quantities can certify delocalized storage, and it provides a lemma that future work on erasure-based diagnostics can rely on.

### 6.3 Structural certification as the next step

Entanglement and correlation metrics certify *that* the state is structured; they do not certify *what kind* of structure. A complementary, dynamics-level benchmark has been proposed for holographic simulations: the adjacent-gap-ratio statistic of random matrix theory, which distinguishes chaotic (GUE-like) from integrable spectra even at small system sizes (Quni-Gudzinas 2026a). The present system is a natural test case, with a caution in the literature: particle-conserving Fredkin circuits include integrable families (Singh, Vasseur, and Gopalakrishnan 2023). Computing the spectral statistic of the twelve-qubit Fredkin step unitary is the immediate next certification step and is included as a protocol in the deposited source.

### 6.4 Relation to the tree-topology error-correction program

The delocalized storage demonstrated here is a precursor effect of the tree-topology quantum error-correction program: ultrametric (tree) geometries confine errors to subtrees by construction (Quni-Gudzinas 2026b), and the Bruhat–Tits tree has been developed as a code geometry in its own right (Quni-Gudzinas 2026c). The present work supplies the dynamical half of that story — a concrete demonstration that local conditional dynamics can generate the non-local redundancy that tree-topology codes then exploit geometrically — and the diagnostics developed here (segment and conditional mutual information under erasure) transfer directly to the validation of candidate tree-topology encodings. The recent demonstration of QCA-based quantum error correction (Guedes, Winter, and Müller 2024) further anchors the direction: cellular-automaton dynamics and error correction are not merely analogous but operationally connected.

### 6.5 Limitations and scope of the claims

Every claim in this paper is bounded by explicit premises. (i) *Scale:* all results are for $N = 12$ qubits, a regime in which the exponential cost of exact state-vector simulation ($2^N$) is affordable; no asymptotic scaling is claimed. (ii) *Diagnostics:* mutual information is a necessary, not sufficient, condition for holographic error correction; no decoder or logical-recovery protocol is demonstrated, and the "holographic-like" vocabulary is a proxy statement, not a certification. (iii) *Dynamics:* the results hold for the documented brickwork layout and gate set; the qualitative robustness check covers initialization within the symmetry-breaking product-state family, not the full space of QCA rules. (iv) *Control:* the swap control is exactly zero for product initializations by construction, which makes the contrast sharp but also means the control probes only the transport channel, not alternative entangling rules. The premises end where these four bounds end; the paper's claims do not extend beyond them.

## 7. What a practitioner can do with this result

The value of this work for practitioners is a pair of cheap, decoder-free diagnostics for screening candidate quantum error-correction encodings before any decoder, code, or hardware commitment is made.

1. **The erasure-screening pipeline.** Given any candidate local gate set (or any proposed processor connectivity graph) and a symmetry-breaking product input state, the deposited source computes, in minutes on a laptop: (a) the endpoint mutual information (the erasure-invariant baseline), (b) the segment mutual information across a sweep of erasure sizes, and (c) the conditional mutual information through the erased block. The pass/fail criterion is the contrast: a candidate whose segment correlations collapse to zero at the first erasure (swap-class behavior) stores information locally; a candidate whose segment correlations decay gradually and whose conditional channel stays non-zero (Fredkin-class behavior) stores information delocalized across the device — the redundancy that error correction requires. No quantum hardware is needed; the screening runs in exact simulation at the 10–14 qubit scale where these diagnostics are conclusive.
2. **Tree-topology validation.** For teams evaluating tree-topology processor architectures (e.g., the 7-ary-depth-3 superconducting layout proposed in the ultrametric quantum-computing program, Quni-Gudzinas 2026b), the same pipeline applies to the proposed connectivity graph: simulate the candidate gate set on the tree, run the erasure sweep, and require the segment-correlation contrast before committing to fabrication-scale design. The diagnostics answer a specific engineering question — "does this gate/topology pair produce the redundancy that a code can exploit?" — with a measurable, reproducible number.
3. **Benchmark discipline.** Any claim that a candidate dynamics is "structurally capable" of holographic-style behavior should be paired with the spectral benchmark of the effective step unitary (adjacent-gap-ratio statistic; protocol in the deposited source and in Quni-Gudzinas 2026a), so that complexity claims are certified at the dynamics level rather than inferred from correlation metrics alone.

Each of these applications is conditional on its domain: the screening is valid for exact-simulation scales (≲14 qubits), the tree-topology guidance is valid for unitary, noise-free candidate dynamics as a first-pass filter, and the benchmark discipline applies to unitary circuits whose spectral statistics can be computed exactly.

## 8. Conclusion

The hypothesis that complexifying QCA dynamics generate non-local information storage survives its own verification, but in a corrected and better-bounded form. The fixed-point obstruction and the erasure-invariance lemma remove the original paper's headline claims and replace them with a reproducible, initialization-documented simulation whose genuine content is the zero-versus-nonzero contrast: Fredkin dynamics delocalize information across a chain in ways that transport dynamics cannot, at every erasure scale tested, and the diagnostics that certify this are two lines of information theory that any practitioner can run on a laptop. The result is a proof of principle — bounded by twelve qubits, by the proxy status of mutual information, and by the documented premises — that local conditional unitary dynamics can generate the redundancy on which error-correcting structure is built, and that this generation is measurable before any decoder exists.

## References

Almheiri, A., X. Dong, and D. Harlow. 2015. "Bulk Locality and Quantum Error Correction in AdS/CFT." *Journal of High Energy Physics* 2015 (4): 163. https://doi.org/10.1007/JHEP04(2015)163.

Pastawski, F., B. Yoshida, D. Harlow, and J. Preskill. 2015. "Holographic Quantum Error-Correcting Codes: Toy Models for the Bulk/Boundary Correspondence." *Journal of High Energy Physics* 2015 (6): 149. https://doi.org/10.1007/JHEP06(2015)149.

Harlow, D. 2017. "The Ryu–Takayanagi Formula from Quantum Error Correction." *Communications in Mathematical Physics* 354 (3): 865–912. https://doi.org/10.1007/s00220-017-2904-z.

Hillberry, L. E., M. T. Jones, D. L. Vargas, P. Rall, N. Yunger Halpern, and N. Bao. 2021. "Entangled Quantum Cellular Automata, Physical Complexity, and Goldilocks Rules." *Quantum Science and Technology* 6 (1): 015005. https://doi.org/10.1088/2058-9565/ac1c41.

Guedes, G., A. Winter, and M. Müller. 2024. "Quantum Cellular Automata for Quantum Error Correction and Density Classification." *Physical Review Letters* 133 (15): 150601. https://doi.org/10.1103/PhysRevLett.133.150601.

Singh, H., R. Vasseur, and S. Gopalakrishnan. 2023. "Fredkin Staircase: An Integrable System with a Finite-Frequency Drude Peak." *Physical Review Letters* 130 (4): 046001. https://doi.org/10.1103/PhysRevLett.130.046001.

Bravyi, S., and B. Terhal. 2010. "Tradeoffs for Reliable Quantum Information Storage in 2D Systems." *Physical Review Letters* 104 (5): 050503. https://doi.org/10.1103/PhysRevLett.104.050503.

Quni-Gudzinas, R. B. 2026a. "Spectral Benchmarking of Holographic Quantum Simulations: A Proposed Framework for Escaping the Artifact Zone." QNFO. https://papers.qnfo.org/papers/spectral-benchmarking-of-holographic-quantum-simulations/.

Quni-Gudzinas, R. B. 2026b. "Ultrametric Quantum Computing: Tree-Topology Error Correction." QNFO. https://papers.qnfo.org/papers.

Quni-Gudzinas, R. B. 2026c. "Ultrametric Code Spaces: The Bruhat–Tits Tree as a Quantum Error-Correction Geometry." QNFO. https://papers.qnfo.org/papers.

**Corrections record:** version 1.1 supersedes version 1.0 (this record's earlier versions) per the corrections documented in Section 3. The simulation source, the erasure-lemma verification, and the universal-ignorance audit artifact accompany this version. The SSRN mirror of version 1.0 (10.2139/ssrn.6054275) is superseded by this record; cite this version.
