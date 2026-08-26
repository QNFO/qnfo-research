# Phase 1 Due Diligence + Gap Analysis — QNFO.JPC.003

**Date:** 2026-08-26
**Corpus:** 8,325 KG nodes / 1,662 Paper nodes (query_graph stats, 2026-08-26)
**Gate:** DUE-DILIGENCE-DEPTH-1 (full-corpus sweep, ≥3 formulations, cross-system ID validation, ≥2 adjacent domains, external verification, evidence discipline)

## 1. Query Formulations Executed

| # | Tool | Formulation | Results |
|---|------|-------------|---------|
| F1 | qnfo-memory-mcp | "thermodynamic energy cost of quantum error correction Landauer" | 16 (top: Bottlenecks 0.779, Joules-per-Solution 0.779, FTQC bottlenecks ×4) |
| F2 | qnfo-memory-mcp | "tree codes hierarchical nested-ball ultrametric error correction" | 16 (QEC-Darwinism, Qudit QEC, p-adic metrology, ultrametric foundations) |
| F3 | qnfo-memory-mcp | "flash memory NAND LDPC endurance energy per bit" | 16 (Structural Persistence ×many, JPCUB leading-indicator, Lifecycle FTQC) |
| F4 | qnfo-memory-mcp | "photosynthesis magnetoreception quantum coherence robustness biological protection" | 16 (PSII coherence, boson-mediated transfer, Structural vs Driven) |
| F5 | qnfo-memory-mcp | "autonomous dissipative quantum error correction cat qubit energy cost" | 16 (Autonomous Dissipative Processing, Kerr cancellation, GKP stabilization) |
| F6 | qnfo-memory-mcp | "joules per correct answer ranking error correcting code families overhead" | 16 (Huang advantage audit, JPCUB landscape, LLM energy) |
| F7 | D1 living-paper | body_md LIKE '%Landauer%' | 26 papers |
| F8 | D1 living-paper | body_md LIKE '%erasure engine%' / '%kT ln 2%' / '%k_B T ln 2%' / '%kT·ln2%' | 3 papers (Principia Ontologica; Physics of Computation; p-adic metrology) |
| F9 | recall_facts | keyword Landauer, QEC | Rosetta Axis 3; CWI cross-event themes; JPC.002 P1 crossover curve; Qubit Delusion 10²–10³ |
| F10 | arXiv | "thermodynamics of quantum error correction energy cost Landauer" | Vedral '99; Landi et al. '19; Korepin–Terilla '02; Ishida–Hasegawa '26; Taranto et al. '21; Ma et al. '21; Bedingham–Maroney '16; Chattopadhyay et al. '25 |

## 2. Key Records (cross-system validated)

### 2.1 Corpus — direct overlap risk (cited or differentiated)

| Record | ID / DOI | Relation to JPC.003 |
|--------|----------|---------------------|
| Thermodynamic and Informational Bottlenecks of Scalable FTQC | 10.5281/zenodo.17955898 (v1.0.1, 2025-12) | Full-machine thermal model (qubits × cooling × decode speed); asymptotic infeasibility. **Complementary, must cite** — no per-family erasure floor, no classical test. |
| Thermodynamic and Quantum Constraints on Scalable Quantum Computing | 10.5281/zenodo.17937531 (v2.0, 2025-12) | Cryogenic architectural inversion (4K stage, TLS loss). Cooling-side, not correction-side. Cite. |
| Thermodynamics of Structural Persistence (Topological Memory) | id qnfo-2025-12-thermodynamics-of-structural-persistence; r2 qnfo/releases/2025/12/ | Structural protection thermodynamics. **Directly supports H3.** Cite. |
| Autonomous Dissipative Quantum Processing | id qnfo-2025-11-autonomous-dissipative-quantum-processing; r2 qnfo/releases/2025/11/ | The scope-boundary case (audit Q4/Q8a). Cite as the boundary record. |
| Joules-per-Solution Metric (JPC.002) | QNFO.JPC.002, branch res/paper/thermodynamic-optimized-computing | Metric source. **Parent record; BUILDS_ON edge at P8.** |
| JPCUB Competitive Landscape v2.0 | slug jpcub-competitive-landscape | 17-platform JPCUB estimates — platform-level; mine is code-family-level. Cite. |
| Qudit Advantage | slug qwave-qudit-advantage | System-level JPCUB comparison precedent. Cite. |
| QEC-Darwinism | 10.5281/zenodo.21964674 (QNFO.QEC.001, P8) | Closest QEC sibling (ultrametric QEC tradeoff). Cite + BRIDGES edge. |
| Passive Error Resilience Through Ultrametric Geometry | slug ultrametric-p-adic-metrology | Passive/structural protection via p-adic metrology. Cite. |
| Lifecycle of a Fault-Tolerant Quantum Computer | slug lifecycle-of-a-fault-tolerant-quantum-computer | Lifecycle energy accounting. Cite. |
| Physics of Computation: ... Honest Boundaries | slug paper-physics-of-computation | kT·ln2 phrasing present. Cite. |
| PSII Quantum Coherence; Non-Markovian boson-mediated transfer; Structural vs Driven Coherence | slugs psii-quantum-coherence; non-markovian-hamiltonian-dynamics-of-boson-mediated-energy-transfer; structural-vs-driven-quantum-coherence | Biology side of H3. Cite. |
| Resonant Kerr-Cancellation; GKP Stabilization | slugs resonant-kerr-cancellation-dynamics-in-dissipative-bosonic-stabilization; stabilization-of-gottesman-kitaev-preskill-states | Dissipative stabilization (boundary). Cite. |
| Huang 2025 Quantum Advantage Audit | slug huang-2025-quantum-advantage-audit | Anti-gaming/advantage framing. Cite. |
| Qubit Delusion series | memory (2026-07) | QEC overhead ×10²–10³ (established). Cite the series. |
| Rosetta Axis 3 (Thermodynamics of Translation) | memory (2026-07-22) | Landauer extension + 5-component entropy decomposition + calorimetry falsification. Methodological sibling. Cite. |

### 2.2 External — closest works (verified abstracts)

| Work | ID | Relation |
|------|----|----------|
| Vedral, "Landauer's erasure, error correction and entanglement" | quant-ph/9903049 (1999) | **Ancestor.** QEC as Maxwell's demon; Landauer applied to correction. Cite first. |
| Landi, Oliveira, Buksman, "Thermodynamic analysis of quantum error correcting engines" | 1911.06354 (2019) | **Closest external.** 3-qubit + Shor-9 cycles as Otto engines; correction work = heat injected by error; encoding/decoding work always positive; coherence correction adds Hadamard cost. Differentiation: per-cycle engine analysis vs. my per-family erasure-count floor + JPCUB ranking + architecture-choice + classical test. |
| Korepin & Terilla, "Thermodynamic interpretation of QEC criterion" | quant-ph/0202054 (2002) | QEC criterion ↔ thermodynamics. Cite. |
| Ishida & Hasegawa, "Thermodynamic Recycling of Algorithmic Failure Branches..." | 2601.07522 (2026) | Failure-branch recycling with QEC demo — erasure-minimization cousin. Cite. |
| Taranto et al., "Landauer vs. Nernst" | 2106.05151 (2021) | Cooling-side cost. Cite. |
| Ma, Chen, Sun, Dong | 2112.07311 (2021) | Qubit-initialization energy. Cite. |
| Bedingham & Maroney | 1604.03749 (2016) | Thermodynamic cost of quantum operations. Cite. |
| Chattopadhyay et al. | 2506.10876 (2025) | Landauer survey. Cite. |

## 3. Gap Analysis (what JPC.003 adds)

1. **Per-family erasure-count floor decomposition.** No located record (corpus or external) publishes the erasure-count → kT·ln2 floor table across repetition / Hamming / surface / qLDPC families with computational verification. Landi et al. analyze single cycles (3-qubit, Shor-9) as engines; Vedral gives the principle. The per-family JPCUB ranking table is open.
2. **The bounded architecture-choice thesis.** "Overhead converges to a positive thermodynamic floor; the floor is an architecture choice (nature witnesses it); active correction is the bounded scope, autonomous/dissipative correction the named boundary" — no located record makes this specific, scope-bounded argument. The Bottlenecks paper argues infeasibility (different thesis); JPC.002 has the crossover curve (different unit of analysis: protection energy vs QEC energy for platforms, not correction-cycle erasure pricing for code families).
3. **The classical flash-RAM test (H2).** Tree/nested-ball codes vs LDPC on NAND workloads, energy-per-corrected-bit with endurance amortization — pre-registered, near-term, no quantum hardware. No located record proposes or executes it. **This is the paper's keystone empirical payload** (audit Q15: H2 is the keystone).
4. **Biology crosswalk with the "prepaid" correction.** "Structure costs capital energy (scaffold maintenance), correction costs operating energy (erasures); both are joules" — no located record states the capital/operating split explicitly (Structural Persistence comes closest).
5. **Scope discipline from the audit.** Explicit bounding to active correction, naming autonomous/dissipative QEC as the boundary, stating the relevance caveat (distance-to-floor at current operating points) — this is the anti-poster guarantee (audit Q10).

## 4. Adjacent-Domain Scan (CROSSWALK-TRANSLATION-1)

| Term (QEC engineering) | Adjacent-domain equivalent | Fidelity |
|---|---|---|
| Syndrome reset / ancilla re-init | Bit erasure (information theory); reset-to-reference (thermodynamics of computation) | Exact |
| Correction work | Heat rejected to the bath (Otto-cycle language, Landi et al.) | Exact |
| Structural protection | Passive stability; energy landscape (protein folding, quantum biology) | Good |
| Scaffold maintenance cost | Capital depreciation / housekeeping metabolism | Metaphor, flagged |
| JPCUB (joules per correct answer) | Energy-per-corrected-bit; P/E endurance amortization (NAND industry) | Exact for classical storage |
| Overhead (qubit ratio) | Redundancy rate (coding theory) | Exact |

## 5. Evidence Discipline

All counts and DOIs above were collected live this session (2026-08-26) via: qnfo-memory-mcp search_papers (6 formulations, limit 16 each), D1 living-paper LIKE queries, recall_facts, arXiv search (relevance-sorted), resolve_paper_id, get_paper_context. Raw responses are in this session's tape. This file is the consolidated evidence artifact (artifacts/external-search/phase1-evidence.md equivalent, kept in artifacts/ per repo convention).

## 6. Phase-1 Verdict

**Proceed to P2.** The core claim survives due diligence with a tightened novelty locus: (i) per-family erasure floor table + JPCUB ranking (computationally verified), (ii) bounded architecture-choice thesis, (iii) H2 flash-RAM test as the empirical keystone, (iv) capital/operating energy crosswalk. The claim as originally worded ("erasure engine, thermodynamic floor") is pre-dated by Vedral '99 and Landi et al. '19 at the level of PRINCIPLE — the paper must open by crediting them and must not present the principle itself as new. Novelty is in the decomposition, the ranking, the scope discipline, and the classical test.
