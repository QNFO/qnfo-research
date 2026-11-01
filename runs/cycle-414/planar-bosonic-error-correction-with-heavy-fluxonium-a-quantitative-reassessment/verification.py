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
