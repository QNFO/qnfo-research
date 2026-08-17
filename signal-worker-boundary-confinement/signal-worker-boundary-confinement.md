---
title: "Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport"
author: "Quni-Gudzinas, Rowan Brad"
orcid: "0009-0002-4317-5604"
affiliation: "QNFO Research Collective"
date: "2026-08-17"
version: "v0.3"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21974194"
status: "published"
keywords: ["Signal-Worker ontology", "topological insulators", "bulk-boundary correspondence", "Meissner effect", "quantum Hall effect", "non-Hermitian skin effect", "skin effect", "bundled conductors", "Litz wire", "band structure", "Weyl semimetals", "Cooper pairs", "spin-statistics theorem"]
---

**Author:** Quni-Gudzinas, Rowan Brad (QNFO Research Collective)
**ORCID:** 0009-0002-4317-5604
**Date:** 2026-08-17
**Version:** v0.3
**WBS:** QNFO.INM.001 · **Slug:** signal-worker-boundary-confinement
**Status:** Published v0.3 (2026-08-17 — DOI 10.5281/zenodo.21974194; concept 10.5281/zenodo.21931224)

---

## Abstract

The Signal-Worker (S-W) ontology — boson = *signal* (the delocalized field instruction), fermion = *worker* (the localized state that performs work) — is the QNFO corpus's proposed decomposition of the wave–particle duality fog. This paper delivers the red-team-hardened correction of that ontology's boundary-confinement reading, following a 3-slot adversarial audit (2026-08-14) that found 5 HARD defects. The correction is a taxonomy, not a renaming: only *mode-confinement* phenomena (topological insulators, the quantum Hall effect, and the non-Hermitian skin effect) confine fermionic transport to the material boundary; the Meissner effect and the AC skin effect expel the *field/current density* while the electrons (the "workers") continue to flow through the bulk. The mapping also fails on composite bosons (Cooper pairs — two fermions condensing into one boson) and self-conjugate particles (Majorana zero modes), and the corpus's own flagship substrate (TaAs, a Weyl semimetal with a gapless conducting bulk) contradicts the "worker excluded from the bulk" claim. Every claim carries an epistemic label and a falsifiability condition; the ontology itself is explicitly labeled an unconfirmed internal proposal. **Why a reader should care:** the corrected taxonomy determines where "the worker is confined to the surface" is physically true (topological insulators, quantum Hall, non-Hermitian skin effect) and where it is a category error (Meissner, skin effect) — a distinction that decides which boundary phenomena can carry quantized transport and which cannot, with direct consequences for interpreting conductance measurements and for the corpus's superconductivity program. **Premise-depth disclosure:** the TERRITORY claims are as deep as the published physics they cite (bulk–boundary correspondence, spin-statistics, non-Hermitian topology); the MAP claims are derived from the ontology's own primitives (signal = delocalized field instruction, worker = localized state that performs work) and the imported corpus records [7–15]; the framework's premises END at the pre-registered falsifiability conditions P1–P3 (§10) — no deeper postulate is claimed.

**v0.2 (2026-08-16).** This newversion adds a classical-electrodynamics companion section (§3.6: bundling practice, skin-depth thresholds, and the quantum origin of the bulk–insulator distinction) and completes the deposited source set with `references.bib` and `citation-audit.md`. No changes to the v0.1 taxonomy or falsifiability register.

**v0.3 (2026-08-17, published).** Engages the NHSE literature in depth — the consolidated review [16] and the experimental realization [17] — naming non-reciprocal skin localization as the third member of the surface trichotomy; embeds the KIF-60 pre-registered predictions (P1–P3) in the falsifiability register (§10); closes the zero-in-text citation gaps on refs [6], [13], [15]. Red-team remediation (2026-08-17, commit 66764cd) scoped PRE-REG-1 with the point-gap/line-gap boundary condition and added the quantized-transport boundary literature [18,19]. Published 2026-08-17 as 10.5281/zenodo.21974194 (newversion of 10.5281/zenodo.21969297; concept 10.5281/zenodo.21931224).

---

## 1. Introduction and Positioning

The Signal-Worker ontology originates in five QNFO corpus records: *Unifying Photosynthetic Energy Transduction and Ambient Superconductivity* [7], *Structural versus Driven Quantum Coherence* [8], *Quantum Architectonics* [9], *Gauge-Invariant Field Theory of Signal-Worker Interactions* [10], and *Quantum Abacus* [11]. It proposes that bosons (photons/phonons) act *strictly as informational signals* directing localized fermions (electrons/excitons) to perform work, and that this functional decomposition is "non-dualistic."

A 3-slot CMD RED TEAM SUB (Accuracy / Completeness / Dependency, 2026-08-14) audited the ontology's central reading — *"the signal orders where the worker may act; in topologically-protected phases the worker is excluded from the bulk and confined to the boundary."* Verdict: the underlying physics claims are accurate (Accuracy: 0 HARD), but the unifying reading is overgeneralized (Completeness: 5 HARD) and the corpus carries a terminology collision (Dependency: LCI used for two different concepts). This paper formalizes the corrected position.

**Scope.** This paper does NOT re-derive the S-W ontology or the topological-material corpus (see the deep-due-diligence report, companion artifact). It corrects the boundary-confinement claim, the composite-particle mapping, and the epistemic status of the ontology, and it fixes the LCI terminology collision. v0.2 adds §3.6 — the classical-EM companion that applies this correction to engineering practice — plus the two missing provenance files.

---

## 2. The Signal-Worker Ontology, Stated

| Role | Carrier | What it does | Corpus label |
|:-----|:--------|:-------------|:-------------|
| **Signal** | boson (photon / phonon) | carries the *instruction* — a delocalized field modifier | information |
| **Worker** | fermion (electron / exciton) | performs the *work* — a localized state vector | action |

**Statement 1 [MAP — interpretive, proposed].** Wave–particle duality is functionally decomposable into a bosonic *instruction* role and a fermionic *action* role in driven non-equilibrium systems. *Status: internal proposal; unconfirmed; ambient superconductivity has never been achieved.* The framing is *hierarchical* (the signal orders the worker), so it is not non-dualistic in the strict sense — it privileges one pole.

---

## 3. The Established Physics: Surface vs Bulk — a Taxonomy

The counterintuitive surface-vs-bulk phenomena the ontology cites are real, but they are **mechanistically heterogeneous**. They split into three classes: (i) **mode confinement** — boundary-localized transport with gapped/inert bulk (topological insulators §3.1, quantum Hall effect §3.2, non-Hermitian skin effect §3.5); (ii) **field expulsion** — the field leaves the bulk while the carriers stay (Meissner §3.3); (iii) **current-density redistribution** — no confinement at all (AC skin effect §3.4). The trichotomy is fixed by mechanism, not by scale (§3.6, §4).

### 3.1 Mode confinement (topological insulators) — TERRITORY

A 3D Z₂ topological insulator has a gapped (insulating) bulk and hosts gapless, metallic *surface* states [1,2]. The surface states are protected by time-reversal symmetry and the bulk Z₂ index via the bulk–boundary correspondence. **Electron transport is genuinely confined to the boundary.** This is a *mode-confinement* phenomenon: the bulk does not conduct, the surface does, and the surface modes are spin-momentum locked (helical).

### 3.2 Mode confinement (quantum Hall effect) — TERRITORY

In a 2D electron gas at strong magnetic field, the quantized Hall conductance is carried by **chiral edge channels**; the bulk is inert [2]. Again, transport is genuinely boundary-localized (chiral, in this case).

### 3.3 Field expulsion (Meissner effect) — TERRITORY

A superconductor actively **expels** the magnetic field: B ≈ 0 in the bulk, with the field decaying over the London penetration depth (λ_L ≈ 10–100 nm) [2]. This is *active expulsion*, distinct from a perfect conductor's flux-trapping. **Crucially, the electrons do NOT leave the bulk** — they flow through it as a dissipationless supercurrent. The London depth is the *field's* decay length, not an electron-localization length. The "worker" stays; the "field" leaves. The corpus's own superconductivity-validation record — *Superconductivity Quadrangle* [13] — is consistent with this reading: tensor-locked resilience in topological substrates concerns the condensate and its screening response, not boundary confinement of the carriers.

### 3.4 Current-density redistribution (AC skin effect) — TERRITORY

At high frequency, AC current density crowds toward the conductor surface over the skin depth δ ∝ 1/√f. This is a *current-density redistribution* within the conductor — **no particle confinement**, no boundary-localized eigenmodes.

### 3.5 Mode collapse (non-Hermitian skin effect) — TERRITORY (external, recent)

Under non-Hermiticity (gain/loss or asymmetric hopping), the **non-Hermitian skin effect (NHSE)** drives *all* bulk eigenmodes to collapse onto the boundary (Yao–Wang 2018) [3]. This is the literal "bulk → boundary" analog and the most on-point mode-confinement phenomenon for the ontology's vocabulary — and it is absent from the S-W corpus (a Completeness finding of the 2026-08-14 audit). [v0.3] The mechanism is now consolidated: the review literature [16] systematizes the modified non-Bloch bulk–boundary correspondence — spectral-winding and point-gap invariants replace the Hermitian Z₂/Chern classification — and the effect has been **experimentally realized**: an ultrafast topological non-Hermitian skin mode bound to a frequency-jump interface inside a gain-switched semiconductor laser, with direct intensity sampling of the skin modes (583 ± 16 fs FWHM) [17]. NHSE is therefore the third member of the surface trichotomy — **non-reciprocal skin localization** — distinct from both classical field redistribution (§3.4) and Hermitian mode confinement (§3.1–3.2). Its defining quantity is the point-gap winding number, an integer count, not a length scale. Quantized conductance in non-Hermitian systems arises only from line-gap/biorthogonally protected edge channels — demonstrated for non-Hermitian Chern insulators (Yu & Zhai 2018 [18]) — never from skin-localized bulk modes alone; NHSE can even localize chiral edge states outright (Liu et al. 2024 [19]). PRE-REG-1 (§10) codifies this boundary condition.

---

### 3.6 Engineering companion: bundling, skin-depth thresholds, and the quantum bulk–insulator boundary [v0.2]

A recurring misreading holds that conductors are *bundled* because of the skin effect. The engineering record says otherwise — and the distinction is a live instance of the category discipline of §4. [TERRITORY — claimed identity; disconfirmed if the engineering record shows skin-effect mitigation as the dominant bundling motive at mains frequency (it does not: stranded = flexibility, HV bundled = corona suppression, Litz = high-frequency only)]

**Bundling practice.** Three distinct practices are conflated under "bundling":

- **Stranded conductors** (ordinary copper cable) exist for mechanical flexibility. At 50/60 Hz the skin depth in copper is $\delta = \sqrt{2\rho/\omega\mu} \approx 9.2$ mm at 50 Hz and $\approx 8.4$ mm at 60 Hz (computed with $\rho = 1.678\times10^{-8}\ \Omega\text{m}$, $\mu = \mu_0$; BP-10 recompute 2026-08-17), so stranded wires below ~17 mm overall diameter conduct through essentially the full cross-section at mains frequency.
- **Bundled conductors on high-voltage lines** (2–4 subconductors per phase, usually aluminum conductor steel-reinforced — ACSR, not copper) exist primarily to suppress **corona discharge** by reducing the surface electric-field gradient. Electrically, bundling lowers the series inductance (larger effective geometric mean radius) and raises the shunt capacitance (larger equivalent radius), which raises the surge-impedance loading and the power-transfer capability.
- **Litz wire** (individually insulated strands) is the only bundling scheme whose purpose *is* the skin/proximity effect — and it exists for high-frequency use, not mains.

So the AC skin effect is real, but almost none of the wire we see is bundled because of it. The error is a category slip: a *field/current-density* phenomenon (skin effect) is misattributed as the motive for a *structural* practice (bundling) — the same slip the corrected taxonomy of §4 exists to prevent.

**Where quantum effects actually enter the bulk–insulator boundary.** The conductor/insulator distinction itself is quantum mechanical: copper conducts because its band structure provides a partially filled band of delocalized Bloch states, while an insulator presents a filled valence band plus a gap. The AC skin effect, by contrast, is classical Maxwell electrodynamics — no quantum input is required at macroscopic scales. Quantum physics becomes explicit for surface-vs-bulk questions when a length scale approaches the Fermi wavelength ($\lambda_F \approx 0.46$ nm in copper) or the electron mean free path (~40 nm at room temperature): conductance quantization in integer multiples of the conductance quantum $G_0 = 2e^2/h$, ballistic transport, quantum confinement, and — genuinely quantum and genuinely boundary-localized — the topological surface states of §3.1, protected by bulk topology. The skin effect and the topological boundary are therefore *not* the same kind of "surface": the former is a classical field redistribution inside a conductor; the latter is a mode-confinement effect. The §4 category distinction survives the nanoscale.

**S-W reading.** In Signal-Worker vocabulary: under the AC skin effect, the *signal* (the electromagnetic field) is redistributed toward the surface while the *workers* (the conduction electrons) remain distributed through the bulk; in a topological insulator, the boundary *modes* carry the work. Nothing in this companion section changes the v0.1 taxonomy — it supplies the engineering and quantum-threshold context in which that taxonomy is applied.

---

## 4. The Category Error and Its Correction

**Finding [HARD].** The S-W reading "the worker is excluded from the bulk and confined to the boundary" conflates **field/current-density expulsion** (Meissner, skin effect) with **mode confinement** (topological insulator, quantum Hall). They are different physical mechanisms with different consequences for where the "worker" may act.

**Correction (this paper's primary claim):**

| Class | Phenomena | What is at the boundary | Does the "worker" (electron) leave the bulk? |
|:------|:----------|:------------------------|:---------------------------------------------|
| Mode confinement | TI surface states, QH edge channels, NHSE | Electron transport modes | **Yes** (bulk gapped/inert) |
| Field expulsion | Meissner effect | The B field | **No** (electrons flow through bulk) |
| Current-density redistribution | AC skin effect | The current density | **No** (redistribution, not confinement) |

**Statement 2 [MAP — to be defended].** The boundary-confinement reading of the S-W ontology is valid **only** for the mode-confinement class. A corrected framing must distinguish field-expulsion from mode-confinement. *Falsifiability condition C2: the corrected taxonomy is disconfirmed if it yields no new observable consequence beyond the standard bulk–boundary correspondence — i.e., if it is pure relabeling (the criterion the Prime Valuation Depth follow-on applied to itself).*

---

## 5. The Composite-Boson Problem

**Finding [HARD].** The ontology's flagship example is superconductivity, yet the superconducting charge carrier is a **bosonic Cooper pair** — two fermionic "workers" condensing into a "signal-like" boson. The mapping `boson = signal / fermion = worker` is **not closed under composite particles**:

- Cooper pairs (two fermions → one boson): the superconducting "worker" is a boson; in the condensate gauge invariance is spontaneously broken and the photon acquires mass (Anderson 1963 [6]) — a pairing-level fact the functional split does not generate. The corpus's own fluxonium record (*Ab Initio Architectonics* [15]) applies the S-W vocabulary to exactly such Cooper-pair devices, where the operative "worker" is the pair, not the electron.
- Phonons: bosons that serve as both the pairing *glue* (the signal) and a lattice excitation — the instruction/action split blurs.
- Majorana zero modes (self-conjugate, neither boson nor fermion): fall outside both labels. The corpus itself works this thread (ZBW-Majorana, [14]).

**Correction.** The functional split is a *regime-specific interpretation*, not a universal classification. It must explicitly exclude composites and self-conjugate particles.

---

## 6. Spin-Statistics Engagement

**Finding.** "boson = signal / fermion = worker" is a teleological gloss over the real boson/fermion distinction — the **spin-statistics theorem** (integer vs half-integer spin). The ontology re-describes a kinematic fact without deriving a new observable.

**Correction.** The corrected framing must engage spin-statistics directly: the *kinematic* distinction (integer/half-integer spin → symmetric/antisymmetric statistics) is the ground truth; the *functional* signal/worker roles are a valid interpretation only where field modifiers and localized carriers are mechanistically distinct (driven non-equilibrium regimes).

---

## 7. The Weyl-Semimetal Counterexample

**Finding [HARD].** The corpus's own flagship substrate is **TaAs, a Weyl semimetal** — with a **gapless, conducting bulk** and Fermi-arc *surface* states (Quantum Abacus [11]; Xu et al. 2015 [5]; Wan et al. 2011 [4]). The corpus additionally contains *Hamiltonian Engineering of Topological Deconfinement in Weyl Semimetals* [12], which already engages Weyl physics directly. Weyl semimetals are **not** Z₂ topological insulators: the bulk conducts. Therefore "the worker is excluded from the bulk" is **false for the corpus's own material**.

**Correction.** The paper must distinguish: (a) gapped-bulk mode confinement (TI/QH), (b) gapless-bulk Weyl/Dirac semimetals (Fermi arcs — boundary states *on top of* a conducting bulk). The S-W vocabulary may describe Fermi arcs as boundary-*enhanced* work, but not as bulk-*excluded* work.

---

## 8. The LCI Acronym Collision

**Finding [HARD — dependency].** The corpus uses **LCI** for two different concepts:

| Record | LCI = |
|:-------|:------|
| Gauge-Invariant Field Theory [10] (10.5281/zenodo.18466522) | **Logical Cloning Prohibition** (Ward identity of the Signal gauge field) |
| Structural vs Driven [8] (10.5281/zenodo.18441402); Quantum Architectonics [9] (10.5281/zenodo.18515458) | **Lossless Complexity Index** |

**Correction.** This paper uses **LCI** only for *Logical Cloning Prohibition* [10] and spells out *Lossless Complexity Index* in full wherever it appears [8,9]. Any cross-corpus citation must disambiguate.

---

## 9. The Corrected Signal-Worker Framing

The corrected framing is a **three-part statement**:

1. **[TERRITORY — claimed identity; disconfirmed if a boundary-localized transport phenomenon falls outside all three classes (mode confinement / field expulsion / current-density redistribution), or if fermionic boundary transport is observed in a gapless-bulk geometry without bulk conduction]** The boson/fermion distinction is the spin-statistics theorem (kinematic). Surface-vs-bulk transport splits into mode confinement (TI, QH, NHSE — boundary-localized transport, gapped/inert bulk), field expulsion (Meissner — field leaves, electrons stay), and current-density redistribution (skin — no confinement).
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
| P1 | Skin-localized bulk modes in the pure point-gap (NHSE) regime do NOT themselves carry quantized conductance G = nG0 and are NOT classical field redistribution; quantized conductance in non-Hermitian systems requires line-gap/biorthogonally protected edge channels [18], and NHSE can localize such chiral edge channels [19] | MAP (pre-registered, KIF-60) | observation of G = nG0 quantization carried by skin-localized bulk modes absent a line-gap protected edge channel, or demonstration that NHSE localization is classical field redistribution | PRE-REGISTERED 2026-08-16; REVISED 2026-08-17 |
| P2 | Cooper-pair boundary transport does NOT obey the original boson=signal mapping (composite-boson exception C4 holds) | MAP (pre-registered, KIF-60) | Cooper-pair boundary transport obeys boson=signal with no exception | PRE-REGISTERED 2026-08-16 |
| P3 | The surface/bulk distinction becomes experimentally indistinguishable as k_BT → Δ_gap (edge quantization vanishes with T/T_gap → 1) | MAP (pre-registered, KIF-60) | quantized edge conductance survives at k_BT >> Δ_gap | PRE-REGISTERED 2026-08-16 |

**[v0.3] Pre-registration (KIF-60, 2026-08-16).** Rows P1–P3 are the risky predictions pre-registered in the Phase 1b Bayesian Evidential Weight gate (`artifacts/bayesian-evidential-weight.md`, commit 03ac213, sha256 064e1ee6…). C1 is established physics (zero novelty weight); C2 is [RETRODICTION] until P1–P3 are tested; P1 is the only claim with a pre-registered experimental falsification path (platform: [17]). **P1 was revised 2026-08-17 (commit 66764cd)** with the line-gap/biorthogonal scoping and boundary-condition refs [18,19]; the original 2026-08-16 wording is preserved in the BEW file's revision record.

---

## 11. Conclusion

The counterintuitive surface physics of topological conductors is real and correctly described — but it is **narrower** than the Signal-Worker framing claimed. "Electron confined to the surface" holds for topological insulators, the quantum Hall effect, and the non-Hermitian skin effect (gapped/inert bulk → boundary transport). It does *not* hold for the Meissner effect or the AC skin effect (field/current expulsion — electrons still flow through the bulk), and it does *not* hold for the corpus's own Weyl-semimetal substrate (conducting bulk with Fermi arcs). The Signal-Worker ontology, corrected, is a *regime-specific functional interpretation*, explicitly unconfirmed, with its composite-particle, spin-statistics, and terminology gaps closed. The physics survives the audit; the ontology, corrected, survives it too — as a falsifiable MAP, not as established doctrine. The falsifiability register now carries three pre-registered risky predictions (P1–P3, §10): experimental confirmation of any of them would give the corrected ontology positive evidential weight; until then its MAP claims remain explicitly unconfirmed.

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
16. R. Lin, T. Tai, L. Li, and C. H. Lee. *Topological non-Hermitian skin effect*. Frontiers of Physics, 18(5):53605, 2023. DOI 10.1007/s11467-023-1309-z.
17. B. Schneider, A. Dikopoltsev, M. Bestler, P. Täschler, M. Beck, D. Burghoff, O. Zilberberg, and J. Faist. *Ultrafast Non-Hermitian Skin Effect*. arXiv:2505.03658, 2025.
18. C. Yu and H. Zhai. *Hall conductance of a non-Hermitian Chern insulator*. Physical Review B, 98:245130, 2018. DOI 10.1103/PhysRevB.98.245130.
19. G.-G. Liu, S. Mandal, P. Zhou, X. Xi, R. Banerjee, Y.-H. Hu, M. Wei, M. Wang, Q. Wang, Z. Gao, H. Chen, Y. Yang, Y. Chong, and B. Zhang. *Localization of Chiral Edge States by the Non-Hermitian Skin Effect*. Physical Review Letters, 132:113802, 2024. DOI 10.1103/PhysRevLett.132.113802.
