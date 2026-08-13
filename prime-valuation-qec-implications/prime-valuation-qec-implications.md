# Implications for Computing and Quantum Error Correction

**Author:** Quni-Gudzinas, Rowan Brad (QNFO Research Collective)
**ORCID:** 0009-0002-4317-5604
**WBS:** QNFO.RES.006
**Date:** 2026-08-13
**Version:** v0.2
**License:** CC-BY-4.0\n**Changelog:** v0.2 (2026-08-13) — §6 precision patch (83% per-family breakdown; rule-based Algorithm 4.4 reframing; reproduction protocol pointer) + reference corrections (Gubser–Knaute venue; Bhattacharyya DOI) per P4 red-team (see artifacts/red-team-P4.md, artifacts/rq3-reproduction-protocol.md).

**Anchor:** *Prime Valuation Depth: Multiplication as Branching, the Calculus of Indications, and the Structural No-Cloning Reading* (QNFO.RES.005, DOI 10.5281/zenodo.21918838).

---

## Abstract

The anchor paper introduced the *branch-depth reading*: the p-adic valuation v_p(n) is a measure of depth along a prime branch of the integer factorization tree (not a measure of size), and because the tensor product multiplies Hilbert-space dimensions, v_2(dim H) = n counts tensor-branch depth for n qubits. This follow-on subjects that reading to its own stated falsifiability condition in the two domains the anchor flagged but did not pursue — computing and quantum error correction. The central finding is a *correction, not a confirmation*: the naive mapping of a [[n,k,d]] stabilizer code to branch depths, n = v_2(dim H) and k = v_2(dim H_L), is **trivially true by definition** (a code is defined on n qubits encoding 2^k logical states) and therefore carries no new content; and the code distance d — a minimum operator *weight*, not a *depth* — does not admit a valuation reading at all. The genuinely open question is whether there exists a **non-trivial** valuation invariant of stabilizer codes beyond the definitional n and k, and it is here — not in the naive mapping — that the existing QNFO "83% classification accuracy" claim (Kodaira–Néron classifier, DOI 10.5281/zenodo.21193487) lives and must be independently reproduced. The structural no-cloning reading is retained but repositioned honestly: it is a known categorical result (Abramsky 2009; Coecke 2009), which the branch-depth vocabulary re-expresses rather than discovers. Every non-empirical claim below carries an explicit falsifiability condition.

---

## 1. Introduction and Positioning

### 1.1 What the anchor paper established

*Prime Valuation Depth* developed three claims, each with a stated falsifiability condition:

1. **[TERRITORY — established, Ostrowski 1916]** Every positive integer is a finite product of prime powers; v_p(n) is depth along the prime-p branch, not size.
2. **[MAP — interpretive]** The valuation-as-depth reading is a bridge between the calculus of indications (branching distinctions) and number theory (the prime divisor tree).
3. **[MAP — interpretive]** The tensor product multiplies dimensions, so prime factorization of dim H labels branch types and v_p(dim H) counts branch depth; the no-cloning theorem is then the impossibility of a linear diagonal map — cloning is nonlinear in the amplitudes, and quantum evolution preserves only linear structure.

### 1.2 The honest starting point of this paper

The anchor paper labels its own quantum reading as "interpretive rather than new physics" and attaches the falsifiability condition: *disconfirmed if the reading yields no explanatory or predictive content beyond the standard formalism — i.e., if it is pure relabeling.* This follow-on takes that condition seriously and applies it to the two domains the anchor flagged for later work. The result, reported here without flinching, is that **the most obvious extension — reading [[n,k,d]] parameters as valuations — is largely pure relabeling.** This is not a failure of the program; it is the falsifiability machinery doing its job, and it sharpens the question to the one place where the branch-depth vocabulary could carry real weight.

### 1.3 External precedent (confirmation-bias correction)

The anchor's quantum reading does not occur in a vacuum. The categorical content — that quantum processes form a compact-closed (monoidal but non-Cartesian) category, and that no-cloning follows from this — is established in the categorical quantum mechanics literature [Abramsky & Coecke 2004; Abramsky 2009; Coecke 2009; Coecke & Duncan 2011]. Independently, the connection between p-adic geometry and quantum error-correcting codes is established in the holographic tensor-network literature [Heydeman, Marcolli, Saberi & Stoica 2018; Bhattacharyya, Hung, Lei & Li 2018; Gubser & Knaute 2017]. The present paper does not claim priority on either bridge; its narrow contribution is the specific *branch-depth vocabulary* (valuation as depth, in the calculus-of-indications sense) applied to code parameters, and its consequence for how QEC limits are framed.

---

## 2. The Branch-Depth Reading, Restated

Let n ∈ ℤ⁺ factor as n = ∏ pᵢ^{aᵢ}. The anchor's reading: each prime pᵢ is a *branch type*, and the exponent aᵢ = v_{pᵢ}(n) is the *depth* of nesting along that branch. A tensor product of Hilbert spaces multiplies dimensions: dim(H₁ ⊗ H₂) = dim(H₁)·dim(H₂). Hence for n qubits, dim H = 2ⁿ and

v₂(dim H) = n.

This is the single quantitative bridge the anchor supplies. The question this paper asks is: **what does it buy us?**

---

## 3. The [[n,k,d]] Mapping — and Why It Is Mostly Relabeling

### 3.1 The definitional facts

A [[n,k,d]] stabilizer code is a 2ᵏ-dimensional subspace (the codespace) of an n-qubit Hilbert space H ≅ (ℂ²)^⊗n, with dim H = 2ⁿ. Two identities follow immediately:

n = v₂(dim H) = v₂(2ⁿ) = n,
k = v₂(dim H_L) = v₂(2ᵏ) = k.

**Claim [MAP — to be tested]:** these identities constitute a "branch-depth reading" of the code parameters.

**Finding [SELF-CORRECTION]:** the identities are *definitional*. n is the number of qubits *by construction*, and k is the number of logical qubits *by construction*. Restating them as v₂ of a dimension adds nothing: the valuation is doing no work that the exponent of 2 in "2ⁿ" and "2ᵏ" was not already doing. This is the anchor's own falsifiability condition, triggered: **the n and k mappings are pure relabeling.**

### 3.2 The distance d does not have a valuation reading

The code distance d is the minimum weight (number of non-identity Pauli factors) of a non-trivial logical operator. It is a **Hamming weight** — a count of tensor factors an error touches — not a p-adic depth. There is no integer whose valuation yields d in the way 2ⁿ yields n. The tempting phrase "d = branch-crossing error weight" is a metaphor, not a valuation identity, and must not be presented as mathematics. **[Falsifiability condition: disconfirmed if any specific valuation identity for d is claimed; d is a weight, and the burden of proof for any valuation-based bound on d is on the claimer.]**

### 3.3 What is left after the relabeling is stripped away

Stripping the definitional n and k mappings and the unavailable d mapping leaves a single, precise, and genuinely open question:

> **Does there exist a non-trivial valuation invariant of a stabilizer code — one not equal to v₂(dim H) or v₂(dim H_L) — that carries classification or predictive power across code families?**

This is where the existing QNFO result attaches.

---

## 4. Computing as Path-Tracing: A Scoped, Falsifiable Claim

The anchor's computing leg was left as a flagged direction. The honest scope is narrow:

**Claim [MAP — interpretive, scoped]:** reversible classical computation and Clifford quantum computation are *path-tracing through a branching state space*, and the p-adic valuation is the natural depth coordinate on that tree, in the specific sense that the Hensel-code arithmetic of exact rational computation [cf. the p-adic arithmetic literature] is computation *on* the branch tree.

**Falsifiability condition:** disconfirmed if no computational task can be shown to have a *valuation-based* complexity characterization that differs from (or tightens) its standard characterization. The claim is advanced only as a research program, not as an established result. **[CONTESTED] — no such characterization has yet been produced; this section is explicitly promissory.]**

---

## 5. Structural No-Cloning and the Necessity of QEC

### 5.1 The honest attribution

The claim "cloning would require a nonlinear diagonal map, and quantum evolution preserves only linear structure" is a known categorical result. In the categorical quantum mechanics framework, a compact-closed category is **non-Cartesian**: the monoidal product ⊗ is not a categorical product, so there is no natural diagonal Δ: A → A ⊗ A that is linear (a morphism in the category). No-cloning is the physical statement of the absence of this linear diagonal [Abramsky 2009; Coecke 2009]. The anchor paper's contribution is the *vocabulary* — expressing the same fact as "multiplicative branching cannot be linearly duplicated" — not the *result*.

**Claim [MAP — re-expression]:** the branch-depth vocabulary re-expresses no-cloning as: *a branch (tensor factor) cannot be duplicated by a linear process, so redundancy — the resource QEC consumes — must be carried in non-orthogonal (entangled) configurations, never in clones.*

**Falsifiability condition:** disconfirmed if this re-expression cannot be shown to yield at least one new, checkable consequence for QEC limits that the standard no-cloning statement does not already imply. **[Risk: HIGH — this is the relabeling risk again, and it is flagged as such.]**

### 5.2 The one place the framing could bite

A candidate consequence, stated as a falsifiable hypothesis: **if redundancy is non-cloneable, then the overhead (physical-to-logical qubit ratio) of a QEC code is bounded below by a function of the code's own valuation structure.** Whether this bound is tighter than, equivalent to, or weaker than the quantum Singleton bound n − k ≥ 2(d−1) is the test. **[UNTESTED — no bound has been derived; deriving one, and comparing it to the Singleton bound, is the concrete task that would elevate this framing from metaphor to mathematics.]**

---

## 6. The 83% Classification Claim: Status and Reproduction Requirement

QNFO.UF reports (NTOF, DOI 10.5281/zenodo.21193487) that a **rule-based** Kodaira–Néron-fiber
classifier (Algorithm 4.4: binary symplectic form H → Cox ring R_C → Weierstrass coefficients →
degenerate loci → fiber type) assigns code families with **166/200 (83%)** correct on 50 test codes
per family: Surface 46/50 (92%), CSS 39/50 (78%), Optimal 45/50 (90%), Random 36/50 (72%), with
Mahler v_p^max = 28 for optimal versus v_p^max = 4 for random ensembles. The source itself records
a documented partial failure — "FAIL for surface codes (systematic mismatch in the I_n*
classification boundaries)" — so the aggregate 83% conceals a known per-family defect. The NTOF
record ships no dataset, no implementation, and no baseline; the classifier is deterministic
rule-based, not a learned ML classifier. The program registry's summary "p-adic valuations
classify QEC codes at 83% accuracy" is therefore a compressed (and partially misleading)
rendering of this state of affairs.

**Status [UNVERIFIED-INTERNAL]:** this is an internal report. It has not, to this author's knowledge, been independently reproduced on a fresh, held-out test set with a stated leakage-control protocol. Until it is, the 83% figure is a claim to be tested, not a result to be built upon.

**Reproduction requirement (this paper's P4 critical path):** because the classifier is
rule-based and the source ships no implementation, the reproduction is a **re-implementation from
specification** (Algorithm 4.4) plus **fresh code-family generation** (50 per family; surface, CSS,
optimal, random) with (i) a stated generation protocol and seeds, (ii) an independent computation
of the v_p-spectral invariant, (iii) baselines (majority-class and random-assignment) reported
alongside, and (iv) the source's documented surface-code boundary defect tested explicitly.
Full protocol: artifacts/rq3-reproduction-protocol.md. Success is reproduction *within stated
confidence* (pre-registered acceptance criteria); failure is reported honestly either way.

**Falsifiability condition:** the "83% accuracy" claim is disconfirmed if independent reproduction fails to exceed a stated baseline by a pre-registered margin. **[The reproduction is out of scope for this v0.1 manuscript and is deferred to P4; its absence is disclosed, not hidden.]**

---

## 7. Complete Falsifiability Register

| # | Claim | Type | Falsifiability condition | Current status |
|:--|:------|:-----|:--------------------------|:---------------|
| C1 | v_p(n) is depth along a prime branch | established (Ostrowski) | — | established |
| C2 | n = v₂(dim H), k = v₂(dim H_L) is a "branch-depth reading" of [[n,k,d]] | MAP | disconfirmed (pure relabeling) | **SELF-CORRECTED** |
| C3 | d admits a valuation reading | MAP | no valuation identity exists | **REJECTED** |
| C4 | a non-trivial valuation invariant of codes exists | open question | no such invariant found ⇒ program fails | OPEN |
| C5 | computing = path-tracing, with valuation-based complexity content | MAP | no valuation-based complexity characterization produced | PROMISSORY |
| C6 | no-cloning re-expressed as non-cloneable redundancy | re-expression | no new checkable consequence ⇒ relabeling | RISK-HIGH |
| C7 | overhead bounded by valuation structure | hypothesis | compare to Singleton bound | UNTESTED |
| C8 | Kodaira–Néron classifier is 83% accurate | empirical (internal) | independent reproduction vs baseline | UNVERIFIED-INTERNAL |

---

## 8. Relation to Prior Work (External)

- **Categorical QM / no-cloning:** Abramsky & Coecke (2004) *A categorical semantics of quantum protocols*; Abramsky (2009) *No-Cloning in Categorical Quantum Mechanics*; Coecke (2009) *Quantum Pictorialism*; Coecke & Duncan (2011) *Interacting Quantum Observables*. The no-cloning content of §5 is theirs; this paper adds only vocabulary.
- **p-adic holographic QEC:** Heydeman, Marcolli, Saberi & Stoica (2018) *Tensor networks, p-adic fields, and algebraic curves* (ATMP 22:93); Bhattacharyya, Hung, Lei & Li (2018) *Tensor network and (p-adic) AdS/CFT*; Gubser & Knaute (2017) *p-Adic AdS/CFT*. The p-adic/QEC connection is theirs; this paper's branch-depth framing is a distinct, narrower lens.
- **Stabilizer methods:** Bravyi, Browne, Calpin, Campbell, Gosset & Howard (2019) *Simulation of quantum circuits by low-rank stabilizer decompositions* — the working background for §3–§4.

**Relation to QNFO internal corpus:** the p-adic QEC space is densely worked internally (see artifacts/due-diligence.md §2 for the DOI list). This paper's narrow differentiation is the branch-depth vocabulary and the self-correction of §3, which the existing corpus (which treats valuation as a *classifier weight*, not a *depth*) does not perform.

---

## 9. Conclusion

The branch-depth reading, applied honestly to computing and quantum error correction, yields a **negative and a positive result**. The negative result: the obvious extension — reading [[n,k,d]] parameters as valuations — is definitional for n and k and unavailable for d; it is, in the anchor's own terms, pure relabeling, and this paper says so rather than papering over it. The positive result: stripping the relabeling leaves one precise open question — *does a non-trivial valuation invariant of stabilizer codes exist?* — and one concrete falsifiable task — *derive a valuation-based QEC-overhead bound and compare it to the Singleton bound.* The 83% classification claim is a testable hypothesis at the center of that question, and it must be independently reproduced before it is treated as established. This is the honest state of the program: a sharp question, a clear test, and a prior claim awaiting verification.

---

## References

1. Abramsky, S., & Coecke, B. (2004). A categorical semantics of quantum protocols. *LICS 2004*.
2. Abramsky, S. (2009). No-Cloning in Categorical Quantum Mechanics. In *Semantic Techniques in Quantum Computation*.
3. Coecke, B. (2009). Quantum Pictorialism. *Contemporary Physics*.
4. Coecke, B., & Duncan, R. (2011). Interacting Quantum Observables: Categorical Algebra and Diagrammatics. *New Journal of Physics*.
5. Heydeman, M., Marcolli, M., Saberi, I., & Stoica, B. (2018). Tensor networks, p-adic fields, and algebraic curves. *Adv. Theor. Math. Phys.* 22:93. arXiv:1605.07639.
6. Bhattacharyya, A., Hung, L.-Y., Lei, Y., & Li, W. (2018). Tensor network and (p-adic) AdS/CFT. *JHEP* 2018(1):139. arXiv:1703.05445. DOI 10.1007/jhep01(2018)139.
7. Gubser, S. S., & Knaute, J. (2017). A p-adic version of AdS/CFT. *Adv. Theor. Math. Phys.* 21(7):1655–1683. DOI 10.4310/atmp.2017.v21.n7.a3.
8. Bravyi, S., Browne, D., Calpin, P., Campbell, E., Gosset, D., & Howard, M. (2019). Simulation of quantum circuits by low-rank stabilizer decompositions. *Quantum* 3:181.
9. Ostrowski, A. (1916). Über einige Lösungen der Funktionalgleichung φ(x)φ(y)=φ(xy). *Acta Mathematica*.
10. Quni-Gudzinas, R. B. (2026). Prime Valuation Depth. Zenodo. DOI 10.5281/zenodo.21918838.
11. QNFO Research Collective (2026). Number-Theoretic Ultrametric Foundations. Zenodo. DOI 10.5281/zenodo.21193487.
