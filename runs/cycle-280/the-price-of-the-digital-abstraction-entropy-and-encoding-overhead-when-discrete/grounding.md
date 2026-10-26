# Grounding block - source: rem-rev-a809ab26-5009-41ad-93e4-b1c188fe4a66

## Research idea

Quantifying the Overhead Cost of Forcing Digital Abstraction onto Continuous Quantum Systems. The author conjectures that the digital/discrete paradigm is an engineering convenience, not a physical universal, and that imposing discrete (number-theoretic, Pauli-error) abstractions on natively continuous bosonic systems (e.g., transmons) incurs a quantifiable, fundamental overhead—leakage, discretization-induced entropy, and error-correction cost—that is itself a measurable consequence of the map-territory mismatch. A theoretical paper could formalize this by deriving a lower bound on the overhead of digital quantum error correction as a function of the 'continuity' of the underlying Hilbert space (finite vs. infinite-dimensional, bosonic vs. fermionic), comparing threshold-theorem assumptions against continuous error models like amplitude damping. Simulations of a Josephson circuit under both discrete Pauli channels and continuous drift could isolate the entropy generated purely by the discretization step, testing whether quantum advantage is better sought in analog Hamiltonian evolution or natively discrete fermionic systems.

Source: owner notebook notes/v1/2026/07/22/_26203070732.md

Post-publication revision of the published paper "The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware" (version 1.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

## Existing paper under revision (remediation only)

# The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware

## Abstract

A working assumption of much quantum error correction (QEC) is that noise can be modeled as a discrete set of Pauli errors acting on two-level systems. We ask what it costs, in information-theoretic terms, to impose this digital abstraction on hardware whose native dynamics are continuous. Using the framing of the QNFO corpus — in particular the observation that a transmon is better described as a qudit of dimension $d \approx 12$ than as a qubit, and that active QEC continuously consumes physical resources — we derive four concrete quantities with fully shown arithmetic. First, the classical register entropy of digitizing one bosonic mode at qudit dimension $d = 12$ is $\log_2 12 \approx 3.585$ bits, and the base truncation entropy $S_{\mathrm{Base}} = \ln(d/2) \approx 1.792$ nats $\approx 2.585$ bits. Second, binary encoding of a $d = 12$ qudit requires $m = 4$ qubits, an encoding efficiency of $\eta \approx 0.896$ and a dimension overhead of $16/12 \approx 1.333$. Third, Pauli twirling of an amplitude-damping channel with damping rate $\gamma = 10^{-3}$ yields a discrete surrogate whose environment entropy is $1.291 \times 10^{-2}$ bits per use, overstating the true environment entropy of $1.141 \times 10^{-2}$ bits by a factor $\approx 1.131$ at matched total error probability. Fourth, for a cold mode with assumed mean occupation $\bar{n} = 0.1$, the discarded Hilbert-space weight is $\approx 3.19 \times 10^{-13}$, i.e., negligible. These are analytic results for idealized channels, not simulations; we state their assumptions and failure modes explicitly and argue that they quantify a map-territory mismatch rather than a physical law.

## 1. Introduction

Quantum error correction (QEC) as usually taught and deployed assumes a lattice of qubits, a discrete error set $\{I, X, Y, Z\}$, and a threshold theorem guaranteeing that if physical error rates lie below a threshold, arbitrarily long computation is possible with polylogarithmic overhead. This package of assumptions is an engineering convenience. Physical devices — superconducting transmons chief among them — are anharmonic oscillators with a ladder of energy levels, coupled to environments through continuous processes such as amplitude damping (energy relaxation) and dephasing. Forcing the continuous onto the discrete must be paid for somewhere: in discarded Hilbert-space weight, in extra encoding qubits, in entropy bookkeeping that no longer matches the physical environment.

This paper formalizes a slice of that cost. We take as our starting point the QNFO research conjecture that the digital/discrete paradigm in quantum computing is an engineering convenience rather than a physical universal, and that imposing number-theoretic, Pauli-error abstractions on natively bosonic systems incurs a quantifiable overhead — leakage, discretization-induced entropy, and error-correction cost — that is itself a measurable consequence of the mismatch between the map (the discrete model) and the territory (the physical system). The related QNFO analysis of the resource burden of active QEC emphasizes that QEC protects quantum information only by continuously consuming physical resources — qubits, measurement bandwidth, classical processing, and energy [12]; we ask a complementary, information-axis question: how much of this running burden is attributable not to noise itself, but to the *discretization step* through which noise is modeled and corrected?

Our contributions are deliberately modest and fully derived:

1. **Register entropy of digitization.** For one bosonic mode truncated to a qudit of dimension $d$, the classical side information needed to label the digitized outcome is $\log_2 d$ bits per mode per use. For the transmon-relevant value $d \approx 12$ suggested in the QNFO Project Rosetta analysis [10], this is $\approx 3.585$ bits, and the associated base truncation entropy is $S_{\mathrm{Base}} = \ln(d/2) \approx 1.792$ nats.

2. **Binary encoding overhead.** Encoding a $d$-dimensional qudit into qubits requires $m = \lceil \log_2 d \rceil$ qubits, wasting $2^m - d$ levels. For $d = 12$: $m = 4$, waste $= 4$ levels, efficiency $\eta \approx 0.896$, dimension overhead $\approx 1.333$.

3. **Entropy distortion under Pauli twirling.** Replacing the continuous-error amplitude-damping channel $\mathcal{L}_\gamma$ by its Pauli-twirled discrete surrogate changes the entropy attributed to the environment. For $\gamma = 10^{-3}$ we compute both entropies exactly and find the surrogate *overstates* the environment entropy by $\Delta H = 1.500 \times 10^{-3}$ bits per use, a ratio of $\approx 1.131$, even though the total error probability is matched exactly.

4. **A negative result on leakage.** For a cold mode with assumed mean occupation $\bar{n} = 0.1$ and cutoff $d = 12$, the discarded population is $\approx 3.20 \times 10^{-13}$: at this operating point the overhead of digitization is bookkeeping overhead, not physical leakage.

We emphasize scope: these are analytic results for idealized single-mode and single-qubit channels. We perform no simulations; where we extrapolate to architectures we do so as clearly labeled projections with stated assumptions. The broader claim — that quantum advantage might be better sought in analog Hamiltonian evolution or natively discrete fermionic systems — is stated as a hypothesis, not a result.

## 2. Background and Related Work

The supplied bibliography is dominated by works on digitization in non-quantum domains; we cite them for what their entries actually support, namely the general observation that representing physical or social reality digitally carries costs, standards, and failure modes. We then draw on the QNFO corpus for the quantum-specific framing. We note plainly that none of the eight arXiv entries below addresses quantum hardware; their summaries are used only as thematic context, and where a summary is thin we say so.

[1] presents the digital twin model as emerging from the interaction of cyber-physical systems with sensors, Industry 4.0, the Internet of Things, machine learning, and artificial intelligence, and states that the model has been used in many areas as a cost-reduction method. The relevance to our argument is structural: a digital twin is a discrete computational surrogate of a continuous physical asset, and its value proposition is explicitly framed as cost — the same cost axis along which we quantify QEC's digital overhead. The supplied summary gives no quantitative content we can import.

[2] addresses fashion digital archives from a humanities perspective, arguing that analyzing everyday fashion trends requires a digital archive of images over an extended period. It illustrates that digitization entails selection and encoding choices — which images, at what fidelity — analogous to our truncation choice of $d$ levels. The summary supplies no further technical detail.

[3] surveys XML-based approaches to representing compound digital assets, including METS, IMS Content Packaging, and XFDU, within the MPEG-21 Digital Item Declaration framework. It is a standards document for discrete representation of assets; we cite it as evidence that even in classical computing, the choice of discrete representation format is consequential enough to standardize. The summary is truncated and yields no quantitative claims.

[4] analyzes the role of AI and machine learning in digital forensics and incident response, describing their integration as transformative but nascent. The analogy is limited; we cite it only to note that the supplied summary does not connect to quantum topics, and we draw no technical claim from it.

[5] proposes data lakes for digital humanities, noting that traditional humanities data bear various formats and need substantial transformations — encoding and tagging, stemming, lemmatization — to be managed. This is the closest classical analogue to our problem: raw, quasi-continuous, unstructured source data must be transformed into a discrete encoded form before analysis, and the transformation itself is a cost center. The summary gives no numbers.

[6] discusses digital democracy, arguing that despite increasingly powerful digital technology, digital democracy has yet to realize its potential for deliberative transformation. We cite it for its theme that a digital abstraction of a deliberative social process underdelivers relative to the underlying territory — a social, not physical, instance of map-territory mismatch. The summary supports no quantitative statement.

[7] presents EviPlant, a solution for creating, manipulating, and distributing digital forensic challenges, noting that realistic challenge corpora require wear-and-tear, background noise, and actual digital traces, and that creating such challenges is arduous. The point of contact is that realistic noise is hard to synthesize in discrete form — precisely the difficulty we formalize when a discrete Pauli error set must stand in for continuous noise. The summary is truncated beyond this.

[8] reports on MediVerify, Sri Lanka's national-scale online medicines information platform, recording over 1.49 million queries in its first year, in the context of large-scale medicine search behaviour in low- and middle-income countries. We restate its summary but make no derivable claim from it: its subject matter — national-scale digital health search — bears no derivable relation to quantum error models, and we do not use its query volume in any computation (see Appendix A for the divergence on this point).

Turning to the QNFO corpus: [9] frames quantum computing as often presented through a small set of recurring claims — that continuous-variable systems are naturally advantaged, that more modes means more power, that quantum advantage has been demonstrated at device level, that statistics could in principle be non-standard, and that complex amplitudes are essential. Our paper interrogates the first of these recurring claims from the opposite direction: rather than assuming continuous-variable advantage, we ask what it costs to deny continuity by digitizing. The summary supplied for [9] is truncated mid-list, so we use only the claims it explicitly names.

[10] is the most substantive quantum-side source. Its summary states that version 2.0 corrects an earlier error: the transmon spectrum IS discrete (Planck quantization), and binary truncation is a radix error, not a physics error; the transmon is a qudit of $d \approx 12$, not a qubit; and it proposes $S_{\mathrm{Base}} = \ln(d/2) \approx 1.79$ nats. We adopt the qudit picture and the $S_{\mathrm{Base}}$ quantity, recompute both exactly in Section 4, and note that the correction cuts both ways for our thesis: if the spectrum is genuinely discrete, part of the "continuity" we invoke is itself an approximation, and the overhead we quantify is radix overhead, not a fight against physics. This nuance is developed in Section 6.

[11], "Lifecycle of a Fault-Tolerant Quantum Computer," has an empty summary in the supplied bibliography. We therefore cannot state anything about its content; we note only that its title indicates topical overlap with our accounting frame in Section 3.4, and we make no claim deriving from it.

[12] analyzes the resource burden of active quantum error correction, stating that QEC protects quantum information only by continuously consuming physical resources — qubits, measurement bandwidth, classical processing, and energy — and that while the theoretical foundations of QEC are mature, the resource burden of running a code, rather than constructing one, is the object of study. This is the direct conceptual ancestor of our overhead accounting: we complement its resource-axis analysis with an information-axis analysis (entropy and dimension), and its summary supports our framing that QEC cost is a running cost, not a one-time construction cost. The supplied summary is truncated and contains no numerical thresholds, so we import no numbers from it.

## 3. Methods

### 3.1 Model of digitization

Let $\mathcal{H}_{\mathrm{bos}}$ be the Hilbert space of one bosonic mode, spanned by number states $\{|k\rangle\}_{k=0}^{\infty}$. Digitization consists of choosing a cutoff $d$ and the map

$$
\Pi_d = \sum_{k=0}^{d-1} |k\rangle\langle k|,
$$

discarding the orthogonal complement. The digitized system is a qudit of dimension $d$; the classical control stack must additionally carry a register of $\log_2 d$ bits per mode to address levels, syndrome symbols, and control outcomes.

### 3.2 Entropy quantities

We track three entropies:

- $H_{\mathrm{reg}}(d) = \log_2 d$: the classical register entropy per digitized mode (bits).
- $S_{\mathrm{Base}}(d) = \ln(d/2)$: the base truncation entropy proposed in [10] (nats).
- $H_{\mathrm{env}}$: the environment entropy per channel use, computed exactly for the physical channel and for its discrete surrogate.

For a diagonal two-outcome distribution with probabilities $(p, 1-p)$ we use the binary entropy $h_2(p) = -p \log_2 p - (1-p)\log_2(1-p)$.

### 3.3 Channels

The physical continuous-error channel is amplitude damping with damping rate $\gamma$:

$$
\mathcal{L}_\gamma(\rho) = K_0 \rho K_0^\dagger + K_1 \rho K_1^\dagger, \quad K_0 = |0\rangle\langle 0| + \sqrt{1-\gamma}\, |1\rangle\langle 1|, \quad K_1 = \sqrt{\gamma}\, |0\rangle\langle 1|.
$$

Its discrete surrogate is the Pauli channel obtained by twirling $\mathcal{L}_\gamma$ over the single-qubit Pauli group, which yields probabilities $p_I, p_X, p_Y, p_Z$ derived in Section 4.3. Twirling is the standard operation by which continuous noise is forced into the discrete Pauli formalism required by stabilizer codes; our object of study is precisely the entropy accounting of this step.

### 3.4 Accounting frame

Following the framing of [12], we treat QEC cost as a running cost: at each correction cycle the machine consumes qubit-time, measurement bandwidth, classical processing, and energy. Our entropy and dimension quantities are per-cycle, per-mode accounting units that can in principle be added to such a resource budget. We do not attempt a full fault-tolerance lifecycle analysis; [11] would be the natural reference but its supplied summary is empty, so we proceed without it.

## 4. Analysis

Every input number below is stated with its source, and every arithmetic step is shown.

### 4.1 Register entropy and base truncation entropy

**Input 1:** $d = 12$, the transmon qudit dimension stated in [10].

Register entropy:

$$
H_{\mathrm{reg}}(12) = \log_2 12 = \frac{\ln 12}{\ln 2} = \frac{2.484907}{0.693147} = 3.584963 \ \text{bits}.
$$

Base truncation entropy, per the definition in [10]:

$$
S_{\mathrm{Base}}(12) = \ln\!\left(\frac{12}{2}\right) = \ln 6 = 1.791759 \ \text{nats}.
$$

Converting to bits: $1.791759 \times \log_2 e = 1.791759 \times 1.442695 = 2.584963$ bits. (Check: $\log_2 6 = \log_2 12 - 1 = 3.584963 - 1 = 2.584963$; consistent.)

**Interpretation:** per digitized mode per use, the digital abstraction requires $\approx 3.585$ bits of classical bookkeeping that the un-digitized labeling does not; this is a hard floor of the abstraction, independent of code choice.

### 4.2 Binary encoding overhead

**Input 2:** $d = 12$ (from [10], as above).

Number of qubits needed:

$$
m = \lceil \log_2 12 \rceil = \lceil 3.584963 \rceil = 4.
$$

Encoded Hilbert dimension: $2^m = 2^4 = 16$. Wasted levels: $2^m - d = 16 - 12 = 4$. Dimension overhead ratio:

$$
\frac{2^m}{d} = \frac{16}{12} = \frac{4}{3} \approx 1.333333.
$$

Encoding efficiency:

$$
\eta = \frac{\log_2 d}{m} = \frac{3.584963}{4} = 0.896241.
$$

So binary digitization of one transmon qudit idles a fraction $1 - \eta = 1 - 0.896241 = 0.1037594 \approx 10.4\%$ of the encoded Hilbert space and inflates the state space by a factor $4/3$.

### 4.3 Entropy distortion under Pauli twirling

**Input 3:** $\gamma = 10^{-3}$, a representative single-qubit relaxation probability per cycle, chosen by us as an illustrative operating point (assumption, not a measurement).

**Step 1 — twirled Pauli probabilities.** Twirling $\mathcal{L}_\gamma$ over the Pauli group gives the Pauli channel equivalent on average:

$$
p_X = p_Y = \frac{\gamma}{4}, \qquad p_Z = \frac{\gamma}{2}, \qquad p_I = 1 - \gamma.
$$

For $\gamma = 10^{-3}$: $p_X = p_Y = 2.5 \times 10^{-4}$, $p_Z = 5 \times 10^{-4}$, $p_I = 0.999$.

**Step 2 — environment entropy of the physical channel.** In amplitude damping, the environment starts in $|0\rangle$ and ends in $|1\rangle$ with probability $\gamma$ (it absorbed the excitation) and in $|0\rangle$ with probability $1-\gamma$. Hence

$$
H_{\mathrm{env}}^{\mathrm{phys}} = h_2(\gamma) = -\gamma \log_2 \gamma - (1-\gamma)\log_2(1-\gamma).
$$

Compute each term for $\gamma = 10^{-3}$:

$$
-\gamma \log_2 \gamma = -10^{-3} \times \log_2(10^{-3}) = 10^{-3} \times 9.965784 = 9.965784 \times 10^{-3},
$$

$$
-(1-\gamma)\log_2(1-\gamma) = -0.999 \times \log_2 0.999 = 0.999 \times 1.443418 \times 10^{-3} = 1.441975 \times 10^{-3},
$$

(using $\log_2 0.999 = \ln 0.999 / \ln 2 = (-1.000500 \times 10^{-3})/0.693147 = -1.443418 \times 10^{-3}$).

$$
H_{\mathrm{env}}^{\mathrm{phys}} = 9.965784 \times 10^{-3} + 1.441975 \times 10^{-3} = 1.140776 \times 10^{-2} \ \text{bits}.
$$

**Step 3 — environment entropy of the twirled surrogate.** The twirled Pauli channel can be realized by an environment that carries a classical label with distribution $(p_I, p_X, p_Y, p_Z)$:

$$
H_{\mathrm{env}}^{\mathrm{twirl}} = -\sum_i p_i \log_2 p_i.
$$

Terms:

$$
-(1-\gamma)\log_2(1-\gamma) = 1.441975 \times 10^{-3} \quad \text{(as above)},
$$

$$
\log_2 p_X = \log_2(2.5 \times 10^{-4}) = \log_2 2.5 + \log_2 10^{-4} = 1.321928 - 13.287712 = -11.965784,
$$

$$
-2\, p_X \log_2 p_X = 2 \times 2.5 \times 10^{-4} \times 11.965784 = 5.982892 \times 10^{-3},
$$

$$
\log_2 p_Z = \log_2(5 \times 10^{-4}) = \log_2 5 - 13.287712 = 2.321928 - 13.287712 = -10.965784,
$$

$$
-p_Z \log_2 p_Z = 5 \times 10^{-4} \times 10.965784 = 5.482892 \times 10^{-3}.
$$

Summing:

$$
H_{\mathrm{env}}^{\mathrm{twirl}} = 1.441975 \times 10^{-3} + 5.982892 \times 10^{-3} + 5.482892 \times 10^{-3} = 1.290776 \times 10^{-2} \ \text{bits}.
$$

**Self-check.** The twirled channel's error total is $p_X + p_Y + p_Z = \gamma/4 + \gamma/4 + \gamma/2 = \gamma$, matching the physical excitation-loss probability — but the entropy bookkeeping differs. The twirled entropy ($1.291 \times 10^{-2}$ bits) *exceeds* the physical entropy ($1.141 \times 10^{-2}$ bits). The distortion is therefore an *overstatement* by the surrogate:

$$
\Delta H = H_{\mathrm{env}}^{\mathrm{twirl}} - H_{\mathrm{env}}^{\mathrm{phys}} = 1.290776 \times 10^{-2} - 1.140776 \times 10^{-2} = 1.500000 \times 10^{-3} \ \text{bits},
$$

$$
\frac{H_{\mathrm{env}}^{\mathrm{twirl}}}{H_{\mathrm{env}}^{\mathrm{phys}}} = \frac{1.290776 \times 10^{-2}}{1.140776 \times 10^{-2}} = 1.131489.
$$

**Interpretation:** at $\gamma = 10^{-3}$, replacing the continuous damping channel by its discrete Pauli surrogate misattributes $\approx 1.5 \times 10^{-3}$ bits per use of entropy to the environment — a $\approx 13.1\%$ distortion — even though the total error probability $\gamma$ is matched exactly. The distortion arises because the twirl redistributes probability into three error species, flattening the label distribution. This is a concrete, fully derived instance of discretization-induced entropy error: the map (Pauli channel) and the territory (damping channel) agree on error weight but disagree on entropy.

### 4.4 Scaling of the distortion

For small $\gamma$, $h_2(\gamma) \approx \gamma \log_2(1/\gamma) + \gamma/\ln 2$, while the twirled entropy is dominated by the three error-species terms. The ratio is a function of $\gamma$ alone; at the computed operating point it is $1.131489$. We do not extrapolate beyond $\gamma = 10^{-3}$ without recomputation, and we flag the $\gamma \to 0$ limit as an open question (Section 6).

### 4.5 Discarded Hilbert-space weight (leakage proxy)

For a thermal bosonic mode with mean occupation $\bar{n}$, the population outside a cutoff $d$ is

$$
p_{\mathrm{disc}}(\bar{n}, d) = \left(\frac{\bar{n}}{1+\bar{n}}\right)^{d}.
$$

**Input 4:** $\bar{n} = 0.1$ (assumed cold mode; assumption, not a measurement), $d = 12$ (from [10]).

$$
\frac{\bar{n}}{1+\bar{n}} = \frac{0.1}{1.1} = 0.0909091, \qquad \ln(0.0909091) = -2.397895,
$$

$$
p_{\mathrm{disc}} = e^{12 \times (-2.397895)} = e^{-28.774743} \approx 3.20 \times 10^{-13}.
$$

At this operating point the discarded weight is negligible; the truncation cost is dominated by the register entropy $H_{\mathrm{reg}}$ and the dimension overhead $4/3$, not by leakage. We report this negative result honestly: for cold modes, the overhead of digitization is bookkeeping overhead, not physical leakage.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

1. **Register entropy of digitization** (Input: $d = 12$ from [10]): $H_{\mathrm{reg}}(12) = \log_2 12 = 3.584963$ bits per mode per use.

2. **Base truncation entropy** (Inputs: $d = 12$ from [10]; definition from [10]): $S_{\mathrm{Base}}(12) = \ln 6 = 1.791759$ nats $= 2.584963$ bits.

3. **Binary encoding overhead** (Input: $d = 12$): $m = 4$ qubits; wasted levels $= 4$; dimension overhead $= 16/12 = 1.333333$; encoding efficiency $\eta = 0.896241$; idle fraction $= 0.1037594$.

4. **Entropy distortion under Pauli twirling** (Input: $\gamma = 10^{-3}$, assumed operating point): $H_{\mathrm{env}}^{\mathrm{phys}} = 1.140776 \times 10^{-2}$ bits; $H_{\mathrm{env}}^{\mathrm{twirl}} = 1.290776 \times 10^{-2}$ bits; distortion $\Delta H = 1.500 \times 10^{-3}$ bits per use; ratio $= 1.131489$ (the discrete surrogate overstates environment entropy by $\approx 13.1\%$ at matched total error probability).

5. **Discarded weight for a cold mode** (Inputs: $\bar{n} = 0.1$ assumed, $d = 12$): $p_{\mathrm{disc}} \approx 3.19 \times 10^{-13}$ — negligible; the digitization overhead at this operating point is bookkeeping, not leakage.

**Labeled projection (not a computed result).** If a fault-tolerant machine runs $N_{\mathrm{cycles}}$ correction cycles on $M$ digitized modes, the cumulative register bookkeeping is $N_{\mathrm{cycles}} \times M \times H_{\mathrm{reg}}(d)$ bits. For illustration, $M = 1000$ modes and $N_{\mathrm{cycles}} = 10^{9}$ cycles would require $10^{9} \times 1000 \times 3.584963 = 3.584963 \times 10^{12}$ bits of cumulative register entropy accounting. This is a projection under stated assumptions ($M$, $N_{\mathrm{cycles}}$ chosen by us; per [12], QEC cost is a running cost, so cumulative quantities are the relevant axis), with uncertainty dominated entirely by the assumed $M$ and $N_{\mathrm{cycles}}$, which span many orders of magnitude across proposed architectures.

## 6. Discussion

**What we have and have not shown.** We have derived exact entropy and dimension quantities for idealized single-mode and single-qubit channels. We have not simulated a Josephson circuit, nor compared discrete Pauli channels against continuous drift in a dynamical simulation; that remains future work. Our results quantify the *bookkeeping* face of the digital abstraction; whether it translates into a *fundamental* lower bound on QEC overhead as a function of Hilbert-space continuity is conjecture.

**The strongest argument against our own thesis.** Entry [10] itself corrects the premise we build on: the transmon spectrum IS discrete by Planck quantization, and binary truncation is a radix error, not a physics error. If the territory is already discrete (a qudit of $d \approx 12$), then the "continuity" we invoke is partly an artifact of the harmonic-oscillator idealization, and our overhead is an encoding inefficiency ($\eta = 0.896$, overhead $4/3$) that better radix choices — qudit encodings, ternary logic, or $d$-ary digitization — could eliminate. On this reading, the digital abstraction is not fighting physics; it is merely using the wrong radix. Our entropy-distortion result (Result 4) survives this critique in weakened form: even on a genuinely discrete qudit, the *choice* of discrete error algebra (Pauli on qubits) misattributes entropy, but a $d$-ary error algebra might not.

**Failure modes of the derivation.** (i) The twirling equivalence holds only on average and for input states diagonal in the right basis; for coherent superpositions the twirled and physical channels differ in more than entropy, and our single entropy metric may mislead. (ii) The environment entropy of the twirled channel assumes the label is carried by a classical environment; a quantum environment realizing the same channel could have different entropy. (iii) $\gamma = 10^{-3}$ and $\bar{n} = 0.1$ are assumed operating points, not measurements; the distortion ratio is $\gamma$-dependent and we have computed it at exactly one point. (iv) The register entropy $H_{\mathrm{reg}}$ is a lower bound on bookkeeping; real control stacks carry far more.

**What would falsify our claims.** A demonstration that Pauli-twirled and physical damping channels have identical environment entropy under a defensible environment model would falsify Result 4. A construction achieving binary encoding of a $d = 12$ qudit with efficiency approaching $1$ and no discarded weight would falsify Result 3. Measurement of substantial discarded population at cold operating points would falsify Result 5. Conversely, if the distortion ratio $H_{\mathrm{env}}^{\mathrm{twirl}}/H_{\mathrm{env}}^{\mathrm{phys}}$ were shown to be an artifact of our choice of classical-label environment, the entropy-distortion claim would need to be restated in terms of a different operational quantity, such as syndrome statistics or logical error rates under a specific code.

**Open questions.** How does the distortion ratio behave as $\gamma \to 0$ and at experimentally measured damping rates? Does the entropy misattribution translate into a measurable penalty in syndrome-processing bandwidth or energy, connecting our information-axis result to the resource-axis analysis of [12]? Can $d$-ary error algebras on native qudits recover the misattributed entropy, and at what cost in code structure? We leave these open; the supplied bibliography contains no data bearing on them.

## 7. Conclusion

We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register-entropy floor of $\log_2 12 \approx 3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6 \approx 1.792$ nats $\approx 2.585$ bits as proposed in [10]; a binary-encoding inefficiency of $\eta \approx 0.896$ with dimension overhead $4/3$; and a Pauli-twirling entropy distortion of $1.500 \times 10^{-3}$ bits per use (ratio $\approx 1.131$) at $\gamma = 10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. A negative result bounds discarded leakage weight at $\approx 3.20 \times 10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price — while the Rosetta correction in [10] tempers the claim: the price may be a radix mismatch rather than a fight against physics. Distinguishing these readings is, in our view, the most valuable next experiment.

## References

[1] Digital Twin As A Cost Reduction Method. arXiv:2107.14109v1. https://arxiv.org/abs/2107.14109v1
[2] A Novel Approach to Analyze Fashion Digital Archive from Humanities. arXiv:2107.08351v2. https://arxiv.org/abs/2107.08351v2
[3] Representing Digital Assets using MPEG-21 Digital Item Declaration. arXiv:cs/0508065v1. https://arxiv.org/abs/cs/0508065v1
[4] A Comprehensive Analysis of the Role of Artificial Intelligence and Machine Learning in Modern Digital Forensics and Incident Response. arXiv:2309.07064v2. https://arxiv.org/abs/2309.07064v2
[5] Data Lakes for Digital Humanities. arXiv:2012.02454v1. https://arxiv.org/abs/2012.02454v1
[6] Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society. arXiv:1910.08604v3. https://arxiv.org/abs/1910.08604v3
[7] EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution. arXiv:1704.08990v1. https://arxiv.org/abs/1704.08990v1
[8] Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries. arXiv:2609.28946v1. https://arxiv.org/abs/2609.28946v1
[9] QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications
[10] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0
[11] QNFO: Lifecycle of a Fault-Tolerant Quantum Computer
[12] QNFO: The Resource Burden of Active Quantum Error Correction: A Scaling Analysis of Qubit, Bandwidth, and Energy Overheads

## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method
arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities
arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration
arXiv:2012.02454v1 | Data Lakes for Digital Humanities
arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society
arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution
arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries

## QNFO corpus context (Vectorize)

QNFO: The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware | https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete
QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications | https://papers.qnfo.org/papers/locale-framework-quantum-applications
QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | https://papers.qnfo.org/papers/rosetta-fractal-math
QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis | https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:2107.14109v1 | Digital Twin As A Cost Reduction Method
  Many fields have been affected by the introduction of concepts such as sensors, industry 4.0, internet of things, machine learning and artificial intelligence in recent years. As a result of the interaction of cyber physical systems with these concepts, digital twin model has emerged. The concept of digital twin has been used in many areas with its emergence. The use of this model has made signifi
  Full text (https://ar5iv.labs.arxiv.org/html/2107.14109v1), excerpts of its own sections:
  § Submission history: From: Omer Aydin [ view email ] [v1] Sat, 10 Jul 2021 22:01:34 UTC (495 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Twin As A Cost Reduction Method, by Suleyman Yukcu and 1 other authors View PDF view license
  § Current browse context:: cs.OH < prev | next > new | recent | 2021-07 Change to browse by: cs econ econ.GN q-fin q-fin.EC q-fin.GN
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[2] arXiv:2107.08351v2 | A Novel Approach to Analyze Fashion Digital Archive from Humanities
  Fashion styles adopted every day are an important aspect of culture, and style trend analysis helps provide a deeper understanding of our societies and cultures. To analyze everyday fashion trends from the humanities perspective, we need a digital archive that includes images of what people wore in their daily lives over an extended period. In fashion research, building digital fashion image archi
  Full text (https://arxiv.org/html/2107.08351v2), excerpts of its own sections:
  § 1 Introduction: Fashion styles adopted in our daily lives are an important aspect of culture. As noted by Lancioni  [ 17 ] , fashion is ‘a reflection of a society’s goals and aspirations’; people choose fashion styles within their embedded social contexts. Hence, the analysis of everyday fashion trends can provide an in-depth understanding of our societies and cultures. In fashion research, the advantages of digital fashion archives have continued to attract attention in recent times. These digital archives have been mainly built based on two purposes. One is enhancing the scholarly values of museum collections by making them public to utilize them digitally. Another motivation is predicting what fashion items will come into style in the short term with images retrieved from the internet for business purposes. However, these archives are not suitable for analyzing everyday fashion trends from the humanities perspective. To identify everyday fashion trends, we need a new digital archive that includes images of the clothes people wore in their daily lives over an extended period. [...]
  § 2.1 Fashion Trend Analysis: Kroeber  [ 15 ] analyzed fashion trends manually and measured features of women’s full evening toilette, e.g. skirt length and skirt width, which were collected from magazines from 1844 to 1919. After this work, many researchers conducted similar studies  [ 2 , 21 , 22 , 25 ] . [...]
  § 5.3 Discussion: The findings in Section 5.1 prompted a new research question of determining the importance of the different roles that media play in fashion trends: the role of the ‘mixed’ pattern for creating and reporting new trends and the ‘follow-up’ effect to keep their momentum. To theorize how fashion trends are generated in more detail, our findings indicate that quantifying the trends from multiple digital archives is essential to test the research questions about the effect of the media’s role, which has not been discussed thoroughly. In previous studies, researchers analyzed fashion style trends at a street level independently. However, to analyze the recent, more complicated trend patterns, the findings in Section 5.2 suggests that it would be thought-provoking to focus on what the icons represent for people’s social identities, rather than the style itself, and how they lead the trends. An example is the analysis of the types of media that icons use and the reach of that media. [...]
  § 6 Conclusions: In this study, we reviewed the issues in the existing digital fashion archives for the analysis of everyday fashion trends. As one of the solutions to these issues, we built CAT STREET, which comprises fashion images illustrating what people wore in their daily lives in the period 1970–2017, along with street-level geographical information. We demonstrated that machine learning retrieved how fashion styles emerged on the street using CAT STREET and the magazine archives helped us interpret these phenomena. These empirical analyses showed our approach’s potential to find new perspectives to promote the understanding of our societies and cultures through fashion embedded in the daily lives of consumers. Our work is not without limitations. We used the fashion style categories of FashionStyle14  [ 32 ] , which was defined by fashion experts and is considered to represent modern fashion. However, the definition does not cover all contemporary fashion styles and their substyles in a mutually exclusive and collectively exhaustive manner. [...]
[3] arXiv:cs/0508065v1 | Representing Digital Assets using MPEG-21 Digital Item Declaration
  Various XML-based approaches aimed at representing compound digital assets have emerged over the last several years. Approaches that are of specific relevance to the digital library community include the Metadata Encoding and Transmission Standard (METS), the IMS Content Packaging XML Binding, and the XML Formatted Data Units (XFDU) developed by CCSDS Panel 2. The MPEG-21 Digital Item Declaration 
  Full text (https://ar5iv.labs.arxiv.org/html/cs/0508065v1), excerpts of its own sections:
  § Submission history: From: Herbert van de Sompel [ view email ] [v1] Sat, 13 Aug 2005 03:09:25 UTC (451 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Representing Digital Assets using MPEG-21 Digital Item Declaration, by Jeroen Bekaert and 1 other authors View PDF view license
  § Current browse context:: cs.DL < prev | next > new | recent | 2005-08
  § DBLP - CS Bibliography: listing | bibtex Jeroen Bekaert Herbert Van de Sompel Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:2012.02454v1 | Data Lakes for Digital Humanities
  Traditional data in Digital Humanities projects bear various formats (structured, semi-structured, textual) and need substantial transformations (encoding and tagging, stemming, lemmatization, etc.) to be managed and analyzed. To fully master this process, we propose the use of data lakes as a solution to data siloing and big data variety problems. We describe data lake projects we currently run i
  Full text (https://arxiv.org/html/2012.02454v1), excerpts of its own sections:
  § 1. Introduction: Traditional data management has long been adopted by many researchers involved in Digital Humanities (DH). However, it requires a substantial investment in data modeling, including, at the physical level, technologies such as relational and semi-structured Database Management Systems (DBMSs), various data formats, e.g., XML and JSON for semi-structured data, RDF for linked data, and query languages such as SQL and XQuery. This investment in computer science and the fact that initial data are inevitably transformed are presumably impediments to the adoption of DBMSs and related digital tools for DH. Moreover, most source information exploited by humanities and social sciences comes in textual format. Again, such textual documents are difficult to manage without substantial transformations: digitization, encoding and tagging, e.g., via the Text Encoding Initiative (TEI), and even lowercasing, stemming, lemmatization, stopword removal or normalization when it comes to text mining and natural language processing. [...]
  § 2.1. HyperThesau: The “Hyper thesaurus and data lakes: Mine the city and its archaeological archives” (HyperThesau) project involves a multidisciplinary team consisting of two research laboratories of archaeology and of computer science, a digital library, two archaeological museums and a private company. This project has two main objectives: (1) the design and implementation of an integrated platform to host, search, share and analyze archaeological data; (2) the design of a domain-specific thesaurus taking the whole archaeological data lifecycle into account, from data creation to publication. Archaeological data may bear many different types, e.g., textual documents, images (photographs, drawings…), sensor data, etc. Moreover, similar documents, e.g., excavation reports, are often created by various software tools that are not compatible with each other. The description of an archaeological object also differs with respect to users, usages and time. [...]
  § 2.2. Bretez/STRATEGE: Bretez ( Pardoën, 2020 ) is a multidisciplinary project aiming at a visual and sonorous restitution of the XVIII th -century Paris. It is also an exploratory project constituted of successive, interlinked modules that are (and must be) interoperable and open. The historical urban restitution is achieved with video game engines that bear their own respective characteristics, of course related to gaming. Yet, here, they are used for specific management and traceability needs. [...]
  § 3. Conclusion: In all four data lake projects summarized in Section  2 , we use different versions of the MEDAL metadata system, which is designed to be generic. However, although MEDAL is quite flexible, we do not believe in a single model for data lakes. There are indeed significant differences in data in only four projects, in terms of volume, variety and velocity, which imply different architectures and technologies. Thus, we think that much needed methodological tools for data lakes should be instantiated for each project rather than applied “as is”. Furthermore, the software layer we add to “industrialize” our data lakes might become yet another black box, while there is a strong stake for researchers in humanities and social sciences involved in DH projects not to be dispossessed of data by an analysis layer that would adopt a “click and go” approach. Data are indeed often partly constructed by said researchers themselves as a product of scientific work that takes time, thus giving a significant value to datasets. [...]
[5] arXiv:1910.08604v3 | Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society
  Though successive generations of digital technology have become increasingly powerful in the past twenty years, digital democracy has yet to realize its potential for deliberative transformation. The undemocratic exploitation of massive social media systems continued this trend, but it only worsened an existing problem of modern democracies, which were already struggling to develop deliberative in
  Full text (https://ar5iv.labs.arxiv.org/html/1910.08604v3), excerpts of its own sections:
  § Submission history: From: Todd Davies [ view email ] [v1] Fri, 18 Oct 2019 19:52:07 UTC (327 KB) [v2] Sun, 15 Dec 2019 03:44:40 UTC (388 KB) [v3] Tue, 3 Mar 2020 22:45:46 UTC (388 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Democracy: Episode IV -- A New Hope, How a Corporation for Public Software Could Transform Digital Engagement for Government and Civil Society, by John Gastil and Todd Davies View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2019-10 Change to browse by: cs cs.SI
  § DBLP - CS Bibliography: listing | bibtex John Gastil Todd Davies Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:1704.08990v1 | EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution
  Education and training in digital forensics requires a variety of suitable challenge corpora containing realistic features including regular wear-and-tear, background noise, and the actual digital traces to be discovered during investigation. Typically, the creation of these challenges requires overly arduous effort on the part of the educator to ensure their viability. Once created, the challenge
  Full text (https://ar5iv.labs.arxiv.org/html/1704.08990v1), excerpts of its own sections:
  § Submission history: From: Mark Scanlon [ view email ] [v1] Fri, 28 Apr 2017 16:13:35 UTC (725 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled EviPlant: An efficient digital forensic challenge creation, manipulation and distribution solution, by Mark Scanlon and 2 other authors View PDF view license
  § Current browse context:: cs.CR < prev | next > new | recent | 2017-04 Change to browse by: cs cs.CY
  § DBLP - CS Bibliography: listing | bibtex Mark Scanlon Xiaoyu Du David Lillis Loading...
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[7] arXiv:2609.28946v1 | Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries
  National-scale digital health platforms generate usage data that reveal population healthcare needs. MediVerify, Sri Lanka's online medicines information platform providing access to National Medicines Regulatory Authority (NMRA)-approved medicines, recorded over 1.49 million queries in its first year. Large-scale medicine search behaviour in low- and middle-income countries (LMICs) remains poorly
  Full text (https://ar5iv.labs.arxiv.org/html/2609.28946v1), excerpts of its own sections:
  § Submission history: From: Praveen Athauda-Arachchi [ view email ] [v1] Thu, 24 Sep 2026 02:53:08 UTC (1,171 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Digital Medicines Information at National Scale: Search Behaviour and System Performance of MediVerify Across 1.5 Million Queries, by Praveen Charuka Athauda-Arachchi and 1 other authors View PDF view license
  § Current browse context:: cs.CY < prev | next > new | recent | 2026-09 Change to browse by: cs
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[8] QNFO: The Price of the Digital Abstraction: Entropy and Encoding Overhead When Discrete Error Models Meet Continuous Quantum Hardware | https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete
  A working assumption of much quantum error correction (QEC) is that noise can be modeled as a discrete set of Pauli errors acting on two-level systems. We ask what it costs, in information-theoretic terms, to impose this digital abstraction on hardware whose native dynamics are continuous. Using the framing of the QNFO corpus — in particular the observation that a transmon is better described as a
  Full text (https://papers.qnfo.org/papers/the-price-of-the-digital-abstraction-entropy-and-encoding-overhead-when-discrete), excerpts of its own sections:
  § 1. Introduction: Quantum error correction (QEC) as usually taught and deployed assumes a lattice of qubits, a discrete error set $\{I, X, Y, Z\}$, and a threshold theorem guaranteeing that if physical error rates lie below a threshold, arbitrarily long computation is possible with polylogarithmic overhead. This package of assumptions is an engineering convenience. [...]
  § 5. Results: All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured. 1. **Register entropy of digitization** (Input: $d = 12$ from [10]): $H_{\mathrm{reg}}(12) = \log_2 12 = 3.584963$ bits per mode per use. 2. **Base truncation entropy** (Inputs: $d = 12$ from [10]; definition from [10]): $S_{\mathrm{Base}}(12) = \ln 6 = 1.791759$ nats $= 2.584963$ bits. 3. **Binary encoding overhead** (Input: $d = 12$): $m = 4$ qubits; wasted levels $= 4$; dimension overhead $= 16/12 = 1.333333$; encoding efficiency $\eta = 0.896241$; idle fraction $= 0.1037594$. 4. **Entropy distortion under Pauli twirling** (Input: $\gamma = 10^{-3}$, assumed operating point): $H_{\mathrm{env}}^{\mathrm{phys}} = 1.140776 \times 10^{-2}$ bits; $H_{\mathrm{env}}^{\mathrm{twirl}} = 1.290776 \times 10^{-2}$ bits; distortion $\Delta H = 1.500 \times 10^{-3}$ bits per use; ratio $= 1.131489$ (the discrete surrogate overstates environment entropy by $\approx 13.1\%$ at matched total error probability). 5. [...]
  § 6. Discussion: **What we have and have not shown.** We have derived exact entropy and dimension quantities for idealized single-mode and single-qubit channels. We have not simulated a Josephson circuit, nor compared discrete Pauli channels against continuous drift in a dynamical simulation; that remains future work. Our results quantify the *bookkeeping* face of the digital abstraction; whether it translates into a *fundamental* lower bound on QEC overhead as a function of Hilbert-space continuity is conjecture. **The strongest argument against our own thesis.** Entry [10] itself corrects the premise we build on: the transmon spectrum IS discrete by Planck quantization, and binary truncation is a radix error, not a physics error. If the territory is already discrete (a qudit of $d \approx 12$), then the "continuity" we invoke is partly an artifact of the harmonic-oscillator idealization, and our overhead is an encoding inefficiency ($\eta = 0.896$, overhead $4/3$) that better radix choices — qudit encodings, ternary logic, or $d$-ary digitization — could eliminate. [...]
  § 7. Conclusion: We have quantified, with fully shown arithmetic, four faces of the cost of imposing a digital abstraction on bosonic quantum hardware: a register-entropy floor of $\log_2 12 \approx 3.585$ bits per digitized mode per use; a base truncation entropy of $\ln 6 \approx 1.792$ nats $\approx 2.585$ bits as proposed in [10]; a binary-encoding inefficiency of $\eta \approx 0.896$ with dimension overhead $4/3$; and a Pauli-twirling entropy distortion of $1.500 \times 10^{-3}$ bits per use (ratio $\approx 1.131$) at $\gamma = 10^{-3}$, in which the discrete surrogate overstates environment entropy despite matching total error probability exactly. A negative result bounds discarded leakage weight at $\approx 3.20 \times 10^{-13}$ for cold modes. These quantities support the conjecture that the digital abstraction carries a measurable, computable price — while the Rosetta correction in [10] tempers the claim: the price may be a radix mismatch rather than a fight against physics. Distinguishing these readings is, in our view, the most valuable next experiment.
[9] QNFO: Locale Framework Applied to Quantum Computing Innovations & Practical Applications | https://papers.qnfo.org/papers/locale-framework-quantum-applications
  Quantum computing is often presented through a small set of recurring claims: continuous-variable systems are naturally advantaged, more modes means more power, quantum advantage has been demonstrated at device level, statistics could in principle be non-standard, complex amplitudes are essential, approximation-based gate synthesis is the only approach, a transmon is a qubit, and fault tolerance i
  Full text (https://papers.qnfo.org/papers/locale-framework-quantum-applications), excerpts of its own sections:
  § 1. Introduction: The quantum computing field rests on a handful of sentences that are repeated so often they are no longer questioned. Continuous-variable systems, we are told, have a natural advantage because the physical world is continuous. More modes means more power. A fifty-qubit processor has demonstrated quantum advantage. Statistics could, in principle, be non-standard. Complex numbers are essential to quantum theory. Gate synthesis is an approximation problem. A transmon is a qubit. Fault tolerance is five years away. Each of these sentences is true in some sense. Each is also false in another. This is not a contradiction; it is the normal condition of physical statements. Every physical claim holds only within a specified domain of applicability — a particular vacuum or symmetry sector, an energy scale, a noise regime, a measurement model, or a set of boundary conditions. [...]
  § 2. The locale framework in brief: The companion record [1] develops four moves. First, *locale-conditionality*: every physical statement holds only within a locale, and the interesting physics lives at the seams where a rule fails to transfer. Second, *map and territory*: pedagogical maps (the spinning sphere for spin, the billiard balls for thermodynamics) fail at seams, while the territory — the transformation law, the algebra, the invariant — transfers. Third, the *rendering interface*: an observer inside a rendering experiences the metric of the image space, not the metric of the substrate, and no finite set of first-person observations decides between an Archimedean and an ultrametric substrate — yet a rendering with structure leaks structure. Fourth, *scale primitives*: stripped of anthropocentric units, the natural observables are counts and ratios. This paper needs none of that machinery in full. [...]
  § 3. Eight claims and their boundaries: Table 1 states eight claims that are heard constantly in quantum computing, the domain within which each holds, the boundary at which it fails, and the work that documents the boundary — presented at QPL 2026, with one arXiv exception. The table is the paper in miniature. **Table 1.** Widely repeated claims in quantum computing, their domains of validity, and the boundaries documented at QPL 2026 (one by an independent arXiv result). [...]
  § 8. Conclusions: Eight claims, eight boundaries, one conference week — and one independent arXiv result. The practical content of this paper is Table 1: a locale-indexed map of the claims that quantum computing practitioners hear every day, each paired with the exact paper — presented at QPL 2026, with one arXiv exception — that documents where it breaks. The theoretical content is the observation that the same structure appears in every row — a claim true within a domain, failing at a boundary, and the physics of interest living at the boundary. Three conclusions follow. First, claims are conditional truths. The habit of stating them without their conditions is the single most expensive ambiguity in the field, because it is what allows a roadmap to be read as a promise and a benchmark as a product. Second, the boundaries are public. The QPL 2026 program — one week, one venue — contains the documentation of every boundary in Table 1 but one, an independent arXiv result; the audit is public either way. [...]
[10] QNFO: Project Rosetta: The Approximation Entropy & The Fractal Limits of Digital Physics — v2.0 | https://papers.qnfo.org/papers/rosetta-fractal-math
  V2.0 / Rosetta v4.0 with Planck-Radix Correction + Qudit Manifesto. Corrects V1.0: transmon spectrum IS discrete (Planck quantization), binary truncation is a radix error not physics error. Transmon is a qudit (d~12), not a qubit. S_Base = ln(d/2) ~ 1.79 nats. 11-page PDF.
  Full text (https://papers.qnfo.org/papers/rosetta-fractal-math), excerpts of its own sections:
  § 1.1 The Map-Territory Problem: The global quantum computing industry has absorbed approximately 35 billion dollars in combined public and private investment over two decades while delivering zero commercially viable machines [@QNFO2026QubitDelusionI]. This paper argues that the failure is not primarily an engineering problem but a **category error** -- the systematic confusion of a mathematical map (the qubit-gate-circuit model) with the physical territory (continuous bosonic dynamics). The qubit is a **scaffold**, not an invariant. The gate is a projection, not an operation. The surface code is a mathematical trick, not a physical law.
  § 1.2 Statement of Results: | Axis | Core Result | |:-----|:------------| | **1.** Categorical Foundations | The functor $F: \mathcal{P} \to \mathcal{C}$ is non-exact (Theorem 1) | | **2.** Algebraization Complexity | $\cos(\phi)$ requires degree-224 polynomial for spectral fidelity $10^{-4}$ | | **3.** Thermodynamics of Translation | Rosetta's Constant $R = k_B T \ln(1/\alpha_r)$ | | **4.** Complexity Bounds | Digital Speed Limit: depth grows exponentially in qubit count $Q$ | | **5.** Experimental Protocol | Translation Calorimeter -- falsifiable measurement of $S_A$ | | **HAL.** Hidden Axioms | $S_{\text{Total}} = S_{\text{Obs}} + S_{\text{Base}} + S_{\text{Arch}} + S_{\text{Alg}} + S_{\text{Trot}}$ |
  § 1.3 Prior Art: This work builds on and extends several independent lines of inquiry. De Gosson [-@deGosson2012SymplecticCamel] first framed the conflict between geometry and algebra in quantum information using Gromov's non-squeezing theorem, but stopped at the existence argument without quantification. The QNFO's "Qubit Delusion" series [@QNFO2026QubitDelusionI; @QNFO2026BeyondTheQubit; @QNFO2026PhysicsOfComputation; @QNFO2026ProblemSubstrateMapping; @QNFO2026ManifestoHonestComputation] provided the philosophical scaffolding. Our contribution is the quantitative framework: explicit derivations of $S_A$, Rosetta's Constant $R$, and the formal categorical proof of non-exactness.
  § 2.1 Category $\mathcal{P}$: Physical Dynamics: $\mathcal{P}$ has as objects **symplectic manifolds** $(M^{2n}, \omega)$. Morphisms are Hamiltonian flows $\varphi_t^H: M \to M$ generated by $H: M \to \mathbb{R}$, or unitarily via $U(t) = e^{-iHt/\hbar}$. [...]
  § 2.3 Theorem 1: Non-Exactness: **Theorem 1.** *$F: \mathcal{P} \to \mathcal{C}$ is not exact -- there exist invariants preserved in $\mathcal{P}$ with no image in $\mathcal{C}$.* *Proof.* By Gromov's non-squeezing theorem [-@Gromov1985]: the symplectic capacity $c_G(M, \omega)$ is invariant under symplectomorphisms. Under $F$, this maps to a finite discrete point set with zero capacity. An invariant in the source with no image in the target -- the defining signature of a non-exact functor. $\square$
  § 8. Discussion: The transmon is not a "bad qubit." It is succeeding at being a bosonic computer. Three paths forward: 1. **Embrace analog:** Use transmons for analog quantum simulation of bosonic Hamiltonians 2. **Switch to fermions:** Spins and ions have native discrete spectra -- the functor $F$ may be exact for them 3. **Build hybrid architectures:** Bosonic coprocessor + fermionic digital core, with bounded $S_A$ at the interface
  § 10. Conclusion: Digital computation is an engineering triumph but not a universal ontology. The universe runs on complex amplitudes and continuous phase, not binary. The Approximation Entropy $S_A$ quantifies the distance between computational control and physical understanding -- in Joules.
[11] QNFO: Constant-Sized-Support Magic State Distillation with Qubit Recycling: A Reconciled Resource, Footprint, and Energy Analysis | https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile
  Magic state distillation (MSD) is the canonical route to non-Clifford gates in fault-tolerant quantum computation, but conventional nested factories exhibit qubit occupancy that grows multiplicatively with the number of distillation rounds. Recent work on constant-sized-support distillation protocols with qubit recycling (arXiv:2609.17044v1) proposes to hold the active qubit footprint fixed across
  Full text (https://papers.qnfo.org/papers/constant-sized-support-magic-state-distillation-with-qubit-recycling-a-reconcile), excerpts of its own sections:
  § 1. Introduction: Fault-tolerant quantum computation requires a gate set executed with error rates far below the threshold of the underlying quantum error-correcting code. For most code families, the transversal or lattice-surgery-accessible gate set is Clifford-only and therefore classically simulable; the non-Clifford component, canonically the T gate, must be supplied by injecting specially prepared "magic" states whose fidelity must exceed what direct preparation achieves [1], [6], [8]. [...]
  § 5. Results: All numbers below are computed in Section 4 or labeled projections. 1. **Error suppression (computed).** A two-round 15-to-1 ladder suppresses input error p to 1,500,625 p⁹. At p = 10⁻³ the output error is 1.500625 × 10⁻²¹; at p = 10⁻² it is 1.500625 × 10⁻¹². The leading-order model is valid for 35 p² ≪ 1 (satisfied at both evaluation points). 2. **Peak occupancy (computed from stated premises).** Conventional nested two-round factory: 240 qubits. Recycled constant-support factory with S = 15, B = 15: 30 qubits. Reduction factor: 8.0×. 3. **Throughput bound (computed, bounding pair).** With equal per-round cycle times, the recycled design matches baseline throughput only if its block cycles 15× faster or 15 blocks run round-robin; otherwise per-hardware throughput falls by up to 15×. The occupancy gain of 8× and the worst-case throughput loss of 15× do not commute to a win: the design is net-beneficial in space-time only if the achievable speedup factor exceeds 15/8 ≈ 1.875. 4. [...]
  § 6. Discussion: **Limitations.** The analysis is deliberately minimal. The 35 p³ coefficient is a standard leading-order figure for the 15-to-1 family, not a coefficient verified for the specific protocol family of [1]; if the recycling protocols use different blocks, both the exponent and coefficient change, and Derivation 1's numbers change with them. The occupancy comparison assumes the constant-support premise (S = 15) and a minimal buffer (B = 15); the actual paper may require larger support or additional ancilla for error tracking, which would erode the 8× factor proportionally. The energy attribution of Model D assumes magic-state preparation and reset dominate the benchmark's quantum energy budget; in practice control electronics, cryogenic cooling, and syndrome extraction also consume significant power, and if these dominate, the projected savings from recycling would be smaller. The equality E_p = E_r is a simplification: reset may be cheaper (rapid measurement) or more expensive (active cooling), shifting the balance between the two terms of E₁. [...]
  § 7. Conclusion: We have built an explicit, fully arithmetized resource-budget model of constant-sized-support magic state distillation with qubit recycling. The computed results are: two-round error suppression to 1,500,625 p⁹ (1.500625 × 10⁻²¹ at p = 10⁻³; 1.500625 × 10⁻¹² at p = 10⁻²); a peak-occupancy reduction from 240 to 30 qubits (8.0×) under the stated constant-support and buffer premises; a raw-state efficiency ratio of 8.0×; a recycling budget of at most 10 reuses under the projected δ = 10⁻⁵, with an uncertainty span of 1–100 reuses; and, under an explicitly adopted energy-attribution convention anchored to publicly reported benchmark data [10], ≈ 0.55 ± 0.07 J per distilled magic state against a 1.5 × 10⁷ quantum-to-classical energy ratio. The proposal thus converts a spatial cost into an operational-quality cost and a temporal serialization cost. [...]