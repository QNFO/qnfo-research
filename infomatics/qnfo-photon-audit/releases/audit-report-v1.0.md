# Photonic Substrate Hypotheses for Emergent Spacetime: A Technical Audit

**Project:** qnfo-photon-audit  
**Version:** v1.0 — Draft  
**Date:** 2026-07-21  
**Methodology:** Falsifiability-first, pre-registration-governed, bin-classified

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
| **C-** | Implausible/formally unfalsifiable — free parameters allow the claim to accommodate any outcome |

### 1.3 Pre-Registration Gate

Per Phase 1.5, every Bin B/C claim was subjected to an analytic gate BEFORE any Phase 2 "test" was designed. This prevents the common failure mode of designing a test that can only confirm the hypothesis (confirmation bias in test design). Gates were resolved using existing literature and mathematical analysis, not new experiments (per the LLM-Executable Research Gate — this audit performs no new physical experiments).

---

## 2. Per-Hypothesis Audit

### 2.1 H1 — EM-Knot Solitons as Electron Models

**Literature base:** 17 sources (Rañada 1989/1990; Trueba & Rañada 1996; Irvine & Bouwmeester 2008; Kedia et al. 2013; Arrayás et al. 2017; Burinskii 2000/2015/2023; Chernitskii 1999; Hestenes 1990/2010).

**Sub-claims:**
- **H1a** (electron g-2 explained by Dirac equation): **Bin A**, confirmed, non-evidential.
- **H1b** (knotted photon → electron observables): **Bin B**, gate not met.
- **H1c** (EM knots → spin-½ statistics): **Bin C**, blocked by spin-statistics theorem except via unproven composite-boson route.
- **H1-G1** (KN → g=2 classical): **Bin A**, PASS but non-evidential (required by relativity).
- **H1-G2** (KN → g-2 QED corrections): **Bin C**, BLOCKED. No published derivation exists; requires unsolved KN quantization / full quantum gravity theory.

**Key finding:** The Kerr-Newman electron model (Burinskii) is the most mathematically developed attempt in this literature, reproducing the classical g=2 gyromagnetic ratio. However, it provides no path to the QED g-2 correction — the most precisely tested prediction in physics (agreement to 1 part in 10¹²). This is the single most severe blocking condition for the entire photonic-substrate program.

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

**H4a scale estimate** (Planck→Rydberg bridge): **Bin C-, implausible.** Under standard QFT scaling, the suppression is E_Ry/E_P ≈ 10⁻²⁷ — completely undetectable. An ultrametric non-locality scenario could in principle produce a detectable ~11 GHz signal at the geometric mean of Planck and Rydberg energy scales, but NO PRINCIPLE selects this metric over the standard (undetectable) one or an intermediate exponential decay. The claim is formally unfalsifiable in its current form: any null experimental result can be accommodated by choosing a sufficiently suppressed metric.

### 2.5 Cross-Cutting: Spin-Statistics Theorem

**Literature base:** 11 sources (Dowker & Sorkin 1996/2001; Mund 2008; Suzuki 2017; Volovik 2007; Balachandran et al. 2000).

**Finding:** The spin-statistics theorem is NOT an absolute barrier to the photonic-substrate hypothesis, but it is a significant constraint. Four circumvention routes exist: (1) 2+1-dimensional anyonic statistics, (2) topological geons in quantum gravity with non-trivial spatial topology (Dowker & Sorkin), (3) composite gauge bosons emerging dynamically from fermionic matter fields (Suzuki 2017 — the least problematic route), and (4) emergent-spacetime scenarios where the theorem's assumptions (pre-existing Minkowski spacetime) simply do not apply. No photonic-substrate paper has instantiated any of these routes with a concrete model.

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
| C (blocked/unsupported) | 8 | H1c, H1-G2, H2, H2b, H3, H4, H4b |
| C- (implausible) | 1 | H4a |
| Untested (data gap) | 1 | H2a |
| Confirmed non-discriminating | 1 | H5 |

---

## 5. Overall Conclusion

**No sub-hypothesis of the photonic-substrate claim cluster achieves evidentially-supportive status specific to the hypothesis.** The strongest apparent successes (KN reproducing g=2, Suzuki's composite-boson theorem) are either non-discriminating (already required by mainstream physics) or unapplied (valid theorem, but no photonic-specific instantiation exists). Every distinctive, falsifiable claim unique to the program — electron g-2 from soliton structure, knot-to-mass mapping, COTT beating Landauer's limit, and a physically fixed p-adic base prime — is confirmed blocked by either an established theorem or an absence of literature support.

**The single most severe and well-defined blocking condition is H1-G2: no photonic-substrate or soliton model derives the electron's anomalous magnetic moment (g-2) to any precision.** This is the highest-priority open problem for any future work in this program: absent this derivation, claims that "electrons are photonic solitons" cannot be evaluated as more than a structural analogy.

**Recommendation:** Future work in this research program should either (a) produce a concrete Lagrangian-level model addressing H1-G2, with an explicit derivation compared to the CODATA g-2 value, or (b) formally reclassify the photonic-substrate hypothesis as a philosophical/structural framework rather than a physical theory making testable predictions, per the Publication Language Gate's certainty calibration requirements.

---

## 6. Adversarial Review

*(Pending — see `artifacts/adversarial-review.md` for the independent red-team challenge to this report's own methodology and conclusions.)*

---

## Appendices

- Bin table detail: `artifacts/verdict-table.md`
- Curve-fitting exclusions: `artifacts/curve-fitting-audit.md`
- Literature reviews: `artifacts/lit-review-h1.md` through `h4.md`
- Gate memos: `artifacts/h1-gate-memo.md`, `h2b-gate-memo.md`, `h3-gate-memo.md`, `h4b-gate-memo.md`
- Gate summary: `artifacts/gate-summary.md`
- Cross-cutting analyses: `artifacts/spin-statistics-barrier.md`, `artifacts/h4a-scale-estimate.md`
- Phase 2 test results: `artifacts/h2a-test-results.md`, `artifacts/h5-verification.md`
