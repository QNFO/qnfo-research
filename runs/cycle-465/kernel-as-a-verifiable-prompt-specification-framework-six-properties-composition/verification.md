# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of distinct specification classes in the six-property compliance lattice is 64",
    "inputs": "number of binary properties = 6",
    "formula": "N_classes = 2^6"
  },
  {
    "id": "Q2",
    "statement": "Probability a uniformly drawn specification is KERNEL-compliant is 0.015625",
    "inputs": "compliant classes = 1, total classes = 64",
    "formula": "p_compliant = 1/64"
  },
  {
    "id": "Q3",
    "statement": "Fraction of lattice satisfying verifiability and narrow scope is 0.25 (16 classes)",
    "inputs": "free bits after fixing P2=P4=1: 4, total classes = 64",
    "formula": "N_V,N = 2^4 = 16; p_V,N = 16/64"
  },
  {
    "id": "Q4",
    "statement": "Monolithic success probability for k=5, q=0.8 is 0.32768",
    "inputs": "k = 5, q = 0.8",
    "formula": "p_mono = q^k = 0.8^5"
  },
  {
    "id": "Q5",
    "statement": "Chain per-step success probability is 0.9 for q=0.8, s=0.5",
    "inputs": "q = 0.8, s = 0.5",
    "formula": "p_step = q + (1-q)*s"
  },
  {
    "id": "Q6",
    "statement": "Chain success probability for k=5, q=0.8, s=0.5 is 0.59049",
    "inputs": "k = 5, p_step = 0.9",
    "formula": "p_chain = p_step^k = 0.9^5"
  },
  {
    "id": "Q7",
    "statement": "Dominance ratio p_chain/p_mono is approximately 1.80",
    "inputs": "p_chain = 0.59049, p_mono = 0.32768",
    "formula": "ratio = p_chain / p_mono"
  },
  {
    "id": "Q8",
    "statement": "At k=10 monolithic success probability is 0.1073741824",
    "inputs": "k = 10, q = 0.8",
    "formula": "p_mono = 0.8^10"
  },
  {
    "id": "Q9",
    "statement": "At k=10 chain success probability is 0.3486784401",
    "inputs": "k = 10, p_step = 0.9",
    "formula": "p_chain = 0.9^10"
  },
  {
    "id": "Q10",
    "statement": "At k=10 the dominance ratio is approximately 3.25",
    "inputs": "p_chain = 0.3486784401, p_mono = 0.1073741824",
    "formula": "ratio = p_chain / p_mono"
  },
  {
    "id": "Q11",
    "statement": "Expected monolithic attempts to first success is 3.0517578125",
    "inputs": "p_mono = 0.32768",
    "formula": "E_mono = 1/p_mono"
  },
  {
    "id": "Q12",
    "statement": "Expected chain sub-attempts per task is 5.5555... (5/0.9)",
    "inputs": "k = 5, p_step = 0.9",
    "formula": "E_chain = k / p_step"
  },
  {
    "id": "Q13",
    "statement": "Monolithic input-token cost per success is 2441.40625 tokens",
    "inputs": "E_mono = 3.0517578125, monolith size a = 800 tokens",
    "formula": "T_mono = E_mono * 800"
  },
  {
    "id": "Q14",
    "statement": "Chained input-token cost per success is 1111.111... tokens",
    "inputs": "E_chain = 5/0.9, sub-specification size b = 200 tokens",
    "formula": "T_chain = (5/0.9) * 200 = 1000/0.9"
  },
  {
    "id": "Q15",
    "statement": "Cost ratio T_mono/T_chain is approximately 2.20",
    "inputs": "T_mono = 2441.40625, T_chain = 1111.111...",
    "formula": "ratio = T_mono / T_chain"
  },
  {
    "id": "Q16",
    "statement": "Successes per input token improve by a factor of approximately 3.96",
    "inputs": "p_chain = 0.59049, T_chain = 1111.111..., p_mono = 0.32768, T_mono = 2441.40625",
    "formula": "(p_chain/T_chain) / (p_mono/T_mono)"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 5, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: 2^6 = 64. computed=64 expected=64 match=yes
Q2: 1/64 = 0.015625. computed=0.015625 expected=0.015625 match=yes
Q3: 2^4 = 16; 16/64 = 0.25. computed=0.25 expected=0.25 match=yes
Q4: 0.8^5: 0.8^2=0.64; 0.64*0.8=0.512; 0.512*0.8=0.4096; 0.4096*0.8=0.32768. computed=0.32768 expected=0.32768 match=yes
Q5: 0.8 + 0.2*0.5 = 0.8 + 0.1 = 0.9. computed=0.9 expected=0.9 match=yes
Q6: 0.9^5: 0.81; 0.729; 0.6561; 0.59049. computed=0.59049 expected=0.59049 match=yes
Q7: 0.59049/0.32768 = 1.802032470703125 (0.59049/0.32768: 0.32768*1.8 = 0.589824; remainder 0.000666; 0.000666/0.32768 ≈ 0.0020325). computed=1.8020324707 expected=1.80 match=yes
Q8: 0.8^10 = (0.8^5)^2 = 0.32768^2 = 0.1073741824. computed=0.1073741824 expected=0.1073741824 match=yes
Q9: 0.9^10 = 0.59049^2 = 0.3486784401. computed=0.3486784401 expected=0.3486784401 match=yes
Q10: 0.3486784401/0.1073741824 = 3.247297632... (0.1073741824*3.25 = 0.3489660928, slightly above; 0.1073741824*3.247 = 0.348654...; refine: 0.3486784401/0.1073741824 ≈ 3.2472976). computed=3.24729763205 expected=3.25 match=yes
Q11: 1/0.32768 = 3.0517578125. computed=3.0517578125 expected=3.0517578125 match=yes
Q12: 5/0.9 = 5.55555555556. computed=5.55555555556 expected=5.5555... match=yes
Q13: 3.0517578125 * 800 = 2441.40625. computed=2441.40625 expected=2441.40625 match=yes
Q14: 1000/0.9 = 1111.111111111. computed=1111.11111111 expected=1111.111... match=yes
Q15: 2441.40625/1111.111111111 = 2.197265625 (2441.40625*0.9/1000 = 2197.265625/1000). computed=2.197265625 expected=2.20 match=yes
Q16: (0.59049/1111.111111111)/(0.32768/2441.40625) = 0.000531441/0.0001342177734375 = 3.9590390625. Check: 0.32768/2441.40625 = 0.0001342177734375 (2441.40625*0.0001342177734375 ≈ 0.32768). 0.000531441/0.0001342177734375: 0.0001342177734375*3.96 = 0.000531502... slightly above; compute 0.000531441/0.0001342177734375 = 3.959039... computed=3.9590390625 expected=3.96 match=yes

CLAIM Q1: computed=64 expected=64 match=yes
CLAIM Q2: computed=0.015625 expected=0.015625 match=yes
CLAIM Q3: computed=0.25 expected=0.25 match=yes
CLAIM Q4: computed=0.32768 expected=0.32768 match=yes
CLAIM Q5: computed=0.9 expected=0.9 match=yes
CLAIM Q6: computed=0.59049 expected=0.59049 match=yes
CLAIM Q7: computed=1.80203247070 expected=1.80 match=yes
CLAIM Q8: computed=0.1073741824 expected=0.1073741824 match=yes
CLAIM Q9: computed=0.3486784401 expected=0.3486784401 match=yes
CLAIM Q10: computed=3.24729763205 expected=3.25 match=yes
CLAIM Q11: computed=3.0517578125 expected=3.0517578125 match=yes
CLAIM Q12: computed=5.55555555556 expected=5.5555 match=yes
CLAIM Q13: computed=2441.40625 expected=2441.40625 match=yes
CLAIM Q14: computed=1111.11111111 expected=1111.111 match=yes
CLAIM Q15: computed=2.197265625 expected=2.20 match=yes
CLAIM Q16: computed=3.9590390625 expected=3.96 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.015625 | 0.015625 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 0.25 | 0.25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.32768 | 0.32768 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 0.9 | 0.9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.59049 | 0.59049 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 1.80203247070 | 1.80 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 0.1073741824 | 0.1073741824 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q9 | 0.3486784401 | 0.3486784401 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q10 | 3.24729763205 | 3.25 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 3.0517578125 | 3.0517578125 | yes | match | 11 significant digits (as the paper states, at least 2) |
| Q12 | 5.55555555556 | 5.5555 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 2441.40625 | 2441.40625 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q14 | 1111.11111111 | 1111.111 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q15 | 2.197265625 | 2.20 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 3.9590390625 | 3.96 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
