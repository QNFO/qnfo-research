# Toy-Model Suite Deposit — Publication Decision (P7)

**WBS:** QNFO.RES.009.P7 · **Date:** 2026-08-14 · **Status:** DECISION MADE — separate Zenodo deposit
**Scope:** publication vehicle for the T4–T7 toy-model suite + disciplined companion essay.

## PUBLICATION RECORD (2026-08-15, executed)

### Version chain (concept 10.5281/zenodo.21940821)

| Version | DOI | State | Content |
|---|---|---|---|
| v1.0 | 10.5281/zenodo.21940822 | published | 18 files (essay + T4–T7 notebooks + docs + registry) |
| v1.1 | 10.5281/zenodo.21941122 | published — **SUPERSEDED** | 4 files only (partial first newversion attempt; ignore) |
| v1.2 | 10.5281/zenodo.21941145 | published — **COMPLETE corrected release** | 19 files: remediated T5/T6 (functional H2/H3/G3, computed eigenvalues), T1/T2 notebook added, README updated |
| v1.3 | 10.5281/zenodo.21941150 | published — **CURRENT** | v1.2 + essay frontmatter DOI fixed to its own DOI (NEWVERSION-FRONTMATTER-CARRYOVER-1 remediation) |

- **Record (current):** https://zenodo.org/records/21941150 — 19 files, license cc-by-4.0, 9 keywords, community qnfo, related_identifiers (GitHub isSupplementTo + paper DOI references); verified in-record: essay frontmatter carries its own DOI; t5 notebook contains the functional H2 test.
- **Live checks:** doi.org/10.5281/zenodo.21941150 → HTTP 200; zenodo.org/records/21941150 → HTTP 200.
- **papers.qnfo.org:** https://papers.qnfo.org/papers/from-distinction-to-dissipation/ → HTTP 200 (qa-ux-battery 1/1 PASS).
- **D1 living-paper:** zenodo_doi 10.5281/zenodo.21941150, zenodo_url/pdf_url → v1.3 record, html_url → concept 21940821 — read-back verified.
- **R2 archive:** releases:qnfo-releases/releases/2026/08/from-distinction-to-dissipation/ — rclone check 0 differences (19 files).
- **Git release tree:** `releases/2026/08/from-distinction-to-dissipation/` (19 files, incl. corrected T5/T6 + T1/T2 notebook).

**Pipeline notes (kaizen candidates):**
1. Deposit-API `related_identifiers` MUST use the legacy shape `{"relation": "isSupplementTo", "identifier": ..., "scheme": "url"}` — the `relation_type` key (string OR object form) crashes the deposit API with HTTP 500 (verified 6+ variants, 5-retry backoff). The records API accepts `{"relation_type": {"id": "issupplementto"}}` but SILENTLY DROPS license/keywords/communities (ZENODO-RECORDS-API-DROPS-METADATA-1 confirmed live).
2. D1 body_html must stay under 1 MB (SQLITE_TOOBIG) — store the pandoc HTML with the CDN MathJax script tag, NOT the 2.3 MB inlined variant.
3. Test deposition 21940863 (records-API bisect draft) deleted (HTTP 204).

## Decision record

**Question:** should the T4–T7 toy-model suite (companion essay + four executable
notebooks) be published as (a) a separate Zenodo deposit, or (b) attached to the paper
v1.1 newversion?

**Decision: SEPARATE Zenodo deposit.** Rationale:
1. **v1.1 is a correction vehicle.** Its scope is the §5/F2 abelian-pair amendment and
   references.bib remediation (concurrent session's cycle). The toy-model suite is a
   research expansion, not a correction — mixing them muddies both artifacts.
2. **No Zenodo collision.** The concurrent session owns the v1.1 newversion; a second
   writer on the same deposit risks NEWVERSION-FRONTMATTER-CARRYOVER-1-class races.
3. **The suite is a coherent standalone contribution:** one arc (statistics from
   syntactic exchange → boundary cost → capacity ceiling → second-law-gated braids),
   four executable models, honest [TOY MODEL — SYNTACTIC] / [NOT YET EVIDENCE] labels,
   and a disciplinary story (three idealizations caught by pre-registered tests in T7
   alone — the suite is itself a case study in pre-registration discipline).

## Deposit bundle manifest

| File | Role |
|---|---|
| `docs/companion-essay-draft.md` | Flagship essay (disciplined register; [RETRODICTION]/[NOT YET EVIDENCE]/[EXTRAPOLATION] labels) |
| `artifacts/notebooks/t4-toy-model.md` + `.py` | Statistics from syntactic exchange (P1, REG-009-001) |
| `artifacts/notebooks/t5-boundary-cost-model.md` + `.py` | Boundary cost (FQ1, REG-009-002) |
| `artifacts/notebooks/t6-capacity-bound.md` + `.py` | Capacity ceiling (FQ1 formal, REG-009-003) |
| `artifacts/notebooks/t7-second-law-gated-braid.md` + `.py` | Second-law-gated braids (FQ3, REG-009-004; exact-chain version) |
| `docs/fq3-irreversibility-mapping.md` | FQ3 mapping (arrow at the erasure gate) |
| `RESEARCH-CONTINUITY-REGISTRY.md` | Pre-registration scaffold + falsifiability ledger |
| README (generated at deposit time) | Bundle map + relationship to the published paper (DOI 10.5281/zenodo.21938971) + the three-deep-inquiry-note provenance |

## Proposed metadata (for the CMD PUBLISH cycle)

- **Title:** "From Distinction to Dissipation: Companion Essay and Executable Toy-Model
  Suite for the Boson/Fermion Distinction Program" (final title decision at publish).
- **Description:** the suite answers the deep-inquiry question "what is the cost of
  drawing a boundary?" at toy-model level: the draw is free (reversible), the upkeep is
  not; capacity ceiling floor(ΔS/k_B ln 2); implementable braid set = f(p, P, T) with
  inversion toll 2 kT ln 2. All claims labeled [TOY MODEL — SYNTACTIC] / [NOT YET
  EVIDENCE]; no physical derivation is claimed.
- **License:** cc-by-4.0. **Community:** qnfo. **Language:** eng.
- **Related identifiers (isSupplementTo):** https://github.com/QNFO/qnfo-research/tree/res/paper/spin-statistics-distinction
  (PUBLICATION-SOURCE-COMPLETENESS-1 shape) + the paper DOI 10.5281/zenodo.21938971.

## Publish checklist (for the CMD PUBLISH cycle)

**Pre-publish verification record (2026-08-14, second pass — COMPLETE):**

| Item | Result | Evidence |
|---|---|---|
| Citation audit | **4/6 verified live** | Pauli ✓ (Crossref: PR 58, 716–722, 1940-10-15, exact match); Quni-Gudzinas 2026 ✓ (Zenodo API: state=done v1.0); Jabs quant-ph/0311078 ✓ (S2: "Spin, statistics, and the spinor ambiguity", 2003); Lev hep-th/0212178 ✓ (S2: "Reduced Spin-Statistics Theorem", 2002) |
| Citation audit — pending | 2 to re-verify at publish | Marletto–Vedral arXiv:2112.03392 [S2/arXiv rate-limited this session — standard record]; Spencer-Brown 1969 [book, no DOI; OpenLibrary timed out — standard record] |
| Notebook re-runs | **4/4 PASS** | T4 rc=0 no FAIL; T5 "H1/H2/H3 all PASS"; T6 "G1/G2/G3/D all PASS"; T7 "T7-1/T7-2/T7-3 all PASS" (2026-08-14 second pass) |
| BP gates on essay | **PASS** | INTERNAL-REF-1: no WBS codes/program slugs; AI-filler banned words: none; bare Unicode math: none; language: 0 non-Latin chars (English-only); length 6009 chars / 120 lines |

- [x] Verify the essay's four references (citation audit above; re-verify the two
      pending entries — Marletto–Vedral arXiv:2112.03392, Spencer-Brown 1969 — at
      publish time).
- [x] Re-run all four notebooks one final time (pinned outputs) — PASS, second pass
      recorded above.
- [x] BP-1..BP-10 gates (research skill §P5): language gate, no internal WBS codes in
      the essay body (INTERNAL-REF-1), AI-quality gate — PASS.
- [ ] README generation + GitHub related_identifiers (branch URL).
- [ ] Zenodo new deposit (not a newversion of the paper — separate concept) → publish →
      verify records API + DataCite + OpenAIRE.
- [ ] Registry §7 log entry; memory closeout.
