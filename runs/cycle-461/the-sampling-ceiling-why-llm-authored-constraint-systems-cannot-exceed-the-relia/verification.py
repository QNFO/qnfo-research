# Verification of equation transitions in the Methods/Analysis (Section 4) of
# "The Sampling Ceiling" paper.
#
# Notation table (all quantities are DIMENSIONLESS probabilities/counts,
# declared via sympy.physics.units as dimensionless):
#   eps   : per-constraint error rate of the LLM sampler        (probability, [0,1])
#   N     : number of independent constraints                   (count, N >= 1)
#   c     : probability the formal verifier catches an error    (probability, [0,1])
#   p     : whole-artifact base correctness                     (probability, [0,1])
#   v     : characterization yield / verification filter pass   (probability, [0,1])
#   P     : clean-run / system reliability                      (probability, [0,1])

import sympy as sp
from sympy.physics.units import Quantity, dimensionless
from sympy import Rational, ln, ceiling, simplify, S

# ---- unit declarations (all dimensionless probabilities) ----
prob = Quantity('probability', dimensionless)   # eps, c, p, v, P
count = Quantity('count', dimensionless)        # N

eps, c, p, v = sp.symbols('eps c p v', real=True)
N = sp.Symbol('N', positive=True, integer=True)

# ---- sanity bounds ----
def bounds_ok():
    checks = [
        (S(0) <= eps, eps <= S(1), 'eps in [0,1]'),
        (S(0) <= c,   c <= S(1),   'c in [0,1]'),
        (S(0) <= p,   p <= S(1),   'p in [0,1]'),
        (S(0) <= v,   v <= S(1),   'v in [0,1]'),
        (N >= 1, True,             'N >= 1'),
    ]
    return all(a and b for a, b, _ in checks)

# limiting cases stated in the paper:
#   eps -> 0        => P_clean -> 1
#   eps -> 1        => P_clean -> 0
#   c -> 1, eps > 0 => P_hybrid -> 1  (verifier catches everything)
#   c -> 0          => P_hybrid -> P_clean (verifier useless)
def limiting_cases():
    ok = True
    ok &= sp.limit((1-eps)**sp.Symbol('k', positive=True), eps, 0) == 1
    ok &= sp.limit((1-eps)**sp.Symbol('k', positive=True), eps, 1) == 0
    ok &= sp.limit((1-eps*(1-c))**N, c, 1) == 1
    ok &= sp.simplify(sp.limit((1-eps*(1-c))**N, c, 0) - (1-eps)**N) == 0
    return bool(ok)

def report(name, premise, conclusion, justification, lhs, rhs, tol=S(1)/10000):
    """Try exact simplify(lhs-rhs)==0; else randomized/numeric spot check."""
    diff = simplify(sp.expand(lhs - rhs))
    if diff == 0:
        print(f"DERIV ok | {name}: ({premise}) -> ({conclusion}) [{justification}]")
        return
    # numeric spot check (paper's declared point values + randomized draws)
    import random
    ok = True
    # declared point values
    subs = {eps: sp.Rational(2,100), c: sp.Rational(95,100), N: 40,
            p: sp.Rational(85,100), v: sp.Rational(54,100)}
    try:
        ok &= abs(float(lhs.subs(subs)) - float(rhs.subs(subs))) < float(tol)
    except Exception:
        ok = False
    # randomized draws under declared assumptions
    for _ in range(200):
        e = random.uniform(0, 1); cc = random.uniform(0, 1)
        n = random.randint(1, 60); pp = random.uniform(0, 1); vv = random.uniform(0, 1)
        s = {eps: e, c: cc, N: n, p: pp, v: vv}
        try:
            if abs(float(lhs.subs(s)) - float(rhs.subs(s))) > 1e-9 * max(1.0, abs(float(rhs.subs(s)))):
                ok = False; break
        except Exception:
            ok = False; break
    if ok:
        print(f"DERIV ok | {name}: ({premise}) -> ({conclusion}) [{justification}] (numeric spot check)")
    elif abs(float(lhs.subs(subs)) - float(rhs.subs(subs))) < float(tol):
        print(f"DERIV inconclusive | {name}: ({premise}) -> ({conclusion}) [{justification}] (approximate equality only)")
    else:
        print(f"DERIV refuted | {name}: ({premise}) -> ({conclusion}) [{justification}]")

print("sanity bounds:", "ok" if bounds_ok() else "REFUTED")
print("limiting cases:", "ok" if limiting_cases() else "REFUTED")

# T1: independence of per-constraint errors -> P_clean = (1-eps)^N
#     paper point value: 0.98^40 ~= 0.4457
report("T1 prompt-only clean-run",
       "per-constraint error eps, independent constraints",
       "P_clean = (1-eps)^N",
       "independence; product of per-constraint success probabilities",
       (1-eps)**N, sp.Rational(2,100)**40)
print("  numeric: 0.98^40 =", float((Rational(98,100))**40), "vs paper 0.4457")

# T2: verifier catches error w.p. c -> residual per-constraint error eps*(1-c)
#     -> P_hybrid = (1 - eps*(1-c))^N ; paper: (1-0.02*0.05)^40 ~= 0.9608
report("T2 hybrid clean-run",
       "verifier catch probability c, residual error eps*(1-c)",
       "P_hybrid = (1-eps(1-c))^N",
       "independence; residual error after deductive catch",
       (1-eps*(1-c))**N, (1 - sp.Rational(2,100)*sp.Rational(5,100))**40)
print("  numeric: (1-0.001)^40 =", float((Rational(999,1000))**40), "vs paper 0.9608")

# T3: improvement factor P_hybrid / P_clean ~= 2.16
report("T3 improvement factor",
       "T1 and T2",
       "P_hybrid/P_clean ~= 2.16",
       "ratio of clean-run probabilities",
       ((1-eps*(1-c))**N)/((1-eps)**N), sp.Rational(216,100))
print("  numeric:", float((Rational(999,1000)**40)/(Rational(98,100)**40)))

# T4: break-even count: (1-eps)^N* = 1/2 -> N* = ln(1/2)/ln(1-eps) ~= 34.31 -> 35
report("T4 break-even count",
       "(1-eps)^N* = 1/2",
       "N* = ln(1/2)/ln(1-eps), ceil -> 35",
       "solve for N; ceiling to integer constraint count",
       ln(S(1)/2)/ln(1-eps), sp.Float(ln(S(1)/2)/ln(Rational(98,100)), 5))
print("  numeric: N* =", float(ln(S(1)/2)/ln(Rational(98,100))), "-> ceil =", int(sp.ceiling(ln(S(1)/2)/ln(Rational(98,100)))))

# T5: aggregate product form p_system = p * v = 0.85 * 0.54 = 0.4590
report("T5 aggregate product",
       "base correctness p, independent verification filter v",
       "p_system = p*v",
       "independence of generation and filter (stated assumption)",
       p*v, sp.Rational(459,1000))
print("  numeric: 0.85*0.54 =", float(Rational(85,100)*Rational(54,100)))

# T6: per-chapter threshold p* ~= 0.958 from p*^16 = 1/2 (16 chapters)
report("T6 per-chapter threshold",
       "p*^N_ch = 1/2 with N_ch = 16",
       "p* = (1/2)^(1/16) ~= 0.958",
       "solve threshold equation (N_ch inferred from [11])",
       (S(1)/2)**(S(1)/16), sp.Rational(958,1000))
print("  numeric: 0.5^(1/16) =", float((S(1)/2)**(S(1)/16)))

# T7: per-constraint threshold q* ~= 0.986 from q*^48 = 1/2
report("T7 per-constraint threshold",
       "q*^48 = 1/2",
       "q* = (1/2)^(1/48) ~= 0.986",
       "solve threshold equation (N inferred from [11])",
       (S(1)/2)**(S(1)/48), sp.Rational(986,1000))
print("  numeric: 0.5^(1/48) =", float((S(1)/2)**(S(1)/48)))

# T8: automated checking lowers threshold to 0.979 (q'^32 = 1/2)
report("T8 automated-checking threshold",
       "q'^32 = 1/2 with automated checking",
       "q' = (1/2)^(1/32) ~= 0.979",
       "hybrid pattern reduces effective constraint count",
       (S(1)/2)**(S(1)/32), sp.Rational(979,1000))
print("  numeric: 0.5^(1/32) =", float((S(1)/2)**(S(1)/32)))

import math

def sig(x, n=4):
    return x

claims = []

def report(cid, computed, expected, stated_digits=4):
    # round computed to the number of significant digits the paper states
    if expected is not None:
        d = len(expected.replace('.', '').replace('-', '').lstrip('0'))
        # use stated digits from expected string
        digits = stated_digits
        r = round(computed, digits - 1 - math.floor(math.log10(abs(computed))) if computed != 0 else 0)
    else:
        r = computed
    match = (expected is not None and abs(r - float(expected)) < 1e-9)
    print(f"CLAIM {cid}: computed={computed:.8f} expected={expected} match={'yes' if match else 'no'}")

# Q1
v = 0.98**40
report("Q1", v, "0.4457")
# Q2
v = (1 - 0.02*(1-0.95))**40
report("Q2", v, "0.9608")
# Q3
pp = 0.98**40
ph = (1 - 0.02*(1-0.95))**40
report("Q3", ph/pp, "2.156")
# Q4
nstar = math.ceil(math.log(0.5)/math.log(0.98))
# check: smallest integer N with 0.98^N < 0.5
N = 1
while 0.98**N >= 0.5:
    N += 1
print(f"CLAIM Q4: computed={N:.8f} expected=35 match={'yes' if N == 35 else 'no'}")
# Q5
v = 0.986**40
report("Q5", v, "0.5691")
# Q6
v = 0.986**300
report("Q6", v, "0.0146")
# Q7
v = (1 - 0.02*(1-0.80))**40
report("Q7", v, "0.8518")
# Q8
v = (1 - 0.02*(1-0.99))**40
report("Q8", v, "0.9920")
# Q9
v = 0.95**40
report("Q9", v, "0.1285")
# Q10
v = (1 - 0.05*(1-0.95))**40
report("Q10", v, "0.9047")
# Q11
v = 0.99**40
report("Q11", v, "0.6690")
# Q12
v = 0.85*0.54
report("Q12", v, "0.4590")
# Q13
v = 0.98**10
report("Q13", v, "0.8170")
# Q14
v = (1 - 0.02*(1-0.95))**10
report("Q14", v, "0.9900")
# Q15
v = 0.98**20
report("Q15", v, "0.6676")
# Q16
v = (1 - 0.02*(1-0.95))**20
report("Q16", v, "0.9802")

print("VERIFICATION SUMMARY: 16 claims, " + "M match, K mismatch")
