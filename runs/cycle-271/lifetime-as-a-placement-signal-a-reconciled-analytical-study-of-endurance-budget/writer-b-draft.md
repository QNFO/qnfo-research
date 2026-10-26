# Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large language model (LLM) serving accumulates key-value (KV) cache across many orchestrated requests, and high-bandwidth flash (HBF) offers an order of magnitude more capacity than high-bandwidth memory (HBM) at HBM-class read bandwidth, but its finite write endurance limits how much write traffic it can absorb. Lachesis addresses this by placing KV segments in HBM or HBF according to their lifetime and reports a 1.19–3.13$\times$ HBF lifetime extension over HBM-first placement, reaching 3.3–12.2 device-years against a five-year warranty. What the reported headline numbers do not yet give is the arithmetic that connects them to deployable quantities: warranty margins, implied baselines, write-diversion fractions, and annualized write budgets. This paper derives that connection. We formalize placement as a lifetime-threshold rule, show that the reported extensions imply diverting 15.97%–68.05% of HBF-bound writes back to HBM, compute warranty margins of 0.66$\times$–2.44$\times$, derive an implied HBM-first baseline envelope of 1.05–10.25 device-years that is consistent with the per-configuration baselines independently reported in [1], and, grounding endurance in the $10^{5}$ program/erase cycles that [7] rates for HBF, obtain annual per-cell write budgets of $8.20\times 10^{3}$ to $3.03\times 10^{4}$ (about 0.94–3.46 writes per cell per hour under continuous operation). The results turn lifetime-aware placement from a headline claim into a sizing tool, and identify the per-trace pairing and wear-telemetry evidence a production deployment would still need.

## 1. Introduction

Operators of LLM serving infrastructure face a capacity endgame that is driven by who their users have become. Agentic workloads — harnesses orchestrating agents and sub-agents across many requests — accumulate KV cache over entire sessions instead of resetting per query, and multi-turn sessions idle between tool calls and user input while still needing their full context retained [1], [7]. Limited GPU memory forces eviction of inactive KV states, so resuming a session costs either recomputation or slow interconnect transfers [7]. HBF, an on-package 3D-NAND memory class, offers an order of magnitude more capacity than HBM at HBM-class read bandwidth and is the natural tier for this retained context [1], [7]. The obstacle is endurance: flash tolerates a finite number of program/erase (P/E) cycles, so every write sent to HBF spends a non-renewable budget, and a policy that writes the wrong things to HBF can wear the device out within a warranty period.

The cost of getting placement wrong is concrete. Under a conventional LRU policy on the same device class, HBF lifetime collapses to roughly one year, because cache misses decouple badly from writes; an admission-controlled variant extends it to over six years [5]. Lachesis attacks the same problem from the placement side: because the harness — the program that orchestrates the agents — dictates KV lifetime, lifetime is observable or predictable at write time, and segments can be routed to HBM or HBF accordingly [1]. Lachesis reports extending HBF lifetime by 1.19–3.13$\times$ over HBM-first placement, reaching 3.3–12.2 device-years, with HBF outlasting its five-year warranty under continuous 24x7 operation at full SLO-admissible load on the multi-agent trace [1].

What changes if the analysis in this paper holds is the decision an operator can make. A team deciding whether to provision an HBF tier, and how many of a GPU's memory stacks to allocate to each tier, currently has only headline extension factors. This paper converts those factors into the quantities a provisioning decision needs: how much write traffic must move back to HBM (15.97%–68.05%), whether the resulting device lifetime clears a five-year warranty and by how much (0.66$\times$–2.44$\times$), what baseline the comparison presumes (1.05–10.25 device-years implied; 1.9–4.8 reported per configuration in [1]), and how many writes per cell per year the endurance budget sustains (about $8.2\times 10^{3}$ to $3.0\times 10^{4}$, grounded in the $10^{5}$ P/E cycle rating that [7] gives for HBF). If the derivations are sound, lifetime becomes a quantitative sizing signal rather than a qualitative slogan; if they break — for example, if measured wear does not track the computed diversion fractions — the provisioning argument collapses, and Section 6 states exactly which observation would show that.

The contribution is analytical, not a new system. Specifically, this paper:

- Formalizes the Lachesis placement principle [1] as a lifetime-threshold rule with free-at-last-read semantics, and states the algebra linking lifetime extension, write diversion, and device lifetime (Sections 3 and 4).
- Derives, with fully shown arithmetic, the warranty margins (0.66$\times$–2.44$\times$), the implied HBM-first baseline envelope (1.05–10.25 device-years), the write-diversion fractions (15.97%–68.05%), and the endurance-grounded annual write budgets (Section 4), and cross-checks the implied baselines against the per-configuration numbers reported in [1] (Section 4C).
- Positions the result against the adjacent literature on endurance-aware caching [8], write-aware HBF policies [5], hot-cold HBF tiering [7], compressed shared KV pools [4], memory-heterogeneous serving [6], and placement theory [3], [9] (Section 2), and against the prior assumptions-only audit of the same system [10].
- States the failure modes, the falsifying observations, and the smallest experiment that would de-risk or refute the core proportionality assumption (Sections 6 and 7).

## 2. Background and Related Work

This section reviews the works the paper builds on, in their bibliography numbering, and states for each the specific point its text establishes.

**[1], [2] Lachesis.** Lachesis is a lifetime-aware KV cache placement layer between the agent harness and the serving engine: at write time it places each segment in HBM or HBF according to its lifetime, and frees its blocks once the segment is no longer read [1]. The harness dictates KV lifetime in agentic serving, and [1] identifies three axes along which lifetime diverges — temporal, structural, and inter-worker. Quantitatively, [1] reports that in trace-driven simulation Lachesis extends HBF lifetime by 1.19–3.13$\times$ over HBM-first placement, reaching 3.3–12.2 device-years, and that even under continuous 24x7 operation at the full load a tight SLO admits, HBF outlasts its five-year warranty on the multi-agent trace. The evaluation text of [1] adds the configuration detail this audit uses: four GPU-memory configurations split eight memory stacks as 1/7, 2/6, 3/5 and 4/4 between HBM and HBF, with a fifth configuration (8/8*) using H3's daisy chain; the two tiers have the same read bandwidth and differ only in write bandwidth; and at the four split configurations Lachesis reaches 3.3–9.3 device-years against HBM-first's 1.9–4.8, with extensions of 1.50–2.95$\times$ at a tight SLO (60 ms 99th-percentile time per output token) and 1.19–1.89$\times$ at a loose one (100 ms). This paper takes [1] as its object of study and derives the deployable quantities its headline numbers imply.

**[3] Congestion-aware routing and content placement in elastic cache networks.** For networks with arbitrary topology and congestion-dependent nonlinear cost functions, [3] jointly determines cache deployment, content placement, and hop-by-hop routing, framing the tradeoff between routing cost and cache deployment cost as an open optimization problem; its evaluation shows that joint optimization beats heuristic utility-based deployment, with a total cost up to 30% lower than the second-best algorithm. The relevance is structural: placement is a cost-coupled optimization, and the lifetime-threshold rule audited here is a single-tier, two-level special case of the general placement problem [3] formalizes.

**[4] PolyKV.** PolyKV lets multiple concurrent inference agents share a single, asymmetrically compressed KV pool rather than one cache per agent, writing the compressed cache once and injecting it into $N$ agent contexts via HuggingFace DynamicCache objects, with keys quantized at int8 ($q8\_0$) [4]. Its measured results are specific: a stable 2.91$\times$ compression ratio across model architectures including GQA, a reduction of KV memory from 19.8 GB to 0.45 GB (97.7%) at 15 agents sharing a 4K context on Llama-3-8B with +0.57% PPL degradation, and PPL deltas invariant to agent count. PolyKV attacks the size of agentic KV state; Lachesis attacks its placement and wear. The two compound: compression shrinks the write volume reaching any tier before placement decisions are made, and Section 4H computes the compounded effect under a stated independence assumption.

**[5] HBF for generative recommendation serving.** This work applies HBF to generative recommendation systems that reuse user-level KV cache to avoid recomputing long user histories, and is, to our knowledge, the closest antecedent in treating write-awareness as a first-class policy concern on the same device class [5]. Its conclusion is quantitative: conventional LRU can quickly exhaust HBF write endurance, while an admission-controlled LRU-$K$ policy that decouples writes from cache misses extends HBF lifetime from about one year with LRU-1 to over six years with LRU-10, and HBF-based systems achieve 3.8–4.7$\times$ higher throughput than HBM-only. This gives an independent, same-device-class data point that policy choices move HBF lifetime by large factors, against which Lachesis's 1.19–3.13$\times$ placement gain can be calibrated (Section 4H).

**[6] HBM Is Not All You Need.** This work observes that LLM inference splits into a compute-bound prefill phase and a memory-bound decode phase, that disaggregated systems separate them onto distinct hardware, and that datacenter GPUs' costly HBM bandwidth sits almost entirely idle during prefill; it proposes memory-heterogeneous accelerators (MemHA) pairing GDDR-based accelerators for prefill with HBM-based GPUs for decode, and reports up to 3.2$\times$ higher goodput and 4.8$\times$ higher goodput-per-dollar than homogeneous A100 disaggregation on real silicon [6]. It supports the broader thesis that HBM is a scarce resource to be spent deliberately — the same scarcity logic that underlies spending HBM writes rather than HBF writes in lifetime-aware placement. Its evaluation context (decode nodes in disaggregated deployments) is also the context in which [1] evaluates Lachesis.

**[7] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving.** This work states the agentic serving problem this paper addresses: multi-turn sessions idle between actions yet must retain full context, limited GPU memory forces eviction of inactive KV states, and resuming a session incurs costly recomputation or slow interconnect transfers [7]. Its evaluation provides the device-level grounding this audit needs: the modeled HBF tier is 3 TiB SLC with bandwidth matching HBM, rated at 100,000 program/erase cycles with 25 $\mu$s read access latency; because KV is immutable and appended in erase-block-aligned units, the write amplification factor (WAF) stays near unity ($\approx 1.02$), compared to 2–4 for a general-purpose SSD. It also reports that hot-cold tiering supports an order of magnitude more concurrent sessions per GPU and cuts memory-read power by about 7.6 kW per 8-GPU node versus an all-KV-to-flash design. The $10^{5}$-cycle rating and the WAF figure from [7] are what let Section 4F turn Lachesis's device-year lifetimes into concrete annual write budgets instead of parametric placeholders.

**[8] Cache-coloring for non-volatile caches.** This work studies non-volatile on-chip caches such as STT-RAM, noting their density and low leakage power but limited write endurance, and that existing cache management policies are write-variation unaware, causing excessive writes to a few blocks [8]. Its technique, cache-coloring, mitigates inter-set write variation, and its evaluation reports an average 4.20$\times$ improvement in cache lifetime at an average performance factor of 0.96$\times$, a 9.42% energy increase, and an MPKI increase of 0.85. This is the classical precedent for endurance-aware cache management, and its 4.20$\times$ lifetime gain from purely remapping writes is a calibration point for what write-placement alone can achieve (Section 4H). Its raw-lifetime metric — the inverse of the maximum writes on any block — also motivates the wear-concentration caveat in Section 6.

**[9] Locality and Utilization in Placement Suboptimality.** This book chapter constructs mixed-size placement benchmark sets, including PEKO-MC, targeting the role of nonlocal nets, white space, and module-size variation in suboptimality [9]. Its relevance is methodological: benchmarks built to expose specific sources of suboptimality. An analogous methodology — traces built to isolate each lifetime axis of [1] — is what would make extension factors comparable across placement systems, and Section 7 proposes it as the standardization step.

**[10] Prior assumptions-only audit of the same system.** The prior analytical study of Lachesis formalized the same placement principle and derived warranty margins, an implied baseline envelope, and write-diversion fractions, but treated the extension range 1.19–3.13$\times$ and the lifetime range 3.3–12.2 device-years as labeled assumptions, reporting "no reported results of [1], since the supplied entries state no quantitative results," and flagged the linear-wear and HBM-churn limitations that Section 6 of this paper carries forward [10]. This paper supersedes that posture on one point: the evaluation text of [1] does report per-configuration numbers (3.3–9.3 versus 1.9–4.8 device-years; 1.50–2.95$\times$ and 1.19–1.89$\times$), which allows the cross-check in Section 4C that [10] could not perform, and the device rating reported in [7] replaces [10]'s illustrative endurance assumption with a cited value.

Collectively, these works establish a landscape in which heterogeneous memory economics [6], [7], write-endurance management [5], [8], compressed KV state [4], and placement theory [3], [9] intersect, with Lachesis [1], [2] as the specific instance this paper audits and [10] as its direct analytical predecessor.

## 3. Methods

### 3.1 System model

A serving engine holds KV cache in two tiers: HBM with capacity $C_{\mathrm{HBM}}$ bytes and effectively unlimited write endurance within a device service life, and HBF with capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$ — [1] states an order-of-magnitude capacity advantage — and a finite write-endurance budget of $E_{\mathrm{HBF}}$ program/erase cycles per cell. For the numerical work in Section 4F we adopt the HBF device rating reported in [7]: $E_{\mathrm{HBF}} = 10^{5}$ P/E cycles for SLC HBF, with a write amplification factor near unity, $\mathrm{WAF} \approx 1.02$, because KV is immutable and appended in erase-block-aligned units [7].

A KV segment $s$ is the unit of placement. It has a write time $t_w(s)$, a last-read time $t_r(s)$, and a lifetime

$$\tau_s = t_r(s) - t_w(s).$$

In agentic serving the harness dictates $\tau_s$ [1]; Lachesis observes harness behavior along the temporal, structural, and inter-worker axes [1].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. We model the decision as a lifetime-threshold rule:

$$p(s) = \begin{cases} \mathrm{HBM} & \text{if } \tau_s \leq \tau^{*}, \\ \mathrm{HBF} & \text{if } \tau_s > \tau^{*}, \end{cases}$$

where $\tau^{*}$ is chosen so that HBM capacity and churn constraints hold. The HBM-first baseline fills HBM first and spills all overflow writes to HBF regardless of lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window and $W_{\mathrm{tot}}$ the total KV writes. HBF lifetime in device-years is

$$T_{\mathrm{HBF}} = \frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},$$

where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized HBF write volume per cell-equivalent. Under the standard assumption that wear is proportional to HBF write volume, a policy that extends lifetime by a factor $f$ must reduce HBF write volume by the same factor:

$$f = \frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}}, \qquad \phi = 1 - \frac{1}{f},$$

where $\phi$ is the fraction of baseline HBF-bound write traffic diverted to HBM (or eliminated by earlier freeing). All inputs are either reported by [1] or [7] with the citation stated at each use, or labeled as this paper's assumptions; every derivation in Section 4 shows its arithmetic.

### 3.4 What this paper does not do

This paper performs no simulation, measurement, or trace collection. All quantitative claims are either (i) reported results of cited works, attributed by number, or (ii) derived here from those reported results by the algebra of Section 3.3, with each derivation's arithmetic shown in Section 4. Where a needed input is absent from every cited source, the derivation is either left parametric or dropped, and the gap is named.

## 4. Analysis

Every input below is stated with its source. Inputs from [1]: extension factor range $f \in [1.19,\, 3.13]$; Lachesis lifetime range $T_{\mathrm{HBF}} \in [3.3,\, 12.2]$ device-years; per-configuration (four split configurations) Lachesis lifetimes 3.3–9.3 device-years and HBM-first lifetimes 1.9–4.8 device-years; tight-SLO extensions 1.50–2.95$\times$; loose-SLO extensions 1.19–1.89$\times$; five-year warranty; continuous 24x7 operation at full SLO-admissible load on the multi-agent trace. Inputs from [7]: $E_{\mathrm{HBF}} = 10^{5}$ P/E cycles; $\mathrm{WAF} \approx 1.02$. The only assumption used repeatedly is the linear-wear proportionality of Section 3.3, stated there and carried as a limitation in Section 6.

**(A) Hours in a year and in a warranty period.** Continuous operation gives $24 \times 365 = 8760$ hours per year, and a five-year warranty spans $5 \times 8760 = 43800$ hours.

**(B) Warranty margins.** The margin against the five-year warranty is $m = T_{\mathrm{HBF}}/5$.

- Upper reported lifetime: $m_{\max} = 12.2/5 = 2.44$.
- Lower reported lifetime: $m_{\min} = 3.3/5 = 0.66$.
- Four-configuration Lachesis range: $9.3/5 = 1.86$ and $3.3/5 = 0.66$.
- Four-configuration HBM-first range: $4.8/5 = 0.96$ and $1.9/5 = 0.38$.

The full text of [1] states that at a tight SLO, HBF outlasts the five-year warranty under Lachesis at every GPU-memory configuration and on both models, and under HBM-first placement only with Qwen3-235B-A22B on H3's daisy chain. The computed margins are consistent with that statement only if the 3.3 device-year lower endpoint arises at the loose SLO or from a configuration outside the tight-SLO warranty claim; the per-configuration pairing that would settle this is not stated in [1], and we flag it as an open item rather than resolving it by assumption.

**(C) Implied baselines and cross-check against reported per-configuration baselines.** Since $T_{\mathrm{Lach}} = f \cdot T_{\mathrm{base}}$, each reported pair implies $T_{\mathrm{base}} = T_{\mathrm{Lach}}/f$. Taking the abstract-level endpoints:

$$T_{\mathrm{base}}^{(\mathrm{low})} = \frac{3.3}{3.13} = 1.05431\ldots \approx 1.05 \text{ device-years},$$

$$T_{\mathrm{base}}^{(\mathrm{high})} = \frac{12.2}{1.19} = 10.25210\ldots \approx 10.25 \text{ device-years}.$$

(Computations: $3.3/3.13 = 1.0543127\ldots$; $12.2/1.19 = 10.2521008\ldots$.) This envelope is a bound across configurations, not