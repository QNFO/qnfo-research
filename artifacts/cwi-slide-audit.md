# CWI Slide Audit — Evidence Inventory (QNFO.JPC.003 §9)

Source: CWI summer school on Quantum Algorithms and Quantum Error Correction (Amsterdam, 24–28 Aug 2026).
Share: https://surfdrive.surf.nl/s/8ASHtZ679ycskes (password distributed in the organizers' "Slides summer school" email, 2026-08-25).
Retrieved: 2026-08-26 via public WebDAV (public.php/webdav). Local copies: D:\Obsidian\notes\v1\2026\08\26\cwi_slides\.

## Decks

| File | Lecturer | Pages (raw) |
|---|---|---|
| Leverrier-1.pdf | A. Leverrier (Inria) | 75 (41 slides + animation frames) |
| Leverrier-2.pdf | A. Leverrier (Inria) | 62 (51 slides) |
| tutorial_code_constructions.pdf | A. Leverrier (Inria) | 10 |
| cwi-learning-states-no-build-aug-2026.pdf | A. Nayak (Waterloo) | 36 |
| cwi-quantum-walk-search-no-build-aug-2026.pdf | A. Nayak (Waterloo) | 27 |
| cwi-span-programs-no-build-aug-2026.pdf | A. Nayak (Waterloo) | 16 |
| algorithms-tutorial-1-questions.pdf | A. Nayak (Waterloo) | 2 |

## Claim → evidence map (§9)

| Claim | Deck | Slide | Quote (verbatim) |
|---|---|---|---|
| Concatenation overhead 10^7–10^8 for RSA-2048 | Leverrier-1 | 15 | "in practice: break RSA with 4000 logical qubits, but 10^7 − 10^8 physical qubits ..." |
| Hardware alone insufficient | Leverrier-1 | 4 | "quantum chemistry: >10^12 gates; Shor's factoring: >10^15 gates =⇒ hardware progress alone won't get us there!" |
| Decoder latency budget, not energy | Leverrier-2 | 18 | "Time complexity should be at most (roughly) linear in n. Ideally, process available syndrome bits as they are produced. Streaming decoders..." |
| BP+OSD runtime tails | Leverrier-2 | 13 | "Heavy runtime tails" |
| ML decoder training cost | Leverrier-2 | 14 | "expensive training and hyperparameter searches" |
| Decoding wide open | Leverrier-2 | 2 | "QLDPC decoding is still wide open. Degeneracy, correlations, circuit-level noise... Optimal performance is usually unknown, even for code capacity." |
| Linear-time decoders impractical | Leverrier-1 | 40 | "interesting theory results, maybe not so useful in practice" |
| Gross code + successors | Leverrier-1 | 32–39 | [[144,12,12]]; Kasai rate-1/2; QuEra co-design; 20%-rate families |
| Pinnacle architecture (cited) | Leverrier-2 | refs | Webster et al., arXiv:2602.11457 |
| Cain et al. (cited) | Leverrier-2 | refs | Cain et al., arXiv:2603.28627 |

## Energy-term scan

Full-text scan (case-insensitive) of all 7 extracted deck texts for: joule, energy, power, watt, kT, thermodynamic, cooling, Landauer, consumption, dissipation-as-cost.
Result: **0 pricing statements.** Near-hits are latency vocabulary ("time complexity", "runtime"), not energy. Scan date 2026-08-26.

## External verification (arXiv API, 2026-08-26)

- arXiv:2602.11457 — "The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes" (Webster et al., published 2026-02-12). Abstract confirms: <100,000 physical qubits at p=10^-3, 1 µs code cycle, 10 µs reaction time.
- arXiv:2603.28627 — "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits" (Cain et al., published 2026-03-30). Abstract confirms: 10,000 qubits; P-256 discrete log in days at 26,000 qubits; RSA-2048 one to two orders of magnitude longer.

## Scope note

This inventory supports §9's documentation-level claim (what the field's curriculum prices and omits). It is not a hardware measurement and does not bear on Equation (1)'s floor.
