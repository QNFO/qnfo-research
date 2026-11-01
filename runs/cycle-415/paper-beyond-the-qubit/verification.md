# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Abelian exchange modulus |R| = 1 for R = e^{2*pi*i*s}",
    "inputs": "R = e^{2*pi*i*s}, s real",
    "formula": "|R| = sqrt(cos^2(2*pi*s) + sin^2(2*pi*s)) = 1"
  },
  {
    "id": "Q2",
    "statement": "Braid length L = ln(1/epsilon) ≈ 7 at epsilon = 10^-3 (unit proportionality constant, natural log)",
    "inputs": "epsilon = 10^-3, constant = 1",
    "formula": "L = ln(1/epsilon) = ln(10^3) = 3*ln(10)"
  },
  {
    "id": "Q3",
    "statement": "Measurement iterations N = 100 for precision delta = 0.1 under 1/sqrt(N) law",
    "inputs": "delta = 0.1, constant = 1",
    "formula": "N = 1/delta^2"
  },
  {
    "id": "Q4",
    "statement": "Threshold margin p_c/p = 37 with p_c = 0.037 and p = 10^-3",
    "inputs": "p_c = 0.037, p = 10^-3",
    "formula": "p_c/p"
  },
  {
    "id": "Q5",
    "statement": "Central overhead N_phys = 10^3 physical qubits per logical qubit",
    "inputs": "alpha = 10^2, p_th = 10^-2, p = 10^-3, beta = 1",
    "formula": "N_phys = alpha*(p_th/p)^beta"
  },
  {
    "id": "Q6",
    "statement": "Lower endpoint of overhead band ≈ 9.09*10^2 at p = 1.1*10^-3",
    "inputs": "alpha = 10^2, p_th = 10^-2, p = 1.1*10^-3, beta = 1",
    "formula": "N_phys = alpha*(p_th/p)^beta"
  },
  {
    "id": "Q7",
    "statement": "Upper endpoint of overhead band ≈ 1.11*10^3 at p = 0.9*10^-3",
    "inputs": "alpha = 10^2, p_th = 10^-2, p = 0.9*10^-3, beta = 1",
    "formula": "N_phys = alpha*(p_th/p)^beta"
  },
  {
    "id": "Q8",
    "statement": "Total physical qubits at lower endpoint: 10^2 logical × 909.09 ≈ 9.09*10^4 ≈ 10^5",
    "inputs": "N_log = 10^2, N_phys = 909.0909...",
    "formula": "N_tot = N_log * N_phys"
  },
  {
    "id": "Q9",
    "statement": "Total physical qubits at upper endpoint: 10^3 logical × 1111.11 ≈ 1.11*10^6 ≈ 10^6",
    "inputs": "N_log = 10^3, N_phys = 1111.1111...",
    "formula": "N_tot = N_log * N_phys"
  },
  {
    "id": "Q10",
    "statement": "Extrapolated overhead at p = 10^-4: N_phys = 10^4 (noted as unphysical for the linear model)",
    "inputs": "alpha = 10^2, p_th = 10^-2, p = 10^-4, beta = 1",
    "formula": "N_phys = alpha*(p_th/p)^beta"
  }
]

## Script
```python
import math

def fmt(x):
    return f"{x:.8g}"

claims = []

# Q1: |R| = 1 for R = e^{2*pi*i*s}, s real (test representative values of s)
s_vals = [0.0, 0.13, 0.5, 1.0, 2.7]
q1_ok = True
for s in s_vals:
    R = math.cos(2*math.pi*s) + 1j*math.sin(2*math.pi*s)
    if abs(abs(R) - 1) > 1e-12:
        q1_ok = False
claims.append(("Q1", 1.0, 1.0, q1_ok))

# Q2: L = ln(1/epsilon) = ln(10^3) = 3*ln(10)
L = 3 * math.log(10)
claims.append(("Q2", L, 6.908, round(L, 3) == 6.908))

# Q3: N = 1/delta^2, delta = 0.1
N = 1 / (0.1 ** 2)
claims.append(("Q3", N, 100.0, round(N) == 100))

# Q4: p_c / p = 0.037 / 10^-3
margin = 0.037 / 1e-3
claims.append(("Q4", margin, 37.0, round(margin) == 37))

# Q5: N_phys = alpha * (p_th/p)^beta, alpha=1e2, p_th=1e-2, p=1e-3, beta=1
alpha, p_th, beta = 1e2, 1e-2, 1
Np5 = alpha * (p_th / 1e-3) ** beta
claims.append(("Q5", Np5, 1000.0, round(Np5) == 1000))

# Q6: lower endpoint, p = 1.1e-3
Np6 = alpha * (p_th / 1.1e-3) ** beta
claims.append(("Q6", Np6, 909.09, round(Np6, 2) == 909.09))

# Q7: upper endpoint, p = 0.9e-3
Np7 = alpha * (p_th / 0.9e-3) ** beta
claims.append(("Q7", Np7, 1111.11, round(Np7, 2) == 1111.11))

# Q8: N_tot = 1e2 * 909.0909...
Ntot8 = 1e2 * (alpha * (p_th / 1.1e-3) ** beta)
claims.append(("Q8", Ntot8, 90909.09, round(Ntot8, 2) == 90909.09))

# Q9: N_tot = 1e3 * 1111.1111...
Ntot9 = 1e3 * (alpha * (p_th / 0.9e-3) ** beta)
claims.append(("Q9", Ntot9, 1111111.11, round(Ntot9, 2) == 1111111.11))

# Q10: extrapolated overhead at p = 1e-4
Np10 = alpha * (p_th / 1e-4) ** beta
claims.append(("Q10", Np10, 10000.0, round(Np10) == 10000))

for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={'yes' if ok else 'no'}")

n = len(claims)
m = sum(1 for c in claims if c[3])
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1 expected=1.0 match=yes
CLAIM Q2: computed=6.9077553 expected=6.908 match=yes
CLAIM Q3: computed=100 expected=100.0 match=yes
CLAIM Q4: computed=37 expected=37.0 match=yes
CLAIM Q5: computed=1000 expected=1000.0 match=yes
CLAIM Q6: computed=909.09091 expected=909.09 match=yes
CLAIM Q7: computed=1111.1111 expected=1111.11 match=yes
CLAIM Q8: computed=90909.091 expected=90909.09 match=yes
CLAIM Q9: computed=1111111.1 expected=1111111.11 match=yes
CLAIM Q10: computed=10000 expected=10000.0 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 6.9077553 | 6.908 | yes | match | 4 significant digits (as printed, at least 3) |
| Q3 | 100 | 100.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 37 | 37.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 1000 | 1000.0 | yes | match | 5 significant digits (as printed, at least 3) |
| Q6 | 909.09091 | 909.09 | yes | match | 5 significant digits (as printed, at least 3) |
| Q7 | 1111.1111 | 1111.11 | yes | match | 6 significant digits (as printed, at least 3) |
| Q8 | 90909.091 | 90909.09 | yes | match | 7 significant digits (as printed, at least 3) |
| Q9 | 1111111.1 | 1111111.11 | yes | match | 9 significant digits (as printed, at least 3) |
| Q10 | 10000 | 10000.0 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
