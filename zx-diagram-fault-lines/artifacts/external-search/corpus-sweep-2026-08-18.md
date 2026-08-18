# Phase 1 Evidence — Corpus Sweep (2026-08-18)

Session: zEFqXZMy70BKZf0AY0i9Y · WBS: QNFO.RES.015 · Phase: P1 due diligence
Channels: qnfo-memory-mcp search_papers (limit 16, VECTORIZE-TOP-K-50-1 compliant), search_papers_enriched, search_memories, recall_facts, query_graph, resolve_paper_id, arXiv.

## Corpus baseline

- KG stats: 8,296 nodes / 8,448 edges; Paper 1,635; Project 153; Program 21.
- D1 program_registry: 56 rows; highest RES project before this claim = RES.014.
- KG name scan for zx/pauli web/cafeteria: **0 nodes** → net-new project confirmed.

## Query formulations executed (7 formulations, 4 topics)

| # | Topic | Formulation | Top hits (slug @ score) |
|---|---|---|---|
| 1 | ZX | "ZX calculus spiders Pauli webs gadgets diagrammatic quantum computing" | (empty response `{}` — no semantic match at threshold) |
| 2 | ZX | "diagrammatic reasoning map territory quantum mechanics formal language physical bearing" | conditional-truths-locale-framework @0.669 · topology-of-quanta @0.667 · post-quantum-synthesis @0.661 · syntactic-token-calculus-m1-foundational-syntax @0.661 · time-as-epistemic-cognitive-fiction @0.659 |
| 3 | ZX | "categorical quantum mechanics string diagrams spiders tensor network circuit optimization" | spacetime-volume-and-fractal-surfaces @0.710 · prime-valuation-qec-implications @0.693 · thermodynamic-genesis-of-the-standard-model @0.684 · there-are-no-theories @0.679 · phase-transitions-of-logic @0.675 |
| 4 | Cafeteria | "cafeteria imports siloed disciplines mixing formalisms mutual compatibility cross-disciplinary synthesis" | quantifying-structural-unification-and-epistemic-scaffolding-in-scientific-progress @0.675 · there-are-no-theories @0.666 · meta-pattern-of-reification-in-physics @0.656 |
| 5 | Thermo | "thermodynamics entropy import quantum information energy metric consistency" | massenergyentropyinformation-proof @0.677 · thermodynamic-and-informational-bottlenecks-of-scalable-fault-tolerant-quantum-computation @0.674 · thermodynamics-of-knowing @0.663 |
| 6 | MBQC | "measurement-based quantum computation graph states flow one-way quantum computer" | paper-the-qubit-delusion @0.687 · beyond-the-qubit @0.660 · zbw-majorana-tqc @0.657 |
| 7 | Reification | "reification metaphor conflation formal system physical reality category error representation" | meta-pattern-of-reification-in-physics @0.669 · category-error-of-the-ego @0.672 · pile-of-babel @0.651 |

## Cross-system ID validation (resolve_paper_id)

| Slug | Result | Verdict |
|---|---|---|
| conditional-truths-locale-framework | doi 10.5281/zenodo.21984929 · zenodo_doi 21983659 · identifier 21983324 · status published | OK — 3-DOI version chain (v0.1/v0.3/companion); expected, not an inconsistency |
| locale-framework-quantum-applications | doi==zenodo_doi==10.5281/zenodo.21991270 · r2_key qnfo-releases/2026/08/... | OK — clean, distributed |
| meta-pattern-of-reification-in-physics | identifier_type arxiv · id 5db96bbf00e4c4fa · r2_key qnfo/releases/2026/04/... | OK |

## KG + memory hits

- KG nodes: paper:conditional-truths-locale-framework (+ proj-conditional-truths-locale-framework), paper:locale-framework-quantum-applications, paper:meta-pattern-of-reification-in-physics (+ zenodo-19605446 + paper:the-meta-pattern-of-reification-in-physics — duplicate node set, data-quality note), paper:reification-and-non-archimedean-foundations-in-theoretical-physics.
- Memories: RES.011 Phase-0 precedent (WBS resolve → branch → PROJECT-PLAN → claim lock → tag); kaizen UIA integration pattern H (Q1–8 before Phase 2, Q9–15 before Phase 5).

## Adjacent WBS domains swept

- **UMP** (ultrametric physics): conditional-truths-locale-framework (UMP.011), locale-framework-quantum-applications (UMP.012), topology-of-quanta, post-quantum-synthesis, prime-valuation-qec-implications, zbw-majorana-tqc.
- **SLB** (laws of form): reentrant-distinctions @0.662 (diagrammatic calculus of marks — internal QNFO precedent for diagrammatic reasoning).
- **RES** (research archive): meta-pattern-of-reification-in-physics, there-are-no-theories, paper-the-qubit-delusion.
- **INM** (infomatics): massenergyentropyinformation-proof, thermodynamics-of-knowing, syntactic-token-calculus.

## External verification (arXiv)

| ID | Title / relevance |
|---|---|
| 2209.14894 | Wang, "Completeness of the ZX-calculus" — full-pure-qubit completeness via ZW translation |
| 1903.06035 | Jeandel–Perdrix–Vilmart, "Completeness of the ZX-Calculus" — Clifford+T, full language |
| 1602.08954 | Backens, "Completeness and the ZX-calculus" — stabilizer + Clifford+T + Spekkens toy theory |
| 1602.04744 | Backens–Perdrix–Wang, "A Simplified Stabilizer ZX-calculus" |
| 1709.08903 | Backens–Perdrix–Wang, "Towards a Minimal Stabilizer ZX-calculus" |
| 1706.09877 | Ng–Wang, "A universal completion of the ZX-calculus" |
| 1704.08670 | de Beaudrap–Horsman, "The ZX calculus is a language for surface code lattice surgery" — **spiders ↔ lattice-surgery merges (QEC import)** |
| 2601.04467 | Wan–Price–Yao, "Holographic codes seen through ZX-calculus" — **Pauli webs for holographic-code stabilizers, Rényi entropy, black-hole toy models (AdS/QG import)** |
| 2111.03114 | East–Martin-Dussaud–Van de Wetering, "Spin-networks in the ZX-calculus" — **SU(2)/LQG spin-network import** |
| 2407.10171 | Vandaele, "Qubit-count optimization using ZX-calculus" — gadgetization, Pauli Fusion |
| 2103.07264 | Majid, "Quantum and braided ZX calculus" — quantum-group import (u_q(sl_2)) |
| 2508.04296 | Carette–Cojocaru–Vilmart, "The decohered ZX-calculus" — classical/probabilistic fragment |
| 2607.04015 | Comfort–de Felice, "The Delayed Stabilizer ZX-Calculus" — translation-invariant/lattice codes |
| 2606.12383 | Stoltz, "Minimality of the Stabilizer ZX Calculus" |

**Key external finding:** the import-mixing the note describes is not hypothetical — the published
record shows ZX diagrams being loaded with imports from lattice surgery (QEC), holography/AdS-CFT
(entropy, black-hole toy models), loop quantum gravity (spin networks), and quantum groups —
each import accompanied by its own completeness/soundness story, with no published cross-silo
compatibility audit. The claim's falsifier (find the passing compatibility audit) did NOT turn up
in this sweep; the absence is the gap, not the proof.

## arXiv falsifier queries (external audit, reviewer pass-2, 2026-08-18)

Independent verification of the scoped negative claim "no published cross-silo compatibility
audit as of Aug 2026" — performed by the red-team reviewer (session 9AKEz5BZolb28GPQVl0eh)
with live arXiv API, 3 formulations:

| # | Query formulation | Results examined | Compatibility audit found? |
|---|---|---|---|
| F1 | ZX + compatibility/cross-silo semantics | 2 | No |
| F2 | diagrammatic + spin networks/holographic + compatibility | 15 | No |
| F3 | "Pauli webs" + holographic/LQG + ZX | 6 | No (only the import papers and Pauli-web applications) |

Total: 33 results examined, no published compatibility audit surfaced. Combined with the
Phase-1 sweep (14 arXiv records), the scoped negative claim survives independent spot-check.
