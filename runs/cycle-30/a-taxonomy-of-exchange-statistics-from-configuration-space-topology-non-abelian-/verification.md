# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal Hall conductance quantum pi^2 k_B^2/(3h) = 9.464311516e-13 W K^-2",
    "inputs": "k_B = 1.380649e-23 J/K, h = 6.62607015e-34 J s, pi^2 = 9.869604401",
    "formula": "pi^2 * k_B^2 / (3*h)"
  },
  {
    "id": "Q2",
    "statement": "k_B^2 = 1.906191661e-46 J^2 K^-2",
    "inputs": "k_B = 1.380649e-23 J/K",
    "formula": "k_B^2"
  },
  {
    "id": "Q3",
    "statement": "pi^2 k_B^2 = 1.881335761e-45 J^2 K^-2",
    "inputs": "pi^2 = 9.869604401, k_B^2 = 1.906191661e-46 J^2 K^-2",
    "formula": "pi^2 * k_B^2"
  },
  {
    "id": "Q4",
    "statement": "3h = 1.987821045e-33 J s",
    "inputs": "h = 6.62607015e-34 J s",
    "formula": "3 * h"
  },
  {
    "id": "Q5",
    "statement": "kappa_xy/T = 4.732155758e-13 W K^-2 for c_- = 1/2",
    "inputs": "c_- = 0.5, quantum = 9.464311516e-13 W K^-2",
    "formula": "0.5 * 9.464311516e-13"
  },
  {
    "id": "Q6",
    "statement": "kappa_xy/T = 9.464311516e-13 W K^-2 for c_- = 1",
    "inputs": "c_- = 1, quantum = 9.464311516e-13 W K^-2",
    "formula": "1 * 9.464311516e-13"
  },
  {
    "id": "Q7",
    "statement": "kappa_xy/T = 1.419646727e-12 W K^-2 for c_- = 3/2",
    "inputs": "c_- = 1.5, quantum = 9.464311516e-13 W K^-2",
    "formula": "1.5 * 9.464311516e-13"
  },
  {
    "id": "Q8",
    "statement": "kappa_xy/T = 2.366077879e-12 W K^-2 for c_- = 5/2",
    "inputs": "c_- = 2.5, quantum = 9.464311516e-13 W K^-2",
    "formula": "2.5 * 9.464311516e-13"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: thermal Hall conductance quantum
pi2 = 9.869604401
kB = 1.380649e-23
h = 6.62607015e-34
q1 = pi2 * kB**2 / (3 * h)
results.append(check("Q1", q1, 9.464311516e-13))

# Q2: k_B^2
q2 = kB**2
results.append(check("Q2", q2, 1.906191661e-46))

# Q3: pi^2 * k_B^2
q3 = pi2 * kB**2
results.append(check("Q3", q3, 1.881335761e-45))

# Q4: 3h
q4 = 3 * h
results.append(check("Q4", q4, 1.987821045e-33))

# Q5-Q8: kappa_xy/T for various c_-
quantum = pi2 * kB**2 / (3 * h)  # computed independently
for cid, c, exp in [("Q5", 0.5, 4.732155758e-13),
                    ("Q6", 1.0, 9.464311516e-13),
                    ("Q7", 1.5, 1.419646727e-12),
                    ("Q8", 2.5, 2.366077879e-12)]:
    results.append(check(cid, c * quantum, exp))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.464311516300952e-13 expected=9.464311516e-13 match=yes
CLAIM Q2: computed=1.9061916612010003e-46 expected=1.906191661e-46 match=yes
CLAIM Q3: computed=1.8813357608538894e-45 expected=1.881335761e-45 match=yes
CLAIM Q4: computed=1.987821045e-33 expected=1.987821045e-33 match=yes
CLAIM Q5: computed=4.732155758150476e-13 expected=4.732155758e-13 match=yes
CLAIM Q6: computed=9.464311516300952e-13 expected=9.464311516e-13 match=yes
CLAIM Q7: computed=1.4196467274451427e-12 expected=1.419646727e-12 match=yes
CLAIM Q8: computed=2.366077879075238e-12 expected=2.366077879e-12 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
