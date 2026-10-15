# Relaxation in Noisy Quantum Maps versus Classical Iterative Algorithms: A Shared Decay Law with a Divergent Semiclassical Limit

## Abstract

Operators of hybrid classical-quantum compute facilities must decide, before any hardware is committed, whether a relaxation-type workload converges faster as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum co-processor; no side-by-side convergence law with explicit arithmetic is available to guide that decision. This paper supplies one. Both processes are formulated as linear contractions toward a fixed point, yielding the shared step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$ for depolarizing strength $\varepsilon$, initial distance $D_0$, and tolerance $\delta$. Evaluated at $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$, both a qubit under depolarizing noise and a classical iteration with convergence factor $0.99$ need $1374.6$ steps ($1375$ integer steps); reducing $\varepsilon$ tenfold raises the count only to $13808.6$, a factor of $10.045$. A fidelity clock $F(t)=\frac{1}{2}(1+(1-\varepsilon)^t)$ converts any threshold $F_\ast>1/2$ into a step count, giving $2.011$ steps to $F_\ast=0.99$ at $\varepsilon=0.01$. The principal result is that at fixed $\varepsilon$ and finite $\hbar$ the two relaxations are step-count-indistinguishable; the only grounded locus of divergence is the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, where relaxation time of quantized toral maps is sensitive to classical chaos. This redirects deployment decisions from speedup exponents to per-step costs and limit ordering, and yields a pre-registered falsification protocol.

## 1. Introduction

Computational facilities that mix classical solvers with quantum processors face a scheduling problem that is currently solved by guesswork. A relaxation-type workload — driving a system from an arbitrary initial state to a target stationary or near-stationary state — can run as a classical stationary iteration on a CPU cluster or as a repeatedly applied noisy quantum map on a quantum device, and the operator must decide how many steps, and therefore how much wall-clock time and energy, each route needs. If the two routes obey different relaxation laws, one route can be ruled out by scaling alone before any hardware is bought; if they obey the same finite-step law, the decision hinges on per-step cost and on limit-ordering questions instead. Today no such side-by-side law is available in explicitly comparable form, so procurement and scheduling decisions rest on unquantified intuitions about "quantum speedup".

The cost of this gap is concrete in both directions. A team that assumes a quadratic-type quantum advantage for a relaxation task, by analogy with phase and amplitude estimation where a quadratic speedup is known [4], may commit to hardware whose actual relaxation time scales no better than a classical iteration at the relevant noise level. A team that assumes equivalence may miss regimes, identified in the quantum-maps literature, where relaxation time depends on the chaotic character of an underlying classical system and therefore cannot be matched by any classical iteration with a fixed convergence factor [5]. A decision rule that separates the regime where the two processes coincide from the regime where they can differ would change what is computed before purchase, what is measured during commissioning, and what a claimed quantum advantage must demonstrate to be credited to quantumness rather than to unmatched parameters.

This paper answers the question: does relaxation in noisy quantum maps differ from relaxation in classical algorithms? The answer is constructed by placing both processes in the simplest common mathematical frame — linear contraction toward a fixed point — deriving the step-count law both obey at fixed noise strength, evaluating that law with full arithmetic, contrasting it with two relaxation laws from the literature that are genuinely different in form (a continuous-time level-to-level decay from a damped Madelung fluid model [8] and an algebraic coarsening law from a cellular-automaton emulation study [9]), and then identifying the one place, the joint semiclassical and weak-noise limit, where the quantum case is known to behave differently [5]. The falsification condition is stated in advance, following the pre-registered falsification methodology demonstrated for measurement-triggered relaxation claims [10].

The contributions are:

- A unified contraction-frame derivation of the relaxation step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$, valid identically for a depolarizing qubit channel and for a classical stationary iteration with convergence factor $1-\varepsilon$, with explicit evaluation at $\varepsilon=0.01$, $\delta=10^{-6}$, $D_0=1$ giving $1374.6$ steps (Section 4.1).
- A crossover analysis showing the law is logarithmically insensitive to $\varepsilon$: reducing $\varepsilon$ by a factor of ten multiplies the step count by $10.045$, computed explicitly, against a factor of exactly $10$ for the algebraic law $\tau=1/\sqrt{ab\varepsilon}$ of the rule-110 emulation study (Section 4.2).
- A fidelity clock $F(t)=\frac{1}{2}(1+(1-\varepsilon)^t)$ with worked threshold crossings at $F_\ast=0.99$ for three noise strengths (Section 4.3).
- A limit-ordering argument, grounded in the relaxation-time results for quantized toral maps [5], that locates the only known quantum-classical divergence in the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, together with a pre-registered falsification criterion modeled on the checksummed, tolerance-based protocol of [10] (Sections 4.4, 4.5 and 6).

## 2. Background and Related Work

The closest formal antecedent on the quantum side is the relaxation time introduced for noisy quantum maps on the $2d$-dimensional torus, which generalizes the earlier classical notion of dissipation time [5]. That work shows that relaxation time is sensitive to the chaotic behavior of the corresponding classical system when the semiclassical limit ($\hbar\to 0$) and the limit of small noise strength ($\varepsilon\to 0$) are considered simultaneously. Two features of this result drive the present analysis. First, relaxation time is a property of the map's approach to equilibrium, exactly the quantity a classical numerical analyst calls convergence time; the paper's own introduction frames it as the speed at which a conservative dynamical system subjected to noise converges to equilibrium, generalizing the dissipation-time studies in which density fluctuations decay during noisy evolution. Second, the sensitivity to chaos appears only in a joint limit, which means that at fixed $\hbar$ and fixed $\varepsilon$ no statement of difference is available from that result. The present paper supplies the fixed-$\varepsilon$ comparison that [5] deliberately does not address, and then uses the joint-limit sensitivity as the candidate locus of genuine divergence. The same source also fixes useful asymptotic conventions: $a(\epsilon)\ll b(\epsilon)$ iff $a(\epsilon)/b(\epsilon)\to 0$, $a(\epsilon)\sim b(\epsilon)$ iff the ratio is bounded above and below by positive constants, and $a(\epsilon)\approx b(\epsilon)$ iff the ratio tends to $1$; these conventions are adopted in Section 4.4.

On the classical side, the parallel Jacobi family of one-sided trigonometric and hyperbolic Jacobi-type algorithms for Hermitian eigenvalue problems is the named representative of the class of stationary iterations whose convergence factor is treated here as a free parameter. The prior version of this analysis used exactly this role for the Jacobi family and noted that its convergence quality is instance-dependent in ways a single-$\rho$ model hides [11]. The present paper keeps that role: the derivation of Section 4.1 is a comparison of structural laws, not of specific implementations.

The quantum speedup question is bounded by known results on phase and amplitude estimation, which admit a quadratic quantum speedup [4]. The same work records that Wang, Higgott and Brierley showed there is a continuous trade-off between quantum speedup and circuit depth through a family of algorithms known as $\alpha$-QPE, and derives the scaling of $\alpha$-QPE within the Quantum Singular Value Transformation (QSVT) framework. Its discussion makes the trade-off explicit: approximating the step function up to error $\eta/2$ outside $[-\delta,\delta]$ relates the parameters as $\eta+\frac{1}{2}\delta^{\alpha}=1$, so that $\alpha$ parametrizes how lower-degree polynomials (lower circuit depths) are compensated by running the circuits more times. This matters here because it shows that even for the best-understood quantum speedups the advantage is a trade-off curve, not a step-count constant; a relaxation comparison that reports only asymptotic exponents would overstate the practical difference. The present analysis keeps the comparison at the level of explicit step counts at fixed parameters.

A different relaxation law from the quantum-foundations side comes from the hydrodynamic research program in which quantum jumps are reinterpreted as continuous, deterministic relaxation events in a damped Madelung fluid [8]. That work adds a linear drag term $-m\gamma\mathbf{v}$ to the Madelung momentum equation, shows eigenstate densities remain exact fixed points of the damped flow, and derives closed-form level-to-level relaxation times $t_{n\to n-1}=\ln[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})]/(2\gamma)$, giving $t_{1\to 0}=0.549306/\gamma$ and $t_{2\to 1}=0.255413/\gamma$, with energy decay $E(t)=E_0\,e^{-2\gamma t}$ under orbit averaging. Its own discussion flags that the Lyapunov argument establishes attractivity of the fixed-point set, not global convergence to a unique eigenstate, and that degenerate spectra, limit cycles, or chaotic attractors could prevent convergence to a single outcome. This is directly relevant: it is a second exponential relaxation law, in continuous time and with mode-dependent rates, and its stated failure modes (persistent oscillations when perturbations inject energy faster than dissipation removes it) mark exactly the conditions under which a single-contraction-factor frame fails. Section 4.2 uses its $t_{1\to 0}=0.549306/\gamma$ as the continuous-time counterpart of the discrete step-count law.

A third, algebraic relaxation law comes from the study of emergent universality in cellular automata, in which the Turing-complete, chiral elementary cellular automaton rule 110 is emulated by three individually mirror-symmetric and individually trivial rules — rules 36, 37, and 5 — arranged in a fixed period-3 spatial schedule [9]. That work models the desynchronization boundaries between phase domains as point particles with density $\rho(t)$ that annihilate on contact, with noise of strength $\varepsilon$ creating new walls at rate $a\,\varepsilon$ per site per step. Its derived results include the steady-state scaling $\rho^{*}=\sqrt{a\varepsilon/b}$, the relaxation time $\tau=1/\sqrt{ab\varepsilon}$ (giving $\tau=10$ steps at $\varepsilon=10^{-2}$ and $\tau=100$ steps at $\varepsilon=10^{-4}$ for $a=b=1$), and the transient law $\rho(t)=\rho_0/(1+b\rho_0 t)$ at zero noise, showing algebraic coarsening. Its discussion concedes that one-dimensional coarsening can admit logarithmic corrections to mean-field exponents and that the prefactor $\sqrt{a/b}$ has not been measured. Section 4.2 uses this law as the contrast case: an algebraic relaxation whose parameter sensitivity differs qualitatively from the exponential contraction law derived here.

The methodology of stating a falsification condition in advance is taken from the pre-registered falsification of deterministic measurement-triggered relaxation [10]. That work tested whether deterministic relaxation toward eigenstate basins can reproduce Born probabilities of a two-level system: all seven configurations produced the verdict FAIL, with a maximum deviation of $0.5$ against a pre-registered tolerance of $10^{-2}$, because a deterministic map from a fixed initial state yields a degenerate outcome channel taking only the values $0$ or $1$. Its practitioner section packages the protocol as reusable: fixed Hamiltonian, sealed test set, pre-registered tolerance, checksummed code, threshold terminal rule, so that a claim can be re-verified in minutes without trusting the authors. Section 3.5 and Section 6 adopt this template for the present central claim.

The prior version of this comparison [11] established the shared step-count law and its evaluation ($1374.6$ steps at $\varepsilon=0.01$, $\delta=10^{-6}$; a factor of $10.045$ for a tenfold noise reduction; a fidelity-threshold crossing analysis), and located the divergence locus in the joint semiclassical and weak-noise limit. The present paper re-derives those results with the arithmetic shown, replaces the prior paper's imported external fidelity threshold with a generic threshold analysis at $F_\ast=0.99$, and adds the cross-model law contrasts against [8] and [9] that sharpen what "different relaxation" would even mean.

Three further works shape the engineering framing. The distributed maximum-clique work defines the target figure of merit as the costup — an increase in performance greater than the increase in cost, be it measured in money or energy — and achieves it by a simple modification of a state-of-the-art exact algorithm distributed over an ad-hoc cluster of over 100 teaching machines accessible only through SSH, NFS and Java [1]. Its conclusion reports concrete numbers: instances that take weeks on a single machine solved in under 4 to 11 hours on the cluster, with less than a week of development effort, e.g. frb35-17-2 in under 7 hours against over 13 days on a single machine. The costup is adopted here as the gate any quantum-relaxation deployment must pass: a route wins only if its step-count advantage survives the development effort of realizing it.

The submodular maximization literature supplies the per-step-cost lesson. Maximizing a non-negative monotone submodular function under a cardinality constraint admits polynomial-time approximation algorithms, yet solving it in practice often involves frequently querying the submodular function, so query cost dominates runtime [2]. The same work's algorithms achieve adaptive complexities independent of $n$ — the main algorithm LS+GS has adaptive complexity dependent on parameters $p$ and $k$, with query complexity $O((\frac{1}{\varepsilon k}+1)\frac{n}{\varepsilon^{3}})$ for its LALS subroutine — demonstrating that the resource that binds in practice (queries, i.e. per-step evaluations) is distinct from the iteration count. The analogue for relaxation is that per-step cost, not step count alone, determines wall-clock time; Section 4.5 formalizes this as a parity condition.

The TSP-with-neighborhoods work illustrates how far structural results transfer across instance classes. TSPN, a generalization of the Euclidean TSP in which the salesman must visit connected regions rather than points, is NP-hard; for disjoint unit disks a constant-factor approximation exists with tour length $|T|\leq((1+\frac{8}{\pi})|T^{*}|+8)(1+\epsilon)$, and a PTAS exists for equal-size disjoint disks, but a recent APX-hardness result rules out a PTAS for the general case [3]. Its conclusion lists as open whether a constant-factor approximation exists for arbitrary connected regions in the plane. By analogy, relaxation-time results for structured maps (tori, as in [5]) need not transfer to unstructured instances; Section 6 carries this as a limitation.

Finally, two algorithmic existence results are reminders that existence of a quantity does not imply availability of an efficient procedure to control it. The consensus-tree work constructs the majority rule (+) consensus tree in $O(kn)$ time, which is optimal because the input size is $\Omega(kn)$, and the frequency-difference consensus tree in $\min\{O(kn^{2}),\,O(kn(k+\log^{2}n))\}$ time, fully deterministically and without hashing [6]. The odd-gracefulness work states that in spite of the large number of papers published on graph labeling, there are few algorithms researchers can actually use to gracefully label graphs, and provides generalized odd graceful solutions for a specific graph construction [7]. Both patterns recur here: a relaxation time can be defined for a broad class of systems, as [5] does, while the efficient computation or control of that quantity — the thing an operator actually needs — is the missing piece this paper addresses at the level of explicit laws.

## 3. Methods

### 3.1 Common contraction frame

Both processes under comparison are discrete-time linear contractions toward a fixed point. Let $x_t$ be the state after $t$ steps, $x_\ast$ the fixed point, and suppose

$$\|x_{t+1}-x_\ast\| \le \rho\,\|x_t-x_\ast\|,$$

with contraction factor $0\le\rho<1$. Iterating gives

$$\|x_t-x_\ast\| \le \rho^{\,t}\,\|x_0-x_\ast\|.$$

Define the initial distance $D_0=\|x_0-x_\ast\|$ and a tolerance $\delta$ with $0<\delta<D_0$. The step count $t_\delta$ at which the distance first falls to $\delta$ satisfies $\rho^{\,t_\delta}D_0=\delta$, hence

$$t_\delta=\frac{\ln(\delta/D_0)}{\ln\rho}.$$

This frame is method-level and parameter-level only. It assumes linearity of the contraction, time-independence of $\rho$, and a norm in which the contraction inequality holds. No hardware, dataset, or simulation is used anywhere in this paper; every number in Section 5 is computed by hand arithmetic in Section 4 from the stated inputs.

### 3.2 Quantum instantiation: depolarizing noise on a qubit

For a single qubit undergoing a depolarizing channel of strength $\varepsilon$ per step, the state updates as

$$\rho_{t+1}=(1-\varepsilon)\,\rho_t+\varepsilon\,\frac{\mathbb{I}}{2},$$

so that after $t$ steps

$$\rho_t=(1-\varepsilon)^t\rho_0+\bigl(1-(1-\varepsilon)^t\bigr)\frac{\mathbb{I}}{2}.$$

The maximally mixed state $\mathbb{I}/2$ is the fixed point, and the trace distance from the fixed point contracts as

$$D\bigl(\rho_t,\mathbb{I}/2\bigr)=(1-\varepsilon)^t\,D\bigl(\rho_0,\mathbb{I}/2\bigr),$$

which is the contraction frame with $\rho=1-\varepsilon$. The identification of the depolarizing channel as a convex mixture with the maximally mixed state is the standard definition of that channel; no empirical claim is involved.

### 3.3 Classical instantiation: stationary iteration

For a classical stationary iteration $x_{t+1}=Mx_t+c$ with iteration matrix $M$ of spectral radius $\rho(M)<1$, the error propagates as $e_{t+1}=Me_t$, giving $\|e_t\|\le\rho(M)^t\|e_0\|$. Setting $\rho(M)=1-\varepsilon$ makes the classical and quantum instantiations share the identical step-count law with identical parameters. This identification is a modeling choice, and its consequence — that at fixed $\varepsilon$ the two processes are step-count-indistinguishable — is a theorem of the frame, not an empirical observation.

### 3.4 Fidelity clock

For the qubit channel of Section 3.2, the fidelity between $\rho_t$ and the pure initial state $\rho_0=|\psi\rangle\langle\psi|$ is

$$F(t)=\langle\psi|\rho_t|\psi\rangle=(1-\varepsilon)^t+\bigl(1-(1-\varepsilon)^t\bigr)\frac{1}{2}=\frac{1+(1-\varepsilon)^t}{2}.$$

This converts any fidelity threshold $F_\ast$ into a step count $t_\ast$ via $(1-\varepsilon)^t=2F_\ast-1$, i.e.

$$t_\ast=\frac{\ln(2F_\ast-1)}{\ln(1-\varepsilon)},$$

valid when $F_\ast>1/2$. Section 4.3 evaluates this clock at the representative threshold $F_\ast=0.99$ for three noise strengths. No external fidelity threshold is imported in this version: the generic threshold analysis preserves the demonstrative content of the prior version's imported marker [11] without borrowing an unsupported number.

### 3.5 Falsification protocol

Following the pre-registration pattern of [10] — fixed test set, pre-registered tolerance, checksummed code, and a verdict rule fixed before the run — the observation that would falsify the paper's central claim is stated in advance. The central claim is: at fixed $\varepsilon$ and fixed finite $\hbar$, quantum and classical relaxation obey the same step-count law. The pre-registered falsifier is any rigorously derived or empirically measured pair $(t_\delta^{\mathrm{Q}},t_\delta^{\mathrm{C}})$ at the same $\varepsilon$, $\delta$, and $D_0$ whose ratio differs from $1$ by more than a pre-registered tolerance, set here at $10^{-2}$ relative, matching the tolerance discipline of [10]. Section 6 develops what such a pair would require.

## 4. Analysis

### 4.1 Baseline step count at $\varepsilon=0.01$, $\delta=10^{-6}$

Inputs: $\varepsilon=0.01$ (chosen as a representative per-step noise strength; the scaling is derived in Section 4.2), $D_0=1$ (worst case: a pure state maximally far from the maximally mixed state in trace distance), $\delta=10^{-6}$ (a tolerance at which residual coherence is negligible for most protocol purposes).

Step 1: contraction factor $\rho=1-\varepsilon=0.99$.

Step 2: $\ln(\delta/D_0)=\ln(10^{-6})=-6\ln 10=-6\times 2.302585=-13.815510$.

Step 3: $\ln\rho=\ln(0.99)$. Expanding $\ln(1-x)=-x-x^2/2-x^3/3-\cdots$ with $x=0.01$:

$$\ln(0.99)=-0.01-0.00005-0.000000333-0.0000000025=-0.010050336.$$

Step 4:

$$t_\delta=\frac{-13.815510}{-0.010050336}=1374.6.$$

Check: $1374.6\times 0.010050336=13.8155$, matching the numerator. So both the depolarizing qubit and the classical iteration with $\rho=0.99$ need $1374.6$ steps, i.e. $1375$ integer steps, to reach $\delta=10^{-6}$.

### 4.2 Logarithmic insensitivity to $\varepsilon$, and contrast with two other relaxation laws

Reduce the noise strength to $\varepsilon=0.001$, so $\rho=0.999$. Then

$$\ln(0.999)=-0.001-0.0000005-0.000000000333=-0.001000500.$$

The step count is

$$t_\delta=\frac{13.815510}{0.001000500}=13808.6.$$

The ratio to the $\varepsilon=0.01$ case is

$$\frac{13808.6}{1374.6}=10.045.$$

$$t_\delta=\frac{13.815510}{0.001000500}=13808.6.$$

The ratio to the $\varepsilon=0.01$ case is

$$\frac{13808.6}{1374.6}=10.045.$$

A tenfold reduction in noise strength multiplies the relaxation step count by $10.045$, not by $10$: the step count scales as $1/\varepsilon$ up to a logarithmic correction of relative size $\varepsilon/2$ (from the $x^2/2$ term in $\ln(1-x)$). Explicitly, $t_\delta\approx\frac{\ln(\delta/D_0)}{-\varepsilon-\varepsilon^2/2}$, so $t_\delta\cdot\varepsilon\approx\ln(\delta/D_0)\cdot\frac{1}{1+\varepsilon/2}$; at $\varepsilon=0.01$ the correction factor is $\frac{1}{1.005}=0.99502$, i.e. a $0.498\%$ reduction relative to the pure $1/\varepsilon$ law. This is the quantitative sense in which the relaxation clock is logarithmically insensitive to its parameters: only $\ln(\delta/D_0)$ and $1/\varepsilon$ matter, and the former changes by $2.302585$ per decade of tolerance.

The same arithmetic gives the contrast with the two other relaxation laws cited in Section 2. The algebraic coarsening law of the rule-110 emulation study, $\tau=1/\sqrt{ab\varepsilon}$ with $a=b=1$, gives $\tau=10$ steps at $\varepsilon=10^{-2}$ and $\tau=100$ steps at $\varepsilon=10^{-4}$ [9]: a tenfold reduction in $\varepsilon$ multiplies its relaxation time by exactly $10$, the pure $1/\varepsilon$ scaling with no logarithmic correction. The exponential contraction law derived here gives $10.045$ for the same change, so the two laws are distinguishable in principle by a $0.45\%$ excess factor at a tenfold noise reduction, growing with further decades. The continuous-time law of the damped Madelung fluid, $t_{n\to n-1}=\ln[(n+\tfrac{1}{2})/(n-\tfrac{1}{2})]/(2\gamma)$ with $t_{1\to 0}=0.549306/\gamma$ [8], is exponential in form like the present law but has mode-dependent rates and a continuous time parameter; it matches the contraction frame only after a fixed mode $n$ and a step-to-time conversion are chosen, which the hydrodynamic work does not supply.

### 4.3 Fidelity-threshold crossing at $F_\ast=0.99$

Input: $F_\ast=0.99$, chosen as a representative generic threshold strictly above the maximally mixed fidelity $1/2$; no external number is imported.

Step 1: $2F_\ast-1=2\times 0.99-1=0.98$.

Step 2: $\ln(0.98)$. Expanding $\ln(1-x)=-x-x^2/2-x^3/3-x^4/4-\cdots$ with $x=0.02$:

$$\ln(0.98)=-0.02-0.0002-0.000002667-0.000000004=-0.020202707.$$

Step 3: at $\varepsilon=0.01$ ($\ln(0.99)=-0.010050336$ from Section 4.1),

$$t_\ast=\frac{-0.020202707}{-0.010050336}=2.011.$$

So a pure qubit state falls below fidelity $F_\ast=0.99$ after $2.011$ steps, i.e. $3$ integer steps, at $\varepsilon=0.01$.

Step 4: at $\varepsilon=0.1$ ($\rho=0.9$). Expanding $\ln(0.9)=-0.1-0.005-0.000333-0.000025=-0.105361$ (the series converges more slowly here; the four terms shown give $-0.105358$, and the standard value $\ln 0.9=-0.105361$ is used):

$$t_\ast=\frac{-0.020202707}{-0.105361}=0.192.$$

Step 5: at $\varepsilon=0.001$ ($\ln(0.999)=-0.001000500$ from Section 4.2),

$$t_\ast=\frac{-0.020202707}{-0.001000500}=20.19.$$

The margin interpretation: the threshold sits at fraction $2F_\ast-1=0.98$ of the initial-to-fixed-point contraction, i.e. only $2\%$ of the initial-to-fixed-point fidelity distance is consumed before the threshold is crossed, which is why the step counts are small at all three noise strengths.

### 4.4 Where the quantum case can diverge: the joint limit

At fixed $\varepsilon$ and fixed finite $\hbar$, Sections 4.1–4.3 show the quantum relaxation clock is fully determined by the contraction factor $1-\varepsilon$ and is identical in form to the classical stationary-iteration clock. The known point of divergence is supplied by the toral-map result [5]: relaxation time is sensitive to the chaotic behavior of the corresponding classical system when the semiclassical limit ($\hbar\to 0$) and the small-noise limit ($\varepsilon\to 0$) are taken simultaneously. The structural reason the two limits must be joint is visible in the present formulas: as $\varepsilon\to 0$ at fixed tolerance, $t_\delta\to\infty$ like $1/\varepsilon$ (Section 4.2), so the noise-induced relaxation that defines the clock vanishes exactly in the limit where the classical dynamics would control the behavior; any chaos-dependence must therefore be resolved in the ordering of $\hbar\to 0$ relative to $\varepsilon\to 0$.

The scale condition can be stated explicitly. The noise sets a relaxation scale $t_{\mathrm{noise}}\sim 1/\varepsilon$: from Section 4.2, $t_\delta\varepsilon\approx\ln(\delta/D_0)$, so per unit of $\ln(\delta/D_0)$ the scale is $1/\varepsilon$. The semiclassical evolution sets an Ehrenfest-type scale; the toral-map result asserts that relaxation time depends on classical chaos in the regime where both limits are taken together [5]. A quantitative ordering parameter would be the ratio of the Ehrenfest time to $1/\varepsilon$, but no formula for the Ehrenfest time or for the relaxation time as a function of $\hbar$ and $\varepsilon$ is available for computation here, so that ratio is flagged as the key open quantity in Section 6. The asymptotic conventions of [5] — $a(\epsilon)\ll b(\epsilon)$ iff $a(\epsilon)/b(\epsilon)\to 0$, $a(\epsilon)\sim b(\epsilon)$ iff the ratio is bounded above and below by positive constants, and $a(\epsilon)\approx b(\epsilon)$ iff the ratio tends to $1$ — are adopted for any future statement of that ordering.

### 4.5 Per-step cost and the costup criterion

Step count alone does not determine wall-clock time. The submodular-maximization literature makes the analogous point that practice is dominated by the cost of frequently querying the function being optimized [2]: its main algorithm LS+GS achieves adaptive complexity independent of $n$, dependent on parameters $p$ and $k$, with query complexity $O((\frac{1}{\varepsilon k}+1)\frac{n}{\varepsilon^{3}})$ for its LALS subroutine, showing that the binding resource (queries, i.e. per-step evaluations) is distinct from the iteration count. For the present comparison, let $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$ be the per-step costs (in time or energy) of one quantum-map application and one classical iteration, respectively. Wall-clock parity requires

$$c_{\mathrm{Q}}\,t_\delta^{\mathrm{Q}}<c_{\mathrm{C}}\,t_\delta^{\mathrm{C}}.$$

Since Section 4.1 gives $t_\delta^{\mathrm{Q}}=t_\delta^{\mathrm{C}}$ at matched parameters, parity reduces to $c_{\mathrm{Q}}<c_{\mathrm{C}}$, and any quantum advantage must come from a smaller per-step cost or from operating at a smaller effective $\varepsilon$. Neither $c_{\mathrm{Q}}$ nor $c_{\mathrm{C}}$ is computable from the analysis of this paper, so no cost numbers are reported, and the costup criterion of [1] — an increase in performance greater than the increase in cost, be it measured in money or energy — is adopted as the qualitative gate a deployment must pass. That work's own demonstration is a reminder that the gate is passable by non-obvious routes: a simple modification of a state-of-the-art exact algorithm, distributed over an ad-hoc cluster of over 100 teaching machines accessible only through SSH, NFS and Java, solved instances that take weeks on a single machine in under 4 to 11 hours, with frb35-17-2 in under 7 hours against over 13 days on a single machine and less than a week of development effort [1].

## 5. Results

All numbers below are computed in Section 4 by explicit arithmetic from the stated inputs; none are measured or simulated.

**R1 (shared step-count law).** At $\varepsilon=0.01$, $D_0=1$, $\delta=10^{-6}$, both the depolarizing qubit channel and a classical stationary iteration with convergence factor $0.99$ relax in $t_\delta=1374.6$ steps ($1375$ integer steps). The two processes are step-count-indistinguishable at matched parameters.

**R2 (logarithmic insensitivity).** Reducing $\varepsilon$ from $0.01$ to $0.001$ raises the step count from $1374.6$ to $13808.6$, a factor of $10.045$. The step count obeys $t_\delta\approx\ln(\delta/D_0)/(-\varepsilon-\varepsilon^2/2)$, with a $0.498\%$ logarithmic correction at $\varepsilon=0.01$. Against the algebraic law $\tau=1/\sqrt{ab\varepsilon}$ of [9], which scales by exactly $10$ per decade of $\varepsilon$, the exponential law carries a $0.45\%$ excess per decade.

**R3 (fidelity-threshold crossing).** A pure qubit state crosses the generic threshold $F_\ast=0.99$ after $2.011$ steps ($3$ integer steps) at $\varepsilon=0.01$, after $0.192$ steps at $\varepsilon=0.1$, and after $20.19$ steps at $\varepsilon=0.001$. The threshold sits at $98\%$ of the initial-to-fixed-point contraction.

**R4 (locus of divergence).** At fixed $\varepsilon$ and finite $\hbar$, no divergence between quantum and classical relaxation is derivable in the contraction frame. The only grounded locus of divergence is the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, where relaxation time of noisy quantum maps on tori is sensitive to the chaos of the underlying classical system [5]. The quantitative ordering parameter (an Ehrenfest-time-to-$1/\varepsilon$ ratio) is not computable here and is listed as open.

**R5 (cost gate).** Wall-clock parity at matched parameters requires $c_{\mathrm{Q}}<c_{\mathrm{C}}$; no per-step cost values are derivable in this paper, so this is stated as a gate, not a number.

## 6. Discussion

The central result, R1, is a negative one: in the simplest common frame, relaxation in a noisy quantum map and relaxation in a classical iterative algorithm are the same process mathematically, and the interesting physics lives entirely in the joint limit that the contraction frame deliberately freezes. This framing has three limitations that a reader should weigh before using R1 in any decision.

First, the contraction frame assumes a time-independent, linear contraction with a single fixed point. Real quantum maps can have multiple fixed points, limit cycles, or non-normal contraction structure, and real classical solvers use preconditioning, acceleration, and adaptive tolerances that change the effective $\rho$ from step to step. The parallel Jacobi family cited as the classical representative has convergence quality that is instance-dependent in ways a single-$\rho$ model hides [11], and the damped-Madelung work states the analogous failure on the quantum side explicitly: its Lyapunov argument establishes attractivity of the fixed-point set, not global convergence to a unique eigenstate, and degenerate spectra, limit cycles, or chaotic attractors could prevent convergence to a single outcome [8]. Where such structure is present, the single-contraction-factor law of Section 4.1 does not apply.

Second, the identification $\rho(M)=1-\varepsilon$ is a modeling choice. A classical iteration with $\rho=0.99$ and a qubit under $\varepsilon=0.01$ depolarizing noise match by construction, but nothing forces a real workload to present matched parameters. The honest statement is conditional: *if* the parameters are matched, the step counts are equal. The falsification protocol of Section 3.5 is designed around exactly this conditionality. A third framing limit is structural transfer: relaxation-time results for structured maps (tori, as in [5]) need not transfer to unstructured instances, in the same way that TSPN admits a constant-factor approximation and a PTAS for equal-size disjoint disks but is ruled out of a PTAS in the general case by a recent APX-hardness result, with a constant-factor approximation for arbitrary connected regions still open [3].

**What would falsify the main result.** The main result (R1, with R4 as its boundary) is falsified if any of the following is established: (i) a noisy quantum map at fixed $\varepsilon$ and finite $\hbar$ whose relaxation time to tolerance $\delta$ differs from $\ln(\delta/D_0)/\ln(1-\varepsilon)$ by more than the pre-registered relative tolerance of $10^{-2}$ — this would show the single-parameter contraction frame fails for quantum maps, e.g. through non-unimodal spectral structure; (ii) a classical stationary iteration and a quantum map with matched contraction factors whose measured or rigorously derived step counts differ at the same $\delta$ and $D_0$ by more than $10^{-2}$ relative; (iii) a derivation showing that the chaos-sensitivity of relaxation time in the toral-map setting [5] survives at fixed finite $\hbar$ and $\varepsilon$, rather than only in the joint limit. Any one of these would force a revision of R1; none is currently available. The pre-registered form follows the template demonstrated in [10], where a fixed Hamiltonian, sealed test set, pre-registered tolerance of $10^{-2}$, checksummed code, and a threshold terminal rule produced a verdict (FAIL, maximum deviation $0.5$, fifty times tolerance, from a degenerate outcome channel taking only the values $0$ or $1$) that a practitioner can re-verify in minutes without trusting the authors; the same audit structure is proposed here for any claimed violation of R1.

**Limitations list.**

- *Single fixed point, linear contraction.* R1 holds only within the frame of Section 3.1; sensitivity to this assumption is total, since the entire derivation is the frame.
- *Depolarizing noise model.* The quantum instantiation uses the standard depolarizing channel; other channels (amplitude damping, dephasing) contract in different norms and can give different fixed points, so R1's numerical value $1374.6$ is model-specific, though the law's form survives any geometric contraction.
- *Matched-parameter condition.* The equality in R1 requires $\rho(M)=1-\varepsilon$; unmatched parameters reintroduce a difference that is trivially large, so the result constrains only fair comparisons.
- *Generic threshold.* R3 uses the representative threshold $F_\ast=0.99$ chosen in this paper; it is not an externally certified operating point, and step counts at other thresholds follow from $t_\ast=\ln(2F_\ast-1)/\ln(1-\varepsilon)$.
- *No per-step costs.* R5 is a gate without numbers because no cost data exist in this analysis; any cost claim would be unsupported.
- *Open ordering parameter.* The ratio of the semiclassical (Ehrenfest-type) time to $1/\varepsilon$, which would quantify R4, is not derivable here; the paper's divergence claim is therefore qualitative at exactly the point where it would be most useful.
- *Instance-dependence of the classical representative.* The convergence factor of a real classical solver is instance-dependent [11], so the matched-parameter equality is an idealization even on the classical side.
- *Algebraic-law contrast is mean-field.* The $\tau=1/\sqrt{ab\varepsilon}$ law of [9] carries the caveat, stated in that work, that one-dimensional coarsening can admit logarithmic corrections to mean-field exponents and that the prefactor $\sqrt{a/b}$ has not been measured; the $0.45\%$-per-decade contrast of R2 is therefore between an exact exponential law and a mean-field algebraic law.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are operators and architects of hybrid classical-quantum compute facilities who must decide, for a relaxation-type workload, whether to schedule it on classical hardware or on a quantum co-processor. If R1 holds, the decision rule changes from "estimate the quantum speedup exponent" to "compare per-step costs $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$ at matched contraction parameters, and check whether the workload's effective noise strength $\varepsilon$ can be lowered on either route." Concretely, a scheduling policy derived from R1 is: compute $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$ for the workload's tolerance and noise level, apply it identically to both routes, and break the tie only on per-step cost and limit-ordering risk (R4). A second user group is the authors and consumers of quantum-relaxation proposals: R1 supplies the fair-comparison condition $\rho(M)=1-\varepsilon$ that any claimed quantum advantage must satisfy before it is credited to quantumness rather than to unmatched parameters. A third group is grant reviewers and due-diligence analysts, who can apply the three-ingredient audit structure of [10] — fixed test set, pre-registered tolerance, checksummed code — to any claimed violation of R1, reusing the template that [10] packages as reusable for relaxation-dynamics claims.

**(b) Current readiness.** This work is purely analytical and has not been peer reviewed: the contraction frame of Section 3.1, the derivations of Section 4, and the falsification protocol of Section 3.5 are all pen-and-paper results with no hardware, simulation, or experimental component. Against the NASA Technology Readiness Level definitions, this places the work at TRL 1–2: basic principles observed and reported, with the underlying physical and mathematical assumptions formulated but not applied in any demonstrated context. Analytical work cannot exceed TRL 3, and nothing in this paper supports a claim of experimental validation, component development, or manufacturing readiness.

**(c) The smallest next test.** The smallest de-risking calculation is a numerical one, requiring no quantum hardware: implement the depolarizing qubit channel of Section 3.2 and a classical stationary iteration with $\rho(M)=1-\varepsilon$ on the same computer, run both from matched initial conditions to tolerance $\delta=10^{-6}$ at $\varepsilon=0.01$, and verify that both reach the tolerance at the same step count, predicted to be $1375$ integer steps (Section 4.1). The outcome that refutes R1 is a measured step-count mismatch between the two implementations at matched parameters beyond floating-point round-off; the outcome that refutes the frame itself is a quantum-map simulation at fixed $\varepsilon$ and finite effective $\hbar$ whose relaxation step count deviates from $\ln(\delta/D_0)/\ln(1-\varepsilon)$ by more than the pre-registered relative tolerance of $10^{-2}$ (falsifier (i) of Section 6). A second, larger next step is to compute or bound the ordering parameter identified in Section 4.4 — the ratio of the semiclassical (Ehrenfest-type) time to $1/\varepsilon$ — for a specific quantized toral map, which would convert the qualitative divergence claim R4 into a quantitative one.

**(d) Binding constraints.** Because this is analytical work, the constraints that would bind first in any future engineering use are, in order: (i) *noise characterization* — the law's input $\varepsilon$ must be the actual per-step noise strength of the device, and no device-level noise data exist in this analysis, so this is an open question rather than a derived constraint; (ii) *channel validity* — the quantum instantiation assumes depolarizing noise; whether a real device's error channel contracts in trace distance with a single factor $1-\varepsilon$ is an open question that falsifier (i) of Section 6 would resolve; (iii) *per-step cost data* — the cost gate of R5 requires $c_{\mathrm{Q}}$ and $c_{\mathrm{C}}$, neither of which is derivable here, so wall-clock comparisons remain blocked on measurement; (iv) *limit-ordering theory* — the Ehrenfest-time-to-$1/\varepsilon$ ratio of Section 4.4 is not computable here, so any deployment in the joint-limit regime is blocked on theory before it is blocked on hardware. Materials, tolerances, and component constraints do not bind at this stage because no hardware design is proposed.

**(e) Order-of-magnitude bounds.** The only quantitative bounds this paper can state as projections are step-count scalings already derived in Section 4, restated here with their assumptions. Assuming the depolarizing model and $D_0=1$: a tenfold reduction in tolerance (one decade of $\delta$) adds $2.302585/0.010050336\approx229.1$ steps at $\varepsilon=0.01$ (from $\ln 10=2.302585$, divided by the Section 4.1 denominator); a tenfold reduction in $\varepsilon$ multiplies the step count by $10.045$ (Section 4.2). No cost, energy, market, or performance figures are stated, because no per-step cost or device data exist in this analysis; any such figure would be unsupported.

**(f) Risks and misuse paths.** The principal misuse is the one the paper is designed to prevent, in both directions: citing R1 to claim "no quantum advantage is possible" (it constrains only matched-parameter, fixed-$\varepsilon$, single-fixed-point comparisons), or citing R4 to claim "quantum relaxation is chaos-accelerated" (the chaos-sensitivity of [5] is established only in the joint $\hbar\to 0$, $\varepsilon\to 0$ limit, and no ordering parameter is computed here). A second misuse path is reading R3 as a hardware-relevant lifetime prediction; R3 uses a generic threshold chosen for demonstration, not a certified operating point. A third is treating the algebraic-law contrast of R2 as a measured distinction; it is a comparison of functional forms under the mean-field caveat of [9].

## 8. Conclusion

Relaxation in a noisy quantum map and relaxation in a classical stationary iteration, placed in the same linear-contraction frame with matched parameters, obey the identical step-count law $t_\delta=\ln(\delta/D_0)/\ln(1-\varepsilon)$: at $\varepsilon=0.01$ and $\delta=10^{-6}$ both need $1374.6$ steps, and the law is logarithmically insensitive to its inputs, a tenfold noise reduction buying only a factor of $10.045$ in step count. The fidelity clock derived from the same frame crosses the generic threshold $F_\ast=0.99$ after $2.011$ steps at $\varepsilon=0.01$. Within this frame, therefore, there is no quantum-classical distinction to exploit or fear; the one grounded locus of distinction is the joint semiclassical and weak-noise limit, where relaxation time of quantized toral maps is known to depend on the chaos of the underlying classical system, and where the quantitative ordering parameter remains open. The practical yield of the analysis is a fair-comparison condition, a pre-registered falsifier, and a smallest next test — a matched-parameter numerical run of the depolarizing channel against a stationary iteration, predicted to terminate at the same $1375$th step — by which the central claim can be refuted if it is wrong.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Distributing an Exact Algorithm for Maximum Clique: maximising the costup. arXiv:1209.4560v1. https://arxiv.org/abs/1209.4560v1
[2] Fast Parallel Algorithms for Submodular $p$-Superseparable Maximization. arXiv:2311.13123v2. https://arxiv.org/abs/2311.13123v2
[3] Approximation algorithms for TSP with neighborhoods in the plane. arXiv:1703.01640v1. https://arxiv.org/abs/1703.01640v1
[4] Simplifying a classical-quantum algorithm interpolation with quantum singular value transformations. arXiv:2207.14810v3. https://arxiv.org/abs/2207.14810v3
[5] Relaxation Time of Quantized Toral Maps. arXiv:math-ph/0406055v3. https://arxiv.org/abs/math-ph/0406055v3
[6] Algorithms for the Majority Rule (+) Consensus Tree and the Frequency Difference Consensus Tree. arXiv:1307.7821v2. https://arxiv.org/abs/1307.7821v2
[7] An Algorithm for Odd Gracefulness of the Tensor Product of Two Line Graphs. arXiv:1103.4502v1. https://arxiv.org/abs/1103.4502v1
[8] QNFO: Quantization as Hydrodynamic Relaxation: Eigenstates as Attractor Basins in a Dissipative Madelung Fluid
[9] QNFO: Emergent Universality from Symmetric Rules: Rule-110 Emulation by Alternating Trivial Cellular Automaton Rules
[10] QNFO: A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation
[11] QNFO: Relaxation in Noisy Quantum Maps versus Classical Iterative Algorithms: A Shared Decay Law with a Divergent Semiclassical Limit
