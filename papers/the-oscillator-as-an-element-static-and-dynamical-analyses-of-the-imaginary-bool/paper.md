# The Oscillator as an Element: Static and Dynamical Analyses of the Imaginary Boolean Value in the Algebra of Eventually Periodic Truth Sequences

## Abstract

Revision-theoretic treatments of the liar paradox produce an oscillator $\iota = \langle U,P,U,P,\ldots\rangle$ that alternates between two states forever, but they leave $\iota$ a process rather than a value. This paper tests the conjecture that $\iota$ can be promoted to a static element of a genuine Boolean algebra of eventually periodic truth sequences. We define the algebra $\mathcal{B}_{\mathrm{EP}}$ of eventually periodic binary sequences under pointwise negation, conjunction, and disjunction, and prove it is a Boolean algebra. The central identity fails: $\iota \neq \neg\iota$ in $\mathcal{B}_{\mathrm{EP}}$, since the two sequences differ at coordinate $0$. We prove a collapse theorem: any Boolean congruence identifying $\iota$ with $\neg\iota$ is the universal congruence, because in a Boolean algebra $x = \neg x$ forces $x = 0 = 1$; no nontrivial Boolean algebra therefore contains a self-negating element. The algebra $\mathcal{B}_{\mathrm{EP}}$ is countably infinite ($|\mathcal{B}_{\mathrm{EP}}| = \aleph_0$) and provably non-isomorphic both to the two-element classical algebra and non-embeddable into Kleene's strong three-valued algebra. What survives is an exact dynamical characterization: $\iota$ is one of exactly $2$ shift-exact period-$2$ sequences, satisfies $\sigma(\iota) = \neg\iota$ for the shift $\sigma$, and its depth-$d$ unfolding truncations converge pointwise, pinning $\iota$ to a cylinder of uniform product measure $2^{-d}$ (for $d = 10$, $9.765625 \times 10^{-4}$). The oscillator is thus a computably approximable element of a Boolean algebra whose self-negation holds dynamically, not algebraically — a discrimination that turns the promotion conjecture into a precise, partially refuted, partially confirmed theorem.

## 1. Introduction

The liar paradox is not merely a curiosity for philosophers of logic; it is a live engineering obstacle wherever a formal system must evaluate a sentence that refers to its own truth. Any truth-evaluation engine — a theorem prover with a reflective truth predicate, a database of self-referential definitions, an implementation of a distinction-based calculus — that admits the sentence $L$ with $L \leftrightarrow \neg L$ either halts with no value, diverges in an evaluation loop, or must be walled off by a syntactic hierarchy (Tarskian levels) that forbids the very reflexivity the application wants. The revision-theoretic response is to let the evaluation run: $L$ is revised to $\neg L$, then to $\neg\neg L$, and so on, producing the oscillator $\iota = \langle U,P,U,P,\ldots\rangle$ that alternates between unmarked and marked, false and true, forever. The cost of this response is ontological: the oscillator is a process, not a value, and a system that can only assign values cannot use it. What would change if the results of this paper hold: a practitioner could treat the liar oscillator as a well-defined, finitely approximable object inside an ordinary Boolean algebra, with a theorem saying exactly in what sense it is and is not a self-negating truth value — turning a metaphysical dispute ("is the oscillator a third value?") into a checkable algebraic statement, and telling implementers precisely what their evaluator converges to and at what rate.

The conjecture under test has three parts: (1) the eventually periodic binary sequences form a Boolean algebra under pointwise operations; (2) in that algebra the distinguished element $\iota$ satisfies $\iota = \neg\iota$ as an algebraic identity, and the resulting structure is not isomorphic to classical two-valued or three-valued $(T,F,N)$ logic; (3) finite-depth unfoldings of the rewriting dynamics converge to $\iota$'s equivalence class, so the value is well-defined and computationally approximable. The conjecture is attractive because it promises the static, compositional clarity of a Boolean algebra together with the dynamic, paradox-tolerant behavior of revision semantics. The central tension is that if $\iota$ is only a sequence it adds nothing beyond period-$2$ revision theory, while if it is a value it must live in a static domain whose operations compose coherently.

This paper resolves the tension by proving both halves of it, with opposite verdicts. The algebra exists and is Boolean (Theorem 3.2). But the identity $\iota = \neg\iota$ is false in it (Proposition 4.3), and it cannot be repaired by quotienting: any Boolean congruence that identifies $\iota$ with $\neg\iota$ collapses the entire algebra (Theorem 4.5), a consequence of the elementary fact that a self-negating element of a Boolean algebra forces $0 = 1$. The non-isomorphism claims survive and strengthen: $\mathcal{B}_{\mathrm{EP}}$ is not isomorphic to classical logic (it is infinite), and no structure-preserving map embeds the three-valued algebra $K$ defined in Section 5 into it (Section 5, R3), because excluded middle holds pointwise in $\mathcal{B}_{\mathrm{EP}}$ and fails at the value $N$ of $K$. The dynamical half of the conjecture is confirmed with a quantitative rate: reading the depth profile of the liar's finite unfoldings as a sequence, one more unfolding acts as the shift $\sigma$, the profile is exactly $\iota$, and the depth-$d$ truncation determines $\iota$ on its first $d$ coordinates, confining it to a cylinder set of uniform product measure $2^{-d}$.

Our contributions are:

1. Definition of the algebra $\mathcal{B}_{\mathrm{EP}}$ of eventually periodic binary sequences and proof that it forms a Boolean algebra (Sections 3 and 4.1).
2. Refutation of the static self-negation claim: $\iota \neq \neg\iota$ in $\mathcal{B}_{\mathrm{EP}}$, plus a collapse theorem showing that no quotient of any nontrivial Boolean algebra can contain a self-negating element (Section 4.2).
3. Cardinality and separation results: $|\mathcal{B}_{\mathrm{EP}}| = \aleph_0$, non-isomorphism to the two-element classical algebra, and non-embeddability of Kleene's strong three-valued algebra (Section 4.3).
4. An exact dynamical characterization of $\iota$: $\sigma(\iota) = \neg\iota$, exactly $2$ shift-exact period-$2$ sequences, and depth-$d$ truncations confining $\iota$ to a cylinder of measure $2^{-d}$, computed explicitly for $d = 10$ (Section 4.4).

## 2. Background and Related Work

The present construction builds on several strands of algebraic and logical research.

[1] establishes duality theorems for left-handed skew Boolean algebras, demonstrating that Boolean-like structures can be generalized beyond classical algebras while preserving categorical equivalences. This motivates our search for a non-classical Boolean algebra based on sequence objects, and it cautions us: dualities that preserve Boolean behavior will not tolerate a self-negating element, which is exactly what our collapse theorem confirms.

[2] extends the eliminant construction for commuting elements in the $q$-deformed Heisenberg algebra, providing a method for generating algebraic identities in non-commutative settings. We adapt the constructive strategy of generating identities from explicit presentations when we define pointwise operations on sequences and check which identities they satisfy.

[3] proves that coefficient algebras of Lie algebra representations can be characterized explicitly, illustrating how algebraic objects derived from representations retain tractable structure. Our sequence algebra can be viewed as a coefficient algebra of the shift representation on binary strings, and the explicit characterization style of [3] is reflected in our explicit coordinate-level proofs.

[4] shows that the forgetful functor from Hopf algebras to algebras possesses a right adjoint, an instance of a categorical construction endowing an algebraic structure with a universal property. The present paper uses no adjunction; the properties of the distinguished element $\iota$ are derived in Section 4 from the ambient operations of $\mathcal{B}_{\mathrm{EP}}$ alone.

[5] introduces quantum Boolean algebras as analogues of Weyl algebras for Boolean affine spaces, highlighting that Boolean operations admit non-classical extensions. Our work parallels this program by extending Boolean operations to the space of eventually periodic sequences, while our collapse theorem marks a boundary that quantum Boolean algebras do not by themselves address.

[6] develops deformation theory for algebras over the Landweber-Novikov algebra, showing how algebraic structures can be deformed while preserving core identities. The deformation perspective underlies our analysis of the stability of the dynamical identity $\sigma(\iota) = \neg\iota$ under finite-depth approximations: the identity is exact at every finite depth on the coordinates the truncation reaches.

[7] classifies connected Hopf algebras of dimension $p^{2}$, providing concrete examples of finite algebraic structures with non-trivial primitive elements. This illustrates that algebraic objects can possess distinguished elements with constrained self-relations; our Proposition 4.3 shows the analogous constraint in the Boolean setting is fatal to self-negation.

[8] studies deformations of dual Leibniz algebra morphisms, taking the morphisms between algebras, rather than only the algebras, as the deformable objects. Our verification of the Boolean laws takes an analogous object-level approach at small scale: each law for the pointwise operations on $\mathcal{B}_{\mathrm{EP}}$ is checked directly at the level of individual coordinates, without appeal to an ambient presentation.

Throughout this paper we assume a careful separation between the revision states $U$ and $P$, the static values $0$ and $1$, and the oscillator $\iota$; our results (Proposition 4.3 and Theorem 4.5) show that $\iota$ is a dynamical object that no static Boolean value can equal.

## 3. Methods

### 3.1. Eventually periodic binary sequences

A binary sequence $s = (s_{0}, s_{1}, s_{2}, \ldots)$ with $s_{k} \in \{0,1\}$ is *eventually periodic* if there exist integers $n \geq 0$ and $p \geq 1$ such that for all $k \geq n$,

$$
s_{k+p} = s_{k}.
$$

The pair $(n,p)$ is called a *preperiod–period* pair. The set of all eventually periodic binary sequences is denoted $\mathcal{B}_{\mathrm{EP}}$. Sequences are indexed: coordinate $0$ is part of the data, and two sequences are equal exactly when they agree at every coordinate.

### 3.2. Pointwise Boolean operations

For $s, t \in \mathcal{B}_{\mathrm{EP}}$ we define:

$$
(s \wedge t)_{k} = s_{k} \cdot t_{k}, \qquad
(s \vee t)_{k} = s_{k} + t_{k} - s_{k} \cdot t_{k}, \qquad
(\neg s)_{k} = 1 - s_{k},
$$

where multiplication and addition are taken in $\{0,1\}$ with ordinary arithmetic, so that each coordinate value remains in $\{0,1\}$. Because the pointwise operations preserve eventual periodicity — if $s$ has period $p_{s}$ from $n_{s}$ and $t$ has period $p_{t}$ from $n_{t}$, then $s \wedge t$, $s \vee t$, and $\neg s$ are periodic with period dividing $\mathrm{lcm}(p_{s}, p_{t})$ from $\max(n_{s}, n_{t})$ — the results remain in $\mathcal{B}_{\mathrm{EP}}$.

### 3.3. Distinguished element $\iota$ and the shift

Define the *oscillator* $\iota$ as the sequence with preperiod $n = 0$ and period $p = 2$ given by

$$
\iota_{k} =
\begin{cases}
0 & \text{if } k \text{ is even},\\
1 & \text{if } k \text{ is odd}.
\end{cases}
$$

Thus $\iota = \langle 0,1,0,1,\ldots\rangle$. The *shift* $\sigma$ is the operator on sequences defined by $(\sigma s)_{k} = s_{k+1}$. A period-$p$ sequence is *shift-exact* if it is fixed by $\sigma^{p}$ but not by $\sigma^{m}$ for any $0 < m < p$.

### 3.4. Depth-$d$ unfoldings and truncations

For each depth $d \geq 0$, the depth-$d$ unfolding of the liar sentence is the finite approximation obtained by expanding the self-reference $d$ times; its revision profile is a finite binary string of length $d$. We define the truncation $\tau_{d}(\iota) = (\iota_{0}, \ldots, \iota_{d-1})$, the first $d$ coordinates of $\iota$. The dynamical claim under test is that successive unfoldings act as the shift on the profile, so that the depth-$d$ profile equals $\tau_{d}(\iota)$.

### 3.5. Verification framework

We verify the Boolean axioms (commutativity, associativity, distributivity, identity elements, complements) by direct pointwise calculation: for each axiom we take arbitrary $s, t, u \in \mathcal{B}_{\mathrm{EP}}$ and use the fact that the corresponding law holds in $\{0,1\}$ at every coordinate. The negative results (Proposition 4.3, Theorem 4.5, Proposition 4.8) are proved by exhibiting a specific coordinate or a specific algebraic consequence, as shown in Section 4.

## 4. Analysis

### 4.1. Boolean algebra axioms

1. **Commutativity of $\wedge$ and $\vee$**: For any $k$, $s_{k} t_{k} = t_{k} s_{k}$ and $s_{k} + t_{k} = t_{k} + s_{k}$, hence $(s \wedge t)_{k} = (t \wedge s)_{k}$ and $(s \vee t)_{k} = (t \vee s)_{k}$.

2. **Associativity**: $(s \wedge (t \wedge u))_{k} = s_{k}(t_{k} u_{k}) = (s_{k} t_{k}) u_{k} = ((s \wedge t) \wedge u)_{k}$; similarly for $\vee$.

3. **Distributivity**: At coordinate $k$,
$$
(s \wedge (t \vee u))_{k} = s_{k}(t_{k} + u_{k} - t_{k} u_{k}) = s_{k} t_{k} + s_{k} u_{k} - s_{k} t_{k} u_{k} = ((s \wedge t) \vee (s \wedge u))_{k},
$$
where the last equality holds because $s_{k} \in \{0,1\}$ makes $s_{k} t_{k} + s_{k} u_{k} - s_{k} t_{k} u_{k}$ equal to the coordinatewise disjunction of $s_{k} t_{k}$ and $s_{k} u_{k}$ in all four cases $(s_{k}, t_{k}, u_{k}) \in \{0,1\}^{3}$.

4. **Identity elements**: Define $\mathbf{0} = (0,0,0,\ldots)$ and $\mathbf{1} = (1,1,1,\ldots)$. Then $(s \vee \mathbf{0})_{k} = s_{k} + 0 - s_{k} \cdot 0 = s_{k}$ and $(s \wedge \mathbf{1})_{k} = s_{k} \cdot 1 = s_{k}$.

5. **Complement**: $(s \vee \neg s)_{k} = s_{k} + (1 - s_{k}) - s_{k}(1 - s_{k}) = 1$ for both values of $s_{k}$, and $(s \wedge \neg s)_{k} = s_{k}(1 - s_{k}) = 0$ for both values of $s_{k}$.

Since each axiom holds at every coordinate $k$, we obtain:

**Theorem 3.2.** $(\mathcal{B}_{\mathrm{EP}}, \wedge, \vee, \neg, \mathbf{0}, \mathbf{1})$ is a Boolean algebra.

It is nontrivial: $\mathbf{0} \neq \mathbf{1}$ because they differ at coordinate $0$.

### 4.2. The self-negation claim fails, and cannot be repaired

**Proposition 4.3.** In $\mathcal{B}_{\mathrm{EP}}$, $\iota \neq \neg\iota$.

*Proof.* $(\neg\iota)_{0} = 1 - \iota_{0} = 1 - 0 = 1$, while $\iota_{0} = 0$. The sequences differ at coordinate $0$, hence $\iota \neq \neg\iota$. In fact they differ at every coordinate: $(\neg\iota)_{k} = 1 - \iota_{k} = \iota_{k+1}$ for all $k$, so $\neg\iota = \sigma(\iota) = \langle 1,0,1,0,\ldots\rangle$, which is a distinct element of $\mathcal{B}_{\mathrm{EP}}$. $\square$

The identity $\iota = \neg\iota$ therefore holds only *up to shift*, i.e., dynamically, not as an equality of elements. The following theorem shows this cannot be fixed by quotienting.

**Lemma 4.4.** In any Boolean algebra, if $x = \neg x$ then $x = 0$ and $x = 1$.

*Proof.* Using idempotence and the complement laws,
$$
x = x \wedge x = x \wedge \neg x = 0,
$$
and
$$
x = x \vee x = x \vee \neg x = 1.
$$
Hence $0 = 1$ and the algebra is the trivial one-element algebra. $\square$

**Theorem 4.5 (Collapse theorem).** Let $\equiv$ be a Boolean congruence on $\mathcal{B}_{\mathrm{EP}}$ (an equivalence relation compatible with $\wedge, \vee, \neg$) with $\iota \equiv \neg\iota$. Then $\equiv$ is the universal congruence.

*Proof.* From $\iota \equiv \neg\iota$ and compatibility with $\wedge$:
$$
\iota \wedge \neg\iota \equiv \iota \wedge \iota = \iota,
$$
and $\iota \wedge \neg\iota = \mathbf{0}$ by the complement law, so $\mathbf{0} \equiv \iota$. From compatibility with $\vee$:
$$
\iota \vee \neg\iota \equiv \iota \vee \iota = \iota,
$$
and $\iota \vee \neg\iota = \mathbf{1}$, so $\mathbf{1} \equiv \iota$. Hence $\mathbf{0} \equiv \mathbf{1}$. For any $y \in \mathcal{B}_{\mathrm{EP}}$, compatibility with $\wedge$ gives $y = y \wedge \mathbf{1} \equiv y \wedge \mathbf{0} = \mathbf{0}$, so every element is congruent to every other: $\equiv$ is universal. $\square$

Consequently no nontrivial Boolean algebra — and no nontrivial quotient of $\mathcal{B}_{\mathrm{EP}}$ — contains an element $x$ with $x = \neg x$. The liar oscillator cannot be a static self-negating value in any Boolean setting; this is a structural obstruction, not an artifact of the sequence representation.

### 4.3. Cardinality and separation from classical and three-valued algebras

**Proposition 4.6.** $|\mathcal{B}_{\mathrm{EP}}| = \aleph_{0}$.

*Proof.* Each eventually periodic sequence is determined by a finite tuple
$$
(n, p, a_{0}, \ldots, a_{n-1}, b_{0}, \ldots, b_{p-1}),
$$
with $n \geq 0$, $p \geq 1$, and $a_{i}, b_{j} \in \{0,1\}$; for fixed $(n,p)$ there are $2^{n+p}$ such tuples. Encoding each tuple as a single finite binary string gives an injection $\mathcal{B}_{\mathrm{EP}} \hookrightarrow \{0,1\}^{<\omega}$, the set of finite binary strings. That set is countable, being $\bigcup_{m=0}^{\infty} \{0,1\}^{m}$, a countable union of finite sets of size $2^{m}$. The algebra is infinite: for each $m \geq 0$ the sequence $s^{(m)}$ that is $1$ exactly at coordinate $m$ and $0$ elsewhere is eventually periodic (preperiod $m+1$, period $1$), and the $s^{(m)}$ are pairwise distinct. An infinite subset of a countable set is countably infinite, hence $|\mathcal{B}_{\mathrm{EP}}| = \aleph_{0}$. $\square$

### 4.4. Dynamical characterization of $\iota$

The static failure of self-negation leaves the dynamical identity intact. We now characterize it exactly.

**Proposition 4.7.** $\sigma(\iota) = \neg\iota$, and $\sigma^{2}(\iota) = \iota$.

*Proof.* At coordinate $k$, $(\sigma\iota)_{k} = \iota_{k+1}$. If $k$ is even then $k+1$ is odd and $\iota_{k+1} = 1 = 1 - \iota_{k} = (\neg\iota)_{k}$; if $k$ is odd then $k+1$ is even and $\iota_{k+1} = 0 = 1 - \iota_{k}$. Hence $\sigma(\iota) = \neg\iota$ at every coordinate. Applying $\sigma$ again, $\sigma^{2}(\iota)_{k} = \iota_{k+2} = \iota_{k}$ because $\iota$ has period $2$, so $\sigma^{2}(\iota) = \iota$. $\square$

**Proposition 4.8.** There are exactly $2$ shift-exact period-$2$ sequences in $\mathcal{B}_{\mathrm{EP}}$.

*Proof.* A period-$2$ sequence with $n = 0$ is determined by the pair $(b_{0}, b_{1}) \in \{0,1\}^{2}$, giving $2^{2} = 4$ candidates: $\langle 0,0,\ldots\rangle$, $\langle 1,1,\ldots\rangle$, $\iota = \langle 0,1,0,1,\ldots\rangle$, and $\langle 1,0,1,0,\ldots\rangle$. The first two are fixed by $\sigma$ itself, hence not shift-exact. The last two satisfy $\sigma^{2}(s) = s$ but $\sigma(s) \neq s$ (they differ at coordinate $0$), so each is shift-exact. There are therefore exactly $2$ shift-exact period-$2$ sequences, namely $\iota$ and $\sigma(\iota) = \neg\iota$. $\square$

**Proposition 4.9 (Cylinder confinement).** For each $d \geq 1$, the truncation $\tau_{d}(\iota)$ determines $\iota$ exactly on the cylinder set
$$
C_{d} = \{ s \in \{0,1\}^{\omega} : s_{k} = \iota_{k} \text{ for all } k < d \},
$$
and under the uniform product measure $\mu$ on $\{0,1\}^{\omega}$, $\mu(C_{d}) = 2^{-d}$.

*Proof.* The cylinder $C_{d}$ fixes $d$ coordinates, leaving the remaining coordinates free; each of the $2^{d}$ binary strings of length $d$ defines one cylinder of equal measure under the uniform product measure, and the cylinders partition $\{0,1\}^{\omega}$, so each has measure $2^{d}$-th of the total:
$$
\mu(C_{d}) = \frac{1}{2^{d}} = 2^{-d}.
$$
For $d = 10$: $2^{10} = 1024$, so
$$
\mu(C_{10}) = \frac{1}{1024} = 0.0009765625 = 9.765625 \times 10^{-4}.
$$
Thus each additional unfolding depth multiplies the uncertainty cylinder's measure by exactly $\tfrac{1}{2}$: the approximation converges pointwise (every coordinate of $\iota$ is pinned once $d$ exceeds its index) but never in total variation, since $\mu(C_{d}) \to 0$ yet no finite $d$ determines $\iota$ as an element of $\{0,1\}^{\omega}$. $\square$

The dynamical picture is therefore exact rather than approximate: one unfolding step is precisely the shift, the shift on $\iota$ is precisely pointwise negation, and the depth-$d$ profile is precisely $\tau_{d}(\iota)$. What revision theory produces is a computably approximable element of $\mathcal{B}_{\mathrm{EP}}$ whose self-negation is realized by the dynamics ($\sigma(\iota) = \neg\iota$) and refuted by the algebra ($\iota \neq \neg\iota$).

## 5. Results

Combining Sections 4.1–4.4, the conjecture resolves into four results with mixed verdicts.

**R1 (Confirmed).** $\mathcal{B}_{\mathrm{EP}}$ is a genuine Boolean algebra (Theorem 3.2), countably infinite (Proposition 4.6), with $\iota$ a well-defined element of it. The static half of the promotion program succeeds: the oscillator has an address in an ordinary Boolean algebra.

**R2 (Refuted).** $\iota \neq \neg\iota$ in $\mathcal{B}_{\mathrm{EP}}$ (Proposition 4.3): the sequences differ at coordinate $0$ (and at every coordinate). No quotient can repair this (Theorem 4.5): any Boolean congruence with $\iota \equiv \neg\iota$ forces $\mathbf{0} \equiv \mathbf{1}$ and is universal. The algebraic identity $\iota = \neg\iota$ is not merely unproven but impossible in any nontrivial Boolean algebra (Lemma 4.4).

**R3 (Confirmed, strengthened).** $\mathcal{B}_{\mathrm{EP}}$ is separated from the comparison structures: it is not isomorphic to the two-element classical algebra because it is infinite while the classical algebra has $2$ elements; and it admits no embedding of the three-valued algebra $K$, which we define here on the set $\{T, F, N\}$ by imposing $\neg T = F$, $\neg F = T$, $\neg N = N$, $N \vee N = N$, $N \wedge N = N$, and the usual two-element behavior when only $T$ and $F$ occur. In $K$, excluded middle fails at $N$: $N \vee \neg N = N \neq T$. Excluded middle holds at every coordinate of $\mathcal{B}_{\mathrm{EP}}$ ($(s \vee \neg s)_{k} = 1$ for all $k$, Section 4.1, item 5), so any homomorphism from $K$ into $\mathcal{B}_{\mathrm{EP}}$ preserving $\wedge, \vee, \neg$ would have to send $N$ to an element $x$ with $x \vee \neg x = \mathbf{1}$ and $x \wedge \neg x = \mathbf{0}$ simultaneously with $x \neq \mathbf{0}, \mathbf{1}$ — and Lemma 4.4 shows no Boolean algebra contains such an element. The oscillator is therefore not a third value in any sense that a Boolean target can represent.

**R4 (Confirmed, quantitative).** The dynamical identity is exact: $\sigma(\iota) = \neg\iota$ (Proposition 4.7), there are exactly $2$ shift-exact period-$2$ sequences (Proposition 4.8), and depth-$d$ truncations confine $\iota$ to a cylinder of measure $2^{-d}$, with the computed value $\mu(C_{10}) = 9.765625 \times 10^{-4}$ (Proposition 4.9). The convergence rate is exactly one bit of $\iota$ per unfolding step.

## 6. Discussion

The results split the original conjecture cleanly. Its algebraic half is half-right: the algebra exists, but the self-negation identity inside it is structurally impossible, and the impossibility is not a defect of the sequence representation but a consequence of the complement laws of any Boolean algebra. Its dynamical half is fully right, and stronger than conjectured: the unfolding dynamics is not merely convergent but isomorphic to the shift, so the "approximation" is an exact orbit.

**Limitations.** The negative and positive results rest on the following assumptions, with sensitivity noted for each.

1. **Pointwise operations.** The Boolean algebra structure is defined coordinatewise. A different operation (for example, one sensitive to phase or preperiod) could yield a non-Boolean algebra in which $\iota = \neg\iota$ holds; the collapse theorem would then not apply, but neither would the guarantee of coherent composition that motivated the Boolean requirement. The result is maximally sensitive to this choice: it is the entire content of Theorem 3.2.
2. **Coordinate indexing from $0$.** Proposition 4.3 turns on $\iota_{0} = 0$. Indexing from $1$ swaps the roles of $\iota$ and $\neg\iota$ but not the fact of inequality; the refutation is insensitive to this convention.
3. **Boolean congruences only.** Theorem 4.5 constrains quotient maps that preserve $\wedge, \vee, \neg$. A non-Boolean quotient (for instance, one collapsing to a De Morgan algebra or a Kleene algebra, where $x = \neg x$ is consistent) escapes the theorem — but then the target is no longer a Boolean algebra, which is what the promotion conjecture demanded.
4. **Uniform product measure.** The rate $2^{-d}$ is relative to the uniform measure on $\{0,1\}^{\omega}$. Under a biased product measure with coordinate bias $q \neq \tfrac{1}{2}$, the cylinder measure would be $q^{\lceil d/2 \rceil}(1-q)^{\lfloor d/2 \rfloor}$, still exponentially decaying but not $2^{-d}$; the qualitative conclusion (pointwise convergence, no total-variation convergence at any finite depth) is unchanged.
5. **Revision profile identification.** Section 3.4 assumes the depth-$d$ unfolding's revision profile equals $\tau_{d}(\iota)$. This is the standard period-$2$ revision behavior of the liar, but it is an identification of the revision dynamics with the sequence $\iota$, not a theorem proved here about an arbitrary revision semantics; a revision rule that dampens or permutes states would break the identification $\sigma = $ one unfolding step.

**What would falsify the main result.** The central negative claim — that no nontrivial Boolean algebra contains a self-negating element — would be falsified by a single explicit counterexample: a structure satisfying all Boolean axioms (commutativity, associativity, distributivity, identities, complements) with more than one element, containing an $x$ with $x = \neg x$. Lemma 4.4 derives $x = 0$ and $x = 1$ from the axioms alone, so such a structure would have to violate an axiom; exhibiting which axiom fails in any proposed "Boolean algebra of paradox values" is exactly the check our theorem forces. Correspondingly, the positive claim R4 would be falsified by a revision semantics for the liar whose depth profiles are not eventually periodic with period $2$, or whose successive profiles are not related by the single-coordinate shift.

**Open questions.** Three remain. First, which non-Boolean algebras do admit $\iota = \neg\iota$ coherently — De Morgan and Kleene algebras are the immediate candidates, and the collapse theorem says nothing about them. Second, whether the shift orbit $\{\iota, \neg\iota\}$ can be given a universal property in some category of dynamical systems on Boolean algebras, making "the oscillator" a defined object rather than a chosen one. Third, whether the cylinder-confinement rate $2^{-d}$ is optimal, i.e., whether any coarser observable than the coordinate truncation can pin $\iota$ faster.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are implementers of truth-evaluation engines that must confront self-referential sentences: builders of reflective theorem provers, of distinction-based calculi with re-entry, and of any evaluator that currently detects the liar loop and aborts. If R2 and R4 hold, the design decision changes from "wall off self-reference behind a Tarskian hierarchy" to "represent the liar's evaluation as the element $\iota \in \mathcal{B}_{\mathrm{EP}}$ and expose $\sigma(\iota) = \neg\iota$ as a transition rule": the evaluator returns a finite truncation $\tau_{d}(\iota)$ plus an explicit statement of its cylinder uncertainty $\mu(C_{d}) = 2^{-d}$, instead of diverging. What the result forbids is equally actionable: no implementation should attempt to store a single static value for the liar that equals its own negation inside a Boolean module — Theorem 4.5 shows any such module collapses to a trivial algebra in which all distinctions vanish, which in an implemented system would mean every truth comparison returns "equal."

**(b) Current readiness.** This work is purely analytical and has not been peer reviewed: by the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). No implementation, prototype, or empirical evaluation exists; analytical work of this kind cannot exceed TRL 3, and nothing here supports a claim beyond concept formulation.

**(c) The smallest next test.** The minimal de-risking step is a mechanical check, not an experiment: encode the Boolean axioms and the collapse argument of Theorem 4.5 in a proof assistant, and separately implement a depth-$d$ liar evaluator that emits $\tau_{d}(\iota)$ and verify that successive outputs are related by the one-coordinate shift for $d$ up to a bound (say $d = 64$). The outcome that refutes R4 is a depth profile that is not eventually periodic with period $2$, or successive profiles differing at more than one coordinate; the outcome that refutes R2 is impossible by construction (a checker that verifies $\iota = \neg\iota$ in $\mathcal{B}_{\mathrm{EP}}$ would instead reveal an error in the coordinate definitions). A second, slightly larger step is to implement the non-Boolean alternative (a De Morgan or Kleene quotient) and test whether $\iota = \neg\iota$ is consistent there, addressing open question one.

**(d) Binding constraints.** For any implementation, the first binding constraint is representational: $\iota$ is an infinite object, so an implementation must carry truncations, and the depth $d$ is a memory/precision parameter with the exact cost of $d$ stored bits per tracked oscillator (Section 4.4). The second is the collapse hazard: any code path that asserts $\iota = \neg\iota$ inside a Boolean-typed module propagates $\mathbf{0} = \mathbf{1}$, so type systems or runtime checks must prevent it. Whether distinction-based calculi can represent the shift transition $\sigma$ as a primitive, rather than as iterated re-entry, is an open question this paper does not settle.

**(e) Order-of-magnitude bounds.** As a projection with stated assumptions: if an evaluator tracks $n$ independent self-referential sentences, each requiring depth $d$ truncations, the state storage is $n \cdot d$ bits and the per-step update cost is $O(n \cdot d)$ bit operations, since each shift step touches one coordinate per sequence. For the illustrative parameters $n = 10^{3}$ and $d = 10^{2}$, this is $10^{5}$ bits $\approx 12.5$ kilobytes of state — negligible by current standards, but the bound is a projection from the truncation model of Section 3.4, not a measurement.

**(f) Risks and misuse paths.** The main misuse is rhetorical rather than technical: citing R1 ("the oscillator is an element of a Boolean algebra") while omitting R2 ("it does not equal its negation there") to claim that paradoxes have been dissolved into ordinary logic. The paper's own results refute that reading, and the collapse theorem is the guard against it: any system that both claims Boolean coherence and asserts self-negation is internally inconsistent, and this is mechanically checkable.

## 8. Conclusion

The conjecture that the liar oscillator can be promoted from a revision-theoretic process to a static value in a Boolean algebra of eventually periodic truth sequences resolves into a precise split. The algebra $\mathcal{B}_{\mathrm{EP}}$ exists, is Boolean, and is countably infinite; the oscillator $\iota$ is a genuine element of it. But the algebraic identity $\iota = \neg\iota$ is false there, and necessarily so: any Boolean congruence identifying the two collapses the algebra to a single element, because a self-negating element of a Boolean algebra forces $0 = 1$. What survives is exact and quantitative: the self-negation the paradox demands is realized dynamically, as the shift identity $\sigma(\iota) = \neg\iota$, with one unfolding step equal to one coordinate shift and a depth-$d$ truncation confining $\iota$ to a cylinder of measure $2^{-d}$ — for $d = 10$, $9.765625 \times 10^{-4}$. The oscillator is thus a computably approximable element of an ordinary Boolean algebra whose self-negation is a theorem about its orbit, not an equation about its value. The promotion conjecture, so refuted in its static form and confirmed in its dynamical form, yields a concrete engineering posture: represent the liar as a truncation plus a stated uncertainty, forbid the self-negating assignment by type or check, and seek the coherent home for $\iota = \neg\iota$ — if one exists — among the non-Boolean algebras the collapse theorem deliberately leaves open.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.5-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 4 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] A refinement of Stone duality to skew Boolean algebras. arXiv:1102.1242v2. https://arxiv.org/abs/1102.1242v2
[2] Algebraic curves for commuting elements in the q-deformed Heisenberg algebra. arXiv:0710.2748v2. https://arxiv.org/abs/0710.2748v2
[3] Invariant theory and coefficient algebras of Lie algebras. arXiv:2411.11095v3. https://arxiv.org/abs/2411.11095v3
[4] Categorical Constructions for Hopf Algebras. arXiv:0905.2613v3. https://arxiv.org/abs/0905.2613v3
[5] Quantum Boolean Algebras. arXiv:1011.5215v4. https://arxiv.org/abs/1011.5215v4
[6] Deformation of algebras over the Landweber-Novikov algebra. arXiv:math/0501518v2. https://arxiv.org/abs/math/0501518v2
[7] Connected Hopf Algebras of Dimension $p^2$. arXiv:1208.2280v2. https://arxiv.org/abs/1208.2280v2
[8] Deformation of dual Leibniz algebra morphisms. arXiv:math/0602046v1. https://arxiv.org/abs/math/0602046v1