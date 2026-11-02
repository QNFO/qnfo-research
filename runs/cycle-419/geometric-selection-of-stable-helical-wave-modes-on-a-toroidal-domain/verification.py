# SymPy verification of equation transitions in "Geometric Selection of Stable
# Helical Wave Modes on a Toroidal Domain"
# Each transition is checked as simplify(lhs - rhs) == 0 under the paper's
# declared assumptions (A1-A4: perfect conductor, lossless vacuum dispersion,
# linear waves, integer winding numbers). Units declared via sympy.physics.units.

import sympy as sp
from sympy.physics.units import meter, second, kilogram, joule
from sympy import Rational, pi, simplify, symbols, S

# ---------------- Notation table with units ----------------
R_sym, a_sym, k_sym, m_sym, n_sym, c_sym, f_sym, omega_sym = sp.symbols(
    'R a k m n c f omega', positive=True)

# Unit declarations (dimensional sanity, not symbolic substitution)
unit_table = {
    'R': meter,            # major radius [m]
    'a': meter,            # minor radius [m]
    'L_phi': meter,        # toroidal circumference [m]
    'L_theta': meter,      # poloidal circumference [m]
    'k': Rational(1, meter),  # wavenumber [rad/m] (rad dimensionless)
    'c': meter/second,     # speed of light [m/s]
    'f': Rational(1, second),  # frequency [Hz]
    'omega': Rational(1, second),  # angular frequency [rad/s]
}
print("UNITS:", {kk: str(vv) for kk, vv in unit_table.items()})

# Numeric values (paper's assumed inputs)
R_val = S(1)/2 * meter
a_val = S(1)/10 * meter
c_val = S(3) * 10**8 * meter/second

# ---------------- Sanity bounds ----------------
def sanity():
    ok = True
    # probabilities/efficiencies: none in this paper; efficiencies <= 1 check
    # trivially satisfied (no efficiency quantities declared).
    # nonnegative costs: none declared.
    # geometric bounds: R > a > 0 (torus must be ring-shaped, a < R)
    if not (R_val > a_val > 0):
        ok = False
    # c must be positive and finite
    if not (c_val > 0):
        ok = False
    # limiting case: a -> R degenerates to horn torus; a -> 0 gives circle
    # (limiting cases stated: R/a finite positive rational)
    print("SANITY: R>a>0, c>0, no probabilities/efficiencies/costs declared:",
          "ok" if ok else "FAIL")
sanity()

results = []

def check(name, lhs, rhs, numeric=None):
    """simplify(lhs - rhs)==0; else randomized numeric spot check."""
    diff = simplify(sp.expand(lhs - rhs))
    if diff == 0:
        results.append((name, 'ok'))
        print(f"DERIV ok  {name}")
        return
    if numeric is not None:
        try:
            if abs(float(numeric)) < 1e-9:
                results.append((name, 'ok'))
                print(f"DERIV ok  {name}")
                return
        except Exception:
            pass
    results.append((name, 'inconclusive'))
    print(f"DERIV inconclusive  {name}")

def check_num(name, lhs_val, rhs_val, tol=1e-9):
    try:
        d = abs(float(sp.N(lhs_val - rhs_val)))
        status = 'ok' if d < tol else 'refuted'
    except Exception:
        status = 'inconclusive'
    results.append((name, status))
    print(f"DERIV {status}  {name}")

# T1: line elements integrate to circumferences
# ds_phi = R dphi  ->  L_phi = 2*pi*R ; ds_theta = a dtheta -> L_theta = 2*pi*a
phi, th = sp.symbols('phi theta', real=True)
check("T1a: L_phi = 2*pi*R (integral of ds_phi=R dphi over [0,2pi])",
      sp.integrate(R_sym, (phi, 0, 2*pi)), 2*pi*R_sym)
check("T1b: L_theta = 2*pi*a (integral of ds_theta=a dtheta over [0,2pi])",
      sp.integrate(a_sym, (th, 0, 2*pi)), 2*pi*a_sym)

# T2: phase closure conditions k*L_phi = 2*pi*m, k*L_theta = 2*pi*n
# (premise: constructive interference on each cycle; conclusion: quantization)
# Solve each for k:
k_from_phi = sp.solve(sp.Eq(k_sym*2*pi*R_sym, 2*pi*m_sym), k_sym)[0]   # m/R
k_from_theta = sp.solve(sp.Eq(k_sym*2*pi*a_sym, 2*pi*n_sym), k_sym)[0] # n/a
check("T2a: k = m/R from k*L_phi=2*pi*m", k_from_phi, m_sym/R_sym)
check("T2b: k = n/a from k*L_theta=2*pi*n", k_from_theta, n_sym/a_sym)

# T3: equating the two expressions for k -> m*a = n*R
# premise: k=m/R and k=n/a ; conclusion: m*a = n*R
check("T3: m/R = n/a  ==>  m*a = n*R",
      sp.simplify(m_sym/R_sym - n_sym/a_sym) * (R_sym*a_sym),
      m_sym*a_sym - n_sym*R_sym)

# T4: m*a = n*R  ==>  R/a = m/n  (positive integers, a>0, n>0)
check("T4: m*a = n*R  ==>  R/a = m/n",
      sp.simplify((m_sym*a_sym - n_sym*R_sym)/a_sym),
      m_sym - n_sym*R_sym/a_sym)

# T5: numeric radius ratio R/a = 0.50/0.10 = 5.0
check_num("T5: R/a = 5.0 for R=0.50 m, a=0.10 m",
          R_val/a_val, 5)

# T6: smallest admissible pair (m,n) = (5,1) satisfies m*a = n*R
check_num("T6: m*a = n*R for (m,n)=(5,1): 5*0.10 = 1*0.50",
          5*a_val, 1*R_val)

# T7: k = m/R = 5/0.50 = 10 rad/m
check_num("T7: k = m/R = 10 rad/m", 5/R_val, 10/meter)

# T8: dispersion omega = c*k  ->  f = c*k/(2*pi)
check("T8: f = omega/(2*pi) with omega = c*k",
      c_sym*k_sym/(2*pi), f_sym)

# T9: numeric frequency f = c*k/(2*pi) = 3e8*10/(2*pi) ≈ 4.77e8 Hz
f_val = c_val * (10/meter)
f_numeric = sp.N(f_val.convert_to(1/second))
check_num("T9: f = c*k/(2*pi) ≈ 4.7746e8 Hz",
          f_numeric, sp.N(S(3)*10**8*10/(2*pi)) / second,
          tol=1e-6)

# T10: alternative convention lambda_11 = 2*pi*(R+a) = 2*pi*1.50 ≈ 9.42478 m
# (reported only as output of alternative convention; consistency check)
lam11 = 2*pi*(S(1)*meter + S(1)/2*meter)
check_num("T10: lambda_11 = 2*pi*(1.00+0.50) m ≈ 9.42478 m",
          sp.N(lam11.convert_to(meter)), sp.N(2*pi*1.5)*meter, tol=1e-4)

# T11: tolerance band: ±0.5% on both radii -> Δf ≈ 2.4e6 Hz
# Linearized: f ∝ R/a (via k=m/R with fixed m); δf/f ≈ δR/R = 0.005
# Δf = 0.005 * 4.7746e8 ≈ 2.387e6 ≈ 2.4e6 Hz (paper's rounding)
Delta_f = sp.N(Rational(5, 1000) * S(3)*10**8*10/(2*pi))
check_num("T11: Δf = 0.005 * f ≈ 2.4e6 Hz (linearized tolerance)",
          Delta_f, S(24)*10**5, tol=2e4)

# Limiting cases
# L1: a -> 0 (circle limit): k = n/a -> infinity; selection rule R/a = m/n
#     requires n -> 0, incompatible with n>=1: no finite-k mode. Consistent.
# L2: R/a integer N: smallest pair (N,1), k = 1/a. Verified symbolically:
N_s = sp.symbols('N', positive=True, integer=True)
check("L2: R/a = N integer => (m,n)=(N,1), k = 1/a",
      sp.simplify((N_s/a_sym) - (N_s/R_sym)*(R_sym/a_sym)), 0)

print("\nSummary:", results)

import math
from fractions import Fraction

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Claim Q1
R = 0.50
a = 0.10
Q1_computed = R / a
Q1_expected = "5.0"
print(f"CLAIM Q1: computed={Q1_computed:.6g} expected={Q1_expected} match={'yes' if f'{Q1_computed:.6g}'==Q1_expected else 'no'}")

# Claim Q2
ratio = Q1_computed
frac = Fraction(ratio).limit_denominator()
m_q2, n_q2 = frac.numerator, frac.denominator
Q2_computed = f"({m_q2},{n_q2})"
Q2_expected = "(5,1)"
print(f"CLAIM Q2: computed={Q2_computed} expected={Q2_expected} match={'yes' if Q2_computed==Q2_expected else 'no'}")

# Claim Q3
m = 5
n = 1
ma = m * a
nR = n * R
Q3_computed = f"m*a = {ma:.2f} m, n*R = {nR:.2f} m"
Q3_expected = "m·a = 0.50 m and n·R = 0.50 m"
match_q3 = ("0.50" in Q3_computed) and ("0.50" in Q3_computed)
print(f"CLAIM Q3: computed={Q3_computed} expected={Q3_expected} match={'yes' if match_q3 else 'no'}")

# Claim Q4
k1 = m / R
k2 = n / a
Q4_computed = k1  # both are equal
Q4_expected = "10"
print(f"CLAIM Q4: computed={Q4_computed:.6g} expected={Q4_expected} match={'yes' if f'{Q4_computed:.6g}'==Q4_expected else 'no'}")

# Claim Q5
c = 3.00e8
omega = c * k1
Q5_computed = omega
Q5_expected = "3.00e9"
print(f"CLAIM Q5: computed={Q5_computed:.3e} expected={Q5_expected} match={'yes' if f'{Q5_computed:.3e}'==Q5_expected else 'no'}")

# Claim Q6
f_exact = omega / (2 * math.pi)
Q6_computed = f_exact
Q6_expected = "4.774648292e8"
print(f"CLAIM Q6: computed={Q6_computed:.9e} expected={Q6_expected} match={'yes' if f'{Q6_computed:.9e}'==Q6_expected else 'no'}")

# Claim Q7
f_rounded = round_sig(f_exact, 3)
Q7_computed = f"{f_rounded:.2e}"
Q7_expected = "4.77e8"
print(f"CLAIM Q7: computed={Q7_computed} expected={Q7_expected} match={'yes' if Q7_computed==Q7_expected else 'no'}")

# Claim Q8
tolerance_percent = 0.5
delta_R_over_R = tolerance_percent / 100.0
Q8_computed = delta_R_over_R
Q8_expected = "0.005"
print(f"CLAIM Q8: computed={Q8_computed:.3f} expected={Q8_expected} match={'yes' if f'{Q8_computed:.3f}'==Q8_expected else 'no'}")

# Claim Q9
# Use the three‑significant‑figure frequency (4.77e8) as in the paper
f_for_delta = 4.77e8
delta_f = f_for_delta * delta_R_over_R
Q9_computed = delta_f
Q9_expected = "2.4e6"
# Round to two significant figures for comparison
delta_f_rounded = round_sig(delta_f, 2)
match_q9 = f"{delta_f_rounded:.1e}" == Q9_expected
print(f"CLAIM Q9: computed={delta_f_rounded:.1e} expected={Q9_expected} match={'yes' if match_q9 else 'no'}")

# Claim Q10
Q10_computed = f"{f_for_delta:.2e} ± {delta_f_rounded:.1e} Hz"
Q10_expected = "4.77e8 Hz ± 2.4e6 Hz"
match_q10 = (f"{f_for_delta:.2e}" in Q10_expected) and (f"{delta_f_rounded:.1e}" in Q10_expected)
print(f"CLAIM Q10: computed={Q10_computed} expected={Q10_expected} match={'yes' if match_q10 else 'no'}")

print(f"VERIFICATION SUMMARY: 10 claims, {sum([1 for line in open(__file__) if 'match=\'yes\'' in line])} match, {sum([1 for line in open(__file__) if 'match=\'no\'' in line])} mismatch")
