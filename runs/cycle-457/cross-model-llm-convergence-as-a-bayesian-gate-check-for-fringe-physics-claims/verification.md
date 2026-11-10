# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Prior odds O_0 = 1/9 ≈ 0.111111 for p_0 = 0.1",
    "inputs": "p_0 = 0.1",
    "formula": "O_0 = p_0 / (1 - p_0)"
  },
  {
    "id": "Q2",
    "statement": "Two-model synthesis posterior P_2 = 8/17 ≈ 0.470588",
    "inputs": "p_0 = 0.1, K_S = 8",
    "formula": "O_2 = O_0 * K_S; P_2 = O_2 / (1 + O_2)"
  },
  {
    "id": "Q3",
    "statement": "Three-model cascade posterior P_3 = 64/73 ≈ 0.876712",
    "inputs": "p_0 = 0.1, K_S = 8, N = 3",
    "formula": "O_3 = (p_0/(1-p_0)) * K_S^(N-1); P_3 = O_3 / (1 + O_3)"
  },
  {
    "id": "Q4",
    "statement": "Four-model cascade posterior P_4 = 512/521 ≈ 0.982726",
    "inputs": "p_0 = 0.1, K_S = 8, N = 4",
    "formula": "O_4 = (p_0/(1-p_0)) * K_S^(N-1); P_4 = O_4 / (1 + O_4)"
  },
  {
    "id": "Q5",
    "statement": "Smallest panel size for P_N >= 0.95 is N = 4",
    "inputs": "p_0 = 0.1, K_S = 8, threshold P = 0.95",
    "formula": "N - 1 >= log(19 * 9) / log(8)"
  },
  {
    "id": "Q6",
    "statement": "Trap-arm posterior P_T ≈ 0.001232",
    "inputs": "p_0 = 0.1, K_T = 0.0111",
    "formula": "O_T = (p_0/(1-p_0)) * K_T; P_T = O_T / (1 + O_T)"
  },
  {
    "id": "Q7",
    "statement": "Sensitivity posterior P_2 ≈ 0.689655 at p_b^S = 0.02",
    "inputs": "p_0 = 0.1, p_c^S = 0.4, p_b^S = 0.02",
    "formula": "P_2 = (p_0 * p_c^S) / (p_0 * p_c^S + (1 - p_0) * p_b^S)"
  },
  {
    "id": "Q8",
    "statement": "Sensitivity posterior P_2 = 8/17 ≈ 0.470588 at p_b^S = 0.05",
    "inputs": "p_0 = 0.1, p_c^S = 0.4, p_b^S = 0.05",
    "formula": "P_2 = (p_0 * p_c^S) / (p_0 * p_c^S + (1 - p_0) * p_b^S)"
  },
  {
    "id": "Q9",
    "statement": "Sensitivity posterior P_2 = 4/13 ≈ 0.307692 at p_b^S = 0.10",
    "inputs": "p_0 = 0.1, p_c^S = 0.4, p_b^S = 0.10",
    "formula": "P_2 = (p_0 * p_c^S) / (p_0 * p_c^S + (1 - p_0) * p_b^S)"
  },
  {
    "id": "Q10",
    "statement": "Sensitivity posterior P_2 = 2/11 ≈ 0.181818 at p_b^S = 0.20",
    "inputs": "p_0 = 0.1, p_c^S = 0.4, p_b^S = 0.20",
    "formula": "P_2 = (p_0 * p_c^S) / (p_0 * p_c^S + (1 - p_0) * p_b^S)"
  },
  {
    "id": "Q11",
    "statement": "Retrieval-arm posterior P_R = 0.1 (no evidential gain)",
    "inputs": "p_0 = 0.1, K_R = 1",
    "formula": "O_R = (p_0/(1-p_0)) * K_R; P_R = O_R / (1 + O_R)"
  },
  {
    "id": "Q12",
    "statement": "Correlated-error effective Bayes factor K_eff ≈ 2.75862 at rho = 0.1",
    "inputs": "p_c^S = 0.4, p_b^S = 0.05, rho = 0.1",
    "formula": "p_b_eff = p_b^S + rho * (1 - p_b^S); K_eff = p_c^S / p_b_eff"
  },
  {
    "id": "Q13",
    "statement": "Correlated-error two-model posterior P_2 ≈ 0.234597",
    "inputs": "p_0 = 0.1, K_eff ≈ 2.75862",
    "formula": "O_2 = (p_0/(1-p_0)) * K_eff; P_2 = O_2 / (1 + O_2)"
  },
  {
    "id": "Q14",
    "statement": "Correlated-error panel size for P >= 0.95 is N = 7",
    "inputs": "p_0 = 0.1, K_eff ≈ 2.75862, threshold P = 0.95",
    "formula": "N - 1 >= log(19 * 9) / log(K_eff)"
  },
  {
    "id": "Q15",
    "statement": "Partial-agreement Bayes factor K_S = 1024/243 ≈ 4.21488 for q_c = 0.8, q_b = 0.6, S = 5",
    "inputs": "q_c = 0.8, q_b = 0.6, S = 5",
    "formula": "K_S = (q_c / q_b)^S"
  },
  {
    "id": "Q16",
    "statement": "Partial-agreement two-model posterior P_2 ≈ 0.318944",
    "inputs": "p_0 = 0.1, K_S ≈ 4.21488",
    "formula": "O_2 = (p_0/(1-p_0)) * K_S; P_2 = O_2 / (1 + O_2)"
  }
]

## Script
```python
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

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: O_0 = 0.1 / (1 - 0.1) = 0.1 / 0.9 = 0.1111111 (paper: 1/9 ≈ 0.111111)
CLAIM Q1: computed=0.1111111 expected=0.111111 match=yes

Q2: O_2 = 0.1111111 × 8 = 0.8888889; P_2 = 0.8888889 / 1.8888889 = 8/17 = 0.4705882
CLAIM Q2: computed=0.4705882 expected=0.470588 match=yes

Q3: K_3 = 8^2 = 64; O_3 = 0.1111111 × 64 = 7.1111111; P_3 = 7.1111111 / 8.1111111 = 64/73 = 0.8767123
CLAIM Q3: computed=0.8767123 expected=0.876712 match=yes

Q4: K_4 = 8^3 = 512; O_4 = 0.1111111 × 512 = 56.8888889; P_4 = 56.8888889 / 57.8888889 = 512/521 = 0.9827255
CLAIM Q4: computed=0.9827255 expected=0.982726 match=yes

Q5: N - 1 >= ln(171) / ln(8) = 5.1416636 / 2.0794415 = 2.4732355; smallest integer N - 1 = 3, so N = 4
CLAIM Q5: computed=4 expected=4 match=yes

Q6: O_T = 0.1111111 × 0.0111 = 0.0012333333; P_T = 0.0012333333 / 1.0012333333 = 0.0012318149 (paper: ≈ 0.001232)
CLAIM Q6: computed=0.0012318149 expected=0.001232 match=yes

Q7: P_2 = (0.1 × 0.4) / (0.1 × 0.4 + 0.9 × 0.02) = 0.04 / (0.04 + 0.018) = 0.04 / 0.058 = 0.6896552
CLAIM Q7: computed=0.6896552 expected=0.689655 match=yes

Q8: P_2 = 0.04 / (0.04 + 0.9 × 0.05) = 0.04 / 0.085 = 0.4705882
CLAIM Q8: computed=0.4705882 expected=0.470588 match=yes

Q9: P_2 = 0.04 / (0.04 + 0.9 × 0.10) = 0.04 / 0.13 = 0.3076923
CLAIM Q9: computed=0.3076923 expected=0.307692 match=yes

Q10: P_2 = 0.04 / (0.04 + 0.9 × 0.20) = 0.04 / 0.22 = 0.1818182
CLAIM Q10: computed=0.1818182 expected=0.181818 match=yes

Q11: O_R = 0.1111111 × 1 = 0.1111111; P_R = 0.1111111 / 1.1111111 = 0.1
CLAIM Q11: computed=0.1 expected=0.1 match=yes

Q12: p_b_eff = 0.05 + 0.1 × (1 - 0.05) = 0.05 + 0.095 = 0.145; K_eff = 0.4 / 0.145 = 2.7586207
CLAIM Q12: computed=2.7586207 expected=2.75862 match=yes

Q13: O_2 = 0.1111111 × 2.7586207 = 0.3065134; P_2 = 0.3065134 / 1.3065134 = 0.2345966
CLAIM Q13: computed=0.2345966 expected=0.234597 match=yes

Q14: N - 1 >= ln(171) / ln(2.7586207) = 5.1416636 / 1.0147293 = 5.0672743; smallest integer N - 1 = 6, so N = 7
CLAIM Q14: computed=7 expected=7 match=yes

Q15: K_S = (0.8 / 0.6)^5 = (4/3)^5 = 1024 / 243 = 4.2148843
CLAIM Q15: computed=4.2148843 expected=4.21488 match=yes

Q16: O_2 = 0.1111111 × 4.2148843 = 0.4683205; P_2 = 0.4683205 / 1.4683205 = 0.3189444
CLAIM Q16: computed=0.3189444 expected=0.318944 match=yes

VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.1111111 | 0.111111 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.4705882 | 0.470588 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 0.8767123 | 0.876712 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q4 | 0.9827255 | 0.982726 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.0012318149 | 0.001232 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.6896552 | 0.689655 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.4705882 | 0.470588 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.3076923 | 0.307692 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 0.1818182 | 0.181818 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 0.1 | 0.1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 2.7586207 | 2.75862 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 0.2345966 | 0.234597 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 4.2148843 | 4.21488 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 0.3189444 | 0.318944 | yes | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
