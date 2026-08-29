# Deep Research & Structured Forecast — QNFO.RES.031 (Phase 4)

- **Date:** 2026-08-29 · **WBS:** QNFO.RES.031.P4 · **Gate:** M4 (red team delivered; HARD findings remediated or pre-registered)
- **Method:** research skill Phase 4 protocol, scope-scaled (the record adds no empirical claims — the empirical content is RES.030's adjudication).

## Stage -1: Credence Statement (stated-with-bases priors)

**Honesty label (red-team A-4, 2026-08-29).** The priors below are stated-with-bases credences, NOT a scoring-rule calibration: the base rate derives from a selected sample of audited instances (instances are known precisely because they were error-audited — selection effect, small N), and no calibration scoring rule has been applied. The numbers' direction carries the information; their precision does not.

**Base rates (from this record's own lineage).** The arithmetic-statistics line has shipped four records. RES.030's P3/P4 found 2 correctable quantitative errors already in the *published* lineage (D-1 Dyson window mismatch; D-4 316.3 attribution) and adjudicated D2 as disconfirmed-as-pre-registered. UMP.014 shipped the line's first negative real-data result. The seed Dictionary for this record carried **11** quantitative errors (the C3 ledger). Empirically, the base rate of "a correspondence-dictionary record in this line contains at least one correctable quantitative error at first audit" is ≈ 1.0 — every prior instance had at least one.

**Calibrated priors for the locked claim set (stated with bases):**

| Claim | P(correct) | Basis | Disconfirmation trigger |
|---|---|---|---|
| C1 exact dictionary (identities) | 0.97 | theorem-level; 18/18 + 34/34 code checks; independently re-run by 2 red-team slots; residual risk = an identity outside the explicit coverage list | any identity fails in the deposited suites |
| C2 five-level ladder (L2 ≠ L4; L3-only bridge) | 0.80 | methodological; no external precedent (gap, not constraint); risk is an exhibited admissible L2→L4 inference | an admissible L2→L4 inference is exhibited |
| C3 correction ledger complete (no twelfth error) | 0.65 | audit-level by definition; the seed had 11, so a twelfth is plausible; consequence pre-registered: a twelfth found error is a data-quality finding + record update, NOT falsification of the record's purpose | a twelfth uncorrected error is found by an independent audit |
| C4 negative discipline survives publication prose | 0.75 | depends on P5 prose discipline; the Novelty red-team slot already caught one internal-vocabulary leak in §2 (M-3, remediated) | published prose re-imports an L2→L4 slide |
| P(record ships with zero red-team HARD findings this pass) | 0.50 | history: every phase of this record found at least one HARD/MEDIUM item; RES.030 P4 found 1 HIGH | — (expectation, not a claim) |

**Calibration discipline:** these priors are written BEFORE the P4 red team runs (this document precedes the slots). Post-hoc calibration check goes in the red-team aggregation.

## Stages 0–8 (scope-scaled)

- **Stage 0 — object and scope.** The record: the audited corrected dictionary (C1), the interpretive ladder (C2), the correction ledger (C3), the negative list (C4). Premise boundaries (unchanged from P1): the L3/L4 boundary (no physical temperature at any p-adic place); the β = s identification (formal choice); the C3-completeness claim (audit-level).
- **Stage 1 — evidence inventory.** P2 suite (18/18), P3 suite (34/34), external verification set (Crossref/DataCite/OpenAlex/arXiv/Patents/CDX probes), triage (39/39 records classified, 0 Reject), UIA 15Q (P1), red-team reports (P1×5 slots, P2×2, P3×2). Count note (red-team A-9): the 18/34 counts include paired facets (raw + tail-corrected identity pairs; cache coarse + bounded) — net distinct assertions ≈ 15 + ~30; no vacuous padding.
- **Stage 2 — disconfirmation matrix (concrete instruments).** C1: the deposited suites are the falsification instrument — any failing identity is a theorem-level falsification. C2: an exhibited admissible L2→L4 inference. C3: an independent audit finding a twelfth uncorrected error. C4: the published prose violating the negative list. No new empirical claims exist to falsify — the empirical content remains RES.030 (D1 CONFIRMED, D2 disconfirmed as pre-registered).
- **Stage 3 — forecast per claim.** C1: near-certain; the forecast risk is coverage, not correctness (the coverage list is explicit). C2: the ladder's central rule is the record's core novelty — the most likely challenge is not a refutation but a *claim of vacuity* ("the rule forbids only what nobody asserts"), addressed by the practitioner-facing use (it decides what an arithmetic-spectrometer experiment can claim in advance). **P5 gate note (red-team A-2):** the published prose must frame the ladder as methodological discipline, not discovery — "admissible L2→L4 inference" is self-defined, so the rule is a pre-commitment, not a test; the honest framing is pre-registered here. C3: a twelfth error, if found, is expected and survivable (pre-registered). C4: the highest-probability failure point (prose discipline) — the P5 gate list carries the strip requirements, now including the A-3 wording fix ("prevents propagation," not "readers copy").
- **Stages 4–8 — scenario forecast.** (i) *Reception risk (navel-gazing charge):* the external literature is correct and current (two JHEP 2025 papers); the record's hazard is framing, not facts — mitigated by the triage's S1 positioning and the M-3 remediation. (ii) *Currency risk:* the JHEP papers evolve; the record cites their v1 status (noted in external-verification evidence). (iii) *Lineage risk:* RES.030's own artifact (zero cache precision) is a data-quality note this record carries — the P6-era fix belongs to RES.030, not RES.031. (iv) *Opportunity:* the record is the first corrected reference for an actively-used construction; the practitioner hook is time-sensitive while the JHEP activity is current.

## Stage 9: Practical Applications (MANDATORY)

- **The corrected dictionary is a specification** for an engineered log-prime spectrum emulator (superconducting registers / photonic arrays): mode frequencies ∝ ln p, occupation caps m, readout per §IV formulas — every formula now code-verified rather than asserted.
- **The five-level ladder is a scope statement** a practitioner can use *before* building: the L2-≠-L4 rule decides in advance what a realization claim may consist of (protocol: specified spectrum + counting rule + pre-registered null + pre-registered test) — directly actionable for an experimental proposal.
- **The verification suites are reusable templates**, including the P3 lessons (grid-centered number variance — Palm counts have mean 2∫₀^{L/2}R₂, not L; all-pairs two-point estimator; edge clipping) — the estimator-construction pitfalls are documented in the suite comments and the P3 memory.
- **Data-quality deliverable for downstream users of RES.030:** the deposited zero cache is a coarse approximation (max|err| ≈ 0.38) — quantified, provenance-recorded, not trusted for tight checks. Any downstream computation reusing `riemann-zeros-3000.npy` should re-derive zeros via mpmath.
- **DR5 (P5):** interactive primon-gas partition-function emulator via qwav-demo-kit.

## Stage 10: Counterfactual Backcasting (MANDATORY)

- **World A — record judged navel-gazing or physically empty.** Backcast the decisions that would have produced it: shipping the seed Dictionary without the C3 audit; keeping the "two dialects of the same statistical language" preamble; never holding UIA Q10/Q15; never engaging the JHEP 2025 literature. The actual record blocked each node: the preamble was withdrawn, Q10/Q15 were held in print, the ledger was code-verified, and the external currency evidence is deposited. The remaining exposure is P5 prose — the known weak point.
- **World B — a twelfth C3 error found after publication.** Backcast: it becomes scandal-shaped only if the completeness claim was presented as proven. The record pre-registers the audit-level status of C3; a found twelfth error is a data-quality finding + record update. The counterfactual lesson: the pre-registration is the load-bearing choice, and it is already in §1.2.
- **World C — an admissible L2→L4 inference is exhibited.** Then the ladder's central rule breaks, and the record's reason-for-existing (UIA Q15) collapses to "erratum." Backcast: the record would have over-claimed by asserting the rule as a theorem of physics rather than a methodological stance. The actual record states the rule as the interpretive architecture's spine — its falsifiability is precisely the point, and the negative branch (the record becomes an erratum-scoped consolidation) remains publishable.

## Decision threshold (M4)

Red team delivered; HARD findings remediated in-turn or pre-registered; the UIA re-audit records the P1→P4 deltas. Anything found here that survives remediation is carried into P5 as a gate item, never silently dropped.
