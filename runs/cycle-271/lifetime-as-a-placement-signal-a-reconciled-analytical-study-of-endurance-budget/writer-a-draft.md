# Lifetime as a Placement Signal: A Reconciled Analytical Study of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large language model (LLM) serving accumulates key‑value (KV) cache across many orchestrated requests, and high‑bandwidth flash (HBF) offers an order of magnitude more capacity than high‑bandwidth memory (HBM) at HBM‑class read bandwidth, but its finite write endurance constrains how much write traffic it can absorb. This paper develops an analytical treatment of the lifetime‑aware placement principle underlying Lachesis, a placement layer that assigns KV segments to HBM or HBF by expected lifetime and frees blocks at last read. We formalize the placement decision as a lifetime‑threshold rule, derive the relationship between write‑diversion fraction and achievable lifetime extension, and audit an assumed result set — an extension of $1.19$–$3.13\times$ over HBM‑first placement and $3.3$–$12.2$ device‑years of HBF lifetime, carried as labeled assumptions rather than stated in the supplied abstract of [1] — with fully shown arithmetic. We compute warranty margins of $2.44\times$ and $0.66\times$ against a five‑year warranty, infer an implied HBM‑first baseline lifetime envelope of $1.05$–$10.25$ device‑years, and show that the reported extensions correspond to diverting $15.97\%$–$68.05\%$ of HBF‑bound write traffic. Under a labeled parametric endurance assumption, we further derive annualized HBF write budgets. The analysis clarifies when lifetime‑aware placement suffices, when it fails, and what evidence a production deployment would require.

## 1. Introduction

LLM serving is increasingly dominated by agentic workloads: harnesses orchestrate agents and sub‑agents that accumulate context as KV cache across many requests, consuming substantial memory [1], [2]. High‑bandwidth flash (HBF), an on‑package 3D‑NAND memory class, promises an order‑of‑magnitude greater capacity than HBM at HBM‑class read bandwidth, making it a natural tier for context that exceeds HBM capacity. The obstacle is endurance: flash devices tolerate a finite number of program/erase cycles, so every write sent to HBF consumes a non‑renewable budget.

The insight examined in this paper is that KV cache should be placed across HBM and HBF by its *lifetime* — the interval between a segment’s first write and its last read. Placing shorter‑lived data in HBM lets HBM absorb more of an agent run’s writes and sends fewer of them to HBF. Because the lifetime of KV cache in agentic serving is dictated by the harness — the program that orchestrates the agents — lifetime is, in principle, observable or predictable at write time, not merely inferred from access counters [1].

The contribution of this paper is not a new system but an analytical companion to the Lachesis design [1], [2]. We (i) formalize the placement rule and its three lifetime axes (temporal, structural, inter‑worker), (ii) derive the algebra connecting write diversion, endurance, and device lifetime, and (iii) audit an assumed result set — carried as labeled assumptions because the supplied abstract of [1] states no quantitative results — with explicit arithmetic, converting headline factors into warranty margins, implied baselines, and write‑diversion percentages. Section 6 discusses failure modes and what evidence would falsify the approach.

## 2. Background and Related Work

We review the works supplied in the bibliography, in their exact numbering.

**[1], [2] Lachesis.** The arXiv query entry [1] and its abstract record [2] describe the same system: a lifetime‑aware KV cache placement layer between the agent harness and the serving engine. At write time it places each segment in HBM or HBF according to its lifetime, and frees blocks once the segment is no longer read. The abstract identifies three axes along which lifetime diverges in agentic serving — temporal, structural, and inter‑worker — and notes that HBF offers an order‑of‑magnitude capacity advantage. No quantitative result is given; the extension range $1.19$–$3.13\times$, the lifetime range $3.3$–$12.2$ device‑years, the five‑year warranty, and the 24×7 full‑SLO‑load multi‑agent‑trace condition are therefore treated in this paper as labeled assumptions for the audit, not as reported results of [1].

**[3] Congestion‑aware routing and content placement in elastic cache networks.** This work addresses, for networks with arbitrary topology and congestion‑dependent nonlinear cost functions, the joint determination of cache deployment, content placement, and hop‑by‑hop routing, noting that the optimal tradeoff between routing cost and cache deployment cost remains open. It supplies the general framing that placement is a cost‑coupled optimization, not a local heuristic; our lifetime‑threshold rule is a single‑tier special case of such placement problems.

**[4] PolyKV.** PolyKV lets multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool rather than allocating a separate cache per agent, writing a compressed cache once and injecting it into $N$ independent agent contexts via HuggingFace DynamicCache objects, with keys quantized at int8 ($q8\_0$). PolyKV attacks the *size* of agentic KV state; Lachesis attacks its *placement and wear*. The two are complementary: compression reduces the write volume that reaches any tier, which also stretches HBF endurance, though the supplied entry does not quantify endurance effects.

**[5] HBF for generative recommendation serving.** This work applies HBF to generative recommendation systems that reuse user‑level KV cache to avoid recomputing long user histories, and introduces a write‑aware KV cache policy; the entry notes HBF offers substantially higher capacity than HBM while approaching HBM‑class read bandwidth. It is the closest antecedent in spirit — write‑awareness as a first‑class policy concern on the same device class — though in a recommendation rather than agent‑orchestration context; the supplied summary is truncated before its mechanism, so we attribute no specific policy design to it.

**[6] HBM Is Not All You Need.** This work observes that LLM inference splits into a compute‑bound prefill phase and a memory‑bound decode phase, that disaggregated systems separate them onto distinct hardware, and that datacenter GPUs’ costly HBM bandwidth sits almost entirely idle during prefill; it proposes memory‑heterogeneous accelerators (MemHA) pairing GDDR‑based accelerators for prefill with HBM‑based GPUs for decode. It supports the broader thesis that HBM is a scarce resource to be spent deliberately — the same scarcity logic that motivates spending HBM writes rather than HBF writes in Lachesis. The supplied summary is cut off before quantitative claims, so we cite it only for this framing.

**[7] Hot‑Cold Tiering of HBM and High‑Bandwidth Flash for Agentic LLM Serving.** This work describes agentic serving with multi‑turn sessions that idle between actions yet must retain full context, where limited GPU memory forces eviction of inactive KV states so that resuming a session incurs costly recomputation or slow interconnect transfers, and proposes HBF — described as an on‑package 3D‑NAND memory — for tiering. It establishes the HBM/HBF two‑tier substrate for agentic serving; the supplied entry is truncated and gives no detail on its placement policy or endurance treatment, so we relate it to our argument only through the tiering problem it states.

**[8] Cache‑coloring for non‑volatile caches.** This work studies non‑volatile on‑chip caches such as STT‑RAM, noting their density and low leakage power but limited write endurance, and that existing cache management policies are write‑variation unaware, causing excessive writes to a few blocks. It is the classical precedent for endurance‑aware cache management: the inter‑set write‑variation problem it addresses is the same *wear concentration* phenomenon that lifetime‑aware placement mitigates at the HBM/HBF boundary.

**[9] Locality and Utilization in Placement Suboptimality.** This book chapter constructs mixed‑size placement benchmark sets — including PEKO‑MC, a set of standard examples — targeting the role of non‑local nets and of white space and module‑size variation in suboptimality. Its relevance is methodological: benchmarks constructed to expose specific sources of suboptimality. Our audit of Lachesis against an HBM‑first baseline plays the analogous role for placement policies, though we construct no new benchmark suite.

**[10] Re‑entry dynamics as a switching process.** This entry contrasts the per‑operation switching costs of stored‑program (von Neumann) architectures — instruction fetch, decode, and memory traffic — with a proposed Hamiltonian‑computation paradigm. We invoke it only as a reminder that per‑operation costs (here, per‑write endurance wear) are a general architectural currency; the supplied summary is truncated and supports no further claim.

**[11] QuWARP Reconciled.** This entry notes that classical quantum‑circuit simulation increasingly appears as repeated‑run workloads — variational quantum eigensolver sweeps, noisy multishot studies, and quantum error‑correction cycles — and discusses the QuWARP planner’s workload‑level reuse planning. The analogy is structural: both works treat *reuse across repeated invocations* as a plannable resource, as Lachesis treats harness‑dictated KV lifetime. The entry is truncated and supports no quantitative claim here.

**[12] Thermodynamics of Structural Persistence.** The supplied entry has no abstract text, so no substantive statement about it can be grounded; we note its existence for completeness only.

**[13] LiveBench‑grounded LLM audit.** This entry audits the frontier LLM landscape (August 2026) for mathematics‑heavy scientific research and agentic AI, grounded in the LiveBench 2026‑06‑25 contamination‑free benchmark, finding no Llama model in the top 42 and identifying a mathematics price‑performance leader. We cite it only as evidence that agentic AI is an active evaluation target, motivating serving‑efficiency work; its findings bear no arithmetic on our results.

Collectively, these works establish a landscape in which heterogeneous memory economics [6], [7], write‑endurance management [5], [8], and placement theory [3], [9] intersect, with Lachesis [1], [2] as the specific instance under analysis.

## 3. Methods

### 3.1 System model

A serving engine holds KV cache in two tiers: HBM with capacity $C_{\mathrm{HBM}}$ bytes and effectively unlimited write endurance within a device service life, and HBF with capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$ (the abstract of [1] states an order‑of‑magnitude capacity advantage) and a finite write‑endurance budget of $E_{\mathrm{HBF}}$ program/erase‑equivalent cycles per cell.

A KV *segment* $s$ is the unit of placement. It has a write time $t_w(s)$, a last‑read time $t_r(s)$, and a lifetime
$$
\tau_s = t_r(s) - t_w(s).
$$
The harness dictates $\tau_s$ in agentic serving [1]; Lachesis observes harness behavior along three axes — temporal (when segments die), structural (which segments belong to which agent or sub‑agent), and inter‑worker (how lifetime differs across workers) [1].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. We model the decision as a lifetime‑threshold rule:
$$
p(s) = \begin{cases}
\mathrm{HBM} & \text{if } \tau_s \leq \tau^{*},\\[4pt]
\mathrm{HBF} & \text{if } \tau_s > \tau^{*},
\end{cases}
$$
where $\tau^{*}$ is chosen so that HBM’s capacity and churn constraints are respected. The HBM‑first baseline, by contrast, fills HBM first and spills all overflow writes to HBF regardless of lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window and $W_{\mathrm{tot}}$ the total KV writes. The HBF lifetime in device‑years is
$$
T_{\mathrm{HBF}} = \frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},
$$
where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized HBF write volume. Under the standard assumption that wear is proportional to HBF write volume, a placement policy that extends lifetime by a factor $f$ must reduce HBF write volume by the same factor:
$$
f = \frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}}, \qquad
\phi = 1 - \frac{1}{f},
$$
where $\phi$ is the fraction of baseline HBF‑bound write traffic diverted to HBM (or eliminated by earlier freeing). All derivations below use only numbers stated in [1] and arithmetic shown in Section 4; where an endurance figure is needed that [1] does not supply, we use explicitly labeled illustrative assumptions.

## 4. Analysis

Every input number below is stated with its source. Assumed inputs (labeled assumptions for this audit, not stated in the supplied abstract of [1]): extension factor range $f \in [1.19,\, 3.13]$ and HBF lifetime range $T_{\mathrm{HBF}} \in [3.3,\, 12.2]$ device‑years; warranty duration $5$ years; continuous 24×7 operation.

**(A) Hours in a year and in a warranty period.** Continuous operation gives $24 \times 365 = 8760$ hours per year, and a five‑year warranty spans $5 \times 8760 = 43800$ hours.

**(B) Warranty margins.** The margin against the five‑year warranty is
$$
m = \frac{T_{\mathrm{HBF}}}{5}.
$$
For the upper reported lifetime: $m_{\max} = 12.2 / 5 = 2.44$. For the lower: $m_{\min} = 3.3 / 5 = 0.66$.

**(C) Implied baseline (HBM‑first) lifetimes.** Since $T_{\mathrm{Lach}} = f \cdot T_{\mathrm{base}}$, the baseline lifetime implied by each reported pair is $T_{\mathrm{base}} = T_{\mathrm{Lach}} / f$.
\[
T_{\mathrm{base}}^{(\mathrm{low})} = \frac{3.3}{3.13} = 1.0543127\ldots \approx 1.05\ \text{device‑years},
\]
\[
T_{\mathrm{base}}^{(\mathrm{high})} = \frac{12.2}{1.19} = 10.2521008\ldots \approx 10.25\ \text{device‑years}.
\]

**(D) Geometric‑mean extension.** The geometric mean of the reported extension range is
$$
\bar{f} = \sqrt{1.19 \times 3.13} = \sqrt{3.7247} = 1.92999\ldots \approx 1.93\times.
$$

**(E) Write‑diversion fraction.** Under the proportionality assumption of Section 3.3,
$$
\phi = 1 - \frac{1}{f}.
$$
For $f = 1.19$: $1/1.19 = 0.840336\ldots$, so $\phi = 0.159664\ldots \approx 15.97\%$.  
For $f = 3.13$: $1/3.13 = 0.319490\ldots$, so $\phi = 0.680510\ldots \approx 68.05\%$.

**(F) Annualized write budget (parametric, labeled projection).** The abstract of [1] does not state $E_{\mathrm{HBF}}$ or the absolute write rate. We therefore give a parametric inversion: from $T_{\mathrm{HBF}} = E_{\mathrm{HBF}} / W_{\mathrm{HBF}}^{(\mathrm{yr})}$,
$$
W_{\mathrm{HBF}}^{(\mathrm{yr})} = \frac{E_{\mathrm{HBF}}}{T_{\mathrm{HBF}}}.
$$
*Illustrative assumption (labeled projection):* if $E_{\mathrm{HBF}} = 10^{5}$ cycles, then at $T_{\mathrm{HBF}} = 12.2$ device‑years,
$$
W_{\mathrm{HBF}}^{(\mathrm{yr})} = \frac{10^{5}}{12.2} = 8196.72\ldots \approx 8.20 \times 10^{3}\ \text{writes/year},
$$
which under 24×7 operation is $8196.72 / 8760 = 0.93570\ldots \approx 0.9357$ writes per hour.  
At the low endpoint $T_{\mathrm{HBF}} = 3.3$: $10^{5}/3.3 = 30303.03\ldots \approx 3.03 \times 10^{4}$ writes/year, i.e. $30303.03/8760 = 3.45970\ldots \approx 3.46$ writes/hour.  
If instead $E_{\mathrm{HBF}} = 3 \times 10^{3}$ cycles, the budgets scale down by $0.03$, yielding about $245.90$ and $909.09$ writes/year respectively.

**(G) HBM headroom required.** The diverted traffic of (E) must fit in HBM’s write bandwidth and churn budget. As a fraction of total KV writes $W_{\mathrm{tot}}$, the diverted volume is $\phi \cdot W_{\mathrm{HBF,base}}$; without the ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ — not stated in [1] — we cannot convert this to an absolute HBM load, and we flag this as the principal data gap in the audit.

## 5. Results

We report (i) numbers computed in Section 4 from explicitly labeled assumed inputs, and (ii) no reported results of [1], since the supplied entries state no quantitative results. No simulation or measurement was performed for this paper. Every range cited below — the extension factor $1.19$–$3.13\times$, the lifetime range $3.3$–$12.2$ device‑years, and the warranty condition — is a labeled assumption for this audit, not a stated result of [1].

**Assumed inputs for this audit (not stated in the supplied abstract of [1]):** HBF lifetime extension of $1.19$–$3.13\times$ over HBM‑first placement; HBF lifetime of $3.3$–$12.2$ device‑years; HBF outlasting the five‑year warranty under continuous 24×7 operation at full SLO‑admissible load on the multi‑agent trace.

**Computed here:**

- Warranty margins: $m_{\max}=2.44\times$ and $m_{\min}=0.66\times$ against the five‑year warranty (Section 4B).  
- Implied HBM‑first baseline lifetime envelope: $1.05$–$10.25$ device‑years (Section 4C).  
- Geometric‑mean extension: $\bar{f}\approx1.93\times$ (Section 4D).  
- Write‑diversion fraction implied by the extension range: $\phi\approx15.97\%$ to $68.05\%$ of baseline HBF‑bound writes (Section 4E).  
- Parametric annualized HBF write budgets under the illustrative assumption $E_{\mathrm{HBF}}=10^{5}$ cycles: $8.20\times10^{3}$ writes/year ($0.9357$/hour) at $12.2$ device‑years and $3.03\times10^{4}$ writes/year ($3.46$/hour) at $3.3$ device‑years; scaled by $0.03$ if $E_{\mathrm{HBF}}=3\times10^{3}$ (Section 4F, projections).  
- Continuous‑operation arithmetic: $8760$ hours/year; $43800$ hours in a five‑year warranty (Section 4A).

The headline qualitative result of the audit: the reported extension range is large enough that even its lower endpoint ($1.19\times$, i.e. a $15.97\%$ write diversion) is meaningful, but only the upper portion of the reported lifetime range clears the five‑year warranty with margin, and the $3.3$ device‑year endpoint falls $0.66\times$ short of it.

## 6. Discussion

**Limitations.**  
1. All quantitative grounding comes from a single source, the abstract of [1]; the underlying trace characteristics, per‑trace extension factors, endurance figure, and write‑rate measurements are not supplied, so several of our quantities (the baseline envelope, the diversion fractions) are bounds or envelopes rather than per‑trace values.  
2. The endurance‑to‑lifetime inversion in Section 4F rests on a labeled illustrative endurance assumption and on linear wear accumulation; real flash wear exhibits cell‑to‑cell variation and wear‑leveling effects, and the write‑variation problem documented for non‑volatile caches [8] suggests concentration effects that a uniform‑rate model misses.  
3. The proportionality between lifetime extension and write diversion (Section 3.3) holds only if the policy does not otherwise change read traffic or HBM churn; if lifetime‑aware placement increases HBM eviction and re‑prefill traffic, some diverted writes return indirectly.

**Failure modes.** Lifetime‑aware placement fails when the harness cannot expose or the layer cannot predict segment lifetime: mispredicting a long‑lived segment as short‑lived sends it to HBM (capacity pressure, eviction churn), while mispredicting a short‑lived segment as long‑lived sends it to HBF (wasted endurance, exactly the pathology the policy exists to prevent). It also fails under adversarial or degenerate harnesses in which all segments have similar lifetime, collapsing the temporal axis and reducing the policy to the baseline; the assumed $1.19\times$ lower endpoint may reflect precisely such a trace, though no supplied source says so. Finally, the warranty result is trace‑specific: our computed $m_{\min}=0.66$ shows that at least one evaluated configuration does *not* clear five years, so “outlasts the warranty” cannot be generalized across workloads.

**What would falsify the claims.** The central claim — that lifetime‑aware placement materially extends HBF life — would be falsified if per‑trace data showed the extension factors to be artifacts of baseline pathology (e.g., an HBM‑first baseline that spills gratuitously), if measured HBF wear under Lachesis did not scale with the computed diversion fractions $\phi$, or if harness‑predicted lifetimes proved no better than access‑frequency heuristics at comparable cost. The warranty claim would be falsified by any workload class where the implied baseline envelope’s low end ($1.05$ device‑years) is typical and the extension stays near $1.19\times$, yielding roughly $1.05\times1.19\approx1.25$ device‑years — far below warranty.

**Open questions.**  
- How does joint optimization with compression (e.g., PolyKV [4]) affect the write volume that reaches HBF?  
- How should $\tau^{*}$ adapt online when harness behavior shifts along the inter‑worker axis [1]?  
- Can the placement‑suboptimality benchmark methodology of [9] be adapted to build standard traces that isolate each lifetime axis, so that extension factors become comparable across systems?  
- Can placement be co‑optimized with prefill/ decode disaggregation across memory‑heterogeneous hardware [6], in the spirit of the joint routing‑placement formulations of [3]?

## 7. Practical Implications and Engineering Pathways

**Who could use this and for what decision.** The primary users are (i) serving‑infrastructure teams deciding whether to provision an HBF tier alongside HBM for agentic workloads, and (ii) agent‑harness developers deciding whether to expose lifetime metadata (segment creation, expected last read, agent/sub‑agent identity) to the serving layer. The audit’s computed quantities translate directly into provisioning decisions: the warranty margin $m = T_{\mathrm{HBF}}/5$ (Section 4B) tells an operator whether a given workload’s HBF write volume clears a five‑year device‑replacement horizon, and the write‑diversion fraction $\phi = 1 - 1/f$ (Section 4E) tells them how much additional HBM write bandwidth and churn headroom the lifetime‑aware policy must absorb — between $15.97\%$ and $68.05\%$ of baseline HBF‑bound writes under the linear‑wear model of Section 3.3. A harness team that can demonstrate its traces sit near the favorable end of the extension range (near $3.13\times$) has a quantified argument for the HBF tier; one whose traces sit near the $1.19\times$ endpoint, with the implied baseline low end of $1.05$ device‑years, faces a projected worst case of $1.05 \times 1.19 \approx 1.25$ device‑years (Section 6), which does not clear warranty and would argue for compression (e.g., the shared compressed pools of PolyKV [4]) or workload reshaping before adding flash.

**How it would be built.** The placement layer sits between the harness and the serving engine, as described for Lachesis [1], [2]. The engineering pathway has three components:

1. *Lifetime instrumentation in the harness.* The harness already dictates segment lifetime along the temporal, structural, and inter‑worker axes [1]; exposing $\tau_s$ (or a predictor of it) at write time requires hooking segment‑creation and agent‑teardown events and emitting a lifetime annotation with each KV write. This is a software change to the orchestration layer, not to the model or the accelerator.  
2. *A threshold‑based placer.* The rule of Section 3.2 — place in HBM if $\tau_s \leq \tau^{*}$, else HBF, with free‑at‑last‑read block release — is implementable as a small policy module in the serving engine’s allocator. The threshold $\tau^{*}$ must be tuned against two constraints: HBM capacity $C_{\mathrm{HBM}}$ and the HBM churn budget that absorbs the diverted fraction $\phi$ of writes (Section 4G identifies the missing ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ as the quantity an operator must measure to size this headroom).  
3. *Endurance telemetry.* Because the lifetime‑to‑lifetime inversion $W_{\mathrm{HBF}}^{(\mathrm{yr})}=E_{\mathrm{HBF}}/T_{\mathrm{HBF}}$ (Section 4F) is linear only under uniform wear, a deployment needs per‑block write counters and wear‑leveling feedback, in the spirit of the write‑variation mitigation that cache‑coloring provides for non‑volatile caches [8]. Without such telemetry, the computed device‑year figures are envelopes, not guarantees.

**Adoption path.** A plausible sequence is: (a) replay recorded agent traces through a simulator implementing the threshold rule, reproducing the audit’s quantities ($f$, $T_{\mathrm{HBF}}$, $\phi$) per trace rather than as ranges; (b) shadow‑deploy the placer on a live serving cluster with lifetime annotations from a cooperative harness, comparing measured HBF write volume against the simulated prediction; (c) only then make procurement or warranty‑horizon decisions based on measured, not projected, $W_{\mathrm{HBF}}^{(\mathrm{yr})}$. Standardized traces that isolate each lifetime axis — analogous in purpose to the suboptimality‑isolating benchmark methodology of [9] — would make extension factors comparable across systems and vendors.

**What stands between the result and real use.**  
1. *Evidence maturity*: the extension, lifetime, warranty, and load figures used in this audit are labeled assumptions, not statements of the supplied abstract of [1]; the endurance figure $E_{\mathrm{HBF}}$ and absolute write rates are likewise not supplied, so any deployment sizing today rests on the labeled parametric assumptions of Section 4F.  
2. *Harness cooperation*: the approach requires the harness to expose or make predictable segment lifetime; harnesses that cannot do so reduce the policy to the HBM‑first baseline (Section 6).  
3. *HBF hardware availability and its actual endurance specification*: the device‑level parameter $E_{\mathrm{HBF}}$ must come from the memory vendor’s specification, and the write budgets computed in Section 4F scale linearly with it (a factor of $0.03$ between the two illustrative values $3\times10^{3}$ and $10^{5}$ cycles).  
4. *HBM headroom*: the diverted writes must fit within HBM’s spare write bandwidth and capacity without degrading SLOs; this is measurable but not yet quantified by any supplied source.

**Smallest concrete next test.** The minimal experiment is a trace‑replay study on a single recorded multi‑agent session: instrument the harness to record $(t_w(s), t_r(s))$ for every KV segment, run both the HBM‑first baseline and the threshold rule with a swept $\tau^{*}$, and measure the achieved ratio $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}/W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ against the predicted diversion $\phi = 1 - 1/f$. If the measured write reduction matches the linear prediction at the swept thresholds, the core proportionality assumption of Section 3.3 is validated on real traces, and the audit’s arithmetic becomes a usable sizing tool; if it diverges — for example because HBM eviction forces re‑writes of diverted segments — the discrepancy itself quantifies the HBM‑churn penalty that Section 4G flags as the principal data gap.

**Technology readiness.** The analytical nature of this work places it at TRL 2 (conceptual analysis) according to NASA definitions; no hardware or prototype has been built, and the method does not exceed TRL 3.

## 8. Conclusion

We presented an analytical audit of lifetime‑aware KV cache placement across HBM and high‑bandwidth flash for agentic LLM serving. Formalizing the Lachesis placement principle [1] as a lifetime‑threshold rule with free‑at‑last‑read semantics, we derived the algebra linking write diversion to endurance lifetime and computed, with fully shown arithmetic, that the assumed $1.19$–$3.13\times$ extension corresponds to diverting $15.97\%$–$68.05\%$ of HBF‑bound writes, that the assumed $3.