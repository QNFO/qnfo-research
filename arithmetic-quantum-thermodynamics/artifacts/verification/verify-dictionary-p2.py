"""verify-dictionary-p2.py — QNFO.RES.031 P2 smoke suite (VERIFY-IN-CODE-1).

Checks every computable row of the corrected dictionary (docs/corrected-dictionary.md)
against exact truncated products, closed forms, and finite differences.
Deterministic (no randomness). Run: python verify-dictionary-p2.py
Output goes to stdout; redirect to verify-dictionary-p2-output.txt for the record.

v2 fixes (from v1 run): tail-corrected comparisons for truncated products at
P=1e6 (tail ~ 1/(P ln P) ~ 7e-8); Gentile m=1 tolerance relaxed for float
round-off; fugacity product/sum use the same prime cutoff (200000); twin-gap
demo restricted to primes >= 3 (the (2,3) gap-1 pair excluded per dictionary).
"""
import math
from math import log, pi

def sieve_upto(N):
    s = bytearray([1]) * (N + 1)
    if N >= 0: s[0] = 0
    if N >= 1: s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(2, N + 1) if s[i]]

results = []
def check(name, got, want, tol):
    # ABSOLUTE tolerance (red-team A-6 fix, 2026-08-29): the check names state
    # absolute windows; relative semantics (tol*max(1,|want|)) silently widened
    # large-magnitude guardrails — e.g. the 311.9 anchor at tol 0.5 would have
    # accepted 316.3. All tolerances below are absolute.
    ok = abs(got - want) <= tol
    results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} want={want!r} tol={tol}")

BETA = 2.0
P = 10**6
primes = sieve_upto(P)

# --- C1 identities at beta=2 ------------------------------------------------
ZB = 1.0
ZF = 1.0
lZMB = 0.0
for p in primes:
    x = p ** (-BETA)
    ZB *= 1.0 / (1.0 - x)
    ZF *= 1.0 + x
    lZMB += x
z2 = pi * pi / 6.0
z4 = pi ** 4 / 90.0
# Truncation tail of each log at P=1e6: sum_{p>P} p^-2 ~ E1(ln P)/P with the
# 3-term expansion (1 - 1/lnP + 2/ln^2P); the 1-term form 1/(P ln P) errs by ~7%.
tail = (1.0 / (P * log(P))) * (1.0 - 1.0 / log(P) + 2.0 / (log(P) ** 2))
check("Z_Bose = zeta(2) (raw, tol 2e-7)", ZB, z2, 2e-7)
check("ln Z_Bose = ln zeta(2) - tail (tail-corrected)", log(ZB) + tail, log(z2), 1e-9)
check("Z_Fermi = zeta(2)/zeta(4) (raw, tol 2e-7)", ZF, z2 / z4, 2e-7)
check("ln Z_Fermi = ln(zeta2/zeta4) - tail (tail-corrected)", log(ZF) + tail, log(z2 / z4), 1e-9)
check("ln Z_MB = P(2) (raw, tol 1e-7)", lZMB, 0.4522474200410655, 1e-7)
check("ln Z_MB = P(2) - tail (tail-corrected)", lZMB + tail, 0.4522474200410655, 1e-9)

# --- Prime-zeta expansions (k=1..30) ----------------------------------------
def P(kb):
    return sum(p ** (-kb) for p in primes)
lZB_exp = sum(P(BETA * k) / k for k in range(1, 31))
lZF_exp = sum((-1) ** (k + 1) * P(BETA * k) / k for k in range(1, 31))
check("unification: ln Z_Bose = sum P(2k)/k", lZB_exp, log(ZB), 1e-9)
check("unification: ln Z_Fermi = sum (-1)^(k+1) P(2k)/k", lZF_exp, log(ZF), 1e-9)

# --- Gentile family -----------------------------------------------------------
def Z_gentile(m, beta):
    out = 1.0
    for p in primes:
        x = p ** (-beta)
        out *= (1.0 - x ** (m + 1)) / (1.0 - x)
    return out
check("Gentile m=1 -> Fermi (tol 1e-9, float round-off aware)", Z_gentile(1, BETA), ZF, 1e-9)
check("Gentile m=40 -> Bose (approx)", Z_gentile(40, BETA), ZB, 1e-12)

# --- Thermodynamic fixes at beta=2 (Bose) ------------------------------------
U = sum(log(p) * p ** (-BETA) / (1.0 - p ** (-BETA)) for p in primes)
CV_formula = BETA * BETA * sum(log(p) ** 2 * p ** (-BETA) / (1.0 - p ** (-BETA)) ** 2 for p in primes)
h = 1e-6
def U_beta(b):
    return sum(log(p) * p ** (-b) / (1.0 - p ** (-b)) for p in primes)
CV_fd = -(BETA * BETA) * (U_beta(BETA + h) - U_beta(BETA - h)) / (2 * h)
dU_fd = (U_beta(BETA + h) - U_beta(BETA - h)) / (2 * h)
check("C_V = -beta^2 dU/dbeta (finite-diff)", CV_formula, CV_fd, 1e-6)
check("C_V != +dU/dbeta (draft error reproduced as mismatch)", CV_formula != dU_fd, True, 0)
S_formula = sum(-log(1 - p ** (-BETA)) + BETA * log(p) * p ** (-BETA) / (1 - p ** (-BETA)) for p in primes)
check("S = ln Z + beta U", S_formula, log(ZB) + BETA * U, 1e-9)

# --- Anchors at beta=1.06 ----------------------------------------------------
b = 1.06
pole = b * b / (b - 1.0) ** 2
check("analytic anchor beta^2/(beta-1)^2", pole, 312.111111, 1e-5)
N = 10**7
big = sieve_upto(N)
S = sum(log(p) ** 2 * p ** (-b) / (1.0 - p ** (-b)) ** 2 for p in big) * b * b
tailc = b * b * (N ** (-(b - 1.0)) * (log(N) / (b - 1.0) + 1.0 / (b - 1.0) ** 2))
exact_total = S + tailc
check("exact total C_V(1.06) ~ 311.9 (parent-verified)", exact_total, 311.9, 0.5)
check("legacy 316.3 is NOT the exact value", abs(316.3 - exact_total) > 1.0, True, 0)

# --- Twin-gap hard core (primes >= 3; (2,3) excluded as the unique gap-1 pair) ---
small = [p for p in primes if 3 <= p < 1000]
gaps = [small[i+1] - small[i] for i in range(len(small) - 1)]
mean_gap = sum(gaps) / len(gaps)
min_unfolded = min(gaps) / mean_gap
check("twin-gap: min gap = 2 for primes >= 3", min(gaps), 2, 0)
print(f"[INFO] primes in [3,1000): min gap = {min(gaps)}, mean gap = {mean_gap:.2f}, min unfolded spacing = {min_unfolded:.4f}")
print(f"[INFO] first bin [0, {0.5 * min_unfolded:.4f}) contains zero spacings by construction (bin width < min unfolded spacing)")

# --- Fugacity vs character ----------------------------------------------------
# Same prime cutoff (200000) on both sides: product over primes <= 200000,
# sum over n <= 200000 (all of whose prime factors are <= 200000).
z = 0.5
LIM = 200000
Zmu_product = 1.0
for p in primes:
    if p <= LIM:
        Zmu_product *= 1.0 / (1.0 - z * p ** (-BETA))
def omega(n):
    c = 0
    for p in primes:
        if p * p > n: break
        while n % p == 0:
            c += 1; n //= p
    if n > 1: c += 1
    return c
Zmu_sum = sum(z ** omega(n) * n ** (-BETA) for n in range(1, LIM + 1))
check("fugacity Z_mu = prod (1 - z p^-beta)^-1 = sum z^Omega(n) n^-beta (same cutoff)", Zmu_product, Zmu_sum, 1e-6)
print("[INFO] Z_mu is the z-weighted generating function — NOT an L-function (no character twist)")

print()
print(f"SUMMARY: {sum(results)}/{len(results)} checks passed")
exit(0 if all(results) else 1)
