# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Total quantum dimension at k=1: D_{k=1}=sqrt(1^2+1^2)=sqrt(2)≈1.41421356",
    "inputs": "d_0=1, d_{1/2}=1 (computed from d_j=sin((2j+1)π/(k+2))/sin(π/(k+2)) with k=1)",
    "formula": "D=sqrt(sum_a d_a^2)"
  },
  {
    "id": "Q2",
    "statement": "Total quantum dimension at k=2 (sum-of-squares convention): D_{k=2}=sqrt(1^2+(sqrt2)^2+1^2)=2",
    "inputs": "d_0=1, d_{1/2}=sqrt2, d_1=1 (from d_j formula with k=2)",
    "formula": "D=sqrt(sum_a d_a^2)"
  },
  {
    "id": "Q3",
    "statement": "Closed-form total quantum dimension at k=2: D=(k+2)/(2 sin(π/(k+2)))=2√2≈2.82842712",
    "inputs": "k=2",
    "formula": "D=(k+2)/(2*sin(pi/(k+2)))"
  },
  {
    "id": "Q4",
    "statement": "Quantum dimension d_{1/2} at k=2: sin(2π/4)/sin(π/4)=√2",
    "inputs": "k=2, j=1/2",
    "formula": "d_j=sin((2j+1)π/(k+2))/sin(π/(k+2))"
  },
  {
    "id": "Q5",
    "statement": "Quantum dimension d_{1/2} at k=3: φ=(1+√5)/2≈1.61803399",
    "inputs": "k=3, j=1/2",
    "formula": "d_j=sin((2j+1)π/(k+2))/sin(π/(k+2))"
  },
  {
    "id": "Q6",
    "statement": "Total quantum dimension at k=3 (sum-of-squares convention): D_{k=3}=sqrt(5+√5)≈2.68999405",
    "inputs": "d_0=1, d_{1/2}=φ, d_1=φ, d_{3/2}=1 with φ=(1+√5)/2",
    "formula": "D=sqrt(sum_a d_a^2)"
  },
  {
    "id": "Q7",
    "statement": "Closed-form total quantum dimension at k=3: D=5/(2 sin(π/5))≈4.25325404",
    "inputs": "k=3",
    "formula": "D=(k+2)/(2*sin(pi/(k+2)))"
  },
  {
    "id": "Q8",
    "statement": "Ratio of closed-form to sum-of-squares D at k=3: 4.25325404/2.68999405≈1.58113883=√2.5",
    "inputs": "D_closed(k=3)≈4.25325404, D_sumsq(k=3)≈2.68999405",
    "formula": "ratio=D_closed/D_sumsq"
  },
  {
    "id": "Q9",
    "statement": "Determinant of Ising S-matrix at k=2: det S=(1/2)^3·(−8)=−1",
    "inputs": "S=(1/2)·[[1,√2,1],[√2,0,−√2],[1,−√2,1]]",
    "formula": "det(S)=(1/2)^3*det(M), det(M)=-8"
  },
  {
    "id": "Q10",
    "statement": "Exchange phase for k=1,2,3: φ=π/(k+2) = π/3≈1.04719755, π/4≈0.78539816, π/5≈0.62831853; gaps ≈0.26179939 and ≈0.15707963 rad",
    "inputs": "k=1,2,3",
    "formula": "phi=pi/(k+2)"
  },
  {
    "id": "Q11",
    "statement": "Angular uncertainty from flux precision 10^{-3} Φ_0: Δφ≈10^{-3}×2π≈0.00628 rad, relative error ≈0.8% on q for k=2",
    "inputs": "flux precision 10^{-3} Φ_0, k=2",
    "formula": "Δφ=10^{-3}*2π; relative error=Δφ/(π/4)"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: D_{k=1} = sqrt(1^2 + 1^2) = sqrt(2)
d0 = math.sin(math.pi / 3) / math.sin(math.pi / 3)
dh = math.sin(2 * math.pi / 3) / math.sin(math.pi / 3)
D1 = math.sqrt(d0**2 + dh**2)
results.append(("Q1", D1, "1.41421356"))

# Q2: D_{k=2} = sqrt(1^2 + (sqrt2)^2 + 1^2) = 2
d0 = math.sin(math.pi / 4) / math.sin(math.pi / 4)
dh = math.sin(2 * math.pi / 4) / math.sin(math.pi / 4)
d1 = math.sin(3 * math.pi / 4) / math.sin(math.pi / 4)
D2 = math.sqrt(d0**2 + dh**2 + d1**2)
results.append(("Q2", D2, "2"))

# Q3: closed form D = (k+2)/(2 sin(pi/(k+2))) at k=2
D2c = 4 / (2 * math.sin(math.pi / 4))
results.append(("Q3", D2c, "2.82842712"))

# Q4: d_{1/2} at k=2
d_h2 = math.sin(2 * math.pi / 4) / math.sin(math.pi / 4)
results.append(("Q4", d_h2, "1.41421356"))

# Q5: d_{1/2} at k=3 = golden ratio
d_h3 = math.sin(2 * math.pi / 5) / math.sin(math.pi / 5)
results.append(("Q5", d_h3, "1.61803399"))

# Q6: D_{k=3} = sqrt(5 + sqrt5)
phi = (1 + math.sqrt(5)) / 2
D3 = math.sqrt(1 + phi**2 + phi**2 + 1)
results.append(("Q6", D3, "2.68999405"))

# Q7: closed form at k=3
D3c = 5 / (2 * math.sin(math.pi / 5))
results.append(("Q7", D3c, "4.25325404"))

# Q8: ratio D3c / D3
ratio = D3c / D3
results.append(("Q8", ratio, "1.58113883"))

# Q9: det S at k=2
M = [[1, math.sqrt(2), 1],
     [math.sqrt(2), 0, -math.sqrt(2)],
     [1, -math.sqrt(2), 1]]
detM = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
detS = (0.5)**3 * detM
results.append(("Q9", detS, "-1"))

# Q10: exchange phases and gaps
p1 = math.pi / 3
p2 = math.pi / 4
p3 = math.pi / 5
g12 = p1 - p2
g23 = p2 - p3
results.append(("Q10a", p1, "1.04719755"))
results.append(("Q10b", p2, "0.78539816"))
results.append(("Q10c", p3, "0.62831853"))
results.append(("Q10d", g12, "0.26179939"))
results.append(("Q10e", g23, "0.15707963"))

# Q11: angular uncertainty and relative error at k=2
dphi = 1e-3 * 2 * math.pi
relerr = dphi / (math.pi / 4)
results.append(("Q11a", dphi, "0.00628"))
results.append(("Q11b", relerr, "0.008"))

match_count = 0
for rid, computed, expected in results:
    exp_val = float(expected)
    # number of significant digits stated in the paper's expected value
    digits = len(expected.replace(".", "").replace("-", "").lstrip("0"))
    match = "yes" if sig(computed, digits) == exp_val else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {rid}: computed={computed:.8f} expected={expected} match={match}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.41421356 expected=1.41421356 match=yes
CLAIM Q2: computed=2.00000000 expected=2 match=yes
CLAIM Q3: computed=2.82842712 expected=2.82842712 match=yes
CLAIM Q4: computed=1.41421356 expected=1.41421356 match=yes
CLAIM Q5: computed=1.61803399 expected=1.61803399 match=yes
CLAIM Q6: computed=2.68999405 expected=2.68999405 match=yes
CLAIM Q7: computed=4.25325404 expected=4.25325404 match=yes
CLAIM Q8: computed=1.58113883 expected=1.58113883 match=yes
CLAIM Q9: computed=-1.00000000 expected=-1 match=yes
CLAIM Q10a: computed=1.04719755 expected=1.04719755 match=yes
CLAIM Q10b: computed=0.78539816 expected=0.78539816 match=yes
CLAIM Q10c: computed=0.62831853 expected=0.62831853 match=yes
CLAIM Q10d: computed=0.26179939 expected=0.26179939 match=yes
CLAIM Q10e: computed=0.15707963 expected=0.15707963 match=yes
CLAIM Q11a: computed=0.00628319 expected=0.00628 match=yes
CLAIM Q11b: computed=0.00800000 expected=0.008 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.41421356 | 1.41421356 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q2 | 2.00000000 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 2.82842712 | 2.82842712 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q4 | 1.41421356 | 1.41421356 | yes | match | 9 significant digits (as printed, at least 3) |
| Q5 | 1.61803399 | 1.61803399 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q6 | 2.68999405 | 2.68999405 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q7 | 4.25325404 | 4.25325404 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q8 | 1.58113883 | 1.58113883 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q9 | -1.00000000 | -1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10a | 1.04719755 | 1.04719755 | yes | match | 9 significant digits (as printed, at least 3) |
| Q10b | 0.78539816 | 0.78539816 | yes | match | 8 significant digits (as printed, at least 3) |
| Q10c | 0.62831853 | 0.62831853 | yes | match | 8 significant digits (as printed, at least 3) |
| Q10d | 0.26179939 | 0.26179939 | yes | match | 8 significant digits (as printed, at least 3) |
| Q10e | 0.15707963 | 0.15707963 | yes | match | 8 significant digits (as printed, at least 3) |
| Q11a | 0.00628319 | 0.00628 | yes | match | 3 significant digits (as printed, at least 3) |
| Q11b | 0.00800000 | 0.008 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 16.
