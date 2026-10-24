Companion paper to JPCUB P0 (DOI 10.5281/zenodo.21637028). Bridges P0 (metric definition) and P1 (quantum energy audit).

## Published (v2.3 — red-team corrected)
- **DOI: 10.5281/zenodo.21821767** (published, DataCite findable)
- PDF + HTML + MD on Zenodo; R2 archived; papers-server live
- v2.3 = v2.2 + full red-team audit (3 adversarial reviewers): 2 CRITICAL, 4 HIGH, 5 MEDIUM, 6 LOW findings — ALL fixed
- Red-team report: competitive-landscape/artifacts/red-team-v22.md

## Key red-team corrections (v2.3)
1. **C1 (CRITICAL):** classical GNFS core-years were off by 7-9 OOM. Corrected: ~2.6e17 core-years (RSA-768 anchored), E_classical ~1.6e27 J (~1e7x world electricity, not 5.8%), quantum win ratio ~1e16x (not 2.2e8x)
2. **C2 (CRITICAL):** AES-256 energy rebuilt on §9.1's own full-stack model (2.9e-5 J/gate): ~9.9e33 J (~1e14x world electricity), not 3.4e23 J — the 1e-15 J/op figure implied a 10 uW machine
3. **H1:** AES-256 time corrected to ~1.1e25 yr at Gidney-Ekera logical rate (7.8e14x universe age)
4. **H2:** §8.2 atlas vs §9.1 Landauer basis reconciled (marginal per-logical-op vs full-system per-physical-gate)
5. **H3:** §8.2 CMOS row relabeled per-transistor theoretical (was inconsistent with §8.1 J/op by 8 OOM)
6. **M1:** factoring-15 op count corrected 5e3 -> 1e2; penalty now 4.5e6-1.8e7x
7. **M4/M5:** fleet 33 GWh relabeled upper bound (sensitivity 17.5-65.8); power envelope 0.5-10 MW
8. **L1-L6:** Grover pi/4 footnote, Yoo title, Thonnart author, QEC year 2024, speculative flags

## Scope (unchanged)
- Roster: 6 (qwav.tech) to 17 platforms (13 gate-model + 4 non-gate-model/pre-commercial)
- Exclusions documented with OpenAlex evidence

## Key findings (unchanged by red team)
1. Same-task baselines: classical 1e-8-2e-7 J; IBM Eagle 0.89 J (4.5e6-1.8e7x worse); QWAV target <1e-3 J
2. Gate speed dominates JPCUB: superconducting 0.05-0.71 J/sol; neutral atoms 0.32-0.62; trapped ions 8.5-16.3
3. RSA-2048: quantum wins ~1e16x IF the 20M-qubit machine existed — but 20,000x beyond SOTA, per-op efficiency 2e20x above Landauer, target retired by NIST PQC
4. AES-256: ~1e34 J and ~1e25+ years — thermodynamically AND temporally immune
5. NISQ fleet: ~33 GWh/yr idle (upper bound) for zero JPCUB-beating solutions

## Verification
- All v2.3 numbers BP-1 fit-verified (independent recomputation, ALL PASS)
- All citations verified live (15/15 external DOIs resolve correctly; 3 nits fixed)
- PDF 802 KB, 422 math elements, decompressed-content mojibake check CLEAN
