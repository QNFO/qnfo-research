---
title: "Prime Valuation Depth: Multiplication as Branching, the Calculus of Indications, and the Structural No-Cloning Reading"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-13"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "TBD"
status: "draft"
version: "v0.1-draft"
keywords:
  - p-adic valuation
  - laws of form
  - calculus of indications
  - no-cloning theorem
  - tensor product
  - Ostrowski's theorem
---

## Abstract

This paper develops a structural reading of the p-adic valuation as a measure of depth along a prime branch of the integer factorization tree, rather than a measure of size. The reading, grounded in Ostrowski's classification of absolute values on the rationals, is proposed as a bridge between the calculus of indications (Spencer-Brown's theory of distinction) and number theory (the tree of prime divisors). The correspondence is stated at the level of shared structural laws: both structures satisfy a nesting/hierarchy condition, and the p-adic valuation is the unique measure of multiplicity along a labeled branch. The reading is then extended to quantum mechanics: the tensor product multiplies Hilbert-space dimensions, so prime factorization of dimension labels the branch types and the p-adic valuation of dimension counts tensor-branch depth. Within this vocabulary, the no-cloning theorem is expressed as the impossibility of linearly duplicating multiplicative branching: the diagonal map sending a state to its tensor square is nonlinear, and the image of such a map is not a linear subspace. The categorical content of this statement is established in the literature by Coecke and Duncan and by Coecke and Paquette; the contribution of the present paper is the p-adic-depth vocabulary and its branch-depth framing, which is explicitly labeled as an interpretive reading rather than new physics. Falsifiability conditions are stated for every non-empirical claim, and the limits of the reading are discussed, including the absence of a direct literature anchor for p-adic-specific no-cloning theorems.

**Keywords:** p-adic valuation; laws of form; calculus of indications; no-cloning theorem; tensor product; Ostrowski's theorem

## 1. Introduction

Multiplication is standardly defined by recursive addition, yet recursion obscures a structural fact: multiplication generates a new dimension of distinctions. The product of two positive integers is the count of pairs, and counting pairs requires pairing — a new level of distinction between the two factors. This paper takes that observation literally. Prime factorization makes the branching explicit: every positive integer is a finite product of prime powers, each prime is a distinct branch type, and the exponent counts the depth of nesting along that branch. The p-adic valuation $v_p(n)$ is therefore a measure of depth along a prime branch, not a measure of size.

This reading of valuation as depth is proposed as a bridge between two structures that developed independently: the calculus of indications of Spencer-Brown [@spencerbrown1969], in which a distinction is the primitive act and nesting produces form, and number theory, in which the fundamental theorem of arithmetic produces the tree of prime divisors. The bridge is grounded in Ostrowski's theorem [@ostrowski1916]: the only nontrivial absolute values on the rationals are the Archimedean one and the p-adic ones, so the prime-depth valuations are exhaustive among the non-Archimedean measures of closeness.

The reading is then extended to quantum mechanics. The tensor product is not a Cartesian product; it multiplies dimensions and thereby generates paired distinctions. Prime factorization of a Hilbert-space dimension identifies the branch types, and for $n$ qubits the dimension is $2^n$, so the 2-adic valuation $v_2(\dim H) = n$ is exactly the number of tensor factors. Within this vocabulary, the no-cloning theorem [@wootters1982; @dieks1982] is expressed structurally: cloning would require a diagonal map sending a state to its tensor square, which is nonlinear in the amplitudes, and the image of such a map is not a linear subspace. The tensor product is monoidal but not Cartesian, and no linear map can duplicate multiplicative branching.

The paper is organized as follows. Section 2 develops the valuation-as-depth reading and its Ostrowski grounding. Section 3 states the correspondence between the calculus of indications and the prime tree. Section 4 translates the reading to the tensor product. Section 5 gives the structural no-cloning statement and its adjacent theorems. Section 6 discusses the adelic frontier and the limits of the reading. Section 7 concludes.

## 2. Valuation as Depth

### 2.1 The Prime Tree

By the fundamental theorem of arithmetic, every positive integer $n$ admits a unique factorization

$$n = \prod_{p} p^{e_p(n)},$$

where the product is over primes and only finitely many exponents $e_p(n)$ are nonzero. The p-adic valuation is the exponent map

$$v_p(n) = e_p(n),$$

with the convention $v_p(0) = \infty$. The valuation satisfies the two defining identities of a discrete valuation on the rationals:

$$v_p(mn) = v_p(m) + v_p(n), \qquad v_p(m+n) \geq \min\bigl(v_p(m), v_p(n)\bigr).$$

The first identity is multiplicativity: depth along a branch adds when branches are composed. The second is the strong triangle inequality, which characterizes non-Archimedean structure: the depth of a sum is never less than the minimum depth of its terms.

The tree picture is direct: the integer $n$ occupies the node reached from the root by, for each prime $p$, taking $v_p(n)$ steps along the branch labeled $p$. A prime is a branch type; the exponent is the depth of nesting along that branch. Two integers are close in the p-adic metric precisely when they share a long initial segment along the $p$-branch.

### 2.2 Ostrowski's Exhaustiveness

Ostrowski's theorem [@ostrowski1916] states that every nontrivial absolute value on the rationals is equivalent either to the usual Archimedean absolute value or to a p-adic absolute value of the form

$$\lvert x \rvert_p = p^{-v_p(x)}.$$

The p-adic absolute value inverts depth: the deeper along the $p$-branch a rational lies, the smaller it is in the p-adic topology. This is the precise sense in which valuation is depth, not size: the valuation $v_p$ itself counts nesting, while the derived absolute value converts that nesting into a non-Archimedean size.

**Statement 1 [TERRITORY — established].** For every positive integer $n$ and prime $p$, the p-adic valuation $v_p(n)$ is the multiplicity of $p$ in the factorization of $n$; equivalently, it is the depth of $n$ along the $p$-branch of the prime tree. This is the definition of the valuation together with the fundamental theorem of arithmetic. Ostrowski's theorem establishes that the p-adic valuations, together with the Archimedean absolute value, exhaust the nontrivial absolute values on the rationals. *No falsifiability condition is required: this is a mathematical fact, not a hypothesis.*

## 3. The Calculus of Indications and the Prime Tree

### 3.1 The Correspondence

The calculus of indications [@spencerbrown1969] takes the act of distinction as primitive. A mark distinguishes an inside from an outside; the act of calling a distinction again is the act of crossing; nesting of distinctions generates form. The formal literature includes three-valued interpretations [@varela1979], recursive distinctioning [@isaacson2016], and connections to self-reference and quantum mechanics [@rapoport2009].

The correspondence proposed here maps the two structures term by term:

| Calculus of indications | Prime tree | Reading |
|:------------------------|:-----------|:--------|
| A distinction | A prime branch type | Both are primitive types of separation |
| Drawing a distinction | Multiplying by a prime | Both generate a new level of structure |
| Nesting a distinction | Increasing the exponent | Both count depth along a type |
| The marked state at depth $e$ | The prime power $p^e$ | Both are determined by type and depth |
| The unmarked state | $n = 1$ | The empty product; no distinctions drawn |
| Re-entering a distinction | Repeating a prime factor | Both are the same type drawn again |

The map is not an identity: a distinction is a logical act, while a prime is an arithmetic atom. The correspondence is structural, and its content must be judged by whether the two structures share laws beyond the relabeling.

### 3.2 Shared Structural Laws

The correspondence is nontrivial only if it preserves structure. Two shared laws are identified.

**Law 1 (nesting/hierarchy).** In the calculus of indications, a form is a hierarchy of nested distinctions: the whole is never larger than its largest part, in the sense that the form determined by a nested set is determined by the innermost boundary. In the prime tree, the strong triangle inequality

$$v_p(m+n) \geq \min\bigl(v_p(m), v_p(n)\bigr)$$

is the same statement: the depth of a sum never exceeds the minimum depth of its terms. Both structures are ultrametric; neither accumulates small deviations. This is a shared structural law, not a naming coincidence.

**Law 2 (multiplicativity of depth).** In the calculus of indications, drawing a new distinction adds a level; drawing the same type of distinction twice adds two levels. In the prime tree, the valuation is multiplicative:

$$v_p(mn) = v_p(m) + v_p(n).$$

Depth along a branch adds under composition in both structures. For composite bases the multiplicative law fails [@heydeman2018], which is precisely why primes are the branch types: prime labels are the ones for which depth is additive.

**Statement 2 [MAP — interpretive reading, defended].** The valuation-as-depth reading is a structure-preserving correspondence between the calculus of indications and the prime tree, in the sense that both structures satisfy a nesting/hierarchy law and a multiplicativity-of-depth law. *Falsifiability condition: the correspondence is disconfirmed if the shared laws reduce to relabeling — that is, if for every structural property of the prime tree there is a property of the calculus of indications that is preserved only by definition. The two laws above are offered as the test; a critic must show either that they are vacuous or that they hold between any two nested structures whatsoever.*

The Bayesian evidential-weight discipline applies: the correspondence was constructed to fit the structures, so it carries zero evidential weight as a prediction [KIF-60 classification: RETRODICTION]. It is presented as a reading, not as evidence. The test of the reading is whether it generates a falsifiable delta elsewhere — the candidate delta is stated in Section 5.

## 4. The Tensor Product as Multiplicative Branching

Quantum mechanics provides the natural arena for the reading, because the tensor product is multiplication in Hilbert space. For finite-dimensional systems,

$$\dim(H_A \otimes H_B) = \dim H_A \cdot \dim H_B.$$

Prime factorization of the composite dimension labels the branch types of the tensor product. For $n$ qubits,

$$\dim H = 2^n, \qquad v_2(\dim H) = n.$$

The 2-adic valuation of the dimension is the number of qubit tensor factors: it is the tensor-branch depth. For a general finite-dimensional system of dimension $d = \prod_p p^{e_p}$, the branch-depth is the tuple $(v_p(d))_p$ over all primes; the no-cloning diagonal argument of Section 5 holds for any $d > 1$ and does not depend on the valuation — the valuation provides the reading, not the proof. The tensor product is not a Cartesian product; it is a pairing that generates a new level of structure, exactly as multiplication generates a new dimension of distinctions in the arithmetic case.

The p-adic dimension-depth reading connects to the established p-adic structures in physics: p-adic string theory [@volovich1987], p-adic CFT as holographic tensor networks [@hung2019], and tensor networks over p-adic fields [@heydeman2018]. In those frameworks the p-adic tree is the geometry; here the p-adic valuation of dimension is the depth measure.

**Statement 3 [MAP — interpretive reading, developed].** For a composite quantum system, the prime factorization of the Hilbert-space dimension identifies the branch types of the tensor product, and $v_p(\dim H)$ counts the depth along the $p$-branch. *Falsifiability condition: this reading is disconfirmed if it yields no structural content beyond the standard multiplicativity of dimensions — that is, if $v_p(\dim H)$ tracks no feature of the tensor-product structure other than the dimension number itself. The candidate structural content is stated in Section 5 (the diagonal map and its absence).*

## 5. The Structural No-Cloning Reading

### 5.1 The Diagonal Map Is Nonlinear

The no-cloning theorem [@wootters1982; @dieks1982] states that there is no linear map (and no unitary map, with an ancilla) that sends every unknown state $\lvert\psi\rangle$ to its tensor square $\lvert\psi\rangle \otimes \lvert\psi\rangle$. The standard proof is a linearity argument. In the branch-depth vocabulary the statement acquires a structural form.

Let $H$ have dimension $d > 1$, and consider the diagonal map

$$\delta \colon H \to H \otimes H, \qquad \lvert\psi\rangle \mapsto \lvert\psi\rangle \otimes \lvert\psi\rangle.$$

For $\lvert\psi\rangle = a \lvert 0 \rangle + b \lvert 1 \rangle$,

$$\delta(\lvert\psi\rangle) = a^2 \lvert 00 \rangle + ab \lvert 01 \rangle + ab \lvert 10 \rangle + b^2 \lvert 11 \rangle.$$

The coefficients are quadratic in $a$ and $b$: the cross terms $ab$ are precisely the paired distinctions generated by the multiplication of the amplitudes. A linear map from $H$ to $H \otimes H$ can produce only coefficients linear in $a$ and $b$ along a fixed basis, so it cannot produce the cross terms for all states. The diagonal map is nonlinear.

Equivalently, the diagonal image

$$\{\lvert\psi\rangle \otimes \lvert\psi\rangle : \lvert\psi\rangle \in H\}$$

is not a linear subspace of $H \otimes H$ when $d > 1$: it is the Veronese embedding, a nonlinear subvariety, not a linear subspace. The no-cloning theorem is the statement that the tensor product has no linear diagonal.

### 5.2 The Category-Theoretic Statement

The categorical formulation is established: the category of Hilbert spaces with the tensor product is monoidal but not Cartesian [@coeckeduncan2011; @coeckepaquette2010]. In a Cartesian category every object has a natural diagonal map; in a monoidal category that is not Cartesian, no such natural diagonal exists. The no-cloning theorem is the physical face of this categorical fact. The forbidden diagonal is the same nonlinear map of Section 5.1. Related no-go results in the same family include the forbidden quantum adder [@alvarez2015], which proves that a natural nonlinear-looking operation on amplitudes is impossible under linearity.

The structural reading does not change the theorem. The contribution of the vocabulary is interpretive: the no-cloning theorem is read as the impossibility of linearly duplicating multiplicative branching. You cannot copy a distinction without drawing a new distinction.

### 5.3 The Branch-Depth Accounting

The p-adic dimension-depth suggests a branch-depth accounting. For $n$ qubits, $v_2(\dim H) = n$ is the number of tensor factors: the 2-adic depth is a count of qubit-branch levels. Cloning a state of a $d$-dimensional system would map a space of depth $v_p(d)$ to a space of depth $2 v_p(d)$, doubling every prime-branch depth. The obstruction is not the increase in depth — linear isometries can increase dimension — but the requirement that the increase follow the diagonal, which is not a linear subspace. The p-adic depth of the tensor square is doubled; the diagonal map that would realize the doubling is absent. Whether this accounting corresponds to a genuine resource monotone under allowed quantum operations is left as an open question (see the continuity registry, FQ3); the term "resource" is not claimed.

**Statement 4 [MAP — speculative, falsifiable].** The no-cloning theorem admits the structural reading: cloning would require the nonlinear diagonal map, whose image is not a linear subspace, and the p-adic valuation of dimension counts the branch depth that cloning would double. *Falsifiability condition: the reading is disconfirmed if it yields no explanatory or predictive content beyond the standard linearity proof of the no-cloning theorem — in particular, if no statement expressible in the branch-depth vocabulary (about tensor-factor depth, monogamy, or no-broadcasting) fails to follow from the standard formalism alone. The honest default is that this claim starts at [RETRODICTION — not evidence] and earns weight only by generating a delta; the candidate delta is RQ6 in Section 6.*

### 5.4 Adjacent Theorems

The no-broadcasting theorem and the monogamy of entanglement are adjacent no-go results. In the branch-depth vocabulary: broadcasting non-commuting states would require a common branch decomposition that incompatible observables do not share; monogamy reflects that a qubit's 2-adic depth $v_2(2) = 1$ is a single unit of entanglement resource, which cannot be shared with arbitrarily many parties. These statements are offered as vocabulary, not as new theorems; their content follows from the standard proofs.

## 6. The Adelic Frontier and the Limits of the Reading

### 6.1 Ostrowski and the Adelic Picture

Ostrowski's theorem provides the Archimedean and the p-adic absolute values as the only completions of the rationals. Standard quantum mechanics lives on the Archimedean branch: complex amplitudes and the Born rule depend on the usual absolute value. The p-adic branches are explored in p-adic string theory [@volovich1987] and p-adic holography [@hung2019; @heydeman2018]. An adelic formulation would treat all completions together.

The frontier question is whether the adelic completion of state space constrains any measurable prediction beyond the standard formalism. At present the question is open, and no falsifiable prediction is offered. The honest position is that the structural reading is an interpretation, and an adelic quantum mechanics that yields new predictions has not been constructed here.

### 6.2 Known Limits

Three limits are acknowledged. First, the categorical content of the structural no-cloning reading is established in the literature [@coeckeduncan2011; @coeckepaquette2010]; the present paper claims the vocabulary, not the fact. Second, the p-adic-QM and no-cloning intersection has no direct literature anchor found in the search for this paper: the statement that no-cloning holds in p-adic Hilbert spaces follows from linearity, but no source was located that states it, so it is not asserted as a literature-backed result. Third, a claim that a two-component Bose-Einstein condensate can bypass the no-cloning theorem [@datta2022] is noted adversarially: any bypass must involve nonlinear or effective dynamics or a different notion of cloning, and the standard linearity theorem is not contradicted.

## 7. Conclusion

The p-adic valuation is a measure of depth along a prime branch, not a measure of size. This reading, grounded in Ostrowski's theorem, is a structure-preserving correspondence between the calculus of indications and the prime tree, and it transfers to quantum mechanics, where the tensor product multiplies dimensions and the p-adic valuation of dimension counts tensor-branch depth. Within this vocabulary, the no-cloning theorem is the impossibility of linearly duplicating multiplicative branching: the diagonal map is nonlinear, and its image is not a linear subspace.

The reading is offered with explicit epistemic labels. The valuation-as-depth fact is mathematical and established. The bridge correspondence and the structural no-cloning reading are interpretive, carry zero evidential weight as predictions, and are subject to stated falsifiability conditions. The value of the reading is heuristic: it connects the calculus of indications, number theory, and quantum foundations under a common vocabulary of branching and depth, and it leaves open an adelic frontier question that is not yet empirically constrained.

## Declarations

**Funding.** This work received no external funding.

**Competing interests.** The author declares no competing interests.

**Data availability.** No experimental data were generated or analyzed for this work. All literature evidence is cited with persistent identifiers.

**Materials availability.** No new materials were generated.

**Code availability.** No code was required for the proofs in this work.

**Author contributions.** The author conceived the reading, developed the correspondence, and wrote the manuscript.

**Ethics approval.** Not applicable.

**Consent for publication.** The author consents to publication under the stated license.

**Preprint policy.** This manuscript is posted as a preprint; it has not been submitted to any journal.

## References

1. A. Ostrowski. Über einige Lösungen der Funktionalgleichung $\psi(x)\cdot\psi(x)=\psi(xy)$. *Acta Mathematica*, 41:271–284, 1916. doi:10.1007/bf02422947.
2. G. Spencer-Brown. *Laws of Form*. Julian Press, New York, 1969.
3. W. K. Wootters and W. H. Zurek. A single quantum cannot be cloned. *Nature*, 299:802–803, 1982. doi:10.1038/299802a0.
4. D. Dieks. Communication by EPR devices. *Physics Letters A*, 92(6):271–272, 1982. doi:10.1016/0375-9601(82)90084-6.
5. I. V. Volovich. p-adic string. *Classical and Quantum Gravity*, 4(4):L83–L87, 1987. doi:10.1088/0264-9381/4/4/003.
6. B. Coecke and R. Duncan. Interacting quantum observables: categorical algebra and diagrammatics. *New Journal of Physics*, 13(4):043016, 2011. doi:10.1088/1367-2630/13/4/043016.
7. B. Coecke and É. O. Paquette. Categories for the practising physicist. In *New Structures for Physics*, Lecture Notes in Physics 813, pages 173–286. Springer, 2010. doi:10.1007/978-3-642-12821-9_3.
8. L.-Y. Hung, W. Li, and C. M. Melby-Thompson. p-adic CFT is a holographic tensor network. *Journal of High Energy Physics*, 2019(04):170, 2019. doi:10.1007/jhep04(2019)170.
9. M. Heydeman, M. Marcolli, I. A. Saberi, and B. Stoica. Tensor networks, p-adic fields, and algebraic curves: arithmetic and the AdS3/CFT2 correspondence. *Advances in Theoretical and Mathematical Physics*, 22(1):93–176, 2018. doi:10.4310/atmp.2018.v22.n1.a4.
10. F. J. Varela. The extended calculus of indications interpreted as a three-valued logic. *Notre Dame Journal of Formal Logic*, 20(1):141–146, 1979. doi:10.1305/ndjfl/1093882412.
11. D. L. Rapoport. Surmounting the Cartesian cut through philosophy, physics, logic, cybernetics, and geometry: self-reference, torsion, the Klein bottle, the time operator, multivalued logics and quantum mechanics. *Foundations of Physics*, 39:767–800, 2009. doi:10.1007/s10701-009-9334-5.
12. A. Almheiri, X. Dong, and D. Harlow. Bulk locality and quantum error correction in AdS/CFT. *Journal of High Energy Physics*, 2015(04):163, 2015. doi:10.1007/jhep04(2015)163.
13. U. Alvarez-Rodriguez, M. Sanz, L. Lamata, and E. Solano. The Forbidden Quantum Adder. *Scientific Reports*, 5:11983, 2015. doi:10.1038/srep11983.
14. S. Datta. A two-component Bose-Einstein condensate can 'bypass' the no-cloning theorem. TechRxiv preprint, 2022. doi:10.36227/techrxiv.21716615.v1.
15. G. Niestegge. Non-classical conditional probability and the quantum no-cloning theorem. arXiv:1502.02151, 2015.
16. J. Isaacson and L. H. Kauffman. Recursive distinctioning. arXiv:1606.06965, 2016.
17. Z. Ji, Y.-K. Liu, and F. Song. Pseudorandom states, non-cloning theorems and quantum money. arXiv:1711.00385, 2017.
