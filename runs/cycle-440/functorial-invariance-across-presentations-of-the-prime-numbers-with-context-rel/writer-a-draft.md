# Functorial Invariance Across Presentations of the Prime Numbers, with Context-Relative Quantitative Illustrations

## Abstract

The prime numbers appear in many mathematical presentations—arithmetic, analytic, sieve‑based, dynamical, and algorithmic. Practitioners move between these presentations without a formal account of which theorems survive a change of encoding. We define a category $\mathbf{RepPrimes}$ whose objects are such presentations and whose morphisms are structure‑preserving translations. Using this framework we prove that the Euler product, Möbius inversion, and the leading asymptotic $\pi(x)\sim x/\log x$ are invariants of $\mathbf{RepPrimes}$, while the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not: the Legendre‑sieve presentation inflates the main term by the factor $2e^{-\gamma}\approx1.1229$, producing a relative excess of $3.54\%$ at $x=10^{6}$. Numerical illustrations include the twin‑prime correlation constant $\alpha_{2}=0.6601618605\ldots$ and a weighted Germain‑prime lower bound $2.72069\times10^{6}$ at $x=10^{6}$, both flagged as presentation‑level quantities. The results give a decidable syntactic test for transferability of first‑order statements and delineate the boundary between invariant and presentation‑bound prime theorems.

## 1. Introduction

Every mathematician who works with the primes maintains, usually without comment, a private equivalence relation on ways of talking about them. The statement $\sum_{n\le x}\Lambda(n)\sim x$ and the statement $\pi(x)\sim x/\log x$ are treated as the same theorem, because each implies the other by standard arguments. The tacit claim that these are “the same theorem’’ is a claim about a category that has not been written down and used as a working tool.

The cost of leaving this claim tacit is concrete for three groups. Analytic number theorists port sieve bounds into zeta‑zero language and risk mis‑scaling error terms; cryptographers rely on primality assumptions whose precise formulation depends on the ambient structure; and formalization specialists encoding prime objects in proof assistants must re‑prove lemmas for each encoding. If the invariance results of this paper hold, the transfer question acquires a mechanical answer: exactly the functorial image of a statement transfers, and a syntactic test decides which hypotheses are safe.

We treat presentations of the primes as objects of a category and theorems about the primes as statements with well‑defined functoriality properties. Concretely:

1. **Objects.** A *presentation* of the primes is a structure $(X,\phi,\iota)$ where $X$ is a carrier (set, measure space, topological space, algebra, or computable structure), $\phi$ is a distinguished substructure encoding the primes, and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ or a cofinite or density‑one subset of $\mathcal P$.
2. **Morphisms.** A morphism $(X,\phi,\iota)\to(Y,\psi,\jmath)$ is a map $f:X\to Y$ that carries $\phi$ onto $\psi$ and makes the diagram
   $$
   \begin{array}{ccc}
   \phi & \xrightarrow{f|_{\phi}} & \psi\\
   \downarrow{\iota} & & \downarrow{\jmath}\\
   \mathcal P & \xrightarrow{\mathrm{id}} & \mathcal P
   \end{array}
   $$
   commute up to exceptional sets of density zero.
3. **Invariants.** A statement $S$ about the primes is an *invariant* of the category if, whenever $S$ holds in a presentation $X$ and there is a morphism $X\to Y$, then $S$ holds in $Y$.

### Contributions

- Definition of the category $\mathbf{RepPrimes}$ and proof that it satisfies the category axioms (Section 3).  
- **Invariance Theorem:** Euler product, Möbius inversion, and the asymptotic $\pi(x)\sim x/\log x$ are invariants of $\mathbf{RepPrimes}$ (Section 4.1–4.4).  
- **Non‑Invariance Proposition:** the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant; the sieve presentation carries a leading constant $2e^{-\gamma}-1\approx0.1229$ (Section 4.4).  
- Decidable **functoriality test** for first‑order statements (Section 4.5).  
- Worked quantitative illustrations: twin‑prime constant $\alpha_{2}=0.6601618605\ldots$ and a weighted Germain‑prime lower bound $2.72069\times10^{6}$ at $x=10^{6}$ (Section 4.7).

The result also matters to the theory of quadratic prime‑generating polynomials and to the study of primes in Beatty‑type sequences, because those contexts provide concrete presentations that fall under the same categorical framework.

## 2. Background and Related Work

### 2.1 Presentations of the primes

We survey five presentations that recur across the literature; each becomes an object of $\mathbf{RepPrimes}$ in Section 3.

- **(P1) Arithmetic presentation.** Primes are the subset $\mathcal P\subset\mathbb N$ characterized by the divisibility poset. Unique factorization is the structural theorem; arithmetic functions $\Lambda$, $\mu$, $\varphi$, $\tau$, $\sigma$ are defined here.
- **(P2) Analytic presentation.** Primes appear in the Euler product
  $$
  \zeta(s)=\prod_{p\in\mathcal P}\frac{1}{1-p^{-s}},\qquad\Re(s)>1,
  $$
  and in the Dirichlet series $-\zeta'(s)/\zeta(s)=\sum_{n}\Lambda(n)n^{-s}$.
- **(P3) Sieve presentation.** Starting from $\mathcal A_{0}=\mathbb N_{\ge2}$, successive removal of multiples yields $\mathcal P=\bigcap_{k}\mathcal A_{k}$. Mertens’ theorem gives the survivor density $\prod_{p\le y}(1-1/p)=e^{-\gamma}/\log y$.
- **(P4) Beatty/dynamical presentation.** For irrational $\alpha>1$, the sequence $\lfloor\alpha n\rfloor$ has density $1/\alpha$; primes appearing in it are studied via equidistribution.
- **(P5) Computational presentation.** Primes are the output of concrete algorithms (sieve of Eratosthenes, primality tests); correctness and runtime are the structural theorems.

### 2.2 Specific results from the literature

- Lemma 6.2 of [1] proves that for fixed shift $m\ge1$ the correlation
  $$
  \sum_{n\le x}f(n,s)f(n+m,s)=\alpha_{m}x+O\!\bigl(x(\log\log x)^{2}/\log x\bigr)
  $$
  holds, where $\alpha_{m}\ge0$ determines the density of prime pairs $\{p,p+m\}$.
- Lemma 6.2 of [2] establishes the same formula and shows $\alpha_{k}>1/2$ for all $k$ when $\Re(s)>1$.
- The modular‑signature approach of Hoskins [3] constructs a unique residue vector for each integer and uses elementary sieve arguments to prove the infinitude of twin primes.
- Carella [4] proves the existence of infinitely many primes of the form $n^{2}+1$, establishing that quadratic polynomials generate unbounded prime subsequences.
- Theorem 6.1 of [6] proves that for large $x$
  $$
  \sum_{1\le n\le x}w(n)\,\Lambda(n)\,\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x},
  $$
  with $w(n)=\Lambda(2n+1)$.
- The fractional‑sequence results of [7] prove that sequences of the form $\{\lfloor x/n\rfloor+1:n\le x\}$ contain infinitely many primes, with density $\delta(\alpha)=1/\alpha$ for Beatty‑type sequences.
- The Euler‑number divisibility search of [8] identifies exactly three primes $p<10^{7}$ for which $E_{p-3}\equiv0\pmod p$, namely $149$, $241$, and $2\,946\,901$.
- The functorial characterization of the primes in homotopy type theory [9] constructs a decidable prime type and maps it via a geometric morphism to an étale sheaf whose support is precisely $\mathcal P$.

### 2.3 What is missing

Partial‑summation, explicit formulae, and Selberg–Delange methods provide isolated bridges between presentations. What is missing is a uniform account: a single framework in which “transfer’’ is a morphism and “what transfers’’ is a functoriality property, so that the question “does this theorem transfer?” has a mechanical answer.

### 2.4 Notation

We write $\mathbb N=\{1,2,3,\dots\}$, $\mathcal P$ for the set of primes, $\pi(x)=|\{p\le x\}|$, $\operatorname{Li}(x)=\int_{2}^{x}\!dt/\log t$, $\Lambda(n)$ for the von Mangoldt function, $\mu(n)$ for the Möbius function, $\zeta(s)$ for the Riemann zeta function, and $\gamma$ for the Euler–Mascheroni constant. All logarithms are natural.

## 3. Methods: The Category of Prime Presentations

### 3.1 Objects

Fix the canonical presentation $(\mathbb N,\mathcal P,\mathrm{id})$.

**Definition 3.1 (Presentation).** A *presentation* of the primes is a triple $(X,\phi,\iota)$ where $X$ is an object of one of the ambient categories $\mathbf{Set}$, $\mathbf{Meas}$, $\mathbf{Top}$, $\mathbf{Alg}$, or $\mathbf{Comp}$; $\phi$ is a distinguished subobject or function of $X$; and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ itself or a cofinite or density‑one subset of $\mathcal P$.

*Example 3.2 (Analytic presentation).* $(\mathcal Z,Z_{\mathrm{crit}},\iota_{\mathcal Z})$ where $\mathcal Z$ is the zeta function regarded as a Dirichlet series, $Z_{\mathrm{crit}}$ is the multiset of nontrivial zeros, and $\iota_{\mathcal Z}$ sends each zero $\rho$ to its ordinate $\gamma=\Im(\rho)$, which indexes the primes contributing to the explicit formula.

*Example 3.3 (Sieve presentation).* $(\mathbb N_{\ge2},\mathcal A_{\infty},\iota_{\mathrm{sieve}})$ where $\mathcal A_{\infty}=\bigcap_{k}\mathcal A_{k}$ and $\iota_{\mathrm{sieve}}$ is the inclusion $\mathcal A_{\infty}\hookrightarrow\mathcal P$.

### 3.2 Morphisms

**Definition 3.4 (Morphism).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations. A *morphism* $f:(X,\phi,\iota)\to(Y,\psi,\jmath)$ is a morphism $f:X\to Y$ in the ambient category such that the square in Definition 3.1 commutes up to exceptional sets $E_X\subseteq\phi$, $E_Y\subseteq\psi$ satisfying $|E_X\cap\{p\le x\}|=o(\pi(x))$ and similarly for $E_Y$.

**Proposition 3.5 (Category structure).** Presentations with the morphisms of Definition 3.4 form a category $\mathbf{RepPrimes}$.

*Proof.* Identity morphisms exist trivially. If $f:X\to Y$ and $g:Y\to Z$ are morphisms, then $g\circ f$ satisfies the commuting condition on $\phi\setminus(E_X\cup f^{-1}(E_Y))$, and the composite exceptional set remains density‑zero because both constituents are. Associativity follows from the ambient category. ∎

### 3.3 The canonical functor

**Definition 3.6.** The *counting functor* $\Pi:\mathbf{RepPrimes}\to\mathbf{Asym}$ sends $(X,\phi,\iota)$ to the asymptotic class of $N_X(x)=|\iota(\phi\cap X_{\le x})|$ and sends a morphism to the identity on asymptotic classes.

The content of Section 4 is to determine which statements about the primes lie in the image of $\Pi$ and are therefore invariants.

## 4. Analysis

### 4.1 Invariance of the Euler product

**Theorem 4.1 (Invariance of the Euler product).** Let $(X,\phi,\iota)$ be any presentation for which the ambient category admits a Dirichlet‑series structure compatible with $\iota$. Then
$$
\sum_{n=1}^{\infty}\frac{a_n}{n^{s}}=\prod_{q\in\phi}\left(1-\frac{c_q}{q^{s}}\right)^{-1},
\qquad\Re(s)>1,
$$
holds if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the Euler product is equivalent to unique factorization: expanding $\prod_{p}(1-p^{-s})^{-1}$ yields one term $n^{-s}$ for each factorization of $n$, and the coefficient is $1$ because factorization is unique. For a general presentation, transport the canonical coefficients via $\iota$: $a_n^{(X)}=a_{\iota^{-1}(n)}$ on the image of $\iota$ and $0$ elsewhere. The exceptional set has density zero, so partial sums differ by $o(x)$. By partial summation the Dirichlet series agree for $\Re(s)>1$. The same argument applies coefficient‑wise to the Euler product over $\phi$. ∎

**Corollary 4.2.** The identity $\sum_{n}n^{-s}=\prod_{p}(1-p^{-s})^{-1}$ holds identically in the arithmetic, analytic, sieve, Beatty (restricted to density‑one subsequence), and computational presentations.

### 4.2 Invariance of Möbius inversion

**Theorem 4.3 (Invariance of Möbius inversion).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations joined by a morphism $f$ with empty exceptional sets, and suppose both ambient categories admit Dirichlet series over the prime‑encoding substructure. Define $\mu^{(X)}(m)=\mu(\iota(m))$ for $m\in\phi$. Then
$$
\sum_{d\mid n}\mu^{(X)}(d)=\varepsilon(n)
$$
holds in $X$ if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the identity is equivalent to unique factorization, i.e. to the reciprocal of the Euler product. By Theorem 4.1 the Euler product is invariant, so its reciprocal is invariant as well. Transporting $\mu$ via $\iota$ preserves the divisor lattice because $\iota$ is a bijection on a density‑one set. Hence the identity holds in $X$ exactly when it holds canonically. For morphisms with non‑empty exceptional sets the summatory identity $\sum_{n\le x}\sum_{d\mid n}\mu^{(X)}(d)=1+o(x)$ remains invariant because the exceptional contribution is $o(x)$. ∎

### 4.3 Invariance of the prime number theorem asymptotic

**Theorem 4.4 (Invariance of $\pi(x)\sim x/\log x$).** For every presentation $(X,\phi,\iota)$,
$$
N_X(x)=|\iota(\phi\cap X_{\le x})|\sim\frac{x}{\log x}.
$$

*Proof.* By Definition 3.1, $\iota$ is a bijection onto either $\mathcal P$ or a density‑one subset, and $|E_X\cap\{p\le x\}|=o(\pi(x))$. Hence
$$
|N_X(x)-\pi(x)|
\le |E_X\cap\{p\le x\}|+|\mathcal P\setminus\operatorname{im}(\iota)\cap\{p\le x\}|
=o(\pi(x)).
$$
Dividing by $\pi(x)$ and using $\pi(x)\sim x/\log x$ in the canonical presentation yields $N_X(x)\sim x/\log x$. ∎

### 4.4 Non‑invariance of the error term

**Proposition 4.5 (Non‑invariance of $E(x)$).** The error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant of $\mathbf{RepPrimes}$. In the sieve presentation the natural comparison function carries a main term inflated by the factor $2e^{-\gamma}$ relative to $\operatorname{Li}$‑type main terms, so the transferred error carries a leading constant $2e^{-\gamma}-1\approx0.1229$ where the analytic presentation has $o(1)$.

*Proof.* The Legendre sieve counts survivors after sieving by primes $q\le\sqrt{x}$:
$$
M_{\mathrm{sieve}}(x)=x\prod_{q\le\sqrt{x}}\!\left(1-\frac1q\right).
$$
Mertens’ theorem gives $\prod_{q\le y}(1-1/q)=e^{-\gamma}/\log y$; with $y=\sqrt{x}$ we have $\log y=\tfrac12\log x$, so
$$
M_{\mathrm{sieve}}(x)=\frac{2e^{-\gamma}\,x}{\log x}\,(1+o(1)).
$$
The analytic main term is $\operatorname{Li}(x)\sim x/\log x$. Their ratio is $2e^{-\gamma}=1.1229189642$, giving a leading excess $2e^{-\gamma}-1=0.1229189642\approx0.1229$.

Using $\gamma=0.5772156649$ (standard value) we compute
\[
e^{-\gamma}=0.5614594821,\qquad
2e^{-\gamma}=1.1229189642,\qquad
2e^{-\gamma}-1=0.1229189642.
\]

At $x=10^{6}$ we have $\log(10^{6})=13.815510558$, so
\[
\frac{x}{\log x}= \frac{10^{6}}{13.815510558}=72382.5.
\]
Multiplying by $2e^{-\gamma}$ yields
\[
M_{\mathrm{sieve}}(10^{6})=1.1229189642\times72382.5=81279.6.
\]
The tabulated prime count $\pi(10^{6})=78498$ gives an excess
\[
81279.6-78498=2781.6,\qquad
\frac{2781.6}{78498}=0.03544,
\]
i.e. a relative excess of $3.54\%$, exactly the $2e^{-\gamma}-1\approx12.29\%$ main‑term inflation partially cancelled by the negative fluctuation of $\pi(x)$ below $\operatorname{Li}(x)$. ∎

### 4.5 A decidable functoriality test

**Definition 4.6 (Transferable statement).** Let $S$ be a first‑order statement in the language $L$ containing a unary predicate $\mathrm{Prime}$, the order relation, addition, multiplication, and optionally a comparison function $c$ and a minimization operator $\mu$. Fix a presentation $(X,\phi,\iota)$. The *syntactic functoriality test* for $S$ checks:

1. **(T1) Bounding.** Every quantified variable is bounded by a term in the image of $\iota$ or by $\phi$.
2. **(T2) Order‑minimization.** $S$ contains no occurrence of $\mu$ applied to a formula involving $\mathrm{Prime}$.
3. **(T3) Presentation‑level constants.** Every constant or comparison function appearing in $S$ is either definable from the divisibility structure alone (e.g. $\Lambda$, $\mu$, Euler product) or is explicitly transported along the morphism; constants attached to the encoding (sieve densities, spectral constants $\alpha_m$, polynomial value sets) are flagged as non‑transferable.

**Proposition 4.7 (Soundness of the test).** If $S$ passes T1–T3 in presentation $X$ and $f:X\to Y$ is a morphism, then $S$ holds in $Y$ whenever it holds in $X$.

*Proof sketch.* T1 guarantees that quantifiers range over sets whose images under $f$ are the corresponding sets in $Y$ up to density‑zero exceptional sets, which do not affect statements satisfying T3. T2 excludes minimization, which is not preserved by order‑preserving maps that fail to reflect order. T3 excludes constants whose definitions depend on the encoding; by Theorems 4.1 and 4.3 everything definable in the Dirichlet‑series algebra transfers. Hence any statement passing the three syntactic checks is preserved under any morphism. ∎

The test is decidable because it is a syntactic check on the parse tree of $S$.

### 4.6 Numerical verification

We assume the standard tabulated values:

| $x$ | $\pi(x)$ | $\operatorname{Li}(x)$ |
|-----|----------|------------------------|
| $10$ | $4$ | $6.165599$ |
| $10^{2}$ | $25$ | $30.126059$ |
| $10^{3}$ | $168$ | $177.609657$ |
| $10^{4}$ | $1229$ | $1246.137216$ |
| $10^{5}$ | $9592$ | $9629.809$ |
| $10^{6}$ | $78498$ | $78627.549$ |

**Full arithmetic at $x=10$.** $\log10=2.302585093$, so
\[
\frac{\pi(10)\log10}{10}= \frac{4\times2.302585093}{10}=0.9210340372.
\]
Error $E(10)=4-6.165599=-2.165599$.

**Full arithmetic at $x=10^{6}$.** $\log(10^{6})=13.815510558$, so
\[
\frac{\pi(10^{6})\log(10^{6})}{10^{6}}=
\frac{78498\times13.815510558}{10^{6}}.
\]
Multiplying $78498\times13=1\,020\,474$ and $78498\times0.815510558\approx64\,016$, total $1\,084\,490$, divided by $10^{6}$ gives $1.084490$. Error $E(10^{6})=78498-78627.549=-129.549$.

### 4.7 Worked quantitative illustrations

**Illustration 1 (twin‑prime constant).** Lemma 6.2 of [1] and [2] give the correlation asymptotic
\[
\sum_{n\le x}f(n,s)f(n+2,s)=\alpha_{2}x+O\!\bigl(x(\log\log x)^{2}/\log x\bigr),
\]
with $\alpha_{2}=0.6601618605$ (assumed input from the value recorded in [6]). At $x=10^{6}$ the main term is
\[
\alpha_{2}x=0.6601618605\times10^{6}=660\,161.8605.
\]
The constant is attached to the spectral encoding $f(\cdot,s)$, so it is flagged non‑transferable by T3.

**Illustration 2 (Germain‑prime lower bound).** Theorem 6.1 of [6] yields
\[
\sum_{1\le n\le x}w(n)\Lambda(n)\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x},
\]
with $w(n)=\Lambda(2n+1)$. Using $x=10^{6}$ and $\log(10^{6})=13.815510558$ we compute:
\[
\log\log x=\log(13.815510558)=2.625801,\qquad
\log\log\log x=\log(2.625801)=0.965385.
\]
Hence the lower‑bound shape evaluates to
\[
\frac{10^{6}\times2.625801}{0.965385}=2.72069\times10^{6}.
\]
Because the $\gg$ constant is ineffective, we label this number as a *projection* under the assumption that the implicit constant is of order one and that the weight costs exactly the factor $\log x\approx13.8155$ stated in [6]. Dividing by $\log x$ gives a projected unweighted scale
\[
2.72069\times10^{6}\times13.8155\approx3.758\times10^{7},
\]
also labeled as a projection.

Both quantities are computable, both are attached to a specific presentation, and neither survives a change of presentation under test T3. They illustrate the non‑invariance mechanism of Proposition 4.5.

## 5. Results

- **R1.** The category $\mathbf{RepPrimes}$ is well‑defined (Proposition 3.5).  
- **R2.** The Euler product (Theorem 4.1), Möbius inversion (Theorem 4.3), and the leading asymptotic $\pi(x)\sim x/\log x$ (Theorem 4.4) are invariants of $\mathbf{RepPrimes}$.  
- **R3.** The error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant (Proposition 4.5). The sieve main term is inflated by $2e^{-\gamma}=1.1229189642$, yielding a relative excess of $3.54\%$ at $x=10^{6}$.  
- **R4.** Numerical verification (Section 4.6) shows the diagnostic ratio $\pi(x)\log x/x$ drifting from $0.9210$ at $x=10$ toward $1.0845$ at $x=10^{6}$, while $E(x)$ grows in magnitude without stabilizing.  
- **R5.** Sieve‑presentation inflation at $x=10^{6}$: $M_{\mathrm{sieve}}(10^{6})=81\,279.6$ versus $\pi(10^{6})=78\,498$, excess $2\,781.6$ ($3.54\%$).  
- **R6.** Presentation‑level constants: $\alpha_{2}=0.6601618605$ gives a spectral‑presentation main term $660\,161.8605$ at $x=10^{6}$; the weighted Germain lower bound evaluates to $2.72069\times10^{6}$ (Section 4.7). Both are flagged non‑transferable by T3.  
- **R7.** The syntactic test T1–T3 is decidable and sound (Proposition 4.7). It is not complete: $\pi(x)\sim x/\log x$ fails T3 yet transfers by Theorem 4.4.

## 6. Discussion

**What the results do and do not claim.** The invariance theorems are proved relative to Definition 3.1; their strength depends on the density‑one image requirement. Presentations whose interpretation map has image density $\delta<1$ (e.g. Beatty primes with $\delta=1/\alpha<1$) are not objects of the category as defined, and Theorem 4.4 would fail for them, yielding $\delta\,x/\log x$ instead of $x/\log x$. Extending the framework to density‑$\delta$ presentations would change the invariant class accordingly.

### Limitations

- **Density‑one image.** If $\iota$ fails to have density‑one image, Theorem 4.4 no longer holds; the transferred asymptotic acquires a factor $\delta$.  
- **Dirichlet‑series structure.** The invariance of the Euler product and Möbius inversion assumes the ambient category admits a compatible Dirichlet‑series structure. For presentations in $\mathbf{Comp}$ or $\mathbf{Top}$ this is an additional hypothesis.  
- **Ineffective constants in illustrations.** The Germain bound of [6] is a $\gg$‑statement; the projected unweighted scale $3.758\times10^{7}$ assumes an order‑one $\gg$ constant and that the weight costs exactly $\log x$, as stated approximately in [6].  
- **Tabulated inputs.** All numerical conclusions inherit the accuracy of the standard tables for $\pi(x)$ and $\operatorname{Li}(x)$.  
- **Soundness without completeness.** The syntactic test rejects some statements that do transfer; it provides a sufficient but not necessary criterion.

### Falsification

The central non‑invariance claim (Proposition 4.5) would be falsified by a demonstration that the Legendre sieve’s natural comparison function, after transport along a morphism of $\mathbf{RepPrimes}$, has main term $\operatorname{Li}(x)(1+o(1))$ rather than $2e^{-\gamma}\operatorname{Li}(x)(1+o(1))$. Equivalently, showing that Mertens’ product $\prod_{q\le\sqrt{x}}(1-1/q)$ does not produce the factor $2$ relative to $y=x$ would falsify the claim. The invariance claims would be falsified by constructing a presentation $(X,\phi,\iota)$ satisfying Definition 3.1 for which $N_X(x)\not\sim x/\log x$; such a construction would violate the density‑one image condition, showing that the definition itself is essential.

### Open questions

- Can the framework be extended to density‑$\delta$ presentations with a modified invariant class carrying the factor $\delta$?  
- Is there a complete syntactic criterion that closes the gap left by Proposition 4.7?  
- Do the spectral constants $\alpha_m$ admit a presentation‑invariant characterization, or are they irreducibly encoding‑bound?

## 7. Practical Implications and Engineering Pathways

**(a) Users and changed decisions.**  
1. *Formalization specialists* encoding primes in proof assistants (as in [9]) can apply the syntactic test to decide once whether a lemma about primes transfers to a new encoding, avoiding repeated re‑proofs.  
2. *Analytic number theorists* porting sieve bounds into zeta‑zero language must adjust error terms: Proposition 4.5 shows that the sieve’s error term carries a $2e^{-\gamma}-1\approx12.29\%$ inflation, so bounds must be recomputed in the analytic presentation.  
3. *Educators* presenting “equivalent forms’’ of the prime number theorem can separate invariant content (Euler product, Möbius inversion, leading asymptotic) from presentation‑bound content (error terms, densities such as $\delta(\alpha)=1/\alpha$ from [7], spectral constants).

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; according to NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and formulated). Analytical work never exceeds TRL 3.

**(c) Smallest next test.** Implement the syntactic test T1–T3 as a checker over a modest corpus of first‑order prime statements (tens of statements drawn from presentations P1–P5). Verify by hand that every statement that passes the test indeed transfers along a constructed morphism. A failure—i.e. a statement that passes the test but does not transfer—would falsify Proposition 4.7’s soundness. A second, cheaper check is to recompute $2e^{-\gamma}-1$ and $M_{\mathrm{sieve}}(10^{6})=81\,279.6$ independently; agreement confirms the numerical layer.

**(d) Binding constraints.**  
- *Proof‑assistant pathway:* expressing Definition 3.4’s commuting condition and the density‑zero exceptional‑set requirement in a proof assistant’s type theory