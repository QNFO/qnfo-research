# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of admissible predicates for N=64 is 2^(2^64) ≈ 10^(5.553×10^18)",
    "inputs": "N=64, log10(2)=0.30103",
    "formula": "log10(2^(2^N)) = 2^N * log10(2)"
  },
  {
    "id": "Q2",
    "statement": "Number of states |S_64| = 2^64 = 1.8446744×10^19",
    "inputs": "N=64",
    "formula": "2^N"
  },
  {
    "id": "Q3",
    "statement": "Reachable short predicates N_short = 1.5318446128384×10^13",
    "inputs": "N=64, L_max=9",
    "formula": "sum_{k=1}^{9} C(64,k)*2^k"
  },
  {
    "id": "Q4",
    "statement": "Landauer erasure energy per bit at 300 K is 2.8709×10^-21 J",
    "inputs": "k_B=1.380649×10^-23 J/K, T=300 K, ln2=0.693147",
    "formula": "E_bit = k_B * T * ln(2)"
  },
  {
    "id": "Q5",
    "statement": "Erasure power for 10^9 distinctions at 1 Hz is 2.8709×10^-12 W",
    "inputs": "f_cycle=1 Hz, N_dist=10^9, E_bit=2.8709×10^-21 J",
    "formula": "P_erase = f_cycle * N_dist * E_bit"
  },
  {
    "id": "Q6",
    "statement": "Maximum distinguishable bits for a 10^-12 W observer is 3.48×10^8",
    "inputs": "P_obs=10^-12 W, tau=1 s, E_bit=2.8709×10^-21 J",
    "formula": "N_max = P_obs * tau / E_bit"
  },
  {
    "id": "Q7",
    "statement": "Ultrametric compression factor kappa = 1.048576×10^6 ≈ 1.05×10^6",
    "inputs": "fine balls 2^30, coarse balls 2^10",
    "formula": "kappa = 2^30 / 2^10 = 2^20"
  },
  {
    "id": "Q8",
    "statement": "Mean occupancy per coarse ball lambda ≈ 97.66",
    "inputs": "m=10^5, coarse balls=1024",
    "formula": "lambda = m / 1024"
  },
  {
    "id": "Q9",
    "statement": "Probability a coarse ball contains exactly one object p1 ≈ 3.78×10^-41",
    "inputs": "lambda=97.66",
    "formula": "p1 = lambda * exp(-lambda)"
  },
  {
    "id": "Q10",
    "statement": "Expected resolvable objects m_real ≈ 3.9×10^-38",
    "inputs": "coarse balls=1024, p1=3.78×10^-41",
    "formula": "m_real = 1024 * p1"
  },
  {
    "id": "Q11",
    "statement": "Critical compression depth r_crit ≈ 23",
    "inputs": "m=10^5, L=40, b=2",
    "formula": "r_crit = L - ceil(log2(m))"
  },
  {
    "id": "Q12",
    "statement": "Excess precision Δn = 36 bits",
    "inputs": "n_prec=100, N=64",
    "formula": "Δn = n_prec - N"
  },
  {
    "id": "Q13",
    "statement": "Realistic-device sustainable rate N_max^real ≈ 3.48×10^5 distinctions per second",
    "inputs": "P_obs=10^-12 W, E_bit^real=2.8709×10^-18 J",
    "formula": "N_max^real = P_obs / E_bit^real"
  },
  {
    "id": "Q14",
    "statement": "Maintaining 40 distinctions for 1 s at 300 K requires P ≈ 1.15×10^-19 W",
    "inputs": "N=40, E_bit=2.8709×10^-21 J, tau=1 s",
    "formula": "P = N * E_bit / tau"
  },
  {
    "id": "Q15",
    "statement": "Maintaining 64 distinctions requires ≈1.84×10^-19 W",
    "inputs": "N=64, E_bit=2.8709×10^-21 J, tau=1 s",
    "formula": "P = N * E_bit / tau"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 6, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: log10(2^64) = 2^64 × log10(2) = 1.8446744×10^19 × 0.30103. Step: 1.8446744 × 0.30103 = 1.8446744×0.3 + 1.8446744×0.00103 = 0.55340232 + 0.00190001 = 0.55530233. So log10 = 5.5530233×10^18, and 2^(2^64) ≈ 10^(5.5530233×10^18).
CLAIM Q1: computed=5.5530233e+18 expected=5.553e+18 match=yes

Q2: 2^64 = 18446744073709551616 = 1.8446744074×10^19.
CLAIM Q2: computed=1.8446744074e+19 expected=1.8446744e+19 match=yes

Q3: Sum C(64,k)·2^k for k=1..9:
k=1: 64×2 = 128
k=2: 2016×4 = 8064
k=3: 41664×8 = 333312
k=4: 635376×16 = 10166016
k=5: 7624512×32 = 243984384
k=6: 74974368×64 = 4798359552
k=7: 621216192×128 = 79515672576
k=8: 4426165368×256 = 1133098334208
k=9: 27540584512×512 = 14100779270144
Running total: 128+8064=8192; +333312=341504; +10166016=10507520; +243984384=254491904; +4798359552=5052851456; +79515672576=84568524032; +1133098334208=1217666858240; +14100779270144=15318446128384 = 1.5318446128384×10^13. (Note: the paper's summation line transcribes the k=6 term as 4,798,263,552, a digit transposition; the correct term 4,798,359,552 still yields the stated total, so the final value matches.)
CLAIM Q3: computed=15318446128384 expected=15318446128384 match=yes

Q4: E_bit = 1.380649×10^-23 × 300 × 0.693147. Step 1: 1.380649×300 = 414.1947, so 4.141947×10^-21. Step 2: 4.141947 × 0.693147 = 4.141947×0.7 − 4.141947×0.006853 = 2.8993629 − 0.0283814 = 2.8709815. E_bit = 2.8709815×10^-21 J.
CLAIM Q4: computed=2.8709815e-21 expected=2.8709e-21 match=yes

Q5: P = 1 × 10^9 × 2.8709815×10^-21 = 2.8709815×10^-12 W.
CLAIM Q5: computed=2.8709815e-12 expected=2.8709e-12 match=yes

Q6: N_max = 10^-12 × 1 / 2.8709815×10^-21 = (1/2.8709815)×10^9 = 0.348346×10^9 = 3.48346×10^8. (1/2.8709815: 2.8709815×0.348 = 0.99910; remainder 0.00090/2.87098 ≈ 0.000314; so 0.348314… refine: 2.8709815×0.34835=1.000033 → 0.348338; converged ≈0.348346.)
CLAIM Q6: computed=3.48346e+8 expected=3.48e+8 match=yes

Q7: kappa = 2^30/2^10 = 2^20 = 1048576 = 1.048576×10^6.
CLAIM Q7: computed=1048576 expected=1048576 match=yes

Q8: lambda = 100000/1024 = 97.65625.
CLAIM Q8: computed=97.65625 expected=97.66 match=yes

Q9: p1 = 97.65625 × e^-97.65625. Convert: 97.65625/ln10 = 97.65625/2.302585 = 42.41157 (2.302585×42 = 96.70857; remainder 0.94768/2.302585 = 0.41157). So e^-97.65625 = 10^-42.41157 = 10^(-0.41157)×10^-42 = 0.38770×10^-42 = 3.8770×10^-43. p1 = 97.65625 × 3.8770×10^-43 = 3.7867×10^-41.
CLAIM Q9: computed=3.7867e-41 expected=3.78e-41 match=yes

Q10: m_real = 1024 × 3.7867×10^-41 = 3.8776×10^-38.
CLAIM Q10: computed=3.8776e-38 expected=3.9e-38 match=yes

Q11: ceil(log2(10^5)): 2^16 = 65536 < 100000; 2^17 = 131072 ≥ 100000, so ceil = 17. r_crit = 40 − 17 = 23.
CLAIM Q11: computed=23 expected=23 match=yes

Q12: Δn = 100 − 64 = 36.
CLAIM Q12: computed=36 expected=36 match=yes

Q13: N_max^real = 10^-12 / 2.8709815×10^-18 = 0.348346×10^6 = 3.48346×10^5.
CLAIM Q13: computed=3.48346e+5 expected=3.48e+5 match=yes

Q14: P = 40 × 2.8709815×10^-21 / 1 = 1.1483926×10^-19 W.
CLAIM Q14: computed=1.1483926e-19 expected=1.15e-19 match=yes

Q15: P = 64 × 2.8709815×10^-21 / 1 = 1.8374282×10^-19 W.
CLAIM Q15: computed=1.8374282e-19 expected=1.84e-19 match=yes

VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5.5530233e+18 | 5.553e+18 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 1.8446744074e+19 | 1.8446744e+19 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q3 | 15318446128384 | 15318446128384 | yes | match | 14 significant digits (as the paper states, at least 2) |
| Q4 | 2.8709815e-21 | 2.8709e-21 | yes | match | 5 significant digits (as printed, at least 3) |
| Q5 | 2.8709815e-12 | 2.8709e-12 | yes | match | 5 significant digits (as printed, at least 3) |
| Q6 | 3.48346e+8 | 3.48e+8 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 1048576 | 1048576 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 97.65625 | 97.66 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 3.7867e-41 | 3.78e-41 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 3.8776e-38 | 3.9e-38 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 23 | 23 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 36 | 36 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 3.48346e+5 | 3.48e+5 | yes | match | 3 significant digits (as printed, at least 3) |
| Q14 | 1.1483926e-19 | 1.15e-19 | yes | match | 3 significant digits (as printed, at least 3) |
| Q15 | 1.8374282e-19 | 1.84e-19 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 15.
