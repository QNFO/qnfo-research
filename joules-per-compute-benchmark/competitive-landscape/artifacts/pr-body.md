Companion paper to JPCUB P0 (DOI 10.5281/zenodo.21637028). Bridges P0 (metric definition) and P1 (quantum energy audit).

## Published (v2.1 — corrected §2.3 math rendering)
- **DOI: 10.5281/zenodo.21821316** (published, DataCite findable)
- PDF + HTML + MD on Zenodo; R2 archived (etag-verified); papers-server live

## Scope
- Roster expanded: 6 (qwav.tech) to 17 platforms
- 13 gate-model: 7 superconducting (Google Willow/Sycamore, IBM Heron/Eagle, Rigetti Ankaa-3/Aspen-M-3, IQM Garnet), 4 trapped-ion (IonQ Aria/Forte, Quantinuum H1-1/H2), 2 neutral-atom (QuEra Aquila, Pasqal Fresnel)
- 4 non-gate-model/pre-commercial: D-Wave Advantage/Advantage2, Xanadu Borealis, QWAV target
- Exclusions documented (Oxford Ionics, Alice&Bob, Origin Wukong, PsiQuantum, Microsoft) with OpenAlex evidence

## Key finding
Gate speed dominates joules-per-solution:
- Superconducting: 0.05-0.71 J/sol (30-500 ns gates)
- Neutral atoms: 0.32-0.62 J/sol (1.5-2 us gates, 4 kW)
- Trapped ions: 8.5-16.3 J/sol (50-100 us gates) - room-temp advantage overwhelmed by gate-time penalty

## Deliverables
- PROJECT-PLAN.md (WBS QNFO.RES.JPCUB-CL)
- docs/jpcub-competitive-landscape-v2.md (4,719 words, all publication gates PASS)
- artifacts/jpcub-computation.py (reproducible)
- artifacts/specification-sources.md (traceability)
- artifacts/extra-platform-search.json (OpenAlex evidence)

## Verification
- Only IBM Eagle has published JPCUB (0.89 J/sol, P0)
- All other values are conservative system-level upper bounds pending independent measurement
