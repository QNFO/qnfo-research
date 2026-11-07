import math

def sig(x, d):
    # round to d significant digits
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (d - 1))

results = []

# Q1: sigma_q(60) = 1/(60*sqrt(12)) ms
q1 = 1000.0 / (60.0 * math.sqrt(12.0))
results.append(("Q1", q1, "4.811", 4))

# Q2: sigma_q(120) = 1/(120*sqrt(12)) ms
q2 = 1000.0 / (120.0 * math.sqrt(12.0))
results.append(("Q2", q2, "2.406", 4))

# Q3: sigma_ERP(60) = sqrt(3^2 + 4.811^2)
q3 = math.sqrt(3.0**2 + 4.811**2)
results.append(("Q3", q3, "5.67", 3))

# Q4: sigma_ERP(120) = sqrt(3^2 + 2.406^2)
q4 = math.sqrt(3.0**2 + 2.406**2)
results.append(("Q4", q4, "3.85", 3))

# Q5: delta = 5.670 - 3.846
q5 = 5.670 - 3.846
results.append(("Q5", q5, "1.82", 3))

# Q6: n = (1.96*sqrt(p0(1-p0)) + 1.6449*sqrt(p1(1-p1)))^2 / 0.05^2
p0, p1 = 0.5077, 0.5577
za, zb = 1.96, 1.6449
q6 = (za * math.sqrt(p0 * (1 - p0)) + zb * math.sqrt(p1 * (1 - p1)))**2 / (p1 - p0)**2
results.append(("Q6", q6, "1292", 4))

# Q7: variance inflation at 60 Hz
s0 = 20.0
dq60 = 4.811**2
s1sq = s0**2 + dq60
barsq = (s0**2 + s1sq) / 2.0
q7 = 2.0 * (za + zb)**2 * barsq**2 / (s1sq - s0**2)**2
results.append(("Q7", q7, "8200", 2))

# Q8: variance inflation at 120 Hz
dq120 = 2.406**2
s1sq8 = s0**2 + dq120
barsq8 = (s0**2 + s1sq8) / 2.0
q8 = 2.0 * (za + zb)**2 * barsq8**2 / (s1sq8 - s0**2)**2
results.append(("Q8", q8, "126000", 3))

# Q9: n = ((za+zb)/atanh(0.05))^2 + 3
q9 = ((za + zb) / math.atanh(0.05))**2 + 3
results.append(("Q9", q9, "5193", 4))

# Q10: sigma_q(240) and sigma_ERP(240)
q10a = 1000.0 / (240.0 * math.sqrt(12.0))
q10b = math.sqrt(3.0**2 + q10a**2)
results.append(("Q10", q10b, "3.232", 4))

# Q11: delta with sigma_bio = 6
q11 = math.sqrt(6.0**2 + 4.811**2) - math.sqrt(6.0**2 + 2.406**2)
results.append(("Q11", q11, "1.23", 3))

match_count = 0
for cid, comp, exp_str, d in results:
    rounded = sig(comp, d)
    match = "yes" if abs(rounded - float(exp_str)) < 10**(-(d)) * max(1, abs(float(exp_str))) or f"{rounded:.{d}g}" == exp_str else "no"
    # robust match: compare formatted strings
    match = "yes" if f"{rounded:.{d}g}" == exp_str else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={comp:.8f} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
