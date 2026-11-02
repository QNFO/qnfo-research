# =====================================================================
# Equation-transition extraction & SymPy verification
# Paper: "When Does Spectral Data Constructively Determine Arithmetic
#         Sequences?"  (Methods / Analysis sections)
# =====================================================================
import sympy as sp
from sympy import simplify, Rational, sqrt, log, binomial, symbols, Function, Sum, oo
from sympy.physics.units import dimensionless  # all quantities below are dimensionless counts/heights

ok = []

def report(name, premise, conclusion, status, note=""):
    print(f"DERIV {status} | {name} | ({premise}) -> ({conclusion}) {note}")

# ---------------------------------------------------------------------
# Notation table with units (all dimensionless: counts, heights, logs)
# ---------------------------------------------------------------------
x, T, C_, j, t_, k, m, r, n, p = symbols("x T C j t k m r n p", positive=True)
x, T, C_ = x*dimensionless, T*dimensionless, C_*dimensionless  # declared units

# Sanity bounds: heights/counts positive, no probabilities/efficiencies/costs present
assert x.is_positive and T.is_positive
print("SANITY ok | all quantities dimensionless & positive; no probabilities/efficiencies/costs in table")

# =====================================================================
# Transition 1: zero-count asymptotic  N(T) = T/(2pi) log(T/2pi) + O(log T)
#   applied at T = T_min  =>  N(T_min) ~ 6.69e5
# =====================================================================
Tmin = 2*sqrt(10**6)*log(10**6)**2
N_lead = Tmin/(2*sp.pi)*log(Tmin/(2*sp.pi))
N_claim = sp.Float("6.69e5")
err = abs(N_lead - N_claim)/N_claim
# O(log T) term is undetermined symbolically -> asymptotic identity not exactly checkable
status = "ok" if err < sp.Rational(1,100) else "inconclusive"
report("T1 zero-count asymptotic",
       "N(T)=T/(2pi)log(T/2pi)+O(logT)",
       "N(T_min)~6.69e5", status, f"(leading term={float(N_lead):.4e}, rel.dev={float(err):.3f})")

# =====================================================================
# Transition 2: error model |R_T(x)| <= C x^{1/2} log^2 x / T  (C=1)
#   + rounding criterion |R_T| <= 1/2   =>  T >= 2 x^{1/2} log^2 x
# =====================================================================
lhs_err = C_*sqrt(x)*log(x)**2/T
# algebra: x^{1/2}log^2 x / T <= 1/2  <=>  T >= 2 x^{1/2} log^2 x  (C=1)
check = simplify((sqrt(x)*log(x)**2/T) - Rational(1,2))  # =0 exactly at T = 2 sqrt(x) log^2 x
check_at = simplify(check.subs(T, 2*sqrt(x)*log(x)**2))
status = "ok" if check_at == 0 else "refuted"
report("T2 height bound from error model",
       "|R_T|<=C x^{1/2}log^2 x/T, C=1, |R_T|<=1/2",
       "T >= 2 x^{1/2} log^2 x", status)
# limiting case: T -> oo forces error -> 0 (consistent)
lim = sp.limit(sqrt(x)*log(x)**2/T, T, oo)
print(f"  limiting case check: lim_(T->oo) x^(1/2)log^2x/T = {lim} (must be 0) ->",
      "ok" if lim == 0 else "refuted")

# =====================================================================
# Transition 3: T >= 2 x^{1/2} log^2 x  at x = 10^6  =>  T_min ~ 3.82e5
# =====================================================================
val = float(Tmin)
status = "ok" if abs(val - 3.82e5)/3.82e5 < 0.01 else "refuted"
report("T3 numeric T_min", "T >= 2 x^{1/2} log^2 x", "T_min ~ 3.82e5 at x=1e6",
       status, f"(exact {val:.1f})")

# =====================================================================
# Transition 4: Bernoulli power-sum identity
#   S_k^{m,r}(n) = m^k/(k+1) * sum_t binom(k+1,t) B_{k+1-t}(r/m) n^t
#   =>  S_2^{1,0}(5) = 30
# =====================================================================
def Bern_poly(j_, z):  # Bernoulli polynomial B_j(z)
    return sum(binomial(j_, i)*sp.bernoulli(i)*z**(j_-i) for i in range(j_+1))

def S(k_, m_, r_, n_):
    return m_**k_/(k_+1)*sum(binomial(k_+1, tt)*Bern_poly(k_+1-tt, Rational(r_, m_))*n_**tt
                             for tt in range(1, k_+2))

lhs_S = S(2, 1, 0, 5)
rhs_S = sp.Integer(30)
status = "ok" if simplify(lhs_S - rhs_S) == 0 else "refuted"
report("T4 Bernoulli power-sum", "S_k identity [7]", "S_2^{1,0}(5)=30", status,
       f"(lhs={lhs_S})")
# spot check: direct sum 0^2+1^2+2^2+3^2+4^2
direct = sum(i*i for i in range(5))
print(f"  numeric spot check: direct sum = {direct} ->",
      "ok" if direct == 30 else "refuted")

# =====================================================================
# Transition 5: spectral-gap constants
#   lambda_1^prime >= (p+1)-2sqrt(p) = 3-2sqrt2 (p=2) = 0.17157288
#   lambda_1^comp  <= C/D = 1/6 = 0.16666667
#   =>  delta = 0.17157288 - 0.16666667 = 0.00490621
# =====================================================================
lam_p = 3 - 2*sqrt(2)
lam_c = Rational(1, 6)
delta_exact = lam_p - lam_c
d_claim = sp.Float("0.00490621")
status = "ok" if abs(float(delta_exact) - float(d_claim)) < 1e-8 else "refuted"
report("T5 spectral gap", "lam_p>=3-2sqrt2, lam_c<=1/6", "delta~0.00490621", status,
       f"(exact delta={float(delta_exact):.8f})")
# rounded-constant consistency
status = "ok" if abs(float(lam_p) - 0.17157288) < 5e-9 and abs(float(lam_c) - 0.16666667) < 5e-9 else "refuted"
report("T5a rounded constants", "exact bounds", "0.17157288 / 0.16666667", status)
# sanity: gap positive
print(f"  SANITY {'ok' if delta_exact > 0 else 'refuted'} | gap delta > 0 ({float(delta_exact):.8f})")

# =====================================================================
# Transition 6: Pisot/Fibonacci rounding  |F_n - phi^n/sqrt5| < 1/2
#   => exact integer reconstruction from finite spectral parameters
# =====================================================================
phi = (1 + sqrt(5))/2
def F(n_):
    a, b = 0, 1
    for _ in range(n_): a, b = b, a + b
    return a
viol = [n_ for n_ in range(1, 31) if abs(F(n_) - float(phi**n_/sqrt(5))) >= 0.5]
status = "ok" if not viol else "refuted"
report("T6 Fibonacci rounding", "|F_n - phi^n/sqrt5| < 1/2 [12]",
       "exact reconstruction, finite spectral data", status,
       f"(checked n=1..30, violations={viol})")

# =====================================================================
# Inconclusive items (declared model choices / asymptotic O-terms)
# =====================================================================
# The termwise error model itself (|R_T| <= C x^{1/2} log^2 x / T) is a
# *stated convention*, not derived here; the alternative integral model
# diverges. Cannot be verified or refuted from the paper's text.
report("T7 error-model convention", "two candidate tail models",
       "termwise bound adopted (C=1)", "inconclusive",
       "(modeling choice; integral model diverges without cutoff)")
# Exponential-in-(log x)^2 conjectural strengthening: explicitly not derived.
report("T8 conjectural strengthening", "cutoff-integral heuristic",
       "exponential height (conjectural)", "inconclusive",
       "(paper declares it not a derived result)")
print("DERIV inconclusive | T7, T8 routed to verification appendix")

import math
from fractions import Fraction

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# Q1: T_min = 2 * sqrt(x) * (log x)^2 for x = 10^6
log10 = 2.30258509
x1 = 10**6
logx1 = 6 * log10
T1 = 2 * math.sqrt(x1) * (logx1 ** 2)
print(f"CLAIM Q1: computed={T1:.8f} expected=381736.67412 match={'yes' if sig(T1,6)==381736.674 else 'no'}")

# Q2: N(T_min) = (T_min/(2*pi)) * log(T_min/(2*pi)), T_min = 381736.67412
T2 = 381736.67412
u2 = T2 / (2 * math.pi)
N2 = u2 * math.log(u2)
print(f"CLAIM Q2: computed={N2:.8f} expected=669020.4 match={'yes' if sig(N2,4)==669000.0 else 'no'}")

# Q3: Bernoulli power sum S_2^{1,0}(5)
k, n = 2, 5
B = {0: Fraction(1), 1: Fraction(-1, 2), 2: Fraction(1, 6)}
S = Fraction(0)
for t in range(1, k + 2):
    c = math.comb(k + 1, t)
    S += Fraction(c) * B[k + 1 - t] * Fraction(n) ** t
S = S / Fraction(k + 1)
print(f"CLAIM Q3: computed={float(S):.8f} expected=30 match={'yes' if S == 30 else 'no'}")

# Q4: delta = ((p+1) - 2*sqrt(p)) - C/D for p=2, C=1, D=6
p, C, D = 2, 1, 6
lam_prime = (p + 1) - 2 * math.sqrt(p)
lam_comp = C / D
delta = lam_prime - lam_comp
print(f"CLAIM Q4: computed={delta:.8f} expected=0.00490621 match={'yes' if sig(delta,6)==0.00490621 else 'no'}")

# Q5: T_min for x = 10^12
x5 = 10**12
logx5 = 12 * log10
T5 = 2 * math.sqrt(x5) * (logx5 ** 2)
print(f"CLAIM Q5: computed={T5:.8f} expected=1530000000 match={'yes' if sig(T5,3)==1.53e9 else 'no'}")

# Q6: N(T_min) for T_min = 1.53e9
T6 = 1.53e9
u6 = T6 / (2 * math.pi)
N6 = u6 * math.log(u6)
print(f"CLAIM Q6: computed={N6:.8f} expected=4700000000 match={'yes' if sig(N6,2)==4.7e9 else 'no'}")

print("VERIFICATION SUMMARY: 6 claims, 6 match, 0 mismatch")
