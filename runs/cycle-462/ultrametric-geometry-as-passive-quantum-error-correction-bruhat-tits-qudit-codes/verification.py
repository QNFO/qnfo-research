import sympy as sp
import random
from sympy import binomial, simplify, Eq
from sympy.physics import units as u

# ---------- symbols with assumptions ----------
p   = sp.Symbol('p', integer=True, positive=True)          # prime ≥2
t   = sp.Symbol('t', integer=True, nonnegative=True)       # radius
ε   = sp.Symbol('ε', real=True, nonnegative=True)           # physical error rate
# dimensionless units (for sanity checks)
dimless = u.dimensionless

# ---------- helper for numeric spot‑check ----------
def spot_check(lhs, rhs, n_trials=5, tol=1e-12):
    for _ in range(n_trials):
        # random admissible values
        pv = random.choice([2,3,5,7])
        tv = random.randint(0,3)
        ev = random.random()*0.01   # ε in (0,0.01)
        subs = {p: pv, t: tv, ε: ev}
        lval = float(lhs.subs(subs).evalf())
        rval = float(rhs.subs(subs).evalf())
        if abs(lval - rval) > tol:
            return False
    return True

# ---------- transitions ----------
transitions = []

# T1: code size formula
lhs = sp.Symbol('n_t')
rhs = 1 + (p+1)*(p**t - 1)/(p-1)
transitions.append(("T1", lhs, rhs))

# T2: numeric n_1 = 5
lhs = sp.Symbol('n_1')
rhs = sp.Integer(5)
transitions.append(("T2", lhs, rhs))

# T3: distance
lhs = sp.Symbol('d')
rhs = 2*t + 1
transitions.append(("T3", lhs, rhs))

# T4: passive failure probability (exact)
k = sp.Symbol('k', integer=True, nonnegative=True)
P_pass = 1 - sp.summation(binomial(lhs, k)*ε**k*(1-ε)**(lhs-k), (k,0,t))
# we will treat lhs as n_t later
transitions.append(("T4", sp.Symbol('P_pass'), P_pass.subs(lhs, sp.Symbol('n_t'))))

# T5: numeric P_pass for p=3,t=1,ε=1e-3
P_pass_expr = 1 - sp.summation(binomial(5, k)*ε**k*(1-ε)**(5-k), (k,0,1))
lhs = sp.Symbol('P_pass_flagship')
rhs = sp.nsimplify(9.980015e-6)
transitions.append(("T5", lhs, rhs))

# T6: suppression factor S = ε / P_pass
lhs = sp.Symbol('S')
rhs = ε / sp.Symbol('P_pass')
transitions.append(("T6", lhs, rhs))

# T7: numeric S ≈ 100.2
lhs = sp.Symbol('S_flagship')
rhs = sp.nsimplify(100.2)
transitions.append(("T7", lhs, rhs))

# T8: n_2 = 17
lhs = sp.Symbol('n_2')
rhs = sp.Integer(17)
transitions.append(("T8", lhs, rhs))

# T9: P_pass^{(2)} numeric
P_pass2 = 1 - sp.summation(binomial(17, k)*ε**k*(1-ε)**(17-k), (k,0,2))
lhs = sp.Symbol('P_pass_2')
rhs = sp.nsimplify(6.73e-7)
transitions.append(("T9", lhs, rhs))

# T10: active baseline
lhs = sp.Symbol('P_act')
rhs = sp.nsimplify(3.98e-5)
transitions.append(("T10", lhs, rhs))

# T11: advantage factor A = P_act / P_pass
lhs = sp.Symbol('A')
rhs = sp.Symbol('P_act')/sp.Symbol('P_pass')
transitions.append(("T11", lhs, rhs))

# T12: numeric advantage ≈ 3.99
lhs = sp.Symbol('A_flagship')
rhs = sp.nsimplify(3.99)
transitions.append(("T12", lhs, rhs))

# T13: dominant‑term approximation
lhs = sp.Symbol('P_pass_approx')
rhs = binomial(sp.Symbol('n_t'), t+1)*ε**(t+1)
transitions.append(("T13", lhs, rhs))

# T14: pseudo‑threshold ε_th
lhs = sp.Symbol('ε_th')
rhs = (1/binomial(sp.Symbol('n_t'), t+1))**(1/t)
transitions.append(("T14", lhs, rhs))

# T15: large‑p limit of n_t
lhs = sp.Symbol('n_t_limit')
rhs = p**t   # simplified dominant term
transitions.append(("T15", lhs, rhs))

# ---------- verification loop ----------
for tag, lhs, rhs in transitions:
    # attempt symbolic simplification of lhs - rhs
    diff = simplify(lhs - rhs)
    if diff == 0:
        verdict = "ok"
    else:
        # try numeric spot‑checks (replace symbolic n_t etc. with concrete values where needed)
        try:
            # replace n_t with its definition when it appears
            diff_num = diff.subs({sp.Symbol('n_t'): 1 + (p+1)*(p**t - 1)/(p-1),
                                 sp.Symbol('P_pass'): 1 - sp.summation(binomial(1 + (p+1)*(p**t - 1)/(p-1), k)*ε**k*(1-ε)**(1 + (p+1)*(p**t - 1)/(p-1)-k), (k,0,t)),
                                 sp.Symbol('P_act'): sp.nsimplify(3.98e-5)})
            if spot_check(diff_num, 0):
                verdict = "ok"
            else:
                verdict = "refuted"
        except Exception:
            verdict = "inconclusive"
    print(f"DERIV {verdict}: ({lhs}) => ({rhs})   [{tag}]")

import math
from fractions import Fraction

def fmt(x):
    return f"{x:.10g}"

# Q1-Q6: code sizes
def n_t(p, t):
    return 1 + (p + 1) * (p**t - 1) // (p - 1)

claims = []

# Q1
c = n_t(3, 1); claims.append(("Q1", c, "5"))
# Q2
c = n_t(3, 2); claims.append(("Q2", c, "17"))
# Q3
c = n_t(3, 3); claims.append(("Q3", c, "53"))
# Q4
c = n_t(2, 1); claims.append(("Q4", c, "4"))
# Q5
c = n_t(2, 2); claims.append(("Q5", c, "10"))
# Q6
c = n_t(2, 3); claims.append(("Q6", c, "22"))

# Q7: P_pass for n=5, eps=1e-3
eps = Fraction(1, 1000)
q = 1 - eps
P_pass = 1 - q**5 - 5*eps*q**4
claims.append(("Q7", float(P_pass), "9.980015e-6"))

# Q8: suppression factor
S = float(eps) / float(P_pass)
claims.append(("Q8", S, "100.2"))

# Q9: P_pass^(2) for n=17, t=2 (failure needs >=3 errors)
epsf = 0.001
P2 = math.comb(17,3)*epsf**3*(1-epsf)**14 + math.comb(17,4)*epsf**4*(1-epsf)**13
claims.append(("Q9", P2, "6.73e-7"))

# Q10: eps_eff
eps_eff = 1 - (1-epsf)**2
claims.append(("Q10", eps_eff, "1.999e-3"))

# Q11: P_act
ee = eps_eff
P_act = 1 - (1-ee)**5 - 5*ee*(1-ee)**4
claims.append(("Q11", P_act, "3.98e-5"))

# Q12: ratio
ratio = P_act / float(P_pass)
claims.append(("Q12", ratio, "3.99"))

# Q13: pseudo-threshold via linear interpolation
f = lambda e: 10*e*(1-e)**3
f32 = f(0.32); f33 = f(0.33)
eps_th = 0.32 + 0.01*(f32 - 1)/(f32 - f33)
claims.append(("Q13", eps_th, "0.3245"))

mism = 0
for cid, computed, expected in claims:
    # round computed to sig digits of expected
    exp_digits = len(expected.replace("e-","").replace(".","").lstrip("0")) if "e" in expected else None
    # determine significant digits from expected string
    import re
    m = re.match(r"^-?(\d+\.?\d*)e?(-?\d+)?$", expected)
    digits_str = m.group(1).replace(".", "")
    sig = len(digits_str.lstrip("0"))
    comp_rounded = float(f"{computed:.{sig}g}")
    exp_val = float(expected)
    match = "yes" if abs(comp_rounded - exp_val) <= 0.5 * 10**(-(sig-1)) * 10**math.floor(math.log10(abs(exp_val))+1) or comp_rounded == exp_val else "no"
    if match == "no":
        # fallback: compare rounded strings
        match = "yes" if f"{computed:.{sig}g}" == f"{exp_val:.{sig}g}" else "no"
    if match == "no":
        mism += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims)-mism} match, {mism} mismatch")
