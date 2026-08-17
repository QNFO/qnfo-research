# PROJECT PLAN — QNFO.INM.001

**Title:** Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport
**Slug:** signal-worker-boundary-confinement
**WBS:** QNFO.INM.001 (parent: QNFO.INM — Infomatics)
**Repo:** QNFO/qnfo-research · **Branch:** res/paper/signal-worker-boundary-confinement
**Date:** 2026-08-17 · **Status:** Published v0.3 (10.5281/zenodo.21974194, 2026-08-17; concept 10.5281/zenodo.21931224); P8 complete. Version history: v0.1 10.5281/zenodo.21931225 → v0.2 10.5281/zenodo.21969297 → v0.3 10.5281/zenodo.21974194.
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

## 4. Phase Plan (all complete)

- **Phase 0:** WBS resolve (QNFO.INM.001) → branch → PROJECT-PLAN.md → core claim locked → commit/tag/push → registry INSERT. **DONE (2026-08-14)**
- **Phase 1:** Due diligence — full-corpus sweep per DUE-DILIGENCE-DEPTH-1. **DONE (2026-08-14; `artifacts/deep-due-diligence.md`)** + post-v0.2 re-sweep 2026-08-16 (commit 1e38ea7) + **Phase 1b KIF-29/KIF-60 gates DONE 2026-08-16** (`artifacts/consilience-gate.md`, `artifacts/bayesian-evidential-weight.md`, commit 03ac213).
- **Phase 2–4:** Drafting (all 5 red-team HARD findings applied), verification (spin-statistics, Cooper pairs, NHSE, register, citation audit), builds. **DONE (v0.1, 2026-08-14)**
- **Phase 5:** Publication. **DONE** — v0.1 10.5281/zenodo.21931225 (2026-08-14); v0.2 10.5281/zenodo.21969297 (2026-08-16: classical-EM companion §3.6 + full source set incl. references.bib + citation-audit.md).
- **Phase 8:** Distribution. **DONE (2026-08-16)** — D1 living-paper (v0.2), R2 mirror `qnfo-releases/2026/08/signal-worker-boundary-confinement/` (9 objects), KG node distributed + BELONGS_TO `prog-qnfo-inm`, papers.qnfo.org live.

## 4b. Next-Version Backlog (deposit-immutable SOFTs)

- Zenodo metadata `version` = None on 21969297 (records-API PUT 500s on this deployment; kaizen candidate LEGACY-PUT-VERSION-OMISSION-1).
- README/PROJECT-PLAN status docs — fixed in repo 2026-08-16; the v0.2 deposit carries the pre-fix "Phase 0" text (immutable).
- Refs [6]/[13]/[15] bibliography-only with zero in-text citations — pre-existing v0.1 structure, not a fold-in regression. **FIXED in v0.3 draft (2026-08-17)** — contextual citations added (§3.3, §5).

## 5. Deliverables

- Phase 1: deep-due-diligence report + gap analysis
- Final: corrected-ontology paper (.md/.html/.pdf) + citation-audit.md + PROJECT-PLAN + README + artifacts

## 6. Adjacent Work (do NOT re-derive)

- Prime Valuation Depth (RES.005) + Implications for Computing/QEC (RES.006): no-cloning as monoidal-non-Cartesian / Ward identity — the S-W LCI thread extends this.
- Signal-Worker corpus (5 records above): the ontology source papers.
- QEC-Darwinism ultrametric (21819232): quantum-darwinism no-go.
