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
- Extended derivations connecting the framework to an irreducibility correspondence for polynomial zeta functions, a modular-signature presentation, quadratic value sets, an Euler-number computational presentation, an optimization reading of indivisibility, and a discrete-foundations program (Section 4.8).

The result also bears on the theory of quadratic prime-generating polynomials and on primes in Beatty-type sequences, because those contexts supply concrete presentations that fall under the same categorical framework. Beyond number theory, the same relativity mechanism speaks to formal verification, where statements must transfer between encodings of a specification, and to any discrete-versus-continuous foundational question of the kind raised by the ultrametric program of [11].

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
holds, where $\alpha_{m}=\sum_{q\ge1}\bigl|\mu(q)/(q^{s-1}\varphi(q))\bigr|^{2}c_{q}(m)\ge0$ is delivered by the Wiener–Khintchine step and determines the density of the prime pairs $\{p,p+m\}$ in the set of primes. This supplies a spectral presentation (P2-variant) in which prime-pair density is encoded in a constant attached to the encoding function $f(\cdot,s)$; the constant is precisely the kind of presentation-level quantity our test T3 of Section 4.5 flags as non-transferable. The same work [1] proves, in its Theorem 1.1, a lower bound for the quadratic correlation $\sum_{n^{2}+1\le x}\Lambda(n^{2}+1)\Lambda(n^{2}+3)$, obtained by exploiting the duality of the Ramanujan-series and Taylor-series domains; this is an example of a presentation built from congruence data (a refinement of P1) whose structural theorem — quadratic twin-prime infinitude — is far stronger than what the standard sieve delivers, illustrating that the strength of a theorem can depend on the encoding as much as on the mathematics.

Lemma 6.2 of [2] establishes the same correlation formula and shows in addition, via its Theorem 7.1 as invoked in its proof of Theorem 1.1, that $\alpha_{k}>1/2$ for all $k$ when $\Re(s)>1$, which [2] combines with the Taylor-domain formula to obtain lower bounds for the de Polignac pair counts $\sum_{n\le x}\Lambda(n)\Lambda(n+2k)$. The agreement of the asymptotic shape across [1] and [2] while the constants carry encoding-dependent meaning motivates the distinction between invariant statements and presentation-bound constants that Section 4 formalizes.

The modular-signature construction of [3] associates a unique numerical sequence to each positive integer, built from its residues under the primes, distinguishes core seed primes from non-core seed primes, groups the signatures within primorials, and uses elementary sieve properties and combinatorial principles to prove the twin-prime conjecture. In the vocabulary of Section 3 this is a candidate presentation whose encoding is a refinement of P1; Section 4.8 reads it through the framework.

The quadratic-prime presentation of [4] concerns the subset $\{p=an^{2}+bn+c:n\ge1\}$ generated by an irreducible polynomial over the integers, which [4] describes as widely believed to be an unbounded subset of the primes, and provides the details of a possible proof for some of these polynomials, in particular for the simplest subset $\{p=n^{2}+1\}$. The value set is a distinguished substructure whose relation to $\mathcal P$ is not a bijection onto a density-one subset; Section 4.8 shows that this excludes it from $\mathbf{RepPrimes}$ under Definition 3.1 and predicts an encoding-dependent density factor for any asymptotic attached to it.

Theorem 6.1 of [6] proves that for large $x$
$$
\sum_{1\le n\le x}w(n)\,\Lambda(n)\,\Lambda(2n+1)\gg\frac{x\log\log x}{\log\log\log x},
$$
with $w(n)=\Lambda(2n+1)$, and records that the extra weight factor provides effective control over the error term at the cost of a smaller main term, by a factor of approximately $\log x$. The same work records the twin-prime constant $C_2=\prod_{p\ge3}\bigl(1-1/(p-1)^{2}\bigr)=0.6601618605898407646766938915352060\ldots$ in its Conjecture 1.1. This weighted Germain-prime bound is the source of the quantitative illustration in Section 4.7; because the implicit $\gg$-constant is ineffective, the number we attach to it is labeled a projection.

The Beatty-prime presentation is treated in [7], which gives the counting function $\pi_{1}(x)=\delta(\alpha)\,x/\log x+O\bigl(x/\log^{2}x\bigr)$ with density $\delta(\alpha)=1/\alpha>0$ for the Beatty primes $\{p=\lfloor\alpha n\rfloor\}$, and which further records, in its Conjecture 12.1, the circle-method heuristic $\sum_{n\le x}\Lambda(n)\Lambda(2n+1)=s_{1}x+O(x/\log x)$ with density constant $s_{1}=0.6601618158468\ldots$. The density factor $1/\alpha$ is the model case for the density-$\delta$ presentations excluded by Definition 3.1, discussed in Section 6.

The computational presentation (P5) is instantiated by [8], which uses a congruence for Euler numbers and a Mathematica 8 computation to show that only three primes below $10^{7}$ satisfy $E_{p-3}\equiv0\pmod p$, namely $149$, $241$, and $2\,946\,901$; the same work recalls that only two Wieferich primes, $p=1093$ and $p=3511$, are known despite intensive searches. The structural theorem here is an exhaustive search result; the three identified primes are data bound to the encoding of Euler numbers and do not transfer as such, as Section 4.8 quantifies.

The functorial characterization of the primes in homotopy type theory [9] constructs a decidable Prime type as a dependent sum $\sum_{n:\mathbb{N}}\|\mathsf{isPrime}(n)\|_{-1}$ proven to be a $0$-type, and maps it via the composed functor $G=\gamma_{*}\circ I$ through logical, computational, and geometric strata to an étale sheaf whose support — assuming the Baillie–PSW conjecture — is exactly the set of primes. It is the existing formalization closest in spirit to $\mathbf{RepPrimes}$: a geometric morphism of toposes plays the role of our presentation morphism, and the sheaf support plays the role of the encoding $\phi$.

The optimization reading of [10] treats the primes through four paradigms — quantum chaos, classical optimization, algorithmic information theory, and deterministic law — and argues that the apparent complexity of primes is a representational artifact; its Section 1.1.1 identifies category theory as the abstraction framework in which functors provide "the mechanism for creating systematic, structure-preserving maps between different mathematical categories," and its conclusion states that through geometric representation the primes can be understood as universal optimization primitives whose fundamental property of indivisibility provides solutions to constraint-satisfaction problems. Section 4.8 connects that indivisibility property to our level-relative atomicity.

The ultrametric program of [11] begins from the observation that the continuous real-number field underlying standard quantum mechanics is a source of fragility, develops a discrete tree structure in its place via an ontological pivot motivated by Ostrowski's theorem on the equality of completions of the rationals, and lists among the testable signatures in its Section 7.6 "prime periodicity in particle mass ratios." Whatever the fate of that physical prediction, its methodological direction — discrete structure primary, continuous structure emergent — aligns with the atomicity schema of Section 3.4.

Finally, the framework of [12] proves a two-way Irreducibility Correspondence between irreducibility of a polynomial $P(x)$ over $\mathbb{Q}$ and non-factorizability of its associated zeta function $\zeta_P(s)$ into non-trivial $L$-functions, and proposes in its Section 5.3 a formal dictionary enabling cross-domain theorem transfer between Pisot-recurrence domains and prime-distribution domains. Section 4.8 reads both as transfer mechanisms of the kind our morphisms formalize.

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

**Examples.** At level $\mathbb N$ with ordinary multiplication, the atoms are the primes $\mathcal P$. At level $\mathbb Z_p$ (the $p$-adic integers) with its valuation, the atom is the uniformizer $p$ — a single element, atomic relative to a factorization theory in which every other nonzero element is a unit times a power of it. At the level of the absolute Galois group $G_{\mathbb Q}$ with conjugacy-class factorization of Frobenius data, the atoms are conjugacy classes attached to primes. The same integer $p$ is atomic at the first level, a unit-times-uniformizer decomposition at the second, and a conjugacy-class label at the third.

**Atomicity Relativity Conjecture.** For any two levels $L_1,L_2$ joined by a morphism of $\mathbf{RepPrimes}$ that preserves the invariants of Section 4 (Euler product, Möbius inversion, leading asymptotic), the induced map on atoms is a bijection up to density zero, so that atomicity shifts with level exactly when the invariant class is preserved.

This conjecture is stated, not proved; Section 4.6 verifies its first instances and Section 6 records what would falsify it.

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

**Proposition 4.5 (Non-invariance of $E(x)$).** The error term $E(x)=\pi(x)-\operatorname{Li}(x)$ is not an invariant of $\mathbf{RepPrimes}$. In the sieve presentation the natural comparison function carries a main term inflated by the factor $2e^{-\gamma}$ relative to $x/\log x$-type main terms,