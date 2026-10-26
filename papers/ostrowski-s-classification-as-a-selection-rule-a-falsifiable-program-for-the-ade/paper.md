# Ostrowski's Classification as a Selection Rule: A Falsifiable Program for the Adelic Shadow of the Standard Model Gauge Group

## Abstract

Ostrowski's theorem classifies the completions of the rational numbers $\mathbb{Q}$: exactly one Archimedean completion, $\mathbb{R}$, and one $p$-adic completion $\mathbb{Q}_p$ for each prime. Theoretical physics uses only the first. A conjecture in the adelic physics program holds that the observed gauge group $SU(3)_c \times SU(2)_L \times U(1)_Y$ is the Archimedean shadow of a symmetry structure defined over all places of $\mathbb{Q}$, and that coupling constants and particle representations must satisfy adelic consistency conditions. The gap this paper addresses is that the conjecture has never been stated with explicit falsification criteria tied to existing experimental precision budgets. We formulate three tests: automorphic embedding of the Standard Model on the adele ring, coupling constraints from adelic product formulas, and Bruhat–Tits tree dynamics checked against frequency-space physics. We verify the product formula $\prod_v |q|_v = 1$ explicitly ($q = 60$: $60 \cdot 2^{-2} \cdot 3^{-1} \cdot 5^{-1} = 1$), independently reproduce the tabulated QED one-loop coefficient $\beta_0 = 2/\pi = 0.636620$, derive that the global gauge-group ambiguity an adelic selection rule must resolve is finite of order $6$, and compute a quantitative visibility bound for the proposed collider prime-clustering signature: at the documented $10\%$ jet systematic floor, a null result excludes a Möbius-weighted amplitude coefficient $a \geq 0.20$ at harmonic $n = 2$. The program adds no new symmetry beyond Ostrowski's classification, and its failure modes are internal and algebraic as well as experimental.

## 1. Introduction

Particle phenomenologists who build models of physics beyond the Standard Model face a decision today that no accepted principle resolves: the global form of the gauge group. The Lie algebra of the Standard Model is fixed, but the group $\tilde{G} = SU(3)_c \times SU(2)_L \times U(1)_Y$ and its quotient by a subgroup of order $6$ are physically distinct theories, differing in which heavy particles they permit [5]. Every proposal for a heavy exotic particle, and every unification scenario that introduces new matter, inherits this ambiguity. The cost is concrete: model builders cannot determine whether a candidate spectrum is internally consistent without knowing the faithful gauge group, and the ambiguity propagates into the interpretation of collider searches for the heavy particles that would pin the global form down [5].

A second, older decision sits underneath the first. Theoretical physics takes the real numbers $\mathbb{R}$ as the number system for coordinates, field values, coupling constants, and probability amplitudes. Ostrowski's theorem shows this choice is not forced: the rational numbers $\mathbb{Q}$ admit exactly one Archimedean completion and one $p$-adic completion for each prime, and these are all the completions [8], [9], [10]. If the restriction to the real place is an unstated assumption rather than a physical principle, then a unification route exists that adds no new symmetry at all: it merely removes the assumption that physics lives at one place of $\mathbb{Q}$. The adelic program proposes precisely this — that the full symmetry group of physics is adelic, with the observed gauge group being the Archimedean shadow of a product structure over all places [8], [10].

What changes if the conjecture holds is the selection principle itself. A demonstrated adelic consistency condition on coupling constants would fix the global form of the gauge group as a by-product, because the condition is formulated over the adele ring $\mathbb{A}_\mathbb{Q}$, where the discrete quotient ambiguity has no place to hide. What changes if the conjecture fails is equally valuable: part of the failure would be an internal, algebraic falsification requiring no new experiment, establishing that Ostrowski's classification constrains arithmetic but not physics.

This paper converts the conjecture from a research-program statement into a testable protocol. The contributions are:

- A precise three-part statement of the adelic shadow conjecture — automorphic embedding, adelic coupling constraints, and Bruhat–Tits tree dynamics — each with an explicit falsification condition (Section 3).
- An explicit verification of the adelic product formula $\prod_v |q|_v = 1$ with full arithmetic, an independent reproduction of the tabulated QED one-loop coefficient $\beta_0 = 2/\pi = 0.636620$, and a derivation that the gauge-group ambiguity an adelic selection rule must resolve is finite of order $6$ (Section 4).
- A quantitative visibility threshold for the proposed collider prime-clustering signature: at the $10\%$ jet systematic uncertainty floor documented for hadron-collider QCD analyses [1], a null result excludes a Möbius-weighted amplitude coefficient $a \geq 0.20$ at harmonic $n = 2$ (Section 4).
- The echo-delay spectrum $\Delta t_n = 4M \ln n$ in units of the mass scale $M$, with the Möbius amplitude hierarchy $|\mu(n)|/n$, as the gravitational-wave counterpart of the same threshold logic (Section 4).
- A falsification protocol that imports the statistical discipline of an existing honest negative result in the adelic program — five hundred zeta zeros, Bonferroni correction, permutation null — into the three tests (Sections 3 and 6).

## 2. Background and Related Work

The empirical anchor for any collider test of adelic substructure is the state of QCD precision at hadron colliders. The Tevatron Run 2 experiments each accumulated over $1\;\mathrm{fb}^{-1}$ of high-transverse-momentum data, enabling comparisons between theory and experiment at the few-percent level, and the report of the QCD working group documents that jet systematic uncertainties stood at the $10\%$ to $50\%$ level with the explicit goal of pushing below $10\%$ [1]. The same report establishes that the seedless cone algorithm is infrared-safe while seeds introduce undesirable infrared sensitivity in theoretical calculations, and that cone and $k_T$ algorithms provide useful cross-checks at the LHC [1]. Two points from this work carry directly into the present program: the $10\%$ systematic floor is the visibility threshold any new jet substructure must beat, and the lesson that algorithmic choices (seeds, merge parameters $f_{\mathrm{merge}}$ and $p_{T,\min}$) silently shape rates is a warning for how an adelic fractal signature could be hidden or manufactured by analysis choices [1].

The mathematical technology for the third test — Bruhat–Tits tree dynamics — is the theory of groups acting on graphs and on non-positively curved spaces. A new bound for the rank of the intersection of finitely generated subgroups of a free group, formulated topologically in the spirit of Stallings via coverings and their pullbacks, contributes to the strengthened Hanna Neumann conjecture [2]. This matters here because Bruhat–Tits trees are graphs, and the way subgroups of tree-acting groups intersect controls whether an Archimedean symmetry and a $p$-adic symmetry can share a common quotient; rank bounds of the type proved in [2] are the quantitative form of that control. On the geometric side, the survey of groups acting on CAT(0) spaces establishes rigidity results that constrain any dynamics placed on $p$-adic buildings: any crystallographic group acting discretely and cocompactly on $\mathbb{R}^n$ contains an Abelian group $\mathbb{Z}^n$ of finite index, with finitely many isomorphism classes, and a free Abelian group of rank $n$ acting properly by semi-simple isometries on a CAT(0) space yields a flat torus theorem [7]. Since Bruhat–Tits buildings are CAT(0), these rigidity theorems apply to adelic dynamics and forbid large classes of would-be adelic symmetry groups before any physics is imposed [7].

The gauge-group ambiguity that motivates the whole program is documented precisely in the SMEFT analysis of the Standard Model gauge group. A specific $\mathbb{Z}_6$ subgroup of $\tilde{G} = SU(3)_c \times SU(2)_L \times U(1)_Y$, generated by the centers of $SU(3)_c$ and $SU(2)_L$ combined with a specific rotation of $U(1)_Y$, acts trivially on all Standard Model fields, so the faithful gauge group remains undetermined by Standard Model data alone [5]. The toy model of $SU(2)$ versus $SO(3) = SU(2)/\mathbb{Z}_2$ shows the two theories differ physically in their allowed line operators and matter spectra [5]. The resolution route is empirical: heavy particles not invariant under the $\mathbb{Z}_6$ subgroup would pin down the faithful group, and measuring the mass scale of the lightest such exotic particle is equivalent to measuring the scale at which the electric one-form global symmetry acting on Wilson lines is explicitly broken [5]. An adelic selection rule, if valid, would resolve the same ambiguity algebraically; Section 4 derives that the ambiguity has order $6$.

If $p$-adic places carry their own compact gauge-like groups, their central extensions are classified by Schur multipliers, and the explicit determination of the Schur multiplier of special $p$-groups of rank $2$ supplies the relevant machinery [6]. For a special $p$-group with minimal generating set of size $d$, the derived bounds are $p^{\frac{1}{2}d(d-1)-2} \leq |\operatorname{M}(G)| \leq p^{\frac{1}{2}d(d-1)-1}$, together with the capability dichotomy: the group is capable (realizable as $H/\operatorname{Z}(H)$) precisely when its epicenter is trivial [6]. These results constrain which finite $p$-groups can appear as internal symmetry groups at $p$-adic places, and Section 4 evaluates the bound at $d = 3$ as a worked example.

The adelic program's own foundations supply the conjecture and its predicted signatures. The adelic-distinction framework argues that the restriction of physics to the real place is an unstated assumption that Ostrowski's theorem exposes as optional, that the idele class group is the single object whose automorphic representations should generate gauge symmetries, particle species, and cosmological parameters, and that the product formula $\prod_v |q|_v = 1$ is the invariant enforcing conservation laws, charge quantization, and CPT symmetry [8]. Its experimental-signatures section lists four falsifiable predictions: gravitational-wave echo delays $\Delta t_n = 4M \ln n$ for $n$ a product of small primes with amplitudes proportional to $\mu(n)/n$; a parity-violating CMB $C_l^{EB}$ component tied to prime harmonic sums; fractal, prime-number clustering of jet energy deposits at sufficiently high energies; and quantum simulation of the adelic Ising model on a Bruhat–Tits tree using qudits [8]. The framework is explicitly described as a research program, not a completed theory [8].

The quantitative discipline of the program has already been tested once, negatively. The Phase 1 adelic-constraints project asked whether adelic structure fixes fundamental constants, ran the numerological hypothesis that zeta-zero gap ratios match particle mass ratios through a proper analysis — five hundred zeta zeros, Bonferroni correction for multiple comparisons, a permutation null model — and statistically falsified all three candidate matches, concluding that mathematical beauty does not imply physical truth and that the boundary between mathematical property and numerology is drawn by statistical rigor [9]. Its master table reports an adelic product formula error below $10^{-12}$, an adelic beta constraint error $\max\|\beta_\infty + \sum \beta_p\|$ below $10^{-13}$, a Veneziano beta at the symmetric point $\beta_\infty(0.5) = -5.372183$, a QED one-loop coefficient $\beta_0 = 2/\pi = 0.636620$, and a compactification ratio $R(0.5) = 8.438606$ [9]. Section 4 independently checks the $\beta_0$ entry against its stated formula.

The broader consilience case is assembled in two synthesis documents. The consilience paper organizes the convergence of quantum mechanics, quantum field theory, and the Standard Model spectrum with Ostrowski's theorem, Tate's thesis, the zeta function, and Bruhat–Tits buildings around a four-component kernel — valuation theory, the adele ring, Bruhat–Tits trees, and the adelic product formula $\prod_v |\lambda|_v = 1$ — and states Ostrowski's theorem as a selection rule: every consistent physical theory using distance or magnitude must specify which completions of $\mathbb{Q}$ its dynamics operate in, and current physics implicitly chooses only the $\infty$-completion [10]. It further records that adelic quantum mechanics is form-invariant under interchange of $\mathbb{R}$ and $\mathbb{Q}_p$, so physics can be formulated across completions without internal contradiction [10]. The five-pillars synthesis documents five independent research lines converging on the same adelic core, including a cryptographic primitive built on $b$-adic valuation (silent radix encryption, infeasible brute force for $b \sim 2^{128}$) and a classification of quantum error-correcting code families by Kodaira–Néron fibers at $83\%$ accuracy, while marking the physical claims as speculative with no $p$-adic experimental signature confirmed and seven falsifiable predictions with quantitative thresholds [11]. The $83\%$ classification figure is the only quantitative, checkable hit rate in the program to date, and it demonstrates that adelic-valued structure can be tested against data at all [11].

Two cautionary results from pure mathematics bound what the program may assume. The unit conjecture for group rings — that for a torsion-free group $G$ the only units of $K[G]$ are the trivial ones — was disproved by a concrete counterexample: a torsion-free, virtually abelian group $P$ with presentation $\langle a,b \mid b^{-1}a^2b = a^{-2},\ a^{-1}b^2a = b^{-2} \rangle$ over the field of order two, whose group ring contains non-trivial units; the group of units is not finitely generated, and finding non-trivial units in characteristic zero remains open [3]. The lesson for the adelic program is that universality conjectures about algebraic structures associated to groups can fail even in the virtually abelian case, so the assumption that adelic group algebras behave uniformly across places must be tested, not presumed [3]. Similarly, the Andrews–Curtis and Nielsen equivalence machinery — elementary Nielsen moves on generating tuples, the class $\mathfrak{C}$ of groups in which every maximal subgroup is normal and every normally generating set is a generating set, and the open transitivity question of $\operatorname{Aut}F_n$ on $\operatorname{Epi}(F_n, G)$ — provides the tools for checking whether candidate gauge-group presentations at different places are equivalent, with the known result that the Akbulut–Kirby candidate pairs become Andrews–Curtis equivalent in every abelian group, so abelian images cannot distinguish them [4]. Any adelic embedding proof that reduces to presentation equivalence must therefore use non-abelian test groups [4].

## 3. Methods

The conjecture under test is stated in three parts, each with a falsification condition.

**Test T1: Automorphic embedding.** The Standard Model gauge group $SU(3)_c \times SU(2)_L \times U(1)_Y$ with its chiral matter content should be realizable as the local component at the Archimedean place of an automorphic representation on the adele ring $\mathbb{A}_\mathbb{Q}$ or the idele class group, in the sense of the adelic-distinction framework [8]. Concretely, there should exist an automorphic representation whose $\infty$-component reproduces the Standard Model representation data $(R_3, R_2, Q_Y)$ — the color representation $R_3$, the weak representation $R_2$, and the hypercharge assignments $Q_Y$ — for one full generation of quarks and leptons. Falsification condition: a constructive search over automorphic representations on $\mathbb{A}_\mathbb{Q}$ (or a structural argument in the spirit of the CAT(0) rigidity theorems [7]) shows that no such representation exists, or that every candidate fails to reproduce the chiral matter content. Because presentation-equivalence checks in abelian images cannot distinguish candidates [4], the search must use non-abelian test groups.

**Test T2: Adelic coupling constraints.** Each gauge coupling $g$ admits local components $\{g_v\}$ over the places $v$ of $\mathbb{Q}$, and the adelic consistency condition is the product formula $\prod_v |g_v|_v = 1$, by analogy with the product formula for adeles that the adelic-distinction framework identifies as the invariant enforcing conservation laws and charge quantization [8]. Falsification condition: a measured set of coupling values, propagated to local components, violates the product constraint by more than the combined experimental and theoretical uncertainty. As a prerequisite, the arithmetic machinery of the program must be internally consistent; Section 4 checks the tabulated QED one-loop coefficient $\beta_0 = 2/\pi$ against its own formula [9].

**Test T3: Bruhat–Tits tree dynamics against frequency-space physics.** Dynamics on the $p$-adic places, modeled on Bruhat–Tits trees, should produce the frequency-space signatures listed in the adelic-distinction framework: gravitational-wave echo delays $\Delta t_n = 4M \ln n$ with amplitudes proportional to $\mu(n)/n$, prime harmonic structure in the parity-violating CMB $C_l^{EB}$ spectrum, and prime-number clustering of jet energy deposits at sufficiently high energies [8]. Falsification condition: null results in the corresponding searches past the visibility thresholds derived in Section 4, analyzed with the statistical discipline established in the Phase 1 study — large pre-registered look-elsewhere correction (five hundred zeta zeros there), Bonferroni correction, and a permutation null model [9].

The statistical protocol is part of the method, not an afterthought. The Phase 1 result shows that adelic-flavored numerology fails when subjected to standard multiple-comparisons discipline [9]; any positive claim in T2 or T3 must survive the same treatment before it counts as evidence for the conjecture.

## 4. Analysis

This section carries out every derivation with the input numbers stated and the arithmetic shown. Four computations are performed: the adelic product formula at $q = 60$, the reproduction of the tabulated QED one-loop coefficient, the order of the gauge-group ambiguity, and the collider visibility threshold, followed by the echo-delay spectrum and a worked Schur-multiplier bound.

### 4.1 The adelic product formula at $q = 60$

The product formula states that for every nonzero rational $q$,

$$\prod_v |q|_v = 1,$$

where the product runs over all places $v$ of $\mathbb{Q}$: the Archimedean place $\infty$ with $|q|_\infty$ the ordinary absolute value, and one $p$-adic place for each prime with $|q|_p = p^{-\nu_p(q)}$, where $\nu_p(q)$ is the exponent of $p$ in the factorization of $q$ [8], [10]. We verify this explicitly for $q = 60$.

**Input numbers.** The prime factorization of $60$ is $60 = 2^2 \cdot 3 \cdot 5$. All other primes $p \geq 7$ satisfy $\nu_p(60) = 0$, so $|60|_p = p^0 = 1$ and they do not affect the product.

**Local norms.**

$$|60|_\infty = 60, \qquad |60|_2 = 2^{-2} = \frac{1}{4}, \qquad |60|_3 = 3^{-1} = \frac{1}{3}, \qquad |60|_5 = 5^{-1} = \frac{1}{5}.$$

**Product.**

$$\prod_v |60|_v = 60 \cdot \frac{1}{4} \cdot \frac{1}{3} \cdot \frac{1}{5} = \frac{60}{4 \cdot 3 \cdot 5} = \frac{60}{60} = 1.$$

The formula holds exactly, with no rounding at any step, because the exponents in the factorization cancel the Archimedean magnitude term by term. This is the invariant that the adelic-distinction framework identifies as enforcing conservation laws and charge quantization [8], and it is the template for the coupling constraint of Test T2.

### 4.2 Reproduction of the QED one-loop coefficient

The Phase 1 adelic-constraints study tabulates a QED one-loop coefficient $\beta_0 = 2/\pi = 0.636620$ in its master table [9]. We check this entry against its stated closed form.

**Input numbers.** The closed form is $\beta_0 = 2/\pi$; the tabulated decimal is $0.636620$ [9]. We use $\pi = 3.14159265358979$.

**Computation.**

$$\beta_0 = \frac{2}{\pi} = \frac{2}{3.14159265358979} = 0.63661977236758.$$

Rounding to the six decimal places of the tabulated entry:

$$0.63661977236758 \approx 0.636620.$$

The tabulated value is the correctly rounded form of $2/\pi$; the residual is $|0.636620 - 0.63661977236758| = 2.28 \times 10^{-7}$, which is below the half-unit of the last displayed digit ($5 \times 10^{-7}$). The internal consistency check required by Test T2 passes: the program's quantitative tables reproduce their own stated formulas [9].

### 4.3 The order of the gauge-group ambiguity

Test T2's payoff condition is that an adelic selection rule resolves the global form of the gauge group. We derive the size of the ambiguity it must resolve, from the $\mathbb{Z}_6$ subgroup documented in the SMEFT analysis [5].

**Setup.** The naive gauge group is $\tilde{G} = SU(3)_c \times SU(2)_L \times U(1)_Y$. A specific subgroup $\mathbb{Z}_6 \subset \tilde{G}$ acts trivially on all Standard Model fields, so Standard Model data alone cannot distinguish $\tilde{G}$ from $\tilde{G}/\mathbb{Z}_6$ [5].

**Generator.** The trivially acting element combines the center of $SU(3)_c$, which has order $3$, with the center element of $SU(2)_L$, which has order $2$, together with a compensating $U(1)_Y$ rotation. Write the generator as $g = (c_3, c_2, e^{i\alpha})$ with $c_3^3 = 1$, $c_2^2 = 1$.

**Order computation.** The order of $g$ is the least common multiple of the orders of its effective components:

$$\operatorname{ord}(g) = \operatorname{lcm}(3, 2) = 6.$$

Explicitly, $g^1 \neq 1$, $g^2 = (c_3^2, 1, e^{2i\alpha}) \neq 1$ since $c_3^2 \neq 1$, $g^3 = (1, c_2, e^{3i\alpha}) \neq 1$ since $c_2 \neq 1$, and $g^6 = (c_3^6, c_2^6, e^{6i\alpha}) = (1, 1, 1)$. No smaller power is trivial, so the subgroup generated has order $6$.

**Conclusion.** The ambiguity an adelic selection rule must resolve is finite of order $6$: the faithful gauge group is either $\tilde{G}$ or its quotient by this $\mathbb{Z}_6$, and no other global form is compatible with the trivial action on Standard Model fields [5]. The toy model of Section 2 — $SU(2)$ versus $SO(3) = SU(2)/\mathbb{Z}_2$, physically distinct in their allowed line operators and matter spectra [5] — shows that this quotient is a physical distinction, not a notation issue.

### 4.4 Collider visibility threshold for the prime-clustering signature

The adelic-distinction framework predicts fractal, prime-number clustering of jet energy deposits at sufficiently high energies [8]. We derive the amplitude coefficient that a null search excludes, using the jet systematic floor documented for hadron-collider QCD analyses.

**Input numbers.**
- Systematic uncertainty floor for jet observables: $\sigma_{\mathrm{sys}} = 0.10$ (the report documents jet systematics at the $10\%$ to $50\%$ level with the goal of pushing below $10\%$, and states that precision much better than $10\%$ is not yet guaranteed) [1].
- Harmonic index: $n = 2$.
- Möbius weight: $\mu(2) = -1$, so $|\mu(2)|/2 = 1/2$.
- Parametrization: the prime-clustering modulation of the jet amplitude is assumed to take the Möbius-weighted form $\delta_n = a \cdot |\mu(n)|/n$, where $a$ is the dimensionless amplitude coefficient of the adelic signature. This parametrization is the paper's working assumption, following the amplitude hierarchy stated for the echo signature in [8].

**Visibility condition.** We assume the standard single-observable visibility rule: a modulation is detectable only if its size reaches the dominant systematic uncertainty, $\delta_n \geq \sigma_{\mathrm{sys}}$. At $n = 2$:

$$\delta_2 = a \cdot \frac{|\mu(2)|}{2} = a \cdot \frac{1}{2} = \frac{a}{2}.$$

Setting $\delta_2 \geq \sigma_{\mathrm{sys}} = 0.10$:

$$\frac{a}{2} \geq 0.10 \quad \Longrightarrow \quad a \geq 0.20.$$

**Interpretation.** A null search for prime clustering at harmonic $n = 2$, analyzed at the current $10\%$ systematic floor, excludes any Möbius-weighted amplitude coefficient $a \geq 0.20$. Conversely, the signature is visible today only if $a \geq 0.20$; any coefficient below this bound hides beneath the systematic floor and must wait for sub-$10\%$ systematics [1]. The same logic transfers to other harmonics: at $n = 6$, $|\mu(6)|/6 = 1/6$, and the visibility condition $\delta_6 \geq 0.10$ requires $a \geq 0.60$ — the Möbius hierarchy $|\mu(n)|/n$ makes higher harmonics progressively harder to see, so $n = 2$ is the most sensitive channel.

### 4.5 The echo-delay spectrum

The gravitational-wave counterpart signature is the echo delay $\Delta t_n = 4M \ln n$ for $n$ a product of small primes, with amplitudes proportional to $\mu(n)/n$ [8]. We tabulate the delays in units of the mass scale $M$ and the amplitude weights, with the arithmetic shown.

**Input numbers.** $\ln 2 = 0.693147$, $\ln 3 = 1.098612$, $\ln 5 = 1.609438$, $\ln 6 = 1.791759$; $\mu(2) = -1$, $\mu(3) = -1$, $\mu(5) = -1$, $\mu(6) = 1$ (one prime factor each for $2, 3, 5$; two distinct prime factors for $6$).

**Delays.**

$$\Delta t_2 = 4M \ln 2 = 4M \times 0.693147 = 2.772588\,M,$$

$$\Delta t_3 = 4M \ln 3 = 4M \times 1.098612 = 4.394449\,M,$$

$$\Delta t_5 = 4M \ln 5 = 4M \times 1.609438 = 6.437752\,M,$$

$$\Delta t_6 = 4M \ln 6 = 4M \times 1.791759 = 7.167036\,M.$$

**Amplitude weights.**

$$\frac{|\mu(2)|}{2} = 0.5, \qquad \frac{|\mu(3)|}{3} = 0.333333, \qquad \frac{|\mu(5)|}{5} = 0.2, \qquad \frac{|\mu(6)|}{6} = 0.166667.$$

The delay spectrum is logarithmic in $n$ while the amplitude hierarchy falls as $1/n$ times the Möbius function, so the earliest, largest echo ($n = 2$, at $2.772588\,M$ with relative weight $0.5$) dominates the detectable signal. Note that $\Delta t_6 = \Delta t_2 + \Delta t_3$ exactly, since $\ln 6 = \ln 2 + \ln 3$: the spectrum has built-in additive structure that a search can exploit as a self-consistency check, and that a spurious instrumental echo would not generically satisfy.

### 4.6 Worked Schur-multiplier bound at $d = 3$

If $p$-adic places carry compact internal symmetry groups, their central extensions are controlled by Schur multipliers [6]. For a special $p$-group with minimal generating set of size $d$, the derived bounds are

$$p^{\frac{1}{2}d(d-1)-2} \leq |\operatorname{M}(G)| \leq p^{\frac{1}{2}d(d-1)-1}.$$

At $d = 3$ and $p = 2$:

$$\frac{1}{2} \cdot 3 \cdot 2 - 2 = 3 - 2 = 1, \qquad \frac{1}{2} \cdot 3 \cdot 2 - 1 = 3 - 1 = 2,$$

so

$$2^1 = 2 \leq |\operatorname{M}(G)| \leq 2^2 = 4.$$

A rank-$2$ special $2$-group on three generators has a Schur multiplier of order $2$ or $4$; the capability dichotomy — the group is capable precisely when its epicenter is trivial [6] — then decides whether it can appear as $H/\operatorname{Z}(H)$, i.e., as the internal symmetry of a $p$-adic place written as a central quotient. This is a concrete, checkable constraint on the building blocks of Test T3.

## 5. Results

The analysis yields five results, each with its derivation in Section 4.

**R1 (product formula).** The adelic product formula holds exactly at $q = 60$: $60 \cdot 2^{-2} \cdot 3^{-1} \cdot 5^{-1} = 1$, with no rounding (Section 4.1). The invariant that the adelic program proposes as the enforcement mechanism for conservation laws [8] is arithmetically sound.

**R2 (internal consistency).** The tabulated QED one-loop coefficient $\beta_0 = 0.636620$ [9] is the correctly rounded value of its stated closed form $2/\pi = 0.63661977236758$, with residual $2.28 \times 10^{-7}$ below the rounding half-unit (Section 4.2). The program's quantitative tables pass their own consistency check.

**R3 (ambiguity order).** The global gauge-group ambiguity that an adelic selection rule must resolve is finite of order $6$, generated by an element combining the order-$3$ center of $SU(3)_c$ and the order-$2$ center of $SU(2)_L$ (Section 4.3) [5].

**R4 (visibility threshold).** At the documented $10\%$ jet systematic floor [1], under the visibility rule $\delta_n \geq \sigma_{\mathrm{sys}}$ and the Möbius-weighted parametrization $\delta_n = a|\mu(n)|/n$, a null search at harmonic $n = 2$ excludes $a \geq 0.20$; the corresponding threshold at $n = 6$ is $a \geq 0.60$ (Section 4.4). The $n = 2$ channel is the most sensitive because $|\mu(2)|/2 = 0.5$ is the largest weight in the hierarchy.

**R5 (echo spectrum).** The echo delays in units of $M$ are $\Delta t_2 = 2.772588\,M$, $\Delta t_3 = 4.394449\,M$, $\Delta t_5 = 6.437752\,M$, $\Delta t_6 = 7.167036\,M$, with amplitude weights $0.5$, $0.333333$, $0.2$, $0.166667$, and the exact additive relation $\Delta t_6 = \Delta t_2 + \Delta t_3$ (Section 4.5).

**R6 (Schur bound).** For a special $2$-group on $d = 3$ generators, $2 \leq |\operatorname{M}(G)| \leq 4$ (Section 4.6) [6].

All of R1–R6 are exact algebraic or arithmetic consequences of stated inputs; none involves simulation or fitted data. R4 is the only result whose input ($\sigma_{\mathrm{sys}} = 0.10$) is an empirical documentation from a collider analysis [1], and its assumption (the visibility rule and the Möbius parametrization) is stated explicitly.

## 6. Discussion

**What the results do and do not establish.** R1 and R2 establish that the adelic program's arithmetic core is internally consistent; they do not establish that physics is adelic. R3 establishes the size of the prize: resolving the order-$6$ ambiguity algebraically would be a genuine selection principle that no current framework provides [5]. R4 and R5 convert two predicted signatures into thresholds that existing and near-term analyses can act on. None of these results confirms the conjecture; they make it falsifiable.

**Failure modes.** The program has three distinct failure modes, and it is a strength of the formulation that they are separable. First, an internal algebraic failure: the constructive search of Test T1 finds no automorphic representation on $\mathbb{A}_\mathbb{Q}$ reproducing the chiral matter content, or a CAT(0) rigidity argument [7] rules out the candidate symmetry groups outright. This failure requires no experiment. Second, a coupling failure: measured couplings, propagated to local components, violate $\prod_v |g_v|_v = 1$ beyond combined uncertainties, falsifying Test T2 directly. Third, an experimental failure: null results in the echo, CMB, and jet-clustering channels past the thresholds of R4 and R5, analyzed with the Phase 1 statistical discipline of pre-registered look-elsewhere correction, Bonferroni correction, and permutation nulls [9]. The Phase 1 study already demonstrated the third mode in miniature: three candidate zeta-zero/mass-ratio matches, each statistically falsified after correction, with the explicit conclusion that mathematical beauty does not imply physical truth [9].

**Falsification of the main result.** The main quantitative result of this paper is R4, the visibility threshold. It would be falsified in either direction by a single observation: a statistically significant prime-clustering modulation at harmonic $n = 2$ with fitted coefficient $a < 0.20$ in an analysis whose jet systematic floor is demonstrated to be at or below $10\%$ — this would break the visibility rule $\delta_n \geq \sigma_{\mathrm{sys}}$, showing that sub-floor modulations are detectable and that the threshold logic understates sensitivity; or, conversely, a certified detection at $a \geq 0.20$ that fails the Phase 1 multiple-comparisons discipline [9], which would show the threshold was reachable but the signature was a look-elsewhere artifact. Either observation forces a revision of the threshold derivation; neither requires new machinery.

**Limitations.** The results rest on the following assumptions, with sensitivity noted for each.

- *The visibility rule $\delta_n \geq \sigma_{\mathrm{sys}}$.* R4 scales linearly with this choice; a $2\sigma$ rule would double the excluded coefficient to $a \geq 0.40$, and a $5\sigma$ discovery threshold would raise it to $a \geq 1.00$. The qualitative conclusion — $n = 2$ is the most sensitive channel — is insensitive to the rule, but the number $0.20$ is not.
- *The Möbius parametrization $\delta_n = a|\mu(n)|/n$.* This is adopted from the amplitude hierarchy stated for the echo signature [8]; if the jet-clustering amplitude follows a different law, the thresholds change accordingly. The paper does not derive the parametrization from the product formula; it inherits it.
- *The systematic floor $\sigma_{\mathrm{sys}} = 0.10$.* Taken from the documented Tevatron-era jet systematics and the stated goal of pushing below $10\%$ [1]. Modern analyses may already sit lower, which would tighten the threshold proportionally; the derivation shows how to re-run it for any floor.
- *The echo parametrization $\Delta t_n = 4M \ln n$.* Inherited from [8]; the mass scale $M$ is a free parameter, so R5 fixes the shape but not the absolute timing.
- *The automorphic embedding conjecture (T1).* No partial result exists; the CAT(0) rigidity theorems [7] and the subgroup-rank bounds [2] constrain candidates but do not construct or exclude the embedding.
- *Uniformity of adelic algebra across places.* The unit-conjecture counterexample — a torsion-free, virtually abelian group whose group ring over $\mathbb{F}_2$ has non-trivial units, with a unit group that is not finitely generated [3] — shows that universality claims about group-associated algebras can fail in the simplest virtually abelian settings; the assumption that adelic group algebras behave uniformly across places must be tested place by place.
- *Presentation equivalence.* Any embedding proof that reduces to checking equivalence of group presentations must use non-abelian test groups, since abelian images cannot distinguish the Akbulut–Kirby candidate pairs [4]; the transitivity of $\operatorname{Aut}F_n$ on $\operatorname{Epi}(F_n, G)$ remains open in general [4].

**Open questions.** Whether the idele class group admits automorphic representations with the right $\infty$-component is untouched here. Whether the product formula constraint on couplings survives renormalization-group running — the scale dependence governed by the QCD evolution equation [1] — is unresolved and is arguably the first obstacle Test T2 meets. Whether the $83\%$ classification accuracy for quantum error-correcting code families by Kodaira–Néron fibers [11] generalizes beyond that code family is unknown. And the boundary drawn by the Phase 1 study — between mathematical property and numerology, drawn by statistical rigor [9] — must be re-drawn for each new signature; this paper supplies the thresholds but not the data.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** Three user groups exist. First, model builders beyond the Standard Model: R3 tells them the selection problem they face is finite of order $6$, and an adelic consistency check on couplings — if Test T2 survives — would fix the faithful gauge group without waiting for a heavy-particle discovery of the kind that otherwise pins the global form down [5]. The decision that changes is which gauge group a new-physics spectrum is written against. Second, collider analysis teams: R4 gives a concrete exclusion threshold ($a \geq 0.20$ at $n = 2$) that can be attached to any jet-substructure search as a reported limit, in the same way systematic floors are reported [1]. Third, gravitational-wave search groups: R5 gives the echo-delay template $\Delta t_n = 4M \ln n$ with the amplitude hierarchy and the self-consistency relation $\Delta t_6 = \Delta t_2 + \Delta t_3$, which can be added to matched-filter banks as a pre-registered template family. No user can act on Test T1 today; that part of the work is foundational, since automorphic embedding is a mathematical existence question whose resolution would precede any experimental design.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical and has not been peer reviewed: it is TRL 1–2. The derivations are paper-and-pencil arithmetic and algebra on top of documented inputs [1], [5], [8], [9]; no prototype, no simulation, no hardware, and no experimental campaign exists. Analytical work never exceeds TRL 3, and nothing here approaches it: the proposed signatures have not been observed, and the embedding conjecture has not been constructed or excluded.

**(c) The smallest next test.** The cheapest de-risking step is a reanalysis, not an experiment: take an existing published jet-substructure dataset and analysis chain, apply the Möbius-weighted harmonic template at $n = 2$ and $n = 6$, and report the fitted coefficient $a$ with the Phase 1 statistical protocol (pre-registered look-elsewhere correction, Bonferroni correction, permutation null) [9]. The outcome that refutes the threshold logic of R4 is a significant fitted $a < 0.20$ under a demonstrated $\leq 10\%$ systematic floor; the outcome that refutes the signature itself is a null result at $a \geq 0.20$ sensitivity, which then excludes the Möbius-weighted adelic clustering hypothesis at that amplitude. A second, independent step is the arithmetic one: extend the product-formula check of Section 4.1 to the coupling values $\{g_v\}$ for the measured strong, weak, and hypercharge couplings, propagating experimental uncertainties, to see whether Test T2's constraint is even approximately satisfiable before any renormalization subtlety is addressed.

**(d) Binding constraints.** The first constraint to bind is systematic uncertainty, not statistics: the entire visibility argument of R4 is set by the $10\%$ jet systematic floor [1], and the documented dependence of jet rates on algorithmic choices — seeds, the split/merge parameters $f_{\mathrm{merge}}$ and $p_{T,\min}$ [1] — means an adelic fractal signature could be suppressed or manufactured by analysis choices; the protocol must therefore fix the jet algorithm and parameters before unblinding, favoring the seedless infrared-safe cone algorithm with $k_T$ cross-checks [1]. The second constraint is the renormalization-scale problem: couplings run with the scale $Q$ through the QCD evolution equation [1], and Test T2's product constraint has no defined place in that running; until a scale prescription is stated, the coupling test is not executable. The third is statistical: the look-elsewhere correction grows with the number of harmonics and primes scanned, and the Phase 1 experience [9] shows this correction is decisive. Data volume, compute, and cost are not binding at this stage; the reanalysis of (c) uses existing data. Whether the automorphic embedding search (T1) is computationally tractable at all is an open question.

**(e) Order-of-magnitude bounds.** The only quantitative bounds this paper can state are those derived in Section 4: the exclusion threshold $a \geq 0.20$ at $n = 2$ and $a \geq 0.60$ at $n = 6$ (projection, assuming the visibility rule $\delta_n \geq \sigma_{\mathrm{sys}}$ and the Möbius parametrization, both stated in Section 4.4), and the echo delays of R5 in units of the free mass scale $M$. No cost, market, or performance figure beyond these is derivable from the inputs used here, and none is claimed.

**(f) Risks and misuse paths.** The prime-clustering and echo signatures are template-based searches on noisy data; the documented misuse path is the one the Phase 1 study already fell into and corrected — selecting a numerological match (zeta-zero gap ratios against particle mass ratios) without multiple-comparisons discipline, which produced apparent matches that dissolved under a permutation null [9]. Any group reporting a prime-clustering or echo detection without pre-registered correction and a permutation null is repeating that failure mode, and the thresholds of R4 and R5 should not be cited as evidence of adelic structure until the discipline is applied.

## 8. Conclusion

This paper converted the adelic shadow conjecture from a program statement into a falsifiable protocol. The conjecture was stated in three tests — automorphic embedding, adelic coupling constraints, and Bruhat–Tits tree dynamics against frequency-space physics — each with an explicit falsification condition. The arithmetic core was verified: the product formula holds exactly at $q = 60$, and the program's tabulated QED coefficient reproduces its closed form to rounding. The selection problem was sized: the gauge-group ambiguity an adelic rule must resolve is finite of order $6$. The signatures were quantified: a null jet search at the documented $10\%$ systematic floor excludes a Möbius-weighted amplitude coefficient $a \geq 0.20$ at harmonic $n = 2$, and the echo-delay spectrum $\Delta t_n = 4M \ln n$ carries the amplitude hierarchy $|\mu(n)|/n$ with an exact additive structure at $n = 6$. The program adds no symmetry beyond Ostrowski's classification; its failure, if it fails, will be visible either in algebra — no embedding, or rigidity exclusions [7] — or in data, judged by the statistical discipline the program has already applied to itself once, negatively [9]. The next step is a reanalysis of existing jet data under pre-registered thresholds, which would either de-risk or falsify the most accessible prediction of the adelic program.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Tevatron-for-LHC Report of the QCD Working Group. arXiv:hep-ph/0610012v1. https://arxiv.org/abs/hep-ph/0610012v1
[2] Graphs, free groups and the Hanna Neumann conjecture. arXiv:math/0701214v2. https://arxiv.org/abs/math/0701214v2
[3] A counterexample to the unit conjecture for group rings. arXiv:2102.11818v4. https://arxiv.org/abs/2102.11818v4
[4] Andrews-Curtis and Nielsen equivalence relations on some infinite groups. arXiv:1304.2668v2. https://arxiv.org/abs/1304.2668v2
[5] Understanding the SM gauge group from SMEFT. arXiv:2404.04229v3. https://arxiv.org/abs/2404.04229v3
[6] Schur multipliers of special p-groups of rank 2. arXiv:1908.06409v1. https://arxiv.org/abs/1908.06409v1
[7] Groups acting on spaces of non-positive curvature. arXiv:1603.04573v2. https://arxiv.org/abs/1603.04573v2
[8] QNFO: The Adelic Distinction: Physics as Automorphic Representation Theory on the Idele Class Group
[9] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1
[10] QNFO: Consilience Between Physics and Number Theory: Convergent Theses from Ostrowski's Theorem to Adelic Quantum Mechanics
[11] QNFO: Five Pillars, One Structure: Consilient Convergence in QNFO Research