# Phase 1 Due Diligence Report — Joules-per-Compute Universal Benchmark (JPCUB)

**Date:** 2026-07-27 | **Phase:** 1 | **Status:** Complete
**Author:** QNFO
**Disclosures:** CONFIRMATION-BIAS-RISK, CROSS-DOMAIN-CONSILIENCE-QUALIFYING

---

## §1. Internal QNFO Discovery

### §1.1 Vectorize Semantic Search (7 domains queried)

All seven domain queries returned the SAME set of QNFO-internal papers with no external literature:

| Domain Query | Top Result | Score | Source |
|:-------------|:-----------|:------|:-------|
| Quantum computing energy efficiency | "The Physics of Computation" | 0.743 | QNFO-internal |
| AI training energy cost | "Differential LLM Inference" | 0.704 | QNFO-internal |
| Post-quantum cryptography energy | "Ultrametric Quantum Computation" | 0.743 | QNFO-internal |
| Data center energy efficiency PUE | "Ultrametric Quantum Computation" | 0.660 | QNFO-internal |
| CPU ISA energy efficiency benchmark | "Ultrametric Quantum Computation" | 0.650 | QNFO-internal |
| Neuromorphic computing energy efficiency | "The Physics of Computation" | 0.730 | QNFO-internal |
| Edge/IoT inference energy benchmark | "The Problem-Substrate Mapping" | 0.672 | QNFO-internal |

### §1.2 Confirmation-Bias Disclosure (KIF-29 / research skill §C3)

**[CONFIRMATION-BIAS-RISK: only internal corpus searched across all 7 domains.]** The QNFO Vectorize index contains ONLY QNFO-authored papers. 100% of results across all seven domain queries are self-referential. This is NOT external corroboration — it is the corpus searching itself. No "literature confirms" claim can be made from Vectorize alone. External validation required (see §2).

### §1.3 Knowledge Graph (2,455 nodes, 1,492 edges)

Paper nodes exist for the Qubit Delusion series (5 papers), BQNN v2, and ultrametric quantum computation papers. No external Paper nodes exist in the KG. The KG is QNFO-internal only.

### §1.4 Prior Relevant QNFO Publications

| Paper | Relevance to JPCUB | Score |
|:------|:-------------------|:------|
| The Physics of Computation (2026-07-08) | Landauer/Margolus-Levitin/Bremermann limits — the theoretical foundation | 0.743 |
| The Qubit Delusion (2026-07-08) | $35B investment, zero commercially viable QC — diagnosed the failure mode | 0.723 |
| The Problem-Substrate Mapping (2026-07-08) | "The substrate IS the algorithm" — honest computational investment | 0.711 |
| Manifesto for Honest Computation (2026-07-08) | "Joules per solution as the universal metric" — the direct precursor | 0.686 |
| Institutional Reform (2026-07-08) | Fixing the epistemic incentive structure | 0.685 |
| BQNN v2 (DOI 10.5281/zenodo.21623218) | Demonstrated classical GPU beats quantum proposals on joules-per-solution | 0.710 |

**Verdict:** The QNFO internal corpus provides the theoretical foundation (physical limits, joules-per-solution metric, institutional critique) but DOES NOT contain any cross-domain empirical benchmarking data — that is the gap JPCUB fills.

---

## §2. External Literature Discovery

### §2.1 arXiv API Results (7 domains, 42 papers total)

#### S1 — Quantum Computing (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| "Quantum Computing: Vision and Challenges" (2403.02240) | 2024 | Survey — mentions challenges but not joules-per-gate |
| "Tianyan: Cloud services with quantum advantage" (2512.10504) | 2025 | Claims quantum advantage without energy audit |
| "Harnessing Quantum Computing for Energy Materials" (2601.16816) | 2026 | Uses QC FOR energy optimization, not measuring QC's energy |

**Finding:** ZERO papers measure quantum computing's own energy consumption. The literature evaluates QC on speed, not joules. Papers about "quantum + energy" are about using QC to optimize energy systems, not auditing QC's energy cost.

#### S2 — AI/ML (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| "Toward Sustainable Generative AI: A Scoping Review of Carbon Footprint" (2511.17179) | 2025 | **CLOSEST** — reviews AI carbon footprint but not joules-per-parameter systematically |

**Finding:** One scoping review on AI sustainability exists. No universal joules-per-trained-parameter benchmark. Frontier model training costs (GPT-4 ~50 GWh) are estimated by journalists, not measured by a standardized protocol. Inference energy is almost entirely unmeasured.

#### S3 — Cryptography (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| "Energy-Efficient Configurable Lattice Cryptography Processor for IoT" (1903.04570) | 2019 | **RELEVANT** — measures lattice crypto energy on embedded hardware |
| "Complexity of Post-Quantum Cryptography in Embedded Systems" (2504.13537) | 2025 | **RELEVANT** — optimization strategies for PQC |
| "Measurement Study of Post-Quantum Readiness of Internet" (2606.16473) | 2026 | **RELEVANT** — TLS handshake measurement, not energy per se |

**Finding:** Some embedded-systems papers measure PQC energy, but all are device-specific. No universal "joules per encryption/decryption" benchmark comparing RSA/ECC to lattice/code/hash across device classes.

#### S4 — Data Centers (6 papers)

**Finding:** Search terms ("data center energy efficiency PUE") returned mostly irrelevant results (Byzantine ML, remote sensing, dark energy, particle physics). The arXiv corpus returned false positives from the word "data." Data center energy literature may be in industry white papers (Google, Microsoft, Amazon) rather than arXiv preprints.

#### S5 — CPUs (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| "Benchmarking Deep Learning Convolutions on Energy-constrained CPUs" (2509.26217) | 2025 | **RELEVANT** — but DL-inference-specific |
| "Racing to Idle: Energy Efficiency of Matrix Multiplication" (2507.20063) | 2025 | **RELEVANT** — cross-CPU/GPU but operation-specific |
| "Performance and energy consumption of HPC workloads on Arm ThunderX2" (2007.04868) | 2020 | **RELEVANT** — CPU energy in HPC context |

**Finding:** CPU energy benchmarking exists but is domain-specific (HPC, DL inference) or vendor-specific (Arm vs x86 in specific workloads). No cross-ISA universal joules-per-instruction benchmark. **SPECpower** (industry standard) exists but is server-class only and measures throughput/watt, not joules-per-solution for specific computational tasks.

#### S6 — Neuromorphic & Thermodynamic (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| **"NeuroBench: A Framework for Benchmarking Neuromorphic Computing Algorithms and Systems"** (2304.04640) | 2023 | **HIGHLY RELEVANT** — the closest existing analogue to JPCUB |
| "Neuromorphic computing for attitude estimation onboard quadrotors" (2304.08802) | 2023 | Mentions "high energy efficiency" of neuromorphic processors |

**Finding:** **NeuroBench is the closest existing benchmark to JPCUB's vision.** It provides a standardized framework for benchmarking neuromorphic algorithms and systems. However, it is domain-specific (neuromorphic only) and does not use "joules per solution" as a universal metric — it uses task-specific accuracy and throughput metrics alongside power measurements.

#### S7 — Edge/IoT (6 papers)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| **"The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization"** (2505.06371) | 2025 | **HIGHLY RELEVANT** — ML inference energy benchmark |
| "Benchmarking the Energy Cost of Assurance in Neuromorphic Edge Robotics" (2603.13880) | 2026 | **RELEVANT** — edge robotics energy benchmark |

**Finding:** ML.ENERGY measures inference energy for ML models across hardware. Closest to the JPCUB vision but ML-inference-specific only.

### §2.2 Semantic Scholar Results

Only S7-Edge queried successfully (rate-limited on all other domains). Results aligned with arXiv: mobile edge computing energy optimization papers, no universal benchmark.

---

## §3. Closest Analogue Benchmarks (The Competition)

| Benchmark | Domain | Year | What It Measures | Gap vs. JPCUB |
|:----------|:-------|:-----|:-----------------|:--------------|
| **NeuroBench** (2304.04640) | Neuromorphic computing | 2023 | Algorithm accuracy + throughput + power on neuromorphic hardware | Domain-specific (neuromorphic only); no cross-paradigm comparison; power ≠ joules-per-solution |
| **ML.ENERGY** (2505.06371) | ML inference | 2025 | Automated inference energy measurement for ML models | Domain-specific (ML inference only); no cross-domain comparison |
| **SPECpower_ssj2008** | Server-class CPUs | 2007+ | Server-side Java throughput per watt | Workload-specific (Java enterprise); throughput/watt ≠ joules-per-solution; server-only |
| **Green500** | HPC/supercomputing | 2007+ | FLOPs/watt for TOP500 machines | HPC-only; FLOPs/watt ≠ joules-per-solution for diverse task types |
| **MLPerf Power** | ML training/inference | 2019+ | Power during MLPerf benchmarks | ML-only; power snapshot ≠ total system energy; no crypto/quantum/edge coverage |
| **EEMBC ULPMark** | Microcontrollers/IoT | 2014+ | Energy per benchmark on MCUs | MCU-only; task-specific (ULPMark workloads); no AI/quantum/crypto coverage |
| **TPC-Energy** | Database/transaction | 2010 | Watts per transaction | Database-only; deprecated/rarely used |

**Conclusion:** Every existing energy/performance benchmark is DOMAIN-SPECIFIC. None spans quantum, AI, crypto, data centers, CPUs, neuromorphic, and edge under a single "joules per solution" metric. **The JPCUB novelty claim is CONFIRMED.**

---

## §4. Gap Analysis

### §4.1 Gap 1: No Universal Metric

Every paradigm benchmarks itself on its own terms: quantum volume, FLOPs, PUE, SPEC, accuracy. The concept of "joules per solution" as a cross-domain universal metric does not exist in any reviewed literature.

### §4.2 Gap 2: No Cross-Domain Comparison

NeuroBench (neuromorphic), ML.ENERGY (ML inference), SPECpower (servers), and Green500 (HPC) all exist but operate in separate silos. No framework exists to compare an Intel Xeon against a Google TPU against an IBM quantum processor against a Loihi 2 neuromorphic chip on a common energy-efficiency scale.

### §4.3 Gap 3: No Anti-Gaming Protocol

Existing benchmarks are designed by the same industry that they evaluate. SPEC benchmarks are defined by hardware vendors. MLPerf is defined by the AI industry. Quantum volume is defined by IBM. No benchmark exists with explicit anti-gaming provisions and independent, physics-grounded measurement protocols.

### §4.4 Gap 4: No Total-System Energy Accounting

Existing benchmarks measure chip power (TDP), not total system energy including cooling, power conversion, networking, and amortized manufacturing energy. The gap between chip power and total system energy is particularly large for quantum computing (cryogenic cooling multiplies chip power by 10-100×) and data centers (PUE of 1.1 still means 10% overhead, but the real story is in per-computation utilization, not facility efficiency).

### §4.5 Gap 5: No Living Benchmark Protocol

Existing benchmarks are static (SPEC2006, SPEC2017) and become stale as hardware evolves. No benchmark exists with a protocol for ongoing annual updates, community contribution, and versioned measurement reports.

### §4.6 What JPCUB Uniquely Provides

1. **Universal metric:** joules-per-solution, defined with anti-gaming provisions in P0
2. **Cross-domain comparison:** P9 Comparative Atlas places all 7 domains on one scale
3. **Total-system accounting:** cooling, power conversion, networking, amortized manufacturing
4. **Independent methodology:** physics-grounded, not industry-defined
5. **Living protocol:** annual updates, community contribution, versioned reports

---

## §5. Novelty Verdict

| Criterion | Finding |
|:----------|:--------|
| Universal joules-per-solution metric? | **NOVEL** — no existing benchmark uses this cross-domain metric |
| Cross-domain comparison framework? | **NOVEL** — all existing benchmarks are domain-specific |
| Anti-gaming provisions? | **NOVEL** — existing benchmarks are industry-defined |
| Total-system energy accounting? | **NOVEL** — existing benchmarks measure chip power, not system energy |
| Living benchmark protocol? | **NOVEL** — existing benchmarks are static version releases |
| Quantum computing energy audit? | **NOVEL** — ZERO arXiv papers measure QC's own energy cost |
| Cross-crypto energy comparison? | **PARTIALLY NOVEL** — embedded-systems papers exist but no universal benchmark |
| CPU cross-ISA energy benchmark? | **PARTIALLY NOVEL** — SPECpower exists but is server/Java-specific |

**Overall: The JPCUB research program is genuinely novel across all 7 domains.** The closest analogues (NeuroBench, ML.ENERGY, SPECpower, Green500) each cover one domain. No prior work combines them under a universal physics-grounded metric.

---

## §6. Cross-Domain Consilience Gate (KIF-29)

**Trigger:** This project spans Physics (thermodynamics, Landauer limit), Computer Science (benchmarking, architectures), Information Theory (entropy, channel capacity), and Sociology (institutional incentives, bubble dynamics). **Consilience gate applies.**

### §6.1 Core Dynamic

**Joules-per-solution functions as an invariant constraint across all computational substrates.** Every system that computes pays an energy cost. The ratio of energy-in to useful-computation-out is the honest measure of value, independent of substrate. What appears as "energy efficiency" in physics is "resource-bounded computation" in CS, "metabolic efficiency" in biology, and "cost-benefit ratio" in sociology.

### §6.2 Cross-Domain Lexicon

| Source Term | Physics | CS | CogSci | InfoTheory | Biology | Sociology |
|:------------|:--------|:---|:-------|:-----------|:--------|:----------|
| Joules-per-solution | Thermodynamic efficiency | Algorithmic complexity × hardware cost | Cognitive effort per insight | Energy per bit of mutual information | Metabolic cost per adaptive behavior | Resource cost per institutional decision |
| Benchmark | Measurement protocol | Performance evaluation suite | Psychometric test | Channel capacity measurement | Fitness assay | Audit framework |
| Computational advantage | Lower free energy path | Faster/more efficient algorithm | More accurate mental model | Higher rate–distortion performance | Higher fitness in niche | More effective policy |
| Anti-gaming | Calibration against physical law | Adversarial validation | Debiasing protocol | Error-correcting code | Selection pressure for honest signals | Independent oversight |

### §6.3 Domain Translations

#### Physics
- **Lexicon:** Thermodynamic efficiency (η = W/Q), free energy minimization
- **Instance:** The Landauer bound (kT ln 2 per bit erased) — the irreducible physical cost of computation
- **Ramification:** Any claim of computational advantage that ignores thermodynamic cost is a claim to violate the Second Law

#### Computer Science
- **Lexicon:** Algorithmic complexity, resource-bounded computation, benchmarking
- **Instance:** SPEC/MLPerf/NeuroBench — domain-specific benchmarks that optimize for speed, not energy
- **Ramification:** Every benchmark implicitly encodes a value function; changing the function from FLOPs to joules would redirect R&D investment

#### Cognitive Science
- **Lexicon:** Cognitive effort (attention, working memory), mental model accuracy
- **Instance:** The "cognitive miser" — humans optimize for least effort, not most accuracy
- **Ramification:** Institutional preference for familiar benchmarks (quantum volume, FLOPs) over honest ones (joules) is itself a cognitive bias — status quo bias + sunk cost

#### Information Theory
- **Lexicon:** Channel capacity, rate–distortion, mutual information
- **Instance:** Shannon's channel coding theorem — maximum reliable transmission rate is bounded by channel capacity
- **Ramification:** Joules per solution is a joint source–channel coding problem: the computation is the source, the hardware is the channel, and the energy is the cost of reliable transmission through the channel

#### Biology
- **Lexicon:** Metabolic efficiency, fitness landscape, adaptive behavior
- **Instance:** The brain's ~20 W power budget performing ~10^16 synaptic operations per second — approximately 2 × 10^(-15) J per "operation," three orders of magnitude more efficient than CMOS
- **Ramification:** Biology already achieves what JPCUB advocates: energy-efficiency optimization through evolutionary selection pressure. The question is whether we can engineer systems that approach biological efficiency without requiring evolutionary timescales.

#### Sociology
- **Lexicon:** Institutional incentives, audit frameworks, independent oversight
- **Instance:** Financial auditing (GAAP, IFRS) — standardized, independently verified accounting that prevents self-reported claims from being taken at face value
- **Ramification:** JPCUB is to computational claims what GAAP is to financial claims — a standardized, independently auditable framework that prevents self-dealing. The $35B quantum computing bubble is structurally identical to the Enron scandal: self-reported metrics without independent verification.

### §6.4 Synthesis Consilience

**Meta-Principle:** The invariant across all six domains is that **self-reported metrics without independent, physics-grounded verification create systematic overestimation of value.** Whether in finance (Enron), computation (quantum volume), or cognition (confirmation bias), the absence of a universal, falsifiable, externally verifiable metric enables narrative capture. Joules-per-solution is the metric that physics enforces regardless of what humans choose to measure.

**Frontier Question:** If "joules per solution" were adopted as the universal benchmark, which currently dominant computational paradigm would suffer the largest reputational loss, and which currently underfunded paradigm would gain the most?

### §6.5 Research Integration

- **Scoping (Phase 2):** Use translated Lexicon terms as additional search queries: "thermodynamic efficiency computing benchmark," "channel capacity computation energy," "metabolic efficiency silicon comparison," "audit framework computational claims"
- **Deep Dive (Phase 4):** The Frontier Question becomes a Stage 5 Calibration Register entry: "By 2028, if joules-per-solution were a mandatory reporting requirement, quantum computing investment would decrease by X% and neuromorphic investment would increase by Y%."
- **Execution (Phase 5-9):** The Cross-Domain Lexicon table is publication-ready for P0 (The Joules-per-Solution Metric) as a dedicated "Cross-Domain Implications" section.

---

## §7. Red-Team Corrigendum (2026-07-27)

### §7.1 Missed Competitor Papers (FINDING 1 — HARD)

The Phase 1 external search missed three significant competitor works. These were discovered in the autonomous red-team review. The Phase 1 novelty verdict has been revised accordingly.

#### Missed Paper A: "Sustainable Quantum Computing: Opportunities and Challenges of Benchmarking Carbon in the Quantum Computing Lifecycle" (arXiv:2408.05679, 2024)

- **Authors:** Nivedita Arora, Prem Kumar
- **Abstract:** "While researchers in both industry and academia are racing to build Quantum Computing (QC) platforms with viable performance and functionality, the environmental impacts of this endeavor, such as its carbon footprint, e-waste generation, mineral use, and water and energy consumption, remain largely unknown. A similar oversight occurred during the semiconductor revolution and continues to have disastrous consequences..."
- **Relevance to JPCUB:** DIRECT — benchmarks carbon and total-system environmental impact of quantum computing. This is the closest existing paper to JPCUB's P1 (Quantum Energy Audit). It benchmarks carbon (not joules-per-solution), is QC-specific (not cross-domain), has no anti-gaming protocol, and is a static publication (not a living benchmark). **The claim "ZERO papers measure QC's own energy cost" is FALSE — retracted.**
- **Differentiation:** JPCUB's P1 distinguishes itself by: (a) measuring joules-per-solution directly, not carbon proxies, (b) providing a cross-domain comparison framework, (c) embedding anti-gaming provisions, (d) establishing a living benchmark protocol for annual updates.

#### Missed Paper B: "Approximate Computing Survey, Part II: Application-Specific & Architectural Approximation Techniques and Applications" (arXiv:2307.11128, 2023)

- **Authors:** Vasileios Leon, Muhammad Abdullah Hanif, Giorgos Armeniakos, Xun Jiao, Muhammad Shafique
- **Abstract:** "Approximate Computing appears as an emerging solution, allowing to tune the quality of results in the design of a system in order to improve the energy efficiency and/or performance."
- **Relevance to JPCUB:** DIRECT — surveys the energy-quality tradeoff space that JPCUB's P0 measurement protocol (correctness threshold ε) explicitly addresses. Approximate computing's "quality-configurable energy" is structurally isomorphic to JPCUB's "joules-per-solution at correctness threshold ε."
- **Differentiation:** Domain-specific (approximate computing techniques only), no cross-domain framework, no anti-gaming protocol, no living benchmark.

#### Missed Subfield: Reversible/Adiabatic Computing

The reversible computing community has been working on energy-efficient computation at the physics level for decades. Key papers include:
- "Ballistic reversible gates matched to bit storage" (arXiv:1806.08011, 2018)
- "Generalized Reversible Computing" (arXiv:1806.10183, 2018)
- "Reversible Logic Circuit Synthesis" (arXiv:quant-ph/0207001, 2002)

**Relevance:** These papers approach the Landauer limit from the engineering side. JPCUB differentiates by measuring joules-per-solution rather than designing for adiabatic operation, and by being cross-domain rather than paradigm-specific.

### §7.2 Revised Novelty Verdict

| Original Claim | Revised Verdict | Justification |
|:---------------|:----------------|:--------------|
| "ZERO papers measure QC's own energy cost" | **FALSE — RETRACTED** | SQC (2408.05679) benchmarks carbon/energy in QC lifecycle |
| "Universal joules-per-solution metric" | **NOVEL (confirmed)** | No existing benchmark uses this exact metric cross-domain |
| "Cross-domain comparison framework" | **NOVEL (confirmed)** | All competitor papers are single-domain |
| "Anti-gaming provisions" | **NOVEL (confirmed)** | No competitor has embedded anti-gaming protocol |
| "Total-system energy accounting" | **PARTIALLY NOVEL (revised)** | SQC (2408.05679) does total-system but carbon-focused; JPCUB quantifies joules directly |
| "Living benchmark protocol" | **NOVEL (confirmed)** | All competitors are static version releases (SPEC2006, SPEC2017, etc.) |

**Overall:** JPCUB is not the first to propose energetic or carbon benchmarking of computation. It IS the first to propose a **universal, cross-domain, joules-per-solution metric with embedded anti-gaming provisions and a living benchmark protocol.** The novelty claim survives but is QUALIFIED, not absolute.

### §7.3 Self-Referential Foundation Disclosure (FINDING 4)

**Disclosure:** The Phase 1 report cites 6 QNFO-internal papers as the "theoretical foundation" for JPCUB. These papers themselves make strong claims that have not been independently verified against external literature. This is the Institution Fallacy (KIF-16) applied reflexively — treating our own work as "established" without external validation.

**Phase 2 requirement:** The literature search MUST include external papers that directly challenge QNFO foundations:
- Papers arguing FOR gate-model quantum computing (Google Sycamore, IBM Eagle/Heron, PsiQuantum, IonQ, Quantinuum)
- Papers challenging the Landauer/Margolus-Levitin/Bremermann interpretation
- Papers arguing that quantum advantage has been demonstrated for specific use cases
- The Mandatory Symmetry Template (KIF-18) requires both "Supporting" AND "Constraining" sections

### §7.4 External Search Limitations (FINDING 2)

| Source | Status | Papers Found |
|:-------|:-------|:-------------|
| QNFO Vectorize | Complete (7 queries) | 70 results (100% QNFO-internal) |
| arXiv API | Complete (12 queries: 7 original + 5 gap-fill) | 47 papers across 12 subfield queries |
| Semantic Scholar | Incomplete (rate-limited) | 8 papers (S7-Edge only, remaining 6 domains failed) |
| Google Scholar / Web | NOT SEARCHED | 0 papers |
| Industry white papers | NOT SEARCHED | 0 papers (Google, Amazon, Microsoft data center data) |

**Phase 2 must prioritize:** Web search for industry benchmarks, Google Scholar for missed academic literature, and a retry of Semantic Scholar with proper rate-limit handling.

### §7.5 Expanded Competitor Inventory (FINDING 5)

Additional benchmarks identified during red-team review (not in original Phase 1 report):

| Benchmark | Domain | Year | Relevance |
|:----------|:-------|:-----|:----------|
| **Green Graph 500** | Graph processing | 2010+ | Energy-efficient graph benchmarks for HPC |
| **EEMBC CoreMark-Pro** | Embedded/IoT | 2015+ | More comprehensive than ULPMark |
| **CloudSuite** | Cloud computing | 2011+ | Scale-out datacenter workloads with energy measurement |
| **HPCG** | HPC | 2014+ | Alternative to LINPACK for TOP500 ranking |
| **SQC (2408.05679)** | Quantum computing | 2024 | Carbon/energy in QC lifecycle |
| **Approx. Comp. Survey (2307.11128)** | Cross-cutting | 2023 | Energy-quality tradeoffs |
| **Google ML Carbon Footprint** | AI/ML | 2022+ | Industry white papers on training energy |

Total competitor benchmarks inventoried: **14** (up from 7 in original report).

### §7.6 Falsifiability Gap (FINDING 3)

The PROJECT-PLAN.md §1.2 disconfirmation condition uses "real-world computational value" without operational definition. This makes the claim difficult to falsify in practice. Recommended tightening for P0:

> "This would be disconfirmed if, for a representative sample of ≥100 real-world computational tasks spanning ≥4 of the 7 domains, a different metric (wall-clock time, FLOPs, or quantum volume) predicted procurement outcomes more accurately than joules-per-solution, where procurement outcome is defined as the system chosen by an independent evaluator given total cost of ownership data including energy costs."

---

## §8. Recommendations for Phase 2 (Updated)

1. **Prioritize P0 first** — the metric paper unblocks all domain-specific audits
2. **Search industry white papers** for data center energy data (Google, Microsoft, Amazon publish PUE but not per-computation cost)
3. **Contact NeuroBench authors** — they are the closest existing effort and may be collaborators
4. **Deep-dive ML.ENERGY** — understand their measurement methodology before designing P0's protocol
5. **Cross-reference Green500 data** — the TOP500 list provides FLOPs/watt for HPC systems
6. **Register with SPECpower methodology** — understand the industry standard
7. **NEW: Run Mandatory Symmetry Template (KIF-18)** — include papers that challenge QNFO foundations
8. **NEW: Search all 14 competitor benchmarks** as Phase 2 seed terms
9. **NEW: Retry Semantic Scholar with proper rate-limit handling** across all 7 domains
10. **NEW: Search Google Scholar and industry white papers** for data center/AI energy data

---

## §8. Version

| Version | Date | Status |
|:--------|:-----|:-------|
| v0.1 | 2026-07-27 | Phase 1 Due Diligence — Draft |
| v1.1 | 2026-07-27 | Phase 1 Due Diligence — Red-Team Remediated (6 findings, 2 HARD fixes, §7 corrigendum) |
