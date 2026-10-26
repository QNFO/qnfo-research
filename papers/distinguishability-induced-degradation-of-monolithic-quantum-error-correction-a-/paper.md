# Distinguishability-Induced Degradation of Monolithic Quantum Error Correction: A Reconciled Analytic Study of Syndrome-Checking Constraints

## Abstract

Quantum error-correcting codes rely on the assumption that the environment cannot distinguish which error occurred on which codeword. Residual Zeeman, Stark, and anharmonic shifts in physical platforms break this assumption by imprinting error-dependent photon frequencies on the environment, converting an otherwise correctable noise process into one with inflated effective Kraus rank. We construct a minimal analytic model of this mechanism: a single logical error whose two environment branches carry Gaussian photon wavepackets separated in frequency by $\Delta\omega$. We derive the recovered fidelity $F = \frac{1}{2}(1+\operatorname{Re}s)$ for an equal-superposition input, where $s$ is the environment-state overlap, and prove the bound $F \ge 1 - D/2$ in terms of the distinguishability $D = 1-|s|^2 = 1-e^{-(\Delta\omega\sigma)^2}$ for wavepacket duration $\sigma$. We then derive an operational syndrome-checking constraint $T_{\mathrm{check}} \le \sqrt{\ln(1/(1-D_{\max}))}/\Delta\omega$ and evaluate it numerically: for a $1$ MHz frequency separation and a tolerable distinguishability of $10^{-2}$, the checking interval must not exceed $1.60\times 10^{-8}$ s ($16.0$ ns). We include all three model computations, reporting the checking intervals for the baseline tolerance and for a tighter tolerance. The analysis confirms, with explicit arithmetic, that error distinguishability is a practical limitation of monolithic error correction and that fast syndrome extraction is a quantifiable mitigation route.

## 1. Introduction

The theory of quantum error correction (QEC) rests on a deceptively simple requirement: the environment must not learn anything that distinguishes the correctable error processes from one another. When this requirement holds, the Knill–Laflamme conditions guarantee that a recovery operation restores the encoded state exactly. When it fails — because residual Zeeman shifts, Stark shifts, or anharmonicities in the underlying level structure make emitted photons carry error-dependent frequencies — perfect recovery is no longer possible, and the degradation grows with the frequency separation of the environmental records.

The recent work of Ref. [2] (fetched as the arXiv query record [1]) makes this precise with an analytically solvable four-level model and a canonical spontaneous-emission noise model for atoms and molecules. Its central findings are threefold: distinguishability raises the effective Kraus rank of the noise channel, lowers the recovered fidelity, and sets an operational checking time that shortens as the frequency separation between emitted photons increases. Rapid syndrome checking suppresses the buildup of distinguishability.

The purpose of the present preprint is to reconcile and consolidate these claims in a self-contained analytic framework whose every number is derived with shown arithmetic. Three independent analyses of the same source material produced quantitatively different checking-time estimates (4.8 ns, 45 ns, and 16.0 ns at $\Delta\omega = 2\pi\times1$ MHz) because they adopted different model conventions; Appendix A documents each divergence and the convention chosen here. We adopt the exact two-branch dephasing model: we isolate the minimal mechanism — a two-branch environment record with Gaussian photon wavepackets — and carry out three computations: (i) the exact recovered fidelity as a function of the environment overlap $s$; (ii) the distinguishability $D$ as a function of the dimensionless separation $\Delta\omega\,\sigma$; and (iii) the maximum permissible syndrome-checking interval $T_{\mathrm{check}}$ for a target distinguishability $D_{\max}$. Each result is a closed-form expression evaluated at concrete parameter values, so that the qualitative claims of Ref. [2] are anchored to reproducible arithmetic.

Our contribution is deliberately modest in scope but explicit in derivation. We do not claim new physics beyond Ref. [2]; rather, we provide an independent, arithmetic-transparent reconstruction of its core scalings, situate them in the broader QEC literature [7], [8], [9], [10], and connect them to platform-level constraints on monolithic superconducting processors [3] and to overhead considerations in fault-tolerant schemes [4]. The QNFO corpus analyses of low-overhead modular QEC [14] and of QEC implications for computing [12] motivate the practical question: does distinguishability change the overhead calculus of error-corrected architectures?

## 2. Background and Related Work

**The source paper.** Ref. [2] (with its query record [1]) studies monolithic QEC in the presence of distinguishability. Its abstract identifies the mechanism studied here: residual Zeeman, Stark, or anharmonic interactions shift the underlying states, making errors distinguishable and weakening the conditions for perfect recovery. It analyzes a four-level model with spontaneous-emission noise, finds that distinguishability raises the effective Kraus rank of the noise channel and lowers recovered fidelity, and identifies fast syndrome checking as the mitigation. Our Section 4 reconstructs the fidelity and checking-time scalings with explicit arithmetic.

**Foundational QEC.** Ref. [8] introduces the canonical machinery — encoding, syndrome extraction, error operators, and code construction — and shows that general noise on two-state systems decomposes into Pauli operators, a subset of which any code corrects. That decomposition implicitly assumes the error operators act within a fixed operator algebra; distinguishability violates precisely the orthogonality-of-error-spaces premise behind it. Ref. [9] frames QEC as storing information in a code subspace designed so that common errors move the state into orthogonal error spaces; our model quantifies what happens when the environment records distinguish those spaces. Ref. [10] extends QEC beyond qubits (qudits, bosonic codes, and subsystem structures) and emphasizes that decoherence noise models must be matched to code structure — relevant here because spontaneous emission into frequency-resolved modes is a bosonic noise process whose Kraus structure is platform-dependent. Ref. [7] surveys the path from classical to quantum error-correcting codes and stresses that quantum channels behave differently from classical ones; the distinguishability effect is a paradigmatic instance: classically, which-error information in the environment is harmless, while quantumly it destroys the coherence the code must protect.

**Continuous-time and alternative formulations.** Ref. [5] develops continuous-time QEC (CTQEC), treating both noise and correction as continuous processes via weak measurement and feedback, from the subsystem principle. CTQEC is the natural limit of the fast-checking regime our Section 4 quantifies: as $T_{\mathrm{check}} \to 0$, discrete syndrome extraction approaches continuous monitoring, and the distinguishability buildup we compute is suppressed at the same rate. Ref. [6] introduces entanglement-assisted QEC codes, in which pre-shared entanglement between encoder and decoder relaxes code-construction constraints; one open question (Section 6) is whether ancillary entanglement can absorb distinguishability-induced Kraus-rank inflation. Ref. [11] proposes QEC strategies in quaternionic Hilbert spaces, extending Pauli-operator analogues beyond complex Hilbert spaces; while formally distinct, it illustrates that the operator-algebraic assumptions underlying standard QEC — the same assumptions distinguishability undermines — are themselves objects of active generalization.

**Platform and overhead context.** Ref. [3] reports error-corrected memory and logic on a heavy-hex superconducting-qubit processor and highlights fabrication-induced component heterogeneity in monolithic devices. Heterogeneity and distinguishability are cousins: both are monolithic-fabrication artifacts that make error processes less uniform than the code assumes. Ref. [4] (NOBOL) analyzes low-overhead fault-tolerant computing, noting that logical operations incur linear time and resource overhead in monolithic architectures; if distinguishability additionally forces faster syndrome checking, the time-overhead budget tightens further. Finally, the QNFO corpus study of boundary-connected planar modules [14] documents how two-dimensional code layout forces vanishing encoding rate and hundreds-to-thousands of physical qubits per logical qubit, and the QNFO analysis of QEC implications for computing [12] frames these overheads architecturally. Our results add a temporal constraint — a maximum checking interval — to that spatial overhead accounting.

## 3. Methods

### 3.1 Notation

Let $\mathcal{H}_L$ be the logical (code) Hilbert space with basis $\{|0_L\rangle, |1_L\rangle\}$, $\mathcal{H}_E$ the environment, and $\rho_L$ a logical state. A quantum channel $\mathcal{E}$ has Kraus representation $\mathcal{E}(\rho) = \sum_k K_k \rho K_k^\dagger$; the minimal number of Kraus operators is the Kraus rank. The Knill–Laflamme conditions for exact correctability of an error set $\{E_k\}$ on a code projector $P$ read

$$P E_i^\dagger E_j P = c_{ij} P, \qquad c_{ij} \in \mathbb{C}.$$

The scalar $c_{ij} = \langle \alpha_i | \alpha_j \rangle_E$ is the Gram matrix of the environment states $|\alpha_k\rangle = E_k|\psi\rangle$ produced by the errors on any code state; exact correctability holds iff this Gram matrix factors with the $|\alpha_k\rangle$ spanning a space independent of the code state — equivalently, the environment cannot distinguish the errors.

### 3.2 Minimal distinguishability model

We consider a single error process (e.g., spontaneous emission at rate $\Gamma$) that can occur on either of the two logical basis components. The emitted photon carries a frequency $\omega_0$ if the error acted on the $|0_L\rangle$ component and $\omega_0 + \Delta\omega$ if it acted on the $|1_L\rangle$ component — the physical signature of a residual Zeeman or Stark shift between the two emitting transitions. The photon wavepacket envelope is Gaussian with duration parameter $\sigma$:

$$\psi_{\omega}(t) = (2\pi\sigma^2)^{-1/4} \exp\!\left(-\frac{t^2}{4\sigma^2}\right) e^{-i\omega t}.$$

The joint post-error state on $\mathcal{H}_L \otimes \mathcal{H}_E$ for an input $|\psi\rangle = a|0_L\rangle + b|1_L\rangle$ is

$$|\Psi_{\mathrm{out}}\rangle = a\,|0_L\rangle|\alpha\rangle + b\,|1_L\rangle|\beta\rangle,$$

where $|\alpha\rangle = |\psi_{\omega_0}\rangle$ and $|\beta\rangle = |\psi_{\omega_0+\Delta\omega}\rangle$ are the two environment branches. The environment overlap is

$$s \equiv \langle \alpha | \beta \rangle = \int dt\, \psi_{\omega_0}^*(t)\,\psi_{\omega_0+\Delta\omega}(t).$$

### 3.3 Recovery model

The recovery operation $\mathcal{R}$ acts only on $\mathcal{H}_L$ after the environment is traced out. It can restore the populations $|a|^2, |b|^2$ but multiplies the off-diagonal coherence by the factor $s$ (derived in Section 4.1). The recovered fidelity against the input is

$$F = \langle \psi | \mathcal{R}(\mathcal{E}(|\psi\rangle\langle\psi|)) | \psi \rangle.$$

### 3.4 Checking-time model

Between syndrome checks separated by $T_{\mathrm{check}}$, the photon wavepacket duration is bounded by the time available for emission, so we take $\sigma \simeq T_{\mathrm{check}}$ as the optimistic (shortest-packet) assignment. We require the distinguishability

$$D \equiv 1 - |s|^2$$

to remain below a tolerance $D_{\max}$, and solve for the maximum checking interval.

## 4. Analysis

All inputs are stated with their provenance; all arithmetic is shown step by step. Numbers not measured in any experiment are properties of the analytic model of Section 3, and Section 5 labels them accordingly.

### 4.1 Derivation of the recovered fidelity

**Step 1: environment-traced channel.** Tracing $\mathcal{H}_E$ out of $|\Psi_{\mathrm{out}}\rangle\langle\Psi_{\mathrm{out}}|$ gives

$$\rho_L' = |a|^2 |0_L\rangle\langle 0_L| + |b|^2 |1_L\rangle\langle 1_L| + a b^* s^* |0_L\rangle\langle 1_L| + a^* b\, s\, |1_L\rangle\langle 0_L|,$$

because $\operatorname{Tr}_E\big(|\alpha\rangle\langle\beta|\big) = \langle\beta|\alpha\rangle = s^*$ and $\operatorname{Tr}_E\big(|\alpha\rangle\langle\alpha|\big) = 1$. The populations are untouched; the coherence is multiplied by $s$. This is the channel's Kraus-rank statement: if $s = \pm 1$ the two branches are the same environment state and the emission subchannel has Kraus rank $1$ (a unitary up to phase); if $|s| < 1$ the branches are linearly independent and the emission subchannel has Kraus rank $2$. Distinguishability, i.e., $|s|<1$, is exactly the statement that the effective Kraus rank of the emission subchannel has been raised from $1$ to $2$. (If the no-jump branch is counted as a separate Kraus operator, the full channel over one checking interval has rank up to $3$; see Appendix A, divergence D2.)

**Step 2: optimal recovery.** A recovery on $\mathcal{H}_L$ alone can at best undo the deterministic part of the channel. Since the populations are already correct, the best any trace-preserving recovery achieves is to keep the coherence factor at $s$ (no operation on $\mathcal{H}_L$ can increase a coherence damped by the environment; formally, the channel is a dephasing-type map with coherence multiplier $s$, and dephasing multipliers are invariant under unitary recovery and can only decrease under measurement-and-reprepare recovery). Hence the optimal recovered state is

$$\rho_{\mathrm{rec}} = |a|^2 |0_L\rangle\langle 0_L| + |b|^2 |1_L\rangle\langle 1_L| + a b^* s^* |0_L\rangle\langle 1_L| + a^* b\, s\, |1_L\rangle\langle 0_L|.$$

**Step 3: fidelity for an equal superposition.** Take $a = b = 1/\sqrt{2}$ and $s$ real (the phase of $s$ is absorbable into a logical $Z$ rotation, so WLOG $\operatorname{Im} s = 0$). Then

$$F = \langle\psi|\rho_{\mathrm{rec}}|\psi\rangle = \frac{1}{4}\left(1 + 1 + s + s\right) = \frac{1}{2}(1 + s).$$

Explicitly: the diagonal terms contribute $\frac{1}{4}+\frac{1}{4} = \frac{1}{2}$; each off-diagonal term $|0_L\rangle\langle 1_L|$ and $|1_L\rangle\langle 0_L|$ contributes $\frac{1}{4}s$; total $\frac{1}{2} + \frac{s}{2}$.

**Step 4: bound in terms of distinguishability.** Define $D = 1 - |s|^2$. For real $s \in [0,1]$ we have $s \ge s^2$ (since $s - s^2 = s(1-s) \ge 0$), hence

$$F = \frac{1+s}{2} \ge \frac{1+s^2}{2} = \frac{1 + (1-D)}{2} = 1 - \frac{D}{2}.$$

So the fidelity penalty is at least half the distinguishability:

$$F \ge 1 - \frac{D}{2}, \qquad D = 1 - |s|^2.$$

### 4.2 Derivation of the distinguishability for Gaussian wavepackets

**Step 1: the overlap integral.** With $\psi_\omega(t) = (2\pi\sigma^2)^{-1/4} e^{-t^2/(4\sigma^2)} e^{-i\omega t}$,

$$s = \int_{-\infty}^{\infty} dt\, (2\pi\sigma^2)^{-1/2} e^{-t^2/(2\sigma^2)} e^{i\omega_0 t} e^{-i(\omega_0+\Delta\omega)t} = \int dt\, (2\pi\sigma^2)^{-1/2} e^{-t^2/(2\sigma^2)} e^{-i\Delta\omega\, t}.$$

This is the characteristic function of a Gaussian with variance $\sigma^2$:

$$s = e^{-\frac{1}{2}(\Delta\omega)^2 \sigma^2}.$$

**Step 2: the distinguishability.** Since $s$ is real and positive,

$$|s|^2 = e^{-(\Delta\omega\sigma)^2}, \qquad D = 1 - e^{-(\Delta\omega\sigma)^2}.$$

**Step 3: numerical evaluations.** Input: dimensionless separations $x \equiv \Delta\omega\,\sigma \in \{0.1, 0.5, 1.0, 2.0\}$ (model parameters, no external source).

- $x = 0.1$: $x^2 = 0.01$; $e^{-0.01} = 0.9900498$ (using $e^{-0.01} \approx 1 - 0.01 + 0.00005 - 0.000000167 = 0.9900498$); $D = 1 - 0.9900498 = 0.0099502$; $F \ge 1 - 0.0099502/2 = 0.9950249$.
- $x = 0.5$: $x^2 = 0.25$; $e^{-0.25} = 0.778801$; $D = 0.221199$; $F \ge 1 - 0.110600 = 0.889400$.
- $x = 1.0$: $x^2 = 1$; $e^{-1} = 0.367879$; $D = 0.632121$; $F \ge 1 - 0.316060 = 0.683940$.
- $x = 2.0$: $x^2 = 4$; $e^{-4} = 0.018316$; $D = 0.981684$; $F \ge 1 - 0.490842 = 0.509158$.

The exact fidelity $F = (1+s)/2$ with $s = e^{-x^2/2}$: for $x=0.1$, $e^{-0.005} = 0.9950125$, $F = (1+0.9950125)/2 = 0.9975062$; for $x=0.5$, $e^{-0.125} = 0.882497$, $F = 0.941248$; for $x=1$, $e^{-0.5} = 0.606531$, $F = 0.803265$; for $x=2$, $e^{-2} = 0.135335$, $F = 0.567668$. The bound is loose by $s - s^2 > 0$, as expected for $s\in(0,1)$.

### 4.3 Derivation of the maximum checking interval

*Input 1:* frequency separation $\Delta\omega = 2\pi \times 1\ \mathrm{MHz} = 6.283185 \times 10^{6}\ \mathrm{rad/s}$ (representative residual Zeeman‑split transition separation; model assumption, labeled as such).

*Input 2:* tolerance $D_{\max} = 10^{-2}$ (chosen so that the fidelity bound of Section 4.1 guarantees $F \ge 1 - 5\times10^{-3}$).

*Step 1:* solve the constraint. Require $1 - e^{-(\Delta\omega\,T_{\mathrm{check}})^2} \le D_{\max}$, i.e. $e^{-(\Delta\omega T_{\mathrm{check}})^2} \ge 1 - D_{\max}$, i.e.

$$T_{\mathrm{check}} \le \frac{\sqrt{\ln\!\left(\frac{1}{1-D_{\max}}\right)}}{\Delta\omega}.$$

*Step 2:* arithmetic. $\ln\!\left(\frac{1}{1-0.01}\right) = \ln\!\left(\frac{1}{0.99}\right) = \ln(1.010101) = 0.010050$ (since $\ln(1+u) \approx u - u^2/2$ with $u = 0.010101$: $0.010101 - 0.000051 = 0.010050$). Then $\sqrt{0.010050} = 0.100250$. Hence

$$T_{\mathrm{check}} \le \frac{0.100250}{6.283185 \times 10^{6}} = 1.59577 \times 10^{-8}\ \mathrm{s} \approx 16.0\ \mathrm{ns}.$$

*Step 3:* dependence on separation. The scaling $T_{\mathrm{check}} \propto 1/\Delta\omega$ is the central operational claim. For the same $D_{\max} = 10^{-2}$:

- $\Delta\omega = 2\pi\times 0.1\ \mathrm{MHz} = 6.283185\times10^{5}$ rad/s: $T_{\mathrm{check}} \le 1.59577\times10^{-7}$ s $\approx 160$ ns.
- $\Delta\omega = 2\pi\times 10\ \mathrm{MHz} = 6.283185\times10^{7}$ rad/s: $T_{\mathrm{check}} \le 1.59577\times10^{-9}$ s $\approx 1.6$ ns.

A tenfold increase in frequency separation tightens the checking budget tenfold — confirming that the operational checking time shortens as the frequency separation between emitted photons increases.

*Step 4:* alternative tolerance. For $D_{\max} = 10^{-4}$ (fidelity bound $F \ge 1 - 5\times10^{-5}$) at $\Delta\omega = 2\pi\times1\ \mathrm{MHz}$: $\ln\!\left(\frac{1}{1-10^{-4}}\right) = \ln(1.000100) = 0.000100$; $\sqrt{0.000100} = 0.01$. Hence $T_{\mathrm{check}} \le \frac{0.01}{6.283185\times10^{6}} = 1.59155\times10^{-9}\ \mathrm{s} \approx 1.6\ \mathrm{ns}$.

## 5. Results

The analytic model yields the following concrete numbers:

- Distinguishability $D$ and fidelity lower bound $F \ge 1 - D/2$ for dimensionless separations $x = \Delta\omega\sigma \in \{0.1, 0.5, 1.0, 2.0\}$:
  - $x=0.1$: $D = 9.9502\times10^{-3}$, $F \ge 0.99502$.
  - $x=0.5$: $D = 2.212\times10^{-1}$, $F \ge 0.8894$.
  - $x=1.0$: $D = 6.321\times10^{-1}$, $F \ge 0.6839$.
  - $x=2.0$: $D = 9.817\times10^{-1}$, $F \ge 0.5092$.
- Maximum permissible syndrome‑checking interval for a baseline tolerance $D_{\max}=10^{-2}$:
  - $\Delta\omega = 2\pi\times1\ \mathrm{MHz}$: $T_{\mathrm{check}} \le 1.60\times10^{-8}\ \mathrm{s}$ (16.0 ns).
  - $\Delta\omega = 2\pi\times0.1\ \mathrm{MHz}$: $T_{\mathrm{check}} \le 1.60\times10^{-7}\ \mathrm{s}$ (160 ns).
  - $\Delta\omega = 2\pi\times10\ \mathrm{MHz}$: $T_{\mathrm{check}} \le 1.60\times10^{-9}\ \mathrm{s}$ (1.6 ns).
- For a tighter tolerance $D_{\max}=10^{-4}$ at $\Delta\omega = 2\pi\times1\ \mathrm{MHz}$ the bound tightens to $T_{\mathrm{check}} \le 1.59\times10^{-9}\ \mathrm{s}$ (1.6 ns).

All values are derived directly from the formulas in Section 4 with the arithmetic shown there.

## 6. Discussion

The present analysis rests on several simplifying assumptions. First, we identified the photon‑wavepacket duration $\sigma$ with the syndrome‑checking interval $T_{\mathrm{check}}$, which is optimistic: in a real device the emission may continue beyond the check, effectively increasing $\sigma$ and thus $D$. Second, the Gaussian wavepacket model neglects side‑band structure and possible chirp, which could either increase or decrease the overlap $s$. Third, we treated $s$ as real, absorbing any phase into a logical $Z$ rotation; in practice uncontrolled phases could further degrade fidelity.

Potential failure modes include: (i) under‑estimation of $\sigma$ leading to an actual $D$ larger than the bound; (ii) additional error channels (dephasing, leakage) that compound the distinguishability effect; (iii) hardware latency that prevents syndrome extraction within the computed $T_{\mathrm{check}}$. Any experimental observation of fidelity loss exceeding the $1-D/2$ bound would falsify the simple two‑branch model and indicate missing physics.

Open questions remain: how does entanglement‑assisted error correction mitigate distinguishability‑induced Kraus‑rank inflation? Can continuous‑time QEC schemes fully suppress the buildup of $D$ as $T_{\mathrm{check}}\to0$? And how do realistic pulse‑shaping techniques modify the effective $\sigma$?

## 7. Conclusion

We have reconstructed the core quantitative claims of Ref. [2] with explicit arithmetic, demonstrating that even modest frequency separations between error‑dependent photon emissions impose stringent timing constraints on syndrome extraction. The derived checking‑interval bounds (16 ns for a 1 MHz split at $D_{\max}=10^{-2}$) highlight a practical limitation for monolithic quantum processors and motivate hardware designs that either reduce $\Delta\omega$ or accelerate syndrome measurement. Future work should integrate full device‑level simulations and explore mitigation strategies such as entanglement assistance or continuous monitoring.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2609.26946&amp;start=0&amp;max_results=1
[2] Monolithic Quantum Error Correction in the Presence of Distinguishability. arXiv:2609.26946v1. https://arxiv.org/abs/2609.26946v1
[3] Error-Corrected Memory and Logic on a Heavy-Hex Superconducting-Qubit Processor. arXiv:2610.11658v1. https://arxiv.org/abs/2610.11658v1
[4] Need One Bell-pair Only (NOBOL) for Low-Overhead Fault-Tolerant Quantum Computing. arXiv:2609.01901v1. https://arxiv.org/abs/2609.01901v1
[5] Continuous-time quantum error correction. arXiv:1311.2485v2. https://arxiv.org/abs/1311.2485v2
[6] Entanglement-Assisted Quantum Error-Correcting Codes. arXiv:1610.04013v1. https://arxiv.org/abs/1610.04013v1
[7] An Introduction to Error-Correcting Codes: From Classical to Quantum. arXiv:quant-ph/0602157v1. https://arxiv.org/abs/quant-ph/0602157v1
[8] Quantum Computing and Error Correction. arXiv:quant-ph/0304016v2. https://arxiv.org/abs/quant-ph/0304016v2
[9] Quantum Error Correction. arXiv:1910.03672v1. https://arxiv.org/abs/1910.03672v1
[10] Quantum error correction beyond qubits. arXiv:0811.3734v1. https://arxiv.org/abs/0811.3734v1
[11] Quantum Error Correction in Quaternionic Hilbert Spaces. arXiv:2504.19833v1. https://arxiv.org/abs/2504.19833v1
[12] https://papers.qnfo.org/papers/prime-valuation-qec-implications/. QNFO: Implications for Computing and Quantum Error Correction.
[14] https://papers.qnfo.org/papers/low-overhead-quantum-error-correction-with-boundary-connected-planar-modules-a-r/. QNFO: Low-Overhead Quantum Error Correction with Boundary-Connected Planar Modules: A Reconciled Quantitative Assessment.

## Appendix A. Divergence report

The three independent analyses of the same source material produced checking-time estimates of 4.8 ns, 45 ns, and 16.0 ns at $\Delta\omega = 2\pi\times1$ MHz. The divergence is a convention disagreement, not an arithmetic disagreement: (D1) the 4.8 ns draft used a linear (small-$D$) approximation $D \approx (\Delta\omega\,T_{\mathrm{check}})^2$ together with a different tolerance convention, which under-counts the logarithm and yields a shorter interval; (D2) the 45 ns draft counted the no-jump branch as a separate Kraus operator and folded the resulting rank-$3$ channel into the tolerance budget, effectively loosening $D_{\max}$ and lengthening the interval; (D3) the present draft uses the exact constraint $1 - e^{-(\Delta\omega T_{\mathrm{check}})^2} \le D_{\max}$ with $D_{\max} = 10^{-2}$ and $\sigma \simeq T_{\mathrm{check}}$, giving $T_{\mathrm{check}} \le 1.59577\times10^{-8}$ s $\approx 16.0$ ns. We adopt convention D3 because it uses the exact closed-form distinguishability rather than an approximation and treats the emission subchannel (rank $2$) as the noise process being bounded; the rank-$3$ counting of D2 is retained only as a remark in Section 4.1.

## Appendix B. Claim attribution

The table below maps each quantitative claim of the reconciled paper to its originating draft(s) and agreement status. Drafts are labeled A, B, and C; the reconciled convention adopted in the main text is D3 of Appendix A.

| Claim | Statement | Source draft(s) | Agreement status |
|---|---|---|---|
| C1 | Recovered fidelity for an equal-superposition input is $F = \frac{1}{2}(1+\operatorname{Re}s)$, with $s$ the environment-state overlap. | A, B, C | CONVERGENT |
| C2 | Fidelity lower bound $F \ge 1 - D/2$ with $D = 1 - |s|^2$. | A, B, C | CONVERGENT |
| C3 | Gaussian-wavepacket overlap $s = e^{-\frac{1}{2}(\Delta\omega\sigma)^2}$ and distinguishability $D = 1 - e^{-(\Delta\omega\sigma)^2}$. | A, B, C | CONVERGENT |
| C4 | Numerical values of $D$ and $F$ at $x = \Delta\omega\sigma \in \{0.1, 0.5, 1.0, 2.0\}$ (e.g., $D = 9.9502\times10^{-3}$, $F \ge 0.99502$ at $x=0.1$). | A, B, C | CONVERGENT |
| C5 | Checking-time constraint $T_{\mathrm{check}} \le \sqrt{\ln(1/(1-D_{\max}))}/\Delta\omega$ with $D_{\max} = 10^{-2}$, giving $T_{\mathrm{check}} \le 1.59577\times10^{-8}$ s $\approx 16.0$ ns at $\Delta\omega = 2\pi\times1$ MHz. | C (adopted); A and B used different conventions | DIVERGENT (resolved as D3, Appendix A) |
| C6 | Checking intervals at $\Delta\omega = 2\pi\times0.1$ MHz ($\approx 160$ ns) and $2\pi\times10$ MHz ($\approx 1.6$ ns) for $D_{\max} = 10^{-2}$; tenfold separation tightens the budget tenfold. | A, B, C | CONVERGENT (scaling); DIVERGENT (absolute values, resolved as D3) |
| C7 | Alternative tolerance $D_{\max} = 10^{-4}$ at $\Delta\omega = 2\pi\times1$ MHz gives $T_{\mathrm{check}} \le 1.59155\times10^{-9}$ s $\approx 1.6$ ns. | B, C | CONVERGENT |
| C8 | Kraus-rank statement: $|s| < 1$ raises the emission-subchannel rank from $1$ to $2$; counting the no-jump branch gives rank up to $3$. | A, B | CONVERGENT (rank-2); SINGLE (rank-3 remark, draft B) |
| C9 | Identification $\sigma \simeq T_{\mathrm{check}}$ as the optimistic shortest-packet assignment. | C | SINGLE |
| C10 | Divergent checking-time estimates 4.8 ns (draft A), 45 ns (draft B), 16.0 ns (draft C) at $\Delta\omega = 2\pi\times1$ MHz arise from convention differences, not arithmetic errors. | A, B, C | DIVERGENT (documented in Appendix A) |