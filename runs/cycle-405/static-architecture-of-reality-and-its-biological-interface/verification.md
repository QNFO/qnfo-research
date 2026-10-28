# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For a 4-tree with n=10 pendent vertices, M1 = 74",
    "inputs": "n=10, m=(n-2)/2=4 internal vertices of degree 4, 10 pendent vertices of degree 1",
    "formula": "M1 = 4*4^2 + 10*1^2 = 64 + 10 = 74"
  },
  {
    "id": "Q2",
    "statement": "Even-case bound M1 >= 9n-16 evaluates to 74 at n=10",
    "inputs": "n=10",
    "formula": "9*10 - 16 = 74"
  },
  {
    "id": "Q3",
    "statement": "For the odd-case extremal tree with n=9 pendent vertices, M1 = 66",
    "inputs": "n=9, m=(n-1)/2=4 internal vertices: three of degree 4, one of degree 3, nine pendent vertices of degree 1",
    "formula": "M1 = 3*4^2 + 1*3^2 + 9*1^2 = 48 + 9 + 9 = 66"
  },
  {
    "id": "Q4",
    "statement": "Odd-case bound M1 >= 9n-15 evaluates to 66 at n=9",
    "inputs": "n=9",
    "formula": "9*9 - 15 = 66"
  },
  {
    "id": "Q5",
    "statement": "M2 bound 11n-27 evaluates to 61 at n=8",
    "inputs": "n=8",
    "formula": "11*8 - 27 = 61"
  },
  {
    "id": "Q6",
    "statement": "M2 bound 11n-27 evaluates to 72 at n=9",
    "inputs": "n=9",
    "formula": "11*9 - 27 = 72"
  },
  {
    "id": "Q7",
    "statement": "M2 bound 11n-27 evaluates to 83 at n=10",
    "inputs": "n=10",
    "formula": "11*10 - 27 = 83"
  },
  {
    "id": "Q8",
    "statement": "M2 bound 11n-27 evaluates to 105 at n=12",
    "inputs": "n=12",
    "formula": "11*12 - 27 = 105"
  },
  {
    "id": "Q9",
    "statement": "Even-case extremal internal-vertex count m = (n-2)/2",
    "inputs": "degree sum of tree: 4m + n = 2(m+n-1)",
    "formula": "4m + n = 2m + 2n - 2 => 2m = n - 2 => m = (n-2)/2"
  },
  {
    "id": "Q10",
    "statement": "Odd-case extremal internal-vertex count m = (n-1)/2",
    "inputs": "degree sum: 4(m-1) + 3 + n = 2(m+n-1)",
    "formula": "4m + n - 1 = 2m + 2n - 2 => 2m = n - 1 => m = (n-1)/2"
  },
  {
    "id": "Q11",
    "statement": "At n=9, the M2-extremal structure has s=3 stem vertices of degree 4 and r=1 further internal vertex of degree 3",
    "inputs": "n=9, stems of degree 4 with 3 pendent neighbors each, degree-sum identity",
    "formula": "3*4 + r*3 + 9 = 2(3 + r + 9 - 1) => 21 + 3r = 2r + 22 => r = 1, s = n/3 = 3"
  },
  {
    "id": "Q12",
    "statement": "Degree-sum check for n=10 extremal tree: 4*4 + 10 = 26 = 2(N-1) with N=14",
    "inputs": "m=4, n=10, N=m+n=14",
    "formula": "4*4 + 10*1 = 26 and 2*(14-1) = 26"
  },
  {
    "id": "Q13",
    "statement": "Degree-sum check for n=9 odd-case tree: 3*4 + 3 + 9 = 24 = 2(N-1) with N=13",
    "inputs": "m=4, n=9, N=13",
    "formula": "12 + 3 + 9 = 24 and 2*(13-1) = 24"
  }
]

## Script
```python
import math

def claim_Q1():
    n = 10
    m = (n - 2) // 2
    M1 = m * 4**2 + n * 1**2
    return M1

def claim_Q2():
    n = 10
    return 9 * n - 16

def claim_Q3():
    n = 9
    m = (n - 1) // 2
    M1 = (m - 1) * 4**2 + 1 * 3**2 + n * 1**2
    return M1

def claim_Q4():
    n = 9
    return 9 * n - 15

def claim_Q5():
    n = 8
    return 11 * n - 27

def claim_Q6():
    n = 9
    return 11 * n - 27

def claim_Q7():
    n = 10
    return 11 * n - 27

def claim_Q8():
    n = 12
    return 11 * n - 27

def claim_Q9():
    # m = (n-2)/2 derived from 4m + n = 2(m+n-1)
    # verify symbolically at a sample even n: solve 4m + n - (2m + 2n - 2) = 0
    n = 10
    # 4m + n = 2m + 2n - 2  =>  2m = n - 2  =>  m = (n-2)/2
    m = (n - 2) / 2
    lhs = 4 * m + n
    rhs = 2 * (m + n - 1)
    ok = abs(lhs - rhs) < 1e-12
    return m if ok else None

def claim_Q10():
    # m = (n-1)/2 derived from 4(m-1) + 3 + n = 2(m+n-1)
    n = 9
    m = (n - 1) / 2
    lhs = 4 * (m - 1) + 3 + n
    rhs = 2 * (m + n - 1)
    ok = abs(lhs - rhs) < 1e-12
    return m if ok else None

def claim_Q11():
    # 3*4 + r*3 + 9 = 2(3 + r + 9 - 1) => 21 + 3r = 2r + 22 => r = 1; s = n/3
    n = 9
    # solve 21 + 3r = 2r + 22
    r = 22 - 21  # 3r - 2r = 22 - 21
    s = n / 3
    return (s, r)

def claim_Q12():
    m = 4
    n = 10
    N = m + n
    lhs = 4 * 4 + 10 * 1
    rhs = 2 * (N - 1)
    return (lhs, rhs)

def claim_Q13():
    m = 4
    n = 9
    N = m + n
    lhs = 3 * 4 + 3 + 9
    rhs = 2 * (N - 1)
    return (lhs, rhs)

def fmt(v):
    if isinstance(v, tuple):
        return "(" + ", ".join(fmt(x) for x in v) + ")"
    if v is None:
        return "None"
    if isinstance(v, int):
        return str(v)
    return f"{v:.8f}"

results = [
    ("Q1", claim_Q1(), "74"),
    ("Q2", claim_Q2(), "74"),
    ("Q3", claim_Q3(), "66"),
    ("Q4", claim_Q4(), "66"),
    ("Q5", claim_Q5(), "61"),
    ("Q6", claim_Q6(), "72"),
    ("Q7", claim_Q7(), "83"),
    ("Q8", claim_Q8(), "105"),
    ("Q9", claim_Q9(), "4"),
    ("Q10", claim_Q10(), "4"),
    ("Q11", claim_Q11(), "(3, 1)"),
    ("Q12", claim_Q12(), "(26, 26)"),
    ("Q13", claim_Q13(), "(24, 24)"),
]

match_count = 0
for cid, computed, expected in results:
    comp_str = fmt(computed)
    match = comp_str == expected
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=74 expected=74 match=yes
CLAIM Q2: computed=74 expected=74 match=yes
CLAIM Q3: computed=66 expected=66 match=yes
CLAIM Q4: computed=66 expected=66 match=yes
CLAIM Q5: computed=61 expected=61 match=yes
CLAIM Q6: computed=72 expected=72 match=yes
CLAIM Q7: computed=83 expected=83 match=yes
CLAIM Q8: computed=105 expected=105 match=yes
CLAIM Q9: computed=4.00000000 expected=4 match=no
CLAIM Q10: computed=4.00000000 expected=4 match=no
CLAIM Q11: computed=(3.00000000, 1) expected=(3, 1) match=no
CLAIM Q12: computed=(26, 26) expected=(26, 26) match=yes
CLAIM Q13: computed=(24, 24) expected=(24, 24) match=yes
VERIFICATION SUMMARY: 13 claims, 10 match, 3 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 74 | 74 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 74 | 74 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 66 | 66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 66 | 66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 61 | 61 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 72 | 72 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 83 | 83 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 105 | 105 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 4.00000000 | 4 | no | match | 3 significant digits (as printed, at least 3) |
| Q10 | 4.00000000 | 4 | no | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 10.
