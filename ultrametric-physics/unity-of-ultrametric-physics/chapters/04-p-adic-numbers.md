---
layout: chapter
title: "Chapter 4: The p-adic Absolute Value and Q_p"
permalink: /chapters/04-p-adic-numbers/
previous_chapter: /chapters/03-ultrametric-inequality/
previous_title: "The Ultrametric Inequality"
next_chapter: /chapters/05-bruhat-tits-tree/
next_title: "The Bruhat-Tits Tree"
---

## Chapter 4: The p-adic Absolute Value and $$\mathbb{Q}_p$$

Chapter 3 established the ultrametric inequality as the algebraic signature of nested distinctions. We now construct the most important family of ultrametric spaces — the $$p$$-adic numbers — and discover that they are not an exotic curiosity but a **necessary** completion of the rational numbers, mandated by Ostrowski's Theorem.

The guiding intuition: **the $$p$$-adic numbers measure distinctions at a specific prime $$p$$**. A number highly divisible by $$p$$ is $$p$$-adically small because it is highly distinguished by the prime $$p$$ — it sits deep within the hierarchy of $$p$$-distinctions. A number not divisible by $$p$$ is $$p$$-adically large — it lies near the root of the $$p$$-distinction tree, barely distinguished by $$p$$.

---

### 4.1 The p-adic Valuation: Counting Prime Distinctions

The $$p$$-adic valuation formalizes the idea of measuring a number by "how many distinctions at prime $$p$$ it contains."

<div class="definition">

**Definition 4.1 (p-adic Valuation).** Let $$p$$ be a prime. For a non-zero integer $$a$$, define $$v_p(a)$$ as the exponent of the highest power of $$p$$ dividing $$a$$. That is, write $$a = p^k \cdot m$$ with $$p \nmid m$$; then $$v_p(a) = k$$. For a non-zero rational number $$x = a/b$$ (in lowest terms), extend by:

\[
v_p(x) = v_p(a) - v_p(b).
\]

Set $$v_p(0) = +\infty$$ by convention.

</div>

The valuation counts distinctions: $$v_p(x) = k$$ means $$x$$ is distinguished by $$p$$ exactly $$k$$ times. A large positive $$v_p(x)$$ means $$p$$-distinctions deeply characterize $$x$$.

<div class="theorem">

**Theorem 4.2 (Properties of the Valuation).** For all $$x, y \in \mathbb{Q}$$:

1. **(V1 — Multiplicativity)** $$v_p(xy) = v_p(x) + v_p(y)$$. Prime distinctions compose multiplicatively.
2. **(V2 — Ultrametric inequality)** $$v_p(x + y) \ge \min(v_p(x), v_p(y))$$, with equality whenever $$v_p(x) \ne v_p(y)$$. The sum is at least as distinguished as the less-distinguished term.
3. **(V3 — Zero detection)** $$v_p(x) = +\infty$$ if and only if $$x = 0$$.

</div>

<div class="proof">

**Proof.** (V1) follows from the fundamental theorem of arithmetic: the exponent of $$p$$ in the product is the sum of exponents — distinctions compose. For (V2), write $$x = p^a \cdot r$$ and $$y = p^b \cdot s$$ with $$p \nmid rs$$, and assume without loss that $$a \le b$$. Then

\[
x + y = p^a(r + p^{b-a}s).
\]

Since $$p \nmid r$$, the term in parentheses may or may not be divisible by $$p$$. Thus $$v_p(x + y) \ge a = \min(v_p(x), v_p(y))$$. If $$a < b$$, then $$r + p^{b-a}s \equiv r \pmod{p}$$, so $$p$$ does not divide the sum in parentheses, and equality holds. ∎

</div>

Property (V2) is the ultrametric property in algebraic form: the sum of two numbers cannot be **more** distinguished by $$p$$ than the **less** distinguished of the two — a dramatic departure from ordinary arithmetic.

---

### 4.2 The p-adic Absolute Value: The Inversion of Size

From the valuation, we construct an absolute value that **inverts** our intuition: numbers highly distinguished by $$p$$ are considered **small**.

<div class="definition">

**Definition 4.3 (p-adic Absolute Value).** For $$x \in \mathbb{Q}$$, define

\[
|x|_p = p^{-v_p(x)},
\]

with the convention $$|0|_p = 0$$.

</div>

<div class="theorem">

**Theorem 4.4 (p-adic Absolute Value Axioms).** $$|\cdot|_p$$ satisfies:

1. **(A1 — Positive definiteness)** $$|x|_p \ge 0$$, with equality iff $$x = 0$$.
2. **(A2 — Multiplicativity)** $$|xy|_p = |x|_p \, |y|_p$$.
3. **(A3 — Ultrametric inequality)** $$|x + y|_p \le \max(|x|_p, |y|_p)$$, with equality when $$|x|_p \ne |y|_p$$.

</div>

<div class="proof">

**Proof.** (A1) and (A2) follow immediately from (V1) and (V3). For (A3), using the valuation inequality:

\[
|x + y|_p = p^{-v_p(x+y)} \le p^{-\min(v_p(x), v_p(y))} = \max(p^{-v_p(x)}, p^{-v_p(y)}) = \max(|x|_p, |y|_p).
\]

</div>

<div class="insight">

**Key Insight: The Inversion of Size.** The $$p$$-adic absolute value inverts our Archimedean intuition:

- **Numbers deeply distinguished by $$p$$ are small.** $$|p^n|_p = p^{-n}$$. For $$p = 5$$: $$|5|_5 = 1/5$$, $$|25|_5 = 1/25$$, $$|125|_5 = 1/125$$. The number $$5^{100}$$ is $$p$$-adically less than $$10^{-70}$$ — practically zero.
- **Numbers barely distinguished by $$p$$ are large.** $$|1/p|_p = p$$. For $$p = 2$$: $$|1/2|_2 = 2$$, $$|1/8|_2 = 8$$.

In the hierarchy of $$p$$-distinctions, **deeper = smaller**. The root is large; the leaves are infinitesimal. This is the natural metric on a tree of distinctions.

</div>

---

### 4.3 Ostrowski's Theorem: There Are No Other Distinctions

Ostrowski's Theorem (1916) is one of the most profound results in number theory. It states that the only ways to measure the "size" of a rational number — the only consistent ways to quantify distinction on $$\mathbb{Q}$$ — are the Archimedean way and the $$p$$-adic ways.

<div class="theorem">

**Theorem 4.5 (Ostrowski).** Every non-trivial absolute value on $$\mathbb{Q}$$ is equivalent either to the standard absolute value $$|\cdot|_\infty$$ or to a $$p$$-adic absolute value $$|\cdot|_p$$ for some prime $$p$$.

</div>

**Full proof:** See Appendix A.3.

<div class="insight">

**Why this matters.** Ostrowski's Theorem says the Archimedean and $$p$$-adic geometries are not alternatives among many — they are the **only** possibilities. Every consistent way of measuring distinction on the rational numbers is either additive (Archimedean) or nested ($$p$$-adic). There is no third way. Physics that starts from $$\mathbb{Q}$$ has exactly these two geometric families to choose from. Standard physics chose the Archimedean branch. This work explores the $$p$$-adic branch — and their adelic unification.

</div>

---

### 4.4 The Field $$\mathbb{Q}_p$$: Completing the Rationals

Completing $$\mathbb{Q}$$ with respect to $$|\cdot|_p$$ yields the field of **$$p$$-adic numbers**, denoted $$\mathbb{Q}_p$$. Just as $$\mathbb{R}$$ is the completion of $$\mathbb{Q}$$ with respect to $$|\cdot|_\infty$$, $$\mathbb{Q}_p$$ is the completion with respect to $$|\cdot|_p$$.

<div class="definition">

**Definition 4.6 (p-adic integers $$\mathbb{Z}_p$$).** The **$$p$$-adic integers** are the closed unit ball:

\[
\mathbb{Z}_p = \{x \in \mathbb{Q}_p : |x|_p \le 1\}.
\]

These are the numbers "barely distinguished" by $$p$$ — they sit near the root of the $$p$$-distinction tree.

</div>

Every $$x \in \mathbb{Q}_p$$ has a unique $$p$$-adic expansion:

\[
x = \sum_{n=v_p(x)}^{\infty} a_n p^n, \quad a_n \in \{0, 1, \ldots, p-1\}, \quad a_{v_p(x)} \neq 0.
\]

This is an infinite series in powers of $$p$$ — **increasing powers, not decreasing**. In $$\mathbb{R}$$, we write $$x = \sum_{n=-k}^{\infty} a_n 10^{-n}$$ (decreasing powers). In $$\mathbb{Q}_p$$, we write $$x = \sum_{n=v}^{\infty} a_n p^n$$ (increasing powers). The direction is inverted because **deep distinctions are small**.

<div class="example">

**Example 4.7 (A p-adic number).** In $$\mathbb{Q}_5$$:
\[
x = 2 \cdot 5^{-1} + 3 \cdot 5^0 + 1 \cdot 5^1 + 4 \cdot 5^2 + \cdots
\]
The leading term $$5^{-1}$$ means $$|x|_5 = 5$$ — barely distinguished by 5. The infinite tail encodes finer and finer distinctions.

</div>

<div class="example">

**Example 4.8 (The surprising identity).** In $$\mathbb{Q}_p$$:
\[
1 + p + p^2 + p^3 + \cdots = \frac{1}{1-p}
\]
This series diverges in $$\mathbb{R}$$ but converges in $$\mathbb{Q}_p$$ because $$|p^n|_p = p^{-n} \to 0$$. The terms become **smaller** as $$n$$ grows — deeper in the distinction tree — so the series converges.

</div>

---

### 4.5 Hensel's Lemma: Lifting Distinctions

Hensel's Lemma is the $$p$$-adic analogue of Newton's method. It allows approximate solutions (distinctions at a coarse scale) to be lifted to exact solutions (distinctions at all scales).

<div class="theorem">

**Theorem 4.9 (Hensel's Lemma).** Let $$f \in \mathbb{Z}_p[x]$$ and $$a_0 \in \mathbb{Z}_p$$ with $$f(a_0) \equiv 0 \pmod{p}$$ and $$f'(a_0) \not\equiv 0 \pmod{p}$$. Then there exists a unique $$a \in \mathbb{Z}_p$$ with $$f(a) = 0$$ and $$a \equiv a_0 \pmod{p}$$.

</div>

**Full proof:** See Appendix A.4.

Hensel's Lemma embodies the logic of nested distinctions: if a property holds at the coarsest scale (mod $$p$$) and the derivative is non-singular (the distinction is well-defined), then it holds at **all** finer scales. Distinctions propagate downward through the hierarchy.

---

### 4.6 Topological Properties

$$\mathbb{Q}_p$$ is:
- **Totally disconnected** — as all ultrametric spaces are
- **Locally compact** — $$\mathbb{Z}_p$$ is compact, mirroring the compactness of $$[0,1]$$ in $$\mathbb{R}$$
- **Zero-dimensional** — clopen balls form a base for the topology; boundaries have no thickness

---

### 4.7 Summary: The Two Families of Distinction

| Property | $$\mathbb{R}$$ (Archimedean) | $$\mathbb{Q}_p$$ (Ultrametric) |
|---|---|---|
| Distinction logic | Additive | Nested (by prime $$p$$) |
| Valuation | Size by magnitude | Distinction count $$v_p$$ |
| Absolute value | $$|x|_\infty$$ | $$|x|_p = p^{-v_p(x)}$$ |
| Triangle inequality | $$|x+y| \le |x|+|y|$$ | $$|x+y|_p \le \max(|x|_p,|y|_p)$$ |
| Small numbers | Near 0 (Archimedean) | Highly divisible by $$p$$ |
| Expansion direction | Decreasing powers | Increasing powers of $$p$$ |
| Connectivity | Connected | Totally disconnected |
| Geometry | Smooth manifold | Tree (Chapter 5) |

Both $$\mathbb{R}$$ and $$\mathbb{Q}_p$$ are completions of $$\mathbb{Q}$$ — necessary, inescapable, dictated by Ostrowski's Theorem. Every rational number lives simultaneously in the Archimedean world and in every $$p$$-adic world. The **adele ring** (Chapter 8) is the mathematical object that unifies them all.

---

**Next: [Chapter 5: The Bruhat-Tits Tree →]({{ '/chapters/05-bruhat-tits-tree' | relative_url }})**
