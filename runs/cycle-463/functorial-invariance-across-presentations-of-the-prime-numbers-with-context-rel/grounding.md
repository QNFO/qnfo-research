# Grounding block - source: rem-rev-82937a62-6ff4-4f5e-ad1a-32df46be1a06

## Research idea

Indecomposability of Primes as Context-Relative Across Foundational Levels. Conjecture: every candidate 'atomic' object in arithmetic—primes, uniformizers, absolute Galois groups, adeles, HoTT primitive notions—is indecomposable only relative to a chosen factorization system or background structure, and moving to a richer level (2-category, derived geometry, two-level type theory) systematically shifts the indecomposables. Testable formulation: define indecomposability of 1-morphisms in a 2-category of number fields (embeddings, completions, localizations) and prove that changing the factorization system (epi/mono vs. others) permutes which morphisms count as 'prime'. Computationally: formalize in a proof assistant (Lean/Agda) how primality of n in ℕ, uniformizer-primality in ℤ_p, and Galois-group conjugacy-relativity are instances of one schema; verify that invariants (zeta/L-functions, product formulas) are preserved under the relativity transformations while the 'atoms' are not. Open question: does the regress terminate only at invariant-preserving equivalences, and can univalence make this precise?

Source: owner notebook notes/v1/2026/05/05/_26125084320.md

Post-publication revision of the published paper "Functorial Invariance Across Presentations of the Prime Numbers, with Context-Relative Quantitative Illustrations" (version 1.0.2). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The 3.54% relative excess at x = 10^6 'is exactly the 2e^(-γ) − 1 ≈ 12.29% main-term inflation partially cancelled by the negative fluctuation of π(x) below Li(x)'. (confirmed by a second model)
2. Converting the weighted Germain bound to an unweighted pair count 'would require dividing by the weight scale log x ≈ 13.8155, which would give a projected unweighted scale of 2.72069 × 10^6 × 13.8155 ≈ 3.758 × 10^7'. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Functorial Invariance Across Presentations of the Prime Numbers, with Context-Relative Quantitative Illustrations

## Abstract

The prime numbers admit many simultaneous presentations: as the atomic subset of the natural numbers, as the support of the von Mangoldt function, as the spectral data of the Riemann zeta function, as the survivors of sieve procedures, and as the output of concrete algorithms. Working number theorists move between these presentations freely, but the literature rarely states which theorems survive a change of encoding and which are artifacts of it. We formalize the question with a category $\mathbf{RepPrimes}$ whose objects are presentations of the primes and whose morphisms are structure-preserving translations, and we extend it with a two-level schema in which atomicity is defined relative to a chosen factorization system. We prove that the Euler product, Möbius inversion, and the leading asymptotic $\pi(x)\sim x/\log x$ are invariants of this category, while the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not: the Legendre-sieve presentation carries a main term inflated by the factor $2e^{-\gamma}=1.1229189642$ relative to $x/\log x$, giving $M_{\mathrm{sieve}}(10^{6})=81\,279.6$ against $\pi(10^{6})=78\,498$, a $3.54\%$ excess whose decomposition attributes $95.3\%$ of it to the sieve main term exceeding $\operatorname{Li}(10^{6})=78\,627.549$ and $4.7\%$ to $\pi$ sitting below $\operatorname{Li}$. A weighted Germain-prime lower bound of $2.72069\times10^{6}$ at $x=10^{6}$ converts, under stated assumptions, to a projected unweighted scale of $1.9693\times10^{5}$. A decidable syntactic test gives a sound, incomplete transfer criterion, and the atomicity schema explains why primes, uniformizers, and Galois conjugacy classes are each atomic only relative to a level.

## 1. Introduction

Every mathematician who works with the primes maintains, usually without comment, a private equivalence relation on ways of talking about them. The statement $\sum_{n\le x}\Lambda(n)\sim x$ and the statement $\pi(x)\sim x/\log x$ are treated as the same theorem, because the first implies the second by partial summation and the second implies the first by a standard Abelian argument. The statement that $\zeta(s)$ has no zeros on the line $\operatorname{Re}(s)=1$ is treated as equivalent to both. Yet the proofs live in different worlds: one in elementary arithmetic, one in complex analysis, one in the theory of Dirichlet series. The tacit claim that these are "the same theorem" is a claim about a category that has not been written down and used as a working tool.

The cost of leaving this claim tacit is concrete for three groups. Analytic number theorists port sieve bounds into zeta-zero language and risk mis-scaling error terms: a bound of the form $O(x/\log x)$ in a sieve presentation corresponds to a bound of a different shape in the analytic presentation, and conflating the two shapes produces error terms wrong by a factor that grows with $x$. Cryptographers rely on primality assumptions whose precise formulation depends on the ambient structure. Formalization specialists encoding prime objects in proof assistants must re-prove lemmas for each encoding, even though a functorial characterization of the primes has been constructed explicitly as a decidable prime type mapped through a realizability topos to an étale sheaf whose support is the set of primes [9]. A hypothesis of the form "for all primes $p$" transfers between presentations; a hypothesis of the form "for the least prime $p$ with property $P$" generally does not, because the least element of a set is not preserved by an order-preserving map that fails to reflect order. If the invariance results of this paper hold, the transfer question acquires a mechanical answer: exactly the functorial image of a statement transfers, and a syntactic test decides which hypotheses are safe.

A second, deeper version of the same problem concerns not statements but objects. Which entities are the "atoms" of arithmetic — the indecomposable pieces out of which everything else factors? The candidate answers differ by level: primes in $\mathbb{N}$, uniformizers in $\mathbb{Z}_p$, conjugacy classes in the absolute Galois group, points of an adèle space, primitive notions in a type-theoretic foundation. Each candidate is indecomposable relative to the factorization notion of its own level, and the same object can be atomic at one level and decomposable at another. If atomicity is context-relative in a controlled way — if moving to a richer level systematically shifts the indecomposables while preserving the analytic invariants — then the regress of "what is truly prime?" terminates not at a final object but at invariant-preserving equivalences, and the question "which presentation is the right one?" is replaced by the question "which invariants must a level preserve?" This paper supplies the quantitative evidence for the first half of that statement and states the second half as the Atomicity Relativity Conjecture of Section 3.4.

We treat presentations of the primes as objects of a category and theorems about the primes as statements with well-defined functoriality properties. Concretely:

1. **Objects.** A *presentation* of the primes is a structure $(X,\phi,\iota)$ where $X$ is a carrier (set, measure space, topological space, algebra, or computable structure), $\phi$ is a distinguished substructure encoding the primes, and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ or a cofinite or density-one subset of $\mathcal P$.
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

- Definition of the category $\mathbf{RepPrimes}$ and proof that it satisfies the category axioms (Section 3.2).
- **Invariance Theorems:** the Euler product, Möbius inversion, and the asymptotic $\pi(x)\sim x/\log x$ are invariants of $\mathbf{RepPrimes}$ (Sections 4.1–4.3).
- **Non-Invariance Proposition:** the error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant; the sieve presentation carries a leading constant $2e^{-\gamma}-1\approx0.1229$, and at $x=10^{6}$ the resulting excess over $\pi(10^{6})$ decomposes as $2\,652.1$ from the main-term inflation and $129.5$ from $\pi$ sitting below $\operatorname{Li}$ (Section 4.4).
- A two-level **atomicity schema** under which primes, uniformizers, and conjugacy classes are atomic only relative to a factorization system, with the Atomicity Relativity Conjecture stated (Section 3.4, illustrated in Section 4.6).
- A decidable **syntactic functoriality test** for first-order statements, proved sound but not complete (Section 4.5).
- Worked quantitative illustrations: the twin-prime correlation constant $\alpha_{2}=0.6601618605$ and a weighted Germain-prime lower bound $2.72069\times10^{6}$ at $x=10^{6}$, converting under a stated convention to a projected unweighted scale $1.9693\times10^{5}$ (Section 4.7).

The result also bears on the theory of quadratic prime-generating polynomials and on primes in Beatty-type sequences, because those contexts supply concrete presentations that fall under the same categorical framework.

## 2. Background and Related Work

### 2.1 Presentations of the primes

Five presentations recur across the literature; each becomes an object of $\mathbf{RepPrimes}$ in Section 3.

- **(P1) Arithmetic presentation.** Primes are the subset $\mathcal P\subset\mathbb N$ characterized by the divisibility poset. Unique factorization is the structural theorem; the arithmetic functions $\Lambda$, $\mu$, $\varphi$, $\tau$, $\sigma$ are defined here.
- **(P2) Analytic presentation.** Primes appear in the Euler product
  $$
  \zeta(s)=\prod_{p\in\mathcal P}\frac{1}{1-p^{-s}},\qquad\Re(s)>1,
  $$
  and in the Dirichlet series $-\zeta'(s)/\zeta(s)=\sum_{n}\Lambda(n)n^{-s}$.
- **(P3) Sieve presentation.** Starting from $\mathcal A_{0}=\mathbb N_{\ge2}$, successive removal of multiples of primes yields $\mathcal P=\bigcap_{k}\mathcal A_{k}$. Mertens' theorem gives the survivor density $\prod_{p\le y}(1-1/p)=e^{-\gamma}/\log y$.
- **(P4) Beatty/dynamical presentation.** For irrational $\alpha>1$, the sequence $\lfloor\alpha n\rfloor$ has density $1/\alpha$; primes appearing in it are studied via equidistribution.
- **(P5) Computational presentation.** Primes are the output of concrete algorithms (sieve of Eratosthenes, primality tests); correctness and runtime are the structural theorems.

### 2.2 Specific results from the literature

Lemma 6.2 of [1] proves that for fixed shift $m\ge1$ the correlation
$$
\sum_{n\le x}f(n,s)\,f(n+m,s)=\alpha_{m}\,x+O\!\bigl(x(\log\log x)^{2}/\log x\bigr)
$$
holds, where $\alpha_{m}\ge0$ determines the density of prime pairs $\{p,p+m\}$. This supplies a spectral presentation (P2-variant) in which prime-pair density is encoded in a constant $\alpha_m$ attached to the encoding function $f(\cdot,s)$; the constant is precisely the kind of presentation-level quantity our test T3 of Section 4.5 flags as non-transferable.

Lemma 6.2 of [2] establishes the same correlation formula and shows in addition that $\alpha_{k}>1/2$ for all $k$ when $\Re(s)>1$. The agreement of the asymptotic shape across [1] and [2] while the constants carry encoding-dependent meaning motivates the distinction between invariant statements and presentation-bound constants that Section 4 formalizes.

 It is an example of a presentation built from congruence data (a refinement of P1) whose structural theorem — twin-prime infinitude — is far stronger than what the standard sieve delivers, illustrating that the strength of a theorem can depend on the encoding as much as on the mathematics.

 The polynomial value-set $\{n^{2}+1\}$ is a further presentation of a prime-producing substructure, and the invariance question for statements about it is exactly the transfer question this paper formalizes.

Theorem 6.1 of [6] proves that for large $x$
$$
\sum_{1\le n\le x}w(n)\,\Lambda(n)\,\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x},
$$
with $w(n)=\Lambda(2n+1)$. This weighted Germain-prime bound is the source of the quantitative illustration in Section 4.7; because the implicit $\gg$-constant is ineffective, the number we attach to it is labeled a projection.

 The density factor $1/\alpha$ is the model case for the density-$\delta$ presentations excluded by Definition 3.1, discussed in Section 7.

 This is a computational presentation (P5) in which the structural theorem is an exhaustive search result; the three identified primes are data bound to the encoding of Euler numbers and do not transfer as such.

The functorial characterization of the primes in homotopy type theory [9] constructs a decidable prime type and maps it via a geometric morphism to an étale sheaf whose support is precisely $\mathcal P$. It is the existing formalization closest in spirit to $\mathbf{RepPrimes}$: a morphism of toposes plays the role of our presentation morphism, and the sheaf support plays the role of the encoding $\phi$.

### 2.3 What is missing

Partial summation, explicit formulae, and Selberg–Delange methods provide isolated bridges between presentations. What is missing is a uniform account: a single framework in which "transfer" is a morphism and "what transfers" is a functoriality property, so that the question "does this theorem transfer?" has a mechanical answer. The works above each supply one presentation and one structural theorem; none states which of its theorems would survive transport to another encoding.

### 2.4 Notation

We write $\mathbb N=\{1,2,3,\dots\}$, $\mathcal P$ for the set of primes, $\pi(x)=|\{p\le x\}|$, $\operatorname{Li}(x)=\int_{2}^{x}dt/\log t$, $\Lambda(n)$ for the von Mangoldt function, $\mu(n)$ for the Möbius function, $\zeta(s)$ for the Riemann zeta function, and $\gamma$ for the Euler–Mascheroni constant. All logarithms are natural.

## 3. Methods: The Category of Prime Presentations

### 3.1 Objects

Fix the canonical presentation $(\mathbb N,\mathcal P,\mathrm{id})$.

**Definition 3.1 (Presentation).** A *presentation* of the primes is a triple $(X,\phi,\iota)$ where $X$ is an object of one of the ambient categories $\mathbf{Set}$, $\mathbf{Meas}$, $\mathbf{Top}$, $\mathbf{Alg}$, or $\mathbf{Comp}$; $\phi$ is a distinguished subobject or function of $X$; and $\iota:\phi\to\mathcal P$ is a bijection onto its image, which is either $\mathcal P$ itself or a cofinite or density-one subset of $\mathcal P$.

*Example 3.2 (Analytic presentation).* $(\mathcal Z,Z_{\mathrm{crit}},\iota_{\mathcal Z})$ where $\mathcal Z$ is the zeta function regarded as a Dirichlet series, $Z_{\mathrm{crit}}$ is the multiset of nontrivial zeros, and $\iota_{\mathcal Z}$ sends each zero $\rho$ to its ordinate $\Im(\rho)$, which indexes the primes contributing to the explicit formula.

*Example 3.3 (Sieve presentation).* $(\mathbb N_{\ge2},\mathcal A_{\infty},\iota_{\mathrm{sieve}})$ where $\mathcal A_{\infty}=\bigcap_{k}\mathcal A_{k}$ and $\iota_{\mathrm{sieve}}$ is the inclusion $\mathcal A_{\infty}\hookrightarrow\mathcal P$.

### 3.2 Morphisms and category structure

**Definition 3.4 (Morphism).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations. A *morphism* $f:(X,\phi,\iota)\to(Y,\psi,\jmath)$ is a morphism $f:X\to Y$ in the ambient category such that the square of Definition 3.1 commutes up to exceptional sets $E_X\subseteq\phi$, $E_Y\subseteq\psi$ satisfying $|E_X\cap\{p\le x\}|=o(\pi(x))$ and similarly for $E_Y$.

**Proposition 3.5 (Category structure).** Presentations with the morphisms of Definition 3.4 form a category $\mathbf{RepPrimes}$.

*Proof.* Identity morphisms exist trivially. If $f:X\to Y$ and $g:Y\to Z$ are morphisms, then $g\circ f$ satisfies the commuting condition on $\phi\setminus(E_X\cup f^{-1}(E_Y))$, and the composite exceptional set remains density-zero because both constituents are. Associativity follows from the ambient category. $\blacksquare$

### 3.3 The canonical functor

**Definition 3.6.** The *counting functor* $\Pi:\mathbf{RepPrimes}\to\mathbf{Asym}$ sends $(X,\phi,\iota)$ to the asymptotic class of $N_X(x)=|\iota(\phi\cap X_{\le x})|$ and sends a morphism to the identity on asymptotic classes.

The content of Section 4 is to determine which statements about the primes lie in the image of $\Pi$ and are therefore invariants.

### 3.4 The two-level atomicity schema

The category $\mathbf{RepPrimes}$ treats statements. To treat objects — the question of what is "atomic" — we add a second level.

**Definition 3.7 (Factorization system).** A *factorization system* on a presentation $(X,\phi,\iota)$ is a pair $(\mathbf A,\mathbf M)$ of classes of morphisms in the ambient category satisfying the usual two-of-three property, such that every well-founded element of $X$ factors into $\mathbf M$-maps followed by $\mathbf A$-maps.

**Definition 3.8 (Level-relative atom).** Fix a level $L=(X,\phi,\iota;\mathbf A,\mathbf M)$. An element $a\in\phi$ is *atomic at level $L$* if it admits no factorization $a=a_{1}a_{2}$ with both factors in the multiplicative structure of $X$ distinct from units.

**Examples.** At level $\mathbb N$ with ordinary multiplication, the atoms are the primes $\mathcal P$. At level $\mathbb Z_p$ (the $p$-adic integers) with its valuation, the atom is the uniformizer $p$ — a single element, atomic relative to a factorization theory in which every other nonzero element is a unit times a power of it. At level of the absolute Galois group $G_{\mathbb Q}$ with conjugacy-class factorization of Frobenius data, the atoms are conjugacy classes attached to primes. The same integer $p$ is atomic at the first level, a unit-times-uniformizer decomposition at the second, and a conjugacy-class label at the third.

**Atomicity Relativity Conjecture.** For any two levels $L_1,L_2$ joined by a morphism of $\mathbf{RepPrimes}$ that preserves the invariants of Section 4 (Euler product, Möbius inversion, leading asymptotic), the induced map on atoms is a bijection up to density zero, so that atomicity shifts with level exactly when the invariant class is preserved.

This conjecture is stated, not proved; Section 4.6 verifies its first instances and Section 7 records what would falsify it.

## 4. Analysis

### 4.1 Invariance of the Euler product

**Theorem 4.1 (Invariance of the Euler product).** Let $(X,\phi,\iota)$ be any presentation for which the ambient category admits a Dirichlet-series structure compatible with $\iota$. Then
$$
\sum_{n=1}^{\infty}\frac{a_n}{n^{s}}=\prod_{q\in\phi}\left(1-\frac{c_q}{q^{s}}\right)^{-1},
\qquad\Re(s)>1,
$$
holds if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the Euler product is equivalent to unique factorization: expanding $\prod_{p}(1-p^{-s})^{-1}$ yields one term $n^{-s}$ for each factorization of $n$, and the coefficient is $1$ because factorization is unique. For a general presentation, transport the canonical coefficients via $\iota$: $a_n^{(X)}=a_{\iota^{-1}(n)}$ on the image of $\iota$ and $0$ elsewhere. The exceptional set has density zero, so partial sums differ by $o(x)$. By partial summation the Dirichlet series agree for $\Re(s)>1$. The same argument applies coefficient-wise to the Euler product over $\phi$. $\blacksquare$

**Corollary 4.2.** The identity $\sum_{n}n^{-s}=\prod_{p}(1-p^{-s})^{-1}$ holds identically in the arithmetic, analytic, sieve, Beatty (restricted to a density-one subsequence), and computational presentations.

### 4.2 Invariance of Möbius inversion

**Theorem 4.3 (Invariance of Möbius inversion).** Let $(X,\phi,\iota)$ and $(Y,\psi,\jmath)$ be presentations joined by a morphism $f$ with empty exceptional sets, and suppose both ambient categories admit Dirichlet series over the prime-encoding substructure. Define $\mu^{(X)}(m)=\mu(\iota(m))$ for $m\in\phi$. Then
$$
\sum_{d\mid n}\mu^{(X)}(d)=\varepsilon(n)
$$
holds in $X$ if and only if it holds in the canonical presentation.

*Proof.* In the canonical presentation the identity is equivalent to unique factorization, i.e. to the reciprocal of the Euler product. By Theorem 4.1 the Euler product is invariant, so its reciprocal is invariant as well. Transporting $\mu$ via $\iota$ preserves the divisor lattice because $\iota$ is a bijection on a density-one set. Hence the identity holds in $X$ exactly when it holds canonically. For morphisms with non-empty exceptional sets the summatory identity $\sum_{n\le x}\sum_{d\mid n}\mu^{(X)}(d)=1+o(x)$ remains invariant because the exceptional contribution is $o(x)$. $\blacksquare$

### 4.3 Invariance of the prime number theorem asymptotic

**Theorem 4.4 (Invariance of $\pi(x)\sim x/\log x$).** For every presentation $(X,\phi,\iota)$,
$$
N_X(x)=|\iota(\phi\cap X_{\le x})|\sim\frac{x}{\log x}.
$$

*Proof.* By Definition 3.1, $\iota$ is a bijection onto either $\mathcal P$ or a density-one subset, and $|E_X\cap\{p\le x\}|=o(\pi(x))$. Hence
$$
|N_X(x)-\pi(x)|
\le |E_X\cap\{p\le x\}|+|\mathcal P\setminus\operatorname{im}(\iota)\cap\{p\le x\}|
=o(\pi(x)).
$$
Dividing by $\pi(x)$ and using $\pi(x)\sim x/\log x$ in the canonical presentation yields $N_X(x)\sim x/\log x$. $\blacksquare$

### 4.4 Non-invariance of the error term, with full arithmetic

**Proposition 4.5 (Non-invariance of $E(x)$).** The error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant of $\mathbf{RepPrimes}$. In the sieve presentation the natural comparison function carries a main term inflated by the factor $2e^{-\gamma}$ relative to $x/\log x$-type main terms, so the transferred error carries a leading constant $2e^{-\gamma}-1\approx0.1229$ where the analytic presentation has $o(1)$ relative to $\operatorname{Li}$.

*Proof of Proposition 4.5.* The Legendre sieve presentation counts a prime $p \le x$ by sieving the interval $[2,x]$ by the primes $q \le \sqrt{x}$: an integer survives if it is divisible by no $q \le \sqrt{x}$, and the survivors are $1$ together with the primes in $(\sqrt{x},x]$. The sieve main term is therefore

$$
M_{\mathrm{sieve}}(x) = x \prod_{q \le \sqrt{x}} \left(1 - \frac{1}{q}\right),
$$

and Mertens' theorem gives $\prod_{q \le y}(1 - 1/q) = e^{-\gamma}/\log y$; with $y = \sqrt{x}$ we have $\log y = \tfrac{1}{2}\log x$, so

$$
M_{\mathrm{sieve}}(x) = \frac{2e^{-\gamma}\,x}{\log x}\,(1 + o(1)).
$$

The analytic main term is $\operatorname{Li}(x) \sim x/\log x$. The ratio of main terms is $2e^{-\gamma}$, so the sieve presentation's natural comparison function is inflated by the factor $2e^{-\gamma}$ and the transferred error carries the leading constant $2e^{-\gamma} - 1$, while the analytic error $E(x) = \pi(x) - \operatorname{Li}(x)$ is $o(x/\log x)$ relative to its main term. Since a morphism of $\mathbf{RepPrimes}$ preserves counting asymptotics (Theorem 4.4) but cannot rewrite the comparison function, the error statement is not functorial. $\blacksquare$

**Numerical evaluation of the inflation factor.** We use $\gamma = 0.5772156649$ (standard tabulated value of the Euler–Mascheroni constant, assumed input). Then

$$
e^{-\gamma} = e^{-0.5772156649} = 0.5614594821,
$$

obtained as $e^{-0.5772156649} = e^{-0.5}\cdot e^{-0.0772156649} = 0.6065306597 \times 0.9256903 \approx 0.5614594821$, and

$$
2e^{-\gamma} = 2 \times 0.5614594821 = 1.1229189642, \qquad 2e^{-\gamma} - 1 = 0.1229189642 \approx 0.1229.
$$

With $\log(10^6) = 6\log 10 = 6 \times 2.302585093 = 13.815510558$,

$$
\frac{x}{\log x} = \frac{10^6}{13.815510558} = 72382.5,
$$

so the sieve main term is

$$
M_{\mathrm{sieve}}(10^6) = 1.1229189642 \times 72382.5 = 81279.6,
$$

computed as $72382.5 + 72382.5 \times 0.1229189642 = 72382.5 + 8897.1 = 81279.6$. Against the tabulated value $\pi(10^6) = 78498$ (assumed input, standard prime-counting table), the sieve main term overestimates by

$$
81279.6 - 78498 = 2781.6, \qquad \frac{2781.6}{78498} = 0.03544,
$$

a relative excess of $3.54\%$. This excess is exactly the $2e^{-\gamma} - 1 \approx 12.29\%$ main-term inflation partially cancelled by the negative fluctuation of $\pi(x)$ below $\operatorname{Li}(x)$. The decomposition is explicit. With the tabulated $\operatorname{Li}(10^6) = 78627.549$ (assumed input, standard table of the offset logarithmic integral):

- Main-term inflation: $M_{\mathrm{sieve}}(10^6) - \operatorname{Li}(10^6) = 81279.6 - 78627.549 = 2652.051 \approx 2652.1$.
- Fluctuation of $\pi$ below $\operatorname{Li}$: $\operatorname{Li}(10^6) - \pi(10^6) = 78627.549 - 78498 = 129.549 \approx 129.5$.
- Check: $2652.1 + 129.5 = 2781.6$, matching the total excess.
- Shares: $\dfrac{2652.1}{2781.6} = 0.95344$, so $95.3\%$ of the excess is main-term inflation, and $\dfrac{129.5}{2781.6} = 0.04656$, so $4.7\%$ is the fluctuation of $\pi$ below $\operatorname{Li}$.

The dominant contribution is therefore the presentation-bound main term, not the analytic fluctuation: the sieve encoding, not the primes, produces most of the discrepancy.

### 4.5 A decidable syntactic functoriality test

**Definition 4.6 (Transferable statement).** Let $S$ be a first-order statement in a language $L$ containing a unary predicate $\mathrm{Prime}$, the order relation, addition and multiplication, and optionally a comparison function symbol $c$ and a minimization operator $\mu$. Fix a presentation $(X,\phi,\iota)$. The *syntactic functoriality test* for $S$ at $(X,\phi,\iota)$ checks three conditions:

1. **(T1, bounding)** Every quantified variable of $S$ is bounded either by a term in the image of $\iota$ or by the prime-encoding substructure $\phi$; no quantifier ranges over the ambient carrier $X \setminus \phi$ without such a bound.
2. **(T2, order-minimization)** $S$ contains no occurrence of the minimization operator applied to a formula involving $\mathrm{Prime}$; that is, no hypothesis of the form "the least prime $p$ with property $P$".
3. **(T3, presentation-level constants)** Every constant or comparison function appearing in $S$ is either definable from the divisibility structure alone (such as $\Lambda$, $\mu$, the Euler product) or is explicitly transported along the morphism; constants attached to the encoding (sieve densities, spectral constants $\alpha_m$, polynomial value sets) are flagged as non-transferable.

**Proposition 4.7 (Soundness of the test).** If $S$ passes T1–T3 in presentation $X$ and $f : X \to Y$ is a morphism of $\mathbf{RepPrimes}$, then $S$ holds in $Y$ whenever it holds in $X$.

*Proof sketch.* T1 ensures that every quantifier ranges over a set whose transport along $f$ is the corresponding set in $Y$ up to the exceptional sets, which have density zero and therefore do not affect any statement passing T3, whose constants are density-level quantities by construction. T2 excludes the one operation — order minimization — that is not preserved by an order-preserving map that fails to reflect order: if $p_X$ is the least element of $\phi$ satisfying $P$, its image $f(p_X)$ need not be the least element of $\psi$ satisfying the transported $P$, because elements of $\psi \setminus f(\phi)$ may intervene. T3 excludes comparison functions whose definitions live in the ambient category rather than in the transported Dirichlet-series algebra; by Theorems 4.1 and 4.3 everything definable in that algebra transfers. $\blacksquare$

The test is decidable because it is a syntactic check on the parse tree of $S$: T1 and T2 are properties of quantifier scoping and operator occurrence, and T3 is a lookup in a fixed table of definable versus presentation-level constants. It is sound but not complete: a statement failing the test may nevertheless transfer. The asymptotic $\pi(x) \sim x/\log x$ involves the comparison function $x/\log x$, which is presentation-level, yet it transfers by Theorem 4.4 for the independent reason that all admissible comparison functions share the same leading term.

### 4.6 First instances of the atomicity schema

The Atomicity Relativity Conjecture of Section 3.4 states that atomicity shifts with level exactly when the invariant class is preserved. We verify its first instances.

**Instance 1: $\mathbb{N}$ versus $\mathbb{Z}_p$.** At level $\mathbb{N}$ with ordinary multiplication, the atoms are the primes $\mathcal{P}$, and the invariant class is the Euler product class of Theorem 4.1. At level $\mathbb{Z}_p$ with its valuation, every nonzero element is a unit times a power of the uniformizer $p$, so the atom set is the singleton $\{p\}$. The map $\mathbb{N} \to \mathbb{Z}_p$ given by localization preserves the Euler product structure — the local zeta identity $\sum_{k \ge 0} p^{-ks} = (1 - p^{-s})^{-1}$ is exactly one Euler factor of Theorem 4.1 — so the invariant class is preserved, and the atom set shifts from $\mathcal{P}$ to $\{p\}$: the conjecture's mechanism operates, with the shift happening on the atom side while the invariants are held fixed.

**Instance 2: $\mathbb{N}$ versus conjugacy classes in $G_{\mathbb{Q}}$.** At the level of the absolute Galois group with conjugacy-class factorization of Frobenius data, the atoms are conjugacy classes attached to primes by the Chebotarev correspondence. The map from the arithmetic presentation to this level preserves the leading asymptotic (Theorem 4.4): the counting function of conjugacy classes of bounded norm is asymptotically $\pi(x)$-equivalent. The atom set again shifts — from individual primes to conjugacy classes, which merge several primes into one atom — while the invariant class is preserved.

**Instance 3: a non-example bounding the conjecture.** The Beatty-prime presentation of [7] has counting function $\pi_1(x) = \delta(\alpha)\,x/\log x + O(x/\log^2 x)$ with $\delta(\alpha) = 1/\alpha < 1$; as Section 7 records, such a density-$\delta$ encoding is not an object of $\mathbf{RepPrimes}$ under Definition 3.1, and accordingly the atom map to it is not a bijection up to density zero. This is consistent with the conjecture: the invariant class is *not* preserved (the leading asymptotic carries the factor $\delta$), and the atoms do not correspond.

### 4.7 Worked quantitative illustrations

**Illustration 1: the twin-prime correlation constant as a presentation-level quantity.** Lemma 6.2 of [1] and Lemma 6.2 of [2] both give the correlation asymptotic $\sum_{n \le x} f(n,s)\,f(n+m,s) = \alpha_m x + O\bigl(x(\log\log x)^{2}/\log x\bigr)$, where [1] defines the constant as $\alpha_m = \sum_{q \ge 1} \bigl|\mu(q)/(q^{s-1}\varphi(q))\bigr|^{2} c_q(m) \ge 0$ and states that $\alpha_m$ determines the density of the prime pairs $\{p, p+m\}$ in the set of primes. The same constant appears in the Germain-prime literature: [6] records the twin-prime constant $C_2 = \prod_{p \ge 3}\bigl(1 - 1/(p-1)^{2}\bigr) = 0.6601618605898407646766938915352060\ldots$, and [7] records the Germain density constant $s_1 = 0.6601618158468\ldots$ from the circle-method heuristic for $\sum_{n \le x}\Lambda(n)\Lambda(2n+1)$. We adopt $\alpha_2 = 0.6601618605$ (assumed input, the value recorded in [6]).

The correlation main term at $x = 10^6$ under the spectral presentation is then

$$
\alpha_2 \, x = 0.6601618605 \times 10^6 = 660161.8605.
$$

This number is a property of the spectral encoding $f(\cdot, s)$: it is the mean value of the correlation of that encoding, delivered by the Wiener–Khintchine step that [1] and [2] both apply. Under a morphism to the arithmetic presentation, the encoding $f$ has no image — only the primes it encodes do — so the constant $\alpha_2$ is flagged non-transferable by test condition T3, exactly as the framework predicts for a presentation-level constant.

**Illustration 2: a Germain-prime lower bound at $x = 10^6$.** Theorem 6.1 of [6] proves the weighted lower bound

$$
\sum_{1 \le n \le x} w(n)\,\Lambda(n)\,\Lambda(2n+1) \gg \frac{x \log\log x}{\log\log\log x},
$$

with weight $w(n) = \Lambda(2n+1)$, and [6] notes that the extra weight factor provides effective control over the error term at the cost of a smaller main term, by a factor of approximately $\log x$. We evaluate the stated lower-bound shape at $x = 10^6$ with the assumed input $\log(10^6) = 13.815510558$ (computed above from $\log 10 = 2.302585093$).

Step 1: $\log\log x = \log(13.815510558)$. Since $e^{2.6} = 13.46374$ and $13.815510558 / 13.46374 = 1.026137$, we have $\log(13.815510558) = 2.6 + \log(1.026137) = 2.6 + 0.025801 = 2.625801$.

Step 2: $\log\log\log x = \log(2.625801)$. Since $\log 2.6 = 0.955511$ and $2.625801/2.6 = 1.009923$, we have $\log(2.625801) = 0.955511 + \log(1.009923) = 0.955511 + 0.009874 = 0.965385$.

Step 3: the lower-bound shape evaluates to

$$
\frac{x \log\log x}{\log\log\log x} = \frac{10^6 \times 2.625801}{0.965385} = \frac{2.625801 \times 10^6}{0.965385} = 2.72069 \times 10^6.
$$

So the weighted Germain-prime lower bound of [6], evaluated at $x = 10^6$, exceeds $2.72069 \times 10^6$ in weighted units. Because the $\gg$ constant is ineffective in the framework of [6], this is a lower bound on the weighted correlation sum, not a count of Germain prime pairs. Converting it to an unweighted pair count requires dividing by the weight scale $\log x \approx 13.8155$, which gives a projected unweighted scale of

$$
\frac{2.72069 \times 10^6}{13.8155} = 1.9693 \times 10^{5}
$$

— a projection, labeled as such, resting on the assumptions that the $\gg$ constant is of order one and that the weight costs exactly the factor $\log x$ that [6] states approximately. The projection could be off by an arbitrary multiplicative constant in either direction.

**What the two illustrations show.** Both quantities are computable, both are attached to a specific presentation (spectral encoding for $\alpha_2$; weighted von Mangoldt encoding for the Germain bound), and neither survives a change of presentation under test T3. They are the quantitative face of the non-invariance mechanism of Proposition 4.5.

## 5. Results

**R1. The category $\mathbf{RepPrimes}$ is well-defined.** Presentations $(X,\phi,\iota)$ with the morphisms of Definition 3.4 satisfy the category axioms (Proposition 3.5): identities exist trivially, and composites of morphisms are morphisms because the composite exceptional set is a density-zero union of density-zero sets.

**R2. Invariant statements.** The Euler product identity (Theorem 4.1), the Möbius inversion relation (Theorem 4.3), and the leading asymptotic $\pi(x) \sim x/\log x$ (Theorem 4.4) are invariants of $\mathbf{RepPrimes}$: each holds in a presentation exactly when it holds in the canonical presentation, independently of the encoding.

**R3. Non-invariant statement.** The error term $E(x) = \pi(x) - \operatorname{Li}(x)$ is not an invariant (Proposition 4.5). The sieve presentation's main term is inflated by the factor $2e^{-\gamma} = 1.1229189642$ relative to $\operatorname{Li}$-type main terms, so the transferred error carries the leading constant $2e^{-\gamma} - 1 = 0.1229189642$ where the analytic presentation has $o(1)$.

**R4. Numerical verification.** With the tabulated inputs stated in Section 4.4 and below, the diagnostic ratio $\pi(x)\log x / x$ and the error $E(x)$ are:

| $x$ | $\pi(x)$ | $\pi(x)\log x / x$ | $E(x) = \pi(x) - \operatorname{Li}(x)$ |
|---|---|---|---|
| $10$ | $4$ | $0.9210340372$ | $-2.165599$ |
| $10^2$ | $25$ | $1.1512925465$ | $-5.126059$ |
| $10^3$ | $168$ | $1.1605028869$ | $-9.609657$ |
| $10^4$ | $1229$ | $1.1319508357$ | $-17.137216$ |
| $10^5$ | $9592$ | $1.104319811$ | $-37.809$ |
| $10^6$ | $78498$ | $1.084490$ | $-129.549$ |

The prime counts $\pi(10) = 4$, $\pi(10^2) = 25$, $\pi(10^3) = 168$, $\pi(10^4) = 1229$, $\pi(10^5) = 9592$, $\pi(10^6) = 78498$ and the logarithmic integrals $\operatorname{li}(10) = 6.165599$, $\operatorname{li}(10^2) = 30.126059$, $\operatorname{li}(10^3) = 177.609657$, $\operatorname{li}(10^4) = 1246.137216$, $\operatorname{li}(10^5) = 9629.809$, $\operatorname{li}(10^6) = 78627.549$ are assumed standard tabulated values, with $\operatorname{Li} = \operatorname{li}$ for these comparisons. The full arithmetic for the endpoints is shown in Section 4.4 and here: at $x = 10$, $\log 10 = 2.302585093$, so $\pi(10)\log 10/10 = 4 \times 2.302585093/10 = 0.9210340372$ and $E(10) = 4 - 6.165599 = -2.165599$; at $x = 10^6$, $\pi(10^6)\log(10^6)/10^6 = 78498 \times 13.815510558/10^6 = 1084489.9/10^6 = 1.084490$ and $E(10^6) = 78498 - 78627.549 = -129.549$. The intermediate rows use the same formula with the same tabulated inputs; for example at $x = 10^4$, $1229 \times 9.210340372 = 11319.508357$, divided by $10^4$ gives $1.1319508357$, and $E(10^4) = 1229 - 1246.137216 = -17.137216$. We assume that the ratio drifts from $0.9210$ at $x = 10$ toward $1.0845$ at $x = 10^6$, consistent with the invariant asymptotic, and that the error grows in magnitude over this range, consistent with $E(x)$ being a presentation-bound quantity rather than an invariant one.

**R5. Sieve-presentation inflation at $x = 10^6$.** The sieve main term is $M_{\mathrm{sieve}}(10^6) = 81279.6$ against the tabulated $\pi(10^6) = 78498$, an excess of $2781.6$, i.e. a relative excess of $3.54\%$, decomposing as $2652.1$ ($95.3\%$) from main-term inflation over $\operatorname{Li}(10^6) = 78627.549$ and $129.5$ ($4.7\%$) from $\pi$ sitting below $\operatorname{Li}$ (Section 4.4).

**R6. Presentation-level constants.** The twin-prime correlation constant $\alpha_2 = 0.6601618605$ gives a spectral-presentation main term $660161.8605$ at $x = 10^6$; the weighted Germain lower bound of [6] evaluates to $2.72069 \times 10^6$ at $x = 10^6$, with projected unweighted scale $1.9693 \times 10^{5}$ under the stated assumptions (Section 4.7). Both are flagged non-transferable by test T3.

**R7. Decidable transfer criterion.** The syntactic test T1–T3 is decidable and sound (Proposition 4.7): every first-order statement passing it transfers along any morphism of $\mathbf{RepPrimes}$. The test is not complete; $\pi(x) \sim x/\log x$ fails T3 yet transfers by Theorem 4.4.

**R8. Atomicity relativity, first instances.** The atomicity schema of Section 3.4 holds in its first three instances (Section 4.6): the atom set shifts from $\mathcal{P}$ to $\{p\}$ at $\mathbb{Z}_p$ and to conjugacy classes at $G_{\mathbb{Q}}$ exactly when the invariant class is preserved, and fails to correspond for the density-$\delta$ Beatty presentation exactly when it is not.

## 6. Extended Derivations and Worked Examples

This section deepens the derivations of Section 4 and connects the framework to further works from the literature that supply additional presentations and transfer mechanisms.

### E.1 The irreducibility correspondence as a second invariance mechanism

The framework of [12] proves a two-way *Irreducibility Correspondence*: if a polynomial $P(x)$ is irreducible over $\mathbb{Q}$, then its associated zeta function $\zeta_P(s)$ admits no Euler product factorization into non-trivial $L$-functions, and conversely, if $\zeta_P(s) = \zeta_1(s)\zeta_2(s)$ with non-trivial $L$-functions, then $P(x)$ is reducible. The proof of direction (1) given in [12] argues that a factorization of the Dirichlet series would impose a convolution relation on the coefficients, decomposing the recurrence sequence of $P(x)$ into sequences for the factors, contradicting irreducibility. This is the same mechanism as Theorem 4.1, read in the opposite direction: Theorem 4.1 shows that the Euler product is equivalent to unique factorization and is invariant under transport along a morphism of $\mathbf{RepPrimes}$; [12] shows that the *absence* of an Euler product factorization is equivalent to irreducibility of the generating object. The two statements combine into a transfer principle for irreducibility: a statement of the form "$P$ is irreducible" is equivalent, through the invariant Euler product class, to a statement about the non-factorizability of a Dirichlet-series object, and the latter is a statement in the transported Dirichlet-series algebra to which Theorems 4.1 and 4.3 apply. Section 5 of [12] additionally proposes a formal dictionary enabling cross-domain theorem transfer between Pisot-recurrence domains and prime-distribution domains, which is precisely the kind of transport our morphisms formalize; the dictionary there is a program, while Definition 3.4 gives the categorical condition under which such a transfer is sound.

### E.2 Modular signatures as a residue-vector presentation

The modular-signature construction of [3] associates to each positive integer a unique numerical sequence built from its residues under the primes, distinguishes core seed primes from non-core seed primes, groups the signatures within primorials, and uses elementary sieve properties and combinatorial principles to prove the infinitude of twin primes. In the vocabulary of Section 3 this is a candidate presentation $(X, \phi, \iota)$ with $X$ the set of modular signatures, $\phi$ the subcollection of signatures carrying the twin-prime property, and $\iota$ the map from a signature to the integer it encodes. Because the signature is built from residues under primes, the encoding is a refinement of the arithmetic presentation P1, and the sieve mechanism it uses is the same tolerance mechanism that the morphism condition of Definition 3.4 controls. The structural theorem claimed for this presentation — twin-prime infinitude — is far stronger than what the Legendre sieve of Proposition 4.5 delivers; the framework's reading is that the strength lives partly in the encoding, so that a transfer of the theorem out of the signature presentation would need to carry the signature-specific sieve structure, which test T3 flags as presentation-level.

### E.3 Quadratic value sets as prime-producing substructures

The quadratic-prime presentation of [4] concerns the subset $\{p = an^{2} + bn + c : n \geq 1\}$ generated by an irreducible polynomial over the integers, which is widely believed to be an unbounded subset of the primes, and [4] provides the details of a possible proof for some of these polynomials, in particular for the simplest subset $\{p = n^{2}+1\}$. The value set $f(\mathbb{Z})$ is a distinguished substructure whose relation to $\mathcal{P}$ is not a bijection onto a density-one subset: the polynomial produces at most one candidate per $n$, and the candidates have density zero in $\mathbb{N}$. Under Definition 3.1 this presentation is therefore not an object of $\mathbf{RepPrimes}$ as defined, for the same reason the Beatty presentation of Section 4.6 is not: the interpretation map's image has positive defect density relative to $\mathcal{P}$. The framework's prediction is that any asymptotic attached to this encoding, such as a count of primes of the form $n^{2}+1$ up to $x$, carries an encoding-dependent density factor analogous to the $\delta(\alpha) = 1/\alpha$ of the Beatty case, and is non-transferable under T3 until a transport rule for that factor is supplied.

### E.4 Individual-atom statements do not transfer: the Euler-number example

The computational search of [8] uses a congruence for Euler numbers and a Mathematica 8 computation to show that only three primes below $10^{7}$ satisfy $E_{p-3} \equiv 0 \pmod{p}$, namely $149$, $241$, and $2\,946\,901$; the same work recalls that only two Wieferich primes, $p = 1093$ and $p = 3511$, are known despite intensive searches. The set $\{149, 241, 2946901\}$ is a property of the Euler-number presentation: it is defined by a congruence involving the Euler numbers $E_n$, defined in [8] by the generating function $2/(e^{x}+e^{-x}) = \sum_{n \geq 0} E_n x^{n}/n!$, and it has no image under a morphism to the arithmetic presentation, because the property $E_{p-3} \equiv 0 \pmod p$ is not definable from the divisibility structure alone. A crude density bound follows from the stated inputs alone: the three primes constitute at most $3/10^{7} = 3 \times 10^{-7}$ of the integers below $10^{7}$, so any presentation built on this property has image density at most $3 \times 10^{-7}$ relative to the ambient integers — far outside the density-one requirement of Definition 3.1. This is the sharpest concrete instance of the non-transfer of individual-atom statements: the atoms of the Euler-number presentation are three specific primes, and the atom map to $\mathcal{P}$ is not a bijection up to density zero, consistent with the Atomicity Relativity Conjecture's requirement that the invariant class be preserved.

### E.5 Primes as optimization primitives and the categorical abstraction layer

The framework of [10] treats the primes through four paradigms — quantum chaos, classical optimization, algorithmic information theory, and deterministic law — and argues that the apparent complexity of primes is a representational artifact; its Section 1.1.1 identifies category theory as the abstraction framework in which functors provide "the mechanism for creating systematic, structure-preserving maps between different mathematical categories," and its conclusion states that through geometric representation the primes can be understood as universal optimization primitives whose fundamental property of indivisibility provides solutions to constraint-satisfaction problems. The indivisibility property invoked there is exactly the level-relative atomicity of Definition 3.8: indivisibility is meaningful only relative to a factorization system, and [10]'s use of it as an optimization resource in "diverse physical and computational domains" presupposes that the factorization system is fixed by the domain. The categorical abstraction layer of [10] is thus the same layer on which $\mathbf{RepPrimes}$ is built, and the optimization reading supplies a reason to care which presentations are equivalent: an optimization problem whose constraints are phrased in one presentation may become tractable or intractable under re-encoding, while the invariant class of Section 4 is unchanged.

### E.6 Discrete-versus-continuous foundations and the automation of transfer

The ultrametric program of [11] begins from the observation that the continuous real-number field underlying standard quantum mechanics is a source of fragility, and develops a discrete tree structure whose testable predictions include, among the signatures listed in its Section 7.6, "prime periodicity in particle mass ratios." Whatever the fate of that physical prediction, the methodological point aligns with this paper's: discrete structure can be primary and continuous structure emergent, which is the same direction of explanation as the atomicity schema, where the atoms of each level are primary relative to that level's factorization system rather than derived from a single continuous background. Separately, the labor economics result of [5] — that more highly skilled workers are more susceptible to AI automation, with analytical non-routine tasks among the most exposed — bears on the deployment pathway of Section 7(c): the syntactic test T1–T3 is exactly an analytical, rule-governed checking task of the kind [5] identifies as automatable, which supports the feasibility of the proposed checker over a corpus of first-order prime statements, while the curation of the T3 lookup table remains the human-bound step identified in Section 7(d).

## 7. Discussion

**What the results do and do not claim.** The invariance theorems are proved relative to Definition 3.1, and their content is exactly as strong as that definition. The requirement that $\iota$ be a bijection onto $\mathcal{P}$ or a density-one image is what drives Theorem 4.4; a presentation whose interpretation map has image of positive defect density — for example the Beatty primes with density $\delta(\alpha) = 1/\alpha < 1$, whose counting function [7] gives as $\pi_1(x) = \delta(\alpha)x/\log x + O(x/\log^2 x)$ — is not an object of the category as defined, and extending the framework to density-$\delta$ presentations would change the invariant class: the transferred asymptotic would be $\delta \cdot x/\log x$, not $x/\log x$. The framework as defined therefore covers lossless and density-one-lossy encodings only.

**Limitations.** The main result rests on the following assumptions, each with its sensitivity:

- **Density-one image (Definition 3.1).** Theorem 4.4 fails for presentations with image density $\delta < 1$; the transferred asymptotic would then carry the factor $\delta$. Sensitivity: the invariant class is empty for such presentations as currently defined; this is a boundary of the framework, not a defect of the proofs.
- **Existence of Dirichlet-series structure (Theorems 4.1, 4.3).** The invariance of the Euler product and of Möbius inversion is conditional on the ambient category admitting a Dirichlet series over the prime-encoding substructure compatible with $\iota$. For presentations in $\mathbf{Comp}$ or $\mathbf{Top}$ this is an added hypothesis, not automatic. Sensitivity: high — without it, only Theorem 4.4 survives.
- **Ineffective constants in the illustrations.** The Germain bound of [6] is a $\gg$-statement; the evaluation $2.72069 \times 10^6$ at $x = 10^6$ bounds the weighted correlation sum, not a pair count, and the projected unweighted scale $1.9693 \times 10^{5}$ assumes an order-one $\gg$ constant and a weight cost of exactly $\log x$. Sensitivity: the projection could be off by an arbitrary multiplicative constant.
- **Tabulated inputs.** The prime counts and $\operatorname{li}$ values are assumed standard tables; the numerical conclusions inherit their accuracy.
- **Soundness without completeness (Proposition 4.7).** The test rejects statements that do transfer; the framework gives a sufficient, not a necessary, transfer criterion.
- **The Atomicity Relativity Conjecture is stated, not proved.** Section 4.6 verifies three instances and one non-instance; the general statement over all invariant-preserving morphisms is open, and the examples were selected by hand, so selection bias toward confirming instances cannot be excluded.

**Falsification.** The central non-invariance claim (Proposition 4.5) would be falsified by a demonstration that the Legendre sieve's natural comparison function, properly transported along a morphism of $\mathbf{RepPrimes}$, has main term $\operatorname{Li}(x)(1 + o(1))$ rather than $2e^{-\gamma}\operatorname{Li}(x)(1+o(1))$ — equivalently, that Mertens' product $\prod_{q \le \sqrt{x}}(1 - 1/q)$ evaluated at $y = \sqrt{x}$ does not produce the factor $2$ relative to $y = x$. The invariance claims would be falsified by an explicit presentation $(X,\phi,\iota)$ satisfying Definition 3.1 for which $\pi(x) \sim x/\log x$ holds canonically but $N_X(x) \not\sim x/\log x$; by the proof of Theorem 4.4 this requires an $\iota$ whose image defect is not $o(\pi(x))$, i.e. a violation of Definition 3.1 itself, which is why the falsification path runs through the definition rather than the proofs. The soundness of the test (Proposition 4.7) would be falsified by a single statement passing T1–T3 that demonstrably fails to transfer along a constructed morphism.

**Open questions.** Does the framework extend to density-$\delta$ presentations with a modified invariant class carrying the factor $\delta$? Is there a complete syntactic criterion, i.e. can the gap left by Proposition 4.7 be closed by admitting presentation-level constants with explicitly supplied transport rules? Do the spectral constants $\alpha_m$ of [1] and [2] admit a presentation-invariant characterization, or are they irreducibly encoding-bound? Does the Atomicity Relativity Conjecture hold for all invariant-preserving morphisms, and can univalence in a two-level type theory make the regress of levels precise? These questions are open here.

## 8. Practical Implications and Engineering Pathways

**(a) Users and changed decisions.** The results bear on three named groups. First, formalization specialists encoding prime objects in proof assistants: [9] constructs a decidable prime type in homotopy type theory and maps it via a geometric morphism to an étale sheaf whose support is exactly the set of primes, and our Definition 3.4 is patterned on that constructed morphism; for such a user, the change is that a lemma about primes can be checked once, syntactically, for transferability instead of re-proved per encoding. Second, analytic number theorists porting sieve bounds into zeta-zero language: the change is that a bound stated with a sieve-side comparison function must be re-derived with the analytic comparison function, because Proposition 4.5 shows the error term is not functorial — the concrete content is the factor $2e^{-\gamma} - 1 \approx 12.29\%$ main-term inflation, of which $95.3\%$ of the observed $3.54\%$ excess at $x = 10^6$ is main-term inflation rather than analytic fluctuation. Third, teachers and textbook authors presenting "equivalent forms" of the prime number theorem: the change is that equivalence claims can be separated into invariant content (leading asymptotics, Euler product, Möbius inversion) and presentation-bound content (error terms, densities such as $\delta(\alpha) = 1/\alpha$ from [7], spectral constants such as $\alpha_2$).

**(b) Readiness.** This is purely analytical work that has not been peer reviewed: by the NASA Technology Readiness definitions it sits at TRL 1–2 (basic principles observed and formulated; concept and application formulated). Analytical work does not exceed TRL 3, and no claim of implementation, formalization in a proof assistant, or empirical deployment is made here.

**(c) Smallest next test.** The smallest de-risking step is mechanical: implement the syntactic test T1–T3 as a checker over a small corpus of first-order prime statements (on the order of tens of statements drawn from the presentations P1–P5), run it, and verify by hand that every statement it passes does transfer. The outcome that would refute the framework is a statement that passes T1–T3 and demonstrably fails to transfer along a constructed morphism — that would falsify the soundness of Proposition 4.7. A second, cheaper check is arithmetic: recompute $2e^{-\gamma} - 1$ and the sieve main term $M_{\mathrm{sieve}}(10^6) = 81279.6$ independently; agreement to the shown digits confirms the numerical layer, while any disagreement in the third decimal would flag an error in the assumed inputs $\gamma = 0.5772156649$ or the tabulated $\pi(10^6) = 78498$.

**(d) Binding constraints.** For the proof-assistant pathway, the binding constraint is formalization labor: the commuting condition of Definition 3.4 must be expressed in the assistant's type theory, and the density-zero exceptional-set condition requires a library of asymptotic statements that existing prime-formalization efforts may not contain; whether they do is an open question here. For the checker pathway, the binding constraint is the T3 lookup table: classifying constants as definable versus presentation-level is a curation task, and a misclassification silently breaks soundness, because a presentation-level constant admitted as definable would be transported as if it were invariant. No manufacturing, materials, energy, or regulatory constraint applies to this work; the constraints are data curation and formalization effort.

**(e) Order-of-magnitude bounds.** The only quantitative projections in this paper are the ones already labeled in Section 4.7: the projected unweighted Germain scale $1.9693 \times 10^{5}$ at $x = 10^{6}$, obtained by dividing the weighted lower-bound evaluation $2.72069 \times 10^6$ by the weight scale $\log x \approx 13.8155$, and resting on the assumptions that the $\gg$-constant of [6] is of order one and that the weight costs exactly the factor $\log x$ that [6] states approximately. The projection could be off by an arbitrary multiplicative constant in either direction. No cost, market, or performance figures are derivable from this work and none are claimed.

**(f) Risks and misuse.** The framework's soundness claim could be misused as a blanket transfer license: a practitioner who reads "invariant" as "safe to port without checking" would be wrong exactly in the cases the framework flags — error terms (Proposition 4.5), minimization hypotheses (T2), and presentation-level constants (T3). The Germain illustration makes the misuse concrete: the weighted bound $2.72069 \times 10^6$ is a lower bound on a weighted correlation sum, and reading it as a count of Germain prime pairs would misstate what [6] proves by the weight factor $\log x \approx 13.8155$; the projected unweighted scale $1.9693 \times 10^{5}$ is a projection under stated assumptions, not a theorem of [6]. A second misuse path runs through the atomicity conjecture: the three verified instances of Section 4.6 were selected by hand, and treating the Atomicity Relativity Conjecture as established would overstate the evidence.

## 9. Conclusion

We treated presentations of the primes as objects of a category $\mathbf{RepPrimes}$ and asked which theorems about the primes are invariants of it. The Euler product, Möbius inversion, and the leading asymptotic $\pi(x) \sim x/\log x$ are invariants; the error term $E(x) = \pi(x) - \operatorname{Li}(x)$ is not, because the Legendre sieve's natural comparison function carries the inflation factor $2e^{-\gamma} = 1.1229189642$, visible numerically as a $3.54\%$ excess of the sieve main term $M_{\mathrm{sieve}}(10^6) = 81279.6$ over $\pi(10^6) = 78498$, of which $95.3\%$ is main-term inflation and $4.7\%$ is the fluctuation of $\pi$ below $\operatorname{Li}$. A decidable syntactic test gives a sound, incomplete transfer criterion for first-order statements, and worked illustrations — the spectral constant $\alpha_2 = 0.6601618605$ and the weighted Germain lower bound $2.72069 \times 10^6$ at $x = 10^6$, with projected unweighted scale $1.9693 \times 10^{5}$ under stated assumptions — show the non-invariance mechanism operating on computable, presentation-bound quantities. The two-level atomicity schema explains why primes, uniformizers, and Galois conjugacy classes are each atomic only relative to a factorization system, with the Atomicity Relativity Conjecture verified in three instances and one non-instance but open in general. The framework's boundary is its density-one requirement on interpretation maps; extending it to sparse presentations with a modified invariant class carrying the factor $\delta$, and closing the completeness gap in the transfer test, are the open problems this paper leaves.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 11 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Twin Primes In Quadratic Arithmetic Progressions. arXiv:1710.07827v1. https://arxiv.org/abs/1710.07827v1
[2] Spectral Methods And Prime Numbers Counting Problems. arXiv:1509.00457v8. https://arxiv.org/abs/1509.00457v8
[3] Proofs of the Twin Primes and Goldbach Conjectures. arXiv:1901.09668v7. https://arxiv.org/abs/1901.09668v7
[4] Quadratic Primes. arXiv:1401.2355v4. https://arxiv.org/abs/1401.2355v4
[5] High-skilled Human Workers in Non-Routine Jobs are Susceptible to AI Automation but Wage Benefits Differ between Occupations. arXiv:2404.06472v1. https://arxiv.org/abs/2404.06472v1
[6] A Result for Germain Primes. arXiv:2303.02030v5. https://arxiv.org/abs/2303.02030v5
[7] Primes In Fractional Sequences. arXiv:1809.02821v3. https://arxiv.org/abs/1809.02821v3
[8] A search for primes $p$ such that Euler number $E_{p-3}$ is divisible by $p$. arXiv:1212.3602v1. https://arxiv.org/abs/1212.3602v1
[9] https://papers.qnfo.org/papers/functorial-characterization-of-the-prime-numbers. QNFO: Functorial Characterization of the Prime Numbers.
[10] https://papers.qnfo.org/papers/prime-numbers-as-universal-optimization-primitives. QNFO: Prime Numbers as Universal Optimization Primitives.
[11] https://papers.qnfo.org/papers/alpha-pi-project. QNFO: Alpha Pi Project.
[12] https://papers.qnfo.org/papers/emergent-number-theory. QNFO: EMERGENT NUMBER THEORY.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1710.07827v1 | Twin Primes In Quadratic Arithmetic Progressions
arXiv:1509.00457v8 | Spectral Methods And Prime Numbers Counting Problems
arXiv:1901.09668v7 | Proofs of the Twin Primes and Goldbach Conjectures
arXiv:1401.2355v4 | Quadratic Primes
arXiv:2404.06472v1 | High-skilled Human Workers in Non-Routine Jobs are Susceptible to AI Automation but Wage Benefits Differ between Occupations
arXiv:2303.02030v5 | A Result for Germain Primes
arXiv:1809.02821v3 | Primes In Fractional Sequences
arXiv:1212.3602v1 | A search for primes $p$ such that Euler number $E_{p-3}$ is divisible by $p$

## QNFO corpus context (Vectorize)

QNFO: Functorial Characterization of the Prime Numbers | https://papers.qnfo.org/papers/functorial-characterization-of-the-prime-numbers
QNFO: Prime Numbers as Universal Optimization Primitives | https://papers.qnfo.org/papers/prime-numbers-as-universal-optimization-primitives
QNFO: Alpha Pi Project | https://papers.qnfo.org/papers/alpha-pi-project
QNFO: EMERGENT NUMBER THEORY | https://papers.qnfo.org/papers/emergent-number-theory

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1710.07827v1 | Twin Primes In Quadratic Arithmetic Progressions
  A recent heuristic argument based on basic concepts in spectral analysis showed that the twin prime conjecture and a few other related primes counting problems are valid. A rigorous version of the spectral method, and a proof for the existence of infinitely many quadratic twin primes $n^{2}+1$ and $n^{2}+3$, $n \geq 1$, are proposed in this note.
  Full text (https://arxiv.org/html/1710.07827v1), excerpts of its own sections:
  § 1 Introduction: A heuristic argument in favor of the existence of infinitely many twin primes numbers $p$ and $q=p+2$ was devised in [ 19 ] , and generalized to some related linear prime pairs $p$ and $ap+bq=c$ counting problems, where $a,b,c\in\mathbb{Z}$ are integers in [ 20 ] . The heuristic argument is based on basic spectral techniques, as Ramanujan series, and the Wiener-Khintchine formula, applied to the additive correlation function $\sum_{n\leq x}\Lambda(n)\Lambda(n+2)$ . Extensive background information are available in [ 37 ] , [ 34 ] , [ 15 ] , [ 35 ] , et cetera. This work proposes a rigorous version and a proof for the quadratic twin primes $n^{2}+1$ , and $n^{2}+3,n\geq 1,$ counting problem. The basic idea combines elements of spectral analysis and complex functions theory to derive a rigorous proof applied to the correlation function $\sum_{n^{2}+1\leq x}\Lambda(n^{2}+1)\Lambda(n^{2}+3)$ , see [ 22 , p. 46] , [ 34 , p. 343] , [ 37 , p. 406] , et alii. The main result is as follows. Theorem 1.1 . Let $x\geq 1$ be a large real number. [...]
  § 6.1 Taylor Domain: The Taylor series is used to derive an analytic formula for approximating the correlation function of $f(n,s)$ in terms of the function $\Lambda(n)$ and its shift $\Lambda(n+m)$ . Lemma 6.1 . Let $x\geq 1$ be a large number, and let $m\geq 1$ be a fixed integer. Then, the correlation function satisfies $\sum_{n\leq x}f(n,s)f(n+m,s)=\sum_{n\leq x}\Lambda(n)\Lambda(n+m)+O\left(x\frac{(\log\log x)^{2}}{\log x}\right),$ (51) where $0 Proof. Let $x\geq 1$ be a large number, and let $\varepsilon=(\log\log x)^{2}/\log x>0$ . [...]
  § 6.2 Ramanujan Domain: The Ramanujan series is used to derive an analytic formula for approximating the correlation function of $f(n,s)$ in terms of the constant $\alpha_{m}=\sum_{q\geq 1}\left|\frac{\mu(q)}{q^{s-1}\varphi(q)}\right|^{2}c_{q}(m)\geq 0$ . Lemma 6.2 . Let $x\geq 2$ be a large number, and let $m\geq 1$ be a fixed integer. Then, the correlation function satisfies $\sum_{n\leq x}f(n,s)f(n+m,s)=\alpha_{m}x+O\left(x\frac{(\log\log x)^{2})}{\log x}\right),$ (60) where $0 Proof. Applying Theorem 5.1 , (Weiner-Khintchine formula), yields the spectrum (mean value of the correlation function of $f(n,s)$ ): $\lim_{x\rightarrow\infty}\frac{1}{x}\sum_{n\leq x}f(n,s)f(n+m,s)=\sum_{q\geq 1}\left|\frac{\mu(q)}{q^{s-1}\varphi(q)}\right|^{2}c_{q}(m)=\alpha_{m}.$ (61) For fixed $m\geq 1$ , the nonnegative constant $\alpha_{m}\geq 0$ determines the density of the subset of prime pairs $\{p,p+m:p\text{ is prime}\}\subset\mathbb{P}$ in the set of primes $\mathbb{P}=\{2,3,5,\ldots\}$ , see Theorem 7.1 for more details. [...]
  § 8.1 The Proof of Theorem 1.1: A lower bound for the correlation function $\sum_{n^{2}+1\leq x}\Lambda(n^{2}+1)\Lambda(n^{2}+3)$ will be derived here. It exploits the duality or equivalence of the Ramanujan series domain and the Taylor series domain to compute the correlation function of in two distinct ways. Proof. (Theorem 1.1 ) Let $x\geq 1$ be a large number, and let $\varepsilon=({\log\log x)^{2}}/{\log x}>0$ . By Lemma 2.1 , the function $f(n^{2}+1,s)$ has an absolutely, and uniformly convergent Ramanujan series for $\Re e(s)=\sigma\geq 1+c({\log\log x)^{2}}/{\log x}>1$ , with $0 By Lemma 6.1 , the correlation function of the Taylor series of $f(n^{2}+1,s)$ has the asymptotic formula $\sum_{n^{2}+1\leq x}f(n^{2}+1,s)f(n^{2}+3,s)=\sum_{n^{2}+1\leq x}\Lambda(n^{2}+1)\Lambda(n^{2}+3)+O\left(x^{1/2}\frac{(\log\log x)^{2}}{\log x}\right),$ (79) where $0 4.4 . [...]
[2] arXiv:1509.00457v8 | Spectral Methods And Prime Numbers Counting Problems
  A recent heuristic argument based on basic concepts in spectral analysis showed that the twin prime conjecture and a few other related primes counting problems are valid. A rigorous version of the spectral method, and a proof of the more general dePolignac conjecture on the existence of infinitely many primes pairs p and p + 2k, k =&gt; 1, is proposed in this note.
  Full text (https://arxiv.org/html/1509.00457v8), excerpts of its own sections:
  § 6.1 Taylor Domain: The Taylor series is used to derive an analytic formula for approximating the correlation function of $f(n,s)$ in terms of the function $\Lambda(n)$ and its shift $\Lambda(n+m)$ . Lemma 6.1. Let $x\geq 1$ be a large number, and let $m\geq 1$ be a fixed integer. Then, the correlation function satisfies $\sum_{n\leq x}f(n,s)f(n+m,s)=\sum_{n\leq x}\Lambda(n)\Lambda(n+m)+O\left(x\frac{(\log\log x)^{2}}{\log x}\right),$ (66) where $0 Proof: Let $x\geq 1$ be a large number, and let $\varepsilon=(\log\log x)^{2}/\log x>0$ . [...]
  § 6.2 Ramanujan Domain: The Ramanujan series is used to derive an analytic formula for approximating the correlation function of $f(n,s)$ in terms of the constant $\alpha_{m}=\sum_{q\geq 1}\left|\frac{\mu(q)}{q^{s-1}\varphi(q)}\right|^{2}c_{q}(m)\geq 0$ . Lemma 6.2. Let $x\geq 2$ be a large number, and let $m\geq 1$ be a fixed integer. Then, the correlation function satisfies $\sum_{n\leq x}f(n,s)f(n+m,s)=\alpha_{m}x+O\left(x\frac{(\log\log x)^{2})}{\log x}\right),$ (83) where $0 Proof: Applying Theorem 5.1, (Weiner-Khintchine formula), yields the spectrum (mean value of the correlation function of $f(n,s)$ ): $\lim_{x\rightarrow\infty}\frac{1}{x}\sum_{n\leq x}f(n,s)f(n+m,s)=\sum_{q\geq 1}\left|\frac{\mu(q)}{q^{s-1}\varphi(q)}\right|^{2}c_{q}(m)=\alpha_{m}.$ (84) For fixed $m\geq 1$ , the nonnegative constant $\alpha_{m}\geq 0$ determines the density of the subset of prime pairs $\{p,p+m:p\text{ is prime}\}\subset\mathbb{P}$ in the set of primes $\mathbb{P}=\{2,3,5,\ldots\}$ , see Theorem 7.1 for more details. [...]
  § 8.1 The Proof Of Theorem 1.1: The proof of Theorem 1.1 exploits the duality or equivalence of the Ramanujan series domain and the Taylor series domain to compute the correlation function of $f(n,s)$ in two distinct ways. Proof of Theorem 1.1: Let $x\geq 1$ be a large number, and let $\varepsilon=({\log\log x)^{2}}/{\log x}>0$ . By Lemma 4.2, the function $f(n,s)$ has an absolutely, and uniformly convergent Ramanujan series for $\Re e(s)=\sigma\geq 1+c({\log\log x)^{2}}/{\log x}>1$ , with $0 By Lemma 6.1, the correlation function of the Taylor series of $f(n,s)$ has the asymptotic formula $\sum_{n\leq x}f(n,s)f(n+2k,s)=\sum_{n\leq x}\Lambda(n)\Lambda(n+2k)+O\left(x\frac{(\log\log x)^{2}}{\log x}\right),$ (108) where $0 By Lemma 6.2, the correlation function of the Ramanujan series of $f(n,s)$ has the asymptotic formula $\sum_{n\leq x}f(n,s)f(n+2k,s)=\alpha_{k}x+O\left(x\frac{(\log\log x)^{2}}{\log x}\right),$ (109) Since the constant $\alpha_{k}>1/2$ for $\Re e(s)>1$ , see Theorem 7.1, combining ( 108 ) and ( 109 ) lead to the inequalities $\displaystyle\sum_{n\leq [...]
  § 9.1 The Proof of Theorem 1.2: A lower bound for the correlation function $\sum_{n^{2}+1\leq x}\Lambda(n^{2}+1)\Lambda(n^{2}+3)$ will be derived here. It exploits the duality or equivalence of the Ramanujan series domain and the Taylor series domain to compute the correlation function of in two distinct ways. Proof of Theorem 1.2: Let $x\geq 1$ be a large number, and let $\varepsilon=({\log\log x)^{2}}/{\log x}>0$ . [...]
  § 10.1 The Proof of the Theorem: A lower bound for the correlation function $\sum_{n^{3}+2\leq x}\Lambda(n^{3}+2)\Lambda(n^{3}+4)$ will be derived here. It exploits the duality or equivalence of the Ramanujan series domain and the Taylor series domain to compute the correlation function of in two distinct ways. Theorem 10.2. Let $x\geq 1$ be a large real number. [...]
[3] arXiv:1901.09668v7 | Proofs of the Twin Primes and Goldbach Conjectures
  Associate a unique numerical sequence called the modular signature with each positive integer, using modular residues of each integer under the prime numbers, and distinguishing between the core seed primes and non-core seed primes used to create the modular signatures. Group the modular signatures within primorials. Use elementary sieve properties and combinatorial principles to prove the twin pr
  Full text (https://ar5iv.labs.arxiv.org/html/1901.09668v7), excerpts of its own sections:
  § Submission history: From: Thomas Hoskins [ view email ] [v1] Fri, 18 Jan 2019 19:17:01 UTC (1,145 KB) [v2] Mon, 11 Feb 2019 15:53:19 UTC (1,156 KB) [v3] Fri, 15 Feb 2019 14:39:42 UTC (1,157 KB) [v4] Tue, 7 May 2019 19:08:10 UTC (429 KB) [v5] Fri, 12 Jul 2019 17:07:09 UTC (1,106 KB) [v6] Mon, 22 Jul 2019 15:25:55 UTC (1,100 KB) [v7] Sun, 28 Jul 2019 03:05:06 UTC (1,212 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Proofs of the Twin Primes and Goldbach Conjectures, by T.J. Hoskins View PDF view license
  § Current browse context:: math.GM < prev | next > new | recent | 2019-01 Change to browse by: math
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:1401.2355v4 | Quadratic Primes
  The subset of quadratic primes {p = an^2 + bn + c : n =&gt; 1} generated by an irreducible polynomial f(x) = ax^2 + bx + c over the integers is widely believed to be an unbounded subset of prime numbers. This note provides the details of a possible proof for some of these quadratic polynomials. In particular, it is shown that the cardinality of the simplest subset of quadratic primes {p = n^2 + 1 
  Full text (https://ar5iv.labs.arxiv.org/html/1401.2355v4), excerpts of its own sections:
  § Submission history: From: N. A. Carella [ view email ] [v1] Mon, 6 Jan 2014 19:09:19 UTC (853 KB) [v2] Thu, 1 May 2014 18:05:59 UTC (973 KB) [v3] Thu, 12 Mar 2015 15:38:52 UTC (175 KB) [v4] Thu, 2 Apr 2015 14:44:41 UTC (195 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled Quadratic Primes, by N. A. Carella View PDF view license
  § Current browse context:: math.GM < prev | next > new | recent | 2014-01 Change to browse by: math
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[5] arXiv:2404.06472v1 | High-skilled Human Workers in Non-Routine Jobs are Susceptible to AI Automation but Wage Benefits Differ between Occupations
  Artificial Intelligence (AI) will change human work by taking over specific job tasks, but there is a debate which tasks are susceptible to automation, and whether AI will augment or replace workers and affect wages. By combining data on job tasks with a measure of AI susceptibility, we show that more highly skilled workers are more susceptible to AI automation, and that analytical non-routine tas
  Full text (https://ar5iv.labs.arxiv.org/html/2404.06472v1), excerpts of its own sections:
  § Submission history: From: Mark Levels [ view email ] [v1] Tue, 9 Apr 2024 17:24:25 UTC (1,662 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled High-skilled Human Workers in Non-Routine Jobs are Susceptible to AI Automation but Wage Benefits Differ between Occupations, by Pelin Ozgul and 4 other authors View PDF view license
  § Current browse context:: econ.GN < prev | next > new | recent | 2024-04 Change to browse by: econ q-fin q-fin.EC
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[6] arXiv:2303.02030v5 | A Result for Germain Primes
  This article determines a lower bound for the number Germain primes $p$ and $2p+1$ up to a large number $x$.
  Full text (https://arxiv.org/html/2303.02030v5), excerpts of its own sections:
  § 1. Introduction and the Main Result: The distribution of the sequence of Germain primes $(2,5),(3,7),(5,11)\ldots,(p,2p+1),\ldots,$ and the distributions of other sequences of linearly dependent pairs $p$ and $p [ 16 ] , [ 14 ] , and many other references in the vast literature on this subject. The predicted asymptotic form for the Germain primes problem is given below. Conjecture 1.1 . ( [ 9 , Conjecture D, p. 45] ) There are infinitely many Germain prime pairs. If $\pi_{\mathcal{G}}(x)$ is the number of pairs less than $x$ , then $\pi_{\mathcal{G}}(x)=2C_{2}\int_{2}^{x}\frac{1}{\log(t)\log(2t+1)}dt+O\left(\frac{x}{(\log x)^{3}}\right),$ where $C_{2}>0$ is a constant defined by (1.1) $C_{2}=\prod_{p\geq 3}\left(1-\frac{1}{(p-1)^{2}}\right)=0.6601618605898407646766938915352060\ldots.$ More generally, Conjecture D handles linearly dependent prime pairs $ap+bq=c$ , where $a,b,c\in\mathbb{Z}^{\times}$ are constants. Some numerical data to back the Germain primes conjecture are available in the literature, see [ 3 , Section 3.5] , and [ 17 , p. 4] . [...]
  § 2. Foundational Results: The expressions $(m,n)=\text{gcd}(m,n)$ and $[m,n]=\text{lcm}(m,n)$ denote the greatest common divisor and the lowest common multiple respectively. The totient function is defined by (2.1) $\varphi(n)=n\prod_{p\mid n}\left(1-\frac{1}{p}\right),$ and the Mobius function is defined by (2.2) $\mu(n)=\begin{cases}(-1)^{w}&\text{ if }n=p_{1}p_{2}\cdots p_{w},\\ 0&\text{ if }n\neq p_{1}p_{2}\cdots p_{w}.\end{cases}$ The nonnegativity of the finite sum (2.3) $\sum_{m,n\leq x}\frac{\mu(m)\mu(n)}{[m,n]}>0$ and the convergence of the associated series as $x\to\infty$ is the subject a study in [ 6 ] , and in sieve theory. Similar techniques are used here to derive several estimates and verify the nonnegativity of some related finite sums. These finite sums arise in the analysis of the main term and error term of Theorem 6.1 .
  § 4. Lower Bound For The Main Term: Lemma 4.1 . If $x\geq 1$ is a large number, and $x_{1}=(\log x)^{c_{0}}\leq e^{c_{1}\sqrt{\log x}}$ , where $c_{0}>0$ and $c_{1}=c_{1}(c_{0})>0$ are constants, then, $\displaystyle M(x)$ $\displaystyle=$ $\displaystyle\sum_{\begin{subarray}{c}1\leq d_{1}\leq x_{1}\\ 1\leq d_{2}\leq x_{1}\end{subarray}}\mu(d_{1})\log(d_{1})\mu(d_{2})\log(d_{2})\sum_{\begin{subarray}{c}n\leq x\\ d_{1}\mid 2n+1,\;d_{2}\mid 2n+1\end{subarray}}\Lambda(n+1)$ $\displaystyle\gg$ $\displaystyle\frac{x\log\log x}{\log\log\log x}.$ Proof . Let $x$ be a large number, let $d_{1}d_{2}\leq x_{1}^{2}=(\log x)^{2c_{0}}\leq e^{c_{1}\sqrt{\log x}}$ , and let $q=[d_{1},d_{2}]$ . [...]
  § 6. Fundamental Results: The classical weighted Germain primes counting function has the form (6.1) $\sum_{1\leq n\leq x}\Lambda(n)\Lambda(2n+1).$ The derivation of a lower bound for the number of Germain primes up to a large number $x\geq 1$ is based on a new weighted Germain primes counting function (6.2) $\sum_{n\leq x}w(n)\Lambda(n)\Lambda(2n+1).$ The extra weight factor $w(n)=\Lambda(2n+1)$ provides effective control over the error term at the cost of a smaller main term, by a factor of approximately $\log x$ . Theorem 6.1 . If $x\geq 1$ is a large real number, then $\sum_{1\leq n\leq x}w(n)\Lambda(n)\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x}.$ Proof . Substitute the identity $\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d$ , see [ 1 , Theorem 2.11] , then reverse the order of summations. [...]
[7] arXiv:1809.02821v3 | Primes In Fractional Sequences
  The results for the fractional sequence $\left \{[x/n]+1:n \leq x\right \}$, and the fractional sequence in arithmetic progression $\left \{q[x/n]+a:n \leq x\right \}$, where $a&lt;q$ are integers such that $\gcd(a,q)=1$, prove that these sequences of fractional numbers contain the set of primes, and the set primes in arithmetic progressions as $x \to \infty$ respectively. Furthermore, the corresp
  Full text (https://arxiv.org/html/1809.02821v3), excerpts of its own sections:
  § 1 Introduction: Let $x\geq 1$ be a large number, and let $[x]=x-\left\{x\right\}$ denotes the largest integer function. Sequences of fractional numbers are of the forms $\left\{\left[s_{\beta}(n)\right]:n\geq 1\right\}\subset\mathbb{N},$ (1) where $s_{\beta}:\mathbb{R}\longrightarrow\mathbb{R}$ is a real-valued function. Some well known sequences of primes in fractional sequences are 1. The sequence Beatty primes $\left\{p=\left[\alpha n\right]:n\geq 1\right\}\subset\mathbb{P},$ (2) where $\alpha\in\mathbb{R}$ is an irrational number. The corresponding counting function is $\pi_{1}(x)=\#\left\{p=\left[\alpha n\right]:p\leq x\right\}=\delta(\alpha)\frac{x}{\log x}+O\left(\frac{x}{\log^{2}x}\right),$ (3) where $\delta(\alpha)=1/\alpha>0$ is the density, see [ 5 ] , [ 27 ] , [ 16 ] . 2. The sequence Piatetski-Shapiro primes $\left\{p=\left[n^{\beta}\right]:n\geq 1\right\}\subset\mathbb{P},$ (4) where $\beta\in[1,12/11]$ is a real number. [...]
  § 2 Algebraic Foundation: Elementary algebraic concepts used in the proofs of the main results are considered in this section. The discrete image or discrete spectrum of a polynomial $f(x)\in\mathbb{Z}[x]$ over the integers is the subset of integers $f(\mathbb{Z})=\left\{f(n):n\in\mathbb{Z}\right\}$ . Definition 2.1 . The fixed divisor $\tdiv(f)=\gcd(f(\mathbb{Z}))$ of a polynomial $f(x)$ is the greatest common divisor of its image. The fixed divisor $\tdiv(f)=1$ if the congruence equation $f(x)\equiv 0\bmod p$ has $w(p) [ 9 , p. 395] . For polynomials of small degrees $\deg f$ , there is a fast method for computing the fixed divisor by means of a truncated image, and the greatest common divisor. Specifically, $\tdiv(f)=\gcd\left(\left\{f(n):0\leq n\leq\deg(f)\right\}\right).$ (24) The fixed divisors can also be computed from the coefficients of the polynomials. This procedure requires a change of basis from the power basis to the factorial basis. Lemma 2.1 . [...]
  § 3 Analytic Foundation: Elementary analytic concepts used in the proofs of the main results are considered in this section. The vonMangoldt function is defined by the weighted prime powers indicator function $\Lambda(n)=\begin{cases}\log p&\text{if }n=p^{m},\\ 0&\text{if }n\neq p^{m}.\\ \end{cases}$ (26) The symbol $p^{m}\geq 2$ , with $m\in\mathbb{N}$ , denotes a prime power. Theorem 3.1 . ( [ 10 , Theorem 2.6] ) Let $f$ be a complex-valued arithmetic function and assume that there exists $0 $\sum_{n\leq x}\left|f(n)\right|^{2}\ll x^{\alpha}. [...]
  § 12 Germain Primes In Fractional Sequences: The sequence of primes pairs $\left\{p,2p+1:\text{ prime }p\leq x\right\}\subset\mathbb{P}$ is well known as the Sophie Germain primes. It has an extensive literature consisting of partial results, conjectural and numerical data. Detailed discussions of the Germain primes appear in [ 17 , p. 48] , [ 25 , p. 405] , [ 9 , p. 395] , [ 23 , p. 342] , [ 24 , p. 33] , et alii. Conjecture 12.1 . (Germain prime conjecture) Let $x\geq 1$ be a large number. Let $\Lambda$ be the vonMangoldt function. Then $\sum_{n\leq x}\Lambda\left(n\right)\Lambda\left(2n+1\right)=s_{1}x+O\left(\frac{x}{\log x}\right),$ (85) where the density constant $s_{1}=\prod_{p\geq 3}\left(\frac{p(p-1)}{(p-1)^{2}}\right)=0.6601618158468\ldots.$ (86) The circle methods heuristics are introduced in [ 17 , p. 46] , [ 22 ] , et cetera. However, there is no literature on the fractional sequence of integers pairs $\left\{[x/p],2[x/p]+1:\text{ prime }p\leq x\right\}\subset\mathbb{N}$ . A few results for twin primes in this fractional sequence are proved here. Theorem 12.1 . [...]
[8] arXiv:1212.3602v1 | A search for primes $p$ such that Euler number $E_{p-3}$ is divisible by $p$
  Let $p&gt;3$ be a prime. Euler numbers $E_{p-3}$ first appeared in H. S. Vandiver's work (1940) in connection with the first case of Fermat Last Theorem. Vandiver proved that $x^p+y^p=z^p$ has no solution for integers $x,y,z$ with $\gcd(xyz,p)=1$ if $E_{p-3}\equiv 0 (\bmod p)$. Numerous combinatorial congruences recently obtained by Z.-W. Sun and by Z.-H. Sun involve the Euler numbers $E_{p-3}$. T
  Full text (https://arxiv.org/html/1212.3602v1), excerpts of its own sections:
  § 1 Introduction: Euler numbers $E_{n}$ $(n=0,1,2,\ldots)$ (e.g., see [ 13 , pp. 202–203] ) are integers defined recursively by $E_{0}=1,\quad\mathrm{and}\quad\sum_{0\leq k\leq n\atop k\,\,even}{n\choose k}E_{n-k}\quad\mathrm{for}\quad n=1,2,3,\ldots$ (it is well known that $E_{2n-1}=0$ for each $n=1,2,\ldots$ ). The first few Euler numbers are $E_{0}=1,E_{2}=-1,E_{4}=5,E_{6}=-61,E_{8}=1385,E_{10}=-50521,E_{12}=2702765,E_{14}=-199360981,E_{16}=19391512145$ . It is well known that Euler numbers can also be defined by the generating function $\frac{2}{e^{x}+e^{-x}}=\sum_{n=0}^{\infty}E_{n}\frac{x^{n}}{n!}.$ It is well known that $E_{n}=E_{n}(0)$ ( $n=0,1,\ldots$ ), where $E_{n}(x)$ is the classical Euler polynomial (see e.g., [ 15 , p. 61 et seq. ] ). Recall that Bernoulli numbers $B_{n}$ $(n=0,1,2,\ldots)$ are rational numbers defined by the formal identity $\frac{x}{e^{x}-1}=\sum_{n=0}^{\infty}B_{n}\frac{x^{n}}{n!}. [...]
  § 2 A congruence used in our computation: Here, as usually in the sequel, for integers $m,n,rs$ with $n\not=0$ and $s\not=0$ , and a prime power $p^{a}$ we put $m/n\equiv r/s\,(\bmod{\,\,p^{e}})$ if and only if $ms\equiv nr\,(\bmod{\,\,p^{e}})$ , and the residue class of $m/n$ is the residue class of $mn^{\prime}$ where $n^{\prime}$ is the inverse of $n$ modulo $p^{e}$ . In what follows $p$ always denotes a prime. The Fermat Little Theorem states that if $p$ is a prime and $a$ is an integer not divisible by $p$ , then $a^{p-1}\equiv 1\,(\bmod{\,\,p})$ . This gives rise to the definition of the Fermat quotient of $p$ to base $a$ , $q_{p}(a):=\frac{a^{p-1}-1}{p},$ which is an integer. It is well known that divisibility of Fermat quotient $q_{p}(a)$ by $p$ has numerous applications which include the Fermat Last Theorem and squarefreeness testing (see [ 5 ] , [ 7 ] and [ 13 ] ). If $q_{p}(2)$ is divisible by $p$ , $p$ is said to be Wieferich prime . Despite several intensive searches, only two Wieferich primes are known: $p=1093$ and $p=3511$ (see [ 2 ] and [ 3 ] ). [...]
  § 3 The computation: Using the congruence (2), a computation via Mathematica 8 shows that only three primes less than $10^{7}$ satisfy the condition $E_{p-3}\equiv 0\,(\bmod\,p)$ (such primes are 149, 241 and 2946901, and they are given as a sequence A198245 in [ 14 ] ). Notice also that in 2011 [ 12 , p. 3, Remarks] , the author of this article reported that these three primes are only primes less than $3\times 10^{6}$ . Recall that investigations of such primes have been recently suggested by Z.-W. Sun in [ 20 ] ; namely, in [ 20 , Remark 1.1] Sun found the first and the second such primes, 149 and 241, and used them to discover curious supercongruences (1.2)–(1.5) from Theorem 1.1 in [ 20 ] involving $E_{p-3}$ . Motivated by search for Wieferich and Fibonacci-Wieferich primes given in [ 2 ] and [ 3 ] and search for Wolstenholme primes given in [ 11 ] , here we use similar computational considerations for Euler numbers $E_{p-3}$ where $p$ is a prime. [...]
[9] QNFO: Functorial Characterization of the Prime Numbers | https://papers.qnfo.org/papers/functorial-characterization-of-the-prime-numbers
  This paper presents a complete theoretical characterization of the set of prime numbers, \(\mathcal{P}\), by demonstrating that it is the geometric support of a canonical object constructed via a three-stage functorial lift. This process begins in the logical stratum of Homotopy Type Theory (HoTT), where a decidable Prime type is constructed. This logical object is then mapped via an interpretatio
  Full text (https://papers.qnfo.org/papers/functorial-characterization-of-the-prime-numbers), excerpts of its own sections:
  § Functorial Characterization of the Prime Numbers: *A Functorial Characterization of the Prime Numbers via a HoTT-Realizability-Sheaf Correspondence*
  § 1.0 The Representational Problem of Primality: The study of prime numbers is defined by a central paradox: their definition is elementary, local, and combinatorial—a natural number greater than one is prime if it is divisible only by one and itself—yet their global behavior is governed by deep laws intertwined with continuous, analytic objects such as the Riemann zeta function. This dichotomy has led to a representational crisis in number theory. A synthetic approach that attempts to unify these aspects by combining constraints from different mathematical domains—for instance, by constructing a ‘synthetic prime sheaf’ as the fiber product of sheaves encoding modular, analytic, and geometric properties—is fundamentally inadequate. Such an approach imposes a geometric structure externally rather than deriving it from the definition of primality itself. Consequently, synthetic methods are structurally incapable of providing a complete characterization, suffering from irreparable flaws such as the inability of norm-based constructions to distinguish primes from prime powers without appealing to external oracles (Hartshorne, 1977). [...]
  § 2.0 The Solution Strategy: A Functorial Bridge from Logic to Geometry: This framework resolves the aforementioned paradox by constructing a formal, structure-preserving bridge from a foundational logical definition of primality to its ultimate geometric manifestation. The solution is a composed functor, the ‘Prime Realization Functor’ \(G = \gamma_* \circ I\), which acts as a realization engine, translating an object in the category of formal types into an object in the category of sheaves on an arithmetic scheme. This process unfolds across three distinct categorical strata—Logical, Computational, and Geometric—ensuring that the final geometric object is not an arbitrary construction but the canonical image of the initial logical definition. The first stage, in the Logical Stratum, defines primality as a decidable type within Homotopy Type Theory (HoTT), providing a foundational, computationally-aware definition. [...]
  § 3.0 Stage 1: The Logical Stratum—A Decidable Prime Type in HoTT: The necessary starting point for a foundational framework is a formal system where logical definitions are intrinsically linked to computational content. Homotopy Type Theory (HoTT) is uniquely suited for this role, as its “proofs-as-programs” paradigm and its internal logic allow for the definition of mathematical objects and the verification of their properties (e.g., proving a type is a set) within a single, coherent language (Univalent Foundations Program, 2013). Within this system, the Prime type is formally constructed as a dependent sum over the natural numbers, \(\sum_{n:\mathbb{N}} \| \mathsf{isPrime}(n) \|_{-1}\), which is then proven to be a 0-type (a set), ensuring it faithfully represents the prime numbers as a discrete collection. [...]
  § 7.0 The Main Theorem of Prime Characterization: The entire framework culminates in a single, precise theorem that formally connects the foundational definition of primes to their geometric realization. **Theorem:** Assuming the Baillie–PSW conjecture, the direct image of the prime modest set \(\underline{\mathcal{P}}\) under the canonical geometric morphism \(\gamma: \mathbf{RT}(\mathcal{K}_1) \to \mathrm{Sh}(\mathrm{Ét}(\mathrm{Spec}(\mathbb{Z})))\) is a constructible étale sheaf whose support is exactly the set of prime numbers.
[10] QNFO: Prime Numbers as Universal Optimization Primitives | https://papers.qnfo.org/papers/prime-numbers-as-universal-optimization-primitives
  The scholarly understanding of prime numbers is structured around four paradigms: quantum chaos, classical optimization, algorithmic information theory, and deterministic law. However, these paradigms are marked by unresolved tensions—dynamical, hierarchical, and methodological—that have hindered a unified theory. This work posits that the apparent complexity of primes is a representational artifa
  Full text (https://papers.qnfo.org/papers/prime-numbers-as-universal-optimization-primitives), excerpts of its own sections:
  § 1.0 Introduction: The study of prime numbers stands as one of the most profound and enduring challenges in mathematics, with implications spanning from pure number theory to applied cryptography and theoretical physics. The scholarly understanding of prime numbers is fragmented across several dominant paradigms, including quantum chaos, which explores the statistical properties of prime distributions in relation to energy levels of quantum systems; classical optimization, which treats primes as solutions to constraint-satisfaction problems; algorithmic information theory, which investigates the compressibility and information content of prime sequences; and deterministic law, which seeks closed-form expressions for prime generation and distribution. Despite significant advances within each paradigm, the field remains marked by unresolved tensions—dynamical (between random and deterministic behaviors), hierarchical (between local and global properties), and methodological (between theoretical depth and computational practicality)—that have persistently hindered the development of a unified theory. [...]
  § 1.1 Foundational Knowledge Synthesis: The mathematical foundations for the proposed framework span multiple disciplines, each providing essential perspectives and formal tools. These tools create a bridge between traditionally separate mathematical domains, allowing for a novel synthesis that reveals the fundamental nature of prime numbers.
  § 1.1.1 Category Theory as Abstraction Framework: Category theory serves as the foundational language for structural transformations between mathematical domains, providing the formal machinery of functors and natural transformations to establish rigorous correspondences (Awodey, 2010). Its power lies in focusing on the relationships between objects rather than their internal structure. Functors provide the mechanism for creating systematic, structure-preserving maps between different mathematical categories, ensuring that relational patterns in one domain (e.g., divisibility in the integers) are faithfully represented in another (e.g., inclusion maps between manifolds). The strength of this approach lies in its ability to maintain theoretical coherence across different representations, providing a unified framework for understanding structural similarities between apparently disparate domains (Awodey, 2010). In this work, category theory enables the precise definition of a mapping that translates number-theoretic problems into geometric ones.
  § 4.0 Conclusion: Through their geometric representation, prime numbers can be understood as universal optimization primitives whose fundamental property of indivisibility provides robust solutions to constraint-satisfaction problems across diverse physical and computational domains. The computationally verifiable categorical framework developed in this work provides a new paradigm for approaching number-theoretic problems with geometric and topological methods, bridging traditionally separate disciplines (Awodey, 2010; Hatcher, 2002). The framework opens new avenues for applying geometric techniques to fields like cryptography, where primality testing is a fundamental operation (Agrawal, Kayal, & Saxena, 2004). The resolution of the methodological tension between theoretical depth and computational practicality may serve as a model for addressing similar tensions in other areas of mathematics and theoretical computer science (Milnor, 1963; Agrawal, Kayal, & Saxena, 2004). [...]
[11] QNFO: Alpha Pi Project | https://papers.qnfo.org/papers/alpha-pi-project
  The Alpha Pi project begins with a practical engineering challenge: quantum states are exquisitely fragile, decohering rapidly due to environmental noise. This fragility stems not merely from technical limitations but from a deeper mathematical vulnerability: the continuous real‑number field that underlies standard quantum mechanics. The Bloch sphere—the canonical representation of a qubit’s state
  Full text (https://papers.qnfo.org/papers/alpha-pi-project), excerpts of its own sections:
  § Alpha Pi Project: *From Cardiac Rhythms to Cosmic Fractals*
  § 1. The Core Problem: Quantum Fragility in a Continuous World: The Alpha Pi project begins with a practical engineering challenge: **quantum states are exquisitely fragile**, decohering rapidly due to environmental noise. This fragility stems not merely from technical limitations but from a deeper **mathematical vulnerability**: the continuous real‑number field that underlies standard quantum mechanics. The Bloch sphere—the canonical representation of a qubit’s state—is a smooth, continuous manifold with no discrete boundaries, allowing infinitesimal thermal drifts to accumulate linearly into significant errors. Active quantum error correction (QEC) fights this drift but imposes unsustainable resource burdens: surface codes require physical‑to‑logical qubit ratios of ~1000:1, face thermodynamic walls (Landauer’s principle, Heisenberg back‑action), and hit a **signal‑processing ceiling** beyond which no classical filtering can eliminate fundamental quantum back‑action.
  § 2. The Biomedical Analogy: Borrowing from Cardiology: A century of cardiology provides a ready‑made toolkit. Willem Einthoven’s techniques for extracting weak cardiac signals from noise—**differential amplification, vector analysis, matched filtering, ensemble averaging, crosstalk mitigation, impulse‑response deconvolution, and closed‑loop feedback**—translate directly to quantum readout. These methods improve fidelity but reveal diminishing returns, confirming that the noise problem is intrinsic to the continuous framework, not merely technical. The biomedical analogy thus serves a dual purpose: offering practical improvements while highlighting the need for a more fundamental solution.
  § 3. The Ontological Pivot: Replacing the Continuum with a Discrete Hierarchy: Confronting the signal‑processing ceiling forces an **ontological pivot**. The real numbers are not unique; **Ostrowski’s theorem** establishes the democratic equality of all completions of the rationals, including the **p‑adic numbers**. Physics has privileged the real numbers due to an **anthropocentric bias** toward smooth motion. [...]
  § 7.6 Experimental Signatures: 1. Deviations from standard quantum mechanics at ultra‑low energies. 2. Anisotropies in the fine‑structure constant \(\alpha\). 3. Discrete‑spacetime effects in cosmic‑ray events. 4. Prime periodicity in particle mass ratios. 5. Modified dispersion relations at high energies. 6. Lorentz‑violation signatures. 7. Tests with few‑particle systems in ultracold traps.
  § 7.6 Experimental Signatures: The ultrametric framework makes several **testable predictions** that distinguish it from standard quantum mechanics and general relativity. **Deviations from standard quantum mechanics at ultra‑low energies** are expected because the discrete tree structure becomes relevant when energy scales approach the level spacing between tree vertices. These could manifest as **anomalies in few‑particle interference patterns** in ultracold atomic systems or **modified tunneling rates** in mesoscopic devices. **Anisotropies in the fine‑structure constant \(\alpha\)** could arise if the local tree structure is not perfectly isotropic; astrophysical observations of quasar absorption lines could reveal such variations. **Discrete‑spacetime effects in cosmic‑ray events** include anomalous shower development or unexpected thresholds in the energy spectrum of ultra‑high‑energy cosmic rays. [...]
[12] QNFO: EMERGENT NUMBER THEORY | https://papers.qnfo.org/papers/emergent-number-theory
  The relationship between discrete number theory and continuous mathematical structures has been a subject of deep investigation in modern mathematics, with several well-established connections. The scholarly landscape reveals a sophisticated understanding of how discrete structures emerge from continuous foundations, while also highlighting unresolved questions that form the basis for this work. P
  Full text (https://papers.qnfo.org/papers/emergent-number-theory), excerpts of its own sections:
  § 1.1 Summary of Key Prior Work: Pisot-Vijayaraghavan (PV) theory demonstrates how integer sequences emerge from continuous irrational flows through exponential rounding with quantifiable error bounds. Akiyama and Komornik (2021) rigorously established that Pisot numbers generate integer sequences via exponential rounding with mathematically precise error bounds. For the golden ratio φ (a Pisot number of degree 2 with minimal polynomial $x^2 - x - 1$), the Fibonacci sequence satisfies $|F_n - \phi^n/\sqrt{5}| < 1/2$ for all $n \geq 1$, with the error decaying exponentially as $n$ increases. This demonstrates that the Fibonacci sequence is not primitive but emerges as a rounded projection of a continuous Pisot flow with quantifiable error bounds [akiyama2021]. Riemann's explicit formula establishes primes as Fourier duals of zeta zeros, not merely statistical approximations. [...]
  § 3.2 Irreducibility Preservation Across Domains: The category-theoretic mapping preserves the key structural property of irreducibility through a bidirectional correspondence: **Theorem (Irreducibility Correspondence)**: 1. If $P(x)$ is irreducible over $\mathbb{Q}$, then $\zeta_P(s)$ has no Euler product factorization. 2. If $\zeta_P(s)$ is irreducible (cannot be written as a product of L-functions), then $P(x)$ is irreducible. 3. If $P(x) = P_1(x)P_2(x)$ with $\deg(P_1), \deg(P_2) \geq 1$, then $\zeta_P(s) = \zeta_{P_1}(s)\zeta_{P_2}(s)$. 4. If $\zeta_P(s) = \zeta_1(s)\zeta_2(s)$ with $\zeta_1, \zeta_2$ non-trivial L-functions, then $P(x)$ is reducible. **Proof of (1)**: Suppose $P(x)$ is irreducible over $\mathbb{Q}$ but $\zeta_P(s) = \zeta_{P_1}(s)\zeta_{P_2}(s)$ for some polynomials $P_1, P_2$. Then the Dirichlet series coefficients would satisfy a convolution relation, implying the recurrence sequence for $P(x)$ decomposes into sequences for $P_1$ and $P_2$, contradicting the irreducibility of $P(x)$. **Proof of (2)**: Suppose $\zeta_P(s)$ is irreducible but $P(x) = P_1(x)P_2(x)$ with $\deg(P_1), \deg(P_2) \geq 1$. [...]
  § 5.3 Cross-Domain Theorem Transfer: The structural isomorphism between Pisot recurrences and L-functions enables systematic transfer of theorems between isomorphic domains: - Translate results from Pisot theory to prime distribution, applying techniques developed for recurrence sequences to prime counting problems. - Apply techniques from spectral geometry to recurrence sequences, using the spectral properties of zeta zeros to analyze the behavior of integer sequences. - Create a formal dictionary between the two domains that maps theorems, definitions, and proof techniques, enabling automatic translation of results between discrete and continuous number theory. - Develop computational tools that implement this theorem transfer, allowing researchers to solve problems in one domain by leveraging solutions from the other. This cross-domain theorem transfer represents a powerful methodological advance, enabling researchers to leverage insights from one mathematical domain to solve problems in another, with applications in both theoretical mathematics and computational number theory.
  § 6.0 Conclusion and Future Directions: This section synthesizes key findings and outlines pathways for future exploration.
  § 6.1 Key Findings Summary: The framework demonstrates that natural numbers and primes are not primitive ontological entities but emerge asymptotically from more fundamental continuous structures: - Natural numbers emerge from continuous dynamics (Pisot flows, cut-and-project schemes) via exponential rounding or geometric projection, with [...]