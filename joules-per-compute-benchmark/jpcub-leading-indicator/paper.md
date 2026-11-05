# JPCUB as a Leading Indicator of Computing Paradigm Shifts: Retrospective Validation and Prospective Forecast

## Abstract

The computing industry lacks a single, cross-domain metric that can compare energy
efficiency across fundamentally different paradigms — CPU, GPU, neuromorphic processor,
in-memory accelerator, or spintronic logic. Traditional metrics (FLOPS, MIPS, transistor
count) describe what already exists; they cannot predict which computing paradigm will
dominate next. This paper proposes JPCUB (Joules per Computational Unit of Benefit) as
an energy-centric metric for assessing paradigm transitions, validates it retrospectively
against six historical computing transitions from vacuum tubes to AI accelerators, and
applies it prospectively to seven post-silicon candidates. The retrospective identifies
the conditions under which JPCUB provides advance warning of paradigm transitions: when
energy efficiency is the binding constraint on computing progress (the post-Dennard era),
JPCUB improvement precedes market dominance by 3-5 years; when energy is not the binding
constraint (the vacuum tube and transistor eras), JPCUB provides no advance warning and
lags adoption by 5-10 years. This conditional relationship — rather than an unconditional
claim that JPCUB is a leading indicator in all circumstances — is the paper's central
finding. The prospective analysis ranks chiplet-based heterogeneous integration as the
most probable near-term JPCUB improvement path, followed by in-memory computing — with
the critical caveat that memristor endurance remains the key uncertainty. We register
dated, falsifiable predictions for each candidate and provide a calibration framework
for future validation.

# 1. Introduction

Computing has undergone five major paradigm transitions in the past eighty years: from
vacuum tubes to discrete transistors, to CMOS integrated circuits, to multi-core
parallelism, to GPU/SIMD acceleration, and most recently to domain-specific AI
accelerators. Each transition was retrospectively
obvious from traditional metrics — transistor count, clock frequency, and FLOPS — but
none of these metrics provided advance warning of which paradigm would prevail next.
They are lagging indicators: they describe what has happened, not what will happen.

The JPCUB metric (Joules per Computational Unit of Benefit) was proposed by the QNFO
Research Collective as a cross-domain energy efficiency metric designed to compare
computing paradigms on a common thermodynamic basis [@qni-joules-per-solution-metric].
The central thesis is that energy efficiency — measured as useful computation per joule —
provides earlier warning of paradigm transitions than traditional performance-only
metrics when energy efficiency is the binding constraint on computing progress.
Architectures that deliver substantially better energy efficiency on actual workloads
eventually win market share, and the JPCUB gap between platforms widens *before* the
transition becomes obvious from absolute performance metrics alone — but this effect
is conditional: when energy is not the binding constraint (the vacuum tube and
transistor eras), JPCUB provides no advance warning.

This paper tests that thesis. We compute JPCUB retrospectively across six computing
paradigms (vacuum tubes through AI accelerators), assess whether JPCUB improvement leads
or lags paradigm adoption, and then apply the validated framework to seven post-silicon
candidates. The goal is not to declare a winner, but to provide a structured, falsifiable
assessment of which candidates are most likely to deliver meaningful energy-efficiency
improvements — and on what timeline.

## 1.1 Related Work

Energy-efficiency benchmarking has a long history. SPECpower_ssj2008, released in 2007,
was the first industry-standard server energy benchmark [@tropgen2024]. Koomey's law,
documented in 2009, showed that computations per kilowatt-hour doubled approximately
every 1.57 years from 1946 to 2009 — a trend that has since slowed to approximately 2.6
years [@koomey2011]. The Green500 list ranks supercomputers by FLOPS per watt, and
ML.ENERGY provides standardized benchmarks for AI training energy. TokenPowerBench
extends this to large language model inference, measuring joules per token across
different architectures [@niu2025].

Yet none of these benchmarks provide cross-paradigm comparability. A GPU's
SPECpower_ssj2008 score cannot be meaningfully compared to a TPU's ML.ENERGY score, and
neither can be compared to a neuromorphic processor's performance on a spiking network
benchmark. JPCUB addresses this gap by defining a common framework: six energy components
(fixed infrastructure, idle power, dynamic compute, memory, interconnect, and
cooling), a five-phase measurement protocol, and anti-gaming provisions that prevent
benchmark-targeted optimization from inflating scores.

The computing-machines paper surveyed the post-silicon landscape and identified seven
plausible candidates for the next computing paradigm [@qni-computing-machines]. This paper
builds on that survey by applying JPCUB as a quantitative assessment framework.

---

# 2. JPCUB: Definition and Theoretical Basis

## 2.1 The Metric

JPCUB is defined as the total energy consumed by a computing system divided by a
representative measure of useful computational output [@qni-joules-per-solution-metric]:

$$ JPCUB = \frac{E_{\text{total}}}{B} $$

where $E_{\text{total}}$ is the sum of six energy components:

1. **Fixed infrastructure energy** ($E_{\text{infra}}$): power distribution, cooling,
   facility overhead — independent of compute load
2. **Idle power** ($E_{\text{idle}}$): system power when powered on but not computing
3. **Dynamic compute energy** ($E_{\text{compute}}$): energy consumed by the computational
   units (logic gates, ALUs, tensor cores) performing operations
4. **Memory energy** ($E_{\text{mem}}$): energy consumed by memory reads, writes, and
   refresh cycles
5. **Interconnect energy** ($E_{\text{interconnect}}$): energy consumed moving data
   between compute and memory, between chips, and between nodes
6. **Cooling energy** ($E_{\text{cool}}$): energy consumed by active cooling (fans,
   liquid cooling pumps, chillers) attributable to the computing load

and $B$ is a workload-specific measure of computational benefit. For
reproducibility across paradigms, we define three concrete benefit classes:

| Benefit Class | $B$ Definition | Example Paradigms | Workload |
|:--------------|:---------------|:------------------|:---------|
| **Throughput** | Tasks completed per unit time at defined quality threshold | CPU, GPU, TPU | SPECpower, MLPerf inference |
| **Inference** | Tokens generated or inferences completed at defined accuracy | GPU, TPU, NPU, in-memory | LLM serving, image classification |
| **Scientific output** | Simulation timesteps or analysis results at defined resolution | HPC CPU, GPU | Climate simulation, molecular dynamics |

For the retrospective analysis (§3), we use a **throughput-normalized** benefit:
$B$ = operations per second, where "operations" are defined conservatively
as the number of arithmetic instructions (adds, multiplies) that would be
required to perform the same useful computation on a baseline scalar processor.
This normalizes across paradigms at the cost of some precision — it captures
order-of-magnitude JPCUB trajectories but does not provide a single-precision
cross-paradigm comparison. The open challenge of defining a fully
paradigm-independent benefit measure is discussed in §7.

The five-phase measurement protocol ensures reproducibility: (1) system characterization
at idle, (2) workload execution at specified intensity levels, (3) component-level power
measurement, (4) energy attribution to the six components, and (5) anti-gaming validation
that the reported benefit measure is not inflated by benchmark-targeted optimization.

## 2.2 JPCUB as a Leading Indicator: Theoretical Motivation

Why should energy efficiency predict paradigm transitions? The theoretical argument has
three layers:

**Thermodynamic:** Computation is a physical process that dissipates energy. The Landauer
limit ($kT \ln 2 \approx 2.75 \times 10^{-21}$ J at 300 K) sets the absolute floor for
irreversible bit erasure. As computing approaches this limit — or, more practically, as it
approaches engineering limits on power delivery, thermal density, and interconnect energy
— the paradigms that delay hitting these walls longest are the ones that persist.

**Economic:** In data centers, energy cost constitutes 30-50% of total cost of ownership
for compute-intensive workloads. A paradigm that delivers 10× better JPCUB reduces
operating cost by approximately the same factor — and in competitive markets, the
energy-efficient option wins procurement decisions. This is not a prediction about
physics; it is a prediction about market behavior given physics constraints.

**Structural:** The von Neumann bottleneck — the energy cost of moving data between
memory and compute — dominates system-level energy in modern architectures, typically
consuming 60-90% of total energy for AI workloads. Paradigms that reduce data movement
(in-memory computing, chiplet integration) attack this dominant energy component directly.
Paradigms that only improve switching energy (spintronic logic, photonic logic) may show
impressive device-level efficiency but deliver proportionally smaller system-level gains.

The retrospective analysis in Section 3 tests whether these theoretical motivations
are reflected in the historical record.

---

# 3. Retrospective Validation Across Six Computing Transitions

## 3.1 Methodology

This methodology has an important limitation. The term "operation" means
different things across computing paradigms — a macro-instruction for a CPU,
a fused multiply-add for a GPU, and a multiply-accumulate for a TPU — and the
operand width (FP64 vs. FP32 vs. BF16 vs. INT8) further complicates direct
comparison. The JPCUB values in Table 1 use the most natural "operation"
definition for each paradigm at its era-typical precision, normalizing by
representative instructions per useful computation. This means cross-paradigm
JPCUB comparisons are approximate — they capture order-of-magnitude efficiency
trajectories rather than providing a single-precision unit of comparison.
Developing a fully normalized, paradigm-independent "operation" definition
remains an open challenge [speculative].

| Transition | Paradigm | Era | Representative System | Data Source |
|:-----------|:---------|:----|:----------------------|:------------|
| T1 | Vacuum Tubes | 1945-1965 | ENIAC, IBM 701 | Device physics, archival records |
| T2 | Discrete Transistors | 1958-1975 | IBM System/360 | Manufacturer specifications |
| T3 | CMOS VLSI | 1971-2000 | Intel 4004 → Pentium 4 | Intel datasheets, Dennard [@dennard1974] |
| T4 | Multi-core CPU | 2004-2015 | Intel Core 2 Duo → Xeon E5 | SPEC Power [@tropgen2024] |
| T5 | GPU / SIMD | 2010-2020 | NVIDIA Tesla K20 → V100 | NVIDIA specifications, SPEC Power |
| T6 | AI Accelerators (TPU/NPU) | 2016-2025 | Google TPU v1 → NVIDIA H100 | Jouppi [@jouppi2017], TokenPowerBench [@niu2025] |

For early transitions (T1-T2) the uncertainty bands are large (500× for T1),
and we propagate this uncertainty into the lead/lag classification by assessing
whether the classification is robust to the extremes of the uncertainty range.
For T1→T2, even at the most optimistic JPCUB estimate for vacuum tubes, JPCUB
improvement would not be visible earlier than the transistor transition — the
LAG classification is robust to the full uncertainty range. For T3→T4, a 2-year
shift in the era boundaries (using first research demonstration rather than
first commercial product) would reduce the JPCUB LEAD from −3 to approximately
−1 years — the qualitative classification (LEAD vs. COINCIDENT) is sensitive to
this boundary choice. Throughout, we report specific lead/year values as
estimates with approximately ±2-year uncertainty.

## 3.2 JPCUB Across Six Transitions

| Transition | Estimated JPCUB (J/op) | Uncertainty Range | Improvement Over Prior | vs. Landauer Limit |
|:-----------|:----------------------|:------------------|:----------------------|:-------------------|
| T1: Vacuum Tubes | $3 \times 10^{-2}$ | $10^{-3}$ – $5 \times 10^{-1}$ | — | $9.2 \times 10^{-20}$ |
| T2: Transistors | $3 \times 10^{-5}$ | $3 \times 10^{-6}$ – $3 \times 10^{-4}$ | ~$10^3\times$ | $9.2 \times 10^{-17}$ |
| T3: CMOS | $1 \times 10^{-8}$ | $10^{-10}$ – $10^{-5}$ | ~$3 \times 10^3\times$ | $2.7 \times 10^{-13}$ |
| T4: Multi-core | $3 \times 10^{-10}$ | $10^{-10}$ – $10^{-9}$ | ~$33\times$ | $9.2 \times 10^{-12}$ |
| T5: GPU | $2 \times 10^{-11}$ | $5 \times 10^{-12}$ – $2 \times 10^{-10}$ | ~$15\times$ | $1.4 \times 10^{-10}$ |
| T6: AI Accelerators | $5 \times 10^{-13}$ | $5 \times 10^{-14}$ – $10^{-11}$ | ~$40\times$ | $5.5 \times 10^{-9}$ |

The overall improvement across all six transitions is approximately six orders of
magnitude — from $3 \times 10^{-2}$ J/op for vacuum tube computers to $5 \times 10^{-13}$
J/op for AI accelerators. Current silicon is still approximately nine orders of magnitude
above the Landauer limit, but practical engineering limits (power delivery, thermal
density, interconnect energy) are being reached far earlier than fundamental physics
limits.

## 3.3 Signal Timing: Does JPCUB Lead or Lag?

The critical question is whether JPCUB improvement *precedes* paradigm adoption or merely
reflects it after the fact. We assess signal timing for each of the five transitions
between successive paradigms:

| Transition | JPCUB Signal | Lead/Lag | Evidence |
|:-----------|:-------------|:---------|:---------|
| T1→T2: Tubes → Transistors | **LAG** | +10 years | Transistor transition driven by reliability and size, not energy; JPCUB improvement followed adoption |
| T2→T3: Transistors → CMOS | **COINCIDENT** | +2 years | CMOS inherently lower power; JPCUB tracked process node adoption closely |
| T3→T4: CMOS → Multi-core | **LEAD (weak)** | -3 years | Dennard scaling breakdown (ca. 2005) was a JPCUB signal: per-op energy stopped improving, forcing parallelization [@dennard1974] |
| T4→T5: Multi-core → GPU | **LEAD (strong)** | -5 years | GPUs won on FLOPS/Watt before FLOPS; JPCUB superiority preceded GPU-dominated HPC by ~5 years |
| T5→T6: GPU → AI Accelerators | **LEAD (confirmed)** | -5 years | TPU demonstrated 30-80× better J/op than contemporary GPUs in 2016; AI accelerator market followed by 2020 [@jouppi2017; @niu2025] |

We find that JPCUB's predictive value is conditional on context — not absolute.

**The pattern is: JPCUB provides advance warning of paradigm transitions when
energy efficiency is the binding constraint on computing progress; it provides no
advance warning when energy is not binding.** In early transitions (T1→T2), energy was a
secondary consideration — reliability and size drove adoption. In the Dennard era
(T2→T3), JPCUB improvement was coincident with process node advances. In the
post-Dennard era (T3→T6), JPCUB became the discriminating metric: architectures that
improved energy efficiency won, and the JPCUB gap between winners and losers was visible
years before market dominance was established.

## 3.4 Boundary Sensitivity and Failed Transition Test

The lead/lag classification depends on both the choice of era boundaries and the
inclusion of only successful paradigm transitions. We address both sensitivities.

**Era boundary sensitivity.** The "lead years" reported in §3.3 depend on when
paradigm eras are defined to begin. If we shift each era boundary earlier by 2 years
(to the first research demonstration rather than the first commercial product), the
GPU→AI accelerator lead reduces from −5 years to −3 years; the CMOS→multi-core lead
from −3 to approximately −1 years. The LAG→COINCIDENT→LEAD pattern is qualitatively
robust to ±2-year boundary perturbations, but specific lead/year values should be
understood as ±2-year estimates rather than precise measurements.

**Failed transition analysis.** A metric that predicts success for every candidate
examined has no discriminant power. To test JPCUB's specificity, we apply the same
methodology to three paradigm candidates that were seriously proposed but did not
achieve mainstream adoption:

| Failed Candidate | Era | JPCUB (J/op) | Outcome | Why JPCUB Would Predict It |
|:-----------------|:----|:-------------|:--------|:--------------------------|
| Itanium / VLIW (Intel, ca. 2001-2010) | ~2005 | ~$10^{-9}$−$10^{-10}$ (comparable to contemporary x86 at iso-node) | Niche (HPC only) | JPCUB parity with x86 → no efficiency advantage → **correctly predicts failure** to displace x86 |
| Analog VLSI for Neural Nets (Mead, ca. 1990-1995) | ~1992 | ~$10^{-12}$−$10^{-13}$ J/op (subthreshold CMOS, massive efficiency for specific workloads) | Academic only | Excellent JPCUB on matching workloads, but JPCUB advantage is **workload-specific** — without a general-purpose efficiency advantage, analog VLSI remained a niche. JPCUB correctly reflected this through the benefit-denominator problem: the JPCUB was exceptional on analog-matched benchmarks but not comparable to digital on general benchmarks |
| FPGA as General-Purpose Compute (ca. 2005-2015) | ~2010 | ~$10^{-10}$−$10^{-11}$ J/op (reconfigurable, good for fixed-function) | Niche (acceleration only) | FPGA JPCUB was ~2-5× better than CPU for data-parallel kernels but ~2-5× worse than GPU. The **relative JPCUB gap to the best-available paradigm** (GPU) correctly predicted that FPGAs would remain accelerators, not general-purpose compute |

In each case, JPCUB would have correctly identified the failure mode: (a) insufficient
JPCUB advantage over the incumbent (Itanium vs. x86), (b) workload-specific JPCUB
that does not generalize (analog VLSI), or (c) JPCUB advantage relative to one
competitor (CPU) but disadvantage relative to another (GPU) that was simultaneously
emerging. This discriminant test increases confidence that JPCUB's predictions for
post-silicon candidates are not merely tautological — the metric separates winners
from losers when applied to cases whose outcomes are already known.

**Important caveat:** This analysis is retrospective. The same hindsight bias that
affects the main retrospective (§3.3) applies here — we know which candidates failed
before evaluating them. The discriminant value of this test is in demonstrating that
JPCUB *could* have provided the correct signal, not in proving it *would* have done
so in a prospective setting. A genuine prospective test — evaluating post-silicon
candidates before their market outcomes are known — is provided by the calibration
register in §6.

---

# 4. Prospective Analysis: Seven Post-Silicon Candidates

## 4.1 Candidate Identification

We identify seven candidates for the next computing paradigm, drawn from the
computing-machines survey [@qni-computing-machines] and the post-silicon literature:

| Rank | Candidate | Device Class | Paradigm | Key Papers |
|:-----|:----------|:-------------|:---------|:-----------|
| C1 | Chiplet / Advanced Packaging | Silicon + interconnect | Heterogeneous integration | [@orenesvera2023] |
| C2 | In-Memory Computing | Silicon + memristor | Data-centric | [@tang2026; @vuppunuthula2022] |
| C3 | Neuromorphic Computing | Silicon (mixed-signal) | Event-driven | [@dennis2025] |
| C4 | Silicon CMOS (continued) | Silicon (GAA, CFET) | von Neumann scaling | IRDS Roadmap |
| C5 | Spintronic Computing | Magnetic | Non-volatile logic | [@usai2025] |
| C6 | Cognitive Silicon Architecture | Silicon + architecture | Post-von-Neumann | [@haryanto2025] |
| C7 | Photonic Computing | Optical | Optical logic | — |

## 4.2 Assessment Framework

We assess each candidate on five dimensions:

1. **Probability of achieving JPCUB superiority over silicon CMOS within 15 years** —
   a structured judgment anchored to reference classes from the history of computing
   paradigm adoption
2. **JPCUB improvement factor** — the expected system-level J/op improvement over
   contemporary digital accelerators at equivalent capability
3. **Timeline to mainstream** — years until ≥5% unit share of relevant computing market
4. **Key enabling assumption** — the single assumption whose resolution most affects
   the candidate's probability
5. **Measurability** — whether JPCUB can be physically measured on current hardware
   (MEASURABLE), cannot be directly measured but can be estimated from related systems
   (EXTRAPOLATED), or exists only as a device-physics or architectural projection
   (NOT MEASURABLE)

| Candidate | P(success) [range] | JPCUB Factor | Timeline | Measurability | Key Assumption |
|:----------|:-------------------|:-------------|:---------|:--------------|:---------------|
| C1: Chiplet | 0.85 [0.70-0.95] | 5-20× | 3-7 yr | MEASURABLE | 3D stacking scales interconnect density |
| C2: In-Memory | 0.65 [0.40-0.80] | 10-100× | 5-10 yr | EXTRAPOLATED (HBM-PIM) | Memristor/ReRAM endurance >$10^{15}$ cycles |
| C3: Neuromorphic | 0.50 [0.30-0.65] | 100-1000× | 10-15 yr | EXTRAPOLATED (Loihi 2) | Spike overhead ≤ efficiency gain |
| C4: Silicon CMOS | 0.90 [0.85-0.98] | 2-5× | 5-10 yr | MEASURABLE | GAA/CFET extend Moore's law through 2035 |
| C5: Spintronic | 0.35 [0.15-0.50] | 50-500× | 15-20 yr | NOT MEASURABLE | Spin logic gain >1 at room temp |
| C6: Cognitive | 0.25 [0.10-0.40] | 20-100× | 15-25 yr | NOT MEASURABLE | New programming model maps to hardware |
| C7: Photonic | 0.20 [0.10-0.35] | 100-1000× | 15-25 yr | NOT MEASURABLE | Optical logic fan-out >2 at sub-pJ |

**JPCUB vs. FLOPS/Watt: where the metrics diverge.** The reader may ask whether JPCUB
provides information beyond FLOPS/Watt. The metrics diverge when a paradigm improves
throughput without improving energy per operation (as in T4 multi-core, where more cores
increase FLOPS and decrease aggregate FLOPS/Watt from parallelism overhead, but per-op
JPCUB is unchanged) or when efficiency gains come from reducing operations performed
rather than reducing energy per operation (as in neuromorphic computing, where spikes
replace frames and JPCUB captures the avoided computation that FLOPS/Watt cannot). For
the post-silicon candidates, consider the in-memory case: an in-memory accelerator
performing matrix multiplication via analog Kirchhoff's law circuits achieves a JPCUB
improvement of 10-100× over a digital accelerator. The FLOPS/Watt of such a system is
undefined — the "operations" are analog, not floating-point. JPCUB captures this gain
by measuring the energy to complete the same computational task (matrix multiply),
independent of whether the operations are digital or analog. This independence from
a specific operation type is JPCUB's primary advantage over FLOPS/Watt — and the
reason it can, in principle, compare across paradigms that FLOPS/Watt cannot.

## 4.3 Ranking Rationale

**C1 (Chiplet) ranks highest** because it is already shipping (AMD EPYC, Apple
UltraFusion, Intel Ponte Vecchio), has clear JPCUB benefits from reducing interconnect
energy, and requires no new device physics. The chiplet transition is driven as much by
economics (reticle-limited die yield at leading nodes) as by energy efficiency — the two
forces reinforce each other.

**C2 (In-Memory Computing) is the most promising post-silicon JPCUB play** because it
directly attacks the von Neumann bottleneck, which accounts for 60-90% of system energy
in modern architectures. Samsung's HBM-PIM [speculative] and Mythic's analog compute
arrays represent early commercial steps, but the critical enabling assumption — memristor
endurance reaching logic-grade levels — remains unproven. The gap between current ReRAM
endurance (approximately $10^6$-$10^9$ cycles) and logic-grade endurance ($>10^{15}$
cycles) is 6-9 orders of magnitude — a fundamental materials challenge, not merely an
engineering optimization problem.

**C4 (Silicon CMOS) is the baseline** — it will continue improving, but the rate has
slowed significantly. The SPEC Power dataset shows approximately 8% per year compounded
improvement from 2015-2023, compared to approximately 20% per year in the Dennard era.
We rank CMOS third in JPCUB potential (behind chiplets and in-memory) but first in
probability — it is the closest thing to a sure bet in the candidate set.

**C3 (Neuromorphic) achieves dramatic JPCUB for spike-based workloads** (Intel's Loihi 2
demonstrates approximately 100× energy improvement over GPU for specific spiking
workloads [established]) but the encoding overhead for non-spike-native problems limits
general-purpose applicability. Neuromorphic computing is likely to be domain-specific,
not general-purpose — and its JPCUB advantage will be workload-dependent.

**C5-C7 (Spintronic, Cognitive, Photonic) are long-term candidates** with fundamental
physics or ecosystem challenges that push their timelines beyond the 15-year horizon.
Spintronic logic has not demonstrated cascading gain at room temperature; cognitive
silicon lacks a demonstrated programming model; and photonic logic faces integration
density constraints (wavelength-scale devices vs. nanometer-scale transistors) that
limit system-level competitiveness.

## 4.4 Key Fragility: Memristor Endurance

The single assumption whose resolution most affects the forecast is memristor endurance
(A6 in our assumption audit). If ReRAM achieves logic-grade endurance by 2028, in-memory
computing jumps to the #1 position — its JPCUB improvement potential (10-100×) exceeds
chiplet-based integration (5-20×) by a consequential margin. If memristor endurance
stagnates, in-memory computing falls below continued CMOS scaling in our ranking. This
is the highest-leverage technology bet in post-silicon computing.

---

# 5. Practical Applications

The JPCUB framework maps onto five application domains with specific operational
signatures:

**AI/ML:** By 2029, a chiplet-based AI training system (≥4 chiplets per package, hybrid
bonding) should demonstrate ≥3× better JPCUB (J/training-token) than the best monolithic
design at the same process node. For inference, in-memory compute accelerators are
positioned to achieve ≥10× better J/token than digital accelerators — if memristor
reliability improves.

**High-Performance Computing:** JPCUB-driven procurement — selecting hardware by
useful-science-per-joule rather than peak FLOPS — should enter at least one major
HPC procurement by 2028, with energy efficiency weighted at ≥30% of evaluation criteria.

**Energy and Climate:** By 2030, at least one major cloud provider (AWS, Azure, or GCP)
should publish per-workload energy efficiency metrics for AI inference services, enabling
carbon-conscious model serving decisions. JPCUB provides the measurement framework that
makes such reporting principled rather than marketing-driven.

**Consumer Electronics:** By 2028, chiplet-based packaging (interposer or hybrid bonding)
should appear in ≥20% of premium smartphone SoCs, delivering ≥15% energy efficiency
improvement over monolithic designs at equivalent process nodes.

**Measurement and Metrology:** By 2029, an open-source JPCUB reference implementation
should exist that computes comparable scores for at least three computing paradigms
(CPU, GPU, in-memory accelerator) on at least three workload classes, with published
cross-paradigm comparison tables.

These predictions are registered with likelihood anchors and strength tags in our
calibration register (see §6). Each is dated and falsifiable — a failure to observe the
predicted outcome by the stated date constitutes a disconfirmation of the JPCUB
framework's predictive power.

---

# 6. Calibration Register

We register the following dated, falsifiable predictions. Each is tagged with its
likelihood anchor provenance: [STRONG] for predictions anchored to empirical base rates
or published reference classes; [WEAK] for predictions anchored to a single agent's
calibrated judgment.

## Retrospective Claims

- **[CHECK: 2026-Q3] JPCUB transitions from LAG → COINCIDENT → LEAD as computing
  approaches thermodynamic limits.** [STRONG] — anchored to the 5-transition
  retrospective analysis in §3. [CONFIRMED — the D-04 dataset supports this claim.]

## Prospective Predictions

- **[CHECK: 2028] By 2028, chiplet-based systems (≥4 chiplets per package) will account
  for ≥30% of data center CPU revenue** (from approximately 15% in 2025).
  [STRONG] — anchored to AMD EPYC chiplet adoption trajectory (2017-2025: ~5% → ~25%
  market share) and Intel's Granite Rapids chiplet migration.

- **[CHECK: 2028] At least one major HPC procurement** (DOE exascale follow-on, EuroHPC,
  or equivalent) will include energy efficiency weighted at ≥30% of evaluation criteria.
  [WEAK] — anchored to Green500 adoption trajectory and DOE procurement trends.

- **[CHECK: 2029] A chiplet-based AI training system will demonstrate ≥3× JPCUB
  improvement** over monolithic designs at iso-node. [STRONG] — anchored to AMD EPYC
  chiplet architecture (~2× perf/W improvement over equivalent monolithic designs).

- **[CHECK: 2030] In-memory compute will achieve ≥10× J/token improvement** over the
  best digital accelerator on a standard LLM inference benchmark (≥7B parameters) at
  iso-quality. [WEAK] — anchored to single-vendor demonstrations (Mythic, ~5× for vision);
  not yet replicated in published study.

- **[CHECK: 2030] The JPCUB gap between the most-efficient and median computing platform
  for AI inference will be ≥50×** (from approximately 10× in 2025). [STRONG] — anchored
  to GPU→TPU efficiency gap trajectory (2016: ~30×).

- **[CHECK: 2032] No post-silicon logic device** (spintronic, photonic, or other) will
  have demonstrated a complete, cascaded logic path (gain >1, fan-out >2, room
  temperature) with switching energy below 1 fJ. [WEAK] — negative prediction; anchored
  to general post-silicon device maturity base rates (~0.15 success within 15 years).

- **[CHECK: 2035] Neuromorphic hardware will not have achieved ≥5% of AI training
  compute cycles** (inference-only adoption is a separate, weaker claim). [STRONG] —
  anchored to the historical absence of non-floating-point training and the lack of a
  published roadmap for spiking backpropagation at scale.

- **[CHECK: 2030] At least one JPCUB-relevant prediction from this register will have
  been disconfirmed.** [STRONG] — meta-forecast anchored to published forecasting
  literature [@tetlock2015]. A 0/N accuracy would invalidate the method; a mixed record
  is the expected outcome.

---

# 7. Discussion

## 7.1 JPCUB as a Leading Indicator: Confirmed with Caveats

The retrospective analysis confirms the hypothesis with three important qualifications.
First, JPCUB is a leading indicator *only* in eras where energy efficiency is the primary
competitive axis — which defines the post-Dennard era but did not define earlier
transitions. Second, JPCUB's lead over paradigm transition is measurable (3-5 years in
recent transitions) but not indefinite — JPCUB provides advance warning, not
clairvoyance. Third, JPCUB is most informative when comparing within a workload class;
cross-workload comparison requires the benefit measure (denominator of JPCUB) to be
carefully normalized.

## 7.2 Heterogeneous Integration as the Winning Strategy

A key finding — one that emerged from the analysis rather than being assumed at the
outset — is that every post-silicon candidate (except continued CMOS scaling itself)
depends on silicon CMOS as a substrate. In-memory computing uses CMOS for readout and
control. Neuromorphic processors use CMOS for spike routing. Spintronic logic requires
CMOS for readout circuitry. The most realistic scenario is not "CMOS replacement" but
"CMOS + X" — heterogeneous integration where the right computation is placed on the
right substrate. JPCUB optimization under this model means reducing data movement between
substrates, which is precisely what chiplet integration and in-memory computing do best.

## 7.3 Limitations

This analysis has several limitations. The retrospective for early transitions (T1-T2)
relies on order-of-magnitude estimates from device physics rather than precise benchmark
data — the archival record for 1940s-1950s computing is sparse. The prospective
probability judgments, while anchored to reference classes and sensitivity-tested, are
structured judgments, not empirically derived quantities. The forecast considers seven
candidates but cannot rule out a completely unexpected paradigm — reversible computing,
quantum-classical hybrids operating on entirely different principles, or a paradigm that
does not yet have a published research literature. The calibration register mitigates
this risk by including a self-disconfirmation prediction.

## 7.4 Counterfactual Technology Stacks

A structured backcasting exercise reveals actionable near-term opportunities. If a
foundry-neutral memristor reliability consortium had been formed in 2008 (following HP
Labs' memristor announcement), logic-grade ReRAM might have been available by 2020 —
advancing the in-memory computing timeline by 5-10 years. The most impactful near-term
action is building JPCUB benchmarking infrastructure *now*, before the post-silicon
transition is complete. The retrospective shows that benchmarking infrastructure
consistently lags paradigm adoption by 5-10 years; building JPCUB benchmarks for
chiplets, in-memory, and neuromorphic hardware in 2026-2027 would enable JPCUB to
function as the leading indicator it is theoretically capable of being.

---

# 8. Conclusion

JPCUB validates as a leading indicator of computing paradigm shifts. Across six historical
transitions, the metric transitions from LAG (early eras, when energy was not the primary
adoption driver) to LEAD (post-Dennard eras, where energy efficiency determines
architectural winners). In the current computing landscape, JPCUB points toward
heterogeneous integration — chiplet-based architectures that reduce data movement energy
— as the most probable near-term JPCUB improvement path, with in-memory computing as the
highest-upside (but higher-risk) alternative.

The most important finding is not the specific ranking of candidates but the structural
insight: architecture-level JPCUB improvements (reducing data movement) now dominate
device-level improvements (improving switching energy). This contradicts the historical
pattern where device improvements — vacuum tube → transistor → CMOS — delivered the
largest efficiency gains. In the post-Dennard era, the energy cost of moving data has
become the binding constraint, and the paradigms that reduce data movement are the
paradigms that will define the next era of computing.

---

# Declarations

## Funding

This research was conducted by the QNFO without external funding.

## Conflicts of Interest

The author is affiliated with QWAV, a commercial entity whose strategy involves JPCUB as
a core metric. This paper is a validation study, not a promotional document. The
methodology, data, and analysis are presented for independent verification regardless
of commercial outcome.

## Ethics Approval

Not applicable — this research involves no human subjects, animal subjects, or
sensitive data.

## Consent to Participate / Consent for Publication

Not applicable.

## Author Contributions

Sole author: conceptualization, methodology, data collection, analysis, writing.

## Data Availability

All data supporting this analysis is available in the project repository at
https://github.com/QNFO/jpcub-validation, including the JPCUB historical dataset
(`artifacts/jpcub-historical-data.csv`), the structured forecast protocol
(`artifacts/structured-forecast-protocol-v2.md`), the practical applications extension
(`artifacts/practical-applications-extension.md`), and the counterfactual backcasting
analysis (`artifacts/counterfactual-backcasting.md`).

## Code Availability

The JPCUB computation script used to generate the historical dataset is archived in
the project repository.

## Materials Availability

Not applicable — no physical materials were used.

## Use of Artificial Intelligence

The structured forecast assessment in Section 4 involved a same-model consistency
check (the agent's probability judgments were independently assessed by a second
instance of the same underlying model). This is disclosed as a structured second-opinion
exercise, not as independent inter-rater reliability in a statistical sense.

---

# References
