import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(expected, float) or isinstance(expected, int):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: Gamma_bf = 1/T1_bf
T1_bf = 451e-6
Gamma_bf = 1.0 / T1_bf
results.append(check("Q1", Gamma_bf, 2.2173e3))

# Q2: sigma_Gamma = sigma_T / T1_bf^2
sigma_T = 70e-6
sigma_Gamma = sigma_T / T1_bf**2
results.append(check("Q2", sigma_Gamma, 3.441e2))

# Q3: relative uncertainty = sigma_T / T1_bf
rel_unc = 70.0 / 451.0
results.append(check("Q3", rel_unc, 0.1552))

# Q4: Gamma_L1 = Gamma_L0 / F -> coefficient 1/F
F = 1.59
coeff = 1.0 / F
results.append(check("Q4", coeff, 0.6289))

# Q5: fractional reduction = 1 - 1/F
frac_red = 1.0 - 1.0 / F
results.append(check("Q5", frac_red, 0.371))

# Q6: sigma on 1/F = (1/F^2)*sigma_F
sigma_F = 0.05
sigma_resid = (1.0 / F**2) * sigma_F
results.append(check("Q6", sigma_resid, 0.01978))

# Q7: p_bf = 1 - exp(-Gamma_bf * T_cyc); sigma_p = (T_cyc/T1^2)*exp(-T_cyc/T1)*sigma_T
Gamma_bf_in = 2.2173e3
T_cyc = 1.0e-5
sigma_T7 = 7.0e-5
T1_7 = 4.51e-4
p_bf = 1.0 - math.exp(-Gamma_bf_in * T_cyc)
results.append(check("Q7", p_bf, 0.02193))
sigma_p = (T_cyc / T1_7**2) * math.exp(-T_cyc / T1_7) * sigma_T7
results.append(check("Q7-sigma", sigma_p, 0.0034))

# Q8: p_bf_tm = 1 - exp(-T_cyc/T1_tm)
T1_tm = 3.0e-5
p_bf_tm = 1.0 - math.exp(-T_cyc / T1_tm)
results.append(check("Q8", p_bf_tm, 0.28347))

n = len(results)
m = sum(results)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
