---
title: "The Unpriced Column: A Slide-Level Synthesis of the CWI Summer School on Quantum Algorithms and Quantum Error Correction (Amsterdam, 24–28 August 2026)"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-26"
version: "0.1"
license: "CC BY 4.0"
status: "draft"
wbs: "QNFO.RES.026"
---

## Abstract

The CWI summer school on quantum algorithms and quantum error correction (Amsterdam, 24–28 August 2026) distributed seven slide decks through the organizers' share folder, and the decks were audited for energy content in full-text form. The decks price physical-qubit overhead (1e7–1e8 physical qubits to break RSA-2048 under concatenation; below 1e5 per the Pinnacle architecture; 1e4 per the reconfigurable-atom estimate), decoder budgets in time (roughly linear-in-n, streaming decoders, heavy runtime tails, expensive training), and code overhead in rate and distance (the gross code and its 2026 successors). Across approximately 150 slides there is no energy number. The same decks carry the field's own caveats: hardware progress alone will not reach the required gate counts, quantum LDPC decoding is "still wide open", and the theoretical linear-time decoders may not be useful in practice. This synthesis assembles the priced and the unpriced columns, traces six threads a skeptical attendee extracted from the week, and states what a practitioner can do with the result. It makes no hardware claim; it is evidence about what the field publishes, scoped to the materials as retrieved on 2026-08-26.

## 1. What This Synthesis Is

A summer school is a snapshot of a field's self-presentation: what its lecturers choose to put on slides is what the field decides newcomers should learn. The CWI summer school on quantum algorithms and quantum error correction ran 24–28 August 2026 in Amsterdam. The organizers distributed the lecturers' slide decks through a SURFdrive share (link and password in the organizers' email of 2026-08-25; retrieved 2026-08-26 via the share's public WebDAV endpoint). Seven decks were available at retrieval time: two by Anthony Leverrier on quantum LDPC codes and their decoding, a 90-minute exercise set on code constructions with solutions, and three by Ashwin Nayak on learning quantum states, quantum walk search, and span programs, plus a tutorial question sheet.

The audit method is mechanical. Each PDF was text-extracted, duplicate animation frames removed, and every quantitative or caveat-bearing passage traced to a slide number. A full-text scan for energy vocabulary (joule, energy, power, watt, kT, thermodynamic, cooling, Landauer, consumption) ran across all extracted texts. The evidence map is in `artifacts/cwi-slide-audit.md`. No passage in this synthesis is quoted without a slide number, and nothing beyond the decks is asserted as a fact about the school.

## 2. What the Decks Price

Physical-qubit overhead appears in three forms. Concatenation-based fault tolerance is quoted at 1e7–1e8 physical qubits to break RSA-2048 (Leverrier-1, slide 15). The 2026 architecture estimates cited in the same deck put the cost at below 100,000 physical qubits at a 1e-3 error rate, a 1 µs code cycle, and a 10 µs reaction time (Pinnacle [2]; Leverrier-2 references), and at 10,000 reconfigurable atomic qubits, with P-256 discrete logarithms in days at 26,000 qubits and RSA-2048 one to two orders of magnitude longer (Cain et al. [3]).

Decoder budgets are priced in time. The stated requirement is "Time complexity should be at most (roughly) linear in n. Ideally, process available syndrome bits as they are produced. Streaming decoders…" (Leverrier-2, slide 18). Belief propagation with ordered statistics decoding carries "Heavy runtime tails" (slide 13); machine-learning decoders are fast once trained but have "expensive training" (slide 14); the decoder families are sorted along accuracy, speed, and reliability axes (slide 9).

Code overhead is priced in rate and distance. The toric code's parameters are "terribly bad code parameters, but this is essentially (!) optimal in 2 dimensions" (Leverrier-1, slide 23); the gross code [[144,12,12]] and its successors — the Kasai rate-1/2 template, the QuEra co-design [[1152,580,d<=12]] at 50.35% rate, the 20%-rate families — are presented as the finite-size race (slides 66–72), with the field's own benchmark page as the leaderboard.

Every number in this section is qubits, gates, time, or error rate.

## 3. What the Decks Do Not Price

The energy-term scan returned zero pricing statements across the seven decks; its term list — joule, energy, power, watt, thermodynamic, cooling, Landauer, consumption, dissipation, heat — produced no occurrences at all in the extracted deck texts. There is no joules-per-syndrome-round figure, no decoder energy per bit, no cooling budget, no per-solution energy. The nearest quantities are the latency budgets of section 2: cycle time and reaction time appear as constraints on classical hardware response, not as energy.

The omission is not a criticism of any lecturer. It is a property of the field's vocabulary, and it is exactly the property a joules-per-solution benchmark exists to correct [6]. The field's own curriculum demonstrates that the energy bill is missing from the standard presentation: the quantities a thermodynamic accounting would convert into energy — the syndrome rounds, the decoder throughput, the ancilla resets — are all present on the slides, priced in every currency except energy.

## 4. The Decks' Own Caveats

The materials repeatedly state the limits the field's marketing omits. On required gate counts: "quantum chemistry: >1e12 gates; Shor's factoring: >1e15 gates =⇒ hardware progress alone won't get us there!" (Leverrier-1, slide 4, where classical hardware's 1e-20 error rates are shown for comparison). On the state of decoding: "QLDPC decoding is still wide open. Degeneracy, correlations, circuit-level noise… Optimal performance is usually unknown, even for code capacity" (Leverrier-2, slide 2). On the theory's practical reach: the linear-time decoders are "interesting theory results, maybe not so useful in practice" (Leverrier-1, slide 74), and the new decoder presented during the week ends on "Main open question: why do small lists work so well?" (Leverrier-2, slide 58). On the field's own age: asymptotically good quantum LDPC codes were not known to exist until five years ago (Leverrier-1, slide 2).

The teaching side of the field is substantially more self-critical than its public-facing side. What remains invisible even in the teaching materials is the energy column.

## 5. The Attendee's Threads

Six threads ran through the week, each a reading of the materials rather than a claim about hardware.

**Definitional tautology.** The decks define quantum computing operationally — algorithms, codes, decoders — and never define "quantum" itself. The core object of the field is used everywhere and defined nowhere in the curriculum. This is not unique to the school; it is the standard presentation.

**Unpriced physical cost.** Every active correction cycle is an erasure engine: syndrome extraction, majority voting, and ancilla re-initialization each destroy information they read, and Landauer's principle prices each erased bit at no less than kT·ln2 [4]. The decks price the combinatorial side of correction completely and the physical side not at all; the thread with the strongest deck-level evidence is precisely this asymmetry between sections 2 and 3.

**Design choice dressed as law.** QEC dominance is presented as the path, yet the decks themselves show the alternatives exist: good codes require long-range interaction, so the field drops geometric locality rather than the correction paradigm (Baspin–Krishna, Leverrier-1 slide 40); hardware co-design (the QuEra platform row) is on the slides; and nature runs uncorrected robust quantum processes — photosynthetic energy transfer and radical-pair magnetoreception — that no engineer would design this way [4].

**Geometric fictions.** The computations are discrete — syndromes, Tanner graphs, parity-check matrices — while the theory's ambient space is the continuous Hilbert space. The decks compute on finite structures and speak in continuous ones.

**Reality as a syndrome.** Stabilizer measurement probes the error without revealing the state: the syndrome tells you where the deviation is, never what the state is. The correction loop is a concrete model of measurement without a global vantage — probing a system you never read directly.

**Classical and quantum as epistemic frames.** Two readings of the same mathematics — one in which amplitudes are bookkeeping and one in which they are real — coexist on the same slides. The materials give no criterion for choosing between them, which is itself a finding.

Threads four and six are the attendee's readings, not claims supported by the decks; they are stated as such and carry no hardware assertions.

## 6. Crosswalk

| QEC engineering | Adjacent-domain equivalent | Fidelity |
|---|---|---|
| Syndrome reset / ancilla re-initialization | Bit erasure; reset-to-reference | Exact |
| Correction work | Heat rejected to the bath | Exact ([4], Landi et al.) |
| Decoder latency budget | Throughput constraint; latency budget in classical ECC | Exact |
| Physical-qubit overhead | Redundancy rate in coding theory | Exact |
| Missing energy column | Joules per correct solution (JPCUB) | Exact as a metric [6] |
| Curriculum snapshot | Self-presentation audit; epistemic-legibility audit | Method transfer ([7], [8]) |
| Structural protection | Passive stability; noise margin | Good |

## 7. What a Practitioner Does With This

A practitioner reading this synthesis gets a three-item checklist for any fault-tolerance roadmap. First, price the syndrome round: the number of rounds per logical operation times the cost of each round's measurement and reset, at the operating temperature. Second, price the decoder: bits per second against energy per bit, not just latency — the "linear in n" requirement is a throughput claim, and throughput has a power cost. Third, price the cooling: every quoted qubit count runs at millikelvin, and the refrigerator's coefficient of performance multiplies the whole budget. None of these numbers appear in the field's own teaching materials, which is why a benchmark that counts everything — control electronics, reset pulses, ancilla preparation, cooling amortization — exists as a counterweight [6]. The unpriced column is the audit instrument: where the curriculum has no number, the roadmap has no plan.

## 8. Boundaries

This synthesis claims nothing about any machine's energy consumption. It is evidence about what the field publishes in its teaching materials, scoped to the seven decks as retrieved on 2026-08-26. It does not judge any lecturer; the slides' own caveats (section 4) speak for themselves. The trapped-ion lecture is not among the uploaded decks, so no claim about that material is made. The organizers noted the share would be updated through the week; a final re-check is scheduled, and the scope clause freezes this document at the retrieval date regardless.

## Reproducibility

Retrieval: SURFdrive share `https://surfdrive.surf.nl/s/8ASHtZ679ycskes` (password in the organizers' email of 2026-08-25), public WebDAV at `/public.php/webdav`, fetched 2026-08-26. Local copies and the full slide-to-quote map: `artifacts/cwi-slide-audit.md`. Verification (run 2026-08-26; CPython 3.12 + pypdf, no other dependencies; the seven decks are supplied via `--decks-dir`): `artifacts/verification/energy_scan.py` reproduces section 3's zero result — evidence `artifacts/verification/energy_scan.json` (zero energy-term occurrences across the seven extracted texts); `artifacts/verification/quote_trace.py` asserts every verbatim quote in sections 2–4 against its deck, slide by slide — evidence `artifacts/verification/quote_trace.json` (9/9 fragments found; the truncation-ellipsis convention is documented in the script). The decks remain with the organizers; both scripts run on the seven PDFs as retrieved 2026-08-26.

## References

[1] CWI, "Summer school on Quantum Algorithms and QEC — shared slide decks (Leverrier, Nayak)," SURFdrive share, https://surfdrive.surf.nl/s/8ASHtZ679ycskes, retrieved 2026-08-26.
[2] Paul Webster et al., "The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes," arXiv:2602.11457 (2026).
[3] Madelyn Cain et al., "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits," arXiv:2603.28627 (2026).
[4] Rowan Brad Quni-Gudzinas, "Error Correction Is a Landauer Machine: The Thermodynamic Floor of Quantum Error-Correction Overhead," v1.6, https://doi.org/10.5281/zenodo.22115862 (2026).
[5] Rowan Brad Quni-Gudzinas, "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation," https://doi.org/10.5281/zenodo.17955898 (2025).
[6] Rowan Brad Quni-Gudzinas, "The Joules-per-Solution Metric: Definition, Measurement Protocol, and Anti-Gaming Provisions for Honest Computational Benchmarking," https://doi.org/10.5281/zenodo.21637028 (2026).
[7] Rowan Brad Quni-Gudzinas, "Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck," https://doi.org/10.5281/zenodo.22026592 (2026).
[8] Rowan Brad Quni-Gudzinas, "The Vast World of Quantum Advantage — A Full-Spectrum Audit," https://doi.org/10.5281/zenodo.21440671 (2026).
[9] Rowan Brad Quni-Gudzinas, "Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces," https://doi.org/10.5281/zenodo.21964674 (2026).
[10] Rowan Brad Quni-Gudzinas, "The Universal Ignorance Audit: A Fifteen-Question Method for Systematic Inquiry into the Structure of Not-Knowing," https://doi.org/10.5281/zenodo.21901984 (2026).
