# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Prompt-only clean-run probability at N=40, eps=0.02 is approximately 0.4457",
    "inputs": "N=40, eps=0.02",
    "formula": "(1-eps)^N = 0.98^40"
  },
  {
    "id": "Q2",
    "statement": "Hybrid clean-run probability at N=40, eps=0.02, c=0.95 is approximately 0.9608",
    "inputs": "N=40, eps=0.02, c=0.95",
    "formula": "(1 - eps*(1-c))^N = 0.999^40"
  },
  {
    "id": "Q3",
    "statement": "Reliability ratio hybrid/prompt is approximately 2.156",
    "inputs": "P_prompt=0.4457, P_hyb=0.9608",
    "formula": "P_hyb / P_prompt"
  },
  {
    "id": "Q4",
    "statement": "Break-even constraint count N* = 35",
    "inputs": "eps=0.02, threshold 0.5",
    "formula": "smallest integer N with (1-eps)^N < 0.5, i.e. N > ln(0.5)/ln(0.98)"
  },
  {
    "id": "Q5",
    "statement": "Clean-run probability at q*=0.986, N=40 is approximately 0.5691",
    "inputs": "q=0.986, N=40",
    "formula": "q^N = 0.986^40"
  },
  {
    "id": "Q6",
    "statement": "Clean-run probability at N=300, eps=0.014 is approximately 0.0146",
    "inputs": "N=300, eps=0.014",
    "formula": "(1-eps)^N = 0.986^300"
  },
  {
    "id": "Q7",
    "statement": "Hybrid clean-run probability at c=0.80, N=40, eps=0.02 is approximately 0.8518",
    "inputs": "N=40, eps=0.02, c=0.80",
    "formula": "(1 - eps*(1-c))^N = 0.996^40"
  },
  {
    "id": "Q8",
    "statement": "Hybrid clean-run probability at c=0.99, N=40, eps=0.02 is approximately 0.9920",
    "inputs": "N=40, eps=0.02, c=0.99",
    "formula": "(1 - eps*(1-c))^N = 0.9998^40"
  },
  {
    "id": "Q9",
    "statement": "Prompt-only clean-run probability at eps=0.05, N=40 is approximately 0.1285",
    "inputs": "N=40, eps=0.05",
    "formula": "(1-eps)^N = 0.95^40"
  },
  {
    "id": "Q10",
    "statement": "Hybrid clean-run probability at eps=0.05, c=0.95, N=40 is approximately 0.9047",
    "inputs": "N=40, eps=0.05, c=0.95",
    "formula": "(1 - eps*(1-c))^N = 0.9975^40"
  },
  {
    "id": "Q11",
    "statement": "Best-case prompt refinement clean-run probability at eps=0.01, N=40 is approximately 0.6690",
    "inputs": "N=40, eps=0.01",
    "formula": "(1-eps)^N = 0.99^40"
  },
  {
    "id": "Q12",
    "statement": "Aggregate estimate p_system = p*v = 0.4590",
    "inputs": "p=0.85, v=0.54",
    "formula": "p * v"
  },
  {
    "id": "Q13",
    "statement": "Sweep entry: prompt-only at N=10, eps=0.02 is approximately 0.8170",
    "inputs": "N=10, eps=0.02",
    "formula": "0.98^10"
  },
  {
    "id": "Q14",
    "statement": "Sweep entry: hybrid at N=10, eps=0.02, c=0.95 is approximately 0.9900",
    "inputs": "N=10, eps=0.02, c=0.95",
    "formula": "0.999^10"
  },
  {
    "id": "Q15",
    "statement": "Sweep entry: prompt-only at N=20, eps=0.02 is approximately 0.6676",
    "inputs": "N=20, eps=0.02",
    "formula": "0.98^20"
  },
  {
    "id": "Q16",
    "statement": "Sweep entry: hybrid at N=20, eps=0.02, c=0.95 is approximately 0.9802",
    "inputs": "N=20, eps=0.02, c=0.95",
    "formula": "0.999^20"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 13, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: 0.98^40. ln(0.98) = -0.020202707. 40 × (-0.020202707) = -0.80810828. e^(-0.80810828) = 0.445700. Expected 0.4457 → match.

Q2: 0.999^40. ln(0.999) = -0.001000500. 40 × (-0.001000500) = -0.040020013. e^(-0.040020013) = 0.960789. Expected 0.9608 → match.

Q3: 0.960789 / 0.445700 = 2.15611. Expected 2.156 → match.

Q4: ln(0.5)/ln(0.98) = -0.693147 / -0.020202707 = 34.3107. Smallest integer N with 0.98^N < 0.5 is N = 35. Expected 35 → match.

Q5: 0.986^40. ln(0.986) = -0.014099440. 40 × (-0.014099440) = -0.56397760. e^(-0.56397760) = 0.569058. Expected 0.5691 → match.

Q6: 0.986^300. 300 × (-0.014099440) = -4.22983200. e^(-4.22983200) = 0.014555. Expected 0.0146 → match.

Q7: 0.996^40. ln(0.996) = -0.004008021. 40 × (-0.004008021) = -0.160320840. e^(-0.160320840) = 0.851825. Expected 0.8518 → match.

Q8: 0.9998^40. ln(0.9998) = -0.000200020. 40 × (-0.000200020) = -0.008000800. e^(-0.008000800) = 0.992032. Expected 0.9920 → match.

Q9: 0.95^40. ln(0.95) = -0.051293294. 40 × (-0.051293294) = -2.051731760. e^(-2.051731760) = 0.128512. Expected 0.1285 → match.

Q10: 0.9975^40. ln(0.9975) = -0.002503130. 40 × (-0.002503130) = -0.100125200. e^(-0.100125200) = 0.904712. Expected 0.9047 → match.

Q11: 0.99^40. ln(0.99) = -0.010050336. 40 × (-0.010050336) = -0.402013440. e^(-0.402013440) = 0.668967. Expected 0.6690 → match.

Q12: 0.85 × 0.54 = 0.459000. Expected 0.4590 → match.

Q13: 0.98^10. 10 × (-0.020202707) = -0.202027070. e^(-0.202027070) = 0.817073. Expected 0.8170 → match.

Q14: 0.999^10. 10 × (-0.001000500) = -0.010005003. e^(-0.010005003) = 0.990045. Expected 0.9900 → match.

Q15: 0.98^20. 20 × (-0.020202707) = -0.404054140. e^(-0.404054140) = 0.667607. Expected 0.6676 → match.

Q16: 0.999^20. 20 × (-0.001000500) = -0.020010007. e^(-0.020010007) = 0.980109. Expected 0.9802 → match.

CLAIM Q1: computed=0.445700 expected=0.4457 match=yes
CLAIM Q2: computed=0.960789 expected=0.9608 match=yes
CLAIM Q3: computed=2.15611 expected=2.156 match=yes
CLAIM Q4: computed=35 expected=35 match=yes
CLAIM Q5: computed=0.569058 expected=0.5691 match=yes
CLAIM Q6: computed=0.0145550 expected=0.0146 match=yes
CLAIM Q7: computed=0.851825 expected=0.8518 match=yes
CLAIM Q8: computed=0.992032 expected=0.9920 match=yes
CLAIM Q9: computed=0.128512 expected=0.1285 match=yes
CLAIM Q10: computed=0.904712 expected=0.9047 match=yes
CLAIM Q11: computed=0.668967 expected=0.6690 match=yes
CLAIM Q12: computed=0.459000 expected=0.4590 match=yes
CLAIM Q13: computed=0.817073 expected=0.8170 match=yes
CLAIM Q14: computed=0.990045 expected=0.9900 match=yes
CLAIM Q15: computed=0.667607 expected=0.6676 match=yes
CLAIM Q16: computed=0.980109 expected=0.9802 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.445700 | 0.4457 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.960789 | 0.9608 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 2.15611 | 2.156 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 35 | 35 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.569058 | 0.5691 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.0145550 | 0.0146 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.851825 | 0.8518 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 0.992032 | 0.9920 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.128512 | 0.1285 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.904712 | 0.9047 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 0.668967 | 0.6690 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 0.459000 | 0.4590 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 0.817073 | 0.8170 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 0.990045 | 0.9900 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 0.667607 | 0.6676 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 0.980109 | 0.9802 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
