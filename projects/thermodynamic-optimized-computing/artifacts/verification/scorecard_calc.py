#!/usr/bin/env python3
"""Scorecard computation for QNFO.JPC.002 (P4).

Computes energy per correct solution per platform from the scorecard-data
parameters. Active-correction platforms use the MEASURED surface-code
calibration (d=7 -> 0.143%/cycle, Lambda = 2.14 per +2 distance, arXiv:2408.13687).
Protected platforms use the thermal-activation law L = exp(-Delta/k_B T).

Stdlib only. Run: python scorecard_calc.py
Output: outputs/scorecard_results.csv + console table.
"""
import math, csv, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

K_B    = 1.380649e-23
N_OPS  = 1e6          # benchmark: 1e6 logical operations
L_TARGET = 1e-7       # logical error per cycle giving P(correct) ~ 0.90
L7     = 1.43e-3      # measured d=7 logical error per cycle
LAM    = 2.14         # measured suppression per +2 distance

def distance_for(L_target):
    d, L = 7, L7
    while L > L_target and d < 201:
        d += 2
        L /= LAM
    return d, L

def E_active(E_op, d):
    overhead = (2 * d - 1) ** 2
    return E_op * overhead * N_OPS, overhead

def E_passive(E_op, Delta, T):
    L = math.exp(-Delta / (K_B * T))
    nL = N_OPS * L
    if nL > 700.0:
        return float("inf"), L, 0.0
    p_ok = math.exp(-nL)
    return E_op * N_OPS / p_ok, L, p_ok

platforms = [
    # name, strategy, p (context), E_op, T, Delta
    ("Superconducting transmon + surface code", "active", 1.5e-3, 8.21e-25, 0.015, None),
    ("Trapped ion + surface code",            "active", 1.0e-3, 1.00e-17, 0.015, None),
    ("Silicon spin + surface code",           "active", 1.0e-3, 1.00e-18, 1.000, None),
    ("Photonic (fusion) + lattice code",      "active", 1.0e-2, 1.00e-12, 300.0, None),
    ("Topological Majorana InAs/Al (~200 ueV gap)", "passive", None, 8.21e-25, 0.020, 3.00e-23),
    ("Topological Majorana PbTe/Pb (~1 meV gap)",    "passive", None, 8.21e-25, 0.020, 1.60e-22),
]

header = ["platform", "strategy", "p_physical", "T_K", "Delta_J",
          "distance_d", "logical_error_L", "overhead", "P_correct",
          "E_per_correct_solution_J"]

rows = []
for name, strat, p, E_op, T, Delta in platforms:
    if strat == "active":
        d, L = distance_for(L_TARGET)
        E, overhead = E_active(E_op, d)
        p_ok = math.exp(-N_OPS * L)
        rows.append([name, strat, f"{p:.1e}" if p else "n/a", T, "",
                     d, f"{L:.2e}", overhead, f"{p_ok:.3f}", f"{E:.3e}"])
    else:
        E, L, p_ok = E_passive(E_op, Delta, T)
        rows.append([name, strat, "n/a", T, f"{Delta:.2e}",
                     "", f"{L:.1e}", 1, f"{p_ok:.3f}" if p_ok > 0 else "0",
                     f"{E:.3e}"])

with open(os.path.join(OUT, "scorecard_results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

print(",".join(header))
for r in rows:
    print(",".join(map(str, r)))

# Sensitivity: control-electronics multiplier common to all platforms.
print("\nControl-electronics sensitivity (C_ctrl in [1e4, 1e6]):")
for r in rows[:2] + rows[4:]:
    if r[1] == "active":
        E_base = float(r[9])
        print(f"  {r[0]:52s} quantum-level {E_base:.3e} J -> "
              f"system-level [{E_base*1e4:.1e}, {E_base*1e6:.1e}] J")
    else:
        E_base = float(r[9])
        print(f"  {r[0]:52s} quantum-level {E_base:.3e} J -> "
              f"system-level [{E_base*1e4:.1e}, {E_base*1e6:.1e}] J")
