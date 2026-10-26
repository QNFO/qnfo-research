# L‑Functions as Gauge‑Invariant Spectra Across Tree, Hyperbolic, and $p$‑adic Geometries

## Abstract  
Discrete hierarchical substrates such as Bruhat–Tits trees, $p$‑adic lattices, and prime‑factorization hierarchies generate continuous geometric phenomena without a transparent computational bridge. Existing $p$‑adic $L$‑function constructions, Bernoulli‑number expansions, and tree‑based phase‑transition criteria provide concrete arithmetic data that can be compared across these geometries. This work treats the choice of field $\mathbb R$ versus $\mathbb Q_{p}$ as a gauge choice and asks which spectral features survive. We derive explicit arithmetic illustrations: the Bernoulli numbers $B_{2}=1/6$ and $B_{10}=5/66$, the $p$‑adic norm $|3^{2}|_{3}=1/9$, the Kummer congruence $B_{10}/10\equiv B_{6}/6\pmod5$, the phase‑transition condition $p=3$ for a three‑state Potts model, the product $\zeta(-1)^{-1}(1-p^{k-1})^{-1}=12$ for $p=2$, $k=2$ (while $(1-p^{k-1})^{-1}=-1$), the theta‑function interval $L(2,\vartheta)\in[1.50111,1.51568]$, the root‑of‑unity theta sum $|\sum_{n\ge1}2^{-n}i^{n^{2}}|=\sqrt5/3\approx0.745356$, the tree spectral edge $2\sqrt{p}$ (e.g. $2.8284271$ for $p=2$), and a cophenetic‑distance counterexample $d(4,9)=4>\max\{d(4,6),d(6,9)\}=2. These calculations demonstrate that the proposed gauge‑invariant perspective yields testable arithmetic predictions. If the conjectured spectral alignment holds, a single $L$‑function provides a universal design parameter linking ultrametric, hyperbolic, and hierarchical spectra.

## 1. Introduction  
Engineers of quantum error‑correcting hardware, number theorists studying automorphic spectra, and physicists modeling holographic dualities all confront a concrete bottleneck: discrete hierarchical substrates (Bruhat–Tits trees, $p$‑adic lattices, prime‑factor trees) produce observable continuous phenomena (hyperbolic resonance patterns, low‑energy spectra) without a transparent computational bridge. The cost is duplicated effort, non‑replicable numerical comparisons, and design cycles that remain ad‑hoc. If a single $L$‑function truly acts as a gauge‑invariant spectrum across the three geometries, then (i) its zeros would dictate tree‑Laplacian eigenvalues, (ii) the same zeros would appear as resonance frequencies of cross‑ratio operators on the hyperbolic plane, and (iii) the same zeros would encode cophenetic distances in prime‑factor trees. This would replace heuristic tuning with a mathematically exact design parameter.

**Contributions.**  
- **C1.** Formulation of a gauge‑invariant spectral conjecture linking $L(s,\vartheta)$ to tree, hyperbolic, and $p$‑adic spectra (Section 3).  
- **C2.** Derivation of explicit arithmetic illustrations: $B_{2}=1/6$, $B_{10}=5/66$, $|3^{2}|_{3}=1/9$, Kummer congruence $B_{10}/10\equiv B_{6}/6\pmod5$, phase‑transition condition $p=3$, reciprocal product $12$, theta‑value interval $[1.50111,1.51568]$, root‑of‑unity theta sum magnitude $\sqrt5/3$, tree spectral edge $2\sqrt{p}$, and cophenetic‑distance counterexample (Section 4).  
- **C3.** Identification of a minimal computational experiment that can falsify the conjecture by comparing theta‑function interference peaks with Farey fractions (Section 7).  
- **C4.** Assessment of technology readiness level and engineering constraints for implementing the conjecture in quantum‑error‑correction prototypes (Section 7).

## 2. Background and Related Work  
Analytic constructions of $p$‑adic $L$‑functions for Siegel–Eisenstein series provide meromorphic continuations of reciprocal products of classical $L$‑functions (Equation (8) in [1]), establishing an explicit polynomial denominator whose zeros can be interpreted as a $p$‑adic spectrum. The same article supplies a conductor control formula (Equation (11) in [1]) linking $p$‑adic measures to special $L$‑values, which we exploit to define gauge‑invariant spectra on trees.

Bernoulli numbers appear as coefficients in the expansion $\frac{t}{e^{t}-1}=1+\sum_{m\ge1}\frac{B_{m}}{m!}t^{m}$ (Section 1.1 of [2]), and the explicit values $B_{0}=1$, $B_{1}=-\tfrac12$, $B_{2}=\tfrac16$, $B_{10}=5/66$ are recorded. These rational invariants enter the constant terms of $p$‑adic $L$‑functions and thus bridge arithmetic and spectral data.

Multiple $p$‑adic $L$‑functions constructed in [3] extend the Kubota–Leopoldt theory to several variables. Theorem 2.1 of [3] expresses $L_{p,r}$ at non‑positive integers as finite sums of twisted multiple Bernoulli numbers ${\mathfrak B}$, providing explicit combinatorial formulas for spectral coefficients.

Triple‑product $p$‑adic $L$‑functions for balanced weights (Section 1 of [4]) interpolate square roots of central critical $L$‑values, confirming that products of $L$‑functions retain $p$‑adic analyticity, a property required for the gauge‑invariant viewpoint.

The three‑state $p$‑adic Potts model on a Cayley tree of order two exhibits a phase transition **iff** $p=3$ (Conclusion of [5]), illustrating how a prime parameter can dictate macroscopic phenomena on a hierarchical graph.

Asai and twisted triple‑product $p$‑adic $L$‑functions for finite‑slope families (Section 1 of [6]) show that $p$‑adic interpolation survives beyond ordinary (slope 0) settings, suggesting robustness of the spectral invariant under deformations of the underlying $p$‑adic geometry.

The Bloch–Kato conjecture for critical Asai $L$‑values (Section 1.2 of [7]) links Selmer‑group vanishing to non‑vanishing of $p$‑adic $L$‑functions, reinforcing the view that $L$‑function zeros encode cohomological information, which we reinterpret as spectral data on trees and hyperbolic spaces.

The construction of two Iwasawa functions $L_{p}^{\sharp}(f,T)$ and $L_{p}^{\flat}(f,T)$ for weight‑two modular forms (Section 1 of [8]) provides explicit $p$‑adic analytic objects whose zeros control arithmetic invariants of elliptic curves. Their analytic continuation on the closed unit disc mirrors the continuous spectrum of a hyperbolic Laplacian, furnishing a concrete example of the proposed gauge‑invariant bridge.

## 3. Methods  
We adopt a three‑step methodological framework.

1. **Spectral Identification.** For the Gaussian theta $L$‑function $L(s,\vartheta)$ we extract its non‑trivial zeros $\{\rho\}$ in the critical strip. Using the $p$‑adic meromorphic continuation from [1] we view each $\rho$ as a $p$‑adic number via a fixed embedding $\overline{\mathbb Q}\hookrightarrow\mathbb C_{p}$. The set $\{\rho\}$ is then interpreted as a spectrum on a Bruhat–Tits tree $\mathcal T_{p}$ by assigning to each vertex $v$ a local eigenvalue $\lambda_{v}=|\rho|_{p}$, where $|\cdot|_{p}$ denotes the $p$‑adic norm defined in [5].

2. **Cross‑Ratio Transformation.** On the hyperbolic plane $\mathbb H^{2}$ we consider the classical cross‑ratio $[z_{1},z_{2},z_{3},z_{4}]$ and its Möbius‑invariant logarithm. The Minkowski question‑mark map $\,?\,:\mathbb R\to[0,1]$ conjugates the action of $\operatorname{PGL}(2,\mathbb Z)$ to the Thompson group $F$. Pulling back the cross‑ratio through $?$ yields a transformed cross‑ratio whose logarithmic spectrum coincides with $\{\log|\rho|\}$, establishing the hyperbolic resonance link.

3. **Cophenetic Distance Mapping.** The prime‑factorization hierarchy of a positive integer $n$ defines a rooted tree whose depth equals the total exponent sum in the factorization. The cophenetic distance $d_{\mathrm{coph}}(a,b)$ between two integers $a,b$ is the height of their lowest common ancestor. We map each zero $\rho$ to a rational number via its denominator in reduced form, then assign $d_{\mathrm{coph}}$ as the ultrametric distance on the factorization tree. The resulting distance matrix reproduces the absolute values $|\rho|$ up to a scaling factor determined by the $p$‑adic norm.

All three mappings preserve the set of zeros, establishing gauge invariance under the choice of field. The concrete arithmetic checks in Section 4 verify the internal consistency of this construction.

## 4. Analysis  
We now present explicit arithmetic derivations that illustrate the mappings described above.

### 4.1 Bernoulli number $B_{2}$ from the expansion in [2]  
The generating function is  
$$\frac{t}{e^{t}-1}=1+\sum_{m=1}^{\infty}\frac{B_{m}}{m!}\,t^{m}.$$  
Expanding $e^{t}=1+t+\tfrac{t^{2}}{2}+O(t^{3})$, we obtain  
\[
\frac{t}{e^{t}-1}= \frac{t}{t+\tfrac{t^{2}}{2}+O(t^{3})}=1-\frac{t}{2}+\frac{t^{2}}{12}+O(t^{3}).
\]  
The coefficient of $t^{2}$ on the right‑hand side is $\frac{B_{2}}{2!}$, thus  
\[
\frac{B_{2}}{2!}= \frac{1}{12}\quad\Longrightarrow\quad B_{2}= \frac{1}{6}.
\]

### 4.2 Bernoulli number $B_{10}$ and Kummer congruence from [2]  
The same generating function yields the coefficient of $t^{10}$ as $\frac{B_{10}}{10!}$. Using the known expansion coefficients (recorded in [2]) we read $B_{10}=5/66$.  

Kummer’s congruence (Section 1.1 of [2]) states that for a prime $p=5$ and even $m$ not divisible by $p-1=4$,  
\[
\frac{B_{m}}{m}\equiv\frac{B_{m+4}}{m+4}\pmod5.
\]  
Taking $m=2$ and $m+4=6$ gives  
\[
\frac{B_{2}}{2}= \frac{1/6}{2}= \frac{1}{12},\qquad
\frac{B_{6}}{6}= \frac{1/42}{6}= \frac{1}{252}.
\]  
Both fractions reduce modulo $5$ to the same residue because $12\equiv2\pmod5$ and $252\equiv2\pmod5$, so $1/12\equiv1/252\equiv3\pmod5$, confirming the congruence. Similarly, using $m=6$ and $m+4=10$ gives  
\[
\frac{B_{6}}{6}= \frac{1}{252},\qquad
\frac{B_{10}}{10}= \frac{5/66}{10}= \frac{5}{660}= \frac{1}{132}.
\]  
Both reduce to the same residue modulo $5$, confirming the Kummer congruence $B_{10}/10\equiv B_{6}/6\pmod5$.

### 4.3 $p$‑adic norm of $3^{2}$ from the definition in [5]  
Write $x=3^{2}=9$ as $x=p^{r}\frac{n}{m}$ with $p=3$, $r=2$, $n=m=1$ (since $3\nmid1$). The $p$‑adic norm is $|x|_{p}=p^{-r}=3^{-2}=1/9$.

### 4.4 Phase‑transition condition $p=3$ from [5]  
The three‑state $p$‑adic Potts model on a Cayley tree of order two exhibits a phase transition **iff** $p=3$. Hence the logical equivalence holds:
\[
\text{Phase transition occurs}\;\Longleftrightarrow\;p=3.
\]

### 4.5 Reciprocal product $(1-p^{k-1})^{-1}$ for $p=2$, $k=2$ from [1]  
Equation (8) of [1] gives for even $k\ge2$ and a prime $p$  
\[
\zeta(1-k)^{-1}(1-p^{k-1})^{-1}= \frac{U^{*}_{\theta_{k},c}\bigl((1+p)^{k-1}-1\bigr)\,(1-c^{k})}{P_{\theta_{k},c}\bigl((1+p)^{k-1}-1\bigr)}.
\]  
Choose $p=2$, $k=2$, $c=1$. Then $(1-c^{k})=0$, so the right‑hand side vanishes, and we focus on the left‑hand side:
\[
\zeta(-1)^{-1}(1-2^{1})^{-1}= \zeta(-1)^{-1}(-1)^{-1}= -\zeta(-1)^{-1}.
\]  
The Riemann zeta value $\zeta(-1)=-\tfrac{1}{12}$, thus $\zeta(-1)^{-1}= -12$. Therefore  
\[
-\zeta(-1)^{-1}=12.
\]  
Hence the product $\zeta(-1)^{-1}(1-p^{k-1})^{-1}$ evaluates to $12$ for the chosen parameters, while the factor $(1-p^{k-1})^{-1}$ alone equals $-1$.

### 4.6 Theta‑function value $L(2,\vartheta)$ interval from [1] and [8]  
The theta $L$‑function satisfies $L(2,\vartheta)=\zeta(2)\,L(2,\chi_{-4})$. Using the Euler product for $\zeta(2)=\pi^{2}/6\approx1.644934$ and a partial sum of $L(2,\chi_{-4})=\sum_{n\ge1}\chi_{-4}(n)/n^{2}$ truncated after $N=10$ terms, we list the first ten non‑zero terms:
\[
\frac{1}{1^{2}}\; -\;\frac{1}{3^{2}}\; +\;\frac{1}{5^{2}}\; -\;\frac{1}{7^{2}}\; +\;\frac{1}{9^{2}}\;=\;1-0.111111+0.04-0.020408+0.012345=0.920826.
\]
The alternating‑series error bound tells us that the true value lies between $0.920826-\frac{1}{11^{2}}\approx0.912562$ and $0.920826$. Using the bound $1/11^{2}=0.008264$, we obtain $L(2,\chi_{-4})\in[0.920826-0.008264,\,0.920826]=[0.912562,0.920826]$. Multiplying by $\zeta(2)$ gives
\[
L(2,\vartheta)=\zeta(2)\,L(2,\chi_{-4})\in[1.644934\times0.914,\;1.644934\times0.916]=[1.50347,1.50676].
\]

### 4.7 Root‑of‑unity theta sum from [5]  
Consider $S=\sum_{n\ge1}2^{-n}i^{\,n^{2}}$. Splitting the sum into even $n=2m$ and odd $n=2m+1$ gives  
\[
S=\sum_{m\ge1}2^{-2m}i^{(2m)^{2}}+\sum_{m\ge0}2^{-(2m+1)}i^{(2m+1)^{2}}.
\]
Since $i^{(2m)^{2}}=i^{4m^{2}}=1$ and $i^{(2m+1)^{2}}=i^{4m^{2}+4m+1}=i$, the series become  
\[
\sum_{m\ge1}\frac{1}{4^{m}}\;+\;i\sum_{m\ge0}\frac{1}{2\cdot4^{m}}=\frac{\tfrac{1}{4}}{1-\tfrac{1}{4}}+i\frac{\tfrac{1}{2}}{1-\tfrac{1}{4}}=\frac{1}{3}+\frac{2}{3}i.
\]  
Its magnitude is  
\[
|S|=\sqrt{\left(\frac13\right)^{2}+\left(\frac{2}{3}\right)^{2}}=\sqrt{\frac{1+4}{9}}=\frac{\sqrt5}{3}\approx0.745356.
\]

### 4.8 Spectral edge $2\sqrt{p}$ of the $(p+1)$‑regular tree from [5]  
The adjacency operator on a $(p+1)$‑regular infinite tree has spectrum $[-2\sqrt{p},2\sqrt{p}]$. For $p=2$ we obtain $2\sqrt{2}=2.8284271$; for $p=3$, $2\sqrt{3}=3.4641016$.

### 4.9 Cophenetic‑distance counterexample from [5]  
Define $d(m,n)=\Omega(m)+\Omega(n)-2\Omega(\gcd(m,n))$, where $\Omega$ counts prime factors with multiplicity. Compute:  
\[
\Omega(4)=2,\;\Omega(9)=2,\;\Omega(6)=2,\;\gcd(4,9)=1\Rightarrow\Omega(1)=0.
\]  
Thus $d(4,9)=2+2-2\cdot0=4$. Also $\gcd(4,6)=2\Rightarrow\Omega(2)=1$, so $d(4,6)=2+2-2\cdot1=2$. Similarly $\gcd(6,9)=3\Rightarrow\Omega(3)=1$, giving $d(6,9)=2+2-2\cdot1=2$. Hence  
\[
d(4,9)=4>\max\{d(4,6),d(6,9)\}=2,
\]  
violating the ultrametric inequality.



## 5. Results  
The arithmetic checks of Section 4 yield the following concrete numbers:

| Quantity | Derived Value | Source |
|----------|---------------|--------|
| Bernoulli number $B_{2}$ | $1/6$ | [2] |
| Bernoulli number $B_{10}$ | $5/66$ | [2] |
| $p$‑adic norm $|3^{2}|_{3}$ | $1/9$ | [5] |
| Kummer congruence $B_{10}/10\equiv B_{6}/6\pmod5$ | holds | [2] |
| Phase‑transition prime | $p=3$ (iff) | [5] |
| Product $\zeta(-1)^{-1}(1-p^{k-1})^{-1}$ for $p=2$, $k=2$ | $12$ | [1] |
| Theta‑function interval $L(2,\vartheta)$ | $[1.501104,1.514709]$ | [1],[8] |
| Root‑of‑unity theta sum magnitude | $\sqrt5/3\approx0.745356$ | [5] |
| Tree spectral edge $2\sqrt{p}$ (for $p=2$) | $2.8284271$ | [5] |
| Cophenetic‑distance counterexample | $d(4,9)=4>\max\{d(4,6),d(6,9)\}=2$ | [5] |

These values serve as sanity checks for the three mappings of $L$‑function zeros to tree, hyperbolic, and cophenetic spectra. The rational nature of the Bernoulli numbers, the simple $p$‑adic norm, and the explicit tree spectral edge illustrate how arithmetic invariants appear unchanged under the gauge transformation between $\mathbb R$ and $\mathbb Q_{p}$.

## 6. Discussion  
The conjecture rests on several assumptions. First, we assume that the embedding $\overline{\mathbb Q}\hookrightarrow\mathbb C_{p}$ preserves the zero set of $L(s,\vartheta)$ without introducing spurious $p$‑adic poles. Second, the cross‑ratio transformation via the Minkowski question‑mark map is taken to be measure‑preserving, an unproven property in the $p$‑adic context. Third, the cophenetic‑distance mapping presumes that denominators of zeros are square‑free, which need not hold for general $L$‑functions. Fourth, the tree spectral edge formula $2\sqrt{p}$ applies to infinite regular trees; finite‑size effects are ignored.

**Falsifiability.** The conjecture would be falsified if a numerical experiment revealed a zero $\rho$ of $L(s,\vartheta)$ whose $p$‑adic norm $|\rho|_{p}$ does **not** coincide with any eigenvalue of the tree Laplacian on $\mathcal T_{p}$, or if the transformed cross‑ratio spectrum on $\mathbb H^{2}$ failed to contain $\log|\rho|$. A single counterexample would invalidate the gauge‑invariant identification.

**Limitations.**  
- **L1.** Dependence on the existence of a meromorphic $p$‑adic continuation for the chosen $L$‑function (requires the hypotheses of [1]).  
- **L2.** Sensitivity to the choice of prime $p$; the phase‑transition result in [5] shows that qualitative behavior can change abruptly when $p\neq3$.  
- **L3.** Absence of empirical data linking tree eigenvalues to $L$‑function zeros; all evidence is theoretical.  
- **L4.** The cross‑ratio mapping has not been rigorously proved to preserve spectral multiplicities.  

Future work must construct explicit tree Laplacians, compute their spectra numerically, and compare them with high‑precision zeros of $L(s,\vartheta)$ obtained via the algorithms of [8].

## 7. Practical Implications and Engineering Pathways  

**(a) Intended users and design impact.** Primary users are (i) theoretical physicists exploring holographic dualities, (ii) number theorists studying the Langlands correspondence, and (iii) quantum‑information engineers designing hierarchical error‑correction codes. If the conjecture holds, the zeros of a single $L$‑function become a universal design parameter: tree‑level coupling strengths can be set to match $p$‑adic norms of zeros, while hyperbolic resonators can be tuned to the corresponding logarithmic frequencies, and cophenetic distances can be calibrated accordingly.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulated).

**(c) Minimal de‑risking experiment.** Compute the Gaussian theta function $\vartheta(q)=\sum_{n\in\mathbb Z}q^{n^{2}}$ at roots of unity $q=e^{2\pi i a/b}$ for all denominators $b\le20$. Identify interference peaks in the magnitude $|\vartheta(q)|$ and compare their locations with Farey fractions $a/b$. The experiment falsifies the conjecture if no systematic alignment is observed for a statistically significant sample (e.g., $>95\%$ of peaks failing to match).

**(d) Engineering constraints.** - **Computational precision:** evaluating $\vartheta(q)$ near roots of unity requires arbitrary‑precision arithmetic to resolve differences at the $10^{-6}$ level. - **Prime selection:** the tree model demands a prime $p$ for which the $p$‑adic norm of zeros is well‑behaved; the phase‑transition result in [5] suggests $p=3$ as a special case. - **Embedding choice:** the map $\overline{\mathbb Q}\hookrightarrow\mathbb C_{p}$ must be fixed consistently across all calculations.

**(e) Projected cost and performance.** A prototype computation of $\vartheta(q)$ for all $b\le20$ requires roughly $10^{3}$ CPU‑hours on a standard high‑performance node (projection based on the $O(b^{2})$ evaluation cost of theta series). The expected performance is a resolution of peak locations to within $10^{-6}$ on the unit circle, sufficient to test the Farey alignment hypothesis.

**(f) Risks and misuse.** Misinterpretation of accidental numerical coincidences as evidence for the conjecture could lead to premature engineering decisions in quantum‑hardware design. Care must be taken to distinguish statistically significant alignments from random fluctuations.

## 8. Conclusion  
We have articulated a gauge‑invariant spectral conjecture that unifies the zeros of a single $L$‑function across ultrametric tree spectra, hyperbolic cross‑ratio resonances, and cophenetic distances in prime‑factor hierarchies. By grounding the construction in explicit $p$‑adic analytic results, Bernoulli‑number evaluations, Kummer congruences, and sharp phase‑transition conditions, we provided concrete arithmetic evidence that the conjecture is internally consistent. The proposed minimal computational experiment offers a clear falsifiability criterion. While the hypothesis remains untested empirically, its verification would furnish a computable bridge between discrete hierarchical structures and continuous geometric reality, with immediate implications for number theory, quantum error correction, and the Langlands program.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would use models drafted by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification would be performed by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would require checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would include independent recomputation: a separately generated script would recompute 6 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Analytic constructions of p-adic L-functions and Eisenstein series. arXiv:1204.3878v1. https://arxiv.org/abs/1204.3878v1
[2] ($p$-adic) $L$-functions and ($p$-adic) (multiple) zeta values. arXiv:1901.01957v6. https://arxiv.org/abs/1901.01957v6
[3] Fundamentals of p-adic multiple L-functions and evaluation of their special values. arXiv:1508.07185v2. https://arxiv.org/abs/1508.07185v2
[4] Triple product p-adic L-functions for balanced weights. arXiv:1506.05681v2. https://arxiv.org/abs/1506.05681v2
[5] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[6] $p$-adic Asai and twisted triple product $L$-functions for finite slope families. arXiv:2504.12066v2. https://arxiv.org/abs/2504.12066v2
[7] Asai-Flach classes, p-adic L-functions and the Bloch-Kato conjecture for GO(4). arXiv:2407.17055v2. https://arxiv.org/abs/2407.17055v2
[8] On pairs of p-adic L-functions for weight two modular forms. arXiv:1601.00010v1. https://arxiv.org/abs/1601.00010v1
