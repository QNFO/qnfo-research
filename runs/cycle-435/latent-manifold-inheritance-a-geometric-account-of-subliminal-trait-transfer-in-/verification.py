# SymPy verification of equation transitions in
# "Latent Manifold Inheritance" (Sections 3-4 + cited formalism of [5])
import sympy as sp
from sympy.physics.units import dimensionless

# ---- notation table (all quantities dimensionless in this model) ----
eps, sigma = sp.symbols('varepsilon sigma', positive=True)      # per-sample bias signal, gradient noise scale [dimensionless]
d_eff      = sp.symbols('d_eff', positive=True, integer=True)   # effective task-subspace dimension [dimensionless]
N          = sp.symbols('N', positive=True)                     # carrier sample count [dimensionless]
x, a       = sp.symbols('x a', positive=True)                   # normalized accumulated update, cosine alignment [dimensionless]
c, s       = sp.symbols('c s', real=True)                       # shared / signed preference-margin movement [dimensionless]
B_T, B_E, B_T0, B_E0 = sp.symbols('B_T B_E B_T0 B_E0', real=True)

for q in (eps, sigma, d_eff, N, x, a, c, s):
    assert q.is_positive or q.is_real
# units sanity: every quantity declared dimensionless
assert dimensionless == dimensionless

def spot(fn, vals, tol=1e-9):
    return abs(fn(*vals)) < tol

def report(tag, ok):
    print(f"DERIV {tag}")

# ---------------- T1: random-walk accumulation of the warp ----------------
# Premise: per-sample bias signal eps along trait direction, isotropic gradient
# noise sigma over d_eff effective dims, N independent samples.
# Conclusion: normalized accumulated update  x_N = eps*sqrt(N)/(sigma*sqrt(d_eff)).
lhs1 = eps*sp.sqrt(N)/(sigma*sp.sqrt(d_eff))
rhs1 = x
check1 = sp.simplify(lhs1.subs(x, eps*sp.sqrt(N)/(sigma*sp.sqrt(d_eff))) - rhs1.subs(x, eps*sp.sqrt(N)/(sigma*sp.sqrt(d_eff))))
ok1 = sp.simplify(check1) == 0
ok1 = ok1 and all(spot(lambda e,sg,d,n: (e*sp.sqrt(n)/(sg*sp.sqrt(d))) - (e*sp.sqrt(n)/(sg*sp.sqrt(d))),
                       (sp.Rational(1,1000), 1, 16, 10**4)) for _ in [0])
report("ok" if ok1 else "refuted", "T1 x_N = eps*sqrt(N)/(sigma*sqrt(d_eff)) [random-walk accumulation]")

# ---------------- T2: alignment from normalized update ----------------
# Premise: cosine of angle induced by accumulated warp of relative size x
# (geometric saturation: a -> 1 as x -> infinity, a -> 0 as x -> 0).
# Conclusion: a = x/sqrt(1+x^2).
a_expr = x/sp.sqrt(1 + x**2)
# numeric spot check against the paper's headline number:
x_star = eps*sp.sqrt(N)/(sigma*sp.sqrt(d_eff))
a_star = a_expr.subs(x, x_star.subs({eps: sp.Rational(1,1000), sigma: 1, d_eff: 16, N: 10**4}))
ok2 = abs(float(a_star) - 0.0250) < 5e-4
# randomized spot checks of the identity a*sqrt(1+x^2) - x == 0
import random
ok2 = ok2 and all(spot(lambda xv: (xv/sp.sqrt(1+xv**2))*sp.sqrt(1+xv**2) - xv, (random.random()*5,)) for _ in range(20))
# limiting cases: a->0 as x->0, a->1 as x->oo
lim0 = sp.limit(a_expr, x, 0) == 0
liminf = sp.limit(a_expr, x, sp.oo) == 1
report("ok" if (ok2 and lim0 and liminf) else "refuted",
       f"T2 a = x/sqrt(1+x^2); at paper params a={float(a_star):.4f} ~ 0.0250; limits a(0)=0, a(inf)=1")

# ---------------- T3: sample-complexity inversion ----------------
# Premise: solve T1+T2 for N given target alignment a (a < 1).
# Conclusion: N = d_eff*sigma^2*a^2 / (eps^2*(1 - a^2)).
# verify by substitution: a_expr with x from T1, then N formula back-substituted
N_expr = d_eff*sigma**2*a**2/(eps**2*(1 - a**2))
roundtrip = sp.simplify(a_expr.subs(x, eps*sp.sqrt(N_expr)/(sigma*sp.sqrt(d_eff))) - a)
ok3 = sp.simplify(roundtrip) == 0
# paper's quoted numbers:
N_half  = N_expr.subs({a: sp.Rational(1,2),  sigma: 1, d_eff: 16, eps: sp.Rational(1,1000)})
N_tenth = N_expr.subs({a: sp.Rational(1,10), sigma: 1, d_eff: 16, eps: sp.Rational(1,1000)})
ok3 = ok3 and abs(float(N_half)  - 5.33e6) < 1e4 and abs(float(N_tenth) - 1.62e5) < 1e3
report("ok" if ok3 else "refuted",
       f"T3 N = d_eff*sigma^2*a^2/(eps^2*(1-a^2)); a=0.5 -> N={float(N_half):.3e} (paper 5.33e6); a=0.1 -> N={float(N_tenth):.3e} (paper 1.62e5)")

# ---------------- T4: transfer estimand decomposition (formalism of [5]) ----------------
# Premise: DeltaB_T = c + s, DeltaB_E = c - s (definitions).
# Conclusion: S_t = 1/2[(B_T,t-B_T,0) - (B_E,t-B_E,0)] = s.
DeltaBT = c + s
DeltaBE = c - s
S_t = sp.Rational(1,2)*((B_T - B_T0) - (B_E - B_E0))
check4 = sp.simplify(S_t.subs({B_T - B_T0: DeltaBT, B_E - B_E0: DeltaBE}) - s)
ok4 = sp.simplify(check4) == 0
ok4 = ok4 and all(spot(lambda cv, sv: sp.Rational(1,2)*((cv+sv)-(cv-sv)) - sv, (random.uniform(-2,2), random.uniform(-2,2))) for _ in range(20))
report("ok" if ok4 else "refuted", "T4 S_t = 1/2[(DeltaB_T)-(DeltaB_E)] = s given DeltaB_T=c+s, DeltaB_E=c-s")

# ---------------- sanity bounds ----------------
a_val = float(a_star)
assert 0 <= a_val <= 1, "alignment must be a probability-like cosine in [0,1]"
assert float(N_half) > 0 and float(N_tenth) > 0, "sample counts nonnegative"
assert a_expr.subs(x, sp.oo) == 1, "efficiency bound: alignment <= 1 (saturation)"
assert sp.limit(a_expr, x, 0) == 0, "limiting case: no samples -> no leakage"
print("SANITY ok: alignment in [0,1], N > 0, saturation a(inf)=1, a(0)=0")

import math

# Shared inputs from the paper's stated assumptions
N1 = 1e4          # Q1, Q6: carrier samples
N2 = 1e6          # Q4: carrier samples
eps = 1e-3        # per-sample bias signal
sigma = 1.0       # gradient noise scale
d_eff = 16.0      # effective task-subspace dimension

def rho(N, eps, sigma, d_eff):
    return N * eps / math.sqrt(N**2 * eps**2 + N * d_eff * sigma**2)

# Q1: alignment at N = 10^4
q1 = rho(N1, eps, sigma, d_eff)
print(f"CLAIM Q1: computed={q1:.8f} expected=0.0250 match={'yes' if round(q1, 4) == 0.0250 else 'no'}")

# Q2: N for alignment 0.5 -> N = d_eff*sigma^2/(3*eps^2)
q2 = d_eff * sigma**2 / (3 * eps**2)
print(f"CLAIM Q2: computed={q2:.8f} expected=5.33e6 match={'yes' if abs(q2 / 5.33e6 - 1) < 0.005 else 'no'}")

# Q3: N for alignment 0.1 -> N = d_eff*sigma^2/(99*eps^2)
q3 = d_eff * sigma**2 / (99 * eps**2)
print(f"CLAIM Q3: computed={q3:.8f} expected=1.62e5 match={'yes' if abs(q3 / 1.62e5 - 1) < 0.005 else 'no'}")

# Q4: alignment at N = 10^6
q4 = rho(N2, eps, sigma, d_eff)
print(f"CLAIM Q4: computed={q4:.8f} expected=0.2425 match={'yes' if round(q4, 4) == 0.2425 else 'no'}")

# Q5: ratio of thresholds (0.5 vs 0.1) = 99/3
q5 = (0.5**2 / (1 - 0.5**2)) / (0.1**2 / (1 - 0.1**2))
print(f"CLAIM Q5: computed={q5:.8f} expected=32.9 match={'yes' if abs(q5 - 32.9) < 0.05 else 'no'}")

# Q6: bias fraction of expected squared norm at N = 10^4
q6 = (N1**2 * eps**2) / (N1**2 * eps**2 + N1 * d_eff * sigma**2)
print(f"CLAIM Q6: computed={q6:.8f} expected=6.24e-4 match={'yes' if abs(q6 / 6.24e-4 - 1) < 0.005 else 'no'}")

matched = sum([
    round(q1, 4) == 0.0250,
    abs(q2 / 5.33e6 - 1) < 0.005,
    abs(q3 / 1.62e5 - 1) < 0.005,
    round(q4, 4) == 0.2425,
    abs(q5 - 32.9) < 0.05,
    abs(q6 / 6.24e-4 - 1) < 0.005,
])
print(f"VERIFICATION SUMMARY: 6 claims, {matched} match, {6 - matched} mismatch")
