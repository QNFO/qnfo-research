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
