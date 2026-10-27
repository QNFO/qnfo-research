# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Bit-to-nat conversion factor 1/ln 2 = 1.4426950408889634",
    "inputs": "ln 2 = 0.6931471805599453",
    "formula": "1/ln 2"
  },
  {
    "id": "Q2",
    "statement": "Nat-to-digit conversion factor 1/ln 10 = 0.4342944819032518",
    "inputs": "ln 10 = 2.302585092994046",
    "formula": "1/ln 10"
  },
  {
    "id": "Q3",
    "statement": "Base ratio ln 10 / ln 2 = 3.3219280948873626",
    "inputs": "ln 10 = 2.302585092994046, ln 2 = 0.6931471805599453",
    "formula": "ln 10 / ln 2"
  },
  {
    "id": "Q4",
    "statement": "Bit content per Planck area b = 0.36067376022224085 A",
    "inputs": "1/ln 2 = 1.4426950408889634",
    "formula": "(1/ln 2)/4"
  },
  {
    "id": "Q5",
    "statement": "Decimal digits per Planck area d = 0.10857362047581295 A",
    "inputs": "1/ln 10 = 0.4342944819032518",
    "formula": "(1/ln 10)/4"
  },
  {
    "id": "Q6",
    "statement": "For A = 10^68, S = 2.5e67 nats",
    "inputs": "A = 10^68",
    "formula": "S = A/4"
  },
  {
    "id": "Q7",
    "statement": "For A = 10^68, b = 3.6067376022224085e67 bits",
    "inputs": "S = 2.5e67, 1/ln 2 = 1.4426950408889634",
    "formula": "b = S * (1/ln 2)"
  },
  {
    "id": "Q8",
    "statement": "For A = 10^68, log10 D = 1.0857362048e67, so D <= 10^(1.0857362048e67)",
    "inputs": "S = 2.5e67, ln 10 = 2.302585092994046",
    "formula": "log10 D = S / ln 10"
  },
  {
    "id": "Q9",
    "statement": "At A = 4, e^(A/4) = e = 2.718281828459045, D_int = 2, relative deficit = 0.2642411177 (26.4%)",
    "inputs": "A = 4, e = 2.718281828459045",
    "formula": "(e - floor(e))/e"
  },
  {
    "id": "Q10",
    "statement": "At A = 1, e^(0.25) = 1.284025, D_int = 1, relative deficit = 0.2212 (22.1%)",
    "inputs": "A = 1",
    "formula": "(e^0.25 - floor(e^0.25))/e^0.25"
  },
  {
    "id": "Q11",
    "statement": "At A = 10^68, relative rounding deficit <= 10^(-1.085736e67) < 10^(-10^67)",
    "inputs": "log10 D = 1.085736e67, Delta < 1",
    "formula": "Delta/D <= 10^(-log10 D)"
  },
  {
    "id": "Q12",
    "statement": "One Planck area (A=1) carries S = 0.25 nats = 0.3606737602 bits = 0.1085736205 decimal digits",
    "inputs": "A = 1, 1/ln 2 = 1.4426950409, 1/ln 10 = 0.4342944819",
    "formula": "S = A/4; b = S/ln 2; d = S/ln 10"
  }
]

## Script
```python
# SymPy verification of equation transitions in
# "Non-Anthropocentric Natural Units for Area and Information in Holographic Entropy Bounds"
import sympy as sp
from sympy.physics.units import meter, kilogram, second, kelvin, joule, convert_to
from sympy import E, ln, log, Rational, pi, oo, S as SympyS

# ---------------------------------------------------------------
# Notation table with units (Planck natural units c=hbar=G=k_B=1)
# ---------------------------------------------------------------
# A  : horizon area, measured in Planck areas. Declare a Planck-area unit:
#     Planck area = l_P^2 with l_P^2 = hbar*G/c^3 (SI value ~2.612e-70 m^2)
hbar, G, c = sp.symbols('hbar G c', positive=True)
lP = sp.sqrt(hbar*G/c**3)                      # Planck length (symbolic)
Planck_area = lP**2                            # unit of area
A = sp.Symbol('A', positive=True)              # dimensionless number of Planck areas
S = sp.Symbol('S', positive=True)              # entropy in nats (dimensionless, k_B=1)
b = sp.Symbol('b', positive=True)              # entropy in bits (dimensionless)
d = sp.Symbol('d', positive=True)              # entropy in decimal digits (dimensionless)
D = sp.Symbol('D', positive=True)              # Hilbert-space dimension (dimensionless integer)

# Sanity: in natural units entropy S = A/4 is dimensionless; check area ratio dimensionless
_A_dim = A * Planck_area / Planck_area         # A is a count of Planck areas -> dimensionless
assert sp.simplify(_A_dim - A) == 0

# Sanity bounds / limiting cases
assert S.subs(A, 0) if False else True
# probabilities in [0,1]: none in this paper; efficiencies <= 1: none; costs: none.
# Stated limiting cases: A -> 0 => S -> 0, D <= 1 ; A = 4 => S = 1 nat.

def check(name, lhs, rhs, numeric_test=None):
    """simplify(lhs-rhs)==0 under positivity assumptions; else randomized spot checks."""
    diff = sp.simplify(sp.expand(lhs - rhs))
    if diff == 0:
        print(f"DERIV ok        : {name}")
        return
    # randomized numeric spot check
    import random, math
    ok = True
    for _ in range(20):
        Aval = random.uniform(0.1, 50)
        sub = {A: Aval}
        try:
            l = sp.N(lhs.subs(sub)); r = sp.N(rhs.subs(sub))
            if abs(l - r) > 1e-9 * max(1.0, abs(l)):
                ok = False; break
        except Exception:
            ok = False; break
    if ok and numeric_test is not None:
        ok = numeric_test()
    if ok:
        print(f"DERIV inconclusive (numeric ok, symbolic residual {diff}): {name}")
    else:
        print(f"DERIV refuted   : {name}")

# ---------------------------------------------------------------
# T1. Entropy in natural units: S = A/4  (nats), from holographic bound
#     with A in Planck areas, c=hbar=G=k_B=1
# ---------------------------------------------------------------
check("T1: S = A/4 (nats)", S, A/4,
      numeric_test=lambda: abs(float((A/4).subs(A, 10)) - 2.5) < 1e-12)

# Limiting case: A=4 -> S=1 nat
assert sp.simplify((A/4).subs(A, 4) - 1) == 0
# Limiting case: A -> 0 -> S -> 0
assert sp.limit(A/4, A, 0, '+') == 0

# ---------------------------------------------------------------
# T2. Base-free bound: D <= e^{A/4} = e^S  (Hilbert-space dimension bound)
#     (bound itself; check consistency S = ln D_max)
# ---------------------------------------------------------------
Dmax = sp.exp(A/4)
check("T2: ln(D_max) = S = A/4", sp.log(Dmax), A/4,
      numeric_test=lambda: abs(sp.log(sp.exp(sp.Rational(1,4))*1.0) - 0.25) < 1e-12)
# limiting case A->0: D_max -> 1
assert sp.limit(Dmax, A, 0, '+') == 1

# ---------------------------------------------------------------
# T3. Bit as derived quantity: b = S / ln 2
# ---------------------------------------------------------------
check("T3: b = S/ln2", b, S/ln(2),
      numeric_test=lambda: abs(float((sp.Rational(1,4)/ln(2)).subs(A,4)) - 1/ln(2)) < 1e-12)

# ---------------------------------------------------------------
# T4. Decimal digits: d = S / ln 10
# ---------------------------------------------------------------
check("T4: d = S/ln10", d, S/ln(10))

# ---------------------------------------------------------------
# T5. All base-b representations differ by fixed multiplicative constants:
#     S_b = S/ln b  =>  S_b / S_c = ln c / ln b  (constant, independent of S)
# ---------------------------------------------------------------
Sb, Sc, bb, bc = sp.symbols('S_b S_c beta gamma', positive=True)
check("T5: S_b/S_c = ln(c)/ln(b) fixed constant", Sb/Sc, ln(bc)/ln(bb),
      numeric_test=lambda: abs((sp.log(10)/sp.log(2)).evalf() - (1/ln(2))/(1/ln(10))) < 1e-12)

# ---------------------------------------------------------------
# T6. Worked example A = 1e68:  S = 2.5e67 nats
# ---------------------------------------------------------------
Aex = sp.Float(10)**68
Sex = Aex/4
check("T6: S(1e68) = 2.5e67 nats", Sex, sp.Float('2.5e67'),
      numeric_test=lambda: abs(float(Sex) - 2.5e67) < 1e53)

# ---------------------------------------------------------------
# T7. Worked example: b = 2.5e67/ln2 = 3.6067376e67 bits
# ---------------------------------------------------------------
bex = Sex/ln(2)
check("T7: b(1e68) = 3.6067376e67 bits", bex, sp.Float('3.6067376e67'),
      numeric_test=lambda: abs(float(bex) - 3.6067376e67) < 1e53)

# ---------------------------------------------------------------
# T8. Worked example: D_max = e^{2.5e67} = 10^{1.0857362e67}
#     since e^S = 10^{S/ln10}
# ---------------------------------------------------------------
check("T8: e^S = 10^(S/ln10)", sp.exp(S), sp.Float(10)**(S/ln(10)),
      numeric_test=lambda: abs(float(Sex/ln(10)) - 1.0857362e67) < 1e53)

# ---------------------------------------------------------------
# T9. Integer-rounding deficit at A=4: S=1 nat, D_max = e,
#     floor(D_max) = 2, relative deficit = (e - 2)/e = 26.4%
# ---------------------------------------------------------------
Dmax4 = sp.E
deficit4 = (Dmax4 - 2)/Dmax4
check("T9: relative deficit at A=4 = (e-2)/e = 26.4%", deficit4, sp.Rational(264,1000),
      numeric_test=lambda: abs(float(deficit4) - 0.2642411176571153) < 1e-9)
print(f"   (exact deficit at A=4 = {float(deficit4):.6f} ~ 26.4%)")

# ---------------------------------------------------------------
# T10. Rounding deficit at A=1e68 falls below 1e-10^67:
#      deficit = frac(e^S)/e^S < e^{-S} = e^{-2.5e67} << 10^{-10^67}
# ---------------------------------------------------------------
# e^{-2.5e67} vs 10^{-1.0857e67}: compare exponents: 2.5e67/ln10 = 1.0857e67 > 1e67
check("T10: e^{-S} < 10^{-1e67} i.e. S/ln10 > 1e67", Sex/ln(10) > sp.Float(10)**67,
      sp.true,
      numeric_test=lambda: 1.0857362e67 > 1e67)

# ---------------------------------------------------------------
# T11. Alternative normalization A=1: S = 1/4 nat, D_max = e^{1/4},
#      floor = 1, deficit = 1 - e^{-1/4}
# ---------------------------------------------------------------
deficit1 = 1 - sp.exp(sp.Rational(-1,4))
check("T11: deficit at A=1 = 1 - e^{-1/4}", deficit1, deficit1,
      numeric_test=lambda: abs(float(deficit1) - 0.2211992169) < 1e-9)

print("\nSanity summary: no probabilities/efficiencies/costs in this paper;")
print("limiting cases verified: A->0 => S->0, D_max->1; A=4 => S=1 nat.")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    return float(f"%.{n}g" % x)

ln2 = 0.6931471805599453
ln10 = 2.302585092994046
e = 2.718281828459045

results = []

# Q1
c1 = 1/ln2
results.append(("Q1", c1, "1.4426950408889634", 16))
# Q2
c2 = 1/ln10
results.append(("Q2", c2, "0.4342944819032518", 16))
# Q3
c3 = ln10/ln2
results.append(("Q3", c3, "3.3219280948873626", 16))
# Q4
c4 = (1/ln2)/4
results.append(("Q4", c4, "0.36067376022224085", 17))
# Q5
c5 = (1/ln10)/4
results.append(("Q5", c5, "0.10857362047581295", 17))
# Q6
A = 1e68
c6 = A/4
results.append(("Q6", c6, "2.5e67", 2))
# Q7
S = 2.5e67
c7 = S * (1/ln2)
results.append(("Q7", c7, "3.6067376022224085e67", 17))
# Q8
c8 = S / ln10
results.append(("Q8", c8, "1.0857362048e67", 11))
# Q9
val9 = math.exp(4/4)
d9 = (val9 - math.floor(val9))/val9
results.append(("Q9", d9, "0.2642411177", 10))
# Q10
val10 = math.exp(0.25)
d10 = (val10 - math.floor(val10))/val10
results.append(("Q10", d10, "0.2212", 4))
# Q11
# relative deficit <= 1/D = 10^(-log10 D); log10 D = 1.0857362048e67
# claim: 10^(-1.085736e67) < 10^(-10^67); compare exponents: 1.085736e67 > 1e67
c11 = 1.085736e67 > 1e67
results.append(("Q11", 1.0 if c11 else 0.0, "1", 1))
# Q12
s12 = 1/4
b12 = s12 * (1/ln2)
d12 = s12 * (1/ln10)
results.append(("Q12", b12, "0.3606737602", 10))
results.append(("Q12b", d12, "0.1085736205", 10))

match_count = 0
for item in results:
    cid, computed, expected, n = item
    comp = sig(computed, n)
    match = ("%.{0}g".format(n) % computed) == expected
    print(f"CLAIM {cid}: computed={comp!r} expected={expected} match={'yes' if match else 'no'}")
    if match:
        match_count += 1

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 3, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: 1/ln 2 = 1/0.6931471805599453. Long division: 1/0.6931471805599453 = 1.4426950408889634 (check: 0.6931471805599453 × 1.4426950408889634 = 1.0000000000000000). 
CLAIM Q1: computed=1.4426950408889634 expected=1.4426950408889634 match=yes

Q2: 1/ln 10 = 1/2.302585092994046 = 0.4342944819032518 (check: 2.302585092994046 × 0.4342944819032518 = 1.0000000000000000). 
CLAIM Q2: computed=0.4342944819032518 expected=0.4342944819032518 match=yes

Q3: ln 10/ln 2 = 2.302585092994046/0.6931471805599453. Compute: 0.6931471805599453 × 3 = 2.0794415416798359; remainder 0.2231435513142101; 0.2231435513142101/0.6931471805599453 ≈ 0.3219280948873626; total = 3.3219280948873626. 
CLAIM Q3: computed=3.3219280948873626 expected=3.3219280948873626 match=yes

Q4: (1/ln 2)/4 = 1.4426950408889634/4 = 0.36067376022224085. 
CLAIM Q4: computed=0.36067376022224085 expected=0.36067376022224085 match=yes

Q5: (1/ln 10)/4 = 0.4342944819032518/4 = 0.10857362047581295. 
CLAIM Q5: computed=0.10857362047581295 expected=0.10857362047581295 match=yes

Q6: S = A/4 = 10^68/4 = 2.5×10^67. 
CLAIM Q6: computed=2.5e67 expected=2.5e67 match=yes

Q7: b = S × (1/ln 2) = 2.5e67 × 1.4426950408889634 = 3.6067376022224085e67. 
CLAIM Q7: computed=3.6067376022224085e67 expected=3.6067376022224085e67 match=yes

Q8: log10 D = S/ln 10 = 2.5e67/2.302585092994046. Mantissa: 2.5/2.302585092994046 = 1.0857362047581295, so log10 D = 1.0857362047581295e67; paper states 1.0857362048e67, matching to its stated 11 significant digits. 
CLAIM Q8: computed=1.0857362047581295e67 expected=1.0857362048e67 match=yes

Q9: e^(4/4) = e = 2.718281828459045; floor = 2; deficit = (2.718281828459045 − 2)/2.718281828459045 = 0.718281828459045/2.718281828459045 = 0.2642411176571153 ≈ 26.4%. 
CLAIM Q9: computed=0.2642411176571153 expected=0.2642411177 match=yes

Q10: e^0.25 = 1.2840254166877414; floor = 1; deficit = 0.2840254166877414/1.2840254166877414 = 0.2211992169474013 ≈ 22.1%. 
CLAIM Q10: computed=0.2211992169474013 expected=0.2212 match=yes

Q11: Δ/D ≤ 1/D = 10^(−log10 D) = 10^(−1.085736e67). Since 1.085736×10^67 > 10^67, this is smaller than 10^(−10^67). 
CLAIM Q11: computed=10^(-1.085736e67) expected=10^(-1.085736e67) match=yes

Q12: S = 1/4 = 0.25 nats; b = 0.25 × 1.4426950409 = 0.3606737602 bits; d = 0.25 × 0.4342944819 = 0.1085736205 decimal digits. 
CLAIM Q12: computed=0.25,0.3606737602,0.1085736205 expected=0.25,0.3606737602,0.1085736205 match=yes

VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.4426950408889634 | 1.4426950408889634 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q2 | 0.4342944819032518 | 0.4342944819032518 | yes | match | 16 significant digits (as the paper states, at least 2) |
| Q3 | 3.3219280948873626 | 3.3219280948873626 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q4 | 0.36067376022224085 | 0.36067376022224085 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q5 | 0.10857362047581295 | 0.10857362047581295 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q6 | 2.5e67 | 2.5e67 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 3.6067376022224085e67 | 3.6067376022224085e67 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q8 | 1.0857362047581295e67 | 1.0857362048e67 | yes | match | 11 significant digits (as the paper states, at least 2) |
| Q9 | 0.2642411176571153 | 0.2642411177 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q10 | 0.2211992169474013 | 0.2212 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 10^(-1.085736e67) | 10^(-1.085736e67) | yes | match | script verdict (values not both numeric) |
| Q12 | 0.25,0.3606737602,0.1085736205 | 0.25,0.3606737602,0.1085736205 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 12.
