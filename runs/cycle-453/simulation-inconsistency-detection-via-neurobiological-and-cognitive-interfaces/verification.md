# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "A 60 Hz render clock contributes sigma_q = 4.811 ms of cross-modal timing noise",
    "inputs": "f = 60 Hz",
    "formula": "sigma_q = 1/(f*sqrt(12))"
  },
  {
    "id": "Q2",
    "statement": "A 120 Hz render clock contributes sigma_q = 2.406 ms of cross-modal timing noise",
    "inputs": "f = 120 Hz",
    "formula": "sigma_q = 1/(f*sqrt(12))"
  },
  {
    "id": "Q3",
    "statement": "Predicted ERP latency standard deviation is 5.67 ms at 60 Hz",
    "inputs": "sigma_bio = 3 ms, sigma_q(60) = 4.811 ms",
    "formula": "sigma_ERP = sqrt(sigma_bio^2 + sigma_q^2)"
  },
  {
    "id": "Q4",
    "statement": "Predicted ERP latency standard deviation is 3.85 ms at 120 Hz",
    "inputs": "sigma_bio = 3 ms, sigma_q(120) = 2.406 ms",
    "formula": "sigma_ERP = sqrt(sigma_bio^2 + sigma_q^2)"
  },
  {
    "id": "Q5",
    "statement": "Difference in ERP latency standard deviation between 60 Hz and 120 Hz is 1.82 ms",
    "inputs": "sigma_ERP(60) = 5.670 ms, sigma_ERP(120) = 3.846 ms",
    "formula": "delta = sigma_ERP(60) - sigma_ERP(120)"
  },
  {
    "id": "Q6",
    "statement": "Detecting a 5% accuracy deviation from baseline p0 = 0.5077 requires 1292 trials per condition",
    "inputs": "p0 = 0.5077, p1 = 0.5577, z_alpha/2 = 1.96, z_beta = 1.6449, delta_p = 0.05",
    "formula": "n = (z_alpha/2*sqrt(p0*(1-p0)) + z_beta*sqrt(p1*(1-p1)))^2 / (p1 - p0)^2"
  },
  {
    "id": "Q7",
    "statement": "Detecting the variance inflation a 60 Hz clock imposes on a 20 ms biological timing estimate requires approximately 8.2e3 trials",
    "inputs": "sigma_0 = 20 ms, sigma_q(60)^2 = 23.146 ms^2, z_alpha/2 = 1.96, z_beta = 1.6449",
    "formula": "n = 2*(z_alpha/2 + z_beta)^2 * sigma_bar^4 / (sigma_1^2 - sigma_0^2)^2, with sigma_1^2 = sigma_0^2 + sigma_q^2 and sigma_bar^2 = (sigma_0^2 + sigma_1^2)/2"
  },
  {
    "id": "Q8",
    "statement": "At 120 Hz the variance-inflation requirement rises to approximately 1.26e5 trials",
    "inputs": "sigma_0 = 20 ms, sigma_q(120)^2 = 5.789 ms^2, z_alpha/2 = 1.96, z_beta = 1.6449",
    "formula": "n = 2*(z_alpha/2 + z_beta)^2 * sigma_bar^4 / (sigma_1^2 - sigma_0^2)^2"
  },
  {
    "id": "Q9",
    "statement": "Detecting a cross-participant latency correlation of r = 0.05 requires approximately 5193 participants",
    "inputs": "r = 0.05, z_alpha/2 = 1.96, z_beta = 1.6449",
    "formula": "n = ((z_alpha/2 + z_beta)/atanh(r))^2 + 3"
  },
  {
    "id": "Q10",
    "statement": "At 240 Hz the substrate contribution is 1.203 ms and sigma_ERP = 3.232 ms",
    "inputs": "f = 240 Hz, sigma_bio = 3 ms",
    "formula": "sigma_q = 1/(f*sqrt(12)); sigma_ERP = sqrt(sigma_bio^2 + sigma_q^2)"
  },
  {
    "id": "Q11",
    "statement": "If biological jitter were 6 ms, the predicted 60-120 Hz difference would fall to 1.23 ms",
    "inputs": "sigma_bio = 6 ms, sigma_q(60) = 4.811 ms, sigma_q(120) = 2.406 ms",
    "formula": "delta = sqrt(6^2 + 4.811^2) - sqrt(6^2 + 2.406^2)"
  }
]

## Script
```python
import math

def sig(x, d):
    # round to d significant digits
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (d - 1))

results = []

# Q1: sigma_q(60) = 1/(60*sqrt(12)) ms
q1 = 1000.0 / (60.0 * math.sqrt(12.0))
results.append(("Q1", q1, "4.811", 4))

# Q2: sigma_q(120) = 1/(120*sqrt(12)) ms
q2 = 1000.0 / (120.0 * math.sqrt(12.0))
results.append(("Q2", q2, "2.406", 4))

# Q3: sigma_ERP(60) = sqrt(3^2 + 4.811^2)
q3 = math.sqrt(3.0**2 + 4.811**2)
results.append(("Q3", q3, "5.67", 3))

# Q4: sigma_ERP(120) = sqrt(3^2 + 2.406^2)
q4 = math.sqrt(3.0**2 + 2.406**2)
results.append(("Q4", q4, "3.85", 3))

# Q5: delta = 5.670 - 3.846
q5 = 5.670 - 3.846
results.append(("Q5", q5, "1.82", 3))

# Q6: n = (1.96*sqrt(p0(1-p0)) + 1.6449*sqrt(p1(1-p1)))^2 / 0.05^2
p0, p1 = 0.5077, 0.5577
za, zb = 1.96, 1.6449
q6 = (za * math.sqrt(p0 * (1 - p0)) + zb * math.sqrt(p1 * (1 - p1)))**2 / (p1 - p0)**2
results.append(("Q6", q6, "1292", 4))

# Q7: variance inflation at 60 Hz
s0 = 20.0
dq60 = 4.811**2
s1sq = s0**2 + dq60
barsq = (s0**2 + s1sq) / 2.0
q7 = 2.0 * (za + zb)**2 * barsq**2 / (s1sq - s0**2)**2
results.append(("Q7", q7, "8200", 2))

# Q8: variance inflation at 120 Hz
dq120 = 2.406**2
s1sq8 = s0**2 + dq120
barsq8 = (s0**2 + s1sq8) / 2.0
q8 = 2.0 * (za + zb)**2 * barsq8**2 / (s1sq8 - s0**2)**2
results.append(("Q8", q8, "126000", 3))

# Q9: n = ((za+zb)/atanh(0.05))^2 + 3
q9 = ((za + zb) / math.atanh(0.05))**2 + 3
results.append(("Q9", q9, "5193", 4))

# Q10: sigma_q(240) and sigma_ERP(240)
q10a = 1000.0 / (240.0 * math.sqrt(12.0))
q10b = math.sqrt(3.0**2 + q10a**2)
results.append(("Q10", q10b, "3.232", 4))

# Q11: delta with sigma_bio = 6
q11 = math.sqrt(6.0**2 + 4.811**2) - math.sqrt(6.0**2 + 2.406**2)
results.append(("Q11", q11, "1.23", 3))

match_count = 0
for cid, comp, exp_str, d in results:
    rounded = sig(comp, d)
    match = "yes" if abs(rounded - float(exp_str)) < 10**(-(d)) * max(1, abs(float(exp_str))) or f"{rounded:.{d}g}" == exp_str else "no"
    # robust match: compare formatted strings
    match = "yes" if f"{rounded:.{d}g}" == exp_str else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={comp:.8f} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.81125224 expected=4.811 match=yes
CLAIM Q2: computed=2.40562612 expected=2.406 match=yes
CLAIM Q3: computed=5.66971966 expected=5.67 match=yes
CLAIM Q4: computed=3.84562557 expected=3.85 match=yes
CLAIM Q5: computed=1.82400000 expected=1.82 match=yes
CLAIM Q6: computed=1291.45227293 expected=1292 match=no
CLAIM Q7: computed=8218.04415415 expected=8200 match=no
CLAIM Q8: computed=125897.30924530 expected=126000 match=no
CLAIM Q9: computed=5192.45589935 expected=5193 match=no
CLAIM Q10: computed=3.23214468 expected=3.232 match=yes
CLAIM Q11: computed=1.22619701 expected=1.23 match=yes
VERIFICATION SUMMARY: 11 claims, 7 match, 4 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4.81125224 | 4.811 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 2.40562612 | 2.406 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 5.66971966 | 5.67 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 3.84562557 | 3.85 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 1.82400000 | 1.82 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 1291.45227293 | 1292 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 8218.04415415 | 8200 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 125897.30924530 | 126000 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 5192.45589935 | 5193 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 3.23214468 | 3.232 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 1.22619701 | 1.23 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
