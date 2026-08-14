---
title: "Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport"
author: "Quni-Gudzinas, Rowan Brad"
orcid: "0009-0002-4317-5604"
affiliation: "QNFO Research Collective"
date: "2026-08-14"
version: "v0.1"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21931225"
status: "published"
keywords: ["Signal-Worker ontology", "topological insulators", "bulk-boundary correspondence", "Meissner effect", "quantum Hall effect", "non-Hermitian skin effect", "Weyl semimetals", "Cooper pairs", "spin-statistics theorem"]
---

**Author:** Quni-Gudzinas, Rowan Brad (QNFO Research Collective)
**ORCID:** 0009-0002-4317-5604
**Date:** 2026-08-14
**Version:** v0.1
**WBS:** QNFO.INM.001 · **Slug:** signal-worker-boundary-confinement
**Status:** Phase 2 draft (post red-team)

---

## Abstract

The Signal-Worker (S-W) ontology — boson = *signal* (the delocalized field instruction), fermion = *worker* (the localized state that performs work) — is the QNFO corpus's proposed decomposition of the wave–particle duality fog. This paper delivers the red-team-hardened correction of that ontology's boundary-confinement reading, following a 3-slot adversarial audit (2026-08-14) that found 5 HARD defects. The correction is a taxonomy, not a renaming: only *mode-confinement* phenomena (topological insulators, the quantum Hall effect, and the non-Hermitian skin effect) confine fermionic transport to the material boundary; the Meissner effect and the AC skin effect expel the *field/current density* while the electrons (the "workers") continue to flow through the bulk. The mapping also fails on composite bosons (Cooper pairs — two fermions condensing into one boson) and self-conjugate particles (Majorana zero modes), and the corpus's own flagship substrate (TaAs, a Weyl semimetal with a gapless conducting bulk) contradicts the "worker excluded from the bulk" claim. Every claim carries an epistemic label and a falsifiability condition; the ontology itself is explicitly labeled an unconfirmed internal proposal.

---

## 1. Introduction and Positioning

The Signal-Worker ontology originates in five QNFO corpus records: *Unifying Photosynthetic Energy Transduction and Ambient Superconductivity* [7], *Structural versus Driven Quantum Coherence* [8], *Quantum Architectonics* [9], *Gauge-Invariant Field Theory of Signal-Worker Interactions* [10], and *Quantum Abacus* [11]. It proposes that bosons (photons/phonons) act *strictly as informational signals* directing localized fermions (electrons/excitons) to perform work, and that this functional decomposition is "non-dualistic."

A 3-slot CMD RED TEAM SUB (Accuracy / Completeness / Dependency, 2026-08-14) audited the ontology's central reading — *"the signal orders where the worker may act; in topologically-protected phases the worker is excluded from the bulk and confined to the boundary."* Verdict: the underlying physics claims are accurate (Accuracy: 0 HARD), but the unifying reading is overgeneralized (Completeness: 5 HARD) and the corpus carries a terminology collision (Dependency: LCI used for two different concepts). This paper formalizes the corrected position.

**Scope.** This paper does NOT re-derive the S-W ontology or the topological-material corpus (see the deep-due-diligence report, companion artifact). It corrects the boundary-confinement claim, the composite-particle mapping, and the epistemic status of the ontology, and it fixes the LCI terminology collision.

---

## 2. The Signal-Worker Ontology, Stated

| Role | Carrier | What it does | Corpus label |
|:-----|:--------|:-------------|:-------------|
| **Signal** | boson (photon / phonon) | carries the *instruction* — a delocalized field modifier | information |
| **Worker** | fermion (electron / exciton) | performs the *work* — a localized state vector | action |

**Statement 1 [MAP — interpretive, proposed].** Wave–particle duality is functionally decomposable into a bosonic *instruction* role and a fermionic *action* role in driven non-equilibrium systems. *Status: internal proposal; unconfirmed; ambient superconductivity has never been achieved [SOFT-9].* The framing is *hierarchical* (the signal orders the worker), so it is not non-dualistic in the strict sense — it privileges one pole.

---

## 3. The Established Physics: Surface vs Bulk — a Taxonomy

The counterintuitive surface-vs-bulk phenomena the ontology cites are real, but they are **mechanistically heterogeneous**. They split into three classes:

### 3.1 Mode confinement (topological insulators) — TERRITORY

A 3D Z₂ topological insulator has a gapped (insulating) bulk and hosts gapless, metallic *surface* states [1,2]. The surface states are protected by time-reversal symmetry and the bulk Z₂ index via the bulk–boundary correspondence. **Electron transport is genuinely confined to the boundary.** This is a *mode-confinement* phenomenon: the bulk does not conduct, the surface does, and the surface modes are spin-momentum locked (helical).

### 3.2 Mode confinement (quantum Hall effect) — TERRITORY

In a 2D electron gas at strong magnetic field, the quantized Hall conductance is carried by **chiral edge channels**; the bulk is inert [2]. Again, transport is genuinely boundary-localized (chiral, in this case).

### 3.3 Field expulsion (Meissner effect) — TERRITORY

A superconductor actively **expels** the magnetic field: B ≈ 0 in the bulk, with the field decaying over the London penetration depth (λ_L ≈ 10–100 nm) [2]. This is *active expulsion*, distinct from a perfect conductor's flux-trapping. **Crucially, the electrons do NOT leave the bulk** — they flow through it as a dissipationless supercurrent. The London depth is the *field's* decay length, not an electron-localization length. The "worker" stays; the "field" leaves.

### 3.4 Current-density redistribution (AC skin effect) — TERRITORY

At high frequency, AC current density crowds toward the conductor surface over the skin depth δ ∝ 1/√f. This is a *current-density redistribution* within the conductor — **no particle confinement**, no boundary-localized eigenmodes.

### 3.5 Mode collapse (non-Hermitian skin effect) — TERRITORY (external, recent)

Under non-Hermiticity (gain/loss or asymmetric hopping), the **non-Hermitian skin effect (NHSE)** drives *all* bulk eigenmodes to collapse onto the boundary (Yao–Wang 2018) [3]. This is the literal "bulk → boundary" analog and the most on-point mode-confinement phenomenon for the ontology's vocabulary — and it is absent from the S-W corpus [H4].

---

## 4. The Category Error and Its Correction [H1]

**Finding [HARD].** The S-W reading "the worker is excluded from the bulk and confined to the boundary" conflates **field/current-density expulsion** (Meissner, skin effect) with **mode confinement** (topological insulator, quantum Hall). They are different physical mechanisms with different consequences for where the "worker" may act.

**Correction (this paper's primary claim):**

| Class | Phenomena | What is at the boundary | Does the "worker" (electron) leave the bulk? |
|:------|:----------|:------------------------|:---------------------------------------------|
| Mode confinement | TI surface states, QH edge channels, NHSE | Electron transport modes | **Yes** (bulk gapped/inert) |
| Field expulsion | Meissner effect | The B field | **No** (electrons flow through bulk) |
| Current-density redistribution | AC skin effect | The current density | **No** (redistribution, not confinement) |

**Statement 2 [MAP — to be defended].** The boundary-confinement reading of the S-W ontology is valid **only** for the mode-confinement class. A corrected framing must distinguish field-expulsion from mode-confinement. *Falsifiability condition C2: the corrected taxonomy is disconfirmed if it yields no new observable consequence beyond the standard bulk–boundary correspondence — i.e., if it is pure relabeling (the criterion the Prime Valuation Depth follow-on applied to itself).*

---

## 5. The Composite-Boson Problem [H3]

**Finding [HARD].** The ontology's flagship example is superconductivity, yet the superconducting charge carrier is a **bosonic Cooper pair** — two fermionic "workers" condensing into a "signal-like" boson. The mapping `boson = signal / fermion = worker` is **not closed under composite particles**:

- Cooper pairs (two fermions → one boson): the superconducting "worker" is a boson.
- Phonons: bosons that serve as both the pairing *glue* (the signal) and a lattice excitation — the instruction/action split blurs.
- Majorana zero modes (self-conjugate, neither boson nor fermion): fall outside both labels. The corpus itself works this thread (ZBW-Majorana, [14]).

**Correction.** The functional split is a *regime-specific interpretation*, not a universal classification. It must explicitly exclude composites and self-conjugate particles.

---

## 6. Spin-Statistics Engagement [SOFT-6]

**Finding.** "boson = signal / fermion = worker" is a teleological gloss over the real boson/fermion distinction — the **spin-statistics theorem** (integer vs half-integer spin). The ontology re-describes a kinematic fact without deriving a new observable.

**Correction.** The corrected framing must engage spin-statistics directly: the *kinematic* distinction (integer/half-integer spin → symmetric/antisymmetric statistics) is the ground truth; the *functional* signal/worker roles are a valid interpretation only where field modifiers and localized carriers are mechanistically distinct (driven non-equilibrium regimes).

---

## 7. The Weyl-Semimetal Counterexample [H2]

**Finding [HARD].** The corpus's own flagship substrate is **TaAs, a Weyl semimetal** — with a **gapless, conducting bulk** and Fermi-arc *surface* states (Quantum Abacus [11]; Xu et al. 2015 [5]; Wan et al. 2011 [4]). The corpus additionally contains *Hamiltonian Engineering of Topological Deconfinement in Weyl Semimetals* [12], which already engages Weyl physics directly. Weyl semimetals are **not** Z₂ topological insulators: the bulk conducts. Therefore "the worker is excluded from the bulk" is **false for the corpus's own material**.

**Correction.** The paper must distinguish: (a) gapped-bulk mode confinement (TI/QH), (b) gapless-bulk Weyl/Dirac semimetals (Fermi arcs — boundary states *on top of* a conducting bulk). The S-W vocabulary may describe Fermi arcs as boundary-*enhanced* work, but not as bulk-*excluded* work.

---

## 8. The LCI Acronym Collision [H5]

**Finding [HARD — dependency].** The corpus uses **LCI** for two different concepts:

| Record | LCI = |
|:-------|:------|
| Gauge-Invariant Field Theory [10] (10.5281/zenodo.18466522) | **Logical Cloning Prohibition** (Ward identity of the Signal gauge field) |
| Structural vs Driven [8] (10.5281/zenodo.18441402); Quantum Architectonics [9] (10.5281/zenodo.18515458) | **Lossless Complexity Index** |

**Correction.** This paper uses **LCI** only for *Logical Cloning Prohibition* [10] and spells out *Lossless Complexity Index* in full wherever it appears [8,9]. Any cross-corpus citation must disambiguate.

---

## 9. The Corrected Signal-Worker Framing

The corrected framing is a **three-part statement**:

1. **[TERRITORY]** The boson/fermion distinction is the spin-statistics theorem (kinematic). Surface-vs-bulk transport splits into mode confinement (TI, QH, NHSE — boundary-localized transport, gapped/inert bulk), field expulsion (Meissner — field leaves, electrons stay), and current-density redistribution (skin — no confinement).
2. **[MAP]** The S-W "instruction vs action" split is a valid *functional* interpretation in driven non-equilibrium regimes, and a valid *mode-confinement* statement only for the mode-confinement class. It is not a universal decomposition: it fails on composite bosons (Cooper pairs), self-conjugate particles (Majorana zero modes), and gapless-bulk Weyl semimetals.
3. **[EPISTEMIC]** The ontology is an **unconfirmed internal proposal**. Ambient superconductivity has never been achieved; the Ward-identity no-cloning derivation (LCI [10]) is flagged speculative and must be independently reproduced. Boundary confinement is a *transport* statement — it does NOT imply topological-QC fault tolerance at nonzero temperature (the corpus's own evidence synthesis refutes the FCI alternative via thermal anyon proliferation; see deep-due-diligence companion).

---

## 10. Falsifiability Register

| # | Claim | Type | Falsifiability condition | Status |
|:--|:------|:-----|:--------------------------|:-------|
| C1 | TI/QH confine fermionic transport to the boundary; Meissner/skin expel the field/current | established | — | established |
| C2 | The corrected taxonomy (field-expulsion vs mode-confinement) carries content beyond relabeling | MAP | no new observable consequence → relabeling | OPEN |
| C3 | LCI (Logical Cloning Prohibition) as a Ward identity, exponential-in-N scaling | MAP-speculative | independent derivation + reproduction fails | OPEN, flagged |
| C4 | Composite bosons (Cooper pairs) break the boson=signal/fermion=worker mapping | MAP | a closed mapping under composites exists | OPEN |

---

## 11. Conclusion

The counterintuitive surface physics of topological conductors is real and correctly described — but it is **narrower** than the Signal-Worker framing claimed. "Electron confined to the surface" holds for topological insulators, the quantum Hall effect, and the non-Hermitian skin effect (gapped/inert bulk → boundary transport). It does *not* hold for the Meissner effect or the AC skin effect (field/current expulsion — electrons still flow through the bulk), and it does *not* hold for the corpus's own Weyl-semimetal substrate (conducting bulk with Fermi arcs). The Signal-Worker ontology, corrected, is a *regime-specific functional interpretation*, explicitly unconfirmed, with its composite-particle, spin-statistics, and terminology gaps closed. The physics survives the audit; the ontology, corrected, survives it too — as a falsifiable MAP, not as established doctrine.

---

## Declarations

**Funding.** This work received no external funding.
**Competing interests.** The author declares no competing interests.
**Data availability.** No experimental data were generated or analyzed for this work. All literature evidence is cited with persistent identifiers.
**Code availability.** No code was required for this work.
**Ethics approval.** Not applicable.
**Preprint policy.** This manuscript is posted as a preprint; it has not been submitted to any journal.

---

## References

1. M. Z. Hasan and C. L. Kane. *Colloquium: Topological insulators*. Reviews of Modern Physics, 82:3045, 2010. DOI 10.1103/RevModPhys.82.3045.
2. X.-L. Qi and S.-C. Zhang. *Topological insulators and superconductors*. Reviews of Modern Physics, 83:1057, 2011. DOI 10.1103/RevModPhys.83.1057.
3. S. Yao and Z. Wang. *Edge states and topological invariants of non-Hermitian systems*. Physical Review Letters, 121:086803, 2018. DOI 10.1103/PhysRevLett.121.086803.
4. X. Wan, A. M. Turner, A. Vishwanath, and S. Y. Savrasov. *Topological semimetal and Fermi-arc surface states in the electronic structure of pyrochlore iridates*. Physical Review B, 83:205101, 2011. DOI 10.1103/PhysRevB.83.205101.
5. S.-Y. Xu et al. *Discovery of a Weyl fermion semimetal and topological Fermi arcs*. Science, 349:613, 2015. DOI 10.1126/science.aaa9297.
6. P. W. Anderson. *Plasmons, gauge invariance, and mass*. Physical Review, 130:439, 1963. DOI 10.1103/PhysRev.130.439.
7. QNFO Research Collective. *Unifying Photosynthetic Energy Transduction and Ambient Superconductivity via a Non-Dualistic Signal-Worker Ontology*. Zenodo, 2026. DOI 10.5281/zenodo.18330366.
8. QNFO Research Collective. *Structural versus Driven Quantum Coherence: A Proposed 'Signal-Worker' Framework for Ambient Superconductivity*. Zenodo, 2026. DOI 10.5281/zenodo.18441402.
9. QNFO Research Collective. *Quantum Architectonics: A Unified Framework for Substrate Engineering via Topological Genesis, Signal-Worker Dynamics, and Multi-Modal Control*. Zenodo, 2026. DOI 10.5281/zenodo.18515458.
10. QNFO Research Collective. *Gauge-Invariant Field Theory of Signal-Worker Interactions: Deriving the Logical Cloning Prohibition from First Principles of Quantum Architectonics*. Zenodo, 2026. DOI 10.5281/zenodo.18466522.
11. QNFO Research Collective. *Quantum Abacus: A Strain-Engineered Platform for Passive, Reversible Fermionic Computation*. Zenodo, 2026. DOI 10.5281/zenodo.18543167.
12. QNFO Research Collective. *Hamiltonian Engineering of Topological Deconfinement in Weyl Semimetals: Addressing the Thermal Scalability of Quantum Error Correction*. Zenodo, 2026. DOI 10.5281/zenodo.18222365.
13. QNFO Research Collective. *Superconductivity Quadrangle: Validating Tensor-Locked Resilience in Topological Substrates*. Zenodo, 2026. DOI 10.5281/zenodo.18496890.
14. R. Quni. *Vanishing ZBW Signal: The ZBW-Majorana Hypothesis as a Unified Framework for Topological Fermion Distinction*. Zenodo, 2026. DOI 10.5281/zenodo.21574555.
15. QNFO Research Collective. *Ab Initio Architectonics: Rethinking Fluxonium Qutrits through the Signal-Worker Ontology*. Zenodo, 2026. DOI 10.5281/zenodo.18447478.
