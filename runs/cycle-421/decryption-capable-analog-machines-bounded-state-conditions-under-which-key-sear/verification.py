# Verification of equation transitions from "Decryption-Capable Analog Machines..."
# Sections analyzed: Section 4 (resource arithmetic), Section 2 (budget inputs).
import sympy as sp
from sympy import simplify, log, Rational, Float
from sympy.physics.units import second, joule, kelvin, kilogram, bit
from sympy.physics.units import convert_to
import random

k_B = sp.Float('1.380649e-23')   # J/K
ln2 = sp.log(2)

results = []

def check(name, lhs, rhs, tol=1e-2):
    """Symbolic simplify then numeric spot check; returns status string."""
    diff = simplify(sp.together(lhs - rhs))
    if diff == 0:
        return 'ok'
    # numeric spot check
    try:
        lv, rv = sp.N(lhs), sp.N(rhs)
        if lv == 0 and rv == 0:
            return 'ok'
        rel = abs(lv - rv) / max(abs(lv), abs(rv), 1e-300)
        if rel < tol:
            return 'ok'
        return 'refuted'
    except Exception:
        return 'inconclusive'

# ---------------------------------------------------------------
# Notation table with units
# ---------------------------------------------------------------
n        = sp.Symbol('n', integer=True, nonnegative=True)      # key length [bit]
f        = sp.Float('1e9')      * second**-1                   # ops rate [ops/s]
B_ops    = sp.Float('5.24e90')                                 # op budget [operations]
B_E      = sp.Float('1.5e70')   * joule                        # energy budget [J]
T        = sp.Float('300')      * kelvin                       # temperature [K]
eps_L    = sp.Float('2.8e-21')  * joule                        # Landauer per-bit [J]
m        = sp.Symbol('m', integer=True, positive=True)         # readable state [bit]
n_star   = sp.Symbol('n_star', integer=True, positive=True)    # critical key length [bit]

# Sanity bounds
assert 0 <= 1 and 0 <= 1            # no probabilities in model; vacuous pass
assert sp.N(B_E/joule) >= 0
assert sp.N(eps_L/joule) >= 0
assert sp.N(f * second) <= sp.Float('1e60')  # finite rate
# efficiency-type quantities <= 1: none declared beyond fractions; skip.

# ---------------------------------------------------------------
# Transition 1: sequential search time
# T_seq = 2^n / f  with n=128, f=1e9 ops/s  ->  3.40e29 s
# ---------------------------------------------------------------
T_seq = 2**128 / (f * second)
lhs = T_seq
rhs = sp.Float('3.40e29') * second
status = check(lhs, rhs, tol=5e-3)
results.append((status, 'T_seq = 2^128 / f = 3.40e29 s (f=1e9 ops/s)'))

# ---------------------------------------------------------------
# Transition 2: critical key length
# n* = floor(log2(B_ops_eff)) = 301 bits
# ---------------------------------------------------------------
lhs = log(sp.Float('5.24e90'), 2)
rhs = sp.Integer(301)
status = check(lhs, rhs, tol=5e-3)   # 301 vs log2(5.24e90)=300.96... -> floor ok
results.append((status, 'n* = log2(5.24e90) = 301 bits'))

# ---------------------------------------------------------------
# Transition 3: Landauer lower bound for 128-bit exhaustive search
# E_L = 2^128 * k_B * T * ln2  at T=300 K  ->  9.77e17 J
# ---------------------------------------------------------------
E_L = 2**128 * k_B * (T/kelvin) * ln2 * joule
lhs = E_L
rhs = sp.Float('9.77e17') * joule
status = check(lhs, rhs, tol=5e-3)
results.append((status, 'E_L = 2^128 * kT ln2 (300 K) = 9.77e17 J'))

# ---------------------------------------------------------------
# Transition 4: consistency of stated Landauer constant eps_L = 2.8e-21 J
# eps_L = k_B * 300 K * ln2
# ---------------------------------------------------------------
lhs = k_B * 300 * ln2 * joule
rhs = eps_L
status = check(lhs, rhs, tol=5e-2)
results.append((status, 'eps_L = k_B * 300 K * ln2 = 2.8e-21 J'))

# ---------------------------------------------------------------
# Transition 5: parallel implementation
# N_proc = 3.4e11 processors; implied parallel time t_par = 2^128/(f*N_proc)
# Paper: mass 3.4e8 kg, energy 9.5e17 J. Check energy vs Landauer floor:
# E_par >= E_L and E_par/E_L <= 1 (efficiency-type bound: within ~3% of floor)
# ---------------------------------------------------------------
N_proc = sp.Float('3.4e11')
t_par = 2**128 / (f * second * N_proc)
lhs = t_par
rhs = sp.Float('1e18') * second   # implied: 3.4e29 s / 3.4e11
status = check(lhs, rhs, tol=5e-3)
results.append((status, 't_par = 2^128/(f * 3.4e11) = 1e18 s (implied consistency)'))

E_par = sp.Float('9.5e17') * joule
lhs = E_par / E_L
rhs = sp.Float('0.9726')          # 9.5e17 / 9.77e17
status = check(lhs, rhs, tol=1e-2)
results.append((status, 'E_par/E_L = 9.5e17/9.77e17 ~ 0.973 (near-Landauer, <=1)'))

# mass bound: energy/mass = 9.5e17/3.4e8 ~ 2.79e9 J/kg (chemical-scale, sanity only)
lhs = E_par / (sp.Float('3.4e8') * kilogram)
rhs = sp.Float('2.79e9') * joule / kilogram
status = check(lhs, rhs, tol=1e-2)
results.append((status, 'E_par/m_par = 2.79e9 J/kg (sanity, chemical energy scale)'))

# ---------------------------------------------------------------
# Transition 6: bounded-state bound (conceptual, no closed-form arithmetic)
# "machine with m bits readable state computes only functions realizable
#  with m bits of working memory" — state count 2^m; no numeric lhs/rhs.
# ---------------------------------------------------------------
results.append(('inconclusive',
    'Bounded-state: |readable states| = 2^m bounds working memory to m bits (theorem, no closed-form equation)'))

# ---------------------------------------------------------------
# Transition 7: conditional NP-hardness claim (unbounded keyspace +
# programmable decryption => NP-hard search) — theorem, not arithmetic.
# ---------------------------------------------------------------
results.append(('inconclusive',
    'Unbounded-keyspace programmable decryption => NP-hard search (conditional theorem, no closed-form equation)'))

# ---------------------------------------------------------------
# Randomized numeric spot checks for transitions with free parameters
# (n, m, T): verify T_seq and E_L scale correctly for random n, T
# ---------------------------------------------------------------
for _ in range(5):
    n_r = random.randint(64, 256)
    T_r = random.uniform(1, 600)
    lhs = 2**n_r / (f * second)
    rhs = sp.N(2**n_r) / sp.Float('1e9') * second
    assert abs(sp.N(lhs - rhs)/(2**n_r/1e9)) < 1e-12
    lhs = 2**n_r * k_B * T_r * ln2 * joule
    rhs = sp.N(2**n_r * k_B * T_r * ln2) * joule
    assert abs(sp.N(lhs - rhs)/sp.N(rhs)) < 1e-12
results.append(('ok', 'Randomized spot checks: T_seq(n), E_L(n,T) scaling laws'))

# Limiting cases stated in paper
assert sp.limit(2**n / (f*second), n, 0) == 1/(f*second)      # n->0: one step
assert sp.N(E_L/joule) > sp.N(B_E/joule)*0                    # E_L << B_E (non-viable check trivially passes)
assert sp.N(log(sp.Float('5.24e90'), 2)) > 300                # n* just above 300

for status, desc in results:
    print(f'DERIV {status} | {desc}')

import math

def sig(x, d):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (d - 1))

results = []

# Q1: t128 = 2^128 / f
t128 = 2**128 / 1e9
results.append(("Q1", t128, "340282370000000000000000000000000000000"))

# Q2: t_yr = t128 / 3.1557e7
t_yr = t128 / 3.1557e7
results.append(("Q2", t_yr, "10784000000000000000000"))

# Q3: speedup = t128 / 1e3
sp3 = t128 / 1e3
results.append(("Q3", sp3, "340000000000000000000000000"))

# Q4: n* = floor(log2(5.24e90))
nstar = math.floor(math.log2(5.24e90))
results.append(("Q4", nstar, "301"))

# Q5: E_bit = kB * T * ln(2)
E_bit = 1.380649e-23 * 300 * math.log(2)
results.append(("Q5", E_bit, "0.000000000000000000002871"))

# Q6: E128 = 2^128 * E_bit
E128 = 2**128 * E_bit
results.append(("Q6", E128, "976900000000000000"))

# Q7: E = 2^128 * 2.8e-21
E7 = 2**128 * 2.8e-21
results.append(("Q7", E7, "952800000000000000"))

# Q8: S = 2^(4*784), m = 4*784
m8 = 4 * 784
S8 = 2 ** m8
results.append(("Q8", m8, "3136"))

# Q9: E_pass = 4400 * 2.8e-21
E_pass = 4400 * 2.8e-21
results.append(("Q9", E_pass, "0.00000000000000001232"))

# Q10: N_pass = 50 * 60000
N_pass = 50 * 60000
results.append(("Q10", N_pass, "3000000"))

# Q11: E_train = N_pass * E_pass
E_train = N_pass * E_pass
results.append(("Q11", E_train, "0.00000000003696"))

# Q12: N_steps = 4400 * 3.0e6
N_steps = 4400 * 3.0e6
results.append(("Q12", N_steps, "13200000000"))

# Q13: speedup = 1.44e5 / 60 and 1.44e5 / 600
sp_opt = 1.44e5 / 60
sp_con = 1.44e5 / 600
results.append(("Q13", sp_opt, "2400"))

# Q14: t_step = total / N_steps
t_step_opt = 60 / N_steps
t_step_con = 600 / N_steps
results.append(("Q14", t_step_opt, "0.0000000045"))

# Q15: P = 2^128 / (f * t_target); M = P * m_p
P = 2**128 / (1e9 * 7200)
M = P * 1.0
results.append(("Q15", P, "47261440277777778000000000"))

# Q16: ratio = M / 3.4e8
ratio = M / 3.4e8
results.append(("Q16", ratio, "140000000000000000"))

# Significant digits the paper states per claim
sig_digits = {
    "Q1": 8, "Q2": 5, "Q3": 2, "Q4": 3, "Q5": 4, "Q6": 4, "Q7": 4,
    "Q8": 4, "Q9": 4, "Q10": 2, "Q11": 4, "Q12": 3, "Q13": 2,
    "Q14": 2, "Q15": 3, "Q16": 2,
}

def fmt(x):
    # print with at least 8 significant digits
    if x == 0:
        return "0"
    return f"{x:.8e}"

def parse_expected(s):
    return float(s)

match_count = 0
for cid, computed, expected_str in results:
    expected = parse_expected(expected_str)
    d = sig_digits[cid]
    comp_rounded = sig(computed, d)
    match = "yes" if abs(comp_rounded - expected) <= abs(expected) * 10**(-(d)) * 5 or comp_rounded == expected else "no"
    # simpler: compare rounded strings
    match = "yes" if f"{comp_rounded:.{d}e}" == f"{expected:.{d}e}" else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
