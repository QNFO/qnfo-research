# Post-Publication Adversarial Analysis — QNFO.RES.021 P7 (2026-08-21)

**Audited artifact:** the LOCKED draft (finite-distinction-quantum-mechanics.md v1.0.0)
on branch `res/paper/finite-distinction-quantum-mechanics` at 7d1f8b3, together with
the verification artifacts (artifacts/verification/), the lock record (PROJECT-PLAN
§2), and the audit chain (UIA P0 + P6, falsifier register P0–P6). READ-ONLY: no
audited file was modified; this report is the gate-mandated aggregation.

**Audit seed (P6 UIA Q15):** "Does the published record make the conjecture-grade of
the emergence claim as legible as the lock makes its wording immutable?"

**Dispatch:** 3 reviewer slots (Accuracy / Completeness / Dependency) were spawned
2026-08-21. All three STALLED mid-run (~1.5 min of active work, then frozen
effect-states; the Completeness and Dependency children additionally called the
write-classified `update_plan` tool — the known stall signature of this environment,
REDTEAM-SUBAGENT-GATE-STALL-1). Per the gate's fallback, the direct 5-adversary
parent audit below is authoritative; the stalled children remain in the delegation
registry and any late completions are superseded by this recorded verdict.

---

## Direct 5-adversary audit

### 1. Accuracy — CLEAN (0 findings)

- Every number in the draft's §9 Results block matches the deposited run log and
  results JSON exactly: σ(N) exponent −0.88, symplecticity-defect exponent −1.00,
  Born deviation −1.09, clock error −2.00; V2 0/262,144 ultrametric violations with
  83,328 Archimedean-control violations; σ(2¹⁴) = 6.7×10⁻⁶; V6 3.15×10⁻⁸ at n =
  1024; runtime 25.9 s (25.851 in log); CPython 3.12.10; seed 20260821.
- The locked claim (PROJECT-PLAN §2) embeds the SAME exponents (−0.88/−1.00) and
  the seed 20260821.
- Frontmatter: `version: 1.0.0`, `locked: 2026-08-21 (P6; tag v1.0.0-phase6-res021)`,
  `doi: PENDING-ZENODO` (correct pre-P8 placeholder state).
- Abstract and §1 use the restated phrasing ("uncountable precision is unphysical;
  computable depth and p-adic valuation remain physically real"); the prohibited P0
  wording ("the Archimedean continuum is unphysical as an ontology") appears nowhere
  in the draft.
- 37 numbered references ↔ 37 bib entries, bidirectional (BIB-ORPHAN-1 clean); all
  DOIs/arXiv IDs live-verified (P3 full enumeration + P4 addendum), zero fabricated
  attributions.

### 2. Completeness — 1 SOFT

**Seed question answered: YES — the conjecture-grade is legible.** The draft's §2
premise-depth table lists the L3 conjectures explicitly; §5 opens "The central
conjecture of this paper"; §6 opens "The second conjecture"; §11 grades the record as
identity / dictionary / conjecture; the P6 falsifier-register entry states the lock
freezes the WORDING, not the grades. The legibility of the conjecture-grade is
therefore at least as strong as the immutability of the wording.

- SOFT-1: §7 (relational time) frames H-TIME as "The prediction (F5)" without the
  word "conjecture". The grade is carried by the §2 L3 row and §11, so no HARD
  defect — but a uniform one-word label in §7 would make the record airtight.
- All publication-gate sections verified present: premise-depth disclosure (L0–L3),
  F1–F5, verification table V1–V6 with results + executed acceptance criteria,
  practitioner section (4 deliverables), reproducibility statement
  (artifacts/verification/README.md), grading ladder.
- The γ = 1/N model-assumption admission is present in §9 prose (P6 UIA Q12/Q13
  actionable item executed).
- P8 deposit completeness: citation-audit.md, references.bib, verification source +
  passing log + JSON, P0 UIA, P6 UIA, hypothesis cards, PROJECT-PLAN — all present
  on-branch.

### 3. Dependency — CLEAN (0 findings)

- Amendment trail complete and non-circular: P0 wording preserved at tag
  v0.1-phase0-res021 / commit 3027054 → P1 grade re-mapping (PROJECT-PLAN §9) → P6
  restatement at 7d1f8b3 / tag v1.0.0-phase6-res021; the lock record cites every leg
  consistently.
- UIA Q15 seed chain intact: P0 seed ("is the large-distinction limit itself
  continuous?") → answered in draft §5 ("UIA Q15 seed (answered here; red-team H-2
  remediation)") → P6 seed (conjecture-grade legibility) → registered for this P7
  audit and answered above.
- Falsifier register carries dated entries for P0, P2, P4, P5, P6 gates; no
  contradictions between them; the P5 entry (no falsifier triggered) is consistent
  with the deposited 5/5 PASS log.
- Internal cross-references (§2→§8→§9→§10 chains; [n] citations ↔ References list)
  resolve; verification evidence (script + log + JSON) is on-branch.

### 4. Novelty — HOLD

G1 (entropy-Hessian → unitarity emergence with finite-N predictions) remains
uncovered in the corpus after 17 sweep formulations across three cycles; external
anchors (Gisin, PBR, Hardy, Aaronson, Vedral, RTV, Luce) constrain but do not
pre-empt. The P5 program supplies the novel finite-N content (the four exponents).
Novelty claim: HOLD at conjecture grade.

### 5. Status — 1 registered obligation

- Branch head 7d1f8b3 and tag v1.0.0-phase6-res021 both ls-remote verified;
  program_registry P6 / current_version 1.0.0 (read-back verified).
- **P7.2 obligation registered (HARD-gate compliance):** the POST-PUBLICATION
  ADVERSARIAL ANALYSIS GATE requires the adversarial audit to run against the
  PUBLISHED artifact. This P7 pass audits the locked draft (pre-publication). After
  P8 publishes the Zenodo record, a SECOND pass (P7.2) MUST audit the published
  record + its distribution state (R2 mirror, D1/KG, program_registry re-point)
  before the program closes. P8 MUST NOT be skipped ahead of that obligation.

---

## Aggregate verdict

**0 HARD, 1 SOFT (SOFT-1: §7 conjecture-label uniformity), 1 registered obligation
(P7.2 post-publish re-audit). Zero integrity findings: no fabricated citations, no
claim inflation, no dangling references, no audit-chain breaks. The record answers
its own seed question affirmatively: the conjecture-grade is as legible as the lock
is immutable.**

Remediation plan: SOFT-1 is a one-word fix executed at P8's pre-publish pass (§7:
"The prediction (F5)" → "The conjecture (F5)"); P7.2 is scheduled immediately after
the P8 publish as a read-only pass against the published record.
