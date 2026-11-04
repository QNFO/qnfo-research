# Audit Rubric — Evidence Tags and Bin Gate Criteria

**Project:** qnfo-photon-audit  
**Version:** v0.1  
**Date:** 2026-07-18

---

## Evidence Tags

Every claim in the final audit report is tagged with exactly one of:

| Tag | Full Name | Definition | When to use |
|---|---|---|---|
| `[Est]` | Established | Supported by peer-reviewed literature with explicit citation (DOI/arXiv). The result is generally accepted in the relevant community. | Standard textbook results, well-cited experimental confirmations. |
| `[Open]` | Open problem | The question is well-posed in the literature and actively researched, but no consensus answer exists. The state of the art is quantified. | Frontier research questions where multiple groups publish competing results. |
| `[Unsup]` | Unsupported | No derivation or evidence exists that supports this claim as stated. This does not mean the claim is *false* — only that it lacks evidential backing at present. | Claims that are plausible but have no citable support, or claims that are too vaguely stated to be evaluated. |
| `[Blocked]` | Theorem-blocked | The claim as stated is inconsistent with a known theorem unless the model specifies which theorem assumption it circumvents. Stronger than [Unsup] — requires affirmative justification to escape. | Spin-statistics theorem, no-cloning theorem, second law of thermodynamics, etc. |
| `[CE]` | Category error | The claim conflates concepts from different domains in a way that invalidates the argument structure, independent of empirical content. | Claiming complexity-class advantage from algebraic structure change without defining the computational model. |

### Decision tree for tagging:

```
Is there a citable peer-reviewed result supporting this?
  ├── YES → Is it generally accepted in the relevant community?
  │         ├── YES → [Est]
  │         └── NO  → [Open] (with quantification of disagreement)
  └── NO  → Is the claim logically well-posed?
              ├── YES → Is it inconsistent with a known theorem?
              │         ├── YES → [Blocked] (cite theorem + explain which assumption)
              │         └── NO  → [Unsup] (no evidence yet, could change)
              └── NO  → [CE] (explain the category confusion)
```

---

## Bin Gate Criteria

Claims must clear the following gates to be classified in each bin:

### Bin A — Runnable now

A claim is bin A iff ALL of:
1. A parameter-sparse (or parameter-free) prediction exists with explicit functional form.
2. The prediction has been locked (timestamped) before comparison to data.
3. The comparison data exists (literature values, published datasets) or can be collected with known methodology.
4. Both positive and negative outcomes are defined — the test can fail.

### Bin B — Needs theory first

A claim is bin B iff:
1. The testing methodology is sound (we know *how* we would test it if we had a prediction).
2. But no lockable prediction currently exists (no explicit Lagrangian, no computed number).
3. The claim could in principle escape to bin A if a derivation succeeds.

### Bin C — Not falsifiable as posed

A claim is bin C iff ANY of:
1. The comparison procedure has ≥N free parameters for ≤N facts to explain (curve-fitting).
2. No negative outcome is defined — the claim can always be reinterpreted to survive apparent falsification.
3. The claim is stated at a level of vagueness that precludes operationalization.
4. The claim invokes entities or mechanisms not connected to observables by any specified bridge principle.

### Bin U — Unfalsifiable as formulated

A claim is bin U iff ALL of:
1. The report itself demonstrates that no experimental outcome could disconfirm the hypothesis as currently formulated.
2. The hypothesis can always be reinterpreted or parameter-adjusted to survive any apparent falsification.
3. This category is more severe than Bin C: Bin C means "no test exists YET" (unsupported/blocked); Bin U means "no test CAN exist without changing the hypothesis itself."

Bin U is reserved for claims with qualitatively worse unfalsifiability: arbitrary free-parameter choice, no defined bridge to observables, or reliance on entities not connected to measurement by any specified principle.

A U→C promotion requires: the claim must be reformulated with a fixed, operational bridge to observables such that at least one well-defined negative outcome is possible.

### Promotion gate (bin C → B, or bin B → A):

A C→B promotion requires: the claim is restated with specific, operational content.
A B→A promotion requires: a lockable prediction is produced with fewer parameters than facts.

---

## Pre-Registration Compliance Checklist

For every comparison in the final report:

- [ ] Functional form of prediction fixed BEFORE comparison
- [ ] All free parameters enumerated and counted
- [ ] Number of free parameters < number of independent facts to explain
- [ ] Prediction timestamp-locked (git commit or equivalent)
- [ ] Comparison data source cited
- [ ] Both positive and negative outcomes specified
