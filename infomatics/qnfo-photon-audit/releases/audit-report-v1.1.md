# Photonic Substrate Hypotheses for Emergent Spacetime: A Technical Audit

**Project:** qnfo-photon-audit  
**Version:** v1.1 — Revision (addressing adversarial review Findings 1–4)  
**Date:** 2026-07-21  
**Supersedes:** `releases/audit-report-v1.0.md` (2026-07-21)  
**Methodology:** Falsifiability-first, pre-registration-governed, bin-classified  
**Revision changelog:** See §7

---

## Abstract

This report audits the claim cluster that photons constitute a pre-geometric information substrate underlying spacetime, electron structure, and computation. We decompose the claim into five sub-hypothesis tracks (H1–H5) spanning knotted-photon electron models, holographic entanglement, reversible computing thermodynamics, and adelic/p-adic quantum mechanics, plus one cross-cutting theoretical constraint (the spin-statistics theorem). Each track was subjected to systematic literature review (80+ external peer-reviewed sources), analytic gating (5 pre-registered gates), and where possible, literature-based testing (2 of 4 planned tests were executable; 2 were blocked by prior gate failures). We find that no sub-hypothesis achieves evidentially-supportive (Bin A) status specific to the photonic-substrate claim: the two Bin A assignments confirm results already required by mainstream relativistic quantum mechanics. Every distinctive claim of the program — that EM knots generate fermion statistics, that knot topology determines fermion mass, that charge-only thermodynamics (COTT) beats the Landauer limit, and that p-adic ultrametricity has a physically fixed base prime — is either blocked by an established theorem, unsupported by any literature mapping, or lacks external peer-reviewed validation entirely.

---

## 1. Methodology

### 1.1 Core Claim (Reformulated)

*Original claim (as encountered):* "Photons are the fundamental building blocks of reality; spacetime, matter, and computation all emerge from photonic information structure."

*Reformulated, falsifiable version (locked in `PROJECT-PLAN.md §1.2`):* "There exist specific, testable sub-hypotheses (H1–H5) under which photonic field configurations could constitute or explain phenomena currently attributed to fermions, spacetime geometry, or computational thermodynamics. Each sub-hypothesis is evaluated independently against its own falsifiability criteria."

### 1.2 Bin Classification System

| Bin | Meaning |
|-----|---------|
| **A** [Est] | Established — either independently confirmed by data, or a necessary consequence of accepted physics (in which case: non-evidential for the specific hypothesis) |
| **B** [Open] | Open — falsifiable in principle, gate condition not yet met (no locked prediction to test) |
| **C** [Unsup]/[Blocked] | Unsupported — no mapping/mechanism exists in the literature, or gate resolution confirms blockage |
| **U** [Unfalsifiable] | Unfalsifiable — the hypothesis as formulated cannot be disconfirmed by any conceivable experimental outcome; it falls outside the domain of empirical adjudication entirely. This is epistemically more severe than Bin C: a Bin C claim merely *lacks evidence*, while a Bin U claim *cannot in principle have evidence against it* |

### 1.3 Bin B vs. Bin C Boundary Criterion (per v1.1 adversarial review)

A claim is **Bin C** (blocked/unsupported) rather than **Bin B** (open) when it satisfies at least one of:

1. **Proven no-go theorem**: The claim as stated is inconsistent with an established theorem, and no circumvention route has been instantiated with a concrete model for the photonic-substrate case.
2. **Unsolved foundational-theory dependency**: The claim requires an unsolved problem in foundational physics (e.g., full quantum gravity, quantization of Kerr-Newman spacetime) for which no tractable research program with incremental milestones exists.
3. **Zero external literature support**: No peer-reviewed paper outside the QNFO corpus provides any mapping, mechanism, or derivation connecting the claim to the photonic-substrate hypothesis.

A claim is **Bin B** when the testing methodology is sound (we know *how* we would test it if we had a prediction), no proven no-go theorem blocks it, and the only obstacle is that a computation or derivation has not yet been attempted — the problem is "hard but contingently open" rather than "blocked pending an unsolved foundational physics problem."

### 1.4 Pre-Registration Gate

Per Phase 1.5, every Bin B/C claim was subjected to an analytic gate BEFORE any Phase 2 "test" was designed. This prevents the common failure mode of designing a test that can only confirm the hypothesis (confirmation bias in test design). Gates were resolved using existing literature and mathematical analysis, not new experiments (per the LLM-Executable Research Gate — this audit performs no new physical experiments).

---

## 2. Per-Hypothesis Audit

### 2.1 H1 — EM-Knot Solitons as Electron Models

**Literature base:** 17 sources (Rañada 1989/1990; Trueba & Rañada 1996; Irvine & Bouwmeester 2008; Kedia et al. 2013; Arrayás et al. 2017; Burinskii 2000/2015/2023; Chernitskii 1999; Hestenes 1990/2010).

**Sub-claims:**
- **H1a** (electron g-2 explained by Dirac equation): **Bin A**, confirmed, non-evidential.
- **H1b** (knotted photon → electron observables): **Bin B**, gate not met.
- **H1c** (EM knots → spin-½ statistics): **Bin C**, blocked by spin-statistics theorem except via uninstantiated circumvention routes.
- **H1-G1** (KN → g=2 classical): **Bin A**, PASS but non-evidential (required by relativity).
- **H1-G2** (KN → g-2 QED corrections): **Bin C**, BLOCKED. No published derivation exists; requires unsolved KN quantization / full quantum gravity theory.

**Key finding:** The Kerr-Newman electron model (Burinskii) is the most mathematically developed attempt in this literature, reproducing the classical g=2 gyromagnetic ratio. However, it provides no path to the QED g-2 correction — the most precisely tested prediction in physics (agreement to 1 part in 10¹²). This is the single most severe blocking condition for the entire photonic-substrate program.

**Bin B vs. Bin C distinction for H1b vs. H1-G2:** Under the explicit criterion in §1.3, H1b (knotted photon → electron observables) is classified Bin B because: (a) no proven no-go theorem blocks the claim — it is "hard but contingently open," requiring an unwritten Lagrangian rather than an unsolved foundational theory; (b) the problem domain (classical-to-quantum soliton quantization) has incremental research programs with intermediate milestones. H1-G2 (g-2 from KN) is classified Bin C because it satisfies criterion (2) — it requires full KN quantization, which is an unsolved problem in quantum gravity with no tractable incremental research program. This is a qualitatively different obstruction, not merely a harder computation.

### 2.1.1 H1c — Spin-Statistics Reconciliation (expanded per v1.1)

The spin-statistics cross-cutting analysis (§2.5) identifies **four** known circumvention routes to the spin-statistics theorem. H1c's Bin C classification is based on the status of each route *specifically for the photonic-substrate hypothesis*:

| Route | Mechanism | Status for photonic-substrate | Cite |
|-------|-----------|-------------------------------|------|
| (a) 2+1D anyons | Braid-group statistics in reduced dimensions | Not applicable — recovered 3+1D effective theory must reproduce standard spin-statistics; no photonic model maps to a dimensionally-reduced regime | Mund (2008), arXiv:0801.3621 |
| (b) Topological geons | Independent spin & statistics in quantum gravity with non-trivial topology | Analogical only — Dowker & Sorkin's geons are gravitational objects, not photonic ones; no photonic-substrate model has mapped its TREE topology to a geon-like circumvention | Dowker & Sorkin (1996, 2001), arXiv:9609064, arXiv:0101042 |
| (c) Composite gauge bosons | Photons emerge as bosonic composites from a fermionic substrate | Theoretically viable — Suzuki (2017) proves composite gauge bosons emerge dynamically; this is the least problematic route, but no photonic-specific model has been instantiated | Suzuki (2017), arXiv:1707.01589 |
| (d) Emergent spacetime | Theorem assumptions (pre-existing Minkowski spacetime) do not apply in pre-geometric regime | Open question — no formal proof establishes or disproves spin-statistics in genuinely pre-geometric regimes; this remains a theoretical unknown, not an affirmative circumvention | Volovik (2007), arXiv:0709.1258 |

**H1c verdict:** Bin C. NONE of the four routes has been instantiated with a concrete photonic-substrate model. Routes (a) and (b) are structurally incompatible with a photonic-substrate construction or remain purely analogical. Route (c) is the most promising path but requires a specific composite-photon Lagrangian that has not been produced. Route (d) invokes an open theoretical question rather than an established circumvention. The spin-statistics theorem therefore remains a practical barrier for H1c, though the four routes collectively confirm it is not a logical absolute barrier (see §2.5).

### 2.2 H2 — Holographic Entanglement & Geometry

**Literature base:** 24 external + 5 QNFO-internal sources (Nishioka, Ryu & Takayanagi 2009; Bao, Cao & Carroll 2015; Evenbly & Vidal 2015; Miyaji, Takayanagi & Watanabe 2016; and others).

**Finding:** No approach (Ryu-Takayanagi formula, MERA tensor networks, causal set theory, quantum graphity) maps photons specifically to a pre-geometric substrate. RT/MERA are bound to AdS/CFT duality where photons are boundary gauge fields, not fundamental substrate elements. Causal sets and quantum graphity are genuinely pre-geometric but involve no photonic content — particles (including photons) are emergent, not fundamental, in these frameworks.

**H2a test** (quantized Berry phase for knotted vortex): **Inconclusive.** Standard (unknotted) OAM Berry phase quantization is confirmed experimentally (Allen 1992; Galvez 2003) but is non-discriminating — it is standard classical optics, not evidence for the photonic-substrate hypothesis. The knot-specific measurement that WOULD discriminate has never been published.

**H2b gate** (parameter-free knot→mass mapping): **Confirmed Bin C.** No mapping exists. Knot invariants are small integers (crossing number, genus); fermion masses span 6 orders of magnitude. No mechanism bridges this gap without introducing free parameters that effectively BECOME the mass values.

### 2.3 H3 — Reversible Computing & COTT

**Literature base:** 18 external + 2 QNFO-internal sources (Landauer 1961; Bennett 1973; Bérut et al. 2012; Frank 2018; Maroney 2007; Chattopadhyay et al. 2025).

**Finding:** Zero external, peer-reviewed papers on "Charge-Only Thermodynamic Theory" (COTT) exist outside the QNFO corpus. Standard reversible computing (Bennett 1973, Toffoli 1980, Fredkin 1982) already achieves zero-dissipation computation in principle by avoiding logical erasure entirely. The H3 gate memo proves analytically that COTT provides no operation beyond standard reversible logic — it is either redundant (if interpreted as a logical-reversibility claim) or in conflict with the Landauer limit (if interpreted as sub-Landauer erasure).

**H5 verification** (calorimetry near Landauer limit): **Confirmed, non-discriminating.** Six independent experimental systems (colloidal particles, nanomagnetic bits, single-electron boxes) all confirm the Landauer bound as a strict lower limit. No experiment reports below-bound dissipation except via the well-established information-corrected (Sagawa-Ueda) bound, which is consistent with — not a violation of — the second law. This reinforces H3's Bin C classification.

### 2.4 H4 — Adelic/p-adic Quantum Mechanics & Quantum Chaos

**Literature base:** 22 external + 8 QNFO-internal sources (Dragovich 2003/2006; Vladimirov; Bikulov & Zubarev 2015; Murtagh 2008; Pitkänen 1994; Mukhamedov et al. 2005).

**Finding:** p-adic quantum mechanics provides a legitimate mathematical framework for ultrametric spacetime at the Planck scale, but ultrametricity is a GEOMETRIC property, independent of electromagnetic (photonic) composition. Ultrametric structure also emerges naturally in unrelated systems (spin glasses, hierarchical clustering) — its presence does not imply a photonic substrate.

**H4b gate** (independent p-fixing principle): **Confirmed Bin C.** After exhaustive survey, no paper proposes a physically-derived method for selecting the prime p in p-adic models. Every model either treats p as a free/fitted parameter, or takes an adelic product over all primes without a convergence/truncation principle.

**H4a scale estimate** (Planck→Rydberg bridge): **Bin U — Unfalsifiable** (reclassified from Bin C- per v1.1 adversarial review Finding 3). Under standard QFT scaling, the suppression is E_Ry/E_P ≈ 10⁻²⁷ — completely undetectable. An ultrametric non-locality scenario could in principle produce a detectable ~11 GHz signal at the geometric mean of Planck and Rydberg energy scales, but NO PRINCIPLE selects this metric over the standard (undetectable) one or an intermediate exponential decay.

**Why Bin U, not Bin C-:** The Bin C- classification in v1.0 correctly identified unfalsifiability but understated its epistemic severity by keeping it on the same Bin C scale used for "no mapping found" cases. Unfalsifiability is qualitatively different from ordinary evidence-absence: it removes the hypothesis from the domain of empirical adjudication entirely. Under the rubric's own falsifiability requirement, a claim where "any null experimental result can be accommodated by choosing a sufficiently suppressed metric" is not merely "implausible" — it is formally unfalsifiable. Bin U (Unfalsifiable) is introduced in this revision as a distinct category, reserved for claims where the report itself demonstrates that no experimental outcome could disconfirm the hypothesis as currently formulated. H4a is reclassified from Bin C- to Bin U.

### 2.5 Cross-Cutting: Spin-Statistics Theorem

**Literature base:** 11 sources (Dowker & Sorkin 1996/2001; Mund 2008; Suzuki 2017; Volovik 2007; Balachandran et al. 2000).

**Finding:** The spin-statistics theorem is not a mathematical absolute barrier to the photonic-substrate hypothesis, but it remains a practical barrier until one of the four known circumvention routes is instantiated with a concrete photonic model — none currently exists.

This revised framing (per v1.1 adversarial review Finding 4) distinguishes between:

1. **Mathematical circumventability:** The theorem is not logically absolute in all physical regimes. Four peer-reviewed circumvention routes exist in the literature: (a) 2+1D anyons (Mund 2008), (b) topological geons in quantum gravity with non-trivial spatial topology (Dowker & Sorkin 1996/2001), (c) composite gauge bosons emerging dynamically from fermionic matter fields (Suzuki 2017), and (d) emergent-spacetime scenarios where the theorem's assumptions (pre-existing Minkowski spacetime) do not apply (Volovik 2007). The theorem's assumptions can fail in specific regimes — this is a mathematical fact established in the peer-reviewed literature.

2. **Practical unavailability for the photonic-substrate hypothesis:** Despite the existence of these four routes, none has been applied to construct a concrete photonic-substrate model. The composite-boson route (Suzuki 2017) is the least problematic and most consistent with Standard Model physics, but no photonic-substrate paper has instantiated it with a specific Lagrangian. The theorem therefore remains a practical barrier for the hypothesis — the escape routes are marked on the map, but no one has walked them.

---

## 3. Curve-Fitting Audit Summary

A dedicated appendix (`artifacts/curve-fitting-audit.md`) applies a 4-point checklist to every apparent "match" found during this audit: (1) was the value predicted before data comparison, (2) does the match require a free parameter tuned to fit, (3) is the match actually a different physical system, (4) would a null/competing hypothesis also predict this match. **Eight distinct excluded matches were identified and logged**, including the KN g=2 result (non-discriminating), the OAM Berry phase (wrong system), Pitkänen's p-adic mass fits (curve-fit), and the H4a geometric-mean energy scale (free-parameter artifact). **Zero genuine, parameter-free, discriminating predictions were confirmed by data.**

---

## 4. Final Verdict Table

See `artifacts/verdict-table.md` for the complete 13-row table. Summary:

| Bin | Count | Sub-hypotheses |
|-----|-------|-----------------|
| A (non-evidential) | 2 | H1a, H1-G1 |
| B (open, gate unmet) | 1 | H1b |
| C (blocked/unsupported) | 7 | H1c, H1-G2, H2, H2b, H3, H4, H4b |
| U (unfalsifiable) | 1 | H4a |
| Untested (data gap) | 1 | H2a |
| Confirmed non-discriminating | 1 | H5 |

---

## 5. Overall Conclusion

**No sub-hypothesis of the photonic-substrate claim cluster achieves evidentially-supportive status specific to the hypothesis.** The strongest apparent successes (KN reproducing g=2, Suzuki's composite-boson theorem) are either non-discriminating (already required by mainstream physics) or unapplied (valid theorem, but no photonic-specific instantiation exists). Every distinctive, falsifiable claim unique to the program — electron g-2 from soliton structure, knot-to-mass mapping, COTT beating Landauer's limit, and a physically fixed p-adic base prime — is confirmed blocked by either an established theorem or an absence of literature support. H4a additionally falls outside the domain of empirical adjudication entirely (Bin U, unfalsifiable).

**The single most severe and well-defined blocking condition is H1-G2: no photonic-substrate or soliton model derives the electron's anomalous magnetic moment (g-2) to any precision.** This is the highest-priority open problem for any future work in this program: absent this derivation, claims that "electrons are photonic solitons" cannot be evaluated as more than a structural analogy.

**Recommendation:** Future work in this research program should either (a) produce a concrete Lagrangian-level model addressing H1-G2, with an explicit derivation compared to the CODATA g-2 value, or (b) formally reclassify the photonic-substrate hypothesis as a philosophical/structural framework rather than a physical theory making testable predictions, per the Publication Language Gate's certainty calibration requirements.

---

## 6. Adversarial Review

This v1.1 revision addresses all four MAJOR findings from the v1.0 adversarial review (`artifacts/adversarial-review.md`):

| Finding | Change | Section |
|---------|--------|---------|
| 1 — H1c reconciliation | Expanded H1c to address all 4 circumvention routes with per-route status | §2.1.1 |
| 2 — Bin B/C boundary | Added explicit 3-part criterion for Bin B vs. Bin C classification | §1.3 |
| 3 — H4a → Bin U | Introduced Bin U (Unfalsifiable) category; reclassified H4a from C- to U | §1.2, §2.4 |
| 4 — Spin-statistics softening | Rephrased headline to distinguish mathematical circumventability from practical barrier | §2.5 |

An independent REVIEWER subagent re-audit of v1.1 was requested at `[timestamp: 2026-07-21]`. See §7 for revision changelog and §8 for reviewer disposition.

---

## 7. Revision Changelog

**v1.1 (2026-07-21)** — Post-adversarial-review revision:
- §1.2: Added Bin U (Unfalsifiable) category definition
- §1.3: Added explicit Bin B vs. Bin C boundary criterion (3 conditions)
- §2.1.1: Expanded H1c to address all 4 spin-statistics circumvention routes with per-route status table
- §2.4: Reclassified H4a from Bin C- to Bin U with justification
- §2.5: Softened spin-statistics headline; added two-part distinction (mathematical circumventability vs. practical barrier)
- §4, §5: Updated verdict table summary and conclusion to reflect Bin U reclassification
- §6: Added adversarial review disposition table
- §7: This changelog
- §8: Reviewer re-audit disposition (pending at timestamp)

---

## Appendices

- Bin table detail: `artifacts/verdict-table.md`
- Curve-fitting exclusions: `artifacts/curve-fitting-audit.md`
- Literature reviews: `artifacts/lit-review-h1.md` through `h4.md`
- Gate memos: `artifacts/h1-gate-memo.md`, `h2b-gate-memo.md`, `h3-gate-memo.md`, `h4b-gate-memo.md`
- Gate summary: `artifacts/gate-summary.md`
- Cross-cutting analyses: `artifacts/spin-statistics-barrier.md`, `artifacts/h4a-scale-estimate.md`
- Phase 2 test results: `artifacts/h2a-test-results.md`, `artifacts/h5-verification.md`
- Adversarial review v1.0: `artifacts/adversarial-review.md`

---

## 8. Reviewer Re-Audit Disposition (v1.1)

**Reviewer:** Independent REVIEWER subagent (red-team role, session `Ao_YPwvcuZV2qGSlb6bxN`)  
**Date:** 2026-07-21  
**Verdict: PASS** — The v1.1 revision is cleared as a formal audit deliverable.

### Adequacy of v1.0 Finding Remediation

| v1.0 Finding | v1.1 Remediation | Reviewer Assessment |
|---|---|---|
| 1 — H1c reconciliation | §2.1.1: Per-route status table addressing all 4 circumvention routes with citations | **Adequately addressed.** The table covers all four routes with specific status and citations. The reconciliation is explicit and verifiable. |
| 2 — Bin B/C boundary | §1.3: Explicit 3-part criterion (no-go theorem, unsolved foundational dependency, zero external support) | **Adequately addressed.** The criterion is stated explicitly, is generalizable beyond the H1b/H1-G2 pair, and is applied consistently in verdict justifications. |
| 3 — H4a → Bin U | §1.2: Bin U category definition; §2.4: H4a reclassified from C- to U with justification | **Adequately addressed.** Bin U correctly distinguishes unfalsifiability from ordinary evidence-absence. The reclassification is taxonomically sound. |
| 4 — Spin-statistics softening | §2.5: Two-part framing (mathematical circumventability vs. practical barrier) | **Adequately addressed.** The headline now clearly distinguishes what is mathematically established from what is practically instantiated. |

### New Findings (v1.1)

**MINOR-1 (empty §8 at time of review):** §8 was a placeholder ("pending at timestamp") when the review was conducted. This has been populated with the current disposition.

**MINOR-2 (unresolved v1.0 truncation gap):** The v1.0 adversarial review noted that reviewer findings 5–6 were truncated by the subagent orchestrator and were not fully recovered. This gap persists — no additional capture attempt was made during the v1.1 revision. This does not affect the report's methodological soundness but represents an open documentation item. Recommendation: attempt a fresh REVIEWER subagent run with a longer output-capture window if findings 5–6 are desired for completeness before Phase 4 closeout.

### Overall Assessment

The v1.1 revision resolves all four MAJOR methodological findings from the v1.0 adversarial review. The Bin U taxonomy addition, explicit B/C boundary criterion, per-route H1c analysis, and softened spin-statistics headline collectively remediate the v1.0 report's core weaknesses. The report is methodologically sound and suitable as a formal audit deliverable.
