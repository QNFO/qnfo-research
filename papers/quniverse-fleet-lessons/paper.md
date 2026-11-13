# Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet (Post-Retraction Revision)

## Abstract

Autonomous research fleets must keep serverless worker scripts, databases, and storage buckets operational while publishing cost and performance metrics that external stakeholders can trust. The fleet's own published reliability study was retracted because it presented quantitative claims its derivations did not support, leaving operators without a corrected, recomputable decision framework. This revision rebuilds that framework from the fleet's documented counts and stated policy parameters. It combines a Bernoulli failure-propagation model with a mitigation factor derived from the fleet's recorded action counts, $\alpha = 1{,}889/(1{,}889+1{,}264) \approx 0.5991$, correcting the retracted version's unsupported use of $\alpha = 0.5$; it names the denominator of every billing ratio explicitly; and it recomputes each published claim with shown arithmetic and unit-dimension checks. The model yields an expected $E[F]=1.732$ unresolved worker-script failures per month (standard deviation $\sigma_F \approx 1.284$), a corpus productivity of $9.65$ papers per active project, a high-severity gap proportion of $11.9\%$, a composite autonomy score of $4.26$ rising to $4.66$ when the per-worker failure probability is halved, and projected monthly gateway spend of $\$158.66$ falling to $\$154.33$. A detection layer calibrated to the $93.5\%$ silent-failure detection rate reported for the FAME monitor lowers expected unresolved failures to $0.113$ per month under stated assumptions. The cents-as-dollars billing misread inflates perceived spend to $\$11{,}000$ — $73.3$ times the $\$150$ cap and $122.2$ times the $\$90$ per-30-day gate — while the corrected spend of $\$110$ exceeds that gate by $22.2\%$. Operators, funders, and auditors can use these recomputed levers to size monitoring, budget against the correct units, and enforce claim integrity; the work remains analytical at TRL 2 pending the 30-day measurement pilot specified here.

## 1. Introduction

Platform operators of the Quniverse autonomous research fleet run a continuously active collection of thirty-six serverless worker scripts, ten SQLite databases, eight vector indexes, and nineteen object-storage buckets that generate and publish scientific content without human intervention. Two intertwined problems currently block the fleet's value. First, unplanned downtime arises from script failures and drift between the service registry and the deployed code; failures that escape both the self-healing layer and human notice accumulate silently. Second, self-reported metrics may be unreliable: the fleet's own reliability study was retracted after publication because it presented quantitative claims its derivations did not support, including a mitigation factor attributed to counts it did not come from and a billing comparison that mixed two different denominators. An operator who cannot trust either the failure counts or the dollar figures cannot budget, cannot set alert thresholds, and cannot demonstrate compliance to a funder.

The retraction is itself the strongest evidence that the problem is real. A fleet that publishes a reliability model about itself, and that model then fails its own integrity audit, has demonstrated that claim-integrity checking is not an optional add-on but a load-bearing component of fleet operations. If the corrected framework proposed here holds, three things change: research velocity rises because fewer unresolved failures interrupt pipelines, operational cost falls because failure-driven overruns are bounded against the documented $\$150$ cap and the $\$90$ per-30-day gate, and stakeholder trust is restored because every published number can be recomputed from stated inputs. Conversely, if the reliability model is wrong, a bounded monitoring window will show it, and the operator will have lost only the cost of reading a log file.

This revision corrects two confirmed errors of the retracted version [10]. First, the retracted abstract placed the statement that the misread spend "exceeds the documented $\$90$ per 30 days gate by $22.2\%$" next to a "$73.3\times$ cap violation" without separating the two denominators; the $22.2\%$ figure belongs to the corrected spend of $\$110$ against the $\$90$ gate, while the $73.3$-fold figure belongs to the misread spend of $\$11{,}000$ against the $\$150$ cap. This revision states every ratio with its denominator named explicitly (Sections 4.7 and 5). Second, the retracted text described $\alpha = 0.5$ as if it came from the counts of $1{,}889$ self-heal actions and $1{,}264$ handoff actions; the count-derived factor is $\alpha = 1{,}889/3{,}153 \approx 0.5991$, and $\alpha = 0.5$ is retained only as a clearly labeled conservative assumption for sensitivity bounding (Section 4.1).

**Contributions.**
- **C1.** Derive a Bernoulli failure-propagation model with the count-derived mitigation factor $\alpha = 1{,}889/(1{,}889+1{,}264) \approx 0.5991$ and compute the expected number of unresolved worker-script failures per month, $E[F]=1.732$, with variance $\operatorname{Var}[F]=1.6485$ and standard deviation $\sigma_F \approx 1.284$ (Section 4.1).
- **C2.** Quantify corpus productivity ($9.65$ papers per active project) and the high-severity gap proportion ($11.9\%$) (Sections 4.2–4.3).
- **C3.** Show that halving the per-worker failure probability lowers the expected failure count from $1.732$ to $0.866$ and reduces projected monthly gateway spend from $\$158.66$ to $\$154.33$, while raising the composite autonomy score from $4.26$ to $4.66$ (Sections 4.5–4.6).
- **C4.** Recompute every quantitative claim of the retraction notice with denominators named explicitly, separating the cap-relative ratio ($73.3$-fold), the cap-relative excess ($72.3$-fold), the gate-relative ratio ($122.2$-fold), and the corrected-spend gate exceedance ($22.2\%$) (Sections 4.7–4.9).
- **C5.** Extend the model with a silent-failure detection layer calibrated to the $93.5\%$ detection rate reported for the FAME monitor, lowering expected unresolved failures from $1.732$ to $0.113$ per month under stated assumptions (Section 4.8).
- **C6.** Specify a minimal pilot — a 30-day failure-count measurement and a billing-feed unit-dimension check, with an optional six-month extension — with explicit refutation thresholds (Section 7).

The failure-propagation and claim-audit structure developed here could also transfer to any fleet of autonomous software agents that publishes self-reported reliability and cost figures, and the symmetric evidence standard applied to the retraction notice mirrors adjudication rubrics used to evaluate contested research claims in adjacent domains.

## 2. Background and Related Work

Analytical reliability modeling, fleet-level learning, and claim-integrity auditing provide the methodological foundation of this revision. Each work below is discussed for the specific method or result its text reports.

**[1]** studies the interaction of rainfall-induced landslides and soil erosion as a cascade of interacting processes, and quantifies the interaction stochastically: on 1,000 Monte Carlo simulations of cumulated pre-failure and post-failure soil erosion, the authors estimate a $20\%$ increase in total soil loss, with the post-failure erosion rate on average around $3.5$ times the pre-failure value and a bootstrap analysis over 10,000 runs giving post-failure increases of approximately 1,700 tons per year (bootstrap $p \leq 0.05$). This is a worked example of the pattern this paper needs: a system of interacting processes whose aggregate behavior is quantified by stochastic propagation over a baseline, with uncertainty assessed by resampling. Our Bernoulli propagation over a baseline failure probability follows the same logic at much smaller scale.

**[2]** presents FLEET, a federated learning emulation and evaluation testbed that integrates the Flower federated-learning framework with the Containernet Docker-based network emulator, is configured through TOML files, and exports comprehensive metrics from all components to ZMQ, CSV, or log files. Its design premise — that algorithmic performance is deeply coupled with the operational environment and must be evaluated under realistic conditions — motivates our pilot design: the fleet's failure counts and billing feed must be captured as structured telemetry of the same kind FLEET exports, not as narrative claims.

**[3]** frames reliability qualification of advanced semiconductor devices as a sequential decision problem and presents an adaptive test-planning framework combining Monte Carlo Tree Search with an extended Kalman filter; over 5,000 planning iterations the planner improves characterization yield from $20\%$ to over $54\%$ while keeping damage fractions below $0.57$ in the best successful test sequence. This supports our choice of an adaptive, staged monitoring pilot rather than a fixed one-shot measurement: the fleet's failure-model parameters should be re-estimated as observations arrive.

**[4]** studies robot fleet learning via policy merging, aggregating parameters of trained policies from distributed, heterogeneous datasets while handling parameterization ambiguity with recurrent neural networks, and introduces the Fleet-Tools benchmark for generalizable tool-use tasks. The fleet-level aggregation problem it addresses — many heterogeneous agents producing data too large to centralize — is structurally the same problem the Quniverse fleet faces when aggregating per-worker failure telemetry into a single reliability model.

**[5]** formulates fleet size and mix vehicle routing with split deliveries and vehicle-commodity incompatibility as modular MIP models, splitting the problem into fleet-design and routing components, and reports a case study in which refrigerated vehicles are more expensive to run than regular vehicles so that chilled and ambient demand are sized separately. Its separation of heterogeneous cost classes within one fleet is the template for our treatment of the fleet's distinct cost lines (gateway spend, per-failure cost, storage), which are budgeted separately rather than folded into one number.

**[6]** introduces FAME, a framework for verifiable AI reliability against silent failures, and reports concrete detection results: in 100 nominal scenarios the monitored DNN performed with $99\%$ reliability and the monitor generated zero false alarms, while in 100 challenging scenarios the DNN failed silently in 31 runs and the FAME monitor detected 29 of the 31 silent failures, a $93.5\%$ detection rate. This supplies a measured detection probability for a silent-failure monitor, and Section 4.8 uses $d = 0.935$ from it as the calibration point for the fleet's detection layer, with the transfer to worker-script failures stated as an assumption.

**[7]** addresses the convergence of communication, computing, and control and states that analytical and optimizing frameworks for this convergence are not yet readily developed. Our multiplicative system-reliability composition in Section 4.9 is a deliberately simple first step into that gap, applied to the fleet's three-layer stack, and its limitations are stated where it is used.

**[8]** proposes a two-stage training framework integrating Supervised Fine-Tuning and Direct Preference Optimization for multimodal disaster severity assessment, motivated by the requirement that reliable damage assessment provide both accurate predictions and transparent explanations. Its pairing of an accuracy dimension with an explainability dimension parallels the structure of our composite autonomy score, which combines capability, self-heal, and output-consistency sub-scores; we use an additive weighted form where [8] uses staged training, and the additive-versus-multiplicative choice is left open (Section 6).

**[9]** investigates control strategies for autonomous vehicles from theoretical and practical viewpoints, covering longitudinal and lateral control with coupled and de-coupled schemes, and describes the vehicle stack of perception, planning, and control in which the control system generates commands so that the plant tracks a prescribed trajectory. The control-loop view — each cycle drives the plant state back toward a reference — is the analogy behind our treatment of self-healing as a per-failure mitigation applied before failures accumulate.

**[10]** is the retracted predecessor of this paper. Its results table reports $E[F]=1.732$ alongside a conservative alternative $E[F]^{(0.5)}=2.16$, papers per project $9.65$, high-severity gap proportion $11.9\%$, composite scores $4.26$ and $4.66$, projected spends $\$158.66$ and $\$154.33$, and a minimal next experiment that would measure worker-script failures over a 30-day window and verify the billing feed by extracting raw usage in cents. This revision keeps every one of those numbers that its own arithmetic supports, corrects the two confirmed errors identified in the retraction notice, and completes the derivations the retracted version left implicit.

**[11]** audits a quantum-neural-network benchmarking paper and demonstrates claim-integrity auditing under a Phase 1–4 pipeline: it verifies novelty by due diligence over a knowledge graph of 2,168 nodes and 1,462 edges, reconstructs the audited paper's architecture (three hidden layers of 16 qubits, fully separable circuits, 55 test images), and concludes that the multi-platform benchmarking claim is sustained while the advantage claims are not, noting that the joules-per-solution ratio is approximately $10^9$ above the classical break-even point and that the statistical evidence ($N = 55$, overlapping error bars) is insufficient. Its method — parse the claim, reconstruct the asserted relation, recompute, and grade — is the template for the claim-integrity recomputation in Section 3.4.

**[12]** synthesizes the history of computing substrate transitions and identifies an invariant dynamic: constraint saturation, then substrate shift, then Wright's Law cost decline, then institutional adoption, citing the electromechanical era's Harvard Mark I with roughly 3,000 relays failing measurably during operation as a case where reliability, not raw logic, was the binding constraint. Section 4.10 uses this dynamic, clearly labeled as a projection, to ask what happens to the fleet's documented cap if execution volume doubles.

**[13]** adjudicates a five-point critique under a symmetric evidence standard, grading each objection as confirmed, partially confirmed, or unsupported against premises traced to primary texts, and distills a reusable rubric: decompose the claim into premises, verify each premise against a primary source, apply the same standard to both sides, and check the literature the claim ignores. Its grade taxonomy is the provenance classification used in Section 3.4, and its central lesson — that a claim is only as good as the verification of its premises — is the reason this revision exists.

Collectively, these works supply the building blocks for an integrated framework addressing reliability, cost, and claim integrity together, and each is used for a specific method or number rather than for general framing.

## 3. Methods

The analytical pipeline consists of four deterministic modules, each expressed in closed form. All calculations are performed symbolically and then evaluated numerically with the input values listed in Section 4. This paper introduces no empirical measurements; every count and policy parameter traces to the fleet's documented records as reported in [10], and every assumed value is labeled as an assumption at the point of use.

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

$$\alpha = \frac{1{,}889}{3{,}153} = 0.599112\ldots \approx 0.5991,$$

$$1-\alpha = \frac{1{,}264}{3{,}153} = 0.400888\ldots \approx 0.4009.$$

This corrects the retracted version's attribution of $\alpha = 0.5$ to these counts: the counts give $0.5991$, not $0.5$.

**Effective failure probability.**

$$p_{\text{eff}} = 0.12 \times 0.400888 = 0.0481066.$$

**Expected unresolved failures.**

$$E[F] = 36 \times 0.0481066 = 1.731836 \approx 1.732.$$

**Variance and standard deviation.**

$$\operatorname{Var}[F] = 36 \times 0.0481066 \times (1 - 0.0481066) = 1.731836 \times 0.9518934 = 1.648524,$$

$$\sigma_F = \sqrt{1.648524} = 1.28395 \approx 1.284.$$

**Conservative bound (assumed $\alpha=0.5$).** If $\alpha=0.5$, then $p_{\text{eff}}^{(0.5)} = 0.12 \times 0.5 = 0.06$, $E[F]^{(0.5)} = 36 \times 0.06 = 2.16$, $\operatorname{Var}[F]^{(0.5)} = 36 \times 0.06 \times 0.94 = 2.0304$, and $\sigma_F^{(0.5)} = \sqrt{2.0304} = 1.4249 \approx 1.425$.

**Sensitivity.** $E[F]$ is linear in both $p_f$ and $(1-\alpha)$. Halving $p_f$ to $0.06$ gives $E[F] = 36 \times 0.06 \times 0.400888 = 0.865914 \approx 0.866$. A one-percentage-point change in $p_f$ changes $E[F]$ by $36 \times 0.01 \times 0.400888 = 0.1443$ failures per month. A change $\Delta\alpha$ changes $E[F]$ by $-36 \times 0.12 \, \Delta\alpha = -4.32\,\Delta\alpha$; reverting from $\alpha=0.5991$ to $\alpha=0.5$ ($\Delta\alpha=-0.0991$) raises $E[F]$ by $4.32 \times 0.0991 = 0.428$, matching the difference $2.16 - 1.732 = 0.428$.

### 4.2 Papers per Active Project

Inputs: total papers $P_{\text{total}}=917$, active projects $N_{\text{proj}}=95$ (both per [10]).

$$\frac{P_{\text{total}}}{N_{\text{proj}}}= \frac{917}{95}=9.6526\approx 9.65\ \text{papers/project}.$$

### 4.3 High-Severity Gap Proportion

Inputs: high-severity gaps $G_{\text{high}}=5$, total identified gaps $G_{\text{total}}=42$ (both per [10]).

$$\frac{G_{\text{high}}}{G_{\text{total}}} = \frac{5}{42} = 0.119048\ldots \approx 11.9\%.$$

Five of the forty-two identified gaps are classified as high severity; the proportion is reported with its denominator stated so that it cannot be confused with a share of papers, projects, or failures.

### 4.4 Storage Aggregation

Inputs: $S_{db}=304\ \text{MB}$ (ten D1 databases, per [10]); vector-index rows $34{,}657$ at $512\ \text{B}$ per row (per [10]).

$$S_{vi} = 34{,}657 \times 512\ \text{B} = 17{,}744{,}384\ \text{B}.$$

Converting to MiB ($1\ \text{MiB} = 1{,}048{,}576\ \text{B}$):

$$S_{vi} = \frac{17{,}744{,}384}{1{,}048{,}576} = 16.92236328\ \text{MiB} \approx 16.922\ \text{MiB}.$$

Under the stated MB–MiB interchangeability assumption (bounded by $5\%$ at one decimal place):

$$S_{\text{tot}} = 304 + 16.922 = 320.922 \approx 320.9\ \text{MB}.$$

The interchangeability assumption contributes at most $16.922 \times 0.05 \approx 0.85\ \text{MB}$ of uncertainty to $S_{\text{tot}}$, which is small relative to the $304\ \text{MB}$ database term.

### 4.5 Composite Autonomy Score

Baseline sub-scores $S_c=4.5$, $S_{sh}=4.0$, $S_{oc}=4.2$; weights $w_c=0.4$, $w_{sh}=0.3$, $w_{oc}=0.3$ (per [10]).

$$C_{\text{base}} = 0.4 \times 4.5 + 0.3 \times 4.0 + 0.3 \times 4.2 = 1.80 + 1.20 + 1.26 = 4.26.$$

Improved sub-scores (adding the modeling increment $\Delta=0.4$): $S_c'=4.9$, $S_{sh}'=4.4$, $S_{oc}'=4.6$.

$$C_{\text{new}} = 0.4 \times 4.9 + 0.3 \times 4.4 + 0.3 \times 4.6 = 1.96 + 1.32 + 1.38 = 4.66.$$

$$C_{\text{new}} - C_{\text{base}} = 4.66 - 4.26 = 0.40.$$

The increment equals $\Delta$ exactly because the weights sum to $1$: $\Delta \times (w_c + w_{sh} + w_{oc}) = 0.4 \times 1.0 = 0.40$. The increment is a modeling device, not a measured effect; its justification and limits are discussed in Section 6.

### 4.6 Monthly Gateway Spend Projection

Assumptions: documented cap $S_{\text{cap}}=\$150$ and extra cost per unresolved failure $c_f=\$5$ (both per [10]). The projection is linear in $E[F]$.

**Baseline projection (count-derived $\alpha$).**

$$E_{\text{extra}} = 1.731836 \times 5 = 8.65918,$$ i.e., approximately \$8.66.

$$S_{\text{proj}} = 150 + 8.66 = 158.66,$$ i.e., approximately \$158.66.

**Improved scenario (halved $p_f$, so $E[F]=0.865914$).**

$$E_{\text{extra}}' = 0.865914 \times 5 = 4.32957 \approx \$4.33,$$

$$S_{\text{proj}}' = 150 + 4.33 = \$154.33.$$

For reference, the conservative $\alpha=0.5$ bound would give $E_{\text{extra}} = 2.16 \times 5 = \$10.80$ and $S_{\text{proj}} = \$160.80$; the count-derived factor therefore lowers projected spend by \$10.80 $-$ \$8.66 $=$ \$2.14 relative to that bound. Both projections are labeled as projections: they hold only if p_f, $\alpha$, and $c_f$ remain as stated.

### 4.7 Billing-Unit Misread

Inputs: unit-error factor $f_{\text{unit}}=100$ (cents interpreted as dollars, per [10]); corrected spend $S_{\text{corr}}=\$110$ (per [10]).

$$S_{\text{misread}} = f_{\text{unit}} \times S_{\text{corr}} = 100 \times 110 = 11{,}000,$$ i.e., \$11,000.

The unit-dimension check of Section 3.4 catches this error class: a billing feed quoted in cents must be divided by $100$ before it is compared against a cap or gate quoted in dollars.

### 4.8 Silent-Failure Detection Layer

The retracted model treats every unresolved failure as equally likely to escape notice. [6] reports that the FAME monitor detected 29 of 31 silent failures in 100 challenging scenarios, a $93.5\%$ detection rate, with zero false alarms in 100 nominal scenarios. We take $d = 0.935$ from that result as the calibration point for a detection layer over the fleet's worker scripts, and we state explicitly that the transfer from DNN perception failures to worker-script failures is an assumption; [6] itself notes that cross-domain extension of its design patterns awaits empirical validation.

If a fraction $d$ of otherwise unresolved failures are detected and mitigated, the effective unresolved-failure probability becomes

$$p_{\text{eff}}' = p_{\text{eff}} \times (1 - d).$$

Using the baseline $p_{\text{eff}} = 0.0481066$ (Section 4.1):

$$p_{\text{eff}}' = 0.0481066 \times (1 - 0.935) = 0.0481066 \times 0.065 = 0.00312693,$$

$$E[F]' = N_w \, p_{\text{eff}}' = 36 \times 0.00312693 = 0.112569 \approx 0.113\ \text{failures/month}.$$

The detection layer therefore lowers expected unresolved failures from $1.732$ to $0.113$ per month, a reduction factor of $1/0.065 \approx 15.4$. The variance under the detection layer is

$$\operatorname{Var}[F'] = 36 \times 0.00312693 \times (1 - 0.00312693) = 0.112569 \times 0.996873 = 0.112216,$$

$$\sigma_{F'} = \sqrt{0.112216} = 0.33499 \approx 0.335.$$

No monetary monitoring cost is attached to this layer: [6] reports no cost figure, and we do not invent one. The cost of operating a detection layer is an open input for the pilot of Section 7.

### 4.9 Cap-Violation and Gate Ratios with Denominators Named

Cap $C_{\text{cap}}=\$150$; gate $G_{\text{gate}}=\$90$ per 30 days (both per [10]). Each ratio below names its denominator explicitly, which is the specific correction to the retracted abstract's conflation of the two baselines.

**Cap-relative ratio (misread spend as a multiple of the cap):**

$$\frac{S_{\text{misread}}}{C_{\text{cap}}} = \frac{11{,}000}{150} = 73.333\ldots \approx 73.3\ \text{fold}.$$

**Cap-relative excess (how many times the cap amount is exceeded):**

$$\frac{S_{\text{misread}} - C_{\text{cap}}}{C_{\text{cap}}} = \frac{11{,}000 - 150}{150} = \frac{10{,}850}{150} = 72.333\ldots \approx 72.3\ \text{fold}.$$

**Gate-relative ratio (misread spend as a multiple of the gate):**

$$\frac{S_{\text{misread}}}{G_{\text{gate}}} = \frac{11{,}000}{90} = 122.222\ldots \approx 122.2\ \text{fold}.$$

**Corrected-spend gate exceedance:**

$$\text{Exceedance} = \frac{110 - 90}{90} \times 100 = \frac{20}{90} \times 100 = 22.222\ldots\% \approx 22.2\%.$$

The retracted abstract attached the $22.2\%$ figure to the misread spend; the recomputation shows that $22.2\%$ belongs to the corrected spend of $\$110$ against the $\$90$ gate, while the $73.3$-fold and $122.2$-fold figures belong to the misread spend of $\$11{,}000$ against the cap and gate respectively. The corrected spend of $\$110$ remains below the $\$150$ cap ($110/150 = 0.733$, i.e., $73.3\%$ of the cap) but exceeds the $\$90$ gate by $22.2\%$.

### 4.10 Scaling Projection Under Volume Doubling

[12] identifies a recurring dynamic in computing-substrate transitions — constraint saturation, substrate shift, Wright's Law cost decline, institutional adoption — and documents the electromechanical era's Harvard Mark I, whose roughly 3,000 relays failed measurably during operation, as a case where reliability rather than raw logic was the binding constraint. We use this dynamic, clearly labeled as a projection, to ask what happens to the fleet's documented cap if execution volume doubles. We assume the Wright's Law form that each doubling of volume halves the unit cost of the constrained resource, so the effective cap becomes

$$S_{\text{cap}}' = \frac{150}{2} = \$75.$$

Recomputing the baseline spend with the count-derived $E[F]=1.731836$:

$$S_{\text{proj}}'' = 75 + 1.731836 \times 5 = 75 + 8.66 = \$83.66.$$

Under this projection the projected spend falls below the \$90 gate, eliminating the $22.2\%$ exceedance of Section 4.9. This projection rests on two assumptions beyond the fleet's records: that the Wright's Law cost dynamic applies to serverless gateway pricing, which [12] establishes only for computing-substrate transitions, and that the per-failure cost of \$5 ($c_f$) is volume-invariant. Both are stated as assumptions; neither is derived from fleet data.

## 5. Results

The derivations of Section 4 produce the quantitative outcomes listed below. Every value follows from the arithmetic shown in Section 4; no additional empirical measurements are introduced.

| Result | Value | Derivation | Interpretation |
|--------|-------|------------|----------------|
| **R1. Expected unresolved failures per month** | $E[F]=1.732$ | Section 4.1 | Roughly two unresolved worker-script failures per month after count-derived self-heal mitigation. |
| **R1a. Conservative alternative ($\alpha=0.5$, assumed)** | $E[F]^{(0.5)}=2.16$ | Section 4.1 | The labeled sensitivity bound raises expected failures by $0.428$. |
| **R1b. Failure-count dispersion** | $\operatorname{Var}[F]=1.6485$, $\sigma_F \approx 1.284$ | Section 4.1 | Binomial dispersion under the count-derived $\alpha$. |
| **R2. Papers per active project** | $9.65$ | Section 4.2 | Corpus productivity: $917$ papers across $95$ active projects. |
| **R3. High-severity gap proportion** | $11.9\%$ | Section 4.3 | Five of forty-two identified gaps are high severity. |
| **R4. Total storage** | $320.9\ \text{MB}$ | Section 4.4 | Databases plus vector indexes, under the MB–MiB assumption. |
| **R5. Baseline composite autonomy score** | $C_{\text{base}}=4.26$ | Section 4.5 | Weighted capability, self-heal, and output-consistency sub-scores. |
| **R6. Improved composite autonomy score** | $C_{\text{new}}=4.66$ | Section 4.5 | The modeled halving of $p_f$ raises the score by $0.40$. |
| **R7. Projected monthly gateway spend (baseline)** | $S_{\text{proj}}=\$158.66$ | Section 4.6 | Cap plus expected failure cost, count-derived $\alpha$. |
| **R8. Projected monthly gateway spend (improved)** | $S_{\text{proj}}'=\$154.33$ | Section 4.6 | Halving p_f reduces the failure-cost term to $\$4.33$. |
| **R9. Billing-unit misread spend** | $S_{\text{misread}}=\$11{,}000$ | Section 4.7 | Cents interpreted as dollars inflate the corrected spend by a factor of $100$. |
| **R10. Cap-relative ratio of misread spend** | $73.3$-fold | Section 4.9 | $\$11{,}000$ against the $\$150$ cap. |
| **R10a. Cap-relative excess** | $72.3$-fold | Section 4.9 | The misread spend exceeds the cap by $72.3$ cap amounts. |
| **R10b. Gate-relative ratio of misread spend** | $122.2$-fold | Section 4.9 | $\$11{,}000$ against the $\$90$ per-30-day gate. |
| **R11. Corrected-spend gate exceedance** | $22.2\%$ | Section 4.9 | The corrected $\$110$ exceeds the $\$90$ gate by $22.2\%$; it remains below the $\$150$ cap. |
| **R12. Expected failures with detection layer** | $E[F]'=0.113$, $\sigma_{F'} \approx 0.335$ | Section 4.8 | Calibrated to the $93.5\%$ detection rate of [6]; transfer to worker scripts is an assumption. |
| **R13. Halved-$p_f$ expected failures** | $E[F]=0.866$ | Section 4.1 | Linear sensitivity: halving $p_f$ halves $E[F]$. |
| **R14. Volume-doubling spend projection** | $S_{\text{proj}}''=\$83.66$ | Section 4.10 | Labeled projection under the Wright's Law cap-halving assumption of [12]. |

The headline comparisons are: the misread spend of $\$11{,}000$ is $73.3$ times the $\$150$ cap and $122.2$ times the $\$90$ gate, while the corrected spend of $\$110$ is $73.3\%$ of the cap and exceeds the gate by $22.2\%$; and the detection layer calibrated to [6] lowers expected unresolved failures by a factor of approximately $15.4$, from $1.732$ to $0.113$ per month, under the stated transfer assumption.

## 6. Discussion

### 6.1 What the Corrections Change

The two confirmed errors of the retracted version are not cosmetic. The $\alpha$ correction changes the expected failure count by $0.428$ per month ($2.16$ versus $1.732$), which propagates linearly into the spend projection as a $\$2.14$ difference; an operator sizing alert thresholds at the conservative bound would over-provision monitoring by roughly a quarter of the expected failure load. The denominator correction changes the compliance story qualitatively: under the misread framing the fleet appears to violate its cap by $73.3$ times, an existential figure, whereas the corrected spend of $\$110$ sits $73.3\%$ of the way to the cap and exceeds only the tighter $\$90$ gate, by $22.2\%$. The first framing would justify emergency restructuring; the second justifies a bounded cost-reduction effort. Which decision is correct depends entirely on which denominator is named, which is why Section 3.4 makes denominator naming a mandatory step of the audit sequence.

### 6.2 Limitations

The analysis rests on explicit assumptions, each with a stated sensitivity:

1. **Baseline failure probability $p_f=0.12$** is an assumed value carried from [10], not a measured fleet statistic. $E[F]$ scales linearly in $p_f$: a one-percentage-point change moves $E[F]$ by $0.1443$ failures per month (Section 4.1). The headline $E[F]=1.732$ is therefore only as good as this assumption.
2. **Mitigation factor $\alpha=0.5991$** is derived from recorded counts under the convention that a handoff is a failure not resolved automatically. If handoffs include preventive escalations rather than failed self-heals, $\alpha$ is overestimated and $E[F]$ underestimated; the conservative $\alpha=0.5$ bound raises $E[F]$ by $0.428$ ($24.7\%$ of $1.732$).
3. **Independence of worker failures** is assumed in the binomial variance. Correlated failures (a shared dependency failing across workers) would leave $E[F]$ unchanged under a Poisson-binomial view with common marginal probabilities but would inflate $\sigma_F$ and the tail risk; the model reports no tail quantiles for this reason.
4. **Homogeneous per-worker failure probability** is assumed; heterogeneity across the thirty-six workers would inflate variance relative to $\operatorname{Var}[F]=1.6485$.
5. **Cost per failure of \$5 ($c_f$)** is a documented constant from [10]; downstream costs of an unresolved failure (lost corpus output, manual triage time) are omitted, so projected spend is a lower bound on failure-driven cost.
6. **The cap $S_{\text{cap}}=\$150$ and gate $G_{\text{gate}}=\$90$** are treated as fixed policy parameters; Section 4.10 shows the compliance conclusion reverses if the cap halves under volume growth.
7. **The composite-score increment $\Delta=0.4$** is a modeling device linking a halved $p_f$ to sub-score improvements; no measured dose-response relation supports the magnitude, and the additive weighting ignores interactions between sub-scores.
8. **The detection-layer calibration $d=0.935$** comes from [6]'s DNN perception scenarios; its transfer to worker-script failures is an assumption, and [6] itself marks cross-domain empirical validation as future work.
9. **The MB–MiB interchangeability** in Section 4.4 is bounded at $5\%$ but is a real unit inconsistency of the same family as the billing error the paper criticizes.
10. **The Wright's Law projection of Section 4.10** imports a dynamic that [12] establishes for computing-substrate transitions, not for serverless pricing; it is a labeled projection, not a result.

### 6.3 Falsification

The central reliability claim — that the fleet experiences $E[F]=1.732$ unresolved worker-script failures per month with $\sigma_F \approx 1.284$ — would be falsified if the 30-day pilot specified in Section 7 observed a failure count $F_{\text{obs}}$ lying outside the interval $E[F] \pm 2\sigma_F$, i.e., outside $[1.732 - 2.568,\ 1.732 + 2.568] = [-0.836,\ 4.300]$, truncated at zero to $[0,\ 4.3]$; an observed count of five or more unresolved failures in the window refutes the model at approximately the two-sigma level. The central cost claim would be falsified if the billing feed, extracted in its raw unit and converted with an explicit division by $100$, yielded a corrected monthly spend whose ratio to the raw figure differs from $100$, or if the corrected spend did not land within the $\$90$–$\$150$ band the records support. The detection-layer extension would be falsified if a monitor deployed at the FAME-style specification detected a substantially lower fraction of injected silent failures than $93.5\%$ in the fleet's own environment, which would show the cross-domain transfer assumption fails.

### 6.4 Open Questions

- Does the count-derived $\alpha_{\text{counts}}$ remain stable across months, or does it drift with workload composition? The counts behind $\alpha$ are a single snapshot; no trend data exist.
- How does correlation among worker failures affect the aggregate count and its variance? A shared-dependency failure model would replace the binomial with a compound distribution.
- What is the operating cost of a FAME-style detection layer over serverless scripts? [6] reports detection performance but no cost, and this paper attaches no invented figure.
- Does the additive weighted form of the composite autonomy score, rather than a multiplicative form as in the accuracy-times-explainability pairing discussed in Section 2, change the ranking of improvement scenarios? The choice is left open.
- Can automated unit-dimension verification extend to resource feeds beyond billing (storage, request counts) without manual rule definition?

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended Users and Decision Impact

- **Platform operators** of the fleet use $E[F]=1.732$ and $\sigma_F \approx 1.284$ to size monitoring and set alert thresholds; the decision that changes is the alert threshold on unresolved failures, which should be set against the two-sigma band $[0,\ 4.3]$ rather than against the conservative bound $2.16$ or an unnamed intuition.
- **Funders and auditors** use the corrected spend figures to assess compliance: the decision that changes is whether the fleet is in cap violation (it is not; $\$110$ is $73.3\%$ of the $\$150$ cap) or gate exceedance (it is, by $22.2\%$ of the $\$90$ gate), and whether a published multiplier carries its denominator.
- **Developers of the fleet's self-healing layer** treat the gap between $\alpha=0.5991$ and $\alpha=1$ as the remaining mitigation headroom, and the modeled score improvement from $4.26$ to $4.66$ as a target for a halved failure probability.
- **Publishers of fleet metrics** adopt the audit sequence of Section 3.4 — parse, reconstruct, recompute, unit-check, grade provenance — as a pre-publication gate, so that a retraction of the kind [10] underwent becomes structurally preventable.

### 7.2 Technology Readiness Level

The work is purely analytical and has not been peer reviewed; it therefore resides at **TRL 2** (concept formulation and basic analytical principles). Analytical work never exceeds TRL 3, and no manufacturing or deployment readiness is claimed. The detection-layer extension inherits its calibration from [6]'s proof-of-concept results, which that work reports as a demonstration; the fleet-specific application remains at the analytical stage.

### 7.3 Minimal Next Experiment

A pilot study would:

1. **Measure** the number of worker-script failures over a 30-day window, recording raw failure events, self-heal actions, and handoff actions per worker, so that both $p_f$ and $\alpha$ are re-estimated from data rather than assumed.
2. **Verify** the billing feed by extracting raw usage in cents and converting to dollars with an explicit division by $100$, checking unit-dimension consistency against the $\$150$ cap and $\$90$ gate.
3. **Optionally extend** for six months to test whether $\alpha_{\text{counts}}$ drifts across workload compositions.

Refutation thresholds: if the observed 30-day unresolved-failure count lies outside $[0,\ 4.3]$ (the two-sigma band derived in Section 6.3), the failure model's assumptions are refuted at approximately the two-sigma level; if the billing conversion factor differs from $100$, the unit-dimension model of the misread is refuted. A single 30-day window with thirty-six workers yields at most $36$ Bernoulli trials per month, so the pilot's power to pin down $p_f$ precisely is limited; the six-month extension exists to address this.

### 7.4 Engineering Constraints

- **Logging infrastructure** must capture per-worker failure timestamps and self-heal outcomes with at least minute granularity; without per-worker attribution, the homogeneity assumption of Section 6.2 cannot even be tested.
- **Billing API access** is required to retrieve raw usage in the original monetary unit (cents); the audit of Section 4.7 is impossible against a feed that only exposes post-converted dollars.
- **Configuration control** over the self-healing layer is needed to run the halved-$p_f$ scenario as an intervention rather than an observation.
- **Registry drift** between the declared thirty-six workers and the deployed set would bias $N_w$; the pilot must reconcile the registry against deployed code first.
- **Detection-layer specification** for worker scripts has no existing artifact: [6] provides design patterns for automotive, medical, industrial, and aerospace domains and marks cross-domain empirical validation as future work, so writing the fleet's monitor specification is itself an engineering task before any measurement.

### 7.5 Projected Cost Bounds (Assumptions Stated)

Assuming the documented cap of \$150 ($S_{\text{cap}}$), the per-failure cost of \$5 ($c_f$), and the derived $E[F]$ values of Section 4:

- **Baseline projection:** $S_{\text{proj}} = 150 + 1.732 \times 5 = \$158.66$.
- **Improved projection:** $S_{\text{proj}}' = 150 + 0.866 \times 5 = \$154.33$.
- **Volume-doubling projection (Section 4.10 assumptions):** $S_{\text{proj}}'' = 75 + 1.732 \times 5 = \$83.66$.

These bounds hold only while $p_f$, $\alpha$, and $c_f$ remain as modeled; they are projections, not observations, and they exclude any monitoring-layer operating cost, for which no source supplies a figure.

### 7.6 Risks and Misuse Paths

- **Over-reliance on the model** could lead operators to dismiss anomalies the Bernoulli assumption cannot represent, particularly correlated failures, which the model's variance understates.
- **Misreading the composite autonomy score** as a safety guarantee would obscure the fact that it is a weighted opinion of sub-scores with a modeling increment, not a measured capability.
- **Threshold gaming**: because the refutation band $[0,\ 4.3]$ is published, an operator under pressure could redefine what counts as a "failure" to stay inside it; the pilot's log definition must be fixed before the window opens and held fixed.
- **Unit errors elsewhere**: the same cents-as-dollars failure class could exist in storage or request-count feeds; the audit of Section 3.4 should be applied to every monetary and unit-bearing feed, not only the gateway bill.

## 8. Conclusion

This revision rebuilds the fleet's reliability and cost framework so that every published number is recomputable from stated inputs. The count-derived mitigation factor $\alpha = 1{,}889/3{,}153 \approx 0.5991$ replaces the retracted version's unsupported $\alpha=0.5$, which survives only as a labeled sensitivity bound raising $E[F]$ by $0.428$ to $2.16$. The corrected model yields $E[F]=1.732$ unresolved worker-script failures per month with $\sigma_F \approx 1.284$, a detection layer calibrated to the $93.5\%$ rate reported in [6] lowers this to $0.113$ per month under a stated transfer assumption, and the billing audit separates the misread spend's $73.3$-fold cap ratio and $122.2$-fold gate ratio from the corrected spend's $22.2\%$ gate exceedance. Halving the per-worker failure probability halves $E[F]$ to $0.866$ and lowers projected monthly gateway spend from $\$158.66$ to $\$154.33$, while the modeled composite autonomy score rises from $4.26$ to $4.66$. The work remains analytical at TRL 2; the 30-day measurement pilot with its explicit refutation band $[0,\ 4.3]$ is the smallest step that would confirm or falsify the central claims, and the retraction that motivated this revision is itself the demonstration that the claim-integrity gate it specifies is load-bearing rather than optional.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.55.12). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 16 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Estimating the effects of water-induced shallow landslides on soil erosion. arXiv:1501.05739v1. https://arxiv.org/abs/1501.05739v1
[2] FLEET: A Federated Learning Emulation and Evaluation Testbed for Holistic Research. arXiv:2509.00621v2. https://arxiv.org/abs/2509.00621v2
[3] Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search. arXiv:2608.09622v1. https://arxiv.org/abs/2608.09622v1
[4] Robot Fleet Learning via Policy Merging. arXiv:2310.01362v3. https://arxiv.org/abs/2310.01362v3
[5] Fleet Size and Mix Split-Delivery Vehicle Routing. arXiv:1612.01691v1. https://arxiv.org/abs/1612.01691v1
[6] Taming Silent Failures: A Framework for Verifiable AI Reliability. arXiv:2510.22224v1. https://arxiv.org/abs/2510.22224v1
[7] Modeling the System-Level Reliability towards a Convergence of Communication, Computing and Control. arXiv:2206.11522v1. https://arxiv.org/abs/2206.11522v1
[8] Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning. arXiv:2609.00879v1. https://arxiv.org/abs/2609.00879v1
[9] Control Strategies for Autonomous Vehicles. arXiv:2011.08729v3. https://arxiv.org/abs/2011.08729v3
[10] https://papers.qnfo.org/papers/quniverse-fleet-lessons. QNFO: Quantitative Integrity and Reliability Modeling of the Quniverse Autonomous Research Fleet.
[11] https://papers.qnfo.org/papers/auditing-bqnn. QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage?.
[12] https://papers.qnfo.org/papers/computing-machines. QNFO: Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050.
[13] https://papers.qnfo.org/papers/pqs-critique-adjudication. QNFO: Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis.
