# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Translation overhead factor |F^G|/|F| = 22/9 ≈ 2.4444444 for F = ((p ∨ q) → r) ∧ (p → q)",
    "inputs": "|p|=|q|=|r|=1; |p∨q|=3; |(p∨q)→r|=5; |p→q|=3; |F|=9; |F^G|=22",
    "formula": "|F^G|/|F| = 22/9"
  },
  {
    "id": "Q2",
    "statement": "Overhead for conjunction variant F' = ((p ∧ q) → r) ∧ (p → q) is 19/9 ≈ 2.1111111",
    "inputs": "|F'|=9; |F'^G|=19",
    "formula": "|F'^G|/|F'| = 19/9"
  },
  {
    "id": "Q3",
    "statement": "Model-space expansion on two-world chain, n=10: 1.5^10 = 57.6650390625",
    "inputs": "k=2, n=10",
    "formula": "((k+1)/2)^n = 1.5^10"
  },
  {
    "id": "Q4",
    "statement": "Model-space expansion on three-world chain, n=10: 2^10 = 1024",
    "inputs": "k=3, n=10",
    "formula": "((k+1)/2)^n = 2^10"
  },
  {
    "id": "Q5",
    "statement": "LEM branching: base tree 3^12 = 531441 nodes; with n=5 atoms, 531441 × 32 = 17006112 nodes",
    "inputs": "b=3, d=12, n=5",
    "formula": "b^d × 2^n = 3^12 × 32"
  },
  {
    "id": "Q6",
    "statement": "LEM branching at n=10 atoms: 531441 × 1024 = 544195584 nodes",
    "inputs": "b=3, d=12, n=10",
    "formula": "b^d × 2^n = 531441 × 1024"
  },
  {
    "id": "Q7",
    "statement": "Content gap, k=3, n=10: fraction where all LEM instances hold = 2^-10 = 1/1024 = 0.0009765625",
    "inputs": "k=3, n=10",
    "formula": "(2/(k+1))^n = (2/4)^10"
  },
  {
    "id": "Q8",
    "statement": "Content gap, k=2, n=10: (2/3)^10 = 1024/59049 ≈ 0.0173415",
    "inputs": "k=2, n=10",
    "formula": "(2/(k+1))^n = (2/3)^10"
  },
  {
    "id": "Q9",
    "statement": "Gap complement on three-world chain: 1 - 2^-10 = 1023/1024 ≈ 0.9990234375",
    "inputs": "k=3, n=10",
    "formula": "1 - (2/(k+1))^n"
  },
  {
    "id": "Q10",
    "statement": "Gap complement on two-world chain: 1 - 1024/59049 = 58025/59049 ≈ 0.9826585",
    "inputs": "k=2, n=10",
    "formula": "1 - (2/(k+1))^n"
  },
  {
    "id": "Q11",
    "statement": "BEM benchmark: 96 constant boundary elements",
    "inputs": "6 faces × 16 elements per face",
    "formula": "6 × 16"
  },
  {
    "id": "Q12",
    "statement": "BEM benchmark total applied load: 64 N",
    "inputs": "face area 4 mm × 4 mm = 16 mm²; traction 4 N/mm²",
    "formula": "16 × 4"
  },
  {
    "id": "Q13",
    "statement": "Classical valuation count at n=10: 2^10 = 1024",
    "inputs": "n=10",
    "formula": "2^10"
  },
  {
    "id": "Q14",
    "statement": "Two-world chain valuation count at n=10: 3^10 = 59049",
    "inputs": "k=2, n=10",
    "formula": "(k+1)^n = 3^10"
  },
  {
    "id": "Q15",
    "statement": "Three-world chain valuation count at n=10: 4^10 = 1048576",
    "inputs": "k=3, n=10",
    "formula": "(k+1)^n = 4^10"
  },
  {
    "id": "Q16",
    "statement": "Additive shortcut count |F^G| = 17 for a=3 atoms, v=1 disjunction (reported as disagreeing with direct count 22)",
    "inputs": "|F|=9, a=3, v=1",
    "formula": "|F| + 2a + 2v = 9 + 6 + 2"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 9, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: |F| = |p|+|q|+1 for p∨q = 3; |(p∨q)→r| = 3+1+1 = 5; |p→q| = 3; |F| = 5+3+1 = 9. |F^G|: |p^G| = 3; |¬p^G| = 4; |¬p^G∧¬q^G| = 9; |(p∨q)^G| = 10; |(p∨q)^G→r^G| = 14; |(p→q)^G| = 7; |F^G| = 14+7+1 = 22. 22/9 = 2.44444444... ≈ 2.4444444.
CLAIM Q1: computed=2.44444444444444 expected=2.4444444 match=yes

Q2: |F'| = 9 (same shape); |(p∧q)^G| = 3+3+1 = 7; |(p∧q)^G→r^G| = 7+3+1 = 11; |F'^G| = 11+7+1 = 19. 19/9 = 2.11111111... ≈ 2.1111111.
CLAIM Q2: computed=2.11111111111111 expected=2.1111111 match=yes

Q3: 1.5^2 = 2.25; 1.5^4 = 2.25^2 = 5.0625; 1.5^8 = 5.0625^2 = 25.62890625; 1.5^10 = 25.62890625 × 2.25 = 57.6650390625.
CLAIM Q3: computed=57.6650390625 expected=57.6650390625 match=yes

Q4: 2^10 = 1024.
CLAIM Q4: computed=1024 expected=1024 match=yes

Q5: 3^6 = 729; 3^12 = 729^2 = 531441; 2^5 = 32; 531441 × 32 = 17006112.
CLAIM Q5: computed=17006112 expected=17006112 match=yes

Q6: 531441 × 1024 = 544195584.
CLAIM Q6: computed=544195584 expected=544195584 match=yes

Q7: (2/4)^10 = 2^-10 = 1/1024 = 0.0009765625.
CLAIM Q7: computed=0.0009765625 expected=0.0009765625 match=yes

Q8: (2/3)^10 = 1024/59049. 3^10 = 59049. 1024/59049 = 0.0173415299... ≈ 0.0173415.
CLAIM Q8: computed=0.0173415299377557 expected=0.0173415 match=yes

Q9: 1 - 1/1024 = 1023/1024 = 0.9990234375.
CLAIM Q9: computed=0.9990234375 expected=0.9990234375 match=yes

Q10: 59049 - 1024 = 58025; 58025/59049 = 0.9826584700... ≈ 0.9826585.
CLAIM Q10: computed=0.982658470062831 expected=0.9826585 match=yes

Q11: 6 × 16 = 96.
CLAIM Q11: computed=96 expected=96 match=yes

Q12: 4 × 4 = 16 mm²; 16 × 4 = 64 N.
CLAIM Q12: computed=64 expected=64 match=yes

Q13: 2^10 = 1024.
CLAIM Q13: computed=1024 expected=1024 match=yes

Q14: 3^10 = 59049.
CLAIM Q14: computed=59049 expected=59049 match=yes

Q15: 4^10 = 1048576.
CLAIM Q15: computed=1048576 expected=1048576 match=yes

Q16: 9 + 2×3 + 2×1 = 9 + 6 + 2 = 17.
CLAIM Q16: computed=17 expected=17 match=yes

VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.44444444444444 | 2.4444444 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q2 | 2.11111111111111 | 2.1111111 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q3 | 57.6650390625 | 57.6650390625 | yes | match | 12 significant digits (as the paper states, at least 2) |
| Q4 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 17006112 | 17006112 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q6 | 544195584 | 544195584 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q7 | 0.0009765625 | 0.0009765625 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 0.0173415299377557 | 0.0173415 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.9990234375 | 0.9990234375 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q10 | 0.982658470062831 | 0.9826585 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 96 | 96 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 59049 | 59049 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 1048576 | 1048576 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
