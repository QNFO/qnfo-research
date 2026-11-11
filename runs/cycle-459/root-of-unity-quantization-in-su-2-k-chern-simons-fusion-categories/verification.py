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
