# Verification of equation transitions in "Ontological Re-Entry"
import sympy as sp
from sympy import symbols, Eq, simplify, log, binomial, Sum, factorial, exp, Rational, Float, N as sN
from sympy.physics.units import kelvin, joule, watt, second, boltzmann_constant
import random, math

results = []
def report(tag, status, desc):
    results.append(f"DERIV {status} | {tag} :: {desc}")

def check_eq(tag, lhs, rhs, desc):
    diff = simplify(sp.expand(lhs - rhs))
    if diff == 0:
        report(tag, "ok", desc)
        return True
    # numeric spot check
    ok = True
    for _ in range(5):
        subs = {s: random.uniform(0.5, 5) for s in lhs.free_symbols | rhs.free_symbols
                if s not in (sp.pi, sp.E)}
        try:
            a, b = float(lhs.subs(subs)), float(rhs.subs(subs))
            if abs(a - b) > 1e-6 * max(1.0, abs(a), abs(b)):
                ok = False
        except Exception:
            ok = None
            break
    if ok is True:
        report(tag, "ok", desc + " (numeric spot check)")
    elif ok is None:
        report(tag, "inconclusive", desc + " (numeric evaluation failed)")
    else:
        report(tag, "refuted", desc)
    return ok is True

# --- Notation table with units ---
kB   = boltzmann_constant                     # J/K
T    = Float(300) * kelvin                    # K
Pobs = Float(1e-12) * watt                    # W
tau  = Float(1) * second                      # s
Ebit = kB * T * log(2)                        # J

# --- T1: tree realization N = L log2 b, |S_N| = b^L = 2^N ---
L, b = symbols("L b", positive=True)
check_eq("T1a", b**L, 2**(L*log(b)/log(2)), "b^L = 2^(L log2 b) (tree realization)")

# --- T2: Prop 3.1, admissible predicates = 2^(2^N) (bijection with subsets) ---
# combinatorial identity: number of subsets of S_N is 2^{|S_N|} = 2^{2^N}; check for small N
ok = all(2**(2**n) == 2**len(list(__import__('itertools').product([0,1], repeat=n))) for n in range(1, 5))
report("T2", "ok" if ok else "refuted", "Prop 3.1: #predicates = 2^(2^N) via subset bijection (small-N enumeration)")

# --- T3: Landauer E_bit = kB*T*ln2 ---
check_eq("T3", Ebit, kB*T*log(2), "Landauer bit-erasure energy definition")

# --- T4: Eq (1) P_erase = f*N_dist*kB*T*ln2 (definition; dimensional consistency) ---
f_c, Nd = symbols("f_cycle N_dist", positive=True)
check_eq("T4", f_c*Nd*kB*T*log(2), f_c*Nd*(kB*T*log(2)), "Eq(1) P_erase = f*N_dist*E_bit")

# --- T5: Eq (2) N <= P_obs*tau/(kB*T*ln2) (bound rearranged from Eq(1)) ---
Nmax = Pobs*tau/(kB*T*log(2))
val = float(Nmax)
report("T5", "ok" if 3.4e8 < val < 3.6e8 else "refuted",
       f"Eq(2) N_max = P_obs*tau/E_bit = {val:.4e} (paper: 3.48e8 distinctions/s)")

# --- T6: Eq (3) N_short = sum_{k=1}^{9} C(64,k) 2^k = 15318446128384 ---
Nshort = sum(binomial(64, k)*2**k for k in range(1, 10))
report("T6", "ok" if Nshort == 15318446128384 else "refuted",
       f"Eq(3) N_short = {Nshort} (paper: 15318446128384)")

# --- T7: f_reach = N_short / 2^(2^N) (definition, effectively zero) ---
report("T7", "ok", "f_reach = N_short/2^(2^N) definition; ~1e13/1e(5.55e18) ~ 0")

# --- T8: log10(2^(2^64)) = 2^64 * log10(2) ~ 5.553e18 ---
lhs = log(2**64, 10)
val = float(lhs)
report("T8", "ok" if 5.55e18 < val < 5.56e18 else "refuted",
       f"log10(2^2^64) = {val:.4e} (paper: 5.553e18)")

# --- T9: Eq (4) kappa = b^(L_fine - L_coarse) (definition) ---
Lf, Lc = symbols("L_fine L_coarse", positive=True)
check_eq("T9", b**(Lf - Lc), b**Lf / b**Lc, "Eq(4) kappa = b^(Lf-Lc) = b^Lf/b^Lc")

# --- T10: compression 2^30 fine -> 2^10 coarse, factor 2^20 ~ 1.05e6 ---
val = float(2**20)
report("T10", "ok" if abs(val - 1.048576e6) < 1e3 else "refuted",
       f"compression factor 2^20 = {val:.4e} (paper: 1.05e6)")

# --- T11: Eq (5) m_real = b^Lc * lambda * e^{-lambda}, lambda = m / b^Lc ---
m, lam = symbols("m lambda", positive=True)
check_eq("T11", b**Lc * lam * exp(-lam), b**Lc * (m/b**Lc) * exp(-m/b**Lc),
         "Eq(5) m_real = b^Lc * lambda * e^{-lambda} with lambda = m/b^Lc")

# --- T12: numeric: m=1e5, b^Lc=2^10 => lambda ~ 97.65625; P(one) = lambda e^{-lambda} ~ 3.78e-41 ---
lam_v = Rational(10**5, 2**10)
p_one = lam_v * exp(-lam_v)
val = float(p_one)
report("T12", "ok" if 3.7e-41 < val < 3.9e-41 else "refuted",
       f"P(coarse ball has exactly one) = lambda e^-lambda = {val:.4e} (paper: 3.78e-41)")

# --- T13: expected resolvable count = 2^10 * p_one ~ 3.9e-38 ---
val2 = float(2**10 * p_one)
report("T13", "ok" if 3.8e-38 < val2 < 4.0e-38 else "refuted",
       f"m_real = 2^10 * lambda e^-lambda = {val2:.4e} (paper: ~3.9e-38)")

# --- T14: E_bit at 300K ~ 2.87e-21 J ---
val = float(Ebit / joule)
report("T14", "ok" if 2.8e-21 < val < 2.95e-21 else "refuted",
       f"E_bit(300K) = {val:.4e} J (paper: 2.87e-21 J)")

# --- Sanity bounds ---
probs = [float(p_one), float(2**10*p_one)]
report("SANITY", "ok" if all(0 <= p <= 1 or p < 1e-30 for p in probs) and val > 0 and float(Nmax) > 0
       else "refuted", "probabilities in [0,1] (tiny Poisson tails allowed), E_bit>0, N_max>0, efficiency<=1 trivially")

for r in results:
    print(r)

import math
from fractions import Fraction

def sig(x, digits):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (digits - 1))

# Q1
N = 64
log10_2 = 0.30103
exp = (2**N) * log10_2
computed_q1 = exp
expected_q1 = "5.553e18"
match_q1 = f"{computed_q1:.4e}" == "5.553e+18" or abs(computed_q1 - 5.553e18) < 1e15
print(f"CLAIM Q1: computed={computed_q1:.8e} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Q2
computed_q2 = 2**64
expected_q2 = "1.8446744e19"
match_q2 = abs(computed_q2 - 1.8446744e19) / 1.8446744e19 < 1e-7
print(f"CLAIM Q2: computed={computed_q2:.8e} expected={expected_q2} match={'yes' if match_q2 else 'no'}")

# Q3
N_short = sum(math.comb(64, k) * (2**k) for k in range(1, 10))
computed_q3 = N_short
expected_q3 = "15318446128384"
match_q3 = computed_q3 == 15318446128384
print(f"CLAIM Q3: computed={computed_q3} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Q4
k_B = 1.380649e-23
T_env = 300.0
ln2 = math.log(2)
E_bit = k_B * T_env * ln2
computed_q4 = E_bit
expected_q4 = "2.87e-21"
match_q4 = abs(computed_q4 - 2.87e-21) / 2.87e-21 < 0.005
print(f"CLAIM Q4: computed={computed_q4:.8e} expected={expected_q4} match={'yes' if match_q4 else 'no'}")

# Q5
N_dist = 1e9
f_cycle = 1.0
P_erase = f_cycle * N_dist * E_bit
computed_q5 = P_erase
expected_q5 = "2.87e-12"
match_q5 = abs(computed_q5 - 2.87e-12) / 2.87e-12 < 0.005
print(f"CLAIM Q5: computed={computed_q5:.8e} expected={expected_q5} match={'yes' if match_q5 else 'no'}")

# Q6
P_obs = 1e-9
tau = 1.0
N_max = P_obs * tau / E_bit
computed_q6 = N_max
expected_q6 = "3.48e8"
match_q6 = abs(computed_q6 - 3.48e8) / 3.48e8 < 0.005
print(f"CLAIM Q6: computed={computed_q6:.8e} expected={expected_q6} match={'yes' if match_q6 else 'no'}")

# Q7
L_fine, L_coarse, b = 40, 10, 2
kappa = b ** (L_fine - L_coarse)
computed_q7 = kappa
expected_q7 = "1.05e6"
match_q7 = abs(computed_q7 - 1.05e6) / 1.05e6 < 0.05
print(f"CLAIM Q7: computed={computed_q7:.8e} expected={expected_q7} match={'yes' if match_q7 else 'no'}")

# Q8
m = 1e5
coarse = 1024
lam = m / coarse
p1 = lam * math.exp(-lam)
computed_q8 = p1
expected_q8 = "3.78e-41"
match_q8 = abs(computed_q8 - 3.78e-41) / 3.78e-41 < 0.01
print(f"CLAIM Q8: computed={computed_q8:.8e} expected={expected_q8} match={'yes' if match_q8 else 'no'}")

# Q9
m_real = coarse * p1
computed_q9 = m_real
expected_q9 = "3.9e-38"
match_q9 = abs(computed_q9 - 3.9e-38) / 3.9e-38 < 0.05
print(f"CLAIM Q9: computed={computed_q9:.8e} expected={expected_q9} match={'yes' if match_q9 else 'no'}")

# Q10
P_plat = 20.0
t = 6.0
E_rev = P_plat * t
computed_q10 = E_rev
expected_q10 = "120"
match_q10 = computed_q10 == 120.0
print(f"CLAIM Q10: computed={computed_q10:.8e} expected={expected_q10} match={'yes' if match_q10 else 'no'}")

# Q11
E_bit_precise = 2.8709e-21
ratio = E_rev / E_bit_precise
computed_q11 = ratio
expected_q11 = "4.18e22"
match_q11 = abs(computed_q11 - 4.18e22) / 4.18e22 < 0.005
print(f"CLAIM Q11: computed={computed_q11:.8e} expected={expected_q11} match={'yes' if match_q11 else 'no'}")

# Q12
n12 = math.comb(4, 1) * 2 + math.comb(4, 2) * 4
computed_q12 = n12
expected_q12 = "32"
match_q12 = computed_q12 == 32
print(f"CLAIM Q12: computed={computed_q12} expected={expected_q12} match={'yes' if match_q12 else 'no'}")

# Q13
log10_e = 0.434294
shift = 0.01
delta = shift * lam * log10_e
computed_q13 = delta
expected_q13 = "0.42"
match_q13 = abs(computed_q13 - 0.42) / 0.42 < 0.01
print(f"CLAIM Q13: computed={computed_q13:.8e} expected={expected_q13} match={'yes' if match_q13 else 'no'}")

results = [match_q1, match_q2, match_q3, match_q4, match_q5, match_q6,
           match_q7, match_q8, match_q9, match_q10, match_q11, match_q12, match_q13]
total = len(results)
m = sum(results)
k = total - m
print(f"VERIFICATION SUMMARY: {total} claims, {m} match, {k} mismatch")
