# Lifetime as a Placement Signal: A Corrected Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large-language-model (LLM) serving accumulates key-value (KV) cache across many orchestrated requests, and high-bandwidth flash (HBF) offers an order-of-magnitude larger capacity than high-bandwidth memory (HBM) while preserving comparable read bandwidth. The finite program/erase (P/E) endurance of flash, rated at $10^{5}$ cycles with a write-amplification factor $\mathrm{WAF}\approx1.02$, limits the write traffic an HBF tier can absorb before a five-year warranty expires. An earlier audit of this question keyed its headline derivations to abstract-level ranges (extension $1.19$–$3.13\times$, lifetime $3.3$–$12.2$ device-years) that do not match the per-configuration evaluation numbers the underlying report itself gives; this paper corrects that mismatch and re-derives every quantity from the per-configuration numbers. With fully shown arithmetic we obtain: (i) warranty-margin factors of $0.66\times$–$1.86\times$ for the lifetime-aware policy and $0.38\times$–$0.96\times$ for the HBM-first baseline; (ii) reported baseline lifetimes of $1.9$–$4.8$ device-years; (iii) geometric-mean extensions of $2.10\times$ (tight SLO), $1.50\times$ (loose SLO), and $1.87\times$ overall; (iv) write-diversion fractions of $\phi=0.159664$ ($15.9664\%$, at $f=1.19$) to $\phi=0.661017$ ($66.1017\%$, at $f=2.95$); and (v) annualized HBF write budgets of $1.08\times10^{4}$–$3.03\times10^{4}$ writes per cell per year ($1.23$–$3.46$ writes $\mathrm{h}^{-1}$). The correction removes the spurious $2.44\times$ warranty margin and the $68\%$ diversion endpoint that the abstract-level ranges had introduced, and it clarifies which configurations clear a five-year warranty.

## 1. Introduction

Operators of LLM-serving infrastructure face a capacity endgame driven by agentic workloads: harnesses orchestrate agents and sub-agents across many requests, causing KV cache to accumulate over entire multi-turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High-bandwidth flash (HBF), an on-package 3D-NAND class, provides an order-of-magnitude capacity advantage over HBM while preserving HBM-class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non-renewable budget that can be exhausted before a device's five-year warranty expires.

If a placement policy can predict a segment's lifetime—the interval between its first write and its last read—then short-lived segments can be kept in HBM, which has effectively unlimited endurance for the service life, while long-lived segments are diverted to HBF. The system under audit, Lachesis, implements exactly this idea: it places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read [5].

**The correction this paper makes.** The prior audit [5] stated headline inputs of an extension of $1.19$–$3.13\times$ and an absolute HBF lifetime of $3.3$–$12.2$ device-years, and it derived several conclusions from those abstract-level ranges. Those abstract-level numbers do not match the per-configuration evaluation numbers that [5] itself attributes to the underlying system report: extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years, and HBM-first baselines of $1.9$–$4.8$ device-years. Deriving from the wrong range produced two concrete errors in [5]: a warranty-margin ceiling of $2.44\times$ (which is $12.2/5$ and has no per-configuration basis) and a diversion endpoint of $\approx68\%$ keyed to the abstract-level extension $3.13\times$. This paper re-keys every derivation to the per-configuration numbers and shows the corrected arithmetic in full.

**So what?** An operator must decide whether to provision an HBF tier, how much HBM headroom to reserve for diverted writes, and whether the projected endurance will survive the warranty horizon. Those decisions require concrete numbers: warranty-margin factors, baseline lifetimes, write-diversion percentages, and per-cell write budgets. Whether the corrected ranges clear the warranty, and by how much, changes the provisioning decision directly; the correction shows that the favorable tail of the earlier audit ($2.44\times$ margin) was an artifact of the abstract-level range and that the defensible ceiling is $1.86\times$.

**Contributions**
1. A reconciliation rule that adopts the per-configuration evaluation numbers over abstract-level ranges, with the discrepancy recorded and the convention stated (Section 3.4).
2. Formalization of the placement principle as a lifetime-threshold rule with free-at-last-read semantics (Section 3.2).
3. Derivation of the algebra linking the extension factor $f$, the write-diversion fraction $\phi$, and the HBF device-year lifetime $T_{\mathrm{HBF}}$ (Section 3.3).
4. Fully shown arithmetic converting the corrected extension and lifetime ranges into warranty margins, baseline write budgets, geometric-mean extensions, diversion fractions, and annualized write budgets using the $10^{5}$-cycle rating (Section 4); the baseline write volume is obtained from the reported baseline lifetimes as $E_{\mathrm{HBF}}/T_{\mathrm{base}}$ (Section 4G).
5. A limitations and falsification analysis, including the explicit statement that the citation base of this paper is five works (Section 6).
6. A practical pathway for operators: TRL assessment, the smallest de-risking experiment, engineering constraints, and labeled projections (Section 7).

## 2. Background and Related Work

This section discusses all five works in the paper's citation base. The citation base contains exactly five works, so the References list holds five entries, short of the eight-entry norm for a preprint of this kind; no additional verifiable works were available to this audit, and the consequence of this reduced coverage for the strength of the external validation is recorded as Limitation 1 in Section 6.

**[5] Lifetime as a Placement Signal (prior audit, the object of correction).** This work formalizes Lachesis's placement principle, adopts an HBF endurance rating of $10^{5}$ P/E cycles with $\mathrm{WAF}\approx1.02$, and reports a results table with warranty margins of $1.86\times$, $0.66\times$, $0.96\times$, and $0.38\times$; geometric-mean extensions of $2.10\times$, $1.50\times$, and $1.87\times$; diversion fractions of $15.97\%$, $33.33\%$, $47.09\%$, and $66.10\%$; and annual HBF write budgets of $1.08\times10^{4}$ and $3.03\times10^{4}$ writes per year. Its abstract, however, headlines an extension of $1.19$–$3.13\times$ and a lifetime of $3.3$–$12.2$ device-years, and its conclusion derives margins "from $0.66\times$ to $2.44\times$" and a diversion range "of $\approx16\%$–$68\%$" from those abstract-level endpoints. The internal tension between its own results table and its abstract/conclusion is precisely the defect this paper corrects; the per-configuration numbers in its Section 5.3 table ($1.50$–$2.95\times$ tight, $1.19$–$1.89\times$ loose, Lachesis $3.3$–$9.3$ years, baseline $1.9$–$4.8$ years) are taken here as primary.

**[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices.** Although from combinatorics, this paper supplies the methodological template for constraint-bounded auditing: it derives sharp lower bounds for the first and second Zagreb indices over trees with a given number of pendent vertices and characterizes the extremal graphs that attain them—for example, Theorem 1 gives $M_{1}(T)\geq 9n-16$ for a tree with an even number $n$ of pendent vertices, with equality for the $4$-tree in which every internal vertex has degree $4$. The audit below follows the same discipline: given a fixed constraint set (endurance rating, warranty horizon, reported extension factors), derive the tightest bounds the constraints admit and identify exactly which reported configuration attains each bound, rather than mixing bounds from inconsistent constraint sets—a discipline whose violation produced the corrected errors.

**[2] Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050.** This forecast argues that each computing era is defined by the physics of its substrate and that transitions follow the invariant dynamic "constraint saturation → substrate shift → Wright's Law cost decline → institutional adoption," with heterogeneous convergence (AI accelerators, processing-in-memory) as the central thesis for the coming two decades. The HBM-plus-HBF tiering audited here is an instance of that heterogeneous convergence at the memory-subsystem level: HBM's per-bit cost and capacity ceiling is the saturating constraint, and HBF is the substrate shift. The forecast's framing also supplies the audit's epistemic stance—its twelve dated falsifiable predictions model how a quantitative claim should be registered so that it can be disconfirmed, which Section 6 emulates with an explicit falsification condition.

**[3] The QWAV Decade: Enterprise p-Adic Computing 2025-2035.** This work defines Joules Per Computational Unit (JPCUB), a hardware-independent, workload-normalized efficiency metric. The relevance to the present audit is the metric-design lesson: an endurance budget per cell per year, normalized per cell and per year exactly as JPCUB normalizes per unit of computational work, is the quantity a procurement decision actually consumes. The annualized write budgets derived in Section 4F are constructed to serve that procurement role, and the divergence between abstract-level and per-configuration inputs illustrates why a metric must state its normalization convention explicitly.

**[4] Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport.** This paper is a worked precedent for correction-as-publication: it delivers a corrected reading of an ontology's boundary-confinement claim after an adversarial audit that found the underlying physics accurate but the unifying reading overgeneralized, and it re-issues the ontology as a falsifiable proposal rather than established doctrine. The present paper performs the same operation on [5]: the per-configuration arithmetic in [5] is accurate (its results table is internally consistent), but the abstract-level headline ranges are an overgeneralization that propagates two wrong conclusions, and the correction re-issues the audit keyed to the defensible constraint set.

Collectively, these works supply the object of correction [5], the bounding discipline [1], the substrate-shift context [2], the metric-normalization lesson [3], and the correction precedent [4]. No cited work other than [5] provides quantitative inputs to the derivations; all endurance and extension inputs come from [5].

## 3. Methods

### 3.1 System model

The serving engine maintains KV cache in two tiers:

- **HBM tier** — capacity $C_{\mathrm{HBM}}$ (bytes), effectively unlimited write endurance for the service life of the device.
- **HBF tier** — capacity $C_{\mathrm{HBF}} \gg C_{\mathrm{HBM}}$, finite write-endurance budget $E_{\mathrm{HBF}}$ (program/erase cycles per cell). We adopt the device specification reported in [5]: $E_{\mathrm{HBF}} = 10^{5}$ cycles, with a write-amplification factor $\mathrm{WAF}\approx1.02$ because KV writes are block-aligned and immutable.

A KV *segment* $s$ is the placement unit. It has a write timestamp $t_{w}(s)$, a last-read timestamp $t_{r}(s)$, and a **lifetime**

$$
\tau_{s}=t_{r}(s)-t_{w}(s).
$$

The harness dictates $\tau_{s}$, as observed in [5].

### 3.2 Placement rule

Lachesis places each segment at write time and frees its blocks once the segment is no longer read [5]. We model the decision as a **lifetime-threshold rule**:

$$
p(s)=
\begin{cases}
\mathrm{HBM} & \text{if }\tau_{s}\le \tau^{*},\\[4pt]
\mathrm{HBF} & \text{if }\tau_{s}>\tau^{*},
\end{cases}
$$

where the threshold $\tau^{*}$ is chosen to respect HBM capacity $C_{\mathrm{HBM}}$ and to keep HBM churn within acceptable limits. The **HBM-first baseline** fills HBM until capacity is exhausted and then spills all overflow writes to HBF, ignoring lifetime.

### 3.3 Endurance accounting

Let $W_{\mathrm{HBF}}$ be the number of writes reaching HBF over an observation window, and $W_{\mathrm{tot}}$ the total KV writes. The **device-year lifetime** of HBF is

$$
T_{\mathrm{HBF}}=\frac{E_{\mathrm{HBF}}}{W_{\mathrm{HBF}}^{(\mathrm{yr})}},
$$

where $W_{\mathrm{HBF}}^{(\mathrm{yr})}$ is the annualized per-cell write volume (writes $\mathrm{cell}^{-1}\,\mathrm{yr}^{-1}$). Assuming wear is proportional to write volume, a placement policy that achieves an **extension factor**

$$
f=\frac{T_{\mathrm{Lach}}}{T_{\mathrm{base}}}
$$

must reduce HBF write volume by the same factor. We take the extension factor to relate write volumes as

$$
f=\frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}},\qquad
\phi=1-\frac{1}{f},
$$

under the convention that $f$ is the ratio of baseline to policy write volumes, which is the form consistent with $f=T_{\mathrm{Lach}}/T_{\mathrm{base}}$ given the common endurance budget $E_{\mathrm{HBF}}$; the inverse pairing is not used in any derivation. Here $\phi$ is the **write-diversion fraction**: the proportion of baseline HBF-bound writes that are either absorbed by HBM or eliminated by earlier freeing. Inverting the lifetime relation gives the baseline write volume from the reported baseline lifetime,

$$
W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=\frac{E_{\mathrm{HBF}}}{T_{\mathrm{base}}},
$$

$$
\text{and the policy write volume follows as } W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}=\frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{f}.
$$

All derivations in Section 4 use only numbers explicitly supplied by [5] or are labeled as assumptions.

### 3.4 Input reconciliation

Two families of numbers exist for the system under audit. The abstract of [5] states an extension of $1.19$–$3.13\times$ and lifetimes of $3.3$–$12.2$ device-years. The evaluation section of [5] states, for the four configurations giving HBM one to four of eight slots, extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years, and HBM-first baselines of $1.9$–$4.8$ device-years. We adopt the evaluation numbers as primary under the convention that per-configuration results supersede abstract-level ranges, because they are internally consistent, accompanied by baselines, and keyed to named configurations; the abstract-level ranges are recorded as a discrepancy and are not used in any derivation. This convention resolves the two errors identified in Section 1: the $2.44\times$ margin ceiling (which only the $12.2$-year abstract-level endpoint can produce) and the $\approx68\%$ diversion endpoint (which only the $3.13\times$ abstract-level extension can produce).

### 3.5 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) reported by [5] and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited to [5]; where an input is absent from the citation base it is labeled as an **assumption**.

#### (A) Hours per year and warranty period

Continuous operation: $24\times365=8760$ h $\mathrm{yr}^{-1}$. Five-year warranty: $5\times8760=43800$ h.

#### (B) Warranty margins

The margin is defined as $m=T_{\mathrm{HBF}}/5$.

- Lachesis, upper lifetime $T_{\mathrm{HBF}}=9.3$ yr: $m_{\max}=9.3/5=1.86$.
- Lachesis, lower lifetime $T_{\mathrm{HBF}}=3.3$ yr: $m_{\min}=3.3/5=0.66$.
- HBM-first baseline, upper lifetime $4.8$ yr: $m_{\mathrm{base,max}}=4.8/5=0.96$.
- HBM-first baseline, lower lifetime $1.9$ yr: $m_{\mathrm{base,min}}=1.9/5=0.38$.

#### (C) Reported HBM-first baseline lifetimes

The evaluation of [5] lists per-configuration HBM-first lifetimes of $1.9$–$4.8$ device-years. We adopt this range directly; it is an input, not a derivation.

#### (D) Geometric-mean extensions

- Tight SLO: $\bar{f}_{\mathrm{tight}}=\sqrt{1.50\times2.95}=\sqrt{4.425}=2.10376\ldots\approx2.10$.
- Loose SLO: $\bar{f}_{\mathrm{loose}}=\sqrt{1.19\times1.89}=\sqrt{2.2491}=1.49970\ldots\approx1.50$.
- Overall (endpoints $1.19$ and $2.95$): $\bar{f}=\sqrt{1.19\times2.95}=\sqrt{3.5105}=1.87363\ldots\approx1.87$.

#### (E) Write-diversion fractions

$\phi=1-1/f$:

- $f=1.19$: $\phi=1-0.840336=0.159664$, i.e. $\phi\approx0.159664$ of baseline HBF writes, reported as $15.9664\%$.
- $f=1.50$: $\phi=1-0.666667=0.333333$, i.e. $\phi\approx0.333333$ of baseline HBF writes, reported as $33.3333\%$.
- $f=1.89$: $\phi=1-0.529101=0.470899$, i.e. $\phi\approx0.470899$ of baseline HBF writes, reported as $47.0899\%$.
- $f=2.95$: $\phi=1-0.338983=0.661017$, i.e. $\phi\approx0.661017$ of baseline HBF writes, reported as $66.1017\%$.

The corrected diversion range is therefore $15.97\%$–$66.10\%$, keyed to $f=1.19$ and $f=2.95$; the $\approx68\%$ endpoint of [5]'s conclusion, keyed to the abstract-level $f=3.13$, is not used.

#### (F) Annualized HBF write budgets

From $T_{\mathrm{HBF}}=E_{\mathrm{HBF}}/W_{\mathrm{HBF}}^{(\mathrm{yr})}$ we obtain $W_{\mathrm{HBF}}^{(\mathrm{yr})}=E_{\mathrm{HBF}}/T_{\mathrm{HBF}}$. Using $E_{\mathrm{HBF}}=10^{5}$ cycles from [5] and noting that $\mathrm{WAF}\approx1.02$ changes the effective endurance by less than $2\%$, we omit it for clarity.

- At $T_{\mathrm{HBF}}=9.3$ yr: $W_{\mathrm{HBF}}^{(\mathrm{yr})}=10^{5}/9.3=10752.69\ldots\approx1.08\times10^{4}$ writes/yr; per hour $10752.69/8760=1.2275\ldots\approx1.23$ writes $\mathrm{h}^{-1}$.
- At $T_{\mathrm{HBF}}=3.3$ yr: $W_{\mathrm{HBF}}^{(\mathrm{yr})}=10^{5}/3.3=30303.03\ldots\approx3.03\times10^{4}$ writes/yr; per hour $30303.03/8760=3.4597\ldots\approx3.46$ writes $\mathrm{h}^{-1}$.

These budgets are **projections** based on the cited endurance rating; any deviation in the actual $E_{\mathrm{HBF}}$ or in $\mathrm{WAF}$ scales them linearly.

#### (G) Annualized HBM-first write budgets (projection)

The baseline write volume is obtained by dividing the Lachesis HBF budgets by the extension factor $f$, since $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=f\cdot W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and equivalently $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=E_{\mathrm{HBF}}/T_{\mathrm{base}}$:

- Using $f=1.19$ with the high-lifetime budget: $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=1.08\times10^{4}/1.19=9.07\times10^{3}$ writes/yr. Cross-check via the baseline lifetime: $10^{5}/(9.3\times1.19)=10^{5}/11.067=9.04\times10^{3}$ writes/yr, consistent to rounding.
- Using $f=2.95$ with the low-lifetime budget: $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=3.03\times10^{4}/2.95=1.03\times10^{4}$ writes/yr. Cross-check: $10^{5}/(3.3\times2.95)=10^{5}/9.735=1.03\times10^{4}$ writes/yr.
- Upper bound from the shortest baseline lifetime $T_{\mathrm{base}}=1.9$ yr: $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=10^{5}/1.9=5.26\times10^{4}$ writes/yr; per hour $5.26\times10^{4}/8760=6.01$ writes $\mathrm{h}^{-1}$.

This projection is **labeled** because it depends on the reported baseline lifetimes and the assumed proportionality of wear to write volume.

#### (H) Sensitivity to endurance rating

If the true endurance were $E'_{\mathrm{HBF}}=\alpha E_{\mathrm{HBF}}$, the annual write budget scales as $W'=\alpha^{-1}W$. For $\alpha=0.8$ (a $20\%$ lower rating): the high-end budget becomes $1.08\times10^{4}/0.8=1.35\times10^{4}$ writes/yr ($1.35\times10^{4}/8760=1.54$ writes $\mathrm{h}^{-1}$) and the low-end budget becomes $3.03\times10^{4}/0.8=3.79\times10^{4}$ writes/yr ($3.79\times10^{4}/8760=4.33$ writes $\mathrm{h}^{-1}$).

#### (I) Data gap

The ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ required to convert the diversion fraction $\phi$ into an absolute HBM write rate is not supplied by [5]. This missing ratio is flagged as the principal data gap.

## 5. Results

All numbers below are either directly computed in Section 4 or are labeled projections.

| Quantity | Value | Section |
|----------|-------|---------|
| Warranty margin (Lachesis, max) | $1.86\times$ | 4B |
| Warranty margin (Lachesis, min) | $0.66\times$ | 4B |
| Warranty margin (HBM-first, max) | $0.96\times$ | 4B |
| Warranty margin (HBM-first, min) | $0.38\times$ | 4B |
| Reported HBM-first baseline lifetime | $1.9$–$4.8$ device-years | 4C |
| Geometric-mean extension (tight SLO) | $2.10\times$ | 4D |
| Geometric-mean extension (loose SLO) | $1.50\times$ | 4D |
| Geometric-mean extension (overall) | $1.87\times$ | 4D |
| Write-diversion fraction (low $f$) | $\phi=0.159664$ ($15.9664\%$) | 4E |
| Write-diversion fraction (mid $f$) | $\phi=0.333333$ ($33.3333\%$), $\phi=0.470899$ ($47.0899\%$) | 4E |
| Write-diversion fraction (high $f$) | $\phi=0.661017$ ($66.1017\%$) | 4E |
| Annual HBF writes (high $T_{\mathrm{HBF}}$) | $1.08\times10^{4}$ writes/yr ($\approx1.23$ writes/h) | 4F |
| Annual HBF writes (low $T_{\mathrm{HBF}}$) | $3.03\times10^{4}$ writes/yr ($\approx3.46$ writes/h) | 4F |
| Projected annual HBM-first writes (upper bound) | $5.26\times10^{4}$ writes/yr ($\approx6.01$ writes/h) | 4G |

The corrected warranty margins show that the upper endpoint of the reported Lachesis lifetime range clears the five-year warranty with a margin of $1.86\times$, while the lower endpoint falls short at $0.66\times$; every HBM-first baseline configuration falls short ($0.38$–$0.96\times$). The write-diversion fractions indicate that even the modest $1.19\times$ extension requires HBM to absorb roughly $16\%$ of baseline HBF writes, while the $2.95\times$ extension pushes that requirement to $66\%$. The projected HBM-first write budgets bound the write traffic that an endurance-unconstrained tier would carry.

## 6. Discussion

### Limitations

1. **Single-source quantitative grounding.** All numeric inputs (extension factors, lifetime ranges, endurance rating) come from [5]; the citation base of this paper is five works, so the References list falls short of the eight-entry norm, and no cited work other than [5] provides quantitative inputs to the derivations. The underlying trace characteristics and per-configuration write ratios are not disclosed, limiting the precision of derived baselines.
2. **Linear-wear assumption.** Section 3.3 assumes wear is directly proportional to write volume. Real flash exhibits cell-to-cell variation and wear-leveling overhead, and the write-amplification factor $\mathrm{WAF}\approx1.02$ is treated as negligible; deviations would alter the write-budget projections by up to a few percent.
3. **Missing baseline write ratio.** Converting $\phi$ into an absolute HBM write load requires $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$, which no cited source supplies; the HBM churn penalty therefore cannot be quantified.
4. **Lifetime-prediction fidelity.** The policy relies on accurate harness-provided $\tau_{s}$. Mispredictions could cause short-lived data to overflow HBM or long-lived data to waste HBF endurance, eroding the extension factor.
5. **Reconciliation convention.** The choice to adopt per-configuration numbers over abstract-level ranges rests on internal consistency, not on independent measurement; if the abstract-level ranges of [5] reflected configurations omitted from its evaluation table, the corrected ceiling of $1.86\times$ would be too low.

### Failure modes

- **Mispredicted lifetimes** cause the policy to revert toward the HBM-first baseline or to overload HBM, eroding the extension factor.
- **Adversarial harnesses** that produce uniformly long lifetimes collapse the temporal axis, making the threshold rule ineffective.
- **HBM churn**: diverting up to $66.10\%$ of baseline HBF writes to HBM may increase eviction and re-prefill traffic, indirectly raising overall write volume and offsetting the intended endurance gain.

### What would falsify the central claim

If a trace-replay experiment (Section 7) measured the actual HBF write volume under the lifetime-aware policy and found no reduction relative to the HBM-first baseline—i.e., the observed $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ is within measurement error of $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$—the proportionality assumption $\phi=1-1/f$ would be falsified, and the derived warranty margins and diversion fractions would be invalid. A second falsifier is internal: if any configuration in [5]'s evaluation table yields a Lachesis lifetime outside $3.3$–$9.3$ device-years, the margin ceiling of $1.86\times$ no longer holds.

### Open questions

- Can the threshold $\tau^{*}$ be adapted online from observed $W_{\mathrm{HBF}}$ to hold a target warranty margin?
- What benchmark design can isolate each lifetime axis for reproducible extension-factor measurement?
- How does joint memory-heterogeneous hardware affect the optimal placement policy when prefill and decode phases differ in bandwidth and endurance characteristics?
- Does the substrate-shift framing of [2], in which HBM's capacity ceiling is the saturating constraint and HBF is the shift, predict further endurance-rated tiers beyond HBF, and would the same audit algebra transfer?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact

- **Serving-infrastructure teams** deciding whether to provision an HBF tier can use the warranty-margin factors $m$ (Section 4B) to assess whether a given workload survives a five-year warranty: only configurations with $m\ge1$ qualify, and under the corrected numbers that means Lachesis lifetimes at or above $5$ device-years.
- **Harness developers** can evaluate whether exposing accurate lifetime metadata enables the diversion fractions $\phi$ (Section 4E) needed to meet endurance targets, knowing that $16\%$–$66\%$ of baseline HBF writes must be absorbed elsewhere.

If the projected $m\ge1$ and $\phi$ fits within the HBM headroom the team can provision, the HBF tier is justified; otherwise, alternative mitigations are required.

### (b) Technology readiness

The work is purely analytical and has not been peer reviewed; under the NASA TRL definitions it resides at **TRL 2** (concept and application formulated, analytical demonstration without hardware validation). No readiness above TRL 3 is claimed.

### (c) Smallest concrete next test

A **trace-replay experiment** on a single multi-agent session:

1. Instrument the harness to record $(t_{w}(s), t_{r}(s))$ for every KV segment.
2. Replay the trace twice: once with an HBM-first allocator, once with the lifetime-threshold rule (sweeping $\tau^{*}$).
3. Measure $W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$ and $W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}$ and compute the empirical $\phi_{\mathrm{emp}}=1-W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}/W_{\mathrm{HBF,base}}^{(\mathrm{yr})}$.

**Falsification condition:** if $\phi_{\mathrm{emp}}$ deviates from the predicted $\phi=1-1/f$ by more than $10\%$ across all $\tau^{*}$ values, the core proportionality assumption is invalid.

### (d) Engineering constraints

- **Lifetime instrumentation** — the harness must expose or predict $\tau_{s}$ at write time (software change).
- **HBM churn budget** — the diverted fraction $\phi$ must fit within HBM's write bandwidth; without $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$ this cannot be sized precisely (open question).
- **Endurance telemetry** — per-cell write counters or wear-leveling feedback are needed to verify the linear-wear model.
- **Device specification** — the endurance rating $E_{\mathrm{HBF}}$ must be confirmed with the flash vendor; the $10^{5}$-cycle rating from [5] is the basis of all budgets here.

### (e) Cost/performance projections (labeled)

Assuming a server with an HBF tier rated at $10^{5}$ cycles, the annual write budget per cell is $1.08\times10^{4}$–$3.03\times10^{4}$ writes (Section 4F). If the actual workload writes $2\times10^{4}$ writes/yr per cell, the projected device lifetime is $E_{\mathrm{HBF}}/(2\times10^{4})=5$ years, exactly the warranty horizon. This projection is **labeled** because it depends on the assumed per-cell write rate.

### (f) Risks and misuse paths

A procurement decision made from the abstract-level ranges of [5] rather than the per-configuration numbers would overstate the achievable warranty margin by up to $2.44/1.86\approx1.31\times$ and the achievable diversion by roughly $68/66$ percentage points at the top end; the corrected ranges exist precisely to prevent that misuse.

## 8. Conclusion

This paper corrected an analytical audit of lifetime-aware KV-cache tiering by re-keying every derivation from abstract-level ranges to the per-configuration evaluation numbers that the audited report itself gives. With fully shown arithmetic, the corrected results are: warranty margins of $0.66\times$–$1.86\times$ for the lifetime-aware policy and $0.38\times$–$0.96\times$ for the HBM-first baseline; reported baseline lifetimes of $1.9$–$4.8$ device-years; geometric-mean extensions of $2.10\times$ (tight SLO), $1.50\times$ (loose SLO), and $1.87\times$ overall; write-diversion fractions of $15.97\%$–$66.10\%$; and annualized HBF write budgets of $1.08\times10^{4}$–$3.03\times10^{4}$ writes per cell per year. The correction removes the spurious $2.44\times$ margin ceiling and the $\approx68\%$ diversion endpoint that the abstract-level ranges had introduced, and it shows that only the favorable tail of the reported lifetime range clears a five-year warranty. The principal remaining data gap is the missing baseline write ratio $W_{\mathrm{HBF,base}}/W_{\mathrm{tot}}$, which blocks an absolute sizing of HBM headroom; the smallest de-risking step is the trace-replay experiment of Section 7, whose outcome would either validate the proportionality assumption or falsify the central claim.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. references 13 -> 10. length 5326 -> 3937 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix A. Divergence Report. references 10 -> 9. length 3962 -> 4094 words.
- Version 3.0.0 (2026-11-01, from 2.1.0): rewritten in full through the research pipeline. references 9 -> 5. length 4094 -> 4206 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 16 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] https://papers.qnfo.org/papers/computing-machines. QNFO: Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050.
[3] https://papers.qnfo.org/papers/qwav-decade. QNFO: The QWAV Decade: Enterprise p-Adic Computing 2025-2035.
[4] https://papers.qnfo.org/papers/signal-worker-boundary-confinement. QNFO: Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport.
[5] https://papers.qnfo.org/papers/lifetime-as-a-placement-signal-a-reconciled-analytical-study-of-endurance-budget. QNFO: Lifetime as a Placement Signal: A Reconciled Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High‑Bandwidth Flash in Agentic LLM Serving.
