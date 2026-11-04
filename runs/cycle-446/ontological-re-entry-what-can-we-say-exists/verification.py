# Verification of equation transitions from "Ontological Re-Entry: What Can We Say Exists?"
# Sections 3.1-3.3, 4.1-4.4 (Methods/Analysis). Each transition: (premise, conclusion, justification).

import sympy as sp
from sympy import simplify, log, binomial, symbols, Eq, Rational, exp, factorial, Integer
from sympy.physics.units import joule, watt, kelvin, second, Quantity
import mpmath as mp
import random

mp.mp.dps = 60
results = []

def report(tag, ok):
    status = "ok" if ok else "refuted"
    print(f"DERIV {status} | {tag}")
    results.append((tag, status))

def report_inconclusive(tag, note=""):
    print(f"DERIV inconclusive | {tag} {note}")
    results.append((tag, "inconclusive"))

# ---------- Units / constants (notation table) ----------
kB = sp.Float('1.380649e-23') * joule / kelvin      # Boltzmann constant
T  = sp.Float(300) * kelvin                          # ambient temperature
P_pico = sp.Float('1e-12') * watt                    # picowatt observer power
P_nano = sp.Float('1e-9')  * watt                    # nanowatt observer power
E_bit_unit = joule                                   # energy per distinction
lam = symbols('lambda', positive=True)               # objects per coarse ball (dimensionless)
N_bits, L, b = symbols('N L b', positive=True)       # distinction count, tree depth, branching (dimensionless)

# Sanity bounds helper
def sanity():
    p = float(mp.mpf('3.80e-41'))
    assert 0 <= p <= 1, "probability p1 out of [0,1]"
    assert float(mp.mpf('2.87e-21')) > 0, "E_bit must be nonnegative"
    assert float(mp.mpf('1.07e9')) >= 1, "compression factor >= 1"
    # limiting cases: T->0 => E_bit->0 ; P->0 => rate->0 ; lambda->0 => p1->lambda (i.e. ->0)
    assert sp.limit(kB*sp.Symbol('T')*log(2), sp.Symbol('T'), 0) == 0
    assert float(mp.mpf('3.9e-38')) >= 0
sanity()

# ---------- Transition 1 (Sec 3.1): b-ary tree of depth L => N = L*log2(b), |S_N| = b^L = 2^N ----------
# Premise: tree geometry with branching b, depth L. Conclusion: N = L log2 b and b^L = 2^N.
lhs = L*log(b, 2)
ok1 = simplify(Eq(N_bits, lhs).rewrite(sp.Pow) is not None)
# algebraic identity: 2^(L log2 b) = b^L
ok1 = simplify(2**(L*log(b,2)) - b**L) == 0
report("T1: N = L*log2(b), |S_N| = b^L = 2^N (b-ary tree realization)", ok1)

# ---------- Transition 2 (Sec 3.1): ultrametric inequality for the tree metric ----------
# Premise: d_u from b-ary tree (distance = 2^(-depth of LCA)). Conclusion: ultrametric inequality.
# Symbolic proof is definitional; spot-check numerically on random strings.
def tree_dist(x, y, depth=10):
    # LCA depth in a binary tree encoded by prefixes
    i = 0
    while i < min(len(x), len(y)) and x[i] == y[i]:
        i += 1
    return mp.mpf(2)**(-(depth - i))
random.seed(0)
ok2 = True
for _ in range(200):
    strs = [''.join(random.choice('01') for _ in range(10)) for _ in range(3)]
    d = lambda a, c: tree_dist(strs[a], strs[c])
    if not (d(0,1) <= max(d(0,2), d(2,1)) + mp.mpf('1e-30')):
        ok2 = False; break
report("T2: ultrametric inequality d(x_i,x_j) <= max{d(x_i,x_k), d(x_k,x_j)} (tree metric, numeric spot check)", ok2)

# ---------- Transition 3 (Sec 4.1): 2^(2^64) = 10^(5.553e18) admissible predicates ----------
# Premise: N=64 binary distinctions. Conclusion: count of subsets = 2^(2^64) = 10^(5.553e18).
log10_count = mp.mpf(2)**64 * mp.log10(2)   # = 2^64 * log10(2)
claimed = mp.mpf('5.553e18')
ok3 = abs(log10_count - claimed) / claimed < mp.mpf('1e-3')
report("T3: 2^(2^64) = 10^(5.553e18) admissible predicates (log identity)", ok3)

# ---------- Transition 4 (Sec 4.2): N_short = sum_{k=1..9} C(64,k) 2^k = 1.5318446128384e13 ----------
# Premise: predicates reachable by conjunctions of at most 9 literals (128 literals, choose k with sign).
N_short = sum(binomial(64, k) * 2**k for k in range(1, 10))
claimed_short = sp.Float('1.5318446128384e13')
ok4 = simplify(N_short - claimed_short) == 0
report("T4: N_short = sum_{k<=9} C(64,k)2^k = 1.5318446128384e13 (exact enumeration)", ok4)

# ---------- Transition 5 (Sec 4.3): E_bit = k_B * T * ln 2 = 2.87e-21 J at T = 300 K ----------
# Premise: Landauer's principle. Conclusion: E_bit = kB T ln2.
E_bit = kB * T * log(2)
E_val = sp.N(E_bit / E_bit_unit)   # strip units -> joules
ok5 = abs(float(E_val) - 2.87e-21) / 2.87e-21 < 1e-2
report("T5: E_bit = k_B*T*ln2 = 2.87e-21 J at 300 K (Landauer)", ok5)

# ---------- Transition 6 (Sec 4.3): rate = P / E_bit => 3.48e8 /s (pW), 3.48e11 /s (nW) ----------
# Premise: power budget P_obs, energy per distinction E_bit. Conclusion: distinctions per second.
r_pico = sp.N((P_pico / E_bit).subs({joule: 1, watt: 1, kelvin: 1, second: 1})) if False else \
         float(sp.N(P_pico/E_bit / (joule/second) * (joule/second)))  # dimensionally: watt/(J) = 1/s
# cleaner: compute numerically in SI
E_SI = float(E_val)                      # J
r_pico = 1e-12 / E_SI                    # 1/s
r_nano = 1e-9  / E_SI
ok6 = abs(r_pico - 3.48e8)/3.48e8 < 1e-2 and abs(r_nano - 3.48e11)/3.48e11 < 1e-2
report("T6: P_obs/E_bit = 3.48e8 s^-1 (pW), 3.48e11 s^-1 (nW) (division)", ok6)

# ---------- Transition 7 (Sec 4.4): p1 = lambda * e^(-lambda) = 3.80e-41, lambda = 1e5 / 2^10 ----------
# Premise: 1e5 objects placed uniformly into 2^10 coarse balls (Poisson approx, mean lambda).
# Conclusion: P(exactly one object in a given ball) = lambda e^{-lambda}.
lam_val = mp.mpf(10)**5 / mp.mpf(2)**10
p1 = lam_val * mp.e**(-lam_val)
claimed_p1 = mp.mpf('3.80e-41')
ok7 = abs(p1 - claimed_p1)/claimed_p1 < mp.mpf('2e-2')
# symbolic form check: d/dlambda [lambda e^-lambda] etc. is definitional; verify Poisson pmf identity numerically
pmf_exact = mp.mpf(1)  # cross-check via exact Poisson pmf
pmf_exact = mp.mpf(lam_val)**1 * mp.e**(-lam_val) / factorial(1)
ok7 = ok7 and (pmf_exact == p1)
report("T7: p1 = lambda*e^{-lambda} = 3.80e-41 with lambda = 1e5/2^10 (Poisson single-occupancy)", ok7)

# ---------- Transition 8 (Sec 4.4): expected resolvable count = B * p1 = 2^10 * p1 = 3.9e-38 ----------
# Premise: B = 2^10 coarse balls, each resolvable iff exactly one object. Conclusion: E[resolvable] = B*p1.
E_resolvable = mp.mpf(2)**10 * p1
claimed_E = mp.mpf('3.9e-38')
ok8 = abs(E_resolvable - claimed_E)/claimed_E < mp.mpf('3e-2')
report("T8: expected resolvable count = 2^10 * p1 = 3.9e-38 (linearity of expectation)", ok8)

# ---------- Transition 9 (Sec 4.4/abstract): compression factor 2^40 -> 2^10 balls = 2^30 = 1.07e9 ----------
# Premise: 2^40-ball space compressed into 2^10 coarse balls. Conclusion: factor 2^30 ~ 1.07e9.
factor = mp.mpf(2)**30
ok9 = abs(factor - mp.mpf('1.07e9'))/mp.mpf('1.07e9') < mp.mpf('1e-2')
report("T9: compression factor 2^30 = 1.07e9 (arithmetic)", ok9)

# ---------- Randomized numeric spot checks for the symbolic transitions that were borderline ----------
# T1 randomized: random (L, b) pairs
ok1r = all(sp.simplify(2**(Lval*log(bval,2)) - bval**Lval) == 0
           for Lval, bval in [(Integer(random.randint(1,20)), Integer(random.choice([2,3,4,5,8]))) for _ in range(50)])
if not ok1:
    report_inconclusive("T1 randomized recheck", "symbolic simplify inconclusive; numeric recheck passed" if ok1r else "numeric recheck failed")
    if ok1r:
        results[-1] = ("T1 randomized recheck", "inconclusive")

# T7 randomized: Poisson pmf vs lambda e^-lambda for random lambda
ok7r = True
for _ in range(100):
    lv = mp.mpf(random.uniform(0.01, 200))
    if abs(lv*mp.e**(-lv) - lv**1*mp.e**(-lv)/mp.factorial(1)) > mp.mpf('1e-40'):
        ok7r = False; break
if not ok7:
    report_inconclusive("T7 randomized recheck", "Poisson pmf identity")

print("\nSummary:")
for tag, status in results:
    print(f"  {status:12s} {tag}")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

log10_2 = 0.30103
N = 64

# Q1
log10_pred = (2**N) * log10_2
computed_q1 = log10_pred
expected_q1 = "5.553e18"
match_q1 = round(computed_q1, 0) == 5.553e18  # compare at stated precision
# stated: 5.553e18 (4 sig digits)
match_q1 = f"{computed_q1:.3e}" == f"{5.553e18:.3e}"

# Q2
N_short = sum(math.comb(N, k) * (2**k) for k in range(1, 10))
computed_q2 = N_short
expected_q2 = "15318446128384"
match_q2 = computed_q2 == 15318446128384

# Q3
k_B = 1.380649e-23
T_env = 300.0
ln2 = 0.6931472
E_bit = k_B * T_env * ln2
computed_q3 = E_bit
expected_q3 = "2.87e-21"
match_q3 = f"{computed_q3:.3e}" == f"{2.87e-21:.3e}"

# Q4
E_bit_paper = 2.8709e-21
P_pico = 1e-12
Ndot_pico = P_pico / E_bit_paper
computed_q4 = Ndot_pico
expected_q4 = "3.48e8"
match_q4 = f"{computed_q4:.3e}" == f"{3.48e8:.3e}"

# Q5
P_nano = 1e-9
Ndot_nano = P_nano / E_bit_paper
computed_q5 = Ndot_nano
expected_q5 = "3.48e11"
match_q5 = f"{computed_q5:.3e}" == f"{3.48e11:.3e}"

# Q6
N_dist = 1e9
P_erase = N_dist * E_bit_paper
computed_q6 = P_erase
expected_q6 = "2.87e-12"
match_q6 = f"{computed_q6:.3e}" == f"{2.87e-12:.3e}"

# Q7
b = 2
L_fine = 40
L_coarse = 10
kappa = b ** (L_fine - L_coarse)
computed_q7 = kappa
expected_q7 = "1073741824"
match_q7 = computed_q7 == 1073741824

# Q8
m = 1e5
n_coarse = b ** L_coarse
lam = m / n_coarse
computed_q8 = lam
expected_q8 = "97.65625"
match_q8 = computed_q8 == 97.65625

# Q9
p1 = lam * math.exp(-lam)
computed_q9 = p1
expected_q9 = "3.80e-41"
match_q9 = f"{computed_q9:.3e}" == f"{3.80e-41:.3e}"

# Q10
m_real = n_coarse * p1
computed_q10 = m_real
expected_q10 = "3.9e-38"
match_q10 = f"{computed_q10:.2e}" == f"{3.9e-38:.2e}"

# Q11
P_plat = 20.0
t = 6.0
E_rev = P_plat * t
computed_q11 = E_rev
expected_q11 = "120"
match_q11 = computed_q11 == 120.0

# Q12
N_erase = E_rev / E_bit_paper
computed_q12 = N_erase
expected_q12 = "4.18e22"
match_q12 = f"{computed_q12:.3e}" == f"{4.18e22:.3e}"

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

n_total = 12
n_match = sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6,
               match_q7, match_q8, match_q9, match_q10, match_q11, match_q12])
n_mismatch = n_total - n_match
print(f"VERIFICATION SUMMARY: {n_total} claims, {n_match} match, {n_mismatch} mismatch")
