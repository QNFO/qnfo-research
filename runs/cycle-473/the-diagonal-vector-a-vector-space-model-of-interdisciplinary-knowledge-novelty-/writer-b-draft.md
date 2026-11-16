# The Diagonal Vector: A Vector-Space Model of Interdisciplinary Knowledge, Novelty, and the Synthesis Bottleneck

## Abstract

Interdisciplinary research is routinely praised and structurally penalized: researchers who span fields face fragmented vocabulary, siloed evaluation, and funding systems organized by discipline, while the cognitive cost of holding many fields in one mind is unquantified. This paper develops a vector-space model of interdisciplinary knowledge in which disciplines are orthogonal basis directions of an $n$-dimensional knowledge space, an individual's or a paper's knowledge state is a vector of expertise coefficients, and innovativeness is scored by the number of significantly loaded dimensions (the participation ratio) together with angular distance from existing work. The gap addressed is twofold: no existing formalism connects a measurable vocabulary-silo statistic to a synthesis-cost model, and the claim that large language models shift the research bottleneck from information access to synthesis bandwidth has not been given a computable form. Using the measured partitionality index of six arXiv disciplines ($0.9721$, from 453 of 466 technical bigrams being domain-local), we derive the concentration of random-vector overlap in that space (standard deviation $1/\sqrt{466} \approx 0.0463$), a joint-fidelity model in which per-dimension synthesis reliability $p = 0.95$ (assumed) yields end-to-end fidelity $0.95^{10} \approx 0.599$ for a ten-field integration, and a pairwise-cost law $k(k-1)/2$ giving 45 cross-pairs at $k=10$ versus 190 at $k=20$. The model predicts a bandwidth-limited optimum integration width and gives a computable criterion separating genuine synthesis from keyword-level "semantic collage." The framework is analytical (TRL 1-2); its principal use is to turn interdisciplinarity from a rhetorical virtue into a set of measurable quantities that corpus studies and funding taxonomies can test.

## 1. Introduction

A researcher in quantum foundations, a researcher in number theory, and a researcher in machine learning can work on the same structural object and never find each other's work. This is not a hypothetical: a quantitative audit of six arXiv categories (quantum physics, number theory, machine learning, genomics, materials science, economic theory) found that 453 of 466 distinct technical bigrams occur in exactly one domain, that the partitionality index is 0.9721, and that the shared core of terms occurring in three or more domains is empty [8]. The cost of this lexical wall is paid twice. First, duplicate and parallel structures go unrecognized, so the combinatorial surface of possible cross-domain connections is left unexplored. Second, when researchers do attempt integration, they must do so across a vocabulary gap with no shared metric for what counts as a genuine synthesis rather than a surface-level juxtaposition of keywords.

The problem has become more acute, not less, with the arrival of large language models (LLMs). When the marginal cost of retrieving and restating knowledge from any field approaches zero, the scarce resource shifts from information access to the cognitive bandwidth needed to hold several fields' structures in mind at once and to check that the combination is coherent. Yet no existing framework quantifies this shift: how the value of an integrative idea scales with the number of fields it spans, where the curse of dimensionality begins to degrade synthesis quality, and how a genuine "diagonal" contribution can be distinguished computationally from a semantic collage of borrowed terms. Funding agencies and editors currently decide interdisciplinarity cases with rhetoric and review-panel intuition; a computable model would let them ask instead how many dimensions a proposal meaningfully spans, whether those dimensions are orthogonal in practice, and whether the integration compresses or merely concatenates.

This paper builds that framework. We model disciplines as orthogonal basis vectors of an $n$-dimensional knowledge space; an agent's knowledge state is a coefficient vector; and a research idea's innovativeness is a function of its significant components and its angular separation from the existing corpus. The model is deliberately simple, and its value lies in what it makes computable: silo statistics become geometry, synthesis cost becomes a function of integration width, and the distinction between synthesis and collage becomes a testable property of coefficient profiles.

The contributions are:

- A formal definition of the knowledge space, the expertise vector, and two novelty statistics — the participation ratio $N_{\mathrm{eff}}$ and the angular distance $\theta$ from prior work — with worked derivations (Section 3, Section 4).
- A concentration result for random-vector overlap in a vocabulary space of measured dimension, showing that chance lexical overlap is bounded at the level of $\pm 0.09$ cosine similarity for the measured six-domain space, so that observed cross-domain bridge structure above that band is informative (Section 4).
- A synthesis-cost and fidelity model: pairwise cost $k(k-1)/2$ and joint fidelity $p^k$ under an assumed per-dimension reliability, which together predict a finite optimal integration width $k^{\ast}$ and locate the curse of dimensionality for synthesis (Section 4).
- A computable criterion distinguishing genuine synthesis from semantic collage, based on the decay profile of sorted squared coefficients (Section 4).
- A mapping of the framework onto existing taxonomies of scientific contribution and onto a proposed corpus-validation design, with readiness honestly assessed as TRL 1-2 (Sections 6 and 7).

The geometric view developed here may also bear on problems outside research policy — any setting where agents combine knowledge from disjoint label systems, such as ontology alignment or multi-source data fusion — insofar as those settings share the orthogonal-vocabulary structure measured in [8].

## 2. Background and Related Work

The mathematical core of the model — treating a knowledge space as a vector space with orthogonal discipline directions — has precedents across several literatures, which we review for the specific tools each supplies.

Orthogonal decomposition in function spaces. [1] investigates an orthogonal decomposition of a Sobolev space, determining the dimension of the orthogonal difference space and showing how the spaces expand as their regularity exponent increases: the change in regularity "causes increase in length or norm, expansion of the space in terms of distance or separation between distinct elements and change in orthogonality." This is directly relevant as a formal precedent: orthogonality and distance are not fixed properties of a space but depend on the inner product chosen, and refining the space's structure changes the geometry of separation. Our model inherits this lesson — the "orthogonality" of disciplines is a property of the chosen representation (here, disjoint vocabulary), and changing the representation changes which ideas count as diagonal.

Sparse and compressible representations. [5] proposes the optimum subspace decomposition of infinite-dimensional compressible random processes in a locally convex Hausdorff space, measuring the dimension of the decomposition and proving that with a sufficient number of separating points the space admits a Banach-space structure; the work frames compressed sensing as reconstructing a sparse signal "by finding the infimum subspace." This supplies the second formal precedent: knowledge states, like compressible signals, are sparse in the right basis, and the effective dimension of a state is far smaller than the ambient dimension. Our participation-ratio statistic (Section 3) is the elementary analogue of this optimum-subspace idea.

Interpreting vector components as concepts. Whether the components of a learned vector space carry conceptual meaning is an empirical question. [4] trains a neural model to "conceptualize" word vectors — activating higher-order concepts recognized in a given vector — and reports a weighted classification $F_1$ score of $0.22$, with performance varying sharply across concepts: high for sharply bounded concepts such as *province*, poor for vague ones such as *location*. The authors conclude that "the more precise a concept boundary, the higher the classification performance tends to be." This is a caution for our framework: if a knowledge-space axis is to be interpreted as "the discipline," the interpretability of that axis depends on how sharply the discipline's boundary is defined, and axes corresponding to vague fields will support weaker geometric claims.

Novelty as a relational quantity. [3] analyzes sentence-level novelty detection and argues that novelty is "a combination of the partial overlap (PO...)" relations among items rather than an intrinsic property; the paper shows that clustering-based novelty methods fail because partial-overlap relations are not transitive, so sentences "need not necessarily form classes," and reports that human-assessed redundancy rates differ substantially even between comparable collections (34.1% in nv03 versus 53.7% in nv04), a difference the authors tie to method performance. Two lessons carry over: novelty must be defined relative to a reference set (in our model, angular distance from existing work), and naive clustering of "fields" can destroy the overlap structure that novelty measurement depends on.

Empirical vector spaces of skills and knowledge states. [7] develops the Knowledge Query Network (KQN) for knowledge tracing, representing students' knowledge states and skills as vectors, and explicitly tests the sensitivity of conclusions to the embedding dimensionality: skill-distance structure is compared across dimensionalities at $0.5d_{\mathrm{opt}}$, $d_{\mathrm{opt}}$, and $2d_{\mathrm{opt}}$, with Mantel correlations between distance matrices ranging from $0.495$ to $0.825$ across datasets and distance measures (Table 9), and clustering quality measured by Adjusted Rand Index. The finding that distance structure is preserved but not identical across dimensionalities is exactly the robustness question our novelty metric faces: how much does $N_{\mathrm{eff}}$ or $\theta$ change when the vocabulary space is re-embedded at a different dimension?

Cross-dataset integration as information gain. [2] describes the SPACE mission concept, which aims to take near-IR spectra for more than half a billion galaxies, and gives a concrete instance of integration producing information that neither part contains alone: the CMB spectrum $C_l$ depends on the combination $\Omega_m h^2$ while the matter power spectrum $P(k)$ is sensitive to $\Omega_m h$, "thus, combining these two datasets help to break degeneracies and adds tremendous scope to tighten the limits on parameters which result from the use of just one dataset in isolation." This is the physical-science prototype of the "diagonal vector" claim: the joint constraint is not the union of the individual constraints but a qualitatively new one, because the two datasets' parameter degeneracies are oriented differently — geometrically, their degeneracy directions are non-parallel, which is our orthogonality condition in a concrete form.

Quantified silo structure. [8] measures the precondition for any of this geometry to matter: whether domains share vocabulary at all. Beyond the six-domain audit (partitionality 0.9721, 13 bridge terms out of 466, of which 5 are machine-learning method vocabulary such as *machine-learning* and *foundation-models*), the paper probes the QNFO corpus itself and finds that the knowledge graph's semantic edges resolve to 40 record pairs, of which 8 are same-program and 0 are cross-program, while within-program linked pairs share title vocabulary at mean Jaccard 0.115 against 0.028 for random pairs. The within-program elevation of $+0.086$ establishes that shared vocabulary tracks semantic relatedness where links exist — which is what licenses using vocabulary overlap as a coordinate system in the first place, and the zero cross-program links show the coordinate system currently connects nothing across the wall.

Contribution taxonomies and unification as compression. [10] decomposes scientific progress into three functional types — Generative (G-Type, novel empirical predictions), Structural Unification (S-Type, coherence among existing theories), and Epistemic Scaffolding (E-Type, refinement of inquiry methods) — and formalizes non-trivial unification as description-length compression: Theorem 3 requires $G_U(T_U; T_1, T_2) > \delta$ with, for example, $\delta = 0.15 \times (K(T_1) + K(T_2))$, so that the unifying theory is strictly shorter than the sum of its parts. Our synthesis-versus-collage criterion (Section 4) is the vector-space counterpart of this compression condition: a genuine diagonal idea must be simpler than the concatenation of its source-field descriptions.

Testable cross-domain protocols. [11] specifies a Structured Cross-Domain Translation (SCDT) protocol with four executable phases and an evaluation design in which LLM agents either receive an object with a request for "interdisciplinary insights" (baseline) or execute the protocol with fixed lexicons (SCDT condition), measuring novelty, expert validity, and predictive success. Its computed search-space quantities include $N_{\mathrm{hyp}} = 60$ pairwise hypotheses and $E_{\mathrm{total}} = 180$ evaluation points, and its projected false-link risk falls from $P_{\mathrm{any}} \approx 0.265$ unmitigated to $P_{\mathrm{any}}^{\mathrm{tested}} \approx 0.059$ with validation sensitivity $s = 0.8$. This supplies both a template for testing our metrics and a quantified warning: unstructured cross-domain generation carries a spurious-link probability on the order of one in four, which is precisely the failure mode our collage criterion is designed to catch.

Community infrastructure. [6] presents a community-wide strategy for advancing heliophysics and space-weather modeling through open science, noting that applying open-science principles to modeling "requires more careful consideration regarding open data and open software guidelines, as scientific models differ significantly" from other artifacts. For our framework, this establishes both the enabling condition and the friction: corpus-scale tests of the diagonal-vector hypothesis require open, machine-readable cross-domain data and software, and the community norms for such sharing in modeling fields are still being negotiated.

Finally, [9] illustrates the ambition and the risk of grand unification: it posits a universal Hilbert space with $H|\Psi\rangle = 0$ and formalizes cross-domain mappings as functors between information, geometric, and perceptual categories, with perceiver correlations written as mutual information $I(X_p; X_q) = \sum_{x_p,x_q} P(x_p,x_q) \log[P(x_p,x_q)/(P(x_p)P(x_q))]$. We cite it not for its physics claims but for its methodological pattern — cross-domain structure expressed as mappings between formal spaces — and as a reminder, via its own emphasis that the mapping functor "is generally not injective," that cross-domain correspondence loses information, a point our angular-distance metric makes locally and quantitatively.

## 3. Methods

This is an analytical paper. We define a model, derive its properties, and compute all numbers from stated inputs; no experiment, simulation, survey, or corpus analysis is performed here, and every empirical input is attributed to its source or labeled as an assumption.

**Knowledge space.** Let $\{e_1, \dots, e_n\}$ be an orthonormal basis of $\mathbb{R}^n$, where each basis direction $e_i$ represents one discipline (operationally: one domain whose technical vocabulary is disjoint from the others, per the measured structure in [8]). A knowledge state — of a person, a group, or a paper — is a vector

$$x = \sum_{i=1}^{n} x_i e_i, \qquad x_i \geq 0,$$

where $x_i$ measures the depth of expertise in discipline $i$. The non-negativity constraint encodes that expertise is not signed; a paper that misuses a field's methods does not gain negative loadings but rather loadings that fail the coherence checks below.

**Justification of orthogonality as an assumption.** Orthogonality of the basis is an idealization justified by the measured partitionality: [8] finds 453 of 466 technical bigrams domain-local (partitionality index 0.9721) and an empty three-domain shared core. If disciplines shared substantial vocabulary, their basis vectors would have positive mutual inner products and the geometry would need a general metric $g_{ij} = \langle e_i, e_j \rangle$. We take the orthogonal model as the leading approximation under the convention that the measured 0.9721 partitionality is high enough that off-diagonal metric terms are second-order; Section 6 discusses when this fails.

**Effective dimensionality.** Following the sparse-reconstruction idea of finding the minimal subspace supporting a signal [5], we define the effective number of disciplines spanned by a state as the participation ratio

$$N_{\mathrm{eff}}(x) = \frac{\left(\sum_{i=1}^{n} x_i^2\right)^{2}}{\sum_{i=1}^{n} x_i^4}.$$

For a state with $k$ equal components $x_i = c$ and the rest zero, $N_{\mathrm{eff}} = k$ exactly; for uneven profiles, $N_{\mathrm{eff}}$ lies in $[1, k]$ and down-weights states with one dominant component. This is the "number of dimensions meaningfully spanned" made precise.

**Angular novelty.** Let $y$ be the centroid vector of a reference corpus (the existing literature in the idea's neighborhood). We define the angular novelty of idea $x$ as

$$\theta(x, y) = \arccos \frac{\langle x, y \rangle}{\|x\| \, \|y\|} \in [0, \pi].$$

A purely intra-disciplinary advance has small $\theta$; a diagonal idea has large $\theta$ because its mass sits in directions the corpus centroid does not occupy.

**Synthesis cost and fidelity.** Integrating $k$ disciplines requires, at minimum, checking every pairwise interface: we take the pairwise cost law $C(k) = \binom{k}{2} = k(k-1)/2$. For end-to-end fidelity we assume each discipline-interface is handled with per-interface reliability $p$ (an assumption; no source measures it), and interfaces fail independently, giving joint fidelity

$$F(k) = p^{\binom{k}{2}}.$$

**Synthesis versus collage.** A genuine synthesis, following the compression condition of [10], must be structurally simpler than the concatenation of its parts. In vector terms we use the sorted squared-coefficient profile $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_k$ (with $\lambda_i = x_{(i)}^2$). We define the profile decay exponent $\alpha$ by fitting $\lambda_i \propto i^{-\alpha}$ over the significant components and propose, as a hypothesis to be tested rather than a derived theorem, that genuine syntheses exhibit a structured profile (a small number of load-bearing dimensions with $\alpha \gtrsim 1$) while collages exhibit near-flat profiles ($\alpha \approx 0$) — many borrowed terms with near-equal weight and no load-bearing core. The threshold is a convention; we state it as a hypothesis in Section 6.

**Chance-overlap floor.** To distinguish signal from chance in vocabulary-level overlap statistics, we compute the concentration of random-vector cosine similarity in dimension $d$ (Section 4), which sets the floor above which observed cross-domain structure is informative.

## 4. Analysis

Every input is stated with its source; every arithmetic step is shown.

### 4.1 The measured space and its statistics

Inputs from [8]: 466 distinct technical bigrams across six arXiv domains; 453 domain-local; 13 bridge terms (two or more domains); 0 shared-core terms (three or more domains); partitionality index reported as 0.9721.

Check of the partitionality index:

$$\frac{453}{466} = 0.972103\ldots \approx 0.9721. \checkmark$$

Bridge share:

$$\frac{13}{466} = 0.027897\ldots \approx 0.0279,$$

matching the reported bridge share 0.0279 [8]. The two independent ratios confirm internal consistency of the source's table.

Within-program lexical elevation, from [8]: mean title-vocabulary Jaccard of 0.115 for same-program linked pairs versus 0.028 for random pairs:

$$\Delta J = 0.115 - 0.028 = 0.087,$$

which the source reports as $+0.086$; the $0.001$ difference is rounding in the source's inputs, and we use the source's stated elevation $+0.086$ when quoting it.

### 4.2 Chance-overlap floor in the measured space

Model the vocabulary space as $d$-dimensional with $d = 466$ (the number of distinct technical bigrams, from [8]). For two independent random unit vectors in $\mathbb{R}^d$ with i.i.d. zero-mean components, the cosine similarity $c$ has

$$\mathbb{E}[c] = 0, \qquad \mathrm{Var}(c) = \frac{1}{d}.$$

(This is the standard concentration result for random directions; it follows from each pairwise product $u_i v_i$ having mean 0 and variance $1/d^2$, summed over $d$ coordinates.) With $d = 466$:

$$\sigma_c = \frac{1}{\sqrt{466}} = \frac{1}{21.5870\ldots} = 0.046323\ldots \approx 0.0463.$$

The two-sided 95% band under approximate normality is

$$\pm 1.96 \, \sigma_c = \pm 1.96 \times 0.046323 = \pm 0.090793\ldots \approx \pm 0.0908.$$

Interpretation: in a space of the measured size, two unrelated knowledge states will show cosine overlap within about $\pm 0.09$ by chance alone. The within-program lexical elevation $+0.086$ measured in [8] sits at the edge of this band — a point we return to in Section 6, since it warns that single-pair lexical signals near $0.09$ are weak evidence on their own and must be aggregated.

### 4.3 Worked example: participation ratio

Take a hypothetical researcher with expertise coefficients (assumed for illustration, in arbitrary expertise units) $x = (0.9, 0.8, 0.6, 0.1, 0.1)$ across five disciplines, all other components zero.

Compute the squares: $x_i^2 = (0.81, 0.64, 0.36, 0.01, 0.01)$.

$$\sum x_i^2 = 0.81 + 0.64 + 0.36 + 0.01 + 0.01 = 1.83.$$

Fourth powers: $x_i^4 = (0.6561, 0.4096, 0.1296, 0.0001, 0.0001)$.

$$\sum x_i^4 = 0.6561 + 0.4096 + 0.1296 + 0.0001 + 0.0001 = 1.1955.$$

Then

$$N_{\mathrm{eff}} = \frac{(1.83)^2}{1.1955} = \frac{3.3489}{1.1955} = 2.8013\ldots \approx 2.80.$$

Although the vector has five nonzero components, its effective width is 2.80 disciplines: the two 0.1-loadings contribute almost nothing. This is the quantitative content of "meaningfully spans": naive nonzero counting would say 5, the participation ratio says 2.80. A uniform five-field polymath, $x_i = c$ for $i \leq 5$, would give $N_{\mathrm{eff}} = 5$ exactly, since $(5c^2)^2/(5c^4) = 25c^4/5c^4 = 5$.

### 4.4 Synthesis cost

With the pairwise law $C(k) = k(k-1)/2$:

$$C(5) = \frac{5 \cdot 4}{2} = 10, \qquad C(10) = \frac{10 \cdot 9}{2} = 45, \qquad C(20) = \frac{20 \cdot 19}{2} = 190.$$

Doubling the integration width from 10 to 20 fields multiplies the interface count by $190/45 = 4.22\ldots$ — cost grows quadratically, so the marginal discipline is increasingly expensive to integrate.

### 4.5 Joint fidelity and the optimal integration width

Assume per-interface reliability $p = 0.95$ (assumption; no source measures interface reliability — we state it to make the model computable and examine sensitivity). Then

$$F(k) = 0.95^{\binom{k}{2}}.$$

Compute:

$$F(5) = 0.95^{10} = 0.598737\ldots \approx 0.599,$$
$$F(10) = 0.95^{45} = e^{45 \ln 0.95} = e^{45 \times (-0.051293)} = e^{-2.30819} = 0.099457\ldots \approx 0.099,$$
$$F(20) = 0.95^{190} = e^{190 \times (-0.051293)} = e^{-9.74568} = 5.8517 \times 10^{-5} \approx 5.9 \times 10^{-5}.$$

Check $F(5)$: $0.95^2 = 0.9025$; $0.95^4 = 0.9025^2 = 0.81451$; $0.95^8 = 0.81451^2 = 0.66342$; $0.95^{10} = 0.66342 \times 0.9025 = 0.59874$. ✓

Under this model, a ten-field integration has about a 10% chance of being fully coherent end-to-end, and a twenty-field integration is essentially guaranteed to break somewhere. This is the curse of dimensionality for synthesis: not the geometry of distance concentration (which is mild, Section 4.2) but the combinatorial explosion of interfaces that must each be validated.

**Value-fidelity trade-off and $k^{\ast}$.** Suppose the value of an idea grows with its effective width as $V(k) = v \, k$ (assumption: linear value in width, the simplest hypothesis; the "diagonal premium" of [2]-style degeneracy breaking suggests value can grow super-linearly, which would only strengthen the interior optimum). Expected net value:

$$\mathcal{V}(k) = v\, k \, p^{k(k-1)/2}.$$

Maximize over $k$: with $p = 0.95$, $\ln \mathcal{V} = \ln(vk) + \frac{k(k-1)}{2} \ln p$. Setting the derivative to zero:

$$\frac{1}{k} + \left(k - \tfrac{1}{2}\right)\ln p = 0 \quad \Rightarrow \quad \frac{1}{k} = \left(k - \tfrac{1}{2}\right) |\ln p|.$$

With $|\ln p| = 0.051293$:

$$0.051293 \, k^2 - 0.0256465 \, k - 1 = 0,$$
$$k = \frac{0.0256465 + \sqrt{0.0256465^2 + 4 \times 0.051293}}{2 \times 0.051293} = \frac{0.0256465 + \sqrt{0.00065774 + 0.205172}}{0.102586} = \frac{0.0256465 + \sqrt{0.205830}}{0.102586}.$$

$$\sqrt{0.205830} = 0.453687, \qquad k^{\ast} = \frac{0.479334}{0.102586} = 4.6725\ldots \approx 4.7.$$

Under these assumptions the value-optimal integration width is about 5 disciplines — enough for a genuine diagonal, few enough that the interface web stays checkable. Sensitivity: with $p = 0.99$ ($|\ln p| = 0.010050$), the same quadratic gives $0.010050\,k^2 - 0.005025\,k - 1 = 0$, so $k = \frac{0.005025 + \sqrt{0.0000253 + 0.0402}}{0.0201} = \frac{0.005025 + 0.20057}{0.0201} = 10.23$; with $p = 0.90$ ($|\ln p| = 0.10536$), $k^{\ast} = \frac{0.05268 + \sqrt{0.002775 + 0.42144}}{0.21072} = \frac{0.05268 + 0.65132}{0.21072} = 3.34$. The optimum is sensitive to $p$ (roughly $k^{\ast} \propto 1/\sqrt{|\ln p|}$), which is the single most important quantity for any empirical follow-up to measure.

### 4.6 Synthesis versus collage: worked profiles

Construct two five-component profiles with identical $\ell_2$ norm and identical $N_{\mathrm{eff}}$-adjacent structure but different shapes.

Profile S (structured, hypothesized synthesis): squared coefficients $\lambda = (0.60, 0.25, 0.10, 0.04, 0.01)$, total $1.00$.

Profile C (collage): squared coefficients $\lambda = (0.24, 0.22, 0.21, 0.19, 0.14)$, total $1.00$.

Fit $\lambda_i \approx A \, i^{-\alpha}$ for profile S using the first and last points:

$$\frac{\lambda_1}{\lambda_5} = \frac{0.60}{0.01} = 60 = \left(\frac{5}{1}\right)^{\alpha} = 5^{\alpha} \quad \Rightarrow \quad \alpha = \frac{\ln 60}{\ln 5} = \frac{4.09434}{1.60944} = 2.5440\ldots \approx 2.54.$$

For profile C:

$$\frac{\lambda_1}{\lambda_5} = \frac{0.24}{0.14} = 1.7143 = 5^{\alpha} \quad \Rightarrow \quad \alpha = \frac{\ln 1.7143}{\ln 5} = \frac{0.53900}{1.60944} = 0.3349\ldots \approx 0.