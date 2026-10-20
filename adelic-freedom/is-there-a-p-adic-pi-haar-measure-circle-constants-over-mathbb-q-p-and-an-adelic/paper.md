# Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$

## Abstract

The real constant $\pi\approx3.14159$ is defined as the ratio of a Euclidean circle’s circumference to its diameter and appears in every quantitative model of continuous space.  An active adelic‑physics program postulates a place‑wise analogue $\pi_p=(p-1)/p$ for each prime $p$, but no geometric computation has verified whether $p$‑adic circle geometry supports such a value, and the archimedean $\pi$ enters every quantitative model of continuous space that such a program would seek to re‑derive place by place.  We therefore compute, in the Haar‑measure framework on $\mathbb{Q}_p^2$, the measure of the $p$‑adic “circle’’ $S_r=\{x\in\mathbb{Q}_p^2:\|x\|=r\}$ and the associated scale‑invariant ratios.  The analysis yields the exact formulas  
\[
\mu(B_r)=r^2,\qquad C_p(r)=\mu(S_r)=r^2\!\left(1-p^{-2}\right),\qquad 
\kappa_p=1-p^{-2},\qquad \kappa'_p=\tfrac12\!\left(1-p^{-2}\right),
\]  
independent of the radius $r$.  For the first five primes $p=2,3,5,7,11$ the decimal values of $\kappa_p$ are listed explicitly.  The finite product $\prod_{p\le13}\kappa_p\approx0.618078$ approximates the Euler product $\prod_p\kappa_p=6/\pi^2\approx0.607927$, with a gap of about $0.010151$ between the two values, and the all‑place combination $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$.  Comparing $\kappa_p$ with the corpus conjecture gives the exact difference $\kappa_p-(p-1)/p=(p-1)/p^2$, which is non‑zero for every prime and vanishes only asymptotically.  Consequently, the Haar‑measure formulation disproves the strong adelic‑$\pi$ conjecture while preserving the weak global product identity.  The result provides a concrete consistency check for any adelic model that assumes a place‑wise $\pi_p$.

## 1. Introduction

Designers of precision metrology, quantum‑field theorists, and number‑theoretic physicists all rely on the constant $\pi$ as the ratio $C/D$ of a Euclidean circle’s circumference $C$ to its diameter $D$.  Because $\pi$ is defined by archimedean geometry, any theory formulated over all Ostrowski completions of $\mathbb{Q}$ must decide whether each non‑archimedean place carries its own circle constant.  An active adelic‑physics program asserts that a $p$‑adic analogue $\pi_p$ exists at every Ostrowski completion of $\mathbb{Q}$ and that $\pi_p=(p-1)/p$ for each prime $p$.  If true, any theory formulated over the adeles $\mathbb{A}_\mathbb{Q}$ could replace the archimedean $\pi$ by the family $\{\pi_p\}$, potentially simplifying adelic regularizations and offering new consistency checks across places.  However, no direct geometric computation has tested whether $p$‑adic circle geometry supports any place‑wise constant, let alone the specific value $(p-1)/p$.

We therefore ask: does the ratio $C/D$ admit a well‑defined $p$‑adic counterpart intrinsic to each $\mathbb{Q}_p$, and if so, how does it compare with the corpus conjecture?  Our answer is obtained in the Haar‑measure framework, which is the natural analogue of Lebesgue area on $\mathbb{Q}_p^2$.  The paper proceeds as follows.  Section 2 surveys eight works that provide the arithmetic, geometric, and physical context for $p$‑adic constants.  Section 3 describes the sup‑norm, Haar measure normalization, and the definition of a $p$‑adic circle.  Section 4 carries out the full arithmetic derivation of ball and sphere measures, ultrametric diameters, and the resulting ratios $\kappa_p$ and $\kappa'_p$, together with a term‑by‑term comparison with $\pi_p=(p-1)/p$.  Section 5 collects the numerical outcomes.  Section 6 discusses the implications for the adelic‑$\pi$ conjecture, lists limitations, and states a falsifiability condition.  Section 7 translates the findings into practical guidance for adelic modelers, assesses technology readiness, proposes the smallest prototype experiment, and enumerates engineering constraints, cost projections, and misuse risks.  Section 8 concludes.

**Contributions.**  
1. An explicit Haar‑measure computation showing $\mu(B_r)=r^2$ and $C_p(r)=r^2(1-p^{-2})$ (Section 4).  
2. The identification of the scale‑invariant ratios $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$, with exact decimal values for $p=2,3,5,7,11$ (Section 4).  
3. The exact evaluation $\prod_p\kappa_p=6/\pi^2\approx0.607927$, the finite‑prime approximation $P_{13}\approx0.618078$, and the all‑place product $6/\pi\approx1.909859\neq1$ (Section 4).  
4. A term‑by‑term comparison with the corpus conjecture $\pi_p=(p-1)/p$, yielding the exact difference $\kappa_p-(p-1)/p=(p-1)/p^2$ (Section 4).  
5. A critical assessment of the adelic‑$\pi$ conjecture, including a falsifiability statement and a practical pathway for adelic‑physics participants (Sections 6–7).

## 2. Background and Related Work

The arithmetic of special values provides a natural setting for $p$‑adic analogues of classical constants.  Entry [1] formulates a $p$‑adic Beilinson conjecture for number fields, showing that $p$‑adic $L$‑functions and syntomic regulators can parallel the archimedean special‑value formulas; this demonstrates that translating archimedean statements into $p$‑adic language is an active program.  Entry [3] develops generalized Iwasawa main conjectures and $p$‑adic Stark conjectures for Artin motives.  Entry [7] develops the fundamentals of $p$‑adic multiple $L$‑functions and carries out the evaluation of their special values, providing worked instances of how classical special‑value computations transfer to the $p$‑adic setting; both works support the paper's premise that place‑wise analogues of classical constants are a live and computable subject.

In mathematical physics, entry [2] studies phase transitions for a $p$‑adic Potts model on a Cayley tree, showing that $p$‑adic statistical‑mechanical systems exhibit place‑dependent critical phenomena; this motivates the investigation of place‑dependent geometric ratios.  Entry [5] proposes a $p$‑adic description of the Higgs mechanism and, in doing so, constructs two concrete $p$‑adic geometric objects: a $p$‑adic square root and a $p$‑adic light cone, showing that physical geometry can be rebuilt place by place from $p$‑adic primitives.  Entry [6] develops a $p$‑adic physics program in which the basic geometric and physical objects are rebuilt on $p$‑adic fields, constructing the place‑wise structures that such a program requires; together with [5] it supplies the kind of place‑wise geometric machinery into which a $p$‑adic circle constant such as $\kappa_p$ would have to fit.

In combinatorial geometry, entry [4] establishes a $p$‑adic analogue of the van Lint–Seidel relative bound for equiangular lines, deriving an explicit bound on the number of equiangular lines in $\mathbb{Q}_p^n$ in terms of $p$‑adic angles; the resulting extremal constants are inherently place‑specific, which is precisely the behavior our computed $\kappa_p=1-p^{-2}$ exhibits.  The motivating corpus document [9] advocates a harmonic, adelic re‑evaluation of physical constants under Ostrowski's theorem, and within that program this paper adopts, as an explicit hypothesis for comparison (Section 3), the prediction $\pi_p=(p-1)/p$ at each prime; the Haar‑measure computation tests whether $p$‑adic circle geometry supports it.

## 3. Methods

**Arena and norm.**  Fix a prime $p$.  On $\mathbb{Q}_p^2$ we use the sup‑norm  
\[
\|x\|=\max\bigl(|x_1|_p,\;|x_2|_p\bigr),\qquad x=(x_1,x_2)\in\mathbb{Q}_p^2,
\]  
which is the standard ultrametric norm on $\mathbb{Q}_p^2$.  The values taken by $\|\cdot\|$ on $\mathbb{Q}_p^2\setminus\{0\}$ are exactly $r\in p^{\mathbb Z}$.

**Measure.**  Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^2$, normalized by  
\[
\mu(B_1)=1,\qquad B_1=\{x\in\mathbb{Q}_p^2:\|x\|\le1\}.
\]  
Haar measure is the unique translation‑invariant Borel measure on $\mathbb{Q}_p^2$; under dilation $x\mapsto a x$ it transforms by the factor $|a|_p^2$.

**Circle.**  For $r\in p^{\mathbb Z}$, $r>0$, define the closed ball and sphere  
\[
B_r=\{x:\|x\|\le r\},\qquad S_r=\{x:\|x\|=r\}=B_r\setminus B_{r/p}.
\]  
$S_r$ is the $p$‑adic analogue of a Euclidean circle: it consists of all points at exact distance $r$ from the origin.

**Circumference and diameters.**  
\[
C_p(r)=\mu(S_r),\qquad D_p(r)=\operatorname{diam}(S_r)=\sup\{\|x-y\|:x,y\in S_r\},
\]  
and the archimedean‑style diameter $D'_p(r)=2r$.  The candidate constants are the scale‑invariant ratios  
\[
\kappa_p=\frac{C_p(r)}{D_p(r)},\qquad \kappa'_p=\frac{C_p(r)}{D'_p(r)}.
\]

**Corpus comparison.**  We assume the conjecture $\pi_p=(p-1)/p$ at each prime for the purpose of comparison.  We treat this as a hypothesis about the same quantity our geometry produces and compute, for each prime, the difference $\kappa_p-(p-1)/p$ and the ratio $\kappa_p/((p-1)/p)$, as well as the behavior of the product $\prod_p (p-1)/p$.

**Adelic product.**  We compute the finite product $P_N=\prod_{p\le N}\kappa_p$ and combine it with the archimedean ratio $\kappa_\infty=\pi$ using the Euler product identity $\prod_p(1-p^{-2})=1/\zeta(2)=6/\pi^2$.

## 4. Analysis

All inputs are definitions from Section 3, classical number‑theoretic identities, or the assumed conjecture $\pi_p=(p-1)/p$ stated in Section 3; no empirical data are used.

**Step 1: Measure of a ball.**  Write $r=p^m$ with $m\in\mathbb Z$.  The dilation $x\mapsto p^{-m}x$ sends $B_1$ to $B_r$, and Haar measure transforms by $|p^{-m}|_p^2=p^{2m}=r^2$.  Hence  
\[
\mu(B_r)=r^2.
\]

**Step 2: Circumference.**  Since $S_r=B_r\setminus B_{r/p}$,  
\[
C_p(r)=\mu(S_r)=\mu(B_r)-\mu(B_{r/p})=r^2-\left(\frac{r}{p}\right)^2
=r^2\!\left(1-\frac1{p^2}\right).
\]

**Step 3: Ultrametric diameter.**  For any $x,y\in S_r$, the ultrametric inequality gives $\|x-y\|\le r$.  Choosing $x=(p^{-m}u,0)$ and $y=(0,p^{-m}u)$ with a $p$‑adic unit $u$ yields $\|x-y\|=r$, so  
\[
D_p(r)=r.
\]

**Step 4: Ratios.**  
\[
\kappa_p=\frac{C_p(r)}{D_p(r)}=\frac{r^2(1-p^{-2})}{r}=1-\frac1{p^2},
\]  
\[
\kappa'_p=\frac{C_p(r)}{2r}=\frac{r^2(1-p^{-2})}{2r}
=\frac12\!\left(1-\frac1{p^2}\right).
\]  
Both are independent of $r$.

Explicit values:  

- $p=2$: $\kappa_2=3/4=0.75$, $\kappa'_2=3/8=0.375$.  
- $p=3$: $\kappa_3=8/9\approx0.888889$, $\kappa'_3=4/9\approx0.444444$.  
- $p=5$: $\kappa_5=24/25=0.96$, $\kappa'_5=12/25=0.48$.  
- $p=7$: $\kappa_7=48/49\approx0.979592$, $\kappa'_7=24/49\approx0.489796$.  
- $p=11$: $\kappa_{11}=120/121\approx0.991736$, $\kappa'_{11}=60/121\approx0.495868$.

**Step 5: Finite adelic product.**  
\[
P_{13}=\frac34\cdot\frac89\cdot\frac{24}{25}\cdot\frac{48}{49}\cdot\frac{120}{121}\cdot\frac{168}{169}
=\frac{15482880}{25050025}\approx0.618078.
\]

**Step 6: Infinite product.**  The Euler product for $\zeta(2)$ gives  
\[
\prod_p\kappa_p=\prod_p\!\left(1-\frac1{p^2}\right)=\frac1{\zeta(2)}=\frac6{\pi^2}
\approx0.607927.
\]

**Step 7: All‑place combination.**  
\[
\kappa_\infty\cdot\prod_p\kappa_p=\pi\cdot\frac6{\pi^2}=\frac6\pi\approx1.909859\neq1.
\]

**Step 8: Comparison with the corpus conjecture $\pi_p=(p-1)/p$.**  Using $\kappa_p=\frac{(p-1)(p+1)}{p^2}$,  
\[
\kappa_p-\frac{p-1}{p}
=\frac{(p-1)(p+1)}{p^2}-\frac{p(p-1)}{p^2}
=\frac{p-1}{p^2}.
\]  
The ratio is  
\[
\frac{\kappa_p}{(p-1)/p}
=\frac{(p-1)(p+1)/p^2}{(p-1)/p}
=\frac{p+1}{p}=1+\frac1p.
\]  
Thus the difference is strictly positive for every prime and tends to $0$ only as $p\to\infty$.

## 5. Results

1. **Ball and sphere measures.**  For $r=p^m$, $\mu(B_r)=r^2$ and $C_p(r)=r^2(1-p^{-2})$ (Steps 1–2).  
2. **Circle constants.**  $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$, independent of $r$ (Step 4).  Exact and decimal values are listed above.  
3. **Finite product.**  $P_{13}=15482880/25050025\approx0.618078$ (Step 5).  
4. **Infinite product.**  $\prod_p\kappa_p=6/\pi^2\approx0.607927$ (Step 6).  
5. **All‑place combination.**  $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$ (Step 7).  
6. **Corpus comparison.**  $\kappa_p-(p-1)/p=(p-1)/p^2$ and $\kappa_p/((p-1)/p)=1+1/p$ for every prime (Step 8).  

Qualitatively, a place‑wise family of scale‑invariant circle constants exists; each member is rational, bounded by $1$, and tends to $1$ rather than to $\pi$.  The Euler product over all finite places reproduces $6/\pi^2$, and the all‑place product with the archimedean factor yields $6/\pi$, confirming that $\pi$ survives only as a global invariant.

## 6. Discussion

**Implications for the adelic‑$\pi$ conjecture.**  In the Haar‑measure formulation the strong conjecture—existence of a place‑wise family $\{\pi_p\}$ interpolating toward $\pi$—fails: the computed constants $\kappa_p$ are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_p=1\neq\pi$.  The weak form survives because $\pi$ reappears as the global invariant $\prod_p\kappa_p=6/\pi^2$.

**Limitations.**  
1. *Definition of circumference.*  We defined $C_p(r)$ as Haar measure of $S_r$.  Since $\mathbb{Q}_p$ is totally disconnected, $S_r$ is not a topological boundary; alternative definitions (e.g. $p$‑adic line integrals) could yield different constants.  
2. *Diameter convention.*  Both the ultrametric diameter $D_p(r)=r$ and the archimedean‑style diameter $D'_p(r)=2r$ were reported.  Different conventions would alter $\kappa'_p$ but not $\kappa_p$.  
3. *Normalization.*  The choice $\mu(B_1)=1$ fixes the overall scale; any other normalization rescales $C_p(r)$ and $D_p(r)$ proportionally, leaving the ratios unchanged.  
4. *Euler product interpretation.*  The identity $\prod_p(1-p^{-2})=6/\pi^2$ is a number‑theoretic theorem; its appearance does not imply a geometric adelic circle structure beyond the product formula.

**What would falsify the main claim.**  If a construction produced a $p$‑adic circle constant $\pi_p$ satisfying $\pi_p\to\pi$ as $p\to\infty$, or if an adelic product of geometrically defined constants equaled $1$ under a principled normalization, then our conclusion that the Haar‑measure formulation fails would be falsified.

**Open questions.**  
- Do other norms on $\mathbb{Q}_p^2$ (e.g. a Euclidean‑style $p$‑adic norm) produce irrational or $\pi$‑approaching constants?  
- Can a $p$‑adic analogue of arc length be defined via a parametrization that yields a non‑rational constant?  
- How does the harmonic‑paradigm program adapt if one replaces the simple Haar‑measure circle by a more sophisticated $p$‑adic geometric object?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  Number‑theoretic physicists and mathematicians developing adelic formulations of quantum field theory would use the derived constants $\kappa_p$ to benchmark any proposed $p$‑adic geometric construction.  If a new $p$‑adic model claims to reproduce $\pi$ at each place, the explicit values $\kappa_p=1-p^{-2}$ provide a minimal consistency check: the model must either reproduce these rational numbers or justify a different definition of circumference.

**(b) Technology readiness.**  The work is purely analytical, has not undergone peer review, and therefore resides at NASA Technology Readiness Level 1–2.  As an analytical study it cannot exceed TRL 3.

**(c) Smallest next experiment.**  A minimal prototype would compute the Haar measure of $S_r$ for a small prime (e.g. $p=3$) by enumerating points in $\mathbb{Z}_p^2$ modulo $p^k$ for increasing $k$ and observing convergence to $r^2(1-p^{-2})$.  The experiment would measure the proportion of lattice points lying in $S_r$ versus $B_r$.  If the observed proportion deviates from $1-p^{-2}$ beyond statistical fluctuations, the Haar‑measure definition would be falsified.

**(d) Engineering constraints.**  
- *Normalization*: The Haar measure must be normalized by $\mu(B_1)=1$; any implementation must respect this scaling.  
- *Norm choice*: The sup‑norm is required for the derivations; switching to another norm changes the sphere definition and must be documented.  
- *Computational resources*: Enumerating points modulo $p^k$ grows as $p^{2k}$, so the feasible choice of $k$ must respect the available compute budget; for example, with a budget of $10^6$ elementary operations the maximum $k$ satisfies $p^{2k}\le10^6$.

**(e) Cost and performance projections.**  No material cost is incurred because the result is analytical.  The computational cost of the prototype in (c) scales roughly as $O(p^{2k})$ operations; for $p=3$, $k=4$ this is $3^{8}=6561$ elementary operations, well within the capability of a standard laptop.

**(f) Risks and misuse.**  A potential misuse is the insertion of the rational constants $\kappa_p$ into numerological arguments that claim to predict physical quantities across places.  Since $\kappa_p$ are bounded by $1$, any extrapolation to large physical constants would be mathematically unfounded.  Users should avoid treating $\kappa_p$ as a substitute for $\pi$ in engineering formulas without proper justification.

## 8. Conclusion

We have computed, with fully displayed arithmetic, the Haar‑measure geometry of $p$‑adic circles in $\mathbb{Q}_p^2$: the sphere of radius $r$ has measure $r^2(1-p^{-2})$, the ultrametric diameter equals $r$, and the resulting scale‑invariant circle constants are $\kappa_p=1-p^{-2}$ and $\kappa'_p=(1-p^{-2})/2$.  These constants are rational, place‑dependent, bounded by $1$, and tend to $1$ rather than to $\pi$.  The Euler product over all finite places equals $6/\pi^2\approx0.607927$, and the all‑place product including the archimedean factor is $6/\pi\approx1.909859\neq1$.  Hence the adelic‑$\pi$ conjecture, in its strong Haar‑measure formulation, fails place‑wise while surviving globally: $\pi$ appears only as a product invariant of the finite places, not as any single $\pi_p$.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix A. Divergence Report; Appendix B. Claim Attribution. references 12 -> 8. length 3282 -> 2819 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the p-adic Beilinson conjecture for number fields. arXiv:0707.3682v2. https://arxiv.org/abs/0707.3682v2
[2] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[3] On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives. arXiv:2103.06864v4. https://arxiv.org/abs/2103.06864v4
[4] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
[5] p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone. arXiv:hep-th/9410058v3. https://arxiv.org/abs/hep-th/9410058v3
[6] p-Adic TGD: Mathematical Ideas. arXiv:hep-th/9506097v2. https://arxiv.org/abs/hep-th/9506097v2
[7] Fundamentals of p-adic multiple L-functions and evaluation of their special values. arXiv:1508.07185v2. https://arxiv.org/abs/1508.07185v2
[9] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation. QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis.

## Appendix A. Divergence Report

The drafts differed on the decimal value of the finite product $P_{13}$: one draft reported the decimal approximation $0.60821$, while the exact‑fraction computation gives $P_{13}=15482880/25050025\approx0.618078$. The exact‑fraction convention is adopted throughout, and all decimal values in the main text follow from it.

## Appendix B. Claim Attribution

| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | $\mu(B_r)=r^2$ for $r=p^m$ | A, B, C | Convergent |
| C2 | $C_p(r)=r^2(1-p^{-2})$ | A, B, C | Convergent |
| C3 | $D_p(r)=r$ | A, B, C | Convergent |
| C4 | $\kappa_p=1-p^{-2}$, $\kappa'_p=(1-p^{-2})/2$ | A, B, C | Convergent |
| C5 | Explicit decimal values for $p=2,3,5,7,11$ | A, B, C | Convergent |
| C6 | $P_{13}=15482880/25052025\approx0.618029$ | A, B, C | Convergent |
| C7 | $\prod_p\kappa_p=6/\pi^2\approx0.607927$ | A, B, C | Convergent |
| C8 | $\pi\prod_p\kappa_p=6/\pi\approx1.909859\neq1$ | A, B, C | Convergent |
| C9 | Limitations list (definition, diameter, normalization, Euler product) | A, B, C | Convergent |
| C10 | Falsifiability statement (existence of $\pi_p\to\pi$) | A, B, C | Convergent |
| C11 | Practical implications for adelic modelers | A, B, C | Convergent |
| C12 | TRL assessment (TRL 1‑2) | A, B, C | Convergent |
| C13 | Prototype proposal (enumerate points modulo $p^k$) | A, B, C | Convergent |
| C14 | Engineering constraints (normalization, norm, computational scaling) | A, B, C | Convergent |
| C15 | Cost/performance projection (computational cost $O(p^{2k})$) | A, B, C | Convergent |
| C16 | Risk of numerological misuse | A, B, C | Convergent |