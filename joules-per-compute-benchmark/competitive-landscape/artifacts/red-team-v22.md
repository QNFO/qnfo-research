# Red-Team Audit — JPCUB Competitive Landscape v2.2 (DOI 10.5281/zenodo.21821507)

**Date:** 2026-08-06 | **Project:** QNFO.RES.JPCUB-CL | **Branch:** res/paper/jpcub-competitive-landscape
**Method:** Three independent adversarial subagents (Methodology Skeptic + Null-Hypothesis Defender; Scaling Pessimist + Resource Realist; Better-Alternative Proposer + Citation Auditor) in parallel, each with evidence-required prompts (independent Python recomputation + live OpenAlex/Crossref/DataCite/Zenodo citation checks).
**Result:** 2 CRITICAL, 4 HIGH, 5 MEDIUM, 6 LOW. **v2.2 NOT publication-ready as-is; fixes applied in v2.3.**

---

## CRITICAL findings

### C1. Classical GNFS core-year count off by 7–9 orders of magnitude (§9.1)
- **Claim:** "approximately $10^9$ core-years on modern hardware" → $E_{\text{classical}} \approx 6.3 \times 10^{18}$ J = 5.8% of world annual electricity.
- **Recomputation:** $2^{112} = 5.19\times10^{33}$ ops. At 10⁸–10¹⁰ ops/s/core → **1.6×10¹⁶–1.6×10¹⁸ core-years**. RSA-768 anchor (2e20 ops / ~10⁴ core-years, Lenstra et al. 2009, implies 6.3e8 ops/s/core) scaled by 2^44.6 → **2.6×10¹⁷ core-years**. The paper's 10⁹ implies 1.6×10¹⁷ ops/s per core — no physical device achieves this.
- **Fix:** E_classical ≈ 1.6×10²⁷ J (range 10²⁶–10²⁸ J); fraction ≈ 10⁷× world annual electricity, not 5.8%.

### C2. §9.2 AES-256 energy contradicts §9.1's own machine model by ~11 orders of magnitude
- **Claim:** $E \approx 3.4\times10^{38}\ \text{ops} \times 10^{-15}\ \text{J/op} \approx 3.4\times10^{23}$ J ≈ 3,200× world electricity.
- **Recomputation:** §9.1's same-class machine: 2.88×10⁻⁵ J per physical gate. The 10⁻¹⁵ J/op assumption implies a machine drawing `E/T = 3.4e23/3.4e28 = 10 µW` — absurd. Corrected: 3.4e38 × 2.9e-5 = **9.8×10³³ J** (≈10¹⁴× world electricity); or P×t = 1 MW × 1.077e21 yr × 3.156e7 = **3.4×10³⁴ J**.
- **Fix:** rebuild §9.2 on §9.1's full-stack power model; state ≥10¹⁴× world electricity.

## HIGH findings

### H1. §9.2 time understated 4–7 orders (oracle evaluations ≠ gates)
- **Claim:** $T \approx 3.4\times10^{38}/10^{10}\ \text{gates/s} \approx 1.1\times10^{21}$ yr (7.8×10¹⁰× universe age).
- **Recomputation:** 10¹⁰ gates/s is 4.1 orders optimistic as a *logical* rate (Gidney–Ekerå: 2.5e10 logical gates/8h = 8.7e5/s); each Grover oracle = full AES-256 circuit (NISTIR 8105 ≈ 2^150 total ops). Corrected: **≥1.08×10²⁵ yr** at 10⁶ gates/s; **4.5×10²⁷ yr** counting 2^150 ops.

### H2. §8.2 atlas (10¹²–10¹⁵ × Landauer) vs §9.1 (2×10²⁰ × Landauer) — basis mismatch, 5–13 orders
- §9.1 verified: per-physical-gate, full-system including idle power (2.88e-5 J/gate ÷ 1.435e-25 J = 2.0e20). §8.2 atlas is per-logical-op marginal energy. Per logical Toffoli full-system: 2.88e10 J ÷ 2.624e9 = 11.0 J = **7.65×10²⁵ × Landauer** — 10–13 orders above the atlas top. A clarifying basis sentence is mandatory.

### H3. §8.2 CMOS CPU row (10³–10⁴ × Landauer) contradicts §8.1's own J/op by ~8 orders
- §8.1: 5×10⁻¹⁰–2×10⁻⁹ J/op = **1.7×10¹¹–7.0×10¹¹ × Landauer(300 K)**. Atlas says CMOS is 10³–10⁴ × Landauer. No basis reconciles them. Atlas rows need a per-transistor/device-level basis label.

### H4. §9.4 summary inherits C1/H1 errors; "10⁵–10⁶×" upper bound unsupported
- §8.1 ratio arithmetic (9e4–3.6e5×) is correct; §9.4's "10⁵–10⁶×" max is 3.56×10⁵. With honest op counts the penalty is ≥10⁶×. Table must be re-derived.

## MEDIUM findings

| # | Finding | Fix |
|---|---------|-----|
| M1 | §8.1 op count 5×10³ inflated 50–500× (trial division to √15 needs ~10–10² ops) | Use 10² ops → J = 5×10⁻⁸–2×10⁻⁷ J → penalty 4.5×10⁶–1.8×10⁷× (state ≥10⁶×); direction conservative |
| M2 | §8.1 text says 10⁻¹⁰–10⁻⁹ J/op; table has 5×10⁻¹⁰–2×10⁻⁹ | Harmonize to "5×10⁻¹⁰–2×10⁻⁹ J per integer op (chip-level)" |
| M3 | §8.1 comparison basis: 0.89 J is incremental-above-idle (P0 §3.3); classical rows chip-level | Add caveat: both biases favor quantum; ratio is a conservative lower bound; uniform-basis check 5.9×10⁴× (full) – 1.8×10⁷× (incremental) |
| M4 | §9.3 "250 systems × 15 kW = 33 GWh" is top-of-range | Add sensitivity: 200–300 × 10–25 kW → 17.5–65.8 GWh/yr; fleet-weighted ~12.5 kW → ~27 GWh central; 33 GWh = upper bound |
| M5 | §9.1 power envelope 0.5–1 MW is an optimistic floor | Relabel "optimistic floor"; central 1–5 MW (up to 10 MW) → E = 2.9×10¹⁰–2.9×10¹¹ J; still 2–7×10⁷× below classical |

## LOW findings

| # | Finding | Fix |
|---|---------|-----|
| L1 | Grover iterations π/4·2^128 = 2.67×10³⁸ vs paper's 3.4×10³⁸ (1.27× high, conservative) | Footnote the π/4 factor |
| L2 | Citation: Yoo title truncated "…Superconducting Qubit" vs "…Quantum Processor Unit Cell" | Correct title |
| L3 | Citation: Fellous-Asiani omits Thonnart (6 authors in record) | Add Thonnart |
| L4 | Citation: Google QEC year (2025) vs OpenAlex 2024 (Nature 638, Dec 2024) | Use 2024 |
| L5 | Own DOI 10.5281/zenodo.21821507 404s on OpenAlex/Crossref but resolves on DataCite (findable) | Note DataCite registration |
| L6 | "~10¹⁵ physical gates" not verifiable from Gidney–Ekerå abstract (abstract-circuit count 2.6×10⁹ Toffolis); "no roadmap within two decades" is opinion in [established] block | Cite the QEC-inclusive figure; re-flag that clause [speculative] |

## Null-hypothesis assessment (per adversary mandate)
- **Classical cannot be cheaper than claimed:** 2¹¹² ops is NIST-sanctioned; even fantasy hardware (10¹³ ops/s/machine) → 1.04×10²³ J ≈ 10³× world electricity — the paper's 6.3×10¹⁸ J is 4–5 OOM below any defensible floor. Direction: quantum's win is LARGER than printed.
- **Quantum could be costlier (shrinking the win):** 1–5 MW central → ratio ≤1 OOM smaller. Defensible ratio range **10¹⁴–10¹⁸**; the paper's 2.2×10⁸ sits 6–9 OOM below the floor.
- **Verdict:** the qualitative conclusions (classical wins on same-task JPCUB; AES-256 immune; RSA-2048 win requires a non-existent machine) all **survive and are strengthened** — but the printed magnitudes were wrong and required correction in v2.3.

## Evidence
- Three subagent reports (sessions `_YBqbs37zGyAEHD-cllKS`, `HjytOYEanFDF0YeT_zg7Z`, `eaGw3e7zUMYr8Ow8GAvZ1`).
- Independent Python recomputation (2^112, core-years, Landauer multiples, Grover figures, fleet energy) — all cited in findings above.
- Live citation checks: OpenAlex/Crossref/DataCite/Zenodo for all 16 DOIs (15 external verified correct; 3 title/author/year nits).

## Status
- **v2.2 → v2.3:** all C1–C2, H1–H4, M1–M5, L1–L6 fixes applied; gates re-run; PDF rebuilt; republished as DOI 10.5281/zenodo.21821551 (v2.3).
