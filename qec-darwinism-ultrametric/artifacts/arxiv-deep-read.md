# Maity et al. (2026) — Deep Read Summary

**arXiv:** 2608.03944v1, submitted 2026-08-04
**Authors:** Arghya Maity, Kelvin Onggadinata, Teck Seng Koh (NTU Singapore)

---

## 1. Setup: Block-Environment Model

- **Code:** Shor [[9,1,3]], focusing on one logical GHZ block
- **Logical basis:** |z̄_±⟩_b = (|000⟩ ± |111⟩)/√2
- **Environment:** N independent qubits, each initialized in |+⟩ = (|0⟩+|1⟩)/√2
- **Hamiltonian:** Ĥ = g_Z Ẑ_b ⊗ Ŝ_Z + g_X X̂_b ⊗ Ŝ_X
  where Ŝ_Z = Σ_k Z_k, Ŝ_X = Σ_k X_k (collective spin operators)
- **Exactly solvable limit:** g_X = 0 (commuting sector); g_X ≪ g_Z treated perturbatively

## 2. Key Quantities

| Symbol | Definition | Expression |
|:-------|:-----------|:-----------|
| F_L(N) | Post-recovery logical fidelity | Function of g_Z, t, N, recovery efficiency η |
| F_bare | Bare logical fidelity (before recovery) | F_bare = (F_L(N) - η)/(1 - η) |
| χ(F) | Holevo info of fragment F | In solvable model: derived in closed form |
| R_δ | Darwinistic redundancy | #{fragments with χ ≥ (1-δ)ln2} |
| δ | Darwinism threshold | Typically 0.10 |
| η | Imperfect recovery efficiency | Typically 0.60 |

## 3. Theorem 1 (No-Go Theorem — Model-Independent)

**If F_bare > H_2^{-1}[(1-δ)ln 2], then NO environment fragment can satisfy the Darwinism criterion.**

Consequently R_δ = 0, regardless of Hamiltonian or environment structure.

**Proof chain (all steps are inequalities in the general case, equalities in the solvable model):**

χ(F) ≤ χ(E) ≤ S(ρ_E) = S(ρ_B) ≤ H_2(F_bare)

- Lemma 1: S(ρ_B) ≤ H_2(F_bare) with equality iff ρ_B is diagonal in the logical basis
- Purification: S(ρ_E) = S(ρ_B) for pure |Ψ⟩_{BE}
- Darwinism criterion: χ(F) ≥ (1-δ)ln 2 for some fragment
- Chain: (1-δ)ln 2 ≤ χ(F) ≤ χ(E) ≤ S(ρ_E) = S(ρ_B) ≤ H_2(F_bare)
- Monotonicity of H_2 on [1/2, 1]: F_bare ≤ H_2^{-1}[(1-δ)ln 2]

**Corollary (imperfect recovery):**

F_L(N) > η + (1-η)·H_2^{-1}[(1-δ)ln 2] ⟹ R_δ = 0

For δ = 0.10, η = 0.60: **F_L(N) > 0.874 ⟹ no Darwinistic redundancy.**

## 4. Exact Tradeoff (Solvable Model)

In the exactly solvable limit (g_X = 0), the model saturates every inequality in the proof chain:

χ(E) = S(ρ_E) = S(ρ_B) = H_2(F_bare)

Every bit of logical entropy generated in the block is converted into **accessible classical information** in the environment. The solvable model achieves the MAXIMUM Darwinistic redundancy for a given logical fidelity.

**Critical scaling:** R_δ ~ -ln(F_L(N) - F_c) as F_L → F_c^+, where F_c = η + (1-η)·H_2^{-1}[(1-δ)ln 2]

## 5. Numerical Validation

- N = 5, 10, 15 environment qubits
- g_X/g_Z = 0, 0.01, 0.05, 0.10
- For g_X/g_Z = 0.01: deviations < 0.2%
- For g_X/g_Z = 0.05: deviations ~4%
- Not a single data point enters the "forbidden region" (F_L > F_th AND χ_N ≥ (1-δ)ln 2)

---

## 6. QNFO Entry Points (Ultrametric Reformulation)

The entire framework assumes ARCHIMEDEAN metrics:

| Archimedean (Maity et al.) | Ultrametric (QNFO) |
|:---------------------------|:-------------------|
| Hamming distance on codewords | p-adic distance d_p(x,y) = p^{-v_p(x-y)} |
| Collective spin coupling: Σ_k Z_k (equal weight, additive) | Hierarchical coupling on Bruhat-Tits tree: weight ~ p^{-d(k,j)} |
| Shannon entropy H_2(x) = -x log x | Ultrametric entropy measure (Tsallis? valuation-weighted?) |
| Redundancy R_δ = #{distinct non-overlapping fragments} | Fragments are identical OR maximally distant (strong triangle inequality) |
| Tensor product environment E = ⊗^N C^2 | Tree-structured environment with p-adic nesting |
| Trace distance for fidelity | p-adic norm for fidelity |

**Key question for the paper:** Do any of these changes quantitatively (or qualitatively) alter the no-go bound?

The most promising entry point is the **redundancy concept itself:** in an ultrametric, the strong triangle inequality means fragments are either identical or maximally distant. The "partial overlap" notion that gives rise to the continuous redundancy function R_δ may not exist in ultrametric code spaces. Redundancy may be **quantized** — taking only integer multiples of some fundamental redundancy quantum tied to the p-adic valuation v_p.
