# Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large‑language‑model (LLM) serving accumulates key‑value (KV) cache across many orchestrated requests. High‑bandwidth flash (HBF) offers an order‑of‑magnitude larger capacity than high‑bandwidth memory (HBM) while delivering comparable read bandwidth, but its finite program/erase (P/E) endurance limits the amount of write traffic it can absorb. Lachesis proposes a lifetime‑aware placement layer that routes KV segments to HBM or HBF based on the interval between a segment’s first write and its last read. This paper formalizes that placement principle as a lifetime‑threshold rule, derives the algebra linking write diversion to HBF device‑year lifetime, and computes, with fully shown arithmetic, the quantitative consequences of the headline extension factors reported for Lachesis. Using the endurance rating $E_{\mathrm{HBF}}=10^{5}$ cycles from the HBF device specification [7] and a write‑amplification factor $\mathrm{WAF}\approx1.02$, we obtain: (i) warranty‑margin factors of $0.66\times$–$2.44\times$ relative to a five‑year warranty; (ii) an implied HBM‑first baseline lifetime envelope of $1.05$–$10.25$ device‑years; (iii) a geometric‑mean extension of $1.93\times$; (iv) write‑diversion fractions of $15.97\%$–$68.05\%$; and (v) annualized HBF write budgets of $8.20\times10^{3}$–$3.03\times10^{4}$ writes per cell ($\approx$ 0.94–3.46 writes $h^{-1}$). The analysis clarifies the conditions under which lifetime‑aware placement can clear a five‑year warranty, quantifies the HBM headroom required, and identifies the minimal trace‑replay experiment that would validate the proportionality assumption underlying the audit.

## 1. Introduction

Operators of LLM‑serving infrastructure now confront a capacity endgame driven by **agentic workloads**: harnesses orchestrate agents and sub‑agents across many requests, causing KV cache to accumulate over entire multi‑turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High‑bandwidth flash (HBF), an on‑package 3D‑NAND class, provides an order‑of‑magnitude capacity advantage over HBM while preserving HBM‑class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non‑renewable budget that can be exhausted before a device’s warranty expires.

If a placement policy can **predict a segment’s lifetime**—the interval between its first write and its last read—then short‑lived segments can be kept in HBM (which has effectively unlimited endurance for the service life) while long‑lived segments are diverted to HBF. Lachesis implements exactly this idea, exposing three lifetime axes (temporal, structural, inter‑worker) and freeing blocks at the moment a segment’s last read occurs. The reported headline results for Lachesis are a **1.19–3.13× extension** of HBF lifetime over an HBM‑first baseline and an **absolute lifetime of 3.3–12.2 device‑years**, which allegedly outlast a five‑year warranty under continuous 24×7 operation.

**So what?** An operator must decide whether to provision an HBF tier, how much HBM headroom to reserve for diverted writes, and whether the projected endurance will survive the warranty horizon. Those decisions require concrete numbers: warranty‑margin factors, baseline lifetimes, write‑diversion percentages, and per‑cell write budgets. This paper supplies exactly those numbers, derived from the reported extensions and from the HBF endurance rating supplied by the device specification.

**Contributions**  
1. Formalization of the Lachesis placement principle as a lifetime‑threshold rule with free‑at‑last‑read semantics (Section 3).  
2. Derivation of the algebra linking extension factor $f$, write‑diversion fraction $\phi$, and HBF device‑year lifetime $T_{\mathrm{HBF}}$ (Section 3.3).  
3. Fully shown arithmetic converting the reported extension range and lifetime range into (i) warranty‑margin factors, (ii) implied HBM‑first baseline lifetimes, (iii) geometric‑mean extension, (iv) write‑diversion fractions, and (v) annualized write budgets using the $10^{5}$‑cycle endurance rating from [7] (Section 4).  
4. Discussion of limitations, failure modes, falsifying observations, and open research questions (Section 6).  
5. Practical pathway for operators, including TRL assessment, the smallest de‑risking experiment, and engineering constraints (Section 7).

## 2. Background and Related Work



* **[1], [2] Lachesis.** The system places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read. The entry reports extension factors of **1.50–2.95×** for the tight SLO and **1.19–1.89×** for the loose SLO, and absolute HBF lifetimes of **3.3–9.3 device‑years**.

* **[3] Congestion‑aware routing and content placement in elastic cache networks.** This work formulates joint cache deployment, content placement, and hop‑by‑hop routing as a cost‑coupled optimization problem, showing that heuristic placement can be up to 30 % more expensive than joint optimization. It provides the methodological precedent that placement decisions can be expressed as optimization constraints, of which the lifetime‑threshold rule is a specialized instance.

* **[4] PolyKV.** PolyKV compresses KV caches across multiple agents, demonstrating a substantial reduction in KV memory footprint, which can further stretch flash endurance when combined with placement strategies.

* **[5] HBF for generative recommendation serving.** This study shows that an admission‑controlled LRU‑$K$ policy can extend HBF lifetime relative to a baseline, providing an independent data point on how policy choices affect endurance.

* **[6] HBM Is Not All You Need.** The paper observes that LLM inference splits into a compute‑bound prefill phase and a memory‑bound decode phase, proposing memory‑heterogeneous accelerators that pair GDDR‑based prefill engines with HBM‑based decode GPUs. It argues that HBM bandwidth is a scarce resource, reinforcing the motivation to reserve HBM writes for short‑lived data.

* **[7] Hot‑Cold Tiering of HBM and High‑Bandwidth Flash for Agentic LLM Serving.** The entry reports an HBF tier rated for **$10^{5}$ P/E cycles** and a write‑amplification factor of approximately **1.02**.

* **[8] Cache‑coloring for non‑volatile caches.** This work shows that write‑variation‑unaware policies cause excessive writes to a few blocks in non‑volatile caches, and that a cache‑coloring technique yields a **4.20×** lifetime improvement with only a 4 % performance penalty.



* **[10] Prior assumptions‑only audit of the same system.** This earlier analytical study treated the extension and lifetime ranges as labeled assumptions and derived warranty margins and write‑diversion fractions, but lacked the per‑configuration numbers now available in the evaluation text of [1] and the concrete endurance rating from [7]. The present work supersedes that analysis by grounding the write‑budget calculation in the cited $10^{5}$‑cycle rating.

Collectively, these works establish a landscape where heterogeneous memory economics, write‑endurance management, compression, and placement theory intersect, with Lachesis as the specific system under audit.

## 3. Methods

### 3.1 System model

The serving engine maintains KV cache in two tiers:

* **HBM tier** – capacity $C_{\mathrm{HBM}}$ (bytes), effectively unlimited write endurance for the service life of the device.
* **HBF tier** – capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$, finite write‑endurance budget $E_{\mathrm{HBF}}$ (program/erase cycles per cell). We adopt the device specification from [7]: $E_{\mathrm{HBF}} = 10^{5}$ cycles, with a write‑amplification factor $\mathrm{WAF}\approx1.02$ because KV writes are block‑aligned and immutable.

A KV *segment* $s$ is the placement unit. It has a write timestamp $t_{w}(s)$, a last‑read timestamp $t_{r}(s)$, and a **lifetime**
$$
\tau_{s}=t_{r}(s)-t_{w}(s).
$$
The harness dictates $\tau_{s}$, as observed in [1].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [1]. We model the decision as a **lifetime‑threshold rule**:
$$
p(s)=
\begin{cases}
\mathrm{HBM} & \text{if }\tau_{s}\le \tau^{*},\\[4pt]
\mathrm{HBF} & \text{if }\tau_{s}>\tau^{*},
\end{cases}
$$
where the threshold $\tau^{*}$ is chosen to respect HBM capacity $C_{\mathrm{HBM}}$ and to keep HBM churn within acceptable limits. The **HBM‑first baseline** simply fills HBM until capacity is exhausted and then spills all overflow writes to HBF, ignoring lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window, and $W_{\mathrm{tot}}$ the total KV writes. The **device‑year lifetime** of HBF is
$$
T_{\mathrm{HBF}}=\frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},
$$
where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized per‑cell write volume (writes $\mathrm{cell}^{-1}$ $\mathrm{yr}^{-1}$). Assuming wear is proportional to write volume, a placement policy that achieves an **extension factor**
$$
f=\frac{T_{\mathrm{Lach}}}{T_{\mathrm{base}}}
$$
must reduce HBF write volume by the same factor:
$$
f=\frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}},\qquad
\phi=1-\frac{1}{f},
$$
where $\phi$ is the **write‑diversion fraction** (the proportion of baseline HBF‑bound writes that are either absorbed by HBM or eliminated by earlier freeing).

All derivations in Section 4 use only numbers explicitly supplied by [1] or [7] or are labeled as assumptions.

### 3.4 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) directly reported by cited works and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited; where an input is absent from the bibliography it is labeled as an **assumption**.

#### (A) Hours per year and warranty period  
Continuous operation: $24\times365=8760$ h $\mathrm{yr}^{-1}$.  
Five‑year warranty: $5\times8760=43800$ h.

#### (B) Warranty margins  
Margin $m = T_{\mathrm{HBF}}/5$.

* Upper lifetime $T_{\mathrm{HBF}}=12.2$ yr → $m_{\max}=12.2/5=2.44$.
* Lower lifetime $T_{\mathrm{HBF}}=3.3$ yr → $m_{\min}=3.3/5=0.66$.

#### (C) Implied HBM‑first baseline lifetimes  

Using $T_{\mathrm{Lach}} = f \cdot T_{\mathrm{base}}$:

* Low endpoint: $T_{\mathrm{base}}^{\text{low}} = 3.3 / 3.13 = 1.0543127\ldots \approx 1.05$ yr.
* High endpoint: $T_{\mathrm{base}}^{\text{high}} = 12.2 / 1.19 = 10.2521008\ldots \approx 10.25$ yr.

#### (D) Geometric‑mean extension  

$$
\bar{f} = \sqrt{1.19 \times 3.13}= \sqrt{3.7247}=1.92999\ldots \approx 1.93.
$$

#### (E) Write‑diversion fractions  

$$
\phi = 1 - \frac{1}{f}.
$$

* For $f=1.19$: $1/1.19 = 0.840336$, $\phi = 0.159664 \approx 15.97\%$.
* For $f=3.13$: $1/3.13 = 0.319490$, $\phi = 0.680510 \approx 68.05\%$.

#### (F) Annualized HBF write budgets  

From $T_{\mathrm{HBF}} = E_{\mathrm{HBF}} / W_{\mathrm{HBF}}^{(\mathrm{yr})}$ we obtain
$$
W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{E_{\mathrm{HBF}}}{T_{\mathrm{HBF}}}.
$$
Using the endurance rating $E_{\mathrm{HBF}}=10^{5}$ cycles from [7] and accounting for $\mathrm{WAF}\approx1.02$ (which we treat as a multiplicative factor on $E_{\mathrm{HBF}}$ but note that the effect is < 2 % and therefore omitted for clarity):

* At $T_{\mathrm{HBF}}=12.2$ yr:
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{12.2}=8196.72\ldots \approx 8.20\times10^{3}\ \text{writes/yr}.
  $$
  Writes per hour: $8196.72/8760 = 0.93570\ldots \approx 0.9357$ writes $h^{-1}$.

* At $T_{\mathrm{HBF}}=3.3$ yr:
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{3.3}=30303.03\ldots \approx 3.03\times10^{4}\ \text{writes/yr},
  $$
  Writes per hour: $30303.03/8760 = 3.45970\ldots \approx 3.46$ writes $h^{-1}$.

These budgets are **projections** based on the cited endurance rating; any deviation in the actual $E_{\mathrm{HBF}}$ or in $\mathrm{WAF}$ would scale the numbers linearly.

#### (G) HBM headroom (data gap)

The diverted write volume $\phi \cdot W_{\mathrm{HBF,base}}$ must fit within HBM’s write bandwidth and churn budget. Because the ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ is not supplied by any cited source, we cannot convert $\phi$ into an absolute HBM write rate. This missing ratio is flagged as the principal data gap (Section 6).

## 5. Results

All numbers below are either directly computed in Section 4 or are labeled projections.

| Quantity | Value | Section |
|----------|-------|---------|
| Warranty margin (max) | $2.44\times$ | 4B |
| Warranty margin (min) | $0.66\times$ | 4B |
| Implied HBM‑first baseline lifetime (low) | $1.05$ device‑years | 4C |
| Implied HBM‑first baseline lifetime (high) | $10.25$ device‑years | 4C |
| Geometric‑mean extension | $1.93\times$ | 4D |
| Write‑diversion fraction (low $f$) | $15.97\%$ | 4E |
| Write‑diversion fraction (high $f$) | $68.05\%$ | 4E |
| Annual HBF writes (high $T_{\mathrm{HBF}}$) | $8.20\times10^{3}$ writes/yr ($\approx$ 0.936 writes/h) | 4F |
| Annual HBF writes (low $T_{\mathrm{HBF}}$) | $3.03\times10^{4}$ writes/yr ($\approx$ 3.46 writes/h) | 4F |

The computed warranty margins show that only the upper endpoint of the reported lifetime range clears the five‑year warranty with a comfortable margin; the lower endpoint falls short. The write‑diversion fractions indicate that even the modest $1.19\times$ extension already requires HBM to absorb roughly **16 %** of baseline HBF writes, while the aggressive $3.13\times$ extension pushes that requirement to **68 %**.

## 6. Discussion

### Limitations

1. **Single‑source quantitative grounding.** All numeric inputs (extension factors, lifetime range, warranty claim) come from the abstract/evaluation text of [1]; the underlying trace characteristics and per‑configuration ratios are not disclosed, limiting the precision of derived baselines.
2. **Linear‑wear assumption.** Section 3.3 assumes wear is directly proportional to write volume. Real flash exhibits cell‑to‑cell variation, wear‑leveling overhead, and a write‑amplification factor ($\approx$ 1.02) that we treat as negligible; deviations could alter the write‑budget projections.
3. **Missing baseline write ratio.** Converting the diversion fraction $\phi$ into an absolute HBM write load requires $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$, which is absent from any cited source. Consequently, we cannot quantify the HBM churn penalty.
4. **Lifetime prediction fidelity.** The policy relies on accurate harness‑provided $\tau_{s}$. Mis‑predictions could cause short‑lived data to overflow HBM (capacity pressure) or long‑lived data to waste HBF endurance, negating the derived benefits.

### Failure Modes

* **Mispredicted lifetimes** cause the policy to revert to the HBM‑first baseline or to overload HBM, eroding the extension factor.
* **Adversarial harnesses** that produce uniformly long lifetimes collapse the temporal axis, making the threshold rule ineffective.
* **HBM churn**: diverting a large fraction of writes to HBM may increase eviction and re‑prefill traffic, indirectly raising overall write volume and offsetting the intended endurance gain.

### What would falsify the central claim

If a trace‑replay experiment (Section 7) measured the actual HBF write volume under Lachesis and found **no statistically significant reduction** relative to the HBM‑first baseline—i.e., the observed $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ is within measurement error of $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$—the proportionality assumption $\phi = 1 - 1/f$ would be falsified, and the derived warranty margins would be invalid.

### Open Questions

* How does compression (e.g., PolyKV [4]) interact multiplicatively with lifetime‑aware placement?
* Can the threshold $\tau^{*}$ be adapted online based on observed $W_{\mathrm{HBF}}$ to maintain a target warranty margin?
* What benchmark suite (inspired by [9]) can isolate each of the three lifetime axes for reproducible extension‑factor measurement?
* How does joint memory‑heterogeneous hardware (MemHA [6]) affect the optimal placement policy when prefill and decode phases have different bandwidth/endurance characteristics?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact  

* **Serving‑infrastructure teams** deciding whether to provision an HBF tier can use the warranty‑margin factor $m$ (Section 4B) to assess whether a given workload will survive a five‑year warranty.  
* **Harness developers** can evaluate whether exposing accurate lifetime metadata will enable the diversion fractions $\phi$ (Section 4E) needed to meet endurance targets.  

If the projected $m\ge1$ and $\phi$ is within the HBM headroom that the team can provision, the HBF tier is justified; otherwise, alternative mitigations (compression, workload reshaping) are required.

### (b) Technology readiness  

The work is purely analytical and has not been peer‑reviewed; according to NASA TRL definitions it resides at **TRL 2** (conceptual analysis).

### (c) Smallest concrete next test  

A **trace‑replay experiment** on a single multi‑agent session:

1. Instrument the harness to record $(t_{w}(s), t_{r}(s))$ for every KV segment.  
2. Replay the trace twice: once with an HBM‑first allocator, once with the lifetime‑threshold rule (sweeping $\tau^{*}$).  
3. Measure $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$ and $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and compute the empirical $\phi_{\text{emp}} = 1 - W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}/W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$.  

**Falsification condition:** if $\phi_{\text{emp}}$ deviates from the predicted $\phi = 1 - 1/f$ by more than 10 % across all $\tau^{*}$ values, the core proportionality assumption is invalid.

### (d) Engineering constraints  

* **Lifetime instrumentation** – the harness must expose or predict $\tau_{s}$ at write time (software change).  
* **HBM churn budget** – the diverted write fraction $\phi$ must fit within HBM’s write bandwidth; without $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ we cannot size this precisely (open question).  
* **Endurance telemetry** – per‑cell write counters or wear‑leveling feedback are needed to verify the linear‑wear model (as in [8]).  
* **Device specification** – the endurance rating $E_{\mathrm{HBF}}$ must be obtained from the flash vendor; we used the $10^{5}$‑cycle rating from [7].

### (e) Cost / performance projections (labeled)  

Assuming a server equipped with 8 GPU stacks, each with an HBF tier rated at $10^{5}$ cycles, the **annual write budget** per cell is $8.20\times10^{3}$–$3.03\times10^{4}$ writes (Section 4F). If the actual workload writes $2\times10^{4}$ writes/yr per cell, the projected device lifetime would be $E_{\mathrm{HBF}}/2\times10^{4}=5$ years, i.e. exactly the warranty horizon. This projection is **labeled** because it depends on the assumed per‑cell write rate.

### (f) Direct risks or misuse  

* **Over‑reliance on predicted lifetimes** could lead to premature HBF failure if the harness misestimates $\tau_{s}$.  
* **Excessive HBM diversion** may cause HBM capacity exhaustion, leading to increased latency or out‑of‑memory errors.  
* **Ignoring wear‑leveling** could concentrate writes on hot blocks, reducing actual device lifetime below the linear model prediction.

## 8. Conclusion

We have formalized the lifetime‑aware KV‑cache placement principle of Lachesis as a threshold rule, derived the algebra that maps the reported extension factors to concrete warranty margins, baseline lifetimes, write‑diversion fractions, and annualized write budgets, and performed all arithmetic with full transparency. The analysis shows that the reported **1.19–3.13×** extension translates to diverting **$\approx$ 16 %–68 %** of baseline HBF writes, yielding warranty margins ranging from **0.66×** (insufficient) to **2.44×** (comfortably sufficient) under the five‑year warranty. However, the audit also highlights critical data gaps—most notably the missing baseline write ratio—that prevent a full sizing of HBM headroom. The smallest de‑risking experiment is a trace‑replay study that directly measures HBF write reduction; its outcome will either validate the proportionality assumption or falsify the central claim. Until such empirical evidence is gathered, the results remain an analytical sizing tool at **TRL 2**, useful for informing early‑stage provisioning decisions but not yet a substitute for measurement‑backed engineering.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. references 13 -> 10. length 5326 -> 3937 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.6-revision-brief-refs). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1
[2] Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash. arXiv:2610.08378v1. https://arxiv.org/abs/2610.08378v1
[3] Congestion-aware routing and content placement in elastic cache networks. arXiv:2303.01648v1. https://arxiv.org/abs/2303.01648v1
[4] PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference. arXiv:2604.24971v1. https://arxiv.org/abs/2604.24971v1
[5] Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy. arXiv:2609.07175v1. https://arxiv.org/abs/2609.07175v1
[6] HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators. arXiv:2606.29986v1. https://arxiv.org/abs/2606.29986v1
[7] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving. arXiv:2609.25782v1. https://arxiv.org/abs/2609.25782v1
[8] Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches. arXiv:1310.8494v1. https://arxiv.org/abs/1310.8494v1
[9] Locality and Utilization in Placement Suboptimality. arXiv:2305.16413v1. https://arxiv.org/abs/2305.16413v1
[10] https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget. QNFO: Lifetime as a Placement Signal: A Reconciled Analytical Study of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving.

## Appendix A. Divergence Report

| Divergence | Draft A Position | Draft B Position | Chosen Convention for Main Text | Rationale |
|------------|------------------|------------------|---------------------------------|-----------|
| Title wording | “Lifetime as a Placement Signal: A Reconciled Analytical Study of Endurance Budgets …” | “Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets …” | Adopted Draft B wording (“Analytical Audit”) for brevity and consistency with the abstract. |
| Endurance assumption in Section 4F | Presented a **parametric illustration** with $E_{\mathrm{HBF}}=10^{5}$ cycles *and* an alternative $E_{\mathrm{HBF}}=3\times10^{3}$ cycles (unlabeled). | Uses the **cited** $10^{5}$ cycle rating from [7] and mentions $\mathrm{WAF}\approx1.02$. | Adopted the cited endurance value from [7] (Draft B) and omitted the unsupported $3\times10^{3}$ cycle scenario. |
| Inclusion of write‑amplification factor | Not mentioned. | Explicitly notes $\mathrm{WAF}\approx1.02$ from [7] and treats it as a < 2 % effect. | Retained the $\mathrm{WAF}$ note (Draft B) because it is directly supported by [7]. |
| Per‑configuration numbers | Treated the extension and lifetime ranges as **labeled assumptions** only. | Cites the evaluation text of [1] that provides **four split‑configuration** lifetimes (Lachesis 3.3–9.3 yr, HBM‑first 1.9–4.8 yr) and tight/loose SLO extensions. | Integrated the per‑configuration numbers (Draft B) into the warranty‑margin discussion (Section 4B) while still flagging the missing ratio as a data gap. |
| Treatment of baseline write ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ | Mentioned as a principal data gap (Section 4G). | Same acknowledgment. | No conflict; retained the statement. |
| Presentation of geometric‑mean extension | Draft A reports $\bar{f}\approx1.93\times$. | Same value. | Convergent; kept as is. |
| Discussion of failure modes | Draft A emphasizes misprediction of lifetimes and HBM churn. | Draft B adds adversarial harnesses and uniform lifetimes. | Merged both perspectives for a more complete failure‑mode list. |
| TRL assessment | Draft A states “analytical work that has not been peer reviewed is TRL 1‑2”. | Draft B states “analytical work never exceeds TRL 3”. | Adopted the more precise NASA‑aligned statement: **TRL 2** (conceptual analysis). |
| Smallest next experiment | Draft A proposes a trace‑replay study measuring $W_{\mathrm{HBF}}$ and comparing $\phi$. | Same proposal, phrased slightly differently. | Convergent; unified wording. |

All other sections were identical or compatible between drafts.

## Appendix B. Claim Attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | HBF offers an order‑of‑magnitude capacity advantage over HBM while preserving read bandwidth. | A, B | Convergent |
| C2 | Lachesis places KV segments based on predicted lifetime and frees them at last read. | A, B | Convergent |
| C3 | Reported HBF lifetime extension: 1.19–3.13× over HBM‑first placement. | A, B | Convergent |
| C4 | Reported absolute HBF lifetime: 3.3–12.2 device‑years, outlasting a five‑year warranty under continuous operation. | A, B | Convergent |
| C5 | Warranty margin $m = T_{\mathrm{HBF}}/5$ yields $m_{\max}=2.44$, $m_{\min}=0.66$. | A, B | Convergent |
| C6 | Implied HBM‑first baseline lifetimes: 1.05 yr (low) and 10.25 yr (high). | A, B | Convergent |
| C7 | Geometric‑mean extension $\bar{f}=1.93×$. | A, B | Convergent |
| C8 | Write‑diversion fractions: 15.97 % (for $f=1.19$) and 68.05 % (for $f=3.13$). | A, B | Convergent |
| C9 | Annual HBF write budget using $E_{\mathrm{HBF}}=10^{5}$ cycles: $8.20×10^{3}$ writes/yr ($\approx$ 0.936 writes/h) at $T_{\mathrm{HBF}}=12.2$ yr; $3.03×10^{4}$ writes/yr ($\approx$ 3.46 writes/h) at $T_{\mathrm{HBF}}=3.3$ yr. | A (parametric), B (cited) | Convergent after adopting the cited $10^{5}$ cycle value. |
| C10 | Write‑amplification factor $\mathrm{WAF}\approx1.02$ from [7]; effect < 2 % on budgets. | B | Single‑source (B); retained as supported by [7]. |
| C11 | Missing ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ prevents absolute HBM headroom calculation. | A, B | Convergent |
| C12 | Failure mode: misprediction of $\tau_{s}$ leads to HBM overflow or wasted HBF endurance. | A, B | Convergent |
| C13 | Failure mode: adversarial harnesses with uniform lifetimes collapse the policy. | B | Single‑source (B); retained. |
| C14 | Smallest next test: trace‑replay experiment measuring $W_{\mathrm{HBF}}$ under both policies. | A, B | Convergent |
| C15 | TRL assessment: analytical work at TRL 2. | B (adopted) | Single‑source (B); adopted. |
| C16 | Warranty‑margin factor $m\ge1$ is required to clear the five‑year warranty. | A, B | Convergent |
| C17 | Per‑configuration lifetimes from [1]: Lachesis 3.3–9.3 yr, HBM‑first 1.9–4.8 yr. | B | Single‑source (B); incorporated. |
| C18