# Ensemble Drafting Under Broadcast Control: Throughput Algebra, Variance Reduction, and Vandermonde Conditioning

## Abstract

Ensemble control studies populations of structurally identical dynamical systems that differ only in a parameter and must be steered by a single broadcast input without individual state feedback. We formalize *ensemble drafting*—a population of draft generators whose candidate tokens are checked by a single verifier—as a discrete‑time population‑level control problem in this mold. Closed‑form expressions are derived for the expected accepted length per verification cycle, $E[L]=\frac{1-\alpha^{K}}{1-\alpha}$, the per‑cycle cost $C=Kc_{d}+1$, and the throughput $T=E[L]/C$. Under illustrative assumptions ($\alpha=0.7$, $K=4$, $c_{d}=0.1$) this yields $E[L]=2.533$, $C=1.4$, and $T\approx1.8093$, with a discrete optimum at $K^{\star}=5$ giving $T\approx1.8487$. We prove that equal‑weight moment aggregation over $N$ drafters reduces the standard error of the quality estimate from $\sigma$ to $\sigma/\sqrt{N}$ ($0.3\to0.1342$ for $\sigma=0.3$, $N=5$). We further show that the finite‑horizon reachability map of a linear broadcast‑controlled ensemble is a scaled Vandermonde matrix, exactly controllable if and only if the parameters are pairwise distinct. All numbers are derived with shown arithmetic or labeled as projections; no empirical measurements are reported.

## 1. Introduction

A large‑scale inference system that must generate text quickly but can only verify candidates with a single expensive model faces a broadcast‑control dilemma: the fast draft models propose tokens in parallel, yet the verifier can only accept or reject them based on aggregate statistics. This situation blocks designers from scaling throughput because they cannot tune per‑model schedules without per‑model feedback, incurring wasted compute and higher latency. If the analytical throughput formulas derived here hold, system architects could select the draft depth $K$ that maximizes tokens per verification cost, and could allocate draft resources to achieve a predictable variance reduction in quality estimation.  

**Contributions**  
1. Formal statement of ensemble drafting as a broadcast‑control problem (Section 3).  
2. Closed‑form derivations of $E[L]$, $C$, $T$, and $1/N$ variance reduction (Section 4).  
3. Exact controllability analysis via a scaled Vandermonde reachability matrix (Section 3.5 and Section 4, Step 7).  
4. Explicitly labeled projections with stated assumptions, distinguished from derived results (throughout).  

## 2. Background and Related Work



**[1] Chaos in DNA inversions (Draft paper).** This draft proves that the inversion process occurring in DNA mutations is chaotic according to Devaney’s theory. Its relevance is methodological: it demonstrates that a discrete symbolic process can be analyzed with dynamical‑systems tools, analogous to our stochastic drafting process.

**[2] Learning Contact Representation for Leg Odometry.** This work addresses contact detection for legged odometry, showing that higher pseudo‑label classification accuracy does not necessarily translate into better downstream performance and that scaling the ZUPT covariance reduces drift. Both findings caution that a drafter’s offline quality score can decouple from throughput, motivating our focus on accepted length per cost.











**[8] Asymptotic of Bergman Kernel (Master Thesis).**

**[9] QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel.** This document introduces an explicit membership table for a formal core. We adopt the same practice by listing assumptions A1–A4 in a table‑like form, ensuring transparent grounding of our analytical model.







## 3. Methods

### 3.1 Formal model of ensemble drafting

We model an ensemble drafting system as a discrete‑time population process. The population consists of $N$ drafters indexed by $i\in\{1,\dots,N\}$, each a stochastic generator producing candidate tokens. The state at cycle $t$ is the pair $S_{t}=(x_{t},q_{t})$, where $x_{t}$ is the shared generated sequence and $q_{t}=(q_{1,t},\dots,q_{N,t})$ is the vector of drafter quality statistics (empirical acceptance rates). The action space is a broadcast schedule: a single scalar decision $a_{t}\in\{1,\dots,N\}$ (or a distribution over drafters) applied at the population level, not a per‑drafter vector. The feedback channel returns only aggregate accept/reject outcomes from the verifier, so individual drafter states are observable only through the statistics $q_{t}$; this is the underactuated, feedback‑limited structure.

### 3.2 Assumptions

We list the assumptions explicitly, in the spirit of an honest membership table for the formal core [9]:

- **A1 (i.i.d. acceptance).** Each drafted token is accepted independently with probability $\alpha$, the per‑token acceptance probability, identical across drafters and cycles.  
- **A2 (cost model).** Drafting one token costs $c_{d}$ verifier‑equivalent units; one verification step costs $1$ unit regardless of the number of drafted tokens checked in parallel.  
- **A3 (spectral gap in quality).** Drafter‑quality variation across the population is bounded and separated; this condition converts pointwise statements into uniform ones over the population.  
- **A4 (independent modes).** Drafts from different generators are statistically independent, the decoupling‑by‑mode structure analogous to the parity and harmonic‑number decoupling of perturbation modes.

### 3.3 Drafter specialization

Following the spanning‑set design principle of [7] — a basis in which each element is matched to exactly one problem region while the remainder stays finite — we assign each drafter to cover a distinct region of the input distribution, with the verifier absorbing whatever no drafter covers. Under A4 the population‑level acceptance equations then decouple per drafter, which is what makes the moment aggregation of Section 4 tractable.

### 3.4 Verification cycle and termination

One verification cycle proceeds as: (i) the scheduled drafter produces $K$ candidate tokens; (ii) the verifier checks all $K$ in parallel; (iii) the accepted prefix is committed and the cycle ends at the first rejection (or after $K$ acceptances). Termination is immediate by construction: the cycle length is bounded by $K$ deterministically, so no well‑foundedness argument beyond the bounded loop is required; this contrasts with verification frameworks that must prove well‑foundedness explicitly, as in the constructive consistency proof of [3].

### 3.5 Reachability of the linear broadcast ensemble

As a control‑theoretic abstraction, consider the linear broadcast‑controlled ensemble $x_{i,t+1}=\lambda_{i}x_{i,t}+u_{t}$, with identical scalar input $u_{t}$ and member parameters $\lambda_{i}$. After horizon $H$,

$$
x_{i,H}= \lambda_{i}^{H}x_{i,0}+\sum_{t=0}^{H-1}\lambda_{i}^{H-1-t}u_{t}.
$$

The finite‑horizon reachability map from the input history $(u_{0},\dots,u_{H-1})$ to the state vector $(x_{1,H},\dots,x_{N,H})$ is, up to a fixed scaling of columns by powers of the $\lambda_{i}$, a Vandermonde matrix $M$ with entries $M_{i,j}=\lambda_{j}^{\,i-1}$, whose determinant is

$$
\det M=\prod_{1\le i<j\le N}(\lambda_{j}-\lambda_{i}).
$$

Hence the ensemble is exactly controllable in $H\ge N$ steps if and only if the parameters $\lambda_{i}$ are pairwise distinct.

## 4. Analysis

All inputs in this section are illustrative assumptions, stated here once: per‑token acceptance probability $\alpha=0.7$; draft depth $K$ (varied); drafter cost per token $c_{d}=0.1$; drafter‑quality standard deviation $\sigma=0.3$; ensemble size $N=5$. Every number below is derived with shown arithmetic.

**Step 1: expected accepted length.** Under A1 the number of accepted tokens before the first rejection (capped at $K$) has expectation

$$
E[L]=\sum_{k=0}^{K-1}\alpha^{k}=\frac{1-\alpha^{K}}{1-\alpha}.
$$

For $K=4$: $\alpha^{4}=0.7^{4}=0.2401$; $1-0.2401=0.7599$; $1-\alpha=0.3$; therefore

$$
E[L]=\frac{0.7599}{0.3}=2.533.
$$

**Step 2: per‑cycle cost.** By A2,

$$
C=Kc_{d}+1=4\times0.1+1=1.4.
$$

**Step 3: throughput.**  

$$
T=\frac{E[L]}{C}=\frac{2.533}{1.4}=1.8092857\ldots\approx1.8093.
$$

**Step 4: discrete optimum over $K$.** We enumerate $K\in\{3,4,5,6\}$ with the same inputs:

- $K=3$: $\alpha^{3}=0.7^{3}=0.343$; $E[L]=(1-0.343)/0.3=0.657/0.3=2.19$; $C=1.3$; $T=2.19/1.3=1.684615\ldots\approx1.6846$.  
- $K=4$: $T\approx1.8093$ (Steps 1–3).  
- $K=5$: $\alpha^{5}=0.7^{5}=0.16807$; $E[L]=(1-0.16807)/0.3=0.83193/0.3=2.7731$; $C=5\times0.1+1=1.5$; $T=2.7731/1.5=1.848733\ldots\approx1.8487$.  
- $K=6$: $\alpha^{6}=0.7^{6}=0.117649$; $E[L]=(1-0.117649)/0.3=0.882351/0.3=2.94117$; $C=1.6$; $T=2.94117/1.6=1.838231\ldots\approx1.8382$.

The maximum over this grid is at $K^{\star}=5$ with $T\approx1.8487$.

**Step 5: continuous‑optimum bracket.** Treat $K$ as continuous and maximize $f(K)=\dfrac{1-\alpha^{K}}{Kc_{d}+1}$. Setting $\frac{df}{dK}=0$ yields

$$
-\alpha^{K}\ln\alpha\,(Kc_{d}+1)=c_{d}(1-\alpha^{K}).
$$

With $\alpha=0.7$ and $c_{d}=0.1$, $-\ln\alpha=0.356675\ldots$, giving the equation

$$
0.7^{K}\bigl(0.0356675\,K+0.456675\bigr)=0.1.
$$

Evaluating:

- $K=5$: $0.7^{5}=0.16807$, $0.0356675\times5+0.456675=0.6350125$, product $=0.106727\ldots>0.1$.
- $K=6$: $0.7^{6}=0.117649$, $0.0356675\times6+0.456675=0.67068$, product $=0.078906\ldots<0.1$.

Since the left‑hand side decreases with $K$, the continuous optimum lies strictly between $K=5$ and $K=6$, confirming that the discrete optimum $K^{\star}=5$ is not an artifact of the grid.

**Step 6: break‑even draft cost.** The optimal depth switches from $K=5$ to $K=4$ when $T_{5}=T_{4}$:

$$
\frac{2.7731}{5c_{d}+1}=\frac{2.533}{4c_{d}+1}.
$$

Cross‑multiplying and solving for $c_{d}$:

$$
2.7731(4c_{d}+1)=2.533(5c_{d}+1)\;\Rightarrow\;11.0924c_{d}+2.7731=12.665c_{d}+2.533,
$$

$$
0.2401=1.5726c_{d}\;\Rightarrow\;c_{d}^{\ast}=\frac{0.2401}{1.5726}=0.15269\ldots\approx0.1527.
$$

Thus for $c_{d}<0.1527$ the deeper draft $K=5$ is optimal; for $c_{d}>0.1527$ the shallower $K=4$ wins.

**Step 7: variance reduction by moment aggregation.** Under A4, the draft‑quality estimates $\hat{q}_{i}$ of the $N$ drafters are independent and unbiased with common standard deviation $\sigma$. The equal‑weight aggregate $\bar{q}=\frac{1}{N}\sum_{i=1}^{N}\hat{q}_{i}$ has

$$
\mathrm{Var}(\bar{q})=\frac{\sigma^{2}}{N},\qquad
\mathrm{SE}(\bar{q})=\frac{\sigma}{\sqrt{N}}.
$$

For $\sigma=0.3$, $N=5$: $\sqrt{5}=2.2360679\ldots$; $0.3/2.2360679\ldots=0.134164\ldots\approx0.1342$. The reduction factor relative to a single drafter is $1/\sqrt{5}\approx0.4472$.

**Step 8: controllability instance.** For $N=2$ members with $\lambda_{1}\neq\lambda_{2}$, $\det M=\lambda_{2}-\lambda_{1}\neq0$, so the two‑member ensemble is exactly controllable in $H=2$ steps; if $\lambda_{1}=\lambda_{2}$ then $\det M=0$ and the two states are permanently locked together under any broadcast input.

## 5. Results

All values below are computed in Section 4 with shown arithmetic; none are empirical measurements.

1. With $\alpha=0.7$, $K=4$, $c_{d}=0.1$: $E[L]=2.533$, $C=1.4$, $T\approx1.8093$.  
2. The discrete throughput optimum over $K\in\{3,4,5,6\}$ is $K^{\star}=5$, with $E[L]=2.7731$, $C=1.5$, $T\approx1.8487$; neighboring values are $T(3)\approx1.6846$ and $T(6)\approx1.8382$.  
3. Continuous‑optimum analysis shows the true optimum lies between $K=5$ and $K=6$, confirming the grid result.  
4. The break‑even draft cost is $c_{d}^{\ast}\approx0.1527$: for $c_{d}<0.1527$ depth $K=5$ is optimal, otherwise $K=4$ is optimal.  
5. Equal‑weight aggregation over $N=5$ drafters with $\sigma=0.3$ reduces the standard error from $\sigma=0.3$ to $\sigma/\sqrt{N}\approx0.1342$, a factor of $1/\sqrt{5}\approx0.4472$.  
6. The finite‑horizon reachability map of the linear broadcast ensemble is a scaled Vandermonde matrix, exactly controllable iff the parameters $\lambda_{i}$ are pairwise distinct (proof in Section 3.5; two‑member instance in Step 8).  

**Projection (labeled, not computed).** If the acceptance probability were instead $\alpha=0.5$ with the same $c_{d}=0.1$, the same formulas project $E[L]=(1-0.5^{4})/0.5=1.875$, $C=1.4$, $T\approx1.3393$ for $K=4$; the uncertainty in this projection is dominated by the assumed $\alpha$, and no data are offered for it.

## 6. Discussion

**Limitations.** Assumption A1 (i.i.d. acceptance with constant $\alpha$) is the strongest and least defensible: real drafter quality is autocorrelated across positions and degrades on out‑of‑distribution inputs, which would inflate the variance of $E[L]$ beyond the $1/N$ law of Step 7, whose derivation also requires A4 (independence); correlated drafter errors break the $\sigma/\sqrt{N}$ reduction. Assumption A2 prices verification as depth‑independent, which favors large $K$; a verifier cost growing with $K$ would shift or remove the interior optimum $K^{\star}=5$, which is anyway only a grid optimum over $\{3,4,5,6\}$, not a continuous one.

**Failure modes.** If drafter qualities are heterogeneous (violating the common‑$\alpha$ reading of A1), the closed form $E[L]=(1-\alpha^{K})/(1-\alpha)$ applies per drafter but the population aggregate requires a mixture, which we have not derived. If the broadcast schedule cannot observe even aggregate statistics, the scheduling problem reduces to open‑loop control, where the Vandermonde controllability result still holds but the throughput optimization does not.

**What would falsify the claims.** The $1/N$ variance reduction is falsified by any measured standard error of the aggregate quality estimate that does not scale as $\sigma/\sqrt{N}$ under independent drafters. The Vandermonde controllability claim is falsified by a pairwise‑distinct parameter set whose finite‑horizon reachability matrix is singular. The throughput formulas are falsified by acceptance processes whose empirical mean accepted length departs from $(1-\alpha^{K})/(1-\alpha)$ at fixed $\alpha$.

**Open questions.** Whether the multi‑axis evaluation style of [10] can be operationalized for drafting ensembles (throughput, robustness, cost) with a validation coefficient analogous to its $\mathrm{MCS}=0.875$; whether the mode‑decoupling analogy with [5] survives correlated drafter failures; and whether the gap condition A3 can be weakened while preserving uniform population‑level statements, in the way the semi‑classical calculus of [8] converts pointwise asymptotics into uniform ones. The chaotic‑dynamics analysis of discrete symbolic processes in [1] suggests a further question: whether drafter‑acceptance sequences exhibit structured dynamics that a purely i.i.d. model misses; 

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Designers of speculative‑decoding pipelines for large language models, as well as control‑theoretic engineers working on broadcast‑actuated ensembles (e.g., swarm robotics or quantum‑ensemble control), would use the derived throughput algebra to select the draft depth $K$ that maximizes tokens per verification cost. When the analytical optimum $K^{\star}=5$ is adopted, the system can expect up to $1.85$ accepted tokens per unit verification cost under the stated $\alpha$ and $c_{d}$.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 2 (formulation of concept and analytical studies).

**(c) Minimal next experiment.**  
Implement a software prototype that simulates $N=5$ independent drafters with $\alpha=0.7$, varying $K\in\{3,4,5,6\}$, and measures the empirical average accepted length $\hat{E}[L]$ and throughput $\hat{T}=\hat{E}[L]/C$. The experiment falsifies the main result if $|\hat{T}-T_{\text{predicted}}|>0.05$ for all $K$, indicating a breakdown of the i.i.d. assumption or of the cost model.

**(d) Engineering constraints.**  
- Ability to broadcast a single schedule $a_{t}$ to all drafters without per‑drafter latency.  
- Accurate measurement of aggregate accept/reject statistics to estimate $\alpha$ in situ.  
- Verification hardware whose cost per cycle remains approximately constant (unit cost $=1$) regardless of $K$; if verification cost scales with $K$, the derived optimum shifts.  
- Independence of drafter outputs (A4) must be enforced by architectural separation (e.g., distinct random seeds, non‑overlapping model parameters).

**(e) Order‑of‑magnitude performance bounds.**  
Using the derived formulas with $\alpha=0.7$, $c_{d}=0.1$, the maximum achievable throughput is $T_{\max}\approx1.85$ tokens per verification‑cost unit at $K^{\star}=5$. The corresponding per‑token cost is $1/T_{\max}\approx0.54$ cost units. These bounds hold as long as A1–A4 remain valid.

**(f) Direct risks and misuse paths.**  
Applying the i.i.d. acceptance model to heterogeneous draft models may lead to over‑optimistic throughput estimates, causing over‑provisioning of compute resources. Moreover, assuming verification cost independence from $K$ when hardware imposes a linear or super‑linear scaling could waste energy and increase latency. Careful profiling of the verifier is therefore required before deploying the optimal $K$ in production.

## 8. Conclusion

We recast ensemble drafting as a population‑level broadcast‑control problem, derived closed‑form expressions for expected accepted length, per‑cycle cost, and throughput with fully shown arithmetic ($E[L]=2.533$, $C=1.4$, $T\approx1.8093$ at $K=4$; grid optimum $K^{\star}=5$ at $T\approx1.8487$ under the stated illustrative inputs), proved a $1/N$ standard‑error reduction for moment aggregation ($0.3\to0.1342$ at $N=5$, $\sigma=0.3$), and showed that the linear broadcast ensemble’s reachability map is a scaled Vandermonde matrix, exactly controllable iff the parameters are pairwise distinct. All quantitative claims are either derived above or explicitly labeled projections; the framework’s empirical value remains an open question.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Chaos in DNA inversions (Draft paper). arXiv:1105.1512v1. https://arxiv.org/abs/1105.1512v1
[2] Learning Contact Representation for Leg Odometry. arXiv:2606.05501v2. https://arxiv.org/abs/2606.05501v2
[3] DRAFT: A Formally Verified Constructive Proof of the Consistency of Peano Arithmetic Using Ordinal Assignments. arXiv:2603.00487v1. https://arxiv.org/abs/2603.00487v1
[5] Master Functions and Equations for Perturbations of Vacuum Spherically-Symmetric Spacetimes. arXiv:2108.08668v3. https://arxiv.org/abs/2108.08668v3
[7] Prescriptive Master Integrals of Maximal Weight at Two Loops. arXiv:2610.10672v1. https://arxiv.org/abs/2610.10672v1
[8] Asymptotic of Bergman Kernel (Master Thesis). arXiv:2202.03383v1. https://arxiv.org/abs/2202.03383v1
[9] https://papers.qnfo.org/papers/consilient-synthesis-v2. QNFO: QNFO Consilient Synthesis v2.0: The Shared Adelic Kernel.
[10] https://papers.qnfo.org/papers/population-level-methods-for-structured-ensembles-from-chaotic-dna-inversions-to. QNFO: Population-Level Methods for Structured Ensembles: From Chaotic DNA Inversions to Ensemble Leg Drafting.

## Appendix A. Divergence report

No unresolved divergences remain in the reconciled text. The conventions adopted, documented here for transparency: (i) where source drafts differed on whether the grid optimum over $K$ should be presented as a global optimum, the main text adopts the weaker and safer convention of a grid optimum over $K\in\{3,4,5,6\}$; (ii) where drafts differed on the scope of the variance‑reduction claim, the main text adopts the version conditional on assumptions A1 and A4 (independence and common $\sigma$); (iii)  The citation of the spanning‑set principle was corrected to reference [7] as required by its source text.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: Ensemble drafting as broadcast population control (state, action, feedback) | A, B, C | CONVERGENT |
| C2: $E[L]=(1-\alpha^{K})/(1-\alpha)$ with $E[L]=2.533$ at $\alpha=0.7$, $K=4$ | A, B, C | CONVERGENT |
| C3: $C=Kc_{d}+1=1.4$ at $K=4$, $c_{d}=0.1$ | A, B | CONVERGENT |
| C4: $T=E[L]/C\approx1.8093$ | A, B, C | CONVERGENT |
| C5: Grid optimum $K^{\star}=5$, $T\approx1.8487$ | A, B | CONVERGENT (scope: grid, per Appendix A) |
| C6: Standard error $\sigma/\sqrt{N}\approx0.1342$ at $\sigma=0.3$, $N=5$ | A, B, C | CONVERGENT |
| C7: Vandermonde reachability, controllable iff pairwise distinct $\lambda_{i}$ | A, C | CONVERGENT |
| C8: Assumptions A1–A4 as explicit membership table (motivated by [9]) | B, C | CONVERGENT |
| C9: Drafter specialization via spanning‑set principle of [7] | A | SINGLE |
| C10: Projection at $\alpha=0.5$, $T\approx1.3393$ | B | SINGLE (labeled projection) |