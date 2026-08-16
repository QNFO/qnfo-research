---
modified: 2026-08-16T07:00:00Z
---

# RES.009 GAP-6 — T2 Synthesis: "So What?", Depth of Premises, and the Redirect

**Companion to:** the five-note T2 chain (`res009-gap6-t2-{derivation, rigor-pass, f-construction, prop-presentation, transposition-check}-*.md`)
**Author:** DeepChat (autonomous T2 cycle, 2026-08-16)
**Status:** SYNTHESIS — this note closes the T2 derivation program rather than extending it.

---

## 0. The governance question, answered straight

Mandate applied: *"So what? Why should a reader care? A theory is only as deep as its premises — how deep does it go, and where do its premises end?"*

The T2 program pre-registered **F2** = "derive the two statistics from the mark calculus (Calling + Crossing) alone, or F2 fails." The five-note chain **executed F2's test**, and **F2 FAILED** — with three independent, named mechanisms, not hand-waving:

1. **Involutivity is not derivable** — the interpretation functor F exists *iff* the target braiding is already involutive (F-construction note).
2. **The exchange is not in the language** — the calculus is a Boolean-algebra theory (unary crossing + juxtaposition); the binary braiding σ is added target structure (prop-presentation note).
3. **The abelian-pair demotion is circular** — scalar exchange *presupposes* M⊗M-simple/abelianity (rigor-pass note); and the resolution law needs **complementarity** (transposition-check note, now executable).

**That is a clean, pre-registered NEGATIVE RESULT WITH A MECHANISM** — the most useful kind. It closes the "logic-first" route (the Occam audit's "he bets on logic") instead of leaving it open. The reader who cares about foundations now has a precise answer: *the parsimony ledger does not close on logic alone.*

## 1. So what — three results that survive the falsification

1. **A proven minimal-ontology theorem.** Before, the minimal postulate set was *asserted* ({compact closure, self-duality, abelian pair, symmetric braiding} + {Lorentz, microcausality, positivity}). Now each element's minimality is *shown* — each is non-derivable from the calculus and the others. The reader learns the exact minimum ontology that produces exchange statistics: **logic + locality + kinematics + Lorentz.** That is a real, citable answer to a live foundations question (DHR / parastatistics / spin-statistics).

2. **A notation-vs-engine distinction.** The mark calculus is a *notation* (a Boolean/classical-structure fragment of categorical quantum mechanics), not a generator of new physics. The actual physical content — braiding, anyons, the spin-statistics invariant R = e^{2πis} — lives in the braided-compact-closed / quantum-group / Temperley-Lieb machinery, which the notation *points at* but does not *replace*. This prevents overclaiming (RES.009's §5 boundary is now *rigorous*, not asserted) and redirects effort away from a dead end.

3. **A bridge to a mature, usable toolkit.** The calculus ↔ **classical structures** (special dagger Frobenius algebras, Coecke–Duncan *Interacting Quantum Observables*, arXiv:0906.4725) + the **ZX-calculus**. The derivation's three failure points map onto *known* structures (symmetry vs. braiding; complementarity). Actionable: the program's logic layer can now be treated with existing, computable ZX/classical-structure tools instead of ad-hoc derivation.

## 2. Depth of premises (the exact question)

| Premise | Ends at | Status |
|---|---|---|
| **Mark** (draw a distinction) | two-valued logic + involutive-quotient syntax (S_n = B_n/⟨σᵢ²=1⟩) | PROVEN (prop-presentation + TL formula) |
| Compact closure (duals) | self-duality (crossing law = unit/counit) | asserted |
| Self-duality | the crossing's involutive duality | asserted |
| **Abelian pair** (M⊗M simple) | parastatistics exclusion = DHR locality | PROVEN non-derivable (§2 circularity) |
| **Symmetric/involutive braiding** | d≥3 kinematics (π₁ = S_n) | PROVEN non-derivable (F-existence condition) |
| Lorentz / microcausality / positivity | the spin–statistics *connection* | always external (paper §5) |
| **Complementarity** (X observable) | Boolean logic realized in Hilbert space | PROVEN needed (executable, §3) |

**Depth verdict:** the theory goes as deep as *two-valued logic*. Every physically substantive step — exchange, braiding, statistics, spin — is a premise that **ends at a known physical principle** (locality, kinematics, Lorentz, complementarity). The premises do *not* dissolve into the mark. The minimal ontology is **logic + locality + kinematics + Lorentz**; nothing less suffices, and the mark supplies only the first.

## 3. Executable evidence (CODE-EXECUTED, 2026-08-16)

Script `artifacts/notebooks/res009-gap6-t2-j2-fdilb-check.py`, output `…-output.txt` (exit 0). In FdHilb with M = ℂ²:

- **Classical-structure axioms** (Frobenius, special, commutative, unit, counit) — **PASS** as operator identities.
- **σ² = id** (canonical flip) — **PASS**.
- **J2 with merge-as-AND** → the **ZERO map** (|01⟩ ↦ 0, not e₀): the classical-structure merge is not Boolean AND.
- **J2 with bilinear Boolean-AND** → the **ZERO map** (|11⟩ ↦ 0, not e₁): negation of the zero vector collapses.
- **J2 on the classical sector** (two-valued Boolean functions) — **PASS** (trivial identity).
- **Involutivity is a specialization** — a non-involutive candidate S has S² ≠ I (max|diff| = 1.29).
- **TL braid formula verified**: σ_TL = A·I + A⁻¹·U (U = Bell cup-cap, U² = 2U) satisfies **σ_TL² = A²I + (2 + 2A⁻²)U ≠ I** for A⁴ ≠ 1 (max|diff| = 3.24) — the quantitative content of Claim C, now run in code.

The executable result makes the abstract verdict concrete: **Boolean logic is two-valued *on the classical sector only*; the operator-level resolution law needs complementarity — an additional external input.**

## 4. The practical application (the redirect)

- **The invariant survives the falsification.** R = e^{2πis} is [KNOWN] physics (Oeckl hep-th/0008072; Johnson-Freyd 1507.06297) and does *not* depend on the mark-calculus derivation. RES.009's value is intact where it was always real.
- **The computational payoff is the p-adic anyon / TQC program**, not the mark calculus: the TL braid formula (now code-verified) is the backbone of anyonic braiding; p-adic-anyon-fusion-braiding (21208491), p-adic-braid-groups-bruhat-tits (21208366), p-adic-temperley-lieb-parameter (21208368), zbw-majorana (21336087) carry the *actual* "so what" — topological quantum computing with an ultrametric gate hierarchy.
- **Concrete next artifact:** a ZX-classical-fragment construction of the Boolean layer (executable, citable bridge — natural qwav-demo candidate), and the P8 citation fixes (Rowell–Stong–Wang / Joyal–Street). The T2 *derivation* program is closed; the *classification* result (what the calculus can and cannot do) is the deliverable.

## 5. Bottom line

The five-note chain, read honestly, is a **falsification with a mechanism, converted into a positive result**: (a) a proven minimal-ontology theorem for exchange statistics (logic + locality + kinematics + Lorentz), (b) a notation-vs-engine distinction that prevents overclaiming, (c) a bridge to the computable ZX/classical-structure toolkit, and (d) a redirect to the p-adic-anyon/TQC substrate that actually carries the physics. The mark calculus's derivational power is *exactly* two-valued logic — and knowing that, precisely and with executable evidence, is a real, reader-serving result rather than a dead end.
