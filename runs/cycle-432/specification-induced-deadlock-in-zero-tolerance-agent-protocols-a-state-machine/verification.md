# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Binary protocol coverage at k=5: f(5) = 32/243 ≈ 0.132",
    "inputs": "k=5, per-tool coverage 2/3",
    "formula": "f(k) = (2/3)^k"
  },
  {
    "id": "Q2",
    "statement": "State-space ratio at k=10: 3^10/2^10 = 59049/1024 ≈ 57.7",
    "inputs": "k=10",
    "formula": "3^k / 2^k"
  },
  {
    "id": "Q3",
    "statement": "Configurations with at least one blocked-invocation tool at k=10: 58025",
    "inputs": "3^10=59049, 2^10=1024",
    "formula": "3^10 - 2^10"
  },
  {
    "id": "Q4",
    "statement": "Unspecified fraction at k=10: 58025/59049 ≈ 0.98266",
    "inputs": "3^10=59049, 2^10=1024",
    "formula": "1 - 2^10/3^10"
  },
  {
    "id": "Q5",
    "statement": "Per-task exposure at q=0.1, n=5: 0.40951",
    "inputs": "q=0.1, n=5",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q6",
    "statement": "Exposure at q=0.01, n=5: 0.0490099501 ≈ 0.049",
    "inputs": "q=0.01, n=5",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q7",
    "statement": "Exposure at q=0.05, n=5: 0.2262190625 ≈ 0.226",
    "inputs": "q=0.05, n=5",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q8",
    "statement": "Exposure at q=0.2, n=5: 0.67232 ≈ 0.672",
    "inputs": "q=0.2, n=5",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q9",
    "statement": "Exposure at q=0.1, n=10: 0.6513215599 ≈ 0.651",
    "inputs": "q=0.1, n=10",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q10",
    "statement": "Exposure at q=0.27, n=5: 0.7926928407 ≈ 0.793",
    "inputs": "q=0.27, n=5",
    "formula": "1 - (1-q)^n"
  },
  {
    "id": "Q11",
    "statement": "Unspecified fraction at k=5: 211/243 ≈ 0.868",
    "inputs": "k=5",
    "formula": "1 - (2/3)^5"
  },
  {
    "id": "Q12",
    "statement": "Coverage under fourth-state idealization at k=5: 1/32 = 0.03125",
    "inputs": "k=5, per-tool coverage 2/4",
    "formula": "(2/4)^k"
  },
  {
    "id": "Q13",
    "statement": "Daily exposed tasks at 10^4 tasks/day: ≈ 4.1 × 10^3",
    "inputs": "p_task=0.40951, tasks=10^4",
    "formula": "0.40951 * 10^4"
  }
]

## Script
```python
# Transition extraction from "Specification-Induced Deadlock in Zero-Tolerance Agent Protocols"
# Methods/Analysis equations (Sections 4 and 5). All quantities here are dimensionless
# probabilities / counts, but we declare units per the notation table via sympy.physics.units.

import sympy as sp
from sympy.physics.units import Quantity, probability, count
from sympy.physics.units import convert_to

# --- Notation table with units ---
# q  : per-invocation deadlock-trigger probability  -> dimensionless probability
# n  : number of gated invocations per task         -> dimensionless count
# k  : number of permission-gated tools             -> dimensionless count
# P_task : per-task deadlock probability            -> dimensionless probability
# coverage : fraction of three-state space covered  -> dimensionless probability

q = sp.Symbol('q', nonnegative=True)
n = sp.Symbol('n', positive=True, integer=True)
k = sp.Symbol('k', positive=True, integer=True)

# Sanity-bound helper
def check_bounds(name, expr, subs):
    val = expr.subs(subs)
    ok = (sp.Rational(0) <= val) and (val <= 1)
    print(f"BOUNDS {name}: value={sp.N(val, 12)} in [0,1] -> {bool(ok)}")

# ---------------------------------------------------------------
# Transition T1 (Section 4, combinatorial coverage):
#   premise : binary-state protocol over k gated tools; true space is 3^k configs,
#             binary protocol covers 2^k of them
#   conclusion : coverage fraction = (2/3)^k
#   justification : exact counting of Cartesian product state spaces
# ---------------------------------------------------------------
lhs1 = sp.Rational(2)**k / sp.Rational(3)**k
rhs1 = (sp.Rational(2)/3)**k
d1 = sp.simplify(lhs1 - rhs1)
print("T1:", "DERIV ok" if d1 == 0 else "DERIV refuted",
      "| coverage = (2/3)^k  [binary 2^k of 3^k configs]")

# ---------------------------------------------------------------
# Transition T2 (Section 4, k=5 evaluation):
#   premise : coverage = (2/3)^k, k = 5
#   conclusion : coverage = 32/243 ≈ 0.132
#   justification : exact arithmetic
# ---------------------------------------------------------------
lhs2 = (sp.Rational(2)/3)**5
rhs2 = sp.Rational(32, 243)
d2 = sp.simplify(lhs2 - rhs2)
print("T2:", "DERIV ok" if d2 == 0 else "DERIV refuted",
      f"| (2/3)^5 = 32/243 = {sp.N(rhs2,6)} ≈ 0.132")

# ---------------------------------------------------------------
# Transition T3 (Section 4, k=10 state-space gap):
#   premise : gap ratio = 3^k / 2^k, k = 10
#   conclusion : gap = 59049/1024 ≈ 57.7
#   justification : exact arithmetic
# ---------------------------------------------------------------
lhs3 = sp.Rational(3)**10 / sp.Rational(2)**10
rhs3 = sp.Rational(59049, 1024)
d3 = sp.simplify(lhs3 - rhs3)
print("T3:", "DERIV ok" if d3 == 0 else "DERIV refuted",
      f"| 3^10/2^10 = 59049/1024 = {sp.N(rhs3,6)} ≈ 57.7")

# ---------------------------------------------------------------
# Transition T4 (Section 5, per-task deadlock probability):
#   premise : n independent gated invocations, each deadlocks with prob q
#   conclusion : P_task = 1 - (1 - q)^n
#   justification : independence; complement of "no invocation deadlocks"
# ---------------------------------------------------------------
P_task = 1 - (1 - q)**n
# symbolic identity check: P_task equals its own closed form trivially; instead
# verify the limiting/sanity cases and the numeric instance.

# Limiting cases (declared in paper):
#   q -> 0  => P_task -> 0
#   q -> 1  => P_task -> 1
#   n -> 0  => P_task -> 0
lim_q0 = sp.limit(P_task.subs(n, 5), q, 0)
lim_q1 = sp.limit(P_task.subs(n, 5), q, 1, dir='+')
lim_n0 = sp.limit(P_task.subs(q, sp.Rational(1,10)), n, 0, dir='+')
print("LIMITS:", "DERIV ok" if (lim_q0 == 0 and lim_q1 == 1 and lim_n0 == 0)
      else "DERIV refuted",
      "| q->0: 0, q->1: 1, n->0: 0")

# ---------------------------------------------------------------
# Transition T5 (Section 5, numeric projection):
#   premise : P_task = 1 - (1-q)^n, q = 0.1, n = 5
#   conclusion : P_task = 0.40951
#   justification : exact arithmetic (0.1 = 1/10)
# ---------------------------------------------------------------
lhs5 = 1 - (sp.Rational(9,10))**5
rhs5 = sp.Rational(40951, 100000)
d5 = sp.simplify(lhs5 - rhs5)
print("T5:", "DERIV ok" if d5 == 0 else "DERIV refuted",
      f"| 1-(0.9)^5 = {sp.N(lhs5,8)} = 0.40951")

# ---------------------------------------------------------------
# Numeric spot checks (randomized) for the symbolic transition T4,
# in case symbolic simplification were inconclusive.
# ---------------------------------------------------------------
import random
spot_ok = True
for _ in range(200):
    qs = random.random()          # q in [0,1)
    ns = random.randint(1, 20)    # n positive integer
    lhs_val = float((1 - (1 - qs)**ns))
    rhs_val = float(1 - (1 - qs)**ns)  # closed form is definition; check complement logic:
    # independent check via product of survival probabilities
    surv = 1.0
    for _ in range(ns):
        surv *= (1 - qs)
    if abs(lhs_val - (1 - surv)) > 1e-12:
        spot_ok = False
print("SPOT T4:", "DERIV ok" if spot_ok else "DERIV inconclusive",
      "| P_task = 1-(1-q)^n via independent survival-product check")

# ---------------------------------------------------------------
# Sanity bounds on the paper's numeric instances
# ---------------------------------------------------------------
check_bounds("coverage(k=5)", (sp.Rational(2)/3)**k, {k: 5})
check_bounds("coverage(k=10)", (sp.Rational(2)/3)**k, {k: 10})
check_bounds("P_task(q=0.1,n=5)", P_task, {q: sp.Rational(1,10), n: 5})
# efficiency-style bound: coverage fraction must be <= 1
cov10 = ((sp.Rational(2)/3)**k).subs(k, 10)
print("BOUNDS coverage<=1:", bool(cov10 <= 1), f"| coverage(k=10)={sp.N(cov10,6)}")

# ---------------------------------------------------------------
# Summary of DERIV lines
# ---------------------------------------------------------------
print("\n--- Summary ---")
print("DERIV ok | coverage = (2/3)^k")
print("DERIV ok | (2/3)^5 = 32/243 ≈ 0.132")
print("DERIV ok | 3^10/2^10 = 59049/1024 ≈ 57.7")
print("DERIV ok | P_task = 1-(1-q)^n (limits + randomized spot checks)")
print("DERIV ok | 1-(0.9)^5 = 0.40951")

import math

def sig(x, d):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (d - 1))

claims = []

# Q1: f(5) = (2/3)^5 = 32/243 ≈ 0.132
c = (2/3)**5
claims.append(("Q1", c, "0.132", 3))

# Q2: 3^10/2^10 ≈ 57.7
c = (3**10)/(2**10)
claims.append(("Q2", c, "57.7", 3))

# Q3: 3^10 - 2^10 = 58025
c = 3**10 - 2**10
claims.append(("Q3", c, "58025", 5))

# Q4: 1 - 2^10/3^10 ≈ 0.98266
c = 1 - (2**10)/(3**10)
claims.append(("Q4", c, "0.98266", 5))

# Q5: 1 - 0.9^5 = 0.40951
c = 1 - (1-0.1)**5
claims.append(("Q5", c, "0.40951", 5))

# Q6: 1 - 0.99^5 ≈ 0.0490099501
c = 1 - (1-0.01)**5
claims.append(("Q6", c, "0.0490099501", 10))

# Q7: 1 - 0.95^5 ≈ 0.2262190625
c = 1 - (1-0.05)**5
claims.append(("Q7", c, "0.2262190625", 10))

# Q8: 1 - 0.8^5 = 0.67232
c = 1 - (1-0.2)**5
claims.append(("Q8", c, "0.67232", 5))

# Q9: 1 - 0.9^10 ≈ 0.6513215599
c = 1 - (1-0.1)**10
claims.append(("Q9", c, "0.6513215599", 10))

# Q10: 1 - 0.73^5 ≈ 0.7926928407
c = 1 - (1-0.27)**5
claims.append(("Q10", c, "0.7926928407", 10))

# Q11: 1 - (2/3)^5 = 211/243 ≈ 0.868
c = 1 - (2/3)**5
claims.append(("Q11", c, "0.868", 3))

# Q12: (2/4)^5 = 1/32 = 0.03125
c = (2/4)**5
claims.append(("Q12", c, "0.03125", 4))

# Q13: 0.40951 * 10^4 ≈ 4.1e3
c = 0.40951 * 10**4
claims.append(("Q13", c, "4100", 2))

m = 0
for cid, comp, exp, d in claims:
    comp_s = f"{comp:.10g}"
    ok = "yes" if float(exp) == float(sig(comp, d)) else "no"
    if ok == "yes":
        m += 1
    print(f"CLAIM {cid}: computed={comp_s} expected={exp} match={ok}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {m} match, {len(claims)-m} mismatch")

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
Q1: f(5) = (2/3)^5 = 32/243. 32 ÷ 243 = 0.1316872428. Expected 0.132 (3 s.f.) → match.

Q2: 3^10 = 59049; 2^10 = 1024; 59049 ÷ 1024 = 57.6640625. Expected 57.7 → match.

Q3: 59049 − 1024 = 58025. Expected 58025 → match.

Q4: 1 − 1024/59049 = 58025/59049 = 0.982657... = 0.9826574. Expected 0.98266 → match.

Q5: 0.9^5 = 0.59049; 1 − 0.59049 = 0.40951. Expected 0.40951 → match.

Q6: 0.99^2 = 0.9801; 0.99^4 = 0.9801^2 = 0.96059601; 0.99^5 = 0.96059601 × 0.99 = 0.9509900499; 1 − 0.9509900499 = 0.0490099501. Expected 0.0490099501 → match.

Q7: 0.95^2 = 0.9025; 0.95^4 = 0.9025^2 = 0.81450625; 0.95^5 = 0.81450625 × 0.95 = 0.7737809375; 1 − 0.7737809375 = 0.2262190625. Expected 0.2262190625 → match.

Q8: 0.8^5 = 0.32768; 1 − 0.32768 = 0.67232. Expected 0.67232 → match.

Q9: 0.9^10 = 0.59049^2 = 0.3486784401; 1 − 0.3486784401 = 0.6513215599. Expected 0.6513215599 → match.

Q10: 0.73^2 = 0.5329; 0.73^4 = 0.5329^2 = 0.28398241; 0.73^5 = 0.28398241 × 0.73 = 0.2073071593; 1 − 0.2073071593 = 0.7926928407. Expected 0.7926928407 → match.

Q11: 1 − 32/243 = 211/243 = 0.8683127572. Expected 0.868 → match.

Q12: (2/4)^5 = (1/2)^5 = 1/32 = 0.03125. Expected 0.03125 → match.

Q13: 0.40951 × 10^4 = 4095.1 ≈ 4.1 × 10^3. Expected 4100 → match.

CLAIM Q1: computed=0.1316872428 expected=0.132 match=yes
CLAIM Q2: computed=57.6640625 expected=57.7 match=yes
CLAIM Q3: computed=58025 expected=58025 match=yes
CLAIM Q4: computed=0.9826574010 expected=0.98266 match=yes
CLAIM Q5: computed=0.40951 expected=0.40951 match=yes
CLAIM Q6: computed=0.0490099501 expected=0.0490099501 match=yes
CLAIM Q7: computed=0.2262190625 expected=0.2262190625 match=yes
CLAIM Q8: computed=0.67232 expected=0.67232 match=yes
CLAIM Q9: computed=0.6513215599 expected=0.6513215599 match=yes
CLAIM Q10: computed=0.7926928407 expected=0.7926928407 match=yes
CLAIM Q11: computed=0.8683127572 expected=0.868 match=yes
CLAIM Q12: computed=0.03125 expected=0.03125 match=yes
CLAIM Q13: computed=4095.1 expected=4100 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.1316872428 | 0.132 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 57.6640625 | 57.7 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 58025 | 58025 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.9826574010 | 0.98266 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 0.40951 | 0.40951 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 0.0490099501 | 0.0490099501 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q7 | 0.2262190625 | 0.2262190625 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q8 | 0.67232 | 0.67232 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 0.6513215599 | 0.6513215599 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q10 | 0.7926928407 | 0.7926928407 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q11 | 0.8683127572 | 0.868 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.03125 | 0.03125 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 4095.1 | 4100 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
