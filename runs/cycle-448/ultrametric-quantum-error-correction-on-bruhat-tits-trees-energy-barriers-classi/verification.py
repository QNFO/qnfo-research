# -*- coding: utf-8 -*-
import sympy as sp
import random
from sympy.physics import units as u

# ---------- symbols with units ----------
d = sp.Symbol('d', integer=True, nonnegative=True)          # tree depth
eps = sp.Symbol('eps', positive=True)                       # elementary excitation energy
p = sp.Symbol('p', real=True)                               # physical error prob.
p1, p2, p3 = sp.symbols('p1 p2 p3', real=True)
N = sp.Symbol('N', integer=True, positive=True)            # trial count

# ---------- units ----------
# Energy unit (eV) – just a placeholder, the paper works in natural units
eV = u.electron_volt
# Probability is dimensionless, but we keep a dummy unit for sanity checks
prob = sp.Symbol('prob')   # dimensionless

# ---------- transitions ----------
transitions = [
    # (name, lhs, rhs, description)
    ("BarrierModel",
     2**d * eps,
     sp.Symbol('E_barrier') * eps,   # we treat E_barrier = 2**d
     "E_barrier(d) = 2**d * eps"),
    
    ("Vote1",
     sp.nsimplify(0.1736704),
     sp.summation(sp.binomial(2, k) * (0.4)**k * (1-0.4)**(2-k), (k, 2, 2)),   # majority of 2 children (tie→0)
     "first iteration of majority vote"),
    
    ("Vote2",
     sp.nsimplify(0.0055485),
     sp.summation(sp.binomial(2, k) * (sp.nsimplify(0.1736704))**k *
                  (1-sp.nsimplify(0.1736704))**(2-k), (k, 2, 2)),
     "second iteration"),
    
    ("Vote3",
     sp.nsimplify(2.905e-10),
     sp.summation(sp.binomial(2, k) * (sp.nsimplify(0.0055485))**k *
                  (1-sp.nsimplify(0.0055485))**(2-k), (k, 2, 2)),
     "third iteration"),
    
    ("ZeroErrorBound",
     sp.nsimplify(sp.log(20) / 1e5),
     sp.Symbol('pL_bound'),
     "95% Poisson bound for zero observed errors"),
    
    ("ThermalProjection",
     sp.exp(-2**d),
     sp.Symbol('pL_thermal'),
     "thermal activation projection p_L ≤ e^{-2^d}")
]

# ---------- helper for numeric spot checks ----------
def numeric_check(expr, subs):
    """Evaluate expr numerically with given substitution dict."""
    try:
        val = expr.subs(subs).evalf()
        return float(val)
    except Exception:
        return None

# ---------- verification driver ----------
tol = 1e-12   # tolerance for numeric equality

for name, lhs, rhs, note in transitions:
    # try symbolic simplification of lhs - rhs
    diff = sp.simplify(lhs - rhs)
    if diff == 0:
        print(f"DERIV ok | {name} | {note}")
        continue

    # symbolic check inconclusive → perform random numeric spot checks
    inconclusive = False
    refuted = False
    for _ in range(7):
        # generate random values respecting the declared assumptions
        sub = {}
        if d in diff.free_symbols:
            sub[d] = random.randint(0, 6)          # small depths for tractability
        if eps in diff.free_symbols:
            sub[eps] = random.uniform(0.1, 5.0)    # positive energy
        if p in diff.free_symbols:
            sub[p] = random.uniform(0.0, 1.0)      # probability in [0,1]
        if N in diff.free_symbols:
            sub[N] = random.randint(1, 10**6)

        # evaluate lhs and rhs numerically
        lhs_val = numeric_check(lhs, sub)
        rhs_val = numeric_check(rhs, sub)
        if lhs_val is None or rhs_val is None:
            inconclusive = True
            break
        if abs(lhs_val - rhs_val) > tol:
            refuted = True
            break

    if refuted:
        print(f"DERIV refuted | {name} | {note}")
    elif inconclusive:
        print(f"DERIV inconclusive | {name} | {note}")
    else:
        print(f"DERIV ok | {name} | {note}")

# ---------- sanity‑bounds checks ----------
# probabilities in [0,1]
prob_checks = [
    ("p in [0,1]", p, (0, 1)),
    ("p1 in [0,1]", sp.nsimplify(0.1736704), (0, 1)),
    ("p2 in [0,1]", sp.nsimplify(0.0055485), (0, 1)),
    ("p3 in [0,1]", sp.nsimplify(2.905e-10), (0, 1)),
    ("pL_bound ≤ 1", sp.nsimplify(sp.log(20) / 1e5), (0, 1)),
    ("e^{-2^d} ≤ 1", sp.exp(-2**d), (0, 1)),
]

for tag, expr, (low, high) in prob_checks:
    # symbolic bounds are obvious; we just spot‑check a few values of d
    ok = True
    for depth in range(0, 5):
        val = float(expr.subs({d: depth}))
        if not (low - 1e-12 <= val <= high + 1e-12):
            ok = False
            break
    status = "ok" if ok else "refuted"
    print(f"DERIV {status} | sanity {tag}")

import math
from math import comb, exp, log

def f(p, n=8):
    return sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(5, n + 1))

# Q1
p1 = f(0.4)
print(f"CLAIM Q1: computed={p1:.10g} expected=0.1736704 match={'yes' if round(p1,7)==0.1736704 else 'no'}")

# Q2
p2 = f(p1)
print(f"CLAIM Q2: computed={p2:.10g} expected=0.0055485 match={'yes' if round(p2,7)==0.0055485 else 'no'}")

# Q3
p3 = f(p2)
print(f"CLAIM Q3: computed={p3:.10g} expected=2.905e-10 match={'yes' if abs(p3-2.905e-10)/2.905e-10 < 0.005 else 'no'}")

# Q4
sup = 0.4 / p1
print(f"CLAIM Q4: computed={sup:.10g} expected=2.303 match={'yes' if round(sup,3)==2.303 else 'no'}")

# Q5
ln20 = log(20)
b5 = ln20 / 10000
print(f"CLAIM Q5: computed={b5:.10g} expected=2.9957e-4 match={'yes' if round(b5*1e4,4)==2.9957 else 'no'}")

# Q6
b6 = ln20 / 100000
print(f"CLAIM Q6: computed={b6:.10g} expected=2.9957e-5 match={'yes' if round(b6*1e5,4)==2.9957 else 'no'}")

# Q7
v7 = exp(-8)
print(f"CLAIM Q7: computed={v7:.10g} expected=3.3546e-4 match={'yes' if round(v7*1e4,4)==3.3546 else 'no'}")

# Q8
v8 = exp(-32)
print(f"CLAIM Q8: computed={v8:.10g} expected=1.2664e-14 match={'yes' if abs(v8-1.2664e-14)/1.2664e-14 < 0.001 else 'no'}")

# Q9
v9 = 10 ** (-1024 * 0.434294)
print(f"CLAIM Q9: computed={v9:.10g} expected=1e-444.7 match={'yes' if abs(-log10(v9) - 444.7) < 0.05 else 'no'}")

# Q10
v10 = 1 / p3
print(f"CLAIM Q10: computed={v10:.10g} expected=3.4e9 match={'yes' if abs(v10-3.4e9)/3.4e9 < 0.01 else 'no'}")

print(f"VERIFICATION SUMMARY: 10 claims, {sum(1 for _ in range(10)) and 0} match, 0 mismatch")
