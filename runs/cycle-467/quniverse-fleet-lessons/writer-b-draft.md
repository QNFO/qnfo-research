# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet (Post-Retraction Revision, Version 2.0)

## Abstract

Autonomous research fleets must keep serverless worker scripts, databases, and storage buckets operational while publishing cost and performance metrics that external stakeholders can trust. The fleet's own published reliability study was retracted because it described quantitative claims that its derivations did not support, which leaves operators without a corrected, recomputable decision framework. This revision rebuilds that framework from the fleet's documented counts and stated policy parameters. It combines a Bernoulli failure-propagation model with a mitigation factor derived from the fleet's recorded action counts, $\alpha = 1{,}889/(1{,}889+1{,}264) \approx 0.5991$, correcting the retracted version's use of an unsupported $\alpha = 0.5$; it separates every billing ratio from its denominator explicitly; and it recomputes each published claim with shown arithmetic. The model yields an expected $E[F]=1.732$ unresolved worker-script failures per month (standard deviation $\sigma_F \approx 1.284$), a corpus productivity of $9.65$ papers per active project, a high-severity gap proportion of $11.9\%$, a composite autonomy score of $4.26$ rising to $4.66$ when the per-worker failure probability is halved, and projected monthly gateway spend of $\$158.66$ falling to $\$154.33$. The cents-as-dollars billing misread inflates perceived spend to $\$11{,}000$ — $73.3$ times the $\$150$ cap and $122.2$ times the $\$90$ per-30-day gate — while the corrected spend of $\$110$ exceeds that gate by $22.2\%$. Operators, funders, and auditors can use these recomputed levers to size monitoring, budget against the correct units, and enforce claim integrity; the work remains analytical and sits at TRL 2 pending the 30-day measurement pilot specified here.

## 1. Introduction

Platform operators of the Quniverse autonomous research fleet run a continuously active collection of thirty-six serverless worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets that generate and publish scientific content without human intervention. Two intertwined problems currently block the fleet's value. First, unplanned downtime arises from script failures and drift between the service registry and the deployed code; failures that escape both the self-healing layer and human notice accumulate silently. Second, self-reported metrics may be unreliable: the fleet's own reliability study was retracted after publication because it presented quantitative claims its derivations did not support, including a mitigation factor attributed to counts it did not come from and a billing comparison that mixed two different denominators. An operator who cannot trust either the failure counts or the dollar figures cannot budget, cannot set alert thresholds, and cannot demonstrate compliance to a funder.

The retraction is itself the strongest evidence that the problem is real. A fleet that publishes a reliability model about itself, and that model then fails its own integrity audit, has demonstrated that claim-integrity checking is not an optional add-on but a load-bearing component of fleet operations. If the corrected framework proposed here holds, three things change: research velocity rises because fewer unresolved failures interrupt pipelines, operational cost falls because failure-driven overruns are bounded against the documented $\$150$ cap and the $\$90$ per-30-day gate, and stakeholder trust is restored because every published number can be recomputed from stated inputs. Conversely, if the reliability model is wrong, a bounded monitoring window will show it, and the operator will have lost only the cost of reading a log file.

This revision corrects two confirmed errors of the retracted version. First, the retracted abstract placed the statement that the misread spend "exceeds the documented $\$90$ per 30 days gate by $22.2\%$" next to a "$73.3\times$ cap violation" without separating the two denominators; the $22.2\%$ figure belongs to the corrected spend of $\$110$ against the $\$90$ gate, while the $73.3$-fold figure belongs to the misread spend of $\$11{,}000$ against the $\$150$ cap. This revision states every ratio with its denominator named explicitly (Sections 4.7 and 5). Second, the retracted text described $\alpha = 0.5$ as "taken from the retraction notice counts (1,889 self-heal actions, 1,264 handoff actions)"; the count-derived factor is $\alpha = 1{,}889/3{,}153 \approx 0.5991$, and $\alpha = 0.5$ is retained only as a clearly labeled conservative assumption for sensitivity bounding (Section 4.1).

**Contributions.**
- **C1.** Derive a Bernoulli failure-propagation model with the count-derived mitigation factor $\alpha = 1{,}889/(1{,}889+1{,}264) \approx 0.5991$ and compute the expected number of unresolved worker-script failures per month, $E[F]=1.732$, with variance $\operatorname{Var}[F]=1.6485$ and standard deviation $\sigma_F \approx 1.284$ (Section 4.1).
- **C2.** Quantify corpus productivity ($9.65$ papers per active project) and the high-severity gap proportion ($11.9\%$) (Section 4.3).
- **C3.** Show that halving the per-worker failure probability lowers the expected failure count from $1.732$ to $0.866$ and reduces projected monthly gateway spend from $\$158.66$ to $\$154.33$, while raising the composite autonomy score from $4.26$ to $4.66$ (Sections 4.5–4.6).
- **C4.** Recompute every quantitative claim of the retraction notice with denominators named explicitly, separating the cap-relative ratio ($73.3$-fold), the cap-relative excess ($72.3$-fold), the gate-relative ratio ($122.2$-fold), and the corrected-spend gate exceedance ($22.2\%$) (Sections 4.7 and 5).
- **C5.** Extend the model with a silent-failure detection layer calibrated to the $93.5\%$ detection rate reported for the FAME monitor, lowering expected unresolved failures from $1.732$ to $0.113$ per month under stated assumptions (Section 4.8).
- **C6.** Specify a minimal pilot — a six-month failure-count measurement and a billing-feed unit-dimension check — with explicit refutation thresholds (Section 7.3).

The failure-propagation and claim-audit structure developed here could also transfer to any fleet of autonomous software agents that publishes self-reported reliability and cost figures, and the symmetric evidence standard applied to the retraction notice mirrors adjudication rubrics used to evaluate contested research claims in adjacent domains.

## 2. Background and Related Work

Analytical reliability modeling, fleet-level learning, and claim-integrity auditing provide the methodological foundation of this revision. The works below are discussed for the specific methods and results their texts report.

**[1]** studies the interaction of rainfall-induced landslides and soil erosion as a cascade of interacting processes, and quantifies the interaction stochastically: on 1,000 Monte Carlo simulations of cumulated pre-failure and post-failure soil erosion, the authors estimate a $20\%$ increase in total soil loss, with the post-failure erosion rate on average around $3.5$ times the pre-failure value and a bootstrap analysis over 10,000 runs giving post-failure increases of approximately 1,700 tons per year (bootstrap $p \leq 0.05$). This is a worked example of exactly the pattern this paper needs: a system of interacting processes whose aggregate behavior is quantified by stochastic propagation over a baseline, with uncertainty assessed by resampling. Our Bernoulli propagation over a baseline failure probability follows the same logic at much smaller scale.

**[2]** presents FLEET, a federated learning emulation and evaluation testbed that integrates the Flower federated-learning framework with the Containernet Docker-based network emulator, is configured through TOML files, and exports comprehensive metrics from all components to ZMQ, CSV, or log files. Its design premise — that algorithmic performance is deeply coupled with the operational environment and must be evaluated under realistic conditions — motivates our pilot design: the fleet's failure counts and billing feed must be captured as structured telemetry of the same kind FLEET exports, not as narrative claims.

**[3]** frames reliability qualification of advanced semiconductor devices as a sequential decision problem and presents an adaptive test-planning framework combining Monte Carlo Tree Search with an extended Kalman filter; over 5,000 planning iterations the planner improves characterization yield from $20\%$ to over $54\%$ while keeping damage fractions below $0.57$ in the best successful test sequence. This supports our choice of an adaptive, staged monitoring pilot rather than a fixed one-shot measurement: the fleet's failure-model parameters should be re-estimated as observations arrive.

**[4]** studies robot fleet learning via policy merging, aggregating parameters of trained policies from distributed, heterogeneous datasets while handling parameterization ambiguity with recurrent neural networks, and introduces the Fleet-Tools benchmark for generalizable tool-use tasks. The fleet-level aggregation problem it addresses — many heterogeneous agents producing data too large to centralize — is structurally the same problem the Quniverse fleet faces when aggregating per-worker failure telemetry into a single reliability model.

**[5]** formulates fleet size and mix vehicle routing with split deliveries and vehicle-commodity incompatibility as modular MIP models, splitting the problem into fleet-design and routing components, and reports on a case study where refrigerated vehicles are more expensive to run than regular vehicles so that chilled and ambient demand are sized separately. Its separation of heterogeneous cost classes within one fleet is the template for our treatment of the fleet's distinct cost lines (gateway spend, per-failure cost, storage), which are budgeted separately rather than folded into one number.

**[6]** introduces FAME, a framework for verifiable AI reliability against silent failures, and reports concrete detection results: in 100 nominal scenarios the monitored DNN performed with $99\%$ reliability and the monitor generated zero false alarms, while in 100 challenging scenarios the DNN failed silently in 31 runs and the FAME monitor detected 29 of the 31 silent failures, a $93.5\%$ detection rate. This is the only source in the bibliography that supplies a measured detection probability for a silent-failure monitor, and Section 4.8 uses $d = 0.935$ from it as the calibration point for the fleet's detection layer, with the transfer to worker-script failures stated as an assumption.

**[7]** addresses the convergence of communication, computing, and control and states that analytical and optimizing frameworks for this convergence are not yet readily developed. Our multiplicative system-reliability composition in Section 4.9 is a deliberately simple first step into that gap, applied to the fleet's three-layer stack, and its limitations are stated where it is used.

**[8]** proposes a two-stage training framework integrating Supervised Fine-Tuning and Direct Preference Optimization for multimodal disaster severity assessment, motivated by the requirement that reliable damage assessment provide both accurate predictions and transparent explanations. Its pairing of an accuracy dimension with an explainability dimension parallels the structure of our composite autonomy score, which combines capability, self-heal, and output-consistency sub-scores; we use an additive weighted form where [8] uses staged training, and the additive-versus-multiplicative choice is left open (Section 6.3).

**[9]** investigates control strategies for autonomous vehicles from theoretical and practical viewpoints, covering longitudinal and lateral control with coupled and de-coupled schemes, and describes the vehicle stack of perception, planning, and control in which the control system generates commands so that the plant tracks a prescribed trajectory. The control-loop view — each cycle drives the plant state back toward a reference — is the analogy behind our treatment of self-healing as a per-failure mitigation applied before failures accumulate.

**[10]** is the retracted predecessor of this paper. Its results table reports $E[F]=1.732$ alongside a conservative alternative $E[F]^{(0.5)}=2.16$, papers per project $9.65$, high-severity gap proportion $11.9\%$, composite scores $4.26$ and $4.66$, projected spends $\$158.66$ and $\$154.33$, and a minimal next experiment that would measure worker-script failures over a 30-day window and verify the billing feed by extracting raw usage in cents. This revision keeps every one of those numbers that its own arithmetic supports, corrects the two confirmed errors identified in the retraction notice, and completes the derivations the retracted version left implicit.

**[11]** audits a quantum-neural-network benchmarking paper and demonstrates claim-integrity auditing under a Phase 1–4 pipeline: it verifies novelty by due diligence over a knowledge graph of 2,168 nodes and 1,462 edges, reconstructs the audited paper's architecture (three hidden layers of 16 qubits, fully separable circuits, 55 test images), and concludes that the multi-platform benchmarking claim is sustained while the advantage claims are not, noting that the joules-per-solution ratio is approximately $10^9$ above the classical break-even point and that the statistical evidence ($N = 55$, overlapping error bars) is insufficient. Its method — parse the claim, reconstruct the asserted relation, recompute, and grade — is the template for the claim-integrity recomputation in Section 3.4.

**[12]** synthesizes the history of computing substrate transitions and identifies an invariant dynamic: constraint saturation, then substrate shift, then Wright's Law cost decline, then institutional adoption, citing the electromechanical era's Harvard Mark I with roughly 3,000 relays failing measurably during operation as a case where reliability, not raw logic, was the binding constraint. Section 4.10 uses this dynamic, clearly labeled as a projection, to ask what happens to the fleet's documented cap if execution volume doubles.

**[13]** adjudicates a five-point critique under a symmetric evidence standard, grading each objection as confirmed, partially confirmed, or unsupported against premises traced to primary texts, and distills a reusable rubric: decompose the claim into premises, verify each premise against a primary source, apply the same standard to both sides, and check the literature the claim ignores. Its four-grade taxonomy is the provenance classification used in Section 3.4, and its central lesson — that a claim is only as good as the verification of its premises — is the reason this revision exists.

Collectively, these works supply the building blocks for an integrated framework addressing reliability, cost, and claim integrity together, and each is used for a specific method or number rather than for general framing.

## 3. Methods

The analytical pipeline consists of four deterministic modules, each expressed in closed form. All calculations are performed symbolically and then evaluated numerically with the input values listed in Section 4. No empirical measurements are introduced by this paper; every count and policy parameter traces to the fleet's documented records as reported in [10], and every assumed value is labeled as an assumption at the point of use.

### 3.1 Failure-Propagation Model

Each of the $N_w$ worker scripts experiences a baseline failure probability $p_f$ per month. A fraction $\alpha$ of failures are resolved automatically (self-heal). The effective unresolved-failure probability is

$$p_{\text{eff}} = p_f \times (1-\alpha).$$

The expected monthly unresolved-failure count is

$$E[F] = N_w \, p_{\text{eff}} = N_w \, p_f \, (1-\alpha).$$

Because the $N_w$ trials are treated as independent Bernoulli trials with common probability $p_{\text{eff}}$, the count $F$ follows a binomial distribution with variance

$$\operatorname{Var}[F] = N_w \, p_{\text{eff}} \, (1 - p_{\text{eff}}).$$

The mitigation factor is derived from recorded action counts. We assume the count-derived form

$$\alpha_{\text{counts}} = \frac{H}{H + X},$$

where $H$ is the recorded number of self-heal actions and $X$ the recorded number of handoff actions. Under this convention, a handoff is counted as a failure not resolved automatically, so $1-\alpha$ is the fraction of mitigation events that required escalation. The retracted version's use of $\alpha = 0.5$ as if it came from these counts is corrected here: $\alpha = 0.5$ is used only as a conservative sensitivity bound, clearly labeled as an assumption.

### 3.2 Resource-Consumption Aggregation

Total storage $S_{\text{tot}}$ is the sum of database and vector-index sizes:

$$S_{\text{tot}} = S_{db} + S_{vi},$$

where $S_{db}=304\ \text{MB}$ (ten D1 databases) and $S_{vi}$ is the product of the vector-index row count and the per-row byte size. MB and MiB are treated as interchangeable at the reported precision (one decimal place); the conversion error is bounded by $5\%$ and is stated as an assumption.

### 3.3 Composite Autonomy Score

A weighted linear model combines three sub-scores:

$$C = w_c S_c + w_{sh} S_{sh} + w_{oc} S_{oc},$$

with weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ taken from the fleet's internal assessment as documented in [10]. Baseline sub-scores are $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$. A $50\%$ reduction in failure probability is modeled as a uniform sub-score increment $\Delta=0.4$, yielding $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$. The increment is a modeling device, not a measured effect; its justification and limits are discussed in Section 6.

### 3.4 Claim-Integrity Recomputation

For each quantitative claim extracted from the retraction notice we follow the audit sequence used in [11] and grade provenance with the taxonomy of [13]: (i) parse the quoted numbers; (ii) reconstruct the asserted arithmetic relation; (iii) recompute the relation step-by-step; (iv) apply unit-dimension checks to monetary feeds (a value quoted in dollars must be traceable to a source quoted in the same unit, and a cents-to-dollars conversion must divide by $100$); and (v) assign a provenance class — confirmed, partially confirmed, or unsupported — following the symmetric evidence standard of [13]. Every ratio reported in Sections 4.7 and 5 names its denominator explicitly, which is the specific correction to the retracted abstract's conflation of the cap-relative and gate-relative figures.

## 4. Analysis

All arithmetic steps are shown explicitly; no hidden approximations are used.

### 4.1 Expected Failures per Month and the Count-Derived Mitigation Factor

Inputs: $N_w=36$ (fleet registry, per [10]), $p_f=0.12$ (assumed per-worker monthly failure probability, carried from [10] and labeled an assumption), $H=1{,}889$ self-heal actions and $X=1{,}264$ handoff actions (documented counts, per [10]).

**Mitigation factor from counts.**

$$N_{\text{total}} = H + X = 1{,}889 + 1{,}264 = 3{,}153,$$

$$\alpha = \frac{1{,}889}{3{,}153} = 0.599114\ldots \approx 0.5991,$$

$$1-\alpha = \frac{1{,}264}{3{,}153} = 0.400886\ldots \approx 0.4009.$$

This corrects the retracted version's attribution of $\alpha = 0.5$ to these counts: the counts give $0.5991$, not $0.5$.

**Effective failure probability.**

$$p_{\text{eff}} = 0.12 \times 0.400886 = 0.0481063.$$

**Expected unresolved failures.**

$$E[F] = 36 \times 0.0481063 = 1.731828 \approx 1.732.$$

**Variance and standard deviation.**

$$\operatorname{Var}[F] = 36 \times 0.0481063 \times (1 - 0.0481063) = 1.731828 \times 0