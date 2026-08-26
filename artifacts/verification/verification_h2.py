"""JPC.003 verification — H2 flash-memory structural-protection test (toy simulation).

Equal-rate comparison on a clustered NAND-like channel (page = 64 data bits).

  FLAT: 16 x Hamming[7,4] blocks (48 parity bits, rate 64/112 = 4/7).
        Full-pass decoding every round: all 48 syndrome bits measured and reset.

  TREE: 2-level nested structure, same rate 4/7:
        L1: 16 groups of 4 data bits, 1 parity bit each (odd-error detect) = 16 bits.
        L2: 8 super-groups of 2 groups; 4 parity bits per super-group (bitwise XOR
            across the two groups) = 32 bits. Corrects 1 flagged (erased) group per
            super-group by reconstruction, when the sibling group is clean.
        Hierarchical decode: only super-groups with >=1 L1 flag measure L2 parity.

Metrics per round: (a) erasure count — Landauer-relevant energy proxy
(measured-and-reset parity bits); (b) post-decode residual data-bit error
rate, counted honestly including even-count flag escape and reconstruction
propagation.

Reproducibility: Python 3 stdlib only, fixed seed 20260826.
Run: python verification_h2.py
"""
import json, random

SEED = 20260826
N_DATA = 64
N_GROUPS = 16          # 4 data bits per group
N_BLOCKS = 16          # Hamming [7,4] blocks
N_SUPER = 8            # 2 groups per super-group
L1_PARITY = 16
L2_PARITY = 32
FLAT_ERASURES = 48     # 3 syndrome bits x 16 blocks

def flip_page(p_uniform, n_bursts, burst_len, burst_q, rng):
    """Return set of flipped data-bit indices."""
    flips = set()
    for i in range(N_DATA):
        if rng.random() < p_uniform:
            flips.add(i)
    for _ in range(n_bursts):
        start = rng.randrange(N_DATA)
        for j in range(burst_len):
            if rng.random() < burst_q:
                flips.add((start + j) % N_DATA)
    return flips

def flat_decode(flips):
    """Residual data-bit errors after Hamming[7,4] decode (<=1 error corrected/block)."""
    residual = 0
    for b in range(N_BLOCKS):
        # block covers data bits 4b..4b+3 and parities 64+3b..64+3b+2 (parities unflipped here)
        errs = [i for i in range(4*b, 4*b + 4) if i in flips]
        if len(errs) >= 2:
            residual += len(errs)   # decode failure: data errors remain
        # len(errs) <= 1 -> corrected, 0 residual
    return residual

def tree_decode(flips):
    """Residual + erasure count for the 2-level tree."""
    group_errs = [0] * N_GROUPS
    for i in flips:
        group_errs[i // 4] += 1
    flags = [e % 2 == 1 for e in group_errs]   # odd-error detection
    triggers = 0
    residual = 0
    for sg in range(N_SUPER):
        g0, g1 = 2 * sg, 2 * sg + 1
        e0, e1 = group_errs[g0], group_errs[g1]
        f0, f1 = flags[g0], flags[g1]
        if f0 or f1:
            triggers += 1
            if f0 and not f1 and e1 == 0:
                pass  # g0 erased, reconstructed exactly (sibling clean)
            elif f1 and not f0 and e0 == 0:
                pass  # g1 erased, reconstructed exactly
            elif f0 and not f1 and e1 > 0:
                residual += 2 * e1  # g0 reconstructed from corrupted sibling
                residual += e1      # sibling's own errors remain
            elif f1 and not f0 and e0 > 0:
                residual += 2 * e0
                residual += e0
            else:
                # both flagged (or sibling odd+flagged): uncorrectable
                residual += e0 + e1
        else:
            # no flags: silent even errors remain
            residual += e0 + e1
    erasures = L1_PARITY + 4 * triggers
    return residual, erasures

def run_regime(name, p_uniform, n_bursts, burst_len, burst_q, trials=4000):
    rng = random.Random(SEED)
    acc = {"flat_res": 0.0, "tree_res": 0.0, "flat_erase": 0.0, "tree_erase": 0.0,
           "flat_fail": 0, "tree_fail": 0}
    for _ in range(trials):
        flips = flip_page(p_uniform, n_bursts, burst_len, burst_q, rng)
        fr = flat_decode(flips)
        tr, te = tree_decode(flips)
        acc["flat_res"] += fr
        acc["tree_res"] += tr
        acc["flat_erase"] += FLAT_ERASURES
        acc["tree_erase"] += te
        if fr > 0: acc["flat_fail"] += 1
        if tr > 0: acc["tree_fail"] += 1
    out = {
        "regime": name,
        "p_uniform": p_uniform, "n_bursts": n_bursts, "burst_len": burst_len, "burst_q": burst_q,
        "trials": trials,
        "mean_erasures_flat": acc["flat_erase"] / trials,
        "mean_erasures_tree": acc["tree_erase"] / trials,
        "energy_ratio_flat_over_tree": acc["flat_erase"] / max(acc["tree_erase"], 1e-9),
        "mean_residual_bits_flat": acc["flat_res"] / trials,
        "mean_residual_bits_tree": acc["tree_res"] / trials,
        "failure_rate_flat": acc["flat_fail"] / trials,
        "failure_rate_tree": acc["tree_fail"] / trials,
    }
    return out

def main():
    regimes = [
        ("zero-error", 0.0, 0, 0, 0.0),
        ("uniform p=0.005", 0.005, 0, 0, 0.0),
        ("uniform p=0.02", 0.02, 0, 0, 0.0),
        ("burst c=1 L=8", 0.005, 1, 8, 0.3),
        ("burst c=2 L=8", 0.005, 2, 8, 0.3),
        ("heavy burst c=2 L=16", 0.005, 2, 16, 0.5),
    ]
    results = [run_regime(*r) for r in regimes]

    print(f"{'regime':22s} {'eras_f':>6s} {'eras_t':>6s} {'E ratio':>7s} {'res_f':>6s} {'res_t':>6s} {'fail_f':>7s} {'fail_t':>7s}")
    for r in results:
        print(f"{r['regime']:22s} {r['mean_erasures_flat']:6.1f} {r['mean_erasures_tree']:6.1f} "
              f"{r['energy_ratio_flat_over_tree']:7.2f} {r['mean_residual_bits_flat']:6.3f} "
              f"{r['mean_residual_bits_tree']:6.3f} {r['failure_rate_flat']:7.4f} {r['failure_rate_tree']:7.4f}")

    # Structural checks
    checks = {}
    checks["equal_rate_parity_budgets"] = bool((L1_PARITY + L2_PARITY) == FLAT_ERASURES)
    checks["tree_erasure_ceiling_is_flat"] = all(r["mean_erasures_tree"] <= 48.0 + 1e-9 for r in results)
    checks["zero_error_tree_floor_is_16"] = bool(abs(results[0]["mean_erasures_tree"] - 16.0) < 1e-9)
    checks["zero_error_both_clean"] = bool(results[0]["failure_rate_flat"] == 0.0 and results[0]["failure_rate_tree"] == 0.0)
    checks["flat_erasures_constant_48"] = all(abs(r["mean_erasures_flat"] - 48.0) < 1e-9 for r in results)
    checks["tree_adapts_to_error_density"] = bool(
        results[1]["mean_erasures_tree"] < results[5]["mean_erasures_tree"])
    print("\nChecks:", json.dumps(checks, indent=2))

    with open("h2_results.json", "w") as f:
        json.dump({"seed": SEED, "results": results, "checks": checks}, f, indent=2)
    print("wrote h2_results.json")

if __name__ == "__main__":
    main()
