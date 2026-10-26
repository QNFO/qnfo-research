# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The energy density required for an order‑unity index gradient over a length L is u = c^{4}/(8\\pi G L^{2}).",
    "inputs": "c = 2.998×10^{8} m s^{-1}, G = 6.674×10^{-11} m^{3} kg^{-1} s^{-2}, L = 1 m",
    "formula": "u = c^4 / (8 * pi * G * L^2)"
  },
  {
    "id": "Q2",
    "statement": "c^{4} = (2.998×10^{8})^{4} = 8.078×10^{33}.",
    "inputs": "c = 2.998×10^{8} m s^{-1}",
    "formula": "c^4"
  },
  {
    "id": "Q3",
    "statement": "8\\pi G = 8 × 3.1416 × 6.674×10^{-11} = 1.677×10^{-9}.",
    "inputs": "G = 6.674×10^{-11} m^{3} kg^{-1} s^{-2}",
    "formula": "8 * pi * G"
  },
  {
    "id": "Q4",
    "statement": "The required energy density is u = 4.82×10^{42} J m^{-3}.",
    "inputs": "c = 2.998×10^{8} m s^{-1}, G = 6.674×10^{-11} m^{3} kg^{-1} s^{-2}, L = 1 m",
    "formula": "u = c^4 / (8 * pi * G * L^2)"
  },
  {
    "id": "Q5",
    "statement": "The required density exceeds the observed dark‑energy density (10^{-9} J m^{-3}) by 51.7 orders of magnitude.",
    "inputs": "u = 4.82×10^{42} J m^{-3}, dark‑energy density = 1×10^{-9} J m^{-3}",
    "formula": "log10(u / 1e-9)"
  },
  {
    "id": "Q6",
    "statement": "The thrust ceiling for a dielectric‑analogy region is F_{max} = (P/c)(n-1).",
    "inputs": "P = 1.000×10^{3} W, c = 2.998×10^{8} m s^{-1}, n = 3",
    "formula": "F_max = (P / c) * (n - 1)"
  },
  {
    "id": "Q7",
    "statement": "Numerical thrust ceiling: F_{max} = 6.67×10^{-6} N.",
    "inputs": "P = 1.000×10^{3} W, c = 2.998×10^{8} m s^{-1}, n = 3",
    "formula": "F_max = (P / c) * (n - 1)"
  },
  {
    "id": "Q8",
    "statement": "Photon‑rocket thrust limit: F_{γ} = P/c = 3.34×10^{-6} N.",
    "inputs": "P = 1.000×10^{3} W, c = 2.998×10^{8} m s^{-1}",
    "formula": "F_gamma = P / c"
  },
  {
    "id": "Q9",
    "statement": "Energy cost per unit impulse is E/I = c = 2.998×10^{8} J N^{-1} s^{-1}.",
    "inputs": "c = 2.998×10^{8} m s^{-1}",
    "formula": "E / I = c"
  },
  {
    "id": "Q10",
    "statement": "A 100 kg spacecraft requiring Δv = 1 m s^{-1} needs impulse I = 100 N·s and energy E = 3.00×10^{10} J.",
    "inputs": "mass = 100 kg, Δv = 1 m s^{-1}, c = 2.998×10^{8} m s^{-1}",
    "formula": "I = m * Δv; E = I * c"
  },
  {
    "id": "Q11",
    "statement": "With a storage specific energy of 100 Wh kg^{-1} (3.6×10^{5} J kg^{-1}), the required storage mass is M_E = 8.33×10^{4} kg.",
    "inputs": "E = 3.00×10^{10} J, specific energy = 3.6×10^{5} J kg^{-1}",
    "formula": "M_E = E / (specific energy)"
  },
  {
    "id": "Q12",
    "statement": "If the n=3 ceiling halves the required power, the storage mass reduces to 4.17×10^{4} kg.",
    "inputs": "M_E = 8.33×10^{4} kg",
    "formula": "M_E / 2"
  },
  {
    "id": "Q13",
    "statement": "Maintaining 5 kV across a 20 µm gap requires an electric field of 2.5×10^{8} V m^{-1} (250 MV m^{-1}).",
    "inputs": "V = 5×10^{3} V, d = 20×10^{-6} m",
    "formula": "E_field = V / d"
  },
  {
    "id": "Q14",
    "statement": "A torsion‑balance capable of detecting forces down to 1×10^{-8} N would be sufficient for the proposed test.",
    "inputs": "Detection limit = 1×10^{-8} N",
    "formula": "N/A (specification)"
  },
  {
    "id": "Q15",
    "statement": "The falsification threshold is a measured thrust ≥ 3.3×10^{-7} N; values below this support the momentum‑conservation model.",
    "inputs": "Photon‑rocket thrust = 3.34×10^{-6} N",
    "formula": "threshold = (1/10) * photon‑rocket thrust"
  },
  {
    "id": "Q16",
    "statement": "The ratio of required energy density to dark‑energy density is 10^{51.7}, i.e., 51.7 orders of magnitude.",
    "inputs": "u = 4.82×10^{42} J m^{-3}, dark‑energy density = 1×10^{-9} J m^{-3}",
    "formula": "log10(u / 1e-9) = 51.7"
  }
]

## Script
```python
import math

# Constants
c = 2.998e8          # m s^-1
G = 6.674e-11        # m^3 kg^-1 s^-2
pi_approx = 3.1416
L = 1.0              # m
P = 1.000e3          # W
n = 3.0
V = 5.0e3            # V
d = 20.0e-6          # m
mass = 100.0         # kg
dv = 1.0             # m s^-1
specific_energy = 3.6e5   # J kg^-1

# Expected values from the paper (as strings)
expected = {
    "Q1": "4.82e42",
    "Q2": "8.078e33",
    "Q3": "1.677e-9",
    "Q4": "4.82e42",
    "Q5": "51.7",
    "Q6": "6.67e-6",
    "Q7": "6.67e-6",
    "Q8": "3.34e-6",
    "Q9": "2.998e8",
    "Q10": "3.00e10",
    "Q11": "8.33e4",
    "Q12": "4.17e4",
    "Q13": "2.5e8",
    "Q14": "1e-8",
    "Q15": "3.3e-7",
    "Q16": "51.7"
}

def fmt(x):
    """Format a number with at least 8 significant digits, using scientific notation."""
    return f"{x:.8g}"

# Computations
u = c**4 / (8 * pi_approx * G * L**2)                     # Q1, Q4
c4 = c**4                                                  # Q2
eight_pi_G = 8 * pi_approx * G                             # Q3
log_ratio = math.log10(u / 1e-9)                           # Q5, Q16
F_max = (P / c) * (n - 1)                                 # Q6, Q7
F_gamma = P / c                                            # Q8
E_per_I = c                                                # Q9
I = mass * dv                                              # Q10 intermediate
E = I * c                                                  # Q10
M_E = E / specific_energy                                   # Q11
M_E_half = M_E / 2                                          # Q12
E_field = V / d                                            # Q13
detect_limit = 1e-8                                         # Q14 (given)
threshold = F_gamma / 10                                   # Q15

# Prepare results
results = {
    "Q1": fmt(u),
    "Q2": fmt(c4),
    "Q3": fmt(eight_pi_G),
    "Q4": fmt(u),
    "Q5": fmt(log_ratio),
    "Q6": fmt(F_max),
    "Q7": fmt(F_max),
    "Q8": fmt(F_gamma),
    "Q9": fmt(E_per_I),
    "Q10": fmt(E),
    "Q11": fmt(M_E),
    "Q12": fmt(M_E_half),
    "Q13": fmt(E_field),
    "Q14": fmt(detect_limit),
    "Q15": fmt(threshold),
    "Q16": fmt(log_ratio)
}

# Verification output
match_count = 0
total = len(expected)

for qid in sorted(expected.keys()):
    comp = results[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.8161437e+42 expected=4.82e42 match=no
CLAIM Q10: computed=2.998e+10 expected=3.00e10 match=no
CLAIM Q11: computed=83277.778 expected=8.33e4 match=no
CLAIM Q12: computed=41638.889 expected=4.17e4 match=no
CLAIM Q13: computed=2.5e+08 expected=2.5e8 match=no
CLAIM Q14: computed=1e-08 expected=1e-8 match=no
CLAIM Q15: computed=3.335557e-07 expected=3.3e-7 match=no
CLAIM Q16: computed=51.682699 expected=51.7 match=no
CLAIM Q2: computed=8.0784216e+33 expected=8.078e33 match=no
CLAIM Q3: computed=1.6773631e-09 expected=1.677e-9 match=no
CLAIM Q4: computed=4.8161437e+42 expected=4.82e42 match=no
CLAIM Q5: computed=51.682699 expected=51.7 match=no
CLAIM Q6: computed=6.6711141e-06 expected=6.67e-6 match=no
CLAIM Q7: computed=6.6711141e-06 expected=6.67e-6 match=no
CLAIM Q8: computed=3.335557e-06 expected=3.34e-6 match=no
CLAIM Q9: computed=2.998e+08 expected=2.998e8 match=no
VERIFICATION SUMMARY: 16 claims, 0 match, 16 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4.8161437e+42 | 4.82e42 | no | match | 3 significant digits (as printed, at least 3) |
| Q10 | 2.998e+10 | 3.00e10 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 83277.778 | 8.33e4 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 41638.889 | 4.17e4 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 2.5e+08 | 2.5e8 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 1e-08 | 1e-8 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 3.335557e-07 | 3.3e-7 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 51.682699 | 51.7 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 8.0784216e+33 | 8.078e33 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.6773631e-09 | 1.677e-9 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 4.8161437e+42 | 4.82e42 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 51.682699 | 51.7 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 6.6711141e-06 | 6.67e-6 | no | match | 3 significant digits (as printed, at least 3) |
| Q7 | 6.6711141e-06 | 6.67e-6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 3.335557e-06 | 3.34e-6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 2.998e+08 | 2.998e8 | no | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
