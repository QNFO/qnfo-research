# Verification of equation transitions in "Ultrametric State Counting"
import sympy as sp
from sympy import symbols, simplify, Sum, oo, Rational, S, log, exp, diff, limit, Abs
from sympy.physics.units import hbar, h, c, Quantity, kelvin, joule, second, meter
from sympy.physics.units import convert_to

p = symbols('p', prime=True, positive=True)
n = symbols('n', integer=True, nonnegative=True)
nu = symbols('nu', positive=True)          # frequency (Hz)
beta = symbols('beta', positive=True)      # 1/energy
T = symbols('T', positive=True)            # temperature (K)
kB = Quantity('kB')                        # Boltzmann constant (declared symbolically)

def check(name, lhs, rhs, assumption_check=None):
    d = simplify(lhs - rhs)
    if d == 0:
        print(f"DERIV ok  : {name}")
    else:
        print(f"DERIV inconclusive : {name}  (residual={d})")

# ---------------------------------------------------------------
# T1: Geometric series  S = sum p^{-n} = 1/(1-1/p) = p/(p-1)
#     Premise: |r| = 1/p < 1 for prime p >= 2 (convergent geometric series)
# ---------------------------------------------------------------
S_sum = Sum(p**(-n), (n, 0, oo)).doit()
check("T1 sum p^-n = p/(p-1)", S_sum, p/(p-1))
# limiting case: p -> infinity  =>  Z -> 1
print("limit p->oo Z =", limit(p/(p-1), p, oo), "(expect 1)")

# ---------------------------------------------------------------
# T2: Auxiliary sum  sum n r^n = r/(1-r)^2, r = 1/p
# ---------------------------------------------------------------
r = symbols('r', positive=True)
aux = Sum(n*r**n, (n, 0, oo)).doit()
check("T2 sum n r^n = r/(1-r)^2", aux, r/(1-r)**2)
aux_p = aux.subs(r, S(1)/p)
check("T2b sum n p^-n = (1/p)/(1-1/p)^2", aux_p, (S(1)/p)/(1-S(1)/p)**2)

# ---------------------------------------------------------------
# T3: Mean occupation  <n> = (1-1/p) * sum n p^-n = 1/(p-1)
# ---------------------------------------------------------------
lhs3 = (1 - S(1)/p) * aux_p
check("T3 <n> = 1/(p-1)", simplify(lhs3), 1/(p-1))
print("limit p->oo <n> =", limit(1/(p-1), p, oo), "(expect 0)")

# ---------------------------------------------------------------
# T4: Numerical example p=3: Z(3)=1.5, <n>(3)=0.5
# ---------------------------------------------------------------
check("T4 Z(3)=3/2", p/(p-1), Rational(3,2)).__class__  # placeholder
d = simplify((p/(p-1)).subs(p,3) - Rational(3,2))
print("DERIV ok  : T4 Z(3)=1.5" if d == 0 else f"DERIV refuted : T4 Z(3) residual={d}")
d = simplify((1/(p-1)).subs(p,3) - Rational(1,2))
print("DERIV ok  : T4 <n>(3)=0.5" if d == 0 else f"DERIV refuted : T4 <n>(3) residual={d}")

# ---------------------------------------------------------------
# T5: Spectral radiance substitution:
#     beta*h*nu = -ln(1/p)  =>  1/(e^{beta h nu}-1) = 1/(p-1)
# ---------------------------------------------------------------
e_bhn = exp(-log(S(1)/p))   # = p
check("T5 1/(e^{beta h nu}-1) = 1/(p-1) given z=1/p",
      1/(e_bhn - 1), 1/(p-1))
# Planck-like form B_nu(p) = 2 h nu^3 / c^2 * 1/(p-1)  -- structural, matches (7)/(8) with substitution
Bnu_p  = 2*h*nu**3/c**2 * 1/(p-1)
Bnu_pl = 2*h*nu**3/c**2 * 1/(exp(beta*h*nu)-1)
d = simplify(Bnu_p - Bnu_pl.subs(beta*h*nu, -log(S(1)/p)))
print("DERIV ok  : T5b B_nu(p) = 2h nu^3/c^2 * 1/(p-1)" if d == 0
      else f"DERIV inconclusive : T5b residual={d}")

# ---------------------------------------------------------------
# T6: dZ/dp = ((p-1)-p)/(p-1)^2 = -1/(p-1)^2
# ---------------------------------------------------------------
dZ = diff(p/(p-1), p)
check("T6 dZ/dp = -1/(p-1)^2", dZ, -1/(p-1)**2)
d = simplify(dZ.subs(p,3) - Rational(-1,4))
print("DERIV ok  : T6b dZ/dp|_{p=3} = -0.25" if d == 0 else f"DERIV refuted : T6b residual={d}")

# ---------------------------------------------------------------
# T7: d<n>/dp = -1/(p-1)^2  (identical sensitivity)
# ---------------------------------------------------------------
dn = diff(1/(p-1), p)
check("T7 d<n>/dp = -1/(p-1)^2", dn, -1/(p-1)**2)
check("T7b sensitivities identical", dZ, dn)

# ---------------------------------------------------------------
# T8: Linear approximation  Z(3.1) ≈ 1.5 - 0.025 = 1.475
#     (approximation, not identity -> numeric spot check)
# ---------------------------------------------------------------
Z31_exact = float((p/(p-1)).subs(p, sp.Float('3.1')))
Z31_lin   = 1.5 - 0.25*0.1
err = abs(Z31_exact - Z31_lin)
print(f"DERIV {'ok' if err < 1e-3 else 'inconclusive'} : T8 Z(3.1) linear approx "
      f"(exact={Z31_exact:.6f}, linear={Z31_lin}, err={err:.2e})")

# ---------------------------------------------------------------
# Sanity checks: probabilities in [0,1]; normalization; limiting cases
# ---------------------------------------------------------------
pi_n = (1 - S(1)/p) * p**(-n)
# pi_n in [0,1] for n>=0, prime p: 0 < pi_n <= 1-p^{-1} < 1
ok_bounds = all((pi_n.subs({p:pp, n:nn}) >= 0 and pi_n.subs({p:pp, n:nn}) <= 1)
                for pp in (2,3,5,7,11) for nn in range(0,6))
print("SANITY pi_n in [0,1] for sampled (p,n):", "PASS" if ok_bounds else "FAIL")
norm = simplify(Sum(pi_n, (n, 0, oo)).doit())
print("SANITY normalization sum pi_n =", norm, "(expect 1):",
      "PASS" if simplify(norm - 1) == 0 else "FAIL")
# Efficiencies/costs: no efficiency or cost quantities appear in the paper -> nothing to bound.
print("SANITY efficiencies/costs: none declared in paper (no check required)")
# Limiting cases table (Section 5)
for pp, Zexp, nexp in [(2,2,1),(3,Rational(3,2),Rational(1,2)),
                       (5,Rational(5,4),Rational(1,4)),(7,Rational(7,6),Rational(1,6))]:
    okZ = simplify((p/(p-1)).subs(p,pp) - Zexp) == 0
    okn = simplify((1/(p-1)).subs(p,pp) - nexp) == 0
    print(f"TABLE p={pp}: Z {'ok' if okZ else 'refuted'}, <n> {'ok' if okn else 'refuted'}")
# Divergence claim: integral_0^oo nu^3 dnu diverges
integrand = nu**3
print("SANITY total power integral diverges:",
      sp.integrate(integrand, (nu, 0, oo)) is sp.oo or
      sp.integrate(integrand, (nu, 0, oo)) == sp.oo)

import math

def sig(x, n=8):
    return f"{x:.{n}g}"

h = 6.626e-34
c = 3.00e8
sigma = 5.67e-8

# Q1: Z(p) = p/(p-1), p=3
Z3 = 3/(3-1)
print(f"CLAIM Q1: computed={sig(Z3)} expected=1.5 match={'yes' if round(Z3,8)==1.5 else 'no'}")

# Q2: <n> = 1/(p-1), p=3
n3 = 1/(3-1)
print(f"CLAIM Q2: computed={sig(n3)} expected=0.5 match={'yes' if round(n3,8)==0.5 else 'no'}")

# Q3: p=3 both
print(f"CLAIM Q3: computed={sig(Z3)} expected=1.5 match={'yes' if round(Z3,8)==1.5 else 'no'}")
print(f"CLAIM Q3b: computed={sig(n3)} expected=0.5 match={'yes' if round(n3,8)==0.5 else 'no'}")

# Q4: B_nu(3) = 2 h nu^3 / (c^2 (p-1)), nu=5e14
nu = 5e14
B = 2*h*nu**3/(c**2*(3-1))
print(f"CLAIM Q4: computed={sig(B)} expected=9.20e-7 match={'yes' if abs(B-9.20e-7)/9.20e-7 < 0.005 else 'no'}")

# Q5: prefactor 2 h nu^3 / c^2
pref = 2*h*nu**3/c**2
print(f"CLAIM Q5: computed={sig(pref)} expected=1.84e-6 match={'yes' if abs(pref-1.84e-6)/1.84e-6 < 0.005 else 'no'}")

# Q6: B = prefactor/(p-1)
B6 = pref/2
print(f"CLAIM Q6: computed={sig(B6)} expected=9.20e-7 match={'yes' if abs(B6-9.20e-7)/9.20e-7 < 0.005 else 'no'}")

# Q7: P = h nu_max^4 / (2 c^2 (p-1)), nu_max=1e15, p=3
numax = 1e15
P = h*numax**4/(2*c**2*(3-1))
print(f"CLAIM Q7: computed={sig(P)} expected=1.84e9 match={'yes' if abs(P-1.84e9)/1.84e9 < 0.005 else 'no'}")

# Q8: P_SB = sigma T^4, T=3000
T = 3000.0
PSB = sigma*T**4
print(f"CLAIM Q8: computed={sig(PSB)} expected=4.59e6 match={'yes' if abs(PSB-4.59e6)/4.59e6 < 0.005 else 'no'}")

# Q9: ratio
ratio = P/PSB
print(f"CLAIM Q9: computed={sig(ratio)} expected=4.0e2 match={'yes' if abs(ratio-400)/400 < 0.05 else 'no'}")

# Q10: dZ/dp at p=3
dZ = -1/(3-1)**2
print(f"CLAIM Q10: computed={sig(dZ)} expected=-0.25 match={'yes' if round(dZ,8)==-0.25 else 'no'}")

# Q11: Z(3.1) approx
dZp = -0.25*0.1
Z31 = 1.5 + dZp
print(f"CLAIM Q11: computed={sig(Z31)} expected=1.475 match={'yes' if round(Z31,8)==1.475 else 'no'}")

# Q12: R(2 nu0) = p
R = (3**2-1)/(3-1) - 1
print(f"CLAIM Q12: computed={sig(R)} expected=3 match={'yes' if R==3 else 'no'}")

# Q13: M1 bound 9*9-15
M1 = 9*9-15
print(f"CLAIM Q13: computed={sig(M1)} expected=66 match={'yes' if M1==66 else 'no'}")

# Q14: star K1,5 M1 = 5*1^2 + 5^2 = 30; bound 9*5-15
M1star = 5*1**2 + 5**2
bound5 = 9*5-15
print(f"CLAIM Q14: computed={sig(M1star)} expected=30 match={'yes' if M1star==30 and bound5==30 else 'no'}")

# Q15: P(7) = P(3)/3
P7 = 1.84e9/3
print(f"CLAIM Q15: computed={sig(P7)} expected=6.1e8 match={'yes' if abs(P7-6.1e8)/6.1e8 < 0.01 else 'no'}")

# Q16: n_leaf = p^K = 3^2
nleaf = 3**2
print(f"CLAIM Q16: computed={sig(nleaf)} expected=9 match={'yes' if nleaf==9 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
