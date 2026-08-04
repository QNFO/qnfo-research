# PROJECT-PLAN: Joules-per-Compute Universal Benchmark (JPCUB)

**Author:** QNFO Research Collective | **Date:** 2026-07-27 | **Status:** Phase 0 — Scaffold
**License:** QNFO Unified License Agreement (QNFO-ULA)
**Parent Series:** The Qubit Delusion (Phase VI → Generalization)
**Preceded By:** BQNN v2 — DOI 10.5281/zenodo.21623218

---

## §1. Charter

### §1.1 Problem Statement

The global computational infrastructure consumes approximately 1-2% of world electricity production and is growing at ~20% annually. Within that envelope, several domains compete for resources, attention, and investment under claims of "advantage" that lack a common yardstick:

- **Quantum computing** has absorbed ~$35B without delivering a single commercially viable machine. Claims of "quantum advantage" rely on problem-specific speedups that ignore the energetic cost of cryogenic cooling, error correction, and control electronics — overheads that multiply the joules-per-logical-operation by factors of $10^2$ to $10^6$ compared to the idealized gate cost.
- **AI accelerators** (GPUs, TPUs, custom ASICs) are benchmarked on training throughput (FLOPs/s) or inference latency, not on joules per trained parameter or joules per inference — metrics that would reveal the enormous and growing energy cost of frontier models (GPT-4 estimated at ~50 GWh for a single training run).
- **Cryptographic systems** are evaluated on security bits, not on the joules required to break them — a metric that would expose post-quantum schemes (lattice-based, code-based, hash-based) as requiring 10-100$\times$ more energy per operation than classical RSA/ECC, potentially making them *less* practical than the quantum threat they defend against.
- **Data centers** report Power Usage Effectiveness (PUE), a facility-level metric that conceals the per-computation cost. A PUE of 1.1 tells you nothing about whether the computation itself is worth the joules it consumes.
- **Classical CPUs** (x86, ARM, RISC-V) are compared on benchmarks (SPEC, Geekbench) that measure wall-clock time, not energy. A 10% faster processor that consumes 50% more power is "better" by existing metrics — and worse by physics.
- **Neuromorphic and thermodynamic computing** lack any standardized benchmark at all, making them invisible to procurement decisions even when their energy-per-operation is orders of magnitude below digital CMOS.
- **Edge/IoT and mobile computing** operate under battery constraints where joules-per-compute determines device lifetime, yet no standardized cross-platform benchmark exists for making procurement or architecture decisions.

**The common failure:** every domain benchmarks itself on its own terms — speed, FLOPs, PUE, security bits — none of which are honest proxies for what physics charges: energy. A "faster" algorithm that uses 10$\times$ more energy is not faster in any physically meaningful sense; it is less efficient. The universe does not care about FLOPs. It cares about joules.

### §1.2 Core Claim (LOCKED)

> **"Joules-per-solution is the only honest arbiter of computational advantage."**

**Formally:** For any computational task $T$ with a correctness threshold $\epsilon$, the computational advantage of system $A$ over system $B$ is defined as:

$$ \text{Advantage}_T(A, B) = \frac{E_B(T, \epsilon)}{E_A(T, \epsilon)} $$

where $E_X(T, \epsilon)$ is the total system-level energy (joules) consumed by system $X$ to produce a solution to $T$ within correctness bound $\epsilon$. Total system energy includes: computation, memory, I/O, cooling, power conversion losses, and amortized manufacturing energy. System $A$ has advantage over $B$ if and only if $\text{Advantage}_T(A, B) > 1$.

**Falsifiability condition:** This claim would be disconfirmed if a different metric (e.g., wall-clock time, FLOPs, or "quantum volume") consistently predicted real-world computational value better than joules-per-solution across a statistically significant sample of diverse computational tasks. `[speculative — no existing comprehensive cross-domain benchmark data exists to test this]`

**Scope of the claim:** This is a *benchmark claim* — it asserts that joules-per-solution is the correct normative standard for comparing computational systems, not that current systems have been measured under this standard. The validation or refutation of this claim is the purpose of this research program.

### §1.3 Key Insight from BQNN v2

The BQNN v2 paper (DOI 10.5281/zenodo.21623218) established that for Bayesian Quantum Neural Networks, a carefully optimized classical baseline (Monte Carlo dropout + ensemble methods on GPU) matched or exceeded quantum proposals on the same tasks, while consuming orders of magnitude less energy. The lesson generalizes:

> **"Energy is unframeable."** You cannot cheat the physics. Every gate, every memory access, every cooling cycle, every photon detection event costs joules. Claiming "advantage" while ignoring joules is claiming to violate thermodynamics.

**Five new actionable research directions identified across 7 compute domains** in the BQNN v2 closeout now form the seed questions for this expanded program.

---

## §2. Research Program Architecture

### §2.1 Seven Domain Streams

This program investigates seven distinct computational domains, plus a cross-cutting methodology stream. Each domain stream produces: (a) a comprehensive audit of existing benchmarks and their blind spots, (b) a joules-per-solution measurement protocol, (c) empirical measurements on representative hardware, and (d) a comparison against alternative, potentially more efficient paradigms.

| Stream ID | Domain | Existing Benchmark Blind Spot | Key Question |
|:----------|:-------|:------------------------------|:-------------|
| **S1** | Quantum Computing | "Quantum volume" ignores cryogenic overhead, control electronics, and error correction energy | Is any quantum computer more energy-efficient than a classical computer for *any* commercially relevant problem? |
| **S2** | AI/ML Accelerators | FLOPs/s and training time ignore joules per trained parameter and inference energy | What is the true energetic cost of frontier AI, and how does it compare to neuromorphic alternatives? |
| **S3** | Cryptographic Systems | Security bits ignore energy per encryption/decryption/signing operation | Are post-quantum cryptographic schemes *energetically practical* compared to classical RSA/ECC? |
| **S4** | Data Center Infrastructure | PUE conceals per-computation cost; network and storage energy amortized away | What is the true joules-per-bit and joules-per-FLOP in a modern hyperscale data center? |
| **S5** | Classical CPUs | SPEC/Geekbench measure time, not energy; cross-ISA comparison is meaningless in joules | Which ISA (x86, ARM, RISC-V) is most energy-efficient per unit of useful computation? |
| **S6** | Neuromorphic & Thermodynamic | No standardized benchmark exists at all | Can thermodynamic/neuromorphic computing beat digital CMOS by 100-1000× in joules-per-operation for specific problem classes? |
| **S7** | Edge/Mobile/IoT | Battery-life benchmarks are device-specific; no cross-platform energy efficiency metric | What is the joules-per-compute landscape for inference at the edge, and can a standard benchmark drive procurement decisions? |
| **M0** | Cross-Cutting Methodology | No standard for "total system energy" measurement; no protocol for fair cross-paradigm comparison | How do we define, measure, and verify "joules per solution" in a way that is fair, reproducible, and resistant to gaming? |

### §2.2 Twelve Sub-Projects (Independent Research Papers)

Each sub-project is a publishable research paper with its own literature review, methodology, empirical results, and conclusions. Projects are ordered by dependency and impact:

| Project | Title | Domain Stream | Dependencies | Estimated Scope |
|:--------|:------|:-------------|:-------------|:----------------|
| **P0** | The Joules-per-Solution Metric: Definition, Measurement Protocol, and Anti-Gaming Provisions | M0 | None (foundational) | 15-25 pages |
| **P1** | Quantum Computing's Energy Audit: From Cryostat to Qubit — The True Joules per Logical Operation | S1 | P0 | 20-30 pages |
| **P2** | The Hidden Cost of Frontier AI: Joules per Trained Parameter in Large Language Models | S2 | P0 | 15-20 pages |
| **P3** | Post-Quantum Cryptography's Energy Trap: Lattice, Code, and Hash-Based Schemes vs. Classical RSA/ECC | S3 | P0 | 15-20 pages |
| **P4** | Beyond PUE: Joules-per-Bit and Joules-per-FLOP in Hyperscale Data Centers | S4 | P0 | 15-20 pages |
| **P5** | ISA Energy Efficiency: x86 vs. ARM vs. RISC-V Under a Unified Joules-per-Compute Benchmark | S5 | P0 | 15-20 pages |
| **P6** | Neuromorphic Computing's Energy Advantage: A Joules-per-Operation Comparison Against Digital CMOS | S6 | P0, P2 | 20-25 pages |
| **P7** | Thermodynamic Computing: Can Physics Do Computation Cheaper Than Transistors? | S6 | P0, P6 | 15-20 pages |
| **P8** | Edge Inference Energy Landscape: A Cross-Platform Joules-per-Inference Benchmark | S7 | P0, P2 | 15-18 pages |
| **P9** | The Comparative Atlas: Joules-per-Solution Across All Seven Domains | M0 (synthesis) | P0-P8 | 30-40 pages |
| **P10** | Policy Implications: Procurement Reform, Funding Allocation, and Regulatory Standards for Honest Computation | M0 (applied) | P0-P9 | 15-20 pages |
| **P11** | Institutional Reform: How to Prevent the Next $35B Computational Bubble | M0 (applied) | P0-P10 | 12-15 pages |

### §2.3 Research Phases (QNFO Standard Pipeline)

This program follows the standard QNFO research pipeline. Each sub-project (P0-P11) goes through Phases 1-8 independently. Phase 0 (this scaffold) applies to the entire program.

#### Program-Level Phases

| Phase | Name | Deliverables | Estimated Duration |
|:------|:-----|:-------------|:-------------------|
| **Phase 0** | Program Scaffold | This document, repo, WBS, core claim lock, KG seed | Current (2026-07-27) |
| **Phase 1** | Cross-Domain Due Diligence | KG query results, external literature survey across 7 domains, gap analysis, consilience gate audit | 1-2 sessions |
| **Phase 2** | Domain-Specific Literature Search | 7 parallel literature searches (one per domain stream), deduplication, classification into core/supporting/background/reject | 2-4 sessions |
| **Phase 3** | Citation Management | BibTeX database across all 7 domains, verified DOIs, auto-generated missing entries | 1 session |
| **Phase 4** | Deep Research — Paradigm Forecast | 9-stage Bayesian cascade evaluating the energy-efficiency trajectory of each computational paradigm through 2040 | 2-3 sessions |
| **Phase 5** | Publication — P0 (Foundational Metric Paper) | "The Joules-per-Solution Metric" — published to Zenodo with DOI, PDF, provenance bundle | 2-3 sessions |
| **Phase 6** | Publication — P1 through P8 (Domain Audits) | Eight domain-specific energy audit papers, each with independent measurement methodology and empirical results | 8-16 sessions |
| **Phase 7** | Publication — P9 (Synthesis Atlas) | "The Comparative Atlas: Joules-per-Solution Across All Seven Domains" — the capstone synthesis paper | 3-4 sessions |
| **Phase 8** | Publication — P10, P11 (Policy & Reform) | Policy implications paper and institutional reform proposal | 2-3 sessions |
| **Phase 9** | Core Distribution & Dissemination | All 12 papers deployed to GitHub, Zenodo, R2, D1/KG, papers-server, IPFS/DNSLink, Buffer social media, SEO audit | 2-3 sessions |
| **Phase 10** | Living Benchmark Maintenance | Protocol for ongoing measurement updates, annual energy audit reports, community contribution framework | Ongoing |

---

## §3. Deliverable Registry

| ID | Deliverable | Type | Path | Archival Target | Status |
|:---|:------------|:-----|:-----|:----------------|:-------|
| DL-00 | PROJECT-PLAN.md | Document | PROJECT-PLAN.md | GitHub + R2 + Zenodo (Phase 0 snapshot) | Draft (Phase 0) |
| DL-01 | README.md | Document | README.md | GitHub + R2 | Draft (Phase 0) |
| DL-02 | P0 — The Joules-per-Solution Metric | Paper | artifacts/p0-metric.md | Zenodo DOI + R2 + D1 | Pending (Phase 5) |
| DL-03 | P1 — Quantum Energy Audit | Paper | artifacts/p1-quantum-audit.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-04 | P2 — AI Energy Cost | Paper | artifacts/p2-ai-energy.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-05 | P3 — Crypto Energy Trap | Paper | artifacts/p3-crypto-energy.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-06 | P4 — Data Center Joules | Paper | artifacts/p4-datacenter-joules.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-07 | P5 — ISA Energy Efficiency | Paper | artifacts/p5-isa-energy.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-08 | P6 — Neuromorphic Energy Advantage | Paper | artifacts/p6-neuromorphic.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-09 | P7 — Thermodynamic Computing | Paper | artifacts/p7-thermodynamic.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-10 | P8 — Edge Inference Benchmark | Paper | artifacts/p8-edge-inference.md | Zenodo DOI + R2 + D1 | Pending (Phase 6) |
| DL-11 | P9 — Comparative Atlas | Paper | artifacts/p9-comparative-atlas.md | Zenodo DOI + R2 + D1 | Pending (Phase 7) |
| DL-12 | P10 — Policy Implications | Paper | artifacts/p10-policy.md | Zenodo DOI + R2 + D1 | Pending (Phase 8) |
| DL-13 | P11 — Institutional Reform | Paper | artifacts/p11-institutional-reform.md | Zenodo DOI + R2 + D1 | Pending (Phase 8) |
| DL-14 | BibTeX database (all domains) | Data | references/jpcub-bibliography.bib | GitHub + R2 | Pending (Phase 3) |
| DL-15 | Joules-per-solution measurement toolkit | Software | scripts/ | GitHub + R2 | Pending (Phase 5+) |
| DL-16 | Cross-Domain Consilience Audit | Analysis | artifacts/consilience-gate.md | GitHub + R2 | Pending (Phase 1) |

---

## §4. Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| **R1** | Insufficient publicly available energy-consumption data for some hardware platforms (proprietary GPUs, quantum control electronics) | High | Medium | Use physics-based models (Landauer limit, Margolus-Levitin) as theoretical lower bounds; estimate upper bounds from TDP and utilization data; clearly label modeled vs. measured values |
| **R2** | Industry pushback — hardware vendors and quantum computing companies have strong incentives to suppress joules-per-solution comparisons | High | Medium | Pre-register methodology publicly (OSF); all data and code open-source; institutional neutrality gate applies — evaluate claims, not institutions |
| **R3** | Measurement methodology contested as unfair to a particular paradigm (e.g., "cryogenic energy shouldn't count because it will improve") | Medium | Medium | Document methodology with falsifiable boundary conditions in P0; allow parameterized sensitivity analysis ("what if cooling improves by 10×?"); report all assumptions |
| **R4** | Scope creep — 12 papers, 7 domains, multi-year program; risk of incomplete or inconsistent coverage | Medium | High | Each paper is independently publishable; program-level synthesis (P9) depends on P0-P8 but individual papers do not block each other; prioritize by impact × feasibility |
| **R5** | Rapid hardware evolution makes empirical measurements stale within months | Medium | Low | Publish methodology papers (P0) that enable independent replication; design P9 Atlas to be updated annually; measurement dates prominently displayed |
| **R6** | AI training energy data is proprietary (OpenAI, Google, Anthropic do not publish training-joule data for frontier models) | High | Medium | Estimate from known hardware, reported training times, and TDP; clearly label all estimates with uncertainty ranges; use open-weight models (Llama, Mistral) for direct measurement |
| **R7** | Quantum computing advocates dismiss the program as "anti-quantum" rather than engaging with the metric | High | Low | Explicitly frame as pro-honest-computation, not anti-any-paradigm; quantum computing *could* win on joules-per-solution for some problems — the program's goal is to *measure*, not to prejudge; if quantum wins on this metric, we report that too |

---

## §5. Success Criteria

1. **P0 published** — a peer-reviewable definition of "joules per solution" with measurement protocol and anti-gaming provisions, accepted as a reference standard by at least one external research group
2. **P1-P8 published** — eight domain-specific energy audits, each containing at least one empirical measurement showing the joules-per-solution gap between existing dominant paradigms and the most efficient known alternative
3. **P9 published** — a synthesis "atlas" that places all seven domains on a common energy-efficiency scale, revealing which paradigms are closest to fundamental physical limits and which are furthest
4. **P10-P11 published** — actionable policy and institutional reform proposals with specific, falsifiable recommendations
5. **Living benchmark established** — a protocol and infrastructure for ongoing joules-per-solution measurements, updated with new hardware annually
6. **At least one procurement or funding decision influenced** — documented case where joules-per-solution analysis changed a real-world computational resource allocation decision

---

## §6. Prior Art and Intellectual Lineage

This program builds directly on the QNFO "Qubit Delusion" series:

| Prior Paper | DOI / Identifier | Relevance |
|:------------|:-----------------|:----------|
| The Qubit Delusion | QNFO paper | Diagnosed the epistemic failure in quantum computing; proposed joules-per-solution as the corrective metric |
| The Problem-Substrate Mapping | QNFO paper | Formalized the relationship between computational problems and physical substrates; established that "the substrate IS the algorithm" |
| The Physics of Computation | QNFO paper | Established the Landauer, Margolus-Levitin, and Bremermann limits as the honest boundaries of computation |
| Manifesto for Honest Computation | QNFO paper | Synthesized five principles, including joules-per-solution as the universal metric |
| BQNN v2 — Classical Baseline | DOI 10.5281/zenodo.21623218 | Demonstrated that classical GPUs beat quantum proposals on Bayesian inference when measured in joules; "energy is unframeable" |

---

## §7. Version History

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| v0.1-phase0 | 2026-07-27 | QNFO Research Collective | Phase 0 scaffold: charter, WBS, core claim lock, deliverable registry, risk register |
