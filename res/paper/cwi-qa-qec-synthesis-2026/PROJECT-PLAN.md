# PROJECT-PLAN — QNFO.RES.026

- **Title (working):** The Unpriced Column: A Slide-Level Synthesis of the CWI Summer School on Quantum Algorithms and QEC (24–28 Aug 2026)
- **WBS:** QNFO.RES.026 (project, parent QNFO.RES, order 26)
- **Slug:** cwi-qa-qec-synthesis-2026
- **Repo/Branch:** QNFO/qnfo-research @ res/paper/cwi-qa-qec-synthesis-2026
- **Phase:** P0 (this plan) — roadmap P1 → P8 below

## Core claim (LOCKED at P6 — 2026-08-26)

Taken as a snapshot of the field's self-presentation, the CWI summer school's shared slide decks — seven PDFs retrieved 2026-08-26 from the organizers' SURFdrive share — price every cost of fault-tolerant quantum computation except energy. The decks state physical-qubit overhead (1e7–1e8 for RSA-2048 under concatenation, Leverrier-1 slide 11; below 1e5 per Pinnacle, arXiv:2602.11457; 1e4 per Cain et al., arXiv:2603.28627), decoder budgets in time (linear-in-n with streaming decoders, Leverrier-2 slide 15; heavy runtime tails, slide 10; expensive training, slide 11), and code overhead in rate and distance (gross code [[144,12,12]] and successors, slides 32–39). The full-text energy-term scan across the seven extracted deck texts returns zero occurrences of its term list; there is consequently no energy quantity anywhere in the curriculum. The decks' own caveats state the field's limits. The claim is documentation-level — it is about what the curriculum publishes, scoped to the materials as retrieved on 2026-08-26 — and asserts no hardware fact.

## Falsifiers (locked with the claim)

- **F1 (scan):** any pricing-statement hit from `artifacts/verification/energy_scan.py` (energy term + number + unit within ±200 chars) fails the zero-occurrence claim; section 3 must be amended with the hit.
- **F2 (trace):** any verbatim quote failing `artifacts/verification/quote_trace.py` means that passage is not on its cited slide; the citation must be corrected or removed.
- **F3 (share):** any deck added to the share after 2026-08-26 containing an energy quantity triggers the scope clause (retrieval-date corpus); the claim is re-scoped, never silently extended.
- **F4 (citations):** any reference resolving to a different record (DOI/arXiv) than cited fails citation integrity; P3.AUTHOR-GATE re-run required.

## SO-WHAT

External readers get a primary-source audit of what the 2026 QEC curriculum itself counts and what it does not. The single unpriced quantity — energy — is the one a joules-per-solution benchmark (JPCUB) exists to supply. Practitioners and benchmarking groups can reuse the audit method: retrieve the public share, then price the columns the field leaves blank.

## Premise depth

- **L0 (unanalyzable primitives):** the seven slide PDFs as given; verbatim text extraction.
- **L1 (derived):** every critique claim is tied to a quoted passage and a slide number; anything beyond the decks is flagged as external (arXiv refs cited on the slides themselves).
- **L2 (named imported inputs):** the calibration hidden-assumptions list (Obsidian note `_26238172303.md`); the Landauer/JPCUB frame from QNFO.JPC.003 (10.5281/zenodo.22114431) and QNFO.JPC.001 (10.5281/zenodo.21637028). These are inputs, not results of this project.
- **Where premises end:** the synthesis asserts no hardware fact beyond the decks or their cited references.

## Practitioner relevance

A practitioner reads the synthesis and gets: (1) a table of the overhead numbers the field now teaches (physical qubits per logical, decoder runtime budgets, code parameters); (2) the decoder design axes (accuracy / speed / reliability) and the streaming-decoder requirement; (3) the energy column, empty, as the actionable checklist item for any fault-tolerance roadmap.

## Verification plan (COMPUTATIONAL-VERIFICATION-1)

- Every quoted number is traceable to (a) the deposited PDF page and (b) the cited arXiv record (arxiv-mcp verification: 2602.11457, 2603.28627, plus any further refs used).
- Evidence inventory: `artifacts/cwi-slide-audit.md` (deck → claim → slide → quote).
- Rendering gates at P7: CURRENCY-DOLLAR-ESCAPE-1, FRONTMATTER-DUPLICATION-1, `check_rendering.py` PASS.
- Reproducibility: retrieval procedure (share link, password, WebDAV method) documented in README.

## Phase 1 due-diligence seeds (cross-system validated 2026-08-26)

- "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation" — 10.5281/zenodo.17955898 (BUILDS_ON; predecessor thesis, 2025-12).
- "The Joules-per-Solution Metric: Definition, Measurement Protocol, and Anti-Gaming Provisions…" — 10.5281/zenodo.21637028 (QNFO.JPC.001; BELONGS_TO).
- "Lifecycle of a Fault-Tolerant Quantum Computer" — published, no Zenodo DOI (RELATES_TO).
- "Error Correction Is a Landauer Machine: The Thermodynamic Floor of QEC Overhead" — 10.5281/zenodo.22114431 (QNFO.JPC.003; the thesis this synthesis documents from the teaching side).

## UIA audit — Universal Ignorance Audit (5 phases / 15 questions; administered 2026-08-26 on the core claim)

- **P1 Inventory.** Q1 Unknowns about the object: decks beyond the 7 shared (the trapped-ion lecture's slides are not yet uploaded; the share updates through the week). Q2 Unknowns about our own claim: whether any slide carries an energy number we missed (mitigation: full-text re-scan for energy terms before publish). Q3 Unnamed unknowns: spoken content and the poster session are not in the decks.
- **P2 Structure.** Q4 Data-gap vs model-gap: missing decks are a data gap; reading decks as self-presentation is a stated model choice. Q5 Resolvable unknowns: the missing decks (wait for upload). Q6 Permanent unknowns: Q&A, tone, poster discussions.
- **P3 Sources.** Q7 Why we don't know: organizers control the share; read access only. Q8 Who knows: the organizers/lecturers. Q9 Is not-knowing load-bearing: partially — the trapped-ion critique claim stays scoped out until upload.
- **P4 Implications.** Q10 What would flip the claim: any deck carrying an energy budget would require amending the claim. Q11 What we cannot do meanwhile: extend the critique to trapped-ion specifics. Q12 Cost of acting now: low — the claim is explicitly scoped to "shared materials as retrieved 2026-08-26".
- **P5 Meta.** Q13 What the audit misses about itself: single auditor; PDF text extraction may garble math (mitigation: slide-number checks against page markers). Q14 Silence: none recorded. Q15 Next recursive audit: re-run when the share finalizes (calendared 2026-08-28).

## Roadmap

P1 due-diligence ✅ (2026-08-26) → P2 gap analysis ✅ → P3 draft ✅ → P4 computational verification ✅ → P5 red team ✅ → P6 core-claim lock ✅ → **P7 rendering gates** → P8 publish (Zenodo + R2 mirror + D1/KG distribution).
