#!/usr/bin/env python3
"""RQ1/RQ2 computational verification - QNFO.RES.022 Phase 4 (fixed v2).

Tests H1's retrieval claim on two pinned corpora:
  Corpus A: seeded synthetic sparse docs with planted cluster structure.
  Corpus B: QNFO paper titles (pinned from living-paper D1, 2026-08-23).

Comparators (deterministic, fixed seed):
  cosine       : cosine over char-3-gram TF-IDF vectors (flat baseline)
  ultrametric  : DATA-DERIVED ultrametric index - single-linkage dendrogram
                 over cosine distances; cophenetic (ultrametric) distances
                 rank candidates (Murtagh-aligned recoding: the real H1 index)
  padic_hash   : encoding CONTROL - sha256 -> integer; similarity = p-adic
                 valuation depth of the hash difference (UIA Q2: the raw hash
                 is a convention, not physics; it is expected to destroy
                 metric structure and is NOT the H1 index)

Metrics: precision@5, precision@10, MRR over a seeded query sample.
Ground truth: Corpus A = planted cluster label; Corpus B = program label
derived from taxonomy keyword -> program map (majority vote over matched
keywords in title text).
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
OUT = sys.argv[3] if len(sys.argv) > 3 else "artifacts/verification/rq1_results.json"

# ---------------------------------------------------------------- corpus A
def make_corpus_a(seed):
    rng = random.Random(seed)
    n_clusters, per_cluster, vocab = 5, 40, 512
    cluster_tokens = []
    for c in range(n_clusters):
        toks = rng.sample(range(vocab), 24)
        cluster_tokens.append(set(toks))
    docs, labels = [], []
    for c in range(n_clusters):
        for _ in range(per_cluster):
            toks = set(cluster_tokens[c])
            for _ in range(6):
                toks.add(rng.randrange(vocab))          # noise tokens
            docs.append(" ".join(f"t{t}" for t in toks))
            labels.append(c)
    return docs, labels

corpus_a_docs, corpus_a_labels = make_corpus_a(SEED)

# ---------------------------------------------------------------- corpus B
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

corpus_b_labels = [program_label(t) for t in corpus_b_docs]
keep = [(t, l) for t, l in zip(corpus_b_docs, corpus_b_labels) if l is not None]
corpus_b_docs = [t for t, _ in keep]
corpus_b_labels = [l for _, l in keep]

# ---------------------------------------------------------------- features
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

# --------------------------------------------------- ultrametric index (v2)
def single_linkage_ultrametric(sim_fn, n):
    """Data-derived ultrametric distances via single-linkage dendrogram.

    Builds the cophenetic matrix: d(i,j) = the merge level at which i and j
    first join in single-linkage agglomeration. Ultrametric by construction.
    """
    # distance matrix from similarity
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            s = sim_fn(i, j)
            D[i][j] = D[j][i] = 1.0 - s if s < 1.0 else 0.0
    # edges ascending
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((D[i][j], i, j))
    edges.sort()
    parent = list(range(n))
    size = [1] * n
    merge_level = [0.0] * (2 * n)   # node -> level at which it was created
    dend_parent = [-1] * (2 * n)    # dendrogram tree parent
    next_node = n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for w, i, j in edges:
        ri, rj = find(i), find(j)
        if ri == rj:
            continue
        node = next_node
        next_node += 1
        parent[ri] = node
        parent[rj] = node
        parent.append(node)
        size.append(size[ri] + size[rj])
        merge_level[node] = w
        dend_parent[ri] = node
        dend_parent[rj] = node
    root = next_node - 1
    # cophenetic distance: merge level of LCA in dendrogram tree
    depth = [0] * (2 * n)
    order = [root]
    for x in order:
        for c in (i for i in range(next_node) if dend_parent[i] == x):
            depth[c] = depth[x] + 1
            order.append(c)
    up = dend_parent[:next_node]
    def lca_level(a, b):
        da, db = depth[a], depth[b]
        while da > db:
            a = up[a]; da -= 1
        while db > da:
            b = up[b]; db -= 1
        while a != b:
            a = up[a]; b = up[b]
        return merge_level[a]
    coph = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            coph[i][j] = coph[j][i] = lca_level(i, j)
    return coph

# ---------------------------------------------------------------- metrics
def evaluate(docs, labels, rank_fn, n_queries=60, ks=(5, 10)):
    rng = random.Random(SEED + 1)
    idx = list(range(len(docs)))
    rng.shuffle(idx)
    queries = idx[:n_queries]
    p5, p10, mrr = [], [], []
    for q in queries:
        rel = {i for i in idx if labels[i] == labels[q] and i != q}
        if not rel:
            continue
        ranked = rank_fn(q)[:max(ks)]
        rset = set(ranked)
        p5.append(len(rset & rel & set(ranked[:5])) / min(5, len(rel)))
        p10.append(len(rset & rel & set(ranked[:10])) / min(10, len(rel)))
        for rank, i in enumerate(ranked[:10], 1):
            if i in rel:
                mrr.append(1.0 / rank)
                break
        else:
            mrr.append(0.0)
    return {"p@5": round(sum(p5) / len(p5), 4),
            "p@10": round(sum(p10) / len(p10), 4),
            "mrr": round(sum(mrr) / len(mrr), 4)}

def padic_sim(a, b, p=2):
    x = int(hashlib.sha256(a.encode("utf-8")).hexdigest(), 16)
    y = int(hashlib.sha256(b.encode("utf-8")).hexdigest(), 16)
    d = abs(x - y)
    v = 0
    while d % p == 0 and d > 0:
        d //= p
        v += 1
    return v

# ---------------------------------------------------------------- run
results = {"seed": SEED, "method": "RQ1/RQ2 retrieval benchmark (v2: "
           "data-derived single-linkage ultrametric index + hash encoding control)",
           "corpus_a": {"docs": len(corpus_a_docs), "clusters": 5, "sparse_dim": 512},
           "corpus_b": {"docs": len(corpus_b_docs),
                        "labeled_programs": sorted(set(corpus_b_labels)),
                        "source": "living-paper papers (400 pinned, 2026-08-23)"}}

for cname, docs, labels in (("A", corpus_a_docs, corpus_a_labels),
                            ("B", corpus_b_docs, corpus_b_labels)):
    vecs = build_tfidf(docs) if docs else []
    n = len(docs)
    def cos_sim(q, i, vecs=vecs):
        return cosine(vecs[q], vecs[i])
    coph = single_linkage_ultrametric(cos_sim, n) if n else []
    def ult_rank(q, coph=coph, n=n):
        return sorted((i for i in range(n) if i != q),
                      key=lambda i: coph[q][i])
    def cos_rank(q, vecs=vecs, n=n):
        return sorted((i for i in range(n) if i != q),
                      key=lambda i: cos_sim(q, i), reverse=True)
    def pad_rank(q, docs=docs, n=n):
        return sorted((i for i in range(n) if i != q),
                      key=lambda i: padic_sim(docs[q], docs[i]), reverse=True)
    results[f"corpus_{cname}_results"] = {
        "cosine_tfidf": evaluate(docs, labels, cos_rank),
        "ultrametric_singlelink": evaluate(docs, labels, ult_rank),
        "padic_hash_control": evaluate(docs, labels, pad_rank),
    }

rA = results["corpus_A_results"]
rB = results["corpus_B_results"]
verdict = []
for name, r in (("A", rA), ("B", rB)):
    cos, ult = r["cosine_tfidf"], r["ultrametric_singlelink"]
    delta = ult["p@10"] - cos["p@10"]
    verdict.append({"corpus": name, "delta_p10_ultrametric_minus_cosine": delta,
                    "ultrametric_matches_or_beats": delta >= -0.02})
results["verdict_h1"] = {
    "note": "H1 index = data-derived single-linkage ultrametric (Murtagh-aligned "
            "recoding). Naive sha256 p-adic hash is the encoding control: hashes "
            "destroy metric structure by construction (UIA Q2), so it is expected "
            "to underperform and is not the H1 claim.",
    "per_corpus": verdict,
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"RQ1/RQ2 verification v2 - seed {SEED}")
print(f"Corpus A: {results['corpus_a']['docs']} docs, 5 planted clusters")
print(f"Corpus B: {results['corpus_b']['docs']} labeled titles, "
      f"programs {results['corpus_b']['labeled_programs']}")
for cname in ("A", "B"):
    r = results[f"corpus_{cname}_results"]
    print(f"Corpus {cname}:")
    for name in ("cosine_tfidf", "ultrametric_singlelink", "padic_hash_control"):
        m = r[name]
        print(f"  {name:24s} p@5={m['p@5']:.4f} p@10={m['p@10']:.4f} mrr={m['mrr']:.4f}")
print("H1 verdict:", json.dumps(results["verdict_h1"]))
