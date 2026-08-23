#!/usr/bin/env python3
"""RQ2 computational verification - QNFO.RES.022 Phase 5.1 (red-team HARD-2 fix).

Implements the RQ2 test that was missing from Phase 4:
  "Do cross-domain consilience links share p-adic prefixes (valuation depth)
   more often than they share cosine similarity above threshold?"

Protocol (deterministic, seed 20260823):
  For each corpus (A: 200 synthetic docs with planted cluster labels; B: 69
  QNFO titles with program labels), take ALL document pairs and rank them by:
    (a) p-adic valuation depth  v_2(|sha256(i) - sha256(j)|)   [raw-hash prefix]
    (b) cosine TF-IDF similarity                                [flat baseline]
  Then compare same-label rates (consilience-link precision) at matched
  selection counts:
    - top-N pairs by each criterion (N = 50 / 100 / 200)
    - matched-rate: for cosine thresholds theta, take the same number of
      top pairs by p-adic depth and compare same-label rates.

Interpretation: RQ2 is answered by whether p-adic prefix depth identifies
same-program pairs at least as well as cosine at equal selection counts.
Per UIA Q2 the raw sha256 hash is a convention, not physics: the naive
encoding is expected to destroy metric structure. The data-derived
ultrametric recoding is H1's index (rq1); RQ2 tests the *prefix-depth*
encoding directly.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict

SEED = 20260823
random.seed(SEED)

TAXONOMY = sys.argv[1] if len(sys.argv) > 1 else "artifacts/verification/keyword-taxonomy-source.md"
CORPUS_B = sys.argv[2] if len(sys.argv) > 2 else "artifacts/verification/corpus_qnfo_titles.json"
OUT = sys.argv[3] if len(sys.argv) > 3 else "artifacts/verification/rq2_results.json"


def v_p(n, p):
    n = abs(int(n))
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def padic_depth(a, b, p=2):
    """Shared-prefix depth of two documents' sha256 hashes (p-adic valuation)."""
    ha = int(hashlib.sha256(a.encode("utf-8")).hexdigest(), 16)
    hb = int(hashlib.sha256(b.encode("utf-8")).hexdigest(), 16)
    return v_p(ha - hb, p)


def char_ngrams(text, n=3):
    s = re.sub(r"\s+", "", text.lower())
    return [s[i:i+n] for i in range(max(1, len(s) - n + 1))]


def build_tfidf(docs):
    df = Counter()
    feats = []
    for d in docs:
        c = Counter(char_ngrams(d))
        feats.append(c)
        df.update(c.keys())
    n = len(docs)
    idf = {k: math.log((1 + n) / (1 + v)) + 1 for k, v in df.items()}
    vecs = []
    for c in feats:
        norm = math.sqrt(sum((v * idf[k]) ** 2 for k, v in c.items())) or 1.0
        vecs.append({k: v * idf[k] / norm for k, v in c.items()})
    return vecs


def cosine(a, b):
    if not a or not b:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum(v * b.get(k, 0.0) for k, v in a.items())


# ---- corpus A (synthetic, planted clusters) ----
def make_corpus_a(seed):
    rng = random.Random(seed)
    n_clusters, per_cluster, vocab = 5, 40, 512
    cluster_tokens = []
    for c in range(n_clusters):
        cluster_tokens.append(set(rng.sample(range(vocab), 24)))
    docs, labels = [], []
    for c in range(n_clusters):
        for _ in range(per_cluster):
            toks = set(cluster_tokens[c])
            for _ in range(6):
                toks.add(rng.randrange(vocab))
            docs.append(" ".join(f"t{t}" for t in toks))
            labels.append(c)
    return docs, labels


corpus_a_docs, corpus_a_labels = make_corpus_a(SEED)

# ---- corpus B (QNFO titles, program labels via taxonomy keywords) ----
with open(CORPUS_B, encoding="utf-8") as f:
    qnfo_rows = json.load(f)
corpus_b_docs = [r["title"] for r in qnfo_rows if r.get("title")]

prog_kw = defaultdict(list)
for m in re.finditer(r"^##\s+([A-Z]{3})\b(.*?)(?=^##\s|\Z)",
                     open(TAXONOMY, encoding="utf-8").read(), re.M | re.S):
    code, body = m.group(1), m.group(2)
    if code in ("UMP", "SLB", "INM", "CFE", "RES", "PLT", "DEM"):
        prog_kw[code] = [re.sub(r"[^a-z0-9]", "", k.lower())
                         for k in re.findall(r"`([^`]+)`", body)]


def program_label(title):
    toks = re.sub(r"[^a-z0-9 ]", " ", title.lower()).split()
    votes = Counter()
    for t in toks:
        for prog, kws in prog_kw.items():
            if t in kws:
                votes[prog] += 1
    if not votes:
        return None
    return votes.most_common(1)[0][0]


keep = [(t, l) for t, l in zip(corpus_b_docs, [program_label(t) for t in corpus_b_docs])
        if l is not None]
corpus_b_docs = [t for t, _ in keep]
corpus_b_labels = [l for _, l in keep]


def pair_analysis(docs, labels):
    n = len(docs)
    vecs = build_tfidf(docs)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            same = 1.0 if labels[i] == labels[j] else 0.0
            pairs.append((i, j, same,
                          padic_depth(docs[i], docs[j], 2),
                          cosine(vecs[i], vecs[j])))
    return pairs


def matched_topn(pairs, n_sel):
    by_depth = sorted(pairs, key=lambda p: p[3], reverse=True)[:n_sel]
    by_cos = sorted(pairs, key=lambda p: p[4], reverse=True)[:n_sel]
    return {"topN": n_sel,
            "same_rate_padic_depth": round(sum(p[2] for p in by_depth) / n_sel, 4),
            "same_rate_cosine": round(sum(p[2] for p in by_cos) / n_sel, 4)}


def matched_threshold(pairs, theta):
    sel_cos = [p for p in pairs if p[4] >= theta]
    if not sel_cos:
        return None
    n_sel = len(sel_cos)
    by_depth = sorted(pairs, key=lambda p: p[3], reverse=True)[:n_sel]
    return {"cosine_threshold": theta, "n_pairs": n_sel,
            "same_rate_padic_depth": round(sum(p[2] for p in by_depth) / n_sel, 4),
            "same_rate_cosine": round(sum(p[2] for p in sel_cos) / n_sel, 4)}


results = {"seed": SEED,
           "method": "RQ2 consilience-link test: pairwise ranking by p-adic "
                     "prefix depth (v_2 of sha256 hash difference) vs cosine "
                     "TF-IDF; same-label rate at matched selection counts",
           "corpus_a": {"docs": len(corpus_a_docs), "pairs": len(corpus_a_docs) * (len(corpus_a_docs) - 1) // 2},
           "corpus_b": {"docs": len(corpus_b_docs), "pairs": len(corpus_b_docs) * (len(corpus_b_docs) - 1) // 2}}

pairs_a = pair_analysis(corpus_a_docs, corpus_a_labels)
pairs_b = pair_analysis(corpus_b_docs, corpus_b_labels)

results["corpus_A_topN"] = [matched_topn(pairs_a, N) for N in (50, 100, 200)]
results["corpus_B_topN"] = [matched_topn(pairs_b, N) for N in (50, 100, 200)]
results["corpus_A_thresholds"] = [x for t in (0.3, 0.5, 0.7)
                                  if (x := matched_threshold(pairs_a, t)) is not None]
results["corpus_B_thresholds"] = [x for t in (0.3, 0.5, 0.7)
                                  if (x := matched_threshold(pairs_b, t)) is not None]


def verdict_row(rows):
    # RQ2 answered: does p-adic depth identify consilience links >= cosine at
    # matched counts? (per-row pass = same_rate_padic >= same_rate_cosine)
    passes = [r["same_rate_padic_depth"] >= r["same_rate_cosine"] for r in rows]
    return {"rows": len(rows), "passes": sum(passes),
            "padic_never_beats_cosine": sum(passes) == 0,
            "verdict": "NOT SUPPORTED (raw-hash p-adic prefixes do not identify "
                       "consilience links better than cosine; encoding-dependent "
                       "per UIA Q2)" if sum(passes) == 0 else
                       ("PARTIAL" if sum(passes) < len(rows) else "SUPPORTED")}


results["verdict_rq2_A"] = verdict_row(results["corpus_A_topN"])
results["verdict_rq2_B"] = verdict_row(results["corpus_B_topN"])

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"RQ2 consilience-link verification - seed {SEED}")
print(f"Corpus A: {results['corpus_a']['docs']} docs, {results['corpus_a']['pairs']} pairs")
print(f"Corpus B: {results['corpus_b']['docs']} docs, {results['corpus_b']['pairs']} pairs")
for cname in ("A", "B"):
    print(f"Corpus {cname} top-N same-label rates (padic_depth vs cosine):")
    for r in results[f"corpus_{cname}_topN"]:
        print(f"  N={r['topN']:<4d} padic={r['same_rate_padic_depth']:.4f} "
              f"cosine={r['same_rate_cosine']:.4f}")
    for r in results[f"corpus_{cname}_thresholds"]:
        print(f"  theta={r['cosine_threshold']} n={r['n_pairs']:<4d} "
              f"padic={r['same_rate_padic_depth']:.4f} "
              f"cosine={r['same_rate_cosine']:.4f}")
    print(f"  verdict: {results[f'verdict_rq2_{cname}']['verdict']}")
