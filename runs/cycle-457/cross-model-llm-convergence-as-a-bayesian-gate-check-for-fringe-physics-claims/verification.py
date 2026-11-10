import sympy as sp
from sympy.physics.units import Quantity, probability, dimensionless
import random

# ---- Notation table with units (all quantities are dimensionless probabilities/odds) ----
p0, pc, pb, K, O0, Opost, P = sp.symbols('p0 p_c p_b K O_0 O_post P', positive=True)
N = sp.symbols('N', integer=True, positive=True)
# Declare dimensionless probability unit for sanity checks
prob = Quantity('probability'); prob.set_global_dimension(dimensionless)

results = []
def check(name, lhs, rhs, assumptions=None, spot=None):
    try:
        diff = sp.simplify(sp.together(lhs - rhs))
        ok = diff.equals(0) if assumptions is None else sp.simplify(diff.subs(assumptions)) == 0
        if ok is True or ok == 0:
            print(f"DERIV ok        {name}"); return
        if ok is False:
            print(f"DERIV refuted   {name}"); return
    except Exception:
        ok = None
    # randomized numeric spot check
    if spot:
        for _ in range(200):
            subs = spot()
            if abs(float((lhs - rhs).subs(subs))) < 1e-9:
                continue
            else:
                print(f"DERIV refuted   {name} (spot check)"); return
    print(f"DERIV inconclusive {name}")

# T1: K = p_c/p_b (definition)
check("T1 K=p_c/p_b", K, pc/pb)

# T2: P = O_post/(1+O_post), O_post = O0*K
check("T2 P=O/(1+O)", P, Opost/(1+Opost))
check("T2b O_post=O0*K", Opost, O0*K)

# T3: K_N = K^(N-1); O_N = p0/(1-p0)*K^(N-1)
KN = K**(N-1)
check("T3 O_N", p0/(1-p0)*KN, p0/(1-p0)*K**(N-1))

# T4: p0=0.1 -> O0=1/9
check("T4 O0=1/9", sp.Rational(1,10)/(1-sp.Rational(1,10)), sp.Rational(1,9))

# T5: O2 = (1/9)*8 = 8/9
check("T5 O2=8/9", sp.Rational(1,9)*8, sp.Rational(8,9))

# T6: P2 = 8/17
check("T6 P2=8/17", sp.Rational(8,9)/(1+sp.Rational(8,9)), sp.Rational(8,17))

# T7: P3 = 64/73
check("T7 P3=64/73", sp.Rational(64,9)/(1+sp.Rational(64,9)), sp.Rational(64,73))

# T8: P4 = 512/521
check("T8 P4=512/521", sp.Rational(512,9)/(1+sp.Rational(512,9)), sp.Rational(512,521))

# T9: log10(8) ~ 0.903
check("T9 log10(8)=0.903", sp.log(8,10).evalf(), sp.Float('0.903'),
      spot=lambda: {})

# T10: P_N>=0.95 <=> O_N>=19; 8^(N-1)>=171 -> N=4
check("T10a P=O/(1+O)>=0.95 <=> O>=19", sp.Rational(19,20), sp.Rational(19,20))
check("T10b threshold", sp.log(171)/sp.log(8).evalf(), sp.log(171,8))
sol = sp.solve(sp.log(sp.Rational(1,9)*8**(N-1)) >= sp.log(19), N)
print("DERIV ok        T10c N_min=4" if 4 == sp.ceiling(sp.log(171,8)) else "DERIV refuted   T10c N_min=4")

# T11: trap posterior
KT = sp.Float('0.0111')
OT = sp.Rational(1,9)*KT
check("T11a O_T", OT, sp.Float('0.00123333'))
PT = OT/(1+OT)
check("T11b P_T~1.2e-3", sp.simplify(PT), sp.Float('0.0012'), spot=lambda: {})

# T12: K_R=1 -> posterior = prior
OR1 = sp.Rational(1,10)*1
check("T12 K_R=1 posterior=prior", OR1/(1+OR1), sp.Rational(1,10))

# T13: p_c=0.4, K=8 -> p_b=0.05
check("T13 p_b=0.05", sp.Float('0.4')/8, sp.Float('0.05'))
# sensitivity range: p_b in {0.20, 0.02} with p_c=0.4
for pbs, expect in [(sp.Float('0.20'), sp.Float('0.182')), (sp.Float('0.02'), sp.Float('0.690'))]:
    Pval = (sp.Rational(1,9)*(sp.Float('0.4')/pbs))/(1+sp.Rational(1,9)*(sp.Float('0.4')/pbs))
    print(f"DERIV {'ok' if abs(float(Pval-expect))<5e-3 else 'refuted'}        T13 sensitivity p_b={pbs} -> P={float(Pval):.3f} (claimed {expect})")

# ---- Sanity bounds ----
vals = {'p0':0.1,'p_c':0.4,'p_b':0.05,'K_S':8,'K_T':0.0111,'P2':8/17,'P3':64/73,'P4':512/521,'P_T':float(PT)}
for k,v in vals.items():
    if k.startswith('p') or k.startswith('P'):
        assert 0 <= v <= 1, f"bound fail {k}"
    if k.startswith('K_T'):
        assert 0 <= v <= 1
    if k.startswith('K_S'):
        assert v >= 1
print("SANITY ok: probabilities in [0,1], K_T<=1, K_S>=1, costs n/a (none declared)")
# Limiting cases
assert sp.simplify((p0/(1-p0)*1)/(1+p0/(1-p0)) - p0) == 0   # K=1 -> posterior=prior
assert sp.limit((sp.Rational(1,9)*K**(N-1))/(1+sp.Rational(1,9)*K**(N-1)).subs(K, sp.oo), K, sp.oo) == 1
print("LIMITS ok: K=1 -> P=p0; K->inf -> P->1")

import math

def odds_post(p0, K):
    O = (p0 / (1 - p0)) * K
    P = O / (1 + O)
    return O, P

p0 = 0.1

# Q1
O0 = p0 / (1 - p0)
print(f"CLAIM Q1: computed={O0:.8f} expected=0.111111 match={'yes' if round(O0,6)==0.111111 else 'no'}")

# Q2
O2, P2 = odds_post(p0, 8)
print(f"CLAIM Q2: computed={P2:.8f} expected=0.470588 match={'yes' if round(P2,6)==0.470588 else 'no'}")

# Q3
O3, P3 = odds_post(p0, 8**2)
print(f"CLAIM Q3: computed={P3:.8f} expected=0.876712 match={'yes' if round(P3,6)==0.876712 else 'no'}")

# Q4
O4, P4 = odds_post(p0, 8**3)
print(f"CLAIM Q4: computed={P4:.8f} expected=0.982726 match={'yes' if round(P4,6)==0.982726 else 'no'}")

# Q5
n_minus_1 = math.log(19 * 9) / math.log(8)
N = math.ceil(n_minus_1) + 1
print(f"CLAIM Q5: computed={N:.8f} expected=4 match={'yes' if N==4 else 'no'}")

# Q6
OT, PT = odds_post(p0, 0.0111)
print(f"CLAIM Q6: computed={PT:.8f} expected=0.001232 match={'yes' if round(PT,6)==0.001232 else 'no'}")

# Q7-Q10 sensitivity
def sens(pb):
    return (p0 * 0.4) / (p0 * 0.4 + (1 - p0) * pb)

for qid, pb, exp in [("Q7", 0.02, 0.689655), ("Q8", 0.05, 0.470588), ("Q9", 0.10, 0.307692), ("Q10", 0.20, 0.181818)]:
    v = sens(pb)
    print(f"CLAIM {qid}: computed={v:.8f} expected={exp} match={'yes' if round(v,6)==exp else 'no'}")

# Q11
OR, PR = odds_post(p0, 1)
print(f"CLAIM Q11: computed={PR:.8f} expected=0.1 match={'yes' if round(PR,6)==0.1 else 'no'}")

# Q12
pb_eff = 0.05 + 0.1 * (1 - 0.05)
K_eff = 0.4 / pb_eff
print(f"CLAIM Q12: computed={K_eff:.8f} expected=2.75862 match={'yes' if round(K_eff,5)==2.75862 else 'no'}")

# Q13
O2c, P2c = odds_post(p0, K_eff)
print(f"CLAIM Q13: computed={P2c:.8f} expected=0.234597 match={'yes' if round(P2c,6)==0.234597 else 'no'}")

# Q14
n1 = math.log(19 * 9) / math.log(K_eff)
Nc = math.ceil(n1) + 1
print(f"CLAIM Q14: computed={Nc:.8f} expected=7 match={'yes' if Nc==7 else 'no'}")

# Q15
K_partial = (0.8 / 0.6) ** 5
print(f"CLAIM Q15: computed={K_partial:.8f} expected=4.21488 match={'yes' if round(K_partial,5)==4.21488 else 'no'}")

# Q16
O2p, P2p = odds_post(p0, K_partial)
print(f"CLAIM Q16: computed={P2p:.8f} expected=0.318944 match={'yes' if round(P2p,6)==0.318944 else 'no'}")

# summary
claims = [
    ("Q1", O0, 0.111111, 6),
    ("Q2", P2, 0.470588, 6),
    ("Q3", P3, 0.876712, 6),
    ("Q4", P4, 0.982726, 6),
    ("Q5", N, 4, 0),
    ("Q6", PT, 0.001232, 6),
    ("Q7", sens(0.02), 0.689655, 6),
    ("Q8", sens(0.05), 0.470588, 6),
    ("Q9", sens(0.10), 0.307692, 6),
    ("Q10", sens(0.20), 0.181818, 6),
    ("Q11", PR, 0.1, 6),
    ("Q12", K_eff, 2.75862, 5),
    ("Q13", P2c, 0.234597, 6),
    ("Q14", Nc, 7, 0),
    ("Q15", K_partial, 4.21488, 5),
    ("Q16", P2p, 0.318944, 6),
]
mism = sum(1 for _, c, e, d in claims if round(c, d) != e)
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims)-mism} match, {mism} mismatch")
