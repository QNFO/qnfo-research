# E1: Kappa/SIIT Universality Class Determination

**Type:** Research Note | **Date:** 2026-07-31 | **Status:** Complete
**Cross-Reference:** Adelic Core Synthesis (Zenodo 10.5281/zenodo.17218944, 10.5281/zenodo.17230397)

## 1. Research Question

Does the κ(x) information field, as defined in the Scale-Invariant Information Thermodynamics (SIIT) framework, belong to the logistic (Feigenbaum) universality class, or does it define a distinct universality class?

This question is motivated by a historical modeling consideration: an early "logistic ansatz" modeled κ as following sigmoid saturation dynamics:

\[
\frac{d\kappa}{dt} = r \cdot \kappa \cdot (1 - \kappa)
\]

This logistic growth model belongs to the Feigenbaum universality class (period-doubling route to chaos, δ ≈ 4.669, ν = 1/2). If the actual κ(x) dynamics reduce to this class, the framework's claim of genuinely novel physical dynamics is falsified — it would be a repackaged logistic growth model.

## 2. Method

The κ(x) field equation is not defined by a standalone PDE but derived by substituting the effective gauge coupling relation \(g_\text{eff}(x) = g_0 \kappa(x)\) into the standard renormalization group equations of gauge theories (Zenodo 17218944, §Step 2.3).

### 2.1 κ(x) Cubic RG Equation (Actual)

For a gauge theory with one-loop beta function β(g) = C_g * g³, the substitution \(g_\text{eff} = g_0 \kappa\) yields:

\[
\frac{d\kappa}{d(\ln \mu)} = C \cdot \kappa^3
\]

where C is determined by the gauge group:

| Gauge Group | Coefficient C | Sign |
|:------------|:--------------|:-----|
| QED (U(1)) | \(C = g_0^2 / (12\pi^2)\) | Positive → Landau pole |
| QCD (SU(3)) | \(C = -g_0^2 (11 - 2n_f/3) / (16\pi^2)\) | Negative for \(n_f < 16.5\) → asymptotic freedom |

**Closed-form solution:**

\[
\kappa(\mu) = \frac{\kappa_0}{\sqrt{1 - 2C\kappa_0^2 \ln(\mu/\mu_0)}}
\]

For C > 0: Landau pole at \(\mu_\text{pole} = \mu_0 \exp(1/(2C\kappa_0^2))\). κ diverges at finite energy.
For C < 0: κ → 0 as μ → ∞, with power-law decay κ ∝ 1/√(ln μ).

**Source:** Derivation of Standard Model Gauge Couplings from Scale-Invariant Information Thermodynamics (Zenodo 10.5281/zenodo.17218944), Theorem 4.1, Properties 1–5, and Step 2.3 renormalization group flow.

### 2.2 Logistic Ansatz (Retracted)

The logistic growth model posited:

\[
\frac{d\kappa}{dt} = r \cdot \kappa \cdot (1 - \kappa)
\]

with fixed points: κ* = 0 (unstable for r > 0), κ* = 1 (stable).

**Closed-form solution:**

\[
\kappa(t) = \frac{1}{1 + (1/\kappa_0 - 1) \cdot e^{-rt}}
\]

This produces S-shaped sigmoid convergence with half-saturation at t = ln(1/κ₀ − 1)/r. κ is strictly bounded: κ(t) ∈ [0, 1] for all t.

## 3. Universality Class Comparison

| Property | Logistic Ansatz (Retracted) | κ(x) Cubic RG (Actual) |
|:---------|:---------------------------|:-----------------------|
| **ODE Form** | dκ/dt = r·κ·(1−κ) | dκ/d(ln μ) = C·κ³ |
| **Nonlinearity Order** | Quadratic (κ²) | Cubic (κ³) |
| **Stable Fixed Point** | κ* = 1 | κ* = 0 (C < 0) or none (C > 0) |
| **Unstable Fixed Point** | κ* = 0 | κ* = 0 (C > 0) |
| **Convergence Shape** | Sigmoid (S-curve) | Power-law in log-space |
| **Late-time Behavior** | κ → 1 exponentially | κ ~ 1/√(ln μ) or → ∞ (Landau pole) |
| **Saturation Bound** | YES (κ ≤ 1, carrying capacity) | NO (unbounded or → 0) |
| **Universality Class** | Feigenbaum (δ ≈ 4.669) | Cubic-field (distinct) |
| **Correlation Exponent (ν)** | 1/2 (mean-field Ising) | 1/d (different mechanism) |
| **Time Variable** | Physical time (t) | Energy scale (ln μ) |

## 4. Numerical Verification

### Logistic Evolution (κ₀ = 0.01, r = 1.0)

| t | κ(t) |
|:--|:-----|
| 0.0 | 0.010 |
| 1.0 | 0.027 |
| 2.5 | 0.112 |
| 5.1 | 0.612 |
| 10.0 | 0.996 |

**Behavior:** Sigmoid S-curve. Half-saturation at t ≈ 4.6. κ → 1 exponentially.

### Cubic RG — QED-like (C > 0, κ₀ = 0.01)

| μ/μ₀ | κ(μ) |
|:------|:-----|
| 1.0 | 0.010000 |
| 2.6 | 0.010002 |
| 10.5 | 0.010005 |
| 100.0 | 0.010009 |

**Behavior:** Near-constant until Landau pole. No upper bound — κ → ∞ at finite μ.

### Cubic RG — QCD-like (C < 0, κ₀ = 0.5)

| μ/μ₀ | κ(μ) |
|:------|:-----|
| 1.0 | 0.500 |
| 2.6 | 0.359 |
| 10.5 | 0.273 |
| 100.0 | 0.211 |

**Behavior:** Power-law decay. κ ∝ 1/√(ln μ) for large μ. No lower bound at finite μ.

## 5. Structural Distinction Proof

The logistic and cubic dynamics are structurally distinguishable at the ODE level and cannot be RG-equivalent:

1. **Nonlinearity order:** Quadratic vs cubic — these have different renormalization group fixed-point structures. A quadratic interaction generates a non-trivial fixed point; a cubic interaction generates a trivial (Gaussian) fixed point or a pole.

2. **Boundedness:** The logistic ansatz enforces κ ∈ [0, 1] via a carrying capacity. The cubic RG has no intrinsic saturation mechanism — κ either diverges (Landau pole for C > 0) or decays to zero with no lower bound at finite μ (C < 0). A bounded system cannot be RG-equivalent to an unbounded one.

3. **Time variable:** The logistic ansatz uses physical time (t). The cubic RG uses the energy-scale logarithm (ln μ). While a change of variables t ↔ ln μ could potentially map one ODE to another, the functional forms dκ/dt = κ(1−κ) and dκ/dx = κ³ are structurally distinct — the former has a stable fixed point at κ = 1, the latter does not. No smooth change of variables can introduce a new fixed point.

4. **Universality class signature:** The Feigenbaum universality class is characterized by period-doubling critical exponents δ ≈ 4.669, α ≈ 2.502. These are universal for all unimodal maps with quadratic maximum. The cubic RG has no period-doubling structure — it is a monotonic flow with a single trivial fixed point.

## 6. Verdict

**The κ(x) cubic RG dynamics define a DISTINCT universality class from the logistic (Feigenbaum) class.**

The logistic ansatz was correctly retracted. The SIIT framework contains genuinely non-logistic dynamics in its gauge-coupling renormalization group flow. The claim of novel physical dynamics survives this universality-class falsification test.

## 7. Calibration Register

**[CHECK: 2027-07-31] [STRONG]** If κ(x) RG dynamics are shown to belong to the Feigenbaum universality class (δ ≈ 4.669, ν = 1/2 from the period-doubling route to chaos, characterizing all unimodal maps with quadratic maximum), this result is FALSIFIED.

**Likelihood-Anchor:** Empirical Base Rate — cubic and quadratic nonlinearities are structurally distinguishable at the ODE level. A system with a stable fixed point at κ = 1 and bounded dynamics cannot be RG-equivalent to a system with no non-trivial fixed point and unbounded dynamics. The distinction does not depend on precision of measurement; it follows from the topological properties of the ODE vector field.

**Post-hoc risk:** "The logistic ansatz was never a serious proposal — it was just an illustration." This rationalization is blocked by the explicit claim above: the universality class of the logistic ansatz is a specific, falsifiable hypothesis about κ(x). The test shows it is wrong. If the logistic ansatz was never serious, the calibration register entry has no cost; if it was serious, it is falsified.

## 8. Cross-References

- **Zenodo 10.5281/zenodo.17218944:** Derivation of Standard Model Gauge Couplings from Scale-Invariant Information Thermodynamics — source of κ(x) cubic RG equation (Theorem 4.1, Step 2.3)
- **Zenodo 10.5281/zenodo.17230397:** Defining Kappa as a Physical Information Framework — axiomatic foundations of κ as scale-invariant information substrate
- **Adelic Core Synthesis:** Parent framework connecting κ(x) gauge-coupling derivation to measurement stratigraphy
- **Consilient-Gap-Synthesis:** Meta-research program analyzing cross-program dependencies
- **Measurement Stratigraphy (Zenodo v3.0):** Sheaf-theoretic framework connecting mathematical eras to measurement operations

## 9. Next Actions

- [x] E1: Universality class determination — COMPLETE
- [ ] E2: Cramér-von Mises order-statistics test — BLOCKED (input data "8 rung energy scales" not formalized in any artifact; measurement stratigraphy paper defines 7 mathematical eras without physical energy thresholds)
- [ ] E3: Formal research note publication (Zenodo DOI) for E1 finding
