# Specification Sources — JPCUB Competitive Landscape v2.0

**Project:** QNFO.RES.JPCUB-CL | **Date:** 2026-08-06 | **Branch:** res/paper/jpcub-competitive-landscape

Every number used in the JPCUB estimates must trace to a verifiable external source. This table records the source for each specification. Verification status: ✅ = independently verified this session (OpenAlex/arXiv/web retrieval returned the record); ⚠️ = sourced from official vendor documentation (accessed via vendor domain); ❌ = excluded — no verifiable source found.

---

## 1. Superconducting Platforms

| Platform | Qubits | P_sys | 1Q gate | 2Q gate | 2Q fid. | Source | Verif. |
|:---------|:------|:------|:--------|:--------|:--------|:-------|:------:|
| IBM Eagle r3 | 127 | 15 kW | 288 ns | 500 ns | 99.0% | IBM Quantum docs (quantum-computing.ibm.com); JPCUB P0 (DOI 10.5281/zenodo.21637028) | ✅ P0 published |
| IBM Heron r2 | 133 | 15 kW | 170 ns | 300 ns | 99.7% | IBM Quantum roadmap 2024; "IBM quantum computers: evolution, performance, and future directions," J. Supercomputing (2025), DOI 10.1007/s11227-025-07047-7 | ✅ OpenAlex |
| Google Sycamore | 53 | 25 kW | 25 ns | 40 ns | 99.8% | Arute et al., Nature 574, 505 (2019), DOI 10.1038/s41586-019-1666-5 | ✅ OpenAlex |
| Google Willow | 105 | 25 kW | 20 ns | 30 ns | 99.95% | Google Quantum AI, Nature 638, 920 (2025), DOI 10.1038/s41586-024-08449-y | ✅ OpenAlex |
| Rigetti Aspen-M-3 | 80 | 15 kW | 200 ns | 400 ns | 97.5% | Rigetti Computing docs (rigetti.com); SEC filings | ⚠️ Vendor |
| Rigetti Ankaa-3 | 84 | 15 kW | 200 ns | 400 ns | 98.0% | Rigetti Computing docs (rigetti.com); SEC filings | ⚠️ Vendor |
| IQM Garnet | 20 | 12 kW | 100 ns | 200 ns | 99.5% | IQM docs (iqm.com); Qibolab OS paper, Quantum 8, 1247 (2024), DOI 10.22331/q-2024-02-12-1247 | ✅/⚠️ mixed |

## 2. Trapped-Ion Platforms

| Platform | Qubits | P_sys | 1Q gate | 2Q gate | 2Q fid. | Source | Verif. |
|:---------|:------|:------|:--------|:--------|:--------|:-------|:------:|
| IonQ Aria | 25 | 3 kW | 20 μs | 100 μs | 99.4% | IonQ docs (ionq.com) | ⚠️ Vendor |
| IonQ Forte | 36 | 3.5 kW | 20 μs | 100 μs | 99.5% | IonQ docs (ionq.com) | ⚠️ Vendor |
| Quantinuum H1-1 | 20 | 4 kW | 10 μs | 50 μs | 99.8% | Quantinuum docs (quantinuum.com); H1-1 technical specs | ⚠️ Vendor |
| Quantinuum H2 | 56 | 4.5 kW | 10 μs | 50 μs | 99.8% | "A Race-Track Trapped-Ion Quantum Processor," PRX 13, 041052 (2023), DOI 10.1103/physrevx.13.041052; arXiv:2305.03828 | ✅ OpenAlex |

## 3. Neutral-Atom Platforms

| Platform | Atoms | P_sys | 1Q gate | 2Q gate | 2Q fid. | Source | Verif. |
|:---------|:------|:------|:--------|:--------|:--------|:-------|:------:|
| QuEra Aquila | 256 | 4 kW | 500 ns | 1.5 μs | 99.5% | QuEra docs (quera.com); Aquila technical datasheet | ⚠️ Vendor |
| Pasqal Fresnel | 100+ | 4 kW | 500 ns | 2.0 μs | 98.0% | Pasqal docs (pasqal.com); "Rearrangement of individual atoms in a 2000-site optical-tweezer array," PRApplied 22, 024073 (2024), DOI 10.1103/physrevapplied.22.024073 | ✅/⚠️ mixed |

## 4. Non-Gate-Model / Pre-Commercial

| Platform | Qubits | P_sys | Spec | Source | Verif. |
|:---------|:------|:------|:-----|:-------|:------:|
| D-Wave Advantage | 5,000+ | 25 kW | ~20 μs anneal | D-Wave docs (dwavesys.com); King et al., Nature 560, 456 (2018), DOI 10.1038/s41586-018-0410-x | ✅/⚠️ mixed |
| D-Wave Advantage2 | 1,200+ | 25 kW | — | D-Wave docs (dwavesys.com) | ⚠️ Vendor |
| Xanadu Borealis | 216 squeezed | 4 kW | GBS | "Quantum computational advantage with a programmable photonic processor," Nature 606, 75 (2022), DOI 10.1038/s41586-022-04725-x | ✅ OpenAlex |
| QWAV (target) | 343 qudits | <0.1 kW | — | JPCUB P0 (DOI 10.5281/zenodo.21637028); qwav.tech | ✅ P0 published |

## 5. System Power Model Sources

| Power source | Value | Reference | Verif. |
|:-------------|:------|:----------|:------:|
| Dilution refrigerator (superconducting QC) | ~10–15 kW | Fellous-Asiani et al., arXiv:2209.05469; PRX Quantum 4, 040319 (2023), DOI 10.1103/PRXQuantum.4.040319 | ✅ OpenAlex |
| Full-system superconducting QC | ~15–25 kW | Auffèves, PRX Quantum 3, 020101 (2022), DOI 10.1103/PRXQuantum.3.020101; Chen, Nat. Comput. Sci. 3, 457 (2023), DOI 10.1038/s43588-023-00459-6 | ✅ OpenAlex |
| Trapped-ion system (lasers + control + vacuum) | ~3–4.5 kW | IonQ/Quantinuum vendor docs; Fellous-Asiani et al. (2022) | ⚠️ Vendor/est |
| Neutral-atom system (lasers + control) | ~4 kW | QuEra/Pasqal vendor docs; Fellous-Asiani et al. (2022) | ⚠️ Vendor/est |

## 6. Excluded Platforms — No Verifiable Specs Found

| Platform | Reason | Evidence |
|:---------|:-------|:---------|
| Oxford Ionics | No published system power / gate fidelity | No primary source returned in OpenAlex/arXiv search |
| Alice & Bob | Cat-qubit specs preliminary, no system power | OpenAlex search returned only QKD/teleportation tangents (2026-08-06) |
| Origin Quantum (Wukong) | Gate times/fidelity not in English-language sources | OpenAlex search returned QFT-feature papers, no hardware specs |
| PsiQuantum | Pre-commercial, no physical hardware specs | OpenAlex search returned photonic roadmap papers only |
| Microsoft (Majorana) | Qubit not yet demonstrated at scale | OpenAlex search returned interface/platform papers only |

## 7. Estimation Model (Reproducibility)

Computation script: `competitive-landscape/artifacts/jpcub-computation.py`

- Task: factoring N=15=3×5, ε=0.95
- Circuit: 30 two-qubit + 50 single-qubit gates (80 total)
- $t_{\text{exec}} = N_{2Q} \times t_{2Q} + N_{1Q} \times t_{1Q}$
- $E_{\text{shot}} = P_{\text{sys}} \times t_{\text{exec}}$
- $p_{\text{succ}} = f_{2Q}^{N_{2Q}}$
- $J_S = E_{\text{shot}} / p_{\text{succ}}$

Re-run: `python competitive-landscape/artifacts/jpcub-computation.py`
