---
modified: 2026-08-16T05:20:00Z
---

# RES.009 GAP-6 — T2 Rigor Pass (companion to res009-gap6-t2-derivation.md v0.1)

**Companion to:** `res009-gap6-t2-derivation.md` (first-pass draft, 2026-08-15)
**Author:** DeepChat (autonomous DD cycle, 2026-08-16)
**Scope:** addresses due-diligence findings HARD-1/2/3 + SOFT-3 from `artifacts/res009-gap6-t2-dd-evidence-2026-08-16.md` (commit bfeaca9); performs the note's stated next step — category-theoretic rigor pass + verification against UMP-domain braid tooling.
**Status:** RIGOR-PASS ANALYSIS (not yet [DERIVATION] grade; the F-construction remains open — see §5).

---

## 0. What the due-diligence cycle found

| # | Severity | Finding | Status here |
|---|---|---|---|
| 1 | HARD | §2 "abelian-pair demoted from axiom to theorem" is circular: Schur per summand gives ⊕λᵢ·id, not a scalar; uniformity imports d_X=1 (the abelian-pair postulate itself); physical M⊗M has two channels (Sym²=+1, Λ²=−1); counterexample V⊗V in Rep(U_q(sl₂)); F2 fails as written | Resolved below (§1–§2) |
| 2 | HARD | T2-notebook citation "Bruillard 10.1007/s00220-009-0908-z" = Rowell–Stong–Wang, *On Classification of Modular Tensor Categories*, CMP (2009) — name/DOI mismatch | Citation fixes (§4) |
| 3 | HARD (infra) | qnfo-memory-mcp Worker 1101: base search_papers all requests; enriched at limit≥20 | Infrastructure item [QNFO.RES.INFRA] — not T2 content |
| 4–6 | SOFT | D1 identifier_type anomalies; r2_key bucket drift; bare "Bruillard" in draft | Data items [QNFO.RES.DATA]; §4 |

---

## 1. The corrected simplicity statement

**Lemma 1 (TRUE, per-channel).** Let M be simple in a semisimple ribbon tensor category C, with M⊗M = ⊕ᵢ Sᵢ semisimple. Then the braiding component σ_{M,M} acts on each simple summand by a scalar:
σ_{M,M} = ⊕ᵢ λᵢ · id_{Sᵢ}, λᵢ ∈ ℂ×.
This is Schur's lemma applied per summand (σ is a natural transformation commuting with End(M⊗M)). **It is NOT a single scalar in general.**

**Lemma 2 (FALSE as stated in the draft).** "M simple ⇒ σ_{M,M} = λ·id" is false.
*Counterexample (anyon regime):* V = the 2-dimensional simple object of Rep(U_q(sl₂)), q generic or a root of unity. Fusion: V⊗V = 1 ⊕ V₃ (trivial + 3-dimensional simple). The R-matrix acts by a phase on the trivial summand and non-scalarly (two distinct eigenvalues) on V₃; σ² ≠ id for q generic. Corpus: p-adic-anyon-fusion-braiding 10.5281/zenodo.21208491 (chain B_n → TL_n → U_q(sl₂)-modules → anyons; R-matrices §5; Fibonacci-anyon example p=5, k=3). Standard refs [KNOWN, also cited by 21208491]: Bakalov–Kirillov, *Lectures on Tensor Categories and Modular Functors* (2001); Kassel, *Quantum Groups* (1995); Wang, *Topological Quantum Computation* (2010).
*Elementary version:* the 2-dimensional irrep of S₃ satisfies σᵢ² = 1 on every pair yet is NOT 1-dimensional — pair-involutivity alone does not imply character-ness (parastatistics are not excluded by σ²=id).

**Lemma 3 (TRUE, the sound form).** σ_{M,M} is scalar ⟺ M⊗M is simple (then End(M⊗M) ≅ ℂ). In particular, if M is abelian/invertible (quantum dimension d_M = 1), then M⊗M is simple and the ribbon identity gives σ_{M,M} = θ_M·id (T2 notebook §2: θ_X = quantum-trace(c_{X,X})/d_X, abelian ⇒ θ_X = c_{X,X} = R_{XX} = e^{2πis}). **SOUND — but it presupposes abelianity (d_M = 1), which is exactly the abelian-pair postulate.**

**Diagnosis of the draft's §2 "Consequence".** The implication is inverted: scalar exchange FOLLOWS from M⊗M-simplicity / abelianity; it does not DELIVER it. The uniformity step (λᵢ = λⱼ) imports d_X = 1 via the T2 ribbon identity, so the abelian-pair postulate is smuggled back in precisely where the draft claims to have demoted it. **DD HARD-1 stands: the abelian-pair postulate is not derived from Calling + Crossing alone.**

---

## 2. What IS derivable from Calling + Crossing alone

**Claim A (SOUND).** In the image of the monoidal functor F (free re-entrant calculus → C; F to be constructed, see §5), σ² = id. Proof: Crossing is the order-2 law; F functorial ⇒ F(c)² = F(c²) = F(id) = id. Hence, per simple summand, λᵢ ∈ {+1, −1}.

**Claim B (SOUND).** σ² = id ⇒ the two idempotent projectors P± = (id ± σ)/2 satisfy P±² = P± (Calling's idempotence law P² = P) and P⁺P⁻ = 0. The two eigenvalues +1 (trivial S_n character, Calling) and −1 (sign character, Crossing) are realized on the two sectors. This is the categorical statement that Calling and Crossing ARE the two 1-dimensional characters of the involutive quotient.

**Claim C (CORPUS-VERIFIED, quantitative).** In TL_n(δ) with the braid embedding σᵢ = A·I + A⁻¹·Uᵢ (Uᵢ² = δUᵢ, δ = −A²−A⁻²):
σᵢ² = A²·I + (1 − A⁻⁴)·Uᵢ ≠ I in general.
Imposing σᵢ² = I (the Crossing quotient) forces Uᵢ to act as a scalar — i.e., the representation collapses to a character — and the quotient is B_n/⟨σᵢ²=1⟩ = S_n (Artin presentation). The note's slogan "3D permutation-like because S_n = B_n mod Crossing" is thereby made quantitative. Source: p-adic-temperley-lieb-parameter 10.5281/zenodo.21208368, §1.1 (fetched live 2026-08-16).

**Boundary (unchanged by the derivation).** Without the involutive quotient, σ² ≠ id: that is the d=2 anyon regime (B_n), realized in-corpus by p-adic-anyon-fusion-braiding 21208491 and p-adic-braid-groups-bruhat-tits 21208366. Which quotient is physical is a kinematical input (π₁ of the configuration space: S_N for d≥3, B_N for d=2 — configuration-space-topology 10.5281/zenodo.21957291, R = ±1 iff π₁ = S_N). The mark calculus supplies the *selection* of the involutive quotient (Crossing), not the geometry of why d≥3 selects it.

**Sharpest statement of the remaining gap.** Even Claim A + Claim B do NOT exclude parastatistics: S_n has higher-dimensional irreps satisfying σᵢ² = 1 on every generator (e.g., the 2-dim irrep of S₃). Upgrading the exchange representation of S_n on N marks from a general rep to a 1-dimensional character IS the abelian-pair postulate — the categorical avatar of excluding parastatistics, supplied in AQFT by locality (DHR 1971/1974; Greenberg–Messiah 1965 — [KNOWN], per the program's T1/T2 finding 2026-08-14). **This is the honest content of F2: it fails as written.**

---

## 3. The honest postulate set (unchanged by the draft)

{compact closure, self-duality, **abelian pair (M⊗M simple — parastatistics exclusion)**, (symmetric braiding OR Crossing-derived involutivity)} + {Lorentz, microcausality, positive energy} for the spin–statistics *connection* (paper §5 boundary; Johnson-Freyd 1507.06297 topological Spin-Statistics Theorem; Oeckl hep-th/0008072).

**Falsifiable claim that DOES pass (F2').** Given exactly two exchange channels for M⊗M (i.e., under the abelian-pair input), the statistics are the two 1-dimensional characters of S_n, identified with Calling (+1, trivial) and Crossing (−1, sign); and in the image of F the pair exchange is involutive. F2' is checkable: (i) construct F; (ii) verify σ²=id in im(F); (iii) verify the character identification; (iv) declare the channel-count input as the single surviving postulate and tie it to DHR locality. The derivation derives the statistics' *values* and their *Calling/Crossing identification* — it does not derive channel-count (parastatistics exclusion) from the primitive alone.

---

## 4. Citation fixes (feed [QNFO.RES.009.P8], next citation-audit newversion)

1. **Bruillard 10.1007/s00220-009-0908-z → Rowell, Stong, Wang, "On Classification of Modular Tensor Categories", Commun. Math. Phys. 292 (2009) 343–389** — Crossref-verified 2026-08-16 (title/author/year/container). This is the correct content support (classification of modular tensor categories backs the abelian/ribbon statements). If a Bruillard work is intended instead, pin the exact work (e.g., Bruillard's premodular-categories classification, J. Algebra) with its own DOI — verify before any publish.
2. **Add Joyal–Street, "Braided Tensor Categories", Adv. Math. 102 (1993) 20–78, DOI 10.1006/aima.1993.1055** — the RES.007-corrected citation for ribbon-category background (published v1.4 T2 notebook cites the [KNOWN] trio without it).
3. The draft note's bare "Bruillard" must carry the corrected DOI after 1.
4. Published v1.4 is READ-ONLY (post-publication gate): these fixes go into the next newversion, not into the live record.

---

## 5. What remains open (draft §5 items, re-ordered by criticality)

1. **F must be constructed explicitly** (free re-entrant calculus → compact closed category). No corpus record constructs it; this is now THE critical path for the derivation program. The draft's §5 item 2.
   **First-pass result (2026-08-16, companion `res009-gap6-t2-f-construction-2026-08-16.md`):** F exists **iff** the target braiding is involutive — the Crossing relation (c² = id) must hold in the image by the universal property of the presented prop. The free braided compact closed category on the mark has non-involutive braidings (B_n; TL: σᵢ² = A²I+(1−A⁻⁴)Uᵢ ≠ I, corpus 21208368), so it does not admit F. F exists exactly in symmetric targets (σ² = id automatic — the d≥3 regime, CST 21957291) or TL at A⁴=1 (δ=−2). **Corollary: involutivity conditions the interpretation rather than being derived by it — Claim A is sound but definitional-in-the-interpretation.** The draft's §0 decisive question therefore answers NO with a precise mechanism; the selection of the involutive quotient is the external kinematical input. Next: prop presentation of the calculus + Transposition/hexagon check (F2'').
2. **Definition/semantics of "simple object" and the physical single-particle Hilbert space as such an M** (draft §5 item 1) — dependent on the category semantics, to be fixed in the same rigor cycle as F.
3. **Uniformity across identical particles** — RESTATED: not the ribbon-identity uniformity (which presupposes d_X=1) but the channel-count postulate; tie to DHR locality.
4. **Spin–statistics connection** (which eigenvalue ↔ which spin) — remains external, per paper §5; unchanged by this pass (correctly).

---

## 6. Verification against UMP-domain tooling (this cycle, live)

| Tooling | DOI | Role in this pass | Verified |
|---|---|---|---|
| p-adic-temperley-lieb-parameter | 10.5281/zenodo.21208368 | σᵢ = A·I+A⁻¹Uᵢ; σᵢ² = A²I+(1−A⁻⁴)Uᵢ ≠ I; involutive quotient = S_n (Claim C) | D1 body fetch 2026-08-16 ✓ |
| p-adic-anyon-fusion-braiding | 10.5281/zenodo.21208491 | Anyon regime: non-involutive σ; V⊗V non-scalar; R-matrices; q = ζ_{2p^k} (counterexample context) | D1 body fetch 2026-08-16 ✓ |
| p-adic-braid-groups-bruhat-tits | 10.5281/zenodo.21208366 | B_n(Q_p) satisfies braid relations; discrete braiding | KG/D1 ✓ |
| zbw-majorana-tqc-p4-zbw-anyon-braiding | 10.5281/zenodo.21336087 | ZBW generates B_n; TQC relevance | KG/D1 ✓ |
| configuration-space-topology | 10.5281/zenodo.21957291 | π₁ route; R = ±1 iff π₁ = S_N (d≥3); complements the algebraic route | D1/KG ✓ |
| exchange-phase-logical-scalar | 10.5281/zenodo.21941238 | R = (−1)^{2s} parity reading (§4 of draft) | D1 ✓ |

All six corpus references verified live (no phantoms). External: Oeckl hep-th/0008072, Johnson-Freyd 1507.06297, Rowell–Stong–Wang via Crossref — all REAL (DD evidence file, commit bfeaca9).

---

## 7. Bottom line for the T2 cycle

The draft's core claims that SURVIVE: (A) involutivity is inherited from Crossing (sound, given F); (B) the two characters ↔ Calling/Crossing (sound, given two channels); (C) S_n = B_n/⟨σᵢ²=1⟩ is the mark's own law (now quantitative via TL). The claim that FAILS as written: the abelian-pair postulate is NOT demoted — the §2 "Consequence" is circular. The next deliverable of the T2 cycle is the explicit construction of F (§5.1); until then the note stays at [DERIVATION-SKETCH] grade, and the falsifiability statement to pre-register is F2' (§3).
