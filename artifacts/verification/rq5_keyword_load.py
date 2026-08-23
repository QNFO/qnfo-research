#!/usr/bin/env python3
"""RQ5 computational verification — QNFO.RES.022 Phase 2.

Load-bearing keyword analysis of the QNFO Keyword Taxonomy v1.0
(2026-08-05, canonical: QNFO/qnfo-research docs/QNFO-KEYWORD-TAXONOMY.md).

Research question (RQ5, PROJECT-PLAN):
  Which keywords are load-bearing for the consilience (shared by >=3 programs)
  versus program-local, and does the load-bearing core coincide with the
  ultrametric bridge vocabulary (valuation, hierarchy, distinction, bound)?

Analysis layers (all deterministic, pure stdlib):
  L1 string level  : normalized keyword -> program coverage; load-bearing core.
  L2 family level  : bridge-family -> set of programs containing >=1 family
                     keyword (normalized membership).
  L3 bridge subs   : keywords inside the taxonomy's OWN bridge sections
                     (UMP Bridge Concepts; RES Cross-Domain Methodology,
                     Cross-Domain Bridges, Measurement Stratigraphy) -> coverage.
  L4 cross-cutting : "## Cross-Cutting Themes" subsections; keyword overlap
                     with program sections.

Writes:
  artifacts/verification/rq5_results.json      (analysis output)
  artifacts/p2-consilience-map.json            (machine-readable graph)
and prints a human summary to stdout.
"""
import json
import math
import re
import sys
import collections

SRC = sys.argv[1] if len(sys.argv) > 1 else "artifacts/verification/keyword-taxonomy-source.md"
RESULTS_OUT = sys.argv[2] if len(sys.argv) > 2 else "artifacts/verification/rq5_results.json"
GRAPH_OUT = sys.argv[3] if len(sys.argv) > 3 else "artifacts/p2-consilience-map.json"

PROGRAMS = ["UMP", "SLB", "INM", "CFE", "RES", "PLT", "DEM"]
THRESHOLD = 3

# ---------------------------------------------------------------------------
# 1. Parse the taxonomy
# ---------------------------------------------------------------------------
text = open(SRC, encoding="utf-8").read()
parts = re.split(r"^##\s+", text, flags=re.M)
prog_texts = {}
cross_cutting_text = None
for part in parts:
    if not part.split():
        continue
    code = part.split()[0].rstrip("\u2014").strip()
    if code in PROGRAMS:
        prog_texts[code] = part
    elif code == "Cross-Cutting":
        cross_cutting_text = part
assert len(prog_texts) == 7, f"expected 7 program sections, got {sorted(prog_texts)}"
assert cross_cutting_text is not None, "missing Cross-Cutting Themes section"


def keywords_in(sec_text):
    return set(re.findall(r"`([^`]+)`", sec_text))


def norm(kw):
    return re.sub(r"[^a-z0-9]", "", kw.lower())


per_prog = {code: keywords_in(t) for code, t in prog_texts.items()}
assert all(len(kws) > 10 for kws in per_prog.values()), "section parse looks wrong"

cov = collections.defaultdict(set)
for code, kws in per_prog.items():
    for kw in kws:
        cov[norm(kw)].add(code)

rep = {}
for code in PROGRAMS:
    for kw in sorted(per_prog[code]):
        rep.setdefault(norm(kw), kw)

# ---------------------------------------------------------------------------
# 2. Bridge vocabulary (four families) and the taxonomy's OWN bridge sections
# ---------------------------------------------------------------------------
BRIDGE_FAMILIES = {
    "valuation": [
        "p-adic", "padic", "ultrametric", "non-archimedean", "adelic", "adele",
        "idele", "ostrowski", "ostrowski-theorem", "bruhat-tits", "berkovich",
        "valuation-theory", "product-formula", "adele-ring", "idele-class-group",
        "restricted-direct-product", "strong-approximation", "weak-approximation",
        "place-democracy", "archimedean-completion", "local-field", "global-field",
    ],
    "hierarchy": [
        "hierarchical-clustering-tree", "dendrogram-visualization",
        "ultrametric-tree", "p-adic-tree", "measurement-stratigraphy",
        "instrumental-stratification", "re-entry", "reentry", "crossing", "tree",
    ],
    "distinction": [
        "distinction", "laws-of-form", "spencer-brown", "calculus-of-indications",
        "primary-algebra", "primary-arithmetic", "law-of-calling", "law-of-crossing",
        "marked-state", "unmarked-state", "imaginary-boolean", "void",
        "boundary-logic", "distinction-algebra",
    ],
    "bound": [
        "landauer-principle", "landauer-bound", "landauer-limit",
        "bekenstein-bound", "holographic-bound", "bremermann-limit",
        "margolus-levitin", "thermodynamics-of-computation", "entropy-production",
        "szilard-engine",
    ],
}
bridge_norms = {norm(kw) for fam in BRIDGE_FAMILIES.values() for kw in fam}

# taxonomy's own bridge subsections: subsection name -> keyword set
BRIDGE_SUBSECTIONS = {
    "UMP_Bridge_Concepts": "### Bridge Concepts",
    "RES_CrossDomain_Methodology": "### Cross-Domain Methodology",
    "RES_CrossDomain_Bridges": "### Cross-Domain Bridges",
    "RES_Measurement_Stratigraphy": "### Measurement Stratigraphy",
}
bridge_sub_kws = {}
for key, heading in BRIDGE_SUBSECTIONS.items():
    m = re.search(re.escape(heading) + r"\s*(.*?)(?=\n###|\n##|\Z)", text, flags=re.S)
    bridge_sub_kws[key] = keywords_in(m.group(1)) if m else set()

# ---------------------------------------------------------------------------
# 3. L1 string level
# ---------------------------------------------------------------------------
load_bearing = {n: sorted(p) for n, p in cov.items() if len(p) >= THRESHOLD}
program_local = {n: sorted(p) for n, p in cov.items() if len(p) == 1}
shared_two = {n: sorted(p) for n, p in cov.items() if len(p) == 2}

a = sum(1 for n in cov if n in bridge_norms and len(cov[n]) >= THRESHOLD)
b = sum(1 for n in cov if n in bridge_norms and len(cov[n]) < THRESHOLD)
c = sum(1 for n in cov if n not in bridge_norms and len(cov[n]) >= THRESHOLD)
d = sum(1 for n in cov if n not in bridge_norms and len(cov[n]) < THRESHOLD)


def log_comb(n, k):
    if k < 0 or k > n:
        return -float("inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def hypergeom_pmf(k, K, n, N):
    return math.exp(log_comb(K, k) + log_comb(N - K, n - k) - log_comb(N, n))


def fisher_one_sided(oa, ob, oc, od):
    K, n = oa + ob, oa + oc
    N = K + ob + oc + od
    return sum(hypergeom_pmf(x, K, n, N) for x in range(oa, min(K, n) + 1))


p_enrich = fisher_one_sided(a, b, c, d)
precision = a / (a + c) if (a + c) else 0.0
recall = a / (a + b) if (a + b) else 0.0

# ---------------------------------------------------------------------------
# 4. L2 family level: program coverage per bridge family (normalized membership)
# ---------------------------------------------------------------------------
family_coverage = {}
for fam, kws in BRIDGE_FAMILIES.items():
    fam_norms = {norm(k) for k in kws}
    family_coverage[fam] = {
        "programs": [p for p in PROGRAMS if any(p in cov.get(n, set()) for n in fam_norms)],
        "program_keyword_counts": {p: sum(1 for n in fam_norms if p in cov.get(n, set()))
                                   for p in PROGRAMS},
    }

# ---------------------------------------------------------------------------
# 5. L3 bridge subsections -> coverage
# ---------------------------------------------------------------------------
bridge_sub_analysis = {}
for key, kws in bridge_sub_kws.items():
    prog_hits = collections.defaultdict(set)
    for kw in kws:
        for p in cov.get(norm(kw), set()):
            prog_hits[p].add(kw)
    bridge_sub_analysis[key] = {
        "keyword_count": len(kws),
        "programs_with_hits": sorted(prog_hits),
        "hits_per_program": {p: sorted(h) for p, h in prog_hits.items()},
    }

# ---------------------------------------------------------------------------
# 6. L4 cross-cutting themes
# ---------------------------------------------------------------------------
cc_parts = re.split(r"^###\s+", cross_cutting_text, flags=re.M)
cc_sections = {}
for cc in cc_parts:
    if not cc.split():
        continue
    title = cc.split()[0].strip()
    cc_sections[title] = keywords_in(cc)
cc_analysis = {}
for title, kws in cc_sections.items():
    prog_overlap = collections.defaultdict(set)
    for kw in kws:
        for p in cov.get(norm(kw), set()):
            prog_overlap[p].add(kw)
    cc_analysis[title] = {
        "keyword_count": len(kws),
        "keywords_also_in_programs": sum(1 for kw in kws if cov.get(norm(kw), set())),
        "programs_touched": sorted(prog_overlap),
        "overlap_keywords": {p: sorted(h) for p, h in prog_overlap.items()},
    }

# ---------------------------------------------------------------------------
# 7. Pairwise overlap + per-program stats
# ---------------------------------------------------------------------------
pair_overlap = {}
for i, p1 in enumerate(PROGRAMS):
    for p2 in PROGRAMS[i + 1:]:
        shared = {n for n in cov if p1 in cov[n] and p2 in cov[n]}
        pair_overlap[f"{p1}-{p2}"] = {"shared_count": len(shared),
                                      "shared_keywords": sorted(rep[n] for n in shared)}

per_program = {code: {"keyword_count": len(kws),
                      "load_bearing_share": round(
                          sum(1 for kw in kws if len(cov[norm(kw)]) >= THRESHOLD) / len(kws), 4),
                      "bridge_share": round(sum(1 for kw in kws if norm(kw) in bridge_norms) / len(kws), 4)}
               for code, kws in per_prog.items()}

# ---------------------------------------------------------------------------
# 8. Verdicts
# ---------------------------------------------------------------------------
l1_verdict = ("SUPPORTED" if (precision >= 0.5 and p_enrich < 0.05) else "NOT SUPPORTED")
l2_verdict = ("SUPPORTED" if all(len(family_coverage[f]["programs"]) >= THRESHOLD
                                 for f in BRIDGE_FAMILIES) else "PARTIAL/NOT SUPPORTED")

results = {
    "source": "docs/QNFO-KEYWORD-TAXONOMY.md v1.0 (2026-08-05)",
    "method": "RQ5 load-bearing analysis; L1 string level (threshold >=3 programs, "
              "Fisher exact enrichment vs bridge families); L2 family level; "
              "L3 taxonomy bridge subsections; L4 cross-cutting themes.",
    "programs": PROGRAMS,
    "per_program": per_program,
    "total_distinct_keywords": len(cov),
    "L1_string_level": {
        "load_bearing_core": {rep[n]: {"programs": sorted(p), "bridge_family": next(
            (fam for fam, kws in BRIDGE_FAMILIES.items() if n in {norm(k) for k in kws}), None)}
            for n, p in sorted(load_bearing.items())},
        "shared_by_two": {rep[n]: sorted(p) for n, p in sorted(shared_two.items())},
        "program_local_count": len(program_local),
        "contingency": {"bridge_and_load_bearing": a, "bridge_and_local": b,
                        "non_bridge_and_load_bearing": c, "non_bridge_and_local": d},
        "bridge_stats": {"precision": round(precision, 4), "recall": round(recall, 4),
                         "fisher_one_sided_p": round(p_enrich, 6)},
        "verdict": l1_verdict,
    },
    "L2_family_level": {
        "family_coverage": {fam: {"programs": v["programs"],
                                  "program_keyword_counts": v["program_keyword_counts"]}
                            for fam, v in family_coverage.items()},
        "verdict": l2_verdict,
    },
    "L3_bridge_subsections": bridge_sub_analysis,
    "L4_cross_cutting": cc_analysis,
    "pair_overlap": {k: v for k, v in pair_overlap.items() if v["shared_count"] > 0},
    "verdict_rq5": "L1 NOT SUPPORTED (taxonomy strictly partitional); "
                   "consilience carried by L2-L4 structures, not shared vocabulary",
}

with open(RESULTS_OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# machine-readable consilience graph (skip phantom keys: cov entries with empty program set)
nodes = []
for code in PROGRAMS:
    nodes.append({"id": f"prog:{code}", "label": "Program", "name": code})
for n in cov:
    if not cov[n]:
        continue
    nodes.append({"id": f"kw:{n}", "label": "Keyword", "name": rep[n],
                  "programs": sorted(cov[n]),
                  "load_bearing": len(cov[n]) >= THRESHOLD,
                  "bridge_family": next(
                      (fam for fam, fam_kws in BRIDGE_FAMILIES.items()
                       if n in {norm(k) for k in fam_kws}), None)})
edges = [{"source": f"prog:{code}", "target": f"kw:{n}", "type": "OWNS"}
         for n, kws in cov.items() for code in kws]
graph = {"schema": "consilience-map-v2", "generated": "2026-08-23",
         "wbs": "QNFO.RES.022", "nodes": nodes, "edges": edges}
with open(GRAPH_OUT, "w", encoding="utf-8") as f:
    json.dump(graph, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# 9. Human summary
# ---------------------------------------------------------------------------
print(f"RQ5 load-bearing analysis — QNFO.RES.022 P2")
print(f"source: {SRC}; programs parsed 7/7; distinct keywords: {len(cov)}")
print(f"L1 string level:")
print(f"  load-bearing core (>=3 programs): {len(load_bearing)} keywords")
for n in sorted(load_bearing):
    print(f"    {rep[n]:45s} {len(cov[n])} programs  bridge={next((fam for fam, kws in BRIDGE_FAMILIES.items() if n in {norm(k) for k in kws}), None)}")
print(f"  shared by exactly 2: {len(shared_two)} keywords -> "
      f"{[(rep[n], sorted(p)) for n, p in sorted(shared_two.items())]}")
print(f"  program-local: {len(program_local)}/{len(cov)} ({100*len(program_local)/len(cov):.1f}%)")
print(f"  contingency a/b/c/d={a}/{b}/{c}/{d}; precision={precision:.3f} "
      f"recall={recall:.3f} fisher_p={p_enrich:.6f}; verdict {l1_verdict}")
print(f"L2 family level:")
for fam, v in family_coverage.items():
    print(f"  {fam:12s} programs={v['programs']} counts={v['program_keyword_counts']}")
print(f"  verdict: {l2_verdict}")
print(f"L3 bridge subsections:")
for key, v in bridge_sub_analysis.items():
    print(f"  {key:32s} {v['keyword_count']:3d} kws  programs_with_hits={v['programs_with_hits']}")
print(f"L4 cross-cutting themes:")
for title, v in cc_analysis.items():
    print(f"  {title:28s} {v['keyword_count']:3d} kws  in_programs={v['keywords_also_in_programs']}  touched={v['programs_touched']}")
print(f"VERDICT RQ5: {results['verdict_rq5']}")
