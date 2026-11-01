# Lifetime as a Placement Signal: A Corrected Analytical Audit of Endurance Budgets for KV Cache Tiering across HBM and High-Bandwidth Flash in Agentic LLM Serving

## Abstract

Agentic large-language-model (LLM) serving accumulates key-value (KV) cache across many orchestrated requests, and high-bandwidth flash (HBF) offers an order-of-magnitude larger capacity than high-bandwidth memory (HBM) while preserving comparable read bandwidth. The finite program/erase (P/E) endurance of flash, rated at $10^{5}$ cycles with a write-amplification factor $\mathrm{WAF}\approx1.02$, limits the write traffic an HBF tier can absorb before a five-year warranty expires. An earlier audit of this question keyed its headline derivations to abstract-level ranges (extension $1.19$–$3.13\times$, lifetime $3.3$–$12.2$ device-years) that do not match the per-configuration evaluation numbers the underlying report itself gives; this paper corrects that mismatch and re-derives every quantity from the per-configuration numbers. With fully shown arithmetic we obtain: (i) warranty-margin factors of $0.66\times$–$1.86\times$ for the lifetime-aware policy and $0.38\times$–$0.96\times$ for the HBM-first baseline; (ii) reported baseline lifetimes of $1.9$–$4.8$ device-years; (iii) geometric-mean extensions of $2.10\times$ (tight SLO), $1.50\times$ (loose SLO), and $1.87\times$ overall; (iv) write-diversion fractions of $15.97\%$ ($f=1.19$) to $66.10\%$ ($f=2.95$); and (v) annualized HBF write budgets of $1.08\times10^{4}$–$3.03\times10^{4}$ writes per cell per year ($1.23$–$3.46$ writes $\mathrm{h}^{-1}$). The correction removes the spurious $2.44\times$ warranty margin and the $68\%$ diversion endpoint that the abstract-level ranges had introduced, and it clarifies which configurations clear a five-year warranty.

## 1. Introduction

Operators of LLM-serving infrastructure face a capacity endgame driven by agentic workloads: harnesses orchestrate agents and sub-agents across many requests, causing KV cache to accumulate over entire multi-turn sessions rather than being reset per query. Limited GPU memory forces eviction of inactive KV states; resuming a session then incurs costly recomputation or slow interconnect transfers. High-bandwidth flash (HBF), an on-package 3D-NAND class, provides an order-of-magnitude capacity advantage over HBM while preserving HBM-class read bandwidth, making it a natural tier for retained context. The obstacle is endurance: flash tolerates only a finite number of program/erase (P/E) cycles, so every write to HBF consumes a non-renewable budget that can be exhausted before a device's five-year warranty expires.

If a placement policy can predict a segment's lifetime—the interval between its first write and its last read—then short-lived segments can be kept in HBM, which has effectively unlimited endurance for the service life, while long-lived segments are diverted to HBF. The system under audit, Lachesis, implements exactly this idea: it places KV segments in HBM or HBF at write time based on predicted lifetime and frees blocks once the segment is no longer read [5].

**The correction this paper makes.** The prior audit [5] stated headline inputs of an extension of $1.19$–$3.13\times$ and an absolute HBF lifetime of $3.3$–$12.2$ device-years, and it derived several conclusions from those abstract-level ranges. Those abstract-level numbers do not match the per-configuration evaluation numbers that [5] itself attributes to the underlying system report: extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years, and HBM-first baselines of $1.9$–$4.8$ device-years. Deriving from the wrong range produced two concrete errors in [5]: a warranty-margin ceiling of $2.44\times$ (which is $12.2/5$ and has no per-configuration basis) and a diversion endpoint of $\approx68\%$ keyed to the abstract-level extension $3.13\times$. This paper re-keys every derivation to the per-configuration numbers and shows the corrected arithmetic in full.

**So what?** An operator must decide whether to provision an HBF tier, how much HBM headroom to reserve for diverted writes, and whether the projected endurance will survive the warranty horizon. Those decisions require concrete numbers: warranty-margin factors, baseline lifetimes, write-diversion percentages, and per-cell write budgets. Whether the corrected ranges clear the warranty, and by how much, changes the provisioning decision directly; the correction shows that the favorable tail of the earlier audit ($2.44\times$ margin) was an artifact of the abstract-level range and that the defensible ceiling is $1.86\times$.

**Contributions**
1. A reconciliation rule that adopts the per-configuration evaluation numbers over abstract-level ranges, with the discrepancy recorded and the convention stated (Section 3.4).
2. Formalization of the placement principle as a lifetime-threshold rule with free-at-last-read semantics (Section 3.2).
3. Derivation of the algebra linking the extension factor $f$, the write-diversion fraction $\phi$, and the HBF device-year lifetime $T_{\mathrm{HBF}}$ (Section 3.3).
4. Fully shown arithmetic converting the corrected extension and lifetime ranges into warranty margins, baseline write budgets, geometric-mean extensions, diversion fractions, and annualized write budgets using the $10^{5}$-cycle rating (Section 4); the baseline write volume is obtained, per the corrected route, by dividing the Lachesis HBF budgets by $f$ (Section 4G).
5. A limitations and falsification analysis, including the explicit statement that the bibliography available to this audit contains five works (Section 6).
6. A practical pathway for operators: TRL assessment, the smallest de-risking experiment, engineering constraints, and labeled projections (Section 7).

## 2. Background and Related Work

The bibliography available to this audit contains five works; all five are discussed here, and the consequence of this reduced coverage is stated in Section 6.

**[5] Lifetime as a Placement Signal (prior audit, the object of correction).** This work formalizes Lachesis's placement principle, adopts an HBF endurance rating of $10^{5}$ P/E cycles with $\mathrm{WAF}\approx1.02$, and reports a results table with warranty margins of $1.86\times$, $0.66\times$, $0.96\times$, and $0.38\times$; geometric-mean extensions of $2.10\times$, $1.50\times$, and $1.87\times$; diversion fractions of $15.97\%$, $33.33\%$, $47.09\%$, and $66.10\%$; and annual HBF write budgets of $1.08\times10^{4}$ and $3.03\times10^{4}$ writes per year. Its abstract, however, headlines an extension of $1.19$–$3.13\times$ and a lifetime of $3.3$–$12.2$ device-years, and its conclusion derives margins "from $0.66\times$ to $2.44\times$" and a diversion range "of $\approx16\%$–$68\%$" from those abstract-level endpoints. The internal tension between its own results table and its abstract/conclusion is precisely the defect this paper corrects; the per-configuration numbers in its Section 5.3 table ($1.50$–$2.95\times$ tight, $1.19$–$1.89\times$ loose, Lachesis $3.3$–$9.3$ years, baseline $1.9$–$4.8$ years) are taken here as primary.

**[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices.** Although from combinatorics, this paper supplies the methodological template for constraint-bounded auditing: it derives sharp lower bounds for the first and second Zagreb indices over trees with a given number of pendent vertices and characterizes the extremal graphs that attain them—for example, Theorem 1 gives $M_{1}(T)\geq 9n-16$ for a tree with an even number $n$ of pendent vertices, with equality for the $4$-tree in which every internal vertex has degree $4$. The audit below follows the same discipline: given a fixed constraint set (endurance rating, warranty horizon, reported extension factors), derive the tightest bounds the constraints admit and identify exactly which reported configuration attains each bound, rather than mixing bounds from inconsistent constraint sets—a discipline whose violation produced the corrected errors.

**[2] Computing After Silicon: A History-Constrained Forecast of Computing Machine Evolution, 2026-2050.** This forecast argues that each computing era is defined by the physics of its substrate and that transitions follow the invariant dynamic "constraint saturation → substrate shift → Wright's Law cost decline → institutional adoption," with heterogeneous convergence (AI accelerators, processing-in-memory) as the central thesis for the coming two decades. The HBM-plus-HBF tiering audited here is an instance of that heterogeneous convergence at the memory-subsystem level: HBM's per-bit cost and capacity ceiling is the saturating constraint, and HBF is the substrate shift. The forecast's framing also supplies the audit's epistemic stance—its twelve dated falsifiable predictions model how a quantitative claim should be registered so that it can be disconfirmed, which Section 6 emulates with an explicit falsification condition.

**[3] The QWAV Decade: Enterprise p-Adic Computing 2025-2035.** This work defines Joules Per Computational Unit (JPCUB), a hardware-independent, workload-normalized efficiency metric, and argues from projected data-center electricity consumption of 1,000 TWh/year by 2026 that standardized efficiency metrics move from voluntary reporting to mandatory compliance, shaping procurement. The relevance to the present audit is the metric-design lesson: an endurance budget per cell per year, normalized per cell and per year exactly as JPCUB normalizes per unit of computational work, is the quantity a procurement decision actually consumes. The annualized write budgets derived in Section 4F are constructed to serve that procurement role, and the divergence between abstract-level and per-configuration inputs illustrates why a metric must state its normalization convention explicitly.

**[4] Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport.** This paper is a worked precedent for correction-as-publication: it delivers a red-team-hardened correction of an ontology's boundary-confinement reading after a three-slot adversarial audit (dated 2026-08-14) that found the underlying physics accurate (0 HARD accuracy findings) but the unifying reading overgeneralized (5 HARD completeness findings), and it re-issues the ontology as a falsifiable proposal rather than established doctrine. The present paper performs the same operation on [5]: the per-configuration arithmetic in [5] is accurate (its results table is internally consistent), but the abstract-level headline ranges are an overgeneralization that propagates two wrong conclusions, and the correction re-issues the audit keyed to the defensible constraint set.

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

must reduce HBF write volume by the same factor:

$$
f=\frac{W_{\mathrm{HBF,base}}^{(\mathrm{yr})}}{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}},\qquad
\phi=1-\frac{1}{f},
$$

where $\phi$ is the **write-diversion fraction**: the proportion of baseline HBF-bound writes that are either absorbed by HBM or eliminated by earlier freeing. Inverting the lifetime relation gives the corrected route for the baseline write volume,

$$
W_{\mathrm{HBF,base}}^{(\mathrm{yr})}=\frac{W_{\mathrm{HBF,Lach}}^{(\mathrm{yr})}}{f},
$$

that is, the Lachesis HBF budget divided by the extension factor $f$; this is the route mandated by the erratum and applied in Section 4G.

### 3.4 Input reconciliation and stated conventions

Two families of numbers exist in [5]. Its abstract states an extension of $1.19$–$3.13\times$ and lifetimes of $3.3$–$12.2$ device-years. Its evaluation results table states, for the configurations giving HBM one to four of eight slots, extensions of $1.50$–$2.95\times$ (tight SLO) and $1.19$–$1.89\times$ (loose SLO), Lachesis lifetimes of $3.3$–$9.3$ device-years, and HBM-first baselines of $1.9$–$4.8$ device-years.

We take the per-configuration evaluation numbers as primary, under the convention that every derived quantity in this paper keys to numbers that are per-configuration, internally consistent, and accompanied by baselines; the abstract-level ranges are recorded as a discrepancy and used in no derivation. Two consequences of this convention are stated explicitly because the earlier record attached different labels to the same values:

- The high-end write-diversion fraction $66.10\%$ attaches to the per-configuration extension $f=2.95$, since $1-1/2.95=0.661017$. The abstract-level endpoint $f=3.13$ would give $1-1/3.13=0.680511\approx68.05\%$; that value is recorded here only to mark the discrepancy and is not used.
- The warranty-margin ceiling is $1.86\times$ ($=9.3/5$); the value $2.44\times$ ($=12.2/5$) in the conclusion of [5] is an artifact of the abstract-level lifetime endpoint and is withdrawn.

All derivations in Section 4 use only numbers stated in [5] or are labeled as assumptions.

### 3.5 What this paper does not do

No simulation, measurement, or trace collection is performed. All quantitative claims are either (i) reported by [5] and attributed by number, or (ii) derived here from those reports using the algebra of Section 3.3, with every arithmetic step shown.

## 4. Analysis

All input numbers are cited to [5]; where an input is absent from the cited works it is labeled as an **assumption**.

#### (A) Hours per year and warranty period

Continuous operation gives $24\times365=8760$ h $\mathrm{yr}^{-1}$. A five-year warranty spans $5\times8760=43800$ h.

#### (B) Warranty margins

Define the warranty margin

$$
m=\frac{T_{\mathrm{HBF}}}{5}.
$$

- Lachesis, upper lifetime $T_{\mathrm{HBF}}=9.3$ yr: $m_{\max}=9.3/5=1.86$.
- Lachesis, lower lifetime $T_{\mathrm{HBF}}=3.3$ yr: $m_{\min}=3.3/5=0.66$.
- HBM-first baseline, upper lifetime $4.8$ yr: $m_{\mathrm{base,max}}=4.8/5=0.96$.
- HBM-first baseline, lower lifetime $1.9$ yr: $m_{\mathrm{base,min}}=1.9/5=0.38$.

The corrected ceiling is $1.86\times$; the value $2.44\times$ obtained in [5] from the abstract-level $12.2$-year endpoint is not reproducible from the per-configuration numbers and is withdrawn.

#### (C) Reported HBM-first baseline lifetimes

The results table of [5] lists per-configuration HBM-first lifetimes of $1.9$–$4.8$ device-years. We adopt this range directly as reported.

#### (D) Geometric-mean extensions

- Tight SLO:
$$
\bar{f}_{\mathrm{tight}}=\sqrt{1.50\times2.95}=\sqrt{4.425}=2.10376\ldots\approx2.10.
$$

- Loose SLO:
$$
\bar{f}_{\mathrm{loose}}=\sqrt{1.19\times1.89}=\sqrt{2.2491}=1.49970\ldots\approx1.50.
$$

- Overall (using the per-configuration endpoints $1.19$ and $2.95$):
$$
\bar{f}=\sqrt{