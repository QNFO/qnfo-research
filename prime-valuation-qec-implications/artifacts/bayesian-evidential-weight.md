# KIF-60 Bayesian Evidential Weight — QNFO.RES.006 (v0.2)

**Slug:** prime-valuation-qec-implications · **DOI:** 10.5281/zenodo.21922813 · **Date:** 2026-08-13

## Scope

Two claims carry evidential weight in this paper: (a) the self-correction (naive [[n,k,d]] mapping is definitional relabeling), and (b) the 83% Kodaira–Néron classification claim under reproduction.

## Claim (a): the relabeling finding — definitional, near-certainty

- **Type:** [ANALYTIC] — the identity n = v₂(dim H) restates the definition of an n-qubit code (dim H = 2^n). The claim "adds nothing" follows from the definition; no experiment needed.
- **P(claim true):** ≈ 1 (definitional; the only failure mode is a misunderstanding of what "content" means, which §3 addresses explicitly).
- **Evidential weight:** none needed beyond the definitions; graded HIGH confidence, not a prediction.

## Claim (b): 83% classification — unverified internal, first attempt failed

- **Type:** [EMPIRICAL, internal] — per-family breakdown: Surface 46/50, CSS 39/50, Optimal 45/50, Random 36/50; Mahler v_p^max 28 (optimal) vs 4 (random).
- **Prior (Ostrowski prior):** p-adic structure is 1 of 2 completions of Q; the specific claim that a Kodaira–Néron fiber classifier achieves 83% has no external precedent (external search: zero external valuation-classifier hits).
- **Prior P(83% reproduces):** ~0.5 under the null model (no common structure), consistent with the Five Pillars KIF-60 treatment.
- **First attempt evidence (P4.2, 2026-08-13):** Mahler spectral leg C7.3' NOT reproduced at n ≤ 18 — observed optimal v_p^max = 4, random median 3 (max 6, which exceeds optimal). This shifts the posterior DOWN: **P(reproduction) < 0.5**.
- **Blocker caveat:** the Mahler target function and Cox-ring ideal I_C are undefined in the source, so the negative result is not yet decisive; it is evidence against, not proof.
- **Updated posterior:** P(83% claim holds as stated) ≈ 0.3–0.4, conditional on the under-specification being resolved in the source's favor. If the source cannot provide the missing definitions, the claim should be treated as [NOT SUPPORTED].

## Calibration

| Claim | Type | Prior | Evidence | Posterior | Disconfirmation condition |
|:------|:-----|:------|:---------|:----------|:--------------------------|
| (a) relabeling | analytic | — | definitions | ~1.0 | any new content claim |
| (b) 83% | empirical | 0.5 | first attempt failed at n ≤ 18 | 0.3–0.4 | fails to beat baseline pre-registered margin |

## Verdict

The paper's headline finding (a) is not an empirical bet; it is a definitional result. The empirical bet (b) is now, after the first failed reproduction attempt, **evidentially negative but not decisive** — pending source clarification. This is the honest evidential status and is disclosed as such in §6.
