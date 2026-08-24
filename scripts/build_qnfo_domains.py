#!/usr/bin/env python3
"""build_qnfo_domains.py — parse the canonical QNFO keyword taxonomy into
domains JSON.

Source: docs/keyword-taxonomy-source.md (flat rendering of
docs/QNFO-KEYWORD-TAXONOMY.md v1.0; the same file deposited with
10.5281/zenodo.22071421 and 10.5281/zenodo.22073477).

Method: identical to the published rq5_keyword_load.py:
  - split on '^## ' section headers (re.M); program code = first token of the
    section body before the em dash
  - keywords = backticked strings in the section
  - normalize: re.sub(r"[^a-z0-9]", "", kw.lower())   ('p-adic' == 'padic')

Also emits the published four bridge families (valuation / hierarchy /
distinction / bound) as 'bridge_families' and the general-family list used
for the spinoff Fisher enrichment test.

Output: {"domains": {CODE: [normalized...]}, "bridge_families": {...},
         "general_families": [...]}
"""
import json
import re
import sys
from pathlib import Path

SRC = Path("docs/keyword-taxonomy-source.md")
OUT = Path("artifacts/external-search/qnfo_domains.json")

PROGRAMS = ["UMP", "SLB", "INM", "CFE", "RES", "PLT", "DEM"]

# Published four bridge families (rq5_keyword_load.py, 10.5281/zenodo.22071421)
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

GENERAL_FAMILIES = [
    # structurally general concept families (cross-domain candidates)
    "consilience", "interdisciplinarity", "transdisciplinarity",
    "knowledge-graph", "ontology", "taxonomy", "classification",
    "isomorphism", "homomorphism", "category-theory", "compositionality",
    "emergence", "hierarchy-theory", "nested-structure", "scale-invariance",
    "self-similarity", "renormalization", "coarse-graining", "effective-theory",
    "phase-transition", "symmetry-breaking", "measurement-theory",
    "epistemology", "observer-dependence", "bayesian-updating",
    "path-dependence", "network-effects", "system-dynamics",
    "agent-based-model", "structural-realism", "relational-ontology",
    "quantum-computing", "quantum-algorithm", "quantum-error-correction",
    "quantum-machine-learning", "llm", "transformer", "embedding-model",
    "semantic-search", "vector-database", "data-pipeline", "observability",
    "rest-api", "python-sdk", "interactive-visualization",
    "data-visualization", "test-automation", "accessibility",
]


def keywords_in(sec_text: str) -> set[str]:
    return set(re.findall(r"`([^`]+)`", sec_text))


def norm(kw: str) -> str:
    return re.sub(r"[^a-z0-9]", "", kw.lower())


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+", text, flags=re.M)
    prog_texts = {}
    for part in parts:
        if not part.split():
            continue
        code = part.split()[0].rstrip("\u2014").strip()
        if code in PROGRAMS:
            prog_texts[code] = part
    assert len(prog_texts) == 7, f"expected 7 program sections, got {sorted(prog_texts)}"

    domains = {}
    for code, t in prog_texts.items():
        domains[code] = sorted({norm(k) for k in keywords_in(t)})

    data = {
        "domains": domains,
        "bridge_families": {k: [norm(x) for x in v] for k, v in BRIDGE_FAMILIES.items()},
        "general_families": [norm(x) for x in GENERAL_FAMILIES],
        "parser": "build_qnfo_domains.py (method = rq5_keyword_load.py; source = "
                  "docs/keyword-taxonomy-source.md)",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1), encoding="utf-8")

    total = sum(len(v) for v in domains.values())
    print(f"programs: {list(domains.keys())}")
    print(f"raw keyword occurrences: {total}")
    for code, kws in domains.items():
        print(f"  {code}: {len(kws)}")
    print(f"WROTE: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
