#!/usr/bin/env python3
"""terminology_silos.py — measurement toolkit for terminology-silo analysis.

Quantities (generalized from RQ5 of the QNFO keyword-taxonomy audit,
10.5281/zenodo.22071421):

  partitionality_index : fraction of keywords occurring in exactly one domain
  shared_core_size     : keywords occurring in >= 3 domains
  bridge_share         : fraction of keywords occurring in >= 2 domains
  per_domain stats     : keyword count, local share, bridge share
  fisher_enrichment    : one-sided Fisher exact test on the
                         bridge x general-family contingency
                         (H0: bridge membership independent of family
                         generality; alternative: bridges enriched in
                         general families)

Input: JSON {"domains": {name: [keywords...]}, "general_families": [kw...]}
Seed fix: the analysis is deterministic (no randomness); any sampling
consumers use random.Random(seed). Every printed number is reproducible.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path


# --------------------------------------------------------------------------
# Fisher exact test (one-sided, enrichment direction), exact integer method
# --------------------------------------------------------------------------

def _log_factorial(n: int) -> float:
    return math.lgamma(n + 1)


def _hypergeom_pmf(a: int, b: int, c: int, d: int) -> float:
    """P(A=a | margins) for the 2x2 table [[a, b], [c, d]]."""
    n = a + b + c + d
    r1 = a + b
    c1 = a + c
    return math.exp(
        _log_factorial(r1) + _log_factorial(n - r1)
        + _log_factorial(c1) + _log_factorial(n - c1)
        - _log_factorial(n)
        - _log_factorial(a) - _log_factorial(b)
        - _log_factorial(c) - _log_factorial(d)
    )


def fisher_one_sided(table: list[list[int]]) -> dict:
    """One-sided (greater) Fisher exact test.

    table = [[bridge_general, bridge_local], [local_general, local_local]].
    Returns dict with p_one_sided_greater, odds_ratio, table, alternative.
    """
    a, b = table[0]
    c, d = table[1]
    n = a + b + c + d
    r1 = a + b
    c1 = a + c
    hi = min(r1, c1)
    p_greater = 0.0
    for x in range(a, hi + 1):
        y = r1 - x
        z = c1 - x
        w = n - r1 - c1 + x
        p_greater += _hypergeom_pmf(x, y, z, w)
    odds_ratio = (a * d) / (b * c) if (b * c) else float("inf")
    return {
        "p_one_sided_greater": p_greater,
        "odds_ratio": odds_ratio,
        "table": table,
        "alternative": "greater",
    }


# --------------------------------------------------------------------------
# Silo measurement
# --------------------------------------------------------------------------

def measure(domains: dict[str, list[str]],
            general_families: set[str] | None = None,
            shared_threshold: int = 3) -> dict:
    """Compute all silo quantities for a domain->keywords partition."""
    # keyword -> set of domains containing it
    kw_domains: dict[str, set[str]] = defaultdict(set)
    for dom, kws in domains.items():
        for kw in kws:
            kw_domains[kw].add(dom)

    total = len(kw_domains)
    local = {kw for kw, ds in kw_domains.items() if len(ds) == 1}
    bridge = {kw for kw, ds in kw_domains.items() if len(ds) >= 2}
    core = {kw for kw, ds in kw_domains.items() if len(ds) >= shared_threshold}

    per_domain = {}
    for dom, kws in domains.items():
        dset = set(kws)
        n_local = sum(1 for kw in dset if kw in local)
        n_bridge = sum(1 for kw in dset if kw in bridge)
        per_domain[dom] = {
            "keyword_count": len(dset),
            "local_share": n_local / len(dset) if dset else 0.0,
            "bridge_share": n_bridge / len(dset) if dset else 0.0,
        }

    result = {
        "total_distinct_keywords": total,
        "partitionality_index": len(local) / total if total else 0.0,
        "local_keyword_count": len(local),
        "bridge_keyword_count": len(bridge),
        "bridge_share": len(bridge) / total if total else 0.0,
        "shared_core_size": len(core),
        "shared_core_keywords": sorted(core),
        "shared_by_two": sorted(
            kw for kw, ds in kw_domains.items() if len(ds) == 2),
        "per_domain": per_domain,
    }

    # Fisher enrichment: bridge x general-family contingency
    if general_families is not None:
        gf = set(general_families)
        all_kws = set(kw_domains.keys())
        a = len(bridge & gf)                 # bridge and general
        b = len(bridge - gf)                 # bridge and domain-specific
        c = len((all_kws - bridge) & gf)     # non-bridge and general
        d = len(all_kws - bridge - gf)       # non-bridge and domain-specific
        fe = fisher_one_sided([[a, b], [c, d]])
        result["fisher_enrichment"] = {
            **fe,
            "bridge_and_general": a,
            "bridge_and_nongeneral": b,
            "nonbridge_and_general": c,
            "nonbridge_and_nongeneral": d,
        }

    return result


# --------------------------------------------------------------------------
# Seed corpus: QNFO taxonomy (docs/QNFO-KEYWORD-TAXONOMY.md v1.0, 335 kws)
# --------------------------------------------------------------------------

QNFO_TAXONOMY: dict[str, list[str]] = {
    "UMP": [
        "ultrametric", "p-adic", "padic", "adelic", "adele", "idele",
        "ostrowski", "bruhat-tits", "non-archimedean", "berkovich",
        "perfectoid", "rigid-geometry", "tate-algebra", "formal-group",
        "lubin-tate", "p-divisible", "dieudonne", "crystalline-cohomology",
        "etale-cohomology", "galois-representation", "local-field",
        "global-field", "class-field-theory", "adeles", "ideles",
        "valuation-theory", "valued-field", "arithmetic-dynamics",
        "p-adic-dynamics", "non-archimedean-dynamics", "berkovich-dynamics",
        "p-adic-hodge", "fontaine", "de-rham", "crystalline", "semistable",
        "breuil-kisin", "langlands-program", "automorphic-form",
        "shimura-variety", "modular-form", "elliptic-curve", "l-function",
        "selberg-trace", "adelic-physics", "ultrametric-physics",
        "non-archimedean-physics", "p-adic-quantum", "archimedean-completion",
        "place-democracy", "sagemath", "padic-sage", "sage-padic",
        "magma-padic", "pari-gp", "padic-calculator", "ostrowski-theorem",
        "product-formula", "adele-ring", "idele-class-group",
        "restricted-direct-product", "strong-approximation",
        "weak-approximation",
    ],
    "SLB": [
        "laws-of-form", "spencer-brown", "calculus-of-indications",
        "primary-algebra", "primary-arithmetic", "law-of-calling",
        "law-of-crossing", "distinction", "marked-state", "unmarked-state",
        "re-entry", "reentry", "imaginary-boolean", "crossing", "void",
        "boundary-logic", "boundary-math", "distinction-algebra",
        "waveform-algebra", "temporal-logic-lof", "self-reference-logic",
        "indication", "form-of-distinction", "observer-theory",
        "second-order-cybernetics", "maturana-varela", "autopoiesis",
        "lof-circuit", "imaginary-boolean-circuit", "distinction-computation",
        "spencer-brown-computer",
    ],
    "INM": [
        "information-physics", "physical-information",
        "information-fundamental", "it-from-bit", "bit-from-it",
        "informational-universe", "landauer-principle", "landauer-bound",
        "landauer-limit", "bekenstein-bound", "holographic-bound",
        "bremermann-limit", "margolus-levitin", "shannon-entropy",
        "kolmogorov-complexity", "algorithmic-information-theory",
        "solomonoff-induction", "minimum-description-length",
        "chaitin-constant", "thermodynamics-of-computation", "maxwell-demon",
        "szilard-engine", "reversible-computing", "entropy-production",
        "information-geometry", "fisher-information", "amari-metric",
        "statistical-manifold", "natural-gradient", "information-metric",
        "free-energy-principle", "bayesian-brain", "predictive-coding",
        "active-inference",
    ],
    "CFE": [
        "paradigm-engineering", "technology-forecasting", "s-curve",
        "innovation-diffusion", "disruptive-technology", "gartner-hype-cycle",
        "scenario-planning", "futures-studies", "long-range-forecasting",
        "technology-roadmap", "exponential-technology", "moore-law",
        "wright-law", "godwin-law", "cascading-foresight", "anticipatory-ethics",
        "precautionary-principle", "speculative-design", "design-fiction",
        "foresight-method", "horizon-scanning", "weak-signal",
        "emerging-technology", "strategic-foresight", "sensemaking",
        "cognitive-bias", "heuristics", "prediction-market",
        "forecast-aggregation", "superforecasting",
        "reference-class-forecasting", "probability-calibration",
        "bayesian-updating", "information-cascade", "complexity-economics",
        "agent-based-model", "system-dynamics", "network-effects",
        "path-dependence", "lock-in", "technological-convergence",
        "convergence-thesis", "general-purpose-technology",
        "platform-economics", "two-sided-market", "inflection-point",
    ],
    "RES": [
        "consilience", "cross-domain-correspondence", "commensurability",
        "structural-isomorphism", "unified-theory", "theory-of-everything",
        "interdisciplinarity", "transdisciplinarity", "multidisciplinarity",
        "knowledge-graph", "ontology", "taxonomy", "classification",
        "semantic-web", "concept-map", "analogy", "metaphor",
        "conceptual-blending", "isomorphism", "homomorphism", "functor",
        "category-theory", "universal-property", "measurement-theory",
        "epistemology", "philosophy-of-science", "scientific-realism",
        "structural-realism", "underdetermination", "confirmation-theory",
        "bayesian-epistemology", "information-theoretic-epistemology",
        "radical-constructivism", "observer-dependence",
        "relational-quantum-mechanics", "relational-ontology",
        "process-philosophy", "mereology", "compositionality", "emergence",
        "downward-causation", "supervenience", "grounding",
        "fundamentality", "hierarchy-theory", "nested-structure",
        "part-whole-relations", "scale-invariance", "self-similarity",
        "fractal", "renormalization", "coarse-graining", "effective-theory",
        "universality-class", "phase-transition", "order-parameter",
        "symmetry-breaking", "criticality", "self-organized-criticality",
        "complexity-measure", "algorithmic-complexity",
        "computational-irreducibility", "wolfram-class", "ruliad",
        "multiway-graph", "branchial-space",
    ],
    "PLT": [
        "cloud-native", "serverless", "edge-computing", "microservices",
        "kubernetes", "container-orchestration", "devops", "ci-cd",
        "infrastructure-as-code", "platform-engineering",
        "quantum-computing", "quantum-algorithm", "quantum-circuit",
        "qubit", "quantum-error-correction", "quantum-hardware",
        "quantum-software", "quantum-cloud", "quantum-simulator",
        "quantum-machine-learning", "quantum-annealing", "gate-model",
        "measurement-based", "topological-quantum-computing",
        "photonic-quantum", "trapped-ion", "superconducting-qubit",
        "neutral-atom", "nvidia-cuda", "cuda-quantum", "qiskit", "cirq",
        "pennylane", "quil", "quantum-sdk", "python-sdk", "rest-api",
        "graphql", "websocket", "event-driven", "data-pipeline",
        "vector-database", "semantic-search",
        "retrieval-augmented-generation", "llm", "transformer",
        "embedding-model", "fine-tuning", "prompt-engineering",
        "agentic-ai", "mcp", "model-context-protocol", "observability",
        "telemetry", "tracing", "error-budget", "sla", "multi-tenancy",
        "billing", "metering", "rate-limiting", "authn", "authz",
        "zero-trust", "quantum-safe", "post-quantum-cryptography",
    ],
    "DEM": [
        "interactive-visualization", "data-visualization", "d3-js",
        "webgl", "canvas", "svg", "react", "typescript", "frontend",
        "ui-ux", "design-system", "storybook", "playwright", "cypress",
        "test-automation", "accessibility", "wcag", "responsive-design",
        "progressive-web-app", "single-page-application", "webassembly",
        "shader", "particle-system", "flow-field", "generative-art",
        "procedural-generation",
    ],
}

QNFO_GENERAL_FAMILIES = {
    # structurally general concept families (cross-domain candidates)
    "hierarchy", "nested-structure", "part-whole-relations", "scale-invariance",
    "self-similarity", "fractal", "renormalization", "coarse-graining",
    "effective-theory", "universality-class", "phase-transition",
    "symmetry-breaking", "emergence", "complexity-measure",
    "algorithmic-complexity", "isomorphism", "homomorphism", "functor",
    "category-theory", "universal-property", "compositionality",
    "interdisciplinarity", "transdisciplinarity", "consilience",
    "knowledge-graph", "ontology", "taxonomy", "classification",
    "semantic-web", "concept-map", "analogy", "conceptual-blending",
    "information-theoretic-epistemology", "bayesian-updating",
    "bayesian-epistemology", "probability-calibration", "network-effects",
    "path-dependence", "system-dynamics", "agent-based-model",
    "measurement-theory", "epistemology", "observer-dependence",
    "relational-ontology", "structural-realism", "quantum-computing",
    "quantum-algorithm", "quantum-circuit", "quantum-error-correction",
    "quantum-machine-learning", "llm", "transformer", "embedding-model",
    "retrieval-augmented-generation", "semantic-search", "vector-database",
    "data-pipeline", "observability", "telemetry", "event-driven",
    "rest-api", "python-sdk", "interactive-visualization",
    "data-visualization", "test-automation", "accessibility",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domains", help="JSON file with domains+general_families")
    ap.add_argument("--out", default="artifacts/verification/silo_measurement.json")
    ap.add_argument("--shared-threshold", type=int, default=3)
    args = ap.parse_args()

    if args.domains:
        with open(args.domains, encoding="utf-8") as f:
            data = json.load(f)
        domains = data["domains"]
        gf = set(data.get("general_families", []))
        source = args.domains
    else:
        domains = QNFO_TAXONOMY
        gf = QNFO_GENERAL_FAMILIES
        source = "builtin QNFO taxonomy v1.0"

    result = measure(domains, gf, shared_threshold=args.shared_threshold)
    result["source"] = source
    result["seed"] = "deterministic (no randomness)"

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")

    print(f"SOURCE: {source}")
    print(f"total keywords: {result['total_distinct_keywords']}")
    print(f"partitionality_index: {result['partitionality_index']:.4f}")
    print(f"local keywords: {result['local_keyword_count']}")
    print(f"bridge keywords: {result['bridge_keyword_count']} "
          f"(share {result['bridge_share']:.4f})")
    print(f"shared core (>=3 domains): {result['shared_core_size']}")
    if result.get("shared_core_keywords"):
        print(f"  core keywords: {result['shared_core_keywords']}")
    if result.get("fisher_enrichment"):
        fe = result["fisher_enrichment"]
        print(f"fisher one-sided p (greater): {fe['p_one_sided_greater']:.6f}")
        print(f"odds ratio: {fe['odds_ratio']}")
        print(f"contingency: {fe['table']}")
    print(f"WROTE: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
