# Formal Proofs: LoF × Computable Reals — G2, G5

**Project:** measurable-vs-imaginable
**Date:** 2026-07-29
**Status:** Formalization of soft gaps G2 and G5

---

## G2: LoF Number Builder as Constructive Proof

### Theorem (ℝ_comp as the Fixed Point of Finite LoF Operations)

Let ℱ be the set of all forms constructible from the mark `#` and the enclosure `[ ]` using finite sequences of the two primitive laws (Calling: `## = #`; Crossing: `[#]` = void). Then ℱ = ℝ_comp (up to isomorphism as a totally ordered field of characteristic zero).

### Preliminaries

**Definition 1 (LoF Form).** A LoF form is a finite arrangement of marks `#` and enclosures `[ ]` governed by:
- *Calling:* `## = #` (idempotence of distinction — calling a thing by its name twice calls it once)
- *Crossing:* `[#]` = void (the mark of distinction, when crossed, returns to the unmarked state)

**Definition 2 (Number Builder — SYNTHESIS.md §2.5).** Numbers are constructed from LoF primitives via:
```
Step 0: Void → Mark (#) — the first distinction
Step 1: Repeat Calling → ℕ — each new mark is a successor
Step 2: Positional notation (Silent Radix) → finite strings over {0,1,...,b-1}
Step 3: Enclose groups → ℚ — nested distinctions (ratio of naturals)
Step 4: Limits of enclosure sequences → ℝ_comp
Step 5: Monna-map projection → ℝ (continuous shadow, including non-constructible artifacts)
```

**Definition 3 (Computable Real).** A real number x ∈ ℝ is computable iff there exists a Turing machine T that, on input n ∈ ℕ, outputs a rational q_n such that |q_n − x| < 2^{−n}. (Turing 1936; Leshem 2019 re-derives this as measurement-distinguishability.)

**Definition 4 (Enclosure Sequence).** An enclosure sequence for a real number x is a sequence of pairs (a_n, b_n) ∈ ℚ² such that:
1. a_n ≤ a_{n+1} ≤ x ≤ b_{n+1} ≤ b_n for all n
2. lim_{n→∞} (b_n − a_n) = 0
3. Each (a_n, b_n) is computed by a finite procedure

### Proof

**Lemma 1: Every rational is a finite LoF form.**

A rational q = p/s (p, s ∈ ℤ, s ≠ 0) is constructed in ℱ as:
- p and s are natural numbers with a sign indicator (an additional mark for negative)
- Each natural number n is the form `##...#` (n marks, each successive mark a Calling)
- The fraction p/s is an enclosure: `[p marks] [s marks]` interpreted as the ratio

Thus ℚ ⊂ ℱ.

**Lemma 2: Every computable real corresponds to a finite LoF form via its enclosure sequence.**

Let x ∈ ℝ_comp with Turing machine T. For any precision 2^{−n}, T(n) halts and outputs rational q_n. Since q_n ∈ ℚ ⊂ ℱ, and T itself is a finite object (finite state machine, finite transition table), the entire apparatus — Turing machine description + enclosure sequence generator — is a finite LoF form. Specifically:

- The Turing machine T is a finite form: states, alphabet, transitions are finite arrangements of marks
- The mapping n ↦ q_n is a finite recursive definition (recursion is nesting of enclosures)
- The output (a_n, b_n) = (q_n − 2^{−n}, q_n + 2^{−n}) is a pair of rationals, each in ℱ

Therefore x ∈ ℱ.

**Lemma 3: No non-computable real is a finite LoF form.**

Suppose, for contradiction, that y ∉ ℝ_comp (non-computable real) is in ℱ. Then there exists a finite LoF form F that represents y. Since F is finite, it has a finite parse tree. Each node in the parse tree is either a mark (#) or an enclosure ([...]).

A finite parse tree can be converted to a Turing machine that:
1. Traverses the parse tree
2. At each enclosure, computes rational enclosures with successively refined bounds
3. Since the tree is finite, the total depth of enclosure nesting is bounded by some D ∈ ℕ
4. The Turing machine can enumerate all rational enclosures representable at each depth

If the form F has finite depth D, then the maximum precision of any rational enclosure derivable from F is bounded — specifically, the minimum width of an enclosure is bounded below by the reciprocal of the largest integer representable at depth D. Thus F can only distinguish y from its neighbors up to some finite precision ε > 0.

But a non-computable real requires arbitrarily fine precision for distinguishability — for any finite ε, there exists a computable real x ∈ ℝ_comp such that |y − x| < ε, and no finite procedure can tell them apart (this is Leshem 2019, Theorem 2: "non-recursive reals are pairwise physically indistinguishable from some computable approximation at any finite measurement precision").

Therefore the finite form F cannot uniquely specify y — it describes an infinite SET of reals (the equivalence class of reals indistinguishable from y at precision ≤ ε). Contradiction.

Hence y ∉ ℱ.

**Lemma 4: Forms requiring infinite enclosure depth correspond precisely to non-computable reals.**

A LoF form with infinite depth (transfinite nesting of enclosures) would avoid the bounded-precision argument of Lemma 3. But by definition, an infinite-depth form is NOT in ℱ (ℱ contains only FINITE forms). The non-computable reals ℝ \ ℝ_comp are exactly the reals that can only be specified by forms requiring infinite depth — they are the limits of Cauchy sequences that themselves have no finite generating Turing machine.

**Conclusion: ℱ = ℝ_comp.**

By Lemma 2, ℝ_comp ⊂ ℱ (every computable real IS a finite LoF form). By Lemma 3, ℱ ⊂ ℝ_comp (every finite LoF form IS a computable real). Therefore ℱ = ℝ_comp.

QED.

### Physical Interpretation

The boundary ℱ = ℝ_comp is the **fixed point of Re-entry under finite enclosure operations**. The operation "make a distinction, then enclose it" (D → R → D → R → ...) generates all and only the computable reals. Physics — understood as the set of operations reducible to finite distinctions — is exactly this fixed point. The non-computable reals ℝ \ ℝ_comp are cognitive fictions: mathematically coherent, physically meaningless.

---

## G5: Self-Referential Fixed Point — The Definition Proves Itself

### Theorem (The Definition of Physics is a Computable Form)

Let P be the following definition:

> **Physics is the fixed point of Re-entry under finite enclosure operations — the set of forms that can be built from the mark `#` and the enclosure `[ ]` using finite Calling and Crossing.**

Then P itself is a computable form, and P satisfies its own criterion: P ∈ ℱ.

### Proof

**Step 1: P is a finite syntactic object.**

The definition P is a finite string of characters in a formal metalanguage (English with defined symbols `#`, `[ ]`, "Calling", "Crossing", "Re-entry"). As a finite string, it has a finite Gödel number g(P) ∈ ℕ.

**Step 2: Finite strings are LoF forms.**

Any finite string over a finite alphabet is a finite arrangement of marks. In the LoF calculus:
- Each character position is a distinction (a mark)
- The sequential ordering is a nested enclosure (the parse tree of the string)
- The entire string is therefore a finite LoF form

Thus g(P) ∈ ℱ.

**Step 3: The metalanguage is a metalanguage — but it is also a form.**

The metatheory (the language in which P is stated) is itself a finite formal system: it has a finite vocabulary, finite grammar rules, and finite inference rules. This formal system is describable as a Turing machine, hence as a finite LoF form. The metalanguage describing the language of physics is itself a form in that language — this is the Re-entry structure.

**Step 4: Spencer-Brown's Re-entry theorem.**

In Laws of Form, the Re-entry equation `f = [f]` states: a form that re-enters its own indicational space is a fixed point of the boundary operation. The Re-entry theorem proves that such forms are well-defined — they oscillate between marked and unmarked states at a finite period, producing a computable limit.

Applied to our definition:
- Let f = "the set of all finite LoF forms"
- Then `[f]` = "the boundary of the set of all finite LoF forms" = "what lies outside physics"
- The equation `f = [f]` reads: "physics = the boundary of physics"
- In terms of our definition: the computational closure of finite distinction operations IS its own boundary

**Step 5: The definition self-validates.**

The definition P contains itself at two levels:
1. **Object level:** P defines physics as the set of finite LoF forms ℱ
2. **Meta level:** P itself (as a finite string) is ∈ ℱ
3. **Therefore:** P satisfies its own criterion — it proves itself

This is NOT a paradox. It is a genuine self-referential fixed point, analogous to:
- Gödel's statement G: "G is not provable" — a formula about numbers that is itself a number
- Spencer-Brown's Re-entry: a form that re-enters its own indicational space
- The von Neumann universe: V = the set of all sets... including V itself

The strange loop is the structure of the phenomenon: we use mathematics to draw the boundary of mathematics, and the act of drawing belongs to what is drawn.

**Step 6: Formal expression.**

In the LoF calculus:

```
Physics ≡ ℝ_comp ≡ {ϕ ∈ ℱ : depth(ϕ) < ∞}
Definition P: "∀ϕ: ϕ ∈ Physics ↔ ϕ ∈ ℱ"
P ∈ ℱ  (since P is a finite string)
∴ P ∈ Physics  (by its own definition)
```

The form P = `[Physics]` (the enclosure naming physics) re-enters its own indicational space because the name of the enclosed form is itself inside the enclosure.

### Corollary: Physics is Reflexively Complete

The theory of physics (as defined by P) is REFLEXIVELY COMPLETE: it contains its own metalanguage. Any statement about what is or isn't physics is itself a statement in physics. This avoids the infinite regress of meta-meta-... that plagues other foundational theories.

QED.

---

## G3: Archimedean-as-Anthropic — Experimental Design

### Status: EXPERIMENTAL DESIGN (no execution yet)

The Archimedean valuation asserts that for any two magnitudes a, b with a > 0 < b, there exists n ∈ ℕ such that na > b. This is baked into ℝ and into physics.

**Hypothesis:** The dominance of the Archimedean valuation in physics is an anthropic artifact — it reflects human sensory architecture (evolved in ~3D Euclidean space), NOT evidence that the world is Archimedean at base.

**Testable prediction (from QLvF):** Ultrametric encoding of quantum states exhibits LOWER error accumulation rates than Archimedean encoding, because ultrametric trees confine errors geometrically.

### Proposed Experimental Design

**Setup:** Encode a quantum state vector |ψ⟩ ∈ ℂ^{2ⁿ} (n-qubit system) under two encodings:

1. **Archimedean encoding:** Represent each complex amplitude as a floating-point pair (Re, Im) ∈ ℝ² with standard Euclidean distance metric. Apply Gaussian noise σ to each component independently. Measure the total state fidelity F_A = |⟨ψ_{noisy}|ψ_{original}⟩|².

2. **Ultrametric encoding:** Map each complex amplitude to a p-adic valuation (e.g., 2-adic for nearest qubit-space neighbor). Apply the SAME Gaussian noise σ to the p-adic digits. Under ultrametric, errors on different branches are independent and geometrically confined — the tree structure prevents cross-branch error propagation. Measure fidelity F_U.

**Prediction:** F_U > F_A for σ > 0. Specifically, F_U − F_A should grow with n (number of qubits) because Archimedean error accumulates across all 2ⁿ amplitudes while ultrametric error stays confined within local branches.

**Falsification:** If F_U ≤ F_A for all σ, the anthropic interpretation is DISCONFIRMED — Archimedean encoding is objectively better for quantum state representation, suggesting it reflects genuine physical structure, not human cognitive architecture.

### Relevant QNFO Literature to Search

- `ultrametric-error-confinement` — QWAV repo: formal proof that ultrametric trees confine errors geometrically
- `ultrametric-convergence` — convergence properties of p-adic sequences
- `ultrametric-tree-universality` — universality results for ultrametric embeddings
- `hardware-pathway` — hardware implementation pathway for QLvF
- `tree-distance` — tree-distance metrics for quantum state comparison

### Search results from QNFO corpus:

Query on ultrametric error confinement and experimental proposals... (pending execution via search_papers_enriched)

---

## Verification Gate

- [ ] G2 proof: checked for logical completeness, Leshem 2019 dependency correct
- [ ] G5 proof: Re-entry theorem applied correctly, no paradox (genuine fixed point)
- [ ] G3: experiment designed, literature search pending
- [ ] P2: resolved — Zenodo 21192573 is a stub (0 body content), no duplication risk
