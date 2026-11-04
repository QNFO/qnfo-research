---
modified: 2026-07-18T14:00:42Z
---
# A Falsifiability-First Research Program on Photonic Substrate Hypotheses for Emergent Spacetime (v2)

**Revision note:** v2 responds to a specific failure found in the prior "experimental design" pass: several proposed tests (knot-invariant mass ratios, an adelic product formula for α) compared a claim against known data using a formula with enough free parameters to be tuned to fit _after seeing the answer_. That is not a test — a procedure that can always be made to match the target isn't falsifiable, regardless of how rigorous the surrounding language sounds. v2 adds a hard structural rule and a new gate phase to prevent this from recurring anywhere else in the program.

---

## The pre-registration rule (governs every phase below)

**No comparison between a model's output and existing data or literature counts as a test of that model unless:**

1. The exact functional form or algorithm producing the prediction is fixed and written down _before_ the comparison is made, with no free parameters left to be chosen after seeing the target value; and
2. The number of free parameters in the model is smaller than the number of independent facts it is being asked to explain (otherwise agreement is guaranteed by construction, not evidence); and
3. The prediction, once locked, is logged (timestamped, in the project record) before comparison, so post-hoc adjustment is externally checkable.

Any sub-program that cannot clear this gate is reclassified from "test" to "unconstrained model-building exercise" in the final report, and is not permitted to claim falsifiability it doesn't have.

---

## Abstract

This program audits a cluster of claims — that the electron has helical internal structure at the Compton scale, that electrons are topologically knotted photons, that a "non-destructive" invertible-zero arithmetic (COTT) confers a thermodynamic or complexity advantage over standard reversible computing, and that ultrametric/adelic number-theoretic structure appears in low-energy electron physics — by sorting each into one of three bins: (A) genuinely testable now, because a parameter-free or parameter-sparse prediction can be derived and locked prior to comparison; (B) requires prior theoretical work before any test is meaningful, because no such prediction currently exists; or (C) not falsifiable as currently posed, because the comparison procedure has enough tunable freedom to match virtually any target. Prior passes over this material found real physics underlying several claims (Rañada–Trueba electromagnetic knots, Kerr–Newman spinning solitons, Ryu–Takayanagi holographic entanglement, Bennett-style reversible/adiabatic computing) but also found that "falsifiable-sounding" experimental designs had been proposed for sub-claims still in bin B or C. This revision restructures the WBS so that bin-C proposals (e.g., an adelic product formula "matching" α, or a knot-invariant formula "matching" the muon/tau mass ratios) are explicitly blocked from being run as tests until they clear the pre-registration gate — and, in the muon/tau and α cases, flags that no known construction currently _can_ clear it, which the report will state plainly rather than paper over with an experiment that can't fail.

---

## Research Thesis

**Thesis statement (unchanged from v1, sharpened):** The overall claim conflates representational adequacy (can this math describe electron-like behavior in some regime?) with ontological priority (is this what an electron actually _is_, more fundamental than space?) and with empirical support (has this been shown to match reality, as opposed to being tunable to match it?). The three are independently gradable, and this program's job is to grade them separately per sub-claim rather than let a passing grade on one smuggle in a passing grade on the others.

**Sub-hypotheses, now tagged by bin as determined in the prior critique (subject to revision once each track is actually run):**

|#|Claim|Bin|Rationale|
|---|---|---|---|
|H1|Helical electron produces calculable g-2 correction|**B**|No field equation yet generates a number; methodology (compare to precision g-2) is sound once one exists|
|H2a|Photonic vortex solitons can exhibit fermion-like behavior in engineered media|**A**|Polariton/synthetic-gauge-field photonics is a real, running experimental field; a specific prediction (e.g. a Berry-phase sign or quantized winding number) can be locked pre-measurement|
|H2b|Knot invariants (Alexander/Jones polynomials of a specified knot family) predict m_μ/m_e ≈ 207, m_τ/m_e ≈ 3477|**C**, pending H2b-gate|Only escapes bin C if a _specific_ knot-to-mass mapping is fixed with fewer free parameters than the two ratios it must hit|
|H3|COTT/invertible-zero arithmetic beats standard reversible computing on dissipation or complexity|**C→B**|The dissipation claim, as stated, has no mechanism distinguishing it from ordinary Bennett-style reversible logic; complexity-class claim is very likely a category error (see below) and should be resolved analytically before any hardware is built|
|H4a|Ultrametric/adelic spectral signatures appear in Rydberg-state spacing statistics|**A**|Spacing-statistic analysis is a standard, model-independent technique; a specific alternative-to-Poisson/Wigner-Dyson signature can be predicted and locked before looking at spectroscopic data|
|H4b|A specific adelic product formula α = ∏ p^(−v_p) reproduces α to known precision|**C**|As posed, valuations v_p are free per prime; with enough primes available, agreement to 12 digits is achievable for _any_ target constant and is therefore not evidence of anything. Escapes bin C only if v_p are fixed by an independent principle stated _before_ checking against α — no such principle currently exists in the literature surveyed|
|H5|Reversible/adiabatic logic chains approach k_BT ln2 dissipation|**A**|Established methodology (Bennett), independent of COTT; genuinely runnable now, and largely already run in the literature — this track becomes a literature-verification task, not a new experiment|

---

## Work Breakdown Structure (WBS) — v2

### Phase 0 — Scoping, Claim Decomposition, Bin Assignment (Week 1)

- 0.1 Re-derive the bin table above independently (do not simply accept the prior pass's assignments — re-argue each one from source literature).
- 0.2 Write the pre-registration rule into a project charter that every subsequent phase must cite compliance with.
- _Deliverable:_ Charter + bin table with justification per row.

### Phase 1 — Literature Synthesis (Weeks 2–5)

- Unchanged in method from v1: systematic review per sub-literature (EM-knot solitons, spinning solitons, holographic entanglement/RT, adelic QM, reversible computing).
- **New:** each reviewed paper is additionally tagged with which bin (A/B/C) its central result belongs to, to build an evidence base for Phase 0's assignments rather than trusting them on priors alone.
- _Deliverable:_ Annotated bibliography (~40+ sources) with bin tags and one-paragraph justification each.

### Phase 1.5 — Pre-Registration Gate (Week 5–6) — **new phase**

For every claim currently in bin B or C, attempt to construct a parameter-sparse, lockable prediction:

- 1.5.1 **H1:** Attempt to derive a g-2 correction from an explicit helical-curve Lagrangian (e.g., using the Kerr–Newman soliton machinery from Phase 1). If a correction can be derived with no adjustable knobs beyond the already-fixed α and Compton wavelength, H1 moves to bin A and a numeric prediction is logged before any comparison to CODATA/experimental g-2. If no such derivation is achievable within this program's scope, H1 is reported as "requires further theoretical development" — not tested.
- 1.5.2 **H2b:** Attempt to fix a specific knot-family-to-mass mapping using only topological invariants and _no free continuous parameters_ (e.g., energy strictly as a function of a knot's crossing number or Alexander polynomial evaluated at a fixed point, with no fitted coefficients). If the resulting two-parameter-free predictions for m_μ/m_e and m_τ/m_e are lockable before comparison, H2b moves to bin A. Given the current literature (Phase 1), the expected outcome is that no such parameter-free mapping exists yet, in which case H2b is reported as bin C and explicitly excluded from the "tests" section of the final report — reported instead as an open modeling problem.
- 1.5.3 **H3:** Resolve analytically (no hardware needed) whether COTT's invertible-zero algebra changes anything at the level of physical information theory versus standard reversible logic. This is a math/logic exercise: show either (a) an operation COTT permits that standard reversible arithmetic (which is already total on its actual domain, since it never maps to an undefined 1/0) does not, or (b) that no such operation exists, meaning H3's "advantage" claim is vacuous and the only real content left is H5 (ordinary reversible computing), already well established.
- 1.5.4 **H4b:** Attempt to find any independent principle (not fitted to α) that would fix the valuations v_p. Survey the Volovich/Vladimirov adelic-physics literature (Phase 1) for whether any existing adelic formula for a physical constant was derived independently of the target value. If none exists for α specifically, H4b is reported as bin C, full stop — no experiment is proposed for it, and the final report states plainly that this sub-claim is not currently falsifiable as posed.
- _Deliverable:_ Gate memo per B/C claim: promoted to bin A with locked prediction, or formally logged as "not yet testable" / "not falsifiable as posed."

### Phase 2 — Runnable Tests and Calculations for Bin-A Claims Only (Weeks 6–10)

- 2.1 **H2a:** Design (on paper; flag for external experimental collaboration if pursued further) a specific polariton/synthetic-photonic-lattice signature — e.g., a predicted quantized Berry phase or spin-locking ratio — locked before any comparison to existing photonic-lattice experimental data pulled from the literature.
- 2.2 **H4a:** Run a spacing-statistics analysis on existing high-precision Rydberg spectroscopic datasets (literature data, not new experiments, within program scope) against the locked prediction from 1.5-equivalent reasoning; report Poisson/Wigner-Dyson/other classification.
- 2.3 **H5:** Literature-verification task — compile existing calorimetry results on adiabatic/reversible logic chains and report how close to k_BT ln2 has actually been demonstrated, since this doesn't require new experiments to answer.
- 2.4 Any claim promoted out of bin B by Phase 1.5 (e.g., H1 if a derivation succeeded) gets its locked prediction compared to existing precision measurements (e.g., published g-2 values) here, for the first time, only now.
- _Deliverable:_ Test results per bin-A claim, each explicitly showing the prediction was locked before the comparison (timestamped log).

### Phase 3 — Synthesis and Audit Report (Weeks 10–12)

- 3.1 Compile final verdict table: for every original H1–H5 claim, report bin, whether it was promoted, and outcome (supported / not supported / still open) with citations.
- 3.2 Explicit "curve-fitting audit" appendix: list every place in the _original_ informal document (and the prior "experimental design" pass) where a comparison was proposed without parameter-sparsity, and show why it doesn't count as a test, as a teaching example.
- 3.3 Independent adversarial review pass, specifically re-checking that no Phase 2 result silently violates the pre-registration rule (i.e., re-verify no parameters were tuned after seeing data).
- _Deliverable:_ Draft report v1.

### Phase 4 — External Sanity Check and Finalization (Weeks 12–14)

- 4.1 Circulate to subject-matter readers per sub-literature where accessible; otherwise structured self-critique against textbook results (spin-statistics theorem, standard RT-formula scope, Bennett's theorem).
- 4.2 Revise; finalize verdict table and curve-fitting audit appendix.
- 4.3 Publish as a technical report with all calculation notebooks and the pre-registration log attached, so every comparison in the report is independently checkable as having been locked-then-compared rather than fitted-then-reported.
- _Deliverable:_ Final report.

---

## What changed from v1, concretely

- Added the pre-registration rule as a governing constraint, not just a methodological aside.
- Added Phase 1.5 as a mandatory gate: claims don't get an "experiment" until they've earned a lockable prediction.
- Reclassified H2b (knot-invariant mass ratios) and H4b (adelic formula for α) as bin C by default, with the burden of proof on finding a parameter-sparse construction — reversing the prior draft's framing, which proposed running these as if they were already well-posed tests.
- Added an explicit curve-fitting audit appendix requirement, so the final report documents _why_ certain proposed tests were excluded, rather than silently dropping them.
- Split H3 into an analytical resolution step (1.5.3) before any hardware-based test is authorized, since building a chip to test a claim that may be a category error wastes the program's limited experimental budget.

## Expected Outcome (updated)

Based on Phase 1 literature to date: H2a, H4a, and H5 are likely to yield genuine, checkable results within program scope (most likely: no fermionic behavior in photonic solitons under presently achievable conditions; no exotic spacing-statistic signature in Rydberg spectra beyond known quantum-chaos physics; reversible-logic dissipation already well-documented near the Landauer bound in existing literature). H1 and H3 are likely to resolve at the gate stage — H1 as "still requires theory before testing," H3 as "no advantage over standard reversible computing once the algebra is examined directly." H2b and H4b are expected not to clear the pre-registration gate at all, and the report will say so directly rather than dressing them up as completed or pending experiments.