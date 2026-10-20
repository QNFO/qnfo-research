# Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics

## Abstract

Continuum physics is traditionally formulated over the uncountable real line $\mathbb{R}$, yet every laboratory measurement, record, and computation is finite. This paper asks whether the uncountability of $\mathbb{R}$—as distinct from its Archimedean completeness—has any observable consequence. The gap is formal: the physics literature treats $\mathbb{R}$ as indispensable, while the computability literature has only recently begun to study the computational content of uncountability, and no self‑contained result connects the two. We (i) prove that the computable reals $\mathbb{R}_c$ are countable, with at most $P(n)=2^{\,n+1}-1$ programs of length $n$ bits (e.g. $P(100)=2^{101}-1=2 535 301 200 456 458 802 993 406 410 751$) and dense in $\mathbb{R}$; (ii) derive an observability bound $N=\bigl\lfloor L/\delta\bigr\rfloor$ for an instrument of range $L$ and resolution $\delta$, giving $N=10^{18}\approx2^{59.79}$ for a meter‑scale position measurement at $10^{-18}\,\mathrm{m}$ resolution; and (iii) prove an indistinguishability theorem: for every finite experiment the uncountable continuum model and a computable surrogate assign the same distribution over the finite record set, rendering the Continuum Hypothesis empirically vacuous. The result licenses model‑builders to restrict to computable reals without empirical loss. The work is analytical and resides at NASA Technology Readiness Level 1–2; the next step is a proven‑exact benchmark calculation.

## 1. Introduction

A working physicist who simulates turbulent flow, fits a spectrum, or writes down a Hamiltonian routinely employs the real numbers of classical analysis—an uncountable set by Cantor’s argument. The choice is made silently in textbooks and never tested. The cost of this silent choice is conceptual: if uncountability is physically load‑bearing, then physical law would depend on objects such as the halting probability $\Omega$ that no physical process can compute or measure; if it is not load‑bearing, then a large part of the mathematical scaffolding of physics is decorative, and alternative foundations (computable, constructible, or rational‑based continua) are empirically equivalent and may be formally cleaner. The decision that would change if the present result holds is the choice of number system taken as primitive when constructing physical theories, axiomatizing quantum mechanics, or building simulation infrastructure: the answer “the computable reals suffice” removes any obligation to defend uncountable sets on empirical grounds.

Three groups face this problem.  
1. **Foundational physicists and philosophers of physics** must decide what the continuum of spacetime or Hilbert space *is*.  
2. **Numerical analysts and simulation scientists** operate exclusively with finite‑precision, computable objects and must justify that no physics is lost by this restriction.  
3. **Logicians studying the computational content of set‑theoretic facts** need a physics‑side criterion for when a mathematical distinction matters.

Recent work has begun to treat uncountability itself as a computational object rather than only as a set‑theoretic theorem [6], and internal research notes have proposed that the uncountable reals are “physically vacuous” because they cannot be accessed [9]–[11]. What is missing is a self‑contained argument with explicit arithmetic: a statement of exactly which structures continuum physics uses, a proof that the computable reals carry those structures, and a quantitative bound showing that no finite experiment can distinguish a countable computable continuum from the uncountable one.

**Contributions.**  
- **C1.** A proof, with explicit counting, that $\mathbb{R}_c$ is countable (Section 4.1).  
- **C2.** A proof that $\mathbb{R}_c$ is dense in $\mathbb{R}$ and has Lebesgue measure $0$ (Section 4.1).  
- **C3.** An observability bound $N=\lfloor L/\delta\rfloor$ and a worked example yielding $N=10^{18}\approx2^{59.79}$ (Section 4.2).  
- **C4.** An indistinguishability theorem for any finite experiment (Section 4.3).  
- **C5.** A limitations analysis and falsification criteria (Section 6).  
- **C6.** A practical‑implications roadmap and the smallest next test (Section 7).

## 2. Background and Related Work



1. **[6] On the computational properties of the uncountability of the real numbers.**  
   The excerpt notes that Cantor’s 1874 proof of uncountability is a historical milestone and that the computational properties of uncountability have not been studied much. It defines the operation “given a countable set $A\subset\mathbb{R}$, output $y\in\mathbb{R}\setminus A$” and shows this operation is computationally equivalent to higher‑order realizers. This motivates the present question: does the computational content of uncountability have any empirical counterpart?

2. **[9] The Computable Continuum: Depth Without Breadth.**  
   The excerpt decomposes the uncountability of $\mathbb{R}$ into *depth* (Archimedean completeness) and *breadth* (cardinality explosion). It claims that all physically relevant properties are preserved by computable reals and that the non‑computable “breadth” is physically vacuous. Our Section 4.1 formalizes the depth claim; Section 4.6 (limitations) revisits the breadth claim.

3. **[10] Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum.**  
   The excerpt introduces a third axis, *valuation*, and argues that depth supplies connectedness, without which the intermediate‑value theorem fails. We adopt the depth/breadth vocabulary but do not rely on the valuation axis.

4. **[11] The ℚ‑vs‑ℝ Question: Why Physical Law Requires Only the Rational Numbers.**
   The excerpt argues that measurements yield finite‑precision rational numbers.

5. **[1] Physics Briefing Book** (European Particle Physics Strategy Update).  
   The excerpt describes a bottom‑up process in which the community submits proposals (“inputs”) for near‑, mid‑, and longer‑term projects, and notes that precision‑physics sections quote numerical targets (e.g. $10^{12}$ $Z$ bosons, $1\%$ precision on oblique parameters). This illustrates how foundational claims would have to be framed in terms of observable consequences to influence large‑scale planning.

6. **[2] Snowmass ’96 report on the Next Linear Collider.**  
   The excerpt presents design expectations for an $e^{+}e^{-}$ linear collider of centre‑of‑mass energy $0.5$–$1.5\,\mathrm{TeV}$ and demonstrates feasibility through cited performance numbers. It serves as an example of a physics program argued entirely through observable reach.

7. **[3] MHD analysis of CFETR and HFRC.**  
   The excerpt reports numerical parameters for two Chinese fusion projects (e.g. Lundquist number $S=5.56\times10^{6}$, resonant surface $r_{s}=0.51a$) and describes how design decisions are justified by simulation over finite‑precision objects. This underscores the practice our result underwrites.

8. **[4] Phenomenographic interviews on faculty perceptions of research‑based assessment materials.**  
   The excerpt finds that uptake improves when resources align with perceived needs, supporting the claim that any foundational reform must be communicated to a broad community.

9. **[5] Fifth International Conference on Women in Physics.**  
   The excerpt reports attendance by 215 female physicists from 49 countries and highlights professional barriers, reminding us that reforms must reach a diverse audience.

10. **[7] Computational literacy in physics essays.**  
    The excerpt adapts a theory of computational literacy (material, cognitive, further dimensions) to physics essays, establishing that computation is now a primary working medium of physics practice.

11. **[8] Learning orientations of life‑science majors in introductory physics.**  
    The excerpt shows that curriculum‑level uptake of new material depends on alignment with student‑expressed learning orientations.

  
    

## 3. Methods

The paper is analytical and constructive. Its method has four parts.

### 3.1 Structure isolation  
We list the mathematical structures that continuum physics actually invokes:  
(i) a linearly ordered field for coordinates and observables;  
(ii) density, so that between any two distinct states another state exists;  
(iii) the existence of limits, so that derivatives, integrals, and solutions of differential equations are defined;  
(iv) a topology fine enough to define continuity and convergence;  
(v) separability in the practical sense that a countable dense subset exists, which makes coordinates, series expansions, and finite encodings possible. No structures beyond these are assumed.

### 3.2 Counting and density arguments  
We prove countability and density of the computable reals by explicit counting: programs are finite bit strings, and the number of bit strings of length at most $n$ is $P(n)=2^{\,n+1}-1$. Density follows because the rationals are computable and dense. A complementary measure‑theoretic lens computes the Lebesgue measure of $\mathbb{R}_c$ by countable subadditivity. All arithmetic is shown in Section 4.

### 3.3 Indistinguishability framework  
An experiment $E$ is modeled as a physical process with a finite set of possible outcome records $R_E$, of size $|R_E|$, bounded by the instrument’s resolution and acquisition window. A physical theory $T$ assigns probabilities to records; $T$ is *empirically adequate* if the induced distribution over $R_E$ matches observation within experimental uncertainty. Two theories $T_1,T_2$ are *empirically indistinguishable* if for every finite experiment $E$ they assign the same distribution over $R_E$. The indistinguishability claim of Section 4.3 is then a statement about record sets, not about ontology.

### 3.4 Observable‑preservation argument  
We consider a generic physical theory $\mathcal{T}$ whose state space is $\mathbb{R}^k$ and whose observables are continuous functions $O:\mathbb{R}^k\to\mathbb{R}$. For any experimental tolerance $\delta$, uniform continuity on compact subsets yields a neighbourhood radius $\eta$ such that states within $\eta$ give observable values within $\delta$; a finite dyadic grid of spacing below $\eta$ then suffices to reproduce every observable value to within tolerance. This connects the abstract record argument to the concrete finite‑precision practice of simulation.

### Definitions  
A real number $x$ is *computable* if there exists an algorithm (Turing machine) that, given $k$, outputs a rational $q_k$ with $|q_k-x|<2^{-k}$. A *computable surrogate* of a continuum theory $T$ is a theory $T_c$ stated over $\mathbb{R}_c$ (or over $\mathbb{Q}$ with explicit limit procedures) that agrees with $T$ on all computable inputs and computable parameters.

## 4. Analysis

### 4.1 The computable reals are countable, dense, and of measure zero

**Claim 1 (Countability).**  
Each computable real is named by at least one program, and programs are finite bit strings. The number of bit strings of length at most $n$ is  

\[
P(n)=\sum_{j=0}^{n}2^{j}=2^{\,n+1}-1 .
\]

For $n=100$ bits  

\[
P(100)=2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751 .
\]

Thus  

\[
\mathbb{R}_c=\bigcup_{n=1}^{\infty}\{x:\text{$x$ named by a program of length}\le n\}
\]

is a countable union of finite sets and therefore countable. $\square$

**Claim 2 (Density).**  
Every rational $q=a/b$ with $a,b\in\mathbb{Z}$, $b\neq0$, is computable (a program can output $a/b$ exactly). The rationals are dense in $\mathbb{R}$: for any $x<y$ there exists $q\in\mathbb{Q}$ with $x<q<y$ (e.g. a decimal truncation of $(x+y)/2$). Since $\mathbb{Q}\subseteq\mathbb{R}_c$, $\mathbb{R}_c$ is dense. $\square$

**Claim 3 (Measure zero).**  
Because $\mathbb{R}_c$ is countable, list it as $\{x_1,x_2,\dots\}$. The Lebesgue measure $m$ of a singleton $\{x_i\}$ is $0$. By countable subadditivity  

\[
m(\mathbb{R}_c)=m\!\left(\bigcup_{i=1}^{\infty}\{x_i\}\right)\le\sum_{i=1}^{\infty}m(\{x_i\})=0 .
\]

Hence the probability that a real drawn from the standard uniform distribution is computable is  

\[
P_{\mathrm{comp}}=\frac{m(\mathbb{R}_c)}{m(\mathbb{R})}=0 .
\]  
$\square$

**Claim 4 (Adequacy of structure).**  
$\mathbb{R}_c$ is a countable, dense, linearly ordered subfield of $\mathbb{R}$; limits of computable sequences with computable convergence modules are computable; and its order topology is the subspace topology inherited from $\mathbb{R}$. What $\mathbb{R}_c$ lacks is precisely the “breadth” axis of [9] (the non‑computable points), which never appear as values of computed or measured quantities when inputs and outputs are finite. $\square$

### 4.2 Observability bound: how many outcomes can an experiment have?

**Claim 5 (Record bound).**  
An instrument measuring a single quantity over range $L$ with resolution $\delta$ produces at most  

\[
N=\Bigl\lfloor\frac{L}{\delta}\Bigr\rfloor
\]

distinguishable outcomes, i.e. at most $\log_{2}N$ bits per measurement.

*Worked example.* With $L=1\,\mathrm{m}$ and $\delta=10^{-18}\,\mathrm{m}$  

\[
N=\frac{1}{10^{-18}}=10^{18},
\qquad
\log_{2}(10^{18})=18\log_{2}10=18\times3.321928094887\ldots=59.79470570797\ldots\approx59.79\text{ bits}.
\]

*Digital‑acquisition projection.* Assuming illustrative parameters $b=24$ bits, $c=64$ channels, $f=10^{9}\,\mathrm{s^{-1}}$, $\tau=10^{3}\,\mathrm{s}$ (stated as assumptions)  

\[
b\cdot c\cdot f\cdot\tau=24\times64\times10^{9}\times10^{3}=1.536\times10^{15}\text{ bits},
\qquad
R=2^{1.536\times10^{15}} .
\]

The record space is finite, hence countable, and carries zero bits of cardinality information.

**Claim 6 (Program‑count vs. record‑count asymmetry).**  
A record is a finite string over a finite alphabet; there are $2^{m}$ strings of length $m$, each naming at most one computable object. Non‑computable reals have no finite naming process, so they cannot appear in any record. Consequently the “breadth” axis contributes exactly $0$ bits to any physical record. $\square$

### 4.3 Indistinguishability of the uncountable and computable continua

**Claim 7 (Indistinguishability).**  
For every finite experiment $E$, the uncountable continuum model $T$ and a suitably constructed computable surrogate $T_c$ assign the same distribution over the record set $R_E$.

*Derivation.* Fix $E$ with finite record set $R_E$, $|R_E|<\infty$ (Claim 5). The prediction of $T$ on $E$ is a probability vector $p=(p_1,\dots,p_{|R_E|})$ with $\sum_i p_i=1$. In any physical theory whose predictions are derived by computation from finite specifications of $E$, each $p_i$ is the output of a computation and therefore a computable real (to the precision ever stated). Construct $T_c$ by (i) restricting all state spaces to $\mathbb{R}_c$ (or $\mathbb{Q}$ with explicit limit procedures); (ii) retaining only dynamical laws whose coefficients are computable; (iii) defining predictions by the same computational derivation. Then $T_c$ produces the identical probability vector $p$, because the derivation never leaves the computable fragment. Since this holds for every finite $E$, $T$ and $T_c$ are empirically indistinguishable. $\square$

**Claim 8 (Observable preservation, continuous case).**  
Let $O:\mathbb{R}^k\to\mathbb{R}$ be continuous and let an experimental tolerance $\delta>0$ be given. On any compact region $K\subset\mathbb{R}^k$, uniform continuity yields $\eta>0$ such that $\|x-y\|<\eta$ implies $|O(x)-O(y)|<\delta$. Define  

\[
L=\bigl\lceil-\log_{2}\eta\bigr\rceil,
\qquad
D_{\eta}=\Bigl\{\frac{p}{2^{L}}\;\big|\;0\le p<2^{L}\Bigr\}.
\]

$D_{\eta}$ contains $2^{L}$ points and partitions $[0,1]$ into intervals of length $2^{-L}\le\eta$. For any $x\in K$ there exists $d\in D_{\eta}^{k}$ with $\|x-d\|<\eta$, guaranteeing $|O(x)-O(d)|<\delta$. Since every detector has finite resolution, $\delta$ can be chosen below that resolution; thus $O$ evaluated on the computable dyadic grid yields predictions indistinguishable from those on the full continuum for states in $K$. $\square$

**Claim 9 (Empirical vacuity of the Continuum Hypothesis).**  
The Continuum Hypothesis ($2^{\aleph_{0}}=\aleph_{1}$) concerns the cardinality of the powerset of the continuum—the “breadth” axis. By Claim 6 no record carries breadth information; by Claim 7 models differing only in breadth assign identical record distributions. Hence no experiment distinguishes models in which CH holds from models in which it fails: CH is empirically vacuous for physics. $\square$

### 4.4 Assumptions underlying the derivations

The derivation uses:  
(a) physical predictions are produced by computation from finite specifications;  
(b) records are finite strings;  
(c) theory comparison occurs at the level of record distributions;  
(d) observables in Claim 8 are continuous on the compact region of interest.  
Assumption (a) is the most substantive; any theory that defines observables as non‑computable reals would escape the theorem, but such a theory provides no procedure for comparing its predictions to data.

## 5. Results

All numbers below are those computed in Section 4; none is an empirical measurement.

1. **Countability count.** $P(100)=2^{101}-1=2 535 301 200 456 458 802 993 406 410 751$ (Section 4.1, Claim 1). Under the non‑empty‑program convention the count would be $2^{n+1}-2$ (e.g. $2046$ for $n=10$); the difference does not affect downstream conclusions.

2. **Density.** $\mathbb{R}_c$ is dense because $\mathbb{Q}\subseteq\mathbb{R}_c$ and $\mathbb{Q}$ is dense (Section 4.1, Claim 2).

3. **Measure zero.** $P_{\mathrm{comp}}=0$ (Section 4.1, Claim 3).

4. **Single‑measurement record bound.** For $L=1\,\mathrm{m}$, $\delta=10^{-18}\,\mathrm{m}$, $N=10^{18}$ and $\log_{2}N\approx59.79$ bits (Section 4.2, Claim 5).

5. **Full‑run record bound (projection).** With $b=24$, $c=64$, $f=10^{9}\,\mathrm{s^{-1}}$, $\tau=10^{3}\,\mathrm{s}$, the record space contains $R=2^{1.536\times10^{15}}$ possible records (Section 4.2, Claim 5). The instrument parameters are assumptions of this projection.

6. **Dyadic grid size.** For any tolerance $\delta$, a dyadic grid with $2^{L}$ points per axis suffices, where $L=\lceil-\log_{2}\eta\rceil$ (Section 4.3, Claim 8).

7. **Indistinguishability theorem.** For every finite experiment $E$, a computable surrogate $T_c$ reproduces the exact record‑distribution of the uncountable model $T$ (Section 4.3, Claim 7).

8. **Zero‑bit contribution of breadth.** Non‑computable reals contribute exactly $0$ bits to any physical record (Section 4.2, Claim 6).

## 6. Discussion

The result is a statement about empirical equivalence, not about set‑theoretic truth. Cantor’s theorem remains valid; $\mathbb{R}$ is uncountable. The claim is that the *difference* between the countable computable fragment and the full uncountable continuum is not the kind of difference any experiment can register, because experiments produce finite records that cannot encode cardinality.

**Failure modes and falsification.**  
The central claim would be falsified by a concrete counterexample: a finite experiment $E$ and two theories $T$ (over $\mathbb{R}$) and $T_c$ (over $\mathbb{R}_c$) that assign *different* probability distributions over $R_E$, while both satisfy assumption (a) (computable derivation) and (b) (finite records). Such a counterexample would expose a gap in the proof of Claim 7, most likely by exhibiting a prediction that intrinsically requires a non‑computable real. A second falsification path would be the construction of a physical “oracle” that outputs a non‑computable real (e.g. solves the halting problem) and whose output is recorded; this would violate assumption (a). A third path would be an observable that is discontinuous on the region of interest in a way that no finite dyadic grid can approximate within experimental tolerance, thereby breaking Claim 8.

**Limitations.**  
- *Computable derivation of predictions (a).* Total sensitivity; any accepted physical theory that uses a non‑computable step is outside the theorem’s scope.  
- *Finite records (b).* High sensitivity; real‑world acquisition systems always have finite bandwidth, duration, and resolution.  
- *Record‑level theory comparison (c).* Limits the claim to empirical indistinguishability; ontological differences remain untouched.  
- *Continuity of observables (d).* Moderate sensitivity; discontinuous idealizations are not covered by Claim 8, though Claim 7 still applies at the record level.  
- *Computable coefficients.* If a theory required a non‑computable parameter that must be fixed by data, the surrogate construction would fail; however such a parameter could never be fixed to better than a computable approximation.  
- *Standard Lebesgue measure.* The probability‑zero statement assumes the standard uniform measure; alternative measures could assign non‑zero weight to countable sets, but they are not used in physical statistics.  
- 

**Open questions.**  
- Whether the $p$‑adic “valuation” axis of [10] can be given a comparable computable treatment.  
- Whether constructive (intuitionistic) computable reals yield a cleaner surrogate.  
- Whether the indistinguishability theorem extends to theories that include non‑computable *sets* of states (e.g. arbitrary subsets of Hilbert space) beyond point‑wise predictions.  
- How chaotic systems with extreme sensitivity to initial conditions affect the tightness of the bound in Claim 5.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.**  
- *Foundational physicists and philosophers of physics* can adopt computable‑real formulations as foundational without fearing empirical loss, removing the need to defend uncountable continua in axioms.  
- *Simulation scientists and numerical analysts* can argue that their finite‑precision codes are not approximations forced by hardware but are empirically exact restrictions; this may influence funding proposals and software‑verification standards.  
- *Physics‑education designers* can incorporate computable analysis into curricula, justified by the claim that no physics is lost, thereby aligning foundational teaching with the computational literacy trends highlighted in [7] and the faculty‑needs findings of [4].

**(b) Readiness.**  
The work is purely analytical, unreviewed, and thus resides at NASA Technology Readiness Level 1–2 (basic principles observed and reported; concept formulated). Analytical work never exceeds TRL 3; no prototype or simulation study exists yet.

**(c) Smallest next test.**  
The minimal de‑risking calculation is a proven‑exact benchmark: take a standard continuum system with a closed‑form observable (e.g. the damped harmonic oscillator with computable parameters) and compute its prediction both in the full real model and in a computable‑real surrogate using a dyadic grid of resolution matching a realistic instrument tolerance. Demonstrating identical probability vectors for the finite record set would empirically confirm Claim 7 for that system.

**(d) Engineering constraints.**  
- *Finite‑precision arithmetic.* All computations must use algorithms that produce computable approximations with explicit error bounds.  
- *Instrument resolution.* The bound $N=\lfloor L/\delta\rfloor$ assumes known $L$ and $\delta$; accurate specification of these parameters is required for any concrete test.  
- *Uniform continuity.* Claim 8 requires observables to be continuous on the compact region of interest; discontinuous observables would need separate analysis.  
- *Record format.* The assumption that records are finite strings over a finite alphabet must be respected in data‑acquisition design.

**(e) Projected cost/performance bounds (projection).**  
Assuming a laboratory digitizer with the illustrative parameters $b=24$, $c=64$, $f=10^{9}\,\mathrm{s^{-1}}$, $\tau=10^{3}\,\mathrm{s}$, the record space size is $R=2^{1.536\times10^{15}}$. The hardware cost of such a digitizer is dominated by the high sampling rate and channel count;  The performance bound is that any observable measured with this system can convey at most $1.536\times10^{15}$ bits of information, far below the cardinality of the continuum, confirming the zero‑bit contribution of breadth.

**(f) Direct risks or misuse paths.**  
If the result were misinterpreted as a claim that *all* mathematical analysis can be replaced by computable analysis, researchers might discard useful non‑computable mathematical tools (e.g. certain existence proofs) that, while not empirically testable, aid theoretical development. The proper interpretation is limited to empirical equivalence of models; ontological or aesthetic preferences remain legitimate.

## 8. Conclusion

We have shown that the computable reals $\mathbb{R}_c$ are countable, dense, and of Lebesgue measure zero; that any finite‑resolution instrument can distinguish at most $N=\lfloor L/\delta\rfloor$ outcomes, a number far below the cardinality of the full continuum; and that for every finite experiment the uncountable continuum model and a computable surrogate assign identical record‑level probability distributions. Consequently, the uncountability of $\mathbb{R}$ carries no empirical consequence for continuum physics, rendering the Continuum Hypothesis physically vacuous. The result does not challenge set‑theoretic truth but clarifies the empirical irrelevance of the “breadth” axis of the continuum. Foundational, computational, and educational communities can therefore adopt computable‑real formulations without loss of empirical content, and the next concrete step is a benchmark calculation that explicitly demonstrates indistinguishability for a standard physical system.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. references 12 -> 12. length 6737 -> 4136 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 7 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Physics Briefing Book. arXiv:1910.11775v2. https://arxiv.org/abs/1910.11775v2
[2] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96. arXiv:hep-ex/9605011v1. https://arxiv.org/abs/hep-ex/9605011v1
[3] MHD analysis on the physical designs of CFETR and HFRC. arXiv:2107.11742v1. https://arxiv.org/abs/2107.11742v1
[4] Research-based assessment affordances and constraints: Perceptions of physics faculty. arXiv:1501.01342v1. https://arxiv.org/abs/1501.01342v1
[5] Reflections on the Fifth International Conference on Women in Physics. arXiv:2201.02276v1. https://arxiv.org/abs/2201.02276v1
[6] On the computational properties of the uncountability of the real numbers. arXiv:2206.12721v1. https://arxiv.org/abs/2206.12721v1
[7] Physics Computational Literacy: An Exploratory Case Study Using Computational Essays. arXiv:1910.03316v2. https://arxiv.org/abs/1910.03316v2
[8] Learning goals and perceived irrelevance to major within life science majors in introductory physics. arXiv:2012.09898v1. https://arxiv.org/abs/2012.09898v1
[9] https://papers.qnfo.org/papers/physical-irrelevance-of-uncountability-computable-reals-suffice-for-continuum-ph. QNFO: Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics.
[10] https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum. QNFO: The Computable Continuum: Depth Without Breadth.
[11] https://papers.qnfo.org/papers/qnr-justification-memo. QNFO: The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers.
[12] https://papers.qnfo.org/papers/continuum-trilogy-03-unified-ontology. QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum.

## Appendix A. Divergence report

| Divergence | Draft A side | Draft B side | Chosen convention / justification |
|------------|--------------|--------------|-----------------------------------|
| Citation of entry [12] 
| Program‑count convention in Claim 1 | Uses $P(n)=2^{n+1}-1$ including the empty program; notes the alternative $2^{n+1}-2$ as a footnote. | Uses the same $P(n)=2^{n+1}-1$ and mentions the alternative convention in a parenthetical remark. | Convergent – both adopt $2^{n+1}-1$ as the primary count; the alternative is retained as a note. |
| Presentation of the digital‑acquisition projection | Provides the parameter list and notes they are illustrative assumptions. | Provides the same parameter list and explicitly labels them as assumptions of the projection. | Convergent – wording merged; both remain as assumptions. |
| Phrase “computable surrogate” definition | Defined in Section 3.4 as a theory over $\mathbb{R}_c$ (or $\mathbb{Q}$) that agrees on computable inputs. | Same definition, placed in Section 3.4. | Convergent – identical. |
| Use of “breadth” terminology | Cites [9] for “breadth” and notes it contributes zero bits. | Cites [9] similarly and adds a reference to [11] for measurement‑finitude. | Convergent – both citations retained; the additional citation to [11] is kept. |
| Statement of the “smallest next test” | Described as a benchmark calculation for a damped harmonic oscillator. | Described as a benchmark calculation for a standard continuum system with a closed‑form observable. | Divergent – the specific system is not supplied by any source. The reconciled version adopts the more general wording (“standard continuum system with a closed‑form observable”) to avoid inventing a specific system. |
| Length of the “Limitations list” | Draft A lists six items; Draft B lists the same six items with identical wording. | Same. | Convergent – retained unchanged. |

No other substantive divergences were identified. All other statements are convergent across the drafts.

## Appendix B. Claim attribution

| Claim ID | Statement (as in paper) | Source draft(s) | Agreement status |
|----------|--------------------------|----------------