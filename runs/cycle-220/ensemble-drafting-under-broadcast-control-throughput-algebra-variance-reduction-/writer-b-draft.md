# Ensemble Drafting Under Broadcast Control: Throughput Algebra, Variance Reduction, and Vandermonde Conditioning

## Abstract

Ensemble control studies populations of structurally identical dynamical systems, differing only in a parameter, that must be steered by a single broadcast input without individual state feedback. We formalize *ensemble drafting* — a population of draft generators whose candidate tokens are checked by a single verifier — as a discrete-time population-level control problem in this mold. The specific gap is that existing ensemble-drafting systems are tuned empirically, without closed-form guidance on draft depth, ensemble size, or the conditioning of the underlying population model. We derive closed-form expressions for the expected accepted length per verification cycle, $E[L] = (1-\alpha^{K})/(1-\alpha)$, the per-cycle cost $C = K c_d + 1$, and the throughput $T = E[L]/C$; under stated illustrative assumptions ($\alpha = 0.7$, $K = 4$, $c_d = 0.1$) this gives $E[L] = 2.533$, $C = 1.4$, and $T \approx 1.8093$, with a grid optimum at $K^{\star} = 5$ giving $T \approx 1.8487$ and a continuous optimum bracketed between $K = 5$ and $K = 6$. We prove that equal-weight moment aggregation over $N$ drafters reduces the standard error of the quality estimate from $\sigma$ to $\sigma/\sqrt{N}$ ($0.3 \to 0.1342$ for $\sigma = 0.3$, $N = 5$), and that the finite-horizon reachability map of a linear broadcast-controlled ensemble is a scaled Vandermonde matrix, exactly controllable if and only if the parameters are pairwise distinct. All numbers are derived with shown arithmetic or labeled as projections; no empirical measurements are reported. The results give inference-serving designers an analytic rule for draft depth and ensemble size, and a falsifiable target for simulation.

## 1. Introduction

Serving large language models at scale is dominated by verifier cost: in speculative decoding, a fast draft model proposes tokens that a slower target model checks in parallel, and the realized speedup is set by how many drafted tokens the verifier accepts per unit of verification effort. The measurement literature quantifies the stakes. TABED, a test-time adaptive ensemble drafting method for Large Vision-Language Models, reports an average robust walltime speedup of $1.74\times$ over standard decoding and a $5\%$ improvement over single drafting methods, achieved without additional training or tuning [4]. The same work documents the design problem this paper addresses: across 11 benchmark datasets, neither multimodal nor text-only drafting consistently outperformed the other, with scenario-specific performance fluctuations across turns, image inclusion, and out-of-distribution inputs [4]. A serving team today must therefore pick draft models, draft depth, and ensemble weights by benchmarking, because no closed-form algebra tells them what draft depth $K$ or ensemble size $N$ maximizes accepted tokens per verification cost.

This is structurally the ensemble-control dilemma. Moment-based ensemble control treats a population — in the limit a continuum — of structurally identical dynamical systems with parametric variations, and identifies the severely underactuated nature of such systems and the inability to avail comprehensive state feedback as the central challenges for analysis and design [6]. In such systems an aggregated, population-level measurement is often available even though dedicated sensors on each member are not [6]. An ensemble drafting population has exactly this shape: the drafters are individually heterogeneous (parametric variation in quality and calibration), yet verification and scheduling decisions are made at the population level, and the only feedback is aggregate accept/reject statistics from the verifier.

What would change if the results below hold: a serving engineer could compute the throughput-optimal draft depth from two measured quantities (per-token acceptance probability $\alpha$ and per-token draft cost $c_d$) instead of grid-searching by benchmark; a robustness engineer could size the drafter ensemble from a target standard error using the $1/N$ law; and a control theorist could treat the scheduling problem with the same reachability tools used for broadcast-controlled populations.

This paper makes four contributions:

1. A formal statement of ensemble drafting as a population-level control problem, defining the state, the broadcast action space, and the verification feedback channel, with assumptions A1–A4 listed as an explicit membership table for the formal core (Section 3).
2. Closed-form derivations of the expected accepted length $E[L]$, the per-cycle cost $C$, and the throughput $T = E[L]/C$, including a continuous-optimum bracketing argument and a break-even cost $c_d^{\ast} \approx 0.1527$ at which the optimal draft depth changes, plus a proof that moment-based aggregation of draft-quality statistics reduces estimator variance as $1/N$ (Section 4).
3. An exact controllability analysis of the linear broadcast-controlled ensemble: the finite-horizon reachability matrix is a scaled Vandermonde matrix, nonsingular if and only if the parameters are pairwise distinct (Sections 3 and 4).
4. Explicitly labeled projections with stated assumptions, distinguished throughout from derived results; no experimental measurements are reported.

Throughout, "ensemble" means a family of systems indexed by a parameter; "broadcast input" means a single scalar signal applied identically to all members; a "verification cycle" is one round of draft generation followed by parallel verification.

## 2. Background and Related Work

This section discusses the twelve works of the bibliography in its exact order and numbering, grounding every statement in what each work's own text states.

**[1] Chaos in DNA inversions (Draft paper), arXiv:1105.1512v1.** This draft paper proves that the inversion process occurring in DNA mutations is chaotic under Devaney's theory of chaos. Its text defines chaotic iterations over a finite set of Boolean cells updated by a strategy sequence, and describes a "chaotic model" of trinucleotide mutation in which the mutable subset $J(t)$ changes at each time step, with trinucleotide distributions in coding frames grouped into three subsets $X_0$, $X_1$, $X_2$ [1]. The relevance is methodological: a discrete symbolic process with random subset selection can be analyzed as a dynamical system, which supports our treatment of drafter acceptance sequences as a stochastic discrete process rather than a purely i.i.d. stream (Section 6 raises this as a hypothesis).

**[2] Learning Contact Representation for Leg Odometry, arXiv:2606.05501v2.** This work addresses contact detection for legged odometry, where the zero-velocity assumption of the stance foot (ZUPT) makes accurate contact classification a critical subproblem, and proposes self-supervised representation learning that requires neither force sensors nor contact labels [2]. Two of its findings transfer directly to our setting. First, its Table 1 shows supervised CNN classifiers reaching an F1 of $0.998$ in simulation but degrading to $0.907$ on the physical robot, a domain shift the authors attribute to sensor noise and unmodeled terrain compliance [2]. Second, its conclusion states that higher pseudo-label classification accuracy does not necessarily translate into better leg odometry, and that scaling the ZUPT covariance by a GMM posterior fitted in a learned latent space reduces drift [2]. Both findings are cautions for ensemble drafting: a drafter's offline quality score (our analogue of classification accuracy) can decouple from downstream throughput, which is why our framework optimizes accepted length per cost rather than acceptance probability alone.

**[3] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments, arXiv:2603.00487v1.** This work presents a modified version of Gentzen's 1936 consistency proof for Peano Arithmetic, based on Gödel's reformulation, with additional details and corrections needed to prove the well-foundedness of the cut-elimination argument in a constructive environment; its text reviews Gödel's Second Incompleteness Theorem and describes the sequent calculus $\mathrm{PA}^{\omega}$ with a Cut rule that does not preserve consistency [3]. It anchors the verifier side of our framework: the accept/reject step in drafting is a formal verification act, and [3] exemplifies the standard a verification argument should meet — explicit well-foundedness of the termination argument. Our cycle-termination analysis in Section 3.4 is structured so that termination is immediate by construction, avoiding precisely the well-foundedness burden [3] documents.

**[4] TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs, arXiv:2601.20357v1.** This work benchmarks existing inference methods with small draft models on 11 datasets for Large Vision-Language Models and proposes TABED, which dynamically ensembles multiple drafts obtained via batch inference by leveraging deviations of the drafts from past ground truths [4]. Its reported numbers are the empirical anchor for our algebra: TABED achieves the best or second-best block efficiency across all input scenarios, with an average robust walltime speedup of $1.74\times$ over standard decoding, over $5\%$ improvement over single drafting methods, no additional training or inference cost, and negligible ensembling cost [4]. Our framework complements it by supplying the population-level control formalism and the closed-form throughput algebra that such benchmark-driven weight adaptation implicitly relies on; notably, TABED's dynamic weighting is a feedback mechanism our broadcast model deliberately abstracts away, and Section 6 discusses what that abstraction costs.

**[5] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes, arXiv:2108.08668v3.** This work develops perturbation theory of vacuum spherically-symmetric spacetimes, where spherical symmetry allows an expansion of perturbations in scalar, vector, and tensor harmonics, and the resulting perturbative equations decouple for modes with different parity and different harmonic numbers [5]. Its conclusion enumerates the assumptions behind its master functions and reports two branches of solutions, including a new even-parity master function $\Psi_{\rm EN}$ independent of the Zerilli-Moncrief function $\Psi_{\rm ZM}$ [5]. The decoupling-by-mode structure is the analogue we impose on drafting populations: under Assumption A4, drafts from different generators are treated as independent "modes," and the population-level equations decouple accordingly, which is what makes the moment aggregation of Section 4 tractable.

**[6] Moment-Based Ensemble Control, arXiv:2009.02646v1.** This work addresses controlling a large population — in the limit, a continuum — of structurally identical dynamical systems with parametric variations, and identifies the severely underactuated nature of such ensemble systems and the inability to avail comprehensive state feedback as the central challenges for analysis and design [6]. Its text defines ensemble systems as parameterized populations $\frac{d}{dt}x(t,\beta)=F(x(t,\beta),\beta,u(t))$ with a parameter-independent input, notes that aggregated population-level measurements are often available where per-member sensing is not, and develops a dynamic Hausdorff moment problem through which ensemble systems and their moment systems share the same control and controllability properties, accomplishing model reduction from uncountably many systems to countably many agents [6]. Our framework adopts precisely this problem statement: the drafting population is underactuated (one broadcast schedule signal) and individually unobservable (only aggregate accept statistics are returned), so population-level moments are the natural sufficient statistics, and our $1/N$ variance result is the statistical face of the moment transformation [6] advocates.

**[7] Prescriptive Master Integrals of Maximal Weight at Two Loops, arXiv:2610.10672v1.** This work describes the construction of a spanning set of individually pure, planar master integrals involving massless particles in four dimensions including all maximal-weight contributions at two loops, such that every independent infrared-divergent region is individually matched by specific masters while all other masters are manifestly finite in four dimensions [7]. The design principle — a spanning set in which each basis element is matched to exactly one problem region — is the pattern we use for drafter specialization in Section 3.3: each drafter covers a distinct region of the input distribution, with the verifier absorbing whatever remains.

**[8] Asymptotic of Bergman Kernel (Master Thesis), arXiv:2202.03383v1.** This thesis gives a new proof of the pointwise asymptotic expansion for the Bergman kernel of a hermitian holomorphic line bundle at points where the curvature is positive and satisfies a local spectral gap condition, introducing a suitable semi-classical symbol space and related symbolic calculus inspired by recent work of Hsiao and Savale [8]. Its connection to our work is via the notion of a local spectral gap: our Assumption A3 in Section 3.2 (a gap condition on drafter-quality variation) is named after this style of hypothesis, whose role, as in [8], is to convert pointwise statements into uniform ones over the population.

**[9] QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel.** This document describes a shared adelic kernel proceeding from valuation through tree boundary and Ostrowski's theorem to the adeles, restructured kernel-first with an honest kernel-membership table and mandatory symmetry sections, applying seven corrections (C1–C7) from a red-team audit dated 2026-07-25 [9]. We cite it as methodological context: the practice of an explicit membership table (what is and is not inside the shared formal core) is one we adopt by listing assumptions A1–A4 explicitly, and the red-team-audit practice motivates the self-critical Discussion in Section 6.

**[10] QNFO: Population-Level Methods for Structured Ensembles: From Chaotic DNA Inversions to Ensemble Leg Drafting.** This companion work develops a single analytical framework for three population-level settings, including a toy model of random DNA inversions on a binary sequence of length $L = 10$ with uniformly selected contiguous flip segments, and a moment-based broadcast-control baseline over a continuum of first-order units $\dot{x}_{\omega}(t) = \omega\, u(t)$ with uniform gain density on $[-1,1]$, bang-bang inputs $u(t) \in \{-1,+1\}$, and gain-weighted moments $M_k(t)$ [10]. We cite it for two specific points: its restriction of reachability to the first moment $M_1$ under the weakest nontrivial broadcast class is the same discipline of stating exactly which population functional is controllable that our Section 3.5 applies to the discrete linear ensemble; and its use of the chaotic character of the inversion process [1] to motivate a purely statistical treatment parallels our use of [1] in Section 6.

**[11] QNFO: Connecting Geometrogenesis and Biogenesis.** This work addresses a grand conjecture linking the emergence of spacetime (geometrogenesis) to the evolution of life (biogenesis), argues that a direct test is currently computationally and theoretically intractable — noting that characterizing integrated information $\Phi$ is an NP-hard computational problem — and proposes instead a statistically validated classical analogue built on neutral proxies (a global correlation index and a subsystem integration index) as a necessary, falsifiable first step [11]. We cite it for its method of strategic simplification: when the full empirical question is intractable, validate the structural principle on a classical surrogate first. Our paper applies the same move — the broadcast-control abstraction of drafting is a classical surrogate for the full adaptive-ensemble problem, and its predictions are falsifiable by simulation before any deployment.

**[12] QNFO: Ensemble Drafting Under Broadcast Control: Throughput Algebra, Variance Reduction, and Vandermonde Conditioning.** This is the prior version of the present preprint. Its text already states the closed-form throughput results ($E[L] = 2.533$, $C = 1.4$, $T \approx 1.8093$ at $K = 4$; grid optimum $K^{\star} = 5$ at $T \approx 1.8487$), the $1/N$ standard-error reduction ($0.3 \to 0.1342$ at $N = 5$), the Vandermonde controllability claim, and the limitation that a verifier cost growing with $K$ would shift or remove the interior optimum [12]. The present paper revises it: the related-work section is rebuilt against the current bibliography (adding the leg-odometry evidence of [2] and the companion framework [10]), the grid optimum is supplemented with a continuous-optimum bracketing derivation and a break-even cost analysis (Section 4), and a practical-implications section with readiness assessment is added (Section 7).

## 3. Methods

### 3.1 Formal model of ensemble drafting

We model an ensemble drafting system as a discrete-time population process. The population consists of $N$ drafters indexed by $i \in \{1, \dots, N\}$, each a stochastic generator producing candidate tokens. The state at cycle $t$ is the pair $S_t = (x_t, q_t)$, where $x_t$ is the shared generated sequence and $q_t = (q_{1,t}, \dots, q_{N,t})$ is the vector of drafter quality statistics (empirical acceptance rates). The action space is a broadcast schedule: a single scalar decision $a_t \in \{1, \dots, N\}$ (or a distribution over drafters) applied at the population level, not a per-drafter vector. The feedback channel returns only aggregate accept/reject outcomes from the verifier, so individual drafter states are observable only through the statistics $q_t$. This is the underactuated, feedback-limited structure that [6] identifies for continuum ensembles and that [10] instantiates for a gain-weighted continuum with bang-bang broadcast inputs.

### 3.2 Assumptions

We list the assumptions explicitly, in the spirit of the honest kernel-membership table of [9]:

- **A1 (i.i.d. acceptance).** Each drafted token is accepted independently with probability $\alpha$, the per-token acceptance probability, identical across drafters and cycles.
- **A2 (cost model).** Drafting one token costs $c_d$ verifier-equivalent units; one verification step costs $1$ unit regardless of the number of drafted tokens checked in parallel.
- **A3 (spectral gap in quality).** Drafter-quality variation across the population is bounded and separated, a gap-style condition named after the local spectral gap hypotheses of [8]; its role, as there, is to convert pointwise statements into uniform ones over the population.
- **A4 (independent modes).** Drafts from different generators are statistically independent, the decoupling-by-mode structure analogous to the parity and harmonic-number decoupling of perturbation modes in [5].

### 3.3 Drafter specialization

Following the spanning-set design principle of [7] — a basis in which each element is matched to exactly one problem region while the remainder stays finite — we assign each drafter to cover a distinct region of the input distribution, with the verifier absorbing whatever no drafter covers. Under A4 the population-level acceptance equations then decouple per drafter, which is what makes the moment aggregation of Section 4 tractable. The leg-odometry evidence of [2] warns that this specialization must be validated on downstream throughput, not on per-drafter classification-style quality scores alone.

### 3.4 Verification cycle and termination

One verification cycle proceeds as: (i) the scheduled drafter produces $K$ candidate tokens; (ii) the verifier checks all $K$ in parallel; (iii) the accepted prefix is committed and the cycle ends at the first rejection (or after $K$ acceptances). Termination is immediate by construction: the cycle length is bounded by $K$ deterministically, so no well-foundedness argument beyond the bounded loop is required. This contrasts with verification frameworks that must prove well-foundedness explicitly, as the constructive consistency proof of [3] does for cut elimination.

### 3.5 Reachability of the linear broadcast ensemble

As a control-theoretic abstraction, consider the linear broadcast-controlled ensemble $x_{i,t+1} = \lambda_i x_{i,t} + u_t$, with identical scalar input $u_t$ and member parameters $\lambda_i$. After horizon $H$,

$$x_{i,H} = \lambda_i^{H} x_{i,0} + \sum_{t=0}^{H-1} \lambda_i^{H-1-t} u_t.$$

The finite-horizon reachability map from the input history $(u_0, \dots, u_{H-1})$ to the state vector $(x_{1,H}, \dots, x_{N,H})$ is, up to a fixed scaling of columns by powers of the $\lambda_i$, a Vandermonde matrix $M$ with entries $M_{i,j} = \lambda_j^{\,i-1}$, whose determinant is

$$\det M = \prod_{1 \le i < j \le N} (\lambda_j - \lambda_i).$$

Hence the ensemble is exactly controllable in $H \ge N$ steps if and only if the parameters $\lambda_i$ are pairwise distinct. As in [10], where reachability is stated only for a specified population functional ($M_1$) under a specified input class, the claim here is scoped exactly: it concerns the full state vector of the linear ensemble under unconstrained scalar broadcast inputs, and makes no claim about constrained input classes.

## 4. Analysis

All inputs in this section are illustrative assumptions, stated here once: per-token acceptance probability $\alpha = 0.7$; draft depth $K$ (varied); drafter cost per token $c_d = 0.1$; drafter-quality standard deviation $\sigma = 0.3$; ensemble size $N = 5$. Every number below is derived with shown arithmetic.

**Step 1: expected accepted length.** Under A1 the number of accepted tokens before the first rejection (capped at $K$) has expectation

$$E[L] = \sum_{k=0}^{K-1} \alpha^{k} = \frac{1 - \alpha^{K}}{1 - \alpha}.$$

For $K = 4$: $\alpha^{4} = 0.7^{4} = 0.2401$; $1 - 0.2401 = 0.7599$; $1 - \alpha = 0.3$; therefore

$$E[L] = \frac{0.7599}{0.3} = 2.533.$$

**Step 2: per-cycle cost.** By A2,

$$C = K c_d + 1 = 4 \times 0.1 + 1 = 1.4.$$

**Step 3: throughput.**

$$T = \frac{E[L]}{C} = \frac{2.533}{1.4} = 1.8092857\ldots \approx 1.8093.$$

**Step 4: discrete optimum over $K$.** We enumerate $K \in \{3, 4, 5, 6\}$ with the same inputs:

- $K = 3$: $\alpha^{3} = 0.343$; $E[L] = (1 - 0.343)/0.3 = 0.657/0.3 = 2.19$; $C = 1.3$; $T = 2.19/1.3 = 1.684615\ldots \approx 1.6846$.
- $K = 4$: $T \approx 1.8093$ (Steps 1–3).
- $K = 5$: $\alpha^{5} = 0.7^{5} = 0.16807$; $E[L] = (1 - 0.16807)/0.3 = 0.83193/0.3 = 2.7731$; $C = 5 \times 0.1 + 1 = 1.5$; $T = 2.7731/1.5 = 1.848733\ldots \approx 1.8487$.
- $K = 6$: $\alpha^{6} = 0.7^{6} = 0.117649$; $E[L] = (1 - 0.117649)/0.3 = 0.882351/0.3 = 2.94117$; $C = 1.6$; $T = 2.94117/1.6 = 1.838231\ldots \approx 1.8382$.

The maximum over this grid is at $K^{\star} = 5$ with $T \approx 1.8487$. As a cross-check by direct enumeration of the acceptance process for $K = 4$: $E[L] = 1 + 0.7 + 0.49 + 0.343 = 2.533$, matching Step 1.

**Step 5: continuous-optimum bracket.** Treat $K$ as continuous and maximize $f(K) = (1 - \alpha^{K})/(K c_d + 1)$. Setting the derivative to zero:

$$-\alpha^{K} \ln \alpha \,(K c_d + 1) = c_d (1 - \alpha^{K}),$$

which rearranges, using $-\ln 0.7 = 0.356675\ldots$, to

$$\alpha^{K} \left( c_d + (-\ln \alpha)(K c_d + 1) \right) = c_d.$$

With $c_d = 0.1$ the bracket is $0.1 + 0.356675(0.1K + 1) = 0.0356675\,K + 0.456675$. Evaluate the left side $g(K) = 0.7^{K}(0.0356675\,K + 0.456675)$ against the right side $c_d = 0.1$:

- $g(5) = 0.16807 \times (0.1783375 + 0.456675) = 0.16807 \times 0.6350125 = 0.106727\ldots > 0.1$.
- $g(6) = 0.117649 \times (0.214005 + 0.456675) = 0.117649 \times 0.67068 = 0.078906\ldots < 0.1$.

Since $g$ is strictly decreasing in $K$ here, the continuous optimum lies strictly between $K = 5$ and $K = 6$, consistent with the grid optimum $K^{\star} = 5$ of Step 4 and confirming that the grid result is not a grid artifact.

**Step 6: break-even draft cost.** The optimal depth switches from $K = 5$ to $K = 4$ when $T_5 = T_4$, i.e. when $2.7731/(5 c_d + 1) = 2.533/(4 c_d + 1)$. Cross-multiplying: $2.7731(4 c_d + 1) = 2.533(5 c_d + 1)$, so $11.0924\, c_d + 2.7731 = 12.665\, c_d + 2.533$, giving $0.2401 = 1.5726\, c_d$ and

$$c_d^{\ast} = \frac{0.2401}{1.5726} = 0.15269\ldots \approx 0.1527.$$

For $c_d < c_d^{\ast} \approx 0.1527$ the deeper draft $K = 5$ wins; for $c_d > c_d^{\ast}$ the shallower $K = 4$ wins. This is the sensitivity of the design rule to the one cost parameter it depends on.

**Step 7: variance reduction by moment aggregation.** Under A4, the draft-quality estimates $\hat{q}_{i}$ of the $N$ drafters are independent and unbiased with common standard deviation $\sigma$. The equal-weight aggregate $\bar{q} = \frac{1}{N}\sum_{i=1}^{N} \hat{q}_{i}$ has

$$\mathrm{Var}(\bar{q}) = \frac{\sigma^{2}}{N}, \qquad \mathrm{SE}(\bar{q}) = \frac{\sigma}{\sqrt{N}}.$$

For $\sigma = 0.3$, $N = 5$: $\sqrt{5} = 2.2360679\ldots$; $0.3 / 2.2360679\ldots = 0.134164\ldots \approx 0.1342$. The reduction factor relative to a single drafter is $1/\sqrt{5} \approx 0.4472$. This is the discrete-population counterpart of the moment-based reduction of continuum ensembles to countable statistics in [6].

**Step 8: controllability instance.** For $N = 2$ members with $\lambda_1 \neq \lambda_2$, $\det M = \lambda_2 - \lambda_1 \neq 0$, so the two-member ensemble is exactly controllable in $H = 2$ steps; if $\lambda_1 = \lambda_2$ then $\det M = 0$ and the two states are permanently locked together under any broadcast input.

## 5. Results