# P7 Post-Publication Adversarial Audit — QNFO.RES.021 (2026-08-21)

**Target:** locked draft v1.0.0 (`finite-distinction-quantum-mechanics.md`) +
`artifacts/verification/` (script, run log, results JSON, README) on branch
`res/paper/finite-distinction-quantum-mechanics`, head `7d1f8b3`.
**Mode:** READ-ONLY (no modification of the published artifact; this report is the
P7 deliverable per PROJECT-PLAN §4).
**Method:** 3 reviewer subagents dispatched (Accuracy / Completeness / Dependency,
read-only instructions). All three remained `queued` with no child session started
through a 105 s bounded wait (SUBAGENT-SLOT-FAILURE-1 environment pattern). Per the
CMD RED TEAM fallback protocol, the **direct parent-agent 5-adversary audit is
authoritative**; every finding below carries file-level evidence read this session.
**Seed:** the P6 UIA Q15 seed question — "Does the published record make the
conjecture-grade of the emergence claim as legible as the lock makes its wording
immutable?" — is answered in H-3.

---

## Verdict: 3 HARD · 5 SOFT · 0 DESIGN

## HARD findings

### H-1 — §5's "2-norm and complex structure" test promise has no corresponding check
Draft §5: "The candidate route (**to be tested computationally in the verification
program**) is that the symplectic form of the Hessian, together with the
large-distinction limit, selects the 2-norm and the complex structure."
`artifacts/verification/finite-distinction-verification.py` implements V1–V6; **no
check tests norm selection or complex-structure selection** (V3/V4 test entropy
production + dissipative/reversible current ratio only). COMPUTATIONAL-VERIFICATION-1
("any claim a computer can check MUST be checked in code") makes an explicit
computational-test promise without a check a HARD gap. Remediation (next cycle, P7-
remediation): either (a) add V7 — verify the reversible dynamics' amplitude
representation is exactly 2-norm-preserving while generic L^p-norms drift (trivially
executable on the cyclic-permutation model) — or (b) scope the sentence to what the
program actually tests (the F3 half), keeping the ℂ-selection as the theoretical
target it is (Hardy/Aaronson-level, not executable by this program).

### H-2 — V5 does not implement the §9 V5 row it certifies
§9 row: "Max-entropy weights vs Born frequencies | seeded Monte Carlo, fixed
test-state family | **within ±2σ**, deviation shrinks with N (F4)". The deposited
`v5()`: draws random complex-Gaussian vectors (a test-state family **disconnected
from the V3/V4 flow model**), computes P_born = |Σ_{i<K} ψ_i|² vs P_max = K/N with
**K = 4 fixed** — the measured exponent −1.09 is the trivial K/N concentration of a
single random vector (both quantities scale as 1/N), and **no ±2σ tolerance is ever
computed or reported**. The Born-vs-maxent equivalence *in the N-alternative model*
(the draft §6 claim) is not exercised. Remediation: rewrite V5 to measure outcome
frequencies of the V3/V4 flow's quasi-steady states against the Gibbs (max-entropy)
weights, computing and reporting the binomial ±2σ bound — or amend the §9 row to
describe the deposited construction honestly.

### H-3 — the locked claim says "verified at finite N" where §9 says "model assumption … open" (answer to the P6 Q15 seed: the conjecture-grade is NOT fully legible)
PROJECT-PLAN §2 (locked, ships in the P8 deposit per PUBLICATION-SOURCE-
COMPLETENESS-1): "unitary evolution and superposition emerge as the large-
distinction limit of the entropy-Hessian gradient flow — **verified at finite N by
the computational program** (per-step entropy production exponent −0.88,
symplecticity-defect exponent −1.00, seed 20260821)." Draft §9 (same P6 commit):
"The per-distinction rate structure is a **MODEL assumption, not a derived claim**:
its physical status … **is open**, and the post-publication audit must hold this
paper to that admission." The program verified the *defined model family's*
behavior (the exponents track the imposed γ = 1/N scaling, per the README's own
DESIGN note); "verified at finite N" in the locked claim reads as verification of
the *emergence*. The P6 UIA's own Q15 flagged exactly this risk ("does freezing a
conjecture-grade claim inside a locked core claim quietly promote it by one
grade?") — and the locked wording realized it. The hypothesis-cards P6 entry says
"the emergence claims remain conjecture-grade (L3)" — the claim wording does not
say so. Remediation (next cycle): restate "verified at finite N by the
computational program" → "supported at finite N within the per-distinction model
(exponents −0.88 / −1.00, seed 20260821); physical status of the rate structure
open (§9)" — a material change, so per the lock rule: version bump (v1.0.1) +
UIA delta re-run. (The numbers themselves are verified: results JSON ↔ run log ↔
plan all match.)

## SOFT findings

- **S-1** V1 tests only the uniform simplex point (N = 2, 3). The identity is exact
  and the two constructions (score-definition vs analytic Hessian) are independent,
  but a seeded non-uniform point (e.g., (0.2, 0.3)) would remove the symmetry
  caveat. One-line fix next cycle.
- **S-2** §9 V6 row says "relational-dynamics simulation" — the deposited V6 is a
  single-system discrete-time integrator-error test (2nd-order truncated Taylor vs
  exact propagator); no Page–Wootters/history-state construction. The
  discrete-time-artifact half of F5 is genuinely tested (exponent −2.00); the
  relational half is not. Word-scope the row or extend the check next cycle.
  (The P5 red-team already caught and fixed the earlier vacuous-exact-exponential
  construction — VERIFY-FIX-RERUN-1 honored and documented.)
- **S-3** No paper-specific README: branch-root `README.md` is the qnfo-research
  program-repo aggregation readme; only `artifacts/verification/README.md` exists
  (reproducibility). README-MISSING-ON-PUBLISH-1 applies — create a paper README at
  P8 publish-prep (not a draft modification; P7 read-only constraint unaffected).
- **S-4** V3/V4 measured exponents track the imposed γ = 1/N (σ: −0.88 ≈ −1 + log
  correction; defect: −1.00). The draft §9 admission (added at P6) discloses this;
  recorded here for the audit trail, mitigated not open.
- **S-5** Subagent slot availability: 3/3 reviewers queued without start
  (environment pattern). Direct audit substituted; a follow-up subagent pass is
  recommended on the P7-remediation commit when slots recover.

## Positive verifications (CLEAN dimensions)

- **Prose hygiene:** the draft contains zero occurrences of internal pipeline
  vocabulary (WBS codes, gate names, "seed note", "UIA", hypothesis-card names,
  repo paths) — PUBLICATION-PROSE-GATE-1 and PAPERS-NO-NAVEL-GAZING-1 satisfied
  (grep evidence, this session).
- **S-7 restatement consistency:** the restated claim ("uncountable precision is
  unphysical; computable depth and p-adic valuation remain physically real") is
  consistent across PROJECT-PLAN §2 (lock record + amendment trail), the draft
  (§1/§2/abstract), and the hypothesis-cards P6 gate entry; the frozen P0 wording
  is preserved in git history (tag v0.1-phase0-res021) — the lock is a restatement,
  not a retro-edit.
- **Verification-deposit integrity:** run log ↔ results JSON ↔ README ↔ draft §9
  numbers all agree (F₁₁(½)=4; 0/262,144 vs 83,328 control; −0.88 / −1.00; −1.09;
  −2.00 / 3.15e-08); seed 20260821 and CPython 3.12.10 recorded; single-command
  re-run path present; stdlib-only.
- **Falsifier-liveness:** V2's Archimedean control (83,328 violations vs 0) and
  V3's fixed-γ control (exponent +0.14) prove the checks are non-vacuous.
- **Bib integrity (spot):** 37 entries; top-cited keys [14]/[21]/[15]/[11] all
  cited in-body; no orphan spotted; numbering consistent in the spot-checked
  range. (Full bidirectional pass recommended on the remediation commit — the
  Dependency subagent slot did not start.)
- **Named obstacles present:** Hardy [27], Aaronson [28], PBR [29], semiorders [21],
  underdetermination [23] all appear in §2/§5 where the outline promised them.

## Remediation plan (next cycle — P7-remediation → v1.0.1)

1. H-3 restatement in PROJECT-PLAN §2 (material change ⇒ version bump + UIA delta
   re-run per the lock rule; tag `v1.0.1-...`).
2. H-1: add V7 (2-norm invariance of the reversible amplitude representation) or
   scope the §5 sentence.
3. H-2: rewrite V5 against the flow model with the ±2σ bound reported, or amend the
   §9 row.
4. S-1/S-2 one-line strengthening/word-scoping; S-3 paper README at publish-prep.
5. Re-run the full verification (VERIFY-FIX-RERUN-1: deposit only passing logs),
   then P8 Zenodo publish (source-complete deposit incl. verification artifacts,
   R2 `qnfo-releases` mirror, D1/KG distribution, program_registry re-point).
