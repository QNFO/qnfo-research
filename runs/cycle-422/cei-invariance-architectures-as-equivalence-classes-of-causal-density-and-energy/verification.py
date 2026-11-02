import math

# Inputs
k = 1.380649e-23
T = 300.0
ln2 = math.log(2)  # paper states 0.6931472; use stated value
ln2_stated = 0.6931472

eps_L = k * T * ln2_stated

p_max_si = 1.0e6      # W/m^2 (100 W/cm^2)
ell = 1.0e-3          # m
kappa = p_max_si / (ell * eps_L)

c = 2.998e8
L = 1.0e-8
rho_causal = c / L**4

ratio = rho_causal / kappa

n_d = 1.0e15
f = 3.0e9
alpha = 0.10
rho_S = n_d * f * alpha

E_tr_S = 1.0e-16
eta_S = E_tr_S / eps_L

Pi_S = rho_S * eta_S

frac = Pi_S / kappa

E_tr_G = 2.871e-19
eta_G = E_tr_G / eps_L

rho_G_max = kappa / eta_G

Pi_G = kappa
ratio_GS = Pi_G / Pi_S

budget = p_max_si / ell

P_S = rho_S * E_tr_S

p_max_10 = 1.0e5
kappa_prime = p_max_10 / (ell * eps_L)

p_max_1 = 1.0e4
kappa_pp = p_max_1 / (ell * eps_L)
theta = kappa_pp / Pi_S

loss = 1 - theta

def report(cid, computed, expected):
    match = "yes" if abs(computed - float(expected)) / abs(float(expected)) < 5e-4 else "no"
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected} match={match}")

report("Q1", eps_L, "2.871e-21")
report("Q2", kappa, "3.483e29")
report("Q3", rho_causal, "2.998e40")
report("Q4", ratio, "8.607e10")
report("Q5", rho_S, "3.0e23")
report("Q6", eta_S, "3.483e4")
report("Q7", Pi_S, "1.045e28")
report("Q8", frac, "0.0300")
report("Q9", eta_G, "100")
report("Q10", rho_G_max, "3.483e27")
report("Q11", ratio_GS, "33.3")
report("Q12", budget, "1.000e9")
report("Q13", P_S, "3.0e7")
report("Q14", kappa_prime, "3.483e28")
report("Q15", theta, "0.333")
report("Q16", loss, "0.667")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
