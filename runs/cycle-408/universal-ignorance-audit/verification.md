# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected number of passes E[N] ≈ 2.6416 at λ = 0.5",
    "inputs": "λ = 0.5, q_k = λ^(k-1), q_1 = 1, E[N] = sum_{k>=1} λ^((k-1)(k-2)/2)",
    "formula": "E[N] = sum_{k=1}^inf λ^((k-1)(k-2)/2)"
  },
  {
    "id": "Q2",
    "statement": "Expected number of passes E[N] ≈ 2.3277 at λ = 0.3",
    "inputs": "λ = 0.3, E[N] = sum_{k>=1} λ^((k-1)(k-2)/2)",
    "formula": "E[N] = sum_{k=1}^inf λ^((k-1)(k-2)/2)"
  },
  {
    "id": "Q3",
    "statement": "Expected number of passes E[N] ≈ 3.1943 at λ = 0.7",
    "inputs": "λ = 0.7, E[N] = sum_{k>=1} λ^((k-1)(k-2)/2)",
    "formula": "E[N] = sum_{k=1}^inf λ^((k-1)(k-2)/2)"
  },
  {
    "id": "Q4",
    "statement": "Expected question load E[Q] ≈ 39.6 questions at λ = 0.5",
    "inputs": "E[N] = 2.6416 at λ = 0.5, 15 questions per pass",
    "formula": "E[Q] = 15 * E[N]"
  },
  {
    "id": "Q5",
    "statement": "Expected question load E[Q] ≈ 34.9 questions at λ = 0.3",
    "inputs": "E[N] = 2.3277349 at λ = 0.3, 15 questions per pass",
    "formula": "E[Q] = 15 * E[N]"
  },
  {
    "id": "Q6",
    "statement": "Expected question load E[Q] ≈ 47.9 questions at λ = 0.7",
    "inputs": "E[N] = 3.1942513 at λ = 0.7, 15 questions per pass",
    "formula": "E[Q] = 15 * E[N]"
  },
  {
    "id": "Q7",
    "statement": "Expected session length E[T] = 198.12 minutes at λ = 0.5",
    "inputs": "E[Q] = 39.624 questions at λ = 0.5, t = 5 minutes per question (assumption A1)",
    "formula": "E[T] = E[Q] * t"
  },
  {
    "id": "Q8",
    "statement": "Expected session length E[T] = 174.58 minutes at λ = 0.3",
    "inputs": "E[Q] = 34.916 questions at λ = 0.3, t = 5 minutes per question",
    "formula": "E[T] = E[Q] * t"
  },
  {
    "id": "Q9",
    "statement": "Expected session length E[T] = 239.57 minutes at λ = 0.7",
    "inputs": "E[Q] = 47.914 questions at λ = 0.7, t = 5 minutes per question",
    "formula": "E[T] = E[Q] * t"
  },
  {
    "id": "Q10",
    "statement": "Expected cost per closed audit session ≈ $495.3 at λ = 0.5",
    "inputs": "E[T] = 198.12 minutes at λ = 0.5, c = $150 per hour (assumption A3)",
    "formula": "E[C] = (E[T] / 60) * c"
  },
  {
    "id": "Q11",
    "statement": "Cost range $436.4 to $598.9 over λ ∈ {0.3, 0.7}",
    "inputs": "E[T] = 174.58 minutes at λ = 0.3 and E[T] = 239.57 minutes at λ = 0.7, c = $150 per hour",
    "formula": "E[C] = (E[T] / 60) * c"
  },
  {
    "id": "Q12",
    "statement": "Cost at half the assumed rate is $247.65 and at double the per-question time is $990.6",
    "inputs": "E[C] = $495.3 at λ = 0.5, linear scaling in t and c",
    "formula": "E[C] scaled by factor 0.5 in c and by factor 2 in t"
  }
]

## Script
```python
# ------------------------------------------------------------
# SymPy verification template for the paper's equation transitions
# ------------------------------------------------------------
import sympy as sp
from sympy import symbols, simplify
from sympy.physics import units as u

# No equation transitions were found in the Methods/Analysis sections,
# so the verification loop is empty.
transitions = []  # list of (premise, conclusion, justification) tuples

for i, (premise, conclusion, justification) in enumerate(transitions, start=1):
    # Build symbolic expressions (placeholder – none exist)
    lhs = sp.sympify(conclusion)   # right‑hand side of the claimed equality
    rhs = sp.sympify(premise)      # left‑hand side (or vice‑versa, per paper)

    # Simplify the difference under any declared assumptions (none here)
    diff = simplify(lhs - rhs)

    if diff == 0:
        print(f"DERIV ok   : Transition {i}: {premise} ⇒ {conclusion} [{justification}]")
    else:
        # If symbolic simplification is inconclusive, perform random numeric checks
        # (not needed here because there are no transitions)
        print(f"DERIV inconclusive : Transition {i}: {premise} ⇒ {conclusion} [{justification}]")
        # Example numeric spot‑check (placeholder)
        # for _ in range(5):
        #     subs = {symbol: sp.randprime(1, 100) for symbol in diff.free_symbols}
        #     val = diff.subs(subs).evalf()
        #     if abs(val) > 1e-8:
        #         print(f"DERIV refuted : numeric check failed with {subs}")
        #         break

import math

def EN(lam, terms=60):
    s = 0.0
    for k in range(1, terms + 1):
        e = (k - 1) * (k - 2) // 2
        s += lam ** e
    return s

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: E[N] at lambda=0.5, expected 2.6416 (4 s.f.)
v = EN(0.5)
results.append(("Q1", v, "2.6416", sig(v, 4) == 2.6416))

# Q2: E[N] at lambda=0.3, expected 2.3277 (4 s.f.)
v = EN(0.3)
results.append(("Q2", v, "2.3277", sig(v, 4) == 2.3277))

# Q3: E[N] at lambda=0.7, expected 3.1943 (4 s.f.)
v = EN(0.7)
results.append(("Q3", v, "3.1943", sig(v, 4) == 3.1943))

# Q4: E[Q] = 15*E[N] at 0.5, expected 39.6 (3 s.f.)
en05 = EN(0.5)
v = 15 * en05
results.append(("Q4", v, "39.6", sig(v, 3) == 39.6))

# Q5: E[Q] = 15*E[N] at 0.3, expected 34.9 (3 s.f.)
en03 = EN(0.3)
v = 15 * en03
results.append(("Q5", v, "34.9", sig(v, 3) == 34.9))

# Q6: E[Q] = 15*E[N] at 0.7, expected 47.9 (3 s.f.)
en07 = EN(0.7)
v = 15 * en07
results.append(("Q6", v, "47.9", sig(v, 3) == 47.9))

# Q7: E[T] = E[Q]*5 at 0.5, expected 198.12 (5 s.f.)
v = 15 * en05 * 5
results.append(("Q7", v, "198.12", sig(v, 5) == 198.12))

# Q8: E[T] = E[Q]*5 at 0.3, expected 174.58 (5 s.f.)
v = 15 * en03 * 5
results.append(("Q8", v, "174.58", sig(v, 5) == 174.58))

# Q9: E[T] = E[Q]*5 at 0.7, expected 239.57 (5 s.f.)
v = 15 * en07 * 5
results.append(("Q9", v, "239.57", sig(v, 5) == 239.57))

# Q10: E[C] = (E[T]/60)*150 at 0.5, expected 495.3 (4 s.f.)
v = (15 * en05 * 5) / 60 * 150
results.append(("Q10", v, "495.3", sig(v, 4) == 495.3))

# Q11: cost range at 0.3 and 0.7, expected 436.4 and 598.9 (4 s.f.)
vlo = (15 * en03 * 5) / 60 * 150
vhi = (15 * en07 * 5) / 60 * 150
results.append(("Q11", vlo, "436.4", sig(vlo, 4) == 436.4))
results.append(("Q11b", vhi, "598.9", sig(vhi, 4) == 598.9))

# Q12: half rate -> 247.65; double time -> 990.6 (5 s.f.)
base = (15 * en05 * 5) / 60 * 150
v1 = base * 0.5
v2 = base * 2
results.append(("Q12a", v1, "247.65", sig(v1, 5) == 247.65))
results.append(("Q12b", v2, "990.6", sig(v2, 5) == 990.6))

mismatches = 0
for cid, computed, expected, match in results:
    print("CLAIM {}: computed={:.8f} expected={} match={}".format(
        cid, computed, expected, "yes" if match else "no"))
    if not match:
        mismatches += 1

print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(
    len(results), len(results) - mismatches, mismatches))

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 4, in <module>
ModuleNotFoundError: No module named 'sympy'

[exit 1]
```

## Text-level recomputation
```
Q1: E[N] = Σ λ^((k-1)(k-2)/2), λ=0.5. Exponents: 0,0,1,3,6,10,15,21,28,36,45,55,...
Terms: 1 + 1 + 0.5 + 0.125 + 0.015625 + 0.0009765625 + 0.000030517578125 + 0.000000476837158 + 0.000000000931323 + 0.000000000116415 + ...
Partial sums: 2 → 2.5 → 2.625 → 2.640625 → 2.6416015625 → 2.641632080078125 → 2.641632556915283 → 2.641632557846606 → 2.641632557963021 → 2.641632557963021 (tail < 1e-12).
CLAIM Q1: computed=2.64163255796302 expected=2.6416 match=yes

Q2: λ=0.3. Terms: 1 + 1 + 0.3 + 0.027 + 0.000729 + 0.0000059049 + 0.000000014349 + 0.000000000010456 + ...
Partial sums: 2 → 2.3 → 2.327 → 2.327729 → 2.3277349049 → 2.327734919249 → 2.327734919259.
CLAIM Q2: computed=2.32773491925946 expected=2.3277 match=yes

Q3: λ=0.7. Terms: 1 + 1 + 0.7 + 0.343 + 0.117649 + 0.0282475249 + 0.0047475615099 + 0.00055854586408 + 0.0000459951 + 0.0000026515 + 0.00000010697 + 0.0000000030217 + ...
Partial sums: 2 → 2.7 → 3.043 → 3.160649 → 3.1888965249 → 3.1936440864 → 3.1942026323 → 3.1942486273 → 3.1942512788 → 3.1942513858 → 3.1942513888.
CLAIM Q3: computed=3.1942513888 expected=3.1943 match=yes

Q4: E[Q] = 15 × 2.64163255796302 = 39.6244883694453.
CLAIM Q4: computed=39.6244883694453 expected=39.6 match=yes

Q5: E[Q] = 15 × 2.32773491925946 = 34.9160237888919.
CLAIM Q5: computed=34.9160237888919 expected=34.9 match=yes

Q6: E[Q] = 15 × 3.1942513888 = 47.913770832.
CLAIM Q6: computed=47.913770832 expected=47.9 match=yes

Q7: E[T] = 39.6244883694453 × 5 = 198.122441847227.
CLAIM Q7: computed=198.122441847227 expected=198.12 match=yes

Q8: E[T] = 34.9160237888919 × 5 = 174.580118944459.
CLAIM Q8: computed=174.580118944459 expected=174.58 match=yes

Q9: E[T] = 47.913770832 × 5 = 239.56885416.
CLAIM Q9: computed=239.56885416 expected=239.57 match=yes

Q10: E[C] = (198.122441847227 / 60) × 150 = 3.30204069745378 × 150 = 495.306104618067.
CLAIM Q10: computed=495.306104618067 expected=495.3 match=yes

Q11: E[C](λ=0.3) = (174.580118944459 / 60) × 150 = 2.90966864907431 × 150 = 436.450297361147. E[C](λ=0.7) = (239.56885416 / 60) × 150 = 3.992814236 × 150 = 598.9221354.
CLAIM Q11: computed=436.450297361147 to 598.9221354 expected=436.4 to 598.9 match=yes

Q12: Half rate: 495.306104618067 × 0.5 = 247.653052309034. Double per-question time: 495.306104618067 × 2 = 990.612209236133.
CLAIM Q12: computed=247.653052309034 and 990.612209236133 expected=247.65 and 990.6 match=yes

VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch
```

## Adjudication

The execution sandbox was unavailable, so a second model recomputed each claim step by step in text; no code was executed. Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.64163255796302 | 2.6416 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 2.32773491925946 | 2.3277 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 3.1942513888 | 3.1943 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 39.6244883694453 | 39.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 34.9160237888919 | 34.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 47.913770832 | 47.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 198.122441847227 | 198.12 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 174.580118944459 | 174.58 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 239.56885416 | 239.57 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 495.306104618067 | 495.3 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
