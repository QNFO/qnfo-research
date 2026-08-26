# Scorecard Data — Sources and Estimates

**Project:** Thermodynamically Optimized (Topological/Quantum) Computing
**Date:** 2026-08-21 · Working data table for the paper (Section 5)

Every number below is either (a) a published measurement with its source, or (b) an order-of-magnitude estimate whose derivation is stated. Estimates are marked ESTIMATE and the method is shown, so a reader can re-derive or dispute each one. No cell ships without a source or a stated method.

## Platform parameters

| Platform | Physical error rate p | E_operation (quantum level) [J] | Operating temperature | Protection | Source status |
|---|---|---|---|---|---|
| Superconducting transmon + surface code | ~1.5×10⁻³ per two-qubit gate | 8.2×10⁻²⁵ (program anchor) | 15 mK | active correction | Willow fidelities (arXiv:2408.13687); anchor from the thermodynamics-of-translation analysis cited in the references |
| Trapped ion + surface code | ~1×10⁻³ per two-qubit gate | ~1×10⁻¹⁷ ESTIMATE (laser power ~mW × gate time ~µs, quantum-level absorbed energy) | ~1 mK–300 K trap (laser-cooled) | active correction | two-qubit fidelity 99.9% (arXiv:1512.04600) |
| Silicon spin + surface code | ~1×10⁻³ per two-qubit gate | ~1×10⁻¹⁸ ESTIMATE (microwave pulse ~nW × ~100 ns) | ~1 K | active correction | two-qubit gate demonstrated (arXiv:1411.5760); four-qubit array fidelities (arXiv:2312.16101) |
| Reconfigurable neutral atoms + rate-1/2 qLDPC (QuEra/Kasai co-design) | below threshold (FT ops demonstrated) | ~1×10⁻¹⁷ ESTIMATE (optical control per gate; same order as trapped ion) | µK (optical lattice) | active correction, high-rate codes [[1152,580,d≤12]] R=50.35% | Leverrier-1 slide 69; arXiv:2604.16209; FT threshold + arrays (arXiv:2603.28627) |
| Photonic (fusion-based) | ~1×10⁻² per component | ~1×10⁻¹² ESTIMATE (single-photon source + detector overhead per operation, room-temperature system) | 300 K | active correction (lattice code) | component loss rates are standard in the photonic literature; no single canonical source — ESTIMATE flagged |
| Topological (Majorana nanowire, InSb/NbTiN) | no demonstrated qubit | 8.2×10⁻²⁵ assumed equal to transmon quantum level, ESTIMATE | 20 mK | hardware protection, gap Δ ≈ 3×10⁻²³ J (≈200 µeV hard gap) | hard-gap measurement (arXiv:1702.02578) |
| Topological (Majorana nanowire, PbTe/Pb) | no demonstrated qubit | 8.2×10⁻²⁵ assumed equal to transmon quantum level, ESTIMATE | 20 mK | hardware protection, gap Δ ≈ 1.6×10⁻²² J (≈1 meV) | hard-gap measurement (arXiv:2309.01355) |

## Correction-model calibration (measured, not assumed)

The active-correction model is calibrated on the measured performance of a 101-qubit distance-7 surface-code memory operating below threshold: logical error per cycle 0.143% ± 0.003%, suppression factor Λ = 2.14 ± 0.02 per increase of the code distance by two, decoder latency 63 µs at distance 5, cycle time 1.1 µs (arXiv:2408.13687). Applying that measured scaling uniformly to all active-correction platforms is the scorecard's stated assumption; platform-specific threshold measurements would refine it.

## Control-electronics sensitivity

Full-stack analyses show the control and cooling electronics dominate the energy budget of every platform by orders of magnitude relative to the quantum-level gate energy (arXiv:2209.05469; arXiv:2605.19854; arXiv:2111.09241). The scorecard therefore reports the quantum-level ranking, which is robust to the electronics overhead common to all platforms, and applies a control multiplier of 10⁴–10⁶ as an explicit sensitivity band rather than pretending a single number is known.

## 2026 curriculum inputs (CWI summer school, retrieved 2026-08-26)

The CWI summer school on QA and QEC (24–28 Aug 2026) shared seven slide decks (SURFdrive share, retrieved 2026-08-26). Scorecard-relevant inputs:

- QuEra rate-1/2 co-design: H_X,H_Z ∈ F2^(288×1152), [[1152,580,d≤12]], R=50.35% (Leverrier-1 slide 69; arXiv:2604.16209); Kasai template R=50.04% (arXiv:2601.08824v4).
- Locality tension: "good codes require a lot of long-range interaction ⇒ keep sparsity but drop geometric locality" (Baspin–Krishna '21, Leverrier-1 slide 18/41); 2D bound kd² = O(n), tight up to polylog (Portnoy '23). The protected-substrate frame prices exactly this tension: topological protection buys locality at the price of the 2D bound.
- 2026 overhead anchors: RSA-2048 < 100,000 physical qubits at p=10⁻³, 1 µs cycle, 10 µs reaction (Pinnacle, arXiv:2602.11457; verified via arXiv API 2026-08-26); Shor at 10,000 reconfigurable atomic qubits, P-256 discrete log in days at 26,000 (Cain et al., arXiv:2603.28627; verified 2026-08-26).
- Note: the decks price qubits, time, and error rates — no energy numbers appear across ~150 slides. This scorecard exists precisely because that column is missing from the field's own teaching materials.

## What this table does and does not claim

- It claims that the published ingredients exist to rank platforms by energy per correct solution.
- It claims that under the measured surface-code calibration, hardware protection with a 200 µeV gap at 20 mK outperforms active correction on the quantum-level comparison by orders of magnitude — provided a protected qubit with comparable per-operation energy exists.
- It does NOT claim any protected qubit has been demonstrated. No Majorana-based qubit has been; the literature also contains cautionary results in which non-Majorana states mimic the expected signatures (arXiv:2004.08583). This is stated in the paper, not hidden.
