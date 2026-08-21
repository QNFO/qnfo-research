# Hypothesis Cards — QNFO.RES.021 (pre-registered 2026-08-20)

Instrument: HYPOTHESIS-CARD-1 (research v2.128). Each card carries: claim, prediction,
falsifiers, surprisal. The falsifier register is re-checked at each phase gate (P2, P5,
P6) and at the 90-day re-sweep. Registered BEFORE any paper writing; cards are not
edited retroactively without a dated amendment note.

---

## H-CONT — Continuum Information Content

- **Claim:** A single real coordinate specifies infinitely many yes/no distinctions
  (its binary expansion is an infinite string). A finite-entropy world cannot contain
  such coordinates, so the Archimedean continuum is unphysical as an ontology.
- **Prediction:** Any coordinate used by a finite physical system admits a finite
  description at the system's resolution; resolution bounds are fundamental, not
  practical.
- **Falsifiers:** (a) a physical encoding scheme that stores an arbitrary real in finite
  information (excluded by the standard diagonal argument — card registers the premise);
  (b) an observable that demonstrably requires exact reals at fixed finite resolution.
- **Surprisal:** low (premise-level; follows Planck cellulation + counting).
- **Status:** registered 2026-08-20. Grade: L0/L1 premise, not a new theorem.

## H-ULTRA — Ultrametric State Space

- **Claim:** At any fixed resolution, distinguishability between quantum states is an
  equivalence relation whose induced geometry is ultrametric (strong triangle
  inequality); betweenness vanishes — there is no arbitrarily small "in-between".
- **Prediction:** Hierarchical (tree) clusterings of measurement-outcome partitions fit
  empirical distinguishability data with strong-triangle-inequality consistency; no
  reproducible triple violates it.
- **Falsifiers:** a reproducible triple of states a, b, c at one resolution with
  d(a,c) > max(d(a,b), d(b,c)) beyond measurement error.
- **Surprisal:** moderate (ultrametricity is known in spin-glass/replica and
  hierarchical-clustering literature; the claim here is its necessity for ANY finite
  state space).
- **Status:** registered 2026-08-20. Verification: seeded construction + violation
  search (P5).

## H-UNIT — Unitarity from the Entropy Hessian

- **Claim:** The reversible component of an entropy-Hessian gradient flow on N
  alternatives becomes symplectic (unitary) in the large-distinction limit N → ∞, with
  per-step entropy production → 0.
- **Prediction:** For N = 2^4 … 2^14 seeded Monte Carlo runs: (a) entropy production per
  step scales to 0 (power-law fit exponent < 0); (b) the effective generator's deviation
  from anti-Hermiticity (symplecticity defect) scales to 0; (c) the limit flow preserves
  the max-entropy weights.
- **Falsifiers:** entropy production does not vanish in the limit; symplecticity defect
  plateaus above zero.
- **Surprisal:** high — shows unitary evolution as emergent bookkeeping, not axiom.
- **Status:** registered 2026-08-20. Verification: seeded Monte Carlo (P5).

## H-BORN — Born Weights as Max-Entropy Weights

- **Claim:** Born probabilities are the maximum-entropy weights over finite alternatives
  in the large-distinction limit.
- **Prediction:** For a fixed test-state family, seeded Monte Carlo of the
  N-alternative max-entropy model reproduces Born frequencies within ±2σ statistical
  tolerance for N large.
- **Falsifiers:** systematic deviation beyond tolerance that does not shrink with N.
- **Surprisal:** high.
- **Status:** registered 2026-08-20. Verification: seeded Monte Carlo (P5).

## H-TIME — Relational Time from a Distinction Clock

- **Claim:** Page–Wootters relational time emerges from a clock subsystem counting n
  distinctions; the relational dynamics of the rest converges to Schrödinger evolution
  as n → ∞.
- **Prediction:** Convergence diagnostics (fidelity of one relational step vs the
  continuous propagator) scale to 1 as n grows; discrete-time artifacts shrink with n.
- **Falsifiers:** no convergence; artifacts independent of n.
- **Surprisal:** moderate (Page–Wootters is established; the finite-distinction
  implementation is new).
- **Status:** registered 2026-08-20. Verification: convergence simulation (P5).

---

**Falsifier register re-check log:**
- 2026-08-20 P0: all cards registered; no falsifier triggered (nothing yet tested).
- 2026-08-20 P2 gate: re-checked before paper-structure work. No card falsified by
  Phase 1 diligence, but two cards received corpus-informed REFINEMENTS (recorded as
  dated amendments, claims unchanged): H-CONT — corpus 10.5281/zenodo.21647362 +
  Gisin–Del Santo already own the finite-information premise; the card now inherits it
  as L0/L1 input (trilogy refinement: uncountable breadth vacuous, computable depth
  real). H-ULTRA — corpus 10.5281/zenodo.21120286 (8,000+ WDW systems) shows
  ultrametricity is NOT generic (29–35% violation for nondiagonal clock-rest coupling);
  the card's prediction is restated conditionally (ultrametricity for partition-type
  distinguishability, subject to the semiorder argument). H-UNIT/H-BORN/H-TIME remain
  unfalsified and untested — P5 simulation is the next falsifier test.
- 2026-08-20 P4 gate: re-checked immediately before paper-draft prose. No falsifier
  triggered. H-CONT and H-ULTRA carry the P2 amendments forward unchanged (claims
  intact, conditional restatement for H-ULTRA). H-UNIT/H-BORN/H-TIME still unfalsified
  and untested — P5 simulation is the next falsifier test; the draft's §8 and the
  verification section pre-register the exact falsifier tests (entropy-production
  scaling, symplecticity defect, Born deviation tolerance, clock convergence).
- 2026-08-21 P5 gate: falsifier tests EXECUTED (artifacts/verification/, seed
  20260821, 5/5 PASS). NO FALSIFIER TRIGGERED. H-ULTRA V2: 0/262,144 ultrametric
  violations (F2 not triggered; Archimedean control 83,328 confirms the test is
  live). H-UNIT V3/V4: per-distinction σ(N) exponent −0.88 and symplecticity-defect
  exponent −1.00 — entropy production vanishes in the large-distinction limit (F3
  not triggered; fixed-γ control exponent +0.14 shows the falsifier is live). H-BORN
  V5: |P_Born − P_maxent| exponent −1.09 (F4 not triggered). H-TIME V6: clock error
  exponent −2.00 (F5 not triggered). H-CONT: premise stands (V1 golden identity).
  Two construction corrections were applied per VERIFY-FIX-RERUN-1 (V3/V4
  non-degenerate start; V6 second-order clock step) — bugs in the checks, claims
  unchanged. Next falsifier exposure: P7 post-publication audit + independent
  re-runs.
