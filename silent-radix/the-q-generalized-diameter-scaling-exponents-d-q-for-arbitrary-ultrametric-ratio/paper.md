# The q-Generalized α-Diameter: Scaling Exponents D_q^α for Arbitrary Ultrametric Ratios

## Abstract

In the QNFO ultrametric physics program, the fine-structure constant α has been reframed as a cross-ratio of two measurable electron length scales, and adelic extensions on Bruhat–Tits buildings have been proposed. A natural but unresolved question is how the characteristic "depth" associated with the α-gap behaves when the underlying ultrametric hierarchy is re-parameterized to an arbitrary scaling ratio q rather than the privileged ratio q = α⁻¹. This paper adopts the convention D_q^α = ln(1/α)/ln q: the number of hierarchy levels, measured in units of the ratio q, needed to span the interval between the classical electron radius and the reduced Compton wavelength. (Two alternative conventions for the symbol D_q^α — a fractional q-derivative and a Rényi multifractal exponent — were proposed by independent drafts; per the reconciliation policy, they are documented in Appendix A rather than silently merged.) We derive D_q^α in closed form, prove its monotonicity, base covariance, and multiplicativity, and evaluate it numerically for q ∈ {2, 3, φ, 10, α⁻¹}: D₂^α = 7.09841, D₃^α = 4.47860, D_φ^α = 10.22469, D₁₀^α = 2.13683, and D_{α⁻¹}^α = 1 exactly. We extend the construction to the Planck-to-electron scale gap, obtaining D_{α⁻¹} = 9.47262 levels, and verify by explicit arithmetic that the α-gap occupies exactly one self-normalized level within that hierarchy. All numerical results are derived from stated inputs by shown steps; no simulated or empirical data are used. The framework is deliberately definitional and arithmetic; its value is that it converts a physics constant into base-independent bookkeeping that any ultrametric model — clustering, epidemic, or cognitive — can import without re-derivation. Falsifiability criteria, failure modes, and convention-dependences are stated explicitly.

## 1. Introduction

Ultrametric spaces — spaces in which the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)) holds — organize distance hierarchically: at any scale, a point has a well-defined cluster, and clusters nest cleanly. This is the geometry of p-adic numbers, of hierarchical clustering in data, and, in the QNFO program, of a proposed physical organization of scale itself [9], [10], [12]. Within that program, the fine-structure constant α ≈ 1/137.036 has been reframed as a cross-ratio of two measurable electron length scales, the classical electron radius and the reduced Compton wavelength [11]. The reframing raises a question that is simple to state and worth answering precisely: if the α-gap is a rung on an ultrametric ladder, how many rungs is it, when the ladder's rung size is arbitrary?

Every ultrametric model implicitly chooses a scaling ratio q — the factor by which distances shrink (or grow) per hierarchical level. The p-adic norm chooses q = p; binary dendrograms choose q = 2; decimal exponents choose q = 10. A depth measured in one base is not directly comparable to a depth in another, and a claim such as "the α-gap is one level deep" is meaningless until the base is fixed. The present paper supplies the conversion table and the algebra behind it. We define D_q^α, prove its elementary but load-bearing properties, compute it exactly for a family of bases, and show how the same machinery handles the vastly larger Planck-to-electron gap.

Our contribution is deliberately modest in physics ambition and strict in arithmetic discipline. Every number in Section 4 is derived from stated inputs by shown steps; every projected number is clearly labeled with its assumptions. The payoff is a base-independent quantity — the product of depth and log of base is invariant — that any adjacent field importing ultrametric structure can use as a unit conversion, in the same spirit that community planning documents fix shared targets before detailed designs begin [1], [2].

We write for an adjacent-field expert. An *ultrametric* is a metric in which all triangles are isosceles with the two long sides equal; equivalently, balls at each level are either disjoint or nested. A *scaling ratio* q > 1 is the contraction factor per hierarchical level; q need not be an integer, and much of this paper is about what changes — and what does not — when it is not.

## 2. Background and Related Work

**Programmatic context.** The QNFO corpus anchors this work. The ultrametric physics research corpus [9] states the general program; the research plan [10] organizes its open problems, of which arbitrary-q re-parameterization of characteristic depths is one; the cross-ratio reframing of the fine-structure constant [11] demonstrates the methodological stance — reframing a physical constant as a geometric invariant with explicit falsifiability conditions — that we adopt here; and the adelic core synthesis [12] assembles p-adic analysis, Bruhat–Tits geometry, Ostrowski completions, and information-theoretic foundations into a single structure against which any relaxation of the base q must be measured. Our D_q^α is a small, sharp tool intended to slot into that synthesis: on a Bruhat–Tits building, levels are horoball layers indexed by a valuation, and D_q^α counts layers.

**Ultrametric foundations.** The view of ultrametrics as a zero-dimensional analogue of ordinary metrics, with the expectation that metric-space theorems admit ultrametric parallels, is systematized in the embedding–extension–interpolation program [3], which provides ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff compactness characterization. This matters here because D_q^α is a depth functional on an ultrametric space, and the embedding and extension results of [3] are what license moving such a functional between spaces without distortion — the formal backing for our "base covariance" claim in Section 3.

**Data-induced ultrametrics.** Murtagh [5] shows how cross-tabulation data, given a Euclidean metric by correspondence analysis, induces an ultrametric that models anomaly and change as transitions between hierarchy levels, particularly along a sequential axis. The induced ultrametric there is built sequentially, and nothing forces the level-to-level contraction to be an integer ratio; this is a concrete empirical source of arbitrary-q hierarchies and a direct motivation for our parameterization. Murtagh's related work modeling Matte Blanco's principles of symmetric and asymmetric being through ultrametric topology [7] makes the same point cognitively: hierarchical clustering of text and questionnaire data yields ultrametric topologies whose branch ratios are data-determined, not prime-determined. A depth functional like D_q^α would quantify how many asymmetric "levels" separate two concepts, in a base the analyst chooses.

**Ultrametric Cantor sets.** Raut and Datta's ultrametric Cantor sets [6], built from relative infinitesimals and an inversion rule, carry a valuation that is simultaneously scale- and reparametrisation-invariant. That invariance is the deepest precedent for our base-covariance property (D_q^α · ln q = const): if the valuation of [6] survives reparametrization, then invariance under change of ruler is a natural demand on ultrametric observables, and our finite, computable cousin of that invariance inherits its legitimacy.

**Ultrametric dynamics.** The ultrametric SIR model of epidemic spread [8] introduces ultrametrics on populations via hierarchical clustering by average time of infectious contact, with p-adic parameterization as a concrete implementation. There, q is literally a contact-time ratio; our conversion formula lets one translate results between p-adic and binary parameterizations, and Section 5 gives the uncertainty propagation for such an import.

**Contrast with experimental strategy documents.** The Physics Briefing Book of the European Particle Physics Strategy Update [1] exemplifies a bottom-up process in which community inputs structure near-, mid-, and long-term priorities; the Snowmass '96 Next Linear Collider report [2] reviewed design expectations for an e⁺e⁻ collider at 500 GeV–1 TeV and its role in physics beyond the Standard Model. We cite these not for content on scaling — they have none — but as calibration for how a speculative formal proposal should position itself relative to an experimental community: as an input to broader deliberation, with explicit feasibility discussion and falsifiable claims, a discipline we import into Section 6. Similarly, the MHD design analysis of CFETR and HFRC [4] shows fusion physics confronting hierarchical, multi-scale magnetohydrodynamic structure in engineering practice — two design points related by a large ratio, compared by expressing the ratio in a common logarithmic unit. Our paper does to the α-gap what such comparative design studies do to parameter ranges.

Collectively, these twelve works supply the mathematical license [3], [6], the empirical motivation [5], [7], [8], the programmatic target [9]–[12], and the rhetorical discipline [1], [2], [4] for the construction that follows.

## 3. Methods

**3.1 Setup and definitions.** Let (X, d_u) be an ultrametric space whose balls at level n have characteristic diameter q⁻ⁿ for a fixed scaling ratio q > 1; equivalently, the associated valuation v_q(x, y) = −ln d_u(x, y)/ln q is integer-valued on a dense set of pairs. The strong triangle inequality makes level sets of v_q a hierarchy: two points lie in a common level-n ball iff v_q(x, y) ≥ n.

**Definition 1 (q-generalized α-diameter).** Let R_α = λ_C / r_e denote the ratio of the reduced Compton wavelength λ_C to the classical electron radius r_e. The q-generalized α-diameter is

  D_q^α := log_q R_α = ln R_α / ln q,  q > 1.

Because r_e = α λ_C (verified from stated inputs in Section 4), R_α = 1/α, so D_q^α = ln(1/α)/ln q.

**Definition 2 (generalized diameter for an arbitrary gap).** For any scale ratio R > 1, D_q(R) := ln R / ln q. Then D_q^α = D_q(1/α).

**3.2 Properties.** (i) *Monotonicity:* ∂D_q/∂q = −ln R/(q (ln q)²) < 0 for R > 1, so D decreases strictly in q. (ii) *Base covariance:* for bases q, q′ > 1, D_q(R) ln q = D_{q′}(R) ln q′ = ln R. The product depth × ln(base) is the invariant content; depth alone is unit-dependent. (iii) *Multiplicativity:* D_q(R₁ R₂) = D_q(R₁) + D_q(R₂), inherited from ln. (iv) *Normalization:* choosing q = R makes D = 1 — the gap is "one level" in its own base. These are one-line consequences of Definition 2 and are verified numerically in Section 4.

**3.3 Interpretations.** (a) *Valuation depth on buildings:* on a Bruhat–Tits building for a group over a discretely valued field, horoball layers are indexed by valuation; D_q^α counts layers between the two electron scales when the local parameter has ratio q [12]. (b) *Information content:* D₂^α = log₂(1/α) is the number of bits needed to encode the α-gap resolution; D_q^α ln q = ln(1/α) is the same content in nats. (c) *Model import:* any ultrametric model with its own q — clustering [5], [7], epidemic contact hierarchies [8] — can express the α-gap in its native levels by a single division.

**3.4 Inputs.** All numerical work uses: α = 1/137.035999 (CODATA-style value as adopted in the QNFO cross-ratio reframing [11]); reduced Compton wavelength λ_C = 3.861593 × 10⁻¹³ m; classical electron radius r_e = 2.817940 × 10⁻¹⁵ m; Planck length ℓ_P = 1.616255 × 10⁻³⁵ m. These are stated inputs, not measurements performed here.

## 4. Analysis

**4.1 The α-gap ratio.** Input: α = 1/137.035999 [11]. Then 1/α = 137.035999 and

  ln(1/α) = ln 137.035999 = ln 137 + ln(1.00026277).

Compute: ln 137 = ln 1.37 + 2 ln 10 = 0.3148107 + 4.6051702 = 4.9199809; ln(1.00026277) ≈ 0.0002627. So **ln(1/α) = 4.9202436**. Cross-check: e^4.92 = e^5/e^0.08 = 148.4132/1.083287 = 137.004; e^4.92024 ≈ 137.004 × e^0.00024 ≈ 137.037 ✓.

**4.2 The electron-scale identity.** r_e / λ_C = 2.817940 × 10⁻¹⁵ / 3.861593 × 10⁻¹³ = 2.817940/386.1593 = 0.00729735 = α (check: 386.1593 × 0.007 = 2.70312; 386.1593 × 0.00029735 = 0.114823; sum = 2.817940 ✓). Hence R_α = λ_C/r_e = 1/α = 137.035999, confirming D_q^α = ln(1/α)/ln q.

**4.3 Base evaluation table.** Using ln(1/α) = 4.9202436:

- q = 2: ln 2 = 0.6931472. 0.6931472 × 7 = 4.8520304; remainder 0.0682132; /0.6931472 = 0.09841. **D₂^α = 7.09841.**
- q = 3: ln 3 = 1.0986123. 1.0986123 × 4 = 4.3944492; remainder 0.5257944; /1.0986123 = 0.478599. **D₃^α = 4.47860.**
- q = 10: ln 10 = 2.3025851. 2.3025851 × 2 = 4.6051702; remainder 0.3150734; /2.3025851 = 0.136835. **D₁₀^α = 2.13683.**
- q = φ = 1.6180339: ln φ = 0.4812118. 0.4812118 × 10 = 4.8121180; remainder 0.1081256; /0.4812118 = 0.224690. **D_φ^α = 10.22469.**
- q = α⁻¹ = 137.035999: ln q = 4.9202436 = ln(1/α), so **D_{α⁻¹}^α = 1 exactly.**

**4.4 Property verification by arithmetic.** Monotonicity: 7.09841 (q=2) > 4.47860 (q=3) > 2.13683 (q=10) ✓, consistent with ∂D/∂q < 0. Base covariance: D₂^α ln 2 = 7.09841 × 0.6931472 = 4.92024 ✓; D₁₀^α ln 10 = 2.13683 × 2.3025851 = 4.92024 ✓; D_φ^α ln φ = 10.22469 × 0.4812118 = 4.92024 ✓. All three products equal ln(1/α) to the digits shown. Multiplicativity example: D₂((1/α)²) = 2 × 4.9202436/0.6931472 = 14.19682 = 2 × 7.09841 ✓.

**4.5 The Planck-to-electron gap.** R_P = r_e/ℓ_P = 2.817940/1.616255 × 10²⁰ = 1.743522 × 10²⁰ (check: 1.616255 × 1.743522 = 2.817937, agreement to 6 digits ✓). ln R_P = ln 1.743522 + 20 ln 10 = 0.555890 + 46.051702 = 46.607592. Then:

- D_{α⁻¹}(R_P) = 46.607592/4.9202436 = 9 + 2.3253996/4.9202436 = **9.47262.**
- D₂(R_P) = 46.607592/0.6931472 = 67 + 0.1667296/0.6931472 = **67.24055.**
- D₁₀(R_P) = 46.607592/2.3025851 = 20 + 0.555890/2.3025851 = **20.24141.**

**4.6 Composition check.** λ_C/ℓ_P = 3.861593 × 10⁻¹³/1.616255 × 10⁻³⁵ = 2.389298 × 10²²; ln = 0.870899 + 50.656872 = 51.527771. D_{α⁻¹}(λ_C/ℓ_P) = 51.527771/4.9202436 = **10.47262**. Check multiplicativity: 10.47262 − 9.47262 = 1.00000 = D_{α⁻¹}^α ✓. The α-gap is exactly one level in its own base, embedded at level ≈ 9.47 of the Planck-to-electron hierarchy — an arithmetic identity, but a tidy one.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs. No simulation or empirical measurement is reported.

**R1.** The α-gap ratio is R_α = 1/α = 137.035999, with ln R_α = 4.9202436.

**R2.** q-generalized α-diameters: D₂^α = 7.09841; D₃^α = 4.47860; D₁₀^α = 2.13683; D_φ^α = 10.22469; D_{α⁻¹}^α = 1 (exact).

**R3.** Base covariance holds numerically: D_q^α · ln q = 4.92024 for q ∈ {2, 10, φ}, confirming the invariant ln(1/α).

**R4.** Planck-to-electron gap: R_P = 1.743522 × 10²⁰, ln R_P = 46.607592; D_{α⁻¹}(R_P) = 9.47262 levels, D₂(R_P) = 67.24055 bits, D₁₀(R_P) = 20.24141 decimal levels.

**R5.** Composition: D_{α⁻¹}(λ_C/ℓ_P) = 10.47262, and 10.47262 − 9.47262 = 1.00000 = D_{α⁻¹}^α, verifying that the α-gap occupies exactly one self-normalized level within the Planck-to-electron hierarchy.

**R6 (labeled projection, not a computation).** If an ultrametric epidemic-style hierarchy [8] uses a contact-time ratio q, importing the α-gap costs D_q^α levels per the table in R2; the uncertainty in such an import is entirely the uncertainty in q, propagating as δD ≈ (ln R_α/(q (ln q)²)) δq. For q = 2 and a 1% uncertainty in q (δq = 0.02): δD = 4.9202436 × 0.02/(2 × 0.480453) = 0.0984048/0.960906 = 0.10241, i.e., D₂^α = 7.098 ± 0.102 under that assumption. This is a projection from an assumed input uncertainty, not a measured one.

## 6. Discussion

**Limitations.** The central limitation is definitional: D_q^α is a bookkeeping quantity, not a new physical prediction. It converts a known ratio between bases; nothing here constrains α itself. The cross-ratio reframing of [11] supplies the physical interpretation of R_α, but our depth functional would work equally for any ratio, which is both its utility and its emptiness as physics. Second, the assumption of a single uniform ratio q per level is idealized: real dendrograms [5], [7] and real contact hierarchies [8] have non-uniform branching, and a level-counting functional presupposes the homogeneous-lattice idealization underlying Bruhat–Tits buildings [12]. Third, the choice of privileged base q = α⁻¹, which makes D = 1, is cosmetic — every gap is one level in its own base — and one should resist reading numerology into R5; the exactness there is an arithmetic identity (D_R(R) = 1 for any R), not evidence of design.

**Convention-dependence.** If the two electron scales were not taken in the exact ratio α — e.g., if one used the unreduced Compton wavelength 2πλ_C = 2.426310 × 10⁻¹² m — the identity r_e/λ_C = α would fail: r_e/λ_C^{unreduced} = 2.817940/2426.310 × 10⁻³ = 0.00116141 = α/2π, and the "α-gap" would instead be a (2π/α)-gap with ln = 4.9202436 + 1.8378771 = 6.7581207, giving D₂ = 9.74997. Which convention is adopted changes results materially; we resolve in favor of the reduced wavelength per [11] and flag the dependence here rather than burying it.

**Failure modes.** If the hierarchy's branch ratios fluctuate, the level structure underlying Definition 1 fails and D_q^α is undefined rather than merely approximate. If a user applies the conversion to a hierarchy whose q is not independently constrained, the output inherits that unconstrained status and can manufacture spurious coincidences.

**Falsifiability.** The mathematical claims (monotonicity, covariance, multiplicativity) are theorems from Definition 2 and cannot be falsified, only the derivations checked. The interpretive claims are falsifiable: if the QNFO program's adelic extension [11], [12] turns out to have no observable consequence tied to level-counting on buildings — i.e., if no measurement distinguishes hierarchies parameterized by different q — then D_q^α is pure convention with no physical anchor. Conversely, a measurement or model that exhibits a preferred, empirically fixed q (as p-adic parameterization fixes q = p in [8]) would give D_q^α empirical teeth.

**Against ourselves.** A skeptic will say: you have computed logarithms. True. Our defense is narrower than the framing might suggest — that in cross-disciplinary programs where ultrametric language migrates between fields [5], [7], [8], unexamined base-dependence is a real source of spurious coincidence (a "depth of 7" in base 2 is a "depth of 2.14" in base 10), and that publishing the conversion algebra, with every step shown, is cheap insurance. If the QNFO program's larger claims [9], [10] mature, this paper is a footnote; if they do not, the arithmetic stands.

**Open questions.** (1) Does a canonical base exist — e.g., selected by Ostrowski-completion structure [12] — or is base choice irreducibly conventional? (2) Can D_q^α be given a variational characterization over the hierarchy? (3) How does the framework extend to non-discrete valuations, where levels are continuous and "level-counting" must be replaced by measure-theoretic depth in the spirit of the scale-invariant valuation of [6]? (4) Does the embedding/extension machinery of [3] guarantee that D_q^α is preserved under the ultrametric Arens–Eells embedding, making it a genuine isometry invariant? We pose these rather than answer them.

## 7. Conclusion

We defined the q-generalized α-diameter D_q^α = ln(1/α)/ln q, proved its monotonicity, base covariance, and multiplicativity, and evaluated it for q ∈ {2, 3, φ, 10, α⁻¹}, obtaining 7.09841, 4.47860, 2.13683, 10.22469, and 1 exactly. The invariant content ln(1/α) = 4.9202436 nats was verified numerically across three bases. Extended to the Planck-to-electron gap, the framework yields 9.47262 levels in the self-normalized base and confirms by explicit arithmetic that the α-gap occupies exactly one such level within that hierarchy. The construction is a unit-conversion tool for ultrametric modeling — deliberately modest, fully arithmetic, and offered, in the bottom-up spirit of community strategy processes [1], as an input to the QNFO program's broader synthesis [9]–[12]. Its value now depends on measurement: an empirically fixed, preferred scaling ratio in a real hierarchy would elevate D_q^α from bookkeeping to physics.

## References

[1] Physics Briefing Book. arXiv:1910.11775v2. https://arxiv.org/abs/1910.11775v2
[2] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96. arXiv:hep-ex/9605011v1. https://arxiv.org/abs/hep-ex/9605011v1
[3] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[4] MHD analysis on the physical designs of CFETR and HFRC. arXiv:2107.11742v1. https://arxiv.org/abs/2107.11742v1
[5] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[6] Ultrametric Cantor Sets and Growth of Measure. arXiv:1002.3951v4. https://arxiv.org/abs/1002.3951v4
[7] Ultrametric Model of Mind, I: Review. arXiv:1201.2711v3. https://arxiv.org/abs/1201.2711v3
[8] Toward ultrametric modeling of the epidemic spread. arXiv:2005.08761v3. https://arxiv.org/abs/2005.08761v3
[9] https://papers.qnfo.org/papers/ultrametric-physics-m1-ratio-based-valuation-theory/. QNFO: ULTRAMETRIC PHYSICS.
[10] https://papers.qnfo.org/papers/ultrametric-physics-m12-synthesis/. QNFO: Ultrametric Physics Research Plan.
[11] https://papers.qnfo.org/papers/fine-structure-constant-cross-ratio/. QNFO: Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α.
[12] https://papers.qnfo.org/papers. QNFO: Adelic Core Synthesis: Cross-Domain Foundations of Adelic QFT.

## Appendix A. Divergence report

**D1 (core definition of D_q^α) — DIVERGENT, three-way.** Draft A defines D_q^α as a generalized fractional Jackson q-derivative, an infinite series over q-powers of f with generalized binomial coefficients, reducing to the Jackson derivative at α = 1 (benchmark: D_{0.6}^{0.5} x²|_{x=5} ≈ 14.33 via three-term truncation). Draft B defines D_q^α as a Rényi-type multifractal exponent, D_q^α = (1/(1−α)) lim log Z_n(α)/(n log q) on refining ultrametric partitions (benchmarks: uniform Cantor spectrum flat at ln 2/ln 3 = 0.63093; biased (1/3, 2/3) spectrum decreasing from 0.63093 to 0.36907; D_{2.5}^0 = 0.75647). Draft C defines D_q^α = ln(1/α)/ln q, a logarithmic depth of the electron-scale α-gap (benchmarks: D₂^α = 7.09841, etc.). *Underlying convention:* each draft fixes a different meaning of the pair (q, α) — (scaling ratio, derivative order), (refinement ratio, moment order), (rung size, physical fine-structure constant). These are incompatible definitions sharing a symbol; no arithmetic reconciliation is possible without choosing one. *Resolution:* the main text adopts Draft C's convention, because it is the only one in which α is a stated physical input tied to the QNFO cross-ratio program [11], all its numerical claims are exact closed-form arithmetic with no truncation or limit-taking, and its structural properties (monotonicity, covariance, multiplicativity) are provable rather than truncation-dependent. Drafts A and B are recorded here as alternative conventions; their numerical results are not asserted in the main text and are not comparable to the adopted values (they answer different questions). No silent merge was performed.

**D2 (axis of monotonicity) — DIVERGENT.** Draft B proves/verifies monotonicity of its exponent in the moment order α; Draft C proves monotonicity of its depth in the base q. These are monotonicity statements about different objects under the divergent definitions of D1; the main text retains only the q-monotonicity of the adopted convention.

**D3 (role of strategy/engineering documents [1], [2], [4]) — DIVERGENT in emphasis, convergent in substance.** Draft A treats [1], [2], [4] as substantive motivation (scaling ladders in collider staging, hierarchical time scales in MHD); Drafts B and C treat them as rhetorical/positional calibration only, noting explicitly that they contain no scaling content. *Resolution:* the main text follows B/C (calibration framing), which is the more defensible reading of those sources; A's stronger motivational reading is recorded here.

**D4 (physical scope) — DIVERGENT.** Draft A claims applicability to ultrametric SIR dynamics and fusion MHD modeling via its derivative operator; Draft C claims only unit-conversion utility for such models. *Resolution:* the conservative C claim is adopted; A's stronger claim depends on the rejected definition in D1.

## Appendix B. Claim attribution

| # | Claim | Drafts | Status |
|---|-------|--------|--------|
| C1 | D_q^α is a fractional Jackson q-derivative (series definition) | A | SINGLE (divergent; see D1) |
| C2 | D_q^α is a Rényi multifractal exponent on refining partitions | B | SINGLE (divergent; see D1) |
| C3 | D_q^α = ln(1/α)/ln q, a base-dependent depth of the α-gap | C | SINGLE (adopted; see D1) |
| C4 | Ultrametric = strong triangle inequality; balls nest hierarchically | B, C | CONVERGENT |
| C5 | [3] supplies ultrametric embedding/extension/compactness theorems licensing transfer of functionals | A, B, C | CONVERGENT |
| C6 | [5]: correspondence analysis induces sequential ultrametrics from data; branch ratios are data-determined | A, B, C | CONVERGENT |
| C7 | [6]: ultrametric Cantor sets carry scale- and reparametrisation-invariant valuation | A, B, C | CONVERGENT |
| C8 | [8]: ultrametric SIR model builds hierarchies via contact-time clustering; p-adic parameterization fixes q = p | B, C | CONVERGENT |
| C9 | [1], [2], [4] contain no scaling content and are cited as rhetorical/positional calibration only | B, C | CONVERGENT (A's stronger motivational reading recorded in D3) |
| C10 | Monotonicity of D_q^α in the base q | C | SINGLE (adopted; see D2) |
| C11 | Base covariance: D_q(R) ln q = ln R, invariant across bases | C | SINGLE (adopted; see D1) |
| C12 | D_q^α applies to epidemic/MHD models as unit conversion, not as new dynamics | C | SINGLE (adopted; see D4) |