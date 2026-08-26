# PROJECT-PLAN.md — Completeness Senses and the Levi-Civita Field

**WBS:** QNFO.RES.024 (Post-Positional Numeracy)
**Slug:** post-positional-numeracy
**Status:** Phase 8 (published) — this plan covers the P5→P8 publication cycle
**Date:** 2026-08-26

## Core claim (locked at P6)

Ostrowski's theorem classifies rank-one valuations of the rationals, yielding the real numbers and the p-adic fields, but it does not close the question of what a complete number system can be. The word *complete* names three distinct properties — Dedekind, Cauchy, and spherical completeness. The reals are the unique Dedekind-complete ordered field (unconditionally, since Dedekind completeness implies the Archimedean property), but they are not the unique Cauchy-complete ordered field: the Levi-Civita field is Cauchy-complete, ordered, real-closed, and non-Archimedean, a concrete counterexample with infinitesimal resolution the reals cannot admit. The standard decimal identity 0.999... = 1 survives by transfer in every ordered field containing the reals; divergence appears only for nonstandard-indexed decimals. Higher-rank valuations occur only in function fields of transcendence degree at least two.

## Hypothesis cards

- **H-COMPLETE:** "complete" is not univocal; three senses (Dedekind/Cauchy/spherical) give three different uniqueness verdicts for the reals. Falsifier: exhibit an ordered field that is Cauchy-complete but not Archimedean → the Levi-Civita field (established).
- **H-LEVI:** the Levi-Civita field is ordered, real-closed, non-Archimedean, and Cauchy-complete in its natural valuation topology. Falsifier: failure of any of the four properties (established, verified by construction + red team).
- **H-DECIMAL:** 0.999... = 1 survives in every ordered field containing the reals; the != 1 case requires a nonstandard-indexed decimal (Lightstone 1972). Falsifier: a standard decimal expansion unequal to 1 in an ordered extension of the reals (not found; the transfer principle rules it out).
- **H-RANK:** higher-rank valuations exist only in transcendence-degree >= 2 function fields. Falsifier: a higher-rank valuation on Q(x) or C(x) trivial on the base (none — C algebraically closed; Q(x) only via composition construction).

## Premise depth

Derived claims: the completeness trichotomy (from the definitions), the Levi-Civita counterexample (from the field construction), the decimal transfer argument (from the transfer principle), the rank bound (from Abhyankar's inequality). Named imported inputs (premises end here): Ostrowski's theorem, the transfer principle for ordered field extensions, Abhyankar's inequality, the Levi-Civita field construction. No new axiom is introduced.

## Why a reader should care

The completeness question determines which number system a physical theory can be written over. The Levi-Civita field is a concrete ordered alternative to the reals that keeps field structure and metric completeness while adding infinitesimals — directly relevant to exact-arithmetic computation (Hensel codes, p-adic software) and to any theory requiring a distinguished scale. The trichotomy also sharpens existing QNFO continuum work (the Continuum Trilogy's depth/breadth/valuation axes).

## Red-team and novelty history

- 2026-08-26 red team (3 reviewers): Accuracy 7/7 TRUE + 3 SOFT (standard decimal transfer; Q_p sum-of-squares generalization; completeness-sense precision); Completeness HARD (conflated three completeness senses; hyperreals are aleph_1-saturated not complete; surreals are a proper class); Dependency 1 HARD (higher-rank valuations need tr.deg >= 2, not Q(x)/C(x); Abhyankar; Amini–Iriarte arXiv:2208.06237). All corrections folded in.
- Novelty check against corpus: the completeness *decomposition* theme is already published in the Continuum Trilogy; the genuinely novel residue is the Levi-Civita field counterexample, the nonstandard-decimal nuance, and the higher-rank scope correction. This record publishes the corrected refinement and cites the Trilogy as prior art.

## Verification

Script: artifacts/verification/verify_completeness.py. Output: artifacts/verification/verify_completeness_out.txt. Deterministic, Python stdlib only, seed-free. All checks exit 0.
