---
modified: 2026-08-16T06:00:00Z
---

# RES.009 GAP-6 — T2: Prop Presentation of the Calculus (F2''-(i), first pass)

**Companion to:** `res009-gap6-t2-derivation.md` (v0.1) · `res009-gap6-t2-rigor-pass-2026-08-16.md` · `res009-gap6-t2-f-construction-2026-08-16.md`
**Author:** DeepChat (autonomous T2 cycle, 2026-08-16)
**Scope:** executes F2''-(i) — the finite, explicit presentation of the calculus of indications as a syntactic category, so that the interpretation functor F is defined by the universal property. Result of the first pass: a structural clarification that re-derives the F-construction result from the calculus's own signature.
**Status:** FIRST-PASS ANALYSIS (provisional; open points in §4).

---

## 1. What F2''-(i) demands

The F-construction note left two checkable items: (i) the prop presentation of the calculus (finite, explicit), and (iv) the Transposition ↔ hexagon check. This note addresses (i).

**Deliverable:** a presented symmetric monoidal theory ℒ whose morphisms are the calculus's expressions, with generators and relations, such that F: ℒ → C is defined by the universal property and the relations are checkable in any target C.

## 2. The calculus's actual signature: unary crossing + juxtaposition

In the calculus of indications (LoF), expressions are built from the mark by exactly two operations:

- **Juxtaposition** (binary): `a b` — two expressions side by side (Calling: `a a = a`).
- **Crossing** (UNARY): `(a)` — enclosing an expression in a boundary (Position: `(a) a = ` the unmarked state; double crossing `((a)) = a`).

Axioms: Calling (idempotence), Position (contradiction law), Transposition (the distributive law). **Crucially, crossing is a unary operation on expressions — it is not a binary morphism M⊗M → M⊗M.** The mark is drawn once; the crossing wraps an entire expression.

## 3. Main finding — the equational theory is the theory of Boolean algebras

**The equational theory of the primary algebra is the theory of Boolean algebras** [KNOWN, standard in the LoF literature; pin a specific citation in the rigor pass]. Under the standard translation — crossing ↦ negation, juxtaposition ↦ conjunction (reading the unmarked state as the identity/⊥ appropriately) — the theorems of the primary algebra are exactly the identities of Boolean algebra (commutativity, associativity, idempotence, double negation, De Morgan, distributivity all follow from the two initials).

**Consequence.** The syntactic category ℒ is the **Lawvere theory of Boolean algebras**: the algebraic theory with operations {0-ary ⊥ (the unmarked state), binary ∧ (juxtaposition), unary ¬ (crossing)} and the Boolean equations, finitely presented by the two LoF initials. ℒ is a symmetric monoidal (indeed cartesian-commutative) theory.

**Therefore the binary exchange is NOT in the calculus's signature.** ℒ contains no braiding and no binary morphism "exchange of two marks". Its morphisms are the Boolean-algebra operations and their composites. The derivation's σ_{M,M}: M⊗M → M⊗M is not the image of any syntactic crossing morphism — it is **added target structure**: the braiding of C together with the self-duality of M (T2 §3.1 reading: the crossing law as unit/counit pairing).

## 4. The syntactic explanation of the F-construction result

The F-note proved: F exists iff the target braiding is involutive. The prop presentation explains *why* this is unavoidable, at the level of the signature:

1. **Unary involution does not transfer to a binary braiding.** In ℒ, crossing is involutive (Position: ¬¬ = id on expressions). This is a unary identity. It does NOT imply σ² = id for any binary braiding σ_{M,M} in a compact closed target: the anyon/TL regime is the direct counterexample — σᵢ = A·I + A⁻¹·Uᵢ, σᵢ² = A²I + (1−A⁻⁴)Uᵢ ≠ I (p-adic-temperley-lieb-parameter 10.5281/zenodo.21208368 §1.1; p-adic-anyon-fusion-braiding 10.5281/zenodo.21208491). The unary→binary transfer is exactly the additional content the derivation would need — and it is not provided by the calculus.
2. **The identification "σ = image of Crossing under F" is an interpretive addition.** The derivation note's T1 identification (η = +1 ↔ Calling, η = −1 ↔ Crossing) pairs the *exchange phase* with the *mark's laws*. The prop reading makes precise what this does: it injects the binary exchange as an extra datum, alongside the unary crossing — and the involutivity of that extra datum is a condition on C, not a theorem of ℒ.
3. **Consistency with the F-construction note.** F exists exactly in symmetric targets (σ² = id automatic) or TL at A⁴ = 1 (δ = −2) — i.e., exactly when the ADDED braiding happens to be involutive. The signature-level statement: the calculus contributes the character structure (Boolean algebra = the two values) and the involutive-quotient syntax; the exchange, its involutivity, and the channel-count all live in the added categorical/physical structure.

## 5. Sharpened F (what the construction must actually be)

F: ℒ → C, with ℒ the Lawvere theory of Boolean algebras:

- the mark ↦ an object M carrying a **Boolean-algebra-object structure** in C: an idempotent commutative monoid m: M⊗M → M (Calling), unit (the unmarked state), and an involutive unary operation ¬_M: M → M (crossing) satisfying the Boolean equations;
- Calling ↦ idempotence of m / the symmetrizer reading (rigor-pass Claim B);
- crossing ↦ the involution ¬_M (unary), and — by the T2 identification — the self-duality data making M self-dual;
- the braiding σ_{M,M} is **not in the image of ℒ**; it is C-structure used by the physical reading (the exchange), whose involutivity is the F-existence condition (F-construction note).

**Open points (genuine, to be resolved in the next pass):**
- (a) Boolean-algebra objects are classically defined in cartesian settings; the correct notion in a non-cartesian compact closed category (commutative idempotent monoid + involutive antipode, with the distributivity encoded via the appropriate naturality) needs care and a precise definition.
- (b) The exact translation of Transposition (the distributive law) into the algebra-object axioms — expected to be the distributivity of the Boolean structure; must be verified equation-by-equation (ties into F2''-(iv), the hexagon/naturality check).
- (c) Faithfulness of F — whether the calculus embeds (no unintended identifications).

## 6. Falsifiability update (F2''-(i) status)

- **F2''-(i) — first pass COMPLETE at the theory level:** the presentation exists finitely (Lawvere theory of Boolean algebras: 2 operations + equations from the two initials). The genuinely open remainder is the categorical refinement (open points (a)–(c) above) and the Transposition verification (F2''-(iv)).
- **Decisive question, sharpened answer.** NOT ONLY does involutivity condition the interpretation (F-note): the binary exchange is not even in the calculus's language. The parsimony ledger, at this level of analysis: the mark calculus contributes the two-valued character structure and the involutive-quotient syntax; the exchange, its involutivity, and the channel-count (abelian-pair/parastatistics exclusion, DHR locality) are all added structure. This is the precise, signature-level form of the program's honest boundary.

## 7. References to pin before publication (P3.AUTHOR-GATE)

- Primary algebra = Boolean algebra: [KNOWN, standard] — pin a specific work in the rigor pass (candidates: the LoF literature expositions — Kauffman's knot-logic papers, Bricken's boundary logic; verify via Crossref).
- Lawvere theories / props: Lawvere 1963; Lack, "Composing PROPs", Theory Appl. Categ. 13 (2004) 147–163 (already queued in the F-note).
- Joyal–Street 1993 (already queued); Rowell–Stong–Wang 2009 (already queued).

## 8. Bottom line

The prop-presentation first pass delivers the structural clarification that completes the F-construction picture: **the calculus of indications is a Boolean-algebra theory — unary crossing plus juxtaposition — and the binary braiding σ is not syntactic; it is added target structure.** Involutivity cannot be derived from Calling + Crossing because the exchange is not in the language: this re-derives the F-construction result from the signature itself and fixes the program's honest boundary at the syntactic level. **Follow-up completed 2026-08-16:** F2''-(iv) — `res009-gap6-t2-transposition-check-2026-08-16.md` — shows Transposition (J2) requires the special Frobenius/classical structure (duplication + erasure) AND the involutive braiding quotient (hexagon alone insufficient), resolving open point (a) (Boolean-algebra objects = commutative special dagger Frobenius algebras + involutive NOT, Coecke–Duncan arXiv:0906.4725). Next T2 step: explicit FdHilb diagrammatic proof + faithfulness of F.
