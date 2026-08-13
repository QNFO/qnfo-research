import random, json, os
from collections import Counter
from math import comb

OUT = os.path.join(os.environ["TEMP"], "res006-p4b-evidence")
os.makedirs(OUT, exist_ok=True)

def vp(n, p=2):
    n = abs(int(n))
    if n == 0:
        return 0
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v

def weight_of(x, z, n):
    return bin(x | z).count("1")

def binary_rank(vecs, width):
    mat = list(vecs)
    rank = 0
    for col in range(width):
        piv = None
        for i in range(rank, len(mat)):
            if (mat[i] >> col) & 1:
                piv = i
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        for i in range(len(mat)):
            if i != rank and ((mat[i] >> col) & 1):
                mat[i] ^= mat[rank]
        rank += 1
    return rank

def group_from_generators(gens, n):
    m = len(gens)
    elems = set()
    for mask in range(1 << m):
        x = 0; z = 0
        for j in range(m):
            if mask & (1 << j):
                x ^= gens[j][0]; z ^= gens[j][1]
        elems.add((x, z))
    return elems

def weight_enumerator(gens, n):
    elems = group_from_generators(gens, n)
    counts = Counter(weight_of(x, z, n) for (x, z) in elems)
    return [counts.get(i, 0) for i in range(n + 1)], len(elems)

def mahler_coeffs(A):
    return [sum((-1) ** (j - i) * comb(j, i) * A[i] for i in range(j + 1)) for j in range(len(A))]

def vp_spectrum(A, p=2):
    return [vp(x, p) for x in mahler_coeffs(A)]

def verify_code(gens, n):
    m = len(gens)
    for a in range(m):
        for b in range(a + 1, m):
            xa, za = gens[a]; xb, zb = gens[b]
            prod = 0
            for i in range(n):
                prod ^= (((xa >> i) & 1) * ((zb >> i) & 1)) ^ (((za >> i) & 1) * ((xb >> i) & 1))
            if prod:
                return None, f"generators {a},{b} anti-commute"
    rank = binary_rank([x | (z << n) for (x, z) in gens], 2 * n)
    A, gsize = weight_enumerator(gens, n)
    if gsize != 2 ** rank:
        return None, f"group size {gsize} != 2^rank={2**rank}"
    if sum(A) != gsize:
        return None, "enumerator sum mismatch"
    minw = None
    for i in range(1, n + 1):
        if A[i] > 0:
            minw = i
            break
    return {"m": m, "rank": rank, "k": n - rank, "group_size": gsize, "min_stab_weight": minw}, None

def encode_pauli(n, x_bits, z_bits):
    x = 0; z = 0
    for i in x_bits:
        x |= (1 << i)
    for i in z_bits:
        z |= (1 << i)
    return (x, z)

def run_code(name, family, n, gens, expected_k=None):
    info, err = verify_code(gens, n)
    if err:
        return {"name": name, "family": family, "n": n, "valid": False, "error": err}
    if expected_k is not None and info["k"] != expected_k:
        return {"name": name, "family": family, "n": n, "valid": False, "error": f"k={info['k']} != expected {expected_k}"}
    A, gsize = weight_enumerator(gens, n)
    spec = vp_spectrum(A, 2)
    c = mahler_coeffs(A)
    return {"name": name, "family": family, "n": n, "k": info["k"], "valid": True,
            "m": info["m"], "rank": info["rank"], "group_size": gsize, "min_stab_weight": info["min_stab_weight"],
            "enumerator": A, "mahler_coeffs": c, "vp_spectrum": spec,
            "vp_max": max(spec) if spec else 0}

results = []

# ---------- CSS: quantum Hamming ----------
def hamming_check(mbits):
    cols = [v for v in range(1, 1 << mbits)]
    n = len(cols)
    rows = [[i for i, v in enumerate(cols) if (v >> r) & 1] for r in range(mbits)]
    return n, rows

for mbits in [3, 4]:
    n, rows = hamming_check(mbits)
    gens = []
    for r in rows:
        gens.append(encode_pauli(n, r, []))
        gens.append(encode_pauli(n, [], r))
    k = n - 2 * mbits
    results.append(run_code(f"Hamming-CSS-{n}-{k}-3", "CSS", n, gens, k))

# ---------- Surface: toric LxL ----------
def toric(L):
    n = 2 * L * L
    gens = []
    def eidx(i, j, vert):
        i %= L; j %= L
        return (L * L + i * L + j) if vert else (i * L + j)
    for i in range(L):
        for j in range(L):
            gens.append(encode_pauli(n, [eidx(i - 1, j, False), eidx(i, j, False), eidx(i, j, True), eidx(i, j - 1, True)], []))
            gens.append(encode_pauli(n, [], [eidx(i, j, False), eidx(i, j + 1, False), eidx(i + 1, j, True), eidx(i, j, True)]))
    return n, gens

for L in [2, 3]:
    n, gens = toric(L)
    results.append(run_code(f"Toric-{L}-{n}-2-{L}", "Surface", n, gens, 2))

# ---------- Optimal: [[5,1,3]] ----------
g5 = [encode_pauli(5, [0, 3], [1, 2]),
      encode_pauli(5, [1, 4], [2, 3]),
      encode_pauli(5, [0, 2], [3, 4]),
      encode_pauli(5, [1, 3], [0, 4])]
results.append(run_code("Five-Qubit-5-1-3", "Optimal", 5, g5, 1))

# ---------- Random: 50 (FIXED: t != q in CNOT) ----------
def random_clifford_code(n, k, seed):
    rng = random.Random(seed)
    m = n - k
    gens = [(1 << i, 0) for i in range(m)]
    ops = list(range(n))
    for _ in range(6 * n):
        g = rng.random()
        if g < 0.4:
            q = rng.choice(ops)
            others = [x for x in ops if x != q]
            t = rng.choice(others)
            gens = [(x ^ (((x >> q) & 1) << t), z ^ (((z >> t) & 1) << q)) for (x, z) in gens]
        elif g < 0.7:
            q = rng.choice(ops)
            new = []
            for (x, z) in gens:
                xq = (x >> q) & 1; zq = (z >> q) & 1
                new.append(((x & ~(1 << q)) | (zq << q), (z & ~(1 << q)) | (xq << q)))
            gens = new
        else:
            q = rng.choice(ops)
            gens = [(x, z ^ (((x >> q) & 1) << q)) for (x, z) in gens]
    return gens

for seed in range(50):
    n, k = 10, 4
    gens = random_clifford_code(n, k, seed)
    results.append(run_code(f"Random-{seed:02d}-10-4", "Random", n, gens, k))

# ---------- aggregate ----------
families = {}
for r in results:
    families.setdefault(r["family"], []).append(r)

print("=== VALIDITY ===")
ninvalid = sum(1 for r in results if not r["valid"])
for r in results:
    if not r["valid"]:
        print("INVALID:", r["name"], r.get("error"))
print("invalid:", ninvalid, "/", len(results))

print("\n=== FAMILY SUMMARY ===")
table = {}
for fam, rs in families.items():
    valid = [r for r in rs if r["valid"]]
    vps = sorted(r["vp_max"] for r in valid)
    table[fam] = {"count_valid": len(valid), "count_total": len(rs),
                  "vp_max_values": vps,
                  "vp_max_median": vps[len(vps) // 2] if vps else None,
                  "vp_max_min": vps[0] if vps else None, "vp_max_max": vps[-1] if vps else None,
                  "min_stab_weights": sorted(r["min_stab_weight"] for r in valid)}
    print(f"{fam}: valid={len(valid)}/{len(rs)} vp_max={vps}")

print("\n=== C7.3' SEPARATION TEST ===")
opt = [r["vp_max"] for r in families.get("Optimal", []) if r["valid"]]
rnd = [r["vp_max"] for r in families.get("Random", []) if r["valid"]]
css = [r["vp_max"] for r in families.get("CSS", []) if r["valid"]]
surf = [r["vp_max"] for r in families.get("Surface", []) if r["valid"]]
om = sorted(opt)[len(opt) // 2]; rm = sorted(rnd)[len(rnd) // 2]
print(f"vp_max medians: Optimal={om}, Random={rm}, CSS={sorted(css)[len(css)//2]}, Surface={sorted(surf)[len(surf)//2]}")
print(f"gap optimal-random: {om - rm}")
print(f"random max ({max(rnd)}) vs optimal ({opt}): random exceeds optimal: {max(rnd) > max(opt)}")
print(f"CLAIMED: optimal=28 vs random=4 (gap >= 10). OBSERVED at n<=18: gap={om - rm}, optimal max vp_max={max(opt)}")

print("\n=== DETAILED (non-random) ===")
for r in results:
    if r["family"] != "Random":
        slim = {k: v for k, v in r.items() if k not in ("enumerator", "mahler_coeffs", "vp_spectrum")}
        print(json.dumps(slim, default=str))

with open(os.path.join(OUT, "rq3-results.json"), "w", encoding="utf-8") as f:
    json.dump({"families": table, "codes": results}, f, indent=1, default=str)
print("\nSAVED:", os.path.join(OUT, "rq3-results.json"))
