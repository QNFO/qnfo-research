# Bayesian Evidential Weight (KIF-60) — Post-Positional Numeracy (QNFO.RES.024)

Date: 2026-08-26 · Owner: artifacts/consilience-gate.md §4 (expanded) · Gate: KIF-60 sub-gate of KIF-29

## Claim audited

The correspondence: "the adelic product formula is a machine-checkable invariant of multi-place exact arithmetic" — the central structural claim of the paper.

## Three Concrete Tests

| Test | Status | Evidence |
|:-----|:-------|:---------|
| **Pre-registration** | PASS | Hypothesis cards H-PPN-1/2/3 committed in PROJECT-PLAN §3 before any implementation (git commit f3f2806, 2026-08-26 08:52Z, later corrected by the claim amendment at 100ee2c — the amendment itself is timestamped in git). |
| **Falsifiability gradient** | PASS | H-PPN-3: one verified collision of two distinct window rationals disconfirms injectivity (tested: 0 collisions in 10^5 seeded trials + exhaustive small moduli). H-PPN-1: a single S-smooth trial with product ≠ 1 (beyond float error) disconfirms the invariant (tested: 0 in 10^4). H-PPN-4: any published system using the product formula as an invariant disconfirms novelty (adjudicated: none found; closest work AGL 2026 uses multiplicity decoding, not the invariant). |
| **Surprise accounting** | [CONSTRUCTED — engineering weight] | The product formula equaling 1 is a theorem (P = 1 under a correct implementation), not a surprising empirical match. The correspondence therefore carries engineering and pedagogical weight — a checksum with failure-localization — and the paper states this; it claims no novel empirical evidence. Δlog-odds ≈ 0 as evidence for a new physical claim; the value is the verification machinery itself. |
| **Confirmation-seeking test** | PASS | The injectivity test discriminates the two-sided window from the one-sided alternative (Remark 1's collision pair 1/7 ≡ 13 mod 30 fails the one-sided window and is excluded by the two-sided one) — the test would fail the claim if the bound were wrong, which is exactly how the Phase-0 error was caught. |

## Classification

The paper's three mathematical claims (injectivity lemma, invariant theorem, failure localization) are theorems with proofs in the text and computational verification in Section 5. The cross-domain correspondence is classified as a constructed engineering correspondence, not as evidential support for any empirical hypothesis — consistent with the paper's declarations.
