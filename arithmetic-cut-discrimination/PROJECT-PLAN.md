# WBS: QNFO.RES.030

# Project Plan — Arithmetic Cut Discrimination

- **WBS:** QNFO.RES.030
- **Slug:** arithmetic-cut-discrimination
- **Repo:** QNFO/qnfo-research · **Branch:** res/paper/arithmetic-cut-discrimination
- **Program:** QNFO.RES (qnfo-research)
- **Predecessors:** QNFO.RES.027 adelic-quantum-statistics (10.5281/zenodo.22133122), QNFO.RES.028 arithmetic-anyon-contact (10.5281/zenodo.22124744), QNFO.RES.029 adelic-quantum-arithmetic (10.5281/zenodo.22142794), QNFO.UMP.014 distinction-based-ultrametric (10.5281/zenodo.22150472)
- **Phase 0 lock date:** 2026-08-29

## 1. Charter

The QNFO arithmetic-statistics line has published the identification of the two
exchange statistics with two multiplicity rules on one integer lattice
(RES.027), its bounded-occupation continuation (RES.028), and the consolidated
map with the practitioner crosswalk (RES.029). The line's published observable
is computational: the primon-gas specific heat deviates from the
smooth-density-of-states ideal gas at every sampled temperature, by up to
roughly three quarters at low temperature, in both statistics.

The program's own red team then raised the decisive objection in the
provenance chats attached to those records: an irregular spectrum with the same
level density but no prime structure might reproduce the deviation, making the
specific-heat observable level-density content rather than arithmetic content.
Three questions were left open: (1) can the arithmetic cut be distinguished
from a non-arithmetic cut with the same level density; (2) does the separation
survive finite P_max and finite measurement noise; (3) is the distinguishing
information in the specific heat, or only in the two-point statistics.

This project adjudicates those three questions computationally, before any
platform is built. It constructs three matched-level-density non-arithmetic
null ensembles, computes the specific heat and the unfolded two-point
statistics for the arithmetic cut and every null, and reports separation
thresholds in P_max and noise, per statistics and per observable.

### 1.2 Core claim (P6 — LOCKED at Phase 0)

Define the arithmetic cut on mode energies ε_p = ln p for primes p ≤ P_max,
with three occupation rules: unrestricted (Z_B = ∏_{p≤P_max}(1 − p^{−β})^{−1}),
squarefree (Z_F = ∏_{p≤P_max}(1 + p^{−β})), Boltzmann (Z_MB = exp(Σ_{p≤P_max} p^{−β})).
The matched-density non-arithmetic null ensemble is the constructive set:
smooth log-spaced surrogates, P_max-smooth random integers, and a
Poisson-on-log-scale process, all with the same mean level density as the cut.

- **D1 (discriminability).** For P_max beyond a computable minimum, at least one
  observable in {specific-heat curve C_V(β), unfolded pair correlation R_2(s),
  spectral form factor K(τ), number variance Σ²(L)} separates the arithmetic cut
  from every member of the matched-density null ensemble at ≥ 2σ.
- **D2 (information location).** The arithmetic-only information beyond
  level-density content resides in the two-point statistics; the specific heat
  alone cannot separate the arithmetic cut from a matched-density null.
- **D3 (thresholds).** The minimal P_max for separation and its noise tolerance
  are computable and are reported per observable, per statistics, per null.

Disconfirmation matrix (pre-registered): D1 fails if no observable separates at
any feasible P_max; D2 fails if specific-heat-only separation exists while the
two-point observables fail; D3 is a deliverable, not a claim. A negative branch
is published as a result, per the program null-ledger (UMP.014 published its
first negative real-data result the same way).

## 2. Why a reader should care (SO-WHAT)

A spectroscopist or metrologist considering the "arithmetic spectrometer"
platforms (superconducting qudit registers, optical lattices, photonic
waveguide arrays) needs to know, before spending beam time, whether the
predicted specific-heat signature is real arithmetic content or an artifact of
any irregular spectrum, and at what mode count and noise level the signature
becomes resolvable. A number-theorist gets a sharp computational statement of
which spectral function carries the prime-gap information. If the mimicry
objection stands, the published observable is corrected to the two-point
function and the thermodynamic claim is demoted — either outcome changes what
experimentalists should measure, so the result is actionable in both branches.

## 3. Phases with WBS

| Phase | WBS step | Content | Gate |
|---|---|---|---|
| P0 | RES.030.P0 | Init: WBS resolution, branch, scaffold, PROJECT-PLAN, core-claim lock, UIA 15Q | commit/tag/push |
| P1 | RES.030.P1 | Due diligence: ZENODO-INQUIRY-1 UIA, DUE-DILIGENCE-DEPTH-1 corpus sweep, external verification | HARD |
| P2 | RES.030.P2 | Literature + estimator construction (SPECTRAL-ESTIMATOR-CONSTRUCTION-1 six-bug checklist) | HARD |
| P3 | RES.030.P3 | Computational verification suite (VERIFY-IN-CODE-1, golden recovery) | HARD |
| P4 | RES.030.P4 | Deep research + red team (5 adversary positions + UIA) | HARD |
| P5 | RES.030.P5 | Publish: Zenodo deposit, publication gates (PUBLICATION-PROSE-1, COMPUTATIONAL-VERIFICATION-1, PRACTITIONER-RELEVANCE-1) | HARD |
| P6 | RES.030.P6 | Deploy: D1 living-paper, KG node, Vectorize, R2 mirror | HARD |
| P7 | RES.030.P7 | Disseminate: SEO, Buffer, papers.qnfo.org, Internet Archive | SOFT |
| P8 | RES.030.P8 | Distribute: GitHub tag, closeout, registry re-point, memory log | HARD |

## 4. Milestones with gate criteria

- **M0** Phase 0 committed, tagged v0.1-phase0-res030, pushed, ls-remote
  verified; registry row active/P0. (HARD)
- **M1** UIA 15Q committed; corpus sweep with ≥3 query formulations per topic,
  search_papers limit ≥20, resolve_paper_id per hit, ≥2 adjacent WBS domains
  (UMP, RES minimum), external verification (arXiv/OpenAlex/Crossref/CDX),
  every count with an evidence file in artifacts/external-search/. (HARD)
- **M2** Estimators canonical (k-th-neighbor pair correlation, exact Li
  unfolding, full Dyson formula, no rank unfolding, Montgomery–Odlyzko on
  zeros / Gallagher on primes, form factor report-only at fixed τ). (HARD)
- **M3** Every quantitative claim reproduced by deposited deterministic
  scripts; golden anchors recovered (Bost–Connes C_V(1.06)=316.3 vs 312.1;
  GUE pair correlation; Dyson 1.044 vs 0.525; twin-gap first bin zero).
  (HARD)
- **M4** Red team delivered; HARD findings remediated or pre-registered.
- **M5** Published with plain-prose abstract naming the bridge (arithmetic
  cut / specific heat / null models), practitioner section, premise-boundary
  statement, full source deposit. (HARD)
- **M6–M8** Distribution complete; registry re-pointed to published DOI.

## 5. Deliverable Registry

- DR1 Paper `<slug>.md/.html/.pdf` (never `paper.*`).
- DR2 Verification scripts + outputs in `artifacts/verification/` (deposited
  with the paper).
- DR3 Null-ensemble generator (`artifacts/`), seed-fixed, documented.
- DR4 Discrimination protocol + threshold tables: ROC curves, minimal
  P_max(2σ) vs noise, per statistics {B, F, MB} × null × observable.
- DR5 Interactive demo via qwav-demo-kit (DEM-E0 flag, if flagship).
- DR6 Process artifacts: UIA, due-diligence report, red-team reports,
  external-search evidence, deep-research.md.

## 6. Risk Register

- R1 Estimator-construction bugs → SPECTRAL-ESTIMATOR-CONSTRUCTION-1 checklist
  + golden-anchor recovery in P3.
- R2 Null-ensemble contamination by arithmetic structure → nulls constructed
  independently (surrogate spacing, smooth integers, Poisson); generators
  documented and seed-fixed.
- R3 P_max scaling beyond feasible computation → PNT asymptotics + exact
  truncated products; feasible exact range targeted, asymptotics beyond.
- R4 WBS collision → atomic check-then-insert performed at P0 (registry row
  verified by independent re-query).
- R5 DNS flap on external APIs → DNS-FLAP-IP-PIN-1 retry pattern for API hosts.
- R6 Premature claim → pre-registered disconfirmation matrix; negative branch
  publishable.

## 7. Success Criteria

- SC1 Thresholds computed for {B, F, MB} × {3 null ensembles} × {≥3
  confidence levels}, with noise tolerance.
- SC2 Information decomposition: C_V-only vs two-point-only separation, stated
  per observable.
- SC3 Either branch (positive or negative) published with deposited code and
  full provenance.
- SC4 All HARD gates pass at every phase; no deferred items at closeout.

## 8. Premise-depth disclosure

- **L0 — unanalyzable primitives:** none beyond the standard Boltzmann weight
  e^{−βE} with a real inverse temperature β ∈ R. No p-adic amplitude is used;
  no physical length is identified at a p-adic place. The premises end exactly
  at the boundary inherited from RES.027–029 and UMP.014, and this computation
  never crosses it.
- **L1 — definitional:** the three occupation rules; the constructive
  definitions of the matched-density null ensembles.
- **L2 — derived, exact:** Euler-product identities, the specific-heat
  second-derivative forms, high/low-temperature limits.
- **L3 — imported, named (re-verified in code, not re-derived):**
  Montgomery–Odlyzko GUE pair correlation for the Riemann zeros; Gallagher
  Poisson statistics for the primes with twin-gap hard core; Bost–Connes
  Z(β) = ζ(β) transition at β = 1; the Dyson number-variance formula.
- **L4 — risk-bearing claims:** D1, D2 (Section 1.2), carrying the
  disconfirmation matrix.

## 9. Practitioner-facing deliverable (what a practitioner can do)

A metrologist or spectroscopist gets a discrimination machine, not a
conclusion: a deposited script that takes any level sequence plus a cutoff and
a noise model, and returns per-null verdicts — which nulls are excluded at
which confidence, the minimal P_max at which the arithmetic cut separates at
2σ, and the noise tolerance of that separation. The same script converts the
published specific-heat deviation into a threshold table usable as an
engineering specification for qudit-register, optical-lattice, or photonic
platform design. The protocol is blind to the origin of the spectrum, so it
applies to any candidate "arithmetic" system.
