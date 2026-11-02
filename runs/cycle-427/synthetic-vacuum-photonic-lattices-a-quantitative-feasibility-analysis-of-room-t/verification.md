# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal energy at 300 K: k_B T = 25.85 meV",
    "inputs": "k_B = 8.617333e-5 eV/K; T = 300 K",
    "formula": "k_B * T"
  },
  {
    "id": "Q2",
    "statement": "Required gap Delta = 15 k_B T = 0.388 eV",
    "inputs": "k_B = 8.617333e-5 eV/K; T = 300 K; factor 15",
    "formula": "15 * k_B * T"
  },
  {
    "id": "Q3",
    "statement": "Operating frequency nu = 93.76 THz",
    "inputs": "Delta = 0.38778 eV; h = 4.135668e-15 eV*s",
    "formula": "Delta / h"
  },
  {
    "id": "Q4",
    "statement": "Operating wavelength lambda = 3.20 um",
    "inputs": "c = 2.99792458e8 m/s; nu = 9.376e13 Hz",
    "formula": "c / nu"
  },
  {
    "id": "Q5",
    "statement": "Stray-anyon probability at 10 k_B T gap: 9.08e-2 per 10^3-mode device",
    "inputs": "N_mode*g = 2000; Delta = 10 k_B T",
    "formula": "2000 / (exp(10) - 1)"
  },
  {
    "id": "Q6",
    "statement": "Stray-anyon probability at 15 k_B T gap: 6.12e-4 per 10^3-mode device",
    "inputs": "N_mode*g = 2000; Delta = 15 k_B T",
    "formula": "2000 / (exp(15) - 1)"
  },
  {
    "id": "Q7",
    "statement": "Fusion-space dimension for n = 100 anyons: phi^100 = 7.93e20",
    "inputs": "phi = (1+sqrt(5))/2; n = 100",
    "formula": "((1 + sqrt(5)) / 2) ** 100"
  },
  {
    "id": "Q8",
    "statement": "Required raw photonic error rate p <= 1.5e-4 for logical error 1e-4 with f_gp = 2/3",
    "inputs": "f_gp = 2/3; target logical error = 1e-4",
    "formula": "1e-4 / (2/3)"
  },
  {
    "id": "Q9",
    "statement": "Per-hop loss budget p_loss <= 3e-7 for 1e-6 logical error over 100 hops",
    "inputs": "L = 100; r = 1/30; P_logic = 1e-6",
    "formula": "1e-6 / (100 / 30)"
  },
  {
    "id": "Q10",
    "statement": "Physical-to-logical reduction ratio r = 1/30",
    "inputs": "logical error 1e-4; physical error 3e-3",
    "formula": "1e-4 / 3e-3"
  },
  {
    "id": "Q11",
    "statement": "Loss coefficient alpha = 3e-2 m^-1 for hop length 10 um",
    "inputs": "p_loss = 3e-7; ell = 1e-5 m",
    "formula": "3e-7 / 1e-5"
  },
  {
    "id": "Q12",
    "statement": "Gap at 77 K: 9.95e-2 eV",
    "inputs": "k_B = 8.617333e-5 eV/K; T = 77 K; factor 15",
    "formula": "15 * k_B * 77"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

kB = 8.617333e-5
T = 300.0
h = 4.135668e-15
c = 2.99792458e8

# Q1
q1 = kB * T
print(f"CLAIM Q1: computed={q1:.8g} expected=0.02585 match={'yes' if sig(q1,4)==0.02585 else 'no'}")

# Q2
q2 = 15 * kB * T
print(f"CLAIM Q2: computed={q2:.8g} expected=0.388 match={'yes' if sig(q2,3)==0.388 else 'no'}")

# Q3
Delta = 15 * kB * T  # 0.38778 eV
q3 = Delta / h
q3_THz = q3 / 1e12
print(f"CLAIM Q3: computed={q3_THz:.8g} expected=93.76 match={'yes' if sig(q3_THz,4)==93.76 else 'no'}")

# Q4
nu = Delta / h
q4 = c / nu
q4_um = q4 * 1e6
print(f"CLAIM Q4: computed={q4_um:.8g} expected=3.20 match={'yes' if sig(q4_um,3)==3.20 else 'no'}")

# Q5
q5 = 2000 / (math.exp(10) - 1)
print(f"CLAIM Q5: computed={q5:.8g} expected=9.08e-2 match={'yes' if sig(q5,3)==9.08e-2 else 'no'}")

# Q6
q6 = 2000 / (math.exp(15) - 1)
print(f"CLAIM Q6: computed={q6:.8g} expected=6.12e-4 match={'yes' if sig(q6,3)==6.12e-4 else 'no'}")

# Q7
phi = (1 + math.sqrt(5)) / 2
q7 = phi ** 100
print(f"CLAIM Q7: computed={q7:.8g} expected=7.93e20 match={'yes' if sig(q7,3)==7.93e20 else 'no'}")

# Q8
q8 = 1e-4 / (2/3)
print(f"CLAIM Q8: computed={q8:.8g} expected=1.5e-4 match={'yes' if sig(q8,2)==1.5e-4 else 'no'}")

# Q9
q9 = 1e-6 / (100 / 30)
print(f"CLAIM Q9: computed={q9:.8g} expected=3e-7 match={'yes' if sig(q9,1)==3e-7 else 'no'}")

# Q10
q10 = 1e-4 / 3e-3
print(f"CLAIM Q10: computed={q10:.8g} expected=0.033333333 match={'yes' if abs(q10 - 1/30) < 1e-12 else 'no'}")

# Q11
q11 = 3e-7 / 1e-5
print(f"CLAIM Q11: computed={q11:.8g} expected=3e-2 match={'yes' if sig(q11,1)==3e-2 else 'no'}")

# Q12
q12 = 15 * kB * 77
print(f"CLAIM Q12: computed={q12:.8g} expected=9.95e-2 match={'yes' if sig(q12,3)==9.95e-2 else 'no'}")

claims = [q1==q1, True]*0  # placeholder no-op
results = []
# summary
matches = 0
total = 12
# recompute match flags
m = []
m.append(sig(q1,4)==0.02585)
m.append(sig(q2,3)==0.388)
m.append(sig(q3_THz,4)==93.76)
m.append(sig(q4_um,3)==3.20)
m.append(sig(q5,3)==9.08e-2)
m.append(sig(q6,3)==6.12e-4)
m.append(sig(q7,3)==7.93e20)
m.append(sig(q8,2)==1.5e-4)
m.append(sig(q9,1)==3e-7)
m.append(abs(q10-1/30)<1e-12)
m.append(sig(q11,1)==3e-2)
m.append(sig(q12,3)==9.95e-2)
print(f"VERIFICATION SUMMARY: {total} claims, {sum(m)} match, {total - sum(m)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.025851999 expected=0.02585 match=yes
CLAIM Q2: computed=0.38777998 expected=0.388 match=yes
CLAIM Q3: computed=93.764776 expected=93.76 match=yes
CLAIM Q4: computed=3.1972823 expected=3.20 match=yes
CLAIM Q5: computed=0.090803982 expected=9.08e-2 match=yes
CLAIM Q6: computed=0.00061180483 expected=6.12e-4 match=yes
CLAIM Q7: computed=7.9207084e+20 expected=7.93e20 match=no
CLAIM Q8: computed=0.00015 expected=1.5e-4 match=yes
CLAIM Q9: computed=3e-07 expected=3e-7 match=yes
CLAIM Q10: computed=0.033333333 expected=0.033333333 match=yes
CLAIM Q11: computed=0.03 expected=3e-2 match=yes
CLAIM Q12: computed=0.099530196 expected=9.95e-2 match=yes
VERIFICATION SUMMARY: 12 claims, 11 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.025851999 | 0.02585 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.38777998 | 0.388 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 93.764776 | 93.76 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 3.1972823 | 3.20 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.090803982 | 9.08e-2 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 0.00061180483 | 6.12e-4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 7.9207084e+20 | 7.93e20 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 0.00015 | 1.5e-4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 3e-07 | 3e-7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.033333333 | 0.033333333 | yes | match | 8 significant digits (as printed, at least 3) |
| Q11 | 0.03 | 3e-2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.099530196 | 9.95e-2 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12.
