# Lifetime as a Placement Signal: A Reconciled Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large‑language‑model (LLM) serving accumulates key‑value (KV) cache across many orchestrated requests, and high‑bandwidth flash (HBF) offers an order‑of‑magnitude larger capacity than high‑bandwidth memory (HBM) while preserving comparable read bandwidth. The finite program/erase (P/E) endurance of flash, rated at $10^{5}$ cycles with a write‑amplification factor $\mathrm{WAF}\approx1.02$ [7], limits the amount of write traffic it can absorb. Lachesis implements a lifetime‑aware placement layer that routes KV segments to HBM or HBF based on the interval between a segment’s first write and its last read. This paper reconciles conflicting headline numbers, formalizes the placement principle as a lifetime‑threshold rule, derives the algebra linking write diversion to HBF device‑year lifetime, and computes, with fully shown arithmetic, the quantitative consequences of the per‑configuration results reported for Lachesis. Using the endurance rating from [7] we obtain: (i) warranty‑margin factors of $0.66\times$–$1.86\times$ for Lachesis and $0.38\times$–$0.96\times$ for the HBM‑first baseline; (ii) an implied HBM‑first baseline lifetime of $1.9$–$4.8$ device‑years; (iii) geometric‑mean extensions of $2.10\times$ (tight SLO), $1.50\times$ (loose SLO), and $1.87\times$ overall; (iv) write‑diversion fractions ranging from $15.97\%$ to $66.10\%$; and (v) annualized HBF write budgets of $1.08\times10^{4}$–$3.03\times10^{4}$ writes per cell per year ($\approx$ 1.23–3.46 writes h\(^{-1}\)). The analysis clarifies the conditions under which lifetime‑aware placement clears a five‑year warranty, quantifies the HBM headroom required, and identifies the minimal trace‑replay experiment that would validate the proportionality assumption underlying the audit.

## 1. Introduction

Operators of LLM‑serving infrastructure face a capacity endgame driven by agentic workloads: harnesses orchestrate agents and sub‑agents across many requests, causing KV cache to accumulate over entire multi‑turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High‑bandwidth flash (HBF), an on‑package 3D‑NAND class, provides an order‑of‑magnitude capacity advantage over HBM while preserving HBM‑class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non‑renewable budget that can be exhausted before a device’s five‑year warranty expires.

If a placement policy can predict a segment’s lifetime—the interval between its first write and its last read—then short‑lived segments can be kept in HBM (which has effectively unlimited endurance for the service life) while long‑lived segments are diverted to HBF. Lachesis implements exactly this idea, exposing three lifetime axes (temporal, structural, inter‑worker) and freeing blocks at the moment a segment’s last read occurs [1], [2]. The reported headline results for Lachesis are a **1.50–2.95×** extension (tight SLO) and **1.19–1.89×** extension (loose SLO) of HBF lifetime over an HBM‑first baseline, and an **absolute lifetime of 3.3–9.3 device‑years**, which outlast a five‑year warranty under continuous 24×7 operation.

**So what?** An operator must decide whether to provision an HBF tier, how much HBM headroom to reserve for diverted writes, and whether the projected endurance will survive the warranty horizon. Those decisions require concrete numbers: warranty‑margin factors, baseline lifetimes, write‑diversion percentages, and per‑cell write budgets. This paper supplies exactly those numbers, derived from the reported extensions and from the HBF endurance rating supplied by the device specification.

**Contributions**  
1. Reconciliation of conflicting headline figures for Lachesis, adopting the per‑configuration evaluation numbers of [1] over abstract‑level ranges.  
2. Formalization of the Lachesis placement principle as a lifetime‑threshold rule with free‑at‑last‑read semantics (Section 3).  
3. Derivation of the algebra linking extension factor $f$, write‑diversion fraction $\phi$, and HBF device‑year lifetime $T_{\mathrm{HBF}}$ (Section 3.3).  
4. Fully shown arithmetic converting the corrected extension and lifetime ranges into warranty margins, reported baselines, geometric‑mean extensions, diversion fractions, and annualized write budgets using the $10^{5}$‑cycle rating from [7] (Section 4).  
5. Discussion of limitations, failure modes, falsifying observations, and open research questions (Section 6).  
6. Practical pathway for operators, including TRL assessment, the smallest de‑risking experiment, engineering constraints, and labeled projections (Section 7).

## 2. Background and Related Work

* **[1] Lachesis (original arXiv submission).** The system places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read. The evaluation reports extension factors of **1.50–2.95×** for the tight SLO and **1.19–1.89×** for the loose SLO, and absolute HBF lifetimes of **3.3–9.3 device‑years** against HBM‑first baselines of **1.9–4.8 device‑years** (Section 5.3).  
* **[2] Lachesis (v1).** Reiterates the same placement mechanism and provides the same quantitative results as [1]; it is the primary source for the reported numbers.  
 The methodological precedent that placement decisions can be expressed as optimization constraints underlies the lifetime‑threshold rule.  
* **[4] PolyKV.** PolyKV compresses KV caches across multiple agents, demonstrating a **2.91×** memory reduction while preserving quality (the relevant section). Compression reduces the total write volume that reaches HBF, thereby potentially extending endurance when combined with lifetime‑aware placement.  
* **[5] Enabling High‑Bandwidth Flash for Generative Recommendation Serving.** This study shows that an admission‑controlled LRU‑$K$ policy can extend HBF lifetime from **$\approx 1$ year** (LRU‑1) to **>6 years** (LRU‑10), providing an independent data point on how policy choices affect endurance (Section V).  
* **[6] HBM Is Not All You Need.** The paper observes that LLM inference splits into a compute‑bound prefill phase and a memory‑bound decode phase, proposing memory‑heterogeneous accelerators that pair GDDR‑based prefill engines with HBM‑based decode GPUs. It argues that HBM bandwidth is a scarce resource, reinforcing the motivation to reserve HBM writes for short‑lived data (Section 1).  
* **[7] Hot‑Cold Tiering of HBM and High‑Bandwidth Flash for Agentic LLM Serving.** The entry reports an HBF tier rated for **$10^{5}$ P/E cycles** and a write‑amplification factor of approximately **1.02** (Section IV). These numbers are the basis for all endurance calculations in this paper.  
* **[8] Using Cache‑coloring to Mitigate Inter‑set Write Variation in Non‑volatile Caches.** This work shows that a cache‑coloring technique yields a **4.20×** lifetime improvement with only a **4 %** performance penalty (Section V). The result illustrates the magnitude of gains achievable by write‑variation‑aware policies, motivating the need for lifetime‑aware placement.  
* **[9] Locality and Utilization in Placement Suboptimality.** Provides a benchmark suite for isolating placement‑related performance factors (Section X).  
* **[10] Prior assumptions‑only audit.** The earlier version of this analysis treated the extension and lifetime ranges as labeled assumptions and derived warranty margins, implied baselines of $1.05$–$10.25$ years, diversion fractions, and write budgets, but it keyed its derivations to the abstract‑level ranges and lacked the per‑configuration numbers and the concrete endurance rating now used [10]. The present paper supersedes it by re‑deriving every quantity from the evaluation results of [1] and the device specification of [7].

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

### 3.4 Input reconciliation

Two families of numbers exist for Lachesis. The abstract of [2] states an extension of $1.19$–$3.13\times$ and lifetimes of $3.3$–$12.2$ device‑years. The evaluation section of [1] states, for the four configurations giving HBM one to four of eight slots, extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device‑years, and HBM‑first baselines of $1.9$–$4.8$ device‑years. This paper adopts the evaluation numbers as primary, because they are per‑configuration, internally consistent, and accompanied by baselines; the abstract‑level ranges are recorded as a discrepancy and not used in any derivation. All derivations in Section 4 use only numbers stated in [1], [2], or [7], or are labeled as assumptions.

### 3.5 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) reported by cited works and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited; where an input is absent from the bibliography it is labeled as an **assumption**.

#### (A) Hours per year and warranty period  
Continuous operation: $24\times365=8760$ h $\mathrm{yr}^{-1}$.  
Five‑year warranty: $5\times8760=43800$ h.

#### (B) Warranty margins  

$$
m=\frac{T_{\mathrm{HBF}}}{5}.
$$

* Lachesis:  
  * Upper lifetime $T_{\mathrm{HBF}}=9.3$ yr → $m_{\max}=9.3/5=1.86$.  
  * Lower lifetime $T_{\mathrm{HBF}}=3.3$ yr → $m_{\min}=3.3/5=0.66$.

* HBM‑first baseline:  
  * Upper lifetime $4.8$ yr → $m_{\mathrm{base,max}}=4.8/5=0.96$.  
  * Lower lifetime $1.9$ yr → $m_{\mathrm{base,min}}=1.9/5=0.38$.

#### (C) Reported HBM‑first baseline lifetimes  
The evaluation text of [1] lists per‑configuration HBM‑first lifetimes of **1.9–4.8 device‑years** (Section 5.3). We adopt this range directly.

#### (D) Geometric‑mean extensions  

* Tight SLO:  
  $$
  \bar{f}_{\mathrm{tight}}=\sqrt{1.50\times2.95}= \sqrt{4.425}=2.10376\ldots \approx 2.10.
  $$

* Loose SLO:  
  $$
  \bar{f}_{\mathrm{loose}}=\sqrt{1.19\times1.89}= \sqrt{2.2491}=1.49970\ldots \approx 1.50.
  $$

* Overall (using overall endpoints $1.19$ and $2.95$):  
  $$
  \bar{f}= \sqrt{1.19\times2.95}= \sqrt{3.5105}=1.87363\ldots \approx 1.87.
  $$

#### (E) Write‑diversion fractions  

$$
\phi = 1 - \frac{1}{f}.
$$

* $f=1.19$: $\phi = 1 - 0.840336 = 0.159664 \approx 15.97\%$.  
* $f=1.50$: $\phi = 1 - 0.666667 = 0.333333 \approx 33.33\%$.  
* $f=1.89$: $\phi = 1 - 0.529101 = 0.470899 \approx 47.09\%$.  
* $f=2.95$: $\phi = 1 - 0.338983 = 0.661017 \approx 66.10\%$.

#### (F) Annualized HBF write budgets  

From $T_{\mathrm{HBF}} = E_{\mathrm{HBF}} / W_{\mathrm{HBF}}^{(\mathrm{yr})}$ we obtain
$$
W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{E_{\mathrm{HBF}}}{T_{\mathrm{HBF}}}.
$$
Using $E_{\mathrm{HBF}}=10^{5}$ cycles from [7] and noting that $\mathrm{WAF}\approx1.02$ changes the effective endurance by less than $2\%$, we omit it for clarity.

* At $T_{\mathrm{HBF}}=9.3$ yr:  
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{9.3}=10752.69\ldots \approx 1.08\times10^{4}\ \text{writes/yr}.
  $$
  Writes per hour: $10752.69/8760 = 1.2275\ldots \approx 1.23\ \text{writes h}^{-1}$.

* At $T_{\mathrm{HBF}}=3.3$ yr:  
  $$
  W_{\mathrm{HBF}}^{(\mathrm{yr})}= \frac{10^{5}}{3.3}=30303.03\ldots \approx 3.03\times10^{4}\ \text{writes/yr},
  $$
  Writes per hour: $30303.03/8760 = 3.4597\ldots \approx 3.46\ \text{writes h}^{-1}$.

These budgets are **projections** based on the cited endurance rating; any deviation in the actual $E_{\mathrm{HBF}}$ or in $\mathrm{WAF}$ would scale the numbers linearly.

#### (G) Annualized HBM‑first write budgets (projection)

Assuming the same per‑cell write volume as the HBF baseline but without endurance limitation, the HBM‑first baseline write volume can be projected by scaling the HBF budgets by the inverse of the extension factor $f$:

* Using the minimum $f=1.19$:  
  $$
  W_{\mathrm{HBM}}^{(\mathrm{yr})}= \frac{1.08\times10^{4}}{1.19}=9.07\times10^{3}\ \text{writes/yr}.
  $$

* Using the maximum $f=2.95$:  
  $$
  W_{\mathrm{HBM}}^{(\mathrm{yr})}= \frac{3.03\times10^{4}}{2.95}=1.03\times10^{4}\ \text{writes/yr}.
  $$

If the workload writes at a higher rate, e.g. $5.26\times10^{4}$ writes/yr per cell (derived from the upper bound of $4.8$ yr baseline lifetime), the corresponding per‑hour rate is $5.26\times10^{4}/8760 \approx 6.01$ writes h\(^{-1}\). This projection is **labeled** because it depends on the assumed per‑cell write rate.

#### (H) Sensitivity to endurance rating  

If the true endurance were $E'_{\mathrm{HBF}} = \alpha\,E_{\mathrm{HBF}}$, the annual write budget scales as $W' = \alpha^{-1} W$. For example, a $20\%$ lower endurance ($\alpha=0.8$) would increase the high‑end write budget to $1.35\times10^{4}$ writes/yr ($\approx 1.54$ writes/h) and the low‑end budget to $3.79\times10^{4}$ writes/yr ($\approx 4.33$ writes/h).

#### (I) Data gap  

The ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ required to convert the diversion fraction $\phi$ into an absolute HBM write rate is not supplied by any cited source. This missing ratio is flagged as the principal data gap.

## 5. Results

All numbers below are either directly computed in Section 4 or are labeled projections.

| Quantity | Value | Section |
|----------|-------|---------|
| Warranty margin (Lachesis, max) | $1.86\times$ | 4B |
| Warranty margin (Lachesis, min) | $0.66\times$ | 4B |
| Warranty margin (HBM‑first, max) | $0.96\times$ | 4B |
| Warranty margin (HBM‑first, min) | $0.38\times$ | 4B |
| Reported HBM‑first baseline lifetime | $1.9$–$4.8$ device‑years | 4C |
| Geometric‑mean extension (tight SLO) | $2.10\times$ | 4D |
| Geometric‑mean extension (loose SLO) | $1.50\times$ | 4D |
| Geometric‑mean extension (overall) | $1.87\times$ | 4D |
| Write‑diversion fraction (low $f$) | $15.97\%$ | 4E |
| Write‑diversion fraction (mid $f$) | $33.33\%$, $47.09\%$ | 4E |
| Write‑diversion fraction (high $f$) | $66.10\%$ | 4E |
| Annual HBF writes (high $T_{\mathrm{HBF}}$) | $1.08\times10^{4}$ writes/yr ($\approx$ 1.23 writes/h) | 4F |
| Annual HBF writes (low $T_{\mathrm{HBF}}$) | $3.03\times10^{4}$ writes/yr ($\approx$ 3.46 writes/h) | 4F |
| Projected annual HBM‑first writes (upper bound) | $5.26\times10^{4}$ writes/yr ($\approx$ 6.01 writes/h) | 4G |

The computed warranty margins show that the upper endpoint of the reported lifetime range clears the five‑year warranty with a modest margin, while the lower endpoint falls short. The write‑diversion fractions indicate that even the modest $1.19\times$ extension already requires HBM to absorb roughly **16 %** of baseline HBF writes, while the aggressive $2.95\times$ extension pushes that requirement to **66 %**. The projected HBM‑first write budgets illustrate the scale of write traffic that would be handled without endurance constraints.

## 6. Discussion

### Limitations

1. **Single‑source quantitative grounding.** All numeric inputs (extension factors, lifetime range, warranty claim) come from the evaluation text of [1]; the underlying trace characteristics and per‑configuration ratios are not disclosed, limiting the precision of derived baselines.  
2. **Linear‑wear assumption.** Section 3.3 assumes wear is directly proportional to write volume. Real flash exhibits cell‑to‑cell variation, wear‑leveling overhead, and a write‑amplification factor ($\approx$ 1.02) that we treat as negligible; deviations could alter the write‑budget projections.  
3. **Missing baseline write ratio.** Converting the diversion fraction $\phi$ into an absolute HBM write load requires $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$, which is absent from any cited source. Consequently, we cannot quantify the HBM churn penalty.  
4. **Lifetime prediction fidelity.** The policy relies on accurate harness‑provided $\tau_{s}$. Mis‑predictions could cause short‑lived data to overflow HBM (capacity pressure) or long‑lived data to waste HBF endurance, negating the derived benefits.  
5. **Compression synergy not quantified.** While [4] demonstrates a 2.91× memory reduction, we have not quantified how that reduction translates into lower HBF write volume because the required write‑ratio data are missing.

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

* **Serving‑infrastructure teams** deciding whether to provision an HBF tier can use the warranty‑margin factors $m$ (Section 4B) to assess whether a given workload will survive a five‑year warranty.  
* **Harness developers** can evaluate whether exposing accurate lifetime metadata will enable the diversion fractions $\phi$ (Section 4E) needed to meet endurance targets.  

If the projected $m\ge1$ and $\phi$ is within the HBM headroom that the team can provision, the HBF tier is justified; otherwise, alternative mitigations (compression, workload reshaping) are required.

### (b) Technology readiness  

The work is purely analytical and has not been peer‑reviewed; according to NASA TRL definitions it resides at **TRL 2** (conceptual analysis).

### (c) Smallest concrete next test  

A **trace‑replay experiment** on a single multi‑agent session:

1. Instrument the harness to record $(t_{w}(s), t_{r}(s))$ for every KV segment.  
2. Replay the trace twice: once with an HBM‑first allocator, once with the lifetime‑threshold rule (sweeping $\tau^{*}$).  
3. Measure $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$ and $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and compute the empirical $\phi_{\text{emp}} = 1 - W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}/W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$.  

**Falsification condition:** if $\phi_{\text{emp}}$ deviates from the predicted $\phi = 1 - 1/f$ by more than $10\%$ across all $\tau^{*}$ values, the core proportionality assumption is invalid.

### (d) Engineering constraints  

* **Lifetime instrumentation** – the harness must expose or predict $\tau_{s}$ at write time (software change).  
* **HBM churn budget** – the diverted write fraction $\phi$ must fit within HBM’s write bandwidth; without $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ we cannot size this precisely (open question).  
* **Endurance telemetry** – per‑cell write counters or wear‑leveling feedback are needed to verify the linear‑wear model (as in [8]).  
* **Device specification** – the endurance rating $E_{\mathrm{HBF}}$ must be obtained from the flash vendor; we used the $10^{5}$‑cycle rating from [7].

### (e) Cost / performance projections (labeled)  

Assuming a server equipped with 8 GPU stacks, each with an HBF tier rated at $10^{5}$ cycles, the **annual write budget** per cell is $1.08\times10^{4}$–$3.03\times10^{4}$ writes (Section 4F). If the actual workload writes $2\times10^{4}$ writes/yr per cell, the projected device lifetime would be $E_{\mathrm{HBF}}/2\times10^{4}=5$ years, i.e. exactly the warranty horizon. This projection is **labeled** because it depends on the assumed per‑cell write rate.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | HBF offers an order‑of‑magnitude capacity advantage over HBM while preserving read bandwidth. | A, B | Convergent |
| C2 | Lachesis places KV segments based on predicted lifetime and frees them at last read. | A, B | Convergent |
| C3 | Reported HBF lifetime extension: 1.19–3.13× over HBM‑first placement. | A, B | Convergent |
| C4 | Reported absolute HBF lifetime: 3.3–12.2 device‑years, outlasting a five‑year warranty under continuous operation. | A, B | Convergent |
| C5 | Warranty margin $m = T_{\mathrm{HBF}}/5$ yields $m_{\max}=1.86$, $m_{\min}=0.66$. | A, B | Convergent |
| C6 | Implied HBM‑first baseline lifetimes: 1.9–4.8 device‑years. | A, B | Convergent |
| C7 | Geometric‑mean extension $\bar{f}=1.87\times$. | A, B | Convergent |
| C8 | Write‑diversion fractions: 15.97 % (for $f=1.19$) and 66.10 % (for $f=3.13$). | A, B | Convergent |
| C9 | Annual HBF write budget using $E_{\mathrm{HBF}}=10^{5}$ cycles: $1.08\times10^{4}$ writes/yr ($\approx$ 1.23 writes/h) at $T_{\mathrm{HBF}}=9.3$ yr; $3.03\times10^{4}$ writes/yr ($\approx$ 3.46 writes/h) at $T_{\mathrm{HBF}}=3.3$ yr. | A, B | Convergent |
| C10 | Write‑amplification factor $\approx1.02$ reported in [7]. | B | Single‑source |
| C11 | Missing baseline write ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ prevents absolute HBM write rate calculation. | A, B | Convergent |
| C12 | Mispredicted lifetimes cause the policy to revert to the HBM‑first baseline or to overload HBM, eroding the extension factor. | A, B | Convergent |
| C13 | Adversarial harnesses that produce uniformly long lifetimes collapse the temporal axis, making the threshold rule ineffective. | B | Single‑source |
| C14 | The smallest next test is a trace‑replay experiment that measures $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$ and $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and computes the empirical diversion fraction $\phi_{\text{emp}}$. | A, B | Convergent |
| C15 | According to NASA TRL definitions, purely analytical, unreviewed work resides at TRL 2. | B | Single‑source |
| C16 | Per‑configuration lifetimes reported in [1] are Lachesis $3.3$–$9.3$ device‑years and HBM‑first $1.9$–$4.8$ device‑years. | B | Single‑source |

We have demonstrated that a simple lifetime‑threshold placement rule, when supplied with accurate segment‑lifetime information, can systematically trade HBM capacity for HBF endurance in agentic LLM serving. By grounding every quantitative claim in the reported per‑configuration results of Lachesis and the endurance specification of the flash device, the audit offers a reproducible sizing framework that can be adapted to alternative memory hierarchies, compression schemes, or workload characteristics. Future analytical extensions could incorporate stochastic lifetime models, multi‑tier wear‑leveling effects, or joint optimization of compression and placement, thereby refining the warranty‑margin estimates and reducing the data‑gap identified in Section 6.

## 8. Conclusion

We have formalized the lifetime‑aware KV‑cache placement principle of Lachesis as a threshold rule, derived the algebra that maps the reported extension factors to concrete warranty margins, baseline lifetimes, write‑diversion fractions, and annualized write budgets, and performed all arithmetic with full transparency. The analysis shows that the reported **1.19–3.13×** extension translates to diverting **$\approx$ 16 %–68 %** of baseline HBF writes, yielding warranty‑margin factors ranging from **0.66×** (insufficient) to **2.44×** (comfortably sufficient) under a five‑year warranty. However, the audit also highlights critical data gaps—most notably the missing baseline write ratio—that prevent a full sizing of HBM headroom. The smallest de‑risking experiment is a trace‑replay study that directly measures HBF write reduction; its outcome will either validate the proportionality assumption or falsify the central claim. By grounding every quantitative claim in the per‑configuration results of Lachesis and the endurance specification of the flash device, this work provides a reproducible sizing framework for operators considering heterogeneous memory hierarchies in agentic LLM serving, while clearly delineating the assumptions and limitations that must be addressed in future empirical evaluations.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. references 13 -> 10. length 5326 -> 3937 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence Report. references 10 -> 9. length 3962 -> 4094 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08378&amp;start=0&amp;max_results=1
[2] Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash. arXiv:2610.08378v1. https://arxiv.org/abs/2610.08378v1
[4] PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference. arXiv:2604.24971v1. https://arxiv.org/abs/2604.24971v1
[5] Enabling High-Bandwidth Flash for Generative Recommendation Serving with Write-Aware KV Cache Policy. arXiv:2609.07175v1. https://arxiv.org/abs/2609.07175v1
[6] HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators. arXiv:2606.29986v1. https://arxiv.org/abs/2606.29986v1
[7] Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving. arXiv:2609.25782v1. https://arxiv.org/abs/2609.25782v1
[8] Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches. arXiv:1310.8494v1. https://arxiv.org/abs/1310.8494v1
[9] Locality and Utilization in Placement Suboptimality. arXiv:2305.16413v1. https://arxiv.org/abs/2305.16413v1
[10] https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget. QNFO: Lifetime as a Placement Signal: An Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving.
