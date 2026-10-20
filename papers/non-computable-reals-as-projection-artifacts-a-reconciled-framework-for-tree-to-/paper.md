# Non-Computable Reals as Projection Artifacts: A Formal Analysis of Tree‑to‑Manifold Construction of the Continuum

## Abstract

Continuum physics and analysis are formulated over the completed real line, yet every measurement, record, and computation is finite, and the physical role of the uncountable remainder of $\mathbb{R}$ remains unresolved. This paper develops a formal framework for the conjecture that the continuum is constructed rather than primitive: natural numbers, rationals, and computable reals arise from a distinction operator via enclosure operations, while the full real line emerges only through a lossy projection—the Monna‑map—of a discrete, non‑Archimedean Bruhat–Tits tree onto the Archimedean interval. The specific gap addressed is that the computable/non‑computable boundary has been asserted in prior distinction‑based work as a projection effect without explicit counts or falsification conditions. We derive, with all arithmetic shown, that the computable reals have Lebesgue measure $0$, so the artifact set has full measure in $[0,1]$; that at tree depth $n=20$ exactly $129$ reduced rationals shadow $2^{20}=1{,}048{,}576$ paths, a definable fraction of $1.23024\times10^{-4}$; that programs of length at most $100$ number $2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751$; and that the definable fraction decays at least exponentially in depth. The projection thesis itself remains conjectural, with explicit falsification conditions and a proposed but unexecuted enumeration protocol. The framework reinterprets the measure‑theoretic dominance of non‑computable reals as a projection effect and gives constructive‑mathematics‑oriented physicists a checkable boundary for what the discrete substrate can encode.

## 1. Introduction

Physicists, numerical analysts, and instrument designers work daily with the real line as if it were a completed object: continuum differential equations, spectral theory, and floating‑point models all presuppose $\mathbb{R}$. Yet every laboratory measurement is a finite record, and a finite record cannot encode cardinality. Standard set‑theoretic presentations give no account of *where* the non‑computable reals $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ come from or why they dominate $\mathbb{R}$ in measure, and the distinction‑based research program that does address this question has so far stated its central claims— that non‑computables are artifacts of a projection from a discrete substrate—without explicit counts, derivations, or falsification conditions. If the analysis in this paper holds, the measure‑theoretic dominance of non‑computable reals becomes a quantified projection effect, analogous to up‑sampling artifacts in generative synthesis [1, 4], and the boundary between physically meaningful and physically vacuous mathematics acquires a computable test.

The stance taken here follows the distinction‑based program of the QNFO corpus, in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed [8, 9]. In that program, natural numbers arise by iterated enclosure of distinctions, rationals by pairwise enclosure, and computable reals $\mathbb{R}_{\mathrm{comp}}$ by limits of rational procedures [8]. The full continuum $\mathbb{R}$ then emerges only at a final step: a projection of a discrete, non‑Archimedean structure onto a smooth Archimedean manifold. The discrete side is a Bruhat–Tits tree, an infinite non‑Archimedean object in which closeness is measured by a valuation rather than an Archimedean metric; prior work has argued that macroscopic spacetime itself can be derived from the discrete properties of such a tree, with an Archimedean projection yielding continuous real coordinates [10]. The projection—called the Monna‑map, following the corpus terminology [9]—is lossy: many distinct tree paths map to the same Archimedean point, and the points with no finitely specifiable discrete pre‑image are, on the conjecture analyzed here, created by the map rather than discovered in the tree. We call these points **artifacts**, in the same sense that up‑sampling a signal can create features that exist only in the output format but not in the source data [1, 4].

This reframing has two payoffs. First, it re‑derives the computable/constructive hierarchy from pure distinction logic: the boundary between $\mathbb{R}_{\mathrm{comp}}$ and $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ becomes the boundary between what the discrete tree can finitely encode and what only the projection produces. Second, it gives a quantitative skeleton to the position that non‑computable “breadth’’ is physically vacuous [9, 11]: everything the discrete side finitely encodes occupies Lebesgue measure zero of the shadow, so a uniformly random point of $[0,1]$ is an artifact with probability $1$—conditional on the projection conjecture.

Our contributions are:
1. Precise definitions of the distinction operator, the enclosure hierarchy, the valuation tree, and the Monna‑map projection, together with three conjectures (Section 3).
2. Explicit derivations, with all arithmetic shown, that the computable reals have Lebesgue measure $0$ and the artifact set full measure; that the Farey count of depth‑$20$ rational shadows is exactly $129$ against $2^{20}=1{,}048{,}576$ paths; that programs of length at most $100$ number $2^{101}-1$; and that the definable fraction decays exponentially in depth (Section 4).
3. Results and labeled projections, including a comparison between the depth‑$20$ rational pool and the length‑$100$ program pool (Section 5).
4. Limitations, failure modes, falsification conditions, and a practical pathway with readiness assessment and a smallest next test (Sections 6–7).

## 2. Background and Related Work

We organize the related work into four strands: artifacts of lossy representation, the artifact concept beyond engineering, alternative constructions of the reals, and distinction‑based foundations and projection theory.

**Artifacts of lossy representation.** Biswas and Paris report that up‑sampling layers in neural audio synthesis introduce undesired artifacts, and that such artifacts had been overlooked in audio processing [1]. In the image domain, StyleGAN sometimes synthesizes high‑resolution faces containing prominent circular artifacts; a systematic investigation attributes these to the architecture’s up‑sampling pathway and proposes a removal solution [4]. Together, [1] and [4] support the principle that when a generator projects internal discrete structure onto a continuous output manifold, the projection itself can be the source of structured, systematic defects. Our claim is that $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ is exactly such a systematic defect of the tree‑to‑manifold projection.

**The artifact concept beyond engineering.** The notion that artifacts are not mere noise but carry structural consequences has been argued within mathematics itself: an essay extends Langdon Winner’s idea that artifacts have politics into mathematics, providing examples of mathematical artifacts with political dimensions and arguing that all mathematical artifacts have politics, with implications for embedding ethics into curricula [3]. Whatever one makes of the normative thesis, its descriptive core—that mathematical objects can be artifacts of the machinery that produces them, with real consequences—is precisely the ontology we assign to non‑computable reals.

**Alternative constructions of the reals.** In combinatorics, structured counts of finite objects can be organized by generating‑function‑style enumeration; our Farey counts in Section 4.2 adopt that enumerative style directly, summing Euler’s totient over denominators. We retain [5] in the reference list as a pointer to that enumerative literature, and no result derived below depends on its contents. Whether the image of the Monna‑map is all of $\mathbb{R}$, and what its range misses, is treated here as a set‑theoretic and measure‑theoretic question, resolved in Section 4 by counting and covering arguments rather than by operator‑algebraic methods. We retain [6] in the reference list as a pointer to the projection literature, and no claim of this paper rests on its specific results.

**Distinction‑based foundations and the prior framework.** We adopt as a working hypothesis, following the distinction‑based program [8], that the act of drawing a distinction is the primitive operation from which number systems can be built. The specific claims about the computable/non‑computable boundary analyzed in Sections 3–4 are this paper’s own conjectures C1–C3 and derivations, not established results attributed to [8]. The QNFO corpus supplies the specific thesis we analyze: that the uncountability of the reals conflates Archimedean completeness (“depth’’) and set‑theoretic cardinality explosion (“breadth’’), with all physically relevant properties preserved by the computable reals alone [9]. The position that the uncountable breadth of the reals is physically vacuous while the computable reals suffice for continuum physics is adopted here as the interpretive stance behind conjecture C3, with [9] cited as the source of that position and no proved result attributed to it. Likewise, the picture of emergent spacetime on a Bruhat–Tits tree whose Archimedean projection yields continuous real coordinates is taken as a motivating hypothesis, with [10] cited for the geometric picture; in our construction the Bruhat–Tits tree is the Valuation axis made geometric, and the Monna‑map is the passage from Valuation to Depth/Breadth. The enclosure hierarchy of Section 3.1 is our formalization of the generation‑by‑distinction picture these works advance.

## 3. Methods

### 3.1 The distinction operator and enclosure hierarchy

Following the distinction‑based calculus of the QNFO program [8], we take as primitive the act of drawing a distinction. Formally, fix a two‑value form $V_{2}=\{0,1\}$ and let the distinction operator $\delta$ be a map that, applied to an unmarked space, produces a marked and an unmarked region. Iterated application generates a rooted branching structure; the reduction rules of Calling and Crossing ensure that repeated identical distinctions do not create new objects [8].

**Definition 3.1 (Enclosure hierarchy).** Define inductively: $E_{0}=\{\varnothing\}$, the undifferentiated space; $E_{k+1}=\mathcal{P}_{\mathrm{fin}}(E_{k})$, the finite enclosures of level‑$k$ objects. Level‑1 objects correspond to single distinctions; finite multisets of level‑1 distinctions, ordered by iteration, yield the natural numbers $\mathbb{N}$, matching the number‑builder sequence in which one distinction yields $1$ and iterated Calling yields $\mathbb{N}$ [8]. Pairwise enclosure of naturals with an orientation yields the integers $\mathbb{Z}$, and the rationals $\mathbb{Q}$ arise as ordered pairs $(a,b)$ with $b\neq0$, $b\in\mathbb{N}$, modulo $(a_{1},b_{1})\sim(a_{2},b_{2})$ iff $a_{1}b_{2}=a_{2}b_{1}$. Every element of this hierarchy is finitely specifiable: a finite syntactic object built by $\delta$ and enclosure.

### 3.2 The discrete side: valuation trees

**Definition 3.2 (Valuation tree).** Fix a prime $p$ and let $T_{p}$ be the rooted tree whose vertices at level $n$ correspond to residue classes modulo $p^{\,n+1}$, each vertex having $p$ children; this is the Bruhat–Tits tree of $\mathbb{Q}_{p}$ in its standard combinatorial presentation. A path from the root is an element of the boundary $\partial T_{p}$, which carries an ultrametric $d_{p}$ induced by the $p$‑adic valuation $v_{p}$. For concreteness and computability of all counts we work primarily with the binary tree $T_{2}$ ($p=2$), whose boundary $\partial T_{2}$ is in bijection with infinite binary sequences. A second convention—the $(p+1)$‑regular presentation of the Bruhat–Tits tree of $\mathrm{PGL}_{2}$ over $\mathbb{Q}_{p}$, in which every vertex has $p+1$ neighbors—is used in Section 4.5 for the regular‑tree counts and is explicitly labeled as a separate convention.

### 3.3 The Monna‑map projection

**Definition 3.3 (Monna‑map).** The Monna‑map is the projection
$$
\mu:\partial T_{2}\to[0,1],\qquad
\mu\big((b_{1},b_{2},b_{3},\ldots)\big)=\sum_{k=1}^{\infty}b_{k}\,2^{-k},
$$
i.e., the standard binary‑expansion identification of the Cantor‑set boundary with the unit interval. The tree carries the ultrametric $d_{2}$; the interval carries the Euclidean metric $d_{\infty}(x,y)=|x-y|$. The map $\mu$ is continuous from the ultrametric topology onto the Euclidean topology, is many‑to‑one exactly on the dyadic rationals (which have two expansions), and collapses all ultrametric structure. As the prior framework notes, this is the ordinary binary‑expansion map and the framing as a tree projection is a choice, not a canonical identification [9]; nothing derived below depends on a canonical choice.

**Definition 3.4 (Computable shadow, artifact set).** A point $x\in[0,1]$ is a *computable shadow* if there is a finite program that, given $n$, outputs the first $n$ bits of a binary expansion of $x$. Let $\mathbb{R}_{\mathrm{comp}}[0,1]$ denote the set of computable shadows. The *artifact set* is
$$
A=[0,1]\setminus\mathbb{R}_{\mathrm{comp}}[0,1].
$$

### 3.4 Conjectures

- **C1 (Generation).** $\mathbb{N}$, $\mathbb{Q}$, and $\mathbb{R}_{\mathrm{comp}}$ arise from the distinction operator by enclosure operations; each computable real corresponds to a finite or limit‑definable tree path.
- **C2 (Projection).** The Monna‑map is surjective and non‑injective, and points of $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ have no finite or limit‑definable pre‑image: they are artifacts, created by $\mu$ rather than discovered in $\partial T_{2}$.
- **C3 (Dominance).** The artifact set has full Lebesgue measure in $[0,1]$.

C3 is *derived conditionally* in Section 4 from the countability of finite programs plus the standard covering argument; its interpretation as “projection dominance’’ depends on C2, which remains conjectural.

### 3.5 Simulation protocol (proposed, not executed)

Finite‑depth trees of depths $d\in\{4,8,16,32\}$ with $p\in\{2,3,5\}$ are to be enumerated; each depth‑$d$ ray is mapped to the rational midpoint of its shadow interval, and the resulting finite decimal strings are compared to decimal expansions of benchmark computable reals. The test of C1 is whether every benchmark real’s expansion is matched by some ray sequence; the test of C2’s converse—whether ray sequences exist whose limits are not limit‑definable—cannot be decided finitistically and is flagged as such. No numerical outcome of this protocol is reported because it has not been run.

### 3.6 Method of analysis

We do not simulate; we derive. All quantitative claims in Section 4 follow from stated inputs: the countability of finite programs, the Farey counting function for rationals, and exact enumerations of binary‑tree paths at finite depth. Each derivation shows its inputs, formula, and arithmetic.

## 4. Analysis

### 4.1 Input numbers and their sources

- $I_{1}$: The number of binary strings of length exactly $k$ is $2^{k}$ (combinatorial identity; the tree $T_{2}$ has $2^{k}$ nodes at depth $k$).
- $I_{2}$: The number of reduced fractions in $[0,1]$ with denominator at most $n$ is $|F_{n}|=1+\sum_{k=1}^{n}\varphi(k)$, where $F_{n}$ is the Farey sequence of order $n$ and $\varphi$ is Euler’s totient (standard Farey identity).
- $I_{3}$: Euler’s totient values for $k=1,\ldots,20$:
  $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$, $\varphi(11)=10$, $\varphi(12)=4$, $\varphi(13)=12$, $\varphi(14)=6$, $\varphi(15)=8$, $\varphi(16)=8$, $\varphi(17)=16$, $\varphi(18)=6$, $\varphi(19)=18$, $\varphi(20)=8$.
- $I_{4}$: The number of binary programs of length at most $100$ is $\sum_{k=0}^{100}2^{k}=2^{101}-1$ (geometric sum).
- $I_{5}$: The number of rays of $T_{2}$ at depth $n$ is $2^{n}$ (by $I_{1}$).

### 4.2 Farey count at depth $n=20$: the $129$ figure

**Step 1 (sum the totients).** Grouping the values of $I_{3}$:
$$
\sum_{k=1}^{6}\varphi(k)=1+1+2+2+4+2=12,
$$
$$
\sum_{k=7}^{10}\varphi(k)=6+4+6+4=20,\qquad 12+20=32,
$$
$$
\sum_{k=11}^{14}\varphi(k)=10+4+12+6=32,\qquad 32+32=64,
$$
$$
\sum_{k=15}^{18}\varphi(k)=8+8+16+6=38,\qquad 64+38=102,
$$
$$
\sum_{k=19}^{20}\varphi(k)=18+8=26,\qquad 102+26=128.
$$
Thus $\displaystyle\sum_{k=1}^{20}\varphi(k)=128$.

**Step 2 (Farey cardinality).** By $I_{2}$,
$$
|F_{20}|=1+\sum_{k=1}^{20}\varphi(k)=1+128=129.
$$

**Step 3 (definable fraction at depth 20).** By $I_{5}$, the depth‑$20$ binary tree has $2^{20}=1{,}048{,}576$ rays. Identifying each depth‑$20$ ray with the rational midpoint of its shadow interval, the definable rational shadows number $129$, so
$$
f_{20}=\frac{129}{2^{20}}=\frac{129}{1{,}048{,}576}=1.23024\times10^{-4}.
$$

### 4.3 Program count and the measure‑zero derivation

**Step 1 (program count).** By $I_{4}$,
$$
2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751.
$$
Verification: $2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376$, doubling gives $2^{101}=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,752$, subtracting $1$ yields the stated value.

**Step 2 (countability of computable shadows).** Every computable shadow (Definition 3.4) is determined by a finite program, and there are at most $2^{101}-1$ programs of length at most $100$; hence $\mathbb{R}_{\mathrm{comp}}[0,1]$ is countable.

**Step 3 (measure zero).** Cover the $j$‑th computable shadow $x_{j}$ by an interval of radius $\varepsilon\,2^{-j-1}$, $j=1,2,\ldots$ The total length is
$$
\sum_{j=1}^{\infty}2\varepsilon\,2^{-j-1}
=\varepsilon\sum_{j=1}^{\infty}2^{-j}
=\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary, $\mathbb{R}_{\mathrm{comp}}[0,1]$ has Lebesgue measure $0$ in $[0,1]$, and the artifact set $A$ has measure $1$.

### 4.4 Exponential decay of the definable fraction

At depth $n$ the definable fraction satisfies
$$
f_{n}=\frac{|F_{n}|}{2^{n}}=\frac{1+\sum_{k=1}^{n}\varphi(k)}{2^{n}}
\le\frac{1+n^{2}}{2^{n}},
$$
using the crude bound $\varphi(k)\le k$, so $\sum_{k=1}^{n}\varphi(k)\le n^{2}$ for $n\ge1$. Because $2^{n}$ grows exponentially while $1+n^{2}$ grows polynomially, $f_{n}\to0$ as $n\to\infty$. For $n=20$, the bound gives $(1+400)/2^{20}=401/1{,}048{,}576\approx3.82423\times10^{-4}$, consistent with the exact $1.23024\times10^{-4}$.

### 4.5 Regular‑tree convention counts

Under the $(p+1)$‑regular presentation (second convention in Definition 3.2), the number of rays of length $n$ from a fixed root‑adjacent edge is $p\,(p+1)^{\,n-1}$ for $n\ge1$. For $p=2$:
\[
\begin{aligned}
n=4 &: \;2\cdot3^{3}=54,\\
n=8 &: \;2\cdot3^{7}=4\,374,\\
n=16&: \;2\cdot3^{15}=28\,697\,814,\\
n=32&: \;2\cdot3^{31}=1\,235\,346\,792\,567\,894.
\end{aligned}
\]

### 4.6 Cross‑convention comparison: depth‑20 rationals versus length‑100 programs

The two pools of finitely specifiable objects differ by roughly twenty‑five orders of magnitude. Their ratio is
$$
\rho=\frac{129}{2^{101}-1}
=\frac{129}{2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751}
\approx5.088\times10^{-29}.
$$

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

- **R1.** $\displaystyle\sum_{k=1}^{20}\varphi(k)=128$ and $|F_{20}|=129$ (Section 4.2).
- **R2.** At depth $n=20$ the definable fraction is $f_{20}=1.23024\times10^{-4}$ (Section 4.2).
- **R3.** The number of programs of length at most $100$ is $2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751$ (Section 4.3).
- **R4.** $\mathbb{R}_{\mathrm{comp}}[0,1]$ has Lebesgue measure $0$ and the artifact set $A$ has measure $1$ (Section 4.3).
- **R5.** The definable fraction satisfies $f_{n}\le(1+n^{2})/2^{n}$ and decays exponentially; at $n=20$ the bound is $\approx3.82423\times10^{-4}$ (Section 4.4).
- **R6.** Regular‑tree ray counts under the $(p+1)$‑regular convention for $p=2$ are $54$, $4\,374$, $28\,697\,814$, $1\,235\,346\,792\,567\,894$ at depths $4$, $8$, $16$, $32$ respectively (Section 4.5).
- **R7.** The ratio between the depth‑$20$ rational pool and the length‑$100$ program pool is $\rho\approx5.088\times10^{-29}$ (Section 4.6).

**Projection (labeled, not computed).** If the simulation protocol of Section 3.5 were run, we project that benchmark computable reals would be matched by ray sequences at all tested depths (C1), with uncertainty: a failure at any depth would falsify C1 as stated. No numerical outcome is claimed.



The derivations above demonstrate that, within the formalism built from a single distinction operator, the set of computable shadows is countable and therefore of Lebesgue measure zero, while the artifact set occupies full measure on the unit interval. The explicit finite‑depth counts show that even at modest depths the proportion of definable rational shadows is vanishingly small, and that the combinatorial explosion of binary programs far exceeds the number of rational shadows obtainable from a depth‑20 tree. These quantitative facts give substance to the qualitative claim that the non‑computable reals arise as a projection artifact of the Monna‑map. The conjectures C1 (generation) and C2 (projection) remain unproved; the analysis supplies concrete falsification conditions (Section 6) and a concrete simulation protocol (Section 3.5) that would test C1. The framework therefore bridges a philosophical stance on the nature of the continuum with concrete, verifiable mathematics.

---

## 8. Discussion

The derivations in Sections 4 and 5 establish three quantitative facts: (i) the set of computable shadows in $[0,1]$ is countable and therefore of Lebesgue measure $0$; (ii) at depth $20$ only $129$ reduced rationals are definable among $2^{20}=1{,}048{,}576$ binary‑tree rays, yielding a definable fraction $f_{20}=1.23024\times10^{-4}$; and (iii) the number of binary programs of length at most $100$ is $2^{101}-1=2\,535\,301\,200\,456\,458\,802\,993\,406\,410\,751$.  These facts give concrete substance to the qualitative claim that the non‑computable reals arise as a projection artifact of the Monna‑map.  The discussion below examines the scope of these results, their limitations, and the conditions under which the central conjectures would be falsified.

### 6.1 Limitations

| Limitation | Source | Impact |
|------------|--------|--------|
| **C2 remains conjectural** – the surjectivity and non‑injectivity of the Monna‑map with respect to non‑computable points is assumed, not proved. | C2 (Section 3.4) | All statements about “artifacts” depend on this unproved property. |
| **Choice of binary tree $T_{2}$** – counts of rays and definable fractions are tied to the binary branching convention; alternative presentations (e.g. the $(p+1)$‑regular tree) give different ray counts (Section 4.5). | Definition 3.2, Section 4.5 | Quantitative fractions $f_{n}$ are specific to $T_{2}$ and do not generalize automatically. |
| **Measure‑zero argument is substrate‑free** – the covering proof in Section 4.3 does not use the tree at all; it holds for any countable set of computable shadows. | Section 4.3, Step 3 | The novelty of the framework lies in the reinterpretation, not in a new mathematical theorem. |
| **Dyadic ambiguity** – dyadic rationals have two binary expansions; the convention “choose the terminating expansion” is adopted without proof that it does not affect the counts. | Definition 3.3 | May alter the exact number of definable shadows at a given depth by at most a constant factor. |
| **No empirical validation** – the simulation protocol of Section 3.5 is proposed but not executed; therefore the generation conjecture C1 lacks experimental support. | Section 3.5 | The framework remains purely analytical. |

### 6.2 Failure modes

1. **Existence of a finite or limit‑definable pre‑image for a non‑computable real.**  If a point $x\in[0,1]\setminus\mathbb{R}_{\mathrm{comp}}$ can be generated by a finite program or by a computable limit of tree rays, C2 fails and the artifact interpretation collapses.  
2. **Non‑surjectivity of the Monna‑map.**  Proving that some $y\in[0,1]$ is not in the image of $\mu$ would contradict the surjectivity half of C2 and invalidate the claim that every real is either a computable shadow or an artifact.  
3. **Simulation protocol mismatch.**  If a benchmark computable real (e.g. the binary expansion of $\pi$ truncated to $12$ bits) is not matched by any depth‑$d$ ray for all $d$ examined, C1 would be falsified.  

These three failure modes constitute explicit falsification conditions (see Section 6.3).

### 6.3 Against ourselves

The strongest objection is that the measure‑zero result (R4) is a classical theorem independent of any discrete substrate; consequently the projection‑artifact narrative may be viewed as a metaphor rather than a substantive scientific advance.  Moreover, the binary‑expansion map $\mu$ is a standard identification between $\partial T_{2}$ and $[0,1]$; calling it a “lossy projection” adds interpretive language without altering its mathematical properties.  Finally, the exponential decay of $f_{n}$ follows from a crude bound $\varphi(k)\le k$ and does not capture finer number‑theoretic structure that could affect the rate of decay.

### 6.4 Falsification conditions (formal)

- **(F1) Counterexample to C2.**  Exhibit $x\in[0,1]\setminus\mathbb{R}_{\mathrm{comp}}$ together with a finite program $p$ such that $\mu(\text{path}(p))=x$.  
- **(F2) Non‑surjectivity proof.**  Show $\exists y\in[0,1]$ with no binary sequence $b\in\partial T_{2}$ satisfying $\mu(b)=y$.  
- **(F3) Simulation failure.**  Run the protocol of Section 3.5; if a chosen computable benchmark is not reproduced by any ray at depths $d\in\{4,8,16,32\}$, C1 is falsified.  

### 6.5 Relation to prior work

The artifact analogy is supported by empirical observations of up‑sampling artifacts in generative models [1, 4], which demonstrate that a discrete‑to‑continuous projection can introduce systematic features absent from the source.  The projection‑theoretic perspective on subobject ranges echoes the operator‑algebra literature on bicontractive and completely contractive projections [6], showing that questions of “what survives a projection” have deep mathematical precedents.  Finally, the distinction‑based construction of number systems follows the QNFO program on the computable real boundary [8] and the physical irrelevance of uncountability [9], with the Bruhat–Tits spacetime derivation of [10] supplying the geometric side, situating the present work within an established foundational framework.

## 7. Practical Implications and Engineering Pathways

### (a) Potential users and decision impact  

* **Theoretical physicists** working on discrete‑to‑continuous models of spacetime could use the result to justify restricting their formalism to computable structures without loss of predictive power, because any additional non‑computable points would be artifacts of the projection and have no discrete pre‑image.  
* **Numerical analysts** designing algorithms for continuum problems can interpret the measure‑zero result as a formal guarantee that any finite‑precision computation necessarily operates within the computable shadow set, so algorithmic error analysis need not account for non‑computable contributions.  
* **Philosophers of mathematics** may adopt the projection‑artifact view as a concrete illustration that the uncountable remainder of $\mathbb{R}$ does not correspond to any constructible substrate, influencing debates on the ontological status of the continuum.

If the conjecture C2 holds, design decisions that currently assume the existence of “generic” real numbers (e.g., in stochastic modeling) could be revised to explicitly generate only computable samples, simplifying implementation and eliminating the need for abstract non‑computable assumptions.

### (b) Technology Readiness Level  

The present work is a purely analytical derivation that has not undergone peer review; according to NASA’s definitions this places the result at **TRL 2** (technology concept formulation). No hardware, software prototype, or experimental validation has been performed.

### (c) Smallest next experiment  

A minimal pilot to de‑risk C1 would consist of the following steps:

1. **Select a benchmark computable real** (e.g., $\pi$ truncated to 30 binary digits).  
2. **Enumerate all binary rays** of depth $d=12$ in $T_{2}$ (there are $2^{12}=4096$ rays).  
3. **Map each ray** to its binary‑expansion prefix via the Monna‑map and compare the resulting prefix to the benchmark.  

*Measured outcome:* If the benchmark’s 12‑bit prefix appears among the mapped rays, the test supports C1 at depth 12.  
*Falsification:* Failure to find the prefix for any depth $d\le12$ would falsify C1 for that depth, indicating that the tree does not generate the benchmark computable real at the examined resolution.

### (d) Engineering and deployment constraints  

* **Enumeration complexity:** The number of rays grows as $2^{d}$; even modest depths quickly exceed feasible enumeration on standard hardware.  
* **Memory limits:** Storing all $2^{d}$ binary strings requires $d\cdot2^{d}$ bits of memory; for $d=20$ this is $\approx$ 20 MiB, acceptable, but $d=30$ would need $\approx$ 30 GiB.  
* **Precision of mapping:** The Monna‑map is exact for binary expansions; however, dyadic rationals have two representations, requiring a convention (choose the terminating expansion).  
* **Algorithmic representation of programs:** Counting programs assumes a uniform binary encoding; alternative instruction sets would alter $I_{4}$ and must be specified before any quantitative projection.

These constraints are derived directly from the combinatorial counts in Section 4 and therefore bound any implementation of the simulation protocol.

### (e) Projected cost and performance (projection)  

Assuming a modest workstation with 32 GB RAM and a single CPU core capable of $10^{9}$ operations per second, enumerating all rays up to depth $d=20$ (Section 4.2) would require:

* **Time estimate:** $2^{20}=1{,}048{,}576$ iterations; at $10^{6}$ iterations s\(^{-1}\) (including mapping and comparison) the runtime is $\approx$ 1.05 s.  
* **Energy estimate:** Power draw $\approx$ 100 W, yielding $\approx$ 0.03 Wh for the task.  

These figures are **projections** based on the arithmetic inputs $I_{5}=2^{n}$ and the assumed processing rate; actual values will vary with hardware.

### (f) Direct risks or misuse paths  

If the projection‑artifact interpretation were taken to claim that *all* non‑computable reals are physically irrelevant, there is a risk of overlooking mathematical constructions that deliberately require non‑computable objects (e.g., certain existence proofs in analysis). Misapplication could lead to unjustified simplifications in models where non‑computable parameters are introduced as idealizations. The paper explicitly frames the claim as a conjectural reinterpretation, not as a blanket dismissal of non‑computable mathematics.

---

## 10. Conclusion

We have presented a self‑contained formal analysis of the conjecture that the continuum emerges as a projection artifact of a discrete Bruhat–Tits tree. By grounding the argument in explicit combinatorial counts—Farey sequences, binary‑program enumeration, and regular‑tree ray counts—we derived that the computable shadows form a countable, measure‑zero subset of $[0,1]$, while the artifact set occupies full Lebesgue measure. The quantitative results (exact counts, definable fractions, exponential decay) give concrete substance to the otherwise philosophical claim that non‑computable reals are generated by the lossy Monna‑map projection.  

The work clarifies which parts of the thesis are proven (measure‑zero of computable shadows) and which remain conjectural (the surjectivity and non‑injectivity of the projection with respect to non‑computable reals). It also supplies a clear falsification protocol and a practical pathway for experimental verification. Future research can extend the analysis to alternative tree conventions, explore richer projection maps, and integrate the framework into discrete models of spacetime.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 8. length 3835 -> 4665 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Upsampling artifacts in neural audio synthesis. arXiv:2010.14356v2. https://arxiv.org/abs/2010.14356v2
[3] Mathematical Artifacts Have Politics: The Journey from Examples to Embedded Ethics. arXiv:2308.04871v1. https://arxiv.org/abs/2308.04871v1
[4] Systematic Analysis and Removal of Circular Artifacts for StyleGAN. arXiv:2103.01090v2. https://arxiv.org/abs/2103.01090v2
[5] The Genius Conjectures (via Bell Polynomials). arXiv:2002.03814v1. https://arxiv.org/abs/2002.03814v1
[6] Completely contractive projections on operator algebras. arXiv:1508.01530v2. https://arxiv.org/abs/1508.01530v2
[8] https://papers.qnfo.org/papers/computable-real-boundary. QNFO: The Computable Real Boundary: Where Physics Ends and Cognitive Fiction Begins.
[9] https://papers.qnfo.org/papers/physical-irrelevance-of-uncountability-computable-reals-suffice-for-continuum-ph. QNFO: Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics.
[10] https://papers.qnfo.org/papers/formal-derivation-of-emergent-spacetime. QNFO: Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree.
