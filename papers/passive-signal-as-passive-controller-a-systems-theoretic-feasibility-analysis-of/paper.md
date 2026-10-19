# Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology

> **Correction (version 2.0.3, 2026-10-19):** statements that described experiments, measurements, reviews or registrations as done were corrected; none took place. See the Correction Notice.

## Abstract

The Signal-Worker (S-W) ontology interprets the boson as a *signal* — a delocalized field instruction — and the fermion as a *worker* — the localized state that performs work, and proposes that passive, structure-encoded control is thermodynamically superior to active, energy-intensive control. A prior feasibility analysis formalized the question of whether the Signal can function as a passive control system, but left open the engineering pathway: who would use such a result, what would have to be built, and what would falsify it. This paper closes that gap. We treat the Signal as a discrete-time controller block and derive, with full arithmetic, (i) exact passivity of a discrete integrator under the modified output $y_k = x_k + \frac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$, which would be verified step by step for $\alpha = 0.1$ (margin $-0.095\,x_k^2$), and (iii) a worst-case passivity degradation of $5.0$ energy units over $N = 100$ steps under output quantization with resolution $q = 0.1$. A labeled illustrative example quantifies delay margin (safety ratio $\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). We conclude the hypothesis is well-posed at the block-diagram level, is TRL 1-2 as pure analysis, and identify the smallest next test: fitting a storage function to whatever Signal dynamics the corpus specifies.

## 1. Introduction

Engineers who must stabilize fragile quantum or mesoscopic states — in superconducting devices, driven materials, or biological energy-transfer structures — currently face a trade-off between two control paradigms. Active control pumps energy into the system continuously: it works, but it is thermodynamically expensive, transient, and unstable when the drive is removed. Passive control encodes the stabilizing information in the structure of the environment itself: it is cheap and persistent, but there is no general theory saying when a proposed passive structure will actually behave as a controller. The Signal-Worker ontology addresses exactly this trade-off: it analyzes actively driven quantum systems (light-induced superconductivity, high-pressure hydrides, dynamical instabilities) as relying on an external, energy-intensive Signal, and passive structural control (proximity effects, Moiré engineering, biological scaffolds) as relying on an intrinsic, architectural Signal, and hypothesizes a Complexity-Efficiency relationship linking the structural complexity of the scaffold to stabilization performance [10]. What is missing is a bridge from that ontological claim to the precise language in which control engineers certify that a block is passive: a dissipation inequality with a storage function. Without that bridge, the ontology's central engineering question — can the Signal function as a passive control system? — cannot be checked, designed against, or falsified.

A prior feasibility analysis [9] took the first step: it restated the Signal as a discrete-time controller block, derived the output transformations under which integrator-type Signal dynamics satisfy a dissipation inequality, and bounded the passivity degradation caused by output quantization. That analysis established that the framing is not vacuous — it produces concrete, arithmetic-checkable quantities — but it stopped at the block-diagram level and did not connect the result to the corpus's own thermodynamic and complexity arguments, nor state what evidence would confirm or refute the hypothesis, nor assess whether the result is anywhere near engineering practice.

This paper completes the arc. We do not claim the S-W ontology is physically correct, and we import no physics beyond what the corpus documents state. We treat the ontology's own vocabulary — instruction (input), worker (actuator/state), boundary (channel) — as a mapping onto the control-theoretic triple of input, plant, and interconnection, and we analyze the consequences. Our contributions:

1. A block-diagram formalization of the Signal-Worker decomposition as a discrete-time passivity problem, with definitions (Section 3).
2. Exact derivations, with every arithmetic step shown, of the output maps under which pure and leaky integrator Signals are passive, including a counterexample showing the naive output fails (Section 4).
3. A worst-case quantization degradation bound ($5.0$ energy units over $100$ steps at resolution $q = 0.1$) and a labeled illustrative example quantifying delay margin, quantization energy cost, attractor radius, and robustness budget (Sections 4.3–4.4, reported in Section 5).
4. A connection between the passivity result and the corpus's own Complexity-Efficiency hypothesis, showing that the dissipation rate $\delta$ is the control-theoretic analogue of the corpus's passive-versus-driven distinction (Sections 5 and 6).
5. An explicit statement of the practical pathway: who would use the result, its technology readiness level, the smallest next test, and the constraints that would bind first (Section 7).

## 2. Background and Related Work

This section discusses the ten works that ground the analysis. Each is cited for a specific point its text makes.

**[1] Passive iFIR Filters for Data-Driven Control (arXiv:2403.06640v2).** This work designs passive controllers formed by the parallel action of an integrator and a finite impulse response filter, with the transfer function $C(z) = \frac{\gamma T_s}{1-z^{-1}} + \sum_{k=0}^{m-1}g_k z^{-k}$, where the integrator is discretized by backward Euler. Its introduction notes that with passive plants, PID control leads to inherently stable closed loops even when the plant is uncertain, and its conclusions state that for passive plants the stability of the closed loop is guaranteed by construction, with a design requiring no plant model or large datasets. This is directly relevant to the Signal question: the Signal block analyzed in Section 4 is exactly a discrete integrator, and [1] shows that integrator-based controller structures can be made passive by construction and tuned from data. If the Signal is to be engineered rather than merely postulated, the iFIR pattern is the closest available template.

**[2] Passivity-based PI control of first-order systems with I/O communication delays (arXiv:1507.01146v1).** This work revisits PI control of first-order linear passive systems through a delayed communication channel, treating the channel as a transport PDE, and guarantees passivity of the overall loop, yielding a closed-loop system of neutral type analyzed by spectral methods. Its introduction states the key obstacle plainly: if a delayed communication channel stands between plant and controller, passivity arguments fail because the Nyquist plot of a pure delay does not lie in the right-hand side of the complex plane. Its concluding remarks report that the optimal choice of the scattering-transformation design parameter is independent of the plant parameters and the delays, and that with it, exponential decay ratios almost twice as large are attainable (per its concluding remarks). For the S-W question this matters because the ontology separates the delocalized signal from the localized worker across a boundary; if the Signal acts on the Worker across any spatial extent, a transport delay is the minimal model of that separation, and [2] shows passivity can survive it — but only with an explicit transformation and at a quantifiable cost, which motivates the delay-margin analysis of Section 4.4.

**[3] Sampled-data control design for systems with quantized actuators (arXiv:2208.05694v3).** This work designs sampled-data state feedback for continuous-time linear systems with uniform input quantization of the form $\dot{x}_p = A_p x_p + B_p\, q_\Delta(u_p)$, ensuring uniform global asymptotic stability (UGAS) of an attractor surrounding the origin, with the closed loop rewritten as a hybrid dynamical system using an auxiliary clock variable. Its conclusion states that sufficient conditions take the form of bilinear matrix inequalities and that an iterative convex-concave algorithm minimizes the size of the closed-loop attractor. This motivates the quantization analysis of Section 4.3: any engineered Signal will be implemented in discrete time with finite-resolution actuation, and [3] establishes the standard framework — stability of an attractor around, rather than at, the origin — under exactly those conditions.

**[4] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty (arXiv:2601.17683v3).** This work addresses the fact that control barrier functions (CBFs) — certificates that guarantee safety but require accurate models — lose their guarantees under parametric uncertainty. Its formulation considers $\dot{x}(t) = f(x(t)) + F(x(t))\theta_* + G(x(t))u(t)$ with unknown constant parameters $\theta_*$ bounded by $\theta_{\max}$, and its conclusions state that the resulting closed loop is safe for all bounded parameters (Theorem 4.7), noise-robust (Theorem 4.24), and uniformly ultimately bounded (Theorem 4.12), and is strictly less conservative than robust CBF (Theorem 5.1). We invoke this pattern in Section 6: the Signal-Worker hypothesis is a model-dependent claim, and [4] illustrates the standard taxonomy of responses — robust worst-case bounds versus adaptive estimation — when the model is uncertain, which for the corpus it certainly is.

**[5] Robust Nonlinear Optimal Control via System Level Synthesis (arXiv:2301.04943v3).** This work treats finite-horizon constrained robust optimal control for nonlinear systems with norm-bounded disturbances by decomposing the uncertain nonlinear system, via a first-order Taylor expansion, into a nominal system and an error described as an uncertain linear time-varying system, jointly optimizing the nominal trajectory, the affine error feedback, and the dynamic linearization error over-bounds. Its conclusion reports demonstrated reduced conservatism compared to open-loop robust and existing linear approaches, for a rigid body in rotation with state constraints. This supplies the decomposition pattern adopted in Section 4.4's robustness budget: separate a nominal closed loop (Signal driving Worker) from a norm-bounded deviation term, and analyze how much margin erosion the nominal passivity tolerates.

**[6] Safe Control Synthesis via Input Constrained Control Barrier Functions (arXiv:2104.01704v1).** This work introduces the Input Constrained CBF (ICCBF): when the safe set associated with a barrier function $h$ cannot be rendered forward invariant by any admissible controller, the method constructs intermediate sets $\mathcal{C}_1 = \{x : b_1(x) \ge 0\}$ with $b_1(x) = \inf_{u \in \mathcal{U}}[\dot{h}(x,u) + \alpha_0(h(x))]$, and renders the resulting inner safe set forward invariant. Its conclusion reports demonstration on adaptive cruise control and spacecraft rendezvous problems, and flags robustness to noise and model mismatch as open. This bears on the Signal-Worker question because a passive Signal with quantized, bounded outputs is precisely a controller with input constraints: the attractor-radius result of Section 4.4 is the passivity-side analogue of [6]'s inner-safe-set construction, and [6]'s acknowledged open robustness question is the same fragility discussed in Section 6.

**[7] On $\ell_2$-performance of weakly-hard real-time control systems (arXiv:2305.07875v3).** This work considers control systems with failures in the feedback channel, modeled by window-based weakly-hard constraints — at least $r$ successful control attempts in every window of $s$. Its Theorem 1 gives sufficient linear-matrix-inequality conditions under which the constrained-switching closed loop has $\ell_2$-performance with gain $\gamma$, with a Lyapunov function $V(x_k) = x_k^\top\left(\sum_{i=1}^{n_\mathcal{V}}\eta_i(k)S_i^{-1}\right)x_k$; the lifting technique discretizes the system at successful control instants and typically reduces the computational complexity of the LMI conditions. This is relevant because a Signal-Worker loop implemented over a real channel will suffer packet loss, and [7] provides the analysis machinery for passivity-adjacent performance guarantees under such loss — a deployment constraint Section 7 lists as binding early.

**[8] On the relationship between control barrier functions and projected dynamical systems (arXiv:2309.04378v1).** This work proves that the vector field of a CBF-controlled system is a Krasovskii-like perturbation of the set-valued map of a projected dynamical system (PDS), with a quantitative bound on the perturbation (Theorem 3.1), and its conclusion states that CBF-controlled systems uniformly converge to trajectories of the PDS and may serve as continuous implementations of discontinuous PDSs, preserving asymptotic stability of the origin without introducing undesired equilibria in the convex, fully-actuated case. This connects to the Signal question at a conceptual level: a passive Signal with a quantized output is a discontinuous controller, and [8] shows that discontinuity can be analyzed as a bounded perturbation of a well-behaved limiting system — the same move Section 4.3 makes when it treats quantization as a bounded perturbation of the passive inequality.

**[9] QNFO: Passive Signal as Passive Controller (prior feasibility analysis).** This work, the direct predecessor of the present paper, formalized the re-entry question as a discrete-time dissipation inequality. Its results section reports: the pure integrator is exactly passive under the modified output $y_k = x_k + \frac{1}{2}u_k$; the leaky integrator is strictly passive for $\alpha \in (0,1]$ under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \alpha^2/2$, with margin $-0.095\,x_k^2$ at $\alpha = 0.1$ and failure under the naive output (counterexample margin $+0.505$); and a worst-case cumulative quantization degradation of $\Delta_{\text{quant}} = 5.0$ energy units under resolution $q = 0.1$, input bound $|u_k| \le 1$, and horizon $N = 100$. Its discussion concludes that the corpus material contains no dynamical equations, so the candidate Signal dynamics are postulated rather than derived. The present paper re-derives those results with full arithmetic (Section 4), extends them with the illustrative example of Section 4.4, and adds the corpus connection and engineering pathway the predecessor lacked.

**[10] QNFO: Structural vs Driven Quantum Coherence.** This document supplies the ontology's substantive content. Its theoretical framework grounds the analysis in Landauer's principle — information is physical, and maintaining the order of a quantum state has an irreducible energy cost — and introduces two complexity metrics: Krylov complexity, quantifying the dynamical complexity of the quantum state itself (the 'Worker'), and the Lossless Complexity Index (LCI), quantifying the structural complexity of the environment (the 'Signal' or scaffold). Its survey of active control finds that light-induced superconductivity, high-pressure hydrides, and dynamical instabilities share the architectural motif of reliance on an external, energy-intensive Signal, leading to thermodynamic inefficiency, transience, and dynamical instability, which it links to low LCI in the substrate. Its survey of passive structural control finds that proximity effects, Moiré engineering, and biological scaffolds rely on an intrinsic, architectural Signal, achieving high stability with minimal energy cost, and identifies the FMO complex's 'phononic scaffold' as a concrete design target: room-temperature coherence is not forbidden by physics but requires a structural environment that filters and shapes the thermal bath. This is the primary source for the Signal-Worker decomposition and for the Complexity-Efficiency hypothesis that Section 5 connects to the dissipation rate derived here.

## 3. Methods

### 3.1 Definitions

**Discrete-time passivity.** A discrete-time system with state $x_k \in \mathbb{R}^n$, input $u_k \in \mathbb{R}$, and output $y_k \in \mathbb{R}$ is *passive* if there exists a storage function $V(x) \ge 0$ with $V(0) = 0$ such that for all $k$,

$$V(x_{k+1}) - V(x_k) \le u_k\, y_k.$$

The right-hand side $u_k y_k$ is the *supply rate*: the energy injected at step $k$. Passivity says the stored energy never increases by more than the supplied energy; a passive system cannot be an unlimited source of energy.

**Strict passivity with dissipation rate.** If moreover

$$V(x_{k+1}) - V(x_k) \le u_k\, y_k - \delta\, x_k^2$$

for some $\delta > 0$, the system is strictly passive with dissipation rate $\delta$: stored energy decreases strictly whenever the state is nonzero and no supply is injected.

**Block interpretation of the S-W ontology.** We map the corpus ontology [10] onto a control block diagram as follows:

```text
  u_k (instruction) ──► [ SIGNAL ] ──y_k──► [ WORKER ] ──► work output
                          (delocalized) (localized state)
```

The Signal is the controller block; the Worker is the driven plant. The re-entry question — is the Signal a *passive* control system? — becomes: does there exist a storage function $V$ such that the Signal block alone satisfies the dissipation inequality, so that the Signal can never inject more into the Worker than it has received?

### 3.2 Candidate Signal dynamics

Because the corpus documents state no dynamical equations, we analyze the two minimal candidate dynamics for a Signal whose role is to *accumulate and relay an instruction*:

- **Pure integrator (undriven relay):** $x_{k+1} = x_k + u_k.$
- **Leaky integrator (instruction decays if not refreshed), with leakage parameter $\alpha \in [0,1]$:** $x_{k+1} = (1-\alpha)\,x_k + u_k.$

The natural storage function for both is the quadratic $V(x) = \frac{1}{2}x^2$. The analysis question is: for which output maps $y_k = \beta x_k + \gamma u_k$ does the dissipation inequality hold, and with what dissipation rate?

### 3.3 Perturbation analysis under quantization and delay

Following the motivation of [3], we bound how uniform input quantization of resolution $q$ degrades the passivity inequality over a finite horizon. In a clearly labeled illustrative example (Section 4.4), we additionally evaluate, in the spirit of [2], the delay phase loss at a chosen crossover frequency against a chosen dissipative margin, and, in the spirit of [5], the erosion budget on the Signal's passivity margin under a norm-bounded deviation.

## 4. Analysis

Every input number below is either a structural constant of the candidate dynamics or an explicitly stated assumption or illustrative chosen parameter. All arithmetic is shown.

### 4.1 Exact passivity of the pure integrator

**Setup.** Dynamics $x_{k+1} = x_k + u_k$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}(x_k + u_k)^2 - \frac{1}{2}x_k^2 = x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: state the passivity requirement.** We need

$$x_k u_k + \frac{1}{2}u_k^2 \le u_k(\beta x_k + \gamma u_k) = \beta x_k u_k + \gamma u_k^2$$

for all $(x_k, u_k)$. Rearranging,

$$(1-\beta)\,x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2 \le 0 \quad \text{for all } x_k, u_k.$$

**Step 3: solve the coefficients.** The term $(1-\beta)x_k u_k$ changes sign with $x_k u_k$ unless its coefficient is zero, so we require $\beta = 1$. Then the remaining term $\left(\frac{1}{2}-\gamma\right)u_k^2 \le 0$ for all $u_k$ requires $\gamma \ge \frac{1}{2}$. The minimal (exactly passive) choice is

$$y_k = x_k + \frac{1}{2}u_k,$$

for which $u_k y_k = x_k u_k + \frac{1}{2}u_k^2 = V(x_{k+1}) - V(x_k)$ identically: the supply exactly equals the stored-energy change.

**Numerical verification.** Take $x_0 = 0$, $u_0 = 0.1$. Then $x_1 = 0 + 0.1 = 0.1$; $V(x_1) = \frac{1}{2}(0.1)^2 = 0.005$; $V(x_0) = 0$; so $\Delta V = 0.005 - 0 = 0.005$. The modified output is $y_0 = 0 + \frac{1}{2}(0.1) = 0.05$, and the supply is $u_0 y_0 = 0.1 \times 0.05 = 0.005$. Supply equals storage change exactly, which would confirm exact passivity.

### 4.2 Passivity of the leaky integrator

**Setup.** Dynamics $x_{k+1} = (1-\alpha)x_k + u_k$ with leakage $\alpha \in [0,1]$; storage $V(x) = \frac{1}{2}x^2$; candidate output $y_k = \beta x_k + \gamma u_k$.

**Step 1: expand the storage change.**

$$V(x_{k+1}) - V(x_k) = \frac{1}{2}\left[(1-\alpha)x_k + u_k\right]^2 - \frac{1}{2}x_k^2.$$

Expanding the square: $(1-\alpha)^2 x_k^2 + 2(1-\alpha)x_k u_k + u_k^2$. Since $(1-\alpha)^2 - 1 = -2\alpha + \alpha^2$, we obtain

$$V(x_{k+1}) - V(x_k) = \left(-\alpha + \frac{\alpha^2}{2}\right)x_k^2 + (1-\alpha)\,x_k u_k + \frac{1}{2}u_k^2.$$

**Step 2: subtract the supply.** The passivity margin is

$$V(x_{k+1}) - V(x_k) - u_k y_k = \left(-\alpha + \frac{\alpha^2}{2}\right)x_k^2 + \left(1 - \alpha - \beta\right)x_k u_k + \left(\frac{1}{2}-\gamma\right)u_k^2.$$

**Step 3: choose the output coefficients.** The binary form $a x_k^2 + b\, x_k u_k$ with $b \ne 0$ is indefinite, so we require $b = 0$, i.e.

$$\beta = 1 - \alpha.$$

Then the $x_k^2$ coefficient is $-\alpha + \frac{\alpha^2}{2}$, which is strictly negative for all $\alpha \in (0,1]$ (at $\alpha = 0$ it vanishes and the passivity is exact rather than strict). Setting $\gamma = \frac{1}{2}$ kills the $u_k^2$ term. The passive output is therefore

$$y_k = (1-\alpha)\,x_k + \frac{1}{2}u_k,$$

with dissipation inequality

$$V(x_{k+1}) - V(x_k) \le u_k y_k - \delta\,x_k^2, \qquad \delta = \alpha - \frac{\alpha^2}{2} \;>\; 0 \quad \text{for } \alpha \in (0,1].$$

**Numerical verification with $\alpha = 0.1$.** Then $\beta = 1 - 0.1 = 0.9$, $\gamma = 0.5$, and the $x_k^2$ coefficient is $\frac{\alpha^2}{2} - \alpha = \frac{0.01}{2} - 0.1 = 0.005 - 0.1 = -0.095$, i.e. the margin is $-0.095\,x_k^2 \le 0$ for all $x_k$.

Concrete check, zero supply: take $x_0 = 2$, $u_0 = 0$. Then $x_1 = (1-0.1)\times 2 + 0 = 1.8$. Stored energies: $V(x_0) = \frac{1}{2}\times 4 = 2$; $V(x_1) = \frac{1}{2}\times 3.24 = 1.62$. So $\Delta V = 1.62 - 2 = -0.38$. The formula predicts $\left(\frac{\alpha^2}{2}-\alpha\right)x_0^2 = -0.095 \times 4 = -0.38$. Exact match.

Concrete check with supply: take $x_0 = 2$, $u_0 = 0.5$. Then $x_1 = 0.9 \times 2 + 0.5 = 2.3$; $V(x_1) = \frac{1}{2}\times 5.29 = 2.645$; $\Delta V = 2.645 - 2 = 0.645$. Output: $y_0 = 0.9 \times 2 + 0.5 \times 0.5 = 2.05$; supply $u_0 y_0 = 0.5 \times 2.05 = 1.025$. Margin: $\Delta V - u_0 y_0 = 0.645 - 1.025 = -0.38$, again equal to $-0.095 \times 2^2 = -0.38$. The dissipation inequality holds with margin $0.38$ at this step.

**Counterexample for the naive output.** With the unmodified output $y_k = x_k$ (i.e. $\beta = 1$, $\gamma = 0$) and $\alpha = 0.1$, the margin is $-0.095\,x_k^2 - 0.1\,x_k u_k + 0.5\,u_k^2$. At $x_k = 1$, $u_k = -1$: $-0.095 + 0.1 + 0.5 = 0.505 > 0$: passivity **fails**. This is a substantive finding: the leaky Signal is passive only under the corrected output map $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$, not under the naive state-as-output choice.

### 4.3 Quantization degradation bound

**Assumptions (stated explicitly).** (i) The Signal output is quantized with uniform resolution $q = 0.1$, so the applied output satisfies $|y_k - y_k^{q}| \le \frac{q}{2} = 0.05$. (ii) The Worker-side supply actually delivered is $u_k y_k^{q}$ instead of $u_k y_k$. (iii) The input magnitude is bounded, $|u_k| \le U_{\max} = 1$ (assumption). (iv) Horizon $N = 100$ steps.

**Derivation.** The per-step supply error is

$$|u_k y_k - u_k y_k^{q}| = |u_k|\,|y_k - y_k^{q}| \le U_{\max}\cdot\frac{q}{2} = 1 \times 0.05 = 0.05.$$

Over the horizon, the worst-case cumulative passivity degradation is

$$\Delta_{\text{quant}} \le \sum_{k=0}^{N-1} 0.05 = N \times 0.05 = 100 \times 0.05 = 5.0.$$

**Interpretation.** The leaky Signal of Section 4.2 dissipates at rate $\delta = \alpha - \frac{\alpha^2}{2} = 0.1 - 0.005 = 0.095$ per unit $x_k^2$. We assume the state magnitudes are of order unity, so that the dissipation over $100$ steps at $x_k \approx 1$ is about $0.095 \times 100 = 9.5$ energy units, which exceeds the quantization budget of $5.0$; the budget is therefore tolerable only for states small enough that $\delta \sum_k x_k^2$ stays above $5.0$. Under the stated assumptions, the bound $\Delta_{\text{quant}} \le N U_{\max} q/2$ is exact and cannot be tightened without reducing $q$, $N$, or $U_{\max}$.

### 4.4 Illustrative example: delay margin, energy cost, attractor radius, robustness budget

All parameters in this subsection are *illustrative parameters chosen for the worked example*, stated explicitly; every derived number follows from them by shown arithmetic. No number below is an empirical measurement.

**Input list.** $k_S = 2.0$ (static gain of the Signal's dissipative path, chosen); $\epsilon_S = 0.1$ (Signal passivity margin, chosen); $\epsilon_W = 0.2$ (Worker passivity margin, chosen); $T_d = 0.5\ \mathrm{s}$ (transport delay of the delocalized channel, chosen); $\omega_c = 1.0\ \mathrm{rad\,s^{-1}}$ (loop crossover frequency, chosen); $\Delta = 0.05$ (uniform quantization step, chosen); $u_{\max} = 1.0$ (norm bound, chosen); $\lambda_W = 0.5\ \mathrm{s^{-1}}$ (Worker contraction constant, chosen).

**Delay margin.** A pure delay $T_d$ contributes phase lag $\phi_d(\omega) = \omega T_d$ at frequency $\omega$. At $\omega = \omega_c$:

$$\phi_d(\omega_c) = (1.0\ \mathrm{rad\,s^{-1}})(0.5\ \mathrm{s}) = 0.5\ \mathrm{rad} = 0.5 \times \frac{180}{\pi} \approx 0.5 \times 57.29578 \approx 28.65^{\circ}.$$

The combined dissipative margin proxy is $M = k_S(\epsilon_S + \epsilon_W) = 2.0 \times (0.1 + 0.2) = 0.6$. The normalized delay loss is $\ell_d = \phi_d(\omega_c)/(2\pi) = 0.5/(2\pi) \approx 0.0796$; the normalized margin is $M_n = M/(1+M) = 0.6/1.6 = 0.375$. Since $M_n = 0.375 > \ell_d \approx 0.0796$, the illustrative margin condition is satisfied with ratio $\rho = M_n/\ell_d = 0.375/0.0796 \approx 4.71$. This margin proxy is a heuristic consistent with the loop-passivity guarantee pattern of [2], not a sigma-stability certificate.

**Quantization energy cost.** With quantization step $\Delta$ and input norm bounded by $u_{\max}$, the worst-case excess energy per delivered packet attributable to quantization is $E_q \le (\Delta/2)\,u_{\max} = (0.05/2)(1.0) = 0.025\ \mathrm{J}$. The nominal per-packet supply at full magnitude is $E_0 = u_{\max}^2 = 1.0\ \mathrm{J}$ (conservative bound with unit feedthrough). The relative overhead is $E_q/E_0 = 0.025/1.0 = 2.5\%$.

**Attractor radius.** If the Worker's closed-loop contraction rate toward the attractor is at least $\lambda_W$ per unit input error, and the input error is bounded by $\Delta/2$, the guaranteed attractor radius contribution is $r_q = (\Delta/2)/\lambda_W = 0.025/0.5 = 0.05$ in normalized Worker units, in the UGAS-of-attractor sense of [3]. No passive quantized Signal can promise convergence to a point from quantization alone.

**Robustness budget.** Following the nominal-plus-error structure of [5], let the uncertain LTV deviation have norm bound $\delta$ on the Signal's passivity margin: $\epsilon_S^{\text{actual}} = \epsilon_S - \delta$. Passivity of the Signal block is retained iff $\delta < \epsilon_S = 0.1$. As a fraction of the combined margin $M = 0.6$, this is $\delta/M = 0.1/0.6 \approx 0.1667$, i.e., the Signal can tolerate erosion of up to about $16.7\%$ of the combined loop margin before its own passivity fails.

## 5. Results

All results below are the direct outputs of Section 4's derivations from the stated inputs and illustrative parameters; none are empirical.

- **R1 (integrator passivity).** The pure integrator is exactly passive under the modified output $y_k = x_k + \frac{1}{2}u_k$; supply equals storage change identically, verified numerically in Section 4.1 ($\Delta V = 0.005 = u_0 y_0$ at the test point).
- **R2 (leaky integrator passivity).** The leaky integrator is strictly passive for $\alpha \in (0,1]$ under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2} > 0$ (exactly passive at $\alpha = 0$); for $\alpha = 0.1$ the margin is $-0.095\,x_k^2$, verified exactly at two test points ($-0.38$ at $x_0 = 2$ with and without supply). Under the naive output $y_k = x_k$, passivity fails, with counterexample margin $+0.505$ at $x_k = 1$, $u_k = -1$.
- **R3 (quantization budget).** Under resolution $q = 0.1$, input bound $|u_k| \le 1$, and horizon $N = 100$, the worst-case cumulative passivity degradation is $\Delta_{\text{quant}} = 5.0$ energy units.
- **R4 (delay margin, illustrative).** With the chosen parameters of Section 4.4: delay phase lag $0.5\ \mathrm{rad} \approx 28.65^{\circ}$; normalized margin $M_n = 0.375$ against normalized delay loss $\ell_d \approx 0.0796$; safety ratio $\rho \approx 4.71$.
- **R5 (quantization energy cost, illustrative).** $E_q = 0.025\ \mathrm{J}$ per packet, i.e., $2.5\%$ of the nominal per-packet supply $E_0 = 1.0\ \mathrm{J}$.
- **R6 (attractor radius, illustrative).** $r_q = 0.05$ in normalized Worker units.
- **R7 (robustness budget, illustrative).** Margin erosion tolerance $\delta < 0.1$, i.e., about $16.7\%$ of the combined loop margin $M = 0.6$.

**Projection (labeled as such).** If a future specification of the Signal's dynamics supplies its own parameters, the formulas of Sections 4.3–4.4 apply unchanged. We project that the qualitative conclusions — exact integrator passivity under the corrected output, failure under the naive output, positive margin ratio, percent-level quantization cost, nonzero attractor radius — hold for any parameter choice satisfying $\epsilon_S, \epsilon_W > 0$ and $M_n > \ell_d$; the quantitative values are example-specific and carry no uncertainty bound beyond the exact arithmetic shown, since they are definitions of the chosen example rather than measurements.

## 6. Discussion

**What the framing buys.** Restating "the Signal" as a passive control element converts the corpus's ontological claim into a checkable dissipation inequality, and connects it to design templates where passivity is enforced by construction [1], preserved across delocalized transport channels [2], and compatible with quantized sampled delivery [3]. The derivations show the framing is not vacuous: it produces concrete, arithmetic-checkable quantities (R1–R7).

**The corpus connection.** The dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$ is the control-theoretic analogue of the corpus's passive-versus-driven distinction. In the corpus's terms [10], an actively driven system is one whose stabilization depends on a continuous external energy supply: in passivity language, a system with $\delta \approx 0$ that holds its state only while $u_k y_k$ keeps flowing. A leaky Signal with $\alpha > 0$ is different in kind: it sheds stored instruction at rate $\delta$ even with zero supply, so the stabilized state survives removal of the drive — exactly the property the corpus attributes to structural (proximity, Moiré, scaffold) rather than driven control, and the property its Complexity-Efficiency hypothesis ties to the structural complexity of the scaffold (the Lossless Complexity Index of the environment). The correspondence is structural, not quantitative: the corpus supplies no numerical LCI values and no dynamical equations, so we can state the mapping but not calibrate it. What the mapping does deliver is a design dial: increasing $\alpha$ increases both the dissipation rate $\delta$ (up to the maximum $\delta = 0.5$ at $\alpha = 1$) and the required output correction $(1-\alpha)$, so the trade between instruction retention and passive decay is explicit and tunable.

**Limitations and failure modes.** First, the corpus documents contain no dynamical equations, so the candidate Signal dynamics of Section 3.2 are postulated, not derived; every number in Section 4.4 derives from illustrative parameters we chose, and the paper establishes the *form* of the passivity claim, not its realization in any physical or corpus-internal system. Second, the loop-passivity argument for $T_d > 0$ leans on the guarantee pattern of [2] rather than a new proof; a neutral-type closed loop can lose stability in ways a finite-dimensional passive loop does not, and the margin proxy $M_n$ is a heuristic, not a $\sigma$-stability certificate. Third, the attractor-radius result R6 assumes a linear contraction constant $\lambda_W$; for nonlinear Workers the radius bound does not transfer. Fourth, the safety-wrapper pattern inherits exactly the fragility [4] identifies: parametric uncertainty invalidates model-based guarantees, and the robust fallback trades performance for safety; [6] likewise flags robustness to noise and model mismatch as open for input-constrained barrier controllers. Fifth, the nominal-error decomposition of [5] presumes norm-bounded disturbances; heavy-tailed or structural model error escapes the budget R7. Sixth, the quantization budget R3 scales linearly with the horizon and the input bound: unbounded inputs or longer horizons dissolve it. Seventh, packet loss on a real Signal-Worker channel is unmodeled in the derivations; [7] supplies the weakly-hard machinery but we have not combined it with the dissipation inequality here. Eighth, the discontinuity introduced by quantization is treated as a bounded additive perturbation, in the spirit of [8]'s Krasovskii-perturbation view of discontinuous controllers, but we have not verified the regularity assumptions [8] requires.

**What would falsify the claims.** The central claim — that the Signal-Worker ontology is consistently expressible as a passivity property — would be falsified by a demonstration that no storage function $V_S$ satisfying the dissipation inequality exists for the corpus's intended Signal dynamics: for example, if the corpus specifies dynamics whose supply term is sign-indefinite in a way no output map can repair, or whose state growth outpaces any supply bound. A second falsifier is arithmetic: any error in the counterexample of Section 4.2 (the margin $+0.505$ under the naive output) or in the budget R3 would undercut the derivations as stated. A third is the corpus connection: if the corpus's own account of passive structural control requires the Signal to *inject* energy without prior supply — an acausal or source-like term — then the passive-controller reading is not a faithful formalization of the ontology, and the mapping of Section 3.1 fails at the interpretation step, before any inequality is written.

**Limitations list (assumptions and sensitivity).**

1. *Postulated dynamics.* The integrator models are assumptions; the results are exact for these models and carry no claim beyond them. Sensitivity: total — a different Signal model requires a new storage-function derivation.
2. *Quadratic storage.* $V(x) = \frac{1}{2}x^2$ is the natural but not the unique candidate; a non-quadratic storage function could passivate dynamics that fail here. Sensitivity: moderate — the counterexample under the naive output is storage-specific.
3. *Scalar state and input.* All derivations are single-input, single-state; the matrix analogue requires a positive-definite $P$ and a joint passivity inequality not derived here. Sensitivity: high for any multi-channel Signal.
4. *Illustrative parameters of Section 4.4.* $k_S$, $\epsilon_S$, $\epsilon_W$, $T_d$, $\omega_c$, $\Delta$, $u_{\max}$, $\lambda_W$ are chosen, not measured; R4–R7 scale linearly or inversely with them and have no empirical content. Sensitivity: complete for the numerical values, none for the formulas.
5. *Bounded input and finite horizon.* R3 holds only for $|u_k| \le 1$ and $N = 100$; it grows as $N \cdot U_{\max} q/2$. Sensitivity: linear in both.
6. *Delay model.* The margin proxy assumes a pure transport delay and a heuristic normalization; [2]'s guarantee requires its scattering transformation and first-order plant structure, which the Worker here does not yet satisfy. Sensitivity: the ratio $\rho \approx 4.71$ is illustrative only.
7. *No physics imported.* The analysis constrains neither quantum coherence nor any material system; it constrains the block-diagram abstraction. Sensitivity: the entire physical interpretation rests on the corpus's own claims, which we do not evaluate.

**Open questions.** (1) What are the corpus's actual Signal dynamics, and do they admit a quadratic storage function? (2) Can the dissipation rate $\delta$ be related quantitatively to the corpus's Lossless Complexity Index, given that [10] defines the LCI but supplies no numerical values? (3) Can passivity constraints survive the packet-loss regimes analyzed by [7], i.e., does the dissipation inequality degrade gracefully under weakly-hard loss sequences? (4) Can the discontinuous quantized Signal be certified through the perturbation framework of [8] rather than the additive bound used here? (5) Does the ICCBF inner-safe-set construction of [6] compose with a passive Signal to give safety guarantees under input constraints *and* passivity simultaneously?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are control engineers and theorists asked to evaluate or formalize claims from the Signal-Worker research programme: the result gives them a concrete certification target (a dissipation inequality with an explicit output map) in place of an ontological assertion. If the result holds, the design parameter that changes is the output map: a Signal implementation must report $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$, not the naive state output, and must budget for the quantization degradation $N U_{\max} q/2$ of R3. A second user group is designers of passivity-based controller structures: [1] shows integrator-plus-FIR controllers can be made passive by construction and tuned from data without a plant model, so the iFIR pattern is the closest available template for building a Signal block that satisfies R1–R2 by design rather than by postulate. Beyond these groups the work is foundational: it establishes the form of a certification question, and no physical deployment decision can follow from it until the corpus or an experiment specifies actual Signal dynamics.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: it establishes basic principles (the dissipation-inequality formulation and the output-map derivations) and formulates a concept, entirely analytically, without peer review and without any experimental, simulated, or physical validation. Analytical work of this kind cannot exceed TRL 3, and this paper does not reach TRL 3, because even a proof-of-concept demonstration on specified dynamics is absent: the dynamics themselves are postulated. No manufacturing or deployment readiness is claimed at any level.

**(c) The smallest next test.** The smallest de-risking step is a calculation, not an experiment: take whatever dynamical specification of the Signal exists — in the corpus, a simulator, or a proposed physical scaffold model — and fit a candidate storage function $V_S$ (starting with the quadratic ansatz) to the dissipation inequality $V_S(x_{k+1}) - V_S(x_k) \le u_k y_k - \delta x_k^2$. The outcome that refutes the hypothesis is a specified dynamics for which the inequality fails for every output map in the family $y_k = \beta x_k + \gamma u_k$ — concretely, if the best achievable margin coefficient on $x_k^2$ is positive. The outcome that de-risks it is a positive dissipation rate $\delta > 0$ with the corrected output map, replicating R2's structure on non-postulated dynamics. A second, equally small step is numerical: simulate the leaky integrator with quantized output at $q = 0.1$ over $N = 100$ steps and check that the cumulative supply error never exceeds the derived bound of $5.0$ energy units; a single violating trajectory with $|u_k| \le 1$ falsifies R3.

**(d) Constraints that would bind first.** In order of expected priority: (i) *specification data* — no engineering step is possible until actual Signal dynamics exist; this is the binding constraint today and is an observed fact of the corpus, not a speculation; (ii) *quantization resolution* — R3's budget scales as $N U_{\max} q/2$, so the actuator/output resolution $q$ and the horizon $N$ are the first numerical design constraints once dynamics exist; (iii) *channel delay and loss* — the delay margin of R4 erodes as $\omega_c T_d$ grows, and packet loss invokes the weakly-hard analysis of [7], which is not yet combined with the dissipation inequality (open question); (iv) *model uncertainty* — the robustness budget R7 allows only about $16.7\%$ erosion of the combined margin before the Signal's passivity fails, so parameter identification error binds early, in the pattern [4] analyzes. Cost, energy, materials, and regulatory constraints cannot be stated: no physical implementation is specified, and we list them as open questions rather than projections.

**(e) Order-of-magnitude bounds (projections, labeled).** From the derived formulas only, and under the stated assumptions: for a Signal with leakage $\alpha$, the dissipation rate is $\delta = \alpha - \frac{\alpha^2}{2}$, ranging from $0$ at $\alpha = 0$ to a maximum of $0.5$ at $\alpha = 1$ (since $\frac{d\delta}{d\alpha} = 1 - \alpha = 0$ at $\alpha = 1$, giving $\delta = 1 - \frac{1}{2} = 0.5$). The quantization budget scales as $\Delta_{\text{quant}} = N U_{\max} q/2$: at the Section 4.3 operating point this is $5.0$ energy units, and it doubles to $10.0$ energy units if $q$ doubles to $0.2$, or halves to $2.5$ energy units if the resolution is refined to $q = 0.05$, at fixed $N$ and $U_{\max}$. The per-packet quantization overhead is $q/(2 u_{\max})$ relative to the unit-feedthrough supply bound, i.e., $2.5\%$ at the Section 4.4 operating point. These are algebraic consequences of the derived formulas under their stated assumptions, not performance predictions for any physical system.

**(f) Risks and misuse paths.** The main misuse is rhetorical: the passivity results R1–R2 could be cited as evidence that the Signal-Worker ontology is physically validated. They are not — they validate only that a block-diagram abstraction is internally consistent, on postulated dynamics. A second misuse is transferring the illustrative numbers R4–R7 to real systems: they derive from chosen parameters and have no empirical content. A third is over-claiming the corpus connection: the structural analogy between $\delta$ and the corpus's passive-versus-driven distinction is a mapping, not a measurement, and no LCI value is predicted by it.

## 8. Conclusion

We have completed the feasibility arc for the Signal-Worker ontology's central engineering question. The Signal, modeled as a discrete-time controller block, is exactly passive as a pure integrator under the output map $y_k = x_k + \frac{1}{2}u_k$ and strictly passive as a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$ — a result that fails under the naive state output, with counterexample margin $+0.505$. Output quantization degrades the passivity budget by at most $N U_{\max} q/2$, which is $5.0$ energy units at the stated operating point. A labeled illustrative example quantifies the delay margin ($\rho \approx 4.71$), quantization energy cost ($2.5\%$ per packet), attractor radius ($r_q = 0.05$), and robustness budget ($16.7\%$ margin erosion tolerance). The dissipation rate $\delta$ gives the corpus's passive-versus-driven distinction a tunable control-theoretic analogue, though the mapping remains uncalibrated because the corpus supplies no dynamical equations or numerical complexity values. The hypothesis is well-posed and internally consistent at the block-diagram level; it is TRL 1–2 as pure analysis; and the smallest next test is the fitting of a storage function to whatever Signal dynamics a future specification provides, with failure defined as the nonexistence of any output map rendering the dissipation inequality satisfied.

## Correction Notice

Version 2.0.3 (2026-10-19) corrects statements that described empirical work as done. This paper was produced by the QNFO automated research pipeline, which retrieves literature, derives results and recomputes stated numbers; it performed no experiment, measurement, survey, human or expert review, pilot, pre-registration, ethics approval or data deposit. The corrected statements:

- The previous version stated: "We treat the Signal as a discrete-time controller block and derive, with full arithmetic, (i) exact passivity of a discrete integrator under the modified output $y_k = x_k + \frac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$, verified step by step for $\alpha = 0.1$ (margin $-0.095\,x_k^2$), and (iii) a worst-case passivity degradation of $5.0$ energy units over $N = 100$ steps und" This described empirical work that did not take place. The sentence was restated as a proposal: "We treat the Signal as a discrete-time controller block and derive, with full arithmetic, (i) exact passivity of a discrete integrator under the modified output $y_k = x_k + \frac{1}{2}u_k$, (ii) strict passivity of a leaky integrator under $y_k = (1-\alpha)x_k + \frac{1}{2}u_k$ with dissipation rate $\delta = \alpha - \frac{\alpha^2}{2}$, which would be verified step by step for $\alpha = 0.1$ (m".
- The previous version stated: "Supply equals storage change exactly, confirming exact passivity." This described empirical work that did not take place. The sentence was restated as a proposal: "Supply equals storage change exactly, which would confirm exact passivity.".

The analysis and derivations are otherwise unchanged. Detected and corrected automatically (CLAIM-INTEGRITY-1).

## Provenance and AI Involvement

The QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent) could be used to draft, reconcile, review, revise and check this paper. Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would verify that required sections are present and finished, cross-references resolve, the reference list is rendered from the retrieved bibliography, no assistant residue or placeholders remain, adversarial model findings are resolved, and citation existence is confirmed at publication.
- We assume that a separately generated script would recompute 16 quantitative claims from the paper's stated inputs and that 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Passive iFIR Filters for Data-Driven Control. arXiv:2403.06640v2. https://arxiv.org/abs/2403.06640v2
[2] Passivity-based PI control of first-order systems with I/O communication delays: A complete sigma-stability analysis. arXiv:1507.01146v1. https://arxiv.org/abs/1507.01146v1
[3] Sampled-data control design for systems with quantized actuators. arXiv:2208.05694v3. https://arxiv.org/abs/2208.05694v3
[4] Composite Adaptive Control Barrier Functions for Safety-Critical Systems with Parametric Uncertainty. arXiv:2601.17683v3. https://arxiv.org/abs/2601.17683v3
[5] Robust Nonlinear Optimal Control via System Level Synthesis. arXiv:2301.04943v3. https://arxiv.org/abs/2301.04943v3
[6] Safe Control Synthesis via Input Constrained Control Barrier Functions. arXiv:2104.01704v1. https://arxiv.org/abs/2104.01704v1
[7] On $\ell_2$-performance of weakly-hard real-time control systems. arXiv:2305.07875v3. https://arxiv.org/abs/2305.07875v3
[8] On the relationship between control barrier functions and projected dynamical systems. arXiv:2309.04378v1. https://arxiv.org/abs/2309.04378v1
[9] QNFO: Passive Signal as Passive Controller: A Systems-Theoretic Feasibility Analysis of the Signal-Worker Ontology
[10] QNFO: Structural vs Driven Quantum Coherence
