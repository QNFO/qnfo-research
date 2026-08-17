# RESEARCH CONTINUITY REGISTRY — QNFO.INM.001

**Project:** Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport
**WBS:** QNFO.INM.001 · **Branch:** res/paper/signal-worker-boundary-confinement
**Created:** 2026-08-17 (v2.64 HARD protocol — paper carries pre-registered predictions P1–P3 + frontier question)
**Canonical case basis:** ODR Thesis v2.0 (10.5281/zenodo.21784489) + Quasiparticles v2.0 (10.5281/zenodo.21784490)

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Is the corrected surface trichotomy (field redistribution / mode confinement / non-reciprocal skin localization) **exhaustive and disjoint** under the non-Hermitian classification — i.e., does every boundary-localized transport phenomenon in gapped and point-gapped systems fall into exactly one of the three categories? | OPEN | Non-Hermitian classification literature review (line-gap vs point-gap invariants) + candidate counterexample search (Weyl Fermi arcs, higher-order NHSE, dislocation NHSE) | YES — a new-observable prediction per category would be pre-registerable |
| FQ2 | Do skin-localized bulk modes in the pure point-gap regime ever carry quantized conductance G = nG0 (PRE-REG-1 falsification)? | OPEN — pre-registered | Experimental NHSE transport platform (gain-switched laser, cold-atom NHSE, topolectrical circuits) | YES — PRE-REG-1 IS the scaffold |
| FQ3 | Does the composite-boson exception (C4: Cooper pairs break boson=signal) hold in TI/superconductor hybrid edge geometries? | OPEN — pre-registered | Hybrid TI-SC edge transport experiments | YES — PRE-REG-2 IS the scaffold |

## 2. FALSIFIABLE PREDICTIONS (P1–Pn)

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition | Status |
|:---|:-----------|:------------|:-----------|:--------------------------|:-------|
| P1 | Skin-localized bulk modes in the pure point-gap (NHSE) regime do NOT themselves carry quantized conductance G = nG0 and are NOT classical field redistribution; quantized conductance in non-Hermitian systems requires line-gap/biorthogonally protected edge channels (PRB 98, 245130; PRL 132, 113802) | 2026–2028 | Two-terminal conductance measurement in NHSE-metallic regime (gain-switched laser 2505.03658; cold atoms; topolectrical circuits) | Observation of G = nG0 quantization carried by skin-localized bulk modes absent a line-gap protected edge channel; or demonstration that NHSE localization is classical field redistribution | PRE-REGISTERED 2026-08-16; REVISED 2026-08-17 |
| P2 | Cooper-pair boundary transport does NOT obey the original boson=signal mapping (composite-boson exception C4 holds) | 2026–2029 | TI/superconductor hybrid edge transport; fluxonium qubit coherence studies | Cooper-pair boundary transport obeys boson=signal with no exception | PRE-REGISTERED 2026-08-16 |
| P3 | The surface/bulk distinction becomes experimentally indistinguishable as k_BT → Δ_gap (edge quantization vanishes with T/T_gap → 1) | 2026–2028 | Temperature-dependent edge conductance on Z₂ TI / QH platforms | Quantized edge conductance survives at k_BT >> Δ_gap | PRE-REGISTERED 2026-08-16 |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- **FQ1 disconfirmed if:** any boundary-localized transport phenomenon is found that does not fall into exactly one of the three classes, OR a fourth mechanism is shown to produce boundary-localized transport.
- **FQ2 disconfirmed if:** PRE-REG-1's falsification condition fires (G = nG0 from skin-localized modes in pure point-gap regime).
- **FQ3 disconfirmed if:** PRE-REG-2's falsification condition fires (Cooper-pair transport obeys boson=signal without exception).

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-INM001-001 (P1) | NHSE-metallic regime: no G = nG0 quantization from skin modes | Quantized conductance from skin-localized modes absent line gap | 2-terminal G(T,B) in NHSE platforms; report + pre-registered analysis script | 2028-12-31 |
| REG-INM001-002 (P2) | Cooper-pair boundary transport breaks boson=signal | Closed boson=signal mapping under composites | TI-SC hybrid edge transport / fluxonium coherence data | 2029-12-31 |
| REG-INM001-003 (P3) | Edge quantization vanishes continuously as k_BT → Δ_gap | Quantization survives k_BT >> Δ_gap | G(T) on TI/QH platforms across T_gap | 2028-12-31 |

## 5. CALIBRATION REGISTER

| Date | Prediction | Strength | Outcome | Calibration note |
|:-----|:-----------|:---------|:--------|:-----------------|
| 2026-08-16 | PRE-REG-1 as worded | strong (KIF-60 pre-registration) | RETRODICTION-risk identified by red-team (N-1): reworded 2026-08-17 with point-gap/line-gap scoping + boundary refs [18,19] | Calibration improved: unqualified "no quantization in any non-Hermitian system" was overbroad; scoped claim is testable |
| [CHECK: 2027] | P1–P3 | — | — | Annual re-check: literature + experimental status |

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Depends on | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Publish v0.3 (Zenodo newversion; frontmatter DOI patch per NEWVERSION-FRONTMATTER-CARRYOVER-1) | publish-readiness-v0.3.md steps | 2026-08 |
| P1 | NHSE transport experiment monitoring for PRE-REG-1 (literature watch: arXiv + OpenAlex on quantized conductance in NHSE) | published v0.3 | 2026-09–2028 |
| P1 | Non-Hermitian classification review for FQ1 (line-gap vs point-gap taxonomy vs the three classes) | — | 2026-10 |
| P2 | TI-SC hybrid edge transport literature watch for PRE-REG-2 | — | ongoing |

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- **2026-08-16:** P1–P3 pre-registered in Phase 1b KIF-60 gate (bayesian-evidential-weight.md, commit 03ac213).
- **2026-08-17:** PRE-REG-1 revised (point-gap scoping + refs 18/19; commit 66764cd). Registry created (v2.64 HARD; this file).
- **Maintenance protocol:** update this file on every project session that touches P1–P3/FQ1–FQ3; re-check calibration register annually ([CHECK: YYYY]); log every experimental/literature contact with P1–P3 status changes; NEVER delete a row — supersede with status notes (immutable history).
