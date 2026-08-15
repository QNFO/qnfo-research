# bp-gates.md — Braiding Phase Gates from the Re-Entrant Calculus

**WBS:** QNFO.RES.011.P6R (application roadmap artifact, SOFT-3 remediation)
**Status:** ROADMAP — not yet materialized (referenced in paper §8 Applications, item 1)
**Operational signature:** gate table generated from braid words classified by the re-entrant calculus; anyon-platform-agnostic
**Domain-specific falsifiable claim:** a braid word classified bosonic under the calculus maps to a non-trivial gate (→ calculus is not statistics-faithful)

---

## 1. What this artifact will be

A machine-readable table `braid-word → gate operation` derived purely from the
mark calculus's classification of braided structures (paper §5–§6), usable as a
design language for topological quantum computation:

```
re-entrant mark
  → braided monoidal category (abelian sector; ribbon identity, paper T2)
  → braid-word classification (S_N sector in d>=3, B_N sector in d=2)
  → gate table (word → unitary on the fusion space)
```

## 2. Relation to the published claims

- Paper §8 A1: "Gate sets generated from braid words classified by the re-entrant calculus, hardware-agnostic."
- The classification is the paper's T2/T3 construction: exchange scalar R = e^{2πis};
  involutive sector (±1) in d>=3; arbitrary phase in d=2.
- The gate table is therefore *statistics-faithful by construction* in the abelian sector.

## 3. Falsifiable claim (unchanged from paper)

> A braid word classified bosonic under the calculus maps to a non-trivial gate.

If true → calculus classification disagrees with physical braiding → the
classification is not statistics-faithful → T2's construction is bounded.

## 4. First concrete step (next cycle)

1. Enumerate 2-strand and 3-strand braid words (B_2 ≅ ℤ: σ₁ⁿ; B_3: Artin generators σ₁, σ₂).
2. Classify each word by the calculus rules (ribbon identity + abelian-pair postulate → scalar λ = e^{iθ}).
3. Map λ to a standard SU(2)-level gate set (phase gate, NOT gate for θ=π, identity for θ=0).
4. Emit `bp-gates.json` + verify against known anyon gate tables (Fibonacci/Ising, cited in paper §6.2).

## 5. Status

- [ ] 2-strand word enumeration
- [ ] 3-strand word enumeration
- [ ] calculus classification implementation (toy-model suite precedent: companion essay 10.5281/zenodo.21943007)
- [ ] gate-mapping table
- [ ] cross-check vs standard anyon gate sets
- [ ] publication as companion artifact (Zenodo newversion or standalone record)
