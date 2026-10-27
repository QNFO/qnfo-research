# Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds (Version 3.0)

## Abstract

The holographic entropy bound is conventionally stated in bits, a unit that embeds two human conventions: integer counting of states and the choice of logarithm base 2. This revision asks whether the bound can be restated entirely in observer-independent quantities, and it strengthens the published formulation by situating it in the current holographic literature. Working in Planck natural units ($c=\hbar=G=k_{B}=1$), area is a dimensionless number $A$ in Planck areas and physical entropy is the natural-logarithm entropy $S=A/4$ (nats). We derive the base-free bound $D\le e^{A/4}$ on the Hilbert-space dimension $D$, show that the bit appears only as the derived quantity $b=S/\ln 2$, and prove that all base-$b$ representations differ by fixed multiplicative constants, so they are empirically equivalent. A worked example with $A=10^{68}$ gives $S=2.5\times10^{67}$ nats, $b=3.6067376\times10^{67}$ bits, and $D\le 10^{1.0857362\times10^{67}}$. The only residual conventional element is the integer rounding of $D$: at $A=4$ (four Planck areas, $S=1$ nat) the relative deficit is $26.4\%$, while at $A=10^{68}$ it falls below $10^{-10^{67}}$. The revision also corrects two errors of the published version: the Ostrowski-theoretic context is now tied to the work that states it, and the minimal next test is restated with the correct area normalization. The result is foundational: it separates the invariant content of holographic bounds ($A$, $S$, $D$) from methodological conventions.

## 1. Introduction

Anyone who specifies information-capacity limits for quantum-gravity experiments — for example, tabletop analog black-hole simulators or quantum memories used as entropy reservoirs in analog-gravitation platforms — must translate the holographic entropy bound into an operational unit. The standard translation target is the bit, and the bit presupposes two choices made by human information technology: that states are counted as integers, and that the logarithm is taken to base 2. Neither choice is dictated by the bound itself, and their presence obscures whether the bound contains any further hidden anthropocentric choices that could affect the interpretation of data. If the bound can be written solely in observer-independent quantities, a designer can assess capacity limits directly from geometric data, and a theorist can see exactly which parts of the holographic framework are conventions and which are invariants. That separation changes a concrete decision: how capacity specifications for analog-gravitation platforms are written, and which quantities a quantum-gravity theory must fix to make the bound predictive.

The published version of this analysis [12] established the core formulation but contained two defects that this revision corrects. First, its Discussion and Conclusion attributed the "Ostrowski-theoretic perspective" to a reference that does not develop that perspective; the valuation-theoretic material belongs to the invariant-patterns program of [14], which states Ostrowski's theorem as a physical principle. Second, its minimal-next-test section described a model "with area $A=4$ (one Planck area)"; $A=4$ is four Planck areas, chosen because it gives $S=1$ nat. Both corrections are carried through below, and the literature base is replaced: the works now cited are holographic-bound analyses in cosmological and AdS settings [1, 2, 5, 8, 11], holographic complexity bounds [4], scheme-independence questions for holographic energy [3], and the natural-units and invariant-patterns literature [6, 7, 9, 13, 14].

**Contributions.**
(i) A natural-unit formulation of the holographic entropy bound, $D\le e^{A/4}$ with $S=A/4$, in which no logarithm-base constant appears in the core relation — derived in Section 3.
(ii) Explicit arithmetic derivations of the conversion constants between nats, bits, and decimal digits, of a macroscopic worked example at $A=10^{68}$, and of the integer-rounding deficit at $A=4$ and at $A=10^{68}$ — Section 4.
(iii) A proof that all base-$b$ entropy representations are related by fixed multiplicative constants, establishing the empirical equivalence of the invariant and conventional formulations — Section 4.
(iv) A corrected statement of the minimal next test, with $A=4$ identified as four Planck areas ($S=1$ nat), and a corrected attribution of the Ostrowski-theoretic framing to [14] — Sections 6 and 7.

The paper proceeds as follows. Section 2 discusses the related work. Section 3 sets out the natural-unit framework and the analytical method. Section 4 presents the derivations with step-by-step arithmetic. Section 5 reports the computed results. Section 6 discusses limitations, failure modes, and falsification conditions. Section 7 gives practical implications, readiness, and the smallest next test. Section 8 concludes.

## 2. Background and Related Work

This section discusses the works that bear on the two halves of the argument: the physical content of holographic entropy bounds, and the status of units and counting conventions in physics.

**Holographic bounds in cosmology.** [1] compares two holographic arguments that limit inflation — the de Sitter Equilibrium (dSE) cosmology and the approach of Banks and Fischler (BF) — and finds that simple versions yield the same bound on the number of e-foldings. Its excerpts state that in both pictures the entropy $3\pi/\Lambda$ of the de Sitter horizon represents the finite information of the universe, that BF bound the entropy in a cavity the size of the apparent horizon rather than using the horizon entropy, and — decisively for the present argument — that "while the phrasing of the BF bound in terms of entropy sounds pleasingly universal, the details of its implementation rely heavily on the cosmological history of the universe to which it applies." That conclusion is direct support for the thesis of this paper: the universal-sounding entropy phrasing of a holographic bound can conceal implementation-dependent choices, and isolating what is implementation-independent is a real analytical task. [11] develops holographic entropy bounds for radiation-dominated and quasi-de Sitter universes, introducing three entropies and showing in its Discussion that the Hubble bound $S\le S_{\rm H}$ is valid for $R\ge H^{-1}$ while the Bekenstein-Verlinde bound $S\le S_{\rm BV}$ is valid for $R\le H^{-1}$. The regime-dependence of which entropy bound applies reinforces the need to state bounds in quantities whose meaning does not shift between regimes. [2] introduces cosmic holographic bounds with UV and IR cutoffs and concludes that the D-bound derived by analogy with de Sitter spacetime is not appropriate for quantum fluctuations of inflation because the system is weakly gravitating, that the energy bound then plays the central role, and that the indirect entropy bound constrains the UV cutoff to $\Lambda\sim M_{p}$. [5] reaches a compatible conclusion from the perturbation side: holographic bounds on the UV cutoff of inflation depend on the coarse-graining prescription used to compute the entropy, and the paper proposes entanglement entropy as the natural measure of the perturbation entropy. The coarse-graining prescription is exactly the kind of choice this paper's classification scheme is designed to expose: it is a convention-level input that sits upstream of any statement in bits or nats.

**Holographic bounds in AdS and the status of defined quantities.** [8] derives a holographic bound from field-theoretic considerations in the gauge/gravity correspondence, using boundary-compact wavepacket sources, and reports two limitations its own Conclusion states: the particle-number restriction does not apply to pure gravity, where overlapping boundary sources are allowed, and in certain scaling regimes it seems possible to localize arbitrarily many high-energy states in one AdS region, which the authors describe as a severe overcounting of bulk states. This matters here because it shows that even the derivation of a holographic bound carries structural assumptions — about sources, overlaps, and particle number — that are logically prior to any unit convention. [3] examines a different convention-dependence: in holographic duality the total energy obtained from holographic renormalization depends on the choice of quantization scheme, and the paper introduces a modified energy $\mathcal{H}$ that is independent of that choice, applying it to four-dimensional AdS with a massive scalar. The parallel is exact in structure: where [3] removes a scheme choice from the definition of energy, this paper removes a base choice from the definition of entropy. [4] studies the action growth rate $\dot{I}_{\rm WDW}$ of the Wheeler-DeWitt patch for $D\ge4$ AdS black holes with spherical, toric, and hyperbolic horizons ($k=1,0,-1$), proposes bounds on holographic complexity under the complexity=action conjecture, and introduces a modified complexity=volume conjecture with growth rate $\dot{\cal C}_{V}=2P_{\rm th}\,\Delta V_{\rm th}$. Complexity is a holographic quantity that, like entropy, is a count-like number; the existence of sharp bounds on it in geometric form is a further instance of the pattern this paper formalizes, in which the bound's content is geometric and its unit expression is derivative.

**Natural units and conventions.** [6] presents the system of natural units of high-energy physics, defined by setting $c$, $\hbar$, and $k_{B}$ to unity, lists the exact numerical values of those constants in SI units ($c=299\,792\,458\ {\rm m\,s^{-1}}$, $\hbar=1.054\,571\,596\times10^{-34}\ {\rm J\,s}$, $k_{B}=1.380\,650\,3\times10^{-23}\ {\rm J\,K^{-1}}$), and concludes that with $[c]=[\hbar]=[k_{B}]=1$ high-energy physics admits a one-dimensional system of units organized in numerical clusters spanning $10^{\pm80}$. This is the established practice, within a subfield, of expressing physical law in dimensionless constant form — the practice this paper extends to information measures. [7] supplies the historical and conceptual anchor: it recounts that Planck introduced the natural units $h$, $c$, $G$, $k$ in 1897–1899, that only $c$, $\hbar$, $G$ retained status in the "cube of theories," and it argues from the definition $T=dU/dS$ that $k$ is not a natural unit at all but "a ratio of 'hand-crafted' units of temperature and energy," i.e. a conversion factor from degrees to joules. The same argument applies verbatim to the bit: $\ln 2$ is a conversion factor between the natural-log entropy and a unit chosen for engineering convenience. [9] gives the mathematical formalism behind such conversions: it constructs the vector space of physical values, in which different unit systems correspond to different bases and a transformation between unit systems is a matrix-vector multiplication, and it demonstrates the formalism on the subspace spanned by $\{10,\mathrm{m},\mathrm{s},\mathrm{kg}\}$. Under this formalism, the constants $1/\ln 2$ and $1/\ln 10$ derived in Section 4 are change-of-basis coefficients, which is the precise sense in which bits and decimal digits are "derived" units. [13] contributes the methodological caution from a neighboring program: it documents that an earlier analysis "blindly fit decimal PDG masses — numbers derived from an SI unit system calibrated to human-chosen standards," that these are "decimal floating-point artifacts, not physical invariants," and that an unconstrained search produced a retracted "4.8× improvement over random" claim. That case study is the empirical motivation for insisting, as this paper does, that the quantities in a fundamental bound be invariants rather than artifacts of a unit system. Finally, [14] states the organizing principle this paper adopts: physics is the study of invariant patterns under specified transformations, measurement units are scaling conventions pegged to arbitrary reference objects, the true invariants are dimensionless ratios, and in Planck units ($\hbar=c=G=k_{B}=1$) every physical quantity becomes a dimensionless number. Its §3.1 states Ostrowski's theorem — every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the standard real absolute value or to a $p$-adic one — and draws the conclusion that a non-anthropocentric physics would treat all completions of $\mathbb{Q}$ equally. This is the correct home for the Ostrowski-theoretic perspective that the published version of this paper misattributed; Section 6 uses it where it belongs.

**The predecessor.** [12] is the published version 2.0.0 of this analysis. Its Results section states the base-free core $D\le e^{A/4}$, $S=A/4$; the conversion constants $1/\ln 2=1.4426950409$, $1/\ln 10=0.4342944819$, $\ln 10/\ln 2=3.3219280949$; the macroscopic example at $A=10^{68}$; the rounding deficit of $26.4\%$ at $A=4$; and the empirical-equivalence claim R5. This revision keeps all of those results, re-derives them with full arithmetic in Section 4, corrects the two errors noted in the Introduction, and replaces the literature treatment with the works discussed above.

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
* The factor $4$ from the Bekenstein–Hawking relation.
* $e = 2.718281828459045\ldots$

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

The mantissa quotient is $2.5/2.302585092994046 = 1.085736203\ldots$, so

$$
\log_{10}D = 1.085736203\ldots\times10^{67},\qquad D\le 10^{1.085736203\times10^{67}}.
$$

**Step 4: Consistency check.** Convert $\log_{10}D$ back to bits using $\log_{2}10=\ln 10/\ln 2 = 3.3219280948873626$:

$$
b_{\text{from }D}=\log_{2}D = 3.3219280948873626\times 1.085736203\times10^{67}.
$$

The mantissa product is $3.3219280948873626\times 1.085736203 = 3.6067376\ldots$, so

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
  $D\le 10^{1.085736203\times10^{67}}$.

* **R4 (Rounding deficit).** At $A=4$ (four Planck areas, $S=1$ nat): $D_{\text{int}}=2$, relative deficit $26.4\%$. At $A=1$: $D_{\text{int}}=1$, relative deficit $22.1\%$. At $A=10^{68}$ the relative deficit is $<10^{-10^{67}}$.

* **R5 (Empirical equivalence).** Any homogeneous entropy inequality is invariant under base change; therefore the invariant and conventional formulations are empirically indistinguishable.

* **R