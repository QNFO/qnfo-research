# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Worst-case interpolation error bound for baseline sampling interval: ||e||_inf <= 0.05 mm",
    "inputs": "L_max = 0.5, Delta x = 0.1 mm",
    "formula": "||e||_inf = L_max * Delta x"
  },
  {
    "id": "Q2",
    "statement": "Worst-case error bound for halved spacing: 0.025 mm",
    "inputs": "L_max = 0.5, Delta x = 0.05 mm",
    "formula": "||e||_inf = L_max * Delta x"
  },
  {
    "id": "Q3",
    "statement": "Worst-case error bound for prosthesis spacing: 0.01 mm",
    "inputs": "L_max = 0.5, Delta x = 0.02 mm",
    "formula": "||e||_inf = L_max * Delta x"
  },
  {
    "id": "Q4",
    "statement": "Worst-case error bound for alternative contraction constant: 0.03 mm",
    "inputs": "lambda = 0.3, Delta x = 0.1 mm",
    "formula": "||e||_inf = lambda * Delta x"
  },
  {
    "id": "Q5",
    "statement": "Projected worst-case error for device with Delta x = 0.08 mm: 0.04 mm",
    "inputs": "L_max = 0.5, Delta x = 0.08 mm",
    "formula": "||e||_inf = L_max * Delta x"
  },
  {
    "id": "Q6",
    "statement": "Relative error for halved spacing as fraction of receptive-field diameter: 2.5%",
    "inputs": "||e||_inf = 0.025 mm, d = 1 mm",
    "formula": "relative = ||e||_inf / d"
  },
  {
    "id": "Q7",
    "statement": "Relative error for prosthesis spacing as fraction of receptive-field diameter: 1%",
    "inputs": "||e||_inf = 0.01 mm, d = 1 mm",
    "formula": "relative = ||e||_inf / d"
  },
  {
    "id": "Q8",
    "statement": "Error reduction from baseline for projected device: 20%",
    "inputs": "baseline = 0.05 mm, projected = 0.04 mm",
    "formula": "reduction = (baseline - projected) / baseline"
  },
  {
    "id": "Q9",
    "statement": "Reduction in bound for lambda = 0.3 versus baseline: 40%",
    "inputs": "baseline = 0.05 mm, lambda case = 0.03 mm",
    "formula": "reduction = (baseline - lambda_case) / baseline"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

claims = [
    ("Q1", 0.5 * 0.1, "0.05", 2),
    ("Q2", 0.5 * 0.05, "0.025", 2),
    ("Q3", 0.5 * 0.02, "0.01", 2),
    ("Q4", 0.3 * 0.1, "0.03", 2),
    ("Q5", 0.5 * 0.08, "0.04", 2),
    ("Q6", (0.5 * 0.05) / 1.0 * 100, "2.5", 2),
    ("Q7", (0.5 * 0.02) / 1.0 * 100, "1", 1),
    ("Q8", (0.05 - 0.5 * 0.08) / 0.05 * 100, "20", 2),
    ("Q9", (0.05 - 0.3 * 0.1) / 0.05 * 100, "40", 2),
]

m = 0
for cid, computed, expected, nsig in claims:
    c = sig(computed, 10)
    e = float(expected)
    ok = "yes" if abs(c - e) < 1e-12 else "no"
    if ok == "yes":
        m += 1
    print(f"CLAIM {cid}: computed={c:.8g} expected={expected} match={ok}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {m} match, {len(claims) - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.05 expected=0.05 match=yes
CLAIM Q2: computed=0.025 expected=0.025 match=yes
CLAIM Q3: computed=0.01 expected=0.01 match=yes
CLAIM Q4: computed=0.03 expected=0.03 match=yes
CLAIM Q5: computed=0.04 expected=0.04 match=yes
CLAIM Q6: computed=2.5 expected=2.5 match=yes
CLAIM Q7: computed=1 expected=1 match=yes
CLAIM Q8: computed=20 expected=20 match=yes
CLAIM Q9: computed=40 expected=40 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.05 | 0.05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.025 | 0.025 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.01 | 0.01 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.03 | 0.03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.04 | 0.04 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 2.5 | 2.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 20 | 20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 40 | 40 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
