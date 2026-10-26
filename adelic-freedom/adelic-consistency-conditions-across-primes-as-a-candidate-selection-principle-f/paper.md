# Adelic Consistency Conditions Across Primes as a Candidate Selection Principle for Physical Constants: Formulation, Negative Control, and Toy Dynamics

## Abstract

The three constants problem—why the fine-structure constant takes its observed value, why charged-lepton masses are hierarchically spaced, and what fixes the absolute mass scale—has no accepted resolution within the Standard Model. We develop a research program, stated as a testable conjecture rather than a result, in which the missing information is encoded not in the real continuum but in the non-archimedean ($p$-adic) places of an adelic structure over the rationals. The real line is treated as one leaf of an adelic foliation whose other leaves are ultrametric Bruhat–Tits trees; particle stability is conjectured to require consistency conditions satisfied at every prime simultaneously. We formalize this as a variational fixed-point principle on the adèle ring $\mathbb{A}_{\mathbb{Q}}$, verify the adelic product formula by explicit arithmetic, and prove a negative control: the product formula alone is an identity on $\mathbb{Q}^{\times}$ and therefore has zero selection power. We construct a toy cross-prime closure functional whose stationary point can be expressed analytically, and we note that a direct quantitative comparison with the observed fine-structure constant is deferred to future work, and exhibit a Newton iteration for $\sqrt{137}$ as a template exposing how naive dynamics leave the $p$-adic places passive. We relate the program to arithmetic equidistribution theory, adelic line bundles, Weyl consistency conditions, and prior adelic-constraints project reports, and we catalog the epistemological risks, chief among them the danger of fitting rather than predicting.

## 1. Introduction

The Standard Model of particle physics takes roughly two dozen parameters as input: gauge couplings, Yukawa matrices, and the vacuum expectation value that sets the electroweak scale. Among the most striking unexplained facts are (i) the numerical value of the fine-structure constant $\alpha$, (ii) the hierarchy of charged-lepton masses, and (iii) the absolute scale that fixes why any mass is what it is. No internal principle of the Standard Model selects these numbers.

This paper pursues a conjecture: that the missing information is not stored in the real continuum at all, but in the $p$-adic places of an adelic structure. The rationals $\mathbb{Q}$ admit inequivalent completions—one archimedean ($\mathbb{R}$) and one non-archimedean ($\mathbb{Q}_p$) for each prime $p$—linked by a single identity, the adelic product formula. If physics is formulated on the full adèle ring $\mathbb{A}_{\mathbb{Q}}$ rather than on $\mathbb{R}$ alone, then consistency conditions must hold at every prime simultaneously, and these cross-prime conditions are candidate sources of parameter selection invisible to a purely real-valued formulation.

The conjecture has a specific structure. The real line is one leaf of an adelic foliation; the other leaves are ultrametric Bruhat–Tits trees, the canonical geodesic spaces associated with non-archimedean fields. Particle stability—why some configurations persist and others decay—is reinterpreted as a consistency requirement across all leaves. The program makes three methodological commitments:

1. **Variational formulation.** A functional on $\mathbb{A}_{\mathbb{Q}}$ whose stationary points reproduce $\alpha$ and the lepton mass ratios should exist, or the program fails.
2. **Product-formula audit.** What the adelic product formula actually constrains must be determined before any selection mechanism is proposed; Section 4 shows it constrains nothing by itself.
3. **Ultrametric dynamics.** Dynamics on Bruhat–Tits trees should exhibit cross-prime closure that selects the observed values rather than a continuum of them.

We emphasize what this paper does and does not claim. It does not claim a derivation of any physical constant, and it reports no executed simulation of tree dynamics. It claims (a) a precise mathematical skeleton for the conjecture, (b) explicit verifications of the ingredients that can be verified by hand, (c) a negative control showing the product formula is constraint-free, (d) a toy closure model whose unique stationary point is computable and which is empirically falsified in its simplest form—an instructive negative result—and (e) a map of the literature and prior project reports against which progress can be measured. The prior reports in the QNFO corpus [9], [10], [11] posed the central questions about adelic constraints, while [12] recorded arithmetic errors and epistemological risks; we inherit the questions and the caution.

## 2. Background and Related Work

We organize the literature into three strands and discuss all twelve bibliography entries; where a supplied summary is truncated, we say so and use only what is stated.

**Adelic equidistribution.** The entry for quasi-adelic measures and equidistribution on $\mathbb{P}^1$ [1] records that Baker-Rumely and Favre-Rivera-Letelier independently proved an arithmetic equidistribution theorem for points of small height on the Berkovich compactification of the projective line with respect to an adelic measure, and that Chambert-Loir proved a more general version for curves. This is directly relevant: the Berkovich compactification is precisely the kind of hybrid archimedean/non-archimedean space on which our foliation picture lives, and equidistribution of small-height points is a template for how configurations distributed across all places can have a well-defined collective limit. If stationary points of an adelic functional exist, equidistribution theorems of this type are the natural tool for showing that finite-prime approximations converge to the full adelic answer.

**Adelic line bundles and rigidity.** The arithmetic Hodge index theorem for adelic line bundles II [2] extends earlier results from number fields to finitely generated fields and applies the theorem to obtain a rigidity property of the sets of preperiodic points of polarizable algebraic dynamical systems. Rigidity is exactly the phenomenon our conjecture needs: a consistency condition admitting only isolated solutions. The supplied summary gives no further quantitative detail, so we use this work only as evidence that adelic line-bundle techniques produce rigidity statements, not as a source of specific formulas.

**Consistency conditions in field theory.** Consequences of Weyl Consistency Conditions [3] studies the running of quantum field theories via a local renormalization group equation, noting that introducing spacetime-dependence of parameters can efficiently incorporate renormalization effects of composite operators, and that an illustration of the power of these methods was presented. Weyl consistency conditions are constraints among couplings required for consistency under renormalization—structurally the closest existing physics analogue to our "consistency at every prime" requirement. The analogy is heuristic only; [3] concerns renormalization-group consistency on spacetime, not adelic places, and the summary does not state specific consequences derived, so we cite it for the framework rather than for results.

**Adelic tori.** Finite-Dimensional Protori Are Adelic Tori [4] shows that the category of finite-dimensional compact connected abelian groups (finite-dimensional protori) is equivalent to the category of adelic tori, with a complete Lie theory: for each adelic torus $G$ there is a proper short exact sequence
$$
0 \longrightarrow \mathbb{Q}^n \longrightarrow \mathcal{L}(G) \xrightarrow{\exp} G \longrightarrow 0,
$$
with $\exp$ the adelic exponential, and the work extends the definition of nonarchimedean dimension. This supplies group-theoretic infrastructure: if the space of constants carries a compact group structure, it is an adelic torus by [4], and the adelic exponential is the map on which a fixed-point equation would naturally be written. The entry's summary is the sole support for these statements.

**Primes, spectra, and counting.** Four entries concern prime distributions. Twin Primes In Quadratic Arithmetic Progressions [5] presents a heuristic spectral-analysis argument supporting the twin prime conjecture and related counting problems, and offers a rigorous version proving the existence of infinitely many quadratic twin primes $n^2+1$ and $n^2+3$ for $n \geq 1$. Spectral Methods And Prime Numbers Counting Problems [8] uses the same spectral basis to argue for the twin prime conjecture and proposes a proof of the more general de Polignac conjecture on infinitely many prime pairs $p$ and $p+2k$ for $k \geq 1$. Primes In Fractional Sequences [6] proves that the fractional sequences $\{[x/n]+1 : n \leq x\}$ and $\{q[x/n]+a : n \leq x\}$ with $\gcd(a,q)=1$, $a<q$, contain the set of primes and the primes in arithmetic progressions respectively as $x \to \infty$. Quadratic Primes [7] addresses quadratic primes $p = an^2+bn+c$ generated by irreducible polynomials, noting the subset is widely believed unbounded and providing details of a possible proof for some polynomials, in particular the simplest subset $\{p = n^2+1\}$. The supplied summaries for [5]–[8] give limited methodological detail beyond what is quoted; we cite them because our cross-prime closure conditions are, at bottom, statements about how primes distribute along arithmetic and polynomial sequences, and these works represent the analytic toolkit aimed at such questions. We do not rely on the correctness of the proposed proofs, which the summaries themselves frame as proposals.

**The adelic-constraints program itself.** The QNFO corpus supplies four reports. The Adelic Constraints Project — A Complete Account [9] describes a project conducted in May 2026 asking whether the multiple incompatible completions of $\mathbb{Q}$, linked by a single identity, constrain anything; the supplied summary truncates before stating its findings, so we use only this framing. Phase 1 [10] set out to answer whether the adelic completion of the rationals constrains fundamental physical constants, tracing the question to a theorem of Alexander Ostrowski; the summary again truncates before results. Phase 3 Synthesis [11] investigated the central open question left by Phase 2—whether the adelic framework makes a falsifiable numerical prediction differing from the Standard Model—targeting a "suggestive coincidence" discovered in Phase 2; the summary truncates before naming the coincidence, so we treat the existence of such a target as the only established fact. Finally, the Adelic Cross-Domain Program report [12] documents, in its v3.2 correction record dated 2026-07-25, that arithmetic errors in mass ratio triplets were corrected with 5 of 9 triplets verified independently, that an Efimov lambda derivation was replaced with an honest structural correspondence, that a constraining-literature section was added, and that a semigroup density epistemological risk was acknowledged. We cite [12] chiefly as calibration: a program of this type has already produced arithmetic errors and over-claims that its own authors retracted, and any new instantiation must be structured so that such errors are detectable—hence the explicit-arithmetic discipline of Section 4.

## 3. Methods

### 3.1 Adelic skeleton

Let $\mathbb{Q}_p$ denote the $p$-adic completion of $\mathbb{Q}$ with norm $|\cdot|_p$ satisfying $|p|_p = p^{-1}$, and $|\cdot|_\infty$ the usual absolute value. The adèle ring is the restricted product
$$
\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod_{p}{}' \mathbb{Q}_p,
$$
where the prime restricts all but finitely many components to $\mathbb{Z}_p$. The Ostrowski product formula—the "single identity" referenced in [9], [10]—states
$$
\prod_{v} |x|_v = 1 \qquad \text{for all } x \in \mathbb{Q}^{\times},
$$
where $v$ runs over the archimedean place and all primes.

### 3.2 Foliation and stability conjecture

We posit a foliation $\mathcal{F}$ of the adelic configuration space whose leaves $\mathcal{L}_\infty, \mathcal{L}_2, \mathcal{L}_3, \ldots$ correspond to the places; $\mathcal{L}_\infty$ is the real line and $\mathcal{L}_p$ is (a subtree of) the Bruhat–Tits tree $\mathcal{T}_p$ of $\mathbb{Q}_p$, the contractible simplicial complex whose boundary is $\mathbb{P}^1(\mathbb{Q}_p)$, the space on which the equidistribution theorem of [1] is formulated.

> **Conjecture S.** A particle configuration is stable if and only if a consistency functional $\mathcal{C}$ is stationary on every leaf simultaneously; the cross-leaf stationarity conditions couple the places and quantize the allowed parameter values.

### 3.3 Variational principle

For a parameter vector $\theta = (\alpha, r_1, r_2, \mu_0)$ encoding the fine-structure constant, lepton mass ratios, and absolute scale, define an action functional
$$
\mathcal{S}[\theta] = \sum_{v} w_v\, \Phi_v(\theta) + \sum_{v < v'} w_{vv'}\, \Psi_{vv'}(\theta),
$$
with $\Phi_v$ a place-dependent local term, $\Psi_{vv'}$ a coupling between places, and weights $w_v, w_{vv'}$ to be fixed by the theory. Stationarity requires $\partial \mathcal{S} / \partial \theta_i = 0$ for all $i$—at the real place and at every prime simultaneously. Equivalently, $\theta = F(\theta)$ with
$$
F(\theta)_i = \theta_i - \lambda_i\, \frac{\partial \mathcal{S}}{\partial \theta_i}.
$$
The claim to be tested is whether the simultaneous solution set $\mathrm{Fix}(F)$ is finite and contains the observed values. No specific choice of $\Phi_v$ or $\Psi_{vv'}$ is defended here; Section 4 analyzes the simplest nontrivial toy instantiation precisely because the full functional is not yet specified.

### 3.4 The three checks and the honesty protocol

Any implementation must pass three checks: (1) a product-formula audit determining what constraint the identity actually imposes (Section 4.1–4.2); (2) a cross-prime closure check of whether the product formula, supplemented by quantization conditions, yields discrete admissible sets matching observed spectra (Section 4.3 gives a toy version; the full check is open); (3) an ultrametric simulation on the trees $\mathcal{T}_p$ (specified in Section 3.5 but not executed in this paper). Following the correction history of [12], in which arithmetic errors in mass-ratio triplets were found and only partially independently verified, we adopt: every numerical claim is computed in Section 4 with all steps shown; no empirical physics data are used except where explicitly labeled; structural analogies are labeled as such.

### 3.5 Ultrametric dynamics protocol (specified, not executed)

On a Bruhat–Tits tree, the natural metric is $d_p(x, y) = p^{-v_p(x-y)}$ for points identified with elements of $\mathbb{Q}_p$, where $v_p$ is the $p$-adic valuation; it obeys the strong triangle inequality $d_p(x,z) \leq \max(d_p(x,y), d_p(y,z))$, verified explicitly in Section 4.2. The planned protocol would iterate candidate stability maps $T_p$ on each tree and test whether the family $\{T_p\}$ has a common fixed point only for the observed parameter values. No results from this protocol are reported.

## 4. Analysis

Every input number in this section is either a definition internal to the paper, an elementary mathematical constant, or a count taken from bibliography entry [12]; the single qualitative empirical statement is labeled as such.

### 4.1 Verification of the adelic product formula

**Input:** $x = 12 = 2^2 \cdot 3$. Then $|12|_\infty = 12$, $|12|_2 = 2^{-2} = \tfrac{1}{4}$, $|12|_3 = 3^{-1} = \tfrac{1}{3}$, and $|12|_p = 1$ for $p \notin \{2,3\}$:
$$
\prod_v |12|_v = 12 \cdot \frac{1}{4} \cdot \frac{1}{3} \cdot \prod_{p \notin \{2,3\}} 1 = 12 \cdot \frac{1}{12} = 1.
$$

**Input:** $x = \tfrac{3}{5}$. Then $|\tfrac{3}{5}|_\infty = \tfrac{3}{5}$, $|\tfrac{3}{5}|_3 = \tfrac{1}{3}$, $|\tfrac{3}{5}|_5 = 5$, and $|\tfrac{3}{5}|_p = 1$ otherwise:
$$
\frac{3}{5} \cdot \frac{1}{3} \cdot 5 = \frac{3 \cdot 5}{5 \cdot 3} = 1.
$$

**Input:** $x = 137$. We verify the primality of $137$ by explicit trial division.  $137 = 2\cdot68 + 1$, $137 = 3\cdot45 + 2$, $137 = 5\cdot27 + 2$, $137 = 7\cdot19 + 4$, $137 = 11\cdot12 + 5$, and $13^2 = 169 > 137$, so no prime $p\le \sqrt{137}$ divides $137$; therefore $137$ is prime.  Consequently
$$
|137|_\infty = 137,\quad |137|_{137}=137^{-1},\quad |137|_p = 1\text{ for }p\neq 137.
$$
$$
137 \cdot \frac{1}{137} = 1.
$$

### 4.2 Negative control: the product formula selects nothing

Define, for a candidate rational $r = a/b > 0$ in lowest terms and a prime cutoff $P$, the closure defect
$$
D_P(r) = \left| \log \left( |r|_\infty \prod_{p \leq P} |r|_p \right) \right|.
$$
By the product formula, $|r|_\infty \prod_{p \leq P} |r|_p = 1 / \prod_{p > P} |r|_p$. But $|r|_p = 1$ for every prime $p$ not dividing $ab$, of which there are all but finitely many. Choosing $P$ larger than every prime divisor of $ab$ gives $\prod_{p > P} |r|_p = 1$, hence
$$
D_P(r) = |\log 1| = 0 \qquad \text{for all } r \in \mathbb{Q}^{\times} \text{ and all sufficiently large } P.
$$
Concrete instance: $r = 137$ with $P \geq 137$ gives $D_P(137) = 0$, consistent with the direct check $137 \cdot 137^{-1} = 1$ above. Since $D_P$ vanishes identically on $\mathbb{Q}^{\times}$, the product formula is an identity, not a constraint: it holds for every nonzero rational, so a selection principle built on it alone has zero discriminating power. Any adelic selection of $\alpha$ must invoke additional structure—e.g., valuation conditions $v_p(c - c_0) \geq n_p$ at infinitely many primes, a nontrivial coupling $\Psi_{vv'}$, or equidistribution limits in the sense of [1].

### 4.3 Ultrametric triangle inequality on the 2-adic tree

**Inputs:** points $x = 1$, $y = 3$, $z = 7$ in $\mathbb{Q}_2$, metric $d_2(a,b) = 2^{-v_2(a-b)}$.

- $v_2(1-3) = v_2(-2) = 1$, so $d_2(1,3) = 2^{-1} = 0.5$.
- $v_2(3-7) = v_2(-4) = 2$, so $d_2(3,7) = 2^{-2} = 0.25$.
- $v_2(1-7) = v_2(-6) = 1$, so $d_2(1,7) = 2^{-1} = 0.5$.

Check:
$$
d_2(1,7) = 0.5 \leq \max\big(d_2(1,3),\, d_2(3,7)\big) = \max(0.5,\, 0.25) = 0.5.
$$
Note the ultrametric signature: $d_2(3,7) = 0.25 < 0.5 = d_2(1,7)$ even though $3$ lies between $1$ and $7$ in the usual order—on the tree, $3$ and $7$ are closer to each other than either is to $1$, because their difference shares two factors of $2$. This is the geometric mechanism by which cross-prime conditions can distinguish configurations that look identical on the real leaf.

### 4.4 Toy cross-prime closure functional

Define $\Phi(\alpha) = \alpha^2 S_\infty$ with $S_\infty = \sum_{p} p^{-2}$ over primes, and impose the closure condition $\Phi(\alpha) = 1$, giving $\alpha_{\mathrm{toy}} = 1/\sqrt{S_\infty}$.

**Step 1: partial sums.** For $P = 10$ (primes $2, 3, 5, 7$):
$$
S_{10} = \frac{1}{4} + \frac{1}{9} + \frac{1}{25} + \frac{1}{49} = 0.25 + 0.111111 + 0.04 + 0.020408 = 0.421519.
$$
For $P = 50$, the increments for primes $11$ through $47$ are
$$
0.008264 + 0.005917 + 0.003460 + 0.002770 + 0.001890 + 0.001189 + 0.001041 + 0.000730 + 0.000595 + 0.000541 + 0.000453 = 0.026850,
$$
so $S_{50} = 0.421519 + 0.026850 = 0

## References

[1] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$. arXiv:1502.04660v3. https://arxiv.org/abs/1502.04660v3
[2] The arithmetic Hodge index theorem for adelic line bundles II. arXiv:1304.3539v2. https://arxiv.org/abs/1304.3539v2
[3] Consequences of Weyl Consistency Conditions. arXiv:1308.1096v2. https://arxiv.org/abs/1308.1096v2
[4] Finite-Dimensional Protori Are Adelic Tori. arXiv:2411.16000v44. https://arxiv.org/abs/2411.16000v44
[5] Twin Primes In Quadratic Arithmetic Progressions. arXiv:1710.07827v1. https://arxiv.org/abs/1710.07827v1
[6] Primes In Fractional Sequences. arXiv:1809.02821v3. https://arxiv.org/abs/1809.02821v3
[7] Quadratic Primes. arXiv:1401.2355v4. https://arxiv.org/abs/1401.2355v4
[8] Spectral Methods And Prime Numbers Counting Problems. arXiv:1509.00457v8. https://arxiv.org/abs/1509.00457v8
[9] https://papers.qnfo.org/papers/the-adelic-constraints-project-a-complete-account/. QNFO: The Adelic Constraints Project — A Complete Account.
[10] https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-1/. QNFO: Adelic Constraints on Quantum Field Theory: Phase 1.
[11] https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-3-synthesis/. QNFO: Adelic Constraints on Quantum Field Theory — Phase 3 Synthesis.
[12] https://papers.qnfo.org/papers/adelic-cross-domain/. QNFO: The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees.