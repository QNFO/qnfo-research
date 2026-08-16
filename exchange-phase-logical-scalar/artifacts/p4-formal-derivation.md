# P4 Formal Derivation — R = (e^{iπ})^{2s} in the Part VIII System

**WBS:** QNFO.RES.010 | **Phase:** P4 | **Date:** 2026-08-16 | **Branch:** res/paper/exchange-phase-logical-scalar
**Preceded by:** P3 citations (complete 2026-08-16, commit 75e9410) · P4 notebook sketch (2026-08-14, notebooks/p4-half-turn-monodromy.md)
**Companion gate:** PREMISE-DEPTH-1 (user so-what mandate; gate draft on RES.011/RES.010 branches) — every status label audited to its floor.

---

## 0. Target (F1, verbatim from PROJECT-PLAN §1.2)

> The re-entrant mark / Laws-of-Form calculus generates the exchange phase as a power of its half-turn:
> **R = (e^{iπ})^{2s} = e^{2πis} = (−1)^{2s}**, with the boson/fermion dichotomy the parity of 2s.
> Falsifiability F1: falsified if **no derivation exists within the traced differential cohesive linear type theory of 21908818 Part VIII (§36) without importing the relation as an axiom.**

Phrasing discipline (P4 red-team LEVEL-1): the primitive is the *re-entrant mark of the calculus of indications under linear discipline*, not bare self-reference — this scopes RES.010 against Ma & Zhang 2025.

---

## 1. Machinery — verified verbatim against the treatise body (D1 70a58cb3, 111,806 chars, pulled 2026-08-16)

| Ref | Content | Status (treatise's own label) |
|---|---|---|
| §8.3 | Compact closed category: every object A has dual A\*, evaluation/coevaluation; "In a compact closed category, the trace always exists" | [established — Joyal, Street & Verity 1996] |
| §34.1 | S¹ is the self-dual compact object; "the linear endomorphisms of the circle are the phase rotations"; type S¹ ⊸ S¹ = type of the re-entrant mark's transformations | [established — Girard 1987 / HoTT] |
| §34.2 | Trace operator Tr^U(f): A⊗U → B⊗U closes the loop on U; "re-entry = Tr^{S¹}(negation)" | trace [established — JSV 1996]; re-entry-as-trace [my conjecture] |
| §36.1 | π = Tr^{S¹}(id) — internalized scalar | [my conjecture] strong form; [established] in the analytic realization (FQ3 scoping 2026-08-12) |
| §36.2 | "These constants are theorems of the type system"; falsifiability: can the system derive e^{iπ} = −1 without importing ℝ and exp as external axioms? | [my conjecture]; verification = Appendix D proof assistant |
| §12.1 | e^{iπ} = −1 — "the exponential of the half-turn is the negation"; half-turn carries marked ↔ unmarked | [established — Euler's formula] |
| RES.009 T1/T2 | Exchange map σ_{M,M} = η·id for the self-dual mark; ribbon identity η = θ_M; symmetric braiding → η = ±1; η = −1 ↔ Crossing, η = +1 ↔ Calling | [established — RES.009 construction] |

## 2. The derivation

**Step 1 — the exchange map in the compact closed structure.** [established — RES.009 T1/T2]
σ_{M,M}: M⊗M → M⊗M is the braiding of the self-dual mark. In a symmetric braided category σ² = id, so σ has eigenvalues ±1 with idempotent projectors P_sym = ½(1+σ), P_antisym = ½(1−σ).

**Step 2 — the half-turn as the basic monodromy.** [established — treatise §12.1]
The half-turn of the circle carries marked to unmarked: e^{iπ} = −1 = Crossing. This is the single-mark monodromy under rotation by π.

**Step 3 — the trace operator internalizes re-entry.** [trace established — §34.2; identification my conjecture]
In the traced structure (§8.3/§34.2), the re-entrant form f = f̄ is the trace of the negation on S¹: re-entry = Tr^{S¹}(negation). The trace closes the loop that feedback (re-entry) describes.

**Step 4 — exchange phase as monodromy power of the half-turn.** [arithmetic established; identification MAP — model]
The exchange of two particles is a loop in their configuration space (Leinaas–Myrheim 1977 [established]); the phase acquired is that loop's monodromy. RES.010's reading: the exchange monodromy is the (2s)-fold iteration of the mark's half-turn:
R = (e^{iπ})^{2s} = e^{2πis} = (−1)^{2s}.
The arithmetic identity is [established]; the identification of exchange monodromy with a *power of the mark's half-turn* is [MAP — model].

**Step 5 — parity of 2s → the dichotomy.** [established arithmetic + RES.009]
s ∈ ℤ → 2s even → R = +1 → Bose–Einstein (symmetric; Calling). s ∈ ℤ+½ → 2s odd → R = −1 → Fermi–Dirac (antisymmetric; Crossing). The dichotomy *is* the parity of 2s.

**Step 6 — dimension quantization: B₂ vs Z₂.** [established — RES.009 §3]
- d ≥ 3: π₁(C₂(ℝ^d)) = ℤ₂, involutive braiding forces 2s ∈ ℤ → R = ±1.
- d = 2: π₁ = B₂ ≅ ℤ, s continuous → anyon phases e^{2πis} (Leinaas–Myrheim [established]).
- The (e^{iπ})^{2s} form is well-defined for arbitrary s; the (−1)^{2s} form requires 2s ∈ ℤ (scope note, audit correction 7a5717f).

**Step 7 — the Part VIII statement.** [my conjecture — F1 target]
The composite (e^{iπ})^{2s} is expressible in the type system as the (2s)-fold composition of the half-turn endomorphism of S¹ — an element of End(S¹), the phase rotations [established §34.1] — evaluated via the trace/scalar structure (§34.2/§36.1). The claim that the system *computes* the scalar without importing ℝ and exp as external axioms is [my conjecture]; §36.2 names Appendix D (the proof assistant) as the verification path, and that is F1's concrete check.

## 3. Status ladder (PREMISE-DEPTH-1 audit)

| Component | Status |
|---|---|
| Exchange map σ_{M,M}; projectors P_sym/P_antisym | [established — RES.009 T1/T2] |
| Half-turn e^{iπ} = −1; marked↔unmarked | [established — treatise §12.1] |
| η = −1 ↔ Crossing; η = +1 ↔ Calling | [established — RES.009 T2] |
| Trace operator Tr^U; compact closed structure | [established — JSV 1996] |
| S¹ self-dual; End(S¹) = phase rotations | [established — §34.1] |
| (e^{iπ})^{2s} = (−1)^{2s} = ±1 for 2s ∈ ℤ | [established — elementary] |
| Exchange monodromy = (2s)-fold half-turn | [MAP — model of the re-entrant phase] |
| re-entry = Tr^{S¹}(negation) | [my conjecture] |
| π = Tr^{S¹}(id) as logical scalar | [my conjecture]; [established] in analytic realization (FQ3) |
| e/π/R scalar-family unification | [my conjecture] |
| Axiom-free derivation in Part VIII syntax | [my conjecture — F1, Appendix D path] |

**Depth floor (where the premises end):**
1. **The act of distinction** — the mark as primitive act (LoF void; unanalyzable by design).
2. **The categorical machinery** — compact closed/traced structure with self-dual S¹ [established — JSV/HoTT]: imported, not derived.
3. **The analytic realization** — the trace computes π only in the analytic model (§36.1 FQ3 scoping); the bare traced structure is model-dependent (relation/dimension/Euler-characteristic). The treatise concedes this.
4. **Euler's formula** — e^{iπ} = −1 is [established analysis]; the *purely logical* derivation of e and π is exactly the open F1/Appendix D claim.
5. **Physics inputs** — spin values s ∈ {0, ½, 1, …} and exchange-as-rotation (geometric-phase line), 3+1D topology.
6. **The MAP** — exchange monodromy = (2s)-fold half-turn.

**Honest verdict:** the theorem is as deep as (2)+(3)+(4) on the scalar machinery and (5)+(6) on the physics. The genuinely new, honest content is (a) the **composite monodromy-power form** (e^{iπ})^{2s} (absent from RES.009's η = ±1 and from the QFT derivation, which states R = e^{2πis} directly), (b) its placement in the e/π/R scalar family, (c) the parity-of-2s reading. This is a *minimal-premise re-description with a real engine* — not an axiom-free derivation of the constants (that remains F1/Appendix D, honestly open).

## 4. Falsifiability (F1–F3)

- **F1 (formal):** if the Part VIII system cannot derive R = (e^{iπ})^{2s} as a monodromy-power scalar without importing the relation as an axiom → the logical-derivation claim fails. Status: derivation constructed from established components + MAP + conjecture labels; the residual open step is the Appendix D computation (e, π as type-system theorems) — registered, not claimed.
- **F2 (empirical, inherited RES.009):** a stable local relativistic 3+1D excitation with η ≠ e^{2πis} disconfirms the invariant. Evasion class: Ahluwalia–Lee (P3 citation audit); measurement protocol: Kirchner et al. 2025 anyonic spectroscopy.
- **F3 (scope):** arithmetic [established]; identification [MAP]; derivation [my conjecture]. (−1)^{2s} requires 2s ∈ ℤ; general anyon form is e^{2πis}.

## 5. B₂ vs Z₂ — the exchange group statement

The braid group B₂ ≅ ℤ (d=2, anyons) vs the symmetric group ℤ₂ (d≥3, bosons/fermions): the (e^{iπ})^{2s} monodromy-power form is the single formula that covers both — for 2s ∈ ℤ it degenerates to ±1 (involutive braiding), for continuous s it gives e^{2πis} (anyon). This is the missing link the P4 notebook calibration names: *"the (e^{iπ})^{2s} composite reading as the missing link between RES.009 T2's η = ±1 and the anyon generalization."*

## 6. Calibration

- **Success criterion met (minimum viable finding):** the composite monodromy-power reading is constructed within the Part VIII machinery with honest [established]/[MAP]/[my conjecture] labels; the model-theoretic construction in the §8.3 compact closed structure matches the ribbon identity η = θ_M = e^{2πis} for the self-dual mark (RES.009 GAP-6 T2 result, live-verified 2026-08-15).
- **Full success criterion (formal derivation in the Part VIII syntax) — PARTIALLY DISCHARGED:** the composite is expressible in End(S¹) via the trace structure; the axiom-free computation of the constants remains F1/Appendix D, registered in the continuity registry (FQ1).

## 7. Red-team notes (direct parent audit, 2026-08-16)

- LEVEL-1 (Ma & Zhang 2025): delta preserved — primitive is the mark/LoF calculus under linear discipline; power structure for arbitrary s; e/π/R unification absent in their Z₂-only result. PASS.
- LEVEL-2 (Kauffman 1301.6214, P3 support-4): Kauffman derives fermion *algebra* from the mark (Clifford/quaternion); RES.010 derives the exchange-phase *invariant* as monodromy power — algebra-vs-invariant distinction maintained. PASS.
- Accuracy: every treatise citation in this file verified against the pulled body (chars 22808/89113/92034/34580 quoted above). PASS.
- No new claims beyond the status ladder; all labels carry their evidence. PASS.
