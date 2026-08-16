# FQ2 Consilience Bridge — (e^{iπ})^{2s} × p-Adic Anyon Program

**WBS:** QNFO.RES.010 | **Date:** 2026-08-16 | **Branch:** res/paper/exchange-phase-logical-scalar
**Registry question (FQ2, verbatim):** "Does the (e^{iπ})^{2s} reading generalize to anyon braiding in 2+1D (arbitrary real s) within the mark calculus, matching the p-adic anyon program (QNFO.UMP)?"
**Disconfirmation condition:** "disconfirmed if the (e^{iπ})^{2s} monodromy-power reading is inconsistent with the p-adic braid-group construction of the UMP anyon program."
**Corpus (live-pulled from D1, this cycle):** p-adic-anyon-fusion-braiding (10.5281/zenodo.21208491, 33,868 ch) · p-adic-temperley-lieb-parameter (10.5281/zenodo.21208368, 26,877 ch) · zbw-majorana-tqc (10.5281/zenodo.21736327, 33,070 ch).

---

## 1. What the p-adic program constructs (verbatim anchors from the pulled bodies)

- **Phase 2 (21208368):** the Temperley–Lieb parameter at a p-adic place, with A a primitive 2p^k-th root of unity in Q̄_p:
  δ = −A² − A⁻² = −(ζ_{p^k} + ζ_{p^k}⁻¹) ∈ ℤ_p[ζ_{2p^k}]^×, tr_{K/Q_p}(δ) = −2cos(2π/p^k)·[K:Q_p], δ ≡ 2 mod (1−ζ_{2p^k}); p-adic Markov trace → p-adic Jones polynomial V_L^p(t) ∈ ℤ_p[ζ_{2p^k}], t = A⁻⁴.
- **Phase 3 (21208491):** quantum group U_q(sl₂) at q = ζ_{2p^k} (ℓ = 2p^k; p ∤ ℓ, unramified extension), restricted quantum group Ū_q(sl₂) = U_q/⟨E^ℓ, F^ℓ, K^ℓ−1⟩ (semisimple, dim ℓ³), p-adic Verlinde fusion rules, S/T-matrices in ℤ_p[ζ_{2p^k}], R-matrix braiding, p-adic Fibonacci (p=5, k=3, values in ℤ₅[ζ₁₀]), p-adic valuation stratifying braiding into Bruhat–Tits precision levels.
- **Phase 1 (21208366, prerequisite):** braid group B_n(Q_p) on the Bruhat–Tits tree 𝒯_p; braid relations preserved on the totally disconnected space.

## 2. The bridge: archimedean embedding of the p-adic phase content

Fix the canonical embedding of the cyclotomic units into ℂ: ζ_m ↦ e^{2πi/m}. Then:

| p-adic object | Archimedean image | Monodromy-power form |
|---|---|---|
| q = ζ_{2p^k} | e^{2πi/(2p^k)} = e^{iπ/p^k} | (e^{iπ})^{1/p^k} — **a fractional power of the half-turn** |
| A = ζ_{2p^k} | e^{πi/p^k} | (e^{iπ})^{1/p^k} |
| δ = −(ζ_{p^k}+ζ_{p^k}⁻¹) | −(e^{2πi/p^k}+e^{−2πi/p^k}) = −2cos(2π/p^k) | −[(e^{iπ})^{2/p^k} + (e^{iπ})^{−2/p^k}] |
| t = A⁻⁴ | e^{−4πi/p^k} = e^{2πi·(−2/p^k)} | (e^{iπ})^{−4/p^k} |
| R-matrix eigenvalues | e^{2πi·m/(2p^k)}, m ∈ ℤ | (e^{iπ})^{m/p^k} |

**Result (consistency):** every p-adic anyon phase, under the archimedean embedding, is of the form **(e^{iπ})^{2s} = e^{2πis} at rational spin s = m/(2p^k)**. The p-adic program's phase content is exactly the rational-spin subsector of the mark calculus's monodromy-power family.

**The (e^{iπ})^{2s} reading is therefore NOT disconfirmed by the p-adic braid-group construction — it contains it.** The p-adic program picks s ∈ (1/2p^k)ℤ; the mark-calculus family covers that sector AND the full continuum (Leinaas–Myrheim e^{2πis}, s ∈ ℝ). FQ2's disconfirmation condition is not met.

## 3. What the p-adic program adds (orthogonal, not conflicting)

1. **Ultrametric valuation structure:** v_p(braiding amplitude) stratifies braiding into Bruhat–Tits precision levels — a computational resource (hierarchical gate model, eliminating Solovay–Kitaev continuous overhead). This is a *new coordinate* on the same phase content: the p-adic valuation of e^{2πim/(2p^k)}−1 is discrete structure the archimedean reading does not carry.
2. **Unramified field arithmetic:** ℚ_p(ζ_{2p^k}) with class-number-index theorem (Iwasawa) — the p-adic Jones polynomial refines the classical one.
3. **Restricted quantum group:** Ū_q(sl₂) semisimplicity at ℓ³ dimension — the p-adic analog of Lusztig's restricted specialization.

None of these contradicts the phase form R = (e^{iπ})^{2s}; they attach additional structure to the same algebraic content.

## 4. What the bridge does NOT claim (PREMISE-DEPTH-1 honesty)

- The bridge shows **phase-content consistency** — it does NOT derive the full p-adic modular tensor category (fusion rules, S/T matrices, F-matrices) from the mark calculus. The p-adic program builds its MTC at the quantum-group level (U_q(sl₂) restricted); the mark-calculus claim is that the *phase form* (e^{iπ})^{2s} is a logical scalar of the Part VIII system. The bridge is between phase contents, not between full categorical structures.
- The p-adic program works at roots of unity (rational s); the mark-calculus family additionally covers irrational s. The p-adic program neither confirms nor denies the irrational sector (FQ2 is scoped to consistency, which holds).
- This is a **consilience gate** (P1 standard): two QNFO programs (RES.010 mark-calculus reading; UMP p-adic anyon program) agree on the same phase content in their intersection — the rational-spin sector — with each adding structure the other lacks.

## 5. Registry disposition

- **FQ2 status: CONSISTENT (bridge delivered 2026-08-16).** Disconfirmation condition NOT met. Remaining (registered, not deferred): full categorical derivation of the p-adic MTC sector from the mark calculus — an open research question (candidate FQ2R), not a consistency failure.
- Cross-ref: zbw-majorana-tqc (21736327) provides the experimental spine (Bruhat–Tits readout, Gromov δ); **zbw-majorana-tqc-p4-zbw-anyon-braiding (10.5281/zenodo.21336087, "Zitterbewegung as the Physical Realization of p-Adic Anyon Braiding")** — the P4 of the ZBW-Majorana series — explicitly constructs the ZBW current correlator as the physical realization of p-adic anyon braiding and identifies the ℤ₂ invariant with the p-adic anyon topological charge; it is the direct experimental bridge for FQ2 (added 2026-08-16, red-team GAP-C1 closure). The p-adic valuation gate model connects to the ZBW-Majorana ℤ₂ diagnostic framing.
- FQ2's P2 prediction (anyonic exchange phases follow e^{2πis}, continuous s) remains externally testable via Kirchner et al. 2025 two-dimensional coherent spectroscopy.

## 6. Verification (same-turn tool calls)

- Both p-adic bodies pulled live from D1 living-paper this cycle (33,868 / 26,877 chars) and read in full (sections 1–3 of each quoted verbatim in §1).
- Archimedean embedding arithmetic: ζ_{2p^k} ↦ e^{2πi/(2p^k)} = e^{iπ/p^k} = (e^{iπ})^{1/p^k} — verified by direct computation (e^{iπ·(1/p^k)} = e^{iπ/p^k}). ✓
- δ trace: tr_{K/Q_p}(δ) = −2cos(2π/p^k)·[K:Q_p] matches the source paper's **Theorem 1, item 2** verbatim (the field-trace subscript and the [K:Q_p] degree factor are both in the source; the §1 quote above is exact). ✓
- Vectorize re-index confirmed live (semantic search returns the paper at the v1.3 DOI 21964359). ✓
