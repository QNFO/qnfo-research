---
title: "Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α"
author: Rowan Brad Quni-Gudzinas
orcid: 0009-0002-4317-5604
isni: 0000000526456062
date: 2026-07-12
version: 1.0
doi: ""
license: QNFO Unified License Agreement (QNFO-ULA): https://legal.qnfo.org/
abstract: >
  The fine-structure constant $\alpha \approx 1/137.036$ is reframed as the cross-ratio of two
  measurable electron length scales (classical radius $r_e$ / Compton wavelength $\lambda_C$).
  This reveals projective invariance in $\alpha$, connects to integer-ratio precision experiments,
  and integrates five mathematical formalisms: adelic, projective, topological, syntactic, and
  hierarchical. Version 1.0 adds the adelically extended cross-ratio on Bruhat–Tits buildings
  (§7.7), explicit falsifiability conditions (§8.4), and synthesis with the QNFO adelic physics
  program (July 2026).
---

# Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α

## Abstract

The fine-structure constant $\alpha \approx 1/137.036$ is reframed as the cross-ratio of two measurable electron length scales (classical radius $r_e$ / Compton wavelength $\lambda_C$). This reveals projective invariance in $\alpha$, connects to integer-ratio precision experiments, and integrates five mathematical formalisms: adelic, projective, topological, syntactic, and hierarchical. Version 1.0 adds the adelically extended cross-ratio on Bruhat–Tits buildings (§7.7), explicit falsifiability conditions (§8.4), and synthesis with the QNFO adelic physics program (July 2026).

# 1. Introduction

The fine-structure constant $\alpha \equiv e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137.035999084$ is one of the most precisely measured dimensionless numbers in physics [established]. Its value governs the strength of electromagnetic interactions across all energy scales accessible to current experiment. Yet after a century of measurement, its origin remains unexplained — it appears in the Standard Model as a free parameter, inserted by hand rather than derived from deeper principles.

The standard presentation frames $\alpha$ as an abstract coupling strength assembled from three dimensionful constants ($e$, $\hbar$, $c$). While this construction is empirically correct, it obscures a possibility: that $\alpha$ might be understood geometrically, as an invariant of a deeper mathematical structure.

This paper proposes such a geometric understanding. We reframe $\alpha$ as the cross-ratio of two measurable length scales associated with the electron:

$$\alpha = \text{CR}(r_e, \lambda_C; 0, \infty) = \frac{r_e}{\lambda_C}$$

where $r_e = e^2/(4\pi\varepsilon_0 m_e c^2)$ is the classical electron radius and $\lambda_C = h/(m_e c)$ is the Compton wavelength. The cross-ratio is the fundamental invariant of projective geometry — preserved under all projective transformations. This reframing reveals that $\alpha$ carries a projective invariance that the standard formulation conceals.

The paper is organized as follows. §2 reviews the historical and theoretical context of $\alpha$. §3 introduces projective geometry and the cross-ratio. §4 constructs the cross-ratio from electron length scales. §5 develops the mathematical formalism of projective invariance. §6 explores implications for precision measurement. §7 connects this framework to other formalisms, including the adelic extension (§7.7). §8 discusses falsifiability (§8.4) and open questions.

---

# 2. The Fine-Structure Constant: Historical and Theoretical Context

## 2.1 Measurement History

Arnold Sommerfeld introduced $\alpha$ in 1916 to explain the fine structure of hydrogen spectral lines [established]. Since then, its value has been measured with extraordinary precision through multiple independent methods:

| Method | Measured $\alpha^{-1}$ | Uncertainty | Year |
|:-------|:----------------------|:------------|:-----|
| Electron $g-2$ (Gabrielse) | 137.035999084(21) | 0.15 ppb | 2023 |
| Rubidium atom recoil (Morel) | 137.035999206(11) | 0.081 ppb | 2020 |
| Cesium atom recoil (Parker) | 137.035999046(27) | 0.20 ppb | 2018 |
| CODATA 2018 | 137.035999084(21) | 0.15 ppb | 2019 |

The agreement across independent methods confirms the constancy of $\alpha$ at low energies. However, the $g-2$ and atom-recoil measurements show a ~5.5$\sigma$ tension when interpreted through the Standard Model, hinting at possible new physics [debated, $g-2$ vs. Rb 2020–2023].

## 2.2 Theoretical Status

In the Standard Model, $\alpha$ is not predicted — it is measured and inserted. At higher energies, the renormalization group causes $\alpha$ to run: $\alpha(Q^2)$ increases from ~1/137 at low energies to ~1/128 at the $Z$ boson mass. This running is well-understood [established], but the low-energy value remains unexplained.

Several historical attempts to derive $\alpha$ have been proposed:

- **Eddington's numerology** (1929–1946): $\alpha^{-1} = 16 + \frac{1}{2}16(16-1) = 136$, later revised to 137. This was post-hoc curve fitting, not a derivation [speculative, disconfirmed].

- **Wyler's formula** (1969): $\alpha = (9/8\pi^4)(\pi^5/2^4 5!)^{1/4}$ gave 1/137.03608, close to the measured value. However, the derivation lacked physical motivation and relied on arbitrary group-theoretic factors [speculative, no experimental support].

- **Grand unification**: In GUTs, the gauge couplings unify at high energies and $\alpha$ at low energies is determined by the renormalization group running from the unification scale. This approach predicts relationships between couplings but does not uniquely determine $\alpha$ without additional parameters [speculative].

- **Anthropic reasoning**: In a multiverse, $\alpha$ may vary across domains, and we observe a value compatible with carbon-based life [speculative, not yet falsifiable].

## 2.3 The Dimensionality Puzzle

A deeper question concerns dimensionality itself. The standard expression:

$$\alpha = \frac{e^2}{4\pi\varepsilon_0\hbar c}$$

combines three dimensionful constants. In natural units ($\hbar = c = 1$), $\alpha = e^2/4\pi$, but this merely hides the dimensions in the unit choice. The fact that $\alpha$ is dimensionless while built from dimensionful inputs suggests that the dimensionful constants may themselves encode ratios of more fundamental length scales.

---

# 3. Projective Geometry and the Cross-Ratio

## 3.1 The Cross-Ratio as Projective Invariant

Projective geometry studies properties invariant under projective transformations — the most general transformations preserving collinearity. The fundamental projective invariant of four collinear points $A, B, C, D$ is the cross-ratio:

$$\text{CR}(A, B; C, D) = \frac{(A-C)(B-D)}{(A-D)(B-C)}$$

where the notation $(X-Y)$ denotes the directed distance between points $X$ and $Y$.

The cross-ratio is invariant under ALL projective transformations (homographies) of the form:

$$x \mapsto \frac{ax + b}{cx + d}, \quad ad - bc \neq 0$$

This invariance is absolute: any configuration of four collinear points has the same cross-ratio in any projective coordinate system [established, projective geometry since Poncelet 1822].

## 3.2 Special Cases

When one point is at infinity, the cross-ratio simplifies:

$$\text{CR}(A, B; C, \infty) = \frac{A-C}{B-C}$$

This is simply the ratio of two directed distances. When two points are at $\\{0, \infty\\}$:

$$\text{CR}(A, B; 0, \infty) = \frac{A}{B}$$

This is the simplest form: the cross-ratio reduces to the ratio of two distances measured from the origin.

## 3.3 Physical Interpretation

The cross-ratio's projective invariance has profound implications for physics. If a physical quantity can be expressed as a cross-ratio of measurable lengths, then that quantity inherits projective invariance — it is independent of the choice of coordinate system, unit system, or projective frame.

This is precisely the property that $\alpha$ exhibits: it is dimensionless (coordinate-independent), and its value is the same regardless of the unit system used to measure $e$, $\hbar$, and $c$. The cross-ratio framework explains WHY $\alpha$ is dimensionless: it is not merely that the dimensions cancel, but that $\alpha$ is a projective invariant of the electron's intrinsic length scales.

---

# 4. Electron Length Scales and the Cross-Ratio Construction

## 4.1 Two Intrinsic Electron Length Scales

The electron possesses two natural length scales:

1. **Classical electron radius**:
   $$r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.818 \times 10^{-15}\\ \text{m}$$

2. **Compton wavelength** (reduced):
   $$\lambda_C = \frac{\hbar}{m_e c} \approx 3.862 \times 10^{-13}\\ \text{m}$$

Both are constructed from the same physical constants ($e$, $m_e$, $\hbar$, $c$) but in different combinations. Their ratio is:

$$\frac{r_e}{\lambda_C} = \frac{e^2/(4\pi\varepsilon_0 m_e c^2)}{\hbar/(m_e c)} = \frac{e^2}{4\pi\varepsilon_0\hbar c} = \alpha$$

This ratio is exactly the fine-structure constant.

## 4.2 The Cross-Ratio Formulation

Define four points on a projective line representing length scales:

- $A = 0$ (the origin — zero length)
- $B = r_e$ (classical electron radius)
- $C = \lambda_C$ (Compton wavelength)
- $D = \infty$ (the point at infinity)

The cross-ratio is:

$$\text{CR}(0, r_e; \lambda_C, \infty) = \frac{(0 - \lambda_C)(r_e - \infty)}{(0 - \infty)(r_e - \lambda_C)}$$

Using the properties of the point at infinity, this simplifies to:

$$\alpha = \frac{r_e}{\lambda_C}$$

## 4.3 Physical Meaning

This construction reveals that $\alpha$ is not an arbitrary coupling constant but a geometric ratio of the electron's intrinsic length scales. The classical electron radius $r_e$ represents the length scale at which electromagnetic self-energy equals the rest mass energy. The Compton wavelength $\lambda_C$ represents the length scale at which quantum uncertainty in position becomes comparable to the particle's size.

The fact that $r_e \ll \lambda_C$ (by a factor of ~1/137) means that electromagnetic self-energy effects are "small" compared to quantum uncertainty — the electron's charge is weak enough that its self-interaction is a small perturbation on its quantum nature.

## 4.4 Comparison with Other Particles

For the muon:
$$\frac{r_e^{(\mu)}}{\lambda_C^{(\mu)}} = \frac{e^2}{4\pi\varepsilon_0\hbar c} = \alpha$$

The same $\alpha$ appears because the electric charge $e$ is the same for all charged leptons [established, lepton universality]. The cross-ratio formulation explains this universality: $\alpha$ is the projective invariant of the electromagnetic interaction itself, independent of the mass of the particle experiencing it.

---

# 5. Mathematical Formalism: Projective Invariance

## 5.1 Projective Frame Dependence

Let $\mathcal{P}^1$ be the real projective line. A projective frame is a choice of three distinct points $\\{p_0, p_1, p_\infty\\}$ that define the coordinate system. In such a frame, any point $x \in \mathcal{P}^1$ is assigned the coordinate:

$$[x] = \text{CR}(x, p_1; p_0, p_\infty)$$

The cross-ratio $\text{CR}(A, B; C, D)$ is independent of the choice of frame — it is an absolute invariant of the four points.

## 5.2 The Electron as a Projective Structure

The electron's intrinsic length scales $\\{0, r_e, \lambda_C, \infty\\}$ constitute four collinear points on a projective line. Their cross-ratio is:

$$\text{CR}(0, r_e; \lambda_C, \infty) = \alpha$$

This means the electron's electromagnetic structure is characterized by a single projective invariant. Different choices of projective frame (different unit systems, different normalizations) produce different coordinate representations of $r_e$ and $\lambda_C$, but their cross-ratio is frame-independent.

## 5.3 The Dimensionless Constants as Projective Invariants

This framework suggests a broader principle: ALL dimensionless physical constants may be expressible as cross-ratios of more fundamental length scales.

| Constant | Proposed Cross-Ratio | Status |
|:---------|:---------------------|:-------|
| $\alpha$ | $r_e/\lambda_C$ | Demonstrated here |
| $m_e/m_\mu$ | Mass ratio as projective invariant | [speculative] |
| $\alpha_G = Gm_p^2/\hbar c$ | Gravitational analogue | [speculative] |
| $\sin^2\theta_W$ | Weinberg angle as cross-ratio of gauge couplings | [speculative] |

If all dimensionless constants are projective invariants, then physics reduces to the study of projective structures over the reals, complex numbers, and p-adic fields. This is the central conjecture of the QNFO adelic physics program [speculative, see §7.7].

---

# 6. Implications for Precision Measurements

## 6.1 Integer-Ratio Precision

The cross-ratio formulation suggests that $\alpha$ might be expressible as an exact ratio of integers derived from deeper combinatorial or topological principles. Specifically:

$$\alpha^{-1} \approx 137$$

has tantalizing near-integer properties:

$$137.035999084 = 137 + \frac{1}{27.79\ldots}$$

While no exact integer formula has been found, the cross-ratio framework provides geometric motivation for searching: if the relevant length scales arise from a discrete geometric structure (e.g., a Bruhat–Tits building — see §7.7), then their ratio would naturally be a rational number.

## 6.2 Testable Predictions

The cross-ratio framework makes specific, falsifiable predictions:

1. **Running of $\alpha$ as projective curvature**: The renormalization group running of $\alpha(Q^2)$ should be interpretable as the curvature of a projective connection over the space of energy scales. This predicts a specific functional form for the running that can be tested against precision LEP data.

2. **Integer-ratio structure at the Planck scale**: If the electron's length scales originate from a discrete projective geometry, there should be residual signatures at high energies — specifically, rational multiples in the running of $\alpha^{-1}$ near the Planck scale.

3. **Universality across gauge groups**: The cross-ratio framework generalizes to all gauge couplings. It predicts that $\alpha_s(Q^2)$ and $\sin^2\theta_W(Q^2)$ are similarly expressible as projective invariants, leading to specific relationships between them at the unification scale.

## 6.3 Current Experimental Constraints

| Prediction | Current Constraint | Test Feasibility |
|:-----------|:-------------------|:-----------------|
| Projective running of $\alpha$ | Consistent with SM at LEP precision | Requires ~10× improvement in $\alpha(M_Z)$ measurement |
| Integer-ratio at Planck scale | Untestable directly | Indirect tests via GUT-scale predictions |
| Gauge coupling relations | Consistent with MSSM unification | Distinguishable with future collider data |

---

# 7. Connections to Other Formalisms

## 7.1 Klein's Erlangen Program

Felix Klein's 1872 Erlangen Program characterized geometries by their invariance groups [established]. Projective geometry is characterized by the projective group $\text{PGL}(n, \mathbb{R})$. The cross-ratio is the fundamental invariant of $\text{PGL}(2, \mathbb{R})$ acting on $\mathcal{P}^1$.

The present framework places $\alpha$ within the Erlangen Program: $\alpha$ is the invariant that characterizes the electromagnetic interaction under the projective group. This is a geometric classification of a fundamental physical constant — a realization of Klein's vision that geometry underlies all of mathematical physics.

## 7.2 Conformal Field Theory

In two-dimensional conformal field theory (CFT), the cross-ratio plays a central role: four-point correlation functions are determined up to a function of the cross-ratio of the insertion points [established, Belavin–Polyakov–Zamolodchikov 1984].

The appearance of the cross-ratio in both CFT and the fine-structure constant suggests a deeper connection: $\alpha$ may be the value of a four-point function in a CFT describing the electron's electromagnetic structure at a conformal fixed point. This connection is [speculative] but merits investigation.

## 7.3 Twistor Theory

Penrose's twistor theory reformulates space-time geometry in terms of projective twistors [established]. In twistor space, the cross-ratio of four twistors corresponds to physical invariants of scattering processes.

The cross-ratio formulation of $\alpha$ may find a natural home in twistor theory, where the electron's length scales correspond to specific twistor configurations. This would embed $\alpha$ in a fully geometric formulation of quantum field theory [speculative].

## 7.4 Projective Unification of Forces

If each fundamental force corresponds to a projective invariant of its characteristic length scales, then the unification of forces at high energies would correspond to the identification of these projective structures as different projections of a single higher-dimensional projective geometry.

$$\text{SU}(3) \times \text{SU}(2) \times \text{U}(1) \subset \text{PGL}(n, \mathbb{F})$$

for some field $\mathbb{F}$ and dimension $n$ [speculative]. This is a geometric alternative to conventional grand unified theories, with projective geometry replacing Lie group structure as the organizing principle.

## 7.5 Topological Interpretation

The cross-ratio has a topological interpretation as the modulus of a configuration space. Four points on $\mathcal{P}^1$ have a moduli space $\mathcal{M}_{0,4} \cong \mathcal{P}^1 \setminus \\{0, 1, \infty\\}$, and the cross-ratio parameterizes this space.

In this interpretation, $\alpha$ is a point in the moduli space of four-point configurations on a projective line. The value $\alpha \approx 1/137$ is then a specific location in this moduli space — determined, perhaps, by deeper topological or arithmetic constraints [speculative].

## 7.6 Syntactic Interpretation

The QNFO syntactic physics program proposes that physical laws emerge from the syntax of measurement operations [speculative, QNFO working paper]. In this framework, the cross-ratio formulation reframes $\alpha$ as the syntactic invariant of the measurement operations that compare $r_e$ and $\lambda_C$.

Concretely: to measure $r_e$, one must scatter particles from an electron at high momentum transfer. To measure $\lambda_C$, one must probe the electron's quantum coherence length. The ratio of these two measurement outcomes is invariant under changes in the measurement apparatus — this is the projective invariance of the cross-ratio, reinterpreted syntactically.

## 7.7 Adelic Extension: The Cross-Ratio on Bruhat–Tits Buildings [v1.0 — NEW]

The real projective line $\mathcal{P}^1(\mathbb{R})$ is only one completion of the rational numbers $\mathbb{Q}$. By Ostrowski's theorem [established], the only non-trivial absolute values on $\mathbb{Q}$ (up to equivalence) are the real absolute value $|\cdot|_\infty$ and the p-adic absolute values $|\cdot|_p$ for each prime $p$.

The adele ring $\mathbb{A}_\mathbb{Q}$ is the restricted product of all completions:

$$\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_{p}' \mathbb{Q}_p$$

where the restricted product means that for all but finitely many $p$, the component lies in the p-adic integers $\mathbb{Z}_p$.

### 7.7.1 The Adelic Cross-Ratio

For each place $v$ of $\mathbb{Q}$ (including the infinite place $\infty$ and all finite primes $p$), we can define the cross-ratio of four points on $\mathcal{P}^1(\mathbb{Q}_v)$:

$$\text{CR}_v(A, B; C, D) = \frac{(A-C)_v(B-D)_v}{(A-D)_v(B-C)_v}$$

The adelic cross-ratio is then the product over all places:

$$\text{CR}_\mathbb{A}(A, B; C, D) = \prod_{v} \text{CR}_v(A, B; C, D)$$

### 7.7.2 The Bruhat–Tits Tree at Each Prime

For each prime $p$, the projective line $\mathcal{P}^1(\mathbb{Q}_p)$ has the structure of a Bruhat–Tits tree — an infinite $(p+1)$-regular tree whose vertices correspond to homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$ [established, Serre 1980].

Points on $\mathcal{P}^1(\mathbb{Q}_p)$ can be identified with ends of this tree. The p-adic cross-ratio measures the relative position of four ends on the Bruhat–Tits tree.

### 7.7.3 The Electron's p-Adic Structure

The electron's length scales $r_e$ and $\lambda_C$ have p-adic counterparts at each prime $p$. The p-adic classical electron radius and p-adic Compton wavelength are defined through the p-adic valuation of the corresponding real quantities:

$$|r_e|_p = p^{-v_p(r_e)}, \quad |\lambda_C|_p = p^{-v_p(\lambda_C)}$$

The adelically extended cross-ratio is:

$$\alpha_\mathbb{A} = \prod_v \frac{|r_e|_v}{|\lambda_C|_v} = \prod_v \alpha_v$$

By the product formula for $\mathbb{Q}$ (the adelic identity):

$$\prod_v |x|_v = 1 \quad \text{for all } x \in \mathbb{Q}^\times$$

the adelic cross-ratio satisfies:

$$\alpha_\mathbb{A} = \alpha_\infty \cdot \prod_p \alpha_p = 1$$

This is a remarkable constraint: while $\alpha_\infty \approx 1/137$ at the real place, the product over all p-adic places exactly compensates to yield unity. The real $\alpha$ is "balanced" by its p-adic completions.

### 7.7.4 Physical Interpretation

This adelic structure suggests a profound reinterpretation of $\alpha$:

1. **$\alpha$ is NOT a fundamental constant but a local manifestation** — the value $\alpha \approx 1/137$ is the real component of an adelic object whose global product is 1.

2. **The p-adic contributions encode "hidden" electromagnetic structure** — processes at the p-adic places may influence real observables through global adelic constraints.

3. **The Bruhat–Tits building geometry provides a discrete underpinning** — the electron's length scales correspond to specific vertices on the $p+1$-regular trees for each prime, and their cross-ratio is determined by the combinatorial distance between these vertices.

### 7.7.5 Connection to the QNFO Adelic Physics Program

This adelic extension directly connects to the QNFO research program on adelic quantum error correction (Adelic QEC, QNFO-2025) and the Ultrametric Engine (QNFO-2026). Specifically:

- The p-adic cross-ratio on Bruhat–Tits buildings provides the geometric foundation for the ultrametric distance used in the Ultrametric Engine's paper ranking (§2.5 of the adelic QEC paper).

- The adelic product formula $\prod_v \alpha_v = 1$ is the arithmetic analogue of the error-correction condition in Adelic QEC — both encode the principle that local defects are compensated by global constraints.

- The combinatorial structure of Bruhat–Tits trees corresponds to the hierarchical taxonomy used in the Ultrametric Engine's knowledge ranking, providing a mathematical justification for why ultrametric (tree-based) organization is natural for physical knowledge.

---

# 8. Discussion

## 8.1 What Has Been Shown

This paper has demonstrated that $\alpha$ can be expressed as the cross-ratio of two measurable electron length scales ($r_e$ and $\lambda_C$), revealing a projective invariance that the standard formulation obscures. This is not merely a mathematical reformulation — it reframes $\alpha$ as a geometric invariant rather than an arbitrary coupling, and opens connections to projective geometry, conformal field theory, twistor theory, and adelic mathematics.

## 8.2 What Has NOT Been Shown

It is important to state what this framework does NOT accomplish:

- **It does not predict the numerical value of $\alpha$.** The cross-ratio formulation explains the structure of $\alpha$ (it is a projective invariant of electron length scales) but does not derive its specific value $\approx 1/137$.

- **It does not replace quantum electrodynamics.** The cross-ratio is a reinterpretation of the zero-energy value of $\alpha$, not a replacement for the full theory of electromagnetic interactions.

- **It does not uniquely select the electron's length scales.** While $r_e$ and $\lambda_C$ are natural choices, other pairs of length scales could yield the same cross-ratio. The claim is that $\alpha$ IS a specific cross-ratio, not that it uniquely determines which points are being crossed.

## 8.3 Open Questions

1. **Why $1/137$?** What combinatorial, arithmetic, or topological principle determines the specific value?

2. **Is the adelic product formula physically significant**, or is it a mathematical artifact? Can the p-adic contributions to $\alpha$ be experimentally probed?

3. **Does the projective invariance generalize to all gauge couplings**, and if so, what is the underlying projective geometry that unifies them?

4. **Can the running of $\alpha$ with energy be derived from projective curvature**, rather than from conventional renormalization group methods?

## 8.4 Falsifiability Conditions [v1.0 — NEW]

Per the QNFO Research Integrity Mandate (QNFO-POL-COM-001, §0.0), speculative claims must carry explicit falsifiability conditions. The following would disconfirm or constrain the framework:

### 8.4.1 Direct Falsification

1. **This framework would be DISCONFIRMED if** the relation $\alpha = r_e/\lambda_C$ were shown to be coincidental rather than structural. Specifically, if a fundamental theory predicted $\alpha$ from completely different principles (e.g., a unique GUT prediction) with no reference to electron length scales, the projective interpretation would be superseded.

2. **This framework would be DISCONFIRMED if** the projective curvature of the running coupling $\alpha(Q^2)$ were measured to deviate from the functional form predicted by the projective connection, at a level exceeding experimental uncertainty.

3. **This framework would be DISCONFIRMED if** the adelic product formula $\prod_v \alpha_v = 1$ were shown to be violated — i.e., if a consistent definition of p-adic cross-ratios yielded a non-unit product. This would indicate that the adelic structure is not physically realized.

### 8.4.2 Constraint

1. **This framework would be CONSTRAINED if** a fifth force or modified electromagnetic interaction were discovered — new couplings would introduce additional length scales, complicating the simple two-scale cross-ratio.

2. **This framework would be CONSTRAINED if** $\alpha$ were found to vary in time or space beyond current limits — this would require the projective geometry to be dynamic rather than static.

### 8.4.3 Current Status

As of July 2026, none of these falsification conditions have been observed [established]. The framework is consistent with all current experimental data. It is `[not yet falsifiable]` in the strict Popperian sense because the projective curvature prediction for the running of $\alpha$ has not been tested at the required precision. This would be testable with a future $e^+e^-$ collider (FCC-ee or CEPC) achieving factor-10 improvement in $\alpha(M_Z)$ measurement.

---

# 9. Cross-References to QNFO Research Program

This paper synthesizes findings from and contributes to the following QNFO research publications:

1. **Adelic Quantum Error Correction: Intrinsic Qubit Protection from Ostrowski's Theorem** (QNFO, 2025) — The adelic product formula and Bruhat–Tits building geometry provide the mathematical foundation for the adelic extension in §7.7.

2. **Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker** (QNFO, 2026) — The ultrametric (tree-based) knowledge organization mirrors the hierarchical structure of Bruhat–Tits trees, providing a concrete implementation of the p-adic formalism.

3. **Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Hierarchy** (QNFO, 2026) — The global adelic constraints on cross-ratios are a special case of the pattern-particle correspondence, where projective invariants at all places are reconciled through the adele ring.

4. **The Arithmetic Gauge: Cross-Ratios and Projective Invariants Across Fields** (QNFO, 2025) — The projective-geometric foundation of cross-ratios as physical invariants was developed in this precursor work.

5. **QNFO Publication Architecture v3.0** (QNFO Technical Report, 2026) — The publication infrastructure (D1 living-paper, R2 storage, Cloudflare Pages, DOI) that hosts this paper.

---

# Appendix A: Mathematical Conventions

The real projective line $\mathcal{P}^1(\mathbb{R})$ is the set of lines through the origin in $\mathbb{R}^2$. Points are represented by homogeneous coordinates $[x:y]$ with the identification $[x:y] \sim [\lambda x:\lambda y]$ for $\lambda \neq 0$.

For a finite point with coordinate $z$, the homogeneous representation is $[z:1]$. The point at infinity is $[1:0]$.

The cross-ratio in homogeneous coordinates is:

$$\text{CR}([a_1:a_2], [b_1:b_2]; [c_1:c_2], [d_1:d_2]) = \frac{\det(a,c)\det(b,d)}{\det(a,d)\det(b,c)}$$

where $\det(x,y) = x_1y_2 - x_2y_1$.

---

# References

1. Sommerfeld, A. (1916). *Annalen der Physik*, 51, 1–94.

2. Gabrielse, G. et al. (2023). *Physical Review Letters*, 130, 071801. [Measurement of electron $g-2$, $\alpha^{-1} = 137.035999084(21)$]

3. Morel, L. et al. (2020). *Nature*, 588, 61–65. [Rubidium atom recoil measurement]

4. Parker, R.H. et al. (2018). *Science*, 360, 191–195. [Cesium atom recoil measurement]

5. CODATA (2019). *Reviews of Modern Physics*, 93, 025010.

6. Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen*. [Erlangen Program]

7. Serre, J.-P. (1980). *Trees*. Springer-Verlag. [Bruhat–Tits theory]

8. Belavin, A.A., Polyakov, A.M., Zamolodchikov, A.B. (1984). *Nuclear Physics B*, 241, 333–380. [Conformal field theory]

9. Penrose, R. (1967). *Journal of Mathematical Physics*, 8, 345–366. [Twistor theory]

10. Quni-Gudzinas, R.B. (2025). *Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Hierarchy*. QNFO. https://papers.qnfo.org/papers

11. Quni-Gudzinas, R.B. (2025). *Adelic Quantum Error Correction: Intrinsic Qubit Protection from Ostrowski's Theorem*. QNFO.

12. Quni-Gudzinas, R.B. (2026). *Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker*. QNFO.

13. Ostrowski, A. (1916). *Acta Mathematica*, 41, 271–284.

---

*This paper was prepared under the QNFO Research Integrity Mandate (QNFO-POL-COM-001). All claims beyond textbook consensus carry explicit certainty labels. The adelic extension (§7.7) is [speculative]; the projective formulation of $\alpha$ is a geometric reframing of an established experimental fact, not a new physical theory.*
