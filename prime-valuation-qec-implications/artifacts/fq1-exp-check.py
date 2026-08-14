"""FQ1-EXP-001: exploratory scan — do stabilizer weight-enumerator valuation profiles
separate code families?

FQ1 (OPEN): Does there exist a non-trivial valuation invariant of stabilizer codes
(≠ v_2(dim H), v_2(dim H_L)) with classification or predictive power?

Candidate invariant (different from the BLOCKED NTOF Algorithm 4.4): the 2-adic
valuation profile of the stabilizer weight enumerator, v_2(A_j), where
A_j = #{ stabilizer elements of Pauli weight j }.

Design (controls the parameter confound that the 83% claim's design never controlled):
  Structured codes vs random stabilizer codes AT THE SAME (n, k):
    [[5,1,3]] perfect  vs 20 random [[5,1]]
    [[7,1,3]] Steane   vs 20 random [[7,1]]
    [[8,2,2]] toric    vs 20 random [[8,2]]
    [[15,7,3]] Hamming vs 10 random [[15,7]]
  Feature: max_v2 = max_{j>=1} v_2(A_j); n_even = #{j>=1: A_j even}.
  Test: is the structured code's feature an outlier vs the same-parameter random
  distribution? (Exploratory, small sample; NOT the pre-registered REG-RES006-001.)

NOTE: This is EXPLORATORY evidence for FQ1 with a DIFFERENT invariant than the
pre-registered Kodaira-Neron reproduction (still BLOCKED on NTOF source
under-specification: Mahler target function, Cox-ring ideal I_C).
"""
import random


def v2(x):
    c = 0
    while x % 2 == 0 and x > 0:
        x //= 2
        c += 1
    return c


def weight(x, z):
    return bin(x | z).count("1")


def weight_enumerator(gx, gz, n):
    m = len(gx)
    A = [0] * (n + 1)
    A[0] += 1
    for mask in range(1, 1 << m):
        x = 0
        z = 0
        mm = mask
        i = 0
        while mm:
            if mm & 1:
                x ^= gx[i]
                z ^= gz[i]
            mm >>= 1
            i += 1
        A[weight(x, z)] += 1
    return A


def symplectic(x, z, x2, z2):
    return (bin(x & z2).count("1") + bin(z & x2).count("1")) % 2 == 0


def rand_stabilizer_code(n, m, rng):
    """Greedy generation of a random VALID stabilizer code: commuting + independent
    Pauli generators (symplectic pairwise commutativity + group-closure rank check)."""
    gx = []
    gz = []
    group = [(0, 0)]
    for _ in range(m):
        accepted = False
        for _attempt in range(50000):
            x = 0
            z = 0
            for i in range(n):
                t = rng.randrange(4)
                if t in (1, 3):
                    x |= (1 << i)
                if t in (2, 3):
                    z |= (1 << i)
            if not all(symplectic(x, z, gxx, gzz) for gxx, gzz in zip(gx, gz)):
                continue
            new_group = set(group)
            new_group |= {(x ^ gxx, z ^ gzz) for gxx, gzz in group}
            if len(new_group) != 2 * len(group):
                continue
            gx.append(x)
            gz.append(z)
            group = list(new_group)
            accepted = True
            break
        if not accepted:
            raise RuntimeError(f"could not extend stabilizer code at gen {len(gx)} n={n} m={m}")
    return gx, gz


def features(A, n):
    vals = [v2(a) for a in A[1:]]
    return (max(vals) if vals else 0), sum(1 for a in A[1:] if a % 2 == 0)


# ---- structured code generators ----

def five_one_three():
    specs = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
    gx = []
    gz = []
    for s in specs:
        xm = 0
        zm = 0
        for i, c in enumerate(s):
            if c == "X":
                xm |= (1 << i)
            elif c == "Z":
                zm |= (1 << i)
        gx.append(xm)
        gz.append(zm)
    return gx, gz


def steane():
    rows = [(0, 3, 5, 6), (1, 3, 4, 6), (2, 4, 5, 6)]
    gx = []
    gz = []
    for r in rows:
        xm = 0
        for p in r:
            xm |= (1 << p)
        gx.append(xm)
        gz.append(0)
    for r in rows:
        zm = 0
        for p in r:
            zm |= (1 << p)
        gx.append(0)
        gz.append(zm)
    return gx, gz


def hamming15():
    gx = []
    gz = []
    for b in range(4):
        xm = 0
        for p in range(15):
            if ((p + 1) >> b) & 1:
                xm |= (1 << p)
        gx.append(xm)
        gz.append(0)
    for b in range(4):
        zm = 0
        for p in range(15):
            if ((p + 1) >> b) & 1:
                zm |= (1 << p)
        gx.append(0)
        gz.append(zm)
    return gx, gz


def toric(L):
    def eid(i, j, kind):
        return i * L + j if kind == 0 else L * L + i * L + j
    gx = []
    gz = []
    for i in range(L):
        for j in range(L):
            if i == 0 and j == 0:
                continue
            xm = 0
            xm |= (1 << eid((i - 1) % L, j, 0))
            xm |= (1 << eid(i, j, 0))
            xm |= (1 << eid(i, (j - 1) % L, 1))
            xm |= (1 << eid(i, j, 1))
            gx.append(xm)
            gz.append(0)
    for i in range(L):
        for j in range(L):
            if i == 0 and j == 0:
                continue
            zm = 0
            zm |= (1 << eid(i, j, 0))
            zm |= (1 << eid(i, (j + 1) % L, 0))
            zm |= (1 << eid(i, j, 1))
            zm |= (1 << eid((i + 1) % L, j, 1))
            gx.append(0)
            gz.append(zm)
    return gx, gz


# ---- scan ----

def scan():
    rng = random.Random(20260814)  # deterministic seed
    structured = [
        ("[[5,1,3]] perfect", 5, five_one_three(), 20),
        ("[[7,1,3]] Steane", 7, steane(), 20),
        ("[[8,2,2]] toric L=2", 8, toric(2), 20),
        ("[[15,7,3]] Hamming", 15, hamming15(), 10),
    ]
    print("=" * 78)
    print("FQ1-EXP-001: weight-enumerator valuation profiles vs code families")
    print("Invariant: v_2(A_j), A_j = # stabilizer elements of Pauli weight j")
    print("Design: structured vs random AT SAME (n,k); seeded, deterministic")
    print("=" * 78)
    for name, n, (gx, gz), nctrl in structured:
        m = len(gx)
        k = n - m
        A = weight_enumerator(gx, gz, n)
        ok = sum(A) == 2 ** m
        max_v2, n_even = features(A, n)
        print(f"\n{name}: n={n} k={k} m={m} |S|={2**m} sanity={ok}")
        prof = ", ".join(f"w{j}:{A[j]}" for j in range(n + 1) if A[j])
        print(f"  A_j profile: {prof}")
        print(f"  max_v2: {max_v2}  n_even: {n_even}")
        ctrl_v2 = []
        ctrl_even = []
        for _ in range(nctrl):
            cgx, cgz = rand_stabilizer_code(n, m, rng)
            cA = weight_enumerator(cgx, cgz, n)
            cv, ce = features(cA, n)
            ctrl_v2.append(cv)
            ctrl_even.append(ce)
        sv = sorted(ctrl_v2)
        se = sorted(ctrl_even)
        print(f"  control max_v2: min={sv[0]} med={sv[len(sv)//2]} max={sv[-1]}")
        print(f"  control n_even: min={se[0]} med={se[len(se)//2]} max={se[-1]}")
        pv = 100.0 * sum(1 for x in ctrl_v2 if x < max_v2) / nctrl
        pe = 100.0 * sum(1 for x in ctrl_even if x < n_even) / nctrl
        print(f"  structured max_v2 percentile (controls below): {pv:.0f}%")
        print(f"  structured n_even percentile (controls below): {pe:.0f}%")
    print("=" * 78)
    print("Interpretation: pct ~0% = outlier at the LOW end (all-odd enumerator,")
    print("detects structure); pct ~50% = indistinguishable from random at same")
    print("(n,k); pct ~90-100% = outlier at the HIGH end (even-heavy enumerator).")


if __name__ == "__main__":
    scan()
