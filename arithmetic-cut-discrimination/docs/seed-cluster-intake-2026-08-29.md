# Seed-Cluster Intake 2026-08-29 — Binding Amendments to QNFO.RES.030

Date: 2026-08-29. Source: vault seed notes `D:\Obsidian\notes\v1\2026\08\29\_2624*.md`
(five notes, one thread). Status: INTEGRATED into PROJECT-PLAN §1.2, §2, §6;
P3 verification tasks D-1..D-4 appended.

## Provenance

1. `_26241003730.md` — "ExoMol and H₂O POKAZATEL — what they are, and how they
   extend the UMP benchmark" (UMP.014 real-data extension plan: energy-window
   Poisson→GOE scan, molecular atlas, isotopologue invariance, `.trans`/`.pf`
   observables, n-mismatch fix, full-spectrum power).
2. `_26241004648.md` — user's unification claim: the ExoMol note stated to be
   "the unification of classical/statistical/quantum mechanics with
   thermodynamics and information as a distinction-based partition/ontology."
3. `_26241010137.md` — critique: attachment does not match the unification
   claim; six technical points; the claim is closest to RES.021
   finite-distinction QM, a different research object.
4. `_26241011209.md` — senior-reviewer verdict on the program: "sharpen but do
   not rescue"; seven required corrections before a UMP.014 v1.1; bottom line:
   the next move is a desymmetrized, n-matched, energy-window scan with a GUE
   null and a positive control on an engineered arithmetic system.
5. `_26241011536.md` — philosophy thread: prime distinctions ↔ places of Q;
   the infinite place as a limit or place-selection rule; QM over C, not R.

Provenance-quality flag: the seed notes elide DOI suffixes as bare
"10.5281/zenodo" (twice in `_26241003730.md`). Their DOI strings must never be
cited verbatim; resolve against the registry (UMP.014 = 10.5281/zenodo.22150472,
concept 10.5281/zenodo.22150471).

## Verified external anchor

`https://osf.io/ba8ns` (verified via OSF API `v2/guids/ba8ns/`, public node,
created 2026-08-28): "QNFO.UMP.014 H-DIST-3 Disconfirmation Criterion —
Pre-Registration". Registers H1 (RES.023, 10.5281/zenodo.22076816), five
observables, Bonferroni-Holm correction, MC nulls = Poisson and GUE/GOE at
n=2000, pre-commitment anchors at QNFO/ultrametric-physics commits e5a673d
(design) and 39381f6/f9593b0/a0a0734 (execution).

**Implication:** the registered null set does NOT include matched-level-density
non-arithmetic nulls. RES.030's null ensemble (smooth log-spaced surrogates,
P_max-smooth random integers, Poisson-on-log-scale) is a NEW null class that
strengthens H-DIST-3, not a duplication. The RES.030 paper will state this
explicitly and cite the pre-registration.

## Binding amendments

- **A1 (Dyson number-variance anomaly — HARD verification task D-1).** The
  verdict flags UMP.014's reported 1.044 vs predicted 0.525 as an unexplained
  factor-of-two. Before RES.030 inherits the estimator, P3 MUST recompute with
  stated L, stated Li unfolding, stated binning, and finite-N error bars;
  resolve whether the 0.525 reference is the correct full-Dyson value
  (1/π²)[log(2πL)+1+γ−π²/8] for the L used. This is a blocking golden anchor.
- **A2 (GUE null, not GOE stand-in — HARD).** At the arithmetic-correction
  order the GOE/GUE distinction matters. RES.030 nulls use true GUE samples
  plus the analytic GUE bulk curve, matched in N, unfolding, binning, and
  window. (Supersedes the inherited GOE Monte Carlo pattern.)
- **A3 (positive control — HARD, P3).** The five-observable pipeline MUST be
  validated on an engineered arithmetic system where the correction is known —
  the arithmetic cut itself at small P_max with injected known deviations is
  the natural control; a second control is a synthetic spectrum with a planted
  Bogomolny–Keating-type oscillatory term.
- **A4 (Bost–Connes category error — HARD).** A finite molecular Q(T) =
  Σ g_n e^{−E_n/kT} has no pole and no Euler-product structure. Any real-data
  "Bost–Connes observable" must be framed as a finite-size crossover with an
  explicit rounding scale (width ~1/ln P_max), never as a zeta-pole claim.
  RES.030's D1–D3 are map-level claims on the cut; the paper will make the
  map/territory boundary explicit per this amendment.
- **A5 (desymmetrization — HARD for real-data application).** ortho/para
  species, K-ladders, parity, polyads: separate species, unfold per species
  with a per-species smoothed staircase, report N per species per window,
  matched nulls at equal effective N.
- **A6 (computed-level caveat).** ExoMol levels are ab initio PES levels, not
  measurements; high-energy windows near dissociation are less converged.
  Any high-energy classification is a property of the PES model until checked
  against experimental levels. Convergence checks are part of the protocol.
- **A7 (POKAZATEL version/count verification).** 4.7M states / 5.5B
  transitions must be verified against the specific ExoMol release/file
  version before quoting (critique point 1).
- **A8 (unification-thread disposition).** The stated unification claim is
  NOT carried by RES.030. Its closest registered object is RES.021
  (10.5281/zenodo.22046458); the ExoMol plan belongs to the UMP
  spectral-statistics line. RES.030 proceeds as the computational
  discrimination layer; the unification thread remains provenance only unless
  separately commissioned.

## Reviewer bottom line (adopted as project positioning)

"The next move is not a new platform. It is a desymmetrized, n-matched,
energy-window scan of the full H₂O spectrum with a GUE null and a positive
control on an engineered arithmetic system. That computation will either
produce the first credible arithmetic signature or close the molecular channel
cleanly. Either outcome is worth publishing."

RES.030 supplies exactly the missing layer: the matched-density null ensemble,
the GUE-matched controls, and the positive-control arithmetic system, computed
before any real-data scan — so the real-data energy-window work (the ExoMol
plan) lands on a validated, pre-registered discrimination machine.

## P3 task additions (golden anchors)

- D-1: recompute Dyson number variance with exact L/unfolding/binning; resolve
  the 1.044-vs-0.525 question. BLOCKING.
- D-2: GUE-matched Monte Carlo null (N-matched, unfolded identically).
- D-3: positive control — engineered arithmetic cut + planted-oscillation
  synthetic spectrum; pipeline must recover both.
- D-4: finite-size crossover formulation of the Bost–Connes observable with
  explicit rounding scale; no pole language.
