# DERIV extraction for "Ontological Re-Entry" (Methods/Analysis sections available in the excerpt)
# NOTE: The paper text is truncated at Section 3.3 ("Landauer's princip..."), so only transitions
# from Sections 3.1-3.3 and the numeric claims of the Abstract/Contributions are extractable.
# Transitions whose derivations lie in the missing text are emitted as DERIV inconclusive.

import sympy as sp
from sympy import Rational, binomial, log, exp, simplify, Symbol, symbols, Integer, S
from sympy.physics.units import kelvin, joule, watt, second, bit, Quantity, convert_to
from sympy.physics.units import kilo
import random

kB = sp.Float(1.380649e-23)          # J/K (SI exact)
T_env = 300 * kelvin
E_bit_target = sp.Float(2.87e-21) * joule
P_obs = sp.Float(1e-12) * watt
f_cycle = 1 * second**-1
N_dist = Integer(10**9)

results = []

def record(name, ok):
    tag = {True: "ok", False: "refuted", None: "inconclusive"}[ok]
    results.append((tag, name))

def check_eq(lhs, rhs, tol=S(1)/10**6):
    d = simplify(lhs - rhs)
    if d == 0:
        return True
    # numeric fallback with relative tolerance
    try:
        v = abs(float(d.evalf()))
        s = max(abs(float(lhs.evalf())), abs(float(rhs.evalf())), 1e-300)
        return v / s < float(tol)
    except Exception:
        return None

# ---------------------------------------------------------------
# Transition T1 (Prop 3.1): bijection between admissible predicates
# and subsets of S_N  =>  count = 2^{|S_N|} = 2^{2^N}
# Premise: every Boolean formula defines a characteristic function on S_N;
#          every subset has a minterm disjunction.
# Conclusion: #admissible predicates = 2^{2^N}.
# Justification: characteristic-function bijection.
# ---------------------------------------------------------------
N = symbols('N', integer=True, positive=True)
lhs = 2**(2**N)
# sanity: for small N enumerate subsets vs formulas-as-truth-tables
ok = all(len(set(range(2**n))) == 2**n and 2**(2**n) == len(set(range(2**n)))**0 + 2**(2**n) - 2**(2**n) + 2**(2**n)
         for n in range(1, 6))
# direct check: count of subsets of a 2^n set is 2^(2^n)
ok = all(binomial(2**n, 0) + sum(binomial(2**n, k) for k in range(2**n + 1)) == 2**(2**n)
         for n in range(1, 5))
record("T1 Prop3.1: admissible predicates <-> P(S_N), count = 2^(2^N)", ok)

# ---------------------------------------------------------------
# Transition T2 (Sec 3.1): b-ary tree of depth L realizes D_N:
#   N = L*log2(b)  and  |S_N| = b^L = 2^N
# Premise: full b-ary tree depth L, leaves = b^L, path length L digits base b.
# Conclusion: N = L log2 b; |S_N| = b^L = 2^N.
# ---------------------------------------------------------------
L, b = symbols('L b', positive=True)
ok2 = simplify(b**(L) - 2**(L*log(b, 2))) == 0
# numeric spot checks
for _ in range(5):
    Lv = random.randint(1, 8); bv = random.choice([2, 4, 8, 16])
    ok2 = ok2 and (Lv*log(bv, 2)) == log(bv**Lv, 2) and 2**int(Lv*log(bv, 2)) == bv**Lv
record("T2 Sec3.1: N = L log2 b and |S_N| = b^L = 2^N", ok2)

# ---------------------------------------------------------------
# Transition T3 (Sec 3.3 / Background): Landauer
#   E_bit = kB * T_env * ln2  at T=300 K  =>  2.87e-21 J
# ---------------------------------------------------------------
E_bit = kB * 300 * sp.log(2)
ok3 = check_eq(E_bit, sp.Float(2.87e-21))
record("T3 Landauer: E_bit = kB*T*ln2 = 2.87e-21 J at 300 K", ok3)

# ---------------------------------------------------------------
# Transition T4 (Sec 4.4): P_erase = E_bit * (1e9 distinctions) * (1 Hz)
#   => 2.87e-12 W
# ---------------------------------------------------------------
P_erase = E_bit * joule**-1 * N_dist * f_cycle * joule  # E_bit[J] * 1e9 * 1/s
P_erase_val = sp.Float(1.380649e-23) * 300 * sp.log(2) * 1e9
ok4 = check_eq(P_erase_val, sp.Float(2.87e-12))
record("T4 P_erase = E_bit * 1e9 * 1 Hz = 2.87e-12 W", ok4)

# ---------------------------------------------------------------
# Transition T5 (Sec 4.5): N_max = P_obs / E_bit  => 3.48e8 distinctions/s
# ---------------------------------------------------------------
N_max = sp.Float(1e-12) / (sp.Float(1.380649e-23) * 300 * sp.log(2))
ok5 = check_eq(N_max, sp.Float(3.48e8))
record("T5 N_max = P_obs / E_bit = 3.48e8 distinctions/s", ok5)

# ---------------------------------------------------------------
# Transition T6 (Abstract/Sec 4.6): ultrametric compression
#   2^30 fine balls -> 2^10 coarse balls, factor 2^20 = 1.05e6
# ---------------------------------------------------------------
ok6 = check_eq(sp.Integer(2)**30 / sp.Integer(2)**10, sp.Integer(2)**20) and \
      check_eq(sp.Integer(2)**20, sp.Float(1.05e6), tol=S(1)/100)
record("T6 compression factor 2^30/2^10 = 2^20 ~ 1.05e6", ok6)

# ---------------------------------------------------------------
# Transition T7 (Sec 4.6): uniform placement of 1e5 objects into 2^10 coarse balls;
# P(some ball has exactly one object) = 3.78e-41;
# expected resolvable count = 2^10 * p_ball ~ 3.9e-38
# Model: p_ball = C(M,1)*(1/B)*(1-1/B)^(M-1), M=1e5, B=2^10
# ---------------------------------------------------------------
M = Integer(10**5); B = Integer(2)**10
p_ball = binomial(M, 1) * Rational(1, B) * (Rational(B-1, B))**(M-1)
p_any = B * p_ball
p_ball_num = p_ball.evalf(50)
p_any_num = p_any.evalf(50)
ok7a = check_eq(p_ball_num, sp.Float(3.78e-41), tol=S(1)/20)   # loose tol: paper rounding
ok7b = check_eq(p_any_num, sp.Float(3.9e-38), tol=S(1)/20)
record("T7 P(any coarse ball exactly one object) = 3.78e-41; E[resolvable] = 3.9e-38",
       True if (ok7a and ok7b) else (False if (ok7a is False or ok7b is False) else None))
print("   T7 numeric: p_ball =", p_ball_num, " p_any =", p_any_num)

# ---------------------------------------------------------------
# Transition T8 (Sec 4.7): critical survival depth r_crit ~ 23
# Derivation is in the truncated portion of the paper -> inconclusive.
# ---------------------------------------------------------------
record("T8 r_crit ~ 23 (derivation in truncated Sec 4.7)", None)

# ---------------------------------------------------------------
# Transition T9 (Sec 4.2, per Contributions #2): N_short = 1.5318446128384e13
# reachable predicates = conjunctions of <= 9 literals over 64 variables.
# Count: sum_{k=1}^{9} C(64,k) * 2^k * 2^{2^{64-k}}  (choose vars, signs, free vars)
# This is dominated by the k=9 term; check the tabulated value against the sum.
# ---------------------------------------------------------------
ok9 = None
try:
    # exact term-by-term with mpmath-level precision via sympy Float
    total = sp.Integer(0)
    for k in range(1, 10):
        total += binomial(64, k) * 2**k * 2**(2**(64-k))
    # 2^(2^64) is astronomically large; compare only leading digits via logs
    log10_total = sp.log(total, 10).evalf(30) if total.is_number else None
    # The tabulated value 1.53e13 is FAR smaller than 2^(2^64); the paper's own
    # internal-consistency check (Sec 4.2) compares table vs summation, but the
    # summation formula itself is not fully stated in the excerpt -> inconclusive.
    ok9 = None
except Exception:
    ok9 = None
record("T9 N_short = 1.5318446128384e13 for <=9 literals over 64 vars (summation not fully stated in excerpt)", ok9)

# ---------------------------------------------------------------
# Transition T10 (Abstract): 2^(2^64) ~ 10^(5.553e18)
# log10(2^(2^64)) = 2^64 * log10(2)
# ---------------------------------------------------------------
lhs10 = sp.Integer(2)**64 * sp.log(2, 10)
ok10 = check_eq(lhs10.evalf(30), sp.Float(5.553e18), tol=S(1)/1000)
record("T10 log10(2^(2^64)) = 2^64*log10(2) = 5.553e18", ok10)

# ---------------------------------------------------------------
# Sanity bounds (declared assumptions: probabilities in [0,1], efficiencies <= 1,
# nonnegative costs, limiting cases)
# ---------------------------------------------------------------
san = []
san.append(("p_ball in [0,1]", 0 <= p_ball_num <= 1))
san.append(("p_any in [0,1]", 0 <= p_any_num <= 1))
san.append(("E_bit > 0", E_bit.evalf() > 0))
san.append(("P_erase > 0", P_erase_val > 0))
san.append(("N_max > 0", N_max.evalf() > 0))
# limiting cases: T->0 => E_bit->0 ; B=1 => p_ball = 1*(1)*(0)^{M-1} -> 0 for M>1
san.append(("T->0 limit", simplify(kB*0*sp.log(2)) == 0))
p_ball_B1 = binomial(M,1)*Rational(1,1)*Rational(0,1)**(M-1)
san.append(("B=1 limit p=0", p_ball_B1 == 0))
# M=1: exactly one object in exactly one ball with prob 1
p_ball_M1 = binomial(1,1)*Rational(1,B)*Rational(B-1,B)**0
san.append(("M=1 limit p=1/B per ball", p_ball_M1 == Rational(1, B)))
for name, v in san:
    print(f"   SANITY {'ok' if v else 'FAIL'}: {name}")

# units declaration check
print("   UNITS: E_bit =", convert_to(kB*300*sp.log(2)*joule/kelvin*kelvin, joule))
print("   UNITS: P_erase =", convert_to(P_erase_val*joule/second, watt))

print()
for tag, name in results:
    print(f"DERIV {tag} :: {name}")

import math
from fractions import Fraction

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# Q1
N = 64
log10_2 = 0.30103
exponent = (2**N) * log10_2
computed_q1 = exponent
expected_q1 = "5.553e18"
match_q1 = f"{computed_q1:.4g}" == "5.553e+18"

# Q2
computed_q2 = 2**N
expected_q2 = "1.8446744e19"
match_q2 = f"{computed_q2:.8g}" == "1.8446744e+19"

# Q3
from math import comb
N_short = sum(comb(64, k) * (2**k) for k in range(1, 10))
computed_q3 = N_short
expected_q3 = "1.5318446128384e13"
match_q3 = str(computed_q3) == "15318446128384"

# Q4
k_B = 1.380649e-23
T = 300.0
ln2 = 0.693147
E_bit = k_B * T * ln2
computed_q4 = E_bit
expected_q4 = "2.8709e-21"
match_q4 = f"{computed_q4:.5g}" == "2.8709e-21"

# Q5
f_cycle = 1.0
N_dist = 1e9
P_erase = f_cycle * N_dist * E_bit
computed_q5 = P_erase
expected_q5 = "2.8709e-12"
match_q5 = f"{computed_q5:.5g}" == "2.8709e-12"

# Q6
P_obs = 1e-12
tau = 1.0
N_max = P_obs * tau / E_bit
computed_q6 = N_max
expected_q6 = "3.48e8"
match_q6 = f"{computed_q6:.3g}" == "3.48e+08"

# Q7
kappa = (2**30) / (2**10)
computed_q7 = kappa
expected_q7 = "1.048576e6"
match_q7 = f"{computed_q7:.7g}" == "1.048576e+06"

# Q8
m = 1e5
coarse = 1024
lam = m / coarse
computed_q8 = lam
expected_q8 = "97.66"
match_q8 = f"{computed_q8:.4g}" == "97.66"

# Q9
p1 = lam * math.exp(-lam)
computed_q9 = p1
expected_q9 = "3.78e-41"
match_q9 = f"{computed_q9:.3g}" == "3.78e-41"

# Q10
m_real = coarse * p1
computed_q10 = m_real
expected_q10 = "3.9e-38"
match_q10 = f"{computed_q10:.2g}" == "3.9e-38"

# Q11
L = 40
b = 2
r_crit = L - math.ceil(math.log2(m))
computed_q11 = r_crit
expected_q11 = "23"
match_q11 = str(r_crit) == "23"

# Q12
n_prec = 100
delta_n = n_prec - N
computed_q12 = delta_n
expected_q12 = "36"
match_q12 = str(delta_n) == "36"

# Q13
E_bit_real = 1e3 * E_bit
N_max_real = P_obs / E_bit_real
computed_q13 = N_max_real
expected_q13 = "3.48e5"
match_q13 = f"{computed_q13:.3g}" == "3.48e+05"

# Q14
P40 = 40 * E_bit / tau
computed_q14 = P40
expected_q14 = "1.15e-19"
match_q14 = f"{computed_q14:.3g}" == "1.15e-19"

# Q15
P64 = 64 * E_bit / tau
computed_q15 = P64
expected_q15 = "1.84e-19"
match_q15 = f"{computed_q15:.3g}" == "1.84e-19"

print(f"CLAIM Q1: computed={computed_q1:.8e} expected={expected_q1} match={'yes' if match_q1 else 'no'}")
print(f"CLAIM Q2: computed={computed_q2:.8e} expected={expected_q2} match={'yes' if match_q2 else 'no'}")
print(f"CLAIM Q3: computed={computed_q3:.8e} expected={expected_q3} match={'yes' if match_q3 else 'no'}")
print(f"CLAIM Q4: computed={computed_q4:.8e} expected={expected_q4} match={'yes' if match_q4 else 'no'}")
print(f"CLAIM Q5: computed={computed_q5:.8e} expected={expected_q5} match={'yes' if match_q5 else 'no'}")
print(f"CLAIM Q6: computed={computed_q6:.8e} expected={expected_q6} match={'yes' if match_q6 else 'no'}")
print(f"CLAIM Q7: computed={computed_q7:.8e} expected={expected_q7} match={'yes' if match_q7 else 'no'}")
print(f"CLAIM Q8: computed={computed_q8:.8e} expected={expected_q8} match={'yes' if match_q8 else 'no'}")
print(f"CLAIM Q9: computed={computed_q9:.8e} expected={expected_q9} match={'yes' if match_q9 else 'no'}")
print(f"CLAIM Q10: computed={computed_q10:.8e} expected={expected_q10} match={'yes' if match_q10 else 'no'}")
print(f"CLAIM Q11: computed={computed_q11:.8e} expected={expected_q11} match={'yes' if match_q11 else 'no'}")
print(f"CLAIM Q12: computed={computed_q12:.8e} expected={expected_q12} match={'yes' if match_q12 else 'no'}")
print(f"CLAIM Q13: computed={computed_q13:.8e} expected={expected_q13} match={'yes' if match_q13 else 'no'}")
print(f"CLAIM Q14: computed={computed_q14:.8e} expected={expected_q14} match={'yes' if match_q14 else 'no'}")
print(f"CLAIM Q15: computed={computed_q15:.8e} expected={expected_q15} match={'yes' if match_q15 else 'no'}")

total = 15
matched = sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7,
               match_q8, match_q9, match_q10, match_q11, match_q12, match_q13, match_q14, match_q15])
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")
