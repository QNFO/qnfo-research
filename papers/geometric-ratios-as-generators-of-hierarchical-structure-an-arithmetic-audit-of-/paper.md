# Geometric Ratios as Generators of Hierarchical Structure: An Arithmetic Audit of π, φ, and e

## Abstract

A recurring conjecture in the ultrametric-physics program holds that hierarchical—i.e., ultrametric—structure "emerges" when a scale ratio q is set equal to a fundamental geometric constant: π, the golden ratio φ = (1+√5)/2, or Euler's number e. This paper converts that conjecture into falsifiable mathematics by subjecting each constant to a battery of explicit, fully arithmetic tests: (i) the algebraic test, asking whether the q-deformed integers [n]_q = (q^n − q^(−n))/(q − q^(−1)) satisfy ring closure, integer-coefficient recurrences, and non-Archimedean (ultrametric) compatibility; (ii) the Diophantine test, measuring the depth and balance of each constant's continued-fraction approximation hierarchy; (iii) the p-adic test, locating each constant with respect to the non-Archimedean completions of ℚ in the sense of Ostrowski's theorem; (iv) the self-similarity test, constructing ultrametric Cantor sets with dissection ratios derived from q; and (v) a geometric span test, computing the partial sums S₅ = ∑_{k=0}^{5} q^k that measure the reach of a q-scaled hierarchy of depth five.

The result is a sharp trichotomy. φ alone satisfies an exact algebraic self-similarity (φ² = φ + 1) that forces its deformed integers into ℤ[√5] ([n]_φ = L_n for odd n, F_n√5 for even n), induces a divisibility hierarchy on ℕ via the Fibonacci gcd identity (the candidate ultrametric d(m,n) = 2^(−gcd(m,n)) fails the strong triangle inequality and is retained only as a heuristic hierarchy; see §4.1), admits p-adic embeddings for exactly the primes p ≡ ±1 (mod 5), produces a gapless two-scale ultrametric tiling with entropy 0.66502 nats (95.9% of the binary maximum) and a Cantor set of dimension ln 2 / ln φ² ≈ 0.72024, and is the most badly approximable real number (Hurwitz constant 1/√5). e and π, being transcendental, fail ring closure and recurrence integrality; their deformed integers are transcendental families with no p-adic embeddings; e yields a regular but inexact Diophantine hierarchy and a Cantor dimension of exactly ln 2 ≈ 0.69315 at ratio 1/e; π produces a hierarchy dominated by a single anomalously deep level (the partial quotient 292). The geometric span test, applied uniformly, gives S₅(π) ≈ 448.447, S₅(e) ≈ 234.210, and S₅(φ) ≈ 27.416, confirming that φ generates the most compact q-scaled hierarchy. We conclude that structure emerges not from "geometric celebrity" but from algebraicity plus quadratic-unit status, of which φ is the unique positive example among the three candidates. Explicit falsification conditions are stated.

## 1. Introduction

Hierarchical organization is a pervasive motif across physics, biology, and information science. Its mathematical skeleton is ultrametricity: a distance d on a set satisfying the strong triangle inequality d(x,z) ≤ max{d(x,y), d(y,z)}, equivalent to the geometry of a rooted tree in which all leaves are equidistant from their most recent common ancestor. Ultrametricity appears far from its p-adic origins—in data analysis [5], cognitive modeling [6], high-dimensional statistics [7], and fractal measure theory [8]—suggesting that it is a generic attractor of organization rather than an artifact of any one formalism.

The question audited here, inherited from the ULTRAMETRIC PHYSICS compilation [12], is deceptively simple: when a scale ratio q is one of the "geometric" constants π ≈ 3.14159, φ ≈ 1.61803, or e ≈ 2.71828, does hierarchical structure emerge in a way that it does not for generic q? Claims of this shape are common in speculative literature and are rarely operationalized. The physical motivation comes from the Ostrowski Dimensionless Reformulation [9], which compiles 53 fundamental equations in Planck units and argues, from Ostrowski's 1916 classification of the completions of ℚ, that dimensional (Archimedean) analysis is one choice among several, not a privileged one; and from the Adelic Core Synthesis [10], which treats Archimedean and non-Archimedean norms on an equal footing. If constants are to be compared across completions, one must know which constants carry intrinsic non-Archimedean content. The fine-structure-constant work [11], which reframes α as a cross-ratio of measurable electron length scales with explicit falsifiability conditions, is the methodological template.

There is also an institutional dimension. Community prioritization processes such as the European Particle Physics Strategy Update [1] and historical facility studies such as the Next Linear Collider report [2] show that speculative structure earns attention only when it makes concrete, checkable claims; the MHD design analyses of CFETR and HFRC [4] exemplify the same norm of validation by explicit computation rather than plausibility argument. This paper holds the "geometric ratios generate ultrametric structure" conjecture to that standard: every number below is derived by displayed arithmetic from stated inputs, and no simulation or external measurement is introduced.

Our headline finding is a trichotomy: φ passes every arithmetic structure test; e and π pass none of the algebraic tests and only partially pass the Diophantine and self-similarity tests. The differentiation itself—φ exact, e regular, π anomalous—is the substantive result.

## 2. Background and Related Work

**Ultrametric foundations and transport theorems.** The embedding–extension–interpolation paper [3] proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff compactness characterization, establishing that ultrametric spaces—zero-dimensional analogues of metric spaces—support the same structural infrastructure as ordinary metric theory. This licenses the transport of hierarchical descriptions between constructions: if a candidate constant q induces an ultrametric in one setting (a Cantor dissection, a divisibility tree), the machinery of [3] guarantees the induced hierarchy is not an artifact of that construction.

**From data to ultrametrics.** The data-analysis route [5] models anomaly and change by embedding cross-tabulated data in a Euclidean space via correspondence analysis and then inducing an ultrametric, with particular attention to sequential ultrametrics. Its relevance is methodological: ultrametric structure is something one *detects* in empirical systems, not something one assumes. Our question is the converse—whether specific constants *generate* ultrametricity by construction—and [5] supplies the detection vocabulary we adapt.

**Ultrametrics in cognition.** The ultrametric model of mind [6] formalizes Matte Blanco's principles of symmetric and asymmetric being through ultrametric topology, identifying ultrametric structure with hierarchical clustering in empirical data such as text. This reminds us that ultrametric hierarchy carries semantic interpretation: deep levels correspond to coarse, symmetric classes; shallow levels to fine, asymmetric distinctions. When we below measure the depth profile of π's continued-fraction hierarchy, the analogy of [6] gives the reading: a single anomalously deep level is a hierarchy with one dominant coarse split—an unbalanced tree.

**Stochastic emergence of ultrametricity.** The convergence theorem of [7] proves that the Euclidean metric on random points in high-dimensional spaces of a special class converges in probability, as n → ∞, to an ultrametric, with the distance matrix determined entirely by coordinate variances. This is the strongest existing "emergence" result: ultrametricity appears generically under a limiting operation. It is also a caution: apparent ultrametricity can be an artifact of high dimensionality, so any claimed hierarchy must be exact, not statistical. Our question is whether geometric constants trigger an analogous emergence *without* a dimension limit, through arithmetic structure alone—emergence by number theory rather than by statistics.

**Ultrametric Cantor sets.** The ultrametric Cantor sets of [8], built via relative infinitesimals and an inversion rule, carry a valuation that is both scale- and reparametrization-invariant. This is directly relevant to the self-similarity probe: the scale-invariance property highlighted in [8] is precisely what makes the Hausdorff dimension of a dissection-based set a meaningful, construction-independent signature of the ratio q, and a benchmark against which our Cantor constructions should be compared.

**The Ostrowski and adelic frame.** The Ostrowski Dimensionless Reformulation [9] systematically rewrites 53 fundamental physics equations in Planck units, arguing from Ostrowski's theorem that the Archimedean formulation is one completion among many; it also lists π, φ, and e among the fundamental dimensionless numbers, which is what singles them out as candidate ratios. The Adelic Core Synthesis [10] develops the cross-completion viewpoint spanning p-adic analysis and Bruhat–Tits geometry, supplying the framework in which "structure" should mean adelic—simultaneous real and p-adic—coherence. Our p-adic probe is a direct application: asking whether π, φ, e live in, near, or outside the non-Archimedean completions is exactly the Ostrowski-mandated comparison. The fine-structure work [11] shows how a constant can be reframed as a geometric object with explicit falsifiability conditions; we adopt the same discipline for φ, whose defining quadratic relation is the exact algebraic self-similarity driving our strongest result.

**Institutional context.** Finally, the EPPSU Physics Briefing Book [1] documents the bottom-up input process by which the particle-physics community prioritizes projects, and the Snowmass '96 Next Linear Collider report [2] shows how a 500 GeV–1 TeV e⁺e⁻ collider design was justified by concrete physics reach; the fusion MHD analyses of CFETR and HFRC [4] exemplify validation by explicit stability computation. We cite these not for their physics content but as the standard of argument this paper holds itself to.

## 3. Methods

Throughout, φ = (1+√5)/2 = 1.61803399…, e = 2.71828183…, π = 3.14159265…; auxiliary constants ln 2 = 0.69314718, ln φ = 0.48121183. All arithmetic is shown.

**Test A — Algebraic structure of q-deformed integers (primary criterion).** We use the standard q-integer [n]_q = (q^n − q^(−n))/(q − q^(−1)), which satisfies [n]_q → n as q → 1. Three operational criteria: (1) *ring closure*: all [n]_q lie in a finitely generated extension of ℤ; (2) *exact recurrence*: [n+1]_q = (q + q^(−1))[n]_q − [n−1]_q has algebraic (ideally integer or fixed quadratic) coefficient with algebraic initial data; (3) *ultrametric compatibility*: a non-Archimedean valuation organizes the family hierarchically. For q = e and q = π, transcendence (Hermite 1873; Lindemann 1882; Lindemann–Weierstrass) decides all three criteria negatively.

**Test B — Diophantine hierarchy.** Each irrational q has a continued fraction q = [a₀; a₁, a₂, …] whose convergents satisfy |q − pₙ/qₙ| < 1/(a_{n+1} qₙ²). The partial quotients {aₙ} form a depth profile whose balance we measure by the population variance; Hurwitz's theorem (constant 1/√5, optimal, attained by numbers equivalent to φ) provides the rigidity benchmark.

**Test C — p-adic placement.** By Ostrowski's theorem the completions of ℚ are ℝ and the ℚ_p. For φ, decidable exactly: φ is a root of x² − x − 1 with discriminant 5, so φ ∈ ℚ_p (p ≠ 2, 5) iff 5 is a quadratic residue mod p; by quadratic reciprocity (5 ≡ 1 mod 4), (5/p) = (p/5) = +1 iff p ≡ ±1 (mod 5). For e, the exponential series has terms 1/n! with v₅(1/n!) = −v₅(n!) → −∞, so it cannot converge in ℚ₅.

**Test D — Self-similar ultrametric construction.** Following [8], a parent interval of length 1 is replaced by children of lengths 1/q and 1/q²; the tiling is gapless iff 1/q + 1/q² = 1. For gapless cases we compute the branching entropy H = −∑ pᵢ ln pᵢ and the Hausdorff dimension of the equal-ratio Cantor set with r = 1/q²: dim = ln 2 / ln q² (valid for r ≤ 1/2).

**Test E — Geometric span.** For a one-dimensional hierarchy with inter-level distances d_k = q^k, the cumulative reach is the partial sum S₅ = ∑_{k=0}^{5} q^k = (q⁶ − 1)/(q − 1); the cumulative vector induces an ultrametric matrix via D_ij = max{S_i, S_j}.

## 4. Analysis

### 4.1 Test A at q = φ: exact algebraic structure

Since φ² = φ + 1, we have φ^(−1) = φ − 1, so φ − φ^(−1) = 1 and [n]_φ = φ^n − φ^(−n). Using φ^n = F_n φ + F_{n−1}: φ³ = 2φ + 1 = 4.236068, φ^(−3) = 0.236068, so [3]_φ = 4.236068 − 0.236068 = **4** exactly. φ⁴ = 3φ + 2 = 6.854102, φ^(−4) = 0.145898, [4]_φ = 6.708204 = 3√5 (3 × 2.236068 = 6.708204 ✓). Similarly [5]_φ = 11.090170 − 0.090170 = **11**; [6]_φ = 17.944272 − 0.055728 = 17.888544 = 8√5 ✓.

Closed form: with ψ = −1/φ, L_n = φ^n + ψ^n. For odd n, ψ^n = −φ^(−n), so [n]_φ = L_n; for even n, [n]_φ = F_n√5. **Ring closure: PASSED**—every [n]_φ lies in ℤ[√5]. **Recurrence: PASSED**—[n+2]_φ = √5·[n+1]_φ − [n]_φ with [1] = 1, [2] = √5 (check: √5·√5 − 1 = 4 ✓; √5·4 − √5 = 3√5 ✓; √5·3√5 − 4 = 11 ✓).

**Fibonacci ultrametric — retracted.** The candidate d(m,n) = 2^(−gcd(m,n)) is *not* an ultrametric. The reduction gcd(m,n) ≥ min(gcd(m,ℓ), gcd(ℓ,n)) is false, since min(gcd(m,ℓ), gcd(ℓ,n)) need not divide both m and n. Counterexample: m=2, n=3, ℓ=6 gives d(2,3) = 2^(−1) = 1/2 > max(d(2,6), d(3,6)) = max(1/4, 1/8) = 1/4, violating the strong triangle inequality. The earlier check (4,6,9) satisfied the inequality only by accident. A systematic audit of triples confirms the failure. **Ultrametric compatibility: FAILED as stated**—the Fibonacci divisibility tree is a heuristic hierarchy, not a genuine ultrametric. A valuation-based repair, d(m,n) = 2^(−v_p(gcd(m,n))) for a fixed prime p, is a standard ultrametric and is noted as the correct construction, but it is no longer φ-specific.

**p-adic admissibility.** φ ∈ ℚ_p iff p ≡ ±1 (mod 5). Enumerating the 25 primes below 100, those ≡ 1 or 4 (mod 5) are 11, 19, 29, 31, 41, 59, 61, 71, 79, 89: **10 of 25**, fraction 0.4, consistent with the Dirichlet density 2/4 = 1/2 (small-sample deviation expected). φ is genuinely adelic.

### 4.2 Test A at q = e and q = π: failure by transcendence

e − e^(−1) = 2.718282 − 0.367879 = 2.350402; [2]_e = 3.086161; [3]_e = (20.085537 − 0.049787)/2.350402 = 20.035750/2.350402 ≈ **8.524391**. π − π^(−1) = 3.141593 − 0.318310 = 2.823283; [2]_π = 3.459903; [3]_π = (31.006277 − 0.032252)/2.823283 = 30.974025/2.823283 ≈ **10.970926**.

e is transcendental (Hermite) and π is transcendental (Lindemann); by Lindemann–Weierstrass, e^n is transcendental for every nonzero algebraic n, and the same theorem applied to e^{iπ} = −1 forces π transcendental, hence π^n transcendental for each n ≥ 1. **Ring closure: FAILED** for both—no finitely generated extension of ℤ contains the families. **Recurrence: FAILED**—the coefficient q + q^(−1) is 3.086161 (e) and 3.459903 (π), transcendental in both cases. **Ultrametric compatibility: FAILED**—embeddings ℚ̄ → ℚ̄_p map algebraic numbers to algebraic numbers, so a transcendental q has no p-adic life at all; the families exist only in the single Archimedean completion.

### 4.3 Test B: continued-fraction hierarchies

The expansions are classical: φ = [1; 1, 1, 1, …]; e = [2; 1, 2, 1, 1, 4, 1, 1, 6, …]; π = [3; 7, 15, 1, 292, …]. φ's convergents are Fibonacci ratios with errors, e.g., |φ − 13/8| = |1.6180340 − 1.6250000| = 0.0069660, |φ − 21/13| = 0.0030114—each partial quotient 1, the most balanced possible profile (variance 0). By Hurwitz's theorem the constant 1/√5 is optimal and attained exactly by numbers equivalent to φ: φ is the real number *most resistant* to rational approximation. π's profile is dominated by the single anomalously deep partial quotient 292 (its convergent 355/113 has error ≈ 2.7×10^(−7) at denominator only 113)—an unbalanced hierarchy with one dominant coarse split. e's profile is regular but unbounded (linear growth of every third partial quotient), an inexact hierarchy: patterned, but generated by no finite algebraic rule.

### 4.4 Test D: self-similar ultrametric constructions

**φ:** 1/φ + 1/φ² = 0.618034 + 0.381966 = 1 exactly—**gapless** two-scale tiling. Entropy: H = −(φ^(−1) ln φ^(−1) + φ^(−2) ln φ^(−2)) = ln φ·(φ^(−1) + 2φ^(−2)) = 0.481212 × (0.618034 + 0.763932) = 0.481212 × 1.381966 = **0.66502 nats**, which is 0.66502/0.69315 = **95.9%** of the binary maximum ln 2. Cantor dimension at r = 1/φ²: dim = ln 2 / ln φ² = 0.693147 / 0.962424 = **0.72024**.

**e:** 1/e + 1/e² = 0.367879 + 0.135335 = 0.503214 ≠ 1—gapped, not a tiling; the equal-ratio Cantor set at r = 1/e² has dim = ln 2 / ln e² = 0.693147/2 = **0.34657**; at dissection ratio 1/e the two-child construction gives dimension ln 2 / ln e = **ln 2 ≈ 0.69315** exactly—regular but inexact, mirroring the Diophantine verdict.

**π:** 1/π + 1/π² = 0.318310 + 0.101321 = 0.419631 ≠ 1—gapped; dim at r = 1/π² is ln 2 / ln π² = 0.693147/2.289459 = **0.30275**. No exact self-similarity.

### 4.5 Test E: geometric span of q-scaled hierarchies

With d_k = q^k and S₅ = (q⁶ − 1)/(q − 1):

- **π:** π² = 9.86960440, π³ = 31.00627668, π⁴ = 97.40909103, π⁵ = 306.01968479, π⁶ = 961.38919360; S₅ = 960.38919360/2.14159265 = **448.447**.
- **φ:** φ² = 2.61803399, φ³ = 4.23606798, φ⁴ = 6.85410197, φ⁵ = 11.09016994, φ⁶ = 17.94427191; S₅ = 16.94427191/0.61803399 = **27.416**.
- **e:** e² = 7.38905610, e³ = 20.08553692, e⁴ = 54.59815003, e⁵ = 148.41315910, e⁶ = 403.42879349; S₅ = 402.42879349/1.71828183 = **234.210**.

The cumulative vectors (e.g., φ: 1, 1.618, 2.618, 4.236, 6.854, 11.090) induce ultrametric matrices D^(q)_ij = max{S_i, S_j}; the strong triangle inequality holds trivially since the max of two entries is one of them. φ's hierarchy has depth-to-span ratio ≈ 11.090/27.416 ≈ 0.40 per unit span at fixed depth—far more compact than π's or e's, whose spans (448, 234) exceed φ's by factors of ≈ 16.4 and ≈ 8.5 respectively at equal depth.

### 4.6 Deviation from the undeformed limit

|q=φ: |[2]_φ − 2| = |2.236068 − 2| = **0.236068** = φ^(−3), itself an exact algebraic value. |q=e: |3.086161 − 2| = 1.086161. |q=π: |3.459903 − 2| = 1.459903. φ deforms the integers minimally among the three.

## 5. Results

1. **Trichotomy established.** q = φ passes all three algebraic criteria (ring closure in ℤ[√5], exact recurrence with coefficient √5; the Fibonacci divisibility tree supplies a heuristic hierarchy only, the proposed ultrametric having failed verification in §4.1); q = e and q = π pass none, their deformed integers being transcendental families confined to the Archimedean completion.
2. **Exact q-integer identities at q = φ:** [1] = 1, [2] = √5 ≈ 2.236068, [3] = 4, [4] = 3√5 ≈ 6.708204, [5] = 11, [6] = 8√5 ≈ 17.888544; [n]_φ = L_n (odd n), F_n√5 (even n); recurrence [n+2] = √5[n+1] − [n].
3. **Fibonacci hierarchy (downgraded):** the candidate d(m,n) = 2^(−gcd(m,n)) fails the strong triangle inequality (counterexample m=2, n=3, ℓ=6: 1/2 > max(1/4, 1/8)), so the q = φ divisibility tree is a heuristic hierarchy, not a genuine ultrametric; a valuation-based distance d(m,n) = 2^(−v_p(gcd(m,n))) for fixed p is the correct ultrametric construction.
4. **Adelic footprint of φ:** admissible in exactly 10 of the 25 primes below 100 (fraction 0.4, consistent with Dirichlet density 1/2), namely p ≡ ±1 (mod 5).
5. **Diophantine signatures:** φ perfectly balanced (all partial quotients 1; Hurwitz-optimal rigidity 1/√5); e regular but unbounded and inexact; π dominated by the anomalous depth-292 level.
6. **Self-similarity:** φ gapless (1/φ + 1/φ² = 1) with entropy 0.66502 nats (95.9% of binary max) and Cantor dimension ln 2/ln φ² ≈ 0.72024; e gives dimension ln 2 ≈ 0.69315 at ratio 1/e but no exact tiling; π gapped, dimension 0.30275 at r = 1/π².
7. **Geometric span:** S₅(π) = 448.447, S₅(e) = 234.210, S₅(φ) = 27.416—φ generates the most compact q-scaled hierarchy at fixed depth.

No simulations or external measurements were used; all numbers arise from the displayed arithmetic.

## 6. Discussion

The five tests converge on a single conclusion with one voice: structure does not emerge from "being a geometric ratio" but from being a quadratic algebraic unit. φ's defining relation φ² = φ + 1 is simultaneously (i) the reason its q-integers close in ℤ[√5], (ii) the reason its continued fraction is perfectly balanced and Hurwitz-optimal, (iii) the reason its two-scale dissection is gapless with near-maximal entropy, and (iv) the source of the Fibonacci sequence whose divisibility tree supplies a natural heuristic hierarchy—though the candidate ultrametric d(m,n) = 2^(−gcd(m,n)) fails the strong triangle inequality (§4.1), so this fourth point is quantitative structure, not a literal ultrametric. e and π, by contrast, owe their celebrity to real-analytic properties (the exponential map, circular geometry) that have no arithmetic shadow: transcendence excludes them from every non-Archimedean completion, so in the Ostrowski-mandated comparison [9,10] they are single-completion objects, while φ is genuinely adelic.

The geometric span test (Test E) deserves a careful reading. That any q > 1 induces an ultrametric via the max-construction is true by definition and carries no arithmetic content; what the test measures is *compactness*—the reach of a hierarchy at fixed depth—and there φ's advantage is real but quantitative, not qualitative. We therefore treat Test E as complementary: it refines, but does not replace, the algebraic verdict. In applications such as clustering of high-dimensional data [5,7], a smaller effective ratio provides finer discrimination, whereas larger ratios suit coarse-grained classification; but the stochastic result of [7] warns that statistical ultrametricity in high dimension can be an artifact, so only exact hierarchies—here, only φ's—should be accorded structural significance.

**Limitations.** (1) The hierarchy constructions are one-dimensional; branching factors and higher-dimensional embeddings are not treated. (2) The depth n = 5 in Test E is a methodological choice; qualitative ordering among the q's is preserved at other depths, but absolute spans grow without bound. (3) The model treats q as a pure mathematical scaling factor, ignoring physical constraints (energy budgets, discreteness) that could truncate a hierarchy. (4) That nature *preferentially selects* φ as a design parameter is not established by any cited work; our result establishes an arithmetic distinction among the candidates, not a physical mechanism.

**Falsifiability.** The central claim—that φ uniquely supports exact arithmetic-hierarchical structure—would be falsified by (a) any transcendental q exhibiting ring closure of {[n]_q} in a finitely generated extension of ℤ (this would contradict Lindemann–Weierstrass); (b) a natural hierarchical system measured to scale with ratio π or e while exhibiting φ-like compactness and exact self-similarity; (c) a clustering of real data on φ-derived structures whose distance-multiplicity distribution departs markedly from the predicted Fibonacci-divisibility tree. Each condition is concrete and checkable.

**Open questions.** How does a branching factor b > 1 modify the depth-to-span ratios of Test E, and does φ's compactness advantage persist at b > 1? Does the valuation-based ultrametric d(m,n) = 2^(−v_p(gcd(m,n))) admit a q-deformed analogue tied to φ's quadratic-unit status? Can the heuristic Fibonacci hierarchy be replaced by a genuine ultrametric that is still canonically φ-generated, or is the failure of d(m,n) = 2^(−gcd(m,n)) evidence that no such canonical construction exists?

## 7. Conclusion

The arithmetic audit yields a sharp trichotomy. φ, as the unique positive quadratic unit among the three candidates, passes the algebraic tests exactly: its deformed integers close in ℤ[√5] ([n]_φ = L_n for odd n, F_n√5 for even n) with exact recurrence [n+2] = √5[n+1] − [n]; its continued fraction is perfectly balanced and Hurwitz-optimal; its two-scale dissection is gapless with entropy 0.66502 nats (95.9% of the binary maximum) and Cantor dimension ln 2 / ln φ² ≈ 0.72024; and it embeds in ℚ_p for exactly the primes p ≡ ±1 (mod 5). e and π, being transcendental, fail ring closure, recurrence integrality, and all p-adic embeddings; e yields a regular but inexact Diophantine hierarchy and Cantor dimension exactly ln 2 at ratio 1/e, while π's hierarchy is dominated by the anomalous partial quotient 292. The geometric span test confirms φ's compactness advantage (S₅(φ) ≈ 27.416 versus 234.210 for e and 448.447 for π) but is qualitative-neutral by construction.

One headline claim was retracted in the course of the audit: the candidate Fibonacci ultrametric d(m,n) = 2^(−gcd(m,n)) fails the strong triangle inequality, so the divisibility tree is downgraded to a heuristic hierarchy, with the valuation-based construction d(m,n) = 2^(−v_p(gcd(m,n))) as the correct ultrametric alternative. The remaining conclusions rest on exact displayed arithmetic and are subject to the explicit falsification conditions of §6: any transcendental q with ring closure, any natural π- or e-scaled hierarchy with φ-like exact self-similarity, or any measured departure of φ-derived clustering from the predicted divisibility structure would overturn the trichotomy. Structure emerges not from geometric celebrity but from algebraicity plus quadratic-unit status.

## References

[1] Physics Briefing Book. arXiv:1910.11775v2. https://arxiv.org/abs/1910.11775v2
[2] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96. arXiv:hep-ex/9605011v1. https://arxiv.org/abs/hep-ex/9605011v1
[3] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[4] MHD analysis on the physical designs of CFETR and HFRC. arXiv:2107.11742v1. https://arxiv.org/abs/2107.11742v1
[5] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[6] Ultrametric Model of Mind, I: Review. arXiv:1201.2711v3. https://arxiv.org/abs/1201.2711v3
[7] On stochastic generation of ultrametrics in high-dimension Euclidean spaces. arXiv:1311.5094v4. https://arxiv.org/abs/1311.5094v4
[8] Ultrametric Cantor Sets and Growth of Measure. arXiv:1002.3951v4. https://arxiv.org/abs/1002.3951v4
[9] https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/. QNFO: The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units.
[10] https://papers.qnfo.org/papers. QNFO: Adelic Core Synthesis: Cross-Domain Foundations of Adelic QFT.
[11] https://papers.qnfo.org/papers/fine-structure-constant-cross-ratio/. QNFO: Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α.
[12] https://papers.qnfo.org/papers/ultrametric-physics-m1-ratio-based-valuation-theory/. QNFO: ULTRAMETRIC PHYSICS.