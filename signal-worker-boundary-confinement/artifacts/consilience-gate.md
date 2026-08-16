# Consilience Gate — QNFO.INM.001 (KIF-29, HARD)

**WBS:** QNFO.INM.001 — Signal-Worker Boundary Confinement
**Date:** 2026-08-16 · **Trigger:** Phase 1b (post-v0.2 due-diligence re-sweep, CMD CONTINUE)
**Prior gate evidence:** `artifacts/deep-due-diligence.md` (2026-08-14) + `artifacts/gap-analysis-2026-08-16.md` + `artifacts/external-search/*` (10 evidence files, commit 1e38ea7)
**Verdict:** PASS — gate satisfied; Phase 1 now COMPLETE for the v0.3 cycle.

---

## 1. Cross-Domain Lexicon (dynamic selection from Phase 1 evidence)

| # | Domain | Why chosen (evidence) |
|:-:|:-------|:----------------------|
| 1 | Condensed Matter / Mesoscopic Transport (INM primary) | The project's own territory: bulk-boundary correspondence, skin effect, NHSE. Evidence: corpus-sweep-f1/f2/f3.json; openalex-bulk-boundary.json (9,768 hits); openalex-anomalous-skin-effect.json (16,981); arxiv-nhse-search.json. |
| 2 | Quantum Foundations & Interpretation (RES) | The S-W ontology is an interpretation-level decomposition of wave–particle duality; the correction is a spin-statistics-adjacent taxonomy. Evidence: electron-hook-treatise (10.5281/zenodo.21970454); spin-statistics lineage (RES.009); core-claim.md. |
| 3 | Ultrametric / Number-Theoretic Physics (UMP) | The seed note's Ostrowski thread: conductance quantization and topological invariants are integer counts; the Archimedean real is one completion. Evidence: zbw-padic-observable (10.5281/zenodo.21335853); electron-hook-treatise (Archimedean-valuation assumption); note _26228215041.md. |
| 4 | Laws of Form / Distinction Calculus (SLB) | The core correction is a category-error fix — a distinction operation: "field expulsion ≠ mode confinement". Evidence: RES.011 configuration-space-topology (distinction calculus); core-claim.md. |
| 5 | Statistical Thermodynamics (cross-cutting) | The note's entropy-primary thread: temperature = ∂E/∂S; the thermal resolution scale T_gap = Δ/k_B decides when the surface/bulk distinction blurs. Evidence: thermodynamic-imperative (10.5281/zenodo.17928156), thermodynamic-scaling (10.5281/zenodo.17899087); note _26228215041.md. |

## 2. Minimum-Viable-Findings (one non-trivial structural isomorphism per domain)

1. **CM:** The three surface phenomena are three mechanisms identified by three dimensionless ratios — skin effect ↔ δ (Maxwell+Ohm, dissipative, field/current redistribution); topological boundary ↔ mode confinement with protection scale k_BT/Δ_gap; NHSE ↔ point-gap winding (integer). Each category = "which ratio crossed one": δ/λ_F (anomalous skin), ℓ/λ_F (ballistic), k_BT/Δ_gap (thermal blurring). The category distinction survives the nanoscale because it is a mechanism distinction, not a scale distinction.
2. **QF:** The corrected S-W ontology is isomorphic to the exchange-phase taxonomy: boson=signal ↔ symmetric exchange (integer spin), fermion=worker ↔ antisymmetric exchange (half-integer spin). The canonical breakdown is the Cooper pair (composite boson: two fermions, exchange phase 4π) — exactly the C4 counterexample in the falsifiability register.
3. **UMP:** Conductance quantization G = nG0, winding numbers, and topological invariants are all integer counts. Ostrowski (1916): the Archimedean real is ONE completion of Q; the corrected ontology's ratios (δ/λ_F, ℓ/λ_F, k_BT/Δ) are count/ratio statements — consistent with the UMP program's primacy of integer/rational structure. NHSE localization is determined by a winding number (integer) — the count-structure is preserved across all three categories.
4. **SLB:** The correction is a distinction-calculus re-entry: the conductor's surface carries two distinct distinctions (EM-field penetration vs. eigenstate localization). The original S-W reading collapsed them (category error = collapsed distinction); the corrected ontology re-enters the boundary distinction (Spencer-Brown re-entry; RES.011 distinction calculus).
5. **TD:** Temperature = ∂E/∂S (inverse rate of entropy change with energy) ↔ T_gap = Δ/k_B: when k_BT crosses Δ, bulk states populate and the surface/bulk distinction blurs. Thermodynamics is the coarse-graining map, not the territory (note's own resolution): all three surface categories are statements about entropy gradients — dissipation (skin), protection gap (topology), non-reciprocity (NHSE).

## 3. Silo Cost Table

| Domain | Structure Name | Earliest | Connected | Silo Cost | Key Paper |
|:-------|:---------------|:---------|:----------|:----------|:----------|
| EM theory | skin effect | 1885 (Heaviside) | 1948 (Reuter–Sondheimer, anomalous skin → quantum/kinetic theory) | **63 yr** | Reuter & Sondheimer, Proc. R. Soc. A 195, 336 (1948) |
| Topological physics | topological surface states / BBC | 1980 (von Klitzing, QHE) | 2010 (Hasan–Kane RMP synthesis: boundary modes as bulk-topology consequence) | **30 yr** | Hasan & Kane, RMP 82, 3045 (2010) — Crossref-verified |
| Non-Hermitian physics | NHSE / non-Bloch BBC | 1996 (Hatano–Nelson) | 2018 (Yao–Wang GBZ); 2025 experimental (Schneider et al.) | **22 yr** | Yao & Wang, PRL 121, 086803 (2018) — Crossref-verified; arXiv 2505.03658 |
| Number theory | Ostrowski completions | 1916 | 1994 (Vladimirov–Volovich, adelic physics) | **78 yr** | Ostrowski, Acta Math 41 (1916) — canonical Compton-BT lineage |
| Information theory | dimensionless entropy | 1948 (Shannon) | 1957 (Jaynes, max-entropy thermodynamics) | **9 yr** | Shannon, BSTJ 27 (1948) |
| Laws of Form | primitive distinction | 1969 (Spencer-Brown) | NEVER (externally) | **>55 yr** | Spencer-Brown, Laws of Form (1969) → `[SILO-FAILURE: >50 yr gap — the QNFO distinction-calculus program (RES.009/011) is the synthesis that rectifies it]` |

**Independence note (definition of independent consilience):** the converging lines are methodologically independent — classical EM (Maxwell+Ohm), 2D topological physics (QHE/TI), non-Hermitian topology (GBZ), number theory (Ostrowski), information theory (Shannon/Jaynes), Laws of Form (Spencer-Brown) — different formalisms, different communities, different eras. The convergence on "boundary phenomena are mechanism-classified by counts and ratios" is real; its evidential weight is bounded by KIF-60 (the meta-principle is a taxonomy, so the convergence is retrodictive for the taxonomy itself; the weight lives in the pre-registered observable predictions — see bayesian-evidential-weight.md).

## 4. Synthesis Consilience

**Meta-principle (invariant across all translations):** A boundary phenomenon's category is fixed by MECHANISM, not scale: field redistribution (classical electrodynamics), mode confinement (bulk topology), and non-reciprocal skin localization (point-gap topology) are distinct mechanisms; dimensionless ratios (δ/λ_F, ℓ/λ_F, k_BT/Δ, winding numbers) decide which category is operative at a given scale; the Archimedean real is one completion in which those ratios are expressed, not the only one.

**Frontier Question:** Is the corrected surface trichotomy (field redistribution / mode confinement / non-reciprocal localization) EXHAUSTIVE and DISJOINT under the non-Hermitian classification — i.e., does every boundary-localized transport phenomenon in gapped and point-gapped systems fall into exactly one of the three categories?

## 5. KIF-60 Sub-Gate (Three Concrete Tests) — summary

Full detail in `artifacts/bayesian-evidential-weight.md`. Verdicts: C1 [RETRODICTION — established physics, zero novelty weight]; C2 [RETRODICTION until pre-registered]; CORR-3 (NHSE trichotomy) pre-registered THIS COMMIT, positive weight conditional on experimental confirmation; CORR-4 [UNTESTED — defers to UMP corpus].

## 6. Symmetric Audit of Incumbents (2026-08-04 user injunction)

The incumbent frameworks were audited with the same lens, not defaulted to favor:
- **Hermitian bulk-boundary correspondence (the incumbent surface ontology):** it absorbed NHSE only by adding GBZ/point-gap machinery (Yao–Wang 2018; review 2302.03057) — an absorption that is itself a category EXPANSION, confirming the trichotomy rather than contradicting it. Grade: established in Hermitian domain; incomplete in non-Hermitian domain (no single invariant covers both).
- **Wave–particle duality (the incumbent interpretation):** the S-W reading overgeneralized it (the audited failure that created this project); duality itself remains useful in its own domain but is not a surface-transport taxonomy.
- **Classical skin effect (incumbent surface theory for metals):** correct within Maxwell+Ohm domain; anomalous-skin regime required a 63-year silo crossing (1885→1948) to be connected to quantum/kinetic theory.
- No incumbent is graded more falsifiable by default; the trichotomy's own disconfirmation conditions are pre-registered (BEW file).

## 7. Gate Output

This file satisfies the KIF-29 gate (lexicon + MVF + silo table + synthesis + KIF-60 integration). Phase 1 for the v0.3 cycle is COMPLETE; HARD BLOCK on Phase 2 lifted.
