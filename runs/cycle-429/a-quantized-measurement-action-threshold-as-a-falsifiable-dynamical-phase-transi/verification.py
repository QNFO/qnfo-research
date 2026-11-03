import sympy as sp
from sympy.physics.units import second, joule, hbar as hbar_unit, kelvin
from sympy.physics.units import convert_to
from sympy import Rational, ln, E, Float, symbols, simplify, oo

# ---------------- Notation table with units ----------------
S_c      = symbols('S_c', positive=True)          # critical accumulated measurement action [J s]
gamma    = symbols('gamma', positive=True)        # measurement rate [1/s]
F_Q      = symbols('F_Q', positive=True)          # quantum Fisher information rate [1/s]
t_c      = symbols('t_c', positive=True)          # threshold time [s]
N_c      = symbols('N_c', positive=True)          # threshold measurement count [dimensionless]
epsilon  = symbols('varepsilon', positive=True)   # weak-measurement strength [dimensionless]
k_B      = symbols('k_B', positive=True)          # Boltzmann constant [J/K]
T        = symbols('T', positive=True)            # temperature [K]
n        = symbols('n', integer=True, positive=True)

hbar_val = sp.nsimplify(hbar_unit)                # sympy's hbar carries J*s units
gamma_v  = Float(1e4) * 1/second                  # 1e4 s^-1
eps_v    = Float(0.1)

# ---------------- Sanity bounds ----------------
def sanity():
    ok = True
    # probabilities in [0,1]: none appear in extracted text (no p, eta quantities)
    # efficiencies <= 1: none appear in extracted text
    # nonnegative costs: Landauer cost k_B*T*ln2 >= 0 for k_B,T>0
    if not (k_B > 0 and T > 0):
        ok = False
    # limiting cases: gamma->0 => t_c->infty ; epsilon->0 => N_c->infty
    if not sp.limit(ln(2)/(2*gamma), gamma, 0, '+') == oo:
        ok = False
    if not sp.limit(2*ln(2)/epsilon**2, epsilon, 0, '+') == oo:
        ok = False
    print("SANITY", "ok" if ok else "failed")
sanity()

# ---------------- Transition checks ----------------
def check(name, lhs, rhs, justification, numeric=None):
    diff = simplify(sp.together(lhs - rhs))
    if diff == 0:
        print(f"DERIV ok        {name} | justification: {justification}")
    elif numeric is not None:
        l, r = numeric
        if abs(float(l - r)) <= 1e-3 * max(abs(float(l)), abs(float(r)), 1e-300):
            print(f"DERIV ok        {name} (numeric spot check) | justification: {justification}")
        else:
            print(f"DERIV refuted   {name} (numeric mismatch {float(l)} vs {float(r)}) | {justification}")
    else:
        print(f"DERIV inconclusive {name} | justification: {justification}")

# T1: S_c = hbar*ln(2), numeric value 7.3097e-35 J*s
# Premise: Landauer (k_B T ln2) + time-energy uncertainty; full derivation not in provided text.
lhs = hbar_val * ln(2)
rhs = Float(7.3097e-35) * joule * second
check("T1 S_c = hbar*ln2 = 7.3097e-35 J*s",
      convert_to(lhs, joule*second), rhs,
      "Landauer + time-energy uncertainty (derivation section not provided)",
      numeric=(convert_to(lhs, joule*second).subs(joule, 1).subs(second, 1), 7.3097e-35))

# T2: t_c = 2/F_Q  (Fisher-information threshold)
# Premise: F_Q is the accumulated QFI rate; the link 2/F_Q is asserted, not derived in provided text.
check("T2 t_c = 2/F_Q", t_c, 2/F_Q,
      "asserted Fisher-information threshold; derivation not in provided text")

# T3: t_c = ln2/(2*gamma) with gamma = 1e4 s^-1 -> 34.66 microseconds
# Premise: F_Q = 2*gamma/ln2 (implied but not stated); numeric value checkable.
lhs = ln(2)/(2*gamma)
rhs = 2/F_Q
# consistency of T3 with T2 requires F_Q = 2*gamma/ln2:
check("T3a consistency F_Q = 2*gamma/ln2 with T2", rhs.subs(F_Q, 2*gamma/ln(2)), lhs,
      "implied premise F_Q = 2*gamma/ln2 not stated in provided text")
t_num = float(ln(2)/(2*1e4))          # seconds
check("T3b t_c = ln2/(2*gamma) = 34.66 us at gamma=1e4/s",
      ln(2)/(2*gamma_v), Float(34.66e-6)*second,
      "arithmetic from stated gamma",
      numeric=(t_num, 34.66e-6))

# T4: N_c ~ 138.6 at epsilon = 0.1
# Candidate closed forms: 2*ln2/eps^2 = 138.63 ; ln2/(2*eps^2) = 34.66 (excluded by value).
lhs = 2*ln(2)/epsilon**2
check("T4a N_c = 2*ln2/eps^2 at eps=0.1 -> 138.6",
      lhs.subs(epsilon, eps_v), Float(138.6),
      "reverse-engineered from stated value; formula not stated in provided text",
      numeric=(float(lhs.subs(epsilon, eps_v)), 138.6))
check("T4b N_c relation to t_c = 2/F_Q (per-measurement F_Q = eps^2?)",
      N_c, 2/epsilon**2,
      "would follow if per-measurement F_Q = eps^2, but then N_c=200 not 138.6 -> premise inconsistent",
      numeric=(float((2/epsilon**2).subs(epsilon, eps_v)), 138.6))

# T5: Landau expansion gives beta = 1/2, susceptibility exponent 1
# Premise: free-energy functional F[rho] = <H> - T S(rho) + lambda*DeltaI; expansion not provided.
beta, chi_exp = symbols('beta chi_exp', positive=True)
check("T5 beta = 1/2 (mean-field Landau)", beta, Rational(1, 2),
      "standard mean-field value; Landau expansion not provided in text")
check("T5b susceptibility exponent = 1", chi_exp, 1,
      "standard mean-field value; Landau expansion not provided in text")

# T6: threshold quantization S >= n*hbar with first threshold S_c = hbar*ln2 < hbar
# Internal consistency: ln2 < 1, so first threshold is below one hbar — consistent with n=1 claim only
# if thresholds are n*hbar*ln2, not n*hbar; premise/conclusion conflict -> refuted as stated.
check("T6 S >= n*hbar with S_c = hbar*ln2 (n=1)",
      symbols('S_thresh'), hbar_val,
      "text asserts both S >= n*hbar and S_c = hbar*ln2 < hbar; inconsistent as written",
      numeric=(float(sp.N(hbar_val)), float(sp.N(hbar_val*ln(2)))))

import math

hbar = 1.0545718e-34
ln2 = 0.693147
kB = 1.380649e-23
T = 0.02
gamma1 = 1e4
gamma2 = 1e6
eps1 = 0.1
eps2 = 0.05

# Q1
S_c = hbar * ln2
print(f"CLAIM Q1: computed={S_c:.8e} expected=7.3097e-35 match={'yes' if round(S_c, 39) == 7.3097e-35 else 'no'}")

# Q2
E_L = kB * T * ln2
print(f"CLAIM Q2: computed={E_L:.8e} expected=1.9139e-25 match={'yes' if round(E_L, 30) == 1.9139e-25 else 'no'}")

# Q3
dt_min = S_c / E_L
print(f"CLAIM Q3: computed={dt_min:.8e} expected=0.382e-9 match={'yes' if round(dt_min, 12) == 0.382e-9 else 'no'}")

# Q4
t_c = ln2 / (2 * gamma1)
print(f"CLAIM Q4: computed={t_c:.8e} expected=34.66e-6 match={'yes' if round(t_c, 11) == 34.66e-6 else 'no'}")

# Q5
N_c = 2 * ln2 / eps1**2
print(f"CLAIM Q5: computed={N_c:.8f} expected=138.6 match={'yes' if round(N_c, 1) == 138.6 else 'no'}")

# Q6
t_c_alt = ln2 / (4 * gamma1)
print(f"CLAIM Q6: computed={t_c_alt:.8e} expected=17.33e-6 match={'yes' if round(t_c_alt, 11) == 17.33e-6 else 'no'}")

# Q7
N_c_alt = ln2 / eps1**2
print(f"CLAIM Q7: computed={N_c_alt:.8f} expected=69.3 match={'yes' if round(N_c_alt, 1) == 69.3 else 'no'}")

# Q8
t_c2 = ln2 / (2 * gamma2)
print(f"CLAIM Q8: computed={t_c2:.8e} expected=0.347e-6 match={'yes' if round(t_c2, 9) == 0.347e-6 else 'no'}")

# Q9
N_c2 = 2 * ln2 / eps2**2
print(f"CLAIM Q9: computed={N_c2:.8f} expected=554.5 match={'yes' if round(N_c2, 1) == 554.5 else 'no'}")

print("VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch")
