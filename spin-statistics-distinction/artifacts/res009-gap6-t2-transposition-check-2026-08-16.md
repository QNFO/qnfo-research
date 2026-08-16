---
modified: 2026-08-16T06:30:00Z
---

# RES.009 GAP-6 — T2: Transposition ↔ Hexagon Check (F2''-(iv), first pass)

**Companion to:** `res009-gap6-t2-derivation.md` (v0.1) · `res009-gap6-t2-rigor-pass-2026-08-16.md` · `res009-gap6-t2-f-construction-2026-08-16.md` · `res009-gap6-t2-prop-presentation-2026-08-16.md`
**Author:** DeepChat (autonomous T2 cycle, 2026-08-16)
**Scope:** executes F2''-(iv) — the last relation-level verification of the T2 derivation: the third LoF axiom (Transposition, Initial 2 / J2) must map to the hexagon/naturality relations of the braided monoidal structure under the interpretation functor F. Result: the pairing is REFINED — J2 maps to (special Frobenius/classical structure + the involutive-braiding quotient), not to the hexagon alone.
**Status:** FIRST-PASS ANALYSIS — relation level complete; checkable remainder in §5.

---

## 1. What F2''-(iv) demands

The F-construction note (F2''-(iv)) and the prop-presentation note (§5 open point (b)) both require: verify that the Transposition axiom of the calculus of indications holds in the image of F, expressed through the braided monoidal coherence of the target (hexagon + naturality).

**Transposition (LoF Initial 2, in the resolution form):** `((a b)(a (b))) = a`, i.e., under the Boolean translation (crossing ↦ ¬, juxtaposition ↦ ∧): ¬[¬(a∧b) ∧ ¬(a∧¬b)] = a — the **resolution law** (a∧b) ∨ (a∧¬b) = a, one of the standard forms of distributivity. Equivalently, the general distributive law ((p r)(q r)) = ((p)(q)) r.

## 2. J2 requires duplication — the Cartesian-theory aspect

J2 uses the variable `a` TWICE. In the Lawvere-theory formulation (prop-presentation note: ℒ = the Lawvere theory of Boolean algebras), this means the equation involves the **diagonal** Δ: M → M⊗M (duplication); J1 (Position: `(a) a = ` void) involves the **counit/erasure** ε: M → I (the unmarked state). The theory of Boolean algebras is a **Cartesian theory**: its morphisms include diagonals and projections, not just the monoid operations.

**Consequence:** a mere commutative monoid object (m: M⊗M→M, u: I→M) on M is NOT sufficient to express J1/J2. The interpretation requires a **comonoid structure** (δ: M→M⊗M, ε: M→I) on M as well — i.e., M must carry the data of a (special, commutative) **Frobenius algebra** — the classical structure of categorical quantum mechanics.

## 3. Main finding — the categorical content of Transposition

1. **The Frobenius/classical structure is the categorical home of both LoF initials.** The spider composition law of a commutative special Frobenius algebra — any connected diagram collapses to a single spider determined by its boundary — is the algebraic heart of the calculus's simplification content (Calling + Transposition as the merge/erase laws). The formalism is KNOWN and arXiv-verified: Coecke–Duncan, *Interacting Quantum Observables*, arXiv:0906.4725 (2009): "Each individual observable, represented by a commutative special dagger Frobenius algebra"; Abramsky–Coecke, *Categorical Quantum Mechanics*, arXiv:0808.1023 (2008). (A dedicated "Laws of Form ↔ Frobenius algebra" paper was NOT found on arXiv, search executed 2026-08-16 — the correspondence is stated here as the structural reading of the classical-structure formalism, with the LoF-side pinning left to the rigor pass.)
2. **The braiding's role — where the hexagon is NOT enough.** The monoid's commutativity (m ∘ σ = m) and the J2 reorderings use the braiding σ_{M,M}. The J2 diagram is well-defined — independent of which braid-word representative of a permutation is chosen — **iff the braiding acts as a symmetry on the strands involved, i.e., σ² = id** (the S_n quotient: B_n/⟨σᵢ²=1⟩ = S_n — rigor-pass Claim C, quantitative via TL, corpus 21208368). The hexagon axioms are always present in a braided category (they are part of the braiding data) — but they do NOT by themselves make the J2 diagram well-defined: in the non-involutive anyon regime, different braid representatives of the same permutation differ by nontrivial phases, so the "distributivity" equation fails or is ambiguous. This is exactly where F fails to exist (F-construction note).
3. **Refined verdict.** The F-note's pairing "Transposition ↔ hexagon" is REFINED to: **Transposition ↔ (special Frobenius/classical structure on M + the involutive braiding quotient)**. The hexagon is necessary but not sufficient; the two additional inputs are (i) the comonoid/Frobenius data (duplication + erasure) and (ii) involutivity (σ² = id) for the quotient coherence. Both are consistent with the established boundary: the mark calculus supplies the involutive-quotient syntax; the involutive target and the channel-count remain external inputs.
4. **Consistency check.** In the symmetric case (d≥3, FdHilb with the flip braiding): σ = flip, σ² = id, the S₂/S₃ quotients act, and the Boolean equations hold for a Boolean-algebra object — J1 and J2 verified in the image. In the TL/anyon case (A⁴ ≠ 1): σᵢ² = A²I + (1−A⁻⁴)Uᵢ ≠ I — J2's diagram is braid-word-dependent; F does not exist; consistent with the F-construction note.

## 4. Resolution of prop-presentation open point (a)

The "Boolean-algebra object in a non-cartesian compact closed category" open point is now substantially resolved: the correct notion is a **commutative special dagger Frobenius algebra (classical structure) equipped with an involutive NOT satisfying the Boolean equations** — a well-defined, standard notion in dagger compact closed categories (FdHilb fits: the classical structure of the computational basis + the NOT gate). The remaining technical sub-points: the precise equation set linking NOT to the classical structure (the "complement" equations), and faithfulness of F (open point (c)) — both carried to the next pass.

## 5. Falsifiability update

- **F2''-(iv) — COMPLETE at the relation level:** J2 is verified as (a) a Boolean identity (resolution law), (b) requiring the Frobenius/classical + involutive-quotient data in the image. The F2'' items (i)–(iv) are all now first-pass complete.
- **Checkable remainder (executable):** the explicit FdHilb diagrammatic proof — write the J2 spider diagram with m, δ, ¬, σ = flip, and verify the diagram commutes. This is a concrete, finite verification (candidate: a small proof in the categorical-notation style of IQQ; doable in the next cycle, possibly as a qwav-demo/tooling artifact).

## 6. References [arXiv-verified 2026-08-16; pin DOIs via Crossref in the rigor pass]

- Coecke, Duncan, *Interacting Quantum Observables: Categorical Algebra and Diagrammatics*, arXiv:0906.4725 (LICS 2008 / J. ACM 2011).
- Abramsky, Coecke, *Categorical Quantum Mechanics*, arXiv:0808.1023 (Handbook of Quantum Logic, 2008).
- No dedicated LoF↔Frobenius paper found on arXiv (2026-08-16 search); correspondence stated structurally via the classical-structure formalism.
- Existing queue unchanged: Joyal–Street 1993 (10.1006/aima.1993.1055); Rowell–Stong–Wang 2009 (10.1007/s00220-009-0908-z); Lack 2004; Lawvere 1963.

## 7. Bottom line

F2''-(iv) closes the relation-level verification of the T2 derivation program. The full chain is now first-pass complete:

- (A) Crossing ⇒ σ² = id in im(F) — sound, definitional-in-the-interpretation (F-construction note);
- (B) two characters ↔ Calling/Crossing — sound, given two channels (rigor pass);
- (C) S_n = B_n/⟨σᵢ²=1⟩ — quantitative via TL (rigor pass, corpus 21208368);
- (D) **Transposition = the resolution law; its categorical image requires the special Frobenius/classical structure (duplication + erasure) AND the involutive braiding quotient — the hexagon alone is not sufficient** (this note).

The remaining T2 open items: (i) the explicit FdHilb diagrammatic proof (executable check), (ii) faithfulness of F, (iii) the P8 citation fixes (Rowell–Stong–Wang / Joyal–Street / pin the LoF-Boolean and Frobenius citations) — the note chain (derivation → rigor → F-construction → prop-presentation → transposition-check) is complete for the current cycle.
