# OUTLINE — QNFO.RES.026 Phase 2 (draft skeleton)

**Title (working):** The Unpriced Column: A Slide-Level Synthesis of the CWI Summer School on Quantum Algorithms and QEC (Amsterdam, 24–28 August 2026)
**Status:** P2 outline (2026-08-26) — maps deck evidence to each thread; P3 absorbs the Obsidian synthesis draft into this skeleton.

## Evidence inventory (retrieved 2026-08-26, SURFdrive share)
7 decks: Leverrier-1 (QLDPC codes, 41 slides), Leverrier-2 (decoding/Frontier, 51 slides), tutorial_code_constructions, Nayak learning-states / quantum-walk-search / span-programs, algorithms-tutorial-questions. Full slide→quote map in QNFO.JPC.003 `artifacts/cwi-slide-audit.md` (shared evidence).

## Skeleton

**Front matter + Abstract** — one paragraph: what the 2026 curriculum prices (qubits, time, error rates) and what it does not (energy), stated as a documentation-level finding.

**§1 What this synthesis is.** The school as a snapshot of the field's self-presentation; the seven decks as primary evidence; retrieval method; scope (teaching materials, not hardware measurement). No internal pipeline narrative (PAPERS-NO-NAVEL-GAZING-1).

**§2 What the decks price.** Physical-qubit overhead (1e7–1e8 concat; Pinnacle <1e5 at p=1e-3, 1 µs cycle, 10 µs reaction, arXiv:2602.11457; Cain 1e4, arXiv:2603.28627); decoder budgets in time only (linear-in-n, streaming; BP+OSD heavy runtime tails; ML training cost); code overhead in rate/distance (gross code [[144,12,12]], Kasai rate-1/2, QuEra co-design, 20%-rate families). Evidence: L-1 slides 4, 15, 32–39, 40; L-2 slides 13, 14, 18.

**§3 What the decks do not price.** ~150 slides, zero energy numbers; no joules per syndrome round, no decoder energy, no cooling budget. The latency budgets ([30]) are the only adjacent quantities. Evidence: full-text energy-term scan (cwi-slide-audit.md).

**§4 The decks' own caveats.** "hardware progress alone won't get us there!"; "QLDPC decoding is still wide open"; "interesting theory results, maybe not so useful in practice"; "why do small lists work so well?". The teaching side is more self-critical than the marketing side.

**§5 The attendee's threads (each tied to deck evidence where it exists).** From the Obsidian draft (_cwi-synthesis-draft-2026-08-26.md): (a) definitional tautology; (b) unpriced physical cost (Landauer/JPCUB — BUILDS_ON QNFO.JPC.003, 10.5281/zenodo.22114431-concept); (c) design choice dressed as law; (d) geometric fictions; (e) reality-as-a-syndrome; (f) epistemic frames. Carried as the attendee's reading, not as claims beyond the decks.

**§6 Crosswalk.** QEC-engineering → adjacent-domain equivalents (erasure/energy-per-corrected-bit/curriculum-audit/thermodynamic-optimization), per CROSSWALK-TRANSLATION-1; anchors: Bottlenecks (10.5281/zenodo.17955898), JPCUB metric (10.5281/zenodo.21637028), Epistemic Legibility (10.5281/zenodo.22026592), Full-Spectrum Audit (10.5281/zenodo.21440671), Archimedean Shadows (10.5281/zenodo.21964674, canonical title).

**§7 What a practitioner does with this.** The checklist: price syndrome extraction, decoder throughput, and cooling before quoting qubit counts; the energy column as the audit instrument for any fault-tolerance roadmap.

**§8 Boundaries.** What the synthesis does not claim (no hardware measurement; no judgment of individual lecturers; the trapped-ion claim scoped out until that lecture's slides are uploaded; scope frozen at "shared materials as retrieved 2026-08-26").

**Verification appendix.** Retrieval reproducibility (share link + password provenance); slide-number trace method; arXiv verification records for all imported numbers; rendering gates at P7.

**References.** Shared set with JPC.003 §9 (Pinnacle, Cain, CWI share) + the anchors above.

## Phase gates
P3 draft (absorb Obsidian synthesis content) → P4 computational verification (energy-term scan script, quote-trace script) → P5 red team → P6 core-claim lock → P7 deposit prep → P8 publish (Zenodo + R2 + D1/KG).
