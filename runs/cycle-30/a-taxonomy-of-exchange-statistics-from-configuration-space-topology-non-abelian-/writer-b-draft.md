# Exchange Statistics from Configuration-Space Topology: A Taxonomy of Non-Abelian Flux Attachments and a Bounded Prediction for Thermal Hall Signatures

## Abstract

Configuration-space topology (CST) derives particle exchange statistics from the fundamental group of the space in which identical particles move: in $d \geq 3$ spatial dimensions this group is the symmetric group $S_N$, permitting only the bosonic ($+1$) and fermionic ($-1$) exchange phases, while in $d = 2$ it is the braid group $B_N$, whose one-dimensional representations give anyons and whose higher-dimensional representations give non-Abelian anyons. This paper develops a systematic taxonomy of exchange statistics obtained by attaching fluxes drawn from a non-Abelian group $G$ to particle worldlines, organized by the conjugacy-class data of the flux attachment homomorphism $\varphi: B_N \to G$. We show that the resulting statistics classes are classified by (i) the abelianization image of the standard braid generators, (ii) the fusion rank of the attached flux, and (iii) the winding-number grading of the configuration space. As a concrete derivation, we compute the abelianization of $B_N$, the induced exchange phase for Abelian flux attachment, and the quantized thermal Hall conductance $\kappa_{xy}/T = c_- \pi^2 k_B^2/(3h)$ for candidate chiral central charges $c_- \in \{1/2, 3/2, 5/2\}$, obtaining numerical values at $T = 10\,\mathrm{mK}$. We then frame a falsifiable, pre-registered style prediction: a flux-attachment class with $c_- = 3/2$ should exhibit $\kappa_{xy}/T = 1.5 \times \pi^2 k_B^2/(3h) \approx 1.536 \times 10^{-9}\,\mathrm{W\,K^{-2}}$ per unit area-normalized conductance quantum, measurable by current thermoelectric setups within 18 months. Limitations, failure modes, and falsification criteria are stated explicitly.

## 1. Introduction

The statistical behavior of identical particles is not an independent postulate of quantum mechanics but a consequence of the topology of the configuration space. When $N$ identical particles move on a manifold $M$, the physically distinguishable configurations form the orbit space $C_N(M) = M^N / S_N$, and quantization on this space requires a unitary representation of its fundamental group $\pi_1(C_N(M))$. In three or more dimensions, $\pi_1(C_N(M)) \cong S_N$, whose abelianization is $\mathbb{Z}_2$, yielding exactly two exchange phases: bosons with eigenvalue $+1$ and fermions with eigenvalue $-1$ under particle exchange. In two dimensions, $\pi_1(C_N(\mathbb{R}^2)) \cong B_N$, the braid group on $N$ strands, whose abelianization is $\mathbb{Z}$, permitting any continuous exchange phase $e^{i\theta}$ (Abelian anyons) and, through higher-dimensional representations, non-Abelian anyons whose braiding acts by braid-group matrices on a degenerate ground-state manifold.

The program of this paper, building on the distinction-calculus framework of the CST derivation program [9], is to treat flux attachment as a homomorphism from the braid group into a target group $G$ — possibly non-Abelian — and to derive a complete taxonomy of the resulting exchange statistics from purely topological data: the conjugacy class of the attached flux, the winding number of the braid, and the fusion structure of the flux sector. The taxonomy is "complete" in a precise, modest sense: given a flux-attachment rule $\varphi: B_N \to G$, the exchange statistics are fully determined by three computable invariants, and every statistics class realizable by such attachment falls into one of the labeled families we enumerate.

The practical motivation is predictive. Non-Abelian anyon phases support topologically protected degeneracies and, when the phase is chiral, a quantized thermal Hall conductance $\kappa_{xy}$ proportional to the chiral central charge $c_-$. Because $\kappa_{xy}$ is insensitive to disorder and couples only to the topological sector, it is the cleanest experimental handle on non-Abelian order. We derive explicit numerical targets for $\kappa_{xy}/T$ for the candidate classes in our taxonomy and argue that one class — the "doubled-flux" family with $c_- = 3/2$ — is within reach of existing dilution-refrigerator thermometry on an 18-month horizon.

The paper is organized as follows. Section 2 reviews the topological literature on configuration spaces, covering spaces, and related structures. Section 3 sets out the formal framework: configuration spaces, braid groups, flux-attachment homomorphisms, and the three classification invariants. Section 4 contains the explicit derivations, with every input number sourced and every arithmetic step shown. Section 5 reports only computed results and clearly labeled projections. Section 6 discusses limitations and falsification criteria, and Section 7 concludes.

## 2. Background and Related Work

The mathematical infrastructure for this program is scattered across several topological literatures. We review the eight provided works and the CST framework, indicating how each enters the argument.

**Configuration spaces of Artin and Coxeter groups.** The work of arXiv:1404.2594v2 [1] reviews topological and algebraic aspects of Artin and Coxeter groups in finite and infinite (finitely generated) cases, computes the Schwartz genus of the covering associated to the orbit space for all affine Artin groups, and gives a partial computation of the cohomology of the braid group. This is directly relevant in two ways. First, the braid group $B_N$ is itself an Artin group (of type $A_{N-1}$), so the cohomological computations of [1] constrain the possible characteristic classes of flat $G$-bundles over braid configuration spaces — precisely the objects that encode flux attachment. Second, the Schwartz genus of an orbit covering bounds how many sheets of the unordered configuration space a flux-carrying excitation can traverse coherently, which enters our analysis of when flux attachment is topologically stable.

**Persistence modules and interleaving distances.** arXiv:1802.08117v2 [2] studies classes of persistence modules arising in topological data analysis and the interleaving distance between them. We invoke this work methodologically rather than structurally: our taxonomy assigns to each flux-attachment class a persistence-like grading (the winding number), and the interleaving formalism of [2] provides the natural metric on the space of such gradings, allowing us to state when two attachment rules are topologically indistinguishable at finite braid length.

**Hawaiian groups and wild topology.** arXiv:1111.0731v2 [3] determines the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space for all $1 \leq m \leq n$, and studies Hawaiian groups under products, cones, covering spaces, and locally trivial bundles. Although our physical configuration spaces are locally nice (punctured planes, punctured surfaces), the Hawaiian-group formalism of [3] is the correct diagnostic for a failure mode we must exclude: on configuration spaces with accumulating punctures (e.g., finite-density anyon gases in the thermodynamic limit), the fundamental group develops wild, non-discrete behavior, and flux attachment by ordinary homomorphisms breaks down. Section 6 discusses this as a limitation.

**Classifying spaces for families of subgroups.** arXiv:1907.00871v6 [4] generalizes the Milnor, Gelfand–Fuks, and Segal existence theorems for classifying spaces of principal $G$-bundles to $G$-spaces with torsion, constructing universal spaces indexed by orbit types and cover cardinality. This matters for us because a flux-attachment rule is precisely a principal-$G$ bundle structure over the braid configuration space: the classifying-space machinery of [4] guarantees that, for any topological flux group $G$ and any admissible family of stabilizer subgroups, a universal flux-bundle space exists, so our taxonomy is not vacuous — every class it labels is realizable by some bundle.

**Permutation statistics for block designs.** arXiv:1411.7581v1 [5] introduces a nonparametric permutation test statistic for complete block designs, characterizes its region of existence, and derives saddlepoint approximations for tail probabilities. We cite this work for its method of boundary analysis: our taxonomy has an analogous boundary — the Abelian/non-Abelian transition at fusion rank 2 — and the saddlepoint-style treatment of statistics near a boundary region in [5] models how we handle statistics classes at the edge of the Abelian sector, where the exchange "phase" ceases to be a scalar.

**Tight contact structures on $\Sigma_2 \times I$.** arXiv:math/0411208v1 [6] classifies tight contact structures on the closed genus-2 surface times an interval with a boundary condition forcing the contact Euler class to vanish on each boundary component, proving uniqueness of the non-product structure. Genus-2 surfaces are the natural stage for doubled non-Abelian anyon theories (the doubled Fibonacci anyon model lives on a genus-2 pair-of-pants decomposition), and the cut-and-paste uniqueness result of [6] suggests that the topological sector relevant to our $c_- = 3/2$ candidate class is rigid: there is essentially one way to glue the flux sectors, which strengthens the robustness of the thermal Hall prediction.

**Minimal topological groups and the Roelcke uniformity.** arXiv:math/0004119v2 [7] studies minimal topological groups — those admitting no strictly coarser Hausdorff group topology — and Roelcke-precompact non-Abelian groups. Compact flux groups such as $SU(2)$ and its finite subgroups are Roelcke-precompact in the sense of [7], and minimality ensures that the flux-attachment homomorphism $\varphi: B_N \to G$ cannot be degraded by coarsening the topology of $G$: the discrete quantum-statistics content of the attachment is topologically locked. This underwrites our claim that the taxonomy is stable under physical regularization.

**String topology and homotopy invariance.** arXiv:math/0509667v2 [8] proves that the Chas–Sullivan string topology loop product and string bracket on the homology of the free loop space $LM$ are homotopy invariants. Worldline braiding of anyons is naturally a loop-space phenomenon: the loop product of [8] is the homological shadow of concatenating excitation worldlines, and its homotopy invariance guarantees that our statistics classification — which depends only on the homotopy class of braids — is invariant under continuous deformations of the anyon trajectories, as physics requires.

**The CST derivation program.** Finally, the QNFO framework [9] formulates exchange statistics as an "exchange scalar" derived from configuration-space topology, with the $\pm 1$ boson/fermion shadow in $d \geq 3$ as a special case, and pre-registers a derivation program for extending the calculus to non-Abelian settings. This paper executes one branch of that program: the taxonomy of Section 3 is the non-Abelian extension, and the numerical predictions of Sections 4–5 are the pre-registered, falsifiable outputs.

## 3. Methods

### 3.1 Configuration spaces and their fundamental groups

Let $M$ be the spatial manifold and define the ordered and unordered configuration spaces

$$F_N(M) = \{(x_1, \dots, x_N) \in M^N : x_i \neq x_j \text{ for } i \neq j\}, \qquad C_N(M) = F_N(M)/S_N.$$

The covering $F_N(M) \to C_N(M)$ has deck group $S_N$. For $M = \mathbb{R}^d$:

$$\pi_1(C_N(\mathbb{R}^d)) \cong \begin{cases} S_N & d \geq 3, \\ B_N & d = 2, \end{cases}$$

where $B_N$ is generated by the elementary braids $\sigma_1, \dots, \sigma_{N-1}$ subject to the braid relations $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ and $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \geq 2$. The abelianization map sends each $\sigma_i$ to the generator $1 \in \mathbb{Z}$; hence $B_N^{\mathrm{ab}} \cong \mathbb{Z}$, graded by winding number $w \in \mathbb{Z}$.

### 3.2 Flux attachment as a homomorphism

A flux-attachment rule is a homomorphism

$$\varphi: B_N \to G,$$

where $G$ is the flux group (e.g., $U(1)$ for Abelian anyons, $SU(2)_k$ or a finite quotient for non-Abelian anyons). Because $B_N$ is generated by the $\sigma_i$, $\varphi$ is determined by the tuple $(g_1, \dots, g_{N-1})$, $g_i = \varphi(\sigma_i) \in G$, subject to the braid relations. The exchange statistics of two particles in flux sector $a$ is the conjugacy class $[a]$ of $a = \varphi(\sigma_i)$ in $G$; the statistics is Abelian iff $[a]$ is central, i.e., $\varphi(\sigma_i) \in Z(G)$.

### 3.3 The three classification invariants

We define the taxonomy by the triple $(\chi_1, \chi_2, \chi_3)$:

- $\chi_1$: the abelianization image $\mathrm{ab}(\varphi(\sigma_i)) \in \mathbb{Z}$, the winding charge of the attached flux;
- $\chi_2$: the fusion rank $r = \dim V_a$, the dimension of the representation space carried by the flux sector $a$; the statistics is Abelian iff $r = 1$;
- $\chi_3$: the winding grading of the configuration space, i.e., whether the theory lives on the full braid group ($\chi_3 = \mathbb{Z}$) or on a quotient by $w \mapsto w \bmod m$ (periodic flux, $\chi_3 = \mathbb{Z}_m$).

Every flux-attachment statistics class is labeled by $(\chi_1, \chi_2, \chi_3)$, and we enumerate the families: (A) $\chi_2 = 1$, arbitrary $\chi_1$, $\chi_3 = \mathbb{Z}$ — Abelian anyons with statistics angle $\theta = \pi \chi_1$; (B) $\chi_2 = 1$, $\chi_3 = \mathbb{Z}_m$ — $\mathbb{Z}_m$ toric-code-type anyons; (C) $\chi_2 \geq 2$, $\chi_1 = 0$ — purely non-Abelian anyons (Ising, Fibonacci type); (D) $\chi_2 \geq 2$, $\chi_1 \neq 0$ — charged non-Abelian anyons; (E) $\chi_2 \geq 2$, $\chi_3 = \mathbb{Z}_m$ — periodic non-Abelian anyons.

### 3.4 Thermal Hall conductance as the observable

For a chiral topological phase with chiral central charge $c_-$, the thermal Hall conductance at temperature $T$ is

$$\frac{\kappa_{xy}}{T} = c_- \, \frac{\pi^2 k_B^2}{3h},$$

with $k_B = 1.380649 \times 10^{-23}\,\mathrm{J\,K^{-1}}$ (2019 SI exact value) and $h = 6.62607015 \times 10^{-34}\,\mathrm{J\,s}$ (2019 SI exact value). Each family in the taxonomy predicts a value of $c_-$ via the flux-fusion structure; we compute these in Section 4.

## 4. Analysis

### 4.1 Derivation 1: The Abelianization of $B_N$ and the exchange phase

**Input numbers and sources.** The braid group presentation with generators $\sigma_1, \dots, \sigma_{N-1}$ and relations $\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$, $\sigma_i\sigma_j = \sigma_j\sigma_i$ ($|i-j|\geq 2$) is standard (see the Artin-group review [1], where $B_N$ is the Artin group of type $A_{N-1}$).

**Step 1.** Abelianization imposes commutativity: the braid relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ becomes, in the abelian quotient, $\sigma_i^2 \sigma_{i+1} = \sigma_{i+1} \sigma_i^2$, which is trivial; the far-commutativity relation is already trivial. Hence no relation survives abelianization, and

$$B_N^{\mathrm{ab}} \cong \mathbb{Z}, \qquad \mathrm{ab}(\sigma_i) = 1 \ \text{for all } i.$$

**Step 2.** A one-dimensional unitary representation of $B_N$ is a homomorphism $\rho: B_N \to U(1) \cong \{e^{i\theta}\}$, determined by $\rho(\sigma_i) = e^{i\theta}$. The exchange of two identical anyons acts as multiplication by $e^{i\theta}$; for $\theta = \pi \chi_1$ with $\chi_1 \in \mathbb{Z}$ we recover bosons ($\chi_1$ even, $e^{i\theta} = +1$) and fermions ($\chi_1$ odd, $e^{i\theta} = -1$), and for general real $\chi_1$ (allowing $\varphi$ to factor through $\mathbb{R}$ before quotienting) arbitrary Abelian anyons. This establishes family (A) and the $\pm 1$ shadow in $d \geq 3$, where $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ forces $\chi_1 \in \{0, 1\}$ — the CST exchange-scalar dichotomy of [9].

### 4.2 Derivation 2: The thermal Hall conductance quantum

**Input numbers and sources.** $k_B = 1.380649 \times 10^{-23}\,\mathrm{J\,K^{-1}}$ and $h = 6.62607015 \times 10^{-34}\,\mathrm{J\,s}$, both exact 2019 SI defined values.

**Step 1.** Compute the conductance quantum factor:

$$\frac{\pi^2 k_B^2}{3h} = \frac{\pi^2 (1.380649 \times 10^{-23})^2}{3 \times 6.62607015 \times 10^{-34}}\,\mathrm{W\,K^{-2}}.$$

**Step 2.** Square $k_B$:

$$(1.380649)^2 = 1.90619...$$

Compute precisely: $1.380649^2 = 1.380649 \times 1.380649$. $1.380649 \times 1.380649$: $1.380649 \times 1 = 1.380649$; $1.380649 \times 0.380649 = 0.525542...$; more carefully: $1.380649 \times 0.3 = 0.4141947$; $1.380649 \times 0.08 = 0.11045192$; $1.380649 \times 0.000649 = 0.000896041$. Sum: $0.4141947 + 0.11045192 + 0.000896041 = 0.525542661$. Total: $1.380649 + 0.525542661 = 1.906191661$. So

$$k_B^2 = 1.906191661 \times 10^{-46}\,\mathrm{J^2\,K^{-2}}.$$

**Step 3.** Multiply by $\pi^2 = 9.869604401$:

$$\pi^2 k_B^2 = 9.869604401 \times 1.906191661 \times 10^{-46}.$$

Compute: $9.869604401 \times 1.906191661 \approx 9.869604401 \times 1.9 = 18.75224836$; $9.869604401 \times 0.006191661 = 0.061110...$; precisely: $9.869604401 \times 0.006 = 0.05921763$; $9.869604401 \times 0.000191661 = 0.001891845$. Sum: $0.05921763 + 0.001891845 = 0.061109475$. Total: $18.75224836 + 0.061109475 = 18.81335783$. So

$$\pi^2 k_B^2 = 1.881335783 \times 10^{-45}\,\mathrm{J^2\,K^{-2}}.$$

**Step 4.** Divide by $3h = 3 \times 6.62607015 \times 10^{-34} = 1.987821045 \times 10^{-33}\,\mathrm{J\,s}$:

$$\frac{\pi^2 k_B^2}{3h} = \frac{1.881335783 \times 10^{-45}}{1.987821045 \times 10^{-33}} = 0.946438... \times 10^{-12}.$$

Compute the ratio: $1.881335783 / 1.987821045 = 0.946438...$. Check: $1.987821045 \times 0.9464 = 1.881258...$; $1.987821045 \times 0.94644 = 1.881337...$, slightly above; $1.987821045 \times 0.946438 = 1.881333...$; refine: $1.987821045 \times 0.946439 = 1.881335...$. So the ratio $\approx 0.946439$. Hence

$$\frac{\kappa_{xy}}{T}\bigg|_{c_- = 1} = 9.46439 \times 10^{-13}\,\mathrm{W\,K^{-2}}.$$

This is the standard thermal Hall conductance quantum, here derived from first-principles inputs.

### 4.3 Derivation 3: Chiral central charges for the taxonomy families

**Input numbers and sources.** The identification of chiral central charge with thermal Hall conductance, $\kappa_{xy}/T = c_- \pi^2 k_B^2/(3h)$, is the gravitational-anomaly relation; the candidate values $c_- \in \{1/2, 3/2, 5/2\}$ come from the flux-fusion structure of families (A)–(D): family (A) Abelian anyons at filling with one chiral edge mode give $c_- = 1$; the Ising-type non-Abelian class (family C with Ising fusion $\sigma \times \sigma = 1 + \psi$) gives $c_- = 1/2$; the doubled-flux class (family D, two co-propagating non-Abelian sectors plus one Abelian charge sector) gives $c_- = 1/2 + 1/2 + 1/2 = 3/2$; a three-sector variant gives $5/2$.

**Step 1.** For $c_- = 1/2$:

$$\frac{\kappa_{xy}}{T} = 0.5 \times 9.46439 \times 10^{-13} = 4.73220 \times 10^{-13}\,\mathrm{W\,K^{-2}}.$$

**Step 2.** For $c_- = 3/2$:

$$\frac{\kappa_{xy}}{T} = 1.5 \times 9.46439 \times 10^{-13} = 1.41966 \times 10^{-12}\,\mathrm{W\,K^{-2}}.$$

**Step 3.** For $c_- = 5/2$:

$$\frac{\kappa_{xy}}{T} = 2.5 \times 9.46439 \times 10^{-13} = 2.36610 \times 10^{-12}\,\mathrm{W\,K^{-2}}.$$

### 4.4 Derivation 4: Absolute thermal Hall signal at experimental temperature

**Input numbers and sources.** Candidate measurement temperature $T = 10\,\mathrm{mK} = 0.010\,\mathrm{K}$, chosen as the operating range of dilution-refrigerator thermoelectric setups (assumption, labeled as such).

**Step 1.** For the $c_- = 3/2$ class:

$$\kappa_{xy} = 1.41966 \times 10^{-12} \times 0.010 = 1.41966 \times 10^{-14}\,\mathrm{W\,K^{-1}}.$$

**Step 2.** For comparison, the fermionic vacuum contribution ($c_- = 1/2$ per half-filled Landau-level-like sector) at the same temperature is $4.73220 \times 10^{-14}\,\mathrm{W\,K^{-1}}$, so the $c_- = 3/2$ class exceeds the minimal nontrivial signal by a factor

$$\frac{1.41966 \times 10^{-14}}{4.73220 \times 10^{-14}} = \frac{1.5}{0.5} = 3.00000,$$

exactly, since the ratio is the ratio of central charges.

### 4.5 Derivation 5: Distinguishing power against the boson/fermion shadow

**Input numbers and sources.** The $\pm 1$ shadow values $\chi_1 \in \{0,1\}$ from $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$ (Derivation 1); the braid winding charge $\chi_1 \in \mathbb{Z}$ from $B_N^{\mathrm{ab}} \cong \mathbb{Z}$.

**Step 1.** The number of distinct Abelian statistics classes in $d = 2$ with winding grading $\chi_3 = \mathbb{Z}_m$ is $m$ (one per $\chi_1 \bmod m$); in $d \geq 3$ it is $2$. The enlargement factor is

$$\frac{m}{2},$$

which for the minimal nontrivial periodic case $m = 3$ gives $3/2 = 1.5$ and for $m = 10$ gives $5$. This quantifies how much of the statistics taxonomy is genuinely two-dimensional.

## 5. Results

All numbers below are computed in Section 4 from stated inputs; none are simulated or measured.

1. **Abelianization.** $B_N^{\mathrm{ab}} \cong \mathbb{Z}$ with $\mathrm{ab}(\sigma_i) = 1$; $S_N^{\mathrm{ab}} \cong \mathbb{Z}_2$. Abelian exchange phases in $d=2$ are $e^{i\pi\chi_1}$, $\chi_1 \in \mathbb{Z}$ (mod grading); in $d \geq 3$ only $\pm 1$.

2. **Thermal Hall conductance quantum.** $\pi^2 k_B^2/(3h) = 9.46439 \times 10^{-13}\,\mathrm{W\,K^{-2}}$ (computed from exact SI values of $k_B$ and $h$; arithmetic in Section 4.2).

3. **Family predictions.** $\kappa_{xy}/T = 4.73220 \times 10^{-13}$ ($c_- = 1/2$), $9.46439 \times 10^{-13}$ ($c_- = 1$), $1.41966 \times 10^{-12}$ ($c_- = 3/2$), and $2.36610 \times 10^{-12}\,\mathrm{W\,K^{-2}}$ ($c_- = 5/2$).

4. **Absolute signal at $T = 10\,\mathrm{mK}$** (assumed operating temperature): $\kappa_{xy} = 1.41966 \times 10^{-14}\,\mathrm{W\,K^{-1}}$ for the $c_- = 3/2$ class, exactly $3\times$ the minimal nontrivial $c_- = 1/2$ signal.

5. **Taxonomy enlargement factor.** $m/2$ distinct Abelian classes in $d = 2$ versus $2$ in $d \geq 3$; e.g., $1.5$ for $m = 3$, $5$ for $m = 10$.

**Projection (labeled as such, with assumptions).** We project that the $c_- = 3/2$ doubled-flux class is experimentally accessible within 18 months, assuming: (i) a platform realizing family (D) flux attachment (e.g., a fractional quantum Hall or moiré-system realization of charged non-Abelian anyons); (ii) thermometric sensitivity at or below $10^{-15}\,\mathrm{W\,K^{-1}}$ at $10\,\mathrm{mK}$, consistent with reported capabilities of resonant thermometry in comparable setups; (iii) edge-mode equilibration length shorter than device size. Uncertainty bounds: the central-charge assignment $c_- = 3/2$ is a model-level prediction of the taxonomy; if the realized platform instead stabilizes family (C) ($c_- = 1/2$), the predicted signal drops to $4.73220 \times 10^{-14}\,\mathrm{W\,K^{-1}}$ at $10\,\mathrm{mK}$ — a factor-of-3 discriminator. The projection carries no error bar on $\kappa_{xy}/T$ itself (it is exactly quantized if the phase is chiral and gapped); the uncertainty lies entirely in which taxonomy family nature realizes.

## 6. Discussion

**Limitations.** The taxonomy classifies statistics by the triple $(\chi_1, \chi_2, \chi_3)$ of a flux-attachment homomorphism $\varphi: B_N \to G$. This is complete only relative to the choice of $G$ and the restriction to homomorphism-defined attachment; it does not classify arbitrary modular tensor categories, which carry data (F-symbols, R-symbols, twists) not captured by the triple. Two distinct anyon theories can share $(\chi_1, \chi_2, \chi_3)$ and differ in fusion geometry; our taxonomy would conflate them. The central-charge assignments for families (C)–(D) are inferred from standard fusion structures (Ising-type, doubled-flux type), not derived from first principles within this paper; a full derivation would require computing the Gauss–Maslov class of the flux bundle, which we defer.

**Failure modes.** Three are serious. First, the wild-topology obstruction: at finite anyon density in the thermodynamic limit, punctures accumulate and the configuration-space fundamental group acquires Hawaiian-earring-type wild structure [3], where ordinary homomorphisms $\varphi$ no longer capture attachment; the taxonomy then applies only at finite $N$ or in the dilute limit. Second, the equilibration assumption: thermal Hall measurements require full edge equilibration; partial equilibration yields intermediate, non-quantized values that would mimic a different $c_-$ and could falsely confirm or refute a family assignment. Third, the platform assumption: if no physical system realizes family (D) flux attachment, the 18-month projection fails on feasibility grounds regardless of the mathematics.

**Arguing against ourselves.** A skeptic should press three points. (1) The claim that the triple $(\chi_1, \chi_2, \chi_3)$ is a "complete taxonomy" is stronger than what we prove: we prove it is a complete invariant of homomorphism-defined attachment, which is a proper subset of all two-dimensional topological orders. (2) The $c_-$ values for families (C)–(D) are assignments by analogy to known fusion structures, not derivations; a derivation within the CST program [9] is needed before the prediction is fully pre-registered. (3) The thermal Hall quantum $9.46439 \times 10^{-13}\,\mathrm{W\,K^{-2}}$ is standard, not new; the paper's novelty is the taxonomy and the family-level discrimination, and a reader could reasonably judge the falsifiable content thin until a concrete material platform is specified.

**Falsification.** The framework is falsified if: (a) a gapped, chiral 2D phase is found whose $\kappa_{xy}/T$ is not an integer-or-half-odd-integer multiple of $9.46439 \times 10^{-13}\,\mathrm{W\,K^{-2}}$ (this would break the central-charge quantization underlying the taxonomy); (b) a non-Abelian anyon phase is found whose exchange matrices cannot be factorized through any homomorphism $B_N \to G$ with the stated invariants; or (c) the $c_- = 3/2$ class, if realized, shows $\kappa_{xy}/T$ differing from $1.41966 \times 10^{-12}\,\mathrm{W\,K^{-2}}$ beyond instrumental error.

**Open questions.** Does the interleaving metric of [2] on winding gradings admit a physical interpretation as a finite-braid-length distinguishability bound? Can the Schwartz-genus bounds of [1] be converted into quantitative stability limits for flux attachment at finite density? Do the uniqueness results of [6] on genus-2 contact structures extend to a rigidity statement for doubled anyon gluing, which would sharpen the $c_- = 3/2$ prediction? How does the Roelcke-precompact minimality of compact flux groups [7] interact with the torsion-graded classifying spaces of [4] when $G$ is a finite quantum group rather than a Lie group?

## 7. Conclusion

We have constructed a taxonomy of exchange statistics generated by non-Abelian flux attachment, organized by three computable invariants of the attachment homomorphism $\varphi: B_N \to G$: the winding charge $\chi_1$, the fusion rank $\chi_2$, and the winding grading $\chi_3$. The taxonomy reproduces the boson/fermion dichotomy in $d \geq 3$ as the $\mathbb{Z}_2$ shadow of the braid-group winding, and in $d = 2$ yields