# P4 Notebook: The (2s)-Fold Half-Turn — Exchange Phase as Monodromy Power of the Re-Entrant Mark

**WBS:** QNFO.RES.010 | **Phase:** P4 | **Date:** 2026-08-14 | **Branch:** res/paper/exchange-phase-logical-scalar
**Preceded by:** P3 citations (references.bib + citation-audit, tag v0.4-phase3)

---

## 1. Target (F1, restated per red-team Completeness reviewer)

> **The re-entrant mark / Laws-of-Form calculus generates the exchange phase as a power of its half-turn:**
> $$R = (e^{i\pi})^{2s} = e^{2\pi i s} = (-1)^{2s},$$
> **with the boson/fermion dichotomy the parity of 2s.** [my conjecture — derivation within the formal system]

**Phrasing discipline:** the primitive is specifically the *re-entrant mark of the calculus of indications under linear discipline* — not bare "self-reference." This is what scopes RES.010 against Ma & Zhang 2025 (self-referential Riccati/spinor-double-cover framework, P3 red-team LEVEL-1).

## 2. Machinery (all P3-verified)

- **Treatise §8.3** — compact closed categories as "the algebra of self-reference"; traced monoidal structure (Joyal–Street–Verity 1996, DOI 10.1017/S0305004100074338).
- **Treatise §10.2** — the self-dual circle object; loop·loop⁻¹ = id_base [established — HoTT].
- **Treatise §12.1** — e^{iπ} = −1 as the half-turn of the re-entrant mark: "the exponential of the half-turn is the negation" [established — Euler's formula].
- **RES.009 T1/T2** — the exchange map σ_{M,M} = η·id for the self-dual mark in a braided monoidal category; ribbon identity η = θ_M; symmetric braiding forces η = ±1; η = −1 ↔ Crossing (e^{iπ} = −1), η = +1 ↔ Calling. **Boundary: RES.009 does NOT write the (2s)-fold power structure.**

## 3. Derivation sketch

**Step 1 — the exchange map exists in the compact closed structure.** [established — RES.009 T1/T2 construction] The exchange σ_{M,M}: M⊗M → M⊗M is the braiding of the self-dual mark. In a symmetric braided category σ² = id, so σ has eigenvalues ±1 with idempotent projectors P_sym = ½(1+σ), P_antisym = ½(1−σ).

**Step 2 — the half-turn as the basic monodromy.** [established — treatise §12.1] The half-turn of the circle carries marked to unmarked: e^{iπ} = −1 = Crossing. This is the single-mark monodromy under rotation by π.

**Step 3 — exchange phase as a power of the half-turn.** [MAP — model of the re-entrant phase] The exchange of two particles is a loop in their configuration space (Leinaas–Myrheim 1977 [established]). The loop winds the relative coordinate; the phase acquired is the monodromy of that loop. RES.010's reading: the exchange monodromy is the (2s)-fold iteration of the mark's half-turn:
$$R = (e^{i\pi})^{2s} = e^{2\pi i s} = (-1)^{2s}.$$
The arithmetic identity is [established]; the identification of the exchange monodromy with a *power of the mark's half-turn* is [MAP — model].

**Step 4 — parity of 2s → the dichotomy.** [established arithmetic + RES.009 §1] s ∈ ℤ (integer): 2s even → R = +1 → Bose–Einstein (symmetric, Calling). s ∈ ℤ+½: 2s odd → R = −1 → Fermi–Dirac (antisymmetric, Crossing). The dichotomy *is* the parity of 2s.

**Step 5 — dimension quantization.** [established — RES.009 §3] d ≥ 3: π₁(C₂(ℝ^d)) = ℤ₂, involutive braiding forces 2s ∈ ℤ → R = ±1. d = 2: π₁ = B₂ ≅ ℤ, s continuous → anyon phases e^{2πis} [established, Leinaas–Myrheim 1977]. The (e^{iπ})^{2s} power form is well-defined for arbitrary s, unlike the (−1)^{2s} form (which needs 2s ∈ ℤ) — the scoping note from audit correction 7a5717f.

**Step 6 — unification with e and π.** [my conjecture — the scalar family] e = fixed point of Df = f (treatise §9.1 [established analysis]); π = Tr(id_{S¹}) (treatise §10.3 [established geometry; logical derivation my conjecture]); R = (e^{iπ})^{2s} (monodromy power of the half-turn). e (fixed point), π (trace), R (monodromy power) form one family of logical scalars of the re-entrant mark under linear discipline.

## 4. Status ladder

| Component | Status |
|---|---|
| Exchange map σ_{M,M}; projectors P_sym/P_antisym | [established — RES.009 T1/T2] |
| Half-turn e^{iπ} = −1 | [established — treatise §12.1] |
| η = −1 ↔ Crossing; η = +1 ↔ Calling | [established — RES.009 T2] |
| (e^{iπ})^{2s} = (−1)^{2s} = ±1 for 2s ∈ ℤ | [established — elementary] |
| Exchange monodromy = (2s)-fold half-turn | [MAP — model of the re-entrant phase] |
| e/π/R scalar-family unification | [my conjecture] |
| Formal derivation in Part VIII (§36) HoTT | [my conjecture — F1 target] |
| Physical realization (which sign, in 3+1D) | [established physics — RES.009; external Lorentz/microcausality input] |

## 5. Falsifiability

- **F1 (formal):** if the traced differential cohesive linear type theory of 21908818 Part VIII (§36) cannot derive R = (e^{iπ})^{2s} from the re-entrant mark without importing the relation as an axiom, the logical-derivation claim fails. Concrete and checkable. *Re-entrant mark / Laws-of-Form calculus* — not bare self-reference.
- **F2 (empirical, inherited RES.009):** a stable local relativistic 3+1D excitation with exchange phase η ≠ e^{2πis} disconfirms the invariant. Evasion class: Ahluwalia–Lee mass-dimension-3/2 (P3 citation audit); measurement protocol: Kirchner et al. 2025 anyonic spectroscopy.
- **F3 (scope):** arithmetic [established]; identification [MAP — model]; derivation [my conjecture]. The (−1)^{2s} equality requires 2s ∈ ℤ; the general anyon form is e^{2πis}.

## 6. Relation to nearest prior (Ma & Zhang 2025)

- Their primitive: self-referential scattering (Riccati square roots, spinor double cover) in a QFT framework → Z₂ exchange phase.
- RES.010's primitive: the re-entrant mark of the Laws-of-Form calculus under linear discipline → (2s)-fold half-turn monodromy power → e^{2πis} for arbitrary s.
- Delta: (a) primitive is the mark/LoF calculus, not QFT self-reference; (b) power structure for arbitrary s (anyons), absent in their Z₂-only result; (c) e/π/R scalar-family unification, absent. **LEVEL-1 must-distinguish, not blocking.**

## 7. Calibration

- **Success:** formal derivation of R = (e^{iπ})^{2s} as a monodromy-power scalar in the Part VIII system; at minimum, a model-theoretic construction in the compact closed structure (§8.3) matching the ribbon identity η = θ_M = e^{2πis} for the self-dual mark.
- **Minimum viable finding (P1 consilience-gate standard):** the (e^{iπ})^{2s} composite reading as the missing link between RES.009 T2's η = ±1 and the anyon generalization — with honest [MAP]/[my conjecture] labels intact.
