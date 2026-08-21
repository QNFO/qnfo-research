#!/usr/bin/env python3
"""Thermodynamic golden-value verification for QNFO.JPC.002 (P3).

Computes the fundamental thermodynamic bounds and corpus anchors used by the
paper. Standard library only. Run: python thermo_bounds.py
Output: artifacts/verification/outputs/thermo_bounds.csv + console table.
"""
import math, csv, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

K_B  = 1.380649e-23     # J/K   (exact, SI 2019)
H    = 6.62607015e-34   # J s   (exact, SI 2019)
HBAR = H / (2.0 * math.pi)
C    = 2.99792458e8     # m/s   (exact)

def landauer(T_K: float) -> float:
    return K_B * T_K * math.log(2.0)

def margolus_levitin(dt_s: float) -> float:
    return math.pi * HBAR / (2.0 * dt_s)

def bremermann() -> float:
    """Canonical Bremermann bound uses h (not hbar): c^2/h bits per second per kg."""
    return C * C / H

rows = []

for T in (300.0, 77.0, 4.0, 1.0, 0.015):
    rows.append(("Landauer", f"{T} K", landauer(T), "J/bit"))

for dt in (1e-9, 1e-10, 1e-12):
    rows.append(("Margolus-Levitin", f"{dt:.0e} s/op", margolus_levitin(dt), "J/op"))

rows.append(("Bremermann", "c^2/h", bremermann(), "bit/s/kg"))
rows.append(("Bremermann-variant", "c^2/hbar", C * C / HBAR, "rad/s/kg"))

# Corpus anchor recomputation (Rosetta Axis 3, importance-0.85 program memory):
# R = k_B * T * ln(1/alpha_r), T = 15 mK, alpha_r = 1.9%
ALPHA_R, T_OP = 0.019, 0.015
rosetta = K_B * T_OP * math.log(1.0 / ALPHA_R)
rows.append(("Rosetta-Constant", "k_B*15mK*ln(1/0.019)", rosetta, "J/gate"))

# QEC overhead arithmetic (Qubit Delusion: 1e2..1e3 multiplier on thermodynamic cost)
rows.append(("Logical-gate-E-lo", "Rosetta*1e2", rosetta * 1e2, "J/logical gate"))
rows.append(("Logical-gate-E-hi", "Rosetta*1e3", rosetta * 1e3, "J/logical gate"))

# Tree-code vs surface-code threshold ratio (corpus: p_th 2.0e-4 vs 1.1e-2)
P_TREE, P_SURF = 2.0e-4, 1.1e-2
rows.append(("Threshold-ratio", "p_surf/p_tree", P_SURF / P_TREE, "dimensionless"))

# Self-checks (assert expected values within tolerance)
EXPECT = {
    "Landauer 300 K": 2.871e-21, "Landauer 15 mK": 1.435e-25,
    "Margolus-Levitin 1e-09": 1.656e-25,
    "Rosetta-Constant": 8.2e-25, "Threshold-ratio": 55.0,
}
checks = {
    "Landauer 300 K": rows[0][2], "Landauer 15 mK": rows[4][2],
    "Margolus-Levitin 1e-09": rows[5][2],
    "Rosetta-Constant": rows[10][2], "Threshold-ratio": rows[13][2],
}
failures = 0
for name, expected in EXPECT.items():
    got = checks[name]
    ok = abs(got - expected) / expected < 0.05
    print(f"CHECK {name}: got={got:.4e} expected~{expected:.4e} {'PASS' if ok else 'FAIL'}")
    failures += (not ok)

with open(os.path.join(OUT, "thermo_bounds.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["quantity", "parameter", "value_SI", "unit"])
    w.writerows(rows)

print()
for q, p, v, u in rows:
    print(f"{q:18s} {p:22s} {v:.6e} {u}")
print(f"\nSELF-CHECK: {'ALL PASS' if failures == 0 else f'{failures} FAILURES'}")
