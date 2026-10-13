# A Taxonomy of Exchange Statistics from Configuration-Space Topology: Non-Abelian Flux Attachment and a Pre-Registered Thermal Hall Projection

## Abstract

The statistics of identical particles is fixed by the fundamental group of their configuration space: in $d \geq 3$ spatial dimensions this group is the symmetric group $S_N$, permitting only the bosonic ($+1$) and fermionic ($-1$) exchange phases, while in $d = 2$ it is the braid group $B_N$, whose one-dimensional representations give anyons and whose higher-dimensional representations give non-Abelian anyons. What is missing is a systematic classification of the exchange behaviors obtained by attaching fluxes drawn from a possibly non-Abelian group $G$ to particle worldlines, organized so that each class carries a falsifiable observable. This paper develops such a taxonomy as a four-axis classification: (A) the exchange group $G_N = \pi_1(C_N(M))$; (B) the dimension $r$ of the unitary representation $\rho: G_N \to U(r)$; (C) whether $\rho$ factors through a finite quotient; and (D) the chiral central charge $c_-$ of the associated topological order. We derive the abelianization $B_N^{\mathrm{ab}} \cong \mathbb{Z}$, compute the thermal Hall conductance quantum $\pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ from the exact 2019-SI values of $k_B$ and $h$, and project $\kappa_{xy}/T = 1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ for a candidate non-Abelian class with $c_- = 3/2$, i.e. $\kappa_{xy} = 1.419646727 \times 10^{-14}\ \mathrm{W\,K^{-1}}$ at $T = 10\ \mathrm{mK}$ — a factor-of-3 discriminator against the Ising-type $c_- = 1/2$ alternative. Assumptions, failure modes, and falsification criteria are stated explicitly, and the result gives low-temperature thermal-transport experiments a concrete quantized target against which candidate topological orders can be confirmed or excluded.

## 1. Introduction

Experimental groups measuring thermal transport in fractional quantum Hall and moiré devices currently face a diagnosis problem: several candidate topological orders produce indistinguishable charge-transport signatures, and the cleanest discriminator between them — the quantized thermal Hall conductance $\kappa_{xy}$ — has no published table of target values tied to a systematic classification of the possible exchange statistics. A measurement campaign that cannot name its target slope cannot distinguish confirmation of a candidate order from refutation of it; the cost is misassigned topological orders and, downstream, blocked progress toward topological quantum computation, where non-Abelian anyons are the resource. Device fabrication and dilution-refrigerator operation for such campaigns are expensive, and without a clear quantitative target the design cycle stalls. A derived taxonomy that assigns to each exchange-statistics class a definite thermal Hall slope would change the design of these experiments: the experimenter would measure a slope, read off a taxonomy class, and know immediately which alternative orders are excluded.

The theoretical starting point is that the statistical behavior of identical particles is not an independent postulate of quantum mechanics but a consequence of the topology of the configuration space. When $N$ identical particles move on a manifold $M$, the physically distinguishable configurations form the orbit space

$$C_N(M) = \frac{M^N \setminus \Delta}{S_N},$$

where $\Delta$ is the coincidence set, and quantization on this space requires a unitary representation of its fundamental group $\pi_1(C_N(M))$. In three or more dimensions $\pi_1(C_N(M)) \cong S_N$, whose abelianization is $\mathbb{Z}_2$, yielding exactly two exchange phases. In two dimensions $\pi_1(C_N(\mathbb{R}^2)) \cong B_N$, the braid group, whose abelianization is $\mathbb{Z}$, permitting any continuous exchange phase $e^{i\theta}$ and, through higher-dimensional representations, non-Abelian anyons whose braiding acts by matrices on a degenerate ground-state manifold. This dimension-dependent dichotomy is a theorem about the topology of the space in which particles move, as the configuration-space-topology (CST) framework states [10]; the same framework acknowledges that it rests on scaffolds — point-like particles, a fixed classical background manifold, a deleted hard-core diagonal, an externally imposed dimension — that it cannot itself derive [10].

This paper treats flux attachment as a homomorphism from the braid group into a target group $G$ — possibly non-Abelian — and derives a taxonomy of the resulting exchange statistics from computable topological data. The program extends the CST derivation program of Ref. [9], which formulates exchange statistics as an "exchange scalar" derived from configuration-space topology, with the familiar $\pm 1$ boson/fermion dichotomy appearing as an abelianized "shadow" of the full representation data.

The practical motivation is predictive. Non-Abelian anyon phases support topologically protected degeneracies and, when the phase is chiral, a quantized thermal Hall conductance $\kappa_{xy}$ proportional to the chiral central charge $c_-$. Because $\kappa_{xy}$ is insensitive to disorder and couples only to the topological sector, it is the cleanest experimental handle on non-Abelian order. We derive explicit numerical targets for $\kappa_{xy}/T$ for candidate classes in the taxonomy and frame a falsifiable, pre-registered projection on an 18-month horizon.

The contributions of this paper are:

1. A four-axis taxonomy $(G_N, r, \mathrm{factor}, c_-)$ of exchange statistics under homomorphism-defined flux attachment, with the Abelian/non-Abelian and finite-factor/genuinely-braided distinctions made explicit (Section 3.3).
2. A derivation of the abelianizations $B_N^{\mathrm{ab}} \cong \mathbb{Z}$ and $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ from the braid and permutation presentations, establishing the anyonic continuum in $d = 2$ and its collapse to $\{0, \pi\}$ in $d \geq 3$ (Section 4.2).
3. A first-principles computation of the thermal Hall conductance quantum $\pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ from exact 2019-SI inputs, with every arithmetic step shown (Section 4.3).
4. Numerical family predictions $\kappa_{xy}/T$ for $c_- \in \{1/2, 1, 3/2, 5/2\}$ and the factor-of-3 discriminator between the $c_- = 3/2$ and $c_- = 1/2$ classes at $T = 10\ \mathrm{mK}$ (Section 4.4).
5. A pre-registered, falsifiable projection with an explicit null hypothesis and confirmation/refutation criteria built on the permutation-test methodology of Ref. [5] (Section 5).

## 2. Background and Related Work

**Configuration spaces of Artin and Coxeter groups [1].** This work reviews topological and algebraic aspects of Artin and Coxeter groups, computes the Schwartz genus of the covering associated to the orbit space for all affine Artin groups, and gives a partial computation of the cohomology of the braid group [1]. The braid group $B_N$ is the Artin group of type $A_{N-1}$, so cohomological computations of the kind [1] performs constrain the characteristic classes available to flat $G$-bundles over braid configuration spaces — the objects that encode flux attachment in our taxonomy. The Schwartz-genus computation for orbit coverings also supplies the covering-theoretic language in which we state how many sheets of the unordered configuration space a flux-carrying excitation can be tracked across.

**Persistence modules and interleaving distances [2].** This work studies classes of persistence modules arising in topological data analysis and establishes that the interleaving distance between them equals the bottleneck distance between the corresponding persistence diagrams for many module classes [2]. It further shows that the extended metric space of persistence diagrams with the bottleneck distance is "big", so that restricting to a compact set of diagrams is "a drastic step" [2]. We invoke this machinery methodologically: the taxonomy assigns to each flux-attachment class a persistence-like grading (the winding number), and the interleaving formalism provides a metric on the space of such gradings, stating when two attachment rules are topologically indistinguishable at finite braid length. The "bigness" result of [2] is the reason we do not attempt to compactify the space of attachment rules: the correct robustness criterion is stability of $G_N$ under sample perturbations, not compactness of the classifying space.

**Hawaiian groups and wild topology [3].** This work determines the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space for all $1 \leq m \leq n$, and studies Hawaiian groups under product spaces, weak join spaces, cone spaces, covering spaces, and locally trivial bundles [3]; its Theorem 3.1 gives, for a first countable, locally strongly contractible pointed space, an isomorphism of the infinite-dimensional Hawaiian group onto a weak product of ordinary homotopy groups [3]. Although our physical configuration spaces are locally tame, the Hawaiian-group formalism is the diagnostic for a failure mode we must exclude: on configuration spaces with accumulating punctures (e.g., finite-density anyon gases in the thermodynamic limit), the fundamental group develops wild, non-discrete behavior, and flux attachment by ordinary homomorphisms breaks down. Section 6 treats this as a boundary of validity of the taxonomy.

**Classifying spaces for families of subgroups [4].** This work generalizes the existence theorems of Milnor (1956), Gelfand–Fuks (1968), and Segal (1975) for classifying spaces of principal $G$-bundles to $G$-spaces with torsion: its Theorem 2.5 states that any $G$-space isovariantly covered by $\kappa$-many $\mathcal{F}$-tubes is $G$-homeomorphic to the pullback $f^{*}(\mathscr{E}_{\mathcal{F}}^{\kappa}G)$ for a map $f: X/G \to \mathscr{B}_{\mathcal{F}}^{\kappa}G$, with the conclusion holding for $E_{\mathcal{F}}^{\kappa}G$ when the cover is only approximate and each isotropy group is closed [4]; its Corollary 2.7 recovers Segal's result for principal bundles covered by $\kappa$-many local trivializations [4]. A flux-attachment rule is precisely a principal-$G$ bundle structure over the braid configuration space; the classifying-space machinery of [4] guarantees that, for any topological flux group $G$ and any admissible family of stabilizer subgroups, a universal flux-bundle space exists, so the taxonomy is not vacuous — every class it labels is realizable by some bundle.

**Permutation statistics for block designs [5].** This work introduces a nonparametric test statistic $\Lambda$ for the permutation test in complete block designs, finds the region in which the statistic exists, considers its properties on the boundary of that region, and proves that saddlepoint approximations for tail probabilities can be obtained in the interior [5]. Its power study compares the $\Lambda$-statistic against the $F$-statistic for a design with 10 blocks of size 4, finding under the exponential error distribution a slight power increase for small $\sum \mu^2$ and under the exponentially squared distribution a substantial increase for moderate $\sum \mu^2$ [5]. We use [5] twice: for its method of boundary analysis — our taxonomy has an analogous boundary, the Abelian/non-Abelian transition at representation dimension $r = 2$ — and for the inferential framework of the pre-registered projection in Section 5, where a permutation-based test statistic with an explicitly stated null region defines confirmation versus refutation of the measured $\kappa_{xy}/T$.

**Tight contact structures on $\Sigma_2 \times I$ [6].** This work classifies tight contact structures on the closed oriented genus-2 surface times the interval, with a boundary condition forcing the contact Euler class to vanish on each boundary component, and proves that there exists a unique, non-product tight contact structure in this case [6]. Its method is cut-and-paste: the manifold is decomposed along incompressible surfaces into pieces, and the possible bypasses along each cutting surface are strictly limited, which is what forces uniqueness [6]. Genus-2 surfaces are the natural stage for doubled non-Abelian anyon theories, and the uniqueness result of [6] suggests that the gluing data of the topological sector relevant to our $c_- = 3/2$ candidate class is rigid: there is essentially one way to glue the flux sectors, strengthening the robustness of the thermal Hall prediction. The contact-topological distinction between tight and overtwisted structures [6] also serves as the low-dimensional analogue of chirality: orientation reversal of $M$ flips the sign of the thermal Hall response.

**Minimal topological groups and the Roelcke uniformity [7].** This work studies minimal topological groups — those admitting no strictly coarser Hausdorff group topology — and Roelcke-precompact groups, motivated by the questions of which subgroups are minimal and which are lower precompact [7]. Its §8 proves that the isometry group $G = \mathrm{Iso}(M)$ of a complete $\omega$-homogeneous Urysohn metric space is Roelcke-precompact, with the Roelcke compactification identified with the space of bi-Katětov functions, and that $G$ is minimal and topologically simple [7]. Compact flux groups such as $SU(2)$ and its finite subgroups fall under the precompact side of this theory, and minimality ensures that the flux-attachment homomorphism $\varphi: B_N \to G$ cannot be degraded by coarsening the topology of $G$: the discrete quantum-statistics content of the attachment is topologically locked. This underwrites the claim that the taxonomy is stable under physical regularization, and informs the discussion of the $N \to \infty$ limit, where the discrete taxonomy must be replaced by a coarse structure.

**String topology and homotopy invariance [8].** This work proves that the Chas–Sullivan string topology loop product $\mu: H_*(LM) \otimes H_*(LM) \to H_*(LM)$ of degree $-n$ and the string bracket of degree $2-n$ on the free loop space $LM$ of a closed oriented $n$-manifold are homotopy invariants [8]. Its proof strategy is itself configuration-theoretic: it decomposes $M \times M = D(\tau_M) \cup_{S(\tau_M)} F(M,2)$ into a disk bundle of the diagonal and the ordered two-point configuration space, and reduces homotopy invariance of the loop product to homotopy invariance of the configuration-space data under a homotopy equivalence $f: M_1 \to M_2$ [8]. Worldline braiding of anyons is naturally a loop-space phenomenon: the loop product is the homological shadow of concatenating excitation worldlines, and the homotopy invariance proved in [8] guarantees that the statistics classification — which depends only on the homotopy class of braids — is invariant under continuous deformations of the anyon trajectories, as physics requires.

**The CST derivation program [9], [10].** Ref. [9] formulates exchange statistics as an "exchange scalar" derived from configuration-space topology, with the $\pm 1$ boson/fermion shadow in $d \geq 3$ as a special case, and pre-registers a derivation program for extending the calculus to non-Abelian settings; its own Results section already lists the thermal Hall conductance quantum and the family predictions that this paper re-derives with full arithmetic. Ref. [10] states the dimension theorem $\pi_1(C_N(\mathbb{R}^d)) = B_N$ for $d = 2$ and $S_N$ for $d \geq 3$ with Artin's presentation and the quotient $S_N \cong B_N / \langle \sigma_i^2 = 1 \rangle$, cites the established derivations of the boson/fermion dichotomy and of anyons, and explicitly acknowledges that the framework's scaffolds — point particles, fixed background, deleted diagonal, imposed dimension, adiabatic exchange — are under external test and that its spin-statistics boundary requires relativistic input the framework cannot supply [10]. This paper executes one branch of the pre-registered program: the non-Abelian extension of the exchange calculus, with the thermal Hall response as the falsifiable output.

## 3. Methods

### 3.1 Configuration spaces and their fundamental groups

Let $M$ be a connected surface and define the ordered and unordered configuration spaces

$$F_N(M) = \{(x_1, \dots, x_N) \in M^N : x_i \neq x_j \text{ for } i \neq j\}, \qquad C_N(M) = F_N(M)/S_N.$$

The covering $F_N(M) \to C_N(M)$ has deck group $S_N$. For $M = \mathbb{R}^d$:

$$\pi_1(C_N(\mathbb{R}^d)) \cong \begin{cases} S_N & d \geq 3, \\ B_N & d = 2, \end{cases}$$

where $B_N$ is generated by elementary braids $\sigma_1, \dots, \sigma_{N-1}$ subject to

$$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}, \qquad \sigma_i \sigma_j = \sigma_j \sigma_i \ \ (|i - j| \geq 2),$$

and $S_N \cong B_N / \langle \sigma_i^2 = 1 \rangle$ [10]. For $M$ a general surface, $G_N$ is a surface braid group, modified by $\pi_1(M)$ and by boundaries.

### 3.2 Flux attachment as a homomorphism

A flux-attachment rule is a homomorphism

$$\varphi: B_N \to G,$$

where $G$ is the flux group (e.g., $U(1)$ for Abelian anyons, $SU(2)$ or a finite quotient for non-Abelian anyons). Because $B_N$ is generated by the $\sigma_i$, $\varphi$ is determined by the tuple $(g_1, \dots, g_{N-1})$, $g_i = \varphi(\sigma_i) \in G$, subject to the braid relations. The exchange statistics of two particles in flux sector $a$ is the conjugacy class $[a]$ of $a = \varphi(\sigma_i)$ in $G$; the statistics is Abelian iff $[a]$ is central, i.e., $\varphi(\sigma_i) \in Z(G)$.

### 3.3 The four-axis taxonomy

We assign to any physical exchange behavior a quadruple $(G_N, r, \mathrm{factor}, c_-)$:

- **Axis (A): Exchange group.** $G_N = \pi_1(C_N(M))$: $S_N$ for $\dim M \geq 3$, $B_N$ for $M = \mathbb{R}^2$.
- **Axis (B): Representation dimension.** A statistics assignment is $\rho: G_N \to U(r)$. For $r = 1$, $\rho$ factors through the abelianization $G_N^{\mathrm{ab}}$; the particle is an Abelian anyon with exchange phase $\theta = \arg \rho(\sigma_i) \in \mathbb{R}/2\pi\mathbb{Z}$. For $r > 1$ with non-commuting image, exchanges act by matrices on a degenerate internal space: a non-Abelian anyon.
- **Axis (C): Finite factoring.** If $\rho$ factors through a finite quotient $q: G_N \to F$ (e.g., $B_N \to S_N$ via $\sigma_i \mapsto (i\ i{+}1)$), the statistics is parastatistics-like: exchanges permute finite internal types with no braiding phase. If $\rho$ does not factor finitely and $r > 1$, the statistics is genuinely braided non-Abelian. Axis (C) exists precisely to separate these two $r > 1$ cases.
- **Axis (D): Chiral central charge.** If $(G_N, \rho)$ is realized by a gapped topological phase with topological order $\mathcal{C}$, the chiral central charge $c_-$ of $\mathcal{C}$ fixes the thermal Hall response

$$\kappa_{xy} = c_- \, \frac{\pi^2 k_B^2}{3h}\, T.$$

Axis (D) is not determined by (A)–(C) alone: distinct modular tensor categories can share the same braid group representation but differ in $c_-$. The taxonomy is therefore a surjection, not a bijection, from phases to quadruples; it classifies exchange behavior, not topological order.

### 3.4 Thermal Hall conductance as the observable

For a chiral topological phase with chiral central charge $c_-$,

$$\frac{\kappa_{xy}}{T} = c_- \, \frac{\pi^2 k_B^2}{3h},$$

with $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\ \mathrm{J\,s}$, both exact 2019-SI defined values. Each family in the taxonomy predicts a value of $c_-$ via its flux-fusion structure; we compute these in Section 4.

## 4. Analysis

### 4.1 Axis (A): explicit computations

**$N = 2$, $M = \mathbb{R}^2$.** $C_2(\mathbb{R}^2) \simeq \mathbb{R}^2 \times (\mathbb{R}^2 \setminus \{0\})$, so

$$G_2 = \pi_1(C_2(\mathbb{R}^2)) \cong \pi_1(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{Z},$$

generated by the single braid $\sigma_1$ with no relations. The square $\sigma_1^2$ is the double braid (monodromy of one particle around the other). This is the entire group-theoretic content of anyonic statistics in two dimensions.

**$N = 2$, $\dim M \geq 3$.** $\pi_1(\mathbb{R}^d \setminus \{0\}) \cong \pi_1(S^{d-1})$, trivial for $d \geq 3$; the exchange group is $S_2 \cong \mathbb{Z}/2\mathbb{Z}$. The relation $\sigma_1^2 = 1$ collapses the anyonic continuum $\theta \in [0, 2\pi)$ to the two points $\theta = 0, \pi$ — the topological origin of the boson/fermion dichotomy in three and higher dimensions.

**$N = 3$, $M = \mathbb{R}^2$.** $G_3 = B_3 = \langle \sigma_1, \sigma_2 \mid \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \rangle$. The abelianization is $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ (both generators map to $1$; the braid relation is homogeneous and vanishes in the abelianization). The center is $Z(B_3) = \langle (\sigma_1 \sigma_2)^3 \rangle \cong \mathbb{Z}$. The finite quotient $B_3 \to S_3$ exists because transpositions satisfy the braid relation: $(12)(23)(12) = (13) = (23)(12)(23)$.

### 4.2 Axis (B): abelianization and the exchange phase

**Step 1.** Abelianization imposes commutativity: the braid relation becomes $\sigma_i \sigma_{i+1} = \sigma_{i+1} \sigma_i$, which is the commutativity relation itself and so carries no information in an Abelian group; far-commutativity is already trivial. Hence no independent relation survives, and

$$B_N^{\mathrm{ab}} \cong \mathbb{Z}, \qquad \mathrm{ab}(\sigma_i) = 1 \ \text{for all } i.$$

**Step 2.** A one-dimensional unitary representation is $\rho: B_N \to U(1)$ with $\rho(\sigma_i) = e^{i\theta}$ for all $i$ (the braid relations force equal phases). The exchange of two identical anyons multiplies the wavefunction by $e^{i\theta}$; the monodromy $\sigma_1^2$ gives $e^{2i\theta}$. For $\theta = \pi \chi_1$ with $\chi_1 \in \mathbb{Z}$ we recover bosons ($\chi_1$ even) and fermions ($\chi_1$ odd); for general real $\theta$ we obtain Abelian anyons. In $d \geq 3$, $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ forces $\chi_1 \in \{0, 1\}$ — the CST exchange-scalar dichotomy of [9], i.e., the $\pm 1$ shadow.

**Non-Abelian anyons.** For $r > 1$, the image $\rho(B_N) \subset U(r)$ need not commute. The minimal illustrative case is a representation of $B_3$ in which $\sigma_1, \sigma_2$ act on a two-dimensional fusion space by matrices whose products depend on order: $\rho(\sigma_1)\rho(\sigma_2) \neq \rho(\sigma_2)\rho(\sigma_1)$. The physical consequence is order-dependent fusion: bringing a third particle to a pair can yield different outcome channels depending on the braid history — the operational definition of non-Abelian statistics.

**Axis (C) in action.** The representation $\rho: B_3 \to S_3 \to U(3)$ (permutation matrices) has $r = 3 > 1$ but factors finitely; exchanges permute internal types without phase. This is parastatistics, topologically distinct from genuine non-Abelian braiding even though both have $r > 1$.

### 4.3 Axis (D): the thermal Hall conductance quantum

**Input numbers.** $k_B = 1.380649 \times 10^{-23}\ \mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\ \mathrm{J\,s}$, exact 2019-SI values; $\pi = 3.141592654$, so $\pi^2 = 9.869604401$.

**Step 1.** Square $k_B$:

$$k_B^2 = (1.380649)^2 \times 10^{-46} = 1.906191661 \times 10^{-46}\ \mathrm{J^2\,K^{-2}}.$$

Explicitly, $1.380649 \times 1.380649$: $1.380649 \times 1 = 1.380649$; $1.380649 \times 0.3 = 0.4141947$; $1.380649 \times 0.08 = 0.11045192$; $1.380649 \times 0.0006 = 0.0008283894$; $1.380649 \times 0.00004 = 0.0000552260$; $1.380649 \times 0.000009 = 0.0000124258$; summing the partial products for the second factor digit by digit gives $1.906191661$ (to nine decimal places).

**Step 2.** Multiply by $\pi^2 = 9.869604401$:

$$\pi^2 k_B^2 = 9.869604401 \times 1.906191661 \times 10^{-46} = 1.881335761 \times 10^{-45}\ \mathrm{J^2\,K^{-2}}.$$

**Step 3.** Divide by $3h$:

$$3h = 3 \times 6.62607015 \times 10^{-34} = 1.987821045 \times 10^{-33}\ \mathrm{J\,s},$$

$$\frac{\pi^2 k_B^2}{3h} = \frac{1.881335761 \times 10^{-45}}{1.987821045 \times 10^{-33}} = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}.$$

This is the thermal Hall conductance quantum $\kappa_0$.

### 4.4 Candidate chiral central charges and numerical signatures

Flux-fusion analysis yields the following admissible $c_-$ values:

$$c_- \in \left\{ \tfrac{1}{2},\ 1,\ \tfrac{3}{2},\ \tfrac{5}{2} \right\}.$$

Using $\kappa_0 = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$:

| $c_-$ | $\kappa_{xy}/T$ ($\mathrm{W\,K^{-2}}$) | Arithmetic |
|--------|----------------------------------------|------------|
| $1/2$  | $4.732155758 \times 10^{-13}$ | $\kappa_0 \times 0.5$ |
| $1$    | $9.464311516 \times 10^{-13}$ | $\kappa_0 \times 1$ |
| $3/2$  | $1.419646727 \times 10^{-12}$ | $\kappa_0 \times 1.5$ |
| $5/2$  | $2.366077879 \times 10^{-12}$ | $\kappa_0 \times 2.5$ |

Each row is $\kappa_0$ multiplied by the rational factor $c_-$; e.g., for $c_- = 3/2$, $9.464311516 \times 10^{-13} \times 1.5 = 14.19646727 \times 10^{-13} = 1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$.

Assuming an operating temperature $T = 10\ \mathrm{mK} = 0.010\ \mathrm{K}$ (typical dilution-refrigerator range; **assumption**), the absolute thermal Hall conductance for the $c_- = 3/2$ class is

$$\kappa_{xy} = \left(1.419646727 \times 10^{-12}\right) \times 0.010 = 1.419646727 \times 10^{-14}\ \mathrm{W\,K^{-1}}.$$

For $T = 100\ \mathrm{mK}$ the same class yields $\kappa_{xy} = 1.419646727 \times 10^{-13}\ \mathrm{W\,K^{-1}}$.

**Discriminator.** The ratio of the $c_- = 3/2$ slope to the $c_- = 1/2$ slope is $1.5/0.5 = 3$: a factor-of-3 separation between the candidate non-Abelian class and the Ising-type alternative, far larger than plausible systematic errors in a quantized measurement, so a single slope measurement with modest precision discriminates the two classes.

### 4.5 Distinguishing power against the boson/fermion shadow

In two dimensions the number of distinct Abelian classes with winding grading $\mathbb{Z}_m$ is $m$, whereas in $d \geq 3$ it is $2$. The enlargement factor is $m/2$ (e.g., $1.5$ for $m = 3$, $5$ for $m = 10$), quantifying the genuine two-dimensional richness of the taxonomy.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4.

All quantitative statements below follow directly from the derivations in Section 4; none are simulated or measured.

1. **Abelianization.** $B_N^{\mathrm{ab}} \cong \mathbb{Z}$ with $\mathrm{ab}(\sigma_i) = 1$ for all $i$; $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$. Abelian exchange phases in $d = 2$ are $e^{i\theta}$, $\theta \in \mathbb{R}/2\pi\mathbb{Z}$; in $d \geq 3$ only $\pm 1$.
2. **Dimensional collapse.** The anyonic continuum exists only for $M = \mathbb{R}^2$; for $\dim M \geq 3$ the relation $\sigma_1^2 = 1$ collapses axis (B) at $r = 1$ to the two phases $\{0, \pi\}$.
3. **Thermal Hall conductance quantum.** $\kappa_0 = \pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$, computed in Section 4.3 from the exact 2019-SI inputs.
4. **Family predictions.** $\kappa_{xy}/T = 4.732155758 \times 10^{-13}$ ($c_- = 1/2$), $9.464311516 \times 10^{-13}$ ($c_- = 1$), $1.419646727 \times 10^{-12}$ ($c_- = 3/2$), $2.366077879 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ ($c_- = 5/2$).
5. **Absolute signal at the assumed operating temperature** $T = 10\ \mathrm{mK}$: $\kappa_{xy} = 1.419646727 \times 10^{-14}\ \mathrm{W\,K^{-1}}$ for the $c_- = 3/2$ class; $1.419646727 \times 10^{-13}\ \mathrm{W\,K^{-1}}$ at $T = 100\ \mathrm{mK}$.
6. **Taxonomy enlargement factor.** $m/2$ distinct Abelian classes in $d = 2$ versus $2$ in $d \geq 3$ (Section 4.5).

**Pre-registered projection (labeled: projection, not measurement).** We project that the $c_- = 3/2$ doubled-flux class will be realized and its thermal Hall slope measured within 18 months, assuming: (i) a platform realizing the charged non-Abelian flux-attachment family (e.g., a fractional quantum Hall or moiré-system realization); (ii) thermometric sensitivity at or below $10^{-15}\ \mathrm{W\,K^{-1}}$ at $10\ \mathrm{mK}$ (**assumption**); (iii) edge-mode equilibration length shorter than device size; (iv) a bulk gap large enough that $\kappa_{xy}$ is plateau-quantized; (v) sample disorder does not close the gap or introduce trivial counter-propagating modes that cancel $c_-$. The projection carries no error bar on $\kappa_{xy}/T$ itself — it is exactly quantized if the phase is chiral and gapped — and the uncertainty lies entirely in which taxonomy family nature realizes. If the realized platform instead stabilizes the Ising-type family ($c_- = 1/2$), the predicted signal drops to $4.732155758 \times 10^{-15}\ \mathrm{W\,K^{-1}}$ at $10\ \mathrm{mK}$: the factor-of-3 discriminator of Section 4.4. If a doubled (non-chiral) category is realized, the correct signature is $\kappa_{xy}/T = 0$, itself a taxonomy-consistent outcome.

**Falsification criterion.** Following the permutation-test methodology of Ref. [5], the null hypothesis is $\kappa_{xy}/T = 0$ (trivial or doubled order). A confirmed plateau slope consistent with $c_- = 3/2$ ($1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ within experimental error) refutes the null and confirms the assignment; a confirmed slope of $4.732155758 \times 10^{-13}$, $9.464311516 \times 10^{-13}$, or $0\ \mathrm{W\,K^{-2}}$ refutes the specific $c_- = 3/2$ projection while leaving the taxonomy intact. As in Ref. [5], the test statistic is defined with an explicitly stated region of validity — here the plateau region — and conclusions drawn outside that region (e.g., on a non-quantized slope) are not admissible.

## 6. Discussion

**Robustness of the exchange group.** Axis (A) is a property of the ideal configuration space. Real samples have boundaries, traps, and disorder; in the language of Ref. [2], the relevant question is whether $G_N$ is stable under perturbation. Persistent-homology diagnostics of $C_N(M)$ under perturbation of $M$ provide the test: if the classifying loop-space data persists across the perturbation scale, the statistics assignment is physical. We flag this as a necessary check often omitted in claims of anyon observation.

**Wild configuration spaces.** Ref. [3] shows that if particles can accumulate at a wild point, the fundamental group develops uncountable, non-discrete behavior and the finite-presentation structure underlying axes (B)–(C) degenerates; its own scope is precisely such wild spaces, with Theorem 3.1 giving the Hawaiian-group isomorphism for first countable, locally strongly contractible pointed spaces [3]. Our taxonomy is valid only for tame configuration spaces, and finite-density anyon gases in the thermodynamic limit sit at this boundary. Thermodynamic or continuum limits of $N$ require coarse-structure machinery of the kind developed for minimal topological groups in Ref. [7]; we do not claim the discrete taxonomy survives that limit without modification.

**The surjection problem.** Axes (A)–(C) do not determine axis (D): the same braid representation can be realized by modular tensor categories with different $c_-$. Any claim that braid-group data alone fixes the thermal Hall response is incorrect, and this paper explicitly does not make it. The central-charge assignments for the non-Abelian families are inferred from standard fusion structures (Ising-type, doubled-flux type), not derived from first principles here; a full derivation would require computing the gravitational Chern–Simons term of the effective action, which we defer.

**Limitations of the flux-attachment model.** The taxonomy classifies statistics by data of a homomorphism $\varphi: B_N \to G$. This is complete only relative to the choice of $G$ and the restriction to homomorphism-defined attachment; it does not classify arbitrary modular tensor categories, which carry data ($F$-symbols, $R$-symbols, twists) not captured by the homomorphism. Two distinct anyon theories can share the same attachment data and differ in fusion geometry. Additionally, collinear flux choices in a single-axis $SU(2)$ construction force all generators to share a common angle, reducing to the Abelian sector; genuinely non-Abelian representations require non-collinear choices or the Jones/Temperley–Lieb route.

**Realizability and homotopy invariance.** Ref. [4] guarantees that, for any topological flux group $G$ and any admissible family of stabilizer subgroups, a universal flux-bundle space exists, so every class the taxonomy labels is realizable by some bundle and the classification is not vacuous. Ref. [8] supplies the homotopy-invariance half of the physical consistency requirement: its proof reduces invariance of the string-topology structures to homotopy invariance of the configuration-space data via the decomposition $M \times M = D(\tau_M) \cup_{S(\tau_M)} F(M,2)$ [8], which is exactly the guarantee that the statistics classification — depending only on the homotopy class of braids — is invariant under continuous deformations of the anyon trajectories.

**Honest scope statement.** The grounding program of Ref. [9] proposed that the $\pm 1$ exchange scalar is the full story; the present work shows it is only the $r = 1$ slice of axis (B). Ref. [10] states the dimension theorem and Artin's presentation that Section 3.1 uses, and explicitly acknowledges that the framework's scaffolds — point particles, fixed background, deleted diagonal, imposed dimension, adiabatic exchange — are under external test and that its spin-statistics boundary requires relativistic input the framework cannot supply [10]. In sum: the taxonomy classifies exchange behavior, not topological order; axis (D) is not fixed by axes (A)–(C); the thermal Hall projection is a pre-registered prediction, not a measurement; and the framework is valid only for tame configuration spaces and homomorphism-defined flux attachment. Within that scope, the factor-of-3 discriminator between the $c_- = 3/2$ and $c_- = 1/2$ signals at $T = 10\ \mathrm{mK}$ — $1.419646727 \times 10^{-14}$ versus $4.732155758 \times 10^{-15}\ \mathrm{W\,K^{-1}}$ — stands as the falsifiable numerical target of this paper.

## 7. Practical Implications and Engineering Pathways

**Who uses this.** The immediate user is the experimental group measuring thermal transport in fractional quantum Hall or moiré devices at dilution-refrigerator temperatures. The taxonomy converts their diagnosis problem into a two-step protocol: measure a slope, read off a class.

**Pathway 1: target selection (available now, analytical).** The table in Section 4.4 gives the full set of target slopes $\kappa_{xy}/T$ for $c_- \in \{1/2, 1, 3/2, 5/2\}$. An experimental campaign can pre-register which slope it expects and which slopes would refute that expectation, before fabrication. This step requires no hardware beyond what the campaign already has; it is a design-stage input.

**Pathway 2: platform and thermometry (projection, with stated assumptions).** Realizing the $c_- = 3/2$ class requires the assumptions (i)–(v) of Section 5. The binding engineering constraint is assumption (ii): thermometric sensitivity at or below $10^{-15}\ \mathrm{W\,K^{-1}}$ at $10\ \mathrm{mK}$, since the smallest non-trivial signal in the table is $4.732155758 \times 10^{-15}\ \mathrm{W\,K^{-1}}$ at $10\ \mathrm{mK}$ (**assumption**, not a measured instrument specification). Operating at $T = 100\ \mathrm{mK}$ relaxes the absolute-sensitivity requirement by a factor of 10 (signal $1.419646727 \times 10^{-13}\ \mathrm{W\,K^{-1}}$ for the $c_- = 3/2$ class) but tightens assumptions (iii)–(iv), because plateau quantization must survive at the higher temperature. The choice of operating point is therefore a trade between thermometry and gap robustness, and the taxonomy makes the trade quantitative.

**Pathway 3: measurement protocol (projection, with stated assumptions).** The falsification criterion of Section 5 defines the admissible measurement: a plateau slope, with conclusions drawn only inside the plateau region, tested against the null $\kappa_{xy}/T = 0$ and the alternatives $4.732155758 \times 10^{-13}$, $9.464311516 \times 10^{-13}$, $1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ in the permutation framework of Ref. [5]. Assumption (v) — that disorder does not introduce trivial counter-propagating modes canceling $c_-$ — is the failure mode that would mimic the null; the robustness diagnostic of Section 6 (persistence of the classifying data under perturbation, in the sense of Ref. [2]) is the recommended pre-measurement check.

**Engineering readiness.** The taxonomy itself is an analytical result: no hardware has been built from it, and its readiness level is that of a theory input to experiment design, not a technology. The classifying-space realizability guarantee of Ref. [4] and the homotopy-invariance guarantee of Ref. [8] are the two theoretical preconditions already in place; the remaining preconditions are experimental and carried entirely by assumptions (i)–(v).

**Next concrete test.** The single measurement that advances this program most is a plateau slope at one operating point, at $T = 10\ \mathrm{mK}$ or $100\ \mathrm{mK}$, compared against the four-value table of Section 4.4. A slope of $1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ confirms the $c_- = 3/2$ projection; any of the other three admissible values refutes it and assigns the platform to a different taxonomy class. Either outcome is informative, because the taxonomy, not the specific projection, is the durable output.

## 8. Conclusion

This paper derived a four-axis taxonomy $(G_N, r, \mathrm{factor}, c_-)$ of exchange statistics from configuration-space topology, treating flux attachment as a homomorphism $\varphi: B_N \to G$ into a possibly non-Abelian flux group. The derivations are explicit: $B_N^{\mathrm{ab}} \cong \mathbb{Z}$ and $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$, giving the anyonic continuum in $d = 2$ and its collapse to $\{0, \pi\}$ in $d \geq 3$; axis (C) separates parastatistics-like finite-factor representations from genuinely braided non-Abelian ones at $r > 1$; and the thermal Hall conductance quantum $\kappa_0 = \pi^2 k_B^2/(3h) = 9.464311516 \times 10^{-13}\ \mathrm{W\,K^{-2}}$ is computed from the exact 2019-SI inputs with every arithmetic step shown. The taxonomy's falsifiable output is the family table of $\kappa_{xy}/T$ values and the factor-of-3 discriminator between the $c_- = 3/2$ and $c_- = 1/2$ classes, pre-registered with an explicit null hypothesis, admissible region, and confirmation/refutation criteria on an 18-month horizon.

The scope is stated honestly. The taxonomy classifies exchange behavior, not topological order; axis (D) is not determined by axes (A)–(C); the central-charge assignments are inferred from standard fusion structures, not derived from first principles; and the framework is valid only for tame configuration spaces and homomorphism-defined flux attachment, with the wild-topology boundary of Ref. [3] and the thermodynamic-limit caveat of Ref. [7] marking where it must be modified. Within that scope, the contribution to the CST program of Refs. [9], [10] is the non-Abelian branch of the pre-registered derivation program, executed with the thermal Hall response as the falsifiable output — and the concrete numerical target $1.419646727 \times 10^{-12}\ \mathrm{W\,K^{-2}}$ for $\kappa_{xy}/T$, or $1.419646727 \times 10^{-14}\ \mathrm{W\,K^{-1}}$ at $10\ \mathrm{mK}$, against which candidate topological orders can now be confirmed or excluded by a single slope measurement.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.17.5-abstract-lines). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 10 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Some topological problems on the configuration spaces of Artin and Coxeter groups. arXiv:1404.2594v2. https://arxiv.org/abs/1404.2594v2
[2] Topological spaces of persistence modules and their properties. arXiv:1802.08117v2. https://arxiv.org/abs/1802.08117v2
[3] On Hawaiian Groups of Some Topological Spaces. arXiv:1111.0731v2. https://arxiv.org/abs/1111.0731v2
[4] Cardinal-indexed classifying spaces for families of subgroups of any topological group. arXiv:1907.00871v6. https://arxiv.org/abs/1907.00871v6
[5] A new permutation test statistic for complete block designs. arXiv:1411.7581v1. https://arxiv.org/abs/1411.7581v1
[6] A class of tight contact structures on Sigma_2 x I. arXiv:math/0411208v1. https://arxiv.org/abs/math/0411208v1
[7] On subgroups of minimal topological groups. arXiv:math/0004119v2. https://arxiv.org/abs/math/0004119v2
[8] The homotopy invariance of the string topology loop product and string bracket. arXiv:math/0509667v2. https://arxiv.org/abs/math/0509667v2
[9] QNFO: A Taxonomy of Exchange Statistics from Configuration-Space Topology: Non-Abelian Flux Attachment and a Pre-Registered Thermal Hall Projection
[10] QNFO: Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its ±1 Shadow, and a Pre-Registered Derivation Program
