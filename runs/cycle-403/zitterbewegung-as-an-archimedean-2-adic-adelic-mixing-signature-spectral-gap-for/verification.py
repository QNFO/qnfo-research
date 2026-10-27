# NOTE: The provided paper text is truncated mid-Section 2 (Background). Sections 3, 4, and 7
# (the full Methods/Analysis derivations) are NOT present in the supplied text. Only the
# transitions stated explicitly in the Abstract/Introduction can be extracted and checked.
# Transitions whose full derivation lives in the missing sections are emitted as
# DERIV inconclusive and routed to the verification appendix.

import sympy as sp
from sympy import simplify, sqrt, Abs, Rational, symbols, S
from sympy.physics.units import (
    meter, kilogram, second, radian, joule, speed_of_light,
    hbar as hbar_unit, Quantity, convert_to
)
import random

# ------------------------------------------------------------------
# Notation table with units (declared quantities)
# ------------------------------------------------------------------
m_e   = Quantity('m_e')      # electron mass
c     = Quantity('c')        # speed of light
hbar  = Quantity('hbar')     # reduced Planck constant
dE    = Quantity('Delta_E')  # spectral gap
g     = Quantity('g')        # coupling amplitude
Omega = Quantity('Omega')    # two-level oscillation angular frequency
omega = Quantity('omega')    # ZBW angular frequency
lam   = Quantity('lambda')   # reduced Compton wavelength
n     = symbols('n', integer=True, nonnegative=True)

# Numeric constants (CODATA)
m_e_val    = sp.Float('9.1093837015e-31') * kilogram
c_val      = sp.Float('299792458') * meter / second
hbar_val   = sp.Float('1.054571817e-34') * joule * second
claimed_omega = sp.Float('1.55268e21') * radian / second
claimed_lam   = sp.Float('3.8616e-13') * meter

# Sanity-bound helpers
def in_range(x, lo, hi): return lo <= x <= hi

# ------------------------------------------------------------------
# T1: Two-level coupled spectrum -> Omega = sqrt(dE^2 + 4|g|^2)/hbar
#     and Omega >= dE/hbar (spectral-gap proposition, Sec. 3)
# ------------------------------------------------------------------
dE_s, g_s = symbols('DeltaE g', positive=True, real=True)
lhs_T1 = sqrt(dE_s**2 + 4*g_s**2)
rhs_T1 = dE_s
diff_T1 = simplify(lhs_T1 - rhs_T1)          # >= 0 required, not == 0
# inequality check: sqrt(dE^2+4g^2) >= dE  <=>  4g^2 >= 0
T1_ineq = simplify((lhs_T1**2 - rhs_T1**2)) == 4*g_s**2 and g_s**2 >= 0
# equality only when g = 0 (limiting case)
T1_limit = simplify(lhs_T1.subs(g_s, 0) - rhs_T1) == 0
print("DERIV", "ok" if (T1_ineq and T1_limit) else "refuted",
      "| T1: Omega = sqrt(dE^2+4|g|^2)/hbar >= dE/hbar (spectral-gap proposition)")

# ------------------------------------------------------------------
# T2: omega_ZBW = 2 m c^2 / hbar = 1.55268e21 rad/s (numeric anchor)
# ------------------------------------------------------------------
omega_expr = 2 * m_e_val * c_val**2 / hbar_val
omega_si = convert_to(omega_expr, radian/second)
rel_err = Abs(omega_si / (radian/second) - sp.Float('1.55268e21')) / sp.Float('1.55268e21')
T2 = rel_err < sp.Rational(1, 10000)   # 5 significant figures claimed
print("DERIV", "ok" if T2 else "refuted",
      "| T2: omega_ZBW = 2 m_e c^2 / hbar = 1.55268e21 rad/s"
      f" (computed {float(omega_si/(radian/second)):.6e}, rel.err {float(rel_err):.2e})")

# ------------------------------------------------------------------
# T3: reduced Compton wavelength hbar/(m c) = 3.8616e-13 m
# ------------------------------------------------------------------
lam_expr = hbar_val / (m_e_val * c_val)
lam_si = convert_to(lam_expr, meter)
rel_err3 = Abs(lam_si / meter - sp.Float('3.8616e-13')) / sp.Float('3.8616e-13')
T3 = rel_err3 < sp.Rational(1, 10000)
# consistency with T2: omega * lam = 2c  (limiting/consistency case)
T3_cons = simplify(
    sp.Float(omega_si/(radian/second)) * sp.Float(lam_si/meter) - 2*299792458
) / (2*299792458) < sp.Rational(1, 1000)
print("DERIV", "ok" if (T3 and T3_cons) else "refuted",
      "| T3: lambda_C = hbar/(m_e c) = 3.8616e-13 m"
      f" (computed {float(lam_si/meter):.6e}, rel.err {float(rel_err3):.2e}; omega*lam=2c checked)")

# ------------------------------------------------------------------
# T4: 2-adic ball measure mu_2(2^n Z_2) = 2^{-n}  (Haar measure, definitional)
# ------------------------------------------------------------------
mu2 = lambda k: Rational(1, 2)**k
T4 = all(simplify(mu2(k) - Rational(1, 2)**k) == 0 for k in range(8))
# sanity: probabilities in [0,1]; limiting case mu_2(Z_2)=1
T4_bounds = all(in_range(float(mu2(k)), 0, 1) for k in range(8)) and mu2(0) == 1
print("DERIV", "ok" if (T4 and T4_bounds) else "refuted",
      "| T4: mu_2(2^n Z_2) = 2^{-n} (Haar measure of dyadic balls; mu_2(Z_2)=1 limit)")

# ------------------------------------------------------------------
# T5: Projected factor-of-4 amplitude suppression per confinement step
#     (regression of ZBW amplitude against mu_2(2^n Z_2) = 2^{-n})
#     Full derivation is in Section 7, NOT included in supplied text.
#     If amplitude A(n) ∝ mu_2(n)^2 = 4^{-n}, factor 4/step; if A ∝ mu_2, factor 2/step.
#     Cannot be decided from the provided excerpt -> inconclusive.
# ------------------------------------------------------------------
A = sp.Function('A')
ratio_hyp = simplify(A(n+1)/A(n) - Rational(1, 4))   # hypothesized form, unverified
print("DERIV inconclusive | T5: factor-of-4 suppression per confinement step "
      "(requires Section 7 regression model A(n) vs mu_2 = 2^{-n}; excerpt truncated)")

# ------------------------------------------------------------------
# T6: omega = 2E/hbar as the general gap statement with dE = 2 m c^2
#     (Intro: "Compton-scale oscillation at omega = 2E/hbar")
#     Consistency with T2: setting E = m c^2 gives omega = 2 m c^2 / hbar.
# ------------------------------------------------------------------
E_s = symbols('E', positive=True)
lhs_T6 = 2*E_s/hbar_val
T6 = simplify(convert_to(lhs_T6.subs(E_s, m_e_val*c_val**2), radian/second)
              / (radian/second) - sp.Float(omega_si/(radian/second))) == 0
print("DERIV", "ok" if T6 else "refuted",
      "| T6: omega = 2E/hbar with E = m c^2 reproduces omega_ZBW = 2 m c^2 / hbar")

# ------------------------------------------------------------------
# T7: Structural selection p=2: Bruhat-Tits tree of Q_p is (p+1)-regular,
#     so p=2 gives degree 3, smallest among primes.
#     Arithmetic check only (degree formula), minimality over primes.
# ------------------------------------------------------------------
p = symbols('p', integer=True, positive=True)
deg = p + 1
T7 = min(deg.subs(p, q) for q in [2, 3, 5, 7, 11, 13]) == 3
print("DERIV", "ok" if T7 else "refuted",
      "| T7: degree(p) = p+1 minimized at p=2 giving 3 (arithmetic part; "
      "the physical 'dynamical role of 2' claim is interpretive, not derivable here)")

# ------------------------------------------------------------------
# Randomized numeric spot checks for T1 (two-level frequency formula)
# ------------------------------------------------------------------
random.seed(0)
T1_num_ok = True
for _ in range(200):
    dv = random.uniform(0, 10); gv = random.uniform(0, 10)
    Om = (dv**2 + 4*gv**2)**0.5
    if not (Om >= dv - 1e-12 and abs(Om - (dv**2 + 4*gv**2)**0.5) < 1e-9):
        T1_num_ok = False; break
print("DERIV", "ok" if T1_num_ok else "refuted",
      "| T1 numeric spot checks: Omega = sqrt(dE^2+4|g|^2) >= dE over 200 random draws")

# ------------------------------------------------------------------
# Summary of sanity bounds
# ------------------------------------------------------------------
print("# sanity: mu_2 values in [0,1]:", T4_bounds,
      "| efficiencies/couplings nonneg (g_s positive):", g_s.is_positive,
      "| costs: none declared in excerpt")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    d = math.floor(math.log10(abs(x)))
    return round(x, n - 1 - d)

results = []

# Q1: E0 = m_e * c^2
m_e = 9.1093837e-31
c = 2.99792458e8
E0 = m_e * c**2
results.append(("Q1", E0, "8.1871058e-14"))

# Q2: omega_ZBW = 2*E0/hbar
hbar = 1.054571817e-34
omega = 2 * E0 / hbar
results.append(("Q2", omega, "1.55268e21"))

# Q3: f_ZBW = omega/(2*pi)
f = omega / (2 * math.pi)
results.append(("Q3", f, "2.4712e20"))

# Q4: T_ZBW = 1/f
T = 1 / f
results.append(("Q4", T, "4.047e-21"))

# Q5: lambda_C = hbar/(m_e*c)
lam = hbar / (m_e * c)
results.append(("Q5", lam, "3.8616e-13"))

# Q6: Delta_p = hbar/(2*lambda_C)
dp = hbar / (2 * lam)
results.append(("Q6", dp, "1.3654e-22"))

# Q7: sqrt(1+4e-6)-1
r = math.sqrt(1 + 4e-6) - 1
results.append(("Q7", r, "2e-6"))

# Q8: delta_omega = 2e-6 * omega
domega = 2e-6 * omega
results.append(("Q8", domega, "3.11e15"))

# Q9: A_pop = 4e-6/(1+4e-6)
apop = 4e-6 / (1 + 4e-6)
results.append(("Q9", apop, "4.0e-6"))

# Q10: N(4) = 3*2^3
N4 = 3 * 2**3
results.append(("Q10", float(N4), "24"))

# Q11: A_pop(10) = 4e-6 * 4^-10
a10 = 4e-6 * 4**(-10)
results.append(("Q11", a10, "3.81e-12"))

# Q12: D2(10) = 2^-10
d10 = 2**(-10)
results.append(("Q12", d10, "9.77e-4"))

# Q13: 1/sqrt(1e6)
sn = 1 / math.sqrt(1e6)
results.append(("Q13", sn, "1e-3"))

match_count = 0
for qid, comp, exp_str in results:
    exp = float(exp_str)
    # significant digits stated in expected
    digits = len(exp_str.split("e")[0].replace(".", "").lstrip("0").rstrip("0")) or 1
    if "." in exp_str.split("e")[0]:
        digits = len(exp_str.split("e")[0].replace(".", "").lstrip("0"))
        if exp_str.split("e")[0].rstrip("0") == "":
            digits = 1
    # count sig digits properly
    mant = exp_str.split("e")[0]
    digits = len(mant.replace(".", "").lstrip("0"))
    if digits == 0:
        digits = 1
    comp_r = sig(comp, digits)
    match = "yes" if abs(comp_r - exp) <= exp * 10**(-digits) * 0.5 + 1e-300 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp:.8e} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")
