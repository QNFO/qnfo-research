# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds

## Abstract

The holographic entropy bound is conventionally stated in bits, a unit that embeds two human conventions: integer counting of states and the choice of logarithm base 2. This paper asks whether the bound can be restated entirely in observer-independent quantities, and it situates the question in the current holographic literature. Working in Planck natural units ($c=\hbar=G=k_{B}=1$), area is a dimensionless number $A$ in Planck areas and physical entropy is the natural-logarithm entropy $S=A/4$ (nats). We derive the base-free bound $D\le e^{A/4}$ on the Hilbert-space dimension $D$, show that the bit appears only as the derived quantity $b=S/\ln 2$, and prove that all base-$b$ representations differ by fixed multiplicative constants, so they are empirically equivalent. A worked example with $A=10^{68}$ gives $S=2.5\times10^{67}$ nats, $b=3.6067376\times10^{67}$ bits, and $D\le 10^{1.0857362\times10^{67}}$. The only residual conventional element is the integer rounding of $D$: at $A=4$ (four Planck areas, $S=1$ nat) the relative deficit is $26.4\%$, while at $A=10^{68}$ it falls below $10^{-10^{67}}$. The result is foundational: it separates the invariant content of holographic bounds ($A$, $S$, $D$) from methodological conventions, and it changes how capacity specifications for quantum-gravity experiments can be written.

## 1. Introduction

Anyone who specifies information-capacity limits for quantum-gravity experiments — for example, tabletop analog black-hole simulators or quantum memories used as entropy reservoirs in analog-gravitation platforms — must translate the holographic entropy bound into an operational unit. The standard translation target is the bit, and the bit presupposes two choices made by human information technology: that states are counted as integers, and that the logarithm is taken to base 2. Neither choice is dictated by the bound itself, and their presence obscures whether the bound contains any further hidden anthropocentric choices that could affect the interpretation of data. If the bound can be written solely in observer-independent quantities, a designer can assess capacity limits directly from geometric data, and a theorist can see exactly which parts of the holographic framework are conventions and which are invariants. That separation changes a concrete decision: how capacity specifications for analog-gravitation platforms are written, and which quantities a quantum-gravity theory must fix to make the bound predictive.

In reconciling the present treatment we adopt two conventions where alternative readings exist. First, we take the minimal non-trivial example to be $A=4$, i.e. four Planck areas, chosen because it gives $S=1$ nat; under the alternative normalization $A=1$ (one Planck area) the rounding analysis is also carried out below, so both conventions are covered. Second, we attribute the Ostrowski-theoretic perspective — the treatment of all completions of $\mathbb{Q}$ on an equal footing — to the invariant-patterns program of [14], which states Ostrowski's theorem as a physical principle, rather than to any work that does not develop that perspective.

**Contributions.**
(i) A natural-unit formulation of the holographic entropy bound, $D\le e^{A/4}$ with $S=A/4$, in which no logarithm-base constant appears in the core relation — derived in Section 3.
(ii) Explicit arithmetic derivations of the conversion constants between nats, bits, and decimal digits, of a macroscopic worked example at $A=10^{68}$, and of the integer-rounding deficit at $A=4$, at $A=1$, and at $A=10^{68}$ — Section 4.
(iii) A proof that all base-$b$ entropy representations are related by fixed multiplicative constants, establishing the empirical equivalence of the invariant and conventional formulations — Section 4.
(iv) A classification table separating base-free, derived, and conventional ingredients of the bound, and a corrected attribution of the Ostrowski-theoretic framing to [14] — Sections 4 and 6.

The paper proceeds as follows. Section 2 discusses the related work. Section 3 sets out the natural-unit framework and the analytical method. Section 4 presents the derivations with step-by-step arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 gives practical implications, readiness, and the smallest next test. Section 8 concludes.

## 2. Background and Related Work

This section discusses the works that bear on the two halves of the argument: the physical content of holographic entropy bounds, and the status of units and counting conventions in physics.

**Holographic bounds in cosmology.** [1] compares two holographic arguments that limit inflation — the de Sitter Equilibrium (dSE) cosmology and the approach of Banks and Fischler (BF) — and finds that simple versions yield the same bound on the number of e-foldings. In both pictures the entropy $3\pi/\Lambda$ of the de Sitter horizon represents the finite information of the universe; the BF approach bounds the entropy in a cavity the size of the apparent horizon rather than using the horizon entropy, and concludes that "while the phrasing of the BF bound in terms of entropy sounds pleasingly universal, the details of its implementation rely heavily on the cosmological history of the universe to which it applies." That conclusion is direct support for the thesis of this paper: the universal-sounding entropy phrasing of a holographic bound can conceal implementation-dependent choices, and isolating what is implementation-independent is a real analytical task. [11] develops holographic entropy bounds for radiation-dominated and quasi-de Sitter universes, introducing three entropies and showing in its Discussion that the Hubble bound $S\le S_{\rm H}$ is valid for $R\ge H^{-1}$ while the Bekenstein-Verlinde bound $S\le S_{\rm BV}$ is valid for $R\le H^{-1}$. The regime-dependence of which entropy bound applies reinforces the need to state bounds in quantities whose meaning does not shift between regimes. [2] introduces cosmic holographic bounds with UV and IR cutoffs and concludes that the D-bound derived by analogy with de Sitter spacetime is not appropriate for quantum fluctuations of inflation because the system is weakly gravitating, that the energy bound then plays the central role, and that the indirect entropy bound constrains the UV cutoff to $\Lambda\sim M_{p}$. [5] reaches a compatible conclusion from the perturbation side: holographic bounds on the UV cutoff of inflation depend on the coarse-graining prescription used to compute the entropy, and the paper proposes entanglement entropy as the natural measure of the perturbation entropy. The coarse-graining prescription is exactly the kind of choice this paper's classification scheme is designed to expose: it is a convention-level input that sits upstream of any statement in bits or nats.

**Holographic bounds in AdS and the status of defined quantities.** [8] derives a holographic bound from field-theoretic considerations in the gauge/gravity correspondence, using boundary-compact wavepacket sources, and reports two limitations its own Conclusion states: the particle-number restriction does not apply to pure gravity, where overlapping boundary sources are allowed, and in certain scaling regimes it seems possible to localize arbitrarily many high-energy states in one AdS region, which the authors describe as a severe overcounting of bulk states. This matters here because it shows that even the derivation of a holographic bound carries structural assumptions — about sources, overlaps, and particle number — that are logically prior to any unit convention. [3] examines a different convention-dependence: in holographic duality the total energy obtained from holographic renormalization depends on the choice of quantization scheme, and the paper introduces a modified energy $\mathcal{H}$ that is independent of that choice, applying it to four-dimensional AdS with a massive scalar. The parallel is exact in structure: where [3] removes a scheme choice from the definition of energy, this paper removes a base choice from the definition of entropy. [4] studies the action growth rate $\dot{I}_{\rm WDW}$ of the Wheeler-DeWitt patch for $D\ge4$ AdS black holes with spherical, toric, and hyperbolic horizons ($k=1,0,-1$), proposes bounds on holographic complexity under the complexity=action conjecture, and introduces a modified complexity=volume conjecture with growth rate $\dot{\cal C}_{V}=2P_{\rm th}\,\Delta V_{\rm th}$. Complexity is a holographic quantity that, like entropy, is a count-like number; the existence of sharp bounds on it in geometric form is a further instance of the pattern this paper formalizes, in which the bound's content is geometric and its unit expression is derivative.

**Natural units and conventions.** [6] presents the system of natural units of high-energy physics, defined by setting $c$, $\hbar$, and $k_{B}$ to unity, lists the exact numerical values of those constants in SI units ($c=299\,792\,458\ {\rm m\,s^{-1}}$, $\hbar=1.054\,571\,596\times10^{-34}\ {\rm J\,s}$, $k_{B}=1.380\,650\,3\times10^{-23}\ {\rm J\,K^{-1}}$), and concludes that with $[c]=[\hbar]=[k_{B}]=1$ high-energy physics admits a one-dimensional system of units organized in numerical clusters spanning $10^{\pm80}$. This is the established practice, within a subfield, of expressing physical law in dimensionless constant form — the practice this paper extends to information measures. [7] supplies the historical and conceptual anchor: it recounts that Planck introduced the natural units $h$, $c$, $G$, $k$ in 1897–1899, that only $c$, $\hbar$, $G$ retained status in the "cube of theories," and it argues from the definition $T=dU/dS$ that $k$ is not a natural unit at all but "a ratio of 'hand-crafted' units of temperature and energy," i.e. a conversion factor from degrees to joules. The same argument applies verbatim to the bit: $\ln 2$ is a conversion factor between the natural-log entropy and a unit chosen for engineering convenience. [9] gives the mathematical formalism behind such conversions: it constructs the vector space of physical values, in which different unit systems correspond to different bases and a transformation between unit systems is a matrix-vector multiplication, and it demonstrates the formalism on the subspace spanned by $\{10,\mathrm{m},\mathrm{s},\mathrm{kg}\}$. Under this formalism, the constants $1/\ln 2$ and $1/\ln 10$ derived in Section 4 are change-of-basis coefficients, which is the precise sense in which bits and decimal digits are "derived" units. [10] establishes asymptotics for sums counting integer tuples under coprimality conditions using elementary methods only; it is cited in Section 4.5 as an illustration that counting questions of the kind raised by the integer-rounding step admit elementary asymptotic treatment. [13] contributes the methodological caution from a neighboring program: it documents that an earlier analysis "blindly fit decimal PDG masses — numbers derived from an SI unit system calibrated to human-chosen standards," that these are "decimal floating-point artifacts, not physical invariants," and that an unconstrained search produced a retracted "4.8× improvement over random" claim. That case study is the empirical motivation for insisting, as this paper does, that the quantities in a fundamental bound be invariants rather than artifacts of a unit system. Finally, [14] states the organizing principle this paper adopts: physics is the study of invariant patterns under specified transformations, measurement units are scaling conventions pegged to arbitrary reference objects, the true invariants are dimensionless ratios, and in Planck units ($\hbar=c=G=k_{B}=1$) every physical quantity becomes a dimensionless number. Its §3.1 states Ostrowski's theorem — every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value or to a $p$-adic one — and draws the conclusion that a non-anthropocentric physics would treat all completions of $\mathbb{Q}$ equally. This is the correct home for the Ostrowski-theoretic perspective; Section 6 uses it where it belongs.



## 3. Methods

### 3.1 Natural-unit setting

We adopt Planck natural units throughout:

$$
c=\hbar=G=k_{B}=1.
$$

In these units the Planck length $\ell_{P}$ is the unit of length, the Planck area $\ell_{P}^{2}$ is the unit of area, and any physical area $A_{\text{phys}}$ is represented by the dimensionless number

$$
A=\frac{A_{\text{phys}}}{\ell_{P}^{2}}.
$$

This is the move that [14] describes generally — in Planck units every physical quantity becomes a dimensionless number — applied to the one geometric quantity that enters the holographic bound. Entropy is measured in nats, the natural-logarithm entropy $S=\ln D$ for a maximally mixed state on a $D$-dimensional Hilbert space. Following the argument of [7] about $k_{B}$, we treat any logarithm base other than $e$ as a conversion factor, not a unit.

### 3.2 Base-free entropy bound

The Bekenstein–Hawking relation in natural units reads

$$
S_{\text{BH}}=\frac{A}{4}.
$$

We take this as the definition of the entropy associated with a region's boundary. Inverting $S=\ln D$ gives the bound on the Hilbert-space dimension:

$$
D\le e^{S}=e^{A/4}.
$$

The bound involves only the dimensionless area $A$, the geometric factor $4$, and the exponential function of base $e$. No logarithm-base constant appears.

### 3.3 Recovery of derived units

The bit is defined as the entropy of a two-outcome event:

$$
b=\frac{S}{\ln 2}=\frac{A}{4\ln 2}.
$$

Decimal digits are $d=S/\ln 10$. These are derived quantities in the sense of [9]: each requires inserting one change-of-basis constant, exactly as converting a physical value between unit systems in the vector-space formalism requires one matrix-vector multiplication.

### 3.4 Analytical procedure

The analysis proceeds in four steps:

1. List all quantities appearing in the conventional formulation of the bound.
2. Re-express each in the natural-unit framework of Section 3.1.
3. Classify each as base-free (geometric or logarithmic in base $e$ only), derived (requiring insertion of a base constant), or conventional (requiring a human choice such as integer counting).
4. Perform explicit arithmetic for a representative macroscopic area ($A=10^{68}$), the minimal non-trivial case ($A=4$, i.e. four Planck areas, giving $S=1$ nat), and the unit case ($A=1$).

No simulations or empirical measurements are used; every step is analytic. Where a numerical input is a mathematical constant, its value is stated to the precision used. Where a value stands in for data no source gives — the choice of the example area $A=10^{68}$ — it is labeled an assumption.

## 4. Analysis

### 4.1 Classification of quantities

| Quantity | Conventional expression | Natural-unit expression | Status |
|---|---|---|---|
| Area | $A_{\text{phys}}$ (m$^{2}$) | $A=A_{\text{phys}}/\ell_{P}^{2}$ | base-free (geometric) |
| Entropy (nats) | $S_{\text{bits}}$ (bits) | $S=A/4$ | base-free |
| Hilbert-space dimension bound | $D\le 2^{A/(4\ln 2)}$ | $D\le e^{A/4}$ | base-free |
| Bits | $b=S/\ln 2$ | $b=A/(4\ln 2)$ | derived |
| Decimal digits | $d=S/\ln 10$ | $d=A/(4\ln 10)$ | derived |
| Integer rounding | $D\in\mathbb{Z}$ | $D\in\mathbb{Z}$ via $\lfloor e^{A/4}\rfloor$ | conventional |

Only the integer-rounding step introduces a human counting convention. This classification is the paper's central analytical device, and it is the same move in kind as the scheme-independent energy of [3]: identify a convention-dependent ingredient of a standard definition and exhibit the definition that does not need it.

### 4.2 Input constants

All numerical inputs are mathematical constants:

* $\ln 2 = 0.6931471805599453\ldots$
* $\ln 10 = 2.302585092994046\ldots$
* $e = 2.718281828459045\ldots$
* The factor $4$ from the Bekenstein–Hawking relation.

The example area $A=10^{68}$ is an assumption, chosen to represent a macroscopic horizon; no specific physical system is asserted. No empirical measurements are required anywhere in the derivation.

### 4.3 Derivation 1: Conversion constants

The bit-to-nat conversion factor is the reciprocal of $\ln 2$:

$$
\frac{1}{\ln 2}=\frac{1}{0.6931471805599453}=1.4426950408889634\ldots
$$

Check by multiplication:

$$
1.4426950408889634\times 0.6931471805599453 = 1.0000000000000000
$$

to the displayed precision, confirming the reciprocal. Therefore the bit content of a horizon of dimensionless area $A$ is

$$
b=\frac{A}{4}\times\frac{1}{\ln 2}=\frac{A}{4}\times 1.4426950408889634 = 0.36067376022224085\,A,
$$

where the last step is $1.4426950408889634/4 = 0.36067376022224085$.

Similarly,

$$
\frac{1}{\ln 10}=\frac{1}{2.302585092994046}=0.4342944819032518\ldots,
$$

so $d = 0.4342944819032518\,A/4 = 0.10857362047581295\,A$, and

$$
\frac{\ln 10}{\ln 2}=\frac{2.302585092994046}{0.6931471805599453}=3.3219280948873626\ldots
$$

These constants are exact to the displayed precision. In the formalism of [9] they are the entries of the change-of-basis matrix between the nat, bit, and digit representations of the same physical value $S$.

### 4.4 Derivation 2: Worked macroscopic example

**Assumption.** Take a horizon patch with dimensionless area $A=10^{68}$ (a stand-in for a macroscopic horizon; no physical system is asserted).

**Step 1: Entropy in nats.**

$$
S=\frac{A}{4}=\frac{10^{68}}{4}=2.5\times10^{67}\ \text{nats}.
$$

**Step 2: Bits.** Multiply by $1/\ln 2$:

$$
b = S\times 1.4426950408889634 = 2.5\times10^{67}\times 1.4426950408889634.
$$

The mantissa product is $2.5\times 1.4426950408889634 = 3.6067376022224085$, so

$$
b = 3.6067376022224085\times10^{67}\ \text{bits}.
$$

**Step 3: Hilbert-space dimension bound.** Compute $\log_{10}D$:

$$
\log_{10}D=\frac{S}{\ln 10}=\frac{2.5\times10^{67}}{2.302585092994046}.
$$

The mantissa quotient is $2.5/2.302585092994046 = 1.0857362048\ldots$, so

$$
\log_{10}D = 1.0857362048\ldots\times10^{67},\qquad D\le 10^{1.0857362048\times10^{67}}.
$$

**Step 4: Consistency check.** Convert $\log_{10}D$ back to bits using $\log_{2}10=\ln 10/\ln 2 = 3.3219280948873626$:

$$
b_{\text{from }D}=\log_{2}D = 3.3219280948873626\times 1.085736203\times10^{67}.
$$

The mantissa product is $3.3219280948873626\times 1.0857362048 = 3.6067376\ldots$, so

$$
b_{\text{from }D}=3.6067376\times10^{67}\ \text{bits},
$$

matching the direct bit calculation of Step 2 to the displayed precision. The round trip nat $\to$ digits $\to$ bits reproduces the direct nat $\to$ bits conversion, as it must if the conversion constants of Section 4.3 are consistent.

### 4.5 Derivation 3: Integer-rounding deficit

The bound $D\le e^{A/4}$ yields a real number; a physical Hilbert space has an integer dimension, so the operative bound is

$$
D_{\text{int}}=\left\lfloor e^{A/4}\right\rfloor .
$$

Define the deficit

$$
\Delta = e^{A/4}-\left\lfloor e^{A/4}\right\rfloor,\qquad 0\le\Delta<1.
$$

**Minimal non-trivial case.** Take $A=4$, i.e. four Planck areas, the smallest area for which $S=A/4=1$ nat:

$$
e^{A/4}=e^{1}=2.718281828459045\ldots
$$

Hence

$$
D_{\text{int}}=\lfloor 2.718281828\ldots\rfloor = 2,
$$
$$
\Delta = 2.718281828\ldots - 2 = 0.718281828\ldots
$$

Relative deficit:

$$
\frac{\Delta}{e}=\frac{0.718281828\ldots}{2.718281828\ldots}=0.2642411177\ldots\approx 26.4\%.
$$

**Unit case.** At $A=1$ (one Planck area), $S=0.25$ nats and $e^{A/4}=e^{0.25}=1.284025\ldots$, so $D_{\text{int}}=1$ and the relative deficit is $0.284025\ldots/1.284025\ldots = 0.2212\ldots\approx 22.1\%$. The rounding convention is already active at one Planck area.

**Macroscopic case.** For $A=10^{68}$ the absolute deficit satisfies $\Delta<1$ while $D\sim 10^{1.085736\times10^{67}}$, so the relative deficit is bounded above by

$$
\frac{\Delta}{D}\le\frac{1}{10^{1.085736\times10^{67}}}=10^{-1.085736\times10^{67}},
$$

which is smaller than $10^{-10^{67}}$ and therefore astronomically negligible. The integer-counting questions that arise here — counting states and estimating how counting functions behave at large arguments — are the kind of question that admits elementary asymptotic treatment, as illustrated in the number-theoretic literature by [10], which establishes asymptotics for sums counting integer tuples under coprimality conditions using elementary methods only; the present rounding analysis needs far less, only the floor function and the bound $\Delta<1$.

Thus the rounding convention is consequential only at Planck-scale areas.

### 4.6 Derivation 4: Empirical equivalence of base representations

Consider any base $b>1$. The entropy expressed in that base is $S_{b}=S/\ln b$. For two bases $b_{1},b_{2}$,

$$
S_{b_{2}}=\frac{S}{\ln b_{2}}=\frac{\ln b_{1}}{\ln b_{2}}\cdot\frac{S}{\ln b_{1}}=\frac{\ln b_{1}}{\ln b_{2}}\,S_{b_{1}}.
$$

Since the factor $\ln b_{1}/\ln b_{2}$ is a fixed positive number independent of the state, any physical prediction that depends only on the relative values of entropies — in particular any homogeneous entropy inequality, the class that includes the holographic bounds — is unchanged under base change. Consequently, the invariant formulation ($S=A/4$ nats) and the conventional bit formulation ($b=S/\ln 2$) make identical predictions for all observables that are functions of entropy alone. No experiment can distinguish the two representations as long as the underlying theory content is fixed. This is the representational content of the change-of-basis view of units in [9], specialized to the entropy scale.

## 5. Results

All numerical statements below follow directly from the derivations in Section 4.

* **R1 (Base-free core).** The holographic bound can be written as
  $$
  D\le e^{A/4},\qquad S=\frac{A}{4},
  $$
  containing no logarithm-base constant. Bits appear only in the derived expression $b=S/\ln 2$.

* **R2 (Conversion constants).**
  $$
  \frac{1}{\ln 2}=1.4426950409,\qquad \frac{1}{\ln 10}=0.4342944819,\qquad \frac{\ln 10}{\ln 2}=3.3219280949.
  $$
  One Planck area ($A=1$) carries $S=0.25$ nats $=0.3606737602$ bits $=0.1085736205$ decimal digits.

* **R3 (Macroscopic example).** For $A=10^{68}$ (assumed example area):
  $S=2.5\times10^{67}$ nats,
  $b=3.6067376022\times10^{67}$ bits,
  $D\le 10^{1.0857362048\times10^{67}}$.

* **R4 (Rounding deficit).** At $A=4$ (four Planck areas, $S=1$ nat): $D_{\text{int}}=2$, relative deficit $26.4\%$. At $A=1$: $D_{\text{int}}=1$, relative deficit $22.1\%$. At $A=10^{68}$ the relative deficit is $<10^{-10^{67}}$.

* **R5 (Empirical equivalence).** Any homogeneous entropy inequality is invariant under base change; therefore the invariant and conventional formulations are empirically indistinguishable.

* **R6 (Projection).** For a generic physical region with area $A_{\text{phys}}$, the bit capacity is projected as
  $$
  b = 0.3606737602\,\frac{A_{\text{phys}}}{\ell_{P}^{2}},
  $$
  with the arithmetic given by the constants of Section 4.3. This is a projection under the stated assumptions (Planck natural units, $S=A/4$, maximally mixed states); no specific $A_{\text{phys}}$ is asserted.

## 6. Discussion

### Limitations

1. **Representational scope.** The reformulation is purely representational; by R5 it generates no new testable predictions relative to the bit formulation.
2. **Assumed Bekenstein–Hawking relation.** The derivation treats $S=A/4$ as a definition. If future quantum-gravity work shows that the coefficient $1/4$ is itself conventional or receives logarithmic corrections, the base-free claim would need revision.
3. **Hilbert-space factorization.** The bound assumes a well-defined Hilbert-space dimension for a sub-region. If factorization is observer-dependent, the integer-rounding analysis (R4) may not apply; the overcounting problem reported in [8] for AdS bounds is a concrete warning that the state count a bound applies to can be ill-defined.
4. **Nat as distinguished base.** The argument that the natural logarithm is singled out does not prove that entropy must be logarithmic; it inherits that assumption from the Bekenstein–Hawking framework.
5. **Regime-dependence of the bound itself.** As [11] shows, which entropy bound applies depends on the regime ($R\ge H^{-1}$ versus $R\le H^{-1}$), and [2] shows that the D-bound fails for weakly gravitating fluctuations. The base-free reformulation inherits these regime restrictions unchanged.
6. **Bibliographic coverage.** The primary sources for the original Bekenstein bound are not among the works discussed here; the present treatment relies on the cosmological and AdS holographic-bound literature cited in Section 2.

### Failure modes

The program fails if any of the following occurs:

* (i) The factor $4$ in $S=A/4$ is shown to encode a slicing or coordinate convention rather than geometry.
* (ii) Hilbert-space dimensions for sub-regions are demonstrated to be ill-defined or non-integer, invalidating the integer-rounding analysis.
* (iii) Entropy is found to be non-additive at the Planck scale, breaking the uniqueness of the natural logarithm as the base that respects composition.
* (iv) Logarithmic corrections to the Bekenstein–Hawking entropy introduce explicit $\ln 2$ or other base-dependent terms into the core formula.

### Falsification condition

The empirical-equivalence result (R5) would be falsified by exhibiting a well-defined observable $O$ that depends on the logarithm base while all invariant quantities ($A$, $S$, $D$) are held fixed. Concretely, if a quantum-gravity calculation produced a correction term proportional to $\ln 2$ that altered the bound's leading order, the base-free formulation would be invalidated. The rounding analysis (R4) would be falsified if a quantum-gravity framework predicted a different integer rounding rule for $D$ at small areas, for example a rule giving $D_{\text{int}}\neq\lfloor e^{A/4}\rfloor$ at $A=4$.

### Self-critique

The strongest objection is that "bits" may be viewed as merely a convenient human unit, and removing them does not affect physical content. The reply is that the removal clarifies which aspects of the bound are methodological conventions (the choice of base and integer rounding) and which are genuine geometric invariants. By isolating the latter, the analysis provides a cleaner foundation for future theoretical work that may seek to eliminate all anthropocentric artifacts. A second objection is that the classification of "integer counting" as conventional is itself a choice; the defense is that R4 quantifies exactly when that choice matters (only at Planck-scale areas), so its status can be assessed numerically rather than by fiat.

### Open questions

1. Can the coefficient $1/4$ be derived from first principles without invoking a particular horizon slicing?
2. Is there a natural, geometry-based prescription for the integer Hilbert-space dimension that avoids the floor function?
3. Do non-homogeneous entropy inequalities (e.g., those mixing entropy with energy, as in the energy bounds central to [2]) retain base-invariance?
4. How does the Ostrowski-theoretic perspective of [14] — the equal treatment of all completions of $\mathbb{Q}$ — integrate with the rounding deficit identified in Section 4.5?
5. Can the finite-storage argument of [2] be reformulated entirely in nats, removing any hidden base dependence?

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and decision impact

The users of this result are theorists and model builders in quantum gravity, holography, and high-energy astrophysics who must specify information-capacity limits for proposed experiments — for example, tabletop analog black-hole simulators or quantum memories serving as entropy reservoirs on analog-gravitation platforms. If the invariant formulation holds, the specification changes in a concrete way: the capacity limit is written directly as $S\le A_{\text{phys}}/(4\ell_{P}^{2})$ nats, or equivalently $D\le e^{A/4}$, and the conversion to bits is performed once, at the end, as a derived step $b=S/\ln 2$ rather than being built into the specification. This removes one class of unit-conversion error from design documents and makes explicit which part of a capacity figure is geometric input and which part is a representation choice. A second user group is foundational researchers assessing which ingredients of the holographic framework are conventions: the classification table of Section 4.1 gives them a checklist (base-free, derived, conventional) that can be applied to any entropy bound, not only the Bekenstein–Hawking one.

### (b) Technology readiness

This work is purely analytical and has not undergone peer review. Against the NASA Technology Readiness Level definitions, it resides at TRL 2: the basic principles — Planck natural units, the Bekenstein–Hawking relation, and the change-of-basis view of logarithm bases — are known, and the present work formulates a coherent concept from them, but the concept has not been applied in any concrete reference implementation, numerical code, or experimental design that has been exercised. Analytical work of this kind cannot exceed TRL 3, and nothing in this paper approaches an application demonstration.

### (c) Minimal next test

The smallest next step is a numerical calculation, not an experiment. A study would take an analytically tractable black-hole model — for example, a two-dimensional dilaton black hole — compute its horizon area in Planck units, and evaluate the real bound $e^{A/4}$ and the integer bound $\lfloor e^{A/4}\rfloor$ at a small area such as $A=4$ (four Planck areas, $S=1$ nat). The calculation would verify the relative deficit of $26.4\%$ derived in Section 4.5 and check that the rounding analysis is internally consistent when $A$ is obtained from the model's own geometry rather than assumed. The outcome that would refute the rounding analysis is a quantum-gravity framework that predicts a different integer-dimension prescription at small areas, i.e. a rule with $D_{\text{int}}\neq\lfloor e^{A/4}\rfloor$ at $A=4$; the outcome that would refute the base-free claim is a correction term proportional to $\ln 2$ (or any other base constant) entering the bound at leading order. A second, independent de-risking step is an arbitrary-precision recomputation of the conversion constants and the worked example of Section 4.4, since evaluating $e^{A/4}$ for $A\gtrsim 10^{2}$ exceeds standard floating-point range.

### (d) Engineering, computational and conceptual constraints

* **Computational constraints.** For $A\gtrsim 10^{2}$, $e^{A/4}$ overflows double-precision arithmetic; any numerical implementation of the bound at macroscopic areas requires arbitrary-precision libraries, and the exponent should be handled in logarithmic form ($\log_{10}D=S/\ln 10$) rather than by evaluating $e^{A/4}$ directly.
* **Conceptual constraints.** The integer-rounding step assumes that Hilbert-space dimensions for sub-regions are well-defined countable integers. The overcounting problem reported in [8] — that in certain scaling regimes arbitrarily many high-energy states can be localized in one AdS region, which the authors call a severe overcounting of bulk states — is a concrete warning that the state count a bound applies to can be ill-defined; any implementation must first fix the state-counting prescription.
* **Regime constraints.** As [11] shows, which entropy bound applies depends on the regime (the Hubble bound $S\le S_{\rm H}$ for $R\ge H^{-1}$, the Bekenstein–Verlinde bound $S\le S_{\rm BV}$ for $R\le H^{-1}$), and [2] shows that the D-bound is not appropriate for weakly gravitating inflationary fluctuations, where the energy bound plays the central role. A capacity specification must therefore state which bound it uses before any unit question arises.
* **Open question (constraint status unresolved).** Whether the coefficient $1/4$ in $S=A/4$ is purely geometric or encodes a slicing convention is not settled here; if it is conventional, the conversion constants of Section 4.3 inherit that convention.

### (e) Projected cost or performance bounds

No hardware, material, or monetary cost is involved: the work is analytical, and the only performance metric is the precision of the conversion constants, which is exact to the digits displayed in Section 4.3. No cost projection is applicable, and none is asserted.

### (f) Risks and misuse

A misuse path exists on the interpretive side: a reader could claim that the invariant formulation eliminates all conventional aspects of information theory and therefore that bits are dispensable in engineering practice. That claim is not supported. Bits remain the operational unit of communication engineering, and the result of this paper is limited to the foundational formulation of holographic bounds: it identifies which ingredients are conventions, not which units practitioners should abandon. A second risk is overgeneralizing the classification table beyond its scope: it was constructed for the Bekenstein–Hawking area–entropy relation, and applying it to bounds with energy or cutoff inputs (as in [2]) requires re-derivation, since those bounds mix quantities whose base-invariance is an open question (Section 6, open question 3).

## 8. Conclusion

The holographic entropy bound can be stated entirely in observer-independent quantities. In Planck natural units the core relation is $S=A/4$ and $D\le e^{A/4}$, involving only the dimensionless area $A$, the geometric factor $4$, and the natural exponential; no logarithm-base constant appears. The bit is recovered as the derived quantity $b=S/\ln 2$, and all base-$b$ representations differ by fixed multiplicative constants ($1/\ln 2=1.4426950409$, $1/\ln 10=0.4342944819$, $\ln 10/\ln 2=3.3219280949$), so the invariant and conventional formulations are empirically indistinguishable. The worked example at the assumed area $A=10^{68}$ gives $S=2.5\times10^{67}$ nats, $b=3.6067376\times10^{67}$ bits, and $D\le 10^{1.0857362048\times10^{67}}$. The sole residual conventional element is the integer rounding of the Hilbert-space dimension: it produces a $26.4\%$ relative deficit at $A=4$ (four Planck areas, $S=1$ nat), a $22.1\%$ deficit at $A=1$, and a deficit below $10^{-10^{67}}$ at macroscopic areas. The analysis thereby separates the invariant content of holographic bounds ($A$, $S$, $D$) from methodological conventions (logarithm base, integer counting), corrects the attribution of the Ostrowski-theoretic equal-treatment-of-completions perspective to the invariant-patterns program of [14], and locates the reformulation within a literature whose own authors document the implementation-dependent and prescription-dependent choices that survive inside conventionally phrased "universal" bounds [1], [2], [5], [8], [11]. The result is foundational rather than predictive: it changes how capacity specifications can be written and which quantities a quantum-gravity theory must fix, and it leaves open whether the coefficient $1/4$, the floor-function rounding, and the regime restrictions of the underlying bounds can themselves be freed of convention.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.39.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 12 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Holographic bounds and finite inflation. arXiv:1410.6065. https://arxiv.org/abs/1410.6065
[2] Cosmic holographic bounds with UV and IR cutoffs. arXiv:hep-th/0501023. https://arxiv.org/abs/hep-th/0501023
[3] Quantization-scheme-Independent Energy and Its Implications for Holographic Bounds. arXiv:2601.07607. https://arxiv.org/abs/2601.07607
[4] Holographic Complexity Bounds. arXiv:1910.10723. https://arxiv.org/abs/1910.10723
[5] Holographic bounds on the UV cutoff scale in inflationary cosmology. arXiv:hep-th/0306070. https://arxiv.org/abs/hep-th/0306070
[6] Natural units, numbers and numerical clusters. arXiv:hep-ph/0112097. https://arxiv.org/abs/hep-ph/0112097
[7] Cube or hypercube of natural units. arXiv:hep-ph/0112339. https://arxiv.org/abs/hep-ph/0112339
[8] A Holographic Holographic Bound and the Black Hole S-Matrix. arXiv:1209.3040. https://arxiv.org/abs/1209.3040
[9] Natural units and the vector space of physical values. arXiv:1504.02332. https://arxiv.org/abs/1504.02332
[10] Asymptotic Result of A Generalization of A GCD-Sum. arXiv:2206.05023. https://arxiv.org/abs/2206.05023
[11] Holographic entropy bounds in the inflationary universe. arXiv:hep-th/0301073. https://arxiv.org/abs/hep-th/0301073
[13] https://papers.qnfo.org/papers/compton-cross-ratios-v2. QNFO: Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum (Version 2.3).
[14] https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring. QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics.
