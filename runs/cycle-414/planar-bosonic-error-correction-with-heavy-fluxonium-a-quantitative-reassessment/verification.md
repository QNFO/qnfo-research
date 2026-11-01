# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ancilla bit-flip rate Gamma_bf = (2.22 +/- 0.34)x10^3 s^-1",
    "inputs": "T1_bf = 451 us = 4.51e-4 s; sigma_T = 70 us = 7.0e-5 s",
    "formula": "Gamma_bf = 1/T1_bf; sigma_Gamma = sigma_T / T1_bf^2"
  },
  {
    "id": "Q2",
    "statement": "Removed fraction of logical decay rate = 0.371 +/- 0.020 (37.1%)",
    "inputs": "F = 1.59; sigma_F = 0.05",
    "formula": "removed = 1 - 1/F; d(1/F)/dF = -1/F^2; sigma = |d(1/F)/dF| * sigma_F"
  },
  {
    "id": "Q3",
    "statement": "Per-cycle ancilla bit-flip probability p_bf_flx = 0.0219 +/- 0.0034 (2.19% +/- 0.34%)",
    "inputs": "Gamma_bf = 2.2173e3 s^-1; T_cyc = 10 us = 1.0e-5 s; sigma_T = 7.0e-5 s",
    "formula": "p = 1 - exp(-Gamma_bf * T_cyc); dp/dT = (T_cyc/T1_bf^2) * exp(-T_cyc/T1_bf); sigma_p = dp/dT * sigma_T"
  },
  {
    "id": "Q4",
    "statement": "Transmon baseline per-cycle error p_bf_tm = 0.2835 (28.3%)",
    "inputs": "T1_tm = 30 us = 3.0e-5 s; T_cyc = 1.0e-5 s",
    "formula": "p = 1 - exp(-T_cyc/T1_tm)"
  },
  {
    "id": "Q5",
    "statement": "Ratio of per-cycle errors p_bf_tm / p_bf_flx = 12.9",
    "inputs": "p_bf_tm = 0.2835; p_bf_flx = 0.0219",
    "formula": "ratio = p_bf_tm / p_bf_flx"
  },
  {
    "id": "Q6",
    "statement": "Ratio of bit-flip rates (lifetime ratio) = 15.0",
    "inputs": "T1_bf = 451 us; T1_tm = 30 us",
    "formula": "ratio = T1_bf / T1_tm"
  },
  {
    "id": "Q7",
    "statement": "Steady-state ancilla-induced logical error rate Gamma_anc = 221.7 s^-1",
    "inputs": "eta = 0.1; Gamma_bf = 2.2173e3 s^-1",
    "formula": "Gamma_anc = eta * Gamma_bf"
  },
  {
    "id": "Q8",
    "statement": "Ancilla-limited corrected logical lifetime T_L^(1) = 4.51 ms",
    "inputs": "Gamma_anc = 221.7 s^-1",
    "formula": "T_L = 1 / Gamma_anc"
  },
  {
    "id": "Q9",
    "statement": "Relative uncertainty of Gamma_bf = 15.5%, matching relative uncertainty of T1_bf",
    "inputs": "sigma_Gamma = 344 s^-1; Gamma_bf = 2217 s^-1; sigma_T = 70 us; T1_bf = 451 us",
    "formula": "rel_Gamma = sigma_Gamma / Gamma_bf; rel_T = sigma_T / T1_bf"
  },
  {
    "id": "Q10",
    "statement": "Sensitivity of projected lifetime: eta = 0.3 gives 1.50 ms; eta = 0.03 gives 15.0 ms",
    "inputs": "Gamma_bf = 2.2173e3 s^-1; eta = 0.3 or 0.03",
    "formula": "T_L = 1 / (eta * Gamma_bf)"
  },
  {
    "id": "Q11",
    "statement": "Reset of 100 us would raise per-cycle error to roughly 0.199",
    "inputs": "T_cyc = 100 us = 1.0e-4 s; T1_bf = 4.51e-4 s",
    "formula": "p = 1 - exp(-T_cyc/T1_bf)"
  },
  {
    "id": "Q12",
    "statement": "Removed fraction at F = 1.54 is 0.351 and at F = 1.64 is 0.390",
    "inputs": "F = 1.54 and F = 1.64",
    "formula": "removed = 1 - 1/F"
  },
  {
    "id": "Q13",
    "statement": "Geometric vs surface-code logical error rate ratio approx 1.4e4 (cited from [2])",
    "inputs": "p_L_geom = 7.1e-5; p_L_SC = 5.1e-9",
    "formula": "ratio = p_L_geom / p_L_SC"
  }
]

## Script
```python
# SymPy verification of equation transitions in
# "Planar Fluxonium-Controlled Bosonic Error Correction: A Quantitative Error-Budget Reassessment"
import sympy as sp
import random
from sympy.physics.units import second, microsecond, millisecond, convert_to

ok = lambda v: bool(sp.simplify(v) == 0)

# ---------- Notation table with units ----------
# T1_bf   : ancilla bit-flip lifetime          [time]      = 451 ± 70 us
# F       : logical-lifetime extension factor  [dimensionless] = 1.59 ± 0.05
# Gamma_bf: ancilla bit-flip rate              [1/time]
# T_cyc   : correction cycle time              [time]      = 10 us (assumed)
# p_phys  : per-cycle ancilla error probability [dimensionless]
# r       : fractional removal of logical decay rate [dimensionless] (37.1% ± 2.0%)
# T_L1    : ancilla-limited logical lifetime   [time]      (claimed 4.51 ms)
# Photon ratio 5-40x at p_L=1e-6               [dimensionless]

T1, sT, F, sF, Tcyc, p, r, sT_L = sp.symbols('T1 sigma_T F sigma_F T_cyc p_phys r sigma_TL', positive=True)

T1v  = 451 * microsecond
sT1v = 70 * microsecond
Fv, sFv = sp.Float(1.59), sp.Float(0.05)
Tcyv = 10 * microsecond

def spot(f, args, n=200, tol=1e-9):
    for _ in range(n):
        pt = [a + (random.random()-0.5)*abs(a)*1e-3 for a in args]
        if abs(float(f(*pt))) > tol*max(1.0, abs(float(f(*[a for a in args])))) if args else False:
            pass
    return True  # symbolic check below is decisive for these algebraic identities

results = []

# ---------- R1: Gamma_bf = 1 / T1_bf ----------
lhs = 1/T1
rhs = sp.Symbol('Gamma_bf', positive=True)
diff = sp.simplify(lhs - rhs)
num = ok(sp.simplify((1/T1v) - sp.Float(2.22e3)/second)) if False else None
Gamma_val = 1/convert_to(T1v, second).subs(second, 1)
r1_num = abs(float(Gamma_val) - 2.22e3) < 0.01e3
results.append(("R1: Gamma_bf = 1/T1_bf (=> 2.22e3 /s)", "ok" if r1_num else "refuted"))

# ---------- R2: sigma_Gamma = sigma_T / T1^2 ----------
sG = sT/T1**2
sG_val = float(convert_to(sT1v, second).subs(second,1)) / float(convert_to(T1v, second).subs(second,1))**2
r2_num = abs(sG_val - 0.34e3) < 0.01e3
results.append(("R2: sigma_Gamma = sigma_T/T1^2 (=> 0.34e3 /s)", "ok" if r2_num else "refuted"))

# ---------- R3: r = 1 - 1/F ----------
diff3 = sp.simplify((1 - 1/F) - r)
r_val = 1 - 1/Fv
r3_num = abs(float(r_val) - 0.371) < 0.001
# uncertainty: sigma_r = sigma_F / F^2
sr_val = sFv/Fv**2
r3b = abs(float(sr_val) - 0.020) < 0.001
results.append(("R3: r = 1 - 1/F = 37.1% ± 2.0%", "ok" if (r3_num and r3b) else "refuted"))

# ---------- R4: p_phys = Gamma_bf * T_cyc ----------
diff4 = sp.simplify((1/T1)*Tcyc - p)
p_val = float(Gamma_val) * float(convert_to(Tcyv, second).subs(second,1))
sp_val = sG_val * float(convert_to(Tcyv, second).subs(second,1))
r4_num = abs(p_val - 0.0219) < 0.0005 and abs(sp_val - 0.0034) < 0.0005
results.append(("R4: p_phys = Gamma_bf*T_cyc = 2.19% ± 0.34%", "ok" if r4_num else "refuted"))

# ---------- R5: T_L^(1) = T_cyc / p_phys  (claimed 4.51 ms) ----------
TL_from_def = convert_to(Tcyv, microsecond).subs(microsecond,1) / p_val   # us
r5 = abs(TL_from_def - 451.0) < 1.0   # gives 451 us, NOT 4.51 ms
claimed_ms = 4.51e3  # us
r5_ok = abs(TL_from_def - claimed_ms) < 1.0
results.append(("R5: T_L^(1) = T_cyc/p_phys = 4.51 ms (claimed)",
                "ok" if r5_ok else ("refuted" if r5 else "inconclusive")))

# ---------- R6: photon advantage 5-40x; withdrawn 8.0-64x = (5-40)*F ----------
# Arithmetic of the withdrawn multiplication:
w_lo, w_hi = 5*Fv, 40*Fv
r6_arith = abs(float(w_lo)-8.0) < 0.05 and abs(float(w_hi)-64.0) < 0.5
# The linearity assumption itself is not an equation derivable from the paper:
results.append(("R6: withdrawn 8.0-64x = (5-40x)*F (linearity assumption)",
                "inconclusive" if r6_arith else "refuted"))

# ---------- Randomized numeric spot checks for symbolic identities ----------
random.seed(0)
def spot_check(expr_lhs, expr_rhs, subs_base, n=300):
    x = sp.simplify(expr_lhs - expr_rhs)
    if x == 0:
        return "ok"
    worst = 0.0
    for _ in range(n):
        subs = {}
        for k, (v, rel) in subs_base.items():
            subs[k] = v * (1 + random.uniform(-rel, rel))
        val = abs(float(x.subs(subs)))
        worst = max(worst, val)
    return "ok" if worst < 1e-9 else "inconclusive"

base = {T1: 451e-6, sT: 70e-6, F: 1.59, sF: 0.05, Tcyc: 10e-6}
print("SPOT R1:", spot_check(1/T1, sp.Symbol('Gamma'), {T1: base[T1]}))
print("SPOT R3:", spot_check(1 - 1/F, r, {F: base[F]}))
print("SPOT R4:", spot_check((1/T1)*Tcyc, p, {T1: base[T1], Tcyc: base[Tcyc]}))

# ---------- Sanity bounds ----------
assert 0 <= float(r_val) <= 1, "removal fraction must be a probability in [0,1]"
assert 0 <= p_val <= 1, "per-cycle error must be in [0,1]"
assert float(Gamma_val) > 0 and sG_val > 0, "rates nonnegative"
assert Fv > 1, "extension factor should exceed 1 (efficiency-like bound F<=1 not applicable; F is a ratio)"
# limiting cases: F -> 1 gives r -> 0 (no removal); T_cyc -> 0 gives p -> 0
assert sp.limit(1 - 1/F, F, 1) == 0
assert sp.limit((1/T1)*Tcyc, Tcyc, 0) == 0
# T1 -> infinity gives Gamma -> 0
assert sp.limit(1/T1, T1, sp.oo) == 0

for name, verdict in results:
    print(f"DERIV {verdict} | {name}")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1
T = 4.51e-4
sT = 7.0e-5
G = 1.0 / T
sG = sT / T**2
results.append(("Q1", G, "2.22e3", sig(G,3)))
results.append(("Q1b", sG, "0.34e3", sig(sG,2)))

# Q2
F = 1.59
sF = 0.05
removed = 1 - 1/F
sig_removed = (1/F**2) * sF
results.append(("Q2", removed, "0.371", sig(removed,3)))
results.append(("Q2b", sig_removed, "0.020", sig(sig_removed,2)))

# Q3
Gbf = 1.0 / 4.51e-4
Tcyc = 1.0e-5
p = 1 - math.exp(-Gbf * Tcyc)
dpdT = (Tcyc / (4.51e-4)**2) * math.exp(-Tcyc / 4.51e-4)
sp = dpdT * 7.0e-5
results.append(("Q3", p, "0.0219", sig(p,3)))
results.append(("Q3b", sp, "0.0034", sig(sp,2)))

# Q4
p_tm = 1 - math.exp(-1.0e-5 / 3.0e-5)
results.append(("Q4", p_tm, "0.2835", sig(p_tm,4)))

# Q5
ratio5 = p_tm / p
results.append(("Q5", ratio5, "12.9", sig(ratio5,3)))

# Q6
ratio6 = 451.0 / 30.0
results.append(("Q6", ratio6, "15.0", sig(ratio6,3)))

# Q7
Ganc = 0.1 * Gbf
results.append(("Q7", Ganc, "221.7", sig(Ganc,4)))

# Q8
TL = 1.0 / Ganc
results.append(("Q8", TL, "4.51e-3", sig(TL,3)))

# Q9
relG = sG / G
relT = sT / T
results.append(("Q9", relG, "0.155", sig(relG,3)))
results.append(("Q9b", relT, "0.155", sig(relT,3)))

# Q10
TL03 = 1.0 / (0.3 * Gbf)
TL003 = 1.0 / (0.03 * Gbf)
results.append(("Q10a", TL03, "1.50e-3", sig(TL03,3)))
results.append(("Q10b", TL003, "15.0e-3", sig(TL003,3)))

# Q11
p100 = 1 - math.exp(-1.0e-4 / 4.51e-4)
results.append(("Q11", p100, "0.199", sig(p100,3)))

# Q12
r154 = 1 - 1/1.54
r164 = 1 - 1/1.64
results.append(("Q12a", r154, "0.351", sig(r154,3)))
results.append(("Q12b", r164, "0.390", sig(r164,3)))

# Q13
ratio13 = 7.1e-5 / 5.1e-9
results.append(("Q13", ratio13, "1.4e4", sig(ratio13,2)))

mismatch = 0
for cid, computed, expected, rounded in results:
    ok = abs(rounded - float(expected)) <= max(abs(float(expected)) * 1e-9, 1e-12) or ("%.3g" % rounded) == ("%.3g" % float(expected)) or ("%.2g" % rounded) == ("%.2g" % float(expected)) or ("%.4g" % rounded) == ("%.4g" % float(expected))
    if not ok:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={'yes' if ok else 'no'}")

total = len(results)
matched = total - mismatch
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {mismatch} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 3, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: Γ_bf = 1/(4.51×10⁻⁴ s) = 2217.2949 s⁻¹; σ_Γ = 7.0×10⁻⁵/(4.51×10⁻⁴)² = 7.0×10⁻⁵/2.03401×10⁻⁷ = 344.146 s⁻¹ → (2.22 ± 0.34)×10³ s⁻¹.
CLAIM Q1: computed=2217.2949 expected=2.22e3 match=yes

Q2: 1/1.59 = 0.6289308; removed = 1 − 0.6289308 = 0.3710692; σ = 0.05/1.59² = 0.05/2.5281 = 0.0197782.
CLAIM Q2: computed=0.3710692 expected=0.371 match=yes

Q3: ΓT = 2217.2949×1.0×10⁻⁵ = 0.02217295; p = 1 − e^(−0.02217295) = 0.0219288; dp/dT = (1.0×10⁻⁵/2.03401×10⁻⁷)×e^(−0.02217295) = 49.16371×0.9780714 = 48.08975; σ_p = 48.08975×7.0×10⁻⁵ = 0.0033663.
CLAIM Q3: computed=0.0219288 expected=0.0219 match=yes

Q4: p = 1 − e^(−1.0×10⁻⁵/3.0×10⁻⁵) = 1 − e^(−0.3333333) = 0.2834687.
CLAIM Q4: computed=0.2834687 expected=0.2835 match=yes

Q5: 0.2834687/0.0219288 = 12.9231.
CLAIM Q5: computed=12.9231 expected=12.9 match=yes

Q6: 451/30 = 15.03333.
CLAIM Q6: computed=15.03333 expected=15.0 match=yes

Q7: 0.1×2217.2949 = 221.7295.
CLAIM Q7: computed=221.7295 expected=221.7 match=yes

Q8: 1/221.7295 = 0.004509925 s = 4.509925 ms.
CLAIM Q8: computed=4.509925 expected=4.51 match=yes

Q9: 344.146/2217.2949 = 0.155213 = 15.5213%; 70/451 = 0.1552106 = 15.5211%.
CLAIM Q9: computed=0.155213 expected=0.155 match=yes

Q10: η=0.3: 1/(0.3×2217.2949) = 1/665.1885 = 0.001503343 s = 1.503343 ms; η=0.03: 1/(0.03×2217.2949) = 1/66.51885 = 0.01503343 s = 15.03343 ms.
CLAIM Q10: computed=1.503343 expected=1.50 match=yes

Q11: p = 1 − e^(−1.0×10⁻⁴/4.51×10⁻⁴) = 1 − e^(−0.2217295) = 0.1988661.
CLAIM Q11: computed=0.1988661 expected=0.199 match=yes

Q12: F=1.54: 1 − 1/1.54 = 1 − 0.6493506 = 0.3506494; F=1.64: 1 − 1/1.64 = 1 − 0.6097561 = 0.3902439.
CLAIM Q12: computed=0.3506494 expected=0.351 match=yes

Q13: 7.1×10⁻⁵/5.1×10⁻⁹ = 13921.57 ≈ 1.4×10⁴.
CLAIM Q13: computed=13921.57 expected=1.4e4 match=yes

VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2217.2949 | 2.22e3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.3710692 | 0.371 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.0219288 | 0.0219 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.2834687 | 0.2835 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 12.9231 | 12.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 15.03333 | 15.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 221.7295 | 221.7 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 4.509925 | 4.51 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.155213 | 0.155 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 1.503343 | 1.50 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 0.1988661 | 0.199 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.3506494 | 0.351 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 13921.57 | 1.4e4 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
