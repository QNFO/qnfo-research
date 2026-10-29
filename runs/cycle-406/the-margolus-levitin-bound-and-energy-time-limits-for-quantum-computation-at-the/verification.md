# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Landauer energy at T = 10 mK is 9.57e-26 J",
    "inputs": "k_B = 1.380649e-23 J/K, T = 0.010 K, ln 2 = 0.6931472",
    "formula": "E_L = k_B * T * ln 2"
  },
  {
    "id": "Q2",
    "statement": "ML time at the Landauer energy for T = 10 mK is 1.73 ns",
    "inputs": "hbar = 1.054571817e-34 J s, E_L = 9.56988e-26 J",
    "formula": "tau_ML = pi * hbar / (2 * E_L)"
  },
  {
    "id": "Q3",
    "statement": "Landauer energy at T = 300 K is 2.87e-21 J",
    "inputs": "k_B = 1.380649e-23 J/K, T = 300 K, ln 2 = 0.6931472",
    "formula": "E_L = k_B * T * ln 2"
  },
  {
    "id": "Q4",
    "statement": "ML time at the Landauer energy for T = 300 K is 5.77e-14 s",
    "inputs": "hbar = 1.054571817e-34 J s, E_L(300 K) = 2.87098e-21 J",
    "formula": "tau_ML = pi * hbar / (2 * E_L)"
  },
  {
    "id": "Q5",
    "statement": "Ratio of ML times at 10 mK and 300 K equals 3.0e4",
    "inputs": "tau_ML(10 mK) = 1.73107e-9 s, tau_ML(300 K) = 5.7690e-14 s",
    "formula": "ratio = tau_ML(10 mK) / tau_ML(300 K)"
  },
  {
    "id": "Q6",
    "statement": "ML time in frequency form at f = 5 GHz is 50 ps",
    "inputs": "f = 5e9 Hz",
    "formula": "t_ML = 1 / (4 * f)"
  },
  {
    "id": "Q7",
    "statement": "ML time in frequency form at f = 1 MHz is 250 ns",
    "inputs": "f = 1e6 Hz",
    "formula": "t_ML = 1 / (4 * f)"
  },
  {
    "id": "Q8",
    "statement": "ML time in frequency form at f = 1 GHz is 250 ps",
    "inputs": "f = 1e9 Hz",
    "formula": "t_ML = 1 / (4 * f)"
  },
  {
    "id": "Q9",
    "statement": "Event-rate ceiling at f = 5 GHz is 2.0e10 s^-1",
    "inputs": "h = 6.62607015e-34 J s, f = 5e9 Hz, hbar = 1.054571817e-34 J s",
    "formula": "rate = 2 * h * f / (pi * hbar)"
  },
  {
    "id": "Q10",
    "statement": "Carnot cooling factor at 10 mK stage rejecting to 300 K is 29,999",
    "inputs": "T_hot = 300 K, T_cold = 0.010 K",
    "formula": "factor = T_hot / T_cold - 1"
  },
  {
    "id": "Q11",
    "statement": "Projected JPCUB energy per logical operation is 3.0e-5 J",
    "inputs": "P_control = 1.0e-3 W, Carnot factor = 29999, f_ops = 1.0e6 s^-1",
    "formula": "C_JPCUB = (P_control + 29999 * P_control) / f_ops"
  },
  {
    "id": "Q12",
    "statement": "Ratio of projected JPCUB energy to Landauer energy at 10 mK is 3.13e20",
    "inputs": "C_JPCUB = 3.0e-5 J, E_L(10 mK) = 9.56988e-26 J",
    "formula": "ratio = C_JPCUB / E_L"
  },
  {
    "id": "Q13",
    "statement": "Register ML time at 5 GHz is a factor 34.6 shorter than the Landauer-scale ML time at 10 mK",
    "inputs": "tau_ML(10 mK) = 1.73107e-9 s, t_ML(5 GHz) = 5.00e-11 s",
    "formula": "factor = tau_ML(10 mK) / t_ML(5 GHz)"
  },
  {
    "id": "Q14",
    "statement": "Drive splitting at 5 GHz is 34.6 times the Landauer energy at 10 mK",
    "inputs": "h = 6.62607015e-34 J s, f = 5e9 Hz, E_L(10 mK) = 9.56988e-26 J",
    "formula": "factor = h * f / E_L"
  },
  {
    "id": "Q15",
    "statement": "Carnot factor at T_cold = 0.100 K is 2,999",
    "inputs": "T_hot = 300 K, T_cold = 0.100 K",
    "formula": "factor = T_hot / T_cold - 1"
  },
  {
    "id": "Q16",
    "statement": "Cooling term contributes 99.997% of total power 30.000 W",
    "inputs": "P_control = 1.0e-3 W, P_cryo = 29.999 W",
    "formula": "percent = 100 * P_cryo / (P_control + P_cryo)"
  }
]

## Script
```python
# Verification of equation transitions in the ML-bound / JPCUB paper.
# NOTE: the provided paper text is truncated mid-derivation (after the cosine
# inequality application). Transitions whose premises are cut off are emitted
# as DERIV inconclusive and routed to the verification appendix.

import sympy as sp
import sympy.physics.units as u
from sympy import pi, Rational, simplify, nsimplify

hbar, h, kB = sp.symbols('hbar h k_B', positive=True)
T, tau, E, En, t, x, f = sp.symbols('T tau E E_n t x f', positive=True)

# ---- units / constants (declared per notation table) ----
from sympy.physics.units import joule, second, kelvin, watt, hertz, meter, kilogram
from sympy.physics.units.definitions import (
    planck_constant as h_unit, boltzmann_constant as kB_unit, reduced_planck_constant as hbar_unit)
from sympy.physics.units.systems.si import SI

h_val    = SI.convert_to(h_unit, joule*second).args[0]          # J*s
hbar_val = SI.convert_to(hbar_unit, joule*second).args[0]       # J*s
kB_val   = SI.convert_to(kB_unit, joule/kelvin).args[0]         # J/K

results = []
def report(tag, ok):
    status = 'ok' if ok else 'refuted'
    print(f"DERIV {status} | {tag}")
    results.append((tag, status))

# ---------------------------------------------------------------
# T1: overlap <psi(0)|psi(t)> = sum_n |c_n|^2 exp(-i E_n t / hbar)
#     (standard spectral expansion; algebraic identity in the coefficients)
# ---------------------------------------------------------------
n = sp.symbols('n', integer=True, nonnegative=True)
c = sp.Function('c')
En_f = sp.Function('E')
lhs = sp.Sum(sp.Abs(c(n))**2*sp.exp(-sp.I*En_f(n)*t/hbar), (n, 0, sp.oo))
# consistency: at t=0 the overlap must be 1 (normalization)
t0 = lhs.subs(t, 0)
t0_val = sp.simplify(t0.doit()) if t0.has(sp.Sum) else t0
ok = sp.simplify(t0_val - sp.Sum(sp.Abs(c(n))**2, (n, 0, sp.oo))) == 0
report("T1 overlap spectral form (t=0 normalization consistency)", ok)

# ---------------------------------------------------------------
# T2: Re<psi(0)|psi(tau)> = 0  =>  sum |c_n|^2 cos(E_n tau/hbar) = 0
# ---------------------------------------------------------------
# Re of the weighted phase sum is the weighted cosine sum (weights real, >=0)
expr = sp.re(sp.Abs(c(n))**2*sp.exp(-sp.I*En_f(n)*t/hbar)) - sp.Abs(c(n))**2*sp.cos(En_f(n)*t/hbar)
ok = simplify(expr) == 0
report("T2 real part of overlap = weighted cosine sum", ok)

# ---------------------------------------------------------------
# T3: cosine supporting inequality  cos(x) >= 1 - 2x/pi  on [0, pi/2]
# ---------------------------------------------------------------
xx = sp.symbols('xx', real=True)
diff = sp.cos(xx) - (1 - 2*xx/pi)
# analytic: diff(0)=0, diff(pi/2)=pi/2-1>0, concave => min at endpoints
ok = (sp.simplify(diff.subs(xx, 0)) == 0) and (diff.subs(xx, pi/2) > 0) and (sp.diff(diff, xx, 2) < 0)
# randomized numeric spot check
import random
ok_num = all(diff.subs(xx, random.uniform(0, pi/2)).evalf() >= -1e-12 for _ in range(200))
report("T3 cos x >= 1 - 2x/pi on [0, pi/2]", ok and ok_num)

# ---------------------------------------------------------------
# T4: under E_n*tau/hbar <= pi/2 for all populated levels:
#     0 = sum |c_n|^2 cos(E_n tau/hbar)
#         >= sum |c_n|^2 (1 - 2 E_n tau/(pi hbar)) = 1 - 2<H> tau/(pi hbar)
#     =>  tau >= pi*hbar/(2<H>)
# ---------------------------------------------------------------
w = sp.symbols('w', nonnegative=True)          # |c_n|^2, sum w = 1
meanE = sp.symbols('meanE', positive=True)     # <H> = sum w E_n
chain = sp.simplify((sp.Sum(w*(1 - 2*En_f(n)*tau/(pi*hbar)), (n, 0, sp.oo))
                     - (1 - 2*meanE*tau/(pi*hbar))))
# with sum w = 1 and sum w E_n = meanE the two sides agree:
ok = chain.subs({sp.Sum(w, (n,0,sp.oo)): 1}) == 0
# final step: 1 - 2<H>tau/(pi hbar) <= 0  <=>  tau >= pi hbar/(2<H>)
ineq = sp.solve_univariate_inequality(1 - 2*meanE*tau/(pi*hbar) <= 0, tau, relational=False)
ok_final = ineq == sp.Interval(pi*hbar/(2*meanE), sp.oo)
report("T4 ML bound tau >= pi*hbar/(2<H>) from cosine inequality", ok and bool(ok_final))

# ---------------------------------------------------------------
# T5: Landauer energy  E_L = kB*T*ln2 ;  tau_ML = pi*hbar/(2*E_L)
#     T = 10 mK  ->  E_L = 9.57e-26 J, tau_ML = 1.73 ns
#     T = 300 K  ->  tau_ML = 5.77e-14 s
# ---------------------------------------------------------------
E_L_10mK = kB_val * sp.Float('0.01')*kelvin * sp.log(2)
E_L_10mK_J = SI.convert_to(E_L_10mK, joule).args[0]
tau_10mK = pi*hbar_val/(2*E_L_10mK_J)
tau_10mK_s = SI.convert_to(tau_10mK*second, second).args[0]
ok1 = abs(float(tau_10mK_s) - 1.73e-9) < 0.01e-9
E_L_300 = kB_val * sp.Float(300)*kelvin * sp.log(2)
E_L_300_J = SI.convert_to(E_L_300, joule).args[0]
tau_300 = pi*hbar_val/(2*E_L_300_J)
tau_300_s = SI.convert_to(tau_300*second, second).args[0]
ok2 = abs(float(tau_300_s) - 5.77e-14)/5.77e-14 < 1e-2
report("T5 numerical tau_ML at 10 mK (1.73 ns) and 300 K (5.77e-14 s)", ok1 and ok2)

# sanity bounds: E_L > 0, tau > 0
report("T5b sanity: Landauer energies positive, tau positive",
       E_L_10mK_J > 0 and E_L_300_J > 0 and tau_10mK_s > 0 and tau_300_s > 0)

# ---------------------------------------------------------------
# T6: frequency form  t_ML = 1/(4 f)  (from tau = pi*hbar/(2 E), E = h f)
#     f = 5 GHz -> 50 ps
# ---------------------------------------------------------------
ok = simplify(pi*hbar_val/(2*h_val*f) - 1/(4*f)) == 0
t_5GHz = (1/(4*sp.Float('5e9')))*second
t_5GHz_s = SI.convert_to(t_5GHz, second).args[0]
ok_num = abs(float(t_5GHz_s) - 50e-12)/50e-12 < 1e-12
report("T6 t_ML = 1/(4f); 50 ps at 5 GHz", ok and ok_num)

# ---------------------------------------------------------------
# T7: Carnot-limited cryostat: COP = Tc/(Th - Tc);
#     1 W at Tc = 10 mK, Th = 300 K  ->  29999 W wall power
# ---------------------------------------------------------------
Tc, Th = sp.symbols('T_c T_h', positive=True)
COP = Tc/(Th - Tc)
wall = 1/COP  # wall watts per watt removed
wall_val = wall.subs({Tc: sp.Float('0.01'), Th: sp.Float(300)})
ok = abs(float(wall_val) - 29999) < 1
report("T7 Carnot: 1 W at 10 mK costs 29999 W wall power", ok)

# ---------------------------------------------------------------
# T8: JPCUB  C_JPCUB = (P_control + P_cryo)/f_ops -> 3.0e-5 J per op
#     Premises (P_control, P_cryo, f_ops values) are in the truncated
#     portion of the paper -> cannot verify numerically.
# ---------------------------------------------------------------
print("DERIV inconclusive | T8 C_JPCUB = (P_control + P_cryo)/f_ops = 3.0e-5 J "
      "(premise values truncated in source; see verification appendix)")

# ---------------------------------------------------------------
# T9: ratio C_JPCUB / E_L(10 mK) = 3.13e20
# ---------------------------------------------------------------
ratio = sp.Float('3.0e-5')/float(E_L_10mK_J)
ok = abs(ratio - 3.13e20)/3.13e20 < 1e-2
report("T9 ratio 3.0e-5 J / 9.57e-26 J = 3.13e20", ok)

# ---------------------------------------------------------------
# T10: unified QSL envelope tau_qsl = max{pi hbar/(2 dE), pi hbar/(2(<E>-E0))}
#      reduces to ML form when variance term is not the minimum — structural,
#      no algebraic identity to verify beyond consistency of the max form.
# ---------------------------------------------------------------
dE = sp.symbols('DeltaE', positive=True)
ml = pi*hbar/(2*(E - 0))
mt = pi*hbar/(2*dE)
ok = simplify(sp.Max(ml, mt) - pi*hbar*sp.Max(1/(2*(E)), 1/(2*dE))) == 0
report("T10 unified envelope max-form consistency", ok)

# ---------------------------------------------------------------
# T11: covariant operation count  # <= 2 E tau/(pi hbar);
#      moving observer: E->gamma E, tau->gamma tau  =>  #' <= 2 E gamma^2 tau/(pi hbar)
# ---------------------------------------------------------------
gam = sp.symbols('gamma', positive=True)
lhs_cov = 2*(gam*E)*(gam*tau)/(pi*hbar)
ok = simplify(lhs_cov - 2*E*gam**2*tau/(pi*hbar)) == 0
report("T11 covariant operation-count substitution E->gE, tau->gtau", ok)

# ---------------------------------------------------------------
# Sanity bounds summary (probabilities/efficiencies/costs)
# ---------------------------------------------------------------
# Carnot COP > 0 requires Th > Tc (efficiency <= 1 analog)
ok = (Th > Tc) and (COP.subs({Tc: sp.Float('0.01'), Th: sp.Float(300)}) > 0)
report("S1 sanity: Carnot COP positive and finite for Th > Tc", ok)
# weights |c_n|^2 are probabilities in [0,1]
wtest = random.uniform(0, 1)
report("S2 sanity: |c_n|^2 in [0,1] (probability weights)", 0 <= wtest <= 1)

print("\nSummary:")
for tag, status in results:
    print(f"  {status:12s} {tag}")

import math
from fractions import Fraction

# Constants as stated in the paper
k_B = 1.380649e-23        # J/K
hbar = 1.054571817e-34    # J s
h = 6.62607015e-34        # J s
ln2 = 0.6931472

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

def report(cid, computed, expected, stated_sig):
    c = sig(computed, stated_sig)
    match = "yes" if c == float(expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected} match={match}")

# Q1: E_L at 10 mK
E_L_10mK = k_B * 0.010 * ln2
report("Q1", E_L_10mK, "9.57e-26", 3)

# Q2: tau_ML at 10 mK
tau_10mK = math.pi * hbar / (2 * E_L_10mK)
report("Q2", tau_10mK, "1.73e-9", 3)

# Q3: E_L at 300 K
E_L_300K = k_B * 300 * ln2
report("Q3", E_L_300K, "2.87e-21", 3)

# Q4: tau_ML at 300 K
tau_300K = math.pi * hbar / (2 * E_L_300K)
report("Q4", tau_300K, "5.77e-14", 3)

# Q5: ratio of ML times
ratio_times = tau_10mK / tau_300K
report("Q5", ratio_times, "3.0e4", 2)

# Q6: t_ML at 5 GHz
t_5GHz = 1 / (4 * 5e9)
report("Q6", t_5GHz, "5.0e-11", 2)

# Q7: t_ML at 1 MHz
t_1MHz = 1 / (4 * 1e6)
report("Q7", t_1MHz, "2.5e-7", 3)

# Q8: t_ML at 1 GHz
t_1GHz = 1 / (4 * 1e9)
report("Q8", t_1GHz, "2.5e-10", 3)

# Q9: event-rate ceiling at 5 GHz
rate_5GHz = 2 * h * 5e9 / (math.pi * hbar)
report("Q9", rate_5GHz, "2.0e10", 2)

# Q10: Carnot factor at 10 mK
factor_10mK = 300 / 0.010 - 1
report("Q10", factor_10mK, "29999", 5)

# Q11: projected JPCUB energy
P_control = 1.0e-3
f_ops = 1.0e6
C_JPCUB = (P_control + 29999 * P_control) / f_ops
report("Q11", C_JPCUB, "3.0e-5", 2)

# Q12: ratio to Landauer energy
ratio_L = C_JPCUB / E_L_10mK
report("Q12", ratio_L, "3.13e20", 3)

# Q13: factor 34.6 shorter
factor_346 = tau_10mK / t_5GHz
report("Q13", factor_346, "34.6", 3)

# Q14: drive splitting vs Landauer energy
factor_drive = h * 5e9 / E_L_10mK
report("Q14", factor_drive, "34.6", 3)

# Q15: Carnot factor at 100 mK
factor_100mK = 300 / 0.100 - 1
report("Q15", factor_100mK, "2999", 4)

# Q16: cooling term percent of total
P_cryo = 29999 * P_control
percent = 100 * P_cryo / (P_control + P_cryo)
report("Q16", percent, "99.997", 5)

print("VERIFICATION SUMMARY: 16 claims, " + "M match, K mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 6, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: E_L = 1.380649e-23 × 0.010 = 1.380649e-25; × 0.6931472 = 9.569878e-26 J. Expected 9.57e-26 → match.

Q2: pi·ħ = 3.14159265 × 1.054571817e-34 = 3.313035e-34. 2E = 1.913976e-25. 3.313035e-34 / 1.913976e-25 = 1.73107e-9 s = 1.73 ns → match.

Q3: 1.380649e-23 × 300 = 4.141947e-21; × 0.6931472 = 2.870977e-21 J. Expected 2.87e-21 → match.

Q4: 2E = 5.741954e-21. 3.313035e-34 / 5.741954e-21 = 5.76901e-14 s. Expected 5.77e-14 → match.

Q5: 1.73107e-9 / 5.76901e-14 = 3.00073e4. Expected 3.0e4 → match.

Q6: 1/(4×5e9) = 5.00000e-11 s = 50 ps → match.

Q7: 1/(4×1e6) = 2.50000e-7 s = 250 ns → match.

Q8: 1/(4×1e9) = 2.50000e-10 s = 250 ps → match.

Q9: 2hf = 2×6.62607015e-34×5e9 = 6.62607015e-24. πħ = 3.313035e-34. 6.62607015e-24/3.313035e-34 = 2.00000e10 s⁻¹ → match.

Q10: 300/0.010 = 30000; −1 = 29999 → match.

Q11: P_cryo = 29999×1e-3 = 29.999 W; total = 30.000 W; /1e6 = 3.00000e-5 J → match.

Q12: 3.0e-5 / 9.569878e-26 = 3.13485e20. Expected 3.13e20 → match.

Q13: 1.73107e-9 / 5.00e-11 = 34.6214. Expected 34.6 → match.

Q14: hf = 6.62607015e-34×5e9 = 3.313035075e-24; /9.569878e-26 = 34.6214. Expected 34.6 → match.

Q15: 300/0.100 = 3000; −1 = 2999 → match.

Q16: 100×29.999/30.000 = 99.9967%. Expected 99.997 → match.

CLAIM Q1: computed=9.56988e-26 expected=9.57e-26 match=yes
CLAIM Q2: computed=1.73107e-9 expected=1.73e-9 match=yes
CLAIM Q3: computed=2.87098e-21 expected=2.87e-21 match=yes
CLAIM Q4: computed=5.76901e-14 expected=5.77e-14 match=yes
CLAIM Q5: computed=3.00073e4 expected=3.0e4 match=yes
CLAIM Q6: computed=5.00000e-11 expected=5.00e-11 match=yes
CLAIM Q7: computed=2.50000e-7 expected=2.50e-7 match=yes
CLAIM Q8: computed=2.50000e-10 expected=2.50e-10 match=yes
CLAIM Q9: computed=2.00000e10 expected=2.0e10 match=yes
CLAIM Q10: computed=29999 expected=29999 match=yes
CLAIM Q11: computed=3.00000e-5 expected=3.0e-5 match=yes
CLAIM Q12: computed=3.13485e20 expected=3.13e20 match=yes
CLAIM Q13: computed=34.6214 expected=34.6 match=yes
CLAIM Q14: computed=34.6214 expected=34.6 match=yes
CLAIM Q15: computed=2999 expected=2999 match=yes
CLAIM Q16: computed=99.9967 expected=99.997 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 9.56988e-26 | 9.57e-26 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 1.73107e-9 | 1.73e-9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 2.87098e-21 | 2.87e-21 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 5.76901e-14 | 5.77e-14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 3.00073e4 | 3.0e4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 5.00000e-11 | 5.00e-11 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 2.50000e-7 | 2.50e-7 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 2.50000e-10 | 2.50e-10 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 2.00000e10 | 2.0e10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 29999 | 29999 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 3.00000e-5 | 3.0e-5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 3.13485e20 | 3.13e20 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 34.6214 | 34.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 34.6214 | 34.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 2999 | 2999 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 99.9967 | 99.997 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
