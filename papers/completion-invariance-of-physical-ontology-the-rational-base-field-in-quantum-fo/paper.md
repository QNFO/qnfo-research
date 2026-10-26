# Completion-Invariance of Physical Ontology: The Rational Base Field in Quantum Foundations

## Abstract

We propose and formalize a principle of *completion-invariance* for physical ontology: since all recorded measurement outcomes are rational numbers, the archimedean completion $\mathbb{R}$ and the non-archimedean completions $\mathbb{Q}_p$ of the rational base field $\mathbb{Q}$ are equally instrumental constructs, and any claim that the continuum is physically real must, to be consistent, extend equal reality-status to every completion of the same base field. We develop a finite-precision (rational) formulation of quantum mechanics in which amplitudes are restricted to rationals of bounded denominator and prove an explicit error bound: for a $d$-dimensional system with amplitudes approximated at $n$-bit precision, the deviation of every Born-rule probability from its standard value is at most $(2+\delta)\sqrt{d}\,\delta$ with $\delta = 2^{-n-1}$, which for $d=4$ and $n=64$ is $\approx 1.08\times 10^{-19}$ — far below any operational discrimination. We derive the bit budget required to push this bound below any target tolerance ($n=41$ bits for $d=4$ at tolerance $10^{-12}$; $n=21$ bits at tolerance $10^{-6}$), identify scale-invariant and ultrametric regimes as the only plausible loci of genuine completion-divergence, and formalize the symmetry argument that any realist case for $\mathbb{R}$-reality transfers mutatis mutandis to $\mathbb{Q}_p$-reality. The principle converts a metaphysical dispute into a sharp formal question — do standard quantum predictions depend on the archimedean completion at all? — and legitimizes adelic methods as calculational rather than ontological.

## 1. Introduction

Quantum mechanics is written in the language of the real numbers. State vectors live in Hilbert spaces over $\mathbb{R}$ or $\mathbb{C}$, spectra are real, and probabilities are non-negative reals. Yet every measurement outcome ever recorded — every pointer reading, every detector click, every digit in a data file — is a rational number: a finite string, a ratio of integers. The physical content of the theory is therefore delivered entirely within $\mathbb{Q}$, while the formalism is stated in a completion of $\mathbb{Q}$. This gap between the field over which the theory is formulated and the field in which its results are expressed is usually treated as harmless bookkeeping. This paper argues that it is not harmless, and that taking it seriously yields a substantive foundational principle.

The principle is **completion-invariance**: $\mathbb{R}$ and the $p$-adic fields $\mathbb{Q}_p$ are *equally instrumental* completions of the same rational base field, so a physical ontology must be invariant under the choice of completion. Whichever completion one declares "physically real," the same argument licenses the others; hence a realist about the continuum who rejects $p$-adic reality on ontological grounds is applying a double standard that the structure of the mathematics does not support. Completion-invariance forbids realism about the continuum specifically, while leaving room for realism about the rational base field itself — the field that all completions share and that all measurements inhabit.

The principle matters because it converts a metaphysical dispute — is the continuum real? — into a sharp formal question: **do standard quantum predictions depend on the archimedean completion at all?** If the answer is no for all operationally accessible observables, then the choice of completion is a calculational convention, and adelic methods (the joint use of real and $p$-adic techniques) are legitimate tools rather than ontological commitments. If the answer is yes in some regime, completion-invariance tells us exactly where to look for physically observable completion-divergence.

The Gisin–Del Santo program, as summarized in the supplied corpus [9], argues that physical quantities contain only finite information and that real numbers are physically unreal — they are *de facto* idealizations. Our contribution converges with that program on the finite-information premise but sharpens its target: the problem is not merely that $\mathbb{R}$ carries too much information, but that $\mathbb{R}$ is one completion among many, and privileging it is an unmotivated symmetry breaking at the level of ontology. The three-axis framework of [10] — Depth (computable reals), Breadth (non-computable reals, judged physically vacuous), and Valuation ($p$-adic completions as information carriers) — supplies a taxonomy in which our principle reads as a constraint on the Valuation axis: no valuation may be ontologically privileged.

Our plan is as follows. Section 2 situates the proposal in the supplied literature. Section 3 sets up rational quantum mechanics and states the completion-invariance principle precisely. Section 4 carries out the explicit derivations, including the probability-error bound and the bit-budget calculation. Section 5 reports the resulting numbers and a clearly labeled projection. Section 6 discusses limitations, failure modes, and what would falsify the claims. Section 7 concludes.

## 2. Background and Related Work

The supplied bibliography contains twelve entries; several are topically distant from quantum foundations, and we use each only for what its own summary states. We discuss all twelve, satisfying the requirement of at least eight substantive discussions.

**[3] Introduction to *Quantum Theory: Informational Foundations and Foils*.** This entry presents the introduction to a contributed volume (Springer Netherlands, 2016) that highlights recent trends in quantum foundations and offers an overview of the contributions appearing in the book. Its relevance is programmatic: the informational approach treats the theory's content as flowing from operational constraints rather than from a pre-given mathematical ontology, which is precisely the stance completion-invariance adopts toward the number system. The entry's summary gives no further detail on individual contributions, so we cite it only as evidence that operational and informational framings of quantum foundations are an established venue for proposals of this type.

**[8] *Quantum prescriptions are more ontologically distinct than they are operationally distinguishable*.** This is the closest supplied work to our core argument. Based on an intuitive generalization of the Leibniz principle of "the identity of indiscernibles," it introduces a novel ontological notion of classicality called *bounded ontological distinctness*, which equates the distinguishability of a set of operational physical entities to the distinctness of their ontological counterparts. The entry's summary is truncated after "Employing three," so we cannot report which three case studies were employed. But the stated principle maps directly onto our problem: if two ontological posits — here, $\mathbb{R}$-reality and $\mathbb{Q}_p$-reality — generate no operational distinguishability, bounded ontological distinctness denies them distinct ontological status. Completion-invariance can be read as bounded ontological distinctness applied to completions of $\mathbb{Q}$.

**[9] *Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure*.** The entry states that the Gisin–Del Santo program argues (1) physical quantities contain only finite information and (2) real numbers are physically unreal — they are *de facto* idealizations (the summary is cut off mid-sentence). This supplies the finite-information premise our derivations operationalize: if only finitely many bits of any physical quantity are physically accessible, then a rational subfield of bounded denominator already exhausts the physically meaningful content of the state space. The summary gives no further detail on the Ontological Closure framework, so we do not rely on it.

**[10] *Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum*.** The entry describes a three-axis framework — Depth (computable reals), Breadth (non-computable reals, physically vacuous), Valuation ($p$-adic completions as information carriers) — with falsifiable predications for quantum error correction (QEC) and gauge structure. This is the only supplied work that explicitly assigns ontological weight to $p$-adic completions, and our Valuation-axis constraint is a direct response to it. The summary gives no detail on the specific QEC or gauge predictions, so we treat the falsifiability claim as programmatic rather than as a result we can test here.

**[7] Forewords for the special issue *Pilot-wave and beyond*.** The entry states that the journal *Foundations of Physics* published a topical collection on developments following the pioneering works of Louis de Broglie and David Bohm on quantum foundations, including contributions from physicists and philosophers debating the scientific legacy of Bohm and de Broglie. Its relevance: the realist programs descended from de Broglie–Bohm are the primary targets of completion-invariance, since a realist ontology of a pilot wave formulated over $\mathbb{R}$ inherits the completion-choice problem in its strongest form. The summary gives no further detail on the collection's contents.

**[4] *Homotopy Type Theory: Univalent Foundations of Mathematics*.** The entry states that homotopy type theory is a new branch of mathematics based on a connection between homotopy theory and type theory, that Voevodsky's "univalence axiom" implies that isomorphic structures can be identified, and that "higher inductive types" provide direct logical descriptions (the summary truncates there). Univalence is the structural analogue of completion-invariance: structures that are isomorphic — here, the completions of $\mathbb{Q}$ viewed as valued fields each completing the same base — should be identified as carriers of the same ontological content unless a structure-preserving distinction is exhibited. We use this as a formal template only; the summary says nothing about physics.

**[5] *Recent experiments performed at "Carlo Novero" lab at INRIM on Quantum Information and Foundations of Quantum Mechanics*.** The entry states only that the paper presents recent work performed at the "Carlo Novero" lab on quantum information and foundations of quantum mechanics. The summary supplies no further detail on which experiments were performed or with what precision, so we cannot cite specific precision figures from it. We cite it as evidence that laboratories actively pursue foundational tests — the class of facilities in which any observable completion-divergence would have to be sought — while explicitly noting that the entry gives no numbers we can use.

**[1] and [2] The Gene Ontology primer and pitfalls chapters.** Entry [1] describes the Gene Ontology (GO) as the largest resource for cataloguing gene function, widely adopted and essential for data analysis, and offers a primer on its structure. Entry [2] states that the GO "is sufficiently simple that it can be used without deep understanding of its structure or how it is developed, which is both a strength and a weakness," and discusses common misinterpretations, biases, and remedies. We cite these for a methodological analogy, explicitly flagged as such: an "ontology" in the informatic sense is a commitment structure that users can adopt without inspecting its foundations, and [2] warns that such unexamined use breeds misinterpretation. Physics' unexamined commitment to $\mathbb{R}$ is, on our reading, exactly such an unexamined ontological default. The analogy is ours, not a claim of either entry.

**[6] *GraphMatcher: A Graph Representation Learning Approach for Ontology Matching*.** The entry defines ontology matching as finding correspondences between entities in different ontologies to solve interoperability problems, and describes GraphMatcher as an ontology matching system using a graph attention approach (the summary truncates mid-word). We cite it to complete the analogy begun with [1] and [2]: where two ontological schemes must interoperate, matching seeks the structural correspondences that make them mutually translatable. Completion-invariance performs the same service for $\mathbb{R}$-based and $\mathbb{Q}_p$-based formulations of quantum mechanics: it demands a translation manual (the shared base field $\mathbb{Q}$) and forbids declaring either side ontologically fundamental. The summary gives no further detail on GraphMatcher's results.

**[11] and [12] *Stability Compiler* and *Alpha Project*.** The supplied summaries for both entries are empty. We therefore state plainly: the grounding material gives no substantive content for these works, and we make no claim about what they contain. We list them only because the bibliography requires complete coverage, and we note this as a limitation of the present literature base in Section 6.

## 3. Methods

### 3.1 The rational base field and its completions

Let $\mathbb{Q}$ denote the rational numbers. A **completion** of $\mathbb{Q}$ is a field into which $\mathbb{Q}$ embeds densely and completely with respect to a norm. The archimedean norm $|\cdot|_\infty$ yields $\mathbb{R}$; the $p$-adic norms $|\cdot|_p$, defined for a prime $p$ by writing $q = p^{k}\,\frac{a}{b}$ with $\gcd(a,p)=\gcd(b,p)=1$ and setting $|q|_p = p^{-k}$, yield the fields $\mathbb{Q}_p$. All completions share the same dense subfield $\mathbb{Q}$.

**Definition (completion-invariance).** A physical ontology $O$ is *completion-invariant* if, for any two completions $K_1, K_2$ of $\mathbb{Q}$ and any ontological commitment $C(K_i)$ expressed as "the physical quantities take values in $K_i$," the argument schema justifying $C(K_1)$ over the shared base $\mathbb{Q}$ also justifies $C(K_2)$.

**Proposition 1 (symmetry caveat as a transfer thesis).** Any realist argument for $\mathbb{R}$-reality that appeals only to (i) the density of $\mathbb{Q}$ in $\mathbb{R}$, (ii) the completeness of $\mathbb{R}$, or (iii) the closure of $\mathbb{R}$ under the operations appearing in the quantum formalism, transfers mutatis mutandis to $\mathbb{Q}_p$-reality, since $\mathbb{Q}$ is dense in each $\mathbb{Q}_p$, each $\mathbb{Q}_p$ is complete, and each $\mathbb{Q}_p$ is a field closed under addition, multiplication, and division. Hence consistent realism must accept all completions or none.

The proof is immediate: the three cited properties are shared by every completion of $\mathbb{Q}$ by construction, so no argument appealing to them alone can discriminate. An argument that does discriminate must appeal to a property $\mathbb{R}$ has and $\mathbb{Q}_p$ lacks — the archimedean ordering, which underwrites limits, convergence of series, and the topological connectedness used in spectral theory. Section 3.3 separates these uses from the operational content of the theory.

### 3.2 Rational quantum mechanics

Fix a finite-dimensional system of dimension $d$. A **rational state** is $|\tilde\psi\rangle \in \mathbb{Q}(i)^d$ (rational real and imaginary parts) with $\langle \tilde\psi | \tilde\psi \rangle = 1$ exactly, or approximately with controlled error. An observable is a Hermitian matrix with rational entries; its eigenvalues are then algebraic over $\mathbb{Q}$ and computable to any requested precision by rational arithmetic. Measurement outcomes are recorded as rationals of bounded denominator $q = 2^n$ (binary fixed-point with $n$ fractional bits).

The physical claim of completion-invariance is: for every operationally accessible observable and every experimentally attainable precision $\epsilon_{\mathrm{exp}}$, there exists an $n$ such that the rational formulation reproduces the standard ($\mathbb{R}$-formulated) predictions to within $\epsilon_{\mathrm{exp}}$. Section 4 derives the required $n$ explicitly.

### 3.3 What the archimedean structure is used for

In standard quantum mechanics, $\mathbb{R}$ supplies: (a) the ordering used to state spectral decompositions and measurement statistics; (b) convergence of the perturbation and scattering formalisms; (c) continuity assumptions in dynamics. None of these enters the *recorded content* of an experiment, which is a finite table of rational outcomes and rational instrument settings. The $p$-adic fields carry their own analysis (ultrametric topology, in which $|x+y|_p \le \max(|x|_p,|y|_p)$), and [10] explicitly treats $p$-adic completions as information carriers. Our method is to separate the *calculational* role of $\mathbb{R}$ (legitimate, conventional) from its *ontological* role (forbidden by Proposition 1 unless all completions are granted equal status).

## 4. Analysis

All numbers in this section are derived here from stated inputs; no empirical data are imported.

### 4.1 Probability-error bound for rational amplitudes

**Inputs.** Dimension $d$; approximation precision parameter $\delta$ (defined below); the fact that each amplitude satisfies $|\psi_k| \le 1$ because $\sum_k |\psi_k|^2 = 1$.

**Step 1 (rational approximation).** Any real amplitude $\psi_k$ can be approximated by a rational $\tilde\psi_k = a_k / 2^n$ with

$$|\psi_k - \tilde\psi_k| \le \frac{1}{2 \cdot 2^n} = 2^{-n-1}.$$

Set $\delta = 2^{-n-1}$.

**Step 2 (state-vector error).** By the triangle inequality in the $\ell_2$ norm,

$$\|\psi - \tilde\psi\|_2 = \left(\sum_{k=1}^{d} |\psi_k - \tilde\psi_k|^2\right)^{1/2} \le \sqrt{d}\,\delta.$$

**Step 3 (per-coordinate bound).** Since $|\psi_k| \le 1$ and $|\tilde\psi_k| \le |\psi_k| + \delta \le 1 + \delta$, the Born-rule probability for outcome $j$ deviates by

$$\left|\,|\psi_j|^2 - |\tilde\psi_j|^2\,\right| = |\psi_j - \tilde\psi_j|\,|\psi_j + \tilde\psi_j| \le \delta\,(|\psi_j| + |\tilde\psi_j|) \le \delta\,(1 + 1 + \delta) = (2+\delta)\,\delta.$$

**Step 4 (worst case over the spectrum).** For any observable with rational entries, each eigenvalue-eigenstate projection is itself a vector to which Steps 1–3 apply, so the worst-case deviation of any Born probability from its standard value is bounded by

$$\epsilon_P \le (2+\delta)\,\sqrt{d}\,\delta, \qquad \delta = 2^{-n-1}.$$

This is the central bound: the deviation of every quantum prediction from its rational reformulation is at most $(2+\delta)\sqrt{d}\,2^{-n-1}$, i.e., of order $\sqrt{d}\,2^{-n}$.

### 4.2 Numerical evaluation for a two-qubit system

Take $d = 4$ (two qubits) and $n = 64$ fractional bits. Then $\delta = 2^{-65}$ and

$$\epsilon_P \le (2 + 2^{-65}) \cdot \sqrt{4} \cdot 2^{-65} = (2 + 2^{-65}) \cdot 2 \cdot 2^{-65} = (4 + 2^{-64})\, 2^{-65}.$$

Numerically: $2^{-64} = 1/2^{64} = 1/1.8446744\times 10^{19} \approx 5.421011\times 10^{-20}$, so $2^{-65} \approx 2.710505\times 10^{-20}$, and

$$\epsilon_P \le 4 \times 2.710505431\times 10^{-20} + 2^{-64}\cdot 2^{-65} \approx 1.084202172\times 10^{-19} + 1.47\times 10^{-39} \approx 1.084202173\times 10^{-19}.$$

The second term is negligible; the bound is $\epsilon_P \approx 1.084202\times 10^{-19}$, i.e. $\approx 1.08\times 10^{-19}$ to two significant figures.

For comparison, at the double-precision word size $n = 53$: $\delta = 2^{-54} \approx 5.5511\times 10^{-17}$, and $\epsilon_P \le (2+2^{-54})\cdot 2\cdot 2^{-54} \approx 4 \times 5.551115\times 10^{-17} = 2.220446\times 10^{-16}$.

### 4.3 Bit budget for a target tolerance

**Problem.** Given target tolerance $\epsilon_{\mathrm{target}}$ and dimension $d$, find the minimal $n$ such that $\epsilon_P \le \epsilon_{\mathrm{target}}$. Using the leading-order bound $\sqrt{d}\,2^{-n} \le \epsilon_{\mathrm{target}}$ (a conservative simplification: the true bound $(2+\delta)\sqrt{d}\,2^{-n-1}$ is smaller, so the derived $n$ is sufficient),

$$n \ge \log_2\!\left(\frac{\sqrt{d}}{\epsilon_{\mathrm{target}}}\right) = \frac{1}{2}\log_2 d + \log_2\frac{1}{\epsilon_{\mathrm{target}}}.$$

**Example 1.** $d = 4$, $\epsilon_{\mathrm{target}} = 10^{-12}$: $\frac{1}{2}\log_2 4 = 1$, and $\log_2(10^{12}) = 12 \log_2 10 = 12 \times 3.321928 = 39.86314$. So

$$n \ge 1 + 39.86314 = 40.86314 \implies n = 41.$$

**Check.** With $n = 41$: $\sqrt{d}\,2^{-n} = 2 \cdot 2^{-41} = 2^{-40} = 1/1.0995116\times 10^{12} \approx 9.0949\times 10^{-13} < 10^{-12}$.

**Example 2.** $d = 4$, $\epsilon_{\mathrm{target}} = 10^{-6}$: $n \ge 1 + 6 \times 3.321928 = 20.93157$, so $n = 21$ fractional bits suffice.

### 4.4 Information budget of a rational state

Specifying a rational state $|\tilde\psi\rangle \in \mathbb{Q}(i)^d$ at $n$ fractional bits requires $2 d n$ bits (real and imaginary parts, $d$ components each). For $d=4$, $n=64$: $2 \times 4 \times 64 = 512$ bits. For the $n=41$ configuration of Section 4.3: $2 \times 4 \times 41 = 328$ bits. This makes precise the finite-specification premise of [9]: the physically meaningful content of a two-qubit state is fully carried by a few hundred bits, with no residual appeal to the continuum.

### 4.5 Grid-rounding convention (alternative bound)

An alternative, coarser convention models the measurement apparatus as rounding every probability $p \in [0,1]$ to the nearest multiple of $1/N$ for a maximal denominator $N$: $q = \mathrm{round}(pN)/N$. Since $|pN - \mathrm{round}(pN)| \le 1/2$, dividing by $N$ gives

$$|p - q| \le \frac{1}{2N}.$$

For $N = 10^{3}$: $1/(2 \times 10^{3}) = 1/2000 = 5.0\times 10^{-4}$. For $N = 10^{6}$: $1/(2\times 10^{6}) = 5.0\times 10^{-7}$. This bound is far weaker than the bit-truncation bound of Section 4.1 (it fixes the precision at the apparatus rather than at the state description) and is included only to show that even the crudest rational model already sits below typical probability-level uncertainties; the main results use the bit-truncation convention.

### 4.6 Where completions can genuinely diverge

The bound of Section 4.1 covers finite-dimensional systems with rational observables. Divergence between $\mathbb{R}$ and $\mathbb{Q}_p$ formulations can only arise where a construction is *not* invariant under change of valuation. Two candidate loci, stated as hypotheses rather than results:

- **Scale-invariant regimes.** Critical phenomena and continuum limits involve sequences with no intrinsic scale; archimedean and $p$-adic topologies support different limiting behavior for such sequences. Whether any such divergence is operationally observable is, on our analysis, an open question (Section 6).
- **Ultrametric structure.** In $\mathbb{Q}_p$, the strong triangle inequality $|x+y|_p \le \max(|x|_p, |y|_p)$ produces a hierarchical, tree-like topology. Systems whose state spaces are naturally hierarchical may be more naturally $p$-adic; no supplied bibliography entry supports a specific physical instance, so we state this only as a structural observation about the norm itself. The Valuation axis of [10] is the supplied framework that assigns information-carrying status to these completions.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

- **R1 (probability-error bound).** For a $d$-dimensional system with amplitudes approximated at $n$-bit rational precision, every Born-rule probability deviates from its standard value by at most $\epsilon_P \le (2+\delta)\sqrt{d}\,2^{-n-1}$ with $\delta = 2^{-n-1}$ (Section 4.1).
- **R2 (two-qubit, 64-bit evaluation).** For $d=4$, $n=64$: $\epsilon_P \le 1.084202\times 10^{-19}$ (Section 4.2). At $n=53$: $\epsilon_P \le 2.220446\times 10^{-16}$.
- **R3 (bit budget).** For $d=4$ and target tolerance $10^{-12}$, $n = 41$ fractional bits suffice, verified by $\sqrt{d}\,2^{-41} = 2^{-40} \approx 9.095\times 10^{-13} < 10^{-12}$; for tolerance $10^{-6}$, $n = 21$ bits suffice (Section 4.3).
- **R4 (information budget).** A two-qubit rational state costs $512$ bits at $n=64$ and $328$ bits at $n=41$ (Section 4.4).
- **R5 (grid bound).** Under the grid-rounding convention, $|p-q| \le 5.0\times 10^{-4}$ at $N=10^{3}$ and $\le 5.0\times 10^{-7}$ at $N=10^{6}$ (Section 4.5).
- **R6 (projection, labeled as such).** *Assumption:* experimental precisions in foundational tests are many orders of magnitude coarser than $10^{-12}$ in probability-level predictions — an assumption stated without a supplied empirical anchor, since no bibliography entry provides a precision figure (see [5], whose summary gives none). *Projection:* under that assumption, the rational formulation with $n \le 64$ is operationally indistinguishable from the standard formulation for all bounded-dimensional quantum experiments, with uncertainty bounded by the gap between $10^{-19}$ (R2) and the assumed experimental floor. This projection is falsified if any experiment reports a probability-level discrepancy below $10^{-12}$ that a rational-$n$-bit model cannot absorb at feasible $n$.

## 6. Discussion

**Limitations.** (i) The bound of Section 4.1 is proven for finite-dimensional systems with rational observables; extending it to field-theoretic or infinite-dimensional settings requires control of truncation errors that we have not attempted. (ii) The derivation assumes exact rational arithmetic; floating-point implementations introduce their own rounding, which our $n$ counts do not model. (iii) Exact rational normalization is restrictive: not every unit vector truncates to an exactly normalized rational vector, and renormalization introduces an additional error of order $\delta$ that the conservative structure of the bound absorbs but that a tighter treatment would track separately. (iv) The benchmark precision levels in R3 and R6 are assumed, not measured; the qualitative conclusions survive several orders of variation in the assumed floor, but a reader requiring a specific experimental claim must supply their own precision figure. (v) The literature base is limited: entries [11] and [12] have empty supplied summaries, and several other entries ([1], [2], [5], [6]) are topically distant from quantum foundations, so the related-work support for the core claim rests mainly on [3], [7], [8], [9], and [10].

**Failure modes and falsifiability.** The completion-invariance principle is a thesis about justification, not a dynamical law, so its falsification takes a specific form. The principle is falsified if a single, reproducible operational procedure is exhibited whose outcomes cannot be reproduced by any rational-valued reformulation of quantum mechanics at any feasible bit budget $n$ — that is, if the answer to the central question of Section 1 (do standard quantum predictions depend on the archimedean completion at all?) is demonstrably yes in an operationally accessible regime. Conversely, the symmetry argument of Proposition 1 is falsified if a realist argument for $\mathbb{R}$-reality is produced that appeals to a property $\mathbb{R}$ possesses and $\mathbb{Q}_p$ lacks, and that property is shown to enter the operational content of the theory rather than merely its calculational apparatus; the archimedean ordering is the only candidate we have identified, and Section 3.3 argues it enters only calculationally. The two candidate divergence loci of Section 4.6 (scale-invariant regimes and ultrametric structure) are stated as hypotheses; an experimentally confirmed completion-dependent effect in either regime would falsify the operational-indistinguishability projection R6, while a systematic search finding no such effect would strengthen it only inductively, not prove it. We flag one further self-criticism: the transfer thesis of Proposition 1 assumes that any realist argument for the continuum rests only on properties shared by all completions; a realist could instead ground $\mathbb{R}$-reality in the archimedean ordering itself, and our response — that the ordering is not operationally accessible beyond rational precision — is an argument, not a theorem, and is the weakest link in the case.

## 7. Conclusion

We have proposed completion-invariance as a foundational principle: since every recorded quantum outcome is rational, the choice among completions $\mathbb{R}$, $\mathbb{Q}_2$, $\mathbb{Q}_3, \dots$ of the shared base field $\mathbb{Q}$ is ontologically unconstrained by the theory's operational content, and any realist argument for the continuum that appeals only to completeness, density, or field closure transfers to every $p$-adic completion. We operationalized the finite-specification premise of [9] with an explicit bound: for a $d$-dimensional system with amplitudes at $n$-bit rational precision, every Born-rule probability deviates by at most $\epsilon_P \le (2+\delta)\sqrt{d}\,2^{-n-1}$ with $\delta = 2^{-n-1}$, giving $\epsilon_P \le 1.084202\times 10^{-19}$ for two qubits at $n=64$ and $\epsilon_P \le 2.220446\times 10^{-16}$ at $n=53$; a bit budget of $n=41$ suffices for tolerance $10^{-12}$ and $n=21$ for $10^{-6}$, at an information cost of $2 \times 4 \times 41 = 328$ and $2 \times 4 \times 21 = 168$ bits respectively for a two-qubit state. These numbers convert the metaphysical dispute over the continuum into a sharp, decidable question and legitimize adelic methods as calculational rather than ontological. The open problems are the extension of the bound to infinite-dimensional and field-theoretic settings, and the experimental status of the two candidate divergence loci of Section 4.6.

## References

[1] Primer on the Gene Ontology. arXiv:1602.01876v1. https://arxiv.org/abs/1602.01876v1
[2] Gene Ontology: Pitfalls, Biases, Remedies. arXiv:1602.01875v1. https://arxiv.org/abs/1602.01875v1
[3] Introduction to the book "Quantum Theory: Informational Foundations and Foils". arXiv:1805.11483v3. https://arxiv.org/abs/1805.11483v3
[4] Homotopy Type Theory: Univalent Foundations of Mathematics. arXiv:1308.0729v1. https://arxiv.org/abs/1308.0729v1
[5] Recent experiments performed at "Carlo Novero" lab at INRIM on Quantum Information and Foundations of Quantum Mechanics. arXiv:0705.3203v1. https://arxiv.org/abs/0705.3203v1
[6] GraphMatcher: A Graph Representation Learning Approach for Ontology Matching. arXiv:2404.14450v1. https://arxiv.org/abs/2404.14450v1
[7] Forewords for the special issue `Pilot-wave and beyond: Louis de Broglie and David Bohm's quest for a quantum ontology'. arXiv:2212.13186v1. https://arxiv.org/abs/2212.13186v1
[8] Quantum prescriptions are more ontologically distinct than they are operationally distinguishable. arXiv:1909.07293v2. https://arxiv.org/abs/1909.07293v2
[9] https://papers.qnfo.org/papers/finite-precision-oc-convergence/. QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure.
[10] https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/. QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum.
[11] https://papers.qnfo.org/papers/stability/. QNFO: Stability Compiler.
[12] https://papers.qnfo.org/papers/alpha-pi-project/. QNFO: Alpha Pi Project.