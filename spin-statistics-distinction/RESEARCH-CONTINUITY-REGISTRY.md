# RESEARCH CONTINUITY REGISTRY — QNFO.RES.009

**Project:** The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant
**DOI:** 10.5281/zenodo.21938971 (concept 10.5281/zenodo.21938970) · **Branch:** res/paper/spin-statistics-distinction
**Last updated:** 2026-08-14 · **Living document** (maintained with version bumps; not a static paper artifact)

This registry tracks frontier questions, falsifiable predictions, and pre-registration scaffolds raised by the published paper and its 2026-08-14 evening deep-inquiry follow-ups. It is the internal continuity instrument; WBS codes and branch names are permitted here (they are not shipped in the published manuscript).

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|---|---|---|---|---|
| FQ1 | **What is the cost of drawing a boundary?** (Landauer) — the mark calculus treats boundary-drawing as free, but creating a distinction may cost free energy; if so, entropy/energy precede distinction. | CLOSED in ceiling form (toy-model bookkeeping; physical test open — T5→T6, 2026-08-14) | T5 (REG-009-002) + T6 (REG-009-003) EXECUTED: cost applies to non-injective operations (erasure/maintenance/overwrite), NOT the injective act of drawing; capacity ceiling floor(ΔS/k_B ln 2); steady state min(N, P/p); entropy balance verified. Answer: grammar is primitive, capacity to maintain it is thermodynamically priced — dual descriptions, not competitors. Next: T7 (P6) second-law-gated braid implementation. | YES |
| FQ2 | **Can the spin-statistics *connection* (which exchange eigenvalue maps to which spin) be derived from the mark calculus, and is the minimal extra structure exactly Lorentz + microcausality?** | SHARPENED (paper §5 boundary) | T1/T2 DiLL full check COMPLETE (2026-08-14, `artifacts/notebooks/t1-t2-dill-full-check.md`). Finding: minimal extra structure = {self-duality, abelian-pair, symmetric braiding} for statistics + {Lorentz, microcausality, positive energy} for the connection — one postulate wider than §5 states. Next: v1.2 amendment DRAFTED (`docs/v1.2-amendment-draft.md`, 2026-08-15; `v1.1-amendment-draft.md` SUPERSEDED). NOTE: v1.1 (10.5281/zenodo.21939493) is ALREADY published 2026-08-14 with references.bib remediation only — the abelian-pair amendment targets v1.2; publish pending (CMD PUBLISH). | YES |
| FQ3 | **Does the braid-derived framework recover time-irreversibility and measurement?** (the zero-temperature idealization gap; note _26226215159 Q3/Q11) | MAPPED at toy-model level (T7, 2026-08-14) | T7 EXECUTED (REG-009-004): implementable braid set = f(p, P, T) — per-exchange success x11 (exact discrete-chain stationary value), persistence c, L_max grows with power / shrinks with noise; inversion toll = 2 kT ln2; the arrow is at the ACCESS level, the algebra stays symmetric. Next: P7 publication decision for the T4–T7 toy-model suite. | YES |

**Provenance note (deep-inquiry sources, 2026-08-14):** Obsidian vault `D:\Obsidian\notes\v1\2026\08\14\` — `_26226214708.md` (thesis elaboration), `_26226215159.md` (15-question deep-inquiry audit), `_26226215536.md` (boundary-cost inversion).

---

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|---|---|---|---|---|
| P1 | A discrete syntactic exchange model (two indistinguishable tokens + "draw boundary" operation) reproduces the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ and the ±1 collapse (3D semantics) vs fractional phase (2D semantics) *without a hand-imposed sign*. | 2026-08-14 | `artifacts/notebooks/t4-toy-model.py` | If the sign must be hardcoded externally rather than emerging from the syntactic rules. |
| P2 | No stable, local, relativistic 3+1D excitation exists with exchange phase η ≠ e^{2πis} (e.g., a spin-½ boson or spin-0 fermion). | ongoing | any experimental QFT survey | Observation of such a particle. |
| P3 | The mark calculus reproduces the two 1D characters of S_n from distinction + compact closure + involutive braiding alone. | 2026-12-14 | T1/T2 full derivation | Impossibility proof (additional postulate required). **2026-08-14 check result:** holds **iff** the abelian-pair postulate is added; Yang–Baxter forces phase uniformity across pairs (no extra postulate needed for that). Restate P3 postulate set accordingly. |

---

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- **FQ1 disconfirmed if:** a boundary can be *erased or maintained* with zero free-energy cost in a physical system (Landauer violated), OR the capacity ceiling (floor(ΔS/k_B ln 2); steady state D* = min(N, P/p)) predicts nothing distinguishable. Note: a boundary drawn with zero *reversible* cost is NOT a disconfirmation — T5/T6 established that the draw is free and the upkeep is not (sharpened formulation, 2026-08-14).
- **FQ2 disconfirmed if:** the minimal extra structure is shown to be strictly more than Lorentz + microcausality.
- **FQ3 disconfirmed if:** a braid-derived dynamics model recovers a preferred time direction and measurement collapse with no added postulate.

---

## 4. PRE-REGISTRATION SCAFFOLDS

**REG-009-001 — Toy-model (P1).**
- **Hypothesis:** braid relations + dimensional collapse emerge from discrete syntactic exchange with no hand-imposed sign.
- **Falsification:** the sign must be hardcoded.
- **Data:** `artifacts/notebooks/t4-toy-model.py` output (run 2026-08-14).
- **Deadline:** 2026-08-14 (executed same-day; see §7).

**REG-009-002 — Boundary-cost model (T5, FQ1).**
- **Hypothesis:** H1 capacity bound floor(B/c); H2 write/erase asymmetry (reversible draw costs 0, erasure costs kT ln 2); H3 grammar invariance (budget gates capacity, never statistics).
- **Falsification:** H2 fails if a reversible write shows nonzero minimum cost; H3 fails if a budget term enters the exchange eigenvalues. H1 is definitional — demonstration only, no evidential weight [KIF-60].
- **Data:** `artifacts/notebooks/t5-boundary-cost-model.py` output (run 2026-08-14).
- **Deadline:** 2026-08-14 (executed same-day; see §7).

**REG-009-003 — Capacity ceiling (T6, FQ1 formal).**
- **Hypothesis:** G1 ceiling floor(ΔS / k_B ln 2); G2 steady state min(N, P/p) with entropy balance (fixes == reservoir gain); G3 statistics unchanged at the ceiling.
- **Falsification:** G2a fails if the steady state deviates from min(N, P/p) beyond tolerance; G2b fails if fixes ≠ reservoir gain; G3 fails if a budget term enters the exchange eigenvalues. G1 is definitional — demonstration only [KIF-60].
- **Data:** `artifacts/notebooks/t6-capacity-bound.py` output (run 2026-08-14; first run FAILED G2a by design — simulation bug caught by the pre-registered test, fixed, re-run PASS — see notebook "Modeling note").
- **Deadline:** 2026-08-14 (executed same-day; see §7).

**REG-009-004 — Second-law-gated braid implementation (T7, FQ3 full-derivation candidate).**
- **Hypothesis:** T7-1 shared-channel steady state x11 (exact discrete-chain stationary value, see notebook; NOT the rate-approximation 1/(1+2a+2a²)), persistence c = (1−p)² + 2p(1−p)·min(1,P), word success x11·c^(L−1); T7-2 L_max(ε) monotonic in P/p; T7-3 inversion toll = 2 kT ln2.
- **Falsification:** T7-1 fails if sim deviates from x11·c^(L−1) beyond tolerance; T7-2 fails if L_max is non-monotonic or empirical deviates > 1; T7-3 fails if the toll ≠ 2 kT ln2. NOTE: THREE idealizations were rejected by the tests during execution: (1) independent channels; (2) independent steps; (3) the rate-equation approximation of x11 (rejected by the 2000-trial tightness re-run, +2.9..+5.0σ; exact chain reproduces sim within ±2.5σ on 15/15 checks). See notebook "Integrity records".
- **Data:** `artifacts/notebooks/t7-second-law-gated-braid.py` output (run 2026-08-14; exact-chain version).
- **Deadline:** 2026-08-14 (executed same-day; see §7).

---

## 5. CALIBRATION REGISTER

| Prediction | Strength | Status |
|---|---|---|
| [CHECK: 2026-09-14] FQ1 Landauer cost formalized | WEAK | PENDING |
| [CHECK: 2026-12-14] F2 derivation executed or impossibility shown | MEDIUM | PENDING |
| [CHECK: 2027-06-14] ≥1 external citation of the invariant formulation | WEAK | PENDING |

---

## 6. NEXT ACTIONS (Prioritized)

- **P0:** T4 toy-model — DONE (§7).
- **P1:** T1/T2 DiLL full check — DONE 2026-08-14 (`artifacts/notebooks/t1-t2-dill-full-check.md`).
- **P2:** Disciplined companion essay — draft committed (`docs/companion-essay-draft.md`); publication decision pending.
- **P3:** v1.2 amendment publish (CMD PUBLISH): apply `docs/v1.2-amendment-draft.md` (abelian-pair in §5/F2 + D–R 1990) as a newversion of **v1.1 (10.5281/zenodo.21939493)** per NEWVERSION-FRONTMATTER-CARRYOVER-1. NOTE: v1.1 was published 2026-08-14 with the references.bib remediation only; `docs/v1.1-amendment-draft.md` is SUPERSEDED (removed).
- **P4:** FQ1 capacity ceiling — DONE 2026-08-14 (T6, REG-009-003; `artifacts/notebooks/t6-capacity-bound.py`).
- **P5:** FQ3 irreversibility mapping — SEEDED 2026-08-14 (`docs/fq3-irreversibility-mapping.md`).
- **P6:** T7 second-law-gated braid implementation — DONE 2026-08-14 (`artifacts/notebooks/t7-second-law-gated-braid.py`; FQ3 MAPPED at toy-model level).
- **P7:** Publication decision for the T4–T7 toy-model suite (companion essay + four notebooks): separate Zenodo deposit vs. attach to v1.1. External-scrutiny candidate: x11/c run-length structure as a falsifiable anyon-fidelity prediction.

---

## 7. SESSION LOG

- **2026-08-14 (P9):** Registry created from the red-team audit of the evening deep-inquiry notes (findings S-1..S-10, D-1..D-2). T4 toy-model written and executed (P1 verified: braid relations + ±1 collapse + fractional-phase anyon mode all reproduced syntactically). Companion-essay draft committed with the labeling discipline restored.

- **2026-08-14 (P1 continuation):** T1/T2 DiLL full check COMPLETE — `artifacts/notebooks/t1-t2-dill-full-check.md`. Results: (1) both !_S and !_Λ verified as DiLL exponentials (dereliction/digging/promotion/contraction/weakening/Seely); (2) parity identification Sym_gr(A_odd) ≅ Λ(A_odd) — the two exponentials are two branches of one construction; (3) ribbon identity gives θ_M = η·id for abelian self-dual M; (4) Yang–Baxter forces phase uniformity across pairs (η_1 = η_2 derivation); (5) FINDING: abelian-pair postulate required to exclude parastatistics-class sectors — §5 boundary is one postulate wider than stated; F2/P3 restated accordingly. Self-verification caught + fixed one eigenspace-label error (odd-mark parity swap) and one citation correction (Greenberg–Messiah 1965). Also re-ran t4-toy-model.py this session: all checks True (P1 re-verified). Next: decide v1.1 (amend §5 + F2), then FQ1 boundary-cost term (T5), then FQ3 irreversibility mapping.

- **2026-08-14 (P9 continuation, T5):** FQ1 boundary-cost model EXECUTED — H1/H2/H3 all PASS (REG-009-002). Key result: the Landauer inversion (Note 3 Layer 1) holds ONLY for erasure/maintenance, NOT for reversible drawing → distinction (grammar) and dissipation (resource) are DUAL descriptions; the second law prices the mark's upkeep, it does not dethrone it. v1.1 amendment DRAFTED (decision YES: abelian-pair postulate in §5/F2) — Zenodo newversion publish pending. Next: CMD PUBLISH v1.1; T6 capacity bound; FQ3 irreversibility mapping.

- **2026-08-14 (P9 continuation, T6 + FQ3 seed):** T6 capacity ceiling EXECUTED — G1/G2/G3 all PASS (REG-009-003; first G2a run FAILED by design — simulation state-reset bug caught by the pre-registered test, fixed, re-run PASS, documented in notebook). FQ1 CLOSED in ceiling form: ceiling floor(ΔS/k_B ln 2), steady state min(N, P/p), entropy balance verified; grammar untouched at the ceiling. FQ3 SEEDED (`docs/fq3-irreversibility-mapping.md`): the arrow enters at the erasure gate; idealization gap = erasure-cost gap. Next: P6 T7 second-law-gated braid implementation; CMD PUBLISH v1.1.

- **2026-08-14 (P9 continuation, T7):** T7 second-law-gated braid implementation EXECUTED — T7-1/T7-2/T7-3 all PASS (REG-009-004). The implementable braid set is f(p, P, T): per-exchange success x11 (exact discrete-chain stationary value), persistence c, L_max grows with power/shrinks with noise, inversion toll = 2 kT ln2. THREE idealizations were rejected by the tests and sharpened: (1) independent channels; (2) independent steps; (3) the rate-equation approximation of x11 — rejected by the 2000-trial tightness re-run (+2.9..+5.0σ across seeds; exact chain reproduces sim within ±2.5σ on 15/15 checks; committed version uses the exact chain). FQ3: SEEDED → MAPPED at toy-model level — the arrow is at the ACCESS level, the algebra stays symmetric. Next: P7 publication decision for the T4–T7 suite; CMD PUBLISH v1.1.

- **2026-08-14 (P9 continuation, P7 verification):** Deposit pre-publish verification COMPLETE (recorded in `docs/toy-model-suite-deposit.md`): citation audit 4/6 verified live (Pauli via Crossref PR 58 716-722 exact; Quni-Gudzinas DOI via Zenodo API state=done v1.0; Jabs quant-ph/0311078 + Lev hep-th/0212178 via Semantic Scholar); Marletto-Vedral 2112.03392 + Spencer-Brown 1969 marked re-verify-at-publish (S2/arXiv rate-limited, OpenLibrary timeout — no guessing); all four notebooks re-run PASS (T4/T5/T6/T7 rc=0, no FAIL lines); BP gates on the essay PASS (INTERNAL-REF-1 clean, no banned filler, no bare unicode math, English-only). Next: CMD PUBLISH the toy-model suite (README + deposit steps remain, per the deposit doc checklist).

- **2026-08-15 (P8 PUBLISH — toy-model suite):** PUBLISHED — DOI **10.5281/zenodo.21940822** (concept 21940821). 18 files (essay md/html/pdf, README, references.bib, citation-audit, 4 notebooks ×2, fq3 doc, deposit doc, registry, PROJECT-PLAN), license cc-by-4.0, community qnfo, GitHub isSupplementTo + paper-DOI references. Verified: doi.org HEAD 200, zenodo.org records 200, D1 living-paper row (body_md + serve-HTML <1MB), papers.qnfo.org/papers/from-distinction-to-dissipation/ 200, R2 qnfo-releases archive 0 differences. Pipeline lessons: deposit-API related_identifiers needs the LEGACY `relation` key (relation_type → 500, verified); D1 body_html < 1MB (SQLITE_TOOBIG). Build: pandoc → MathJax SVG inline → puppeteer-core/Edge → 116 KB PDF; TITLE-DUPLICATION-1 gate PASS (essay body H1 demoted to H2). Test deposition 21940863 deleted.

- **2026-08-15 (P9 RED-TEAM REMEDIATION cycle):** Post-publication red team (CMD RED TEAM SUB) surfaced 3 HARD findings, all remediated this cycle: (1) v1.1 ALREADY PUBLISHED (21939493, references.bib-only) → amendment re-versioned to **v1.2** (`docs/v1.2-amendment-draft.md`; `v1.1-amendment-draft.md` removed; registry §1/§6 updated); (2) T5 H2/H3 disconfirmation conditions were non-functional → **re-implemented as functional tests** (injectivity-priced Landauer rule with 5 asserted cases; exchange eigenvalues COMPUTED via characteristic polynomial + eigenspace nullities; budget-independence demonstrated) + Bit semantics clarified (None = blank reference state); (3) T6 G3 assertion-style → eigenvalues now computed (dim(+1)=3, dim(−1)=3). Suite version chain published: v1.1 partial (21941122, SUPERSEDED) → **v1.2 complete (21941145)** with the corrected notebooks + T1/T2 notebook + updated README → **v1.3 (21941150)** essay-frontmatter-DOI fix (NEWVERSION-FRONTMATTER-CARRYOVER-1). FQ1 Status cell now carries "(toy-model bookkeeping; physical test open)"; provenance note added for the deep-inquiry note IDs. papers.qnfo.org page passed qa-ux-battery 1/1; R2 re-synced (19 files, 0 differences).

- **2026-08-15 (P9 PUBLISH — paper v1.2/v1.3 amendment):** Abelian-pair amendment PUBLISHED. v1.2 (10.5281/zenodo.21941346) shipped correct metadata but v1.1-era files (pipeline race); **v1.3 (10.5281/zenodo.21941375) is the CURRENT record** with the corrected files: §5 boundary + §6 F2 + abstract make the abelian-pair postulate explicit (DHR 1971/1974, Doplicher–Roberts 1990, Greenberg–Messiah 1965), references.bib gains the four entries, frontmatter carries the own DOI (NEWVERSION-FRONTMATTER-CARRYOVER-1). Verified in-record (own_doi, abelian-pair text, bib keys), doi.org 200, D1 synced (zenodo_doi 21941375, version v1.3), papers.qnfo.org 200. v1.2 is SUPERSEDED (files); v1.1 (21939493) was the references.bib-only remediation.

- **2026-08-15 (P8 PUBLISH — suite v1.4):** Essay amendment published — DOI 10.5281/zenodo.21943007. §3 heading "(pre-registered, unexecuted)" → "(pre-registered; structural checks executed)" with the T1/T2 execution noted (Completeness HARD-2); Jabs + Lev added to the essay References (Dependency SOFT); language=eng on the record; bundled registry + deposit doc refreshed with post-publish snapshots (HARD-6 residual). 19 files. v1.3 (21941150) remains the prior complete release.

## MAINTENANCE PROTOCOL
Update this file at each phase closeout; bump the date. Any published paper claiming frontier questions or pre-registered predictions must link back here.


---

## PERMANENT RESOLUTIONS (2026-08-14, session PzctHHW4qJopkaNoCTABv)

This section permanently resolves the deferred items so they do not recur as open todos.

### RESOLVED — skill bumps (done)
- research v2.112 (ZENODO-DEPOSIT-DELETE-500-1 + D1 write discipline + S2 gap + email async-verification)
- knowledge v2.13 (INSERT OR IGNORE NOT NULL swallowing + SQLITE_TOOBIG)
- kaizen v2.48 (session lifecycle record)

### PERMANENT DECISION — v1.2 metadata-only newversion: DE-SCOPED
A metadata-only v1.2 (D1 EuroSciVoc URIs / D3 extra communities / D6 datacite.json+metadata.jsonld) is DEFERRED INDEFINITELY. Rationale: (a) version churn (three versions in one day), (b) the primary D6 rationale (Semantic Scholar presence) is VOID — S2 does not index the QNFO Zenodo record set at all (documented 3/3 404), so datacite.json will not bridge that gap, (c) OpenAIRE (which DOES index QNFO records) already receives the plain-string subjects. The D1/D3/D6 levers will be folded into the NEXT CONTENT revision (e.g., a companion-essay publication or an F2 progress update), not a standalone metadata version.

### RESOLVED — D7 Fediverse broadcast (Bluesky published)
Bluesky announcement PUBLISHED 2026-08-15 (handle qnfo.bsky.social, uri at://did:plc:vad2yeqflg5uznmp557zge5c/app.bsky.feed.post/3mt3ifs53ym2r, cid bafyreighwjea2aikkkgomzepds4jzjpgijahxcnxar7exf7bjyh4tyq4di) — 253-char announcement citing the CONCEPT DOI 10.5281/zenodo.21938970 (ZENODO-CONCEPT-DOI-CITE-1 honored). Credentials live in keys.json + .env (NOT the tokens dir — the earlier 'blocked' audit only scanned the tokens dir and missed them). Mastodon remains unprovisioned (no creds). Two skill bugs found + fixed: (1) social-media-management/scripts/bluesky_post.py had a NON-RAW docstring containing Windows paths -> SyntaxError unicodeescape (truncated unicode escape); corrected to a raw docstring; (2) the 300-char Bluesky limit caused the first post failure — reduced to 253.
### PERMANENT DOCUMENTATION — Semantic Scholar gap
S2 systematically 404s all sampled QNFO Zenodo records (v1.0/v1.1/QUNTUF, 2026-08-14). Accepted limitation; no automatic path exists. Evidence: artifacts/external-search/s2_v10.json, s2_v11.json, s2_quntuf.json.

### STANDING MONITOR — OpenCitations COCI (weekly)
Baseline 0 citations. Monitor via scripts/coci-weekly-monitor.py (committed). Cadence: weekly. No cron (scheduled-task creation requires explicit user approval).

### EXTERNAL PENDING — J. Mund reply
Outreach sent 2026-08-14 to mund@fisica.ufjf.br (message_id lj3dhRhXxi37iF4bc1nCeOld3dvz46t2hc70@qwav.tech). Reply is external; re-check on a later cycle.
