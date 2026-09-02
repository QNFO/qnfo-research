"""JPC.003 v1.7 evidence delta - robustness sweep of the H2 erasure-ratio claim.

Reuses the EXACT H2 toy model (verification_h2.py) and sweeps the clustered-channel
parameters around the paper's six regimes to map where the flat/tree erasure ratio
1.6-3x persists and where it collapses. Same equal-rate budgets, same metrics.
Run: python verification_h2_sweep.py
"""
import json, random, sys

SEED = 20260826
N_DATA = 64; N_GROUPS = 16; N_BLOCKS = 16; N_SUPER = 8
L1_PARITY = 16; L2_PARITY = 32; FLAT_ERASURES = 48

def flip_page(p_uniform, n_bursts, burst_len, burst_q, rng):
    flips = set()
    for i in range(N_DATA):
        if rng.random() < p_uniform: flips.add(i)
    for _ in range(n_bursts):
        start = rng.randrange(N_DATA)
        for j in range(burst_len):
            if rng.random() < burst_q: flips.add((start + j) % N_DATA)
    return flips

def flat_decode(flips):
    residual = 0
    for b in range(N_BLOCKS):
        errs = [i for i in range(4*b, 4*b+4) if i in flips]
        if len(errs) >= 2: residual += len(errs)
    return residual

def tree_decode(flips):
    group_errs = [0]*N_GROUPS
    for i in flips: group_errs[i//4] += 1
    flags = [e % 2 == 1 for e in group_errs]
    triggers = 0; residual = 0
    for sg in range(N_SUPER):
        g0, g1 = 2*sg, 2*sg+1
        e0, e1 = group_errs[g0], group_errs[g1]
        f0, f1 = flags[g0], flags[g1]
        if f0 or f1:
            triggers += 1
            if f0 and not f1 and e1 == 0: pass
            elif f1 and not f0 and e0 == 0: pass
            elif f0 and not f1 and e1 > 0: residual += 3*e1
            elif f1 and not f0 and e0 > 0: residual += 3*e0
            else: residual += e0 + e1
        else:
            residual += e0 + e1
    return residual, L1_PARITY + 4*triggers

def run_regime(name, p_u, nb, bl, bq, trials=2000):
    rng = random.Random(SEED)
    frs = tres = fe = te = 0
    for _ in range(trials):
        flips = flip_page(p_u, nb, bl, bq, rng)
        fr = flat_decode(flips); tr, tev = tree_decode(flips)
        frs += fr; tres += tr; fe += FLAT_ERASURES; te += tev
    return {"regime": name, "p_uniform": p_u, "n_bursts": nb, "burst_len": bl, "burst_q": bq,
            "mean_erasures_flat": round(fe/trials,3), "mean_erasures_tree": round(te/trials,3),
            "energy_ratio_flat_over_tree": round((fe/trials)/(te/trials),3),
            "mean_residual_bits_flat": round(frs/trials,4), "mean_residual_bits_tree": round(tres/trials,4)}

# Sweep: hold uniform p=0.005 (as in burst regimes), vary burst count/length/quality
regimes = []
for nb, bl, bq in [(1,4,0.3),(1,16,0.3),(1,8,0.1),(1,8,0.5),(3,8,0.3),(2,16,0.3),
                   (2,8,0.1),(2,8,0.5),(2,4,0.3),(4,8,0.3),(2,32,0.3),(1,32,0.5)]:
    regimes.append(run_regime(f"burst c={nb} L={bl} q={bq}", 0.005, nb, bl, bq))

print("Sweep of flat/tree erasure ratio (uniform p=0.005 background):")
print(f"{'regime':24s} {'eras_t':>7s} {'ratio':>7s} {'res_f':>8s} {'res_t':>8s}")
for r in regimes:
    print(f"{r['regime']:24s} {r['mean_erasures_tree']:7.1f} {r['energy_ratio_flat_over_tree']:7.3f} {r['mean_residual_bits_flat']:8.3f} {r['mean_residual_bits_tree']:8.3f}")
ratios = [r["energy_ratio_flat_over_tree"] for r in regimes]
print()
print(f"Erasure-ratio range across swept regimes: {min(ratios):.3f} - {max(ratios):.3f}")
print("Robustness reading: ratio always > 1 (tree always fewer erasures) =>", all(r>1 for r in ratios))
print("Residual reading: tree residual > flat residual in every non-trivial regime =>", all(r["mean_residual_bits_tree"]>r["mean_residual_bits_flat"] for r in regimes if r["regime"]!="zero-error"))
print("wrote h2_sweep_results.json")
json.dump({"seed": SEED, "trials_per_regime": 2000, "results": regimes}, open("h2_sweep_results.json","w"), indent=2)
