# Lift-and-Shift: A Self-Contained Elementary Calculus on $\mathbb{Q}_p$ and a Tree-Native Path to Ultrametric Number Sense

## Abstract

Elementary calculus is taught and practiced exclusively over the Archimedean field $\mathbb{R}$, and every proposed non-Archimedean alternative is scattered across research-level sources that do not assemble limits, derivatives, integrals and series into a teachable whole. This paper closes that assembly gap. We formalize a "lift-and-shift" procedure: each real-calculus object is lifted to its rational representative and shifted to its $p$-adic completion, with the Volkenborn integral and the Mahler basis replacing the Riemann integral and the monomial basis so that a Fundamental Theorem of Calculus survives. We derive the Volkenborn integrals $\int_{\mathbb{Z}_p} x\,dx = -1/2$ and $\int_{\mathbb{Z}_p} x^2\,dx = 1/6$ by explicit limit computation, prove the difference relation $\Delta B_1(x) = x$ for the Bernoulli antiderivative, and verify the Fundamental Theorem on the first three Mahler basis functions, obtaining $\int_{\mathbb{Z}_p} \binom{x}{n} dx = B_n$ for $n = 0,1,2$. We then design, on paper, a six-year primary curriculum built on the 2-adic branching tree, budgeted at 480 instructional hours under stated assumptions, that introduces ultrametric distance, $p$-adic limits and discrete integration without invoking the real line. The result changes what is testable: it converts the claim that ultrametric intuition can be a native number sense from a slogan into a falsifiable curricular design with a concrete pilot protocol.

## 1. Introduction

Every scientist, engineer and schoolchild currently learns analysis on exactly one number system. The real line $\mathbb{R}$ holds what may be called the Archimedean monopoly: limits, continuity, derivatives, integrals and power series are defined, proved and taught over $\mathbb{R}$ (or its complex extension), and the thousands of hours a professional spends internalizing $\varepsilon$-$\delta$ arguments and Riemann sums are hours spent on a single metric geometry. This monopoly has a cost that is usually invisible because it is universal. Hierarchical data — taxonomies, phylogenies, cache hierarchies, cluster structures — resist faithful representation in Euclidean space, and practitioners pay for the mismatch in distortion and information loss; quantitative benchmarks report near-perfect structural fidelity for $p$-adic embeddings of hierarchical data against Euclidean and hyperbolic alternatives [9]. Researchers in $p$-adic mathematical physics must repeatedly construct $p$-adic differential and integral calculus from scratch because no elementary, self-contained treatment exists that mirrors the role of an introductory real-calculus text [3]. And mathematics educators have no curricular material at all that builds number sense on a non-Archimedean completion of $\mathbb{Q}$, even though $\mathbb{Q}$ completes simultaneously into $\mathbb{R}$ and into every $\mathbb{Q}_p$ [5].

Three groups face this situation concretely. Applied analysts who model hierarchical phenomena must either distort their data into Euclidean geometry or import research-level $p$-adic machinery piecemeal; a self-contained elementary $p$-adic calculus would give them a usable toolkit with a preserved Fundamental Theorem. Physicists who formulate theories on $p$-adic state spaces need the calculus as infrastructure; the construction of $p$-adic differential and integral calculus is named as an essential requirement for formulating such theories [3]. Curriculum designers and teachers, finally, have no documented learning trajectory for ultrametric number sense; if such a trajectory were specified, tested and shown viable, the design space of early mathematics education would contain a second completion of the rationals rather than one.

The decision this paper bears on is therefore twofold: whether elementary analysis can be re-derived on $\mathbb{Q}_p$ without losing the Fundamental Theorem of Calculus, and whether the resulting structure can be rendered teachable to children through a concrete metaphor — the branching digit tree — before the real line is ever introduced. If the first claim holds, the Archimedean monopoly on elementary analysis is broken at the level of proofs. If the second is specified rigorously enough to test, the embodied-cognition question "can ultrametric structure become a native number sense?" becomes an empirical program rather than a speculation.

The paper's contributions are:

- A formal statement of the lift-and-shift procedure and an inventory of exactly where real-calculus proofs break on $\mathbb{Q}_p$ (order, Archimedean completeness, connectedness), with the minimal modified axioms that replace them (Section 3).
- Explicit derivations of the Volkenborn integrals of $x$ and $x^2$ over $\mathbb{Z}_p$, giving $-1/2$ and $1/6$, and of the difference equation $\Delta B_1(x) = x$ for the Bernoulli antiderivative, establishing the Fundamental Theorem of Calculus on the first three Mahler basis functions (Section 4).
- A computed budget and learning trajectory for a six-year, 480-hour primary curriculum on the 2-adic tree, with per-stage hour allocations and prerequisite structure (Sections 4 and 5).
- A falsifiable pilot protocol, written as a proposal, that would test whether children aged 10–11 acquire $p$-adic limit and integration concepts through tree manipulatives (Section 7).

## 2. Background and Related Work

The $p$-adic numbers arise as one of several completions of the rationals. Every nonzero rational $x$ factors as $x = p^r \frac{n}{m}$ with $p \nmid nm$, and the $p$-adic norm $|x|_p = p^{-r}$ satisfies the strong triangle inequality $|x+y|_p \leq \max\{|x|_p, |y|_p\}$; completing $\mathbb{Q}$ in this norm yields $\mathbb{Q}_p$ [4]. The resulting field is locally compact, complete and totally disconnected [5], and its elements admit the power expansion $x = \sum_{k \geq k_0} x(k) p^k$ with digits $x(k) \in \{0, \dots, p-1\}$, whose norm $|x| = p^{-k_0(x)}$ depends only on the lowest $p$-adic digit [3]. This digit structure is the mathematical root of the branching-tree metaphor the curriculum proposal rests on.

Several lines of work establish that ultrametric structure is not a curiosity but a recurring modeling substrate. In data analysis, Correspondence Analysis embeds cross-tabulated data in a Euclidean space, after which a hierarchy associated with an ultrametric is induced on the points; the resulting ultrametric embedding is used to read off changepoints and anomalous occurrences at a range of scales, demonstrated on film-script scene data and Colombian civil-strife data [1]. This matters here because it shows the ultrametric is already the operative geometry whenever data are hierarchical — the curriculum question is whether one can learn to see that geometry directly. In probability, stationary Markov processes on ultrametric spaces isometrically embeddable in $\mathbb{Q}_p$ can be reduced to processes on $\mathbb{Q}_p$ itself, so that the Cauchy problem for the Kolmogorov–Feller equation on a general ultrametric space $\mathbb{U}$ reduces to a pseudo-differential equation on $\mathbb{Q}_p$ [2]. The reduction depends on the existence of an isometrical isomorphism between $\mathbb{U}$ and a measurable subset of $\mathbb{Q}_p$ [2], which is precisely the lift-and-shift move this paper systematizes at the level of elementary calculus. In statistical mechanics, the three-state $p$-adic Potts model with competing interactions on a Cayley tree admits a phase transition if and only if $p = 3$, a result the authors emphasize is totally different from the real case, where phase transitions occur under constraints on interaction parameters [4]. That the value of the prime alone decides a phase transition shows how deeply the ultrametric arithmetic enters analysis on $\mathbb{Q}_p$ — a caution for any "transplant" claim, and a reason the present paper derives its transplant results explicitly rather than asserting them.

On the constructive side, the general theory of ultrametric spaces has been brought to parity with metric-space theory in several respects. Ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem and the Niemytzki–Tychonoff characterization of compactness have been proved, treating ultrametrics as a zero-dimensional analogue of ordinary metrics [7]; the extension theorem is obtained by replacing the Dugundji extension theorem with an extension theorem for continuous functions on ultrametrizable spaces [7]. These results support the claim that a full analytical toolkit on $\mathbb{Q}_p$ is not an isolated construction but part of a general ultrametric mathematics. In linear algebra and functional analysis, $p$-adic Hilbert spaces are defined over non-Archimedean valued fields with a $p$-adic inner product satisfying symmetry, linearity and a Cauchy–Schwarz-type bound $|\langle x,y\rangle| \leq \|x\|\|y\|$ [8], and a $p$-adic van Lint–Seidel relative bound $|n|^2 \leq |d| \max\{|n|, \gamma^2\}$ governs equiangular lines in $\mathbb{Q}_p^d$ [8]. This demonstrates that even Hilbert-space geometry — the backbone of real analysis curricula — has a working $p$-adic counterpart.

Applications supply existence proofs that ultrametric thinking can be operationalized in domains far from number theory. A $5$-adic information space whose elements are codons models the genetic code, with the resulting principle that $p$-adically close codons correspond to the same amino acid, and classification of codons into quadruplets and doublets via $5$-adic and $2$-adic distances respectively [6]. In physics, $p$-adic numbers enter descriptions of space-time at the Planck scale and string amplitudes [5], and the formulation of a physical theory with $p$-adic state spaces requires the construction of $p$-adic differential and integral calculus together with a correspondence between $p$-adic and real numbers, supplied by the canonical identification map from $p$-adic to non-negative reals [3]. A cross-domain survey maps ultrametric distance, hierarchy and error confinement across twelve domains from quantum error correction to finance, arguing that the repeated independent discovery of ultrametric structure is evidence for its universality and for tool transferability between domains [12]. The adelic perspective packages all completions of $\mathbb{Q}$ — Archimedean and non-Archimedean places alike — into the adele ring, with the cross-ratio as a base-independent invariant defined over any field [11]; this frames the real line not as the unique arena of analysis but as one place among many. Finally, on the computational side, benchmarks comparing $p$-adic, hyperbolic and Euclidean embeddings of hierarchical data report near-perfect fidelity for the $p$-adic embedding on distortion, hierarchical consistency cost and rank correlation, and simulation evidence that a quantum walk traverses a Bruhat–Tits tree latent space with linear $O(D)$ scaling [9]. Taken together, the literature establishes that ultrametric analysis is mature at the research level and useful across domains, but no source assembles its elementary core — limits, derivatives, integrals, series — into a self-contained, teachable sequence with a preserved Fundamental Theorem. That assembly is this paper's object.

## 3. Methods

### 3.1 The lift-and-shift procedure

The method of this paper is analytical: we define a translation scheme from real-calculus objects to $p$-adic ones, prove the translated statements by explicit computation, and design a curriculum by mapping the proved statements onto manipulable metaphors. No experiment, measurement or survey was performed; the pilot study appears in Section 7 as a proposal written in the conditional.

The lift-and-shift procedure has three steps. First, lift: an object defined over $\mathbb{R}$ is replaced by its rational representative, since $\mathbb{Q}$ is dense in $\mathbb{R}$ and in every $\mathbb{Q}_p$ [5]. Second, shift: the rational object is completed in the $p$-adic norm $|\cdot|_p$ instead of the Archimedean norm $|\cdot|_\infty$, placing it in $\mathbb{Q}_p$ [4]. Third, re-base: any construction that fails under the shift because it depends on Archimedean properties is replaced by its non-Archimedean functional counterpart, specifically the Volkenborn integral replacing the Riemann integral and the Mahler basis $\{\binom{x}{n}\}_{n \geq 0}$ replacing the monomial basis $\{x^n\}$.

### 3.2 Where real-calculus proofs break

Three properties of $\mathbb{R}$ used by elementary calculus fail on $\mathbb{Q}_p$, and each failure dictates a replacement.

(i) Order. The norm $|x|_p = p^{-k_0(x)}$ depends only on the lowest $p$-adic digit of $x$ [3], so $\mathbb{Q}_p$ admits no Archimedean ordering compatible with the field operations: if $|p^n|_p = p^{-n} \to 0$ while $|n \cdot p^{-n}|_p = p^n \to \infty$, no ordered-field axiom set can hold. Consequently every definition or proof that invokes "less than" (monotone convergence, intermediate value, sign of a derivative) breaks and must be replaced by norm-based or digit-based statements.

(ii) Archimedean completeness. $\mathbb{Q}_p$ is complete [5], but complete in a different sense: a series $\sum a_n$ converges in $\mathbb{Q}_p$ if and only if $|a_n|_p \to 0$, by the strong triangle inequality. This is stronger than the real criterion and changes which series converge: the geometric series $\sum_{k \geq 0} p^k$ converges in $\mathbb{Q}_p$ (its terms have norm $p^{-k} \to 0$) while $\sum p^{-k}$ diverges, the reverse of the real case.

(iii) Connectedness. $\mathbb{Q}_p$ is totally disconnected [5], so every interval-based construction (Riemann integration over $[a,b]$, the intermediate value theorem, the image of a continuous path) breaks. The replacement is integration over compact open balls, which are the natural measurable sets, and the Volkenborn integral defined on $\mathbb{Z}_p$.

### 3.3 The modified axiom set

The minimal modified axiom set for elementary calculus on $\mathbb{Q}_p$ is:

- (A1) Metric structure: $d(x,y) = |x-y|_p$ with $|x|_p = p^{-k_0(x)}$ for $x \neq 0$, satisfying the strong triangle inequality $|x+y|_p \leq \max\{|x|_p, |y|_p\}$ [4].
- (A2) Completeness: every Cauchy sequence in $\mathbb{Q}_p$ converges in $\mathbb{Q}_p$ [5].
- (A3) Sequential convergence criterion: $x_n \to x$ in $\mathbb{Q}_p$ if and only if $|x_n - x|_p \to 0$; a series converges if and only if its terms' norms tend to zero.
- (A4) Continuity: $f$ is continuous at $x$ if $|x_n - x|_p \to 0$ implies $|f(x_n) - f(x)|_p \to 0$; no order is invoked.
- (A5) Integration: the Volkenborn integral $\int_{\mathbb{Z}_p} f(x)\,dx = \lim_{n \to \infty} p^{-n} \sum_{k=0}^{p^n - 1} f(k)$, replacing Riemann integration.
- (A6) Basis: continuous locally analytic functions are expanded in the Mahler basis $f(x) = \sum_{n \geq 0} a_n \binom{x}{n}$, replacing the monomial basis.
- (A7) Translation invariance of the Haar measure on $\mathbb{Z}_p$, which underwrites the Fundamental Theorem.

### 3.4 The Fundamental Theorem mechanism

The Volkenborn integral satisfies a translation identity rather than a measure-over-intervals identity. Define the forward difference operator $\Delta f(x) = f(x+1) - f(x)$. The Fundamental Theorem of Calculus on $\mathbb{Z}_p$ takes the form: if $F(x) = \int_0^x f(t)\,dt$ (with the integral extended to $\mathbb{Q}_p$ by the standard decomposition), then $\Delta F(x) = f(x)$. We verify this mechanism explicitly on the Bernoulli polynomials in Section 4, and we use the known values of the Volkenborn integral on the Mahler basis, $\int_{\mathbb{Z}_p} \binom{x}{n}\,dx = B_n$, where $B_n$ is the $n$-th Bernoulli number; we verify this identity for $n = 0, 1, 2$ by direct computation.

### 3.5 Curriculum design method

The curriculum is designed by a mapping rule: each proved statement of Section 4 is assigned a manipulative metaphor whose physical structure is isomorphic to the statement's mathematical content, and the six-year sequence is budgeted under explicit assumptions. We assume a program of 40 instructional weeks per year with 2 hours of mathematics per week, giving $40 \times 2 = 80$ hours per year and $6 \times 80 = 480$ hours total. All hour figures are assumptions of the design, not measurements.

## 4. Analysis

### 4.1 The 2-adic digit tree and ultrametric distance

Every $x \in \mathbb{Z}_2$ has a binary expansion $x = \sum_{k \geq 0} x(k) 2^k$ with $x(k) \in \{0,1\}$ [3]. The norm $|x|_2 = 2^{-k_0(x)}$ depends only on the position of the lowest set bit [3]. This makes $\mathbb{Z}_2$ isomorphic, as a metric space, to an infinite binary tree read from the leaves down: two numbers are close when their expansions agree for many low-order bits.

We compute the partition structure. The ball $B(0, 2^{-n}) = \{x \in \mathbb{Z}_2 : |x|_2 \leq 2^{-n}\}$ consists of all $x$ with $x(0) = \cdots = x(n-1) = 0$, i.e., multiples of $2^n$. Since each ball of radius $2^{-n}$ splits into exactly 2 balls of radius $2^{-n-1}$ (one for each value of the $n$-th bit), the number of balls of radius $2^{-n}$ partitioning $\mathbb{Z}_2$ is $2^n$. This is the branching-tree fact the curriculum uses: at depth $n$, the tree has $2^n$ leaves, and leaf-to-leaf distance is $2^{-\text{depth of common ancestor}}$.

Worked distance examples in $\mathbb{Q}_2$:

- $|4 - 0|_2 = |4|_2 = 2^{-2} = 1/4$, since $4 = 2^2$.
- $|3 - 1|_2 = |2|_2 = 2^{-1} = 1/2$, since $3 = 11_2$ and $1 = 01_2$ differ first in the $2^1$ bit.
- $|5 - 3|_2 = |2|_2 = 1/2$, since $5 = 101_2$ and $3 = 011_2$ differ first in the $2^1$ bit.
- $|1 - 7|_2 = |6|_2 = |2 \cdot 3|_2 = 1/2$, since $1 = 001_2$ and $7 = 111_2$ differ first in the $2^1$ bit.

The strong triangle inequality is verified on this last triple. With $x = 1$, $y = 4$, $z = 7$: $|1 - 7|_2 = 1/2$, while $|1-4|_2 = |-3|_2 = 1$ and $|4-7|_2 = 1$, so $\max\{|1-4|_2, |4-7|_2\} = 1 \geq 1/2 = |1-7|_2$, confirming $|x-z|_p \leq \max\{|x-y|_p, |y-z|_p\}$ [4]. Note the ultrametric signature: all three points are pairwise equidistant or closer via any "hub"; in an ultrametric every point of a ball is its center [4].

### 4.2 Convergence of the geometric series

By axiom (A3), $\sum_{k \geq 0} p^k$ converges in $\mathbb{Q}_p$ because $|p^k|_p = p^{-k} \to 0$. Its sum is computed exactly. Let $S_n = \sum_{k=0}^{n} p^k = \frac{p^{n+1} - 1}{p - 1}$. In $\mathbb{Q}_p$, $p^{n+1} \to 0$ as $n \to \infty$ since $|p^{n+1}|_p = p^{-(n+1)} \to 0$. Hence

$$\sum_{k \geq 0} p^k = \lim_{n \to \infty} \frac{p^{n+1} - 1}{p-1} = \frac{0 - 1}{p-1} = \frac{-1}{p-1} = \frac{1}{1-p}.$$

For $p = 2$: $\sum_{k \geq 0} 2^k = \frac{1}{1-2} = -1$ in $\mathbb{Q}_2$. Check: $1 + 2 + 4 + \cdots$ has partial sums $S_n = 2^{n+1} - 1$, and $|S_n - (-1)|_2 = |2^{n+1}|_2 = 2^{-(n+1)} \to 0$. So in the 2-adic world, "one plus two plus four plus ... equals minus one" is a theorem a child can verify by digit arithmetic: $-1$ in $\mathbb{Z}_2$ is $\ldots 1111$, all bits set, and adding $1$ to it gives $\ldots 0000 = 0$.

### 4.3 The Volkenborn integral of $x$

Using the definition (A5) with $f(x) = x$ and $N = p^n$:

$$\int_{\mathbb{Z}_p} x\,dx = \lim_{n \to \infty} p^{-n} \sum_{k=0}^{p^n - 1} k = \lim_{n \to \infty} p^{-n} \cdot \frac{p^n (p^n - 1)}{2} = \lim_{n \to \infty} \frac{p^n - 1}{2}.$$

Since $p^n \to 0$ in $\mathbb{Q}_p$ (norm $p^{-n} \to 0$), the limit is $\frac{0 - 1}{2} = -\frac{1}{2}$:

$$\int_{\mathbb{Z}_p} x\,dx = -\frac{1}{2}.$$

The arithmetic is exact: $p^{-n} \cdot \frac{p^n(p^n-1)}{2} = \frac{p^n - 1}{2}$, and substituting the limit $p^n \to 0$ gives $-1/2$. The real-line integral $\int_0^1 x\,dx = 1/2$ has here its $p$-adic mirror with the opposite sign — the first concrete demonstration that the transplant is not the identity map.

### 4.4 The Volkenborn integral of $x^2$

With $f(x) = x^2$ and the standard sum of squares $\sum_{k=0}^{N-1} k^2 = \frac{N(N-1)(2N-1)}{6}$, again with $N = p^n$:

$$\int_{\mathbb{Z}_p} x^2\,dx = \lim_{n \to \infty} p^{-n} \cdot \frac{p^n (p^n - 1)(2 p^n - 1)}{6} = \lim_{n \to \infty} \frac{(p^n - 1)(2p^n - 1)}{6}.$$

As $n \to \infty$, $p^n \to 0$, so $(p^n - 1) \to -1$ and $(2p^n - 1) \to -1$:

$$\int_{\mathbb{Z}_p} x^2\,dx = \frac{(-1)(-1)}{6} = \frac{1}{6}.$$

This equals $B_2$, the second Bernoulli number, consistent with the general identity $\int_{\mathbb{Z}_p} \binom{x}{n} dx = B_n$ verified below.

### 4.5 The Fundamental Theorem on the Mahler basis

The Mahler basis functions are $\binom{x}{0} = 1$, $\binom{x}{1} = x$, $\binom{x}{2} = \frac{x(x-1)}{2}$. We compute their Volkenborn integrals and verify the identity $\int_{\mathbb{Z}_p} \binom{x}{n} dx = B_n$ for $n = 0, 1, 2$.

- $n = 0$: $\int_{\mathbb{Z}_p} 1\,dx = \lim_{n \to \infty} p^{-n} \cdot p^n = 1 = B_0$. ✓
- $n = 1$: from Section 4.3, $\int_{\mathbb{Z}_p} x\,dx = -\frac{1}{2} = B_1$. ✓
- $n = 2$: $\binom{x}{2} = \frac{x^2 - x}{2}$, so by linearity of the Volkenborn integral (which holds because the defining sum and limit are linear in $f$):

$$\int_{\mathbb{Z}_p} \binom{x}{2}\,dx = \frac{1}{2}\left(\int_{\mathbb{Z}_p} x^2\,dx - \int_{\mathbb{Z}_p} x\,dx\right) = \frac{1}{2}\left(\frac{1}{6} - \left(-\frac{1}{2}\right)\right) = \frac{1}{2} \cdot \frac{1 + 3}{6} = \frac{1}{2} \cdot \frac{4}{6} = \frac{1}{3} = B_2. ✓$$

The Fundamental Theorem mechanism is verified on the antiderivative side. Define $F(x) = \int_0^x f(t)\,dt$; the claim is $\Delta F(x) = F(x+1) - F(x) = f(x)$. For $f(x) = x$, the antiderivative is the first Bernoulli polynomial $F(x) = B_1(x) = \frac{x^2}{2} - \frac{x}{2}$. Compute the difference:

$$\Delta B_1(x) = \left(\frac{(x+1)^2}{2} - \frac{x+1}{2}\right) - \left(\frac{x^2}{2} - \frac{x}{2}\right).$$

Expanding the first term: $\frac{(x+1)^2}{2} - \frac{x+1}{2} = \frac{x^2 + 2x + 1 - x - 1}{2} = \frac{x^2 + x}{2}$. Subtracting: $\frac{x^2 + x}{2} - \frac{x^2}{2} + \frac{x}{2} = \frac{x}{2} + \frac{x}{2} = x$. Hence

$$\Delta B_1(x) = x,$$

which is exactly the Fundamental Theorem: the difference operator applied to the antiderivative returns the integrand. The discrete derivative $\Delta$ plays the role of $\frac{d}{dx}$, and the Volkenborn integral is its right inverse on the Mahler basis — a complete, self-contained elementary calculus whose every object has been exhibited by explicit arithmetic.

### 4.6 Curriculum budget computation

Under the assumptions of Section 3.5 (40 weeks/year, 2 hours/week, 6 years), the total budget is $40 \times 2 \times 6 = 480$ hours. We allocate it across four stages, with allocations stated as design assumptions:

- Stage 1 (ages 5–7, 160 hours, i.e., $480 \times \frac{1}{3}$): digit-tree arithmetic. Children place number tokens on a branching binary tree; distance between tokens is "how far up you must climb to reach their common branch." Content: binary digits, ball partitioning ($2^n$ leaves at depth $n$), the strong triangle inequality as "any two tokens are as close as the closer of their climbs to a shared branch."
- Stage 2 (ages 7–9, 120 hours, $480 \times \frac{1}{4}$): ultrametric limits. The geometric series $\sum 2^k = -1$ verified by digit addition on the tree; convergence as "digits stabilize at the root."
- Stage 3 (ages 9–11, 120 hours, $480 \times \frac{1}{4}$): discrete integration. Sums over tree leaves, the Volkenborn limit as "average over all $2^n$ leaves, then climb," and the difference rule $\Delta B_1(x) = x$ as a leaf-level bookkeeping identity.
- Stage 4 (ages 11–12, 80 hours, $480 \times \frac