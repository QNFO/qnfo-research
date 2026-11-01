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
