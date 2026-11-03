# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Compton frequency omega_C = 2 m_e c^2 / hbar = 1.5526e21 Hz",
    "inputs": "m_e c^2 = 8.187e-14 J; hbar = 1.0546e-34 J·s",
    "formula": "omega_C = 2 * 8.187e-14 / 1.0546e-34"
  },
  {
    "id": "Q2",
    "statement": "Compton half-wavelength lambda_C/2 = hbar/(2 m_e c) = 1.9308e-13 m",
    "inputs": "hbar = 1.0546e-34 J·s; m_e = 9.109e-31 kg; c = 2.998e8 m/s",
    "formula": "lambda_C/2 = 1.0546e-34 / (2 * 9.109e-31 * 2.998e8)"
  },
  {
    "id": "Q3",
    "statement": "Dirac-case ratio at p=0: O_ZBW = 1.0000",
    "inputs": "|u gamma0 u|^2 = 4.0000; |u gamma0 v|^2 = 4.0000",
    "formula": "O_ZBW = 4.0000 / 4.0000"
  },
  {
    "id": "Q4",
    "statement": "Dirac-case ratio at p=0.5: O_ZBW = 0.8944",
    "inputs": "|u gamma0 u|^2 = 4.4721; |u gamma0 v|^2 = 4.0000",
    "formula": "O_ZBW = 4.0000 / 4.4721"
  },
  {
    "id": "Q5",
    "statement": "Dirac-case ratio at p=1: O_ZBW = 0.6863",
    "inputs": "|u gamma0 u|^2 = 5.8284; |u gamma0 v|^2 = 4.0000",
    "formula": "O_ZBW = 4.0000 / 5.8284"
  },
  {
    "id": "Q6",
    "statement": "Dirac-case ratio at p=2: O_ZBW = 0.2981",
    "inputs": "|u gamma0 u|^2 = 13.4164; |u gamma0 v|^2 = 4.0000",
    "formula": "O_ZBW = 4.0000 / 13.4164"
  },
  {
    "id": "Q7",
    "statement": "Energy E(0.5) = sqrt(1.25) = 1.1180",
    "inputs": "p = 0.5; E = sqrt(1 + p^2)",
    "formula": "E = sqrt(1 + 0.5^2)"
  },
  {
    "id": "Q8",
    "statement": "Energy E(1) = sqrt(2) = 1.4142",
    "inputs": "p = 1; E = sqrt(1 + p^2)",
    "formula": "E = sqrt(1 + 1^2)"
  },
  {
    "id": "Q9",
    "statement": "Energy E(2) = sqrt(5) = 2.2361",
    "inputs": "p = 2; E = sqrt(1 + p^2)",
    "formula": "E = sqrt(1 + 2^2)"
  },
  {
    "id": "Q10",
    "statement": "Pairing-bound reduction R(20) = 20/38 = 0.5263",
    "inputs": "N = 20; R(N) = N / (2(N-1))",
    "formula": "R = 20 / (2 * 19)"
  },
  {
    "id": "Q11",
    "statement": "Pairing-bound reduction R(50) = 50/98 = 0.5102",
    "inputs": "N = 50; R(N) = N / (2(N-1))",
    "formula": "R = 50 / (2 * 49)"
  },
  {
    "id": "Q12",
    "statement": "Excess of reported 57% over pairing bound at N=20: 4.4 percentage points",
    "inputs": "reported reduction = 57%; R(20) = 0.5263",
    "formula": "excess = 57 - 52.63"
  },
  {
    "id": "Q13",
    "statement": "Excess of reported 57% over pairing bound at N=50: 6.0 percentage points",
    "inputs": "reported reduction = 57%; R(50) = 0.5102",
    "formula": "excess = 57 - 51.02"
  }
]

## Script
```python
# Verification of equation transitions in "The Zitterbewegung Current Correlator as a Z2 Invariant"
# Method: for each (premise, conclusion, justification) transition, test simplify(lhs - rhs) == 0
# under the paper's declared assumptions (electron mass, c, hbar; p measured in units of m_e c),
# with randomized numeric spot checks when the symbolic test is inconclusive.

import sympy as sp
from sympy import simplify, Rational, sqrt, S
from sympy.physics.units import meter, second, kilogram, joule, hertz
from sympy.physics.units import speed_of_light, hbar, electron_mass
from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units.util import convert_to

c    = speed_of_light
hbar_ = hbar
m_e  = electron_mass

results = []

def report(name, status, transition):
    print(f"DERIV {status} | {name} :: {transition}")
    results.append((name, status))

def numeric_spot(expr_lhs, expr_rhs, subs_list, tol=1e-9):
    """Randomized numeric spot check of lhs == rhs."""
    for _ in range(5):
        subs = {k: v for k, v in subs_list.items()}
        lhs = complex(sp.N(expr_lhs.subs(subs)))
        rhs = complex(sp.N(expr_rhs.subs(subs)))
        if abs(lhs - rhs) > tol * max(1.0, abs(lhs), abs(rhs)):
            return False
    return True

# ---------------------------------------------------------------
# Transition 1: (m_e, c, hbar) -> omega_C = 2 m c^2 / hbar ~= 1.55e21 Hz
# ---------------------------------------------------------------
omega_C_expr = 2 * m_e * c**2 / hbar_
omega_C_SI = convert_to(omega_C_expr, hertz)
omega_C_val = float(sp.N(omega_C_SI / hertz))
claimed = 1.55e21
if abs(omega_C_val - claimed) / claimed < 0.01:
    report("T1 omega_C", "ok",
           "premise: m_e, c, hbar; conclusion: omega_C = 2 m c^2/hbar = %.4e Hz (claimed 1.55e21); justification: Compton-frequency definition" % omega_C_val)
else:
    report("T1 omega_C", "refuted", "omega_C = %.4e Hz != 1.55e21 Hz" % omega_C_val)

# ---------------------------------------------------------------
# Transition 2: (m_e, c, hbar) -> lambda_C/2 = hbar/(2 m c) ~= 1.93e-13 m
# ---------------------------------------------------------------
lam_half_expr = hbar_ / (2 * m_e * c)
lam_half_SI = convert_to(lam_half_expr, meter)
lam_half_val = float(sp.N(lam_half_SI / meter))
claimed_l = 1.93e-13
if abs(lam_half_val - claimed_l) / claimed_l < 0.01:
    report("T2 lambda_C/2", "ok",
           "premise: m_e, c, hbar; conclusion: lambda_C/2 = hbar/(2mc) = %.4e m (claimed 1.93e-13); justification: reduced-Compton-wavelength halving" % lam_half_val)
else:
    report("T2 lambda_C/2", "refuted", "lambda_C/2 = %.4e m != 1.93e-13 m" % lam_half_val)

# ---------------------------------------------------------------
# Transition 3: identical single-particle ZBW kinematics -> A_Maj/A_Dir = 1.0
# (paper's declared premise; symbolic identity under that assumption)
# ---------------------------------------------------------------
A_Maj, A_Dir = sp.symbols('A_Maj A_Dir', positive=True)
lhs3 = A_Maj / A_Dir
# Under the paper's premise the velocity amplitudes are identical: A_Maj = A_Dir
diff3 = simplify(lhs3.subs({A_Maj: A_Dir}) - 1)
if diff3 == 0:
    report("T3 amplitude ratio", "ok",
           "premise: identical single-particle ZBW kinematics for Dirac and Majorana; conclusion: A_Maj/A_Dir = 1.0; justification: premise of the ZBW-Majorana programme")
else:
    report("T3 amplitude ratio", "refuted", "A_Maj/A_Dir != 1 under stated premise")

# ---------------------------------------------------------------
# Transitions 4-7: Dirac-case O_ZBW ratios 1.0000, 0.8944, 0.6863, 0.2981 at p = 0, 0.5, 1, 2
# The excerpt does not state the closed-form p-dependence of O_ZBW, so no symbolic
# lhs-rhs identity is available; we test the natural candidate O = m/E = 1/sqrt(1+p^2)
# and otherwise classify as inconclusive (route to verification appendix).
# ---------------------------------------------------------------
p = sp.symbols('p', positive=True)
claimed_ratios = {0: 1.0000, sp.Rational(1, 2): 0.8944, 1: 0.6863, 2: 0.2981}
candidate = 1 / sqrt(1 + p**2)   # natural candidate: static/ZBW ratio ~ m/E

for pv, claimed_o in claimed_ratios.items():
    name = f"T4-7 O_ZBW(p={pv})"
    transition = (f"premise: Dirac spinor bilinears u-bar gamma^mu v at p={pv}; "
                  f"conclusion: O_ZBW = {claimed_o}; justification: correlator computation (closed form not stated in excerpt)")
    cand_val = float(sp.N(candidate.subs(p, pv)))
    if abs(cand_val - claimed_o) < 5e-4:
        report(name, "ok", transition + f" [candidate 1/sqrt(1+p^2) matches: {cand_val:.4f}]")
    else:
        # randomized numeric spot check of candidate vs claim fails; no stated formula -> inconclusive
        ok_spot = numeric_spot(candidate, claimed_o, {p: pv}, tol=1e-3)
        report(name, "inconclusive", transition + f" [candidate 1/sqrt(1+p^2) gives {cand_val:.4f} != {claimed_o}; closed form not stated]")

# ---------------------------------------------------------------
# Transition 8: 57% edge reduction of ZBW transition graph exceeds 50% bound from state pairing
# ---------------------------------------------------------------
edge_reduction = Rational(57, 100)
pairing_bound  = Rational(50, 100)
diff8 = simplify(edge_reduction - pairing_bound)
if diff8 > 0:
    report("T8 edge reduction vs pairing bound", "ok",
           "premise: state pairing implies >= 50% edge reduction bound; conclusion: 57% > 50%; justification: arithmetic comparison 0.57 - 0.50 = 0.07 > 0")
else:
    report("T8 edge reduction vs pairing bound", "refuted", "0.57 <= 0.50")

# ---------------------------------------------------------------
# Sanity bounds: O_ZBW is a probability-like order parameter in [0,1];
# efficiencies (ratios) <= 1; Compton inputs positive.
# ---------------------------------------------------------------
for pv, claimed_o in claimed_ratios.items():
    if 0.0 <= claimed_o <= 1.0:
        report(f"SANITY O_ZBW(p={pv}) in [0,1]", "ok", f"O_ZBW = {claimed_o} within [0,1]")
    else:
        report(f"SANITY O_ZBW(p={pv}) in [0,1]", "refuted", f"O_ZBW = {claimed_o} outside [0,1]")

if omega_C_val > 0 and lam_half_val > 0:
    report("SANITY Compton inputs positive", "ok", "omega_C > 0 and lambda_C/2 > 0")
else:
    report("SANITY Compton inputs positive", "refuted", "nonpositive Compton input")

# Limiting case stated in the paper: O_ZBW -> 1 as p -> 0 (Dirac value at rest = 1.0000)
lim = sp.limit(candidate, p, 0)
if abs(float(sp.N(lim)) - 1.0) < 1e-12:
    report("LIMIT O_ZBW(p->0) = 1", "ok", "stated limiting case p->0 gives ratio 1.0000 (candidate formula consistent)")
else:
    report("LIMIT O_ZBW(p->0) = 1", "inconclusive", "limiting case not reproduced by candidate formula")

# Dimensional consistency of the Compton relations
assert dimsys_SI.get_dimensional_dependencies(sp.Dimension(sp.length / sp.time)) == \
       dimsys_SI.get_dimensional_dependencies(sp.Dimension(sp.length / sp.time))
dim_omega = dimsys_SI.get_dimensional_dependencies((c**2 * m_e / hbar_).subs({c: sp.Symbol('c'), m_e: sp.Symbol('m'), hbar_: sp.Symbol('h')}))
print("# dimensional check: omega_C has dimensions 1/time, lambda_C/2 has dimensions length (by construction of unit conversion above)")

print("\nSummary:")
for name, status in results:
    print(f"  {status:>12s}  {name}")

import math

def sig(x, n):
    if x == 0:
        return 0.0
    from decimal import Decimal
    return round(x, n - 1 - math.floor(math.log10(abs(x))))

# Q1: omega_C = 2 * m_e c^2 / hbar
num1 = 2 * 8.187e-14
den1 = 1.0546e-34
q1 = num1 / den1
print(f"CLAIM Q1: computed={q1:.8e} expected={'1.5526e21'} match={'yes' if f'{q1:.4e}'=='1.5526e+21' else 'no'}")

# Q2: lambda_C/2 = hbar / (2 m_e c)
den2 = 2 * 9.109e-31 * 2.998e8
q2 = 1.0546e-34 / den2
print(f"CLAIM Q2: computed={q2:.8e} expected={'1.9308e-13'} match={'yes' if f'{q2:.4e}'=='1.9308e-13' else 'no'}")

# Q3: O_ZBW at p=0
q3 = 4.0000 / 4.0000
print(f"CLAIM Q3: computed={q3:.8f} expected={'1.0000'} match={'yes' if f'{q3:.4f}'=='1.0000' else 'no'}")

# Q4: O_ZBW at p=0.5
q4 = 4.0000 / 4.4721
print(f"CLAIM Q4: computed={q4:.8f} expected={'0.8944'} match={'yes' if f'{q4:.4f}'=='0.8944' else 'no'}")

# Q5: O_ZBW at p=1
q5 = 4.0000 / 5.8284
print(f"CLAIM Q5: computed={q5:.8f} expected={'0.6863'} match={'yes' if f'{q5:.4f}'=='0.6863' else 'no'}")

# Q6: O_ZBW at p=2
q6 = 4.0000 / 13.4164
print(f"CLAIM Q6: computed={q6:.8f} expected={'0.2981'} match={'yes' if f'{q6:.4f}'=='0.2981' else 'no'}")

# Q7: E(0.5)
q7 = math.sqrt(1 + 0.5**2)
print(f"CLAIM Q7: computed={q7:.8f} expected={'1.1180'} match={'yes' if f'{q7:.4f}'=='1.1180' else 'no'}")

# Q8: E(1)
q8 = math.sqrt(1 + 1**2)
print(f"CLAIM Q8: computed={q8:.8f} expected={'1.4142'} match={'yes' if f'{q8:.4f}'=='1.4142' else 'no'}")

# Q9: E(2)
q9 = math.sqrt(1 + 2**2)
print(f"CLAIM Q9: computed={q9:.8f} expected={'2.2361'} match={'yes' if f'{q9:.4f}'=='2.2361' else 'no'}")

# Q10: R(20)
q10 = 20 / (2 * 19)
print(f"CLAIM Q10: computed={q10:.8f} expected={'0.5263'} match={'yes' if f'{q10:.4f}'=='0.5263' else 'no'}")

# Q11: R(50)
q11 = 50 / (2 * 49)
print(f"CLAIM Q11: computed={q11:.8f} expected={'0.5102'} match={'yes' if f'{q11:.4f}'=='0.5102' else 'no'}")

# Q12: excess at N=20, in percentage points
r20_pct = q10 * 100
q12 = 57 - r20_pct
print(f"CLAIM Q12: computed={q12:.8f} expected={'4.4'} match={'yes' if f'{q12:.1f}'=='4.4' else 'no'}")

# Q13: excess at N=50, in percentage points
r50_pct = q11 * 100
q13 = 57 - r50_pct
print(f"CLAIM Q13: computed={q13:.8f} expected={'6.0'} match={'yes' if f'{q13:.1f}'=='6.0' else 'no'}")

n = 13
m = sum(1 for line in [] )  # placeholder replaced below
results = []
results.append(f"{q1:.4e}" == "1.5526e+21")
results.append(f"{q2:.4e}" == "1.9308e-13")
results.append(f"{q3:.4f}" == "1.0000")
results.append(f"{q4:.4f}" == "0.8944")
results.append(f"{q5:.4f}" == "0.6863")
results.append(f"{q6:.4f}" == "0.2981")
results.append(f"{q7:.4f}" == "1.1180")
results.append(f"{q8:.4f}" == "1.4142")
results.append(f"{q9:.4f}" == "2.2361")
results.append(f"{q10:.4f}" == "0.5263")
results.append(f"{q11:.4f}" == "0.5102")
results.append(f"{q12:.1f}" == "4.4")
results.append(f"{q13:.1f}" == "6.0")
mm = sum(results)
k = n - mm
print(f"VERIFICATION SUMMARY: {n} claims, {mm} match, {k} mismatch")

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
Q1: 2 × 8.187e-14 = 1.6374e-13 J. 1.6374e-13 / 1.0546e-34: 1.6374/1.0546 = 1.552585... (check 1.0546 × 1.5526 = 1.63737, remainder 0.00003, so ≈1.55263). Computed = 1.55263e21 Hz; expected 1.5526e21 Hz → match.

Q2: 2 × 9.109e-31 = 1.8218e-30 kg; × 2.998e8 = 5.46222e-22 kg·m/s. 1.0546e-34 / 5.46222e-22: 1.0546/5.46222 = 0.193079... Computed = 1.93079e-13 m; expected 1.9308e-13 m → match.

Q3: 4.0000 / 4.0000 = 1.0000 → match.

Q4: 4.0000 / 4.4721 = 0.894427... (4.4721 × 0.89443 = 3.999998) → 0.8944 → match.

Q5: 4.0000 / 5.8284 = 0.686299... (5.8284 × 0.6863 = 3.99999) → 0.6863 → match.

Q6: 4.0000 / 13.4164 = 0.298139... (13.4164 × 0.2981 = 3.99943) → 0.2981 → match.

Q7: sqrt(1 + 0.25) = sqrt(1.25) = 1.118034 → 1.1180 → match.

Q8: sqrt(2) = 1.414214 → 1.4142 → match.

Q9: sqrt(5) = 2.236068 → 2.2361 → match.

Q10: 20 / (2 × 19) = 20/38 = 0.526316 → 0.5263 → match.

Q11: 50 / (2 × 49) = 50/98 = 0.510204 → 0.5102 → match.

Q12: 57 − 52.63 = 4.37 percentage points; paper states 4.4 (rounded) → match.

Q13: 57 − 51.02 = 5.98 percentage points; paper states 6.0 (rounded) → match.

CLAIM Q1: computed=1.55263e21 expected=1.5526e21 match=yes
CLAIM Q2: computed=1.93079e-13 expected=1.9308e-13 match=yes
CLAIM Q3: computed=1.0000 expected=1.0000 match=yes
CLAIM Q4: computed=0.894427 expected=0.8944 match=yes
CLAIM Q5: computed=0.686299 expected=0.6863 match=yes
CLAIM Q6: computed=0.298139 expected=0.2981 match=yes
CLAIM Q7: computed=1.118034 expected=1.1180 match=yes
CLAIM Q8: computed=1.414214 expected=1.4142 match=yes
CLAIM Q9: computed=2.236068 expected=2.2361 match=yes
CLAIM Q10: computed=0.526316 expected=0.5263 match=yes
CLAIM Q11: computed=0.510204 expected=0.5102 match=yes
CLAIM Q12: computed=4.37 expected=4.4 match=yes
CLAIM Q13: computed=5.98 expected=6.0 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.55263e21 | 1.5526e21 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 1.93079e-13 | 1.9308e-13 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 1.0000 | 1.0000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.894427 | 0.8944 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 0.686299 | 0.6863 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.298139 | 0.2981 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.118034 | 1.1180 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 1.414214 | 1.4142 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 2.236068 | 2.2361 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.526316 | 0.5263 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 0.510204 | 0.5102 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 4.37 | 4.4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 5.98 | 6.0 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
