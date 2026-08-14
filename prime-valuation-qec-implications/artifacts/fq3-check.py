"""FQ3 computational verification: valuation identities for reversible/Clifford computation.

Question (FQ3/C5): does the branch-depth (p-adic valuation) vocabulary yield a complexity
characterization of reversible/Clifford computation that differs from (or tightens) the
standard one?

Shown analytically: the only valuation data reachable by the vocabulary are cardinality/
dimension invariants:
    v_2(dim H)      = n            (n-qubit state space; C2-style trivial)
    v_2(|Cl(n)|)    = 2n + 1       (Clifford group order)
    v_2(|S_{2^n}|)  = 2^n - 1      (reversible permutation group order, Legendre)
-- all of which are complexity-vacuous (Gottesman-Knill simulability is uniform; circuit
depth/size/stabilizer-rank are Hamming-type counts with no valuation reading, cf. C3/FQ2).

This script verifies the arithmetic identities.
"""
from math import factorial, prod


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v2_of_factorial(m):
    # Legendre: v_2(m!) = m - s_2(m), where s_2(m) is the binary popcount.
    return m - bin(m).count("1")


print("=" * 78)
print("FQ3 verification: valuation identities for reversible/Clifford computation")
print("=" * 78)

# --- 1. Clifford group order |Cl(n)| = 2 * prod_{k=1..n} 4(4^k - 1) -------------
print("\n[1] Clifford group order |Cl(n)| = 2 * prod_k 4(4^k - 1)")
print(f"{'n':>3} {'v_2(|Cl(n)|)':>14} {'2n+1':>6} {'match':>6}")
ok1 = True
for n in range(1, 9):
    order = 2 * prod(4 * (4 ** k - 1) for k in range(1, n + 1))
    got, expect = v2(order), 2 * n + 1
    ok1 = ok1 and got == expect
    print(f"{n:>3} {got:>14} {expect:>6} {str(got == expect):>6}")
print("    all match:", ok1)

# --- 2. Reversible group S_{2^n}: v_2((2^n)!) = 2^n - 1 --------------------------
print("\n[2] Reversible functions on n bits = S_{2^n}; v_2((2^n)!) = 2^n - 1 (Legendre)")
print(f"{'n':>3} {'m=2^n':>7} {'v_2(m!)':>10} {'2^n-1':>6} {'match':>6}")
ok2 = True
for n in range(1, 9):
    m = 2 ** n
    got, expect = v2_of_factorial(m), m - 1
    ok2 = ok2 and got == expect
    print(f"{n:>3} {m:>7} {got:>10} {expect:>6} {str(got == expect):>6}")
print("    all match:", ok2)

# --- 3. State space (trivial) -----------------------------------------------------
print("\n[3] State space dim = 2^n -> v_2(dim H) = n (trivial; C2-style relabeling)")
print("    confirmed for n=1..8:", all(v2(2 ** n) == n for n in range(1, 9)))

# --- 4. Complexity vacuity --------------------------------------------------------
print("\n[4] Complexity vacuity of cardinality valuations")
print("    - Gottesman-Knill: every Clifford circuit simulable in O(n^2)/gate,")
print("      uniformly in v_2(|Cl(n)|) -> group-order valuation carries no cost info")
print("    - circuit depth / gate count / stabilizer rank are Hamming-type counts")
print("      (layers/gates/states), NOT p-adic valuations -> no valuation reading")
print("      (same pattern as code distance d, C3/FQ2)")
print("=" * 78)
print("VERDICT: FQ3 DISCONFIRMED -- no valuation-based complexity characterization")
print("differs from standard measures; candidate identities are complexity-vacuous.")
print("Boundary: p-adic ALGORITHMICS (Hensel codes, p-adic lifting) is a legitimate,")
print("separate computer-algebra topic with real complexity content -- NOT the C5 claim.")
