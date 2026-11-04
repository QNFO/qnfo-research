# Phase 3.2 — Curve-Fitting Audit Appendix

**Project:** qnfo-photon-audit  
**Date:** 2026-07-21  
**Status:** Phase 3 — Synthesis and Audit Report  
**Purpose:** List every excluded "test" or "match" encountered during this audit with the specific reason for exclusion, to guard against post-hoc curve-fitting being mistaken for prediction.

---

## 1. Purpose of This Appendix

Per the Phase 0 governing rules (PROJECT-PLAN.md §1.3), this audit distinguishes between:
- **Prediction:** A specific numerical value derived BEFORE comparison to data, with no free parameters tuned to match the result
- **Post-hoc fit:** A parameter or model chosen AFTER seeing the data, specifically to reproduce it

Every case in this audit where a "match" was found between a photonic-substrate claim and known physics is logged here with an explicit determination of which category it falls into.

---

## 2. Excluded/Discounted Matches

| # | Claim | Apparent match | Why excluded as evidence |
|---|-------|-----------------|---------------------------|
| 1 | H1-G1 (KN → g=2) | Kerr-Newman classical geometry reproduces g=2, matching Dirac | **Non-discriminating, not curve-fit.** g=2 is REQUIRED by relativistic quantum mechanics for any spin-½ particle (Dirac 1928) — any model that fails to reproduce g=2 for a spin-½ particle is already wrong. KN reproducing g=2 provides zero additional evidence FOR the photonic-substrate hypothesis, because ANY viable competing model must also reproduce it. |
| 2 | H2a (Berry phase) | OAM beams show γ=2πℓ, "consistent with" knotted-photon prediction | **Non-discriminating, wrong system.** The confirmed data (Allen 1992, Galvez 2003) is for SIMPLE (unknotted) OAM beams — standard, well-understood classical optics. No data exists for the actually-relevant KNOTTED case. Citing the OAM match as support for the knotted-photon hypothesis conflates two different physical systems. |
| 3 | Pitkänen (1994) p-adic mass calculations | p-adic square root formula reproduces certain mass ratios | **Curve-fit.** Pitkänen explicitly selects p to match observed mass ratios post-hoc — this is a textbook curve-fitting exercise, not a prediction. The H4b gate memo confirms no independent p-fixing principle exists; Pitkänen's p values were chosen, not derived. |
| 4 | Dragovich (2006) cosmological p-adic selection | Suggests p=2,3,5,... "naturally" from cosmological evolution | **Speculative narrative, not derivation.** No mathematical derivation connects cosmological parameters to a specific prime. This is a plausibility argument, not a testable prediction — logged as `[Speculative]` in the H4 lit review, excluded from the verdict table's evidentiary weight. |
| 5 | Any H4a "geometric mean" energy scale (11.2 GHz) | Numerically falls in an experimentally accessible microwave band | **Free-parameter artifact, not prediction.** The 11.2 GHz value depends entirely on the CHOICE of ultrametric tree metric f(k) = logarithmic. No principle selects this metric over an exponential one (which gives an undetectable ~10⁻²⁷ suppression) or the standard QFT metric (also ~10⁻²⁷). The "prediction" is an artifact of an arbitrary metric choice — logged explicitly as unfalsifiable in `h4a-scale-estimate.md` §7. |
| 6 | Composite-boson spin-statistics route (Suzuki 2017) | Provides formal path for bosonic photons to emerge from fermionic substrate | **Valid theorem, but not yet applied.** Suzuki's theorem IS a rigorous, peer-reviewed, non-curve-fit result. However, no photonic-substrate paper has actually INSTANTIATED this mechanism with a specific Lagrangian for photons-as-composites. The theorem's existence is real; its APPLICATION to the photonic-substrate hypothesis is speculative and unconfirmed — logged as `[Open]`, not `[Est]`, in the verdict table. |
| 7 | Burinskii KN electron "regularizing" point-particle singularity | KN ring singularity claimed to resolve classical electron self-energy divergence | **Partially non-sequitur.** The KN solution does regularize CLASSICAL point-charge divergences via its extended ring structure — this is a real feature of the classical solution. However, this says nothing about QUANTUM divergences (the actual physically relevant self-energy problem in QED, which is renormalized, not merely "regularized" by extended classical structure). Conflating classical and quantum divergence problems is a category error found in some Burinskii-adjacent secondary literature (not in Burinskii's own peer-reviewed papers, which are more careful). |
| 8 | Spin glass ultrametricity as "evidence" for p-adic photon substrate | Both are ultrametric structures | **Structural analogy only, not physical evidence.** Spin glass ultrametricity (Parisi solution) emerges from THERMODYNAMIC replica symmetry breaking in a specific statistical mechanics model — it has no photonic content whatsoever. Citing spin-glass ultrametricity as support for a p-adic PHOTONIC substrate conflates "both are ultrametric" (true, trivial) with "one explains the other" (false, non-sequitur). Logged explicitly in `lit-review-h4.md` §4b. |

---

## 3. Methodology Note: How Exclusions Were Identified

For each claim in the verdict table, the following checklist was applied:

1. **Was the "matching" value/prediction stated BEFORE the comparison data was consulted?** If no → curve-fit or post-hoc.
2. **Does the match require choosing a free parameter specifically to achieve the match?** If yes → curve-fit, regardless of whether the underlying framework is legitimate.
3. **Is the "match" actually a DIFFERENT physical system than the one the hypothesis claims to explain?** If yes (e.g., OAM vs. knotted vortices) → non-discriminating, logged separately from genuine confirmation.
4. **Would a competing/null hypothesis ALSO predict this match?** If yes (e.g., g=2 from relativity alone) → non-evidential, logged separately.

This four-point checklist was applied uniformly across all 13 sub-hypotheses in the verdict table (`artifacts/verdict-table.md`) and its underlying gate memos.

---

## 4. Verdict

**Zero genuine, parameter-free, discriminating predictions were found to be confirmed by data during this audit.** Every apparent "match" between a photonic-substrate claim and empirical/theoretical results falls into one of: (a) non-discriminating (also predicted by mainstream physics), (b) wrong physical system, (c) curve-fit with post-hoc parameter choice, or (d) structural analogy without physical connection.

This finding is consistent with — and strengthens — the overall verdict in `artifacts/verdict-table.md`: the photonic-substrate claim cluster has not yet produced a single falsifiable, parameter-free prediction that has been experimentally confirmed.
