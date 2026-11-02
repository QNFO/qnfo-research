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
