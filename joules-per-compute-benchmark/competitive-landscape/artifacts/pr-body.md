Companion paper to JPCUB P0 (DOI 10.5281/zenodo.21637028). Bridges P0 (metric definition) and P1 (quantum energy audit).

## Published (v2.2 — baselines + classically-infeasible problem energy)
- **DOI: 10.5281/zenodo.21821507** (published, DataCite findable)
- PDF + HTML + MD on Zenodo; R2 archived; papers-server live
- v2.2 adds: §8 JPCUB baselines vs existing architectures, §9 total joules for classically-infeasible problems

## Scope
- Roster expanded: 6 (qwav.tech) to 17 platforms
- 13 gate-model: 7 superconducting (Google Willow/Sycamore, IBM Heron/Eagle, Rigetti Ankaa-3/Aspen-M-3, IQM Garnet), 4 trapped-ion (IonQ Aria/Forte, Quantinuum H1-1/H2), 2 neutral-atom (QuEra Aquila, Pasqal Fresnel)
- 4 non-gate-model/pre-commercial: D-Wave Advantage/Advantage2, Xanadu Borealis, QWAV target
- Exclusions documented (Oxford Ionics, Alice&Bob, Origin Wukong, PsiQuantum, Microsoft) with OpenAlex evidence

## Key findings
1. **Same-task baselines (factoring N=15):** classical 10^-6-10^-5 J; IBM Eagle 0.89 J (9e4-3.6e5x worse); QWAV target <10^-3 J
2. **Gate speed dominates JPCUB:** superconducting 0.05-0.71 J/sol (30-500 ns gates); neutral atoms 0.32-0.62 J/sol; trapped ions 8.5-16.3 J/sol (50-100 us gates)
3. **RSA-2048 (Shor):** classical GNFS ~6.3e18 J (infeasible, ~6% world electricity); quantum 1.4e10-2.9e10 J IF the 20M-qubit Gidney-Ekera machine existed (2.2e8x win) — but 20,000x beyond state of the art, per-op efficiency 2e20x above Landauer, and the target is being retired by NIST PQC (FIPS 203)
4. **AES-256 (Grover):** ~3.4e23 J and 1.1e21 years — thermodynamically AND temporally immune to quantum attack
5. **Current NISQ fleet:** ~33 GWh/year idle for zero solutions better than classical on any task

## Deliverables
- PROJECT-PLAN.md (WBS QNFO.RES.JPCUB-CL)
- docs/jpcub-competitive-landscape-v2.md (6,231 words, 13 sections, all publication gates PASS)
- artifacts/jpcub-computation.py (reproducible)
- artifacts/specification-sources.md (traceability)
- artifacts/extra-platform-search.json (OpenAlex evidence)

## Verification
- Only IBM Eagle has published JPCUB (0.89 J/sol, P0)
- All other values are conservative system-level upper bounds pending independent measurement
- All citations verified live (Gidney-Ekera DOI corrected to 10.22331/q-2021-04-15-433)
