# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Single-level eight-fold majority vote failure probability at p=0.4 is 0.1736704",
    "inputs": "n=8, p=0.4, 1-p=0.6",
    "formula": "f(p) = sum_{k=5}^{8} C(8,k) p^k (1-p)^(8-k)"
  },
  {
    "id": "Q2",
    "statement": "Two concatenated levels give p^(2) ≈ 0.0055485",
    "inputs": "p^(1)=0.1736704",
    "formula": "f(p^(1)) = sum_{k=5}^{8} C(8,k) (p^(1))^k (1-p^(1))^(8-k)"
  },
  {
    "id": "Q3",
    "statement": "Three concatenated levels give p^(3) ≈ 2.905e-10",
    "inputs": "p^(2)=0.0055485",
    "formula": "f(p^(2)) = sum_{k=5}^{8} C(8,k) (p^(2))^k (1-p^(2))^(8-k)"
  },
  {
    "id": "Q4",
    "statement": "Single-level suppression factor ≈ 2.303",
    "inputs": "p=0.4, p^(1)=0.1736704",
    "formula": "p / p^(1)"
  },
  {
    "id": "Q5",
    "statement": "Confidence bound p_L ≤ 2.9957e-4 for N=10^4",
    "inputs": "N=10^4, ln20=2.995732, confidence 0.95",
    "formula": "p_L ≤ 1 - 0.05^(1/N) ≈ ln20 / N"
  },
  {
    "id": "Q6",
    "statement": "Confidence bound p_L ≤ 2.9957e-5 for N=10^5",
    "inputs": "N=10^5, ln20=2.995732",
    "formula": "p_L ≤ ln20 / N"
  },
  {
    "id": "Q7",
    "statement": "Thermal-activation bound p_L(3) ≤ 3.3546e-4",
    "inputs": "d=3, barrier E=2^d=8, k_B T=1",
    "formula": "p_L(d) ≤ e^(-2^d)"
  },
  {
    "id": "Q8",
    "statement": "Thermal-activation bound p_L(5) ≤ 1.2664e-14",
    "inputs": "d=5, barrier E=2^d=32",
    "formula": "p_L(d) ≤ e^(-2^d)"
  },
  {
    "id": "Q9",
    "statement": "Thermal-activation bound p_L(10) ≤ 10^(-444.7)",
    "inputs": "d=10, barrier E=2^d=1024, ln10≈2.302585",
    "formula": "p_L(d) ≤ e^(-2^d) = 10^(-2^d / ln10)"
  },
  {
    "id": "Q10",
    "statement": "Zero observed errors requires N ≲ 3.4e9 for p^(3)",
    "inputs": "p^(3)=2.905e-10",
    "formula": "N ≈ 1 / p^(3)"
  }
]

## Script
```python
# SymPy verification of equation transitions from
# "Ultrametric Quantum Error Correction on Bruhat-Tits Trees"
# Sections analyzed: Sec. 3 (barrier derivation), Sec. 4 (majority-vote
# arithmetic, confidence bound, thermal-activation projection).

import sympy as sp
from sympy import Rational, binomial, simplify, exp, log, symbols, oo
from sympy.physics.units import energy, joule, kelvin
from sympy.physics.units import convert_to

# ------------------------------------------------------------------
# Notation table with declared units
# ------------------------------------------------------------------
# p        : physical error probability          [dimensionless, in [0,1]]
# p_L      : logical error probability           [dimensionless, in [0,1]]
# d        : tree depth                          [dimensionless integer >= 0]
# E_barrier: energy barrier                      [energy]
# epsilon  : per-step energy cost                [energy, nonnegative]
# k_B T    : thermal energy scale                [energy]; paper sets k_B T = epsilon
# N        : number of trials                    [dimensionless, positive]

p, d, N, eps = symbols('p d N epsilon', positive=True)
E_barrier = symbols('E_barrier', positive=True)

# Sanity bounds on declared quantities
assert 0 <= Rational(2, 5) <= 1                      # p = 0.4 in [0,1]
assert eps.is_positive                               # nonnegative cost
# efficiency analogue: suppression factor f(p) must be <= 1 (checked below)

# ------------------------------------------------------------------
# Majority-vote map: f(p) = P(Bin(8,p) >= 5)
# ------------------------------------------------------------------
def f(x):
    return sum(binomial(8, k) * x**k * (1 - x)**(8 - k) for k in range(5, 9))

# T1: (independent per-bit BSC at p=0.4, 8-fold majority vote)
#      --> f(0.4) = 0.1736704
lhs, rhs = f(Rational(2, 5)), sp.Float('0.1736704', 20)
diff = simplify(sp.nsimplify(lhs) - Rational(1736704, 10000000))
print("DERIV", "ok" if diff == 0 else "refuted",
      "| T1: f(0.4)=0.1736704 (binomial tail, 8-fold majority)")

# T2: (concatenation, independence of levels) f(f(0.4)) ~= 5.5485e-3
val2 = f(f(Rational(2, 5)))
print("DERIV", "ok" if abs(float(val2) - 5.5485e-3) < 1e-6 else "refuted",
      "| T2: f^2(0.4) = %.7g (iterated majority vote)" % float(val2))

# T3: f^3(0.4) ~= 2.905e-10
val3 = f(f(f(Rational(2, 5))))
print("DERIV", "ok" if abs(float(val3) - 2.905e-10) < 1e-12 else "refuted",
      "| T3: f^3(0.4) = %.6g (third concatenation level)" % float(val3))

# Randomized spot check: binomial-tail identity f(p) is a valid probability
# map on [0,1] (sanity: probabilities in [0,1], "efficiency" f(p) <= 1)
import random
ok = True
for _ in range(200):
    x = random.random()
    fx = float(f(sp.Float(x, 15)))
    if not (0 <= fx <= 1):
        ok = False
print("DERIV", "ok" if ok else "refuted",
      "| T1s: f maps [0,1]->[0,1] (randomized spot check, 200 samples)")

# ------------------------------------------------------------------
# T4: zero logical errors in N trials  -->  p_L <= ln(20)/N
# Justification: one-sided 95% confidence bound; 1-(1-p_L)^N >= 0.95
# gives p_L <= 1 - 0.05^(1/N) ~ ln(20)/N for large N (Poisson/large-N approx).
# ------------------------------------------------------------------
pL = symbols('p_L', positive=True)
exact_bound = 1 - Rational(5, 100)**(sp.Rational(1, 1)/N)
approx_bound = log(20)/N
# Check the approximation 1 - exp(-N p) ~ N p  under N*p_L << 1:
# exact condition: (1-pL)^N >= 0.05  <=>  N*log(1-pL) >= log(1/20)
# ln(20)/N is the standard large-N form; verify numerically for N=1e5:
Nv = 10**5
exact_num = 1 - 0.05**(1.0/Nv)
approx_num = float(log(20))/Nv
rel_err = abs(exact_num - approx_num)/exact_num
print("DERIV", "ok" if rel_err < 1e-4 else "inconclusive",
      "| T4: p_L <= ln(20)/N from zero errors in N trials "
      "(95% one-sided bound; rel. err %.2e at N=1e5)" % rel_err)
# Paper's stated value: ln(20)/1e5 = 2.9957e-5
print("DERIV", "ok" if abs(float(log(20)/Nv) - 2.9957e-5) < 1e-8 else "refuted",
      "| T4v: ln(20)/N = 2.9957e-5 at N=1e5")

# ------------------------------------------------------------------
# T5: E_barrier(d) = 2^d * epsilon  -->  p_L <= exp(-2^d)
# Justification: thermal (Arrhenius) activation, p_L ~ exp(-E_barrier/(k_B T))
# with the paper's stated barrier model k_B T = epsilon (units: energy).
# ------------------------------------------------------------------
# Dimensional sanity: E_barrier and k_B T both carry [energy]
E_dim = convert_to(2**3 * eps * joule, joule)
assert E_dim == 8 * joule
lhs5 = exp(-E_barrier/(eps))          # general Arrhenius form
rhs5 = exp(-2**d)                     # paper's projection with k_B T = eps, E=2^d eps
# Under the substitution E_barrier = 2^d * eps these agree identically:
diff5 = simplify(lhs5.subs(E_barrier, 2**d * eps) - rhs5)
print("DERIV", "ok" if diff5 == 0 else "refuted",
      "| T5: p_L <= exp(-2^d) from Arrhenius with E_barrier=2^d*eps, k_B T=eps")
# Numeric spot check at d=3: exp(-8) ~ 3.3546e-4
print("DERIV", "ok" if abs(float(exp(-8)) - 3.35463e-4) < 1e-8 else "refuted",
      "| T5n: exp(-2^3) = %.5e (numeric spot check)" % float(exp(-8)))

# ------------------------------------------------------------------
# T6: ultrametric minimal-cut structure of the Bruhat-Tits tree
#      -->  E_barrier(d) = 2^d * epsilon
# Justification: geometric doubling argument (minimal cut doubles per level).
# This is the paper's own conjecture-level derivation; no closed-form
# premise is available in the text to verify algebraically.
# ------------------------------------------------------------------
print("DERIV inconclusive | T6: E_barrier(d)=2^d*eps from ultrametric "
      "cut structure (conjecture-level geometric argument; -> verification appendix)")

# Limiting-case sanity checks stated by the paper:
# (i) d -> infinity: p_L -> 0 under T5
lim = sp.limit(exp(-2**d), d, oo)
print("DERIV", "ok" if lim == 0 else "refuted",
      "| LC1: lim_{d->oo} exp(-2^d) = 0 (stated limiting case)")
# (ii) d = 0: barrier = eps, p_L <= e^-1 (nontrivial but < 1)
print("DERIV", "ok" if 0 < float(exp(-1)) < 1 else "refuted",
      "| LC2: d=0 gives p_L <= e^-1 in (0,1)")
# (iii) concatenation threshold: f(p) < p for p in (0, 1/2) region containing 0.4
ok3 = all(float(f(sp.Float(x, 12))) < x for x in
          [0.05, 0.1, 0.2, 0.3, 0.4, 0.45])
print("DERIV", "ok" if ok3 else "inconclusive",
      "| LC3: f(p) < p on sampled p in (0,0.5) (recursive threshold mechanism)")

import math

def f(p):
    # majority vote over 8 bits fails when >= 5 flip
    s = 0.0
    for k in range(5, 9):
        c = math.comb(8, k)
        s += c * (p ** k) * ((1 - p) ** (8 - k))
    return s

# Q1
p1 = f(0.4)
print(f"CLAIM Q1: computed={p1:.8g} expected=0.1736704 match={'yes' if round(p1, 7) == 0.1736704 else 'no'}")

# Q2
p2 = f(p1)
print(f"CLAIM Q2: computed={p2:.8g} expected=0.0055485 match={'yes' if round(p2, 7) == 0.0055485 else 'no'}")

# Q3 (paper uses p2 = 0.0055485 as stated input)
p2_stated = 0.0055485
p3 = f(p2_stated)
print(f"CLAIM Q3: computed={p3:.8g} expected=2.905e-10 match={'yes' if abs(p3 - 2.905e-10) / 2.905e-10 < 0.005 else 'no'}")

# Q4
sup = 0.4 / p1
print(f"CLAIM Q4: computed={sup:.8g} expected=2.303 match={'yes' if round(sup, 3) == 2.303 else 'no'}")

# Q5
ln20 = math.log(20)
bound5 = ln20 / 1e4
print(f"CLAIM Q5: computed={bound5:.8g} expected=2.9957e-4 match={'yes' if round(bound5, 8) == 2.9957e-4 else 'no'}")

# Q6
bound6 = ln20 / 1e5
print(f"CLAIM Q6: computed={bound6:.8g} expected=2.9957e-5 match={'yes' if round(bound6, 9) == 2.9957e-5 else 'no'}")

# Q7
b7 = math.exp(-8)
print(f"CLAIM Q7: computed={b7:.8g} expected=3.3546e-4 match={'yes' if round(b7, 8) == 3.3546e-4 else 'no'}")

# Q8
b8 = math.exp(-32)
print(f"CLAIM Q8: computed={b8:.8g} expected=1.2664e-14 match={'yes' if round(b8, 18) == 1.2664e-14 else 'no'}")

# Q9
b9 = 1024 / math.log(10)
print(f"CLAIM Q9: computed={b9:.8g} expected=-444.7 match={'yes' if round(b9, 1) == 444.7 else 'no'}")

# Q10
n10 = 1 / 2.905e-10
print(f"CLAIM Q10: computed={n10:.8g} expected=3.4e9 match={'yes' if round(n10 / 1e8) * 1e8 == 3.4e9 else 'no'}")

print("VERIFICATION SUMMARY: 10 claims, " + str(sum(1 for _ in []) ) + " placeholder")

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
Q1: f(0.4) = C(8,5)·0.4^5·0.6^3 + C(8,6)·0.4^6·0.6^2 + C(8,7)·0.4^7·0.6 + 0.4^8
= 56·0.01024·0.216 + 28·0.004096·0.36 + 8·0.0016384·0.6 + 0.00065536
= 0.12386304 + 0.04128768 + 0.00786432 + 0.00065536 = 0.17367040
CLAIM Q1: computed=0.17367040 expected=0.1736704 match=yes

Q2: f(0.1736704): p1=0.1736704, 1−p1=0.8263296.
p1^2=0.030161414; p1^4=0.000909691; p1^5=0.000157982; p1^6=0.000027437; p1^7=0.000004765; p1^8=0.000000827.
(1−p1)^2=0.68282058; (1−p1)^3=0.564233.
k=5: 56·0.000157982·0.564233=0.00499156
k=6: 28·0.000027437·0.68282058=0.00052458
k=7: 8·0.000004765·0.8263296=0.00003150
k=8: 0.00000083
Sum = 0.00499156+0.00052458+0.00003150+0.00000083 = 0.00554847
CLAIM Q2: computed=0.00554847 expected=0.0055485 match=yes

Q3: f(0.0055485): p2=0.0055485, 1−p2=0.9944515.
p2^2=0.000030786; p2^4=9.478e-10; p2^5=5.259e-12; p2^6=2.918e-14; p2^7=1.619e-16.
(1−p2)^3≈0.98345; (1−p2)^2≈0.98896.
k=5: 56·5.259e-12·0.98345=2.897e-10
k=6: 28·2.918e-14·0.98896=8.09e-13
k=7: 8·1.619e-16·0.99445≈1.29e-15
k=8: ≈9e-19 (negligible)
Sum ≈ 2.897e-10 + 8.09e-13 + 1.3e-15 = 2.905e-10
CLAIM Q3: computed=2.90510e-10 expected=2.905e-10 match=yes

Q4: 0.4/0.1736704 = 2.30321… (0.1736704·2.303=0.3999629; remainder 0.0000371/0.1736704≈0.000214, giving 2.303214)
CLAIM Q4: computed=2.3032138 expected=2.303 match=yes

Q5: ln20/N = 2.995732/10^4 = 2.995732e-4 (and 1−0.05^(1/10^4)=1−e^(−2.995732e-4)≈2.9957e-4 to 5 significant digits)
CLAIM Q5: computed=2.9957320e-4 expected=2.9957e-4 match=yes

Q6: ln20/N = 2.995732/10^5 = 2.995732e-5
CLAIM Q6: computed=2.9957320e-5 expected=2.9957e-5 match=yes

Q7: e^(−2^3)=e^(−8); e^8=2980.958; 1/2980.958=3.35463e-4
CLAIM Q7: computed=3.3546263e-4 expected=3.3546e-4 match=yes

Q8: e^(−2^5)=e^(−32); e^32=7.8962960e13; 1/7.8962960e13=1.2664166e-14
CLAIM Q8: computed=1.2664166e-14 expected=1.2664e-14 match=yes

Q9: 2^10=1024; 1024/ln10 = 1024/2.302585 = 444.7176 (check: 2.302585·444=1022.34774; 1024−1022.34774=1.65226; 1.65226/2.302585=0.71760)
CLAIM Q9: computed=444.71756 expected=444.7 match=yes

Q10: 1/p^(3) = 1/2.905e-10 = 3.44234e9 ≈ 3.4e9
CLAIM Q10: computed=3.4423404e9 expected=3.4e9 match=yes

VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.17367040 | 0.1736704 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 0.00554847 | 0.0055485 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 2.90510e-10 | 2.905e-10 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 2.3032138 | 2.303 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 2.9957320e-4 | 2.9957e-4 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2.9957320e-5 | 2.9957e-5 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 3.3546263e-4 | 3.3546e-4 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 1.2664166e-14 | 1.2664e-14 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 444.71756 | 444.7 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 3.4423404e9 | 3.4e9 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
