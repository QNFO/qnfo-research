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
