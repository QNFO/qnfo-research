# Consilience Gate (KIF-29) — Post-Positional Numeracy (QNFO.RES.024)

Date: 2026-08-26 · Phase 1b · Evidence: docs/deep-research.md + artifacts/external-search/*

## 1. Cross-Domain Lexicon (dynamic, evidence-driven)

| Domain | Chosen because | Evidence anchor |
|---|---|---|
| Number theory (valuation theory) | Ostrowski's theorem + product formula are the paper's mathematical spine | Hensel paper §1.1/§2.1; Decimal Fingers §3; ancestors table |
| Computer algebra / exact computation | Hensel codes, CRT, rational reconstruction are the paper's constructive body | Hensel v1.2.0 deposit (src/tests/benchmarks); Wang–Guy–Davenport 1981; Boehm–Decker–Fieker–Pfister line |
| Numeration / notation | The project is a numeration paper (post-positional numeracy) | NUMERATA; Silent Radix; Nonlinear Tree-Based |
| Epistemology of notation | The conceptual lineage the paper cites (decimal as place-local convention) | Decimal Fingers to Adelic Freedom; Ten-Fingered Trap |

## 2. Minimum-Viable-Finding

**The adelic product formula — the identity that ties the places of Q together — is a machine-checkable integrity invariant for multi-place exact arithmetic, and it is used as such by none of the audited records.** Single-place Hensel arithmetic (published, tested) has no global invariant across places; modular-methods literature uses CRT + Farey bounds without the product formula; the conceptual records assert the formula's centrality without executing it. The structural correspondence "global arithmetic identity ↔ runtime verification invariant" is the paper's contribution.

## 3. Silo Cost Table

| Domain | Structure Name | Earliest | Connected to computation | Silo Cost | Key Paper |
|---|---|---|---|---|---|
| Number theory | Ostrowski completions | 1916 | 1975 (Hensel-code arithmetic) | ~59 yr | Ostrowski, Acta Math. 1916 |
| Number theory | Adelic product formula (Tate thesis framework) | ~1950 | as runtime invariant: NEVER (audit 2026-08-26) | ~76 yr and open | Tate thesis |
| Computer algebra | Hensel codes / error-free computation | 1975 | same | 0 | Krishnamurthy, Gregory et al. |
| Computer algebra | Rational reconstruction (CRT + Farey bounds) | 1981 | same | 0 | Wang, Guy, Davenport 1981 |
| Numeration | Positional notation as ultrametric tree | 2025 | 2026 | ~1 yr | Nonlinear Tree-Based 21046213; Silent Radix 21148596 |

Silo-failure flag: the product formula has been central to number theory since Tate's thesis; exact computation has existed since the 1970s; the two have not been joined as verification machinery. [SILO-FAILURE: >50yr gap — the paper makes the connection explicit and executable.]

## 4. Bayesian Evidential Weight (KIF-60)

The central claim is a **constructed engineering correspondence**, not an empirical prediction:
- **Pre-registration:** H-PPN-1/3/4 written before implementation (PROJECT-PLAN commit = immutable timestamp).
- **Falsifiability gradient:** H-PPN-3 disconfirmation (one collision in 10^5 trials kills injectivity); H-PPN-4 disconfirmation (a published system using the product formula as invariant kills novelty).
- **Surprise accounting:** the product formula equaling 1 is a theorem (P ≈ 1 under any correct implementation) — it carries **engineering and pedagogical weight, not novel empirical evidence**. The paper states this; it does not claim a new physical prediction.
- **Confirmation-seeking check:** the tests discriminate the multi-place construction from the single-place baseline (round-trip exactness across places, failure localization), not merely from "no arithmetic at all".

## 5. Synthesis Meta-Principle + Frontier Question

**Meta-principle:** the global invariants of a number system (here, the product formula) are also its strongest runtime correctness machinery — the identity that unifies the places is the identity that audits the computation.

**Frontier question:** can every global reciprocity-type identity (product formulas, class-field identities) be compiled into a verification invariant for a corresponding family of computations — i.e., is "invariant-as-checksum" a systematic dictionary between number theory and computer algebra? (Feeds the UIA Q15 seed and, at a distance, JPCUB's cost-of-exactness question.)
