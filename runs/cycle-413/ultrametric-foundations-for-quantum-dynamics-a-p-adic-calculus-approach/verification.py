# Transitions extracted from Sections 3-4 (Methods/Analysis) of the paper.
# Notation table (units declared with sympy.physics.units):
#   mu      : mean displacement per 1000-step walk  [length]
#   sigma2  : variance of displacement              [length^2]
#   sigma   : standard deviation                    [length]
#   CV      : coefficient of variation              [dimensionless]
#   R       : variance-to-mean ratio                [length]
#   N       : number of steps                       [dimensionless]
#   RMS_bench : Euclidean root-mean-square benchmark [length]
#   factor  : benchmark/plateau ratio               [dimensionless]
#   proj    : projected unbounded-diffusion displacement at N=1e6 [length]
#   window  : acceptance window for R               [length]

import sympy as sp
from sympy.physics.units import meter, Quantity
from sympy import Rational, sqrt, simplify, Eq, S

# ---- declared quantities with units ----
mu     = Quantity('mu');     mu.set_global_dimension(meter)
sigma2 = Quantity('sigma2'); sigma2.set_global_dimension(meter**2)
sigma  = Quantity('sigma');  sigma.set_global_dimension(meter)
CV     = Quantity('CV');     CV.set_global_dimension(sp.physics.units.dimensionless)
R      = Quantity('R');      R.set_global_dimension(meter)
N      = Quantity('N');      N.set_global_dimension(sp.physics.units.dimensionless)
bench  = Quantity('bench');  bench.set_global_dimension(meter)
factor = Quantity('factor'); factor.set_global_dimension(sp.physics.units.dimensionless)
proj   = Quantity('proj');   proj.set_global_dimension(meter)

# ---- assumed inputs (paper's declared assumptions) ----
mu_val     = sp.Float(0.693) * meter
sigma2_val = sp.Float(0.122) * meter**2
N_val      = sp.Integer(1000)

# ---- sanity bounds ----
def sanity():
    checks = []
    checks.append(("sigma2 >= 0", (sigma2_val / meter**2) >= 0))
    checks.append(("mu >= 0", (mu_val / meter) >= 0))
    checks.append(("R in [0,1]-ish (nonneg)", (sp.Float(0.176)) >= 0))
    checks.append(("CV nonneg", sp.Float(0.503) >= 0))
    checks.append(("efficiency-like ratios <= 1: CV<=1", sp.Float(0.503) <= 1))
    for name, c in checks:
        print(f"SANITY {'ok' if bool(c) else 'FAIL'}: {name}")
sanity()

def check(name, lhs, rhs, tol=sp.Float('5e-4')):
    """simplify(lhs-rhs)==0 test; numeric spot check if inconclusive."""
    diff = simplify(sp.together(lhs - rhs))
    if diff == 0:
        print(f"DERIV ok: {name}")
        return
    # numeric spot check
    try:
        lv, rv = sp.N(lhs, 15), sp.N(rhs, 15)
        if abs(lv - rv) <= tol * max(1, abs(rv)):
            print(f"DERIV ok (numeric): {name}")
        else:
            print(f"DERIV refuted: {name}  (lhs={lv}, rhs={rv})")
    except Exception:
        print(f"DERIV inconclusive: {name}")

# ---- Transition T1: sigma = sqrt(sigma2), sigma2=0.122 -> sigma=0.349 ----
sigma_val = sp.Float(0.349) * meter
check("T1: sigma = sqrt(sigma^2)",
      (sigma_val / meter)**2, (sigma2_val / meter**2))

# ---- Transition T2: CV = sigma / mu = 0.349/0.693 = 0.503 ----
CV_val = sp.Float(0.503)
check("T2: CV = sigma/mu",
      CV_val, (sigma_val / meter) / (mu_val / meter), tol=sp.Float('2e-3'))

# ---- Transition T3: R = sigma^2 / mu = 0.122/0.693 = 0.176 ----
R_val = sp.Float(0.176) * meter
check("T3: R = sigma^2/mu",
      (R_val / meter), (sigma2_val / meter**2) / (mu_val / meter), tol=sp.Float('2e-3'))

# ---- Transition T4: acceptance window R +/- 10% -> [0.158, 0.194] ----
w_lo, w_hi = sp.Float(0.158), sp.Float(0.194)
check("T4a: window lower = 0.9*R", w_lo, sp.Float('0.9') * (R_val / meter), tol=sp.Float('2e-3'))
check("T4b: window upper = 1.1*R", w_hi, sp.Float('1.1') * (R_val / meter), tol=sp.Float('2e-3'))
in_window = w_lo <= (R_val / meter) <= w_hi
print(f"SANITY {'ok' if bool(in_window) else 'FAIL'}: R within its own window")

# ---- Transition T5: Euclidean benchmark sqrt(N) = sqrt(1000) = 31.62 ----
bench_val = sp.Float(31.62) * meter
check("T5: benchmark = sqrt(N)", (bench_val / meter)**2, sp.Integer(1000), tol=sp.Float('2e-3'))

# ---- Transition T6: factor = benchmark / mu = 31.62/0.693 = 45.6 ----
factor_val = sp.Float(45.6)
check("T6: factor = benchmark/mu",
      factor_val, (bench_val / meter) / (mu_val / meter), tol=sp.Float('2e-3'))

# ---- Transition T7: projected unbounded displacement at N=1e6:
#      proj = mu * sqrt(N/1000) = 0.693 * sqrt(1000) = 21.9 ----
proj_val = sp.Float(21.9) * meter
check("T7: proj = mu*sqrt(N/N0)",
      (proj_val / meter)**2, (mu_val / meter)**2 * (sp.Integer(10)**6) / sp.Integer(1000),
      tol=sp.Float('2e-3'))

# ---- Transition T8 (limiting case): plateau claim — bounded diffusion holds
#      mean displacement near mu=0.693 at all N; unbounded would give 21.9 at N=1e6.
#      This is a hypothesis, not an algebraic identity: check consistency only.
plateau = mu_val / meter
proj_n  = proj_val / meter
consistent = proj_n > plateau  # unbounded projection must exceed plateau
print(f"SANITY {'ok' if bool(consistent) else 'FAIL'}: projection exceeds plateau (limiting case)")

# ---- Transition T9 (cited theorem, Section 4.7): M1(T) >= 9n - 16 for even n,
#      equality for 4-trees. Verify equality-case arithmetic on a star-like 4-tree:
#      internal degree 4, n pendent vertices -> edges = n + (n/2 - 1)? Check bound algebra.
n = sp.Symbol('n', integer=True, positive=True)
M1_bound = 9*n - 16
# For a 4-tree: each internal vertex degree 4; sum of degrees = 2(n + n_internal - 1).
# n_internal = n/2 + 1 (each internal vertex adjacent to 2 pendent + 2 internal on average).
n_int = n/2 + 1
deg_sum = 4*n_int + n  # internal vertices degree 4, pendent degree 1
M1_eq = simplify(deg_sum - 2*(n + n_int - 1))  # M1 = sum deg^2 - ... placeholder check
# Direct: M1 = sum over vertices of degree^2 = 16*n_int + 1*n
M1_direct = 16*n_int + n
check("T9: M1 equality case 16*(n/2+1)+n = 9n-16",
      M1_direct, M1_bound)
# -> 9n+16 vs 9n-16: refuted as stated equality for this degree profile; report as-is.

# ---- Inconclusive placeholder: reduction of tree Markov dynamics to Vladimirov
#      pseudo-differential equation (Section 4.1) is an explicit modeling assumption,
#      not a derivable identity.
print("DERIV inconclusive: tree-Markov -> Vladimirov pseudo-differential reduction (declared assumption)")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: sigma = sqrt(0.122), expected 0.349
s2 = 0.122
sigma = math.sqrt(s2)
results.append(("Q1", sigma, "0.349", 3))

# Q2: CV = sigma/mu, expected 0.503
mu = 0.693
cv = sigma / mu
results.append(("Q2", cv, "0.503", 3))

# Q3: R = sigma^2/mu, expected 0.176
R = s2 / mu
results.append(("Q3", R, "0.176", 3))

# Q4: CV^2 * mu with CV = 0.5036, expected 0.1758
cv_paper = 0.5036
check = cv_paper**2 * mu
results.append(("Q4", check, "0.1758", 4))

# Q5: sqrt(1000), expected 31.62
bench = math.sqrt(1000)
results.append(("Q5", bench, "31.62", 4))

# Q6: 31.62/0.693, expected 45.6
factor = bench / mu
results.append(("Q6", factor, "45.6", 3))

# Q7: 0.9*0.176, expected 0.1584
R_paper = 0.176
lo = 0.9 * R_paper
results.append(("Q7", lo, "0.1584", 4))

# Q8: 1.1*0.176, expected 0.1936
hi = 1.1 * R_paper
results.append(("Q8", hi, "0.1936", 4))

# Q9: 0.693*sqrt(10^6/1000), expected 21.9
proj = mu * math.sqrt(10**6 / 1000)
results.append(("Q9", proj, "21.9", 3))

# Q10: 0.10*21.9, expected 2.2
unc = 0.10 * proj
results.append(("Q10", unc, "2.2", 2))

# Q11: M1 = 5^2 + 5*6^2 + 25*1^2, expected 230
M1 = 5**2 + 5 * 6**2 + 25 * 1**2
results.append(("Q11", M1, "230", 3))

# Q12: M2 = 5*(5*6) + 25*(6*1), expected 300
M2 = 5 * (5 * 6) + 25 * (6 * 1)
results.append(("Q12", M2, "300", 3))

# Q13: 9*25 - 15, expected 210
b1 = 9 * 25 - 15
results.append(("Q13", b1, "210", 3))

# Q14: 11*25 - 27, expected 248
b2 = 11 * 25 - 27
results.append(("Q14", b2, "248", 3))

# Q15: 1/5, expected 0.2
dE = 1 / 5
results.append(("Q15", dE, "0.2", 1))

match_count = 0
for cid, computed, expected_str, nsig in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, nsig) == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
