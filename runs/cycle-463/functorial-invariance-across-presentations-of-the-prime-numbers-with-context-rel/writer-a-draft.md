# Functorial Invariance Across Presentations of the Prime Numbers, with Context‑Relative Quantitative Illustrations

## Abstract

The prime numbers appear in many simultaneous presentations—arithmetic, analytic, sieve‑based, dynamical, and computational—yet the literature rarely states which theorems survive a change of encoding. We formalize this question with a category $\mathbf{RepPrimes}$ whose objects are presentations of the primes and whose morphisms are structure‑preserving translations, and we extend it with a two‑level schema in which atomicity is defined relative to a chosen factorization system. We prove that the Euler product, Möbius inversion, and the leading asymptotic $\pi(x)\sim x/\log x$ are invariants of this category, while the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not: the Legendre‑sieve presentation carries a main term inflated by the factor $2e^{-\gamma}=1.1229189642$ relative to $x/\log x$, giving $M_{\mathrm{sieve}}(10^{6})=81\,279.6$ against $\pi(10^{6})=78\,498$, a $3.54\%$ excess whose decomposition attributes $95.3\%$ to the sieve main term and $4.7\%$ to $\pi$ sitting below $\operatorname{Li}$. A weighted Germain‑prime lower bound $2.72069\times10^{6}$ at $x=10^{6}$ converts, under stated assumptions, to a projected unweighted scale $1.9693\times10^{5}$. A decidable syntactic test gives a sound, incomplete transfer criterion, and the atomicity schema explains why primes, uniformizers, and Galois conjugacy classes are each atomic only relative to a level.

## 1. Introduction

Analytic number theorists, cryptographers, and formalization specialists each rely on the primes in distinct computational or logical settings, and each group incurs concrete costs when the underlying presentation changes. Analytic researchers risk mis‑scaling error terms when porting sieve bounds into zeta‑zero language, potentially inflating bounds by a factor that grows with $x$. Cryptographers depend on primality assumptions whose precise formulation varies with the ambient algebraic structure, affecting key‑size recommendations. Formalization engineers must re‑prove lemmas for each encoding of the primes in proof assistants, duplicating effort across presentations. If the invariance results of this paper hold, the transfer question acquires a mechanical answer: exactly the functorial image of a statement transfers, and a syntactic test decides which hypotheses are safe.

We treat presentations of the primes as objects of a category and theorems about the primes as statements with well‑defined functoriality properties. Concretely:

1. **Objects.** A *presentation* of the primes is a structure $(X,\phi,\iota)$ where $X$ is a carrier (set, measure space, topological space, algebra, or computable structure), $\phi$ is a distinguished substructure encoding the primes, and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ or a cofinite or density‑one subset of $\mathcal P$.
2. **Morphisms.** A morphism $(X,\phi,\iota)\to(Y,\psi,\jmath)$ is a map $f:X\to Y$ that carries $\phi$ onto $\psi$ and makes the square
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

- Definition of the category $\mathbf{RepPrimes}$ and proof that it satisfies the category axioms (Section 3.2).  
- **Invariance Theorems:** the Euler product, Möbius inversion, and the asymptotic $\pi(x)\sim x/\log x$ are invariants of $\mathbf{RepPrimes}$ (Sections 4.1–4.3).  
- **Non‑Invariance Proposition:** the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant; the sieve presentation’s main term is inflated by the factor $2e^{-\gamma}=1.1229189642$, yielding a $3.54\%$ excess at $x=10^{6}$ that decomposes as $95.3\%$ main‑term inflation and $4.7\%$ fluctuation of $\pi$ below $\operatorname{Li}$ (Section 4.4).  
- A two‑level **atomicity schema** under which primes, uniformizers, and conjugacy classes are atomic only relative to a factorization system, with the Atomicity Relativity Conjecture stated (Section 3.4) and illustrated (Section 4.6).  
- A decidable **syntactic functoriality test** for first‑order statements, proved sound but not complete (Section 4.5).  
- Worked quantitative illustrations: the twin‑prime correlation constant $\alpha_{2}=0.6601618605$ and a weighted Germain‑prime lower bound $2.72069\times10^{6}$ at $x=10^{6}$, converting under a stated convention to a projected unweighted scale $1.9693\times10^{5}$ (Section 4.7).

The result also bears on the theory of quadratic prime‑generating polynomials and on primes in Beatty‑type sequences, because those contexts supply concrete presentations that fall under the same categorical framework.

## 2. Background and Related Work

### 2.1 Presentations of the primes

Five presentations recur across the literature; each becomes an object of $\mathbf{RepPrimes}$ in Section 3.

- **(P1) Arithmetic presentation.** Primes are the subset $\mathcal P\subset\mathbb N$ characterized by the divisibility poset. Unique factorization is the structural theorem; the arithmetic functions $\Lambda$, $\mu$, $\varphi$, $\tau$, $\sigma$ are defined here.
- **(P2) Analytic presentation.** Primes appear in the Euler product
  $$
  \zeta(s)=\prod_{p\in\mathcal P}\frac{1}{1-p^{-s}},\qquad\Re(s)>1,
  $$
  and in the Dirichlet series $-\zeta'(s)/\zeta(s)=\sum_{n}\Lambda(n)n^{-s}$.
- **(P3) Sieve presentation.** Starting from $\mathcal A_{0}=\mathbb N_{\ge2}$, successive removal of multiples of primes yields $\mathcal P=\bigcap_{k}\mathcal A_{k}$. Mertens’ theorem gives the survivor density $\prod_{p\le y}(1-1/p)=e^{-\gamma}/\log y$.
- **(P4) Beatty/dynamical presentation.** For irrational $\alpha>1$, the sequence $\lfloor\alpha n\rfloor$ has density $1/\alpha$; primes appearing in it are studied via equidistribution.
- **(P5) Computational presentation.** Primes are the output of concrete algorithms (sieve of Eratosthenes, primality tests); correctness and runtime are the structural theorems.

### 2.2 Specific results from the literature

Lemma 6.2 of [1] proves that for fixed shift $m\ge1$ the correlation
$$
\sum_{n\le x}f(n,s)\,f(n+m,s)=\alpha_{m}\,x+O\!\bigl(x(\log\log x)^{2}/\log x\bigr)
$$
holds, where $\alpha_{m}\ge0$ determines the density of prime pairs $\{p,p+m\}$ [1, § 6.2]. Lemma 6.2 of [2] establishes the same correlation formula and shows in addition that $\alpha_{k}>1/2$ for all $k$ when $\Re(s)>1$ [2, § 6.2]. Both works therefore supply a presentation‑level constant $\alpha_{m}$ that varies with the encoding.

Theorem 6.1 of [6] proves that for large $x$
$$
\sum_{1\le n\le x}w(n)\,\Lambda(n)\,\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x},
$$
with $w(n)=\Lambda(2n+1)$ [6, § 6]. This weighted Germain‑prime bound is the source of the quantitative illustration in Section 4.7; the implicit $\gg$‑constant is ineffective, so the number we attach is labeled a projection.

The functorial characterization of the primes in homotopy type theory [9] constructs a decidable prime type and maps it via a geometric morphism to an étale sheaf whose support is precisely $\mathcal P$ [9]. This is the existing formalization closest in spirit to $\mathbf{RepPrimes}$: a morphism of toposes plays the role of our presentation morphism, and the sheaf support plays the role of the encoding $\phi$.

The modular‑signature construction of [3] associates to each positive integer a unique numerical sequence built from its residues under the primes, distinguishes core seed primes from non‑core seed primes, groups the signatures within primorials, and uses elementary sieve properties and combinatorial principles to prove the infinitude of twin primes [3].

The quadratic‑prime presentation of [4] concerns the subset $\{p=an^{2}+bn+c:n\ge1\}$ generated by an irreducible polynomial over the integers, which is widely believed to be an unbounded subset of the primes [4].

The labor‑economics result of [5] shows that more highly skilled workers are more susceptible to AI automation, with analytical non‑routine tasks among the most exposed [5].

The Beatty‑prime presentation of [7] yields a counting function $\pi_{1}(x)=\delta(\alpha)x/\log x+O(x/\log^{2}x)$ with density factor $\delta(\alpha)=1/\alpha$ [7, § 1].

The computational search of [8] finds only three primes below $10^{7}$ satisfying $E_{p-3}\equiv0\pmod p$: $149$, $241$, and $2\,946\,901$ [8, § 3].

The framework of [10] treats the primes through four paradigms—quantum chaos, classical optimization, algorithmic information theory, and deterministic law—and argues that the apparent complexity of primes is a representational artifact; it identifies category theory as the abstraction layer that provides functorial maps between presentations [10].

The ultrametric program of [11] predicts “prime periodicity in particle mass ratios” among other signatures [11, § 7.6].

The emergent‑number‑theory work [12] proves a two‑way Irreducibility Correspondence: if a polynomial $P(x)$ is irreducible over $\mathbb Q$, then its associated zeta function $\zeta_{P}(s)$ admits no Euler‑product factorization, and conversely [12, § 3.2].

### 2.3 What is missing

Partial summation, explicit formulae, and Selberg–Delange methods provide isolated bridges between presentations. What is missing is a uniform account: a single framework in which “transfer” is a morphism and “what transfers” is a functoriality property, so that the question “does this theorem transfer?” has a mechanical answer. The works above each supply one presentation and one structural theorem; none states which of its theorems would survive transport to another encoding.

### 2.4 Notation

We write $\mathbb N=\{1,2,3,\dots\}$, $\mathcal P$ for the set of primes, $\pi(x)=|\{p\le x\}|$, $\operatorname{Li}(x)=\int_{2}^{x}dt/\log t$, $\Lambda(n)$ for the von Mangoldt function, $\mu(n)$ for the Möbius function, $\zeta(s)$ for the Riemann zeta function, and $\gamma$ for the Euler–Mascheroni constant. All logarithms are natural.

## 3. Methods: The Category of Prime Presentations

### 3.1 Objects

Fix the canonical presentation $(\mathbb N,\mathcal P,\mathrm{id})$.

**Definition 3.1 (Presentation).** A *presentation* of the primes is a triple $(X,\phi,\iota)$ where $X$ is an object of one of the ambient categories $\mathbf{Set}$, $\mathbf{Meas}$, $\mathbf{Top}$, $\mathbf{Alg}$, or $\mathbf{Comp}$; $\phi$ is a distinguished subobject or function of $X$; and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ itself or a cofinite or density‑one subset of $\mathcal P$.

*Example 3.2 (Analytic presentation).* $(\mathcal Z,Z_{\mathrm{crit}},\iota_{\mathcal Z})$ where $\mathcal Z$ is the zeta function regarded as a Dirichlet series, $Z_{\mathrm{crit}}$ is the multiset of nontrivial zeros, and $\iota_{\mathcal Z}$ sends each zero $\rho$ to its ordinate $\Im(\rho)$, which indexes the primes contributing to the explicit formula.

*Example 3.3 (Sieve presentation).* $(\mathbb N_{\ge2},\mathcal A_{\infty},\iota_{\mathrm{sieve}})$ where $\mathcal A_{\infty}=\bigcap_{k}\mathcal A_{k}$ and $\iota_{\mathrm{sieve}}$ is the inclusion $\mathcal A_{\infty}\hookrightarrow\mathcal P$.

### 3.2 Morphisms and category structure

**Definition 3.4 (Morphism).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations. A *morphism* $f:(X,\phi,\iota)\to(Y,\psi,\jmath)$ is a morphism $f:X\to Y$ in the ambient category such that the square of Definition 3.1 commutes up to exceptional sets $E_X\subseteq\phi$, $E_Y\subseteq\psi$ satisfying $|E_X\cap\{p\le x\}|=o(\pi(x))$ and similarly for $E_Y$.

**Proposition 3.5 (Category structure).** Presentations with the morphisms of Definition 3.4 form a category $\mathbf{RepPrimes}$.

*Proof.* Identity morphisms exist trivially. If $f:X\to Y$ and $g:Y\to Z$ are morphisms, then $g\circ f$ satisfies the commuting condition on $\phi\setminus(E_X\cup f^{-1}(E_Y))$, and the composite exceptional set remains density‑zero because both constituents are. Associativity follows from the ambient category. $\blacksquare$

### 3.3 The canonical functor

**Definition 3.6.** The *counting functor* $\Pi:\mathbf{RepPrimes}\to\mathbf{Asym}$ sends $(X,\phi,\iota)$ to the asymptotic class of $N_X(x)=|\iota(\phi\cap X_{\le x})|$ and sends a morphism to the identity on asymptotic classes.

The content of Section 4 is to determine which statements about the primes lie in the image of $\Pi$ and are therefore invariants.

### 3.4 The two‑level atomicity schema

**Definition 3.7 (Factorization system).** A *factorization system* on a presentation $(X,\phi,\iota)$ is a pair $(\mathbf A,\mathbf M)$ of classes of morphisms in the ambient category satisfying the usual two‑of‑three property, such that every well‑founded element of $X$ factors into $\mathbf M$‑maps followed by $\mathbf A$‑maps.

**Definition 3.8 (Level‑relative atom).** Fix a level $L=(X,\phi,\iota;\mathbf A,\mathbf M)$. An element $a\in\phi$ is *atomic at level $L$* if it admits no factorization $a=a_{1}a_{2}$ with both factors in the multiplicative structure of $X$ distinct from units.

**Examples.** At level $\mathbb N$ with ordinary multiplication, the atoms are the primes $\mathcal P$. At level $\mathbb Z_p$ (the $p$‑adic integers) with its valuation, the atom is the uniformizer $p$—a single element, atomic relative to a factorization theory in which every other nonzero element is a unit times a power of it. At level of the absolute Galois group $G_{\mathbb Q}$ with conjugacy‑class factorization of Frobenius data, the atoms are conjugacy classes attached to primes. The same integer $p$ is atomic at the first level, a unit‑times‑uniformizer decomposition at the second, and a conjugacy‑class label at the third.

**Atomicity Relativity Conjecture.** For any two levels $L_1,L_2$ joined by a morphism of $\mathbf{RepPrimes}$ that preserves the invariants of Section 4 (Euler product, Möbius inversion, leading asymptotic), the induced map on atoms is a bijection up to density zero, so that atomicity shifts with level exactly when the invariant class is preserved.

The conjecture is stated, not proved; Section 4.6 verifies its first instances and Section 7 records what would falsify it.

## 4. Analysis

### 4.1 Invariance of the Euler product

**Theorem 4.1 (Invariance of the Euler product).** Let $(X,\phi,\iota)$ be any presentation for which the ambient category admits a Dirichlet‑series structure compatible with $\iota$. Then
$$
\sum_{n=1}^{\infty}\frac{a_n}{n^{s}}=\prod_{q\in\phi}\left(1-\frac{c_q}{q^{s}}\right)^{-1},
\qquad\Re(s)>1,
$$
holds if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the Euler product is equivalent to unique factorization: expanding $\prod_{p}(1-p^{-s})^{-1}$ yields one term $n^{-s}$ for each factorization of $n$, and the coefficient is $1$ because factorization is unique. For a general presentation, transport the canonical coefficients via $\iota$: $a_n^{(X)}=a_{\iota^{-1}(n)}$ on the image of $\iota$ and $0$ elsewhere. The exceptional set has density zero, so partial sums differ by $o(x)$. By partial summation the Dirichlet series agree for $\Re(s)>1$. The same argument applies coefficient‑wise to the Euler product over $\phi$. $\blacksquare$

**Corollary 4.2.** The identity $\sum_{n}n^{-s}=\prod_{p}(1-p^{-s})^{-1}$ holds identically in the arithmetic, analytic, sieve, Beatty (restricted to a density‑one subsequence), and computational presentations.

### 4.2 Invariance of Möbius inversion

**Theorem 4.3 (Invariance of Möbius inversion).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations joined by a morphism $f$ with empty exceptional sets, and suppose both ambient categories admit Dirichlet series over the prime‑encoding substructure. Define $\mu^{(X)}(m)=\mu(\iota(m))$ for $m\in\phi$. Then
$$
\sum_{d\mid n}\mu^{(X)}(d)=\varepsilon(n)
$$
holds in $X$ if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the identity is equivalent to unique factorization, i.e. to the reciprocal of the Euler product. By Theorem 4.1 the Euler product is invariant, so its reciprocal is invariant as well. Transporting $\mu$ via $\iota$ preserves the divisor lattice because $\iota$ is a bijection on a density‑one set. Hence the identity holds in $X$ exactly when it holds canonically. For morphisms with non‑empty exceptional sets the summatory identity $\sum_{n\le x}\sum_{d\mid n}\mu^{(X)}(d)=1+o(x)$ remains invariant because the exceptional contribution is $o(x)$. $\blacksquare$

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
Dividing by $\pi(x)$ and using $\pi(x)\sim x/\log x$ in the canonical presentation yields $N_X(x)\sim x/\log x$. $\blacksquare$

### 4.4 Non‑invariance of the error term, with full arithmetic

**Proposition 4.5 (Non‑invariance of $E(x)$).** The error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant of $\mathbf{RepPrimes}$. In the sieve presentation the natural comparison function carries a main term inflated by the factor $2e^{-\gamma}$ relative to $x/\log x$‑type main terms, so the transferred error carries a leading constant $2e^{-\gamma}-1\approx0.1229$ where the analytic presentation has $o(1)$ relative to $\operatorname{Li}$.

*Proof.* The Legendre sieve counts a prime $p\le x$ by sieving $[2,x]$ by the primes $q\le\sqrt{x}$: an integer survives if it is divisible by no $q\le\sqrt{x}$, and the survivors are $1$ together with the primes in $(\sqrt{x},x]$. The sieve main term is therefore
$$
M_{\mathrm{sieve}}(x)=x\prod_{q\le\sqrt{x}}\!\left(1-\frac{1}{q}\right).
$$
Mertens’ theorem gives $\prod_{q\le y}(1-1/q)=e^{-\gamma}/\log y$; with $y=\sqrt{x}$ we have $\log y=\tfrac12\log x$, so
$$
M_{\mathrm{sieve}}(x)=\frac{2e^{-\gamma}\,x}{\log x}\,(1+o(1)).
$$
The analytic main term is $\operatorname{Li}(x)\sim x/\log x$. The ratio of main terms is $2e^{-\gamma}$, so the sieve presentation’s natural comparison function is inflated by that factor and the transferred error carries the leading constant $2e^{-\gamma}-1$, while the analytic error $E(x)=\pi(x)-\operatorname{Li}(x)$ is $o(x/\log x)$ relative to its main term. Since a morphism of $\mathbf{RepPrimes}$ preserves counting asymptotics (Theorem 4.4) but cannot rewrite the comparison function, the error statement is not functorial. $\blacksquare$

**Numerical evaluation of the inflation factor.** We use $\gamma=0.5772156649$ (standard tabulated value).

\[
e^{-\gamma}=e^{-0.5772156649}=0.5614594821,
\qquad
2e^{-\gamma}=1.1229189642,
\qquad
2e^{-\gamma}-1=0.1229189642\approx0.1229.
\]

With $\log(10^{6})=13.815510558$,
\[
\frac{x}{\log x}=\frac{10^{6}}{13.815510558}=72382.5,
\]
so the sieve main term is
\[
M_{\mathrm{sieve}}(10^{6})=1.1229189642\times72382.5=81279.6.
\]

Against the tabulated value $\pi(10^{6})=78498$, the excess is
\[
81279.6-78498=2781.6,\qquad
\frac{2781.6}{78498}=0.03544,
\]
a relative excess of $3.54\%$. Decomposing:
\[
M_{\mathrm{sieve}}(10^{6})-\operatorname{Li}(10^{6})=81279.6-78627.549=2652.1,
\]
\[
\operatorname{Li}(10^{6})-\pi(10^{6})=78627.549-78498=129.5,
\]
and $2652.1+129.5=2781.6$ as required. The shares are
\[
\frac{2652.1}{2781.6}=0.95344\;(95.3\%),\qquad
\frac{129.5}{2781.6}=0.04656\;(4.7\%).
\]

Thus the dominant contribution is the presentation‑bound main term, not the analytic fluctuation.

### 4.5 A decidable syntactic functoriality test

**Definition 4.6 (Transferable statement).** Let $S$ be a first‑order statement in a language $L$ containing a unary predicate $\mathrm{Prime}$, the order relation, addition and multiplication, and optionally a comparison function symbol $c$ and a minimization operator $\mu$. Fix a presentation $(X,\phi,\iota)$. The *syntactic functoriality test* for $S$ at $(X,\phi,\iota)$ checks three conditions:

1. **(T1, bounding).** Every quantified variable of $S$ is bounded either by a term in the image of $\iota$ or by the prime‑encoding substructure $\phi$; no quantifier ranges over $X\setminus\phi$ without such a bound.
2. **(T2, order‑minimization).** $S$ contains no occurrence of the minimization operator applied to a formula involving $\mathrm{Prime}$; i.e. no hypothesis of the form “the least prime $p$ with property $P$”.
3. **(T3, presentation‑level constants).** Every constant or comparison function appearing in $S$ is either definable from the divisibility structure alone (such as $\Lambda$, $\mu$, the Euler product) or is explicitly transported along the morphism; constants attached