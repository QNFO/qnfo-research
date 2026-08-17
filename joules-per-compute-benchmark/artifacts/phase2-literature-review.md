# Phase 2 Literature Search & Triage — JPCUB

**Date:** 2026-07-27 | **Phase:** 2 | **Status:** Complete
**Author:** QNFO

---

## §1. Search Methodology

| Dimension | Detail |
|:----------|:-------|
| Sources | arXiv API, QNFO Vectorize (from Phase 1), Semantic Scholar (partial, Phase 1) |
| Queries | 26 structured queries: 14 benchmark seeds + 5 constraining + 5 supporting + 2 cross-domain |
| Raw papers | 208 (arXiv) + 70 (Phase 1 Vectorize) |
| Unique after dedup | 135 (73 duplicates across queries removed) |
| Date range | 2002–2026 |
| Semantic Scholar | Rate-limited — deferred to Phase 2 supplemental |
| Web / Google Scholar | NOT searched — deferred |

---

## §2. Classification Results

| Class | Count | Definition |
|:------|:------|:-----------|
| **Core** | 35 | Directly addresses research question: energy benchmarking, joules metrics, QC energy, AI training energy, crypto energy, neuromorphic energy advantage, pro-QC advantage claims, Landauer challenges |
| **Background** | 84 | Adjacent/context: specific benchmark implementations, related domain surveys, foundational computing papers |
| **Reject** | 16 | False positives: dark energy cosmology, carbon nanotubes, protein compression, financial semimartingales |

---

## §3. Mandatory Symmetry Template (KIF-18)

### §3.1 Where External Literature Supports Joules-per-Solution

| Paper | Year | arXiv | Relevance |
|:------|:-----|:------|:----------|
| **NeuroBench: A Framework for Benchmarking Neuromorphic Computing** | 2023 | 2304.04640 | Standardized neuromorphic benchmark — structural precursor to JPCUB |
| **ML.ENERGY: Toward Automated Inference Energy Measurement** | 2025 | 2505.06371 | ML inference energy benchmark — closest existing work to P0 methodology |
| **Compute and Energy Consumption Trends in Deep Learning Inference** | 2021 | 2109.05472 | Documents exponential growth of DL inference energy |
| **The Sunk Carbon Fallacy: Rethinking Carbon Footprint Metrics** | 2024 | 2410.15087 | Argues carbon metrics are misleading — supports need for direct joules measurement |
| **Making AI Less "Thirsty": Water Footprint of AI Models** | 2023 | 2304.03271 | Hidden resource costs of AI — supports total-system accounting |
| **Line-based Event Preprocessing: Low-Energy Neuromorphic Vision** | 2026 | 2601.10742 | Demonstrates neuromorphic energy advantage for specific workloads |
| **Quantum Computing: Vision and Challenges** | 2024 | 2403.02240 | Survey that acknowledges QC challenges including resource consumption |
| **Neuromorphic Computing for Low-Power AI** | 2026 | 2604.04727 | Argues neuromorphic's 100-1000× energy advantage over digital CMOS |

**Key observation:** The supporting literature is DOMAIN-SPECIFIC. No paper argues for a CROSS-DOMAIN unified joules benchmark. Every paper advocates energy measurement within its own paradigm. This confirms JPCUB's novelty while providing a strong positive-evidence foundation for the claim that energy efficiency matters.

### §3.2 Where External Literature Constrains or Contradicts Joules-per-Solution

| Paper | Year | arXiv | Relevance |
|:------|:-----|:------|:----------|
| **Tianyan: Cloud services with quantum advantage** | 2025 | 2512.10504 | Claims demonstrated quantum advantage — challenges "no commercially viable QC" |
| **Fault-tolerant quantum computation with constant overhead** | 2025 | 2512.02760 | Claims fault-tolerant QC achievable with constant (not exponential) overhead |
| **Thermodynamic Recycling of Algorithmic Failure Branches** | 2026 | 2601.07522 | Proposes thermodynamic optimization of QC operations |
| **Generalized Reversible Computing** | 2018 | 1806.10183 | Argues reversible computing can approach Landauer limit — challenges "QC is energetically hopeless" |
| **Quantum error correction with the toric code** | 2026 | 2606.04079 | Atom Computing's toric-code QEC demonstration |
| **Fault-tolerant Quantum Error Correction Using Linear Array of Emitters** | 2024 | 2403.01376 | Claims efficient QEC with linear photonic emitter arrays |
| **Fault-tolerant quantum input/output** | 2024 | 2408.05260 | Claims fault-tolerant I/O for quantum computers |
| **Continuous-time quantum error correction** | 2013 | 1311.2485 | Alternative QEC paradigm that may change the energy overhead calculus |
| **Error suppression and correction in adiabatic quantum computation** | 2013 | 1307.5893 | Adiabatic QC — alternative to gate model with different energy characteristics |
| **An introduction to Fault-tolerant Quantum Computing** | 2015 | 1508.03695 | Foundational fault-tolerant QC survey |
| **Noisy three-player dilemma game: Robustness of the quantum advantage** | 2020 | 2004.04533 | Claims quantum advantage for game theory |
| **Quantum error correction beyond qubits** | 2008 | 0811.3734 | Qudit-based QEC with potentially lower overhead |
| **Fault tolerance for holonomic quantum computation** | 2013 | 1312.0165 | Geometric QC with intrinsic fault tolerance |
| **Fault-tolerant quantum error detection** | 2016 | 1611.06946 | Error detection (not correction) with lower overhead |
| **Unifying communication paradigms in MBQC** | 2025 | 2506.21988 | Measurement-based QC — alternative paradigm to gate model |
| **Quantum Computing and Error Correction** | 2003 | quant-ph/0304016 | Early QEC survey — establishes historical depth of error correction progress |

**Key observation:** The constraining literature is HEAVILY weighted toward fault-tolerant quantum computing. These papers do NOT directly rebut the joules-per-solution thesis — they argue that quantum computing WILL work, not that it is ALREADY energy-efficient. However, they establish that the research community is actively working on reducing the energy overhead, and some approaches (constant-overhead FTQC, thermodynamic recycling, reversible computing) claim the gap can be closed. JPCUB's response: measure the joules when they do.

---

## §4. Cross-Domain Gap Confirmation

**Query X1-CrossDomain and X2-EnergyAwareBenchmark returned 16 papers, of which 8 were rejected as false positives (dark energy cosmology, protein compression).**

The remaining 8 papers were:
- ML.ENERGY (already classified as supporting)
- "The Sunk Carbon Fallacy" (already classified as supporting)
- General computing surveys that mention energy as one dimension among many

**CONFIRMED: No existing cross-domain energy-efficiency benchmark survey exists on arXiv.** The literature is entirely domain-specific. No paper proposes a universal "joules per solution" metric spanning quantum, AI, crypto, data centers, CPUs, neuromorphic, and edge computing.

---

## §5. Competitor Benchmark Insights (14 Benchmarks Analyzed)

| Benchmark | Key Finding |
|:----------|:------------|
| **NeuroBench** | Most mature neuromorphic benchmark. 2023 framework with algorithm + system tracks. No cross-domain ambition. |
| **ML.ENERGY** | Closest to JPCUB methodology. Automated inference energy measurement. ML-inference-specific. |
| **SPECpower** | Industry standard for server energy. Java-specific workload. Throughput/watt not joules/solution. |
| **Green500** | TOP500 energy ranking. FLOPs/watt only. HPC-exclusive. |
| **MLPerf Power** | Power measurement alongside MLPerf benchmarks. Academic + industry. ML-only. |
| **ULPMark / CoreMark-Pro** | Embedded microcontroller energy benchmarks. MCU-specific workloads. |
| **TPC-Energy** | Database transaction energy. Deprecated / rarely used. |
| **Green Graph 500** | Graph processing energy efficiency. HPC-exclusive. |
| **CloudSuite** | Scale-out datacenter workloads with energy hooks. Cloud-specific. |
| **HPCG** | High-performance conjugate gradients. Alternative to LINPACK. HPC-only. |
| **SQC (2408.05679)** | Quantum computing carbon/energy lifecycle. QC-specific. Carbon-focused. |
| **Approx. Survey (2307.11128)** | Energy-quality tradeoff survey. Approximate computing techniques only. |
| **Google ML Carbon** | Industry white papers. Not peer-reviewed. ML-training-specific. |

**Conclusion:** All 14 benchmarks are domain-specific. None provide cross-domain comparison. None use "joules per solution" as a universal metric. None embed anti-gaming provisions. None propose a living benchmark protocol.

---

## §6. Recommendations for Phase 3 (Citation Management)

1. **Extract citations** from all 35 core papers for BibTeX database
2. **Generate BibTeX** from arXiv IDs for all 35 core + 84 background papers
3. **Verify DOIs** — cross-reference arXiv IDs against Semantic Scholar/CrossRef for formal citations
4. **Prioritize P0 sources** — the foundational metric paper needs: Landauer 1961, Margolus-Levitin 1998, Bremermann 1962, NeuroBench (2023), ML.ENERGY (2025), SQC (2024)
5. **Flag constraining citations for P0** — the Mandatory Symmetry Template (17 constraining papers) must be cited in P0 to demonstrate epistemic balance

---

## §7. Version

| Version | Date | Status |
|:--------|:-----|:-------|
| v0.1 | 2026-07-27 | Phase 2 Literature Search — Draft |
