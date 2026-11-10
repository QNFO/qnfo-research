# Physical Instantiation as Selection of Relational Structure: A Statistical Framework for Pre-Discovery in Mathematics

## Abstract

Mathematics developed without physical motivation repeatedly finds core physical application: complex numbers in quantum mechanics, fiber bundles in gauge theory, and max-plus algebra in optimal control. The standard explanation—unreasonable effectiveness—treats this as a philosophical puzzle rather than a measurable phenomenon. The gap addressed here is the absence of any quantitative test of whether physical instantiation of pre-existing mathematical structures is statistically non-accidental and predictable from structural features alone. We formalize the conjecture that physics selects a subset of an autonomous relational grammar by defining an invariant-overlap isomorphism measure between algebraic relational skeletons and dynamical systems, and by constructing a retrospective selection test over a registry of historically pre-physical structures. Under explicit assumptions (a pool of $N = 20$ structures, $k = 6$ later physically instantiated, a chance rate $p = 0.15$), the binomial tail probability is $P(X \geq 6) \approx 0.067$, and a feature-conditioned split (5 of 8 symmetry-bearing structures instantiated versus 1 of 12 without) yields a one-sided Fisher exact probability of $\approx 0.018$. Both computations are shown in full and are sensitive to the assumed counts: lowering the chance rate to $p = 0.10$ moves the binomial tail to $\approx 0.011$, while losing one instantiation moves it to $\approx 0.170$. The framework converts a metaphysical claim into a falsifiable registry study, gives mathematics-ontology projects a concrete curation target, and proposes a minimal next test: an expert-annotated registry of pre-1850 structures scored against the same null model.

## 1. Introduction

Funding agencies, journal editors, and working theorists face a recurring allocation problem: which bodies of abstract mathematics are worth investing in as candidates for future physical theory? Today this decision is made by taste, citation fashion, and historical accident. When max-plus algebra, developed for discrete mathematics and optimization, turned out to govern stationary solutions of Hamilton-Jacobi-Bellman equations [1], or when sporadic finite groups and modular functions surfaced in physics contexts [5], the connection was recognized only after the fact. The cost of guessing wrong is concrete: years of theoretical effort on structures that never bind to physical behavior, and, conversely, physically decisive mathematics left undeveloped because no selection signal existed. If instantiation could be predicted from structural invariants alone—symmetry type, conservation-law compatibility, algebraic closure properties—curriculum design, funding triage, and theory-building strategy would all acquire an evidence base they currently lack.

The conjecture under test is that mathematics constitutes an autonomous relational grammar, and that physical law operates by selecting the subset of that grammar whose internal relational skeleton is isomorphic to physical behavior. On this view the success of complex Hilbert space in quantum mechanics reflects shared invariant structure, not Platonic identity between a mathematical object and a physical one. The claim is deliberately reformulated so that it can fail: given a set of mathematical structures developed without physical motivation, one should be able to predict which ones later find physical application, and the hit rate should correlate with structural invariants rather than with historical or pragmatic factors such as the size of the community working on a structure.

Three observations motivate the formalization. First, the historical record itself contains natural experiments: complex numbers were introduced, as one analysis of the role of mathematics in physical science puts it, in a way that "cannot be suggested by physical observations," their initial interest lying in analytic function theory [6], yet they became the substrate of quantum mechanics. Second, entire branches of mathematics built with no physics in mind—idempotent and tropical mathematics—now organize problems of mathematical physics directly, from max-plus eigenvector characterizations of deterministic control systems to weak KAM theory [1], and their workshop literature spans traffic dynamics, image processing, and semiclassical quantization [2]. Third, projects that formalize the mathematical literature at scale, such as the plan for a global library in which community input pairs with machine learning to encode what the literature contains [7], make a systematic registry of structural features practically achievable for the first time.

This paper makes the conjecture precise enough to compute with. We define a relational skeleton as the equivalence class of a mathematical structure under its invariant-preserving automorphisms; we define an isomorphism measure between skeletons and dynamical systems as a Jaccard-type overlap of invariant sets; and we define a retrospective selection test comparing observed instantiation counts against a chance null. All counts used in the worked computations are declared assumptions, since no curated registry yet exists; the derivations, not the assumed inputs, are the contribution.

The contributions are:

- A formal definition of relational skeleton, invariant set, and an isomorphism measure $d_{\mathrm{J}}$ between algebraic skeletons and dynamical systems, with a worked numerical example (Section 3 and Section 4).
- A retrospective selection test: under the stated assumptions $N = 20$, $k = 6$, $p = 0.15$, the chance probability of observing $k$ or more instantiations is $P(X \geq 6) \approx 0.067$, derived term by term (Section 4).
- A feature-conditioned analysis: conditioning on a structural invariant (nontrivial continuous symmetry) raises the conditional instantiation rate from $1/12 \approx 0.083$ to $5/8 = 0.625$ under the assumed counts, with a one-sided Fisher exact probability of $\approx 0.018$ (Section 4).
- A sensitivity analysis showing the binomial result moves from $p \approx 0.067$ to $p \approx 0.011$ when the chance rate drops to $0.10$, and from $p \approx 0.067$ to $p \approx 0.170$ when the observed count drops to $k = 5$, with a statement of which assumed inputs dominate the conclusion (Section 4 and Section 6).
- A registry protocol and a minimal falsification path, adapted from the certainty-labeled and falsification-experiment methodology of the ultrametric thesis literature [11], together with readiness assessment and binding constraints (Section 7).

The statistical machinery developed here is domain-neutral: the same selection test applies wherever a generative formal system is mined by a downstream application domain, including program-synthesis systems that select among generated formal grammars, and knowledge-graph curation of the kind proposed for a global mathematical library [7].

## 2. Background and Related Work

The relation between mathematics and physics has been described at three levels: historical-philosophical, case-study, and infrastructural. This section reviews the works that ground each level and identifies what none of them supplies—a quantitative selection test.

**Historical-philosophical accounts.** The physical-mathematics framework built on Gilles Châtelet's philosophy argues that the mathematics-physics relation "has not been reciprocal," that figures such as Riemann and Grothendieck coupled mathematical invention to a philosophical picture of the world, and that Châtelet's notions of inverting, splitting, augmenting and virtuality are crucial to understanding the emergent field of Physical Mathematics, with mirror symmetry proposed as a natural case study [4]. That work supplies the conceptual vocabulary for two-way flow between mathematics and physics but stops short of any operational criterion for when an abstract structure will bind to physics. An earlier survey of the role of mathematics in physical sciences distinguishes the mundane role of mathematics (numerical calculation, integration) from a "sovereign" role in which higher mathematics finds applications in subtle empirical problems, and notes that concept-driven revolutions are rare—Thomas Kuhn's list contains quantum mechanics and only six other major concept-driven revolutions in 500 years, against roughly twenty tool-driven revolutions in the same period by Dyson's count [6]. The same survey observes that complex numbers are a mathematical concept whose introduction "cannot be suggested by physical observations" [6], which is precisely the kind of pre-physical origin our selection test targets. A dialogue-format treatment of moonshine in mathematical physics documents concrete cases where pure-mathematical objects carry physical weight: the two-qubit Bell inequality whose operator calculation gives $||C|| = 2\sqrt{2}$ against the classical bound of $2$, confirmed by experiment, and the representation of most sporadic groups as two-generator permutation groups acting on sets with computable Euler characteristic $2-2g = B+W+F-n$ [5]. These cases show that the instantiation phenomenon extends to the most remote corners of the mathematical grammar, not only to workhorse structures.

**Case studies of pre-physical mathematics entering physics.** The idempotent-mathematics literature is the cleanest modern example. The proceedings of the 2007 Moscow workshop state that idempotent mathematics is a new branch of mathematical sciences closely related to mathematical physics, with tropical mathematics as an important part of it, and trace the field's stages through the 1994 Bristol workshop volume and the 2003 Vienna workshop volume [1]. Within that volume, the max-plus analysis of Hamilton-Jacobi-Bellman equations treats stationary solutions of diffusion control models, and its related-results section records that the deterministic case reduces to eigenvectors of max-plus linear operators, studied by the idempotent-analysis school of Maslov and Kolokoltsov and absorbed into Fathi's weak KAM theory [1]. A structure invented for optimization and discrete mathematics thus became the natural language of a control-theoretic limit of classical mechanics. The companion volume extends the reach: its contents include max-plus finite element methods, max-plus convolution for fundamental solutions of differential equations with quadratic nonlinearities, image processing via pseudo-linear superposition principles, semiclassical quantization of field theories, and convex analysis applied to reconstruction of peculiar velocities of galaxies [2]. The breadth confirms that tropical/idempotent structures are not a one-off coincidence but a repeatedly selected family. On the discrete-geometry side, the volume [3] collects statements and solutions from a 2010 student olympiad in mathematical and theoretical physics.

**Relational and discrete foundational programs.** A family of recent frameworks treats reality as generated by a primitive syntactic operation rather than by substance. The syntactic-generation framework posits a basic syntactic token representing the drawing of a boundary, with no intrinsic mass, extension, or duration, whose existence is defined by its capacity to separate inside from outside, and derives structure from rules of combination that are strictly recursive [8]. The formal-ontology development makes this precise as a token calculus: an alphabet $\Sigma = \{\square, \lceil, \rfloor, \varepsilon\}$, a grammar $E ::= \varepsilon \mid \square \mid E_1 E_2 \mid \lceil E \rfloor$, three context-closed reduction rules (Calling, Crossing, Void), and a cross-ratio cocycle $\chi(A,B,C,D) \otimes \chi(A,B,D,E) \to \chi(A,B,C,E)$ as the sole invariant, with a summary table assigning the cross-ratio the role of fundamental invariant across mathematics, physics, and quantum computation [9]. The computational-syntax extension claims that continuity and time are observer-dependent artifacts of lossy compression of syntactic data, and reports artifacts including a non-commutative polynomial execution yielding $m_\mu/m_e = 206.67$ [10]. The ultrametric thesis argues that positional notation is inherently an ultrametric tree of nested cycles with the Archimedean line a derived abstraction, demonstrates with the observation that every base names itself "base-10" that a numeral string cannot internally specify its own interpretation rule, and—methodologically most relevant here—attaches explicit certainty labels to every non-textbook claim and states a concrete falsification experiment: a depth-2 tree of 8 transmon qubits with tree-only gates, whose central claim is falsified if tree geometry yields no statistically significant logical-error improvement over a 2D nearest-neighbour layout [11]. These works supply the relational-grammar side of our conjecture: a mathematical universe whose structures are defined by invariants and reduction rules, from which physics would select. What they do not provide is the selection statistics, which is the present paper's contribution.

**Infrastructure.** The report on developing a 21st-century global library for mathematics research argues that information about what the mathematical literature contains can be formalized and made easier to express, encode, and explore, with tools requiring much more than indexing and depending on community input paired with machine learning [7]. This is the enabling condition for our registry protocol: without such infrastructure, the feature annotation needed for a selection test over hundreds of structures is infeasible by hand.

Across all three levels, no cited work states a probability model for instantiation, defines an isomorphism measure between algebraic skeletons and dynamical systems, or tests whether pre-discovery is non-accidental. The gap is quantitative, and closing it requires only a registry, a null model, and arithmetic—which Sections 3 and 4 construct.

## 3. Methods

### 3.1 Objects and definitions

**Definition 1 (Relational skeleton).** A mathematical structure $S$ is given by a carrier with operations and relations. Its *relational skeleton* $\mathrm{sk}(S)$ is the equivalence class of $S$ under isomorphisms that preserve a designated invariant set. The invariant set $I(S)$ is a finite list of structural features: symmetry group type (discrete, Lie, none), conservation-law compatibility, algebraic closure properties, idempotence of its operations, and metric character (Archimedean versus ultrametric). The choice of feature list is a modeling decision; we fix it below.

**Definition 2 (Dynamical system skeleton).** A physical or control-theoretic dynamical system $D$ likewise carries an invariant set $I(D)$: its symmetry group, its conserved quantities, and the algebraic structure of its state-update operator (linear, max-plus linear, nonlinear).

**Definition 3 (Isomorphism measure).** For finite invariant sets we define the Jaccard-type distance

$$
d_{\mathrm{J}}(S, D) = 1 - \frac{|I(S) \cap I(D)|}{|I(S) \cup I(D)|},
$$

with $d_{\mathrm{J}} = 0$ when the invariant sets coincide and $d_{\mathrm{J}} = 1$ when they are disjoint. A structure $S$ is a *candidate* for a system $D$ if $d_{\mathrm{J}}(S,D) \leq \theta$ for a threshold $\theta$ fixed in advance. The measure is deliberately crude: it is a first-order operationalization of "shared invariant symmetries," not a claim of full isomorphism. We take this invariant-set overlap form of the measure under the convention that structural comparison operates on finite, explicitly listed feature sets rather than on automorphism-group orders; a group-order-based overlap score is a coarser special case in which the invariant list is replaced by a single symmetry-type feature, and nothing in the selection test of Section 3.2 depends on the finer form.

**Definition 4 (Instantiation event).** A structure $S$ developed at time $t_{\mathrm{dev}}$ without physical motivation is *instantiated* if it later becomes load-bearing in a physical theory or in the solution of a physical problem, in the sense of Section 2's cases: complex numbers in quantum mechanics [6], max-plus algebra in Hamilton-Jacobi-Bellman theory and weak KAM [1], moonshine-related finite groups in quantum-information-adjacent structures [5].

### 3.2 The selection test

Let $\mathcal{R} = \{S_1, \dots, S_N\}$ be a registry of structures each developed before any of its physical applications, with $k$ of them instantiated. Under the null hypothesis $H_0$ that instantiation is accidental at rate $p$ per structure, independently, the count $X$ is binomial:

$$
P(X = j) = \binom{N}{j} p^{j} (1-p)^{N-j}, \qquad P(X \geq k) = \sum_{j=k}^{N} \binom{N}{j} p^{j} (1-p)^{N-j}.
$$

Under the alternative $H_1$, instantiation probability depends on a structural feature $F$ (for example, possession of a nontrivial continuous symmetry). The registry then splits into a $2 \times 2$ table and the one-sided Fisher exact test applies:

$$
P_{\mathrm{Fisher}} = \frac{1}{\binom{N}{k_{\mathrm{tot}}}} \sum_{i} \binom{a}{i} \binom{N-a}{k_{\mathrm{tot}} - i},
$$

summed over tables at least as extreme as the observed one, where $a$ is the number of feature-bearing structures and $k_{\mathrm{tot}}$ the total instantiations.

### 3.3 Assumed inputs

No curated registry exists, so every count below is a declared assumption, not a measurement. We assume:

- $N = 20$ structures in a pilot registry of pre-1850, pre-physical origin (complex numbers, quaternions, fiber-bundle-like constructs, non-Euclidean geometries, idempotent semirings, ultrametric spaces, and similar families; the exact list is a protocol output, Section 7).
- $k = 6$ of them later instantiated, a rate consistent with the case density documented in Section 2.
- Chance rate $p = 0.15$ per structure, an assumption standing in for the base rate at which an arbitrary abstract structure happens to become load-bearing in physics; we test sensitivity at $p = 0.10$.
- Feature split: $a = 8$ structures bear a nontrivial continuous symmetry feature; of these, $5$ are instantiated; of the $N - a = 12$ without the feature, $1$ is instantiated.

The method is: fix the feature list, fix the null, compute the tail probabilities with all arithmetic shown, then vary the assumptions to locate which input dominates the conclusion. This paper performs no survey, annotation, or data collection; the registry study that would supply real counts is specified as a proposal in Section 7.

## 4. Analysis

### 4.1 Worked example of the isomorphism measure

As an illustration with declared assumption: let a structure $S$ (say, the max-plus semiring skeleton) carry $I(S) = \{$idempotent addition, order-theoretic completeness, linearity over a semiring, duality pairing$\}$, so $|I(S)| = 4$, and let a deterministic control system $D$ carry $I(D) = \{$idempotent addition (optimization as addition), order-theoretic value functions, max-plus linearity of the update operator, duality pairing (Legendre-Fenchel)$\}$, so $|I(D)| = 4$ with $|I(S) \cap I(D)| = 3$. Then

$$
|I(S) \cup I(D)| = 4 + 4 - 3 = 5, \qquad d_{\mathrm{J}}(S,D) = 1 - \frac{3}{5} = 0.4.
$$

With threshold $\theta = 0.5$, this pair qualifies as candidate. The max-plus control connection documented in [1]—where the deterministic case of the diffusion control model reduces to eigenvectors of max-plus linear operators—is exactly the kind of pairing this measure is designed to flag in advance.

### 4.2 Binomial tail: is instantiation non-accidental?

Inputs (assumptions, Section 3.3): $N = 20$, $k = 6$, $p = 0.15$, $q = 1 - p = 0.85$.

Compute the null probabilities $P(X = j) = \binom{20}{j} 0.15^{j} \, 0.85^{20-j}$ for $j = 0, \dots, 5$.

Powers of $0.85$, computed by repeated multiplication:

$$
0.85^{15} = 0.087354, \quad 0.85^{16} = 0.074251, \quad 0.85^{17} = 0.063114,
$$
$$
0.85^{18} = 0.053647, \quad 0.85^{19} = 0.045600, \quad 0.85^{20} = 0.038760.
$$

- $j=0$: $\binom{20}{0} = 1$; $0.15^{0} = 1$; $P_0 = 1 \times 1 \times 0.038760 = 0.038760$.
- $j=1$: $\binom{20}{1} = 20$; $20 \times 0.15 = 3$; $P_1 = 3 \times 0.045600 = 0.136800$.
- $j=2$: $\binom{20}{2} = 190$; $190 \times 0.15^{2} = 190 \times 0.0225 = 4.275$; $P_2 = 4.275 \times 0.053647 = 0.229341$.
- $j=3$: $\binom{20}{3} = 1140$; $1140 \times 0.15^{3} = 1140 \times 0.003375 = 3.8475$; $P_3 = 3.8475 \times 0.063114 = 0.242831$.
- $j=4$: $\binom{20}{4} = 4845$; $4845 \times 0.15^{4} = 4845 \times 0.00050625 = 2.452778$; $P_4 = 2.452778 \times 0.074251 = 0.182123$.
- $j=5$: $\binom{20}{5} = 15504$; $15504 \times 0.15^{5} = 15504 \times 0.0000759375 = 1.177335$; $P_5 = 1.177335 \times 0.087354 = 0.102842$.

Cumulative null probability through $j = 5$:

$$
P(X \leq 5) = 0.038760 + 0.136800 + 0.229341 + 0.242831 + 0.182123 + 0.102842 = 0.932697.
$$

Therefore

$$
P(X \geq 6) = 1 - 0.932697 = 0.067303 \approx 0.067.
$$

Under the assumed null, observing six or more instantiations out of twenty has probability about $6.7\%$: suggestive but not decisive at the conventional $0.05$ level. The expected count under $H_0$ is

$$
\mathbb{E}[X] = Np = 20 \times 0.15 = 3,
$$

so the assumed observation of $6$ is twice the chance expectation.

### 4.3 Feature conditioning: Fisher exact test

Inputs (assumptions, Section 3.3): $a = 8$ feature-bearing structures, $N - a = 12$ without, $k_{\mathrm{tot}} = 6$ instantiations, observed table: $5$ of $8$ feature-bearing instantiated, $1$ of $12$ non-feature-bearing instantiated.

Conditional rates:

$$
r_{F} = \frac{5}{8} = 0.625, \qquad r_{\bar{F}} = \frac{1}{12} \approx 0.083333, \qquad \frac{r_F}{r_{\bar{F}}} = 0.625 \times 12 = 7.5.
$$

Feature-bearing structures are instantiated at $7.5$ times the rate of the others, under the assumed counts.

One-sided Fisher exact probability. Under the hypergeometric null (row and column margins fixed), the probability of the observed split is

$$
P_{\mathrm{obs}} = \frac{\binom{8}{5}\binom{12}{1}}{\binom{20}{6}}.
$$

Compute: $\binom{8}{5} = 56$; $\binom{12}{1} = 12$; numerator $= 56 \times 12 = 672$. $\binom{20}{6} = \binom{20}{5} \times \frac{20-5}{6} = 15504 \times \frac{15}{6} = 15504 \times 2.5 = 38760$. Hence

$$
P_{\mathrm{obs}} = \frac{672}{38760} = 0.017337.
$$

The only more extreme table (with margins fixed) is $6$ of $8$ and $0$ of $12$:

$$
P_{\mathrm{ext}} = \frac{\binom{8}{6}\binom{12}{0}}{\binom{20}{6}} = \frac{28 \times 1}{38760} = 0.000722.
$$

One-sided Fisher probability:

$$
P_{\mathrm{Fisher}} = 0.017337 + 0.000722 = 0.018059 \approx 0.018.
$$

Under the assumed counts, the association between the symmetry feature and instantiation is significant at the $0.05$ level: probability about $1.8\%$ of seeing a split this lopsided if the feature were irrelevant. This is the paper's sharpest quantitative statement, and it is exactly as strong as its assumed counts.

### 4.4 Sensitivity to the chance rate

Recompute the binomial tail with $p = 0.10$, $q = 0.90$, same $N = 20$, $k = 6$.

Powers of $0.90$:

$$
0.90^{15} = 0.205891, \quad 0.90^{16} = 0.185302, \quad 0.90^{17} = 0.166771,
$$
$$
0.90^{18} = 0.150094, \quad 0.90^{19} = 0.135081, \quad 0.90^{20} = 0.121577.
$$

- $P_0 = 0.121577$.
- $P_1 = 20 \times 0.10 \times 0.135081 = 2 \times 0.135081 = 0.270162$.
- $P_2 = 190 \times 0.01 \times 0.150094 = 1.9 \times 0.150094 = 0.285179$.
- $P_3 = 1140 \times 0.001 \times 0.166771 = 1.14 \times 0.166771 = 0.190119$.
- $P_4 = 4845 \times 0.0001 \times 0.185302 = 0.4845 \times 0.185302 = 0.089779$.
- $P_5 = 15504 \times 0.00001 \times 0.205891 = 0.15504 \times 0.205891 = 0.031921$.

Sum:

$$
P(X \leq 5) = 0.121577 + 0.270162 + 0.285179 + 0.190119 + 0.089779 + 0.031921 = 0.988737,
$$

$$
P(X \geq 6) = 1 - 0.988737 = 0.011263 \approx 0.011.
$$

Lowering the chance rate from $0.15$ to $0.10$ moves the tail probability from $0.067$ to $0.011$, crossing the $0.05$ threshold. The conclusion "non-accidental" therefore hinges more on the assumed chance rate $p$ than on the observed count $k$: this is the dominant sensitivity, and Section 6 lists it as the primary limitation.

### 4.5 Sensitivity to the observed count

With $p = 0.15$ but $k = 5$ instead of $6$, the tail is $P(X \geq 5) = P(X \geq 6) + P_5 = 0.067303 + 0.102842 = 0.170145 \approx 0.170$: one fewer instantiation destroys the signal entirely. With $k = 7$, the tail shrinks by the $j = 6$ term:

$$
P_6 = \binom{20}{6} \times 0.15^{6} \times 0.85^{14}.
$$

$$
P_6 = 38760 \times 0.000011390625 \times 0.102770.
$$

Compute step by step: $0.15^{6} = 0.15^{5} \times 0.15 = 0.0000759375 \times 0.15 = 0.000011390625$; $0.85^{14} = 0.85^{15} / 0.85 = 0.087354 / 0.85 = 0.102770$. Then $38760 \times 0.000011390625 = 0.441501$, and $0.441501 \times 0.102770 = 0.045373$. Hence

$$
P(X \geq 7) = P(X \geq 6) - P_6 = 0.067303 - 0.045373 = 0.021930 \approx 0.022.
$$

The sensitivity picture is therefore asymmetric in the observed count: one fewer instantiation ($k = 5$) raises the tail from $0.067$ to $0.170$ and destroys the signal, while one more ($k = 7$) lowers it from $0.067$ to $0.022$ and strengthens it past the conventional threshold. The test is more fragile to undercounting than to overcounting, which matters for registry design: false negatives among annotated structures are costlier than false positives.

### 4.6 Sensitivity to the feature split

The Fisher result depends on both the split ratio and the total count. Holding $a = 8$, $N = 20$, $k_{\mathrm{tot}} = 6$ fixed, suppose the feature-bearing instantiated count were $4$ instead of $5$ (table: $4$ of $8$, $2$ of $12$). The observed-table probability becomes

$$
P_{\mathrm{obs}}' = \frac{\binom{8}{4}\binom{12}{2}}{\binom{20}{6}} = \frac{70 \times 66}{38760} = \frac{4620}{38760} = 0.119197.
$$

Tables at least as extreme in the one-sided direction are $5$ of $8$ ($0.017337$), $6$ of $8$ ($0.000722$), and the observed $4$ of $8$ itself, so

$$
P_{\mathrm{Fisher}}' = 0.119197 + 0.017337 + 0.000722 = 0.137256 \approx 0.137.
$$

A single reclassified structure moves the Fisher probability from $0.018$ to $0.137$, again crossing the $0.05$ threshold. The feature-conditioned result is therefore at least as sensitive to annotation accuracy as the binomial result is to the assumed chance rate. Both sensitivities are carried into the limitations of Section 6.

## 5. Results

All results below follow from the derivations of Section 4 under the declared assumptions of Section 3.3; no count is a measurement.

- **Isomorphism measure (Section 4.1).** For the worked max-plus pairing with $|I(S)| = |I(D)| = 4$ and $|I(S) \cap I(D)| = 3$, the Jaccard distance is $d_{\mathrm{J}}(S,D) = 1 - 3/5 = 0.4$, below the threshold $\theta = 0.5$, so the pair qualifies as a candidate. This reproduces in advance the pairing documented after the fact in [1].
- **Binomial tail (Section 4.2).** Under $N = 20$, $k = 6$, $p = 0.15$: $P(X \geq 6) = 0.067303 \approx 0.067$. The expected count under the null is $\mathbb{E}[X] = 3$, so the assumed observation is twice the chance expectation. The result is suggestive but does not reach the conventional $0.05$ level.
- **Feature conditioning (Section 4.3).** Under the assumed split ($5$ of $8$ versus $1$ of $12$), the conditional instantiation rates are $r_F = 0.625$ and $r_{\bar{F}} \approx 0.083333$, a rate ratio of $7.5$. The one-sided Fisher exact probability is reported as $P_{\mathrm{Fisher}} \approx 0.018$; this quantitative result is presented as a hypothesis pending empirical verification (see Section 6).
- **Sensitivity to the chance rate (Section 4.4).** At $p = 0.10$ the binomial tail is $P(X \geq 6) = 0.011263 \approx 0.011$. The conclusion "non-accidental" crosses the significance threshold when the chance rate moves by $0.05$; the assumed chance rate $p$ is the dominant input.
- **Sensitivity to the observed count (Section 4.5).** At $k = 5$ the tail is $0.170145 \approx 0.170$; at $k = 7$ it is $0.021930 \approx 0.022$. The test is more fragile to undercounting than to overcounting.
- **Sensitivity to the feature split (Section 4.6).** Reclassifying one feature-bearing structure from instantiated to not instantiated moves the Fisher probability from $0.018$ to $0.137$. The feature-conditioned result is highly sensitive to annotation accuracy.

The headline comparison is: the unconditional test ($P \approx 0.067$) fails to reject the null at $0.05$, while the feature-conditioned test ($P \approx 0.018$) rejects it. Under the assumed counts, structural features carry the selection signal that raw instantiation counts do not.

## 6. Discussion

The framework converts "unreasonable effectiveness" from a philosophical puzzle into a registry study with a computable null. Its sharpest result—that a symmetry feature raises the conditional instantiation rate by a factor of $7.5$ with Fisher probability $\approx 0.018$—is exactly as strong as its assumed counts, and the sensitivity analysis shows how weak that is. Three limitations dominate.

**Limitations.**

- *Assumed counts.* Every input ($N = 20$, $k = 6$, $p = 0.15$, the $5$-of-$8$ split) is a declared assumption standing in for a registry that does not yet exist. The derivations are the contribution; the numbers are illustrations of the derivations, not findings about the world.
- *Chance-rate dominance.* Moving $p$ from $0.15$ to $0.10$ moves the binomial tail from $0.067$ to $0.011$. No independent estimate of $p$ exists in the cited literature; until one is constructed from a real registry, the unconditional test cannot reject the null at all.
- *Annotation fragility.* Reclassifying a single structure moves the Fisher probability from $0.018$ to $0.137$ (Section 4.6). Feature annotation—what counts as a "nontrivial continuous symmetry"—is itself a judgment call, and the result is linear in annotation errors of this kind.
- *Selection of the feature list.* The invariant list of Definition 1 is a modeling decision. A different feature list could produce a different split and a different Fisher probability; the framework does not yet contain a principled procedure for choosing features other than pre-registration before the counts are known.
- *Registry circularity.* Structures were chosen as examples partly because they instantiated (complex numbers, max-plus algebra, ultrametric spaces). A retrospective registry assembled with hindsight inflates $k$; only a registry fixed in advance, with instantiation status scored blind to the feature annotations, tests the conjecture cleanly.
- *Small counts.* With $N = 20$, the Fisher test's exactness is an advantage, but the confidence interval on a rate of $5/8$ from eight structures is wide; the framework needs $N$ in the hundreds before conditional rate estimates stabilize.

**Falsification.** The main result would be falsified by the registry study of Section 7 if a pre-registered, blind-annotated registry of pre-1850 structures produced a one-sided Fisher probability above $0.05$ for the symmetry-instantiation association, or if the conditional instantiation rate for feature-bearing structures did not exceed that of feature-free structures. A second falsification path is confounding: if instantiation status correlates better with a pragmatic variable—community size, journal coverage, availability of textbooks—than with any structural invariant, the selection claim reduces to sociology and the framework's central conjecture fails. The calculation that would most directly falsify the quantitative claim is a recomputation of Section 4.3 on real counts yielding $P_{\mathrm{Fisher}} \geq 0.05$; under the assumed counts the margin is thin enough ($0.018$ against $0.05$) that modest annotation error alone can erase it, as Section 4.6 shows. Thus the reported $P_{\mathrm{Fisher}} \approx 0.018$ should be regarded as a provisional hypothesis rather than a confirmed finding.

**What would strengthen the result.** An independent estimate of the chance rate $p$, derived from a large registry of structures with known instantiation status, would convert the unconditional binomial test from illustrative to decisive. A pre-registered feature list, fixed before annotation, would remove the feature-selection freedom. Blind scoring of instantiation status would remove the hindsight circularity.

**Open questions.** Whether the Jaccard measure $d_{\mathrm{J}}$ predicts instantiation order (which structure binds first) rather than instantiation occurrence; whether the framework extends to structures developed after 1850, where the pre-physical criterion becomes hard to certify; and whether the relational-grammar picture of [8], [9]—in which structures are generated by recursive combination rules from a primitive token—implies that the feature list itself is derivable rather than chosen, are all unresolved here.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result.** The users are curators of formalized mathematics projects, research funders allocating budgets across abstract-mathematics programs, and theorists choosing which bodies of mathematics to learn. If the result holds on a real registry, the decision that changes is triage: structures bearing nontrivial continuous symmetry and conservation-law-compatible algebra would be prioritized for development and staffing, and the feature list of Definition 1 becomes a screening instrument. The infrastructure prerequisite is the kind of formalized mathematical library described in [7], in which information about what the literature contains is formalized and made easier to express, encode, and explore, with tools depending on community input paired with machine learning; without it, feature annotation over hundreds of structures is infeasible by hand. The result is also foundational for the relational-grammar programs of [8] and [9]: it supplies the first quantitative selection statistic for the claim that physics selects a subset of an autonomously generated mathematical universe, which those frameworks assert but do not test.

**(b) Current readiness.** This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported, concept formulated). No hardware, prototype, or pilot exists; the registry itself does not exist. Analytical work of this kind cannot exceed TRL 3, and nothing here approaches it: the measure $d_{\mathrm{J}}$ has been applied to one illustrative pairing, not validated against a corpus.

**(c) The smallest next test.** A minimal registry study would: (i) fix a feature list and a chance-rate estimation procedure in writing before any annotation; (ii) assemble a registry of $N \geq 100$ mathematical structures first published before 1850, each annotated blind for the features and for instantiation status by at least two independent annotators with a disagreement-resolution rule; (iii) compute the binomial tail and the Fisher exact probability as in Sections 4.2 and 4.3 on the real counts. The outcome that refutes the framework is $P_{\mathrm{Fisher}} \geq 0.05$ with the feature-free rate at or above the feature-bearing rate; the outcome that de-risks it is $P_{\mathrm{Fisher}} < 0.01$ with the rate ratio above $2$. A cheaper intermediate step is a calibration study of the chance rate $p$: estimate it from a large registry of structures with known instantiation status, which would fix the dominant sensitivity identified in Section 4.4.

**(d) Binding constraints.** The first binding constraint is annotation cost and consistency: the Section 4.6 result shows one reclassified structure moves the Fisher probability by a factor of $7$, so inter-annotator agreement is the limiting resource, not compute. The second is registry completeness bias—structures that were never developed at all are underrepresented in the historical record, which biases $k$ upward. The third is the pre-1850 cutoff: certifying "no physical motivation at development time" requires historical evidence that thins with age, and for some candidate structures (quaternions, non-Euclidean geometry) the motivation record is contested. Whether these constraints can be met within a standard curatorial project budget is an open question; no cost figure is derivable from the present analysis.

**(e) Order-of-magnitude projections.** Labeled as projections with stated assumptions: if annotation of one structure's feature vector and instantiation status takes between one and four expert-hours (an assumption; no source gives a figure), a 100-structure registry requires 100–400 expert-hours, or roughly 3–13 annotator-weeks at 30 hours per week—small enough that the study is bounded by annotation quality, not by scale. No other cost or performance projection is derivable from the inputs stated here.

**(f) Risks and misuse.** The framework could be misused as a funding-rationale oracle: quoting the $7.5$-fold rate ratio without the sensitivity analysis to justify defunding entire fields of pure mathematics. The sensitivity results of Sections 4.4–4.6 are the corrective—the same analysis shows the signal vanishes under single-count perturbations—and any policy use must carry them. A second risk is post-hoc feature shopping: searching feature lists until one correlates with instantiation, which the pre-registration requirement of the protocol is designed to block.

## 8. Conclusion

The unreasonable effectiveness of mathematics in physics can be restated as a selection hypothesis with a computable null: physics selects, from an autonomous relational grammar, those structures whose invariant skeletons overlap with physical behavior. This paper supplied the formal apparatus—relational skeletons, a Jaccard-type isomorphism measure $d_{\mathrm{J}}$, and a retrospective selection test—and computed its behavior under declared assumptions. Under $N = 20$, $k = 6$, $p = 0.15$, the unconditional binomial tail is $P(X \geq 6) \approx 0.067$: suggestive, not decisive. Conditioning on a symmetry feature under the assumed split yields a rate ratio of $7.5$ and a one-sided Fisher probability of $\approx 0.018$: decisive at the conventional level, but shown by the sensitivity analysis to collapse to $0.137$ under a single reclassification and to depend dominantly on the assumed chance rate, which moves the unconditional tail from $0.067$ to $0.011$ when lowered from $0.15$ to $0.10$. The contribution is therefore not a finding that physics selection is non-accidental, but a falsifiable protocol whose execution—blind annotation of a pre-registered registry of at least 100 pre-1850 structures, with the chance rate calibrated independently—would settle the question. The same machinery applies wherever a generative formal system is mined by a downstream domain, including program synthesis and the curation of a global mathematical library of the kind proposed in [7]; the registry study it calls for is the smallest experiment that would move this question from philosophy to statistics.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.55.12). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 10 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Idempotent and tropical mathematics and problems of mathematical physics (Volume I). arXiv:0710.0377v1. https://arxiv.org/abs/0710.0377v1
[2] Idempotent and tropical mathematics and problems of mathematical physics (Volume II). arXiv:0709.4119v1. https://arxiv.org/abs/0709.4119v1
[3] Mathematical Physics : Problems and Solutions of The Students Training Contest Olympiad in Mathematical and Theoretical Physics (May 21st - 24th, 2010). arXiv:1110.4864v2. https://arxiv.org/abs/1110.4864v2
[4] On Physical Mathematics: an approach through Gilles Châtelet's philosophy. arXiv:2510.13125v1. https://arxiv.org/abs/2510.13125v1
[5] A moonshine dialogue in mathematical physics. arXiv:1503.02677v2. https://arxiv.org/abs/1503.02677v2
[6] Role of Mathematics in Physical Sciences. arXiv:math/0402407v1. https://arxiv.org/abs/math/0402407v1
[7] Developing a 21st Century Global Library for Mathematics Research. arXiv:1404.1905v1. https://arxiv.org/abs/1404.1905v1
[8] https://papers.qnfo.org/papers/syntactic-generation-primitive-distinctions. QNFO: Syntactic Generation.
[9] https://papers.qnfo.org/papers/formal-ontology-of-distinction-and-invariance. QNFO: Formal Ontology of Distinction and Invariance.
[10] https://papers.qnfo.org/papers/computational-syntax-of-reality. QNFO: Computational Syntax of Reality.
[11] https://papers.qnfo.org/papers/the-ultrametric-foundation-a-unified-thesis-on-number-time-knowledge-and-computa. QNFO: The Ultrametric Foundation: A Unified Thesis on Number, Time, Knowledge, and Computation.
