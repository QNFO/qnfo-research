# Terminology Audit — BP-2 (QNFO.RES.007)

**Date:** 2026-08-14 · **Gate:** HARD (BP-2) — every field-specific term checked against standard definition.

## Terms used in the draft and their standard definitions

| Term | Standard definition | Draft usage | Verdict |
|:-----|:--------------------|:------------|:--------|
| Invariant | A quantity unchanged under a specified transformation group | "a number that survives all arbitrary choices"; invariants of redundancy groups | MATCH |
| Redundancy group | Group of transformations that leave physical content unchanged (units, coordinates, gauge, basis, scale) | enumerated groups: units, coordinates, gauge, basis, scale | MATCH (usage is explicit and generalizing; standard in gauge-theory and dimensional-analysis contexts) |
| Projective Hilbert space | Space of rays of a Hilbert space; CP(H) | physical state = [ψ] = {e^{iθ}\|ψ⟩} | MATCH |
| Ray | Equivalence class of nonzero vectors under scalar multiplication | equivalence class under global phase | MATCH |
| Spectral invariant | Quantity determined by the spectrum of an operator, invariant under unitary equivalence | measured energy = spectral invariant | MATCH |
| S-matrix | Scattering matrix; unitary operator mapping in-states to out-states | invariant under field redefinitions, gauge choices, renormalization scheme | MATCH |
| Holonomy | Parallel transport around a loop; Aharonov–Bohm phase | AB phase = holonomy of connection | MATCH |
| Chern number | Topological invariant of a vector bundle; first Chern class integrated | quantum Hall conductance = first Chern number | MATCH |
| BRST cohomology | Physical Hilbert space = cohomology of BRST operator (closed modulo exact) | physical states = BRST cohomology | MATCH |
| Bare parameter | Unrenormalized parameter in a Lagrangian; scheme-dependent, typically divergent | infinite, scheme-dependent, unphysical; scaffolding | MATCH |
| Renormalization scheme | Convention for absorbing divergences; physical observables scheme-independent | observables finite and invariant under RG flow | MATCH |
| Fixed point | Point x with f(x)=x; or theory invariant under RG flow | e and π as fixed points of self-referential equations | MATCH (usage extended from analysis to structural characterization; explicitly defined in draft §Formal derivation) |
| Compact closed category | Symmetric monoidal category with duals for every object; enables traces | every object has a dual; processes bend back; traces | MATCH |
| Trace (categorical) | Scalar obtained by closing a loop in a traced monoidal/compact closed category | feedback loops yield scalar invariants | MATCH |
| Adjoint | A†; Hilbert-space adjoint; self-adjoint = A=A† | self-adjointness = mirror fixed point of adjoint involution | MATCH |
| Kernel of exponential map | {x : e^{ix}=1} = 2πℤ for exp: ℝ→U(1) | kernel 2πℤ; π = half-period | MATCH |
| U(1) | Circle group; compact Lie group | compact group with exponential map θ↦e^{iθ} | MATCH |

## Boundary definitions stated in-draft

- **Unit bridge**: dimensionful constant identifying two categories of quantity (c: space/time; ħ: energy/frequency; G: mass-energy/curvature). Standard in dimensional analysis; consistent with ODR place-democracy framing.
- **Self-application / self-closure**: defined operationally in the Formal derivation section (T[f]=f′; periodic boundary conditions). These are introduced definitions — flagged as such, not standard terms misused.

## Numerology classification (BP-8)

- Claims of the form "constant ≈ expression": **NONE** in the draft.
- C3 classification: **Index-Selection/Structural characterization** — exact fixed-point equations with unique solutions; not an approximation claim; no look-elsewhere exposure. BP-3 N/A.
- No Dense-Approximant, Ratio-Factorization, Transcendental-fit, or Pattern-in-Noise claims present.

## Verdict

**PASS** — all field-specific terms match standard definitions; introduced definitions are explicit; no numerology exposure.
