# Journal Submission Strategy — QNFO.RES.005 Prime Valuation Depth (P7, HARD leg)

**Date:** 2026-08-13 · **Phase:** P7 · **WBS:** QNFO.RES.005.P7.T2
**Protocol:** research v2.88 Phase 7 Journal Submission (HARD — the peer-review leg; arXiv is not a guaranteed leg for this author)

## 1. Position

- **Published:** Zenodo DOI 10.5281/zenodo.21918032 (v0.1-draft, cc-by-nc-sa-4.0), DataCite findable, OpenAlex auto-indexing via Zenodo (author profile A5133504808).
- **Peer-review leg:** NOT yet submitted. This artifact defines the target journal, cover-letter protocol, and readiness gates.
- **Nature of the paper:** interpretive/structural reading (explicitly labeled MAP claims with KIF-60 [RETRODICTION] caps). The strongest peer-review asset is the **pre-registered falsifiability conditions** (REG-RES004-001/002, RESEARCH-CONTINUITY-REGISTRY.md).

## 2. Journal shortlist (independent-researcher friendly)

| Rank | Journal | Section/Scope | Fit rationale | OA |
|:-----|:--------|:--------------|:--------------|:---|
| ★★★★★ | Frontiers in Physics | Quantum Computing & Technologies; Mathematical Physics | Same venue family as cited qudit reviews; broad scope covers foundations + math-physics; independent-researcher friendly | Gold OA |
| ★★★★ | Quantum (Vienna) | quantum foundations, quantum information | Diamond OA; strong foundations community; no APC; accepts interpretive/foundational work with rigor | Diamond OA |
| ★★★ | EPJ Quantum Technology | quantum tech foundations | Preprint-friendly; shorter review cycles | Hybrid |
| ★★★ | AVS Quantum Science | QIS | Peer-reviewed, broad QIS | Hybrid |
| ★★ | Entropy (MDPI) | quantum foundations / information theory | Fast; OA; but MDPI reputation trade-off — use only as fallback | Gold OA |

**Primary target:** Frontiers in Physics — the paper's honest structural-reading framing (MAP/TERRITORY labels, falsifiability conditions, explicit retrodiction cap) matches Frontiers' openness to carefully-scoped foundational work and its mathematical-physics section. **Secondary:** Quantum (diamond OA, strong foundations refereeing).

## 3. Cover-letter protocol (from research v2.88)

1. **Lead with the pre-registered falsifiability/disconfirmation condition** — the paper's strongest asset:
   - Statement 4 falsifiability: the structural no-cloning reading is disconfirmed if it yields no explanatory content beyond the standard linearity proof.
   - Pre-registration scaffolds REG-RES004-001 (correspondence non-vacuity, 2027) and REG-RES004-002 (adelic delta or retirement, 2028) with commit timestamps.
2. **State independence + ORCID** (0009-0002-4317-5604), QNFO Research Collective affiliation.
3. **Explicitly invite adversarial validation** — the paper already documents 5-adversary red-team + 4 applied fixes; invite reviewers to test the correspondence non-vacuity.
4. **Keep [speculative]/[MAP] labels** — signal calibration; do not strip.
5. **Post-acceptance:** newversion with `related_identifiers: isPublishedIn` (journal DOI).

## 4. Readiness gates before submission (do not submit before all pass)

| Gate | Check | Status |
|:-----|:------|:-------|
| R1 | Publication Language Gate clean (INTERNAL-REF-1: zero WBS codes in body) | ✅ PASS (P5) |
| R2 | MAP/TERRITORY labels + falsifiability conditions present | ✅ PASS (P5 gate script) |
| R3 | References 17/17 Crossref-verified | ✅ PASS (P3.AUTHOR-GATE) |
| R4 | Zenodo DOI resolves + DataCite findable | ✅ PASS (L1/L2 closeout) |
| R5 | Continuity registry pre-registration scaffolds with timestamps | ✅ PASS (P4) |
| R6 | Copyedit pass (Professional Publication Standards) | ⏳ PENDING — run before submit |
| R7 | Journal-specific formatting (Frontiers template) | ⏳ PENDING — only after shortlist confirmation |

## 5. Submission workflow (autonomous when triggered)

1. Confirm R1–R5 (already PASS) → run R6 copyedit pass → prepare Frontiers manuscript (md → docx or LaTeX per venue).
2. Compose cover letter per §3; include DOI, ORCID, pre-registration references.
3. Submit via journal portal (browser session) — log submission ID + date to `artifacts/submission-log.md`.
4. Set follow-up: 30-day check, respond to reviews with the calibration register as evidence of honest labeling.
5. On acceptance: Zenodo newversion with isPublishedIn + D1/KG update.

## 6. Decision

**Submit to Frontiers in Physics (Quantum Computing & Technologies) when the user triggers the journal leg** — all readiness gates R1–R5 already PASS; R6/R7 are mechanical. This artifact documents the strategy so the leg can execute autonomously on a later CMD.

## 7. Notes

- The reviewer (UvVgwFVWi64PmgGa6kmNH) audit is resolved (WBS renumbering); the paper body is untouched by the renumbering (zero WBS codes), so the submitted version is identical to the published v0.1.
- The adelic frontier (FQ4) and correspondence non-vacuity (FQ1) are explicitly NOT submission blockers — they are tracked as open research items with deadlines (2027/2028).
