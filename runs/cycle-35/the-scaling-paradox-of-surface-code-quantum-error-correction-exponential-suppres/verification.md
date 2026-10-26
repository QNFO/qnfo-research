# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Reaching p_L = 10^-12 at p = 10^-3 requires d = 21.",
    "inputs": "p_L=1e-12, p=1e-3, p_th=1e-2, A=0.1",
    "formula": "d = 2*log10(p_L/A)/log10(p/p_th) - 1 = 2*(-11)/(-1) - 1 = 21"
  },
  {
    "id": "Q2",
    "statement": "Reaching p_L = 10^-12 at p = 10^-4 requires d = 10.",
    "inputs": "p_L=1e-12, p=1e-4, p_th=1e-2, A=0.1",
    "formula": "d = 2*log10(p_L/A)/log10(p/p_th) - 1 = 2*(-11)/(-2) - 1 = 10"
  },
  {
    "id": "Q3",
    "statement": "Reaching p_L = 10^-6 at p = 10^-3 requires d = 9.",
    "inputs": "p_L=1e-6, p=1e-3, p_th=1e-2, A=0.1",
    "formula": "d = 2*(-5)/(-1) - 1 = 9"
  },
  {
    "id": "Q4",
    "statement": "Reaching p_L = 10^-15 at p = 10^-3 requires d = 27.",
    "inputs": "p_L=1e-15, p=1e-3, p_th=1e-2, A=0.1",
    "formula": "d = 2*(-14)/(-1) - 1 = 27"
  },
  {
    "id": "Q5",
    "statement": "Case A (d=21) uses n = 881 physical qubits.",
    "inputs": "d=21",
    "formula": "n = 2*d^2 - 1 = 2*441 - 1 = 881"
  },
  {
    "id": "Q6",
    "statement": "Case B (d=10) uses n = 199 physical qubits.",
    "inputs": "d=10",
    "formula": "n = 2*100 - 1 = 199"
  },
  {
    "id": "Q7",
    "statement": "Case C (d=9) uses n = 161 physical qubits.",
    "inputs": "d=9",
    "formula": "n = 2*81 - 1 = 161"
  },
  {
    "id": "Q8",
    "statement": "Case D (d=27) uses n = 1457 physical qubits.",
    "inputs": "d=27",
    "formula": "n = 2*729 - 1 = 1457"
  }
]

## Script
```python
import math

def close(a, b):
    if b is None:
        return False
    if isinstance(a, float) or isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-6)
    return a == b

def compute_d(p_L, p, p_th, A):
    return 2 * math.log10(p_L / A) / math.log10(p / p_th) - 1

def compute_n(d):
    return 2 * d**2 - 1

claims = []

# Q1
d = compute_d(1e-12, 1e-3, 1e-2, 0.1)
claims.append(("Q1", d, 21.0))

# Q2
d = compute_d(1e-12, 1e-4, 1e-2, 0.1)
claims.append(("Q2", d, 10.0))

# Q3
d = compute_d(1e-6, 1e-3, 1e-2, 0.1)
claims.append(("Q3", d, 9.0))

# Q4
d = compute_d(1e-15, 1e-3, 1e-2, 0.1)
claims.append(("Q4", d, 27.0))

# Q5
n = compute_n(21)
claims.append(("Q5", n, 881))

# Q6
n = compute_n(10)
claims.append(("Q6", n, 199))

# Q7
n = compute_n(9)
claims.append(("Q7", n, 161))

# Q8
n = compute_n(27)
claims.append(("Q8", n, 1457))

match = 0
mismatch = 0
for cid, comp, exp in claims:
    ok = close(float(comp), float(exp))
    if ok:
        match += 1
    else:
        mismatch += 1
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=21.0 expected=21.0 match=yes
CLAIM Q2: computed=10.0 expected=10.0 match=yes
CLAIM Q3: computed=9.0 expected=9.0 match=yes
CLAIM Q4: computed=27.0 expected=27.0 match=yes
CLAIM Q5: computed=881 expected=881 match=yes
CLAIM Q6: computed=199 expected=199 match=yes
CLAIM Q7: computed=161 expected=161 match=yes
CLAIM Q8: computed=1457 expected=1457 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
