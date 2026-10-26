# Non-Computable Reals as Projection Artifacts: A Reconciled Framework for Tree-to-Manifold Construction of the Continuum

## Abstract

We develop a formal framework for the conjecture that the continuum is constructed rather than primitive: natural numbers, rationals, and computable reals arise from a single distinction operator via enclosure operations, while the full real line emerges only through a lossy projection — the Monna‑map — of a discrete, non‑Archimedean Bruhat–Tits tree onto a smooth Archimedean manifold. The central claim under analysis is that non‑computable reals are not discovered but created by this projection: they are artifacts with no discrete counterpart, analogous to upsampling artifacts in generative signal and image synthesis. We derive with explicit arithmetic that the computable reals form a set of Lebesgue measure zero, so the artifact set has full measure in $[0,1]$, reinterpreting the measure‑theoretic dominance of non‑computables as a projection effect. We quantify the gap between finite‑depth tree approximations and their Archimedean shadows: at depth $n=20$, exactly definable rational shadows number $129$ against $2^{20}=1{,}048{,}576$ paths, a definable fraction of $\approx1.23024\times10^{-4}$; programs of length at most $100$ number $2^{101}-1=2{,}535{,}301{,}200{,}456{,}458{,}802{,}993{,}406{,}410{,}751$. We state conjectures, falsification conditions, a proposed simulation protocol, and reconcile divergent conventions among independent formulations of the framework.

## 1. Introduction

The standard set‑theoretic presentation treats the real line $\mathbb{R}$ as a completed object, with the non‑computable reals $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ as an uncountable majority whose existence is guaranteed by completeness. This paper takes the opposite stance, following a Spencer‑Brown‑style research program in which the act of drawing a distinction is the primitive operation from which logic, mathematics, and physics can be constructed [9]. In that program, natural numbers arise by iterated enclosure of distinctions, rationals by pairwise enclosure, and computable reals $\mathbb{R}_{\mathrm{comp}}$ by limits of rational procedures. The full continuum $\mathbb{R}$ then emerges only at a final step: a projection of a discrete, non‑Archimedean structure onto a smooth Archimedean manifold.

The discrete side is a Bruhat–Tits tree: an infinite, non‑Archimedean object in which closeness is measured by a non‑Archimedean valuation rather than an Archimedean metric. The Archimedean side is the familiar real line. The projection — which we call the Monna‑map, following the corpus terminology [11] — is lossy: many distinct tree paths map to the same Archimedean point, and the points with no finitely specifiable discrete preimage are, on the conjecture analyzed here, created by the map rather than discovered in the tree. We call these points **artifacts**, in the same sense in which upsampling a signal can create features that exist in the output format but not in the source data [1], [5].

This reframing has two payoffs. First, it re‑derives the computable/constructive hierarchy from pure distinction logic: the boundary between $\mathbb{R}_{\mathrm{comp}}$ and $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ becomes the boundary between what the discrete tree can finitely encode and what only the projection produces. Second, it gives a quantitative skeleton to the corpus position that non‑computable “breadth’’ is physically vacuous [10], [11]: everything the discrete side finitely encodes occupies Lebesgue measure zero of the shadow, so a uniformly random point of $[0,1]$ is an artifact with probability $1$ — conditional on the projection conjecture.

Our contributions are: (i) precise definitions of the distinction operator, the enclosure hierarchy, and the Monna‑map projection (Section 3); (ii) explicit derivations, with all arithmetic shown, that the computable reals have Lebesgue measure zero, that the artifact set has full measure, that the density of finitely definable rational shadows among tree paths decays exponentially in depth, and exact finite‑depth tree counts under two stated conventions (Section 4); (iii) results and labeled projections (Section 5); and (iv) limitations, failure modes, falsification conditions, and a divergence report reconciling three independent formulations (Sections 6, Appendices A–B).

## 2. Background and Related Work

We organize the related work into four strands: artifacts of lossy representation, the artifact concept beyond engineering, alternative constructions of the reals, and distinction‑based foundations and projection theory.

**Artifacts of lossy representation.** Biswas and Paris report that upsampling layers in neural audio synthesis introduce undesired artifacts, and that while such artifacts are well studied in computer vision — where they are known as checkerboard artifacts due to their characteristic visual pattern — their effect had been overlooked in audio processing [1]. This is the closest methodological analogue to our thesis: a change of representational substrate from discrete samples to a continuous percept creates features that exist only in the output format. In the image domain, vanilla StyleGAN synthesizes high‑resolution, hyper‑realistic face images, but these sometimes contain prominent circular artifacts which severely degrade the quality of generated images; one work provides a systematic investigation of how those circular artifacts arise and how to remove them [5]. Together, [1] and [5] support the general principle we invoke: when a generator projects internal discrete structure onto a continuous output manifold, the projection itself can be the source of structured, systematic defects. Our claim is that $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ is exactly such a systematic defect of the tree‑to‑manifold projection.

**The artifact concept beyond engineering.** The notion that artifacts are not mere noise but carry structural consequences has been argued within mathematics itself: one paper extends Langdon Winner’s idea that artifacts have politics into mathematics, first providing examples showing that mathematical artifacts with politics exist, then arguing that all mathematical artifacts have politics, with implications for embedding ethics into mathematical curricula [4]. Whatever one makes of the normative thesis, its descriptive core — that mathematical objects can be artifacts of the machinery that produces them, with real consequences — is precisely the ontology we assign to non‑computable reals. On the practical side, the reproducibility literature emphasizes that the design and preparation of reproducible artifacts has a fundamental role in the development of science, given challenges of transparency, reliability, and reproducibility of published empirical results [3]; we adopt the corresponding methodological demand that every construction in this paper be reproducible from explicitly stated finite data — which is exactly the definition of computability.

**Alternative constructions of the reals.** A recent rule‑based definition states that a real number is a rule which says Yes or No based on whether the real number ought to be in a given rational interval; the supplied summary indicates it is a teaser for a fuller formalization under the title “Defining Real Numbers as Oracles” and gives no further technical detail [7]. We therefore use it only as evidence that rule‑based definitions of reals are an active alternative to set‑theoretic completion; structurally, a path in a nested‑enclosure tree is exactly such a Yes/No rule over rational intervals. In classical analysis, fractional calculus is reviewed as applied to continuum and statistical mechanics, including mathematical modelling of viscoelastic bodies and the Basset problem of unsteady motion of a particle in a viscous fluid [2]; we cite it as a precedent for continuum descriptions that employ operators not reducible to pointwise classical operations, i.e., continuum apparatus presupposing richer structure than the discrete one — the direction of our projection. In combinatorics, two related conjectures arising from $i$‑matchings in random $r$‑regular bipartite graphs involve only basic properties of convergent power series, one formulation involving Bell polynomials; the authors state they believe only a truly genius mathematician will prove them and advise others not to try [6]. We cite [6] as a cautionary register: our central conjectures are easy to state and may be hard to prove, and we flag which of our claims are derived and which remain conjecture.

**Projection theory.** In operator algebra, a substantial literature studies projections on $C^{*}$‑algebras and their ranges; one paper’s main goal is to find operator‑algebra variants of deep results of Stormer, Friedman and Russo, Choi and Effros, Effros and Stormer, Robertson and Youngson, and Youngson, investigating in particular the bicontractive projection problem [8]. This establishes that “which subobjects survive a projection, and what the projection’s range looks like’’ is a mathematically deep question with a developed theory; our Monna‑map question — is the image all of $\mathbb{R}$, and what does the range miss? — is a set‑theoretic and measure‑theoretic instance of the same genre. The supplied summary of [8] does not state specific range theorems we could import, so we use it as a structural analogy only.

**Distinction‑based foundations.** Spencer‑Brown’s *Laws of Form* proposed the act of drawing a distinction as the primitive operation from which logic, mathematics, and physics can be constructed; a consolidation synthesizes known quantum correspondences of this program, identifies $7$ open problem categories, and proposes $4$ extensions [9]. Our distinction operator is a direct formalization of this primitive. The QNFO corpus supplies the specific thesis we analyze: that the uncountability of the reals conflates Archimedean completeness (“depth’’) and set‑theoretic cardinality explosion (“breadth’’), with all physically relevant properties preserved by the computable reals alone [10]. A three‑axis framework extends this with Depth (computable reals), Breadth (non‑computable reals, described as physically vacuous), and Valuation ($p$‑adic completions as information carriers), together with falsifiable predications for quantum error correction and gauge structure [11]; in our construction the Bruhat–Tits tree is the Valuation axis made geometric, and the Monna‑map is the passage from Valuation to Depth/Breadth. Finally, the corpus entry “Syntactic Generation’’ [12] carries no substantive summary in the material available to us; we note only that its title suggests a generation‑by‑syntax program consonant with our enclosure hierarchy, and we make no claim about its contents.

## 3. Methods

### 3.1 The distinction operator and enclosure hierarchy

Following [9], we take as primitive the act of drawing a distinction. Formally, fix a two‑value form $V_{2}=\{0,1\}$ and let the distinction operator $\delta$ be a map that, applied to an unmarked space, produces a marked and an unmarked region. Iterated application generates a rooted branching structure.

**Definition 3.1 (Enclosure hierarchy).** Define inductively: $E_{0}=\{\varnothing\}$, the undifferentiated space; $E_{k+1}=\mathcal{P}_{\mathrm{fin}}(E_{k})$, the finite enclosures of level‑$k$ objects. Level‑1 objects correspond to single distinctions; finite multisets of level‑1 distinctions, ordered by iteration, yield the natural numbers $\mathbb{N}$. Pairwise enclosure of naturals with an orientation yields the integers $\mathbb{Z}$, and the rationals $\mathbb{Q}$ arise as ordered pairs $(a,b)$ with $b\neq0$, $b\in\mathbb{N}$, modulo $(a_{1},b_{1})\sim(a_{2},b_{2})$ iff $a_{1}b_{2}=a_{2}b_{1}$. Every element of this hierarchy is finitely specifiable: a finite syntactic object built by $\delta$ and enclosure.

### 3.2 The discrete side: valuation trees

**Definition 3.2 (Valuation tree).** Fix a prime $p$ and let $T_{p}$ be the rooted tree whose vertices at level $n$ correspond to residue classes modulo $p^{n+1}$, each vertex having $p$ children; this is the Bruhat–Tits tree of $\mathbb{Q}_{p}$ in its standard combinatorial presentation. A path from the root is an element of the boundary $\partial T_{p}$, which carries an ultrametric $d_{p}$ induced by the $p$‑adic valuation $v_{p}$. The corpus framework [11] treats such $p$‑adic completions as information carriers (the Valuation axis); here they serve as the canonical discrete substrate. For concreteness and computability of all counts we work primarily with the binary tree $T_{2}$ ($p=2$), whose boundary $\partial T_{2}$ is in bijection with infinite binary sequences. A second convention — the $(p+1)$‑regular presentation of the Bruhat–Tits tree of $\mathrm{PGL}_{2}$ over $\mathbb{Q}_{p}$, in which every vertex has $p+1$ neighbors — is used in Section 4.5 for the regular‑tree counts and is explicitly labeled as a separate convention (see Appendix A, D1).

### 3.3 The Monna‑map projection

**Definition 3.3 (Monna‑map).** The Monna‑map is the projection
$$
\mu:\partial T_{2}\to[0,1],\qquad
\mu\big((b_{1},b_{2},b_{3},\ldots)\big)=\sum_{k=1}^{\infty}b_{k}\,2^{-k},
$$
i.e., the standard binary‑expansion identification of the Cantor‑set boundary with the unit interval. The tree carries the ultrametric $d_{2}$; the interval carries the Euclidean metric $d_{\infty}(x,y)=|x-y|$. The map $\mu$ is continuous from the ultrametric topology onto the Euclidean topology, is many‑to‑one exactly on the dyadic rationals (which have two expansions), and collapses all ultrametric structure.

**Definition 3.4 (Computable shadow, artifact set).** A point $x\in[0,1]$ is a *computable shadow* if there is a finite program (equivalently, a finite rule in the sense of [7]) that, given $n$, outputs the first $n$ bits of a binary expansion of $x$. Let $\mathbb{R}_{\mathrm{comp}}[0,1]$ denote the set of computable shadows. The *artifact set* is
$$
A=[0,1]\setminus\mathbb{R}_{\mathrm{comp}}[0,1].
$$

### 3.4 Conjectures

- **C1 (Generation).** $\mathbb{N}$, $\mathbb{Q}$, and $\mathbb{R}_{\mathrm{comp}}$ arise from the distinction operator by enclosure operations; each computable real corresponds to a finite or limit‑definable tree path.
- **C2 (Projection).** The Monna‑map is surjective and non‑injective, and points of $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$ have no finite or limit‑definable preimage: they are artifacts, created by $\mu$ rather than discovered in $\partial T_{2}$.
- **C3 (Dominance).** The artifact set has full Lebesgue measure in $[0,1]$.

C3 is *derived conditionally* in Section 4 from the countability of finite programs plus the standard covering argument; its interpretation as “projection dominance’’ depends on C2, which remains a conjecture. We do not claim, as one formulation of the framework did, that the projection is *proved* to add precisely $\mathbb{R}\setminus\mathbb{R}_{\mathrm{comp}}$; that stronger claim is recorded as a divergence in Appendix A (D3) and treated here as conjectural.

### 3.5 Simulation protocol (proposed, not executed)

Finite‑depth trees of depths $d\in\{4,8,16,32\}$ with $p\in\{2,3,5\}$ are to be enumerated; each depth‑$d$ ray is mapped to the rational midpoint of its shadow interval; the resulting finite decimal strings are compared to decimal expansions of benchmark computable reals. The test of C1 is whether every benchmark real’s expansion is matched by some ray sequence; the test of C2’s converse — whether ray sequences exist whose limits are not limit‑definable — cannot be decided finitistically and is flagged as such. No numerical outcome of this protocol is reported in this paper because it has not been run.

### 3.6 Method of analysis

We do not simulate; we derive. All quantitative claims in Section 4 follow from stated inputs: the countability of finite programs, the Farey counting function for rationals, and exact enumerations of binary‑tree paths at finite depth. Each derivation shows its inputs, formula, and arithmetic.

## 4. Analysis

### 4.1 Input numbers and their sources

- $I_{1}$: The number of binary strings of length exactly $k$ is $2^{k}$ (combinatorial identity; the tree $T_{2}$ has $2^{k}$ nodes at depth $k$).
- $I_{2}$: The number of reduced fractions in $[0,1]$ with denominator at most $n$ is $|F_{n}|=1+\sum_{k=1}^{n}\varphi(k)$, where $F_{n}$ is the Farey sequence of order $n$ and $\varphi$ is Euler’s totient (standard Farey identity: each fraction $a/k$ with $\gcd(a,k)=1$, $0\le a\le k$, contributes, and $\varphi(k)$ counts them for each $k$, plus the endpoint $0/1$).
- $I_{3}$: Euler’s totient values for $k=1,\ldots,20$, each computed as the count of integers in $[1,k]$ coprime to $k$ (e.g., coprime to $10$ are $1,3,7,9$, so $\varphi(10)=4$): $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$, $\varphi(11)=10$, $\varphi(12)=4$, $\varphi(13)=12$, $\varphi(14)=6$, $\varphi(15)=8$, $\varphi(16)=8$, $\varphi(17)=16$, $\varphi(18)=6$, $\varphi(19)=18$, $\varphi(20)=8$.
- $I_{4}$: The number of binary programs of length at most $100$ is $\sum_{k=0}^{100}2^{k}=2^{101}-1$ (geometric sum; each length‑$k$ binary string is one program, and there are $2^{k}$ of them).
- $I_{5}$: The number of rays of $T_{2}$ at depth $n$ is $2^{n}$ (by $I_{1}$, one string per ray prefix).

### 4.2 Farey count at depth $n=20$: the $129$ figure

Step 1 (sum the totients). Grouping the values of $I_{3}$:
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
So $\sum_{k=1}^{20}\varphi(k)=128$.

Step 2 (Farey cardinality). By $I_{2}$, the Farey sequence $F_{20}$ of order $20$ has
$$
|F_{20}|=1+\sum_{k=1}^{20}\varphi(k)=1+128=129,
$$
where the leading $1$ accounts for the endpoint $0/1$ and the summand $\varphi(k)$ counts, for each denominator $k\le20$, the reduced fractions $a/k$ with $0\le a\le k$, $\gcd(a,k)=1$ (this includes $1/1$ via $\varphi(1)$). Thus exactly $129$ reduced rationals in $[0,1]$ have denominator at most $20$.

Step 3 (definable fraction at depth $20$). By $I_{5}$, the depth‑$20$ binary tree has $2^{20}=1{,}048{,}576$ rays. Identifying each depth‑$20$ ray with the rational midpoint of its shadow interval, the definable rational shadows at depth $20$ number $129$, so the definable fraction is
$$
f_{20}=\frac{129}{2^{20}}=\frac{129}{1{,}048{,}576}.
$$
Arithmetic: $129/1{,}048{,}576 = 0.00012302398681640625$ exactly (since $1{,}048{,}576 = 2^{20}$ and $129/2^{20}$ is a dyadic rational), i.e. $f_{20}=1.23024\times10^{-4}$ to six significant figures; check: $1{,}048{,}576\times1.23024\times10^{-4}=129.0000\ldots$

### 4.3 Program count and the measure‑zero derivation

Step 1 (program count). By $I_{4}$,
$$
2^{101}-1=2535301200456458802993406410751,
$$
verified digit‑wise: $2^{100}=1267650600228229401496703205376$, so $2^{101}=2\times2^{100}=2535301200456458802993406410752$, and subtracting $1$ gives the stated value.

Step 2 (countability of computable shadows). Every computable shadow (Definition 3.4) is determined by a finite program, and there are at most $2^{101}-1$ programs of length at most $100$; hence $\mathbb{R}_{\mathrm{comp}}[0,1]$ is countable, being a subset of a countable union of finite sets over all length bounds.

Step 3 (measure zero). Cover the $j$‑th computable shadow $x_{j}$ by an interval of radius $\varepsilon\,2^{-j-1}$, $j=1,2,\ldots$ The total length is
$$
\sum_{j=1}^{\infty}2\varepsilon\,2^{-j-1}=\varepsilon\sum_{j=1}^{\infty}2^{-j}=\varepsilon,
$$
using $\sum_{j=1}^{\infty}2^{-j}=1$. Since $\varepsilon>0$ is arbitrary, $\mathbb{R}_{\mathrm{comp}}[0,1]$ has Lebesgue measure $0$ in $[0,1]$, and the artifact set $A=[0,1]\setminus\mathbb{R}_{\mathrm{comp}}[0,1]$ has measure $1-0=1$: full measure. This derives C3 conditionally on the standard covering argument; it does not by itself derive C2.

### 4.4 Exponential decay of the definable fraction

At depth $n$ the definable fraction is bounded as
$$
f_{n}=\frac{|F_{n}|}{2^{n}}=\frac{1+\sum_{k=1}^{n}\varphi(k)}{2^{n}}\le\frac{1+n^{2}}{2^{n}},
$$
using the crude bound $\varphi(k)\le k$, so $\sum_{k=1}^{n}\varphi(k)\le n(n+1)/2\le n^{2}$ for $n\ge1$. Since $2^{n}$ grows exponentially while $1+n^{2}$ grows polynomially, $f_{n}\to0$: the definable rational shadows decay exponentially in depth. Check at $n=20$: $(1+400)/2^{20}=401/1{,}048{,}576=0.00038242340087890625\approx3.82423\times10^{-4}$, an upper bound consistent with the exact $1.23024\times10^{-4}$ of Section 4.2.

### 4.5 Regular‑tree convention counts

Under the $(p+1)$‑regular presentation (Definition 3.2, second convention; Appendix A, D1), the number of rays of length $n$ from a fixed root‑adjacent edge is $p\,(p+1)^{n-1}$ for $n\ge1$. For $p=2$: $n=4$ gives $2\cdot3^{3}=54$; $n=8$ gives $2\cdot3^{7}=4{,}374$; $n=16$ gives $2\cdot3^{15}=28{,}697{,}814$; $n=32$ gives $2\cdot3^{31}=2\cdot617{,}673{,}396{,}283{,}947=1{,}235{,}346{,}792{,}567{,}894$. These counts are for the simulation protocol of Section 3.5 and are not empirical results.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

- **R1.** $\sum_{k=1}^{20}\varphi(k)=128$ and $|F_{20}|=129$ (Section 4.2, Steps 1–2).
- **R2.** At depth $n=20$ the definable fraction is $f_{20}=129/2^{20}=129/1{,}048{,}576=1.23024\times10^{-4}$ (Section 4.2, Step 3).
- **R3.** The number of programs of length at most $100$ is $2^{101}-1=2535301200456458802993406410751$ (Section 4.3, Step 1).
- **R4.** $\mathbb{R}_{\mathrm{comp}}[0,1]$ has Lebesgue measure $0$ in $[0,1]$ and the artifact set $A$ has measure $1$ (Section 4.3, Step 3; conditional on the covering argument and on the identification of computable shadows with finite programs).
- **R5.** The definable fraction $f_{n}\le(1+n^{2})/2^{n}$ decays exponentially in $n$; at $n=20$ the bound is $\approx3.82423\times10^{-4}$ (Section 4.4).
- **R6.** Regular‑tree ray counts under the $(p+1)$‑regular convention: $54$, $4{,}374$, $28{,}697{,}814$, $1{,}235{,}346{,}792{,}567{,}894$ at depths $4$, $8$, $16$, $32$ respectively for $p=2$ (Section 4.5).

**Projection (labeled, not computed).** If the simulation protocol of Section 3.5 were run, we project that benchmark computable reals are matched by ray sequences at all tested depths (C1), with uncertainty: a failure at any depth would falsify C1 as stated. No numerical outcome is claimed.

## 6. Discussion

**Limitations.** The measure‑zero result R4 is standard mathematics, not a new theorem; the new content is its reinterpretation under C2, which remains conjectural. The Monna‑map of Definition 3.3 is the ordinary binary‑expansion map; calling it a projection of a Bruhat–Tits tree is a framing choice, and the ultrametric‑to‑Euclidean passage is not uniquely determined — other enumerations of $\partial T_{2}$ give other maps, and nothing derived here depends on a canonical choice. The Farey count $129$ measures depth‑$20$ rational shadows, not all definable shadows; programs of length $\le100$ vastly exceed depth‑$20$ rationals, so R2 and R3 measure different notions of “definable’’ and must not be conflated.

**Failure modes.** If non‑computable reals admitted limit‑definable tree paths (e.g., via oracles or non‑constructive choice), C2 would fail and artifacts would be a misnomer. If the artifact set were shown to have a definable structure richer than “complement of a countable set,” the projection‑artifact analogy with [1], [5] would weaken to metaphor.

**Falsification conditions.** (F1) Exhibiting a non‑computable real with a finite or limit‑definable preimage under $\mu$ falsifies C2. (F2) Proving the Monna‑map non‑surjective onto $[0,1]$ falsifies the surjectivity half of C2. (F3) A protocol run (Section 3.5) in which a benchmark computable real is not matched by any ray sequence falsifies C1.

**Against ourselves.** The strongest objection is that R4 needs no tree, no projection, and no distinction operator: the covering argument is substrate‑free, so the framework may add vocabulary rather than content. The reply — that the tree supplies a geometric reading of “where computables live’’ — is an interpretation, and we flag it as such. The corpus position that non‑computable breadth is physically vacuous [10], [11] is a philosophical predication, not a derivation of this paper.

## 7. Conclusion

We formalized a distinction‑based construction in which computable reals are finitely encodable tree phenomena and non‑computable reals are, conjecturally, artifacts of the Monna‑map projection. Derived results: $|F_{20}|=129$, $f_{20}=129/2^{20}\approx1.23024\times10^{-4}$, $2^{101}-1=2535301200456458802993406410751$, measure zero for the computable shadows and full measure for the artifact set, and exponential decay $f_{n}\le(1+n^{2})/2^{n}$. The projection thesis (C2) and the generation thesis (C1) remain conjectures with explicit falsification conditions; the simulation protocol that could test C1 has been specified but not executed.

## References

[1] arXiv:2010.14356v2 | Upsampling artifacts in neural audio synthesis  
[2] arXiv:2308.14122v1 | Preparing Reproducible Scientific Artifacts using Docker  
[3] arXiv:2308.04871v1 | Mathematical Artifacts Have Politics: The Journey from Examples to Embedded Ethics  
[4] arXiv:2103.01090v2 | Systematic Analysis and Removal of Circular Artifacts for StyleGAN  
[5] arXiv:2002.03814v1 | The Genius Conjectures (via Bell Polynomials)  
[6] arXiv:1508.01530v2 | Completely contractive projections on operator algebras  
[7] QNFO: Non-Computable Reals as Projection Artifacts: A Reconciled Framework for Tree-to-Manifold Construction of the Continuum  
[8] QNFO: The Computable Real Boundary: Where Physics Ends and Cognitive Fiction Begins  
[9] QNFO: Physical Irrelevance of Uncountability: Computable Reals Suffice for Continuum Physics  
[10] QNFO: Formal Derivation of Emergent Spacetime to the Bruhat‑Tits Tree  
[11] QNFO: Depth, Breadth, and Valuation: A Unified Ontology of the Physical Continuum  
[12] QNFO: Syntactic Generation  

## Appendix A. Divergence report

- **D1 (tree convention).**