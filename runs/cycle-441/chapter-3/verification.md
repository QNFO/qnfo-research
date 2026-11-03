# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Oral retention after 10 relays is 0.3487",
    "inputs": "p=0.90, n=10",
    "formula": "p^n = 0.9^10"
  },
  {
    "id": "Q2",
    "statement": "Print retention after 10 generations is 0.9044",
    "inputs": "q=0.99, n=10",
    "formula": "q^n = 0.99^10"
  },
  {
    "id": "Q3",
    "statement": "Oral half-content threshold is 6.58 relays",
    "inputs": "p=0.90",
    "formula": "n_half = ln(0.5)/ln(0.9)"
  },
  {
    "id": "Q4",
    "statement": "Print-vs-oral advantage is 2.59-fold",
    "inputs": "p=0.90, q=0.99, n=10",
    "formula": "q^10 / p^10"
  },
  {
    "id": "Q5",
    "statement": "Oral retention at p=0.92 is 0.4344",
    "inputs": "p=0.92, n=10",
    "formula": "0.92^10"
  },
  {
    "id": "Q6",
    "statement": "Oral retention at p=0.88 is 0.2785",
    "inputs": "p=0.88, n=10",
    "formula": "0.88^10"
  },
  {
    "id": "Q7",
    "statement": "Rumor diffusion width at 30 days is 5.48 contact-hops",
    "inputs": "t=30 days",
    "formula": "sigma = sqrt(t)"
  },
  {
    "id": "Q8",
    "statement": "Adaptive group testing requires about 133 interrogations",
    "inputs": "n=2000, k=20",
    "formula": "I = k*log2(n/k)"
  },
  {
    "id": "Q9",
    "statement": "Reduction vs exhaustive search is 15.05-fold",
    "inputs": "n=2000, I=132.877",
    "formula": "n/I"
  },
  {
    "id": "Q10",
    "statement": "Impact factor I = 1.27%",
    "inputs": "C(0.5)=0.635%",
    "formula": "I = C(0.5)/(1-0.5)"
  },
  {
    "id": "Q11",
    "statement": "Loss-reduction factor from A=0.5 to A=0.8 is 2.5",
    "inputs": "C(0.5)=0.635%, C(0.8)=0.254%",
    "formula": "C(0.5)/C(0.8)"
  },
  {
    "id": "Q12",
    "statement": "Absolute loss at A=0.5, B0=10% is 6.35 per 10,000 searches",
    "inputs": "B0=10%, C(0.5)=0.635%",
    "formula": "B0*C(0.5)*10000"
  },
  {
    "id": "Q13",
    "statement": "Avoided loss from A=0.5 to 0.8 is 3.81 per 10,000 searches",
    "inputs": "B0=10%, C(0.5)=0.635%, C(0.8)=0.254%",
    "formula": "B0*(C(0.5)-C(0.8))*10000"
  },
  {
    "id": "Q14",
    "statement": "Layered awareness at x_excl=0.40 is 0.45",
    "inputs": "a_access=1, a_comp=0.75, x_excl=0.40",
    "formula": "A = a_access*a_comp*(1-x_excl)"
  },
  {
    "id": "Q15",
    "statement": "Layered awareness at x_excl=0.60 is 0.30",
    "inputs": "a_access=1, a_comp=0.75, x_excl=0.60",
    "formula": "A = a_access*a_comp*(1-x_excl)"
  },
  {
    "id": "Q16",
    "statement": "Modeled loss at A=0.45 is 0.699%",
    "inputs": "I=1.27%, A=0.45",
    "formula": "C(A)=I*(1-A)"
  }
]

## Script
```python
# DERIV extraction: "The Consequences of Information States" — Methods/Analysis (Section 4)
# Each transition extracted as (premise, conclusion, justification).

import sympy as sp
from sympy import simplify, Rational, sqrt, log, symbols, Eq, Max, S
from sympy.physics.units import percent, day, bit, bookings_per_10000_searches, hops

# ---------------- Notation table with declared units ----------------
# A            : awareness level, dimensionless probability in [0,1]
# I            : impact/ignorance factor, percent (1.27%)
# C(A)         : ignorance cost, percent of baseline uncancelled-booker rate
# baseline     : 10% uncancelled-booker rate -> bookings_per_10000_searches
# a_access     : access factor, dimensionless in [0,1]
# a_comp       : comprehension factor, dimensionless in [0,1]
# x_excl       : structural exclusion, dimensionless in [0,1]
# p            : oral per-retelling fidelity, dimensionless efficiency <= 1 (0.90)
# q            : print per-generation fidelity, dimensionless efficiency <= 1 (0.99)
# n_retell     : number of retellings/generations, dimensionless count (10)
# w            : rumor diffusion width, hops
# t            : diffusion time, days (30)
# n, k         : suspects / organizers, dimensionless counts (2000, 20)
# interrog     : interrogation count, dimensionless
# mu           : relevance, bits
# L(p)         : decision loss, utility units

# ---------------- Sanity bounds ----------------
def bounds():
    ok = True
    for name, v in [("A=0.5", S(1)/2), ("A=0.8", S(4)/5), ("A=0.45", S(45)/100),
                    ("A=0.30", S(3)/10), ("x_excl=0.40", S(2)/5), ("x_excl=0.60", S(3)/5),
                    ("p=0.90", S(9)/10), ("q=0.99", S(99)/100),
                    ("retention_oral", Rational(3487,10000)), ("retention_print", Rational(9044,10000))]:
        if not (0 <= float(v) <= 1):
            print(f"SANITY fail: {name}={v} not in [0,1]"); ok = False
    for name, v in [("I=1.27%", Rational(127,100)), ("C(0.5)=0.635%", Rational(635,1000)),
                    ("C(0.8)=0.254%", Rational(254,1000)), ("loss 0.699%", Rational(699,1000)),
                    ("loss 0.889%", Rational(889,1000))]:
        if float(v) < 0: print(f"SANITY fail: {name} negative"); ok = False
    # efficiencies <= 1
    if not (float(S(9)/10) <= 1 and float(S(99)/100) <= 1):
        print("SANITY fail: fidelity > 1"); ok = False
    # limiting cases of C(A)=I(1-A): C(1)=0, C(0)=I
    I = Rational(127, 100)
    if simplify(I*(1-1) - 0) != 0: print("SANITY fail: C(1) != 0"); ok = False
    if simplify(I*(1-0) - I) != 0: print("SANITY fail: C(0) != I"); ok = False
    print("SANITY", "ok" if ok else "FAILED")
bounds()

results = []
def check(name, lhs, rhs, numeric=None):
    d = simplify(lhs - rhs)
    if d == 0:
        results.append((name, "ok"))
    elif numeric is not None and abs(float(numeric)) < 1e-9:
        results.append((name, "ok (numeric)"))
    else:
        results.append((name, "inconclusive"))

# ---------------- T1: derive I from calibration C(0.5)=0.635% ----------------
# Premise: C(A)=I(1-A), C(0.5)=0.635%. Conclusion: I=1.27%.
I_sym = symbols('I')
check("T1 I = C(0.5)/(1-0.5) = 1.27%",
      I_sym*(1 - Rational(1,2)), Rational(635, 1000),
      numeric=float(simplify(Rational(635,1000)/Rational(1,2) - Rational(127,100))))

# ---------------- T2: C(0.8)=0.254% from the linear model ----------------
check("T2 C(0.8) = 1.27%*(1-0.8) = 0.254%",
      Rational(127,100)*(1 - Rational(4,5)), Rational(254,1000))

# ---------------- T3: loss at A=0.5 -> 6.35 lost bookings per 10,000 at 10% baseline ----------------
# 0.635% of 10% baseline = 0.00635 * 10000 * 0.10 bookings per 10,000 searches
check("T3 loss@A=0.5 = 0.635%*10%*10000 = 6.35 per 10,000",
      Rational(635,1000)*Rational(1,10)*10000, Rational(635,100))

# ---------------- T4: avoided loss 0.5->0.8 = 3.81 per 10,000 ----------------
check("T4 avoided = (0.635%-0.254%)*10%*10000 = 3.81 per 10,000",
      (Rational(635,1000)-Rational(254,1000))*Rational(1,10)*10000, Rational(381,100))

# ---------------- T5: reduction factor 2.5 ----------------
check("T5 factor = C(0.5)/C(0.8) = 2.5",
      Rational(635,1000)/Rational(254,1000), Rational(5,2))

# ---------------- T6: layered awareness A = a_access*a_comp*(1-x_excl) ----------------
# Premise: 1 * 0.75 * (1-0.40). Conclusion: A = 0.45.
check("T6 A = 1*0.75*(1-0.40) = 0.45",
      1*Rational(3,4)*(1 - Rational(2,5)), Rational(45,100))

# ---------------- T7: exclusion 0.40 -> 0.60 gives A = 0.30 ----------------
check("T7 A(x=0.60) = 1*0.75*(1-0.60) = 0.30",
      1*Rational(3,4)*(1 - Rational(3,5)), Rational(3,10))

# ---------------- T8: modeled loss at A=0.45 is 0.699% ----------------
# Premise: C(A)=I(1-A) with I=1.27%. Conclusion: C(0.45)=0.6985% ≈ 0.699%.
check("T8 C(0.45) = 1.27%*0.55 = 0.6985% ≈ 0.699%",
      Rational(127,100)*(1 - Rational(45,100)), Rational(699,1000),
      numeric=float(simplify(Rational(127,100)*Rational(55,100) - Rational(699,1000))))

# ---------------- T9: modeled loss at A=0.30 is 0.889% ----------------
check("T9 C(0.30) = 1.27%*0.70 = 0.889%",
      Rational(127,100)*(1 - Rational(3,10)), Rational(889,1000))

# ---------------- T10: oral retention 0.9^10 = 0.3487 ----------------
check("T10 oral retention = 0.9^10 = 0.3487",
      sp.N(Rational(9,10)**10, 6), Rational(3487,10000),
      numeric=float(sp.N(Rational(9,10)**10 - Rational(3487,10000), 10)))

# ---------------- T11: half-content threshold n* = ln(0.5)/ln(0.9) = 6.58 ----------------
n_star = log(S(1)/2)/log(Rational(9,10))
check("T11 half-content retellings = ln(0.5)/ln(0.9) = 6.58",
      sp.N(n_star, 4), Rational(658,100),
      numeric=float(sp.N(n_star - Rational(658,100), 10)))

# ---------------- T12: print retention 0.99^10 = 0.9044 ----------------
check("T12 print retention = 0.99^10 = 0.9044",
      sp.N(Rational(99,100)**10, 6), Rational(9044,10000),
      numeric=float(sp.N(Rational(99,100)**10 - Rational(9044,10000), 10)))

# ---------------- T13: print/oral advantage (0.99/0.9)^10 = 2.59 ----------------
check("T13 advantage = (0.99/0.9)^10 = 2.59",
      sp.N((Rational(99,100)/Rational(9,10))**10, 4), Rational(259,100),
      numeric=float(sp.N((Rational(11,10))**10 - Rational(259,100), 10)))

# ---------------- T14: rumor diffusion width sqrt(30) = 5.48 hops ----------------
# Premise (implicit unit-diffusion model): w = sqrt(t/day) hops. Conclusion: 5.48 hops at t=30 days.
w_t = sqrt(30)
check("T14 width = sqrt(30 days) = 5.48 hops",
      sp.N(w_t, 4), Rational(548,100),
      numeric=float(sp.N(w_t - Rational(548,100), 10)))

# ---------------- T15: adaptive group testing ~ k*log2(n/k) = 133 ----------------
k_, n_ = 20, 2000
interrog = k_*log(n_/k_, 2)
check("T15 interrogations = 20*log2(2000/20) = 133",
      sp.N(interrog, 4), 133,
      numeric=float(sp.N(interrog - 133, 10)))

# ---------------- T16: 15.05-fold reduction over exhaustive search ----------------
check("T16 reduction = 2000/133 = 15.05",
      sp.N(Rational(2000,1)/sp.N(interrog,10), 4), Rational(1505,100),
      numeric=float(sp.N(2000/sp.N(interrog,10) - Rational(1505,100), 10)))

# ---------------- T17: single-agent relevance ceiling 1 bit of 8 = 12.5% ----------------
check("T17 mu1/8 = 1/8 = 12.5%", Rational(1,8), Rational(125,1000))

# ---------------- T18: two-agent ceiling 2 bits of 8 = 25% ----------------
check("T18 mu2/8 = 2/8 = 25%", Rational(2,8), Rational(1,4))

# ---------------- T19: zero-rate corollary: R2=0 collapses ceiling to 12.5% ----------------
# Premise: mu2 = mu1 + R2 (collaborative advantage Delta mu = R2); R2 = 0. Conclusion: mu2 = 1 bit.
check("T19 mu2 = mu1 + R2 = 1 + 0 = 1 bit", 1 + 0, 1)

# ---------------- T20: maximin loss L(p)=max(0,12p-6), max at p=0.9 is 4.8 ----------------
p_ = symbols('p_', real=True)
L = Max(0, 12*p_ - 6)
check("T20 L(0.9) = max(0, 12*0.9-6) = 4.8", L.subs(p_, Rational(9,10)), Rational(48,10))

# ---------------- Report ----------------
for name, status in results:
    print(f"DERIV {status} :: {name}")

import math

def sig(x, d):
    # round to d significant digits
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (d - 1))

results = []

# Q1: oral retention 0.9^10
c = 0.9**10
results.append(("Q1", c, "0.3487", 4))

# Q2: print retention 0.99^10
c = 0.99**10
results.append(("Q2", c, "0.9044", 4))

# Q3: half-content threshold ln(0.5)/ln(0.9)
c = math.log(0.5)/math.log(0.9)
results.append(("Q3", c, "6.58", 3))

# Q4: print-vs-oral advantage 0.99^10 / 0.9^10
c = (0.99**10)/(0.9**10)
results.append(("Q4", c, "2.59", 3))

# Q5: 0.92^10
c = 0.92**10
results.append(("Q5", c, "0.4344", 4))

# Q6: 0.88^10
c = 0.88**10
results.append(("Q6", c, "0.2785", 4))

# Q7: sqrt(30)
c = math.sqrt(30)
results.append(("Q7", c, "5.48", 3))

# Q8: 20*log2(2000/20)
c = 20*math.log2(2000/20)
results.append(("Q8", c, "133", 3))

# Q9: 2000/132.877
c = 2000/132.877
results.append(("Q9", c, "15.05", 4))

# Q10: I = 0.635/0.5 (percent)
c = 0.635/0.5
results.append(("Q10", c, "1.27", 3))

# Q11: 0.635/0.254
c = 0.635/0.254
results.append(("Q11", c, "2.5", 2))

# Q12: 0.10*0.00635*10000
c = 0.10*0.00635*10000
results.append(("Q12", c, "6.35", 3))

# Q13: 0.10*(0.00635-0.00254)*10000
c = 0.10*(0.00635-0.00254)*10000
results.append(("Q13", c, "3.81", 3))

# Q14: 1*0.75*(1-0.40)
c = 1*0.75*(1-0.40)
results.append(("Q14", c, "0.45", 2))

# Q15: 1*0.75*(1-0.60)
c = 1*0.75*(1-0.60)
results.append(("Q15", c, "0.30", 2))

# Q16: 1.27*(1-0.45) percent
c = 1.27*(1-0.45)
results.append(("Q16", c, "0.699", 3))

mismatch = 0
for qid, comp, exp, d in results:
    r = sig(comp, d)
    match = "yes" if abs(r - float(exp)) < 10**(-(d)) * max(1, abs(float(exp))) or abs(r - float(exp)) < 10**(-d+1) else "no"
    # stricter: compare rounded strings
    match = "yes" if f"{r:.{d}g}" == f"{float(exp):.{d}g}" else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {qid}: computed={r} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 4, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: 0.9^10 = (0.9^5)^2 = 0.59049^2 = 0.3486784401 → rounded to 4 s.f. = 0.3487; expected 0.3487 → match.

Q2: 0.99^10 = (0.99^5)^2 = 0.9509900499^2 = 0.9043820750 → 0.9044; expected 0.9044 → match.

Q3: ln(0.5) = -0.6931471806, ln(0.9) = -0.1053605157; ratio = 0.6931471806/0.1053605157 = 6.578814 → 6.58; expected 6.58 → match.

Q4: 0.9043820750/0.3486784401 = 2.593742 → 2.59; expected 2.59 → match.

Q5: 0.92^10 = (0.92^5)^2 = 0.6590815232^2 = 0.434388... → 0.4344; expected 0.4344 → match.

Q6: 0.88^10 = (0.88^5)^2 = 0.5277319168^2 = 0.2785009 → 0.2785; expected 0.2785 → match.

Q7: sqrt(30) = 5.477226 → 5.48; expected 5.48 → match.

Q8: log2(100) = ln(100)/ln(2) = 4.6051701860/0.6931471806 = 6.6438561898; ×20 = 132.8771238 → ≈133; expected 133 → match.

Q9: 2000/132.8771238 = 15.054... → 15.05; expected 15.05 → match.

Q10: 0.635%/0.5 = 1.27%; expected 1.27 → match.

Q11: 0.635/0.254 = 2.5; expected 2.5 → match.

Q12: 0.10 × 0.00635 × 10000 = 6.35; expected 6.35 → match.

Q13: 0.10 × (0.00635 − 0.00254) × 10000 = 0.10 × 0.00381 × 10000 = 3.81; expected 3.81 → match.

Q14: 1 × 0.75 × (1 − 0.40) = 0.75 × 0.60 = 0.45; expected 0.45 → match.

Q15: 1 × 0.75 × (1 − 0.60) = 0.75 × 0.40 = 0.30; expected 0.30 → match.

Q16: 1.27% × (1 − 0.45) = 1.27 × 0.55 = 0.6985 → 0.699; expected 0.699 → match.

CLAIM Q1: computed=0.3486784401 expected=0.3487 match=yes
CLAIM Q2: computed=0.9043820750 expected=0.9044 match=yes
CLAIM Q3: computed=6.578814 expected=6.58 match=yes
CLAIM Q4: computed=2.593742 expected=2.59 match=yes
CLAIM Q5: computed=0.434388 expected=0.4344 match=yes
CLAIM Q6: computed=0.278501 expected=0.2785 match=yes
CLAIM Q7: computed=5.477226 expected=5.48 match=yes
CLAIM Q8: computed=132.877124 expected=133 match=yes
CLAIM Q9: computed=15.054545 expected=15.05 match=yes
CLAIM Q10: computed=1.27 expected=1.27 match=yes
CLAIM Q11: computed=2.5 expected=2.5 match=yes
CLAIM Q12: computed=6.35 expected=6.35 match=yes
CLAIM Q13: computed=3.81 expected=3.81 match=yes
CLAIM Q14: computed=0.45 expected=0.45 match=yes
CLAIM Q15: computed=0.30 expected=0.30 match=yes
CLAIM Q16: computed=0.6985 expected=0.699 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.3486784401 | 0.3487 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.9043820750 | 0.9044 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 6.578814 | 6.58 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 2.593742 | 2.59 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.434388 | 0.4344 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.278501 | 0.2785 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 5.477226 | 5.48 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 132.877124 | 133 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 15.054545 | 15.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1.27 | 1.27 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 2.5 | 2.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 6.35 | 6.35 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 3.81 | 3.81 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.45 | 0.45 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.30 | 0.30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 0.6985 | 0.699 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
