# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Compton frequency omega_C = 2 m_e c^2 / hbar approx 1.55e21 Hz",
    "inputs": "m_e c^2 = 8.187e-14 J; hbar = 1.0546e-34 J s",
    "formula": "omega_C = 2*8.187e-14 / 1.0546e-34"
  },
  {
    "id": "Q2",
    "statement": "Compton half-wavelength lambda_C/2 = hbar/(2 m_e c) approx 1.93e-13 m",
    "inputs": "hbar = 1.0546e-34 J s; m_e = 9.109e-31 kg; c = 2.998e8 m/s",
    "formula": "lambda_C/2 = 1.0546e-34 / (2*9.109e-31*2.998e8)"
  },
  {
    "id": "Q3",
    "statement": "Dirac-case ZBW/static ratio at p=0 equals 1.0000",
    "inputs": "|u gamma0 u|^2 = 4.0000; |u gamma0 v|^2 = 4.0000",
    "formula": "4.0000/4.0000"
  },
  {
    "id": "Q4",
    "statement": "Dirac-case ZBW/static ratio at p=0.5 equals 0.8944",
    "inputs": "|u gamma0 u|^2 = 4.4721; |u gamma0 v|^2 = 4.0000",
    "formula": "4.0000/4.4721"
  },
  {
    "id": "Q5",
    "statement": "Dirac-case ZBW/static ratio at p=1 equals 0.6863",
    "inputs": "|u gamma0 u|^2 = 5.8284; |u gamma0 v|^2 = 4.0000",
    "formula": "4.0000/5.8284"
  },
  {
    "id": "Q6",
    "statement": "Dirac-case ZBW/static ratio at p=2 equals 0.2981",
    "inputs": "|u gamma0 u|^2 = 13.4164; |u gamma0 v|^2 = 4.0000",
    "formula": "4.0000/13.4164"
  },
  {
    "id": "Q7",
    "statement": "Energy E = sqrt(1+p^2) at p=0.5 equals 1.1180 (table 1.12)",
    "inputs": "p = 0.5",
    "formula": "sqrt(1+0.5^2)"
  },
  {
    "id": "Q8",
    "statement": "Energy E = sqrt(1+p^2) at p=1 equals 1.4142 (table 1.41)",
    "inputs": "p = 1",
    "formula": "sqrt(1+1^2)"
  },
  {
    "id": "Q9",
    "statement": "Energy E = sqrt(1+p^2) at p=2 equals 2.2361 (table 2.24)",
    "inputs": "p = 2",
    "formula": "sqrt(1+2^2)"
  },
  {
    "id": "Q10",
    "statement": "Pairing-bound edge reduction R(N) = N/[2(N-1)] equals 0.5263 at N=20 (52.6%)",
    "inputs": "N = 20",
    "formula": "20/(2*(20-1))"
  },
  {
    "id": "Q11",
    "statement": "Pairing-bound edge reduction R(N) equals 0.5102 at N=50 (51.0%)",
    "inputs": "N = 50",
    "formula": "50/(2*(50-1))"
  },
  {
    "id": "Q12",
    "statement": "Pairing-bound reduction approaches 50% asymptotically",
    "inputs": "N -> infinity",
    "formula": "lim N/(2(N-1)) = 1/2"
  },
  {
    "id": "Q13",
    "statement": "Reported 57% edge reduction exceeds pairing bound by 4.4 percentage points at N=20",
    "inputs": "reported reduction = 57%; R(20) = 0.5263",
    "formula": "57 - 100*20/(2*19)"
  },
  {
    "id": "Q14",
    "statement": "Reported 57% edge reduction exceeds pairing bound by 6.0 percentage points at N=50",
    "inputs": "reported reduction = 57%; R(50) = 0.5102",
    "formula": "57 - 100*50/(2*49)"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = math.floor(log10(abs(x)))
    return round(x, n - 1 - d)

results = []

# Q1: omega_C = 2*8.187e-14 / 1.0546e-34
computed = 2 * 8.187e-14 / 1.0546e-34
expected = "1.55e21"
exp_val = 1.55e21
match = "yes" if f"{sig(computed,3):.3e}" == f"{exp_val:.3e}" else "no"
results.append(("Q1", computed, exp_val, match))

# Q2: lambda_C/2 = 1.0546e-34 / (2*9.109e-31*2.998e8)
computed = 1.0546e-34 / (2 * 9.109e-31 * 2.998e8)
expected = "1.93e-13"
exp_val = 1.93e-13
match = "yes" if f"{sig(computed,3):.3e}" == f"{exp_val:.3e}" else "no"
results.append(("Q2", computed, exp_val, match))

# Q3: 4.0000/4.0000
computed = 4.0000 / 4.0000
exp_val = 1.0000
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q3", computed, exp_val, match))

# Q4: 4.0000/4.4721
computed = 4.0000 / 4.4721
exp_val = 0.8944
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q4", computed, exp_val, match))

# Q5: 4.0000/5.8284
computed = 4.0000 / 5.8284
exp_val = 0.6863
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q5", computed, exp_val, match))

# Q6: 4.0000/13.4164
computed = 4.0000 / 13.4164
exp_val = 0.2981
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q6", computed, exp_val, match))

# Q7: sqrt(1+0.5^2)
computed = math.sqrt(1 + 0.5**2)
exp_val = 1.1180
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q7", computed, exp_val, match))

# Q8: sqrt(1+1^2)
computed = math.sqrt(1 + 1**2)
exp_val = 1.4142
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q8", computed, exp_val, match))

# Q9: sqrt(1+2^2)
computed = math.sqrt(1 + 2**2)
exp_val = 2.2361
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q9", computed, exp_val, match))

# Q10: 20/(2*(20-1))
computed = 20 / (2 * (20 - 1))
exp_val = 0.5263
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q10", computed, exp_val, match))

# Q11: 50/(2*(50-1))
computed = 50 / (2 * (50 - 1))
exp_val = 0.5102
match = "yes" if sig(computed, 4) == exp_val else "no"
results.append(("Q11", computed, exp_val, match))

# Q12: limit N/(2(N-1)) = 1/2
computed = 0.5
exp_val = 0.5
match = "yes" if computed == exp_val else "no"
results.append(("Q12", computed, exp_val, match))

# Q13: 57 - 100*20/(2*19)
computed = 57 - 100 * 20 / (2 * 19)
exp_val = 4.4
match = "yes" if sig(computed, 2) == exp_val else "no"
results.append(("Q13", computed, exp_val, match))

# Q14: 57 - 100*50/(2*49)
computed = 57 - 100 * 50 / (2 * 49)
exp_val = 6.0
match = "yes" if sig(computed, 2) == exp_val else "no"
results.append(("Q14", computed, exp_val, match))

n_match = 0
for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp} match={m}")
    if m == "yes":
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results)-n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.5526266e+21 expected=1.55e+21 match=yes
CLAIM Q2: computed=1.9308807e-13 expected=1.93e-13 match=yes
CLAIM Q3: computed=1 expected=1.0 match=yes
CLAIM Q4: computed=0.89443438 expected=0.8944 match=yes
CLAIM Q5: computed=0.68629469 expected=0.6863 match=yes
CLAIM Q6: computed=0.29814257 expected=0.2981 match=yes
CLAIM Q7: computed=1.118034 expected=1.118 match=yes
CLAIM Q8: computed=1.4142136 expected=1.4142 match=no
CLAIM Q9: computed=2.236068 expected=2.2361 match=no
CLAIM Q10: computed=0.52631579 expected=0.5263 match=yes
CLAIM Q11: computed=0.51020408 expected=0.5102 match=yes
CLAIM Q12: computed=0.5 expected=0.5 match=yes
CLAIM Q13: computed=4.3684211 expected=4.4 match=yes
CLAIM Q14: computed=5.9795918 expected=6.0 match=yes
VERIFICATION SUMMARY: 14 claims, 12 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.5526266e+21 | 1.55e+21 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 1.9308807e-13 | 1.93e-13 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 1 | 1.0 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.89443438 | 0.8944 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 0.68629469 | 0.6863 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.29814257 | 0.2981 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.118034 | 1.118 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 1.4142136 | 1.4142 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 2.236068 | 2.2361 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.52631579 | 0.5263 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 0.51020408 | 0.5102 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 4.3684211 | 4.4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 5.9795918 | 6.0 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 14.
