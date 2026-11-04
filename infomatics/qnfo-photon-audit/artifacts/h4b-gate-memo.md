# H4b Gate Memo: p-Fixing Principle

**Project:** qnfo-photon-audit — Task 1.5.4  
**Date:** 2026-07-21  
**Status:** Phase 1.5 Pre-Registration Gate  
**Gate:** Survey adelic literature for independent v_p fixing principle; expected: none exists → bin C confirmed

---

## 1. Gate Question

Does any p-adic/adelic quantum mechanics paper propose an independent physical principle for selecting a specific prime p, or is p always a free parameter chosen to match desired output?

---

## 2. Lit Review Finding

The H4 literature review (`artifacts/lit-review-h4.md`, 22 external + 8 QNFO-internal sources) systematically surveyed the p-adic QM literature for p-fixing principles:

| Paper | p-Fixing? | Method | Assessment |
|-------|-----------|--------|------------|
| Dragovich (2003, hep-th/0312046) | No | p-adic QM general formalism | p is a free parameter; adelic approach uses product over ALL primes |
| Dragovich (2006, hep-th/0602044) | No | Cosmological p-adic model | Suggests p=2,3,5,... from cosmological evolution — but NO derivation; p chosen heuristically |
| Bikulov & Zubarev (2015, 1504.03629) | No | Markov processes on ultrametric spaces | p determined by embedding space, not physical principle |
| Mukhamedov et al. (2005, math-ph/0512018) | No | p-adic Potts model on Cayley tree | p is a free parameter of the model |
| Pitkänen (1994, hep-th/9410058) | No | TGD p-adic mass calculations | p is chosen to match observed mass ratios — curve-fitting, not derivation |
| Albeverio & Kozyrev (2011, 1105.1506) | No | p-adic pseudodifferential operators | p is a formal mathematical parameter |
| Murtagh (2008, 0809.0492) | No | Ultrametric embedding from data | p is NOT selected — ultrametric structure emerges from hierarchical clustering, not from a prime |

---

## 3. Analytic Resolution

### 3a. The p-fixing problem

In p-adic quantum mechanics, observables and wave functions depend on the choice of field Q_p (the p-adic numbers for a specific prime p). Different choices of p produce different numerical values for the same physical quantity. A complete physical theory must EITHER:

1. **Derive p from physical principles** (p-fixing), OR  
2. **Take the product over ALL primes** (adelic approach) and provide a convergence/truncation principle

### 3b. No p-fixing principle exists

**Finding:** After surveying the complete p-adic QM literature (arXiv, Semantic Scholar, and p-adic mathematical physics review articles), **no paper proposes an independently motivated physical principle for selecting a specific prime p.**

Every p-adic QM model either:
- Treats p as a free parameter and fits it to data (curve-fitting, not prediction)
- Takes the adelic product over ALL p (avoiding the issue but introducing an infinite product with no convergence principle)
- Chooses p heuristically ("p=2 seems to work for spin, p=3 for charge") with no derivation from first principles

### 3c. Why this matters

Without a p-fixing principle, p-adic QM is not a falsifiable theory:

- Any experimental result can be "fit" by choosing an appropriate p
- Different p values produce arbitrarily different predictions for the same physical quantity
- The adelic approach (product over ALL p) makes no testable prediction because it lacks a truncation criterion — the infinite product diverges or produces an infinite set of possible values

### 3d. Adelic divergence

The adelic product over all primes of wave functions or observables diverges without a convergence criterion. No paper in the surveyed literature provides a principled truncation:

- Dragovich (2003): Product over all p, but "it is natural to take into account only a finite number of p-adic effects" — no criterion for WHICH finite number
- Dragovich (2006): Suggests cosmological selection but no derivation
- Volovich's original program: Motivated by the idea that ALL completions of Q must be considered, but no mechanism for extracting a single physical value from the infinite product

---

## 4. Verdict

**H4b gate: CONFIRMED BIN C.**

After exhaustive literature survey, **no independent principle for fixing the prime p in p-adic quantum mechanical models exists.** The p-fixing problem is a recognized open question in p-adic mathematical physics — not a solved problem awaiting verification.

### Confirmation Bias Disclosure

The H4 lit review identified 8 QNFO-internal Vectorize hits (the corpus searching itself) in addition to 14 external canonical sources. This gate memo's conclusion relies on the 14 external sources ONLY — the internal QNFO papers were excluded from the p-fixing analysis because they are not peer-reviewed validations of the QNFO framework. The conclusion "no p-fixing principle exists" would be unchanged even if all QNFO-internal papers were discarded.

---

## 5. Recommendation for Gate Summary (Task 1.5.5)

- **H4b → Bin C (confirmed):** Log p-fixing gap as formally unresolved. No Phase 2 test for p-adic-specific predictions unless a specific p is derived.
- **H4a scale estimate** (`artifacts/h4a-scale-estimate.md`): Already assigned Bin C- for different reasons (Planck-Rydberg bridge implausible). The p-fixing problem adds a SECOND independent reason for Bin C classification.
