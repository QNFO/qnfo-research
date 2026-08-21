# Paper Outline — QNFO.RES.021 (2026-08-20, P2)

Working title: **Finite-Distinction Quantum Mechanics: Unitary Evolution and
Superposition as the Large-Distinction Limit of Stochastic Thermodynamics**

Target format: 12–15 page preprint, RES.020 template (graded claims, premise-depth
disclosure, falsification conditions, deposited verification source). All section
content below reflects the Phase 1 grade re-mapping; the core claim (§2 of
PROJECT-PLAN.md) remains frozen as registered.

---

## 1. Introduction

- Entropic monism as inherited premise: "quantum mechanics is thermodynamics"
  (corpus: entropic-operational-paradigm, 10.5281/zenodo.17687207, 2025).
- The finite-information principle as inherited premise: Gisin 2018/2019
  (arXiv:1803.06824, 1909.03697), Del Santo–Gisin 2024 (arXiv:2409.10601), corpus
  convergence (finite-precision-oc-convergence, 10.5281/zenodo.21647362).
- The new move of this paper: from "quantities carry finite information" to "the
  STATE-SPACE GEOMETRY of finite distinctions is combinatorial/ultrametric", and the
  conjecture that unitarity + superposition are the large-distinction limit of an
  entropy-Hessian gradient flow.
- SO-WHAT (plain prose): if the Hilbert space is a thermodynamic limit, the cost of a
  correct quantum answer is a function of distinctions made — a countable, benchmarkable
  resource (JPCUB). Premise-depth disclosure in §2 (where the premises end).
- Grading ladder declared: identity / dictionary / conjecture (RES.020 convention).

## 2. The Continuum as Infinite Information (H-CONT; inherited premise)

- A single real coordinate = infinitely many yes/no distinctions (binary expansion);
  a finite-entropy world cannot contain it. UV catastrophe, again.
- INHERITED (not new): Gisin–Del Santo finite-information quantities; corpus OC
  convergence (7 convergent theses).
- Trilogy refinement (10.5281/zenodo.21672990): uncountable BREADTH is vacuous;
  computable DEPTH is physically real (dynamics, causality); p-adic VALUATION real but
  not geometric. The paper adopts this: "uncountable precision is unphysical" — NOT
  "the continuum is unphysical".
- Map-territory: coordinates are maps; the claim is about ontology of precision, graded
  thesis-level.

## 3. The Geometry of Finite Distinctions (H-ULTRA; refined)

- Distinguishability as equivalence relation ⇒ partition ⇒ tree/ultrametric distance;
  no arbitrarily small betweenness; Cartesian axes are labels.
- SEMIORDER WOBBLE (Luce 1956, 10.2307/1905751): real indistinguishability is a
  semiorder, not an equivalence relation. The paper must argue the idealization (fixed
  resolution ⇒ threshold + transitivity by construction) — named, not hidden.
- CORPUS CONSTRAINT: conditional-state-distances-pw-clocks (10.5281/zenodo.21120286):
  ultrametricity is NOT generic for PW conditional-state overlap distances (29–35%
  violation; exact iff diagonal H_CR). Two senses disentangled: (a) partition
  distinguishability (this paper's object — trivially tree-like); (b) conditional-state
  overlaps (corpus result). The paper claims (a) and cites (b) as the boundary.
- Underdetermination (UMP.010/UMP.011): rendered-ultrametric vs Archimedean is
  observationally indistinguishable — the ontology claim earns its keep ONLY via
  finite-N predictions (§6, §8).

## 4. Quantum Mechanics as Stochastic Thermodynamics of Finite Alternatives

- The model: N distinct alternatives; entropy S = −Σ p_i ln p_i; entropy Hessian
  ∇²S = Fisher metric (information geometry, Amari/Čencov — imported named input).
- Dynamics: gradient flow on the statistical manifold + a reversible (symplectic)
  component; stochastic thermodynamics of discrete states (Seifert, Esposito–Van den
  Broeck — imported).
- Environment/reservoir story (UIA Q7 thermodynamician demand): the flow must specify
  its heat bath, temperature, and entropy production — otherwise it is kinematics, not
  thermodynamics. The model gets a per-alternative energy assignment via the max-entropy
  constraint (Boltzmann weights), temperature from the Lagrange multiplier.

## 5. Unitarity from the Entropy Hessian (H-UNIT; THE novel conjecture)

- Conjecture (L3-grade): the reversible component of the entropy-Hessian flow on N
  alternatives becomes symplectic as N → ∞, with per-step entropy production → 0.
- THE ℂ GAP (named central problem): a real gradient flow produces real symplectic
  structure; complex amplitudes must come from somewhere. Constraints: Hardy 2001
  (quant-ph/0101012 — continuity axiom "explains the need for complex numbers"),
  Aaronson 2004 (quant-ph/0401062 — real amplitudes fail; only the 2-norm survives).
- Candidate route (to be tested in P5): the Hessian's symplectic form + the
  large-distinction limit must select the 2-norm and complex structure; if the simulator
  shows entropy production NOT vanishing, H-UNIT is falsified and the paper reports the
  negative result honestly (VERIFY-FIX-RERUN-1: a failing check is a bug in the check
  or the claim — fix the construction, re-run until PASS, or downgrade the claim).
- PBR wall (1111.3328): the finite-alternative reading is ψ-epistemic-adjacent; the
  paper must state exactly which PBR assumption its model violates (independent
  preparation / onticity), or accept ψ-ontic grading.
- **UIA Q15 seed (answered here; red-team H-2 remediation):** does the large-distinction
  limit N → ∞ reimport the continuum through the parameter space? Answer: N is a finite
  integer inside every model; the limit is taken over the model FAMILY, not inside any
  model — no coordinate of any finite model is continuous. The continuum re-enters only
  as the MAP (the limiting object we use to describe the family), never as a TERRITORY
  claim; that is the map/territory discipline of §2 applied to the model family itself.
  Registered source: UIA Q15, artifacts/universal-ignorance-audit.md.

## 6. Born Weights as Max-Entropy Weights (H-BORN)

- Conjecture: Born probabilities = max-entropy weights over finite alternatives in the
  large-distinction limit.
- Seeded Monte Carlo test (P5): fixed test-state family, N = 2^4…2^14, tolerance ±2σ.
- Named constraint: PBR/BCLM (1609.01558) experimental reality tests.

## 7. Relational Time from a Distinction Clock (H-TIME)

- Page–Wootters 1983 (PRD 27, 2885) + Marletto–Vedral 2016/2017 (ambiguity
  resolution) as imported machinery; the clock subsystem counts n distinctions.
- IMPORTED vs DERIVED boundary (red-team S-6): IMPORTED — the PW conditioning
  formalism (conditioning a global stationary state on clock readings) and the
  ambiguity resolution of Marletto–Vedral. DERIVED (this paper, conjecture-grade) —
  the finite-distinction clock construction (n distinctions) and its convergence
  behavior (H-TIME). The boundary is re-checked at P6 before the claim locks.
- CORPUS CONSTRAINT + COMPLICATION: Vedral 2022 (arXiv:2203.03065) shows the classical
  analogue exists — "evolution without evolution" is NOT quantum-specific. The quantum
  discriminator = incompatible quantities + ℏ (Del Santo–Gisin 2024, 2409.10601).
- H-TIME prediction: relational dynamics converges to Schrödinger evolution as n → ∞;
  discrete-time artifacts shrink with n (convergence diagnostics in P5).
- Note-1 seed (Euler/timeless math): time is not in the notation; it is added by
  iteration — the distinction clock is that iteration, made explicit.

## 8. Falsification Conditions (F1–F5)

- F1 (continuum): observable requiring an exact real at fixed finite resolution.
- F2 (ultrametricity): reproducible triple violating the strong triangle inequality.
- F3 (unitarity emergence): entropy production not scaling to zero with N.
- F4 (Born emergence): max-entropy weights deviating from Born beyond tolerance.
- F5 (relational time): no clock subsystem yields Schrödinger convergence.

## 9. Verification Plan (COMPUTATIONAL-VERIFICATION-1)

- H-UNIT/H-BORN: seeded Monte Carlo simulator, N-alternative entropy-Hessian flow
  (artifacts/verification/, stdlib-only, deterministic seed; reproducibility statement
  with runtime/seed/versions; VERIFY-FIX-RERUN-1 discipline — deposit the PASSING log).
- H-ULTRA: seeded construction + violation search over hierarchical clusterings.
- H-TIME: clock-subsystem convergence diagnostics.
- Golden values/edge cases for every formula before any prose asserts it
  (VERIFY-IN-CODE-1).

## 10. Practitioner Deliverables (PRACTITIONER-RELEVANCE-1)

1. Resolution-bounded quantum emulator: distinction count as the accuracy resource
   (spec-sheet deliverable).
2. JPCUB distinction budget: joules-per-solution as a function of distinctions made
   per answer — tie to QNFO.JPC.001.
3. Ultrametric QEC decoding: nearest-distinction decoding on the tree (QNFO.UF
   p-adic code classification).
4. Readout metrology: per-measurement distinction budget (RES.020 QND rule extended
   to an audit rule for readout chains).

## 11. Conclusion

- What is identity (finite-information premise), what is dictionary (β_p = ln p analog
  for the state space), what is conjecture (Hessian → unitarity). The paper lives or
  dies on the finite-N predictions (§8 F3–F5); underdetermination (UMP.010) means the
  ontology claim earns its keep ONLY there.
- **P6 obligation (red-team S-7/S-11, registered):** at P6 the paper MUST ship the
  RESTATED core claim — "uncountable precision is unphysical" (breadth vacuous,
  computable depth real — PROJECT-PLAN §9 re-mapping) — reconciling the frozen §2
  wording; the amendment log (PROJECT-PLAN §9) and this registration are the audit
  trail.
- **P3 obligation (red-team S-12, registered):** references.bib + citation-audit.md
  with per-entry live author verification (P3.AUTHOR-GATE-EVERY-ENTRY-1); anchor set
  enumerated in artifacts/external-search/evidence-2026-08-20.md §4–5.
- **P8 distribution obligations (red-team S-13, registered):** Zenodo source-complete
  deposit, R2 mirror qnfo-releases/2026/08/finite-distinction-quantum-mechanics/,
  D1/KG distribution_status=distributed, program_registry re-point
  (PUBLISH-CHECKLIST-PORTFOLIO-REPOINT-1).

---

**Section-to-gap map:** §2→G3, §3→G2/G3, §5→G1 (novel), §6→G1, §7→G4, §8→G2,
§10→G5. Premise-depth disclosure: L0/L1/L2/L3 table from PROJECT-PLAN §2 reproduced
in §2 of the paper; the UIA Q15 seed ("is the large-distinction limit itself
continuous?") is answered explicitly in §5 (UIA Q15 seed block; red-team H-2
remediation).
