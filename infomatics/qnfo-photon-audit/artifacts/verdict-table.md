# Phase 3.1 — Final Verdict Table (v1.1)

**Project:** qnfo-photon-audit  
**Date:** 2026-07-21  
**Status:** Phase 3 — Synthesis and Audit Report (v1.1 revision)  
**Supersedes:** verdict-table v1.0  
**Scope:** All H1–H5 sub-hypotheses, final bin assignment, citation count, and outcome

---

## 1. Verdict Table

| Hypothesis | Sub-claim | Final Bin | Outcome | Key Citations | Artifact |
|-----------|-----------|-----------|---------|----------------|----------|
| **H1a** | Electron g-2 explained by Dirac equation (no internal EM structure needed) | **A** [Est] | CONFIRMED — non-evidential for photonic-substrate hypothesis (already required by relativistic QM) | CODATA 2022; Dirac (1928) | `lit-review-h1.md` |
| **H1b** | Knotted photon → electron observables (general) | **B** [Open] | GATE NOT MET — explicit Lagrangian + g-2 derivation not yet attempted; "hard but contingently open" per §1.3 criterion (no proven no-go theorem) | Rañada (1989, 1990); Burinskii (2000, 2015, 2023) | `lit-review-h1.md`, `h1-gate-memo.md` |
| **H1c** | EM knots produce spin-½ statistics from bosonic fields | **C** [Blocked] | BLOCKED — 4 circumvention routes identified (anyons, geons, composite-boson, emergent-spacetime); none instantiated for photonic case. Composite-boson route (Suzuki 2017) is theoretically viable but unapplied. See `spin-statistics-barrier.md` §3b for per-route status. | Streater & Wightman (1964); Dowker & Sorkin (1996, 2001); Mund (2008); Suzuki (2017); Volovik (2007) | `spin-statistics-barrier.md` |
| **H1-G1** | KN soliton reproduces g=2 (classical) | **A** [Est] | PASS but non-evidential — g=2 required by relativity for any spin-½ particle | Burinskii (2000-2023) | `h1-gate-memo.md` |
| **H1-G2** | KN soliton produces g-2 QED corrections | **C** [Blocked] | BLOCKED — no derivation exists; requires full quantum gravity (KN quantization unsolved). Classified Bin C (not Bin B) per §1.3 criterion (2): unsolved foundational-theory dependency with no tractable incremental research program. | Burinskii (2023) | `h1-gate-memo.md` |
| **H2** | Holographic entanglement/geometry maps to photonic substrate | **C** [Unsup] | NO MAPPING — RT/MERA/causal sets are orthogonal frameworks; photons play no fundamental role in any | Nishioka et al. (2009); Bao et al. (2015) | `lit-review-h2.md` |
| **H2a** | Quantized Berry phase in knotted photonic vortex | **[Untested]** | INCONCLUSIVE — standard OAM Berry phase confirmed (non-discriminating); knot-specific measurement never published | Allen et al. (1992); Kedia et al. (2013) | `h2a-test-results.md` |
| **H2b** | Parameter-free knot→mass mapping | **C** [Unsup] | CONFIRMED BLOCKED — no mapping exists; knot invariants (integer) cannot span 6-order-of-magnitude mass spectrum without free parameters | Chernitskii (1999); Burinskii | `h2b-gate-memo.md` |
| **H3** | COTT enables computation beyond standard reversible logic | **C** [Unsup] | CONFIRMED BLOCKED — zero external COTT validation; standard reversible logic (Bennett 1973) already achieves zero dissipation | Bennett (1973); Landauer (1961); Frank (2018) | `lit-review-h3.md`, `h3-gate-memo.md` |
| **H4** | Adelic/p-adic QM provides pre-geometric photonic substrate | **C** [Unsup] | ULTRAMETRICITY IS GEOMETRIC, NOT PHOTONIC — no paper connects p-adic structure to photonic composition | Dragovich (2003, 2006); Vladimirov | `lit-review-h4.md` |
| **H4a** | Planck-scale ultrametricity → Rydberg-scale signal | **U** [Unfalsifiable] | UNFALSIFIABLE — free metric f(k) accommodates any null result. Reclassified from v1.0 Bin C- per adversarial review: unfalsifiability is epistemically more severe than ordinary evidence-absence. Standard QFT suppression 10⁻²⁷; geometric-mean 11.2 GHz signal is testable but any null can be absorbed. | — (original calculation) | `h4a-scale-estimate.md` |
| **H4b** | Independent p-fixing principle exists | **C** [Unsup] | CONFIRMED BLOCKED — no principle exists in any surveyed paper; p always a free/fitted parameter | Dragovich (2003, 2006); Pitkänen (1994) | `h4b-gate-memo.md` |
| **H5** | Reversible logic calorimetry validates COTT-beating dissipation | **[Confirmed, non-discriminating]** | Landauer bound holds universally across 6 independent physical systems; provides no support for COTT | Bérut et al. (2012); Gavrilov & Bechhoefer (2016) | `h5-verification.md` |
| **Spin-statistics** | Theorem constrains photonic-fundamental-particle claims | **[Established constraint]** | Not a mathematical absolute barrier (4 circumvention routes established in peer-reviewed literature), but remains a practical barrier — none of the 4 routes has been instantiated with a concrete photonic-substrate model. The composite-boson route (Suzuki 2017) is the least problematic path forward. | Dowker & Sorkin (1996, 2001); Mund (2008); Suzuki (2017); Volovik (2007) | `spin-statistics-barrier.md` |

---

## 2. Summary Statistics (v1.1)

| Metric | Count |
|--------|-------|
| Total sub-hypotheses evaluated | 13 |
| Bin A (Established, non-evidential) | 2 (H1a, H1-G1) |
| Bin B (Open, gate not met) | 1 (H1b) |
| Bin C (Blocked/Unsupported) | 7 (H1c, H1-G2, H2, H2b, H3, H4, H4b) |
| Bin U (Unfalsifiable) | 1 (H4a) |
| Untested/Inconclusive | 1 (H2a) |
| Confirmed non-discriminating | 1 (H5) |
| Total distinct external sources cited across all artifacts | 80+ (17 H1, 24 H2, 18 H3, 22 H4, 11 spin-statistics, minus overlaps) |
| Claims promoted from B→A or C→B during Phase 1.5 gating | 0 |

---

## 3. Overall Verdict

**No sub-hypothesis of the photonic-substrate claim cluster survives independent scrutiny at Bin A (evidentially supportive) status.** The two Bin A assignments (H1a, H1-G1) are non-evidential — they confirm results ALREADY required by standard relativistic quantum mechanics, providing no discriminating support for the photonic-substrate hypothesis specifically.

**Every distinctive claim of the photonic-substrate program (H1c, H2, H2b, H3, H4, H4b) is either blocked by an established physical theorem (spin-statistics), unsupported by any mapping in the literature (H2, H2b, H4), or has zero external peer-reviewed validation (H3/COTT, H4b/p-fixing). H4a additionally falls outside empirical adjudication entirely (Bin U, unfalsifiable).**

**The single most severe blocking condition is the electron g-2 anomalous magnetic moment (H1-G2):** no photonic-substrate or soliton model in the literature derives this quantity, which is the most precisely tested prediction in physics (1 part in 10¹²). Until a model produces this derivation, the core claim that "electrons are photonic solitons" cannot advance beyond Bin B.

---

## 4. Cross-Reference to Phase 0 Bin Table

This verdict table is compared against the Phase 0 independently re-derived bin table (`notebooks/phase0-bin-table.md`) for consistency. All Phase 0 expectations for H3 (Bin C) and H4b (Bin C) were CONFIRMED by Phase 1.5 gates. The Phase 0 expectation for H2b (Bin C) was also confirmed. No Phase 0 expectation was overturned during this audit.

**v1.1 revision note:** H4a was reclassified from Bin C- (v1.0) to Bin U (v1.1) per the adversarial review's Finding 3 — this is a taxonomic upgrade, not a scientific re-evaluation. The underlying evidence is unchanged; the classification now correctly reflects the epistemic severity of unfalsifiability as qualitatively distinct from ordinary evidence-absence.

---

## 5. v1.1 Changelog

| Row | Change | Reason |
|-----|--------|--------|
| H1c | Expanded Outcome column to reference all 4 circumvention routes; added Dowker & Sorkin, Mund, Volovik citations | Adversarial review Finding 1 (H1c not reconciled with cross-cutting analysis) |
| H1b | Added "hard but contingently open" justification referencing §1.3 criterion | Adversarial review Finding 2 (Bin B/C boundary) |
| H1-G2 | Added explicit Bin C justification referencing §1.3 criterion (2) for unsolved foundational-theory dependency | Adversarial review Finding 2 (Bin B/C boundary) |
| H4a | Reclassified Bin C- → Bin U; expanded Outcome | Adversarial review Finding 3 (unfalsifiability severity) |
| Spin-statistics | Softened Outcome from "NOT an absolute barrier" to two-part framing (mathematical vs. practical) | Adversarial review Finding 4 (headline softening) |
| Summary stats | Bin C count updated 8→7; Bin U added | H4a reclassification |
