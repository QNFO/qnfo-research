# Journal Submission Package — QNFO.RES.007 (Invariant Structural Value)

**Date:** 2026-08-14 · **Status:** READY — submission requires user decision (journal shortlist confirmation)
**DOI:** 10.5281/zenodo.21929902 (v0.3, latest published; concept 21929478)
**Primary target:** Foundations of Physics (Springer) · **Secondary:** Synthese (Springer)

---

## 1. Draft Cover Letter (Foundations of Physics)

To the Editor, Foundations of Physics

Dear Editor,

I am submitting the manuscript *Invariant Structural Value: Fundamental Constants and Formulas as Invariant Relations* for consideration as a research article.

**Pre-registered disconfirmation conditions (the strongest peer-review asset).** Every claim in the paper carries an explicit falsifiability condition, locked at project initialization (2026-08-14, git commit f718fae) and re-affirmed in the published record:

- **C1** (constants/formulas encode invariant relations, not unit-dependent magnitudes) is disconfirmed if a dimensionful constant is shown to carry invariant physical content beyond its role as a unit bridge, or if a claimed invariant is demonstrated scale-dependent where asserted scale-invariant.
- **C2** (measurable physics is the invariant quotient of a larger mathematical structure modulo redundancy groups: units, coordinates, gauge, basis, scale) is disconfirmed if a measurable quantity is exhibited that is not expressible as an invariant under the enumerated redundancy groups — e.g., a gauge-dependent observable that is nonetheless measured.
- **C3** (e is the fixed point of self-application f′=f; π is the fixed point of self-closure via the exp kernel 2πℤ; the Euler identity is their joint fixed point, derived constructively from mark-and-distinction self-reference) is disconfirmed if e or π can be shown to require input beyond mark-and-distinction plus self-reference, or if a self-referential equation is exhibited whose fixed point is a constant other than e or π with no structural characterization.

I explicitly invite adversarial validation of C3 in particular: it is a `[UNIQUE-CLAIM]` with zero external corroboration found across OpenAlex, Crossref, Zenodo, Europe PMC, and arXiv, and the manuscript supplies the constructive derivation (Picard iteration → series; periodic boundary conditions → kernel 2πℤ) plus pre-registered surprise accounting, rather than pattern-matching.

**Independence and provenance.** Sole author; no external funding; no conflicts of interest. ORCID: 0009-0002-4317-5604.

**Reproducible evidence.** Independent recomputation of every numerical value is recorded in the fit-verify artifact (e series/limit, Machin/Leibniz π, Euler identity |1.2e-16|, f′=f fixed point, periodicity). The bibliography is live-verified (P3.AUTHOR-GATE: 42 unique works, 6 wrong/synthetic DOIs corrected, zero duplicates). The full source set — manuscript, bibliography, verification artifacts, research-continuity registry with frontier questions and falsifiable predictions — is available at DOI 10.5281/zenodo.21929902 (GitHub: QNFO/qnfo-research, branch res/paper/invariant-structural-value).

Thank you for your consideration.

Rowan B. Quni-Gudzinas
Independent researcher, QNFO

---

## 2. Submission Readiness Checklist

| Item | Requirement | Status |
|:-----|:------------|:-------|
| Abstract 150–250 words | research skill professional-publication standard | ⚠️ **~110 words** — expand before submission (candidate expansion in §3) |
| Keywords 4–6 | YAML frontmatter | ✅ 11 present (Zenodo metadata); trim to 4–6 for journal system |
| Title single, non-duplicated | TITLE-DUPLICATION-1 | ✅ verified at build |
| Declarations (9 subsections) | Funding, COI, Data, Materials, Code, Contributions, Ethics, Consent, License | ✅ present in manuscript |
| No internal language / WBS codes | INTERNAL-REF-1 (language gate) | ✅ CLEAN at v0.3 build (BP-gate suite) |
| Certainty labels retained | MAP-TERRITORY-1; signal calibration | ✅ `[TERRITORY]` labels with disconfirmation conditions present |
| Bibliography | P3.AUTHOR-GATE, 42 unique works, 0 dups, 0 synthetic DOIs | ✅ verified (citation-audit.md) |
| Numeric claims | BP-1/BP-6/BP-10 independent recompute (fit-verify.txt) | ✅ ALL PASS |
| Repo ↔ deposit consistency | PUBLICATION-SOURCE-COMPLETENESS-1 | ✅ v0.3 deposit carries md/pdf/html + full artifact set |
| C3 uniqueness burden | KIF-60 surprise accounting; constructive derivation | ✅ documented (phase2-literature-review §4; registry REG-RES007-001) |

## 3. Abstract Expansion (candidate, ~200 words)

> We develop the thesis that the fundamental constants and formulas of physics encode invariant relations rather than unit-dependent magnitudes. A measured physical quantity is a number that survives arbitrary choices — of unit system, coordinate system, gauge, Hilbert-space basis, and energy scale; what is invariant under these choices is what is physical. We characterize the invariant content of constants and formulas as dimensionless ratios (m_p/m_e, the fine-structure constant α), symmetry-group data, topological indices, and fixed-point values, and we argue that dimensionful constants (c, ħ, G, k_B) function as bridges between categories of quantity whose numerical values are conventions. Measurable physics is characterized as the invariant quotient of a larger non-measurable mathematical structure — complex phases, gauge potentials, path-integral histories, ghost fields and BRST cohomology, bare parameters — modulo redundancy groups. The constants e and π are shown to be fixed points of two canonical self-referential operations on a primitive mark-and-distinction: e of self-application (the unique solution of f′=f with f(0)=1, exhibited by Picard iteration) and π of self-closure (the half-period fixed by the exponential map's kernel 2πℤ under periodic boundary conditions). The Euler identity e^{iπ}+1=0 is their joint fixed point. Every claim carries an explicit disconfirmation condition.

## 4. Post-Acceptance (locked in strategy §4)

Newversion with `related_identifiers: isPublishedIn` (journal DOI) per research v2.88 — deposit-API full-object PUT (PARTIAL-PUT-CLEARS-FIELDS-1: preserve all metadata incl. GitHub provenance).

## 5. Open for User Decision

1. Confirm journal shortlist (Foundations of Physics primary / Synthese secondary) or reorder.
2. Authorize actual submission (journal system account/portal, author agreement, possible APC for hybrid OA).
3. Confirm the abstract expansion (§3) before final submission copy.
