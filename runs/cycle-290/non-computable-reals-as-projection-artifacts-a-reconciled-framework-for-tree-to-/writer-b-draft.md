# Non-Computable Reals as Projection Artifacts: A Formal Analysis of Tree-to-Manifold Construction of the Continuum

## Abstract

Continuum physics and analysis are formulated over the completed real line, yet every measurement, record, and computation is finite, and the physical role of the uncountable remainder of $\mathbb{R}$ is unresolved. This paper develops a formal framework for the conjecture that the continuum is constructed rather than primitive: natural numbers, rationals, and computable reals arise from a distinction operator via enclosure operations, while the full real line emerges only through a lossy projection — the Monna-map — of a discrete, non-Archimedean Bruhat–Tits tree onto the Archimedean interval. The specific gap addressed is that the computable/non-computable boundary has been asserted, in prior distinction-based work, to be a projection effect without explicit counts or falsification conditions. We derive, with all arithmetic shown, that the computable reals have Lebesgue measure zero, so the artifact set has full measure in $[0,1]$; that at tree depth $n=20$ exactly $129$ reduced rationals shadow $2^{20}=1{,}048{,}576$ paths, a definable fraction of $1.23024\times 10^{-4}$; that programs of length at most $100$ number $2^{101}-1=2535301200456458802993406410751$; and that the definable fraction decays at least exponentially in depth. The projection thesis itself remains conjectural, with explicit falsification conditions and a proposed but unexecuted enumeration protocol. The framework reinterprets the measure-theoretic dominance of non-computable reals as a projection effect and gives constructive-mathematics-minded physicists a checkable boundary for what the discrete substrate can encode.

## 1. Introduction

Physicists, numerical analysts, and instrument designers work every day with the real line as if it were a completed object: continuum differential equations, spectral theory, and floating-point models all presuppose $\mathbb{R}$. Yet every measurement a laboratory can produce is a finite record, and a finite record cannot encode cardinality; one line of work argues precisely that the uncountability of $\mathbb{R}$, as distinct from its Archimedean completeness, has no physical consequence in a checkable sense [9]. What blocks progress today is conceptual, not instrumental: standard set-theoretic presentation gives no account of *where* the non-computable reals $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ come from or why they dominate $\mathbb{R}$ in measure, and the distinction-based research program that does address this question has so far stated its central claims — that non-computables are artifacts of a projection from a discrete substrate — without explicit counts, derivations, or falsification conditions [7], [8]. If the analysis in this paper holds, the measure-theoretic dominance of non-computable reals becomes a quantified projection effect, analogous to upsampling artifacts in generative synthesis [1], [4], and the boundary between physically meaningful and physically vacuous mathematics acquires a computable test.

The stance taken here follows a Spencer-Brown-style program in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed [8]. In that program, natural numbers arise by iterated enclosure of distinctions, rationals by pairwise enclosure, and computable reals $\mathbb{R}_{\mathrm{comp}}$ by limits of rational procedures [8]. The full continuum $\mathbb{R}$ then emerges only at a final step: a projection of a discrete, non-Archimedean structure onto a smooth Archimedean manifold. The discrete side is a Bruhat–Tits tree, an infinite non-Archimedean object in which closeness is measured by a valuation rather than an Archimedean metric; prior work has argued that macroscopic spacetime itself can be derived from the discrete properties of such a tree, with an Archimedean projection yielding continuous real coordinates [10]. The projection — which we call the Monna-map, following the prior framework [7] — is lossy: many distinct tree paths map to the same Archimedean point, and the points with no finitely specifiable discrete preimage are, on the conjecture analyzed here, created by the map rather than discovered in the tree. We call these points **artifacts**, in the same sense in which upsampling a signal can create features that exist in the output format but not in the source data [1], [4].

This reframing has two payoffs. First, it re-derives the computable/constructive hierarchy from pure distinction logic: the boundary between $\mathbb{R}_{\mathrm{comp}}$ and $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ becomes the boundary between what the discrete tree can finitely encode and what only the projection produces. Second, it gives a quantitative skeleton to the position that non-computable "breadth" is physically vacuous [7], [9]: everything the discrete side finitely encodes occupies Lebesgue measure zero of the shadow, so a uniformly random point of $[0,1]$ is an artifact with probability $1$ — conditional on the projection conjecture.

Our contributions are:

- Precise definitions of the distinction operator, the enclosure hierarchy, the valuation tree, and the Monna-map projection, with three conjectures stated with explicit status (Section 3).
- Explicit derivations, with all arithmetic shown, that the computable reals have Lebesgue measure zero and the artifact set full measure; that the Farey count of depth-$20$ rational shadows is exactly $129$ against $2^{20}=1{,}048{,}576$ paths; that programs of length at most $100$ number $2^{101}-1$; and that the definable fraction decays exponentially in depth (Section 4).
- Results and labeled projections, including a new comparison of depth-$20$ rationals against the length-$100$ program pool (Section 5).
- Limitations, failure modes, falsification conditions, and a practical pathway with readiness assessment and a smallest next test (Sections 6–7).

## 2. Background and Related Work

We organize the related work into four strands: artifacts of lossy representation, the artifact concept beyond engineering, alternative constructions of the reals and their physical status, and distinction-based foundations and projection theory.

**Artifacts of lossy representation.** Biswas and Paris report that upsampling layers in neural audio synthesis introduce undesired artifacts, that in computer vision such artifacts are studied as checkerboard artifacts, and that their effect had been overlooked in audio processing; their survey distinguishes three upsampler families — transposed convolutions, interpolation upsamplers, and subpixel convolutions — and shows that transposed convolutions introduce tonal artifacts through weight initialization, overlap issues, and the loss function, with the no-overlap, partial-overlap, and full-overlap cases each producing distinct artifact regimes [1]. This is the closest methodological analogue to our thesis: a change of representational substrate from discrete samples to a continuous percept creates features that exist only in the output format. In the image domain, vanilla StyleGAN synthesizes high-resolution, hyper-realistic face images that sometimes contain prominent circular artifacts which severely degrade quality; one work provides a systematic investigation of how those circular artifacts arise, finding that they are due to the selective escalation of activation magnitudes promoted by the StyleGAN architecture, with instance-normalization effects compounded through the progressive structure, and proposes a simple removal solution without excessive quality loss [4]. Together, [1] and [4] support the general principle we invoke: when a generator projects internal discrete structure onto a continuous output manifold, the projection itself can be the source of structured, systematic defects. Our claim is that $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ is exactly such a systematic defect of the tree-to-manifold projection.

**The artifact concept beyond engineering.** The notion that artifacts are not mere noise but carry structural consequences has been argued within mathematics itself: one essay extends Langdon Winner's idea that artifacts have politics into mathematics, first providing examples showing that mathematical artifacts with politics exist, then arguing that all mathematical artifacts have politics, with implications for embedding ethics into mathematical curricula [3]. Whatever one makes of the normative thesis, its descriptive core — that mathematical objects can be artifacts of the machinery that produces them, with real consequences — is precisely the ontology we assign to non-computable reals. On the practical side, the reproducibility literature argues that the pursuit of scientific knowledge strongly depends on the ability to reproduce and validate research results, that the scientific community faces challenges of transparency, reliability, and reproducibility of empirical published results, and that consequently the design and preparation of reproducible artifacts has a fundamental role in the development of science [2]; we adopt the corresponding methodological demand that every construction in this paper be reproducible from explicitly stated finite data — which is exactly the definition of computability.

**Alternative constructions and the physical status of the reals.** In classical analysis, fractional calculus is reviewed as applied to continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the Basset problem of unsteady motion of a particle in a viscous fluid [5]; we cite it as a precedent for continuum descriptions that employ operators not reducible to pointwise classical operations, i.e., continuum apparatus presupposing richer structure than the discrete one — the direction of our projection. In combinatorics, two related conjectures arising from $i$-matchings in random $r$-regular bipartite graphs involve only basic properties of convergent power series, one formulation involving Bell polynomials; the authors state they earnestly believe only a truly genius mathematician will prove them and advise others not to try [6]. We cite [6] as a cautionary register: our central conjectures are easy to state and may be hard to prove, and we flag which of our claims are derived and which remain conjecture. On the physical side, the record-bound analysis of experimental outcomes shows that an instrument measuring a single quantity over range $L$ with resolution $\delta$ produces at most $N=\lfloor L/\delta\rfloor$ distinguishable outcomes, and works the example $L=1\,\mathrm{m}$, $\delta=10^{-18}\,\mathrm{m}$, giving $N=10^{18}$ and $\log_{2}N\approx 59.79$ bits, concluding that even this extreme measurement distinguishes fewer than $2^{60}$ outcomes [9]. That bound is the operational reason the computable/non-computable boundary can be crossed by no experiment, and it motivates treating the artifact set as a projection effect rather than a physical resource.

**Projection theory.** In operator algebra, a substantial literature studies projections on $C^{*}$-algebras and their ranges; one paper's main goal is to find operator-algebra variants of deep results of Størmer, Friedman and Russo, Choi and Effros, Effros and Størmer, Robertson and Youngson, and Youngson, investigating in particular the bicontractive projection problem, and it proves structural results such as that a completely contractive projection on an operator algebra picks out a largest approximately unital subalgebra forming a hereditary subalgebra [6]. This establishes that "which subobjects survive a projection, and what the projection's range looks like" is a mathematically deep question with a developed theory; our Monna-map question — is the image all of $\mathbb{R}$, and what does the range miss? — is a set-theoretic and measure-theoretic instance of the same genre.

**Distinction-based foundations and the prior framework.** The Laws of Form calculus of Spencer-Brown, as formalized in recent work, is built from two primitive gestures — the mark, the act of indicating, and enclosure, the boundary created by a distinction — governed by two reduction rules, Calling (two identical indications collapse to one) and Crossing (a distinction that enters and exits its own boundary cancels); that work then constructs the number systems from these primitives by a finite sequence of enclosure operations, in which drawing a distinction once yields the number $1$, iterated Calling yields $\mathbb{N}$, nested enclosures for ratios yield $\mathbb{Q}$, and the fixed point of re-entry under finite enclosure operations is exactly $\mathbb{R}_{\mathrm{comp}}$, with everything beyond it classified as Cognitive Fiction — internally consistent but externally unverifiable [8]. Our distinction operator and enclosure hierarchy are a direct formalization of these primitives, and our artifact set is a measure-theoretic sharpening of the Cognitive Fiction category. The prior reconciled framework paper states the same three conjectures analyzed here — generation, projection, and dominance — and reports the counts we re-derive and extend: $|F_{20}|=129$, $f_{20}=129/2^{20}\approx 1.23024\times 10^{-4}$, $2^{101}-1=2535301200456458802993406410751$, measure zero for computable shadows, and the exponential bound $f_{n}\le(1+n^{2})/2^{n}$; it also records, in its divergence report, that the claim that the projection is *proved* to add exactly $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ was rejected in favor of the conjectural reading, and that its Monna-map is the ordinary binary-expansion map, a framing choice with no canonical status [7]. We build directly on that framework: our Section 4 re-derives its counts from stated inputs, corrects nothing in them, and adds a new comparison (Section 4.6) between the depth-$20$ rational pool and the length-$100$ program pool that the prior paper explicitly flags as two different notions of "definable" that must not be conflated [7]. Finally, the spacetime-derivation program shows that the Bruhat–Tits tree can serve as a fundamental discrete geometry from which an adjacency operator acts as an effective Hamiltonian, epistemic time emerges by coarse-graining, and an Archimedean projection yields continuous real coordinates [10]; we use that program as evidence that the tree-to-Archimedean passage is a live, worked-out direction, of which our Monna-map is the one-dimensional, number-theoretic instance.

## 3. Methods

### 3.1 The distinction operator and enclosure hierarchy

Following the Laws of Form calculus [8], we take as primitive the act of drawing a distinction. Formally, fix a two-value form $V_{2}=\{0,1\}$ and let the distinction operator $\delta$ be a map that, applied to an unmarked space, produces a marked and an unmarked region. Iterated application generates a rooted branching structure; the reduction rules of Calling and Crossing ensure that repeated identical distinctions do not create new objects [8].

**Definition 3.1 (Enclosure hierarchy).** Define inductively: $E_{0}=\{\varnothing\}$, the undifferentiated space; $E_{k+1}=\mathcal{P}_{\mathrm{fin}}(E_{k})$, the finite enclosures of level-$k$ objects. Level-$1$ objects correspond to single distinctions; finite multisets of level-$1$ distinctions, ordered by iteration, yield the natural numbers $\mathbb{N}$, matching the number-builder sequence in which one distinction yields $1$ and iterated Calling yields $\mathbb{N}$ [8]. Pairwise enclosure of naturals with an orientation yields the integers $\mathbb{Z}$, and the rationals $\mathbb{Q}$ arise as ordered pairs $(a,b)$ with $b\neq 0$, $b\in\mathbb{N}$, modulo $(a_{1},b_{1})\sim(a_{2},b_{2})$ iff $a_{1}b_{2}=a_{2}b_{1}$. Every element of this hierarchy is finitely specifiable: a finite syntactic object built by $\delta$ and enclosure.

### 3.2 The discrete side: valuation trees

**Definition 3.2 (Valuation tree).** Fix a prime $p$ and let $T_{p}$ be the rooted tree whose vertices at level $n$ correspond to residue classes modulo $p^{n+1}$, each vertex having $p$ children; this is the Bruhat–Tits tree of $\mathbb{Q}_{p}$ in its standard combinatorial presentation. A path from the root is an element of the boundary $\partial T_{p}$, which carries an ultrametric $d_{p}$ induced by the $p$-adic valuation $v_{p}$. For concreteness and computability of all counts we work primarily with the binary tree $T_{2}$ ($p=2$), whose boundary $\partial T_{2}$ is in bijection with infinite binary sequences. A second convention — the $(p+1)$-regular presentation of the Bruhat–Tits tree of $\mathrm{PGL}_{2}$ over $\mathbb{Q}_{p}$, in which every vertex has $p+1$ neighbors — is used in Section 4.5 for the regular-tree counts and is explicitly labeled as a separate convention.

### 3.3 The Monna-map projection

**Definition 3.3 (Monna-map).** The Monna-map is the projection
$$\mu:\partial T_{2}\to[0,1],\qquad \mu\big((b_{1},b_{2},b_{3},\ldots)\big)=\sum_{k=1}^{\infty}b_{k}\,2^{-k},$$
i.e., the standard binary-expansion identification of the Cantor-set boundary with the unit interval. The tree carries the ultrametric $d_{2}$; the interval carries the Euclidean metric $d_{\infty}(x,y)=|x-y|$. The map $\mu$ is continuous from the ultrametric topology onto the Euclidean topology, is many-to-one exactly on the dyadic rationals (which have two expansions), and collapses all ultrametric structure. As the prior framework notes, this is the ordinary binary-expansion map and the framing as a tree projection is a choice, not a canonical identification [7]; nothing derived below depends on a canonical choice.

**Definition 3.4 (Computable shadow, artifact set).** A point $x\in[0,1]$ is a *computable shadow* if there is a finite program that, given $n$, outputs the first $n$ bits of a binary expansion of $x$. Let $\mathbb{R}_{\mathrm{comp}}[0,1]$ denote the set of computable shadows. The *artifact set* is
$$A=[0,1]\setminus\mathbb{R}_{\mathrm{comp}}[0,1].$$

### 3.4 Conjectures

- **C1 (Generation).** $\mathbb{N}$, $\mathbb{Q}$, and $\mathbb{R}_{\mathrm{comp}}$ arise from the distinction operator by enclosure operations; each computable real corresponds to a finite or limit-definable tree path.
- **C2 (Projection).** The Monna-map is surjective and non-injective, and points of $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ have no finite or limit-definable preimage: they are artifacts, created by $\mu$ rather than discovered in $\partial T_{2}$.
- **C3 (Dominance).** The artifact set has full Lebesgue measure in $[0,1]$.

C3 is *derived conditionally* in Section 4 from the countability of finite programs plus the standard covering argument; its interpretation as "projection dominance" depends on C2, which remains a conjecture. We do not claim, as one formulation recorded in the prior framework's divergence report did, that the projection is *proved* to add precisely $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$; that stronger claim is treated here as conjectural, following the reconciliation in [7].

### 3.5 Simulation protocol (proposed, not executed)

Finite-depth trees of depths $d\in\{4,8,16,32\}$ with $p\in\{2,3,5\}$ are to be enumerated; each depth-$d$ ray is mapped to the rational midpoint of its shadow interval; the resulting finite decimal strings are compared to decimal expansions of benchmark computable reals. The test of C1 is whether every benchmark real's expansion is matched by some ray sequence; the test of C2's converse — whether ray sequences exist whose limits are not limit-definable — cannot be decided finitistically and is flagged as such. No numerical outcome of this protocol is reported in this paper because it has not been run.

### 3.6 Method of analysis

We do not simulate; we derive. All quantitative claims in Section 4 follow from stated inputs: the countability of finite programs, the Farey counting function for rationals, and exact enumerations of binary-tree paths at finite depth. Each derivation shows its inputs, formula, and arithmetic.

## 4. Analysis

### 4.1 Input numbers and their sources

- $I_{1}$: The number of binary strings of length exactly $k$ is $2^{k}$ (combinatorial identity; the tree $T_{2}$ has $2^{k}$ nodes at depth $k$).
- $I_{2}$: The number of reduced fractions in $[0,1]$ with denominator at most $n$ is $|F_{n}|=1+\sum_{k=1}^{n}\varphi(k)$, where $F_{n}$ is the Farey sequence of order $n$ and $\varphi$ is Euler's totient (standard Farey identity: each fraction $a/k$ with $\gcd(a,k)=1$, $0\le a\le k$, contributes, and $\varphi(k)$ counts them for each $k$, plus the endpoint $0/1$).
- $I_{3}$: Euler's totient values for $k=1,\ldots,20$, each computed as the count of integers in $[1,k]$ coprime to $k$ (e.g., coprime to $10$ are $1,3,7,9$, so $\varphi(10)=4$): $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$, $\varphi(11)=10$, $\varphi(12)=4$, $\varphi(13)=12$, $\varphi(14)=6$, $\varphi(15)=8$, $\varphi(16)=8$, $\varphi(17)=16$, $\varphi(18)=6$, $\varphi(19)=18$, $\varphi(20)=8$.
- $I_{4}$: The number of binary programs of length at most $100$ is $\sum_{k=0}^{100}2^{k}=2^{101}-1$ (geometric sum; each length-$k$ binary string is one program, and there are $2^{k}$ of them).
- $I_{5}$: The number of rays of $T_{2}$ at depth $n$ is $2^{n}$ (by $I_{1}$, one string per ray prefix).

### 4.2 Farey count at depth $n=20$: the $129$ figure

Step 1 (sum the totients). Grouping the values of $I_{3}$:
$$\sum_{k=1}^{6}\varphi(k)=1+1+2+2+4+2=12,$$
$$\sum_{k=7}^{10}\varphi(k)=6+4+6+4=20,\qquad 12+20=32,$$
$$\sum_{k=11}^{14}\varphi(k)=10+4+12+6=32,\qquad 32+32=64,$$
$$\sum_{k=15}^{18}\varphi(k)=8+8+16+6=38,\qquad 64+38=102,$$
$$\sum_{k=19}^{20}\varphi(k)=18+8=26,\qquad 102+26=128.$$
So $\sum_{k=1}^{20}\varphi(k)=128$.

Step 2 (Farey cardinality). By $I_{2}$, the Farey sequence $F_{20}$ of order $20$ has
$$|F_{20}|=1+\sum_{k=1}^{20}\varphi(k)=1+128=129,$$
where the leading $1$ accounts for the endpoint $0/1$ and the summand $\varphi(k)$ counts, for each denominator $k\le 20$, the reduced fractions $a/k$ with $0\le a\le k$, $\gcd(a,k)=1$ (this includes $1/1$ via $\varphi(1)=1$). Thus exactly $129$ reduced rationals in $[0,1]$ have denominator at most $20$.

Step 3 (definable fraction at depth $20$). By $I_{5}$, the depth-$20$ binary tree has $2^{20}=1{,}048{,}576$ rays. Identifying each depth-$20$ ray with the rational midpoint of its shadow interval, the definable rational shadows at depth $20$ number $129$, so the definable fraction is
$$f_{20}=\frac{129}{2^{20}}=\frac{129}{1{,}048{,}576}.$$
Arithmetic: $129/1{,}048{,}576=0.00012302398681640625$ exactly (since $1{,}048{,}576=2^{20}$ and $129/2^{20}$ is a dyadic rational), i.e., $f_{20}=1.23024\times 10^{-4}$ to six significant figures; check: $1{,}048{,}576\times 1.23024\times 10^{-4}=129.0000\ldots$

### 4.3 Program count and the measure-zero derivation

Step 1 (program count). By $I_{4}$,
$$2^{101}-1=2535301200456458802993406410751,$$
verified digit-wise: $2^{100}=1267650600228229401496703205376$, so $2^{101}=2\times 2^{100}=2535301200456458802993406410752$, and subtracting $1$ gives the stated value ending in $0751$.

Step 2 (countability of computable shadows). Every computable shadow (Definition 3.4) is determined by a finite program, and there are at most $2^{101}-1$ programs of length at most $100$; hence $\mathbb{R}_{\mathrm{comp}}[0,1]$ is countable, being a subset of a countable union of finite sets over all length bounds.

Step 3 (measure zero). Cover the $j$-th computable shadow $x_{j}$ by an interval of radius $\varepsilon\,2^{-j-1}$, $j=1,2,\ldots$ The total length is
$$\sum_{j=1}^{\infty}2\varepsilon\,2^{-j-1}=\varepsilon\sum_{j=1}^{\infty}2^{-j}=\varepsilon,$$
using $\sum_{j=1}^{\infty}2^{-j}=1$. Since $\varepsilon>0$ is arbitrary, $\mathbb{R}_{\mathrm{comp}}[0,1]$ has Lebesgue measure $0$ in $[0,1]$, and the artifact set $A=[0,1]\setminus\mathbb{R}_{\mathrm{comp}}[0,1]$ has measure $1-0=1$: full measure. This derives C3 conditionally on the standard covering argument; it does not by itself derive C2.

### 4.4 Exponential decay of the definable fraction

At depth $n$ the definable fraction is bounded as
$$f_{n}=\frac{|F_{n}|}{2^{n}}=\frac{1+\sum_{k=1}^{n}\varphi(k)}{2^{n}}\le\frac{1+n^{2}}{2^{n}},$$
using the crude bound $\varphi(k)\le k$, so $\sum_{k=1}^{n}\varphi(k)\le n(n+1)/2\le n^{2}$ for $n\ge 1$. Since $2^{n}$ grows exponentially while $1+n^{2}$ grows polynomially, $f_{n}\to 0$: the definable rational shadows decay exponentially in depth. Check at $n=20$: $(1+400)/2^{20}=401/1{,}048{,}576=0.00038242340087890625\approx 3.82423\times 10^{-4}$, an upper bound consistent with the exact $1.23024\times 10^{-4}$ of Section 4.2.

### 4.5 Regular-tree convention counts

Under the $(p+1)$-regular presentation (Definition 3.2, second convention), the number of rays of length $n$ from a fixed root-adjacent edge is $p\,(p+1)^{n-1}$ for $n\ge 1$. For $p=2$:
$$n=4:\ 2\cdot 3^{3}=2\cdot 27=54;$$
$$n=8:\ 2\cdot 3^{7}=2\cdot 2{,}187=4{,}374;$$
$$n=16:\ 2\cdot 3^{15}=2\cdot 14{,}348{,}907=28{,}697{,}814;$$
$$n=32:\ 2\cdot 3^{31}=2\cdot 617{,}673{,}396{,}283{,}947=1{,}235{,}346{,}792{,}567{,}894.$$
These counts are for the simulation protocol of Section 3.5 and are not empirical results.

### 4.6 Cross-convention comparison: depth-$20$ rationals versus length-$100$ programs

The two pools of finitely specifiable objects measured in Sections 4.2 and 4.3 differ by roughly twenty-five orders of magnitude. The ratio is
$$\rho=\frac{129}{2^{101}-1}=\frac{129}{2535301200456458802993406410751}.$$
Arithmetic: $2^{101}-1\approx 2.5353012\times 10^{30}$, so
$$\rho\approx\frac{129}{2.5353012\times 10^{30}}=\frac{129}{2.5353012}\times 10^{-30}\approx 50.88\times 10^{-30}=5.088\times 10^{-29}.$$
Check: $2.5353012\times 10^{30}\times 5.088\times 10^{-29}\approx 129.0$. So the depth-$20$ rational shadows constitute a