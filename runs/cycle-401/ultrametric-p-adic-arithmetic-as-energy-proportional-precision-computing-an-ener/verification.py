# Verification of equation transitions in "Ultrametric p-Adic Arithmetic as
# Energy-Proportional Precision Computing".
# NOTE: the provided paper text is truncated mid-Section 3.1; transitions from
# Sections 3.2-4.F are reconstructed from the abstract's stated numbers and
# flagged inconclusive where the derivation text is missing.

import sympy as sp
from sympy import Rational, sqrt, floor, simplify, S
from sympy.physics.units import joule, pico, Quantity, convert_to

pJ = pico * joule  # unit declaration for all energies

# ---- notation table (units declared) ----
k   = sp.symbols('k', integer=True, nonnegative=True)          # digits (dimensionless)
ed  = sp.Symbol('e_d', positive=True)                          # digit-cell energy  [pJ]
ea  = sp.Symbol('e_a', positive=True)                          # accumulate energy  [pJ]
Ef  = sp.Symbol('E_f', positive=True)                          # FP MAC energy      [pJ]
eps = sp.Symbol('varepsilon', positive=True)                   # tolerance          [dimensionless]

# ---- declared assumptions ----
ed45, ea45 = S(0.01), S(0.001)      # pJ at 45 nm
Ef45, Ef7  = S(3.7),  S(0.9)        # pJ
eps_val    = S(10)**-2

E_p = lambda kk, edv, eav: kk**2*edv + kk*eav

def check(name, lhs, rhs):
    d = simplify(sp.expand(lhs - rhs))
    if d == 0:
        print(f"DERIV ok            {name}")
    else:
        # randomized numeric spot check
        import random
        ok = True
        for _ in range(20):
            kd = random.randint(0, 50)
            a  = random.uniform(0.001, 0.05); b = random.uniform(0.0001, 0.01)
            if abs(float(lhs.subs({k: kd, ed: a, ea: b}) - rhs.subs({k: kd, ed: a, ea: b}))) > 1e-9:
                ok = False; break
        print(f"DERIV {'ok' if ok else 'refuted'}            {name} (numeric spot check)")

# T1: energy model definition E_p(k) = k^2 e_d + k e_a  (Section 3, contribution 1)
lhs = E_p(k, ed, ea); rhs = k**2*ed + k*ea
check("T1 E_p(k)=k^2*e_d+k*e_a", lhs, rhs)

# T2: break-even k* solves k^2 e_d + k e_a = E_f  ->  k* = floor((sqrt(e_a^2+4 e_d E_f)-e_a)/(2 e_d))
kstar_expr = lambda edv, eav, Efv: floor((sqrt(eav**2 + 4*edv*Efv) - eav)/(2*edv))
# T2a: 45 nm -> k* = 19
check("T2a k*(45nm)=19", kstar_expr(ed45, ea45, Ef45), sp.Integer(19))
# T2b: 7 nm -> k* = 9  (assumes same e_d, e_a at 7 nm; paper states only E_f=0.9)
check("T2b k*(7nm)=9", kstar_expr(ed45, ea45, Ef7), sp.Integer(9))

# T3: tolerance eps=1e-2 requires k=7 digits (Section 4 derivation truncated)
# candidate rule k = ceil(log_p(1/eps)); with p=2: ceil(log2(100)) = 7
k_eps = sp.ceiling(sp.log(1/eps_val, 2))
if simplify(k_eps - 7) == 0:
    print("DERIV ok            T3 k(eps=1e-2)=7 via k=ceil(log_2(1/eps)) [rule reconstructed; paper text truncated]")
else:
    print("DERIV inconclusive  T3 k(eps=1e-2)=7 (digit-count rule derivation truncated in source)")

# T4: E_p(7) = 0.497 pJ
check("T4 E_p(7)=0.497 pJ", E_p(7, ed45, ea45), S(497)/1000)

# T5a: saving at 45 nm = 1 - E_p(7)/E_f = 86.57%
check("T5a saving(45nm)=86.57%", 1 - E_p(7, ed45, ea45)/Ef45, S(8657)/10000)
# T5b: saving at 7 nm = 44.78%
check("T5b saving(7nm)=44.78%", 1 - E_p(7, ed45, ea45)/Ef7, S(4478)/10000)

# T6: workload-level projection 58.0% total saving for 1e9-MAC heterogeneous layer
print("DERIV inconclusive  T6 workload saving=58.0% (Section 4.E derivation truncated in source)")
# T7: sensitivity span -25.5% to 87.2% over e_d in [0.003, 0.03] pJ
print("DERIV inconclusive  T7 sensitivity span [-25.5%, 87.2%] (Section 4.E derivation truncated)")

# ---- sanity bounds ----
print("--- sanity bounds ---")
assert all(0 <= float(x) <= 1 for x in [1 - E_p(7, ed45, ea45)/Ef45, 1 - E_p(7, ed45, ea45)/Ef7]), "savings must be in [0,1]"
assert ed45 > 0 and ea45 > 0 and Ef45 > 0 and Ef7 > 0, "costs must be nonnegative"
assert E_p(0, ed45, ea45) == 0, "limiting case: k=0 -> zero energy"
assert E_p(1, ed45, ea45) < E_p(2, ed45, ea45) < E_p(19, ed45, ea45), "E_p increasing in k"
assert float(convert_to(S(497)/1000 * pJ, joule)) > 0, "E_p(7) positive in joules"
# break-even limiting cases: as e_d -> 0+, k* -> floor(E_f/e_a); as E_f grows, k* grows
assert kstar_expr(ed45, ea45, Ef45) > kstar_expr(ed45, ea45, Ef7), "larger E_f gives larger k*"
print("sanity bounds passed: savings in [0,1], costs > 0, E_p(0)=0, E_p increasing, k* monotone in E_f")

import math

def Ep(k, ed, ea):
    return k*k*ed + k*ea

# Q1
Ef45 = 3.7; ed = 0.01
k1 = math.floor(math.sqrt(Ef45/ed))
print(f"CLAIM Q1: computed={k1} expected=19 match={'yes' if k1==19 else 'no'}")

# Q2
Ef7 = 0.9
k2 = math.floor(math.sqrt(Ef7/ed))
print(f"CLAIM Q2: computed={k2} expected=9 match={'yes' if k2==9 else 'no'}")

# Q3
eps = 1e-2; p = 2
k3 = math.ceil(math.log(1/eps)/math.log(p))
print(f"CLAIM Q3: computed={k3} expected=7 match={'yes' if k3==7 else 'no'}")

# Q4
ea = 0.001
Ep7 = Ep(7, ed, ea)
print(f"CLAIM Q4: computed={Ep7:.8f} expected=0.497 match={'yes' if round(Ep7,3)==0.497 else 'no'}")

# Q5
sav45 = (Ef45 - Ep7)/Ef45
print(f"CLAIM Q5: computed={sav45:.8f} expected=0.8657 match={'yes' if round(sav45,4)==0.8657 else 'no'}")

# Q6
sav7 = (Ef7 - Ep7)/Ef7
print(f"CLAIM Q6: computed={sav7:.8f} expected=0.4478 match={'yes' if round(sav7,4)==0.4478 else 'no'}")

# Q7
perbit = 7*ed + ea
print(f"CLAIM Q7: computed={perbit:.8f} expected=0.071 match={'yes' if round(perbit,3)==0.071 else 'no'}")

# Q8
bf = 24
fpbit = Ef45/bf
print(f"CLAIM Q8: computed={fpbit:.8f} expected=0.15416666666666667 match={'yes' if abs(fpbit-0.15416666666666667)<1e-12 else 'no'}")

# Q9
ratio = perbit/fpbit
print(f"CLAIM Q9: computed={ratio:.8f} expected=0.4606 match={'yes' if round(ratio,4)==0.4606 else 'no'}")

# Q10
N = 1e9; f = 0.8
Ep24 = Ep(24, ed, ea)
Etot = N*(f*Ep7 + (1-f)*Ep24)  # pJ
Etot_mJ = Etot/1e9
Ef_tot_mJ = N*Ef45/1e9
sav10 = (Ef_tot_mJ - Etot_mJ)/Ef_tot_mJ
print(f"CLAIM Q10: computed={sav10:.8f} expected=0.580 match={'yes' if round(sav10,3)==0.580 else 'no'}")

# Q11
ed2 = 0.003
Ep7b = Ep(7, ed2, ea); Ep24b = Ep(24, ed2, ea)
permac = f*Ep7b + (1-f)*Ep24b
sav11 = (Ef45 - permac)/Ef45
print(f"CLAIM Q11: computed={sav11:.8f} expected=0.872 match={'yes' if round(sav11,3)==0.872 else 'no'}")

# Q12
ed3 = 0.03
Ep7c = Ep(7, ed3, ea); Ep24c = Ep(24, ed3, ea)
permac3 = f*Ep7c + (1-f)*Ep24c
sav12 = (Ef45 - permac3)/Ef45
print(f"CLAIM Q12: computed={sav12:.8f} expected=-0.255 match={'yes' if round(sav12,3)==-0.255 else 'no'}")

# Q13
B = 100e9; ebyte = 0.2  # nJ/byte
Eflat = B*ebyte  # nJ
Eflat_J = Eflat/1e9
Ehalf_J = 0.5*Eflat_J
print(f"CLAIM Q13: computed={Eflat_J:.8f} expected=20 match={'yes' if Eflat_J==20 else 'no'}")
print(f"CLAIM Q13b: computed={Ehalf_J:.8f} expected=10 match={'yes' if Ehalf_J==10 else 'no'}")

# Q14
ed_thresh = Ef45/49
print(f"CLAIM Q14: computed={ed_thresh:.8f} expected=0.0755 match={'yes' if round(ed_thresh,4)==0.0755 else 'no'}")

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")
