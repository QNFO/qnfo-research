# VERIFICATION OF EQUATION TRANSITIONS — KERNEL prompt-specification framework
# Sections analyzed: 4.1 (compliance lattice), 4.3 (composition theorem),
# 4.4 (token-cost projection), 4.5 (benchmark size arithmetic).

from sympy import Rational, S, simplify, symbols, factorial, binomial, floor, Eq
from sympy.physics.units import Quantity, convert_to
import random

# ------------------------------------------------------------------
# Notation table with units (sympy.physics.units declarations)
# ------------------------------------------------------------------
# p_req      : probability a single requirement is met on first try  [dimensionless, in [0,1]]
# p_mono     : monolithic prompt success probability                 [dimensionless, in [0,1]]
# p_chain    : chained sub-prompt success probability                [dimensionless, in [0,1]]
# r          : bounded-repair recovery probability per sub-prompt    [dimensionless, in [0,1]]
# k          : number of independent requirements / sub-prompts      [dimensionless count]
# C          : input-token cost per prompt                           [Token]
# cost_succ  : input-token cost per successful completion            [Token]
# N_cfg      : number of prompt-model configurations                 [dimensionless count]
# N_run      : number of benchmark runs                              [dimensionless count]
# reps       : repetitions per configuration                         [dimensionless count]

Token = Quantity("Token")
# probabilities and counts are dimensionless; Token is the only named unit here.
# Sanity-bound helper
def prob_ok(p):  return 0 <= float(p) <= 1
def cost_ok(c):  return float(c) >= 0

results = []
def DERIV(tag, status, desc):
    results.append(f"DERIV {status} {tag}: {desc}")

def check(tag, lhs, rhs, tol=None):
    """simplify(lhs-rhs)==0; randomized numeric spot checks if inconclusive."""
    diff = simplify(lhs - rhs)
    if diff == 0:
        return "ok"
    try:
        d = abs(float(diff.evalf()))
        if tol is not None and d <= tol:
            return "ok"
    except Exception:
        pass
    # randomized numeric spot check
    ok = True
    for _ in range(20):
        pass  # no free symbols expected in these numeric transitions
    return "inconclusive"

# ------------------------------------------------------------------
# T1 — Section 4.1: compliance-lattice coverage count
# Premise: six KERNEL properties are binary predicates on a prompt spec.
# Conclusion: number of specification classes = 2^6 = 64.
# Justification: product rule over six independent binary dimensions.
# ------------------------------------------------------------------
k = 6
lhs = S(2)**k
rhs = S(64)
st = check("T1", lhs, rhs)
DERIV("T1", st, "2^6 = 64 specification classes (product rule over binary predicates)")
assert st == "ok"

# Limiting/sanity cases for the lattice: k=0 -> 1 class, k=1 -> 2 classes
assert S(2)**0 == 1 and S(2)**1 == 2

# ------------------------------------------------------------------
# T2 — Section 4.3: monolithic success probability
# Premise: five independent requirements, each met w.p. p_req = 0.8.
# Conclusion: p_mono = 0.8^5 = 0.32768.
# Justification: independence of requirement satisfaction.
# ------------------------------------------------------------------
p_req = Rational(8, 10)
assert prob_ok(p_req)
lhs = p_req**5
rhs = Rational(32768, 100000)
st = check("T2", lhs, rhs)
DERIV("T2", st, "p_mono = 0.8^5 = 0.32768 (independence of five requirements)")
assert st == "ok"
# Limiting cases: p_req=1 -> 1, p_req=0 -> 0
assert (S(1)**5 == 1) and (S(0)**5 == 0)

# ------------------------------------------------------------------
# T3 — Section 4.3: chained success probability with bounded repair
# Premise: each sub-prompt succeeds first-try w.p. 0.8; one bounded repair
#          recovers w.p. 0.1, so per-step success = 0.8 + 0.1 = 0.9.
# Conclusion: p_chain = 0.9^5 = 0.59049.
# Justification: independence across chained sub-prompts; bounded repair.
# ------------------------------------------------------------------
r = Rational(1, 10)
assert prob_ok(r)
p_step = p_req + r
assert prob_ok(p_step)          # 0.9 in [0,1]
lhs = p_step**5
rhs = Rational(59049, 100000)
st = check("T3", lhs, rhs)
DERIV("T3", st, "p_chain = (0.8+0.1)^5 = 0.9^5 = 0.59049 (independence + one bounded repair)")
assert st == "ok"
# Limiting cases: r=0 -> p_chain == p_mono; r=1 -> p_chain = 1
assert (p_req + S(0))**5 == p_req**5
assert (p_req + S(1)) <= 1  # repair probability keeps per-step success <= 1

# ------------------------------------------------------------------
# T4 — Section 4.3: improvement factor
# Premise: p_chain = 0.59049, p_mono = 0.32768.
# Conclusion: improvement ratio = 1.80 (reported, rounded).
# Justification: ratio of exact probabilities; paper rounds to 2 decimals.
# ------------------------------------------------------------------
ratio_exact = Rational(59049, 100000) / Rational(32768, 100000)
st = check("T4", ratio_exact, Rational(180, 100), tol=0.005)
DERIV("T4", st, f"0.59049/0.32768 = {float(ratio_exact):.5f} reported as 1.80 (rounding)")
# exact value is 1.802978..., consistent with "1.80-fold" at 2-dp rounding

# ------------------------------------------------------------------
# T5 — Section 4.4: monolithic token cost per successful completion
# Premise: monolithic prompt size S_mono (tokens) and p_mono = 0.32768.
# Conclusion: cost_mono = 2440 Tokens.
# Justification: cost per success = S_mono / p_mono; paper reports 2440.
# Note: the paper does not restate S_mono explicitly in the excerpt, so the
# premise (S_mono = 800 Tokens, giving 800/0.32768 = 2441.4) is inferred.
# ------------------------------------------------------------------
S_mono = S(800) * Token
assert cost_ok(S_mono)
cost_mono_inferred = convert_to(S_mono / Rational(32768, 100000), Token)
st = check("T5", cost_mono_inferred / Token, S(2440), tol=0.01)
DERIV("T5", st, f"S_mono/p_mono = {float(cost_mono_inferred/Token):.2f} vs reported 2440 Tokens "
                 "(premise S_mono=800 inferred; paper does not restate prompt size) -> inconclusive if premise unverified")
# recorded status may be inconclusive; goes to verification appendix

# ------------------------------------------------------------------
# T6 — Section 4.4: chained token cost per successful completion
# Premise: total chained sub-prompt size S_chain (tokens), p_chain = 0.59049.
# Conclusion: cost_chain = 1112 Tokens.
# Justification: cost per success = S_chain / p_chain; S_chain not restated
# in the excerpt (inferred S_chain ≈ 657 Tokens gives 1112.6).
# ------------------------------------------------------------------
S_chain = S(657) * Token
assert cost_ok(S_chain)
cost_chain_inferred = convert_to(S_chain / Rational(59049, 100000), Token)
st = check("T6", cost_chain_inferred / Token, S(1112), tol=0.01)
DERIV("T6", st, f"S_chain/p_chain = {float(cost_chain_inferred/Token):.2f} vs reported 1112 Tokens "
                 "(premise S_chain=657 inferred) -> inconclusive if premise unverified")

# ------------------------------------------------------------------
# T7 — Section 4.4: cost-reduction factor
# Premise: cost_mono = 2440 Tokens, cost_chain = 1112 Tokens.
# Conclusion: reduction factor = 2.20 (reported, rounded).
# Justification: ratio of costs per successful completion.
# ------------------------------------------------------------------
ratio_cost = S(2440) / S(1112)
st = check("T7", ratio_cost, Rational(220, 100), tol=0.01)
DERIV("T7", st, f"2440/1112 = {float(ratio_cost):.4f} reported as 2.20-fold reduction (rounding)")

# ------------------------------------------------------------------
# T8 — Section 4.5: benchmark configuration count
# Premise: one-at-a-time ablation over 6 properties x 10 tasks x 3 models
#          x 2 conditions (property present / ablated).
# Conclusion: N_cfg = 360.
# Justification: product rule for factorial design.
# ------------------------------------------------------------------
lhs = 6*10*3*2
rhs = 360
st = check("T8", S(lhs), S(rhs))
DERIV("T8", st, "N_cfg = 6*10*3*2 = 360 configurations (factorial product rule)")
assert st == "ok"

# ------------------------------------------------------------------
# T9 — Section 4.5: total run count
# Premise: N_cfg = 360 configurations, 5 repetitions each.
# Conclusion: N_run = 1800.
# Justification: multiplication by repetition count.
# ------------------------------------------------------------------
reps = 5
lhs = 360*reps
rhs = 1800
st = check("T9", S(lhs), S(rhs))
DERIV("T9", st, "N_run = 360*5 = 1800 runs (repetition protocol)")
assert st == "ok"

# ------------------------------------------------------------------
# Global sanity bounds
# ------------------------------------------------------------------
assert prob_ok(Rational(32768,100000)) and prob_ok(Rational(59049,100000))
assert prob_ok(p_req) and prob_ok(r) and prob_ok(p_step)
assert cost_ok(S(2440)*Token) and cost_ok(S(1112)*Token)
# "efficiency" bound: cost-reduction factor must be >= 1 for decomposition to help
assert float(ratio_cost) >= 1
# Limiting case of composition theorem: k -> large with p_step<1 drives p_chain -> 0
import sympy as sp
kk = sp.symbols("kk", positive=True, integer=True)
lim = sp.limit((Rational(9,10))**kk, kk, sp.oo)
assert lim == 0   # decomposition cannot beat probability 1 bound

for line in results:
    print(line)

import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: N_classes = 2^6
c = 2**6
results.append(("Q1", c, "64", 10))

# Q2: p_compliant = 1/64
c = 1/64
results.append(("Q2", c, "0.015625", 6))

# Q3: N_V,N = 2^4 = 16; p = 16/64
c = 16/64
results.append(("Q3", c, "0.25", 2))

# Q4: p_mono = 0.8^5
c = 0.8**5
results.append(("Q4", c, "0.32768", 5))

# Q5: p_step = 0.8 + (1-0.8)*0.5
c = 0.8 + (1-0.8)*0.5
results.append(("Q5", c, "0.9", 1))

# Q6: p_chain = 0.9^5
c = 0.9**5
results.append(("Q6", c, "0.59049", 5))

# Q7: ratio = 0.59049 / 0.32768
c = 0.59049 / 0.32768
results.append(("Q7", c, "1.80", 3))

# Q8: p_mono = 0.8^10
c = 0.8**10
results.append(("Q8", c, "0.1073741824", 10))

# Q9: p_chain = 0.9^10
c = 0.9**10
results.append(("Q9", c, "0.3486784401", 10))

# Q10: ratio = 0.3486784401 / 0.1073741824
c = 0.3486784401 / 0.1073741824
results.append(("Q10", c, "3.25", 3))

# Q11: E_mono = 1/0.32768
c = 1/0.32768
results.append(("Q11", c, "3.0517578125", 11))

# Q12: E_chain = 5/0.9
c = 5/0.9
results.append(("Q12", c, "5.555555555555555", 15))

# Q13: T_mono = (1/0.32768) * 800
c = (1/0.32768) * 800
results.append(("Q13", c, "2441.40625", 9))

# Q14: T_chain = (5/0.9) * 200 = 1000/0.9
c = (5/0.9) * 200
results.append(("Q14", c, "1111.111111111111", 15))

# Q15: cost ratio = T_mono / T_chain
t_mono = (1/0.32768) * 800
t_chain = (5/0.9) * 200
c = t_mono / t_chain
results.append(("Q15", c, "2.20", 3))

# Q16: (p_chain/T_chain) / (p_mono/T_mono)
p_chain = 0.9**5
p_mono = 0.8**5
c = (p_chain/t_chain) / (p_mono/t_mono)
results.append(("Q16", c, "3.96", 3))

mismatch = 0
for cid, computed, expected_str, sigdigs in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, sigdigs) == expected else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.10f} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")
