# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Electron rest energy E0 = 8.1871058e-14 J",
    "inputs": "m_e = 9.1093837e-31 kg; c = 2.99792458e8 m/s",
    "formula": "E0 = m_e * c^2"
  },
  {
    "id": "Q2",
    "statement": "ZBW angular frequency omega_ZBW = 1.55268e21 rad/s",
    "inputs": "E0 = 8.1871058e-14 J; hbar = 1.054571817e-34 J s",
    "formula": "omega_ZBW = 2*E0/hbar"
  },
  {
    "id": "Q3",
    "statement": "ZBW ordinary frequency f_ZBW = 2.4712e20 Hz",
    "inputs": "omega_ZBW = 1.55268e21 rad/s",
    "formula": "f_ZBW = omega_ZBW/(2*pi)"
  },
  {
    "id": "Q4",
    "statement": "ZBW period T_ZBW = 4.047e-21 s",
    "inputs": "f_ZBW = 2.4712e20 Hz",
    "formula": "T_ZBW = 1/f_ZBW"
  },
  {
    "id": "Q5",
    "statement": "Reduced Compton wavelength lambda_C = 3.8616e-13 m",
    "inputs": "hbar = 1.054571817e-34 J s; m_e = 9.1093837e-31 kg; c = 2.99792458e8 m/s",
    "formula": "lambda_C = hbar/(m_e*c)"
  },
  {
    "id": "Q6",
    "statement": "Momentum spread at Compton localization Delta_p = 1.3654e-22 kg m/s",
    "inputs": "hbar = 1.054571817e-34 J s; lambda_C = 3.8616e-13 m",
    "formula": "Delta_p = hbar/(2*lambda_C)"
  },
  {
    "id": "Q7",
    "statement": "Weak-coupling relative frequency shift 2e-6 for |g| = 1e-3*Delta_E",
    "inputs": "|g|/Delta_E = 1e-3",
    "formula": "sqrt(1+4*(|g|/Delta_E)^2)-1 = sqrt(1+4e-6)-1"
  },
  {
    "id": "Q8",
    "statement": "Absolute frequency shift delta_omega = 3.11e15 rad/s",
    "inputs": "omega_ZBW = 1.55268e21 rad/s; relative shift = 2e-6",
    "formula": "delta_omega = 2e-6 * omega_ZBW"
  },
  {
    "id": "Q9",
    "statement": "Population modulation depth A_pop = 4.0e-6 for |g| = 1e-3*Delta_E",
    "inputs": "|g|/Delta_E = 1e-3",
    "formula": "A_pop = 4*(|g|/Delta_E)^2/(1+4*(|g|/Delta_E)^2)"
  },
  {
    "id": "Q10",
    "statement": "Vertex count at distance n=4 in 3-regular tree N(4) = 24",
    "inputs": "n = 4",
    "formula": "N(n) = 3*2^(n-1)"
  },
  {
    "id": "Q11",
    "statement": "Projected amplitude A_pop(10) = 3.81e-12",
    "inputs": "A0 = 4e-6; n = 10",
    "formula": "A_pop(n) = A0*4^(-n)"
  },
  {
    "id": "Q12",
    "statement": "Delocalization measure D2(10) = 9.77e-4",
    "inputs": "n = 10",
    "formula": "D2(n) = 2^(-n)"
  },
  {
    "id": "Q13",
    "statement": "Shot-noise floor 1e-3 at N = 1e6 shots",
    "inputs": "N = 1e6",
    "formula": "1/sqrt(N)"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 7, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: E0 = m_e·c^2. c^2 = (2.99792458e8)^2 = 8.987551787e16 m^2/s^2. E0 = 9.1093837e-31 × 8.987551787e16 = (9.1093837 × 8.987551787) × 10^-15. 9.1093837 × 8.987551787: 9 × 8.987551787 = 80.887966083; 0.1093837 × 8.987551787 = 0.983091669 (0.898755179 + 0.084336490). Sum = 81.871057752. E0 = 8.1871057752e-14 J.
CLAIM Q1: computed=8.1871057752e-14 expected=8.1871058e-14 match=yes

Q2: omega = 2·E0/hbar = 1.63742116e-13 / 1.054571817e-34 = (1.63742116 / 1.054571817) × 10^21. 1.054571817 × 1.55268 = 1.637412570; remainder 1.63742116 − 1.637412570 = 8.59e-6; 8.59e-6/1.054571817 = 8.147e-6. Ratio = 1.552688147. omega = 1.552688147e21 rad/s.
CLAIM Q2: computed=1.552688147e21 expected=1.55268e21 match=yes

Q3: f = omega/(2π) = 1.552688147e21 / 6.283185307. 6.283185307 × 0.24712 = 1.552700753; overshoot 1.552700753 − 1.552688147 = 1.2606e-5; /6.283185307 = 2.0064e-6. Quotient = 0.247117994. f = 2.47117994e20 Hz.
CLAIM Q3: computed=2.47117994e20 expected=2.4712e20 match=yes

Q4: T = 1/f = 1/2.47117994e20 = (1/2.47117994) × 10^-20. 2.47117994 × 0.40466 = 0.99998... 2.47117994 × 0.4047 = 1.000017; overshoot 1.7e-5 → −6.9e-6 → 0.4046931? Recompute: 2.47117994 × 0.40466 = 0.999998... 2.47117994×0.4 = 0.988471976; ×0.00466 = 0.011515699. Sum = 0.999987675. Remainder 1.2325e-5 → /2.47118 = 4.986e-6. Quotient = 0.404664986. T = 4.04664986e-21 s.
CLAIM Q4: computed=4.04664986e-21 expected=4.047e-21 match=yes

Q5: m_e·c = 9.1093837e-31 × 2.99792458e8 = (9.1093837 × 2.99792458) × 10^-22. 9 × 2.99792458 = 26.98132122; 0.1093837 × 2.99792458 = 0.327924086 (0.299792458 + 0.028131628). Sum = 27.309245306. m_e·c = 2.7309245306e-22. lambda = 1.054571817e-34 / 2.7309245306e-22 = (1.054571817/2.7309245306) × 10^-12. 2.7309245306 × 0.38616 = 1.054574... 2.7309245306×0.386 = 1.054136869; ×0.00016 = 0.000436948. Sum = 1.054573817. Overshoot 2.0e-6 → /2.73092 = 7.3e-7. Quotient = 0.38615927. lambda = 3.8615927e-13 m.
CLAIM Q5: computed=3.8615927e-13 expected=3.8616e-13 match=yes

Q6: Delta_p = hbar/(2·lambda_C) = 1.054571817e-34 / (2 × 3.8616e-13) = 1.054571817e-34 / 7.7232e-13 = (1.054571817/7.7232) × 10^-21. 7.7232 × 0.13654 = 1.054526... 7.7232×0.1365 = 1.0542168; ×0.00004 = 0.000308928. Sum = 1.054525728. Remainder 4.6089e-5 → /7.7232 = 5.966e-6. Quotient = 0.136545966. Delta_p = 1.36545966e-22 kg m/s (paper truncates to 1.3654e-22).
CLAIM Q6: computed=1.36545966e-22 expected=1.3654e-22 match=yes

Q7: sqrt(1+4e-6) − 1. sqrt(1+x) ≈ 1 + x/2 − x^2/8 = 1 + 2e-6 − 2e-12. Shift = 1.999998e-6.
CLAIM Q7: computed=1.999998e-06 expected=2e-6 match=yes

Q8: delta_omega = 2e-6 × 1.55268e21 = 3.10536e15 rad/s.
CLAIM Q8: computed=3.10536e15 expected=3.11e15 match=yes

Q9: A_pop = 4e-6/(1+4e-6) = 4e-6 × (1 − 4e-6 + ...) = 3.999984e-6.
CLAIM Q9: computed=3.999984e-06 expected=4.0e-6 match=yes

Q10: N(4) = 3 × 2^(4−1) = 3 × 8 = 24.
CLAIM Q10: computed=24 expected=24 match=yes

Q11: A_pop(10) = 4e-6 × 4^-10 = 4e-6 / 1048576 = 3.8146973e-12.
CLAIM Q11: computed=3.8146973e-12 expected=3.81e-12 match=yes

Q12: D2(10) = 2^-10 = 1/1024 = 9.765625e-4.
CLAIM Q12: computed=9.765625e-04 expected=9.77e-4 match=yes

Q13: 1/sqrt(1e6) = 1/1000 = 1e-3.
CLAIM Q13: computed=1e-03 expected=1e-3 match=yes

VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8.1871057752e-14 | 8.1871058e-14 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q2 | 1.552688147e21 | 1.55268e21 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 2.47117994e20 | 2.4712e20 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 4.04664986e-21 | 4.047e-21 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 3.8615927e-13 | 3.8616e-13 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 1.36545966e-22 | 1.3654e-22 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 1.999998e-06 | 2e-6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 3.10536e15 | 3.11e15 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 3.999984e-06 | 4.0e-6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 3.8146973e-12 | 3.81e-12 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 9.765625e-04 | 9.77e-4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 1e-03 | 1e-3 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
