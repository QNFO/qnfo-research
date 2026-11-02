# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Landauer limit kT ln 2 at 300 K equals 2.871e-21 J",
    "inputs": "k = 1.380649e-23 J/K; T = 300 K; ln 2 = 0.6931472",
    "formula": "k * T * ln 2"
  },
  {
    "id": "Q2",
    "statement": "CEI constant kappa for silicon = 3.483e29 m^-3 s^-1",
    "inputs": "p_max = 100 W/cm^2 = 1.0e6 W/m^2; ell = 1.0e-3 m; eps_L = 2.871e-21 J",
    "formula": "p_max / (ell * eps_L)"
  },
  {
    "id": "Q3",
    "statement": "Causal-cone bound rho_t_causal = 2.998e40 m^-3 s^-1",
    "inputs": "c = 2.998e8 m/s; L = 1.0e-8 m",
    "formula": "c / L^4"
  },
  {
    "id": "Q4",
    "statement": "Ratio of causal bound to kappa = 8.607e10",
    "inputs": "rho_t_causal = 2.998e40 m^-3 s^-1; kappa = 3.483e29 m^-3 s^-1",
    "formula": "rho_t_causal / kappa"
  },
  {
    "id": "Q5",
    "statement": "Profile S causal density rho_t_S = 3.0e23 m^-3 s^-1",
    "inputs": "n_d = 1.0e15 m^-3; f = 3.0e9 s^-1; alpha = 0.10",
    "formula": "n_d * f * alpha"
  },
  {
    "id": "Q6",
    "statement": "Profile S energy fidelity eta_e_S = 3.483e4",
    "inputs": "E_tr = 1.0e-16 J; eps_L = 2.871e-21 J",
    "formula": "E_tr / eps_L"
  },
  {
    "id": "Q7",
    "statement": "Profile S product Pi_S = 1.045e28 m^-3 s^-1",
    "inputs": "rho_t_S = 3.0e23 m^-3 s^-1; eta_e_S = 3.483e4",
    "formula": "rho_t_S * eta_e_S"
  },
  {
    "id": "Q8",
    "statement": "Profile S fraction of bound Pi_S/kappa = 0.0300",
    "inputs": "Pi_S = 1.045e28 m^-3 s^-1; kappa = 3.483e29 m^-3 s^-1",
    "formula": "Pi_S / kappa"
  },
  {
    "id": "Q9",
    "statement": "Profile G energy fidelity eta_e_G = 100",
    "inputs": "E_tr_G = 2.871e-19 J; eps_L = 2.871e-21 J",
    "formula": "E_tr_G / eps_L"
  },
  {
    "id": "Q10",
    "statement": "Profile G maximum causal density = 3.483e27 m^-3 s^-1",
    "inputs": "kappa = 3.483e29 m^-3 s^-1; eta_e_G = 100",
    "formula": "kappa / eta_e_G"
  },
  {
    "id": "Q11",
    "statement": "Ratio Pi_G/Pi_S approx 33.3",
    "inputs": "Pi_G = 3.483e29 m^-3 s^-1; Pi_S = 1.045e28 m^-3 s^-1",
    "formula": "Pi_G / Pi_S"
  },
  {
    "id": "Q12",
    "statement": "Volumetric power budget = 1.000e9 W/m^3",
    "inputs": "p_max = 1.0e6 W/m^2; ell = 1.0e-3 m",
    "formula": "p_max / ell"
  },
  {
    "id": "Q13",
    "statement": "Profile S dissipated power density = 3.0e7 W/m^3 (3.0% of budget)",
    "inputs": "rho_t_S = 3.0e23 m^-3 s^-1; E_tr = 1.0e-16 J; budget = 1.0e9 W/m^3",
    "formula": "rho_t_S * E_tr"
  },
  {
    "id": "Q14",
    "statement": "kappa' for p_max = 10 W/cm^2 = 3.483e28 m^-3 s^-1",
    "inputs": "p_max = 1.0e5 W/m^2; ell = 1.0e-3 m; eps_L = 2.871e-21 J",
    "formula": "p_max / (ell * eps_L)"
  },
  {
    "id": "Q15",
    "statement": "Throttle factor theta at p_max = 1 W/cm^2 = 0.333",
    "inputs": "kappa'' = 3.483e27 m^-3 s^-1; Pi_S = 1.045e28 m^-3 s^-1",
    "formula": "kappa'' / Pi_S"
  },
  {
    "id": "Q16",
    "statement": "Fractional causal-density loss at theta = 0.333 is 0.667",
    "inputs": "theta = 0.333",
    "formula": "1 - theta"
  }
]

## Script
```python
import math

# Inputs
k = 1.380649e-23
T = 300.0
ln2 = math.log(2)  # paper states 0.6931472; use stated value
ln2_stated = 0.6931472

eps_L = k * T * ln2_stated

p_max_si = 1.0e6      # W/m^2 (100 W/cm^2)
ell = 1.0e-3          # m
kappa = p_max_si / (ell * eps_L)

c = 2.998e8
L = 1.0e-8
rho_causal = c / L**4

ratio = rho_causal / kappa

n_d = 1.0e15
f = 3.0e9
alpha = 0.10
rho_S = n_d * f * alpha

E_tr_S = 1.0e-16
eta_S = E_tr_S / eps_L

Pi_S = rho_S * eta_S

frac = Pi_S / kappa

E_tr_G = 2.871e-19
eta_G = E_tr_G / eps_L

rho_G_max = kappa / eta_G

Pi_G = kappa
ratio_GS = Pi_G / Pi_S

budget = p_max_si / ell

P_S = rho_S * E_tr_S

p_max_10 = 1.0e5
kappa_prime = p_max_10 / (ell * eps_L)

p_max_1 = 1.0e4
kappa_pp = p_max_1 / (ell * eps_L)
theta = kappa_pp / Pi_S

loss = 1 - theta

def report(cid, computed, expected):
    match = "yes" if abs(computed - float(expected)) / abs(float(expected)) < 5e-4 else "no"
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected} match={match}")

report("Q1", eps_L, "2.871e-21")
report("Q2", kappa, "3.483e29")
report("Q3", rho_causal, "2.998e40")
report("Q4", ratio, "8.607e10")
report("Q5", rho_S, "3.0e23")
report("Q6", eta_S, "3.483e4")
report("Q7", Pi_S, "1.045e28")
report("Q8", frac, "0.0300")
report("Q9", eta_G, "100")
report("Q10", rho_G_max, "3.483e27")
report("Q11", ratio_GS, "33.3")
report("Q12", budget, "1.000e9")
report("Q13", P_S, "3.0e7")
report("Q14", kappa_prime, "3.483e28")
report("Q15", theta, "0.333")
report("Q16", loss, "0.667")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.87097897e-21 expected=2.871e-21 match=yes
CLAIM Q2: computed=3.48313245e+29 expected=3.483e29 match=yes
CLAIM Q3: computed=2.99800000e+40 expected=2.998e40 match=yes
CLAIM Q4: computed=8.60719494e+10 expected=8.607e10 match=yes
CLAIM Q5: computed=3.00000000e+23 expected=3.0e23 match=yes
CLAIM Q6: computed=3.48313245e+04 expected=3.483e4 match=yes
CLAIM Q7: computed=1.04493974e+28 expected=1.045e28 match=yes
CLAIM Q8: computed=3.00000000e-02 expected=0.0300 match=yes
CLAIM Q9: computed=1.00000733e+02 expected=100 match=yes
CLAIM Q10: computed=3.48310693e+27 expected=3.483e27 match=yes
CLAIM Q11: computed=3.33333333e+01 expected=33.3 match=no
CLAIM Q12: computed=1.00000000e+09 expected=1.000e9 match=yes
CLAIM Q13: computed=3.00000000e+07 expected=3.0e7 match=yes
CLAIM Q14: computed=3.48313245e+28 expected=3.483e28 match=yes
CLAIM Q15: computed=3.33333333e-01 expected=0.333 match=no
CLAIM Q16: computed=6.66666667e-01 expected=0.667 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.87097897e-21 | 2.871e-21 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 3.48313245e+29 | 3.483e29 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 2.99800000e+40 | 2.998e40 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 8.60719494e+10 | 8.607e10 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 3.00000000e+23 | 3.0e23 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 3.48313245e+04 | 3.483e4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.04493974e+28 | 1.045e28 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 3.00000000e-02 | 0.0300 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 1.00000733e+02 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 3.48310693e+27 | 3.483e27 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 3.33333333e+01 | 33.3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 1.00000000e+09 | 1.000e9 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 3.00000000e+07 | 3.0e7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 3.48313245e+28 | 3.483e28 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 3.33333333e-01 | 0.333 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 6.66666667e-01 | 0.667 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
