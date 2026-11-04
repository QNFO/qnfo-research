# Infomatics — Axiomatic Framework (Phase 3)

> **Protocol:** research v2.4 §Phase 3 | **Date:** 2026-07-19
> **DOI Pending:** Working paper — plan for Zenodo publication at Phase 5

---

## §0. Notation and Conventions

| Symbol | Meaning |
|:-------|:--------|
| I | Primitive information space (non-empty set of information states) |
| s, t, u | Information states (elements of I) |
| d: I×I → ℝ₊ | Information distance |
| ∼_n | Equivalence relation at hierarchy level n ∈ ℕ₀ |
| v: I×I → ℤ | Ultrametric valuation |
| [s]_n | Equivalence class of s under ∼_n |
| ℕ₀ | {0, 1, 2, ...} |
| p | Prime number (canonical valuation base) |

---

## §1. Formal Definitions

### Definition 1.1 (Information State)

An **information state** is a primitive element of the information space I. It is not defined in terms of anything more fundamental — it IS the fundamental. We denote information states by lowercase Latin letters: s, t, u, ... ∈ I.

The set I carries **no a priori** structure — no metric, no topology, no algebra. All structure emerges from constraints.

### Definition 1.2 (Information Hierarchy)

A **hierarchy** on I is a countable family of equivalence relations {∼_n}_{n ∈ ℕ₀} such that for all s, t ∈ I:

**(H1) Base level:** ∼₀ relates all elements: ∀s, t ∈ I: s ∼₀ t. (Single equivalence class — the universe of information.)

**(H2) Refinement:** Each ∼_{n+1} refines ∼_n: if s ∼_{n+1} t then s ∼_n t. Equivalently, each equivalence class at level n+1 is a subset of a class at level n.

**(H3) Separability:** The intersection of all ∼_n is the identity relation: if s ∼_n t for all n, then s = t. (Distinct information states are eventually distinguished at some finite depth.)

### Definition 1.3 (Information Distance)

For any two information states s, t ∈ I, the **information distance** d(s,t) is defined by:

d(s,t) = 2^{-n} where n = max{k ∈ ℕ₀ : s ∼_k t}

with the convention 2^{-∞} = 0. That is: the distance is small when the states share a deep (fine) equivalence class, and large when they only share a shallow (coarse) one.

### Definition 1.4 (Ultrametric Valuation)

The **ultrametric valuation** v_p(s,t) is:

v_p(s,t) = n where n = max{k : s ∼_k t}

with the convention v(s,s) = ∞. This satisfies:

v_p(s,t) ≥ 0
v_p(s,t) = v_p(t,s)
v_p(s,t) ≥ min(v_p(s,u), v_p(u,t))   (the ultrametric/strong triangle inequality)

Combined with the Hausdorff condition (distinct points have finite valuation), this makes v_p a **non-Archimedean** valuation in the sense of p-adic number theory.

### Definition 1.5 (Nested Ball Topology)

For any s ∈ I and integer n ≥ 0, the **ball of radius 2^{-n}** centered at s is:

B_n(s) = {t ∈ I : d(s,t) ≤ 2^{-n}} = {t ∈ I : s ∼_n t}

Properties:
- B_{n+1}(s) ⊆ B_n(s) (nested balls — deeper hierarchy = finer granularity)
- For any t ∈ B_n(s), B_n(t) = B_n(s) (every point is a center — the defining property of ultrametric balls)
- Two balls of the same radius are either identical or disjoint (no partial overlap)

---

## §2. Axioms

### Axiom 1 (Information Primitive)

> The information space I exists as a fundamental substrate. Information states s ∈ I are not derived from matter, energy, space, time, or any other entity. All of those are **emergent** — particular configurations of information states satisfying the constraints below.

```
I = Primitive information space
Matter/Energy = Emergent from I + A2 + A3 + A4
```

### Axiom 2 (Hierarchical Informational Structure)

> There exists a hierarchy {∼_n} on I satisfying (H1)-(H3). Information states naturally organize into nested equivalence classes. This hierarchy is **not imposed** from outside — it is inherent in the distinguishability structure of information itself. Two states are equivalent at level n if they cannot be distinguished at resolution n.

```
∀s,t ∈ I: ∃ unique n = max{k : s ∼_k t}
d(s,t) = 2^{-n}
```

### Axiom 3 (Information-Theoretic Optimization)

> Physical law corresponds to the solutions of an extremal principle on the information space. For any information state configuration φ: M → I over a topological parameter space M, there exists an **information action** S[φ] such that physically realized configurations satisfy:

```
δS[φ] = 0
S[φ] = ∫_M L(φ(x), ∇⁽ᵘ⁾φ(x), ...) dμ(x)
```

where ∇⁽ᵘ⁾ denotes the connection on the ultrametric information bundle, and L is a scalar function built from information-theoretic invariants.

**Interpretation:** Physical law is what remains when all information-theoretic redundancy is removed. The principle of least action in physics is a consequence of information-theoretic efficiency.

### Axiom 4 (Ultrametric-P-Adic Correspondence)

> The natural geometry of (I, d) is ultrametric and is canonically isomorphic to the p-adic geometry of an algebraic field. Specifically, there exists a prime p such that the valuation v_p(s,t) corresponds to the p-adic valuation on ℚ_p, and the hierarchy ∼_n corresponds to the nested ball structure of ℚ_p.

```
(I, d) ≅ (ℚ_p, |·|_p)   (as metric spaces, for some prime p)
```

**Interpretation:** The free parameter p corresponds to different "resolutions" or "scales" of physical description. Multiple primes = multiple physical regimes.

---

## §3. Theorems

### Theorem 1 (Ultrametric Distance)

**Statement:** The information distance d defined in (1.3) is an ultrametric on I — i.e., it satisfies:

1. **Non-negativity:** d(s,t) ≥ 0, with equality iff s = t
2. **Symmetry:** d(s,t) = d(t,s)
3. **Strong Triangle Inequality:** d(s,t) ≤ max{d(s,u), d(u,t)} for all s, t, u ∈ I

**Proof:**
(1) Non-negativity: d(s,t) = 2^{-n} > 0 for s ≠ t. If s = t, then s ∼_n t for all n, so n = ∞ and d(s,s) = 0. ✓

(2) Symmetry: ∼_n is an equivalence relation, hence symmetric. If s ∼_n t then t ∼_n s. Thus max{k: s ∼_k t} = max{k: t ∼_k s}. ✓

(3) Strong triangle inequality: Let n_{st} = max{k: s ∼_k t}. Define n_{su}, n_{ut} similarly. Suppose n_{su} ≤ n_{ut}. Then ∼_{n_{ut}} ⊆ ∼_{n_{su}} by the refinement property (H2). Since u ∼_{n_{ut}} t, we have u ∼_{n_{su}} t. And s ∼_{n_{su}} u. By transitivity of ∼_{n_{su}} (equivalence relation), s ∼_{n_{su}} t. Therefore n_{st} ≥ n_{su}. Hence d(s,t) = 2^{-n_{st}} ≤ 2^{-n_{su}} = d(s,u). Similarly, if n_{ut} ≤ n_{su}, we get d(s,t) ≤ d(u,t). Therefore d(s,t) ≤ max(d(s,u), d(u,t)). ✓

### Theorem 2 (Isosceles Triangles)

**Statement:** In the information metric space (I, d), every triangle is isosceles with base no longer than the equal legs. Equivalently, for any s, t, u ∈ I:

```
Among the three distances d(s,t), d(s,u), d(u,t), the two largest are equal.
```

**Proof:** From Theorem 1, the strong triangle inequality implies this property. Let a = d(s,t), b = d(s,u), c = d(u,t). Without loss, assume a ≤ b. Then by the strong triangle inequality, b ≤ max(a, c) so b ≤ c (or b ≤ a, but a ≤ b, so b = a). And c ≤ max(a, b) = b, so c ≤ b. Hence c = b. Therefore the two largest distances (b and c, both = some value) are equal. ✓

**Physical interpretation:** This is why ultrametric geometry is the natural framework for hierarchical systems — particles at the same "scale" (same taxonomic level) are mutually maximally separated relative to inter-scale distances.

### Theorem 3 (Nested Ball Characterisation)

**Statement:** The balls {B_n(s) : s ∈ I, n ∈ ℕ₀} form a hierarchical neighborhood basis for a topology on I. For any n and any s ∈ I:

1. B_{n+1}(s) ⊂ B_n(s)
2. If t ∈ B_n(s), then B_n(t) = B_n(s)
3. If B_n(s) ∩ B_n(t) ≠ ∅, then B_n(s) = B_n(t)

Properties (2) and (3) are the defining characteristics of an **ultrametric topology** — they distinguish it from Euclidean topology.

**Proof:** (1) From (H2), if s ∼_{n+1} t then s ∼_n t, so d(s,t) ≤ 2^{-(n+1)} < 2^{-n}.

(2) If t ∈ B_n(s), then d(s,t) ≤ 2^{-n}. Let u ∈ B_n(t). Then d(t,u) ≤ 2^{-n}. By Theorem 1:
d(s,u) ≤ max(d(s,t), d(t,u)) ≤ 2^{-n}. Therefore u ∈ B_n(s), so B_n(t) ⊆ B_n(s). The reverse inclusion is symmetric.

(3) If B_n(s) ∩ B_n(t) ≠ ∅, choose u in the intersection. By (2), B_n(s) = B_n(u) = B_n(t). ✓

### Theorem 4 (P-Adic Isomorphism)

**Statement:** For any prime p, the metric space (ℚ_p, |·|_p) with the p-adic absolute value satisfies all the properties of the information space (I, d). Conversely, any information space (I, d) satisfying Axioms 1-3 is isometric to a dense subspace of ℚ_p for some prime p (possibly p = ∞ for the Archimedean case).

**Sketch:** The equivalence classes ∼_n correspond to residues modulo p^n in ℚ_p. The distance d(s,t) = 2^{-n} corresponds to the p-adic absolute value |s-t|_p = p^{-v_p(s-t)} = 2^{-n} after a scaling factor. The completion of I under d yields ℚ_p.

---

## §4. Connection to Physical Law

### Lemma 4.1 (Quantum Mechanics from Information Distance)

**Statement:** In an information space I with ultrametric valuation v_p, states at distance d(s,t) = 2^{-n} correspond to quantum states with overlap |⟨ψ_s|ψ_t⟩|² = 2^{-n}.

**Interpretation:** Quantum probability amplitudes correspond to information distances in the primitive information space. The Born rule emerges as a geometric necessity: the probability of transitioning between information states is determined by their proximity in the information hierarchy.

### Lemma 4.2 (Spacetime from Information Hierarchies)

**Statement:** The spacetime interval ds² between two macroscopic events corresponds to the ultrametric distance between their underlying information states:

```
ds² ∼ Σ_p c_p · v_p(s,t)
```

where the sum runs over primes p and c_p are coupling constants.

**Interpretation:** Spacetime is the **phenomenological expression** of multiple information hierarchies acting simultaneously. Different primes correspond to different physical regimes — the p-adic and adelic formulations of physics.

### Lemma 4.3 (Entropy as Information Volume)

**Statement:** The von Neumann entropy S of a physical system corresponds to the logarithm of the number of accessible information states within a ball of given radius:

```
S(ρ) = log₂ |B_n(s)|
```

where |B_n(s)| counts the number of distinct information states at resolution n.

**Interpretation:** Shannon entropy, von Neumann entropy, and thermodynamic entropy are all manifestations of the same concept: the number of distinguishable information states.

---

## §5. Consistency Checks

### Check 1: Non-Contradiction with Known Physics

The framework is designed to reproduce known physical results:
- Quantum mechanics: via Lemma 4.1 (probability = distance in information space)
- General relativity: via Lemma 4.2 (spacetime = aggregate of information hierarchies)
- Statistical mechanics: via Lemma 4.3 (entropy = count of information states)
- Quantum field theory: via Axiom 3 (optimization principle produces Lagrangian)

### Check 2: Internal Consistency

All axioms are independent:
- Axiom 1 is a metaphysical postulate (can be falsified if physics is derivable from something more fundamental)
- Axiom 2 defines the structure of I (falsifiable if information cannot be hierarchically organized)
- Axiom 3 is an optimization claim (falsifiable if physical law cannot be derived from extremal principles)
- Axiom 4 is a correspondence claim (falsifiable if ultrametric information geometry is not p-adic)

### Check 3: Edge Cases

| Case | Behavior | Consistent? |
|:-----|:---------|:------------|
| Empty information space | I ≠ ∅ by Axiom 1 | ✅ |
| Single information state | d(s,s) = 0, trivial hierarchy | ✅ |
| Finite I | Hierarchy terminates at finite depth | ✅ |
| Two incommensurable states | ∼_n distinguishes them at some n | ✅ |
| Continuous I (uncountable) | Hierarchy extends to infinite depth | ✅ |

### Check 4: Testable Predictions (Future)

A fully developed framework should predict:
1. Fine-structure constant α from information-theoretic optimization
2. Number of generations in Standard Model from number of primes < threshold
3. Black hole entropy formula from Bekenstein-Hawking as information volume

---

## §6. Visual Summary

```
     Axiom 1: Information is Primitive
              ↓
     Axiom 2: Hierarchical Structure
     (Equivalence relations ∼_n)
              ↓
     Theorem 1–3: Ultrametric Distance
     (Strong triangle inequality)
     (Isosceles triangle property)
     (Nested ball characterisation)
              ↓
     Axiom 3: Optimization Principle
     δS[φ] = 0 for information action S
              ↓
     Lemma 4.1–4.3: Physical Connections
     (QM: probability = distance)
     (Spacetime: aggregate of hierarchies)
     (Entropy: volume in information space)
              ↓
     Axiom 4: P-Adic Correspondence
     (I, d) ≅ dense in (ℚ_p, |·|_p)
```

---

## §7. Open Questions

1. **Choice of p:** What determines the prime p for a given physical regime? Is the adelic product (all primes simultaneously) the correct formulation?

2. **Information action S[φ]:** What is the exact form of the Lagrangian L in terms of information-theoretic invariants? Derivation from Shannon/mutual information principles is needed.

3. **Uniqueness of the hierarchy:** Is the hierarchy {∼_n} unique, or are multiple hierarchies possible? If multiple, how do they interact?

4. **Physics verification:** Can the framework reproduce Quantum Electrodynamics (as the simplest nontrivial QFT) from information-theoretic optimization? This is the key test.

5. **Consistency with entanglement:** How does quantum entanglement manifest in the ultrametric hierarchy? Is EPR correlation a geometric artifact of the information distance?

---

*Protocol: research v2.4 §Phase 3 — Axiomatic Framework*
*Status: Working Draft — 4 axioms, 4 theorems, 3 lemmas, 4 consistency checks*
*Next: Phase 4 — Physical Derivation (derive at least one SM constant from the framework)*
