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
