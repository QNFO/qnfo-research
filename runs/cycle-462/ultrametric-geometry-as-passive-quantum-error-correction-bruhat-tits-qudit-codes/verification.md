# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Code size n_t = 1 + (p+1)(p^t - 1)/(p-1); for p=3, t=1 gives n_1=5",
    "inputs": "p=3, t=1",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q2",
    "statement": "Code size for p=3, t=2 gives n_2=17",
    "inputs": "p=3, t=2",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q3",
    "statement": "Code size for p=3, t=3 gives n_3=53",
    "inputs": "p=3, t=3",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q4",
    "statement": "Code size for p=2, t=1 gives n_1=4",
    "inputs": "p=2, t=1",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q5",
    "statement": "Code size for p=2, t=2 gives n_2=10",
    "inputs": "p=2, t=2",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q6",
    "statement": "Code size for p=2, t=3 gives n_3=22",
    "inputs": "p=2, t=3",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q7",
    "statement": "Passive logical failure probability P_pass = 9.980015e-6 for p=3, t=1, eps=1e-3",
    "inputs": "n=5, eps=0.001",
    "formula": "P_pass = 1 - (1-eps)^5 - 5*eps*(1-eps)^4"
  },
  {
    "id": "Q8",
    "statement": "Suppression factor eps/P_pass ≈ 100.2",
    "inputs": "eps=0.001, P_pass=9.980015e-6",
    "formula": "S = eps / P_pass"
  },
  {
    "id": "Q9",
    "statement": "Passive logical failure probability P_pass^(2) ≈ 6.73e-7 for p=3, t=2",
    "inputs": "n=17, eps=0.001",
    "formula": "P_pass2 ≈ C(17,3)*eps^3*(1-eps)^14 + C(17,4)*eps^4*(1-eps)^13"
  },
  {
    "id": "Q10",
    "statement": "Effective per-qudit error eps_eff = 1.999e-3 under (A3)",
    "inputs": "eps=0.001",
    "formula": "eps_eff = 1 - (1-eps)^2"
  },
  {
    "id": "Q11",
    "statement": "Active logical failure probability P_act ≈ 3.98e-5",
    "inputs": "n=5, eps_eff=0.001999",
    "formula": "P_act = 1 - (1-eps_eff)^5 - 5*eps_eff*(1-eps_eff)^4"
  },
  {
    "id": "Q12",
    "statement": "Passive advantage factor P_act/P_pass ≈ 3.99",
    "inputs": "P_act=3.9780533e-5, P_pass=9.980015e-6",
    "formula": "ratio = P_act / P_pass"
  },
  {
    "id": "Q13",
    "statement": "Pseudo-threshold eps_th ≈ 0.3245 under dominant-term approximation",
    "inputs": "f(eps)=10*eps*(1-eps)^3, f(0.32)=1.0061824, f(0.33)=0.9925179",
    "formula": "eps_th = 0.32 + 0.01*(f(0.32)-1)/(f(0.32)-f(0.33))"
  }
]

## Script
```python
import sympy as sp
import random
from sympy import binomial, simplify, Eq
from sympy.physics import units as u

# ---------- symbols with assumptions ----------
p   = sp.Symbol('p', integer=True, positive=True)          # prime ≥2
t   = sp.Symbol('t', integer=True, nonnegative=True)       # radius
ε   = sp.Symbol('ε', real=True, nonnegative=True)           # physical error rate
# dimensionless units (for sanity checks)
dimless = u.dimensionless

# ---------- helper for numeric spot‑check ----------
def spot_check(lhs, rhs, n_trials=5, tol=1e-12):
    for _ in range(n_trials):
        # random admissible values
        pv = random.choice([2,3,5,7])
        tv = random.randint(0,3)
        ev = random.random()*0.01   # ε in (0,0.01)
        subs = {p: pv, t: tv, ε: ev}
        lval = float(lhs.subs(subs).evalf())
        rval = float(rhs.subs(subs).evalf())
        if abs(lval - rval) > tol:
            return False
    return True

# ---------- transitions ----------
transitions = []

# T1: code size formula
lhs = sp.Symbol('n_t')
rhs = 1 + (p+1)*(p**t - 1)/(p-1)
transitions.append(("T1", lhs, rhs))

# T2: numeric n_1 = 5
lhs = sp.Symbol('n_1')
rhs = sp.Integer(5)
transitions.append(("T2", lhs, rhs))

# T3: distance
lhs = sp.Symbol('d')
rhs = 2*t + 1
transitions.append(("T3", lhs, rhs))

# T4: passive failure probability (exact)
k = sp.Symbol('k', integer=True, nonnegative=True)
P_pass = 1 - sp.summation(binomial(lhs, k)*ε**k*(1-ε)**(lhs-k), (k,0,t))
# we will treat lhs as n_t later
transitions.append(("T4", sp.Symbol('P_pass'), P_pass.subs(lhs, sp.Symbol('n_t'))))

# T5: numeric P_pass for p=3,t=1,ε=1e-3
P_pass_expr = 1 - sp.summation(binomial(5, k)*ε**k*(1-ε)**(5-k), (k,0,1))
lhs = sp.Symbol('P_pass_flagship')
rhs = sp.nsimplify(9.980015e-6)
transitions.append(("T5", lhs, rhs))

# T6: suppression factor S = ε / P_pass
lhs = sp.Symbol('S')
rhs = ε / sp.Symbol('P_pass')
transitions.append(("T6", lhs, rhs))

# T7: numeric S ≈ 100.2
lhs = sp.Symbol('S_flagship')
rhs = sp.nsimplify(100.2)
transitions.append(("T7", lhs, rhs))

# T8: n_2 = 17
lhs = sp.Symbol('n_2')
rhs = sp.Integer(17)
transitions.append(("T8", lhs, rhs))

# T9: P_pass^{(2)} numeric
P_pass2 = 1 - sp.summation(binomial(17, k)*ε**k*(1-ε)**(17-k), (k,0,2))
lhs = sp.Symbol('P_pass_2')
rhs = sp.nsimplify(6.73e-7)
transitions.append(("T9", lhs, rhs))

# T10: active baseline
lhs = sp.Symbol('P_act')
rhs = sp.nsimplify(3.98e-5)
transitions.append(("T10", lhs, rhs))

# T11: advantage factor A = P_act / P_pass
lhs = sp.Symbol('A')
rhs = sp.Symbol('P_act')/sp.Symbol('P_pass')
transitions.append(("T11", lhs, rhs))

# T12: numeric advantage ≈ 3.99
lhs = sp.Symbol('A_flagship')
rhs = sp.nsimplify(3.99)
transitions.append(("T12", lhs, rhs))

# T13: dominant‑term approximation
lhs = sp.Symbol('P_pass_approx')
rhs = binomial(sp.Symbol('n_t'), t+1)*ε**(t+1)
transitions.append(("T13", lhs, rhs))

# T14: pseudo‑threshold ε_th
lhs = sp.Symbol('ε_th')
rhs = (1/binomial(sp.Symbol('n_t'), t+1))**(1/t)
transitions.append(("T14", lhs, rhs))

# T15: large‑p limit of n_t
lhs = sp.Symbol('n_t_limit')
rhs = p**t   # simplified dominant term
transitions.append(("T15", lhs, rhs))

# ---------- verification loop ----------
for tag, lhs, rhs in transitions:
    # attempt symbolic simplification of lhs - rhs
    diff = simplify(lhs - rhs)
    if diff == 0:
        verdict = "ok"
    else:
        # try numeric spot‑checks (replace symbolic n_t etc. with concrete values where needed)
        try:
            # replace n_t with its definition when it appears
            diff_num = diff.subs({sp.Symbol('n_t'): 1 + (p+1)*(p**t - 1)/(p-1),
                                 sp.Symbol('P_pass'): 1 - sp.summation(binomial(1 + (p+1)*(p**t - 1)/(p-1), k)*ε**k*(1-ε)**(1 + (p+1)*(p**t - 1)/(p-1)-k), (k,0,t)),
                                 sp.Symbol('P_act'): sp.nsimplify(3.98e-5)})
            if spot_check(diff_num, 0):
                verdict = "ok"
            else:
                verdict = "refuted"
        except Exception:
            verdict = "inconclusive"
    print(f"DERIV {verdict}: ({lhs}) => ({rhs})   [{tag}]")

import math
from fractions import Fraction

def fmt(x):
    return f"{x:.10g}"

# Q1-Q6: code sizes
def n_t(p, t):
    return 1 + (p + 1) * (p**t - 1) // (p - 1)

claims = []

# Q1
c = n_t(3, 1); claims.append(("Q1", c, "5"))
# Q2
c = n_t(3, 2); claims.append(("Q2", c, "17"))
# Q3
c = n_t(3, 3); claims.append(("Q3", c, "53"))
# Q4
c = n_t(2, 1); claims.append(("Q4", c, "4"))
# Q5
c = n_t(2, 2); claims.append(("Q5", c, "10"))
# Q6
c = n_t(2, 3); claims.append(("Q6", c, "22"))

# Q7: P_pass for n=5, eps=1e-3
eps = Fraction(1, 1000)
q = 1 - eps
P_pass = 1 - q**5 - 5*eps*q**4
claims.append(("Q7", float(P_pass), "9.980015e-6"))

# Q8: suppression factor
S = float(eps) / float(P_pass)
claims.append(("Q8", S, "100.2"))

# Q9: P_pass^(2) for n=17, t=2 (failure needs >=3 errors)
epsf = 0.001
P2 = math.comb(17,3)*epsf**3*(1-epsf)**14 + math.comb(17,4)*epsf**4*(1-epsf)**13
claims.append(("Q9", P2, "6.73e-7"))

# Q10: eps_eff
eps_eff = 1 - (1-epsf)**2
claims.append(("Q10", eps_eff, "1.999e-3"))

# Q11: P_act
ee = eps_eff
P_act = 1 - (1-ee)**5 - 5*ee*(1-ee)**4
claims.append(("Q11", P_act, "3.98e-5"))

# Q12: ratio
ratio = P_act / float(P_pass)
claims.append(("Q12", ratio, "3.99"))

# Q13: pseudo-threshold via linear interpolation
f = lambda e: 10*e*(1-e)**3
f32 = f(0.32); f33 = f(0.33)
eps_th = 0.32 + 0.01*(f32 - 1)/(f32 - f33)
claims.append(("Q13", eps_th, "0.3245"))

mism = 0
for cid, computed, expected in claims:
    # round computed to sig digits of expected
    exp_digits = len(expected.replace("e-","").replace(".","").lstrip("0")) if "e" in expected else None
    # determine significant digits from expected string
    import re
    m = re.match(r"^-?(\d+\.?\d*)e?(-?\d+)?$", expected)
    digits_str = m.group(1).replace(".", "")
    sig = len(digits_str.lstrip("0"))
    comp_rounded = float(f"{computed:.{sig}g}")
    exp_val = float(expected)
    match = "yes" if abs(comp_rounded - exp_val) <= 0.5 * 10**(-(sig-1)) * 10**math.floor(math.log10(abs(exp_val))+1) or comp_rounded == exp_val else "no"
    if match == "no":
        # fallback: compare rounded strings
        match = "yes" if f"{computed:.{sig}g}" == f"{exp_val:.{sig}g}" else "no"
    if match == "no":
        mism += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims)-mism} match, {mism} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
**Q1.** $n_1 = 1 + 4\cdot(3^1-1)/(3-1) = 1 + 4\cdot2/2 = 1+4 = 5$.
CLAIM Q1: computed=5 expected=5 match=yes

**Q2.** $n_2 = 1 + 4\cdot(9-1)/2 = 1+16 = 17$.
CLAIM Q2: computed=17 expected=17 match=yes

**Q3.** $n_3 = 1 + 4\cdot(27-1)/2 = 1+52 = 53$.
CLAIM Q3: computed=53 expected=53 match=yes

**Q4.** $n_1 = 1 + 3\cdot(2-1)/1 = 1+3 = 4$.
CLAIM Q4: computed=4 expected=4 match=yes

**Q5.** $n_2 = 1 + 3\cdot(4-1) = 1+9 = 10$.
CLAIM Q5: computed=10 expected=10 match=yes

**Q6.** $n_3 = 1 + 3\cdot(8-1) = 1+21 = 22$.
CLAIM Q6: computed=22 expected=22 match=yes

**Q7.** $(1-\varepsilon)^2 = 0.999^2 = 0.998001$; $(1-\varepsilon)^4 = 0.998001^2 = 0.996005996001$; $(1-\varepsilon)^5 = 0.996005996001\times0.999 = 0.995009990004999$; $5\times0.001\times0.996005996001 = 0.004980029980005$; $P_{\mathrm{pass}} = 1 - 0.995009990004999 - 0.004980029980005 = 0.000009980014996 = 9.980014996\times10^{-6}$, which rounds to $9.980015\times10^{-6}$.
CLAIM Q7: computed=9.980014996e-6 expected=9.980015e-6 match=yes

**Q8.** $S = 10^{-3}/9.980014996\times10^{-6} = 1000/9.980014996 = 100.200347\ldots$, rounds to $100.2$.
CLAIM Q8: computed=100.200347 expected=100.2 match=yes

**Q9.** $\binom{17}{3}=680$; $\varepsilon^3=10^{-9}$; $(1-\varepsilon)^{14}$: $0.999^8 = 0.996005996001^2 = 0.992027944070$; $0.999^{14} = 0.992027944070\times0.996005996001\times0.998001$. First product: $0.992027944070\times0.996005996001 = 0.988065684\ldots$; times $0.998001$: $0.986090532\ldots$. Leading term: $680\times10^{-9}\times0.986090532 = 6.7054156\times10^{-7}$. Next term: $\binom{17}{4}=2380$; $(1-\varepsilon)^{13} = 0.986090532/0.999 = 0.987077609\ldots$; $2380\times10^{-12}\times0.987077609 = 2.3492447\times10^{-9}$. Sum: $6.7054156\times10^{-7} + 0.0234924\times10^{-7} = 6.7289080\times10^{-7}$, rounds to $6.73\times10^{-7}$.
CLAIM Q9: computed=6.72890801e-7 expected=6.73e-7 match=yes

**Q10.** $\varepsilon_{\mathrm{eff}} = 1 - 0.998001 = 0.001999 = 1.999\times10^{-3}$.
CLAIM Q10: computed=0.001999 expected=0.001999 match=yes

**Q11.** $(1-\varepsilon_{\mathrm{eff}})^2 = 0.998001^2 = 0.996005996001$; $(1-\varepsilon_{\mathrm{eff}})^4 = 0.996005996001^2 = 0.992027944070$; $(1-\varepsilon_{\mathrm{eff}})^5 = 0.992027944070\times0.998001$. Exact check via binomial expansion of $(1-0.001999)^5 = 1 - 5(0.001999) + 10(0.001999)^2 - 10(0.001999)^3 + \ldots = 1 - 0.009995 + 0.00003996001 - 0.00000007988006 + \ldots = 0.990044880210$ (the paper's intermediate $0.990044900166$ carries a small slip of $\approx2\times10^{-8}$). Single-error term: $5\times0.001999\times0.992027944070 = 0.009915319301$. $P_{\mathrm{act}} = 1 - 0.990044880210 - 0.009915319301 = 0.000039800489 = 3.9800489\times10^{-5}$, which rounds to $3.98\times10^{-5}$ as stated.
CLAIM Q11: computed=3.98004892e-5 expected=3.98e-5 match=yes

**Q12.** Using the paper's stated inputs: $3.9780533\times10^{-5}/9.980015\times10^{-6} = 3.9780533/0.9980015 = 3.986024\ldots$, rounds to $3.99$. (Using the recomputed exact $P_{\mathrm{act}} = 3.9800489\times10^{-5}$ gives $3.988021\ldots$, which also rounds to $3.99$; the headline factor is unaffected.)
CLAIM Q12: computed=3.98602438 expected=3.99 match=yes

**Q13.** $f(0.32) = 10\times0.32\times0.68^3 = 3.2\times0.314432 = 1.0061824$; $f(0.33) = 10\times0.33\times0.67^3 = 3.3\times0.300763 = 0.9925179$. Interpolation: $\varepsilon_{\mathrm{th}} = 0.32 + 0.01\times(1.0061824-1)/(1.0061824-0.9925179) = 0.32 + 0.01\times0.0061824/0.0136645 = 0.32 + 0.01\times0.452437 = 0.32452437$, rounds to $0.3245$.
CLAIM Q13: computed=0.32452437 expected=0.3245 match=yes

VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 53 | 53 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 22 | 22 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 9.980014996e-6 | 9.980015e-6 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 100.200347 | 100.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 6.72890801e-7 | 6.73e-7 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0.001999 | 0.001999 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 3.98004892e-5 | 3.98e-5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 3.98602438 | 3.99 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.32452437 | 0.3245 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
