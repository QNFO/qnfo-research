# Measurement-and-Feedforward Quantum Circuits as Code Design: Detectability, Branch Counting, and the Location of Nonstabilizerness

## Abstract

Shallow quantum circuits augmented by mid-circuit measurements and classical feedforward can deterministically prepare long-range entangled states and implement global unitaries that no comparable-depth unitary circuit can reach. Recent work established a general correspondence between all such protocols and quantum error-correcting codes (QECCs): the unitary circuit preceding the measurements acts as an encoder, and unitary feedforward eliminates post-selection if and only if the measurement projectors are detectable errors on the codespace. We develop the quantitative consequences of this correspondence. We derive the branch-count identity $N_{\text{br}} = 2^{n-k}$ for an $[[n,k]]$ stabilizer code, the detectability fraction $p_{\text{det}} = 1 - 2^{2-n-k}$ (evaluated for the $[[5,1,3]]$ and $[[7,1,3]]$ codes as $0.9375$ and $0.984375$), and the magic accounting $M_2(|T\rangle) = \log_2(4/3) \approx 0.415037$ bits per injected $T$ state, with linear scaling $M_2^{(m)} = m\,M_2(|T\rangle)$. A worked post-selection comparison on the Steane code shows a depth-reduction factor of $80/17 \approx 4.71$ for an encoder of depth $d=10$. We project the exponential rate penalty $N_{\text{br}} = 2^{n(1-R)}$ for vanishing-rate code families. The analysis recasts measurement-and-feedforward protocol design as a code-design problem with explicit, checkable resource accounting.

## 1. Introduction

A central discovery in the theory of near-term quantum computation is that intermediate measurement and classical feedforward extend the reach of shallow circuits. Deterministic preparation of long-range entangled states and implementation of global unitary operations become possible with circuits whose unitary-only counterparts of equal depth cannot accomplish the same task. The structural reason for this enhancement was recently made precise: every measurement-and-feedforward protocol corresponds to a quantum error-correcting code, with the pre-measurement circuit playing the role of the encoder, and feedforward can remove the need for post-selection if and only if the measurement projectors act as detectable errors on the codespace [1],[2].

This correspondence is more than a classification theorem: it converts a circuit-synthesis problem into a code-design problem. Once the connection is established, the machinery of quantum error correction — stabilizer formalism, normalizer counting, code families, and resource measures — becomes directly applicable to measurement-based protocols. But if the correspondence is to be useful for design rather than merely classificatory, it must come with numbers. A designer choosing a code needs to know: how many feedforward branches does the protocol spawn? What fraction of measurement outcomes can be handled by unitary correction rather than discard? How much non-Clifford resource does the resulting operation carry, and where does it live?

We supply this quantitative layer. Our contributions are:

1. **Branch-count identity.** For a stabilizer code $[[n,k]]$ with independent Pauli measurements completing the stabilizer group, the number of distinct feedforward branches is $N_{\text{br}} = 2^{n-k}$ (Section 4.1).
2. **Detectability fraction.** The fraction of Pauli operators on an $[[n,k]]$ code that are detectable errors is $p_{\text{det}} = 1 - 2^{2-n-k}$, which reduces to $1 - 2^{1-n}$ for the $k = 1$ codes evaluated here; we evaluate it for the $[[5,1,3]]$ and $[[7,1,3]]$ codes (Section 4.2).
3. **Magic accounting.** For stabilizer encoders with Pauli measurements, the nonstabilizerness of the implemented operation originates entirely from the encoder [1]. We quantify this with the stabilizer Rényi entropy $M_2$, computing $M_2(|T\rangle) = \log_2(4/3) \approx 0.415037$ bits per injection and the linear scaling $M_2^{(m)} = m\,M_2(|T\rangle)$ (Section 4.3).
4. **Post-selection cost comparison.** A fully worked Steane-code example quantifies the depth saved by deterministic feedforward over naïve discard-and-retry (Section 4.4).
5. **Rate penalty projection.** For vanishing-rate code families the branch count grows as $2^{n(1-R)}$; we give a labeled projection at $n = 49$, $k = 1$ (Section 4.5).

Throughout, "stabilizer code" means a code whose codespace is the joint $+1$ eigenspace of an abelian Pauli group $\mathcal{S}$ with $n-k$ independent generators; "nonstabilizerness" (magic) refers to the amount of stabilizer-entropy resource a state or operation carries, quantified below by $M_2$.

## 2. Background and Related Work

The primary source for this paper is the measurement–feedforward/code correspondence of [1] (the same content catalogued under its canonical identifier as [2]). That work establishes two structural facts: (i) the circuit preceding the measurements in any measurement-and-feedforward protocol acts as an encoder for a quantum code, and (ii) unitary feedforward can eliminate post-selection if and only if the measurement projectors are detectable errors on the codespace. It further shows that for stabilizer codes with Pauli measurements the resulting operation can be non-Clifford, but its nonstabilizerness originates entirely from the encoder, and that non-Pauli measurements or non-additive codes overcome this restriction, yielding long-range nonstabilizerness with only single-qubit unitary corrections. Our paper takes these structural facts as given and develops their quantitative consequences.

The stabilizer formalism underpinning the detectability criterion is reviewed pedagogically in the tutorial of [8], which develops encoder synthesis, stabilizer measurement circuits, and Pauli-frame tracking for stabilizer error-correcting codes. This is exactly the toolkit the correspondence reinterprets: the "encoder" of [1] is the state-preparation circuit of [8], and the "feedforward rule" is the Pauli-frame update. Automated synthesis of fault-tolerant state-preparation circuits [7] addresses the practical half of the same problem: composing a non-fault-tolerant preparation step with verification checks that catch error spreading. In the language of [1], verification is a post-selection surrogate; the correspondence predicts exactly when unitary feedforward can replace it, a design question [7] does not itself answer.

On the code-construction side, [4] constructs $n$-dimensional toric quantum codes ($n \geq 5$) from lattice codes and generalizes quantum interleaving against burst errors; such topological codes provide geometrically local encoders, which matters because the correspondence inherits the encoder's locality structure into the pre-measurement circuit. [9] studies error-correcting codes built on algebraic surfaces, including codes from blow-ups of projective space and ruled surfaces over genus-$0$ curves; algebraic-geometric constructions can improve on low-rate planar families, and since our branch-count identity $N_{\text{br}} = 2^{n-k}$ penalizes low-rate codes exponentially, high-rate code families are directly relevant to keeping feedforward breadth manageable. [5] provides a self-contained treatment of entanglement-assisted quantum error-correcting codes, in which pre-shared entanglement with a reference relaxes the commutation constraints on the stabilizer; this is a natural resource for the correspondence because non-commuting measurements — the non-Pauli escape hatch of [1] — can be traded against entanglement assistance. [6] treats continuous-time quantum error correction, where both noise and correction are continuous weak-measurement-and-feedback processes viewed through the subsystem principle; this is the continuous-time limit of the measurement–feedforward picture and suggests the correspondence may extend beyond projective measurements. Finally, [3], though a classical (unidirectional byte-error) memory-code study, contributes the architectural precedent that detection must be fast and local to prevent error propagation — the classical analogue of the detectability condition that [1] makes precise for quantum feedforward.

Within the QNFO corpus, three companion analyses shape our resource accounting. [10] develops error attribution as resource allocation: per-component sensitivities $\partial P_L$ of the logical error rate identify which circuit elements drive failure, and we adopt the same philosophy — the correspondence should tell the designer which code parameters drive protocol cost, not just whether a protocol exists. [11] quantifies the encoding-rate penalty of planar surface-code modules and assesses low-overhead modular alternatives; since $N_{\text{br}} = 2^{n-k}$, the rate $k/n$ is the single most consequential code parameter for feedforward breadth, making [11]'s rate comparisons directly load-bearing for our Section 4.5. [12] analyzes ensemble dependence of critical exponents at QEC thresholds, a reminder that protocol-level claims near threshold can be ensemble-sensitive; we flag the analogous risk for measurement-based protocols in Section 6. [13] argues, via a photons-per-logical-qubit comparison at $p_L = 10^{-6}$, that bosonic codes may be the native encoding; while orthogonal to the stabilizer focus of [1], it exemplifies the resource-commensurable comparison standard we apply to feedforward-protocol costs.

## 3. Methods

### 3.1 The correspondence as a design interface

Fix a stabilizer code with Pauli group $\mathcal{P}_n$ on $n$ physical qubits, stabilizer group $\mathcal{S} = \langle g_1, \dots, g_{n-k} \rangle$, and codespace $\mathcal{C}$. A measurement-and-feedforward protocol in the sense of [1] consists of:

- an encoder $U_{\text{enc}}$ mapping $k$ logical qubits (and ancillas) into $\mathcal{C}$;
- a set of projective measurements $\{\Pi_j\}$ performed after encoding;
- a classical feedforward map $f: \text{outcomes} \to \text{unitaries}$ applied conditionally on the outcome record.

The correspondence states that $U_{\text{enc}}$ is literally an encoding circuit, and that post-selection on the outcomes can be replaced by unitary feedforward if and only if each projector $\Pi_j$ is a detectable error on $\mathcal{C}$, i.e., $\Pi_j$ anticommutes with at least one stabilizer generator so that its syndrome is nonzero and it maps $\mathcal{C}$ to an orthogonal, identifiable sector. Formally, the deterministic condition is

$$\forall s:\; \Pi_s = E_s P_{\mathcal{C}} \;\Longrightarrow\; F_s = E_s^{\dagger},$$

so that $F_s \Pi_s U_{\text{enc}} = P_{\mathcal{C}} U_{\text{enc}}$ for every outcome $s$, and the overall map is exactly the intended logical operation without post-selection.

### 3.2 Quantities under study

We track four cost quantities:

- $N_{\text{br}}$: the number of distinct feedforward branches (classical control paths);
- $p_{\text{det}}$: the fraction of Pauli operators that are detectable errors, equivalently the fraction of outcomes admitting unitary correction;
- $M_2$: the stabilizer Rényi entropy carried by the protocol output, defined for a pure state $|\psi\rangle$ on $n$ qubits as

$$M_2(|\psi\rangle) = -\log_2\!\left(\sum_{P \in \mathcal{P}_n} \frac{\langle\psi|P|\psi\rangle^4}{2^n}\right),$$

which vanishes for stabilizer states, is positive for magic states, and is additive under tensor products of independent states;
- $R_{\text{exp}}$: the expected number of repetitions under naïve post-selection, $R_{\text{exp}} = 1/p_{\text{post}}$.

### 3.3 Assumptions

All derivations assume: (A1) the code is a stabilizer code with independent generators; (A2) measurements are Pauli projectors completing or refining $\mathcal{S}$; (A3) injected resource states are independent single-qubit magic states, so additivity of $M_2$ applies. Departures from (A2) (non-Pauli measurements, non-additive codes) are discussed qualitatively following [1]; we compute no numbers for them.

## 4. Analysis

### 4.1 Branch-count identity

**Input 1.** A stabilizer code $[[n,k]]$ has $n-k$ independent stabilizer generators (standard stabilizer-formalism counting; see [8] for the tutorial-level derivation).

**Step 1.** Each independent Pauli measurement yields a binary outcome, so the outcome record $\mathbf{m} \in \{0,1\}^{n-k}$ has

$$|\{0,1\}^{n-k}| = 2^{n-k}$$

distinct values.

**Step 2.** Each outcome record selects one feedforward unitary, so

$$N_{\text{br}} = 2^{n-k}.$$

**Worked instance.** The Steane code $[[7,1,3]]$ has $n = 7$, $k = 1$, hence $n-k = 6$ and

$$N_{\text{br}} = 2^{7-1} = 2^6 = 64.$$

A protocol built on the full Steane stabilizer therefore requires at most $64$ distinct correction branches — typically far fewer in practice, because many outcomes share corrections up to stabilizer equivalence.

### 4.2 Detectability fraction

**Input 2.** The syndrome map $\sigma: \mathcal{P}_n \to \{0,1\}^{n-k}$ sends a Pauli $E$ to the bit vector of its commutation pattern with the generators $g_i$; $\sigma(E) = \mathbf{0}$ iff $E \in \mathcal{S}$ up to phase. The kernel of $\sigma$ within $\mathcal{P}_n$ is $\mathcal{S}$ itself, of size $|\mathcal{S}| = 2^{n-k}$.

**Step 1.** By the correspondence of [1], feedforward eliminates post-selection for an outcome iff its projector is a detectable error, i.e., $\sigma(\Pi_j) \neq \mathbf{0}$.

**Step 2.** The Pauli group $\mathcal{P}_n$ has $4^n$ elements (up to phase, $4^n/4 = 4^{n-1}$ projectors); the fraction with nonzero syndrome is

$$p_{\text{det}} = 1 - \frac{|\mathcal{S}|}{|\mathcal{P}_n|/4} = 1 - \frac{2^{n-k}}{4^{n-1}} = 1 - 2^{n-k-2(n-1)} = 1 - 2^{2-n-k}.$$

**Worked instances.** For the $[[5,1,3]]$ code, $k = 1$, $n = 5$:

$$p_{\text{det}} = 1 - 2^{1-5} = 1 - \frac{1}{16} = \frac{15}{16} = 0.9375.$$

For the $[[7,1,3]]$ Steane code, $k = 1$, $n = 7$:

$$p_{\text{det}} = 1 - 2^{1-7} = 1 - \frac{1}{64} = \frac{63}{64} = 0.984375.$$

Equivalently, of the $2^6 = 64$ outcome records of a full Steane stabilizer measurement, $63$ carry a nonzero syndrome and are correctable by feedforward; the single trivial record requires no correction at all. This is the quantitative content of "feedforward eliminates post-selection": the discard branch is the one-in-$64$ trivial record.

### 4.3 Magic accounting for Pauli-measurement protocols

**Input 3.** [1] establishes that for stabilizer encoders with Pauli measurements, the nonstabilizerness of the implemented operation originates entirely from the encoder (including any magic states it injects). We quantify this with $M_2$.

**Step 1.** Compute $M_2$ for the canonical single-qubit magic state $|T\rangle = T|+\rangle$, where $T = \mathrm{diag}(1, e^{i\pi/4})$. Writing $|T\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt{2}$, the Pauli expectation values are

$$\langle X \rangle_T = \cos\!\left(\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}}, \qquad \langle Y \rangle_T = \sin\!\left(\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}}, \qquad \langle Z \rangle_T = \frac{1 - 1}{2} = 0.$$

**Step 2.** Fourth powers: $\langle X\rangle_T^4 = (1/\sqrt{2})^4 = 1/4$; $\langle Y\rangle_T^4 = 1/4$; $\langle Z\rangle_T^4 = 0$. The sum over $\mathcal{P}_1 = \{I, X, Y, Z\}$ is

$$\sum_{P \in \mathcal{P}_1} \langle T|P|T\rangle^4 = 1 + \frac{1}{4} + \frac{1}{4} + 0 = \frac{3}{2}.$$

**Step 3.** Apply the definition with $n = 1$:

$$M_2(|T\rangle) = -\log_2\!\left(\frac{3/2}{2}\right) = -\log_2\!\left(\frac{3}{4}\right) = \log_2\!\left(\frac{4}{3}\right).$$

**Step 4.** Numerically, $\ln(4/3) = 0.287682$, and $\ln 2 = 0.693147$, so

$$M_2(|T\rangle) = \frac{0.287682}{0.693147} \approx 0.415037 \ \text{bits}.$$

**Step 5.** Additivity: for $m$ independent injections, $M_2^{(m)} = m\,M_2(|T\rangle)$. For the illustrative case $m = 5$:

$$M_2^{(5)} = 5 \times 0.415037 \approx 2.075185 \ \text{bits}.$$

**Interpretation.** Since the encoder is the sole magic source [1], the protocol's magic budget is a line item: each injected $T$-type resource contributes $\log_2(4/3) \approx 0.415037$ bits, and a designer targeting a state with known $M_2^{\text{target}}$ needs at least

$$m_{\min} = \left\lceil \frac{M_2^{\text{target}}}{\log_2(4/3)} \right\rceil$$

single-qubit injections under assumption (A3). For example, a target with $M_2^{\text{target}} = 1$ bit requires $m_{\min} = \lceil 1/0.415037 \rceil = \lceil 2.409438 \rceil = 3$ injections.

### 4.4 Post-selection cost on the Steane code

**Input 4.** Measuring only the three independent $X$-type stabilizers of the Steane code ($r_X = 3$) yields $N_{\text{out}} = 2^{r_X} = 2^3 = 8$ outcome records. Each nontrivial record corresponds to a unique single-qubit $X$ error on one of the seven physical qubits, so $N_{\text{detect}} = 7$ and $N_{\text{trivial}} = 1$.

**Step 1.** Because every record is either trivial or detectable, the deterministic condition holds and $p_{\text{succ}} = (7+1)/8 = 1$.

**Step 2.** Under naïve post-selection (discard all nontrivial records), $p_{\text{post}} = N_{\text{trivial}}/N_{\text{out}} = 1/8$, so the expected number of repetitions is

$$R_{\text{exp}}^{\text{post}} = \frac{1}{p_{\text{post}}} = \frac{1}{1/8} = 8.$$

**Step 3.** Deterministic feedforward instead applies one single-qubit Pauli correction per nontrivial record, $\Delta G = N_{\text{detect}} = 7$ gates. If the encoder has depth $d$, the expected depth under post-selection is $8d$ and under feedforward is $d + \Delta G$, giving the reduction factor

$$\frac{8d}{d + \Delta G} = \frac{8d}{d+7}.$$

**Step 4.** For the stated assumption $d = 10$:

$$\frac{8 \times 10}{10 + 7} = \frac{80}{17} \approx 4.71.$$

### 4.5 Rate penalty on branch count (labeled projection)

**Input 5.** From [11], planar surface-code modules pay an encoding rate $k/n$ that vanishes with distance. Combining with the branch identity: for a code family with rate $R = k/n$ at fixed block size $n$,

$$N_{\text{br}} = 2^{n(1-R)}.$$

**Worked projection.** At $n = 49$ with $k = 1$, $R = 1/49 \approx 0.020408$:

$$N_{\text{br}} = 2^{49 \times (1 - 0.020408)} = 2^{48} = 281{,}474{,}976{,}710{,}656 \approx 2.81 \times 10^{14}.$$

This is a projection of the counting identity under the stated assumptions (fixed $n$, no exploitation of structured feedforward); it bounds worst-case classical control breadth, not realized circuit cost.

## 5. Results

All numbers below are computed in Section 4; none are simulated or measured, except R6, which is explicitly labeled a projection.

**R1 (Branch count).** $N_{\text{br}} = 2^{n-k}$; for the Steane code $[[7,1,3]]$, $N_{\text{br}} = 64$ (Section 4.1).

**R2 (Detectability fraction).** $p_{\text{det}} = 1 - 2^{k-n}$; for $[[5,1,3]]$, $p_{\text{det}} = 15/16 = 0.9375$; for $[[7,1,3]]$, $p_{\text{det}} = 63/64 = 0.984375$ (Section 4.2).

**R3 (Magic per injection).** $M_2(|T\rangle) = \log_2(4/3) \approx 0.415037$ bits, from $\sum_{P \in \mathcal{P}_1} \langle T|P|T\rangle^4 = 3/2$ (Section 4.3, Steps 1–4).

**R4 (Magic scaling).** $M_2^{(m)} = m \times 0.415037$ bits; for $m = 5$, $M_2^{(5)} \approx 2.075185$ bits; a $1$-bit magic target requires $m_{\min} = 3$ injections (Section 4.3, Step 5).

**R5 (Post-selection cost).** For the three-$X$-stabilizer measurement on Steane: $N_{\text{out}} = 8$, $p_{\text{succ}} = 1$, $R_{\text{exp}}^{\text{post}} = 8$, $\Delta G = 7$; depth-reduction factor $80/17 \approx 4.71$ under the stated assumption $d = 10$ (Section 4.4).

**R6 (Rate penalty, labeled projection).** Under the stated assumptions (fixed block size $n$, rate $R$, structured feedforward not exploited), $N_{\text{br}} = 2^{n(1-R)}$; at $n = 49$, $k = 1$, this is $2^{48} \approx 2.81 \times 10^{14}$. Uncertainty is dominated by the unmodeled compression achievable by structured feedforward maps; it bounds worst-case classical control breadth, not realized circuit cost.

**R7 (Design checklist).** The correspondence plus R1–R5 yields the mapping from code parameters to protocol costs: (i) rate $k/n$ controls branch breadth exponentially; (ii) distance $d$ and the normalizer structure $N(\mathcal{S})$ control which measurements satisfy detectability; (iii) encoder magic content controls output nonstabilizerness at $\log_2(4/3) \approx 0.415037$ bits per $T$-type injection.

## 6. Discussion

**Limitations.** Our quantitative results live entirely inside assumptions (A1)–(A3). The branch-count identity assumes Pauli measurements refining the stabilizer; non-Pauli measurements — one of [1]'s escape routes to long-range nonstabilizerness — have non-binary outcome structures, and the identity generalizes to $N_{\text{br}} = \prod_j r_j$ for outcome ranks $r_j$, which we have not computed for any specific non-Pauli measurement. The magic accounting assumes independent single-qubit injections; correlated injections (e.g., multi-qubit magic states with subadditive $M_2$) would change $m_{\min}$. The $n = 49$ projection in R6 is a worst-case bound and should not be read as an implementation cost; structured feedforward (syndrome-keyed lookup tables, or Pauli-frame tracking in the sense of [8]) typically compresses the control map dramatically, and quantifying that compression is open. The depth-reduction factor in R5 depends on the assumed encoder depth $d = 10$; for $d \gg 7$ the factor approaches $8$, while for $d \leq 7$ it shrinks toward $1$, so the advantage is encoder-dependent.

**Failure modes.** The detectability fraction $p_{\text{det}}$ counts Pauli operators uniformly; a specific protocol's measurement set may be unrepresentative of that uniform distribution, and in codes with degenerate syndrome structure some outcomes can be undetectable in ways the counting does not capture. If the encoder itself is faulty, the feedforward map inherits encoder errors — the attribution philosophy of [10] says the designer should compute per-component sensitivities $\partial P_L$ before trusting a feedforward rule derived from noiseless syndrome logic, and we have not done so here. Realistic feedforward latency increases the effective depth and partially offsets the gains of R5.

**What would falsify the claims.** R1–R5 are direct consequences of the stabilizer formalism and the definition of $M_2$; they would fail only if the correspondence of [1] itself failed — i.e., if a measurement-and-feedforward protocol existed whose pre-measurement circuit is not an encoder for the measurement-defined code, or if feedforward eliminated post-selection for an undetectable projector. A single counterexample protocol of either kind would falsify the framework and with it our counting identities. R6 would be falsified as a *practical* claim (not as a bound) by a demonstration that structured feedforward reduces realized control cost to $\mathrm{poly}(n)$ on a vanishing-rate code while preserving determinism.

**Arguing against ourselves.** A skeptic could say the counting identities are trivial restatements of stabilizer folklore. We agree they are elementary; our claim is narrower — that they are the *correct* cost layer for the correspondence, in the same sense that [11] argues rate is the correct cost layer for modular memories and [13] argues photons-per-logical-qubit is the correct layer for bosonic-vs-planar comparison. Whether $M_2$ is the right magic measure for *operations* (as opposed to states) generated by these protocols is genuinely open; [1] shows nonstabilizerness originates in the encoder but does not fix an operational resource monotone, and alternative measures (stabilizer mana, stabilizer rank, dyadic-negativity count) could give different $m_{\min}$ — indeed, the mana of the qubit $T$ state, $\ln((1+\sqrt{2})/2) \approx 0.188226$, differs numerically from $M_2(|T\rangle)$, so the injection count $m_{\min}$ is measure-dependent. Ensemble sensitivity near threshold [12] is a further unquantified risk: our identities are noiseless-counting statements, and threshold-regime behavior of measurement-based protocols could be ensemble-dependent in ways the counting does not see. Finally, the classical precedent of [3] — detect errors early and locally — is an analogy, not a theorem; we have not shown that locality of detection translates into locality of feedforward.

**Open questions.** (1) What is the feedforward-compression complexity of the map $f$ for topological encoders such as those of [4]? (2) Do entanglement-assisted codes [5] relax the detectability condition enough to reduce $N_{\text{br}}$ below $2^{n-k}$? (3) Does the continuous-time limit [6] admit a branch-count analogue, or does the branch notion dissolve into feedback gains? (4) Can algebraic-geometric code families [9] be equipped with low-weight measurements satisfying detectability, and at what magic cost? (5) Can automated synthesis pipelines [7] incorporate the deterministic condition directly?

## 7. Conclusion

The measurement–feedforward/code correspondence of [1] turns protocol design into code design, and code design is a discipline of numbers. We have supplied a quantitative layer: branch breadth $N_{\text{br}} = 2^{n-k}$, detectability fraction $p_{\text{det}} = 1 - 2^{2-n-k}$ ($0.9375$ for $[[5,1,3]]$, $0.984375$ for $[[7,1,3]]$), magic content $\log_2(4/3) \approx 0.415037$ bits per $T$-type injection, and a post-selection comparison showing a depth-reduction factor of $80/17 \approx 4.71$ for a depth-$10$ Steane encoder. The framework turns the design of shallow, deterministic quantum circuits into a code-design problem with explicit, checkable resource accounting, offering a systematic route to resource-efficient quantum algorithms.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.39764&amp;start=0&amp;max_results=1
[2] Measurement and feedforward circuits from quantum error correcting codes. arXiv:2609.39764v1. https://arxiv.org/abs/2609.39764v1
[3] Unidirectional Error Correcting Codes for Memory Systems: A Comparative Study. arXiv:1002.1191v1. https://arxiv.org/abs/1002.1191v1
[4] Characterization of $n$-Dimensional Toric and Burst-Error-Correcting Quantum Codes from Lattice Codes. arXiv:2410.20233v1. https://arxiv.org/abs/2410.20233v1
[5] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[6] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[7] Automated Synthesis of Fault-Tolerant State Preparation Circuits for Quantum Error Correction Codes. arXiv:2408.11894v3. https://arxiv.org/abs/2408.11894v3
[8] Quantum Circuits for Stabilizer Error Correcting Codes: A Tutorial. arXiv:2309.11793v1. https://arxiv.org/abs/2309.11793v1
[9] Error Correcting Codes on Algebraic Surfaces. arXiv:math/0309123v1. https://arxiv.org/abs/math/0309123v1
[10] https://papers.qnfo.org/papers/error-attribution-as-a-resource-allocation-principle-for-quantum-error-correctio/. QNFO: Error Attribution as a Resource-Allocation Principle for Quantum Error Correction: Sensitivity-Guided Noise Reduction and Its Analytic Limits.
[11] https://papers.qnfo.org/papers/low-overhead-quantum-error-correction-with-boundary-connected-planar-modules-a-r/. QNFO: Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules: A Reconciled Quantitative Assessment.
[12] https://papers.qnfo.org/papers/ensemble-dependence-of-critical-exponents-at-quantum-error-correction-thresholds/. QNFO: Ensemble Dependence of Critical Exponents at Quantum Error Correction Thresholds: Analytic Mechanisms and Statistical Consequences.
[13] DOI pending. QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes.