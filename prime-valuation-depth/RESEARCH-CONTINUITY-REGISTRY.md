# RESEARCH CONTINUITY REGISTRY — QNFO.RES.004 Prime Valuation Depth

**Maintained:** 2026-08-13 · **WBS:** QNFO.RES.004 · **Source paper:** `prime-valuation-depth.md` (v0.1-draft)
**Protocol:** Research Continuity Registry Protocol (research v2.64, HARD)

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:----------------|
| FQ1 | Does the LoF↔prime-tree correspondence satisfy at least one non-vacuous shared structural law beyond nesting/multiplicativity? | OPEN | Formalize a candidate law (e.g., a functor from the free monoid on primes to the calculus of indications); test against re-entrant distinction semantics | YES |
| FQ2 | Is there a p-adic dimension-depth statement about tensor products that does not follow from the standard multiplicativity of dimensions? | OPEN | Search for a tensor-network invariant that v_p(dim H) tracks (cf. p-adic tensor networks) | YES |
| FQ3 | Does the structural no-cloning reading yield any statement about no-broadcasting or monogamy expressible only in branch-depth vocabulary? | OPEN | Attempt a branch-depth formulation of monogamy of entanglement as a resource inequality | YES |
| FQ4 | Does an adelic completion of state space (Archimedean amplitudes × p-adic depth profiles) constrain any measurable prediction? | OPEN (FRONTIER) | Derive at least one falsifiable delta or formally retire | YES |
| FQ5 | Does the claimed BEC 'bypass' of no-cloning [@datta2022] survive adversarial analysis, and does it constrain the structural reading? | OPEN | Obtain and analyze the preprint; classify the effective dynamics | NO (review task) |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | The correspondence of §3 is either vacuous (holds between any two nested structures) or non-vacuous (fails for some nested structure); a demonstrated third structure satisfying both laws by coincidence would reduce it to relabeling. | 2026-08-13 → 2027-08-13 | Formalization attempt in FQ1; adversarial examples | If a critic exhibits a nested structure unrelated to primes/distinctions satisfying both Laws 1-2, the correspondence is downgraded to [RELABELING] |
| P2 | No linear cloning map exists for d>1 — the structural reading does not change the theorem. | N/A (theorem) | Standard proof | N/A — theorem; the READING is disconfirmed if it adds no content (see P3) |
| P3 | The branch-depth vocabulary yields at least one statement about quantum no-go theorems not expressible without it. | 2026-08-13 → 2028-08-13 | FQ2/FQ3 derivations | If every branch-depth statement is translatable to standard formalism with no loss, the reading is [RETRODICTION — not evidence] |
| P4 | An adelic state-space formulation either yields a falsifiable prediction or is formally retired. | 2026-08-13 → 2028-08-13 | FQ4 derivation | If after derivation attempts no delta exists, RQ6 is retired with documentation |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Disconfirmed if |
|:---|:----------------|
| RQ1 (LoF×prime-tree correspondence) | The shared laws (nesting/hierarchy + multiplicativity) are shown vacuous — i.e., they hold between any two structures with a notion of nesting |
| RQ2 (Ostrowski exhaustiveness) | A nontrivial absolute value on Q outside the Archimedean/p-adic classes is exhibited (mathematically impossible per Ostrowski; kept for symmetry) |
| RQ3 (v_p(dim H) as tensor-branch depth) | v_p(dim H) tracks no tensor-product feature beyond dimension number (FQ2) |
| RQ4 (structural no-cloning content) | The reading adds no statement beyond the standard linearity proof (P3) |
| RQ5 (adjacent no-go theorems) | Branch-depth statements about no-broadcasting/monogamy all reduce to standard proofs with no new content |
| RQ6 (adelic predictions) | No falsifiable delta after derivation attempts; retired with documentation (P4) |

## 4. PRE-REGISTRATION SCAFFOLDS

### REG-RES004-001 — Correspondence non-vacuity test
- **Hypothesis:** The LoF↔prime-tree correspondence is non-vacuous: there exists a nested structure N (not prime trees, not distinctions) that fails at least one of Laws 1-2.
- **Falsification:** If no such N exists, the laws are too broad → correspondence downgraded to [RELABELING].
- **Data:** Formal definitions of Laws 1-2; candidate counterexamples from order theory (trees, semilattices, ultrametric spaces).
- **Deadline:** 2027-08-13. **Pre-registered:** 2026-08-13 (this file, git commit).

### REG-RES004-002 — Adelic delta or retirement
- **Hypothesis:** An adelic formulation of state space yields at least one falsifiable prediction distinct from standard QM.
- **Falsification:** After documented derivation attempts, no distinct prediction exists → RQ6 retired.
- **Data:** Derivation notes; comparison table vs standard formalism.
- **Deadline:** 2028-08-13. **Pre-registered:** 2026-08-13.

## 5. CALIBRATION REGISTER

```
[CHECK: 2027-08-13] REG-RES004-001 adjudicated: correspondence non-vacuity test done.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2028-08-13] REG-RES004-002 adjudicated: adelic delta or retirement.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2029-08-13] At least one external citation of the p-adic-depth reading
as a bridge between the calculus of indications and number theory.
Strength: [WEAK] | Status: [PENDING]
```

## 6. NEXT ACTIONS (PRIORITIZED)

| Priority | Action | Dependency | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Publish v0.1 (P5 pipeline) | none | Zenodo + GitHub + D1 |
| P1 | FQ1: formalize the LoF→prime-tree functor | P0 | 2026-Q4 |
| P1 | FQ2: search p-adic tensor-network invariants | P0 | 2026-Q4 |
| P2 | FQ5: adversarial analysis of the BEC bypass preprint | P0 | 2027-Q1 |
| P3 | FQ3/FQ4: branch-depth no-go statements + adelic delta | FQ1, FQ2 | 2027-Q2+ |

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- 2026-08-13: Registry created with P0 publication; FQ1-FQ5 seeded; P1-P4 pre-registered.
- Maintenance: update this file on every phase transition and on any publication that adds/changes frontier questions, predictions, or disconfirmation conditions. Version-bump `updated_at` header.
- Companion: `artifacts/calibration-register.md` (gate-level, mirrors §5).
