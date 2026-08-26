# Phase 1 Due Diligence — Post-Positional Numeracy (QNFO.RES.024)

Date: 2026-08-26 · Author: research pipeline · Evidence files: artifacts/external-search/*

## 0. Summary of the adjudication

1. **Check threads + notes:** the topic originates in Obsidian 08-26 notes `_26238100931.md` (156.6K, "Perfect Number System") + `_26238083140.md` (thesis). A prior session (08-26 08:21 UTC) already adjudicated the thesis as a re-derivation of published corpus work — durable memory `mem:task_outcome:1787732507078`.
2. **Corpus verification:** the memory's claims were verified record-by-record. The core thesis ("decimal = convenient lie; adelic-Ostrowski = complete picture") is published in six-plus records (table §2).
3. **User decision:** keep the project, re-scope to the uncovered constructive leg (finite-adele encoding + product-formula verification + demo). Core claim C1′ locked in PROJECT-PLAN §1.2.
4. **Hensel deposit audit (decisive for the delta):** the Hensel framework v1.2.0 (10.5281/zenodo.20756222, 2026-06-19) ships `src/hensel_system.py` (37 KB implementation), `tests/test_hensel.py` (29 KB, 36–37 tests), `benchmarks/` with report, `demo/demo.js` (13 KB) — but is **single-place**: paper.md contains **zero** occurrences of "product formula", "adele", or "adelic"; benchmarks use one prime (p=7, k=30); reconstruction cites Wang–Guy–Davenport (1981). The multi-place product-formula leg is genuinely uncovered.

## 1. Corpus sweep (tools + formulations)

Corpus state: KG 8,325 nodes / 8,503 edges (query_graph stats, 2026-08-26); living-paper D1 (70a58cb3); portfolio-state D1 (d80fdf2a).

Formulations used (>=3 per DUE-DILIGENCE-DEPTH-1):
- F1 "post-positional numeracy positional notation adele ring Ostrowski" (qnfo-memory-mcp, limit 16)
- F2 "Hensel code p-adic exact rational arithmetic reconstruction" (qnfo-memory-mcp, limit 16)
- F3 "decimal system convenient lie perfection of numeral notation Hindu-Arabic" (search_papers_enriched, limit 20)
- F4 "Ostrowski theorem completions p-adic valuation ultrametric absolute value" (qnfo-memory-mcp, limit 16)
- F5 "exact rational arithmetic p-adic Hensel codes decimal fingers adelic freedom" (qnfo-memory-mcp, limit 16)
- Plus: recall_facts ("numeral", "Provincialism"), search_memories ("post-positional numeracy…"), KG node queries (silent/numerat family), resolve_paper_id per hit.

## 2. Ancestor coverage table (verified records)

| Leg of the thesis | Published record | DOI | Status |
|---|---|---|---|
| Decimal = anthropocentric convention | Ten-Fingered Trap | (no DOI, r2 qnfo/releases/2025/00/) | published/draft |
| Decimal → adelic diagnosis + roadmap + Ostrowski §3.1 + product formula §3.2 | From Decimal Fingers to Adelic Freedom | 10.5281/zenodo.21428829 | published 2026-07-18 |
| Positional notation = ultrametric tree + Calculus of Indications remedy | THE SILENT RADIX (+ formal appendix) | 10.5281/zenodo.21148596 (concept 21067593) | published |
| Nonlinear/tree-based numeration synthesis | Nonlinear Tree-Based Numeration Systems | 10.5281/zenodo.21046213 | published |
| Multi-axis numeral evaluation | NUMERATA | 10.5281/zenodo.21441847 | published |
| Cognitive grounding (Lakoff & Núñez) | Embodied Mathematics After Lakoff & Núñez | 10.5281/zenodo.21440894 | published |
| Radix-tag discipline | EXPLICIT FRAME PATTERN LANGUAGE v1.0 | (no DOI) | published |
| **Single-place exact arithmetic (constructive)** | **Exact Rational Arithmetic via p-adic Hensel Codes** (v1.0 / v1.0.1 / v1.2.0) | 10.5281/zenodo.20754449 / 20756305 / 20756222 | published |

## 3. Hensel v1.2.0 deposit audit (evidence: artifacts/external-search/hensel-v120-audit/)

- Files: src\hensel_system.py (37,307 B), tests\test_hensel.py (29,148 B), benchmarks\benchmark.py + BENCHMARK_REPORT.md, demo\demo.js (13,360 B), paper.md (30,539 B), PDFs, README, LICENSE, ARTIFACT-MANIFEST.json.
- paper.md grep: "product formula" 0 · "adele"/"adelic" 0 · "Ostrowski" 12 (grounding + "Ostrowski gap" framing: computation inhabits only the real completion) · reconstruction: Wang–Guy–Davenport (1981) · benchmarks: p=7, k=30 single prime · test suite: 36–37 tests incl. roundtrip encode→arithmetic→decode.
- Source: small_primes = [2,3,5,7,11,13,17] scaffolding exists; arithmetic is mod p^k (single-place); no CRT-based multi-place reconstruction; no product-formula check.
- **Conclusion:** the Hensel framework implements and tests single-place exact arithmetic with a demo. The multi-place (finite-adele) encoding, injectivity window, and product-formula invariant are absent. C1′ scopes to exactly that.

## 4. External literature (arXiv sweeps, evidence in artifacts/external-search/)

- **"Ostrowski numeration systems" = established terminology with a DIFFERENT sense** (continued-fraction/β-expansion numeration): Hieronymi & Terry (arXiv:1407.7000, math.LO); Cabanillas (1904.01874); Mittal & Sharma (2409.06232); Aval & Labbé (2511.11290); Bourla (1511.02179). Name-collision risk for our title — the paper's crosswalk must disambiguate ("Ostrowski's theorem" vs "Ostrowski numeration systems").
- **"p-adic" AND "exact rational arithmetic": 0 arXiv hits** (the classical work is journal literature: Krishnamurthy–Gregory error-free computation; Wang–Guy–Davenport 1981; Dixon 1982).
- **"Hensel code" AND (arithmetic | exact computation): 0 arXiv hits.**
- **Modular rational reconstruction is classical:** Boehm–Decker–Fieker–Pfister et al. (arXiv:1207.1651, 1702.06920, 2401.11606) — CRT + Farey-bound reconstruction, "bad primes" handling. **No surveyed record uses the adelic product formula as a reconstruction invariant or verification checksum.** This is the novel conjunction H-PPN-4 scopes.

## 5. Gap analysis

- **Covered (published):** conceptual thesis (6+ records); single-place exact arithmetic with tests/demo (Hensel framework, 3 versions); numeral evaluation (NUMERATA); notation-as-tree (Silent Radix line).
- **Uncovered (the delta, C1′):** (a) finite-adele multi-place encoding with a proved injectivity window; (b) the product formula as a machine-checkable invariant that verifies and failure-localizes multi-place reconstruction; (c) computational verification suite (golden values + seeded trials) and demo for (a)+(b); (d) explicit disambiguation from external "Ostrowski numeration systems" and from single-place Hensel codes.
- **[CONFIRMATION-BIAS check]:** corpus hits are QNFO-internal by construction; external corroboration = arXiv sweeps + the classical literature cited by the Hensel paper itself. The novelty claim rests on the deposit audit (primary evidence) and the external sweeps — not on internal claims alone.
- **JPCUB adjacency (noted, out of scope this project):** the cost-of-exactness question (multi-place vs single-place energy) surfaced in the UIA Q15 seed; the user declined the JPC route this cycle. Flagged for QNFO.JPC.004.

## 6. Crosswalk (CROSSWALK-TRANSLATION-1)

| Number theory | Exact computation / engineering | Notation / epistemology |
|---|---|---|
| absolute value / place of Q | choice of metric the arithmetic is faithful under | which "distance" the notation presumes |
| Hensel code | finite p-adic truncation (residue mod p^k) | p-adic "digits" — positional, but at a non-Archimedean place |
| finite adele (truncated restricted product) | the record that carries all chosen places at once | multi-place numeracy: a number as its simultaneous local images |
| product formula ∏_v |x|_v = 1 | global integrity checksum / conservation law | the invariant that ties the places: "no place may win" |
| rational reconstruction (CRT + Farey/Wang bounds) | exact decode from multi-place residues | recovering one number from its many local appearances |
| Ostrowski's theorem | why ℝ and ℚ_p are the only completions | why "the" number line was always a choice |

## 7. Next actions (Phase 2+)

P2 literature (ancestor line + Hensel-code literature + disambiguation); P3 BibTeX with live-verified DOIs; P4 injectivity lemma + product-formula derivation + implementation + H-PPN execution; P5 publication with COMPUTATIONAL-VERIFICATION-1 suite; P6–P8 distribution with KG BUILDS_ON → Hensel framework.
