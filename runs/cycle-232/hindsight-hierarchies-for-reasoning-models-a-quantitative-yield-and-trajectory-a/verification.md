# Verification report

## Extracted claims
[
  {
    "id": "C1",
    "statement": "Clean idea amplification per solved problem per round is A = 2.4.",
    "inputs": "m = 5, r = 0.6, p = 0.8",
    "formula": "A = m * r * p"
  },
  {
    "id": "C2",
    "statement": "After five rounds the solved‑problem corpus size is N5 = 4685.59.",
    "inputs": "P = 10000, N0 = 1000, sigma = 0.1, t = 5",
    "formula": "N_t = P - (P - N0) * (1 - sigma)^t"
  },
  {
    "id": "C3a",
    "statement": "Round 1 adds 900 solved problems.",
    "inputs": "sigma = 0.1, U0 = P - N0 = 9000",
    "formula": "addition = sigma * U0"
  },
  {
    "id": "C3b",
    "statement": "Round 2 adds 810 solved problems.",
    "inputs": "sigma = 0.1, U1 = P - N1 = 8100",
    "formula": "addition = sigma * U1"
  },
  {
    "id": "C3c",
    "statement": "Round 3 adds 729 solved problems.",
    "inputs": "sigma = 0.1, U2 = P - N2 = 7290",
    "formula": "addition = sigma * U2"
  },
  {
    "id": "C3d",
    "statement": "Round 4 adds 656.1 solved problems.",
    "inputs": "sigma = 0.1, U3 = P - N3 = 6561",
    "formula": "addition = sigma * U3"
  },
  {
    "id": "C3e",
    "statement": "Round 5 adds 590.49 solved problems.",
    "inputs": "sigma = 0.1, U4 = P - N4 = 5904.9",
    "formula": "addition = sigma * U4"
  },
  {
    "id": "C4",
    "statement": "The corpus after five rounds is 4.68559 times the seed corpus.",
    "inputs": "N5 = 4685.59, N0 = 1000",
    "formula": "ratio = N5 / N0"
  },
  {
    "id": "C5",
    "statement": "Reaching 90 % of the problem pool requires about 21 rounds (t≈20.85).",
    "inputs": "phi = 0.9, P = 10000, N0 = 1000, sigma = 0.1",
    "formula": "t = ln((P - phi * P) / (P - N0)) / ln(1 - sigma)"
  },
  {
    "id": "C6",
    "statement": "Reaching 50 % of the problem pool requires about 6 rounds (t≈5.58).",
    "inputs": "phi = 0.5, P = 10000, N0 = 1000, sigma = 0.1",
    "formula": "t = ln((P - phi * P) / (P - N0)) / ln(1 - sigma)"
  },
  {
    "id": "C7",
    "statement": "The sum of solved problems over rounds 0‑5 is ΣNτ = 17829.69.",
    "inputs": "P = 10000, N0 = 1000, sigma = 0.1, T = 5",
    "formula": "ΣNτ = (T+1) * P - (P - N0) * (1 - (1 - sigma)^{T+1}) / sigma"
  },
  {
    "id": "C8",
    "statement": "Cumulative clean idea pairs after five rounds are C5 = 42791.26.",
    "inputs": "mrp = 2.4, ΣNτ = 17829.69",
    "formula": "C5 = mrp * ΣNτ"
  },
  {
    "id": "C9",
    "statement": "Cumulative amplification relative to seed is A5 = 42.791256 (≈42.79×).",
    "inputs": "C5 = 42791.26, N0 = 1000",
    "formula": "A5 = C5 / N0"
  },
  {
    "id": "C10",
    "statement": "Break‑even extraction precision is p > 1/(m r) = 0.3333.",
    "inputs": "m = 5, r = 0.6",
    "formula": "p > 1 / (m * r)"
  },
  {
    "id": "C11",
    "statement": "Model‑generated corpus fraction after five rounds is f5 = 0.786582 (≈78.66%).",
    "inputs": "N0 = 1000, N5 = 4685.59",
    "formula": "f5 = 1 - N0 / N5"
  },
  {
    "id": "C13",
    "statement": "Total spurious idea pairs after five rounds are 10697.81.",
    "inputs": "p = 0.8, m = 5, r = 0.6, ΣNτ = 17829.69",
    "formula": "spurious = (1 - p) * m * r * ΣNτ"
  }
]

## Script
```python
import math

# Inputs
P = 10000
N0 = 1000
sigma = 0.1
m = 5
r = 0.6
p = 0.8
mrp = m * r * p  # 2.4
phi90 = 0.9
phi50 = 0.5

def round_to_expected(val, expected_str):
    if '.' in expected_str:
        ndigits = len(expected_str.split('.')[1])
    else:
        ndigits = 0
    return round(val, ndigits)

def check(val, expected_str):
    rounded = round_to_expected(val, expected_str)
    match = (str(rounded) == expected_str)
    return rounded, match

# C1
C1_val = mrp
C1_exp = "2.4"
C1_cmp, C1_match = check(C1_val, C1_exp)

# C2
t = 5
N5 = P - (P - N0) * (1 - sigma) ** t
C2_exp = "4685.59"
C2_cmp, C2_match = check(N5, C2_exp)

# C3a
U0 = P - N0
add1 = sigma * U0
C3a_exp = "900"
C3a_cmp, C3a_match = check(add1, C3a_exp)

# C3b
N1 = P - (P - N0) * (1 - sigma) ** 1
U1 = P - N1
add2 = sigma * U1
C3b_exp = "810"
C3b_cmp, C3b_match = check(add2, C3b_exp)

# C3c
N2 = P - (P - N0) * (1 - sigma) ** 2
U2 = P - N2
add3 = sigma * U2
C3c_exp = "729"
C3c_cmp, C3c_match = check(add3, C3c_exp)

# C3d
N3 = P - (P - N0) * (1 - sigma) ** 3
U3 = P - N3
add4 = sigma * U3
C3d_exp = "656.1"
C3d_cmp, C3d_match = check(add4, C3d_exp)

# C3e
N4 = P - (P - N0) * (1 - sigma) ** 4
U4 = P - N4
add5 = sigma * U4
C3e_exp = "590.49"
C3e_cmp, C3e_match = check(add5, C3e_exp)

# C4
ratio = N5 / N0
C4_exp = "4.68559"
C4_cmp, C4_match = check(ratio, C4_exp)

# C5
t90 = math.log((P - phi90 * P) / (P - N0)) / math.log(1 - sigma)
C5_exp = "20.85"
C5_cmp, C5_match = check(t90, C5_exp)

# C6
t50 = math.log((P - phi50 * P) / (P - N0)) / math.log(1 - sigma)
C6_exp = "5.58"
C6_cmp, C6_match = check(t50, C6_exp)

# C7
T = 5
sum_N = (T + 1) * P - (P - N0) * (1 - (1 - sigma) ** (T + 1)) / sigma
C7_exp = "17829.69"
C7_cmp, C7_match = check(sum_N, C7_exp)

# C8
C5_val = mrp * sum_N
C8_exp = "42791.26"
C8_cmp, C8_match = check(C5_val, C8_exp)

# C9
A5 = C5_val / N0
C9_exp = "42.791256"
C9_cmp, C9_match = check(A5, C9_exp)

# C10
threshold = 1 / (m * r)
C10_exp = "0.3333"
C10_cmp, C10_match = check(threshold, C10_exp)

# C11
f5 = 1 - N0 / N5
C11_exp = "0.786582"
C11_cmp, C11_match = check(f5, C11_exp)

# C13
spurious = (1 - p) * m * r * sum_N
C13_exp = "10697.81"
C13_cmp, C13_match = check(spurious, C13_exp)

# Print results
claims = [
    ("C1", C1_cmp, C1_exp, C1_match),
    ("C2", C2_cmp, C2_exp, C2_match),
    ("C3a", C3a_cmp, C3a_exp, C3a_match),
    ("C3b", C3b_cmp, C3b_exp, C3b_match),
    ("C3c", C3c_cmp, C3c_exp, C3c_match),
    ("C3d", C3d_cmp, C3d_exp, C3d_match),
    ("C3e", C3e_cmp, C3e_exp, C3e_match),
    ("C4", C4_cmp, C4_exp, C4_match),
    ("C5", C5_cmp, C5_exp, C5_match),
    ("C6", C6_cmp, C6_exp, C6_match),
    ("C7", C7_cmp, C7_exp, C7_match),
    ("C8", C8_cmp, C8_exp, C8_match),
    ("C9", C9_cmp, C9_exp, C9_match),
    ("C10", C10_cmp, C10_exp, C10_match),
    ("C11", C11_cmp, C11_exp, C11_match),
    ("C13", C13_cmp, C13_exp, C13_match),
]

for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,_,ok in claims if ok)} match, {sum(1 for _,_,_,ok in claims if not ok)} mismatch")

```

## Execution output
```
CLAIM C1: computed=2.4 expected=2.4 match=yes
CLAIM C2: computed=4685.59 expected=4685.59 match=yes
CLAIM C3a: computed=900.0 expected=900 match=no
CLAIM C3b: computed=810.0 expected=810 match=no
CLAIM C3c: computed=729.0 expected=729 match=no
CLAIM C3d: computed=656.1 expected=656.1 match=yes
CLAIM C3e: computed=590.49 expected=590.49 match=yes
CLAIM C4: computed=4.68559 expected=4.68559 match=yes
CLAIM C5: computed=20.85 expected=20.85 match=yes
CLAIM C6: computed=5.58 expected=5.58 match=yes
CLAIM C7: computed=17829.69 expected=17829.69 match=yes
CLAIM C8: computed=42791.26 expected=42791.26 match=yes
CLAIM C9: computed=42.791256 expected=42.791256 match=yes
CLAIM C10: computed=0.3333 expected=0.3333 match=yes
CLAIM C11: computed=0.78658 expected=0.786582 match=no
CLAIM C13: computed=10697.81 expected=10697.81 match=yes
VERIFICATION SUMMARY: 16 claims, 12 match, 4 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| C1 | 2.4 | 2.4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C2 | 4685.59 | 4685.59 | yes | match | 6 significant digits (as the paper states, at least 2) |
| C3a | 900.0 | 900 | no | match | 3 significant digits (as the paper states, at least 2) |
| C3b | 810.0 | 810 | no | match | 3 significant digits (as the paper states, at least 2) |
| C3c | 729.0 | 729 | no | match | 3 significant digits (as the paper states, at least 2) |
| C3d | 656.1 | 656.1 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C3e | 590.49 | 590.49 | yes | match | 5 significant digits (as the paper states, at least 2) |
| C4 | 4.68559 | 4.68559 | yes | match | 6 significant digits (as the paper states, at least 2) |
| C5 | 20.85 | 20.85 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C6 | 5.58 | 5.58 | yes | match | 3 significant digits (as the paper states, at least 2) |
| C7 | 17829.69 | 17829.69 | yes | match | 7 significant digits (as the paper states, at least 2) |
| C8 | 42791.26 | 42791.26 | yes | match | 7 significant digits (as the paper states, at least 2) |
| C9 | 42.791256 | 42.791256 | yes | match | 8 significant digits (as the paper states, at least 2) |
| C10 | 0.3333 | 0.3333 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C11 | 0.78658 | 0.786582 | no | MISMATCH | 6 significant digits (as the paper states, at least 2) |
| C13 | 10697.81 | 10697.81 | yes | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 16.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| C11 | 0.786582 | 0.78658 |
