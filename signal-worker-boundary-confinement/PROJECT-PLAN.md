# PROJECT PLAN — QNFO.INM.001

**Title:** Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport
**Slug:** signal-worker-boundary-confinement
**WBS:** QNFO.INM.001 (parent: QNFO.INM — Infomatics)
**Repo:** QNFO/qnfo-research · **Branch:** res/paper/signal-worker-boundary-confinement
**Date:** 2026-08-14 · **Status:** Phase 0 (scaffold) — net-new project
**Origin:** CMD RED TEAM SUB 2026-08-14 — Signal-Worker / topological-conductors analysis produced 5 HARD findings (Accuracy PASS; Completeness 5 HARD; Dependency: LCI acronym collision). This project formalizes the corrected position.

---

## 1. Motivation

The Signal-Worker (S-W) ontology — boson = signal (the delocalized field instruction), fermion = worker (the localized state that performs work) — is the QNFO corpus's proposed decomposition of the wave–particle duality fog (Unifying Photosynthesis/Superconductivity 18330365; Structural-vs-Driven 18441401; Quantum Architectonics 18515457; Gauge-Invariant Field Theory 18466521; Quantum Abacus 18543167).

A 3-slot red-team audit of the ontology's "signal orders where the worker may act" reading found it **overgeneralizes** the genuine surface-vs-bulk physics of topological conductors. This project builds the corrected, red-team-hardened ontology.

## 2. Core Claim (LOCKED — P6)

See `artifacts/core-claim.md`. In brief:

- **[TERRITORY]** In topologically ordered (gapped-bulk) phases — Z₂ topological insulators and quantum-Hall systems — fermionic transport is confined to the boundary via bulk–boundary correspondence. The Meissner effect and AC skin effect expel the *field/current density*, not the particles.
- **[MAP]** The S-W boundary-confinement reading is overgeneralized: it fails for Meissner/skin (field expulsion ≠ mode confinement) and for the corpus's own Weyl-semimetal (TaAs, conducting bulk with Fermi arcs). A corrected framing must (a) fix the category error, (b) account for composite bosons (Cooper pairs), (c) engage spin-statistics, (d) be labeled an unconfirmed internal proposal.
- **Falsifiability:** disconfirmed if pure relabeling (no new observable beyond bulk–boundary correspondence + spin-statistics taxonomy).

## 3. Falsifiability Register

| # | Claim | Type | Falsifiability condition | Status |
|:--|:------|:-----|:--------------------------|:-------|
| C1 | TI/QH confine fermionic transport to the boundary; Meissner/skin expel the field/current | established | — | established (Physics, Accuracy-PASS) |
| C2 | Corrected S-W framing (field-expulsion vs mode-confinement distinction) carries content beyond relabeling | MAP | no new observable consequence → relabeling | OPEN |
| C3 | LCI (Logical Cloning Prohibition) as a Ward identity, exponential-in-N scaling | MAP-speculative | independent derivation + reproduction fails | OPEN, flagged |
| C4 | Composite bosons (Cooper pairs) break the boson=signal/fermion=worker mapping | MAP | a closed mapping under composites exists | OPEN |

## 4. Phase Plan

- **Phase 0 (this cycle):** WBS resolve (QNFO.INM.001) → branch → PROJECT-PLAN.md → core claim locked → commit/tag/push → registry INSERT. **DONE**
- **Phase 1 (next):** Due diligence — full-corpus sweep (KG-first, ≥3 query formulations/topic, cross-system ID validation, ≥2 adjacent WBS domains, external verification) per DUE-DILIGENCE-DEPTH-1.
- **Phase 2:** Write the corrected-ontology paper (md), applying all 5 red-team HARD findings.
- **Phase 3:** Verification — spin-statistics engagement, Cooper-pair accounting, NHSE inclusion, falsifiability register, citation audit.
- **Phase 5:** Publication (Zenodo newversion-ready; 3-file set + full source set; records-API schema).

## 5. Deliverables

- Phase 1: deep-due-diligence report + gap analysis
- Final: corrected-ontology paper (.md/.html/.pdf) + citation-audit.md + PROJECT-PLAN + README + artifacts

## 6. Adjacent Work (do NOT re-derive)

- Prime Valuation Depth (RES.005) + Implications for Computing/QEC (RES.006): no-cloning as monoidal-non-Cartesian / Ward identity — the S-W LCI thread extends this.
- Signal-Worker corpus (5 records above): the ontology source papers.
- QEC-Darwinism ultrametric (21819232): quantum-darwinism no-go.
