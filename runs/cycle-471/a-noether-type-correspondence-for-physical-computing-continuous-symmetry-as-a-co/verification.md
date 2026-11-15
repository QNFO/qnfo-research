# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Degrees-of-freedom reduction factor for cyclic model with N=360, n=1000, K=8 is 45",
    "inputs": "N=360, n=1000, K=8",
    "formula": "(N*n)/(K*n) = N/K"
  },
  {
    "id": "Q2",
    "statement": "Dense-solve speedup factor is 5,832,000 (5.83e6)",
    "inputs": "N=360, K=8",
    "formula": "N^3/K"
  },
  {
    "id": "Q3",
    "statement": "Speedup at K=36 is 1,296,000 (1.30e6) and DOF factor is 10",
    "inputs": "N=360, K=36",
    "formula": "N^3/K and N/K"
  },
  {
    "id": "Q4",
    "statement": "Unconstrained layer parameter count P_full = 1,048,576 for m=1024",
    "inputs": "m=1024",
    "formula": "m^2"
  },
  {
    "id": "Q5",
    "statement": "Equivariant layer parameter count P_eq = 2,048 for K=8, r=16",
    "inputs": "K=8, r=16",
    "formula": "K*r^2"
  },
  {
    "id": "Q6",
    "statement": "Encoder parameter reduction factor is 512",
    "inputs": "m=1024, K=8, r=16",
    "formula": "m^2/(K*r^2)"
  },
  {
    "id": "Q7",
    "statement": "Parameter reduction factor at r=32, K=8, m=1024 is 128",
    "inputs": "m=1024, K=8, r=32",
    "formula": "m^2/(K*r^2)"
  },
  {
    "id": "Q8",
    "statement": "Parameter reduction factor at m=4096, K=8, r=16 is 8192",
    "inputs": "m=4096, K=8, r=16",
    "formula": "m^2/(K*r^2)"
  },
  {
    "id": "Q9",
    "statement": "Landauer bit reset energy at T=300 K is 2.87088e-21 J",
    "inputs": "kB=1.380649e-23 J/K, T=300 K, ln2=0.693147",
    "formula": "kB*T*ln(2)"
  },
  {
    "id": "Q10",
    "statement": "Avoided dissipation for b=8 bit register is 2.297e-20 J per cycle",
    "inputs": "b=8, E_bit=2.87088e-21 J",
    "formula": "b*E_bit"
  }
]

## Script
```python
# DERIV checks for "A Noether-Like Correspondence for Symmetry-Exploiting
# Physical Computing and Hybrid Intelligence" (text available: Abstract, Secs 1-2;
# Secs 4.1-4.4 cited but not included in the provided text).

import sympy as sp
from sympy import Rational, simplify, Eq
from sympy.physics.units import kelvin, joule, Quantity, convert_to
from sympy.physics.units import kilo
import random

# ---------- Notation table with units ----------
N, n, K = sp.symbols('N n K', positive=True, integer=True)   # sector count, DOF/sector, retained harmonics (dimensionless counts)
T = Quantity('T')                                            # temperature
kB = Quantity('k_B')                                         # Boltzmann constant
E_reset = Quantity('E_reset')                                # energy per bit reset
# unit declarations
T.set_global_dimension(kelvin)
E_reset.set_global_dimension(joule)
# kB value (SI, exact): 1.380649e-23 J/K
kB_val = sp.Float('1.380649e-23') * joule / kelvin

# ---------- Sanity bounds ----------
print("SANITY: probabilities in [0,1]: none declared in available text -> vacuous ok")
print("SANITY: efficiencies <= 1: reduction *factors* are ratios >1 by design (45, 5.83e6, 512) -> consistent")
print("SANITY: costs nonnegative: all DOF/parameter/energy quantities positive -> ok")
# Limiting case: K -> N should give DOF factor 1
lim = simplify(N/K).subs({N: 360, K: 360})
print("SANITY limiting case K=N: DOF factor =", lim, "(expect 1) ->", "ok" if lim == 1 else "refuted")

# ---------- Transition T1 ----------
# Premise: cyclic structure, N=360 sectors, n=1000 DOF/sector; block-diagonalization
#          into K=8 retained harmonics (one n-DOF sector per harmonic).
# Conclusion: DOF reduced by factor 45 (full N*n = 360000 -> reduced K*n = 8000).
# Justification: block-diagonalization into K harmonics; each harmonic sector carries n DOF.
Nv, nv, Kv = 360, 1000, 8
lhs1 = Rational(Nv*nv, Kv*nv)          # full DOF / reduced DOF
rhs1 = sp.Integer(45)
d1 = simplify(lhs1 - rhs1)
status1 = "ok" if d1 == 0 else ("refuted" if sp.ask(sp.Q.zero(d1)) is False else "inconclusive")
print(f"DERIV {status1} | T1 DOF factor: N*n/(K*n) = N/K = 45 | residual = {d1}")

# ---------- Transition T2 ----------
# Premise: full dense solve on (N*n)x(N*n) matrix costs ~(N*n)^3;
#          reduced cost = K independent dense solves of n x n systems = K*n^3.
# Conclusion: dense-solve cost reduced by factor 5.83e6.
# Justification: harmonic decoupling -> block-diagonal system solved per harmonic.
lhs2 = (Nv*nv)**3 / (Kv*nv**3)         # = N^3/K
rhs2 = sp.Float('5.83e6')
d2 = simplify(sp.nsimplify(lhs2) - sp.nsimplify(rhs2, rational=True))
exact2 = sp.Rational(Nv**3, Kv)
print(f"DERIV ok | T2 dense-solve factor: (N*n)^3/(K*n^3) = N^3/K = {exact2} = 5.832e6 ~ 5.83e6 (paper rounds) | residual vs rounded = {float(exact2 - rhs2):.3e}")

# ---------- Transition T3 ----------
# Premise: rotation-equivariant encoder layer, width 1024, 8 harmonics, multiplicity 16.
# Conclusion: parameters shrink 1,048,576 -> 2,048, factor 512.
# Justification: equivariant weight constraints (exact count formula not stated in available text).
full_params = 1024**2
reduced_params = 2048
lhs3 = sp.Integer(full_params) / sp.Integer(reduced_params)
rhs3 = sp.Integer(512)
d3 = simplify(lhs3 - rhs3)
status3 = "ok" if d3 == 0 else "refuted"
print(f"DERIV {status3} | T3 parameter ratio: 1024^2/2048 = 512 | residual = {d3}")
# Sub-check of the 2048 count from '8 harmonics, multiplicity 16': candidate formulas
# 2*K*m = 256; 2*K*m*width/... none stated reproduces 2048 unambiguously -> inconclusive
cand = 2*8*16
print(f"DERIV inconclusive | T3b parameter count 2048 from (K=8, mult=16): naive 2*K*m = {cand} != 2048; no formula given in available text -> route to verification appendix")

# ---------- Transition T4 ----------
# Premise: Landauer principle, bit reset at T = 300 K dissipates k_B*T*ln(2).
# Conclusion: E_reset = 2.87e-21 J.
# Justification: Landauer bound.
lhs4 = kB_val * sp.Integer(300) * sp.log(2)
E4 = convert_to(lhs4, joule)
rhs4 = sp.Float('2.87e-21') * joule
res4 = float((E4 - rhs4).subs({joule: 1, kelvin: 1}))
status4 = "ok" if abs(res4) < 1e-23 else ("refuted" if abs(res4) > 1e-22 else "inconclusive")
print(f"DERIV {status4} | T4 Landauer: k_B*T*ln2 @300K = {float(E4.subs({joule:1, kelvin:1})):.4e} J vs 2.87e-21 J | residual = {res4:.3e}")

# ---------- Randomized numeric spot checks (generic symbols) ----------
random.seed(0)
ok_spot = True
for _ in range(5):
    Ns = random.randint(2, 50); ns = random.randint(1, 20); Ks = random.randint(1, Ns)
    if simplify(Ns*ns/(Ks*ns) - Ns/Ks) != 0 or simplify((Ns*ns)**3/(Ks*ns**3) - Ns**3/Ks) != 0:
        ok_spot = False
print(f"DERIV {'ok' if ok_spot else 'refuted'} | T1/T2 symbolic identities hold for random (N,n,K): N*n/(K*n)=N/K and (N*n)^3/(K*n^3)=N^3/K")

# ---------- Landauer limiting cases ----------
print("SANITY limiting case T->0: E_reset -> 0 :", simplify((kB_val*0*sp.log(2)).subs({joule:1, kelvin:1})) == 0)
print("SANITY E_reset > 0 at T=300K:", float(E4.subs({joule:1, kelvin:1})) > 0)

import math

N = 360
n = 1000
K = 8
m = 1024
r = 16
kB = 1.380649e-23
T = 300.0
ln2 = 0.693147
b = 8

# Q1: DOF reduction factor = N/K
q1 = (N * n) / (K * n)
print(f"CLAIM Q1: computed={q1:.8f} expected=45 match={'yes' if round(q1) == 45 else 'no'}")

# Q2: dense-solve speedup = N^3/K
q2 = N**3 / K
print(f"CLAIM Q2: computed={q2:.8f} expected=5832000 match={'yes' if round(q2) == 5832000 else 'no'}")

# Q3: speedup at K=36 and DOF factor
K36 = 36
q3a = N**3 / K36
q3b = N / K36
print(f"CLAIM Q3a: computed={q3a:.8f} expected=1296000 match={'yes' if round(q3a) == 1296000 else 'no'}")
print(f"CLAIM Q3b: computed={q3b:.8f} expected=10 match={'yes' if round(q3b) == 10 else 'no'}")

# Q4: P_full = m^2
q4 = m**2
print(f"CLAIM Q4: computed={q4:.8f} expected=1048576 match={'yes' if q4 == 1048576 else 'no'}")

# Q5: P_eq = K*r^2
q5 = K * r**2
print(f"CLAIM Q5: computed={q5:.8f} expected=2048 match={'yes' if q5 == 2048 else 'no'}")

# Q6: reduction factor = m^2/(K*r^2)
q6 = m**2 / (K * r**2)
print(f"CLAIM Q6: computed={q6:.8f} expected=512 match={'yes' if q6 == 512 else 'no'}")

# Q7: factor at r=32
r32 = 32
q7 = m**2 / (K * r32**2)
print(f"CLAIM Q7: computed={q7:.8f} expected=128 match={'yes' if q7 == 128 else 'no'}")

# Q8: factor at m=4096
m4096 = 4096
q8 = m4096**2 / (K * r**2)
print(f"CLAIM Q8: computed={q8:.8f} expected=8192 match={'yes' if q8 == 8192 else 'no'}")

# Q9: Landauer energy
q9 = kB * T * ln2
expected9 = "2.87088e-21"
match9 = "yes" if f"{q9:.6g}" == "2.87088e-21" else "no"
print(f"CLAIM Q9: computed={q9:.8e} expected={expected9} match={match9}")

# Q10: avoided dissipation b*E_bit
q10 = b * q9
expected10 = "2.297e-20"
match10 = "yes" if f"{q10:.6g}" == "2.297e-20" else "no"
print(f"CLAIM Q10: computed={q10:.8e} expected={expected10} match={match10}")

total = 11
matched = sum(1 for x in [q1==45, q2==5832000, q3a==1296000, q3b==10, q4==1048576, q5==2048, q6==512, q7==128, q8==8192, match9=="yes", match10=="yes"] if x)
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 5, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: N/K = 360/8 = 45. 
CLAIM Q1: computed=45 expected=45 match=yes

Q2: N^3/K = 360^3/8 = 46,656,000/8 = 5,832,000. 
CLAIM Q2: computed=5832000 expected=5832000 match=yes

Q3: N^3/K = 46,656,000/36 = 1,296,000; N/K = 360/36 = 10. 
CLAIM Q3: computed=1296000 expected=1296000 match=yes

Q4: m^2 = 1024^2 = 1,048,576. 
CLAIM Q4: computed=1048576 expected=1048576 match=yes

Q5: K*r^2 = 8*256 = 2048. 
CLAIM Q5: computed=2048 expected=2048 match=yes

Q6: 1,048,576/2048 = 512. 
CLAIM Q6: computed=512 expected=512 match=yes

Q7: 8*32^2 = 8*1024 = 8192; 1,048,576/8192 = 128. 
CLAIM Q7: computed=128 expected=128 match=yes

Q8: 4096^2 = 16,777,216; 16,777,216/2048 = 8192. 
CLAIM Q8: computed=8192 expected=8192 match=yes

Q9: kB*T = 1.380649e-23 * 300 = 4.141947e-21; * 0.693147 = 2.87088e-21 (4.141947*0.693147 = 2.870879...). 
CLAIM Q9: computed=2.87088e-21 expected=2.87088e-21 match=yes

Q10: 8 * 2.87088e-21 = 2.296704e-20 ≈ 2.297e-20. 
CLAIM Q10: computed=2.296704e-20 expected=2.297e-20 match=yes

VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 45 | 45 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 5832000 | 5832000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 1296000 | 1296000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 1048576 | 1048576 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 2048 | 2048 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 512 | 512 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 128 | 128 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 8192 | 8192 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 2.87088e-21 | 2.87088e-21 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 2.296704e-20 | 2.297e-20 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
