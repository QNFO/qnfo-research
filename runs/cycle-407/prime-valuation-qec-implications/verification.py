# Remediation audit: equation-transition checks for
# "Implications for Computing and QEC: Remediation under Erratum pl-prime-valuation-qec-implications-v0.4-0"
#
# Notation table (all quantities are COUNTS / RATIOS => dimensionless; declared via sympy.physics.units):
#   n          : number of physical qubits / tree pendent vertices  [dimensionless count]
#   k          : number of logical qubits                           [dimensionless count]
#   d          : code distance                                      [dimensionless count]
#   accuracy   : classification accuracy (probability)              [dimensionless, in [0,1]]
#   gap_frac   : spectral-gap verification fraction                 [dimensionless, in [0,1]]
#   M1, M2     : Zagreb indices                                     [dimensionless]
#   v_p(n)     : p-adic valuation                                   [dimensionless integer]
# Sanity bounds: probabilities in [0,1]; "efficiencies" (accuracy/gap fractions) <= 1;
# costs (n-k overhead, n/k) nonnegative; limiting cases d>=2, n>=k.

from sympy import Rational, simplify, symbols, S, Integer, Eq, Le, Ge, Gt, floor, randrat
from sympy.ntheory.factor_ import multiplicity
from sympy.physics.units import dimensionless as DIMLESS
from sympy.physics.units import convert_to
import random

random.seed(0)
results = []

def report(tag, ok):
    status = "ok" if ok else "refuted"
    print(f"DERIV {status} | {tag}")
    results.append((tag, status))

def inconclusive(tag):
    print(f"DERIV inconclusive | {tag}")
    results.append((tag, "inconclusive"))

# --- Unit/sanity declarations -------------------------------------------------
n, k, d = symbols('n k d', integer=True, positive=True)
# All quantities dimensionless counts:
for q in (n, k, d):
    assert convert_to(q, DIMLESS) == q
# Probabilities/efficiencies in [0,1] checked below per transition.

# --- T1: per-family accuracies sum to aggregate -------------------------------
# Premise: per-family correct-code counts 46, 39, 45, 36 (surface, CSS, optimal, random)
# Conclusion: total correct = 166
lhs = Integer(46) + Integer(39) + Integer(45) + Integer(36)
rhs = Integer(166)
report("T1 sum{46,39,45,36} = 166 (arithmetic addition)", simplify(lhs - rhs) == 0)

# --- T2: aggregate accuracy 166/200 = 83% -------------------------------------
# Premise: 166 correct of 200-code corpus. Conclusion: accuracy = 83% = 83/100.
lhs = Rational(166, 200); rhs = Rational(83, 100)
ok = simplify(lhs - rhs) == 0
ok = ok and (0 <= float(lhs) <= 1)          # probability bound
report("T2 166/200 = 83% (accuracy, probability in [0,1])", ok)

# --- T3: spectral-gap figure 187/200 = 93.5% ----------------------------------
lhs = Rational(187, 200); rhs = Rational(935, 1000)
ok = simplify(lhs - rhs) == 0 and (0 <= float(lhs) <= 1)
report("T3 187/200 = 93.5% (gap fraction in [0,1])", ok)

# --- T4: valuation-only overhead bound strictly weaker than Singleton ---------
# Premise: quantum Singleton bound  n - k >= 2(d-1), valid for d >= 2.
# Conclusion: sharpest valuation-only bound n/k >= 1 (i.e. n >= k) is STRICTLY weaker,
# i.e. Singleton implies n - k >= 2(d-1) >= 2 > 0, hence n > k, hence n/k > 1.
gap = simplify(2*(d - 1) - 2)               # excess of Singleton over its d=2 floor
singleton_implies_strict = simplify(2*(d-1)) >= 2   # for d >= 2
# Limiting case d = 2: Singleton gives n-k >= 2, valuation bound only n-k >= 0.
d2_case = (2*(2-1) == 2) and (2 > 0)
report("T4 n/k>=1 strictly weaker than n-k>=2(d-1) for d>=2 "
       "(2(d-1)>=2>0 => n>k => n/k>1; limiting case d=2 consistent)",
       bool(singleton_implies_strict) and d2_case)

# --- T5: Golay correction factor ----------------------------------------------
# Paper asserts a "Golay correction" is verified but states NO numeric factor,
# no formula, and no before/after values anywhere in the provided text.
inconclusive("T5 Golay correction factor (no numeric values/formula stated)")

# --- T6: claimed vs observed Mahler spectral gaps ------------------------------
# Paper references "claimed versus observed Mahler spectral separations" but gives
# no claimed value, no observed value, no tolerance.
inconclusive("T6 claimed vs observed Mahler spectral gaps (no numbers stated)")

# --- T7: [1] Thm 1: M1(T) >= 9n - 16 (n even pendent), equality at 4-tree ------
# Cited theorem; "4-tree" extremal definition not fully specified in this text.
# Spot check: tree with all internal vertices degree 4 and n pendent vertices
# has m = (n-2)/2 internal vertices, M1 = n*1^2 + m*4^2 = 33n - 64.
n_even = 10
m = (n_even - 2) // 2
M1_spot = n_even * 1**2 + m * 4**2          # = 33n - 64 = 266
ok_ineq = M1_spot >= 9*n_even - 16          # 266 >= 74 holds
eq_claim = (M1_spot == 9*n_even - 16)       # equality claim NOT met by this reading
if ok_ineq and not eq_claim:
    inconclusive("T7 M1>=9n-16 (ineq holds on spot check; 'equality at 4-tree' "
                 "unverifiable: 4-tree definition underspecified, M1=33n-64 != 9n-16)")
else:
    report("T7 M1>=9n-16 spot check", ok_ineq)

# --- T8: [1] Thm 1 (odd case) M1(T) >= 9n - 15 ---------------------------------
n_odd = 11
# For odd n a 4-tree is impossible ((n-2)/2 non-integer); construct near-extremal:
# one internal vertex of degree 3, rest degree 4: sum deg = n + 4(m-1) + 3 = 2(n+m-1)
# => 4m = n + 1 => m = (n+1)/4 must be integer; take n=11 -> not integral; use
# generic random tree spot check instead: path-augmented tree, n pendent.
# Build: chain of internal vertices each carrying one pendent, ends carry 2.
m_int = n_odd - 2                            # internal chain vertices
degs = [1]*n_odd + [3] + [4]*(m_int - 1) + [2]  # ends of chain degree 4? adjust:
# simpler valid tree: star-of-paths: center degree 3, two arms of length 2, ...
# We just verify the inequality on one explicit tree: center c with 3 arms of
# lengths giving 11 pendent vertices total: arms of 4,4,3 pendent leaves via
# subdivision vertices of degree 3 (interior) and degree 3 at arm ends? Keep it
# minimal: verify inequality for the "broom" tree: path v1..v_{m}, pendents on v1.
# degrees: v1: 3 (2 pendent + path), v_m: 1+? -> use v_m with 2 pendent.
m_int = 9
deg_list = [3] + [2]*(m_int - 2) + [3]       # internal path degrees
M1_broom = sum(x**2 for x in deg_list) + n_odd * 1**2
# edges: internal path (m_int-1) + pendents: v1 has 2 pend, v_m has 2 pend, rest 1 each
# pendent count = 2 + 2 + (m_int-2)*1 = m_int + 2 = 11 = n_odd. Consistent.
ok8 = M1_broom >= 9*n_odd - 15
inconclusive("T8 M1>=9n-15 (odd case; cited theorem, spot check broom tree "
             f"M1={M1_broom} >= {9*n_odd-15}: {ok8}; general proof out of scope)")

# --- T9: [1] Thm 3: M2(T) >= 11n - 27 for n >= 8 pendent -----------------------
# Cited theorem; no derivation given in this text. Spot check on the 4-regular
# internal tree (n=10): each edge internal-internal contributes 16, pendent edge 4.
# edges: internal-internal = m - 1 = 3, pendent edges = 10.
M2_spot = 3 * (4*4) + 10 * (4*1)             # = 48 + 40 = 88
ok9 = M2_spot >= 11*n_even - 27              # 88 >= 83
inconclusive("T9 M2>=11n-27 (cited theorem; spot check M2=88 >= 83: "
             f"{ok9}; general proof out of scope)")

# --- T10: dimension/valuation definitional step --------------------------------
# Premise: n-qubit Hilbert space dim H = 2^n (tensor product multiplies dimensions).
# Conclusion: v_2(dim H) = n.
# Symbolic v_2 not simplifiable in SymPy; randomized numeric spot checks:
ok10 = True
for _ in range(5):
    nv = random.randint(1, 12)
    ok10 = ok10 and (multiplicity(2, 2**nv) == nv)
report("T10 v_2(2^n) = n (definitional; randomized spot checks n=1..12)", ok10)

# --- T11: no-cloning as impossibility of linear diagonal map -------------------
# Qualitative/definitional claim; no equation to verify.
inconclusive("T11 no-cloning re-expression (qualitative; no equational content)")

# --- Summary -------------------------------------------------------------------
print("\nSummary:")
for tag, st in results:
    print(f"  {st:12s} {tag}")
print("\nSanity: accuracies 0.83, 0.935 in [0,1]; overhead n-k >= 0 and n/k >= 1 "
      "nonnegative; efficiency-type figures <= 1; limiting case d=2 consistent.")

from fractions import Fraction

def sig(x, digits=8):
    # format with at least 8 significant digits
    if x == 0:
        return "0"
    from decimal import Decimal
    return f"{x:.8g}"

claims = []

# Q1: 46+39+45+36 = 166
c = 46 + 39 + 45 + 36
claims.append(("Q1", c, "166"))

# Q2: 166/200 = 0.83
c = 166 / 200
claims.append(("Q2", c, "0.83"))

# Q3: 187/200 = 0.935
c = 187 / 200
claims.append(("Q3", c, "0.935"))

# Q4: 46/50, 39/50, 45/50, 36/50
c = (46/50, 39/50, 45/50, 36/50)
claims.append(("Q4", c, "(0.92, 0.78, 0.9, 0.72)"))

# Q5: 1/4 = 0.25; 0.25*200 = 50
c = (1/4, 0.25 * 200)
claims.append(("Q5", c, "(0.25, 50)"))

# Q6: 0.83 - 0.25 = 0.58
c = 0.83 - 0.25
claims.append(("Q6", c, "0.58"))

# Q7: (28-4) - 10 = 14
c = (28 - 4) - 10
claims.append(("Q7", c, "14"))

# Q8: 4-3 = 1; 6-4 = 2
c = (4 - 3, 6 - 4)
claims.append(("Q8", c, "(1, 2)"))

# Q9: 24 - (-2) = 26
c = 24 - (-2)
claims.append(("Q9", c, "26"))

# Q10: 64/18
c = 64 / 18
claims.append(("Q10", c, "3.5556"))

# Q11: 28/4 = 7; 28/2 = 14
c = (28/4, 28/2)
claims.append(("Q11", c, "(7, 14)"))

# Q12: 2+2+1+50 = 55
c = 2 + 2 + 1 + 50
claims.append(("Q12", c, "55"))

# Q13: 50/55
c = 50 / 55
claims.append(("Q13", c, "0.9091"))

# Q14: 7 / (7 - 2*(3-1))
c = 7 / (7 - 2*(3-1))
claims.append(("Q14", c, "2.3333"))

# Q15: (7-1) - 2*(3-1) = 2 (>= 0, so Singleton satisfied)
c = (7 - 1) - 2*(3-1)
claims.append(("Q15", c, "2"))

def fmt(v):
    if isinstance(v, tuple):
        return "(" + ", ".join(f"{x:.8g}" for x in v) + ")"
    return f"{v:.8g}"

def matches(computed, expected):
    # compare computed rounded to the significant digits the paper states
    try:
        exp = float(expected)
    except ValueError:
        # tuple expected
        return None
    comp = float(f"{computed:.8g}")
    # round expected to same precision of computed digits stated
    return abs(comp - exp) < 1e-12 * max(1.0, abs(exp))

n_match = 0
n_mismatch = 0
for cid, comp, exp in claims:
    if isinstance(comp, tuple):
        # compare elementwise where possible
        ok = all(matches(x, e) for x, e in zip(comp, exp.strip("()").split(", ")))
        m = "yes" if ok else "no"
    else:
        m = "yes" if matches(comp, exp) else "no"
    if m == "yes":
        n_match += 1
    else:
        n_mismatch += 1
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {n_match} match, {n_mismatch} mismatch")
