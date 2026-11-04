# QNFO.UMP.004 — Core Derivation Notes

**Phase 4 | Date: 2026-08-05**

## Overview

The Maity et al. proof chain is:

$$(1-\delta)\ln 2 \leq \chi(F) \leq \chi(E) \leq S(\rho_E) = S(\rho_B) \leq H_2(F_{\text{bare}})$$

Every inequality in this chain assumes Archimedean structures. We now
identify what changes when each term is re-expressed in ultrametric geometry.

## 1. The Hamiltonian — From Additive to Hierarchical Coupling

### Archimedean (Maity et al.)
$$\hat{H} = g_Z \hat{Z}_b \otimes \left(\sum_{k=1}^N Z_k\right) + g_X \hat{X}_b \otimes \left(\sum_{k=1}^N X_k\right)$$

All N environment qubits couple identically and additively. This implies that
ANY fragment of the environment carries the SAME information density — the
scaling is extensive in N.

### Ultrametric (Proposed)
$$\hat{H}^{(p)} = g_Z \hat{Z}_b \otimes \left(\sum_{k=1}^N w_k^{(p)} Z_k\right) + g_X \hat{X}_b \otimes \left(\sum_{k=1}^N w_k^{(p)} X_k\right)$$

where $w_k^{(p)} = p^{-v_p(\text{dist}(k, b))}$ with $v_p$ the p-adic valuation
and dist(k, b) the position of qubit k on the Bruhat-Tits tree relative to the
logical block.

**Consequence:** Environment qubits near the block (small p-adic distance)
couple strongly; distant qubits couple exponentially weakly. The "effective N"
in the tradeoff is reduced to N_eff, the number of qubits within the
characteristic information-spreading radius on the BT tree.

## 2. The Entropy Bound — From H_2 to Ultrametric Entropy

### Archimedean
$$S(\rho_B) \leq H_2(F_{\text{bare}}), \quad H_2(x) = -x\log_2 x - (1-x)\log_2(1-x)$$

This is Lemma 1 of Maity et al. Equality holds iff ρ_B is diagonal in the
logical basis. The assumption is that probabilities are real numbers in [0,1]
and logarithms are base-2 (Shannon).

### Ultrametric (Proposed)

In p-adic quantum mechanics (Khrennikov 1998, DOI: 10.2748/tmpub.10.1), the
inner product is p-adic-valued, not real-valued. The fidelity

$$F_p = |\langle \bar{z}_+ | \rho_B | \bar{z}_+ \rangle|_p$$

is a p-adic norm, not a real number in [0,1]. Probabilities are p-adic numbers
in ℚ_p, and the natural entropy measure is valuation-weighted rather than
Shannon. Several candidates exist:

1. **Valuation entropy:** H_v(x) = -v_p(x) for x ∈ ℚ_p — discrete, integer-valued
2. **Tsallis entropy:** S_q = (1/(1-q))·(Σ p_i^q - 1) — admits non-Archimedean extensions
3. **Log-p entropy:** H_plog(x) = -log_p |x|_p — uses p-adic absolute value

The key structural difference: while H_2(x) is a SMOOTH function on [0,1] with
values in [0,1] nats, H_v(x) is a DISCRETE function taking integer values.

**This matters for the no-go theorem because:** the inequality H_2(F_bare)
≥ (1-δ)ln 2 is continuous — F_bare can approach the threshold from below
arbitrarily closely. But if the ultrametric entropy is discrete, the
inequality H_v(F_bare) ≥ (1-δ)ln_v p may admit only integer values, creating
GAPS in the allowed redundancy.

## 3. Redundancy — From Continuous to Quantized

### Archimedean

R_δ = #{fragments F ⊂ E : χ(F) ≥ (1-δ)ln 2, fragments are distinct/non-overlapping}

"Distinct" means the fragments are disjoint subsets of environment qubits.
In Archimedean (Hamming) space, the number of disjoint subsets grows with N,
allowing R_δ to become large.

The critical scaling: R_δ ~ -ln(F_L - F_c) as F_L → F_c^+ means redundancy
DIVERGES (logarithmically) as fidelity approaches the no-go threshold from below.

### Ultrametric

In an ultrametric space, the strong triangle inequality implies:

> For any three points x, y, z: d(x,z) ≤ max(d(x,y), d(y,z))
> with equality of the two largest distances.

**Critical consequence:** Environment qubits partition into EQUIVALENCE CLASSES
by p-adic distance to the logical block. Qubits in the same class are EVERYWHERE
MUTUALLY INDISTINGUISHABLE in terms of their information content.

This means:

1. **Redundancy is quantized.** For a (p+1)-regular BT tree (where p is the prime
   of the completion):
   - Qubits at distance 0 from root: 1 (the block itself)
   - Qubits at distance 1: (p+1) vertices
   - Qubits at distance k: (p+1)p^{k-1} vertices
   
   If information propagates to distance k on the tree, the MAXIMUM number of
   distinct, information-bearing fragments is (p+1)p^{k-1}. Redundancy grows
   in DISCRETE STEPS — by factors of p — not continuously.

2. **No partial overlap.** Two fragments at different tree positions are
   maximally distant — their information content cannot "partially overlap"
   because the strong triangle inequality forbids intermediate configurations.

3. **Critical scaling changes.** As F_L → F_c^+ in the Archimedean, R_δ
   diverges logarithmically. But in the ultrametric, the maximum possible
   redundancy is bounded by the tree's branching structure. The divergence
   is TRUNCATED to a finite saturation:

   $$R_\delta^{(p)} \leq (p+1)p^{\lfloor \kappa(F_L, g_Z, t) \rfloor - 1}$$

   where κ(F_L, g_Z, t) is the p-adic distance to which information propagates
   for a given coupling strength, evolution time, and logical fidelity.

## 4. The Transformed Tradeoff

### 4.1 Conjecture: The p-Adic No-Go Bound

For p-adic code spaces on the Bruhat-Tits tree, the no-go bound becomes:

$$F_p > \tilde{H}^{-1}[(1-\delta)\ln p] \quad \Longrightarrow \quad R_\delta^{(p)} = 0$$

where F_p is the p-adic fidelity and H̃ is the appropriate ultrametric entropy
measure. The threshold is shifted because:
- The logarithm base changes from e (nats) to p (p-adic information units)
- The fidelity is p-adic rather than Euclidean

### 4.2 What Changes and What Stays

| Quantity | Archimedean | Ultrametric | Consequence |
|:---------|:------------|:------------|:------------|
| Fidelity F | ⟨ψ|ρ|ψ⟩ ∈ [0,1] ⊂ ℝ | |⟨ψ|ρ|ψ⟩|_p ∈ ℚ_p | p-adic norm, non-smooth threshold |
| Entropy H | H_2: [0,1] → [0,1] smooth | H_v: ℚ_p → ℤ discrete | Gaps between allowed redundancy values |
| Redundancy R | R_δ ~ -ln(F_L - F_c) (diverges) | R_δ ≤ (p+1)p^{κ-1} (finite bound) | Divergence is CUT OFF by tree topology |
| Fragment count | Continuous function of N | Integer multiples of (p+1)p^{k-1} | Quantized redundancy |
| Coupling | Σ_k Z_k (equal weight) | Σ_k w_k Z_k, w_k ~ p^{-d(k)} | Effective N_eff < N |

### 4.3 Two Regimes

**Regime 1: The Archimedean bound is a special case.** If p → ∞ (the
Archimedean limit of the BT tree — p becomes large, the tree becomes
dense), the discrete redundancy steps become arbitrarily fine, and the
ultrametric bound reduces to the Archimedean bound. This is the
Ostrowski-compliant statement: the Maity et al. result is the Archimedean
projection of a more general relation.

**Regime 2: Small p admits new regimes.** For small primes (p=2, 3), the
discrete redundancy steps are large, and the tradeoff curve has a staircase
structure. Between steps, there are GAPS — ranges of fidelity where redundancy
cannot change because no new equivalence class of environment qubits has been
reached. In these gaps, QEC performance and classical objectivity may BOTH
be high (or both be low) in ways the Archimedean theory forbids.

## 5. Falsifiable Predictions

### P1 — Quantized Redundancy
In a physical system with hierarchical (power-law) decay of qubit-qubit
interaction strengths — characteristic of ultrametric noise — the Darwinistic
redundancy should grow in discrete, stepwise fashion rather than as a smooth
logarithmic function.

**Test:** Measure R_δ as a function of F_L in a system with 1/f^α noise
(power-law spectrum). If the curve exhibits staircase structure with steps at
predicted p-adic values, the ultrametric hypothesis is supported.

### P2 — No-go threshold shift
The logical fidelity threshold above which redundancy vanishes should shift
to a DIFFERENT value than the Archimedean prediction F_L > 0.874.

**Test:** Compare the measured no-go threshold against the Archimedean
prediction. A statistically significant deviation is evidence for
ultrametric geometry in the noise structure.

### P3 — Ostrowski Limit
As the noise spectrum becomes flatter (α → 0, approaching white Gaussian
noise), the ultrametric prediction should converge to the Archimedean
prediction. This is the "Archimedean limit" of the Ostrowski-compliant bound.

**Test:** Vary the noise spectral exponent α and measure the tradeoff.
Convergence to Maity et al. at α = 0 confirms the Ostrowski reduction.

### Disconfirmation Condition
If the redundancy-fidelity tradeoff measured on ALL physical quantum processors
with power-law noise spectra agrees with the Archimedean prediction at ALL
scales, then either (a) the information spreading radius κ is always below the
BT tree's first branching level, or (b) the no-go theorem is Ostrowski-invariant
at physically accessible scales. Either way, this is a publishable null result
constraining the Continuum Trilogy's experimental content.

---

## Open Mathematical Questions (for §6 or future work)

1. **Ultrametric entropy measure:** What is the correct generalization of
   von Neumann entropy for p-adic Hilbert spaces? Khrennikov's non-Archimedean
   QM provides a framework, but the entropy concept has not been developed.

2. **p-adic fidelity:** How does the p-adic fidelity F_p = |⟨ψ|ρ|ψ⟩|_p relate
   to operational quantities like logical error rates? Is there a p-adic
   Gleason's theorem?

3. **BT tree code construction:** Can we construct explicit QEC codes whose
   codewords are p-adic balls on the BT tree? What is the code distance in
   terms of p-adic valuation?

4. **Experimental noise models:** Which real-world quantum computing platforms
   exhibit noise with ultrametric (hierarchical, power-law) structure?
   Superconducting qubits with 1/f noise are a candidate.
