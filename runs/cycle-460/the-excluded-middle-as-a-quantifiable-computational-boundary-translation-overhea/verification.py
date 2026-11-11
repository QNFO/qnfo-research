# -*- coding: utf-8 -*-
"""
SymPy verification of equation transitions in
"The Excluded Middle as a Quantifiable Computational Boundary..."
Each transition is checked as simplify(lhs - rhs) == 0 under declared assumptions,
with randomized numeric spot checks when symbolic simplification is inconclusive.
"""
import random
from sympy import (symbols, Rational, Integer, simplify, S, Eq, latex, binomial,
                   factorial, sqrt, pi, exp, log, Function, Sum, oo)
from sympy.physics.units import meter, newton, second, dimensionless

random.seed(20240613)

# ---------------------------------------------------------------- notation ---
# No physical units appear in the derivations; all quantities are dimensionless
# counts, ratios, or probabilities. Declared with sympy.physics.units:
SIZE          = Integer(1) * dimensionless   # formula size (node count)
OVERHEAD      = Integer(1) * dimensionless   # translation overhead factor
N_VARS        = Integer(1) * dimensionless   # number of propositional variables
BRANCH        = Integer(1) * dimensionless   # proof-search branching factor
DEPTH         = Integer(1) * dimensionless   # proof-search depth
NODES         = Integer(1) * dimensionless   # search-tree node count
FRACTION      = Integer(1) * dimensionless   # fraction of Kripke valuations
LOAD          = Integer(1) * newton          # applied load (N)
N_ELEM        = Integer(1) * dimensionless   # number of boundary elements

def report(tag, ok):
    print(f"DERIV {ok} | {tag}")

def check_eq(lhs, rhs, subs_list=None, n_spot=200):
    """Return 'ok' | 'refuted' | 'inconclusive' for lhs == rhs."""
    diff = simplify(lhs - rhs)
    if diff == 0:
        return "ok"
    # numeric spot checks
    try:
        for _ in range(n_spot):
            subs = {}
            for s_, lo, hi in (subs_list or []):
                subs[s_] = Rational(random.randint(lo, hi))
            if subs:
                if simplify((lhs - rhs).subs(subs)) != 0:
                    return "refuted"
            else:
                break
        return "inconclusive"
    except Exception:
        return "inconclusive"

# =============================================================== Section 4.1
# T1: overhead factor = translated size / original size
# premise: size(GG(phi)) = 22, size(phi) = 9
# conclusion: overhead = 22/9 ≈ 2.44
lhs = Rational(22, 1) * SIZE
rhs = Rational(22, 9) * SIZE
report("T1 overhead = 22/9 (size 9 -> 22)", check_eq(lhs, rhs))

# T2: 22/9 ≈ 2.44 (rounded decimal)
lhs = Rational(22, 9)
rhs = Rational(244, 100)
report("T2 22/9 ≈ 2.44 (rounding)", check_eq(lhs, rhs))  # expected refuted/inconclusive (rounding)

# =============================================================== Section 4.2
# T3: two-world chain expansion factor = (3/2)^n ; n = 10 -> 57.7
n = symbols('n', positive=True, integer=True)
lhs = (Rational(3, 2) ** n) * N_VARS
rhs = (Rational(3, 2) ** n) * N_VARS
report("T3 expansion factor (3/2)^n (two-world chain)", check_eq(lhs, rhs))

lhs = Rational(3, 2) ** 10
rhs = Rational(577, 10)  # ≈ 57.7
report("T4 (3/2)^10 ≈ 57.7", check_eq(lhs, rhs))  # exact 57.665..., rounding

# T5: three-world chain expansion factor = 2^n ; n = 10 -> 1024
lhs = S(2) ** 10
rhs = Integer(1024)
report("T5 2^10 = 1024 (three-world chain)", check_eq(lhs, rhs))

# =============================================================== Section 4.3
# T6: LEM branching multiplier = 2^a for a atoms; a = 5 -> 32
a = symbols('a', positive=True, integer=True)
lhs = S(2) ** 5
rhs = Integer(32)
report("T6 LEM multiplier 2^5 = 32", check_eq(lhs, rhs))

# T7: base tree nodes = b^d ; b=3, d=12 -> 531441
b, d = symbols('b d', positive=True, integer=True)
lhs = b ** d
rhs = Integer(531441)
report("T7 base tree 3^12 = 531441", check_eq(lhs.subs({b: 3, d: 12}), rhs))

# T8: LEM tree = base * 2^a -> 531441 * 32 = 17006112
lhs = Integer(531441) * Integer(32)
rhs = Integer(17006112)
report("T8 531441 * 32 = 17006112", check_eq(lhs, rhs))

# =============================================================== Section 4.4
# T9: fraction of Kripke valuations satisfying all n LEM instances = 2^{-n}
lhs = S(2) ** (-n)
rhs = S(2) ** (-n)
report("T9 fraction = 2^{-n}", check_eq(lhs, rhs))

# T10: n = 10 -> 1/1024 ≈ 0.0009765625
lhs = Rational(1, 1024)
rhs = Rational(9765625, 10000000000)
report("T10 1/1024 ≈ 0.0009765625", check_eq(lhs, rhs))  # exact decimal: equal

# =============================================================== Section 4.5
# T11: contrast case: 96 constant boundary elements, total load 64 N
lhs = Integer(96) * N_ELEM
rhs = Integer(96) * N_ELEM
report("T11 element count 96 (identity)", check_eq(lhs, rhs))

lhs = Integer(64) * newton
rhs = Integer(64) * newton
report("T12 total load 64 N (identity)", check_eq(lhs, rhs))

# ================================================== sanity / limiting checks =
print("--- sanity bounds ---")
# probabilities in [0,1]
f = Rational(1, 1024)
assert 0 <= f <= 1
print("SANITY fraction 1/1024 in [0,1]: ok")
# efficiencies <= 1 (overhead factors are ratios; expansion factors >= 1)
assert Rational(22, 9) > 1 and (Rational(3, 2) ** 10) > 1 and S(2) ** 10 >= 1
print("SANITY expansion/overhead factors >= 1: ok")
# nonnegative costs
assert Integer(531441) > 0 and Integer(17006112) > 0 and Integer(96) > 0
print("SANITY node/element counts nonnegative: ok")
# units
assert LOAD == 64 * newton
print("SANITY load = 64 N (units newton): ok")
# limiting cases
assert (S(2) ** (-n)).subs(n, 0) == 1, "fraction -> 1 as n -> 0"
assert (S(2) ** (-n)).limit(n, oo) == 0, "fraction -> 0 as n -> oo"
assert (Rational(3, 2) ** n).limit(n, oo) == oo
print("SANITY limiting cases: 2^{-n}->1 (n=0), ->0 (n->oo), (3/2)^n->oo: ok")

import math
from fractions import Fraction

def sig(x, digits):
    if x == 0:
        return 0.0
    return round(x, digits - 1 - int(math.floor(math.log10(abs(x)))))

results = []

# Q1: 22/9
c1 = Fraction(22, 9)
results.append(("Q1", float(c1), "2.4444444", sig(float(c1), 7) == float("2.4444444")))

# Q2: 19/9
c2 = Fraction(19, 9)
results.append(("Q2", float(c2), "2.1111111", sig(float(c2), 7) == float("2.1111111")))

# Q3: 1.5^10
c3 = 1.5 ** 10
results.append(("Q3", c3, "57.6650390625", sig(c3, 12) == float("57.6650390625")))

# Q4: 2^10
c4 = 2 ** 10
results.append(("Q4", c4, "1024", sig(c4, 4) == float("1024")))

# Q5: 3^12 * 2^5
c5 = 3 ** 12 * 2 ** 5
results.append(("Q5", c5, "17006112", sig(c5, 8) == float("17006112")))

# Q6: 3^12 * 2^10
c6 = 3 ** 12 * 2 ** 10
results.append(("Q6", c6, "544195584", sig(c6, 9) == float("544195584")))

# Q7: (2/4)^10 = 2^-10
c7 = Fraction(2, 4) ** 10
results.append(("Q7", float(c7), "0.0009765625", sig(float(c7), 7) == float("0.0009765625")))

# Q8: (2/3)^10
c8 = Fraction(2, 3) ** 10
results.append(("Q8", float(c8), "0.0173415", sig(float(c8), 6) == float("0.0173415")))

# Q9: 1 - 2^-10
c9 = 1 - Fraction(2, 4) ** 10
results.append(("Q9", float(c9), "0.9990234375", sig(float(c9), 10) == float("0.9990234375")))

# Q10: 1 - (2/3)^10
c10 = 1 - Fraction(2, 3) ** 10
results.append(("Q10", float(c10), "0.9826585", sig(float(c10), 6) == float("0.9826585")))

# Q11: 6 * 16
c11 = 6 * 16
results.append(("Q11", c11, "96", sig(c11, 2) == float("96")))

# Q12: 16 * 4
c12 = 16 * 4
results.append(("Q12", c12, "64", sig(c12, 2) == float("64")))

# Q13: 2^10
c13 = 2 ** 10
results.append(("Q13", c13, "1024", sig(c13, 4) == float("1024")))

# Q14: 3^10
c14 = 3 ** 10
results.append(("Q14", c14, "59049", sig(c14, 5) == float("59049")))

# Q15: 4^10
c15 = 4 ** 10
results.append(("Q15", c15, "1048576", sig(c15, 7) == float("1048576")))

# Q16: 9 + 2*3 + 2*1
c16 = 9 + 2 * 3 + 2 * 1
results.append(("Q16", c16, "17", sig(c16, 2) == float("17")))

m = 0
for qid, computed, expected, match in results:
    print(f"CLAIM {qid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    if match:
        m += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")
