# CSS Codes for Quantum Metrology with Discrete-Time Error Correction: A Reconciled Quantitative Analysis

## Abstract

Quantum metrology promises estimation precision scaling as the Heisenberg limit $\Delta\omega \sim 1/(NT)$ rather than the standard quantum limit (SQL) $\Delta\omega \sim 1/\sqrt{NT}$, but noise typically destroys this advantage. Recent work showed that when the noise is perpendicular to the sensing Hamiltonian — the regime permitted by the Hamiltonian-Not-in-Lindblad-Span (HNLS) condition — discrete-time quantum error correction with Calderbank-Shor-Shor (CSS) codes preserves Heisenberg-like temporal scaling over a finite interrogation window whose duration depends on the correction frequency, and that recovery applied only after sensing gives no advantage. This paper reconciles three independent quantitative treatments of that framework into a single arithmetic-transparent analysis. Under a stated convention of independent per-qubit errors with probability $p = 10^{-3}$ per correction cycle, we derive per-cycle logical failure probabilities $P_{\mathrm{fail}}^{(\mathrm{Steane})} \approx 2.09 \times 10^{-5}$ and $P_{\mathrm{fail}}^{(\mathrm{Shor})} \approx 3.58 \times 10^{-5}$ for the $[[7,1,3]]$ Steane and $[[9,1,3]]$ Shor codes, corresponding to interrogation windows of approximately $23.9$ ms and $14.0$ ms at a $1\,\mu$s correction period for a failure budget $\varepsilon = 0.5$. We show that at these parameters the Heisenberg-to-SQL crossover lies outside the window, but that reducing $p$ to $10^{-4}$ places the crossover comfortably inside. We prove via channel composition that post-hoc recovery cannot outperform the uncorrected protocol, and we document all convention choices and divergences among the source drafts explicitly.

## 1. Introduction

The central promise of quantum metrology is that entangled probes can estimate an unknown parameter $\omega$ with variance scaling as $1/N^2$ in the probe number $N$ (Heisenberg scaling) rather than $1/N$ (standard quantum limit, SQL). In any realistic implementation, decoherence couples the probe to its environment and restores SQL-like or worse scaling precisely where the quantum advantage matters [8]. The structural resolution is now known: Heisenberg scaling under active correction is achievable if and only if the signal Hamiltonian lies outside the Lindblad span of the noise operators — the HNLS condition [3].

The work under analysis [2] (retrieved as the identical query record [1]) develops this program for CSS codes — stabilizer codes built from two classical codes whose stabilizer generators split into $X$-type and $Z$-type sets — with correction applied at discrete times during sensing. Its qualitative results are: (i) for noise perpendicular to the sensing Hamiltonian, discrete-time correction preserves Heisenberg-like temporal scaling over a finite interrogation window set by the correction frequency; (ii) recovery applied only after sensing gives no metrological advantage; (iii) the framework is instantiated on the Steane and Shor codes.

This paper is the reconciled quantitative companion to that analysis, produced from three independent drafts. Its contributions are:

1. A single, explicitly stated set of modeling conventions (Section 3), chosen from among the drafts and documented against the alternatives (Appendix A).
2. Fully shown arithmetic for the per-cycle logical failure probabilities of the Steane and Shor codes, the interrogation windows, the QFI retention at the window edge, and the Heisenberg-to-SQL crossover (Section 4).
3. A channel-composition argument for result (ii) that requires no numerics.
4. An explicit divergence report and claim-attribution table (Appendices A and B), including one arithmetic correction applied to a source draft.

Throughout, "Heisenberg-like" means that the mean-squared error scales as $1/T^2$ in interrogation time $T$ over a finite window; under any nonzero logical failure rate the asymptotic advantage must degrade.

## 2. Background and Related Work

**The target protocol.** Reference [2], the primary object of this study (with [1] being the identical fetched record), develops a quantum-metrology protocol based on CSS codes in which error correction is applied at discrete times during the sensing evolution. Its abstract states the three results enumerated above; our Sections 3–5 supply the per-code arithmetic that makes them concrete.

**HNLS and codeword counting.** Reference [3] establishes the HNLS condition — Heisenberg scaling is achievable if and only if the signal Hamiltonian is orthogonal to the span of the Lindblad operators — and explains robust metrology by counting codewords, i.e., by the fraction of codewords that remain distinguishable under the noise. Our model satisfies HNLS by construction, and our failure-probability counting (weight-$\ge 2$ error patterns) is the finite-$$N$$ shadow of the codeword-counting logic of [3].

**CSS code theory.** Reference [6] surveys the passage from classical error-correcting codes to quantum ones, emphasizing that quantum channels behave differently from classical channels and that CSS-style constructions import classical machinery; we use its nested-classical-codes picture throughout. Reference [7] analyzes CSS code performance on symmetric and asymmetric channels via the quantum MacWilliams identities, deriving weight enumerators of undetectable errors and tight upper bounds on logical error rates; our per-cycle failure probabilities are the leading terms of exactly the enumerator quantities that [7] systematizes.

**Entanglement-assisted and topological variants.** Reference [4] provides a self-contained introduction to entanglement-assisted quantum error-correcting codes, which generalize CSS constructions by pre-shared entanglement and could relax duality constraints; whether such codes improve the metrological window is an open question (Section 6). Reference [10] constructs toric and burst-error-correcting quantum codes from lattice codes with interleaving against clustered errors — relevant because metrological probes such as ion chains may suffer spatially correlated noise, violating the independence assumption we adopt.

**Continuous-time correction.** Reference [5] treats continuous-time quantum error correction (CTQEC), in which noise and correction are both continuous processes implemented via weak measurement and feedback, analyzed through the subsystem principle. Discrete-time correction, the subject of [2] and this paper, is the complementary regime; our window-duration results quantify what is lost relative to the CTQEC idealization.

**Fault-tolerant state preparation.** Reference [9] addresses fault-tolerant preparation of CSS stabilizer states from classical codes — a necessary ingredient for any deployment, since each sensing run must begin in a codeword superposition prepared without propagating errors.

**Noisy-era context.** Reference [8] surveys quantum metrology in the noisy intermediate-scale quantum (NIS) era, cataloguing decoherence-limited applications from frequency standards to magnetometry; our crossover time $T_{\mathrm{cross}}$ determines whether a device with a given coherence budget sits inside or outside the protected window.

## 3. Methods

### 3.1 Conventions (reconciled)

The three source drafts used different error models and figures of merit. For the main text we adopt the following convention, chosen because two of three drafts converged on its Steane number and it yields the most concrete, hardware-translatable quantities (alternatives are documented in Appendix A):

- **Error model:** independent errors per physical qubit per correction cycle, with probability $p$ of any non-identity Pauli error ($p = 10^{-3}$, a stated modeling assumption representative of current two-qubit gate error rates as an order of magnitude; it is an assumption, not a measurement).
- **Codes:** Steane $[[7,1,3]]$ ($n = 7$) and Shor $[[9,1,3]]$ ($n = 9$), both of distance $d = 3$, correcting $t = \lfloor (d-1)/2 \rfloor = 1$ arbitrary single-qubit error.
- **Correction period:** $\Delta t = 1\,\mu\mathrm{s} = 10^{-6}\,\mathrm{s}$ (stated assumption).
- **Failure budget:** $\varepsilon = 0.5$ (stated assumption: we accept cumulative failure probability $\approx \varepsilon$ at the window edge).

### 3.2 Logical failure probability per cycle

A logical failure occurs when the accumulated errors in one cycle form an undetectable or mis-corrected pattern, i.e., a pattern of weight $\ge t+1 = 2$ that maps codewords to codewords [7]. We take as the per-cycle failure probability the probability of two or more errors in the block,

$$P_{\mathrm{fail}}(n, p) = \sum_{k=2}^{n} \binom{n}{k} p^k (1-p)^{n-k},$$

evaluated through its leading terms. This is a modeling choice: it counts all weight-$\ge 2$ patterns as failures, which is exact for perfect non-degenerate codes at $t = 1$ and approximate for the degenerate Shor code (Section 6).

### 3.3 Figures of merit

- **Interrogation window** $T_{\max}(\varepsilon) = \varepsilon \Delta t / P_{\mathrm{fail}}$: the total sensing time at which the expected number of logical failures reaches $\varepsilon$; with independent per-cycle failures the cumulative failure probability is $1 - e^{-\varepsilon} \approx \varepsilon$ for small $\varepsilon$.
- **QFI retention** (labeled projection): with independent per-cycle survival, the modeled QFI is $F_{\mathrm{model}} = N^2 T^2 (1 - P_{\mathrm{fail}})^{K}$ with $K = T/\Delta t$ cycles.
- **Crossover time** $T_{\mathrm{cross}}$: the interrogation time at which Heisenberg-like and SQL-like precisions are equal.

### 3.4 Post-hoc recovery cannot help

If recovery is applied only after the full sensing evolution, the sensing channel is $\mathcal{R} \circ \Lambda_T$, where $\Lambda_T$ is the noisy parameter-dependent channel and $\mathcal{R}$ is a trace-preserving, $\omega$-independent recovery. By data processing, the quantum Fisher information of $(\mathcal{R} \circ \Lambda_T)(\rho)$ cannot exceed that of $\Lambda_T(\rho)$: a terminal recovery acts on syndrome information but cannot restore phase coherence already scrambled by uncorrected physical errors during the evolution. Hence post-hoc recovery yields no advantage over the uncorrected protocol, in agreement with [2]. The mechanism is temporal: correction must remove errors *before* they accumulate into logical phase noise.

## 4. Analysis

All inputs are stated; all arithmetic is shown.

**Input 1.** Code parameters: Steane $[[7,1,3]]$, Shor $[[9,1,3]]$ (standard; both correct $t = 1$ arbitrary single-qubit Pauli error).

**Input 2.** Per-qubit per-cycle error probability $p = 10^{-3}$ (stated assumption).

**Input 3.** Correction period $\Delta t = 10^{-6}\,\mathrm{s}$ (stated assumption).

**Input 4.** Failure budget $\varepsilon = 0.5$ (stated assumption; actual cumulative failure probability at the window edge is $1 - e^{-0.5} \approx 0.393$).

### 4.1 Steane code failure probability

The leading term is the exactly-two-error probability:

$$\binom{7}{2} = \frac{7 \times 6}{2} = 21, \qquad p^2 = (10^{-3})^2 = 10^{-6},$$

$$(1-p)^5 = (0.999)^5 = 1 - 5 \times 10^{-3} + 10 \times 10^{-6} - 10 \times 10^{-9} + \cdots \approx 0.995010.$$

$$P_2 = 21 \times 10^{-6} \times 0.995010 = 2.08952 \times 10^{-5}.$$

The three-error term:

$$\binom{7}{3} = 35, \qquad 35 \times 10^{-9} \times (0.999)^4 \approx 35 \times 10^{-9} \times 0.996006 = 3.486 \times 10^{-8}.$$

Total:

$$P_{\mathrm{fail}}^{(\mathrm{Steane})} = 2.08952 \times 10^{-5} + 0.03486 \times 10^{-5} \approx 2.09 \times 10^{-5} \text{ per cycle}.$$

### 4.2 Shor code failure probability

Exactly two errors:

$$\binom{9}{2} = 36, \qquad (0.999)^7 \approx 1 - 7 \times 10^{-3} + 21 \times 10^{-6} \approx 0.993021,$$

$$P_2 = 36 \times 10^{-6} \times 0.993021 = 3.57488 \times 10^{-5}.$$

Exactly three errors:

$$\binom{9}{3} = 84, \qquad 84 \times 10^{-9} \times (0.999)^6 \approx 84 \times 10^{-9} \times 0.994015 = 8.350 \times 10^{-8}.$$

Exactly four errors: $\binom{9}{4} = 126$, contributing $126 \times 10^{-12} \times 0.995 \approx 1.25 \times 10^{-10}$, negligible. Total:

$$P_{\mathrm{fail}}^{(\mathrm{Shor})} = 3.57488 \times 10^{-5} + 0.08350 \times 10^{-5} + 0.0000125 \times 10^{-5} \approx 3.58 \times 10^{-5} \text{ per cycle}.$$

(Note: source draft C reported $3.66 \times 10^{-5}$ here due to an addition slip — $3.5749 \times 10^{-5} + 0.0835 \times 10^{-5} = 3.583 \times 10^{-5}$, not $3.658 \times 10^{-5}$; see Appendix A.)

The Steane code fails less often per cycle at equal distance because its block is smaller ($7$ vs. $9$ qubits), reducing the combinatorial factor from $36$ to $21$.

### 4.3 Interrogation windows

$$T_{\max}^{(\mathrm{Steane})} = \frac{\varepsilon \Delta t}{P_{\mathrm{fail}}} = \frac{0.5 \times 10^{-6}\,\mathrm{s}}{2.09 \times 10^{-5}} = \frac{0.5}{2.09} \times 10^{-1}\,\mathrm{s} = 2.39 \times 10^{-2}\,\mathrm{s} \approx 23.9\,\mathrm{ms}.$$

$$T_{\max}^{(\mathrm{Shor})} = \frac{0.5 \times 10^{-6}\,\mathrm{s}}{3.58 \times 10^{-5}} = 1.397 \times 10^{-2}\,\mathrm{s} \approx 14.0\,\mathrm{ms}.$$

Cycle counts: $K_{\mathrm{Steane}} = 2.39 \times 10^{-2} / 10^{-6} = 23900$; $K_{\mathrm{Shor}} = 13970$.

### 4.4 QFI retention at the window edge (projection)

Under the independent-failure model of Section 3.3, at $T = T_{\max}^{(\mathrm{Steane})}$, $K = 23900$:

$$(1 - P_{\mathrm{fail}})^K = \left(1 - 2.09 \times 10^{-5}\right)^{23900} \approx e^{-23900 \times 2.09 \times 10^{-5}} = e^{-0.4995} \approx 0.607.$$

This matches the budget by construction ($e^{-\varepsilon} = e^{-0.5} = 0.6065$), an internal consistency check of the window definition. The Heisenberg prefactor $N^2 T^2$ is thus retained at $\approx 60.7\%$ at the window edge — a projection under the stated model, not a measurement.

### 4.5 Heisenberg-to-SQL crossover

Setting $\Delta\omega_{\mathrm{H}}(T) = \Delta\omega_{\mathrm{SQL}}(T)$ with $\Delta\omega_{\mathrm{H}} = 1/(NT)$ and $\Delta\omega_{\mathrm{SQL}} = 1/\sqrt{NT}$:

$$\frac{1}{NT} = \frac{1}{\sqrt{NT}} \implies NT = 1 \implies T_{\mathrm{cross}} = \frac{1}{N} = \frac{1}{7}\,\mathrm{s} \approx 0.143\,\mathrm{s}.$$

Since $T_{\mathrm{cross}} = 0.143\,\mathrm{s} > T_{\max} = 23.9\,\mathrm{ms}$ at $p = 10^{-3}$ and $\Delta t = 1\,\mu$s, the corrected protocol under this model does **not** beat the ideal SQL benchmark within its own window at these parameters. The crossover requires smaller $p$, faster correction, or larger $N$.

**Sensitivity check.** Reducing $p$ to $10^{-4}$: $P_{\mathrm{fail}}^{(\mathrm{Steane})} \approx \binom{7}{2} (10^{-4})^2 (1 - 10^{-4})^5 \approx 21 \times 10^{-8} \times 0.9995 = 2.10 \times 10^{-7}$, giving

$$T_{\max} = \frac{0.5 \times 10^{-6}}{2.10 \times 10^{-7}} = 2.38\,\mathrm{s} > T_{\mathrm{cross}} = 0.143\,\mathrm{s}.$$

The window then comfortably contains the crossover and the Heisenberg-like regime is operative. This $p$-sensitivity is itself a quantitative result of the analysis.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs ($p = 10^{-3}$ per cycle, $\Delta t = 1\,\mu$s, $\varepsilon = 0.5$, independent-error model); QFI retention figures are labeled projections under that model.

1. **Per-cycle logical failure probabilities:** Steane $P_{\mathrm{fail}} \approx 2.09 \times 10^{-5}$; Shor $P_{\mathrm{fail}} \approx 3.58 \times 10^{-5}$.
2. **Interrogation windows:** Steane $T_{\max} \approx 23.9\,\mathrm{ms}$ ($K \approx 23900$ cycles); Shor $T_{\max} \approx 14.0\,\mathrm{ms}$ ($K \approx 13970$ cycles).
3. **QFI retention at window edge (projection):** $\approx 60.7\%$ of the ideal Heisenberg prefactor $N^2 T^2$, consistent with $e^{-0.5} = 0.6065$.
4. **Crossover:** $T_{\mathrm{cross}} = 1/7\,\mathrm{s} \approx 0.143\,\mathrm{s}$ for $N = 7$; at $p = 10^{-3}$ the crossover lies outside the window; at $p = 10^{-4}$ the window ($\approx 2.38\,\mathrm{s}$) contains it.
5. **Post-hoc recovery:** no metrological advantage over the uncorrected protocol, by the data-processing argument of Section 3.4.

## 6. Discussion

**Limitations.** (1) The failure model counts all weight-$\ge 2$ patterns as failures; for the degenerate Shor code some such patterns are correctable or harmless, so $P_{\mathrm{fail}}^{(\mathrm{Shor})}$ is an upper-bound-style estimate. (2) Independence of errors per cycle ignores temporally or spatially correlated noise; burst-error constructions [10] or entanglement-assisted codes [4] would be needed for correlated noise. (3) Syndrome extraction is assumed instantaneous and error-free; real implementations add time and gate errors, shrinking the window. (4) The QFI retention figure is a projection of a specific independent-failure model, not a measurement. (5) The crossover comparison uses ideal SQL and Heisenberg scalings; finite-$N$ constants are ignored.

**Failure modes and falsifiability.** The central claim — that discrete-time CSS correction preserves Heisenberg-like scaling over a finite window — would be falsified if experiments showed QFI decaying faster than the modeled $(1 - P_{\mathrm{fail}})^K$ suppression at the stated $p$ and $\Delta t$, or if measured logical failure rates exceeded the binomial prediction systematically. If post-hoc recovery were observed to beat the uncorrected protocol, the data-processing argument of Section 3.4 (which assumes an $\omega$-independent recovery) would be implicated.

**Open questions.** Optimal correction frequency trading measurement overhead against decoherence suppression; whether entanglement-assisted [4] or continuous-time [5] schemes extend the window; multi-parameter sensing; and the interplay of code rate with the $N$ entering the Heisenberg factor.

**Bibliography limitation.** The provided bibliography contains 14 entries; this paper cites entries [1]–[10]. Entries [11]–[14] (qLDPC/threshold, bosonic codes, planar modules, threshold ensemble effects) were not retained because the source drafts' claims referencing them could not be substantiated within this analysis.

## 7. Conclusion

We reconciled three independent analyses of discrete-time quantum error correction for quantum metrology with CSS codes into a single arithmetic-transparent treatment. Under a stated convention of independent per-qubit errors with probability $p = 10^{-3}$ per correction cycle of duration $\Delta t = 1\,\mu\mathrm{s}$, the $[[7,1,3]]$ Steane code yields a per-cycle logical failure probability $P_{\mathrm{fail}} \approx 2.09 \times 10^{-5}$ and an interrogation window $T_{\max} \approx 23.9\,\mathrm{ms}$ at failure budget $\varepsilon = 0.5$; the $[[9,1,3]]$ Shor code yields $P_{\mathrm{fail}} \approx 3.58 \times 10^{-5}$ and $T_{\max} \approx 14.0\,\mathrm{ms}$. At these parameters the Heisenberg-to-SQL crossover time $T_{\mathrm{cross}} = 1/7\,\mathrm{s} \approx 0.143\,\mathrm{s}$ lies outside the protected window, while reducing $p$ to $10^{-4}$ extends the window to $\approx 2.38\,\mathrm{s}$ and places the crossover comfortably inside — a sensitivity result that identifies physical error rate, not correction period, as the binding constraint under this model. A channel-composition argument shows that recovery applied only after sensing cannot outperform the uncorrected protocol, consistent with the qualitative claim of [2]. All convention choices, one corrected arithmetic slip in a source draft, and the full claim-attribution record are documented in Appendices A and B, so that any reader can re-derive every number from the stated inputs alone.

## Appendix A. Divergence report

The three source drafts (A, B, C) diverged on the following points. Each divergence is stated with both sides and the convention adopted in the main text.

**D1. Error model and figure of merit.** Drafts A and B modeled independent per-qubit Pauli errors with probability $p$ per correction cycle and reported per-cycle logical failure probabilities and interrogation windows; draft C instead reported a continuous-time decoherence rate and a QFI-decay constant. *Convention adopted:* the discrete-time independent-error model (A/B), because it matches the discrete-time correction protocol of [2] and yields hardware-translatable quantities. Draft C's continuous-time picture is recoverable from ours in the limit $\Delta t \to 0$ at fixed $p/\Delta t$.

**D2. Steane failure probability.** Drafts A and B converged on $P_{\mathrm{fail}}^{(\mathrm{Steane})} \approx 2.09 \times 10^{-5}$ at $p = 10^{-3}$; draft C reported the same leading term. *Status:* CONVERGENT, adopted.

**D3. Shor failure probability.** Drafts A and B reported $P_{\mathrm{fail}}^{(\mathrm{Shor})} \approx 3.58 \times 10^{-5}$; draft C reported $3.66 \times 10^{-5}$. *Resolution:* draft C's value contains an addition slip — its own components sum to $3.5749 \times 10^{-5} + 0.0835 \times 10^{-5} = 3.583 \times 10^{-5}$, not $3.658 \times 10^{-5}$. The main text uses $3.58 \times 10^{-5}$ (the corrected sum), and the slip is recorded here rather than silently discarded.

**D4. Window definition.** Draft A defined $T_{\max}$ via expected number of failures $\le \varepsilon$; draft B via cumulative failure probability $\le \varepsilon$; draft C via QFI retention $\ge 1 - \varepsilon$. For small $\varepsilon$ these coincide to leading order: with independent per-cycle failures, the cumulative probability is $1 - e^{-\varepsilon} \approx \varepsilon$ and the QFI retention is $e^{-\varepsilon}$. *Convention adopted:* draft A's definition, with the exact cumulative value $1 - e^{-0.5} \approx 0.393$ and retention $e^{-0.5} = 0.6065$ reported as consistency checks (Section 4.4).

**D5. Crossover convention.** Drafts A and C compared against the ideal SQL $\Delta\omega_{\mathrm{SQL}} = 1/\sqrt{NT}$; draft B used a resource-counted SQL with a factor-of-2 prefactor. *Convention adopted:* the ideal comparison (A/C), with the caveat that finite-$N$ constants are ignored (Section 6, limitation 5). Under draft B's convention $T_{\mathrm{cross}}$ would shift by a factor of order unity, not changing the qualitative conclusion at $p = 10^{-3}$.

## Appendix B. Claim attribution

| Claim | Statement | Drafts | Status |
|---|---|---|---|
| C1 | HNLS condition governs achievability of Heisenberg scaling | A, B, C | CONVERGENT |
| C2 | Discrete-time CSS correction preserves Heisenberg-like scaling over a finite window | A, B, C | CONVERGENT |
| C3 | Post-hoc recovery gives no metrological advantage | A, B, C | CONVERGENT |
| C4 | $P_{\mathrm{fail}}^{(\mathrm{Steane})} \approx 2.09 \times 10^{-5}$ at $p = 10^{-3}$ | A, B, C | CONVERGENT |
| C5 | $P_{\mathrm{fail}}^{(\mathrm{Shor})} \approx 3.58 \times 10^{-5}$ at $p = 10^{-3}$ | A, B ($3.58$) vs C ($3.66$, arithmetic slip) | DIVERGENT — resolved to $3.58 \times 10^{-5}$ (D3) |
| C6 | Window definition via expected failures $\le \varepsilon$ | A vs B vs C | DIVERGENT — resolved to A's definition (D4) |
| C7 | Crossover outside window at $p = 10^{-3}$, inside at $p = 10^{-4}$ | A, B | CONVERGENT (C silent) |
| C8 | QFI retention $\approx 60.7\%$ at window edge (projection) | A, B | CONVERGENT, labeled projection |
| C9 | Continuous-time decoherence-rate framing | C only | SINGLE — not adopted (D1) |

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.40022&amp;start=0&amp;max_results=1
[2] CSS codes for Quantum Metrology with Discrete-time Error Correction. arXiv:2609.40022v1. https://arxiv.org/abs/2609.40022v1
[3] Explaining Robust Quantum Metrology by Counting Codewords. arXiv:2503.15743v3. https://arxiv.org/abs/2503.15743v3
[4] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[5] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[6] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[7] Performance Analysis of Quantum CSS Error-Correcting Codes via MacWilliams Identities. arXiv:2305.01301v4. https://arxiv.org/abs/2305.01301v4
[8] Quantum metrology in the noisy intermediate-scale quantum era. arXiv:2307.07701v2. https://arxiv.org/abs/2307.07701v2
[9] Fault-tolerant Preparation of Stabilizer States for Quantum CSS Codes by Classical Error-Correcting Codes. arXiv:1605.05647v4. https://arxiv.org/abs/1605.05647v4
[10] Characterization of $n$-Dimensional Toric and Burst-Error-Correcting Quantum Codes from Lattice Codes. arXiv:2410.20233v1. https://arxiv.org/abs/2410.20233v1
[11] https://papers.qnfo.org/papers/from-random-quantum-codes-to-explicit-qld-codes-a-reconciled-threshold-analysis-/. QNFO: From Random Quantum Codes to Explicit qLD Codes: A Reconciled Threshold Analysis of the Quantum-LCL Framework.
[14] https://papers.qnfo.org/papers/ensemble-dependence-of-critical-exponents-at-quantum-error-correction-thresholds/. QNFO: Ensemble Dependence of Critical Exponents at Quantum Error Correction Thresholds: Analytic Mechanisms and Statistical Consequences.